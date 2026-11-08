# How Much Does Reasoning Effort Affect Score and Cost?

[原文链接](https://www.vals.ai/blogs/reasoning-effort)

Most frontier models let you choose how hard they think when you ask a question, but the higher settings increase the cost per run. By default, we generally run models on their highest setting. In this post, we measure how performance and cost change across reasoning levels. At their lowest setting, four of the seven models kept at least 80% of their Vals Index score for half the cost or less. Claude Opus 5.5, for example, kept 80% of its score for 16% of the cost.

We tested the top model from each of seven AI labs on the eight benchmarks in the Vals Index. Each model ran at three settings: its lowest reasoning setting, a middle one, and the setting our leaderboard runs use, usually its highest. In this post, we refer to the last one as the leaderboard setting. The chart below shows all three settings on the Vals Index, starting with four models, and the model legend adds the rest. The same chart is on the [Vals Index page](/benchmarks/vals_index) and on each of its benchmark pages.

**Reasoning Effort Score at each model's lowest, middle and leaderboard setting Vals Index • Oct 27, 2026**

![原文图表 1](https://private-us-east-1.manuscdn.com/sessionFile/Tbuy55iC9XHL4KZ0e5aApk/sandbox/bdsTOrHUpXYRgKdvgNJ7Kt-images_1794146838787_na1fn_L2hvbWUvdWJ1bnR1L21hcmtkb3duXzIwMjYtMTEtMDgvMDVfYXNzZXRzLzA1X2NoYXJ0XzFfMQ.svg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvVGJ1eTU1aUM5WEhMNEtaMGU1YUFway9zYW5kYm94L2Jkc1RPckhVcFhZUmdLZHZnTko3S3QtaW1hZ2VzXzE3OTQxNDY4Mzg3ODdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyMWhjbXRrYjNkdVh6SXdNall0TVRFdE1EZ3ZNRFZmWVhOelpYUnpMekExWDJOb1lYSjBYekZmTVEuc3ZnIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk2MDgzMjAwfX19XX0_&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEQCIA17WvtkiYiuong5zyzsKmultc3sn9OFlhdzcbbzcf-3AiBRawvKYCmEKWVlVkO5rNACmBZj4qrotFr~7kcO4LBcVg__)

Index costs include Code Migration. Error bars show ±1 standard error.

## Key Takeaways

* Lowering reasoning effort reduces cost much more than it reduces score. At their lowest setting, four of the seven models kept at least 80% of their score for half the cost or less.
* In 22 of the 56 combinations of a model and a benchmark, a lower setting scored as high as the leaderboard setting at lower cost. In those cases, the leaderboard setting cost more without scoring higher.
* Even with perfect hindsight, picking the highest-scoring setting for each task adds only 6.0 points. It also costs more than using the lowest setting everywhere, at 64% of the leaderboard cost against 29%.

## Lowering reasoning effort reduces cost much more than score

**Score kept and cost paid Vals Index score and cost at a lower setting, as a percentage of each model's leaderboard setting**

Lowest setting

| Model / setting | Score, % of leaderboard setting | Cost, % of leaderboard setting |
| --- | --- | --- |
| Gemini 4 Argon low vs high | 99% | 84% |
| DeepSeek V4.1 Flash low vs max | 89% | 50% |
| GPT-6 Astra low vs max | 88% | 18% |
| Grok 4.7 low vs xhigh | 86% | 16% |
| GLM-5.3 low vs max | 81% | 53% |
| Opus 5.5 low vs max | 80% | 16% |
| Muse Spark 1.3 minimal vs xhigh | 77% | 29% |

The dashed line marks the leaderboard setting. A bar at 100% has the same score or cost as that setting.

At the lowest setting, four of the seven models kept at least 80% of their Vals Index score for half the cost or less. [Claude Opus 5.5](/models/anthropic_claude-opus-5-5) kept 80% of its score at 16% of the cost, and [Grok 4.7](/models/grok_grok-4.7) kept 86% at 16%. [Gemini 4 Argon](/models/google_gemini-4-argon) kept 99% of its score at 84% of the cost. At the middle setting, [Gemini 4 Argon](/models/google_gemini-4-argon) scored slightly above its leaderboard setting at 78% of the cost, which is cheaper than its own lowest setting.

## In 22 of 56 cases, a lower setting scored as high at lower cost

In 22 of the 56 model-and-benchmark pairs, a cheaper setting scored as high as the leaderboard setting. Of the cheaper settings we tested, none scored significantly higher than the leaderboard setting, and 33 scored significantly lower. On the Vals Index as a whole, no model matched its leaderboard score at its lowest setting.

**Score change and cost at a lower setting Vals Index, each model's lower setting against its leaderboard setting. Click a model for its eight benchmarks**

![原文图表 3](https://private-us-east-1.manuscdn.com/sessionFile/Tbuy55iC9XHL4KZ0e5aApk/sandbox/bdsTOrHUpXYRgKdvgNJ7Kt-images_1794146838787_na1fn_L2hvbWUvdWJ1bnR1L21hcmtkb3duXzIwMjYtMTEtMDgvMDVfYXNzZXRzLzA1X2NoYXJ0XzNfMQ.svg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvVGJ1eTU1aUM5WEhMNEtaMGU1YUFway9zYW5kYm94L2Jkc1RPckhVcFhZUmdLZHZnTko3S3QtaW1hZ2VzXzE3OTQxNDY4Mzg3ODdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyMWhjbXRrYjNkdVh6SXdNall0TVRFdE1EZ3ZNRFZmWVhOelpYUnpMekExWDJOb1lYSjBYek5mTVEuc3ZnIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk2MDgzMjAwfX19XX0_&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEQCIGzqGPEhuPGD56vASFu-99HXPntwc0pVzEFnNkY0rAgaAiBMfUoOy9DUK4qYRaBM6f3B5DQMFbIvOx7LrPRisKIBAA__)

On the Vals Index, 0 of 7 models scored as high as the leaderboard setting, at lower cost, with their lowest setting. Across both settings and all benchmarks, a lower setting scored as high at lower cost in 22 cases, none significantly different from the leaderboard setting.

## Picking the highest-scoring setting for each task adds only 6.0 points

With hindsight, the models gained a median 6.0 points over their leaderboard setting, at a median 64% of the cost. A real system must choose before it sees the results, so its gain would be smaller.

Some tasks need more reasoning than others, so a system that picked a setting for each task could beat any single setting. To find the most any such system could gain, we looked back at our results and, for each task, chose the cheapest setting that got the best score.

**Score and cost when each task gets its highest-scoring setting Average over the eight benchmarks, against each model's leaderboard setting**

| Model | Leaderboard → best per task | Cost, % of leaderboard cost |
| --- | --- | --- |
| Gemini 4 Argon | 59.8 → 67.6 | 84% |
| DeepSeek V4.1 Flash | 51.5 → 57.4 | 62% |
| GPT-6 Astra | 54.7 → 59.6 | 64% |
| Grok 4.7 | 50.6 → 56.4 | 55% |
| GLM-5.3 | 52.1 → 59.9 | 76% |
| Opus 5.5 | 60.6 → 66.6 | 50% |
| Muse Spark 1.3 | 47.5 → 55.4 | 80% |

This chart uses each task's results to pick its highest-scoring setting. A system that chooses before seeing those results would score lower. The score axis starts at 40.

## More reasoning helped some benchmarks far more than others

The score increase from the lowest setting to the highest varied by benchmark. Legal Research had a median increase of 19.2 points. EMB, HLAB and Finance Agent 2.1 each increased by less than 6 points.

**Score gained from more reasoning, by benchmark Each dot is one model: its score at the highest setting minus its score at the lowest, in points**

| Benchmark | Model | Score change, highest minus lowest | Median |
| --- | --- | --- | --- |
| Legal Research | DeepSeek V4.1 Flash | +11.5 | +19.2 |
| Legal Research | Grok 4.7 | +19.2 | +19.2 |
| Legal Research | Muse Spark 1.3 | +20.2 | +19.2 |
| Legal Research | GPT-6 Astra | +12.5 | +19.2 |
| Legal Research | Opus 5.5 | +27.9 | +19.2 |
| Legal Research | GLM-5.3 | +31.7 | +19.2 |
| Legal Research | Gemini 4 Argon | +2.9 | +19.2 |
| Code Migration 1.1 | DeepSeek V4.1 Flash | -3.3 | +15.6 |
| Code Migration 1.1 | Grok 4.7 | +15.6 | +15.6 |
| Code Migration 1.1 | Muse Spark 1.3 | +15.7 | +15.6 |
| Code Migration 1.1 | GPT-6 Astra | +28.7 | +15.6 |
| Code Migration 1.1 | Opus 5.5 | +21.1 | +15.6 |
| Code Migration 1.1 | GLM-5.3 | +12.3 | +15.6 |
| Code Migration 1.1 | Gemini 4 Argon | -1.8 | +15.6 |
| Terminal-Bench 4 | DeepSeek V4.1 Flash | +19.2 | +12.1 |
| Terminal-Bench 4 | Grok 4.7 | +16.2 | +12.1 |
| Terminal-Bench 4 | Muse Spark 1.3 | +7.1 | +12.1 |
| Terminal-Bench 4 | GPT-6 Astra | +12.1 | +12.1 |
| Terminal-Bench 4 | Opus 5.5 | +28.3 | +12.1 |
| Terminal-Bench 4 | GLM-5.3 | +4 | +12.1 |
| Terminal-Bench 4 | Gemini 4 Argon | +3 | +12.1 |
| Tax Agent Bench | DeepSeek V4.1 Flash | +16.6 | +11.5 |
| Tax Agent Bench | Grok 4.7 | +11.5 | +11.5 |
| Tax Agent Bench | Muse Spark 1.3 | +7.8 | +11.5 |
| Tax Agent Bench | GPT-6 Astra | +5.2 | +11.5 |
| Tax Agent Bench | Opus 5.5 | +22.8 | +11.5 |
| Tax Agent Bench | GLM-5.3 | +33 | +11.5 |
| Tax Agent Bench | Gemini 4 Argon | +4.2 | +11.5 |
| Vibe Code Bench | DeepSeek V4.1 Flash | +10.6 | +10.6 |
| Vibe Code Bench | Grok 4.7 | +20 | +10.6 |
| Vibe Code Bench | Muse Spark 1.3 | +16.6 | +10.6 |
| Vibe Code Bench | GPT-6 Astra | +7.6 | +10.6 |
| Vibe Code Bench | Opus 5.5 | +5.6 | +10.6 |
| Vibe Code Bench | GLM-5.3 | +19.7 | +10.6 |
| Vibe Code Bench | Gemini 4 Argon | +1.3 | +10.6 |
| Finance Agent 2.1 | DeepSeek V4.1 Flash | +5 | +5.0 |
| Finance Agent 2.1 | Grok 4.7 | +1 | +5.0 |
| Finance Agent 2.1 | Muse Spark 1.3 | +5.8 | +5.0 |
| Finance Agent 2.1 | GPT-6 Astra | +2.8 | +5.0 |
| Finance Agent 2.1 | Opus 5.5 | +15.9 | +5.0 |
| Finance Agent 2.1 | GLM-5.3 | +13.2 | +5.0 |
| Finance Agent 2.1 | Gemini 4 Argon | -0.2 | +5.0 |
| HLAB 1.1 | DeepSeek V4.1 Flash | 0 | +3.3 |
| HLAB 1.1 | Grok 4.7 | +5.8 | +3.3 |
| HLAB 1.1 | Muse Spark 1.3 | +24.2 | +3.3 |
| HLAB 1.1 | GPT-6 Astra | +3.3 | +3.3 |
| HLAB 1.1 | Opus 5.5 | +2.5 | +3.3 |
| HLAB 1.1 | GLM-5.3 | +3.3 | +3.3 |
| HLAB 1.1 | Gemini 4 Argon | -1.7 | +3.3 |
| EMB 1.1 | DeepSeek V4.1 Flash | +4.3 | +3.3 |
| EMB 1.1 | Grok 4.7 | +2.3 | +3.3 |
| EMB 1.1 | Muse Spark 1.3 | +16.6 | +3.3 |
| EMB 1.1 | GPT-6 Astra | +0.6 | +3.3 |
| EMB 1.1 | Opus 5.5 | +3.3 | +3.3 |
| EMB 1.1 | GLM-5.3 | +5.8 | +3.3 |
| EMB 1.1 | Gemini 4 Argon | +0.3 | +3.3 |

## Methodology

We ran [DeepSeek V4.1 Flash](/models/deepseek_deepseek-v4.1-flash), [Grok 4.7](/models/grok_grok-4.7), [Muse Spark 1.3](/models/meta_muse_spark_1_3), [GPT-6 Astra](/models/openai_gpt-6-astra), [Claude Opus 5.5](/models/anthropic_claude-opus-5-5), [GLM 5.3](/models/zai_glm-5.3) and [Gemini 4 Argon](/models/google_gemini-4-argon), each at its lowest reasoning setting, a middle setting and its leaderboard setting. The leaderboard setting is max for DeepSeek, Astra, Opus and GLM, and xhigh for Grok and Muse. Gemini’s leaderboard runs set no effort level, so we used its high setting. We ran them on the eight benchmarks that make up the Vals Index: Finance Agent 2.1, EMB 1.1, Terminal-Bench 4, Vibe Code Bench, Code Migration 1.1, Legal Research, HLAB 1.1 and Tax Agent Bench.

Every setting ran on the same fixed subset of each benchmark, about half the tasks. We chose each subset so that it ranks the models in the same order as the full benchmark. For most models, the leaderboard-setting score is the run already on our leaderboard, rescored on that subset. Where no such run existed, including all of Gemini’s, we ran the leaderboard setting fresh.

The Vals Index is a single measure of AI’s potential economic impact. It measures agentic model performance across finance, coding, legal and tax tasks, weighted by each sector’s share of U.S. GDP. A model appears in the Index only when all eight benchmarks have a score. Tax Agent Bench is scored all-pass, as in its main table. Cost per test is at list price. Vals Index cost is the plain mean of the eight benchmarks’ costs, with Code Migration estimated from tokens. Each comparison uses a paired bootstrap test, which resamples the same tasks for both settings to judge whether a score difference is likely real. We ran every comparison in a group before checking which setting scored higher, then adjusted the p-values across each group with the Benjamini–Hochberg method. A result counts as significant when its adjusted p-value is below 0.05. To pick each task’s highest-scoring setting, we take the cheapest setting with the highest score on that task, then compare plain averages over the eight benchmarks.

## Limitations

* Scores are on half the tasks, so each is noisier than the published number, and most benchmarks have one run per setting.
* No significant difference does not mean the scores are equal. With about half the tasks per benchmark, our test can miss a small real difference between two settings.
* Most leaderboard-setting runs are from earlier months and the other settings from October, so provider-side changes in between could affect the comparison.
* We picked each task’s highest-scoring setting from that task’s own results, so the 6.0-point gain is an upper bound on what a real system could achieve.
