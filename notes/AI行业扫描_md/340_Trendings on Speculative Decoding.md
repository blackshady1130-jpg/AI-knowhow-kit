# Trendings on Speculative Decoding 投机解码的趋势

**作者：** Andy Peng
**发布时间：** June 2026
**原文链接：** [https://pengandy.com/blog/2026/speculativedecoding/](https://pengandy.com/blog/2026/speculativedecoding/)

---

Created in June 2026 · 5,595 words · 28 min read 创建于 2026 年 6 月 · 5,595 字 · 28 分钟阅读

2026 · speculative-decoding mtp inference eagle · research

[Hits](https://hits.sh/pengandy.com/blog/2026/speculativedecoding/)

EN 中文

"The fastest token is the one you never have to generate twice."

— the idea at the heart of every speculative-decoding system

Speculative decoding has quietly become the default way to make large language models fast. The premise is simple: a small, cheap _drafter_ guesses several tokens ahead, and the big _target_ model verifies them in a single parallel forward pass — accepting the guesses it agrees with and correcting the first one it doesn't. Because rejected drafts are thrown away, the output stays **bit-for-bit identical** to plain autoregressive decoding. It's a pure efficiency win, not a quality trade.

In my own writing on the LLM space (see my [LLM Year in Review](https://pengandy.com/blog/2025/llm/) ) I've watched this technique go from a clever trick to a production necessity. What's striking about **2026** is how the whole field converged on the same answer in the span of two months — and from three very different angles: Google's open **Gemma 4** drafters, Google's on-device **Gemini Nano** frozen Multi-Token Prediction, and DeepSeek's server-scale **DSpark** . This post walks that timeline, summarizes each, and lays them side by side.

## The 2026 Wave, at a Glance

Three releases, eight weeks, one idea. The rail below is the trend in miniature — from the open-weights drafters that put speculative decoding in everyone's hands, to the edge, to hyperscale serving:

May 5, 2026 — Gemma 4 Assistant (open weights)

Google ships a companion line of autoregressive **drafter** models — officially the **"Gemma 4 Assistant"** (the `-assistant` checkpoints) — plus an **MTP** head for the Gemma 4 family. Up to **3×** faster inference, lossless, Apache-2.0, and supported in Transformers, MLX, vLLM, SGLang and Ollama from day one.

June 26, 2026 — Gemini Nano Frozen MTP (on-device)

Google Research retrofits MTP onto **frozen** Gemini Nano v3 on Pixel 9/10. A "late-exit" head cross-attends to the main model's KV cache (zero-copy), saving **~130 MB** and delivering **50%+** speedups with ~2 extra accepted tokens per pass.

June 27, 2026 — DeepSeek DSpark (server-scale)

DeepSeek layers a "semi-parallel" speculative framework with **confidence-scheduled verification** on top of DeepSeek-V4's built-in MTP-1. Per-user speedups of **57–85%** and throughput gains of **1\.5×–5×** in real production traffic.

Next — Branching & Lenient Verification

Everyone is converging on the same frontier: parallel/branching drafts, auxiliary-head-free designs, and _relaxed_ (non-exact-match) verification to push acceptance even higher. The chapter still being written.

The 2026 speculative-decoding wave — the hollow, dashed node is where the research is heading next.

## Original Sources

DeepSeek DSpark — 10-part X thread (Dmytro Dzhulgakov, co-founder & CTO, Fireworks AI)

[x.com/dzhulgakov/status/2070922887595499930](https://x.com/dzhulgakov/status/2070922887595499930) · [part 4 — "speculation is not free"](https://x.com/dzhulgakov/status/2070922896588087753) · [part 7 — "DSpark ≈ EAGLE + MTP"](https://x.com/dzhulgakov/status/2070922902376198579)

DeepSeek-V4-Flash-DSpark — model card

[huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark)

Gemini Nano frozen MTP — Google Research blog

[research.google/blog/accelerating-gemini-nano-models-on-pixel-with-frozen-multi-token-prediction](https://research.google/blog/accelerating-gemini-nano-models-on-pixel-with-frozen-multi-token-prediction/)

Gemma 4 drafter — X post (Google Gemma)

[x.com/googlegemma/status/2051694045869879749](https://x.com/googlegemma/status/2051694045869879749)

Gemma 4 MTP — official docs & Keyword blog

[ai.google.dev/gemma/docs/mtp/overview](https://ai.google.dev/gemma/docs/mtp/overview) · [blog.google — multi-token-prediction-gemma-4](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

First, the Vocabulary

## Key Terms in Plain English — EAGLE, MTP, DFlash

Three names show up everywhere in these announcements. Here's all three explained side by side — plain English first, then the technical details — using the linked sources:

| |EAGLE |MTP (Multi-Token Prediction) |DFlash (block-diffusion drafter) |
| --- | --- | --- | --- |
|In one line |A _smarter way_ to draft guesses (a tiny extra layer conditioned on target features). |Teach one model to say _several_ words at once (extra prediction heads). |Draft a _whole block_ at once, by diffusion. |
|In plain English |A normal drafter guesses the next word from the words so far. EAGLE instead predicts the big model's internal "thought vector" (its hidden _features_ ) one step ahead and drafts from _that_ , so more guesses get accepted — and more acceptances means more speed. |Normally a model writes one token, feeds it back, writes the next — slow and serial. MTP bolts on lightweight extra "heads" that predict the next 2–4 tokens, piggybacking on the model's own embeddings/activations. The big model verifies them in parallel and keeps only the correct ones, so quality is unchanged. |Instead of guessing one token at a time, DFlash uses a block-diffusion model to "paint" all N draft tokens in a single forward pass, still conditioning on the target's hidden features for quality. Drafting latency becomes nearly free, so the bottleneck shifts to _draft quality_ . |
|Drafting style |**Autoregressive** |**Autoregressive** |**Parallel (non-autoregressive)** |
|Passes for K tokens |K sequential |K sequential |**1** — O(1) |
|Conditioning |Target's last-layer feature + previous token (EAGLE-3: multi-layer fusion) |Shares the target's trunk & embeddings |Target hidden features (target-conditioned), bidirectional within the block |
|How it's trained |Train a 1–2-layer draft head on the target's hidden states (cheap) |MTP heads trained with / onto the backbone to predict the next k tokens |Train a lightweight block-diffusion drafter to denoise a K-token block, conditioned on target features |
|Separate drafter model, or model-free? |**~ A small draft head** — 1–2 extra trained layers riding on the target (not a full standalone model) |**Model-free / integrated** — extra heads built into the target itself; no separate model to load |**Separate drafter** — a lightweight block-diffusion model, trained & shipped per target |
|Strength |High acceptance; coherent on long drafts |Cheap, integrated; rides the model's own compute |Drafting latency ~free; strong at the start of a block; wider blocks ~free on big accelerators |
|Weakness |Serial: latency grows with depth |Serial: K passes for K tokens |Quality can decay deep in the block; needs a diffusion drafter trained per target |
|Where it shows up |The foundation Gemini Nano "builds on." Family: EAGLE-2 (draft trees), EAGLE-3 (training-time test), EAGLE-3.1, P-EAGLE. [arXiv:2401.15077](https://arxiv.org/abs/2401.15077) . |The shared idea across all three releases: Gemma 4 ships MTP heads; Gemini Nano retrofits one onto a frozen model; DeepSeek-V4 bakes one in (see MTP-1 below). [Gemma docs](https://ai.google.dev/gemma/docs/mtp/overview) · [arXiv:2404.19737](https://arxiv.org/abs/2404.19737) . |UCSD Z-Lab, ICML 2026 ( [arXiv:2602.06036](https://arxiv.org/abs/2602.06036) ); the "parallel block" half of DeepSeek's DSpark. _Distinct from the_ DeepSeek-V4- **Flash** _model._ |

So the clean mental model: **EAGLE and MTP are both autoregressive** drafters (they differ in _where_ the drafter lives — an extra feature-conditioned layer vs. extra heads), while **DFlash is the odd one out: it's parallel** , generating the whole block in one shot via diffusion. That single difference — serial vs. one-pass drafting — is the axis the rest of this post turns on.

**Bonus term — MTP-1:** just "MTP with a single extra head," i.e. one predicted-token-ahead. DeepSeek-V4 ships with MTP-1 built in (2 tokens per forward pass); DSpark then stacks its semi-parallel, confidence-scheduled verification on top of that baseline.

**General DFlash — what it is, how it's trained, how it's used.**  
  
**What it is:** DFlash ( _"Block Diffusion for Flash Speculative Decoding"_ , UCSD Z-Lab — Jian Chen, Yesheng Liang, Zhijian Liu; ICML 2026) replaces the autoregressive drafter with a **lightweight block-diffusion model** . Instead of guessing one token at a time, it "paints" a whole block of K candidate tokens in a single forward pass — turning O(K) serial drafting into O(1).  
  
**How it's trained:** a small block-diffusion drafter is trained to denoise/produce a block of future tokens, _conditioned on context features (hidden states) extracted from the target model_ — the same EAGLE-style trick that keeps drafts accurate. Drafters are trained per target model on instruction data and published as checkpoints (e.g. `z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat` , `z-lab/Qwen3-4B-DFlash-b16` ), with a fixed block size K (e.g. 10–16).  
  
**How it's used:** drop it in as the _proposer_ in a speculative-decoding pipeline; the target verifies the whole block in parallel and keeps the correct prefix (lossless). It's integrated into vLLM (GPU/PyTorch) and vLLM-TPU/JAX (PRs #1868–1870), keeping a context buffer of target hidden states across steps. On TPU v5p a "K-flat" effect makes verifying 16 vs. 1024 tokens cost nearly the same, so wider blocks are ~free and the real lever becomes _draft quality_ . Reported: **3\.13×** avg (≈6× peak on math) on TPU v5p; **2\.29×** vs. EAGLE-3's 1.30× head-to-head.  
  
**In DSpark:** DeepSeek's DSpark blends DFlash's _parallel block_ (strong at the start of a block) with an _autoregressive_ EAGLE-3/MTP step (coherent deep into long drafts) — beating either alone. So DFlash is a general, model-agnostic drafting method; DSpark is one production system that uses it as one of its two halves.

The Core Trade-off

## Autoregressive Decoding vs. Parallel Drafting — the axis every method lives on

Underneath all three releases is a single tension. A drafter can produce its guesses **autoregressively** (one token at a time, each guess conditioned on the last) or by **parallel drafting** (predicting a whole block of tokens in one shot). They fail in opposite ways — and the 2026 systems are essentially different bets on how to combine them.

| |Autoregressive drafting |Parallel drafting |
| --- | --- | --- |
|How it drafts |Generates draft tokens _serially_ — each draft token is fed back in to produce the next. |Predicts several draft tokens _at once_ in a single forward pass (a "parallel block"). |
|Cost of K draft tokens |**K sequential** drafter passes — latency grows linearly with speculation depth (a "hidden architectural ceiling"). |**One** pass for the whole block — depth is nearly free. |
|Strength |Later tokens see earlier guesses, so long drafts stay _coherent_ ("EAGLE-3 is more coherent on long drafting"). |Very strong on the _first_ positions, where no context between drafts is needed ("DFlash is stronger at initial positions"). |
|Weakness |Slow drafter or too-deep drafting with a low accept rate can _hurt_ net speed. |Later draft tokens can't see earlier ones, so quality degrades as the block lengthens. |
|Representative |The **EAGLE** family (EAGLE-1/2/3/3.1). |**MTP** heads; **P-EAGLE** (parallel-drafting EAGLE). |

This is exactly the gap **P-EAGLE** ("Parallel-Drafting EAGLE") was built to close: it transforms EAGLE from autoregressive into _parallel multi-token prediction_ via a learnable shared hidden state, removing the serial-pass bottleneck while keeping EAGLE's feature-grounded accuracy ( [arXiv:2602.01469](https://arxiv.org/abs/2602.01469) ; see also the [vLLM](https://vllm.ai/blog/p-eagle) and [Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/parallelize-speculative-decoding-with-p-eagle-on-amazon-sagemaker-ai/) write-ups).

And it's why DSpark's author, **Dmytro Dzhulgakov** — co-founder & CTO of **Fireworks AI** (and a longtime PyTorch core maintainer) — frames DSpark as the _fusion_ of both styles:

> "DSpark ≈ EAGLE + MTP. DFlash is stronger at initial positions; EAGLE-3 is more coherent on long drafting but has lower-quality guesses in the beginning. DSpark combines both parallel-block and autoregressive ideas, beating either approach." — @dzhulgakov

**Speculation is not free.** The same thread spells out the governing equation:  
  
`time_per_token = (num_tokens_drafted × drafter_time + verify_time(num_tokens_drafted)) / num_tokens_accepted`  
  
A drafter that's too slow, or that drafts too many tokens with a low acceptance rate, can actually _hurt_ throughput. Every system above is really just tuning the numerator and denominator of this fraction. — @dzhulgakov (Fireworks AI)

Summary 1  ·  June 27, 2026

## DeepSeek DSpark — speculative decoding at hyperscale

**DSpark** is not a new model — it's an inference-time optimization layered on top of existing **DeepSeek-V4** checkpoints. As Dmytro Dzhulgakov put it in his thread, it "ingeniously integrates many speculative decoding ideas to achieve 1.5× to 5× higher throughput in a real production system." The key word is _integrates_ : DSpark is less a single trick than a careful assembly of the field's best ideas, tuned for serving traffic.

V4 already ships with one built-in **MTP-1** head, so the base model emits _two_ tokens per forward pass before DSpark even enters the picture. DSpark builds on that with what DeepSeek calls a **"semi-parallel"** method: it speculatively generates multiple candidate tokens, then applies **adaptive / confidence-scheduled verification** — only spending verifier compute on the promising guesses instead of rigidly checking one token at a time. The reported effect is the elimination of "computational waste from invalid checks."

* **Per-user speed:** ~60–85% faster on DeepSeek-V4 _Flash_ ; ~57–78% on the _Pro_ variant (secondary reporting).
* **Throughput:** 1\.5×–5× higher depending on concurrency (the thread's headline; reporting cites 51%–400%).
* **No retraining of the base model** — it reuses deployed V4 weights, so the gain is essentially free engineering on top of MTP-1.
* Released as a full paper (33 authors from **Peking University & DeepSeek-AI** , led by Xin Cheng et al., with **Wenfeng Liang** as senior author) plus the open [DeepSpec](https://github.com/deepseek-ai/DeepSpec) training repo and public checkpoints ( `deepseek-ai/dspark_qwen3_4b_block7` , etc.).

> "DSpark ... ingeniously integrates many speculative decoding ideas to achieve 1.5x to 5x higher throughput in a real production system." — @dzhulgakov

The enthusiasm wasn't confined to DeepSeek's research org. **Tianyi Cui** (崔添翼) — the former Jane Street quant who joined DeepSeek in March 2026 to lead its **Harness** team building DeepSeek's agent stack — [spotlighted the open-source DeepSpec repo and DSpark on Weibo](https://weibo.com/7542534202/5314445553436842) . It's a small but telling signal of how broadly the company is leaning on speculative decoding — not just to serve V4 cheaply, but as table-stakes infrastructure for the latency-sensitive agent products the Harness team is racing to ship.

Deep Dive

## Dmytro's Thread, Idea by Idea — the 10-step walkthrough

Dmytro Dzhulgakov (Fireworks AI) explained DSpark as a **"10 ideas"** thread that builds up from the very basics of LLM decoding to the full DSpark design. Here is that thread walked through step by step, each with its original diagram. Every card links back to the source tweet.

🧵

**Dmytro Dzhulgakov** · @dzhulgakov · Jun 27, 2026

DSpark from @deepseek\_ai ingeniously integrates many speculative decoding ideas to achieve 1.5x to 5x higher throughput in a real production system. Let's understand it with 10 ideas, starting from the very basics 🧵

DSpark thread header diagram 1 DSpark thread header diagram 2

[View on X →](https://x.com/dzhulgakov/status/2070922887595499930)

1

@dzhulgakov · Jun 27, 2026

Batching in LLM decoding

Generating tokens is bound on reading weights from memory. So decoding 10 tokens in parallel is only slightly slower than generating 1. Continuous batching leverages this insight.

[View on X →](https://x.com/dzhulgakov/status/2070922889868779707)

2

@dzhulgakov · Jun 27, 2026

Speculative decoding

For the same request, token N+1 depends on token N, so we can't decode them in parallel. But if we can guess what the tokens are ("speculate"), we can quickly verify which prefix of them is correct from the main model perspective.

Speculative decoding diagram

[View on X →](https://x.com/dzhulgakov/status/2070922892142104962)

3

@dzhulgakov · Jun 27, 2026

Draft model

How to speculate? With a model, of course. The simplest is to run a smaller model trained on the same distribution, e.g. Qwen 0.8B for Qwen 397B.

Draft model diagram

[View on X →](https://x.com/dzhulgakov/status/2070922894293749774)

4

@dzhulgakov · Jun 27, 2026

Speculation is not free

`time_per_token = (num_tokens_drafted * drafter_time + verify_time(num_tokens_drafted)) / num_tokens_accepted` Slow to run speculator or drafting too many tokens with a low guess rate can be hurtful. The right balance is needed.

Speculation cost equation diagram

[View on X →](https://x.com/dzhulgakov/status/2070922896588087753)

5

@dzhulgakov · Jun 27, 2026

EAGLE and MTP

Make drafter an extra transformer layer of the main model, i.e. it consumes rich latent representation (last activation) in addition to the previous token. Allows to get away with 1-2 layers instead of the full model. Much faster and more accurate speculator.

EAGLE and MTP diagram

[View on X →](https://x.com/dzhulgakov/status/2070922898425176293)

6

@dzhulgakov · Jun 27, 2026

DFlash

MTP needs to take N steps to generate N draft tokens. DFlash uses diffusion ideas to produce all N tokens in one forward pass. Much faster speculation, but draft quality sometimes better, sometimes worse than MTP/Eagle.

DFlash diffusion drafting diagram

[View on X →](https://x.com/dzhulgakov/status/2070922900400640398)

7

@dzhulgakov · Jun 27, 2026

DSpark ≈ EAGLE + MTP

DFlash is stronger at initial positions. Eagle3 is more coherent on long drafting but has lower quality guess in the beginning. DSpark combines both parallel block and autoregressive ideas, beating either approach.

DSpark = EAGLE + MTP diagram DSpark performance chart

[View on X →](https://x.com/dzhulgakov/status/2070922902376198579)

8

@dzhulgakov · Jun 27, 2026

Cheaper sequential block

Eagle3/MTP run full attention at each drafting position. Since DFlash has parallel block to capture previous context, sequential step can be much cheaper with RNN or even Markov model. All leads to an even faster but still accurate drafter!

Cheaper sequential block diagram 1 Cheaper sequential block diagram 2

[View on X →](https://x.com/dzhulgakov/status/2070922904217543082)

9

@dzhulgakov · Jun 27, 2026

Variable length drafting and hardware-aware scheduler

What num\_draft\_tokens should be? It varies:
\* some requests (e.g. coding) are easier to predict than others
\* optimal length depends on server load (batch size). Speculate more with low load when GPU compute is free.

Variable length drafting diagram 1 Hardware-aware scheduler diagram 2

[View on X →](https://x.com/dzhulgakov/status/2070922906339770683)

10

@dzhulgakov · Jun 27, 2026

Online drafter calibration

Models tend to be overconfident in predicting the next token making it hard to get threshold for stopping drafting. But we can look at the runtime drafter performance and adjust ("calibrate") thresholds on the fly.

Online drafter calibration diagram

[View on X →](https://x.com/dzhulgakov/status/2070922908550209571)

@dzhulgakov · Jun 27, 2026

Putting it together

The magic of DeepSeek is in excellent system engineering with close model co-design. Many of these ideas were published before. It's very impressive how they integrate them together to deliver huge e2e improvements with auto-adapting system.

Putting it together summary diagram

[View on X →](https://x.com/dzhulgakov/status/2070922910148251685)

Summary 2  ·  June 26, 2026

## Gemini Nano Frozen MTP — speculative decoding at the edge

Google Research tackled the opposite extreme from DeepSeek: not a datacenter, but a phone. Mobile inference lives under hard RAM and energy budgets, and a standard speculative-decoding setup wants a _separate_ drafter model (e.g. 128M params) that competes for memory and is "blind" to the main model's internal state. Their answer is to retrofit **Multi-Token Prediction onto a frozen Gemini Nano v3** — already deployed on Pixel 9 and 10.

The design rests on three moves:

* **Late-exit MTP head.** Instead of a standalone drafter, a lightweight Transformer head is appended to the final layers of the main model and predicts future tokens from the backbone's high-dimensional hidden states.
* **Frozen backbone.** The base model's weights are frozen; only the head is trained. This guarantees **zero degradation** in capability or safety alignment, and lets efficiency updates roll out with full backward compatibility — output stays bit-for-bit identical.
* **Zero-copy architecture.** The head _cross-attends directly to the main model's frozen KV cache_ instead of maintaining its own. This eliminates drafter prefill latency and saves **~130 MB** per instance versus a standalone drafter.

In production workloads like AI Notification Summaries and Proofread, MTP correctly predicts **nearly two additional tokens per pass** , yielding **50%+ speedups** on Pixel 9 and up to **55% better token acceptance** on highly structured tasks (e.g. smart replies) — while cutting energy use by waking heavy processors less often. The work explicitly builds on the **EAGLE** framework and **CALM** (Confident Adaptive Language Modeling), and points ahead to branching/parallel decoding and "verification leniency."

Summary 3  ·  May 5, 2026

## Gemma 4 Assistant — speculative decoding for everyone

Gemma 4 is where this trend went **open** . Alongside the main lineup, Google released a companion line of autoregressive **drafter** models plus an **MTP** head — officially branded the **"Gemma 4 Assistant"** and published as the `-assistant` checkpoints (e.g. `google/gemma-4-E4B-it-assistant` ; the Transformers model type is `gemma4_assistant` , loaded as the `assistant_model` ). Under the same Apache-2.0 license, it delivers up to **3×** faster inference "with zero degradation in output quality or reasoning accuracy." Crucially, it shipped with day-one support across **Transformers, MLX, vLLM, SGLang, and Ollama** , so the speedup was usable immediately rather than a research artifact.

Per the official docs, Gemma 4's MTP is more than a bolt-on drafter. Three enhancements make the draft tokens cheaper and more accurate:

* **Shared input embeddings.** The draft model reuses the target's embedding table rather than carrying its own.
* **Target activations.** The drafter takes the target's _last-layer activations_ , concatenates them with token embeddings, and down-projects to the drafter's dimension — so it isn't blind to the backbone's state.
* **Efficient embedder.** To avoid scoring the whole vocabulary, tokens are grouped into clusters; the head first picks likely clusters, then restricts final calculations to those (E2B/E4B variants).

One honest caveat from the docs: for the **MoE** model (Gemma 4 26B A4B), verifying drafted tokens can require loading additional expert weights, which can offset the gains at **batch size 1** on hardware without good parallelism. Higher batch sizes recover the win as expert activations overlap. This Gemma 4 release is the direct ancestor of the Gemini Nano work — the blog explicitly notes the frozen-MTP effort builds on "accelerating Gemma 4 with MTP."

Side by Side

## Comparison — three angles on one idea

|Dimension |Gemma 4 Assistant |Gemini Nano Frozen MTP |DeepSeek DSpark |
| --- | --- | --- | --- |
|Announced |May 5, 2026 |June 26, 2026 |June 27, 2026 |
|Target setting |Open-weights, general / on-device |On-device (Pixel 9 & 10) |Server-scale production serving |
|Base model |Gemma 4 family (incl. 26B A4B MoE) |Gemini Nano v3 |DeepSeek-V4 (Flash & Pro) |
|Open source? |**✔ Yes** — Apache-2.0 weights (HF, Kaggle) |**✗ No** — proprietary; ships inside Pixel updates |**✔ Yes** — MIT: paper + code + checkpoints via the DeepSpec repo |
|Drafter design |Autoregressive drafter + MTP head; shared embeddings, target activations, clustered embedder |"Late-exit" MTP head on frozen backbone; cross-attends to main KV cache (zero-copy) |Built on V4's MTP-1 head + "semi-parallel" candidate generation |
|EAGLE-based? |**~ Partial** — EAGLE- _style_ feature conditioning (consumes the target's last-layer activations), but an MTP "assistant" head rather than the EAGLE algorithm itself |**✔ Yes** — explicitly builds on the **EAGLE** framework (plus CALM late-exit) |**✔ Yes** — an **EAGLE-3 + MTP** hybrid ("DSpark ≈ EAGLE + MTP") |
|Parallel drafting? |**✗ No** — the assistant drafts _autoregressively_ (one token at a time) |**✗ No** — autoregressive MTP head (parallel/branching decoding is stated future work) |**✔ Yes** — _hybrid_ : DFlash parallel block (all N tokens in one pass) + an autoregressive EAGLE-style step |
|Uses DFlash (block-diffusion drafter)? |**✗ No** — autoregressive MTP "assistant" head, no diffusion |**✗ No** — autoregressive late-exit MTP head, no diffusion |**✔ Yes** — the DFlash block-diffusion drafter _is_ the parallel half of DSpark (paired with an autoregressive EAGLE-3/MTP step) |
|Integrated, or separate drafter model? |**~ Separate companion** — a small "assistant" checkpoint loaded alongside, but it shares the target's embeddings & activations |**✔ Integrated** — a late-exit head on the frozen backbone; no standalone model, near-zero extra footprint (zero-copy) |**✔ Integrated** — MTP-1 head + DFlash block ride the deployed V4 weights; no separate standalone LM |
|Shares target KV cache? |**~ Partial** — shares input embeddings & consumes target activations, but not full KV-cache cross-attention |**✔ Yes** — **zero-copy** cross-attention directly to the frozen KV cache (no own cache; ~130 MB saved) |**✔ Yes** — integrated MTP head rides the model's own trunk/KV (no separate drafter cache) |
|Verification |Standard parallel verify (lossless) |Standard parallel verify; bit-for-bit identical |Adaptive / **confidence-scheduled** verification |
|Backbone training |MTP heads pre-trained in tandem with backbone |**Frozen** backbone; only head trained (retrofit) |No base retraining; optimization over deployed weights |
|Headline speedup |Up to **3×** inference |**50%+** on Pixel 9; ~2 extra tokens/pass |**1\.5×–5×** throughput; 57–85% per-user |
|Quality impact |Lossless |Lossless (frozen backbone) |Lossless (drafts discarded on reject) |
|Headline win |Ecosystem reach + day-1 framework support |~130 MB memory saved; lower energy / battery |Real-traffic throughput; no waste on bad checks |
|License / access |Open, Apache 2.0 (HF, Kaggle) |Proprietary, shipped in Pixel updates |Open checkpoint on Hugging Face + paper |

The throughline: all three keep output **lossless** , all three move _away_ from standalone drafters toward heads that reuse the backbone's own state (embeddings, activations, or KV cache), and all three are converging on the same next frontier — branching drafts and relaxed verification. The difference is purely environmental: Gemma 4 optimizes for _reach_ , Gemini Nano for _memory and energy_ , and DSpark for _throughput under load_ .

References

## Papers — the lineage behind the wave

The 2026 releases stand on a well-defined chain of research. The foundational and directly-cited papers, grouped by theme:

1 · Foundations

Fast Inference from Transformers via Speculative Decoding FOUNDATION

Yaniv Leviathan, Matan Kalman, Yossi Matias — _Google Research_

The paper that named speculative decoding: decode K tokens with a cheap drafter, verify in parallel with the target, and accept the correct prefix — faster, with no change to the output distribution.

[arXiv:2211.17192](https://arxiv.org/abs/2211.17192) · [PDF](https://arxiv.org/pdf/2211.17192)

Accelerating Large Language Model Decoding with Speculative Sampling FOUNDATION

Charlie Chen, Sebastian Borgeaud, Geoffrey Irving, Jean-Baptiste Lespiau, Laurent Sifre, John Jumper — _Google DeepMind_

The contemporaneous speculative-sampling formulation, with the rejection-sampling correctness proof that guarantees the accelerated output matches the target model's distribution.

[arXiv:2302.01318](https://arxiv.org/abs/2302.01318) · [PDF](https://arxiv.org/pdf/2302.01318)

Better & Faster Large Language Models via Multi-token Prediction MTP

Fabian Gloeckle, Badr Youbi Idrissi, Baptiste Rozière, David Lopez-Paz, Gabriel Synnaeve — _Meta AI / FAIR_

The MTP training objective — predict several future tokens at once with extra heads. Cited by both Google docs as the "standard MTP implementation" the 2026 drafters build on.

[arXiv:2404.19737](https://arxiv.org/abs/2404.19737) · [PDF](https://arxiv.org/pdf/2404.19737)

Confident Adaptive Language Modeling (CALM) EARLY-EXIT

Tal Schuster, Adam Fisch, Jai Gupta, Mostafa Dehghani, Dara Bahri, Vinh Q. Tran, Yi Tay, Donald Metzler — _Google Research_

The "late-exit"/early-exit lineage the Gemini Nano work draws on: dynamically allocate less compute to easy tokens. Foundation for the late-exit MTP head on a frozen backbone.

[arXiv:2207.07061](https://arxiv.org/abs/2207.07061) · [PDF](https://arxiv.org/pdf/2207.07061) · [CALM blog](https://research.google/blog/accelerating-text-generation-with-confident-adaptive-language-modeling-calm/)

2 · EAGLE family

EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty DRAFTER

Yuhui Li, Fangyun Wei, Chao Zhang, Hongyang Zhang — _Peking University & Microsoft Research_

Drafts at the _feature_ level: the drafter is an extra layer that consumes the target's last activation plus the previous token, making guesses that the target is far more likely to accept.

[arXiv:2401.15077](https://arxiv.org/abs/2401.15077) · [PDF](https://arxiv.org/pdf/2401.15077)

EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees DRAFTER

Yuhui Li, Fangyun Wei, Chao Zhang, Hongyang Zhang — _Peking University & Microsoft Research_

Adds context-aware dynamic draft trees, expanding the most promising draft branches. 3.05–4.26× speedups, 20–40% over EAGLE-1, still lossless.

3\.05–4.26× speedup

[arXiv:2406.16858](https://arxiv.org/abs/2406.16858) · [PDF](https://arxiv.org/pdf/2406.16858)

EAGLE-3: Scaling up Inference Acceleration via Training-Time Test DRAFTER

Yuhui Li, Fangyun Wei, Chao Zhang, Hongyang Zhang — _Peking University & Microsoft Research_

Abandons feature prediction for direct token prediction and fuses multi-layer features via a "training-time test", so the drafter keeps improving with more training data. Up to 6.5× speedup (~1.4× over EAGLE-2); the variant DSpark's author compares against for long drafting.

up to 6.5× speedup

[arXiv:2503.01840](https://arxiv.org/abs/2503.01840) · [PDF](https://arxiv.org/pdf/2503.01840)

EAGLE-3.1: Stabilizing Deeper Speculation RELEASE

EAGLE Team (Yuhui Li, Fangyun Wei, Chao Zhang, Hongyang Zhang) × _vLLM Team_ × _TorchSpec Team_ , with NVIDIA GPU support — team-bylined engineering release (no standalone arXiv preprint; vLLM/TorchSpec contributors credited collectively)

An incremental refinement of EAGLE-3: adds FC normalization after each target hidden state and feeds the post-norm hidden states into the next decoding step. This fixes two instabilities at deeper speculation depths — the fused input getting dominated by higher-layer hidden states, and hidden-state magnitude growing along the unnormalized residual path — making the drafter stable for longer drafts.

[vLLM blog (2026-05-26)](https://vllm.ai/blog/2026-05-26-eagle-3-1)

P-EAGLE: Parallel-Drafting EAGLE with Scalable Training PARALLEL

_Amazon (AWS AI)_

Transforms EAGLE from autoregressive into parallel multi-token prediction via a learnable shared hidden state, removing the serial K-passes bottleneck while keeping feature-grounded accuracy. Checkpoints under `amazon/…-p-eagle` .

[arXiv:2602.01469](https://arxiv.org/abs/2602.01469) · [PDF](https://arxiv.org/pdf/2602.01469) · [vLLM blog](https://vllm.ai/blog/p-eagle) · [SageMaker blog](https://aws.amazon.com/blogs/machine-learning/parallelize-speculative-decoding-with-p-eagle-on-amazon-sagemaker-ai/)

3 · Parallel & diffusion drafting

DFlash: Block Diffusion for Flash Speculative Decoding DIFFUSION ICML 2026

Jian Chen, Yesheng Liang, Zhijian Liu — _Z Lab, UCSD_ (Hao Zhang's group)

Replaces the autoregressive drafter with a lightweight **block-diffusion** model that produces a whole K-token block in a **single** forward pass (O(K)→O(1) drafting), conditioned on the target's hidden features for accuracy. Drafting latency becomes nearly free, shifting the bottleneck to draft quality. It is the "parallel block" half of DeepSeek's DSpark; deployed in vLLM & vLLM-TPU.

>6× lossless; up to 2.5× over EAGLE-3

[arXiv:2602.06036](https://arxiv.org/abs/2602.06036) · [PDF](https://arxiv.org/pdf/2602.06036) · [Z-Lab](https://z-lab.ai/) · [Google TPU blog](https://developers.googleblog.com/supercharging-llm-inference-on-google-tpus-achieving-3x-speedups-with-diffusion-style-speculative-decoding/)

4 · DeepSeek & DSpark

DeepSeek-V3 Technical Report MODEL

DeepSeek-AI — _DeepSeek_

The source of DeepSeek's built-in MTP design (shared embedding/output head for MTP) that the V4 line inherits and DSpark accelerates.

[arXiv:2412.19437](https://arxiv.org/abs/2412.19437) · [PDF](https://arxiv.org/pdf/2412.19437)

DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation SERVING

Xin Cheng\*, Xingkai Yu\*, Chenze Shao\*, Jiashi Li\*, Yunfan Xiong\*, Yi Qian, Jiaqi Zhu, Shirong Ma, Xiaokang Zhang, Jiasheng Ye, Qinyu Chen, Chengqi Deng, Jiping Yu, Damai Dai, Zhengyan Zhang, Yixuan Wei, Yixuan Tan, Wenkai Yang, Runxin Xu, Yu Wu, Zhean Xu, Xuanyu Wang, Muyang Chen, Rui Tian, Xiao Bi, Zhewen Hao, Shaoyuan Chen, Huanqi Cao, Wentao Zhang, Anyi Xu, Huishuai Zhang, Dongyan Zhao, Wenfeng Liang — _Peking University & DeepSeek-AI_ (\* equal contribution; Wenfeng Liang is the senior/last author)

The framework itself. A **semi-autoregressive** drafter — a parallel backbone coupled with a lightweight sequential module — adds intra-block dependency to fix the acceptance decay that pure parallel drafters suffer, while **confidence-scheduled, load-aware verification** tailors the verification length per request from estimated prefix-survival probabilities and engine throughput. In the DeepSeek-V4 serving system under live traffic it beats the MTP-1 production baseline by 60–85% per-user at matched throughput. Open-sourced with the **DeepSpec** training repo (which also ships DeepSeek's own DFlash & EAGLE-3 drafters).

60–85% per-user vs MTP-1

[paper (PDF)](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf) · [DeepSpec repo](https://github.com/deepseek-ai/DeepSpec) · [HF: V4-Flash-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark) · [10-idea thread](https://x.com/dzhulgakov/status/2070922887595499930)

5 · MTP for speculative decoding

FastMTP: Accelerating LLM Inference with Enhanced Multi-Token Prediction MTP

Jinwen Luo et al. — _Tencent_

Aligns MTP training with its inference pattern to improve multi-step draft quality. ~2.03× speedup with lossless output, outperforming vanilla MTP by 82%. Weights at `TencentBAC/FastMTP` .

~2.03× speedup

[arXiv:2509.18362](https://arxiv.org/abs/2509.18362) · [PDF](https://arxiv.org/pdf/2509.18362)

6 · Retrospective

Looking back at speculative decoding BLOG

_Google Research_

Google Research's own retrospective on the technique, linked directly from the Gemini Nano frozen-MTP post.

[research.google/blog/looking-back-at-speculative-decoding](https://research.google/blog/looking-back-at-speculative-decoding/)

**Model checkpoints.** The systems above are not just papers — they ship weights you can run: DSpark on DeepSeek-V4-Flash ( [deepseek-ai/DeepSeek-V4-Flash-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark) ), the open Gemma 4 Assistant MTP drafters ( [google/gemma-4-E4B-it-assistant](https://huggingface.co/google/gemma-4-E4B-it-assistant) ), and the EAGLE/EAGLE-3 drafter checkpoints used across vLLM and SGLang. DSpark's thread author and explainer is **Dmytro Dzhulgakov** ( [@dzhulgakov](https://x.com/dzhulgakov) ), co-founder & CTO of **Fireworks AI** and a longtime PyTorch core maintainer.

The Training Stack

## Where the Drafters Come From — the open-source training libraries

Every system above ships a _trained drafter_ — an EAGLE head, an MTP head, a DFlash block. But who trains them, and on what infrastructure? The quieter half of the 2026 story is the rise of dedicated **open-source training libraries** that turn drafting from a research artifact into a repeatable pipeline. They all wrestle with the same core obstacle — funneling the target model's hidden states into the draft model cheaply, at scale — and each attacks it from a different angle. **DeepSpec** , the repo behind DSpark above, is the newest entry in a line that runs back through 2025:

Jul 2025 — SpecForge (SGLang)

The first purpose-built **EAGLE-3** training framework, natively wired to **SGLang** so a draft model is deployable the moment training finishes. Built-in Training-Time Test (TTT), online & offline hidden-state modes, FSDP + tensor parallelism, and MoE support (Llama 4, DeepSeek).

Nov 2025 — Speculators (vLLM) & SageMaker EAGLE

Two production pushes in one month. **Speculators** (vLLM / Red Hat) standardizes drafters into a single Hugging Face format that runs in vLLM out of the box; Amazon **SageMaker AI** ships **EAGLE-2/3 adaptive** speculative decoding that retrains heads on your _own_ traffic for ~2.5× throughput.

Mar 2026 — TorchSpec (TorchSpec & Mooncake teams)

A torch-native framework for **disaggregated** drafter training: it decouples the inference engine that generates hidden states from the training workers that consume them, streaming tensors over RDMA/TCP through the **Mooncake** store — no disk, no co-location. Trains a Kimi K2.5 EAGLE-3 drafter in ~1,500 H200-hours.

Jun 2026 — DeepSpec (DeepSeek)

The repo DeepSeek open-sourced alongside **DSpark** — shipping not just the DSpark recipe but DeepSeek's own **DFlash** and **EAGLE-3** drafter training, closing the loop from the algorithm research above to a runnable production stack.

A year of training-library releases — the tooling that turns speculative decoding from a paper into a pipeline.

The libraries, in detail

SpecForge: Accelerating Speculative Decoding Training for SGLang TRAINING

The SGLang Team — _LMSYS / SGLang_

A purpose-built, EAGLE-3-focused training framework tightly integrated with SGLang, so a freshly trained draft head runs out of the box at inference. Provides built-in Training-Time Test (TTT) support, both _online_ (hidden states on the fly) and _offline_ (precomputed) modes, FSDP + tensor parallelism for large clusters, and native support for MoE targets like Llama 4 and DeepSeek.

2\.18× MT-Bench (Llama 4 Maverick draft)

[LMSYS blog](https://lmsys.org/blog/2025-07-25-spec-forge/) · [GitHub: sgl-project/SpecForge](https://github.com/sgl-project/SpecForge)

Speculators: Standardized, Production-Ready Speculative Decoding TRAINING FORMAT

_vLLM project / Red Hat (Neural Magic)_

A unified library for building, training, and _storing_ drafters in a single standardized Hugging Face format with immediate vLLM compatibility — so a speculator trained anywhere drops straight into a production server. Training landed in v0.3.0; v0.5.0 (May 2026) added **DFlash** support and fully unified online training on vLLM's native hidden-state extraction.

[Red Hat announcement](https://developers.redhat.com/articles/2025/11/19/speculators-standardized-production-ready-speculative-decoding) · [GitHub: vllm-project/speculators](https://github.com/vllm-project/speculators) · [v0.5.0 (DFlash) blog](https://vllm.ai/blog/2026-05-28-speculators-v050)

EAGLE-Based Adaptive Speculative Decoding on Amazon SageMaker AI TRAINING MANAGED

Amazon SageMaker AI team — _AWS_

A managed path in the SageMaker inference-optimization toolkit that trains **EAGLE-2/3** heads — and, crucially, _re_ trains them on your own captured traffic, so the drafter adapts to your real workload rather than a generic benchmark. Supports six architectures (Llama, Qwen2/3, Qwen3-MoE, GPT-OSS with EAGLE-3; Qwen3-Next with EAGLE-2) and ships pre-trained heads for instant use. (Disclosure: a project I had a hand in shipping on the SageMaker team.)

~2.5× throughput, lossless

[AWS Machine Learning blog](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-introduces-eagle-based-adaptive-speculative-decoding-to-accelerate-generative-ai-inference/)

TorchSpec: Speculative Decoding Training at Scale TRAINING

TorchSpec team & Mooncake team — _PyTorch ecosystem_

A torch-native framework for **disaggregated** drafter training that solves the hidden-state bottleneck head-on: it splits the inference GPUs that _generate_ target hidden states from the training GPUs that _consume_ them, streaming tensors directly over RDMA/TCP via the **Mooncake** store — eliminating both the multi-TB disk cost of offline pipelines and the memory pressure of co-located training. Scales inference and training independently; supports vLLM & SGLang targets.

Kimi K2.5 EAGLE-3 drafter in ~1,500 H200-hrs; +60% throughput @ BS1

[PyTorch blog](https://pytorch.org/blog/torchspec-speculative-decoding-training-at-scale/) · [GitHub: torchspec-project/TorchSpec](https://github.com/torchspec-project/TorchSpec) · [Mooncake](https://github.com/kvcache-ai/Mooncake)

DeepSpec TRAINING

DeepSeek-AI — _DeepSeek_

The training repository DeepSeek open-sourced together with the **DSpark** paper. Beyond the DSpark recipe itself, it ships training for DeepSeek's own **DFlash** block-diffusion and **EAGLE-3** drafters — the production-side counterpart to the algorithm research earlier in this post, and the library that anchors the 2026 end of this timeline.

[GitHub: deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) · [DSpark paper (PDF)](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf)

Two months, two labs, three releases, one converging idea — and beneath them, five open-source training stacks (from SGLang, vLLM/Red Hat, AWS, PyTorch×Mooncake, and DeepSeek) turning those drafters into a reproducible pipeline. If 2024–2025 was about _training_ bigger and cheaper models, 2026 is shaping up to be the year speculative decoding became the standard way to _serve_ them — on a phone, in a datacenter, and everywhere in between.

"最快的 token，是你永远不必生成第二次的那个。"

— 每一套投机解码（speculative decoding）系统的核心思想

投机解码已经悄然成为让大语言模型变快的默认方式。原理很简单：一个小而便宜的 _草稿模型（drafter）_ 一次性向前猜测若干个 token，大的 _目标模型（target）_ 在一次并行前向中验证它们 —— 同意的就采纳，遇到第一个不同意的就纠正。由于被拒绝的草稿会被丢弃，输出与普通自回归解码 **逐比特完全一致** 。这是纯粹的效率收益，而非质量的取舍。

在我自己关于 LLM 领域的写作中（见我的 [LLM 年度回顾](https://pengandy.com/blog/2025/llm/) ），我看着这项技术从一个巧妙的小技巧变成了生产环境的刚需。 **2026 年** 引人注目之处，在于整个领域在短短两个月内、从三个截然不同的角度收敛到了同一个答案：谷歌开源的 **Gemma 4 Assistant** 、谷歌端侧的 **Gemini Nano** 冻结式 Multi-Token Prediction，以及 DeepSeek 服务器规模的 **DSpark** 。本文沿着时间线梳理，逐一总结，并把它们并排对比。

**关于来源的说明。** 本文在下方链接了每一条原始公告。两条 X/Twitter 长帖（Dmytro Dzhulgakov 的 DSpark 长帖、以及 Gemma 4 drafter 帖子）的完整 _回复串_ 受 X 登录墙限制无法被程序抓取 —— 这里的总结基于顶层帖子，外加它们所指向的公开博客、文档、模型卡与论文。凡是数据来自二手报道而非一手文档之处，我都会注明。

## 2026 浪潮一览

三次发布，八周时间，一个思想。下面的时间轴是这股趋势的缩影 —— 从把投机解码送到所有人手中的开源草稿模型，到端侧，再到超大规模服务：

2026 年 5 月 5 日 —— Gemma 4 Assistant（开源权重）

谷歌发布了一系列自回归 **草稿** 模型 —— 官方称为 **"Gemma 4 Assistant"** （即 `-assistant` 检查点）—— 外加为 Gemma 4 家族准备的 **MTP** 头。推理最高提速 **3×** 、无损、Apache-2.0，并自首日起支持 Transformers、MLX、vLLM、SGLang 与 Ollama。

2026 年 6 月 26 日 —— Gemini Nano 冻结式 MTP（端侧）

谷歌研究院把 MTP 改造性地装到 **冻结** 的 Gemini Nano v3 上（Pixel 9/10）。一个"晚退出（late-exit）"头通过交叉注意力直接读取主模型的 KV cache（零拷贝），节省约 **130 MB** ，并带来 **50%+** 的提速，每次前向平均多接受约 2 个 token。

2026 年 6 月 27 日 —— DeepSeek DSpark（服务器规模）

DeepSeek 在 DeepSeek-V4 自带的 MTP-1 之上，叠加了一套"半并行（semi-parallel）"投机框架与 **置信度调度的验证** 。在真实生产流量中，单用户提速 **57–85%** ，吞吐提升 **1\.5×–5×** 。

下一步 —— 分支式草稿与宽松验证

所有人都在朝同一个前沿收敛：并行/分支式草稿、无需辅助头的设计，以及 _放宽_ （非精确匹配）的验证以进一步提高接受率。这一章仍在书写中。

2026 年投机解码浪潮 —— 空心虚线节点是研究正在走向的下一步。

## 原始来源

DeepSeek DSpark —— 10 条 X 长帖（Dmytro Dzhulgakov，Fireworks AI 联合创始人兼 CTO）

[x.com/dzhulgakov/status/2070922887595499930](https://x.com/dzhulgakov/status/2070922887595499930) · [第 4 条 —— "投机并非免费"](https://x.com/dzhulgakov/status/2070922896588087753) · [第 7 条 —— "DSpark ≈ EAGLE + MTP"](https://x.com/dzhulgakov/status/2070922902376198579)

DeepSeek-V4-Flash-DSpark —— 模型卡

[huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark)

Gemini Nano 冻结式 MTP —— 谷歌研究院博客

[research.google/blog/accelerating-gemini-nano-models-on-pixel-with-frozen-multi-token-prediction](https://research.google/blog/accelerating-gemini-nano-models-on-pixel-with-frozen-multi-token-prediction/)

Gemma 4 drafter —— X 帖子（Google Gemma）

[x.com/googlegemma/status/2051694045869879749](https://x.com/googlegemma/status/2051694045869879749)

Gemma 4 MTP —— 官方文档与 Keyword 博客

[ai.google.dev/gemma/docs/mtp/overview](https://ai.google.dev/gemma/docs/mtp/overview) · [blog.google — multi-token-prediction-gemma-4](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

先把术语讲清楚

## 用大白话讲关键术语 — EAGLE、MTP、DFlash

这几个名字在这些公告里到处出现。下面用所链接来源的内容，简单解释每一个：

| |EAGLE |MTP （Multi-Token Prediction） |DFlash （块扩散草稿器） |
| --- | --- | --- | --- |
|一句话 |一种 _更聪明_ 的起草方式（一个以目标特征为条件的微型额外层）。 |让一个模型一次说出 _好几个_ 词（额外预测头）。 |用扩散一次性起草 _一整块_ token。 |
|大白话 |普通草稿模型只根据已有的词来猜下一个词。EAGLE 则提前一步预测大模型内部的"思维向量"（隐藏 _特征_ ），并基于此来起草，于是更多猜测被接受 —— 接受越多，速度越快。 |通常模型写一个 token、回填、再写下一个 —— 串行而慢。MTP 加装轻量的额外"头"，预测接下来的 2–4 个 token，搭便车复用模型自身的嵌入/激活。大模型并行验证、只保留正确的，因此质量不变。 |DFlash 不再一次猜一个 token，而是用块扩散模型在一次前向中"绘制"出全部 N 个草稿 token，同时仍以目标隐藏特征为条件保证质量。起草延迟几乎降为零，瓶颈转移到 _草稿质量_ 。 |
|起草方式 |**自回归** |**自回归** |**并行（非自回归）** |
|K 个 token 的前向次数 |K 次串行 |K 次串行 |**1** 次 —— O(1) |
|条件来源 |目标最后一层特征 + 上一个 token（EAGLE-3：多层融合） |共享目标的主干与嵌入 |目标隐藏特征（目标条件），块内双向 |
|如何训练 |在目标隐藏状态上训练一个 1–2 层草稿头（便宜） |MTP 头与骨干一起 / 在骨干之上训练，预测接下来的 k 个 token |训练一个轻量块扩散草稿器，以目标特征为条件，对一块 K 个 token 去噪 |
|独立草稿模型，还是无草稿模型？ |**~ 小草稿头** —— 搭在目标上的 1–2 层额外训练层（并非完整独立模型） |**无草稿模型 / 集成** —— 额外的头直接做进目标模型本身；无需另外加载模型 |**独立草稿器** —— 一个轻量块扩散模型，按每个目标训练并随附 |
|优势 |接受率高；长草稿连贯 |便宜、集成；搭乘模型自身的计算 |起草延迟≈零；块开头强；大加速器上更宽的块≈免费 |
|劣势 |串行：延迟随深度增长 |串行：K 个 token 要 K 次前向 |块尾质量可能下降；需为每个目标训练扩散草稿器 |
|出处 |Gemini Nano "构建于其上"的基础。家族：EAGLE-2（草稿树）、EAGLE-3（训练期测试）、EAGLE-3.1、P-EAGLE。 [arXiv:2401.15077](https://arxiv.org/abs/2401.15077) 。 |三次发布共同的思想：Gemma 4 内置 MTP 头；Gemini Nano 装到冻结模型上；DeepSeek-V4 原生内置（见下方 MTP-1）。 [Gemma 文档](https://ai.google.dev/gemma/docs/mtp/overview) · [arXiv:2404.19737](https://arxiv.org/abs/2404.19737) 。 |UCSD Z-Lab，ICML 2026（ [arXiv:2602.06036](https://arxiv.org/abs/2602.06036) ）；DeepSeek DSpark 中"并行块"的那一半。 _不同于_ DeepSeek-V4- **Flash** _模型_ 。 |

所以清晰的心智模型是： **EAGLE 与 MTP 都是自回归** 草稿器（区别在草稿器 _住在哪里_ —— 一个以特征为条件的额外层 vs. 额外的头），而 **DFlash 是异类：它是并行的** ，靠扩散一次性生成整块。串行 vs. 一次前向 —— 这正是本文其余部分围绕的那条轴。

**附加术语 —— MTP-1：** 就是"只带一个额外头的 MTP"，即向前预测一个 token。DeepSeek-V4 内置了 MTP-1（每次前向 2 个 token）；DSpark 随后在这个基线之上叠加其半并行、置信度调度的验证。

**通用 DFlash —— 它是什么、怎么训练、怎么使用。**  
  
**是什么：** DFlash（ _"Block Diffusion for Flash Speculative Decoding"_ ，UCSD Z-Lab —— Jian Chen、Yesheng Liang、Zhijian Liu；ICML 2026）用一个 **轻量块扩散模型** 替代自回归草稿器。它不再一次猜一个 token，而是在一次前向中"绘制"出一块 K 个候选 token —— 把 O(K) 的串行起草变为 O(1)。  
  
**怎么训练：** 训练一个小的块扩散草稿器，去噪/生成一块未来 token，并 _以从目标模型抽取的上下文特征（隐藏状态）为条件_ —— 正是让草稿保持准确的 EAGLE 式技巧。草稿器针对每个目标模型在指令数据上训练，并以检查点发布（如 `z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat` 、 `z-lab/Qwen3-4B-DFlash-b16` ），块大小 K 固定（如 10–16）。  
  
**怎么使用：** 作为投机解码流水线里的 _提议器（proposer）_ 直接接入；目标模型并行验证整块并保留正确前缀（无损）。它已集成进 vLLM（GPU/PyTorch）与 vLLM-TPU/JAX（PR #1868–1870），在多步之间维护一个目标隐藏状态的上下文缓冲。在 TPU v5p 上有"K 平坦（K-flat）"现象 —— 验证 16 个与 1024 个 token 代价几乎一样，因此更宽的块≈免费，真正的杠杆变成 _草稿质量_ 。据报告：TPU v5p 上平均 **3\.13×** （数学任务峰值≈6×）；与 EAGLE-3 正面对比为 **2\.29×** 对 1.30×。  
  
**在 DSpark 中：** DeepSeek 的 DSpark 把 DFlash 的 _并行块_ （块开头强）与一个 _自回归_ 的 EAGLE-3/MTP 步骤（长草稿深处连贯）融合，胜过任一单独方法。所以 DFlash 是一种通用、与模型无关的起草方法；DSpark 则是把它用作其两半之一的一个生产系统。

核心权衡

## 自回归解码 vs. 并行草稿 — 每种方法都落在这条轴上

三次发布之下都藏着同一组张力。草稿模型可以 **自回归** 地产出猜测（一次一个 token，每个猜测以上一个为条件），也可以 **并行草稿** （一次预测一整块 token）。它们以相反的方式失效 —— 而 2026 年的这些系统，本质上是关于如何把两者结合的不同押注。

| |自回归草稿 |并行草稿 |
| --- | --- | --- |
|如何起草 |_串行_ 地生成草稿 token —— 每个草稿 token 都要回填以产生下一个。 |在一次前向中 _同时_ 预测若干草稿 token（一个"并行块"）。 |
|K 个草稿 token 的代价 |**K 次串行** 草稿前向 —— 延迟随投机深度线性增长（一个"隐藏的架构天花板"）。 |整块只需 **一次** 前向 —— 深度几乎免费。 |
|优势 |后面的 token 能看到前面的猜测，长草稿更 _连贯_ （"EAGLE-3 在长草稿上更连贯"）。 |在 _开头_ 的位置非常强，因为草稿之间无需上下文（"DFlash 在初始位置更强"）。 |
|劣势 |草稿模型慢、或在低接受率下草稿过深，反而会 _拖累_ 净速度。 |靠后的草稿 token 看不到前面的，块越长质量越差。 |
|代表 |**EAGLE** 家族（EAGLE-1/2/3/3.1）。 |**MTP** 头； **P-EAGLE** （并行草稿 EAGLE）。 |

这正是 **P-EAGLE** （"并行草稿 EAGLE"）要弥合的鸿沟：它通过一个可学习的共享隐藏状态，把 EAGLE 从自回归转变为 _并行多 token 预测_ ，在保留 EAGLE 特征级准确性的同时去除串行前向瓶颈（ [arXiv:2602.01469](https://arxiv.org/abs/2602.01469) ；另见 [vLLM](https://vllm.ai/blog/p-eagle) 与 [Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/parallelize-speculative-decoding-with-p-eagle-on-amazon-sagemaker-ai/) 的文章）。

这也是为什么 DSpark 的作者 **Dmytro Dzhulgakov** （Fireworks AI 联合创始人兼 CTO，也是长期的 PyTorch 核心维护者）把 DSpark 描述为两种风格的 _融合_ ：

> "DSpark ≈ EAGLE + MTP。DFlash 在初始位置更强；EAGLE-3 在长草稿上更连贯，但开头的猜测质量较低。DSpark 结合了并行块与自回归两种思路，胜过任一单独方法。" —— @dzhulgakov

**投机并非免费。** 同一长帖给出了支配性公式：  
  
`time_per_token = (num_tokens_drafted × drafter_time + verify_time(num_tokens_drafted)) / num_tokens_accepted`  
  
草稿模型太慢、或以低接受率草稿过多 token，都可能实际 _拖累_ 吞吐。上面每个系统其实都只是在调这个分式的分子与分母。—— @dzhulgakov（Fireworks AI）

总结 1  ·  2026 年 6 月 27 日

## DeepSeek DSpark — 超大规模下的投机解码

**DSpark** 不是一个新模型 —— 它是叠加在既有 **DeepSeek-V4** 检查点之上的推理期优化。正如 Dmytro Dzhulgakov 在帖子里所说，它"巧妙地整合了许多投机解码思想，在真实生产系统中实现 1.5× 到 5× 的吞吐提升"。关键词是 _整合_ ：DSpark 与其说是单一技巧，不如说是把业界最好的想法精心拼装、并为服务流量调优。

V4 本身已内置一个 **MTP-1** 头，所以在 DSpark 介入之前，基座模型每次前向就能产出 _两个_ token。DSpark 在此之上加入 DeepSeek 所称的 **"半并行（semi-parallel）"** 方法：先投机生成多个候选 token，再施加 **自适应/置信度调度的验证** —— 只在有希望的猜测上花验证算力，而不是死板地逐个 token 检查。据报道其效果是消除了"无效检查带来的算力浪费"。

* **单用户速度：** DeepSeek-V4 _Flash_ 约提速 60–85%； _Pro_ 版本约 57–78%（二手报道）。
* **吞吐：** 视并发不同提升 1.5×–5×（帖子的主标题；报道援引 51%–400%）。
* **无需重训基座模型** —— 复用已部署的 V4 权重，因此收益本质上是在 MTP-1 之上的"免费"工程。
* 以完整论文发布（33 位作者，来自 **北京大学与 DeepSeek-AI** ，由 Xin Cheng 等领衔， **梁文锋（Wenfeng Liang）** 为资深作者），并附开源的 [DeepSpec](https://github.com/deepseek-ai/DeepSpec) 训练仓库与公开检查点（ `deepseek-ai/dspark_qwen3_4b_block7` 等）。

> "DSpark …… 巧妙地整合了许多投机解码思想，在真实生产系统中实现 1.5x 到 5x 的吞吐提升。" —— @dzhulgakov

热度并不止于 DeepSeek 的研究团队内部。 **崔添翼（Tianyi Cui）** —— 这位前 Jane Street 量化工程师于 2026 年 3 月加入 DeepSeek，领衔打造其 Agent 技术栈的 **Harness** 团队 —— 也在 [微博上推介了开源的 DeepSpec 仓库与 DSpark](https://weibo.com/7542534202/5314445553436842) 。这是一个细微却说明问题的信号：这家公司对投机解码的倚重之广 —— 不仅是为了低成本地服务 V4，更是把它当作 Harness 团队正全力推出的、对延迟敏感的 Agent 产品的基础设施。

深入

## Dmytro 的长帖，逐条解读 — 10 步走读

Dmytro Dzhulgakov（Fireworks AI）以一条 **"10 个想法"** 的长帖解释了 DSpark，从 LLM 解码的最基础概念一路搭建到完整的 DSpark 设计。下面逐步走读这条长帖，每条都附上原始示意图。每张卡片都链接回原推文。

🧵

**Dmytro Dzhulgakov** · @dzhulgakov · 2026 年 6 月 27 日

来自 @deepseek\_ai 的 DSpark 巧妙地整合了许多投机解码思想，在真实生产系统中实现 1.5x 到 5x 的吞吐提升。让我们用 10 个想法、从最基础处开始来理解它 🧵

DSpark 长帖头图 1 DSpark 长帖头图 2

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922887595499930)

1

@dzhulgakov · 2026 年 6 月 27 日

LLM 解码中的批处理（Batching）

生成 token 受限于从显存读取权重。所以并行解码 10 个 token 只比生成 1 个略慢。连续批处理（continuous batching）正是利用了这一点。

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922889868779707)

2

@dzhulgakov · 2026 年 6 月 27 日

投机解码

对同一请求，token N+1 依赖 token N，所以我们无法并行解码它们。但如果我们能猜出这些 token（"投机"），就能从主模型的视角快速验证其中哪一段前缀是正确的。

投机解码示意图

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922892142104962)

3

@dzhulgakov · 2026 年 6 月 27 日

草稿模型（Draft model）

如何投机？当然是用一个模型。最简单的是跑一个在相同分布上训练的更小模型，例如用 Qwen 0.8B 给 Qwen 397B 当草稿。

草稿模型示意图

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922894293749774)

4

@dzhulgakov · 2026 年 6 月 27 日

投机并非免费

`time_per_token = (num_tokens_drafted * drafter_time + verify_time(num_tokens_drafted)) / num_tokens_accepted` 投机器跑得慢、或在低命中率下草稿过多 token，都可能有害。需要恰到好处的平衡。

投机代价公式示意图

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922896588087753)

5

@dzhulgakov · 2026 年 6 月 27 日

EAGLE 与 MTP

把草稿器做成主模型的一个额外 transformer 层，即除了上一个 token 之外，它还消费丰富的潜在表示（最后一层激活）。这样只需 1–2 层、而非整个模型，就能得到更快也更准确的投机器。

EAGLE 与 MTP 示意图

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922898425176293)

6

@dzhulgakov · 2026 年 6 月 27 日

DFlash

MTP 需要 N 步来生成 N 个草稿 token。DFlash 借用扩散（diffusion）思想，在一次前向中产出全部 N 个 token。投机快得多，但草稿质量时好时坏，相比 MTP/EAGLE 各有胜负。

DFlash 扩散式草稿示意图

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922900400640398)

7

@dzhulgakov · 2026 年 6 月 27 日

DSpark ≈ EAGLE + MTP

DFlash 在初始位置更强。EAGLE-3 在长草稿上更连贯，但开头的猜测质量较低。DSpark 结合了并行块与自回归两种思路，胜过任一单独方法。

DSpark = EAGLE + MTP 示意图 DSpark 性能图表

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922902376198579)

8

@dzhulgakov · 2026 年 6 月 27 日

更便宜的串行块

EAGLE-3/MTP 在每个草稿位置都跑完整注意力。由于 DFlash 有并行块来捕获之前的上下文，串行步骤可以用 RNN、甚至马尔可夫模型做得便宜得多。这些都带来一个更快、却依然准确的草稿器！

更便宜的串行块示意图 1 更便宜的串行块示意图 2

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922904217543082)

9

@dzhulgakov · 2026 年 6 月 27 日

可变长度草稿与硬件感知调度器

num\_draft\_tokens 应该取多少？这是变化的：
\* 有些请求（如写代码）比其他更容易预测
\* 最优长度取决于服务器负载（批大小）。负载低、GPU 算力空闲时多投机一些。

可变长度草稿示意图 1 硬件感知调度器示意图 2

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922906339770683)

10

@dzhulgakov · 2026 年 6 月 27 日

在线草稿器校准

模型往往在预测下一个 token 时过度自信，这使得很难确定停止草稿的阈值。但我们可以观察运行时草稿器的表现，并在线"校准"阈值。

在线草稿器校准示意图

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922908550209571)

@dzhulgakov · 2026 年 6 月 27 日

把它们拼到一起

DeepSeek 的魔力在于卓越的系统工程与紧密的模型协同设计。其中许多想法此前都已发表。令人印象深刻的是，他们如何把它们整合在一起，用一套自适应系统交付巨大的端到端提升。

总结：把它们拼到一起 示意图

[在 X 上查看 →](https://x.com/dzhulgakov/status/2070922910148251685)

总结 2  ·  2026 年 6 月 26 日

## Gemini Nano 冻结式 MTP — 端侧的投机解码

谷歌研究院攻克的是与 DeepSeek 相反的极端：不是数据中心，而是一部手机。移动推理受制于严苛的内存与能耗预算，而标准投机解码需要一个 _独立的_ 草稿模型（如 128M 参数），它既争抢内存，又对主模型的内部状态"视而不见"。他们的答案是把 Multi-Token Prediction 改造性地装到 **冻结的 Gemini Nano v3** 上 —— 该模型已部署在 Pixel 9 与 10 上。

设计依赖三步：

* **晚退出（late-exit）MTP 头。** 不用独立草稿器，而是在主模型的最后若干层上加一个轻量 Transformer 头，从骨干的高维隐藏状态预测未来 token。
* **冻结骨干。** 基座权重冻结，只训练这个头。这保证能力与安全对齐 **零退化** ，并能以完全向后兼容的方式推送效率更新 —— 输出逐比特一致。
* **零拷贝架构。** 该头 _直接交叉注意力到主模型冻结的 KV cache_ ，而不维护自己的 cache。这消除了草稿器的 prefill 延迟，相比独立草稿器每实例节省约 **130 MB** 。

在 AI 通知摘要、校对等生产工作负载中，MTP 平均每次前向多正确预测 **近两个 token** ，在 Pixel 9 上带来 **50%+ 的提速** ，在结构性强的任务（如智能回复）上 token 接受率最高提升 **55%** —— 同时因更少唤醒重型处理器而降低能耗。该工作明确构建于 **EAGLE** 框架与 **CALM** （Confident Adaptive Language Modeling）之上，并展望了分支/并行解码与"验证宽松化"。

总结 3  ·  2026 年 5 月 5 日

## Gemma 4 Assistant — 人人可用的投机解码

Gemma 4 是这股趋势 **走向开源** 的地方。谷歌在主线之外发布了一系列自回归 **草稿** 模型外加一个 **MTP** 头 —— 官方命名为 **"Gemma 4 Assistant"** ，以 `-assistant` 检查点发布（如 `google/gemma-4-E4B-it-assistant` ；Transformers 模型类型为 `gemma4_assistant` ，作为 `assistant_model` 加载）。在同样的 Apache-2.0 许可下，它带来最高 **3×** 的推理提速，"输出质量与推理准确性零退化"。关键在于它自首日起就支持 **Transformers、MLX、vLLM、SGLang 与 Ollama** ，所以这份提速立刻可用，而非研究摆设。

据官方文档，Gemma 4 的 MTP 不只是外挂草稿器。三项增强让草稿 token 更便宜也更准确：

* **共享输入嵌入。** 草稿模型复用目标的嵌入表，而非自带一份。
* **目标激活。** 草稿器取目标的 _最后一层激活_ ，与 token 嵌入拼接，再降维到草稿器维度 —— 因此它并非对骨干状态"视而不见"。
* **高效嵌入器。** 为避免在整个词表上打分，把 token 聚成簇；头先挑出可能的簇，再把最终计算限制在这些簇内（E2B/E4B 变体）。

文档中一个诚实的注意点：对 **MoE** 模型（Gemma 4 26B A4B），验证草稿 token 可能需要加载额外的专家权重，这在 **批大小为 1** 、且硬件并行性不佳时会抵消收益。批大小更大时，专家激活重叠增多，收益得以恢复。这次 Gemma 4 发布是 Gemini Nano 工作的直接前身 —— 博客明确指出冻结式 MTP 工作构建于"用 MTP 加速 Gemma 4"之上。

并排对比

## 对比 — 同一思想的三个角度

|维度 |Gemma 4 Assistant |Gemini Nano 冻结式 MTP |DeepSeek DSpark |
| --- | --- | --- | --- |
|发布时间 |2026 年 5 月 5 日 |2026 年 6 月 26 日 |2026 年 6 月 27 日 |
|目标场景 |开源权重，通用 / 端侧 |端侧（Pixel 9 与 10） |服务器规模的生产服务 |
|基座模型 |Gemma 4 家族（含 26B A4B MoE） |Gemini Nano v3 |DeepSeek-V4（Flash 与 Pro） |
|是否开源？ |**✔ 是** —— Apache-2.0 权重（HF、Kaggle） |**✗ 否** —— 专有；随 Pixel 更新下发 |**✔ 是** —— MIT：论文 + 代码 + 检查点（DeepSpec 仓库） |
|草稿器设计 |自回归草稿器 + MTP 头；共享嵌入、目标激活、聚簇嵌入器 |冻结骨干上的"晚退出"MTP 头；交叉注意力到主 KV cache（零拷贝） |构建于 V4 的 MTP-1 头 + "半并行"候选生成 |
|是否基于 EAGLE？ |**~ 部分** —— EAGLE _风格_ 的特征条件（消费目标最后一层激活），但是 MTP "assistant" 头，而非 EAGLE 算法本身 |**✔ 是** —— 明确构建于 **EAGLE** 框架（加 CALM 晚退出） |**✔ 是** —— **EAGLE-3 + MTP** 混合（"DSpark ≈ EAGLE + MTP"） |
|是否并行草稿？ |**✗ 否** —— assistant _自回归_ 地起草（一次一个 token） |**✗ 否** —— 自回归 MTP 头（并行/分支解码为明确的未来工作） |**✔ 是** —— _混合_ ：DFlash 并行块（一次产出全部 N 个 token）+ 自回归的 EAGLE 式步骤 |
|是否使用 DFlash（块扩散草稿器）？ |**✗ 否** —— 自回归 MTP "assistant" 头，无扩散 |**✗ 否** —— 自回归晚退出 MTP 头，无扩散 |**✔ 是** —— DFlash 块扩散草稿器 _正是_ DSpark 的并行那一半（与自回归的 EAGLE-3/MTP 步骤配对） |
|集成式，还是独立草稿模型？ |**~ 独立伴随模型** —— 一个小的 "assistant" 检查点与主模型一起加载，但共享目标的嵌入与激活 |**✔ 集成** —— 冻结骨干上的晚退出头；无独立模型，额外占用近乎为零（零拷贝） |**✔ 集成** —— MTP-1 头 + DFlash 块搭乘已部署的 V4 权重；无独立的单独语言模型 |
|是否共享目标 KV cache？ |**~ 部分** —— 共享输入嵌入并消费目标激活，但非完整的 KV cache 交叉注意力 |**✔ 是** —— **零拷贝** 直接交叉注意力到冻结 KV cache（无自有 cache；省约 130 MB） |**✔ 是** —— 集成的 MTP 头搭乘模型自身的主干/KV（无独立草稿器 cache） |
|验证 |标准并行验证（无损） |标准并行验证；逐比特一致 |自适应 / **置信度调度** 验证 |
|骨干训练 |MTP 头与骨干联合预训练 |**冻结** 骨干；只训练头（改造式） |不重训基座；在已部署权重上优化 |
|主打提速 |推理最高 **3×** |Pixel 9 上 **50%+** ；每次前向多约 2 个 token |吞吐 **1\.5×–5×** ；单用户 57–85% |
|质量影响 |无损 |无损（冻结骨干） |无损（被拒草稿丢弃） |
|主打优势 |生态覆盖 + 首日框架支持 |省约 130 MB 内存；更低能耗 / 更省电 |真实流量吞吐；不在坏检查上浪费 |
|许可 / 获取 |开源，Apache 2.0（HF、Kaggle） |专有，随 Pixel 更新下发 |HF 上的开放检查点 + 论文 |

贯穿始终的主线：三者都保持输出 **无损** ，都 _远离_ 独立草稿器、转向复用骨干自身状态（嵌入、激活或 KV cache）的头，并且都在朝同一个下一前沿收敛 —— 分支式草稿与宽松验证。差别纯粹在于环境：Gemma 4 优化 _覆盖面_ ，Gemini Nano 优化 _内存与能耗_ ，DSpark 优化 _负载下的吞吐_ 。

参考文献

## 论文 — 这股浪潮背后的谱系

2026 年的这些发布站在一条清晰的研究链条之上。按主题分组的奠基性与被直接引用的论文：

1 · 奠基

Fast Inference from Transformers via Speculative Decoding FOUNDATION

Yaniv Leviathan、Matan Kalman、Yossi Matias —— _Google Research_

为"投机解码"命名的论文：用便宜的草稿器解出 K 个 token，由目标模型并行验证，接受正确的前缀 —— 更快，且不改变输出分布。

[arXiv:2211.17192](https://arxiv.org/abs/2211.17192) · [PDF](https://arxiv.org/pdf/2211.17192)

Accelerating Large Language Model Decoding with Speculative Sampling FOUNDATION

Charlie Chen、Sebastian Borgeaud、Geoffrey Irving、Jean-Baptiste Lespiau、Laurent Sifre、John Jumper —— _Google DeepMind_

同期的投机采样表述，配有拒绝采样的正确性证明，保证加速后的输出与目标模型分布一致。

[arXiv:2302.01318](https://arxiv.org/abs/2302.01318) · [PDF](https://arxiv.org/pdf/2302.01318)

Better & Faster Large Language Models via Multi-token Prediction MTP

Fabian Gloeckle、Badr Youbi Idrissi、Baptiste Rozière、David Lopez-Paz、Gabriel Synnaeve —— _Meta AI / FAIR_

MTP 训练目标 —— 用额外的头一次预测多个未来 token。被两份谷歌文档引为 2026 年草稿器所构建于其上的"标准 MTP 实现"。

[arXiv:2404.19737](https://arxiv.org/abs/2404.19737) · [PDF](https://arxiv.org/pdf/2404.19737)

Confident Adaptive Language Modeling (CALM) EARLY-EXIT

Tal Schuster、Adam Fisch、Jai Gupta、Mostafa Dehghani、Dara Bahri、Vinh Q. Tran、Yi Tay、Donald Metzler —— _Google Research_

Gemini Nano 工作所借鉴的"晚退出/早退出"谱系：对简单 token 动态分配更少算力。冻结骨干上晚退出 MTP 头的基础。

[arXiv:2207.07061](https://arxiv.org/abs/2207.07061) · [PDF](https://arxiv.org/pdf/2207.07061) · [CALM 博客](https://research.google/blog/accelerating-text-generation-with-confident-adaptive-language-modeling-calm/)

2 · EAGLE 家族

EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty DRAFTER

Yuhui Li、Fangyun Wei、Chao Zhang、Hongyang Zhang —— _北京大学 & 微软研究院_

在 _特征_ 层面起草：草稿器是一个额外层，消费目标的最后一层激活加上一个 token，使其猜测更可能被目标接受。

[arXiv:2401.15077](https://arxiv.org/abs/2401.15077) · [PDF](https://arxiv.org/pdf/2401.15077)

EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees DRAFTER

Yuhui Li、Fangyun Wei、Chao Zhang、Hongyang Zhang —— _北京大学 & 微软研究院_

加入上下文感知的动态草稿树，扩展最有希望的草稿分支。3.05–4.26× 提速，比 EAGLE-1 快 20–40%，仍然无损。

3\.05–4.26× 提速

[arXiv:2406.16858](https://arxiv.org/abs/2406.16858) · [PDF](https://arxiv.org/pdf/2406.16858)

EAGLE-3: Scaling up Inference Acceleration via Training-Time Test DRAFTER

Yuhui Li、Fangyun Wei、Chao Zhang、Hongyang Zhang —— _北京大学 & 微软研究院_

放弃特征预测、改为直接 token 预测，并通过"训练期测试（training-time test）"融合多层特征，使草稿器能随训练数据增多而持续提升。这是 DSpark 作者在长草稿上对比的那个版本。最高 6.5× 提速（比 EAGLE-2 约快 1.4×）。

最高 6.5× 提速

[arXiv:2503.01840](https://arxiv.org/abs/2503.01840) · [PDF](https://arxiv.org/pdf/2503.01840)

EAGLE-3.1：稳定更深的投机 RELEASE

EAGLE 团队（Yuhui Li、Fangyun Wei、Chao Zhang、Hongyang Zhang）× _vLLM 团队_ × _TorchSpec 团队_ ，并获 NVIDIA GPU 支持 —— 团队署名的工程发布（无独立 arXiv 预印本；vLLM/TorchSpec 贡献者以团队整体署名）

EAGLE-3 的增量改进：在每个目标隐藏状态之后加 FC 归一化，并把归一化后的隐藏状态喂入下一解码步。这修复了深投机深度下的两个不稳定 —— 融合输入被高层隐藏状态主导，以及隐藏状态幅度沿未归一化残差路径增长 —— 使草稿器在更长草稿上保持稳定。

[vLLM 博客（2026-05-26）](https://vllm.ai/blog/2026-05-26-eagle-3-1)

P-EAGLE: Parallel-Drafting EAGLE with Scalable Training PARALLEL

_Amazon（AWS AI）_

通过可学习的共享隐藏状态，把 EAGLE 从自回归转变为并行多 token 预测，去除串行 K 次前向瓶颈，同时保留特征级准确性。检查点位于 `amazon/…-p-eagle` 。

[arXiv:2602.01469](https://arxiv.org/abs/2602.01469) · [PDF](https://arxiv.org/pdf/2602.01469) · [vLLM 博客](https://vllm.ai/blog/p-eagle) · [SageMaker 博客](https://aws.amazon.com/blogs/machine-learning/parallelize-speculative-decoding-with-p-eagle-on-amazon-sagemaker-ai/)

3 · 并行 / 扩散草稿

DFlash: Block Diffusion for Flash Speculative Decoding DIFFUSION ICML 2026

Jian Chen、Yesheng Liang、Zhijian Liu —— _UCSD Z Lab_ （Hao Zhang 团队）

用一个轻量 **块扩散** 模型替代自回归草稿器，在 **一次** 前向中产出一整块 K 个 token（把 O(K) 起草降为 O(1)），并以目标隐藏特征为条件保证准确。起草延迟≈零，瓶颈转向草稿质量。它是 DeepSeek DSpark 中"并行块"的那一半；已部署于 vLLM 与 vLLM-TPU。

>6× 无损；比 EAGLE-3 最高快 2.5×

[arXiv:2602.06036](https://arxiv.org/abs/2602.06036) · [PDF](https://arxiv.org/pdf/2602.06036) · [Z-Lab](https://z-lab.ai/) · [Google TPU 博客](https://developers.googleblog.com/supercharging-llm-inference-on-google-tpus-achieving-3x-speedups-with-diffusion-style-speculative-decoding/)

4 · DeepSeek 与 DSpark

DeepSeek-V3 Technical Report MODEL

DeepSeek-AI —— _DeepSeek_

DeepSeek 内置 MTP 设计（为 MTP 共享嵌入/输出头）的来源，V4 系列继承之，DSpark 在其上加速。

[arXiv:2412.19437](https://arxiv.org/abs/2412.19437) · [PDF](https://arxiv.org/pdf/2412.19437)

DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation SERVING

Xin Cheng\*、Xingkai Yu\*、Chenze Shao\*、Jiashi Li\*、Yunfan Xiong\*、Yi Qian、Jiaqi Zhu、Shirong Ma、Xiaokang Zhang、Jiasheng Ye、Qinyu Chen、Chengqi Deng、Jiping Yu、Damai Dai、Zhengyan Zhang、Yixuan Wei、Yixuan Tan、Wenkai Yang、Runxin Xu、Yu Wu、Zhean Xu、Xuanyu Wang、Muyang Chen、Rui Tian、Xiao Bi、Zhewen Hao、Shaoyuan Chen、Huanqi Cao、Wentao Zhang、Anyi Xu、Huishuai Zhang、Dongyan Zhao、Wenfeng Liang —— _北京大学 & DeepSeek-AI_ （\* 共同一作；梁文锋 Wenfeng Liang 为末位/资深作者）

框架本体。 **半自回归（semi-autoregressive）** 草稿器 —— 并行骨干耦合一个轻量串行模块 —— 引入块内依赖，修复纯并行草稿器的接受率衰减； **置信度调度、负载感知的验证** 依据估计的前缀存活概率与引擎吞吐画像，为每个请求动态裁剪验证长度。在 DeepSeek-V4 服务系统的真实流量下，在同等吞吐下相比 MTP-1 生产基线单用户提速 60–85%。随 **DeepSpec** 训练仓库开源（其中也含 DeepSeek 自训的 DFlash 与 EAGLE-3 草稿器）。

单用户相比 MTP-1 提速 60–85%

[论文 PDF](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf) · [DeepSpec 仓库](https://github.com/deepseek-ai/DeepSpec) · [HF: V4-Flash-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark) · [10 想法长帖](https://x.com/dzhulgakov/status/2070922887595499930)

5 · 用于投机解码的 MTP

FastMTP: Accelerating LLM Inference with Enhanced Multi-Token Prediction MTP

Jinwen Luo 等 —— _腾讯（Tencent）_

让 MTP 训练与其推理模式对齐，提升多步草稿质量。约 2.03× 提速、输出无损，比普通 MTP 高 82%。权重位于 `TencentBAC/FastMTP` 。

约 2.03× 提速

[arXiv:2509.18362](https://arxiv.org/abs/2509.18362) · [PDF](https://arxiv.org/pdf/2509.18362)

6 · 回顾

Looking back at speculative decoding BLOG

_Google Research_

谷歌研究院自己对该技术的回顾，直接从 Gemini Nano 冻结式 MTP 帖子链接而来。

[research.google/blog/looking-back-at-speculative-decoding](https://research.google/blog/looking-back-at-speculative-decoding/)

**模型检查点。** 上述系统不只是论文 —— 它们都附带可运行的权重：DSpark 于 DeepSeek-V4-Flash（ [deepseek-ai/DeepSeek-V4-Flash-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark) ）、开源的 Gemma 4 Assistant MTP 草稿器（ [google/gemma-4-E4B-it-assistant](https://huggingface.co/google/gemma-4-E4B-it-assistant) ），以及在 vLLM 与 SGLang 中广泛使用的 EAGLE/EAGLE-3 草稿器检查点。DSpark 长帖的作者与讲解者是 Fireworks AI 联合创始人兼 CTO **Dmytro Dzhulgakov** （也是长期的 PyTorch 核心维护者， [@dzhulgakov](https://x.com/dzhulgakov) ）。

训练栈

## 草稿器从哪里来 — 开源训练库

上面每个系统都附带一个 _训练好的草稿器_ —— 一个 EAGLE 头、一个 MTP 头、或一个 DFlash 块。但谁来训练它们、用什么基础设施训练？2026 年故事里更安静的那一半，是一批专门的 **开源训练库** 的兴起 —— 它们把起草从研究产物变成可复用的流水线。它们都在与同一个核心障碍较劲：如何把目标模型的隐藏状态低成本、大规模地灌入草稿模型 —— 而每一个都从不同角度攻克它。上文 DSpark 背后的 **DeepSpec** ，正是这条可上溯至 2025 年的脉络中最新的一员：

2025 年 7 月 —— SpecForge（SGLang）

首个专为 **EAGLE-3** 打造的训练框架，与 **SGLang** 原生打通 —— 草稿模型一训完即可部署。内置训练期测试（TTT）、在线与离线两种隐藏状态模式、FSDP + 张量并行，并原生支持 MoE 目标（Llama 4、DeepSeek）。

2025 年 11 月 —— Speculators（vLLM）与 SageMaker EAGLE

同一个月里的两记生产化重拳。 **Speculators** （vLLM / Red Hat）把草稿器标准化为统一的 Hugging Face 格式，开箱即在 vLLM 中运行；亚马逊 **SageMaker AI** 推出 **EAGLE-2/3 自适应** 投机解码，在你 _自己_ 的流量上重训草稿头，带来约 2.5× 的吞吐。

2026 年 3 月 —— TorchSpec（TorchSpec 团队与 Mooncake 团队）

一个 torch 原生的 **解耦式（disaggregated）** 草稿器训练框架：把生成隐藏状态的推理引擎与消费隐藏状态的训练 worker 解耦，通过 **Mooncake** 存储以 RDMA/TCP 直接流式传输张量 —— 不落盘，也不共置。约 1,500 H200 小时训出一个 Kimi K2.5 的 EAGLE-3 草稿器。

2026 年 6 月 —— DeepSpec（DeepSeek）

DeepSeek 随 **DSpark** 一起开源的仓库 —— 不仅给出 DSpark 配方，还附带 DeepSeek 自训的 **DFlash** 与 **EAGLE-3** 草稿器训练，把上文的算法研究与可运行的生产栈闭环起来。

一年的训练库发布 —— 让投机解码从一篇论文变成一条流水线的工具。

逐一细看这些库

SpecForge: Accelerating Speculative Decoding Training for SGLang TRAINING

SGLang 团队 — _LMSYS / SGLang_

一个专为 EAGLE-3 打造、与 SGLang 紧密集成的训练框架 —— 刚训好的草稿头即可在推理端开箱运行。内置训练期测试（TTT）支持，提供 _在线_ （即时生成隐藏状态）与 _离线_ （预计算）两种模式，配 FSDP + 张量并行以支撑大集群，并原生支持 Llama 4、DeepSeek 等 MoE 目标。

Llama 4 Maverick 草稿器 MT-Bench 2.18×

[LMSYS 博客](https://lmsys.org/blog/2025-07-25-spec-forge/) · [GitHub: sgl-project/SpecForge](https://github.com/sgl-project/SpecForge)

Speculators: Standardized, Production-Ready Speculative Decoding TRAINING FORMAT

_vLLM 项目 / Red Hat（Neural Magic）_

一个用于构建、训练并 _存储_ 草稿器的统一库，把草稿器规整为单一标准化的 Hugging Face 格式，并即刻兼容 vLLM —— 于是在任何地方训出的投机器都能直接落进生产服务器。训练能力在 v0.3.0 落地；v0.5.0（2026 年 5 月）加入了 **DFlash** 支持，并基于 vLLM 原生隐藏状态抽取统一了在线训练。

[Red Hat 公告](https://developers.redhat.com/articles/2025/11/19/speculators-standardized-production-ready-speculative-decoding) · [GitHub: vllm-project/speculators](https://github.com/vllm-project/speculators) · [v0.5.0（DFlash）博客](https://vllm.ai/blog/2026-05-28-speculators-v050)

EAGLE-Based Adaptive Speculative Decoding on Amazon SageMaker AI TRAINING MANAGED

Amazon SageMaker AI 团队 — _AWS_

SageMaker 推理优化工具箱中的一条托管路径，训练 **EAGLE-2/3** 头 —— 更关键的是，它能在你自己采集的流量上 _重新_ 训练这些头，让草稿器适配你真实的工作负载，而非通用基准。支持六种架构（Llama、Qwen2/3、Qwen3-MoE、GPT-OSS 用 EAGLE-3；Qwen3-Next 用 EAGLE-2），并附带预训练好的头以便即开即用。 （披露：这是我在 SageMaker 团队参与交付的一个项目。）

约 2.5× 吞吐，无损

[AWS 机器学习博客](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-introduces-eagle-based-adaptive-speculative-decoding-to-accelerate-generative-ai-inference/)

TorchSpec: Speculative Decoding Training at Scale TRAINING

TorchSpec 团队与 Mooncake 团队 — _PyTorch 生态_

一个 torch 原生的 **解耦式** 草稿器训练框架，正面解决隐藏状态瓶颈：把 _生成_ 目标隐藏状态的推理 GPU 与 _消费_ 它们的训练 GPU 分离，通过 **Mooncake** 存储以 RDMA/TCP 直接流式传输张量 —— 既消除离线流水线动辄数 TB 的落盘成本，又消除共置训练的显存压力。推理与训练可独立扩展；支持 vLLM 与 SGLang 目标。

约 1,500 H200 小时训出 Kimi K2.5 EAGLE-3 草稿器；BS1 下 +60% 吞吐

[PyTorch 博客](https://pytorch.org/blog/torchspec-speculative-decoding-training-at-scale/) · [GitHub: torchspec-project/TorchSpec](https://github.com/torchspec-project/TorchSpec) · [Mooncake](https://github.com/kvcache-ai/Mooncake)

DeepSpec TRAINING

DeepSeek-AI — _DeepSeek_

DeepSeek 与 **DSpark** 论文一同开源的训练仓库。除 DSpark 配方本身外，它还附带 DeepSeek 自训的 **DFlash** 块扩散与 **EAGLE-3** 草稿器训练 —— 是本文前面算法研究在生产侧的对应物，也是这条时间线 2026 年这一端的压舱石。

[GitHub: deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) · [DSpark 论文（PDF）](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf)

两个月，两家实验室，三次发布，一个收敛的思想 —— 而在它们之下，还有五套开源训练栈（来自 SGLang、vLLM/Red Hat、AWS、PyTorch×Mooncake 与 DeepSeek），把这些草稿器变成可复现的流水线。如果说 2024–2025 是关于 _训练_ 更大更便宜的模型，那么 2026 正在成为投机解码成为 _服务_ 它们之标准方式的一年 —— 在手机上、在数据中心里、以及介于两者之间的一切地方。

  
* * *