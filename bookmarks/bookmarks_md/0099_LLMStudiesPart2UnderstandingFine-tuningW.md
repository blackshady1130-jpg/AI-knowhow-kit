---
url: https://shermwong.com/2023/02/10/llm-studies-part-2/
title: "LLM Studies (Part 2) — Understanding Fine-tuning"
description: "Finetuning LLMs is no doubt the hottest topic of early 2023. Thx to the release of LLaMA, within a couple of months so many high-impact fine-tuning projects emerged: Alpaca, Dolly, Vicuna... (apparently exhausting the list thx to Facebook’s unique taste for this species). It's worth noting that the incumbent \"fine-tuning\" is fundamentally different from the…"
published: "2023-02-10T18:32:09-08:00"
captured_at: "2026-03-08T10:29:09.925Z"
---

# LLM Studies (Part 2) — Understanding Fine-tuning

Finetuning LLMs is no doubt the hottest topic of early 2023. Thx to the release of LLaMA, within a couple of months so many high-impact fine-tuning projects emerged: Alpaca, Dolly, Vicuna… (apparently exhausting the list thx to Facebook’s unique taste for this species).

It’s worth noting that the incumbent “fine-tuning” is fundamentally different from the “fine-tuning” in pre-GPT era — In the ResNet/BERT era (5 years ago? can you imagine the speed of innovation!), fine-tuning is essentially transferring/sharing representations across different tasks. However in the GPT era, now, learning domain invariant representation is no longer the gist, people assume LLM already possess universal knowledge by itself, so the goal of fine-tuning is to “align” LLM output to desirable task formulation. My own understanding this is similar to an earlier research direction named “MetaLearning”, where model is guided to learn not only the task dataset but also the task itself (by differentiating with other tasks for example), but LLM makes it much more explicit and simpler: everything is text-in-text out, you want to translate english to french? Just “tell” the model in plain language — yes, here you go prompt-engineering.

![](https://shermwong.com/wp-content/uploads/2023/06/351666202_1390944118417364_8694859933757391573_n.jpg?w=843)

“Prompting” is way more sophisticating, covering a wide range of cases than fine-tuning for LLM applications, image attributed to [theaiedge.io](https://newsletter.theaiedge.io/)

As one of the earliest practitioners of LLM Fine-tuning, without stressing too much theoretical details, I like to group the use cases into 2 categories:

-   Instruction Fine-tuning (IFT): a pure pre-trained LLM often talks non-sense; if you want a “sane” LLM”: a helpful assistant, a talking cyclopedia, a chatbot aligned with human value, then you need to bake “instructions” into it with IFT.
-   Supervised Fine-tuning (SFT): this is closer to old sense of the domain specific tuning. You train the LLM to adapt to your downstream tasks.

## Instruction Fine-tuning

IFT to me, is identical to prompt engineering, instead of putting everything “in-context”, use finetuning to carefully bake these instructions into LLM. Even a small set of high quality curated IFT set can significantly boost LLM quality, one of such example is LIMA, which has significantly fewer training examples (1000) than Alpaca (10k+). Usually the IFT dataset is formatted as follow:

**Instruction Template:**

*Below is an instruction that describes a task.\\nWrite a response that appropriately completes the request.\\n\\n*

**Instruction**:

*Explain why the following fraction is equivalent to 1/4″*

**Input:**

*4/16*

**Output:**

*The fraction 4/16 is equivalent to 1/4 because both fractions represent the same value. A fraction can be simplified by dividing both the numerator and the denominator by a common factor…*

So where are these instructions coming from? It comes **exactly from prompt-engineering**! There’s the self-curated 1000 pairs from [self-instruct](https://arxiv.org/pdf/2212.10560.pdf) and [LIMA](https://arxiv.org/abs/2305.11206); there’s also the crowdsourcing set from [Dolly](https://huggingface.co/datasets/databricks/databricks-dolly-15k); more recently there’re works to use ChatGPT to enhance instruction writing like [alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html) and [Longform](https://github.com/akoksal/LongForm) and [Humpback](https://medium.com/@yousra.aoudi/meta-unveils-humpback-vicuna-and-stablecode-make-waves-ai-models-to-watch-b4b7054beec5).

![](https://shermwong.com/wp-content/uploads/2023/06/screenshot-2023-06-07-at-4.09.14-pm.png?w=1024)

[Self-Instruct](https://arxiv.org/pdf/2212.10560.pdf) process, 175 human-written seed tasks were to be enhanced by LLMs, ended up generating 50k IFT pairs. Note the generated instructions are not necessarily overlapping with the seed tasks’ topics, the seed tasks “induce” the LLM to generate more diverse topics.

Speaking of the “quality” of IFT datasets, usually they are stressed by:

-   Diversity: instructions that align LLM with a wide range of tasks/domains.
-   De-Ambiguity: the instruction should be simple and clear (to human’s sense), the input-output should be “commonsense” enough, agreed by majority of people, it should not require external context to answer (no external references).

Note that by diversity IFT does not need exhaustive list of instructions in all areas like pre-training (although efforts like Dolly does try to capture as much diversity as they can by crowdsourcing from large audience), nor is there suggestions to use strict math derivations as “ambiguity-free” training data. To me **the IFT curation process is rather free-formed.** We have seen the instructions being generated with all the doozies: human written, ChatGPT written, domain-experts — and they ALL worked! In fact, I wouldn’t be surprised if IFT is theoretically equivalent to few-shot prompting. IFT “activates” the pre-trained LLM rather than injecting new knowledges into it.

What is the ideal size for IFT dataset? Do we expect it to be more “vertically” or “horizontally” used? Neither of the questions have a good answer for now. My own prediction is that we do expect a reasonable size, with <100k examples, high quality IFT golden-set in future, a leading effort on this is [ShareGPT](https://sharegpt.com/) (basically trying to reverse engineer chatGPT’s instruction dataset) — this is in the “horizontal” sense (let’s build more and more ChatGPTs?); for “vertical” applications, see the supervised-finetuning (SFT) section below.

Another interesting observation is that none of the IFT works have applied the “frozen first N layers, tune last 1-2 years” approach that has been pervasive in BERT era. In my own experience, fine-tuning large LLMs, especially beyond 60B parameters is a delicate manner: the loss can easily diverge, learning rate and LR warmups are finely tuned to a specific range. Although it might be possible to freeze a few layers and tune the last year, we believe such method worsen training stability and does not bring much efficiency benefit. As an alternative, the OSS community attends to low-rank approximation methods like LoRA to be able to finetune LLMs on commercial GPUs. As LLM plugs into more vertical scenarios, I can for-see a plethora of low-rank/quantization efforts will be developed to reduce LLM costs by at least 100x (in terms of both FLOPS and memory).

## Supervised Fine-tuning

This is an under-developed, and still mystery field. The question is how to have LLM learn domain specific knowledges that has not present in its pre-training corpus. For example, having LLM fine-tune on my company’s product catalog, would it be able to understand/sell product just like hiring a salesman? Clearly having this fine-tuning capability is a killer move for any LLM application. But in reality we have seen application owners in fact circumvent this capability and resort to 2 alternatives:

1.  Retrieval based: fetch relevant content using a retrieval system and let LLM handle them in-context.
2.  ChatGPT plugin like, a similar work is [Toolformer](https://arxiv.org/abs/2302.04761)/[ToolLLM](https://github.com/OpenBMB/ToolBench), which tries to make LLM use tools (making its own decisions on when and where to call) to fetch→ process knowledges from external sources

Note the boundary between 1-2 is also blurred, hybrid solutions can be designed.
So why is fine-tuning not favored? I would like to answer this in my own understanding, 2 perspectives.

**It’s Dangerous**
It is still dangerous to control exactly LLM’s knowledge structure. How does LLM learn fact/knowledges? If you ask ChatGPT any year of the president of the U.S. it can answer with 100% accuracy, impressive right? In fact, LLM practitioners already found large models CAN memory facts pretty accurately as long as tuned with more epochs (>3). But how does it “store” these facts? In the field of computer science, there are 2 methods: 1) search/retrieval: Google works this way, it “index” vast amount of documents and build query to fetch the relevant document from database; 2) knowledge graph, in this particular US president example, a quadruple is formed in KG: (Lincoln, President, 1860-1866, U.S.A), the query of “who is the president of USA in 1860” is parsed into “entities” of “President”, “1860-1866” where a graph query can be performed to immediate fetch the result of “Lincoln”. Hence KG is considered a more compressed form of retrieval system. What does LLM learn into? We know LLM also learns by compression: P\_{\\theta}(X), the lowest perplexity/entropy indicates optimal compression rate of corpus X. But apparently it’s such a lossy compression to learn by perplexity, and we know LLM is way more than pure memorize — even if certain knowledge not appears in original corpus it is able to correlate and re-construct knowledges: for example, the corpus may just have documents mentioning Lincoln is president from 1860-1866, but when given a query of “US president of 1861”, LLM still needs to reason that first “1861” is within the range of \[1860, 1866\], and somehow “retrieve” the knowledge it “stored” during training. Without a controllable LLM retrieval structure, purely relying on fine-tuning LLM to retrieve facts will always be dangerous, subject to hallucination or bias.
It’s fun to mention that largest SOTA PaLM has already reached 600B landmark, with fp32 this amounts to 2.4TB, which close to its original training corpus size (CC, C4 ~ 2TB), however the training corpus contains way more duplicates, so it’s in theory possible for SOTA LLM to completely memorize all the facts of the world, and retrieve them without err, if possible. There are numerous investigations into LLMs’s factual knowledges, clearly it’s far from “controllable” and anyway comparable to the 2 “traditional” methods above. One interesting observation is that you can trick LLM to lose confidence, by keep asserting his answer, although correct, is wrong.

**It’s Not that Smart, Yet**
As we mentioned above it’s an immature research topic to finetune LLM to learn knowledges, it is still reasonable to believe soon we will be able to instruct-finetuning LLM to memorize facts. Some of the recent works on this include Landmark attention ([https://arxiv.org/pdf/2305.16300.pdf](https://arxiv.org/pdf/2305.16300.pdf)). But memorizing facts is a just the first step, training a domain expert requires high level — college to grad-school level intelligence. Think about the daily works of doctors, accountants, lawyers, programmers: they are reasoning, calculating, planning, making complex decisions — none of these has SOTA LLM getting close to human performance. SOTA LLM still sucks at tasks require hard logical reasoning: still way underperform humans on math benchmarks such as GSM8k, Natural Language Inference (ANLI) and academia tasks like MMLU.

\[Update on Aug 2023\] GPT4 can already beat human in [GSM8k](https://paperswithcode.com/sota/arithmetic-reasoning-on-gsm8k) (94% by itself, 97% using code interpreter), the trend rn is fine-tuning with reasoning traces such as [CoT](https://arxiv.org/abs/2201.11903)/[ToT](https://arxiv.org/abs/2305.10601)/

### Are There any Notable Domain-SFT Works?

There are! I’ve seen many domain-specific ChatGPT works gaining traction — **after all, it wouldn’t hurt throwing domain data to LLM and get first step results!** (many are pretty decent) A few notable ones I recently found:

-   Goat – Finetuned LLaMA outperforms GPT4 on Arithmetic Tasks: [https://arxiv.org/pdf/2305.14201.pdf](https://arxiv.org/pdf/2305.14201.pdf)
-   DoctorGLM: Finetuned LLM on medical Q&A dataset in CN: [https://github.com/xionghonglin/DoctorGLM](https://github.com/xionghonglin/DoctorGLM)
-   BenTsao (original name: HuaTuo): Tuning LLaMA Model With Chinese Medical Instructions: [https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)
-   LawGPT: Finetuned LLaMA on Chinese Legal Resources: [https://github.com/pengxiao-song/LaWGPT](https://github.com/pengxiao-song/LaWGPT)