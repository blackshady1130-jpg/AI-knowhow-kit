# Artificial Analysis 发布了首个编码智能体综合基准指数（Coding Agent Index）

> 来源：https://artificialanalysis.ai/agents/coding-agents

Artificial Analysis

Artificial Analysis

* Models
* Coding Agents
* Speech, Image, Video
* Hardware
* Leaderboards
* About

* AI Trends

* Arenas

 K [](https://x.com/ArtificialAnlys) [](https://www.linkedin.com/company/artificial-analysis/) [](https://www.xiaohongshu.com/user/profile/69ea6345000000000d034c02)

# Artificial Analysis Coding Agent Benchmarks

We measure real-world performance of coding agents on software engineering tasks, including cost, token usage, and execution time. We compare how performance changes across agents, models, and execution settings.

To compare language models see our model benchmarks .

Benchmarks Features Overview

## Artificial Analysis Coding Agent Index

Composite index of 3 benchmarks:

* SWE-Bench-Pro-Hard-AA
  
  Code generation, 150 questions
  
  [By Scale AI](https://scale.com/leaderboard/swe_bench_pro_public)
* Terminal-Bench v2
  
  Agentic terminal use, 84 questions
  
  [By Laude Institute](https://www.tbench.ai/benchmarks/terminal-bench-2)
* SWE-Atlas-QnA
  
  Technical Q&A, 124 questions
  
  [By Scale AI](https://labs.scale.com/leaderboard/sweatlas-qna)

Index represents the average pass@1 across 3 runs of each benchmark. View methodology

Coding Agents General Work Chatbots Presentations OCR Data Analysis Customer Support

Highlights

### Coding Agent Index

Artificial Analysis Coding Agent Index · Higher is better

### Time per Task

Mean agent wall time per task · Lower is better

### Cost per Task

Mean API cost per task (USD) · Lower is better

Performance Harness Comparison Token Usage Cost Execution Time

## Performance

Performance across the Artificial Analysis Coding Agent Index.

Index Score by Benchmark SWE-Atlas-QnA SWE-Bench-Pro-Hard-AA Terminal-Bench v2

### Artificial Analysis Coding Agent Index

Composite average pass@1 across SWE-Bench-Pro-Hard-AA, Terminal-Bench v2, and SWE-Atlas-QnA · Higher is better

Color by

Model Agent

10 of 13 models

### What this metric means

The Artificial Analysis Coding Agent Index is a composite score built from SWE-Bench-Pro-Hard-AA, Terminal-Bench v2, and SWE-Atlas-QnA.

It is useful for quick comparison, but it should be read alongside the per-eval breakdowns. Two agents with similar index values can still have different strengths across repository tasks, terminal workflows, and rubric-based evaluations.

## Harness Comparison

Artificial Analysis Coding Agent Index by harness for Claude Opus 4.7.

Artificial Analysis Coding Agent Index SWE-Atlas-QnA SWE-Bench-Pro-Hard-AA Terminal-Bench v2

### Harness Comparison: Artificial Analysis Coding Agent Index

Composite average pass@1 across Claude Code and Cursor CLI for Claude Opus 4.7 · Higher is better

### What this chart shows

This chart holds the underlying model constant at Claude Opus 4.7 and compares how it performs between Cursor and Claude Code.

## Token Usage

Token consumption across the Artificial Analysis Coding Agent Index, including total usage, token mix, efficiency, and per-benchmark breakdowns.

Token Usage Token Distribution Index vs. Tokens Cache Hit Rate Input vs. Output Tokens by Benchmark

### Token Usage per Task

Mean input, cache, and output tokens per task

10 of 13 models

Input Cached Input Output

Prompt cache hit rates can vary significantly by provider routing, which can materially change effective cost.

### Input tokens

Non-cached input tokens sent to the model, including prompts, instructions, tool context, and task context that were not served from prompt cache.

### Cached input tokens

Reused prompt tokens billed through provider prompt caching when that telemetry is available, rather than being processed as a fully fresh input each time.

### Why cache usage varies

Some providers route repeated requests across different backend replicas. When prompt cache state is not shared consistently across those replicas, a model may receive fewer cache hits even when the benchmark task flow is otherwise identical.

We do not add custom relay headers or provider-specific affinity controls to force higher cache reuse, because that would make the benchmark less representative of a typical user setup. As a result, reported costs reflect the cache behavior observed through the configured provider path, not an optimized best-case cache scenario.

### Output tokens

Tokens returned by the model in its visible response during the task.

## Cost

Cost across the Artificial Analysis Coding Agent Index based on current per-token API pricing, including cache write pricing and cache discounts where available. Many users will access coding agent harnesses through subscription plan offerings rather than pay-per-token.

Cost to Run Cost Distribution Index vs. Cost Total Cost

### Cost per Task

Mean pay-per-token API cost per task (USD) · Lower is better

Color by

Model Agent

10 of 13 models

### What cost is measuring

This chart shows the mean pay-per-token API cost per task across the Artificial Analysis Coding Agent Index, which combines SWE-Bench-Pro-Hard-AA, Terminal-Bench v2, and SWE-Atlas-QnA.

Where applicable, that cost model includes standard input pricing, discounted cached-input pricing, separate cache-write charges, and output pricing rather than treating all prompt tokens as if they were billed at the same uncached input rate.

It is intended to show pay-per-token API cost, not consumer plan pricing or the full operational cost of deploying the system in production. Infrastructure, engineering, and supervision costs are not the focus of this metric.

## Execution Time

Active agent runtime across the Artificial Analysis Coding Agent Index.

Execution Time Index vs. Time Turns

### Time per Task

Mean agent wall time per task · Lower is better

Color by

Model Agent

10 of 13 models

### What execution time is measuring

This chart uses agent wall time: how long the agent process was actively running on each task.

It does not include environment startup, verifier or judge time, or other harness overhead, so it is a cleaner comparison of how long the agent itself was working.

## Run Specifications

## Frequently Asked Questions

### What is the Artificial Analysis Coding Agent Index?

The Artificial Analysis Coding Agent Index is our composite score for coding-agent performance across the public benchmark suite on this page. It currently combines SWE-Bench-Pro-Hard-AA, Terminal-Bench v2, and SWE-Atlas-QnA to capture implementation, terminal workflow, and repository-understanding performance in a single headline metric.

### Which benchmarks are included in the index right now?

The current public index includes SWE-Bench-Pro-Hard-AA, Terminal-Bench v2, and SWE-Atlas-QnA. These benchmarks are combined because they stress different parts of the coding-agent workflow rather than repeating the same task format.

### What kinds of tasks are these benchmarks actually testing?

The public benchmark suite mixes several software engineering task styles. Some tasks are Q&A and repository-understanding tasks that focus on reading a codebase, understanding architecture or behavior, and producing a correct technical answer. Some are implementation and bug-fix tasks that require code changes and are closer to the classic make-a-patch-that-works framing. Some are terminal workflow tasks that test whether the agent can navigate a shell-driven environment, execute tools correctly, and complete a multi-step command-line workflow. The suite also mixes effectively binary outcomes with rubric-scored partial-credit outcomes, which matters because an agent can show useful progress on a difficult task without fully solving it.

### How do Q&A-style tasks differ from SWE-Bench-Pro-Hard-AA-style tasks?

Q&A-style tasks emphasize repository understanding, code reading, tracing behavior, and producing a correct technical explanation. SWE-Bench-Pro-Hard-AA-style tasks are closer to shipping a working change: the agent has to understand the task, navigate the repository, edit files correctly, and satisfy an evaluator or test-based outcome under execution constraints. Those are related capabilities, but they are not identical. An agent can be strong at repository reasoning and still be weaker at reliable patch execution, or vice versa, which is one reason the composite index should be interpreted alongside the per-benchmark chart.

### How are agents scored on each benchmark?

The benchmark page reports component scores using average pass@1. This is the evaluator-assigned score for a task, and depending on the benchmark it can be either binary or partial credit. A passed run is not automatically the same thing as a solved task: a run can complete cleanly and still receive a zero score. In the current methodology, a task is counted as solved only when it passed and received a positive score. This matters especially for rubric-scored tasks such as SWE-Atlas-QnA, where partial credit can capture useful progress that would be lost in a strict pass-fail metric.

### How is the overall index weighted?

The index is computed from the configured benchmark components that make up the current public suite. For the current Artificial Analysis Coding Agent Index, the public methodology is a simple average across the available component benchmark scores, and the current configuration treats the included benchmark components as equal components of that composite. Benchmark methodology can evolve as coverage improves, so comparability is best interpreted within the published benchmark suite and its current component set rather than as a timeless absolute score.

### What does execution time mean?

Execution time on this page refers to wall-clock task runtime per task, not just raw model latency. It is meant to reflect the user-facing time cost of running the whole agent workflow. That includes time spent reasoning, issuing tool calls, reading and writing files, executing shell steps, and waiting on model responses. So an agent can have a fast underlying model and still be slower overall if its workflow is longer or more tool-heavy.

### What does token usage mean, and why does it matter?

Token usage is the average observed token consumption per task across the benchmark suite. On this page we break it out into input, cache, and output tokens. Input tokens are the tokens sent into the model, including prompts, instructions, tool context, and task context. Cache tokens are prompt tokens reused through prompt caching when the provider exposes that telemetry. Output tokens are tokens generated by the model in its response. Token usage matters because it often drives cost and can also indicate how much context an agent consumes to get work done, but token efficiency and cost are not identical because providers price token categories differently and caching can materially change the bill.

### Why can a higher-index agent still be worse for my use case?

A higher index score means stronger performance across the included benchmark mix, but it does not mean the agent is best for every workflow. The index is a balance across benchmark quality, not a direct measure of your specific latency, cost, tooling, or task-type priorities. Real-world choice still depends on whether your workflow looks more like repository Q&A, patching, or terminal execution, and on practical constraints such as IDE integration, model availability, and reliability.

### How realistic are these tasks, and what setup was used for each agent?

These benchmarks measure coding-agent performance across repositories, tools, multi-step workflows, and evaluator-based outcomes. Results on this page reflect specific evaluated agent variants, not just generic product names: model choice, settings, and execution configuration can materially change outcomes, which is why a single agent family may appear in multiple variants in the results. For more background on benchmark runs, task-level scoring, and methodology, see the coding-agents benchmarking methodology page. View the coding-agents benchmarking methodology

Artificial Analysis

Subscribe to our newsletter

Email address Subscribe

Artificial Analysis

[X](https://x.com/ArtificialAnlys) [LinkedIn](https://www.linkedin.com/company/artificial-analysis/) [Rednote](https://www.xiaohongshu.com/user/profile/69ea6345000000000d034c02) [Discord](https://discord.gg/Mk298GPZ7V)

Terms of Use Privacy Policy
