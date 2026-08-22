# Announcing AA-AnalystAgent：面向真实电子表格与文档定量分析的 Agent 基准

> 发布账号：Artificial Analysis（[@ArtificialAnlys](https://x.com/ArtificialAnlys)）  
> 原帖时间：2026 年 8 月 11 日 22:23  
> 整理说明：以下包含原帖，以及同一线程内由 **@ArtificialAnlys** 发布的五条官方评论；未纳入其他账号的回复。

---

## 原帖

Announcing AA-AnalystAgent, our new agentic benchmark for quantitative analysis on real-world spreadsheets & documents. Claude Opus 5 leads at 54%, followed by GPT-5.5 at 50% and Claude Fable 5 at 49%.

In real analyst roles, professional judgment and expertise are as important raw quantitative capabilities. AA-AnalystAgent tests this and requires models to interpret sources, decide which exceptions and caveats apply, and settle on a methodology to successfully complete a task.

Because handing analyst tasks to agents requires not just correct answers but consistent ones, AA-AnalystAgent runs each task five times and reports pass^5 as its headline metric (we call this ‘pass-all-5’). pass^5 means models must get a task correct every time it tries across five independent attempts to pass.

AA-AnalystAgent overview:

- 80 questions across 14 business and scientific domains, including healthcare expenditure reports, trade and commodity statistics, hydrology and weather data, government appropriations, energy cost models, financial models, environmental reporting, and project schedules.
- Five workflow buckets from across real analyst work: source lookup and diagnosis, filter and total, ratios/trends/sensitivities, P&L modeling, and cash/balance sheet/valuation modeling.

Methodology details:

- **Agentic harness**: each task is solved by an agent running in our open-source Stirrup reference harness, with tools for code execution, web fetch, image viewing, and answer submission.
- **Scoring**: each task is run five times per model, with final answers compared to reference solutions by an equality checker. Three metrics: pass^5, pass@1 (average pass rate), pass@5.
- **Privately-held question set** to limit contamination risk. Two example questions from California Medicaid expenditure reports are publicly shown on the methodology page with full prompt and source material.

Key findings:

- [@AnthropicAI](https://x.com/AnthropicAI)’s Claude Opus 5 (max) leads at 54%, followed by [@OpenAI](https://x.com/OpenAI)’s GPT-5.5 (xhigh) at 50% and Claude Fable 5 (max, Opus 4.8 Fallback) at 49%. Anthropic holds three of the top five places, and the top three are separated by three net tasks out of 80.
- Reliability separates the top of the leaderboard more than raw capability: GPT-5.5 (xhigh) has the highest pass@1, but Opus 5 leads on pass^5 because it repeats what it gets right.
- Committing early to a wrong interpretation is the most widespread way models fail, appearing in 57% of the failures we classified.
- The price of a given score varies enormously: Claude Sonnet 4.6 and [@Xiaomi](https://x.com/Xiaomi)’s MiMo-V2.5-Pro both score 20%, at $1.34 and $0.05 per task.
- [@Kimi_Moonshot](https://x.com/Kimi_Moonshot)’s Kimi K3 (max) is the top open weights model at 39%, 15 points behind the closed frontier.

AA-AnalystAgent launches as a standalone leaderboard and is not part of the Artificial Analysis Intelligence Index. See below for further detail.

## 官方评论 1：可靠性

> 原评论：https://x.com/ArtificialAnlys/status/2087303973137252502

Reliability separates the top of the AA-AnalystAgent leaderboard more than raw capability. GPT-5.5 (xhigh) has the highest pass@1 at 66%, with Gemini 3.1 Pro Preview and Claude Opus 5 (max) close behind at 64%, but Opus 5 leads on pass^5 (we call this ‘pass-all-5’) because it repeats its correct workflows each time.

[@GoogleDeepMind](https://x.com/GoogleDeepMind)’s Gemini 3.1 Pro Preview solves 81% of tasks at least once but only 41% on all five, and finishes ninth. An analyst agent is useful if its answers hold up without re-checking — an answer that is right at random still has to be verified, which is the work the agent was meant to remove.

## 官方评论 2：失败模式

> 原评论：https://x.com/ArtificialAnlys/status/2087303975628579271

Failure analysis: We classified 1,567 failing AA-AnalystAgent attempts across ten leading models into seven failure modes, tagging each attempt with every mode it exhibited. The most widespread is anchoring on a wrong early hypothesis, present in 57% of failures. Models commit to a source or interpretation early and defend it for the rest of the trajectory.

The sharpest contrasts are in how models treat sources. Gemini 3.1 Pro Preview takes sources at their word but struggles with execution. It sits below the ten-model median on both misreading domain terms and overriding evidence in favor of a generic prior, while posting above-median rates of modeling, scaling and aggregation errors (51% of its failures) and skipped verification (39%).

[@SpaceXAI](https://x.com/SpaceXAI)’s Grok 4.5 (high) is the reverse. It understands the field’s language, then substitutes its own assumptions for what the documents say, misreading domain terms on 23% of its failures against a 38% median, while overriding evidence on 54% against a 43% median. Kimi K3 (max) misreads on 48%, 25 points clear of Grok 4.5.

## 官方评论 3：得分与单任务成本

> 原评论：https://x.com/ArtificialAnlys/status/2087303978677891289

Score vs Cost per Task: The price of a given score varies enormously on AA-AnalystAgent. Claude Sonnet 4.6 (max) and MiMo-V2.5-Pro both score 20%, at $1.34 and $0.05 per task. The same holds at the top, where Claude Opus 4.7 (max) is the most expensive model to run at $1.98 per task and places eighth, while GPT-5.5 (xhigh) runs it for $1.15 and places second. The Flash tier is not automatically the cheaper option either, with Gemini 3.5 Flash (high) at $1.79 against Gemini 3.1 Pro Preview at $0.80.

## 官方评论 4：开放权重模型表现

> 原评论：https://x.com/ArtificialAnlys/status/2087303981001523638

Open weights models performance: Kimi K3 (max) is the top open weights model on AA-AnalystAgent at launch, scoring 39%, 15 points behind the closed frontier and ahead of the eight other open weights models tested. The next open weights model is [@deepseek_ai](https://x.com/deepseek_ai)’s DeepSeek V4 Flash (Reasoning, Max Effort) at 25%, so the spread inside the open weights field is currently wider than the gap from its leader to the frontier.

## 官方评论 5：榜单、方法与参考 Harness

> 原评论包含链接，见原帖线程。

Explore the leaderboard and full methodology: [artificialanalysis.ai/evaluations/aa-analyst-agent](https://artificialanalysis.ai/evaluations/aa-analyst-agent)

Stirrup, the open-source agent harness used for AA-AnalystAgent tasks, is on GitHub: [github.com/ArtificialAnalysis/stirrup](https://github.com/ArtificialAnalysis/stirrup)

---

## 原帖链接

https://x.com/ArtificialAnlys/status/2087303970725499361
