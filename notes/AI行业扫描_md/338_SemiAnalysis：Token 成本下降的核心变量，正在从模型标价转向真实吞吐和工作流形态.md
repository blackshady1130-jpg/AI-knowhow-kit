# SemiAnalysis：AI Value Capture 相关材料整理

> 整理来源：用户提供的 X/Twitter 截图与 SemiAnalysis 原文截图。  
> 说明：以下内容按截图可见文字整理，尽量保留原文措辞、数字和标点；图表部分整理为标题、坐标说明与数据点。

---

## 1. X / Twitter Thread

**Account:** SemiAnalysis  
**Handle:** @SemiAnalysis_  
**Time:** 1:00 AM · Jun 28, 2026  
**Views:** 191.1K Views

### Tweet 1/4

One of the more uncomfortable observations in our AI Value Capture piece is internal: our token spend at SemiAnalysis now runs at roughly 30% of employee compensation, with employees pulling just under 5 billion tokens per month on average, over 5x more than Meta, and our top contributors clearing 100 billion. We wrote about it openly because every research firm, hedge fund, and law firm we know is heading toward a similar number, just on a delay. (1/4) 🧵

### Tweet 2/4

The substitution math is the part to internalize. Tasks that used to need a junior analyst for several hours, converting a model to a dashboard, building chart packs from earnings, rebuilding a comp set, now resolve in minutes for a few dollars of tokens. The blended Opus 4.7 cost we observe is about $0.99 per million against $5/$25 sticker, mostly because agentic workloads run 300:1 input-to-output ratios and cache hit rates above 90% pull the effective price down. Thats a real change in the unit economics of professional services, not a 10% efficiency gain. (2/4)

### Tweet 3/4

The throughput math has gotten the most pushback in our reader notes, so its worth being precise. On the same B300 running DeepSeek R1, baseline FP8 sits near 1,000 tokens/sec/GPU, adding wideEP plus disagg gets you to roughly 8,000, and layering MTP on top pushes it to about 14,000, a 14x gain from software alone. Factor in hardware too and the most optimized GB300 NVL72 hits about 17x the best H100 config in FP8, 32x in FP4. Once you accept that compression is real, model-lab gross margin expansion stops looking like a temporary pricing oddity and starts looking structural. (3/4)

### Tweet 4/4

If you are an operator trying to write down what tokens will cost in 2027, the answer is materially lower than today, and the firms that have already adopted are the ones setting the pace. The full math, plus a value capture breakdown across labs, hyperscalers, inference providers, neoclouds, and memory vendors, is in the piece. (4/4)

---

## 2. Chart in Tweet

**Title:** Software is doing more of the work than people think  
**Subtitle:** Frontier-model throughput, tokens / second / GPU  
**Y-axis:** tokens / sec / GPU

| Hardware / Setup | Throughput |
|---|---:|
| H100 | 60 tokens/sec/GPU |
| GB300 baseline | 1,000 tokens/sec/GPU |
| GB300 + wideEP/disagg | 8,000 tokens/sec/GPU |
| GB300 + wideEP/MTP | 14,000 tokens/sec/GPU |

**Source:** SemiAnalysis — AI Value Capture: The Shift To Model Labs (Apr 2026)

---

## 3. Original Article Excerpt

# Tokens Are Getting Cheaper to Produce

At the same time, the cost of producing each token has plummeted. This is the largest driver of value accretion to inference providers, and it is a key reason for the sharp increase in margins at large AI Labs.

Cost of production for token has fallen sharply because increases in accelerator pricing generation-over-generation have been more than offset by much higher throughput (tokens/sec/gpu). Average blended price per million tokens has fallen dramatically over the past few months, agentic workloads are inherently multi-turn with longer input/output ratios and higher cache hit rates, but inference margins have gone up from < 40% to > 70% in the same time frame. For in-depth estimates on true blended price per million tokens, token production volumes, and gross margins for all the major models from OpenAI, Anthropic, and more, see our Tokenomics model.

InferenceX remains the best benchmark for tracking real-world inference performance over time for open source models given both hardware and software improvements.

The following chart shows throughput vs interactivity for B300s running DeepSeek R1 on 8k input tokens to generate 1k output tokens. The top line reflects token throughput with wideEP + disagg + MTP, the middle reflects wideEP + disagg and the lowest line is without any of the three software optimizations. The gap is startling with the same B300 able to yield ~1k, ~8k, and ~14k tokens/sec/gpu on the same hardware. One can 14x throughput with software improvements alone.

---

## 4. Extracted Key Numbers

| Metric | Value |
|---|---:|
| SemiAnalysis token spend as share of employee compensation | ~30% |
| Average employee token usage | just under 5B tokens/month |
| Relative to Meta | >5x Meta |
| Top contributors token usage | >100B tokens/month |
| Observed blended Opus 4.7 cost | ~$0.99 / million tokens |
| Sticker price comparison | $5 / $25 |
| Agentic workload input-to-output ratio | 300:1 |
| Cache hit rate | >90% |
| Inference margins | from <40% to >70% |
| B300 DeepSeek R1 baseline FP8 throughput | ~1,000 tokens/sec/GPU |
| B300 + wideEP + disagg throughput | ~8,000 tokens/sec/GPU |
| B300 + wideEP + disagg + MTP throughput | ~14,000 tokens/sec/GPU |
| Software-only throughput gain | ~14x |
| Optimized GB300 NVL72 vs best H100 config | ~17x in FP8, ~32x in FP4 |
