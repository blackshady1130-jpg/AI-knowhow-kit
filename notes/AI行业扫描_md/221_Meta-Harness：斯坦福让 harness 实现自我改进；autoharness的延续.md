# Meta-Harness

> 原文链接: https://yoonholee.com/meta-harness/paper.pdf
> 抓取时间: 2026-04

> 说明：原始链接为 PDF；尝试去掉 `.pdf` 的 HTML 地址返回 404。以下正文来自项目主页 [https://yoonholee.com/meta-harness/](https://yoonholee.com/meta-harness/)（与论文同源站点）。论文全文见 [arXiv:2603.28052](https://arxiv.org/abs/2603.28052)。

## Meta-Harness

Best viewed on a desktop browser. Interactive elements use mouse hover, and margin figures need a wide screen.

## TerminalBench-2: Harness Evolution

This is not the run that produced our final reported harness. It is an earlier, smaller search run that we find especially instructive for understanding what Meta-Harness does internally. We deliberately chose a hard 19-task subset where most agents struggle (note the low baseline scores), so that improvements from pure harness changes would be clearly visible. Starting from Terminus-KIRA (28.5%), the search reaches 46.5% by iteration 7.

Step through the iterations to see the proposer's reasoning. It performs counterfactual diagnosis across execution traces, identifies specific failure modes by reading raw logs through the filesystem, and proposes targeted fixes. Each proposal is grounded in concrete evidence from prior runs. Full-benchmark results on all 89 tasks are in the Results section below. Click any dot or use arrow keys to inspect code changes.

← Prev Iteration 1 / 10 Next →

Meta-Harness search loop. (1) An agent reads a filesystem containing all prior candidates' source code, execution traces, and scores, and proposes a new harness. (2) We evaluate the proposed harness on held-out tasks. (3) All logs are stored in the filesystem, and the loop repeats.

## What Makes This Different

There are many methods for optimizing text and code with LLM feedback. The key difference is how much the optimizer gets to see. Most prior methods compress everything into a short summary, a scalar score, or a sliding window of recent candidates. That works for small problems, but harness engineering produces failures that are hard to diagnose without seeing the raw execution trace.

Meta-Harness takes a different approach: it gives the proposer a filesystem containing the full source code, scores, and execution traces of every prior candidate. The proposer is a coding agent (Claude Code) that reads what it needs via `grep`, `cat`, and other standard tools. In practice, this means up to 10M tokens of diagnostic context per step, vs. at most 26K for all prior methods we surveyed. The result is that the proposer can trace a failure back to the specific harness decision that caused it, rather than guessing from a score. See [the paper](https://arxiv.org/abs/2603.28052) for details.

（页面含多列表格对比 Self-Refine、OPRO、TextGrad、MIPRO、AlphaEvolve、GEPA、Feedback Descent、TTT-Discover 与 Meta-Harness 的上下文规模；此处从略，请必要时在浏览器中查看原页。）

Context available per optimization step. Mtok/iter = estimated context per evaluation in each paper's largest setting. Hover a row for details.

## Results

### Text Classification

We follow the online text classification setup of ACE: an LLM receives labeled examples one at a time, updates its memory, and is evaluated on a held-out test set. We search over harnesses using three datasets — LawBench (215 classes), Symptom2Disease (22 classes), and USPTO-50k (180 classes) — with GPT-OSS-120B as the model. We ran 20 evolution iterations with two candidates per iteration, producing 40 candidate harnesses. All test sets are held out until the final evaluation.

The best discovered harness (Label-Primed Query) achieves 48.6% vs. ACE’s 40.9% — a 7.7-point improvement using 4× fewer context tokens. Gains concentrate on tasks with large, confusable label spaces: LawBench (215 classes) sees +16 points, Symptom2Disease +9 points. None of the discovered harnesses require additional LLM calls beyond the main task-solving call.

| Harness | USPTO ↑ | S2D ↑ | Law ↑ | Acc ↑ | Ctx (K) ↓ |
| --- | --- | --- | --- | --- | --- |
| Zero-shot | 12.0 | 63.2 | 7.0 | 27.4 | 0 |
| Few-shot (N=4) | 11.0 | 68.4 | 18.0 | 32.5 | 4.0 |
| Few-shot (N=8) | 14.0 | 67.9 | 21.0 | 34.3 | 8.0 |
| Few-shot (N=16) | 15.0 | 67.0 | 20.0 | 34.0 | 15.4 |
| Few-shot (N=32) | 13.0 | 72.2 | 21.0 | 35.4 | 31.5 |
| Few-shot (all) | 15.0 | 78.3 | 29.0 | 40.8 | 49.3 |
| ACE | 16.0 | 77.8 | 29.0 | 40.9 | 203.0 |
| MCE | 14.0 | 83.0 | 23.0 | 40.0 | 114.0 |
| Meta-Harness (Ours) | 14.0 | 86.8 | 45.0 | 48.6 | 45.5 |

Test accuracy on three text classification benchmarks (GPT-OSS-120B). Ctx = average additional input context (thousands of characters).

We also directly compare Meta-Harness against two representative program-search methods, OpenEvolve and TTT-Discover (with PUCT selection), giving each the same proposer and evaluation budget. Meta-Harness matches their final accuracy with 10× fewer evaluations, and its final accuracy surpasses theirs by more than 10 points. We attribute this to the filesystem-based interface: both OpenEvolve and PUCT compress history into a fixed prompt format, discarding the execution traces that Meta-Harness uses for targeted diagnosis.

Search progress over ~60 proposals. Meta-Harness (red) outperforms all baselines and reaches the next-best optimizer’s final accuracy in just 4 iterations. TTT-Discover, Best-of-N, OpenEvolve, ACE, few-shot, and zero-shot shown for comparison.

### Math Reasoning

We study retrieval-augmented math solving: a language model is given retrieved examples from a large corpus before attempting each problem. Meta-Harness searches over retrieval programs that can implement arbitrary filtering, branching, and formatting logic using corpus metadata and BM25 scores. The corpus contains ≥500K problems drawn from eight open-source datasets. We evolve a single retrieval harness on a 250-problem search set, then evaluate it on 200 held-out IMO-level problems. The same harness is then tested on five models unseen during search, directly measuring transfer.

A single discovered retrieval harness improves accuracy by +4.7 points on average (34.1% → 38.8%) across five held-out models. It matches or exceeds the strongest fixed baselines on average, outperforming BM25 retrieval by 1.3 points overall.

| Method | GPT-5.4n ↑ | GPT-5.4m ↑ | Gem-3.1FL ↑ | Gem-3F ↑ | GPT-20B ↑ | Avg ↑ |
| --- | --- | --- | --- | --- | --- | --- |
| No Retriever | 23.0 | 28.8 | 28.6 | 42.6 | 47.6 | 34.1 |
| Random Few-shot | 23.1 (+0.1) | 24.5 (-4.3) | 31.0 (+2.4) | 40.4 (-2.2) | 41.8 (-5.8) | 32.2 (-1.9) |
| BM25 Retrieval | 30.2 (+7.2) | 29.2 (+0.4) | 32.8 (+4.2) | 46.6 (+4.0) | 48.9 (+1.3) | 37.5 (+3.4) |
| Meta-Harness (Ours) | 31.7 (+8.7) | 30.4 (+1.6) | 34.9 (+6.3) | 46.3 (+3.7) | 50.6 (+3.0) | 38.8 (+4.7) |

Retrieval-augmented math reasoning on 200 IMO-level problems (pass@1, avg. over 3 samples). Absolute improvement over no retriever in parentheses. The discovered Meta-Harness retrieval strategy improves reasoning across all five held-out models, with a 4.7-point average gain.

### Agentic Coding (TerminalBench-2)

TerminalBench-2 evaluates LLM agents on 89 Dockerized tasks spanning code translation, distributed ML setup, systems programming, bioinformatics, and cryptanalysis, with binary pass/fail grading and 5 independent trials per task. These tasks are difficult because they require long-horizon, fully autonomous execution under complex dependencies, truncated terminal outputs, and substantial domain knowledge.

Meta-Harness evolves the full coding harness (system prompts, tool definitions, completion-checking logic, and context management). The proposer reads per-task execution traces (command logs, error messages, timeout behavior) to diagnose failure modes and propose targeted fixes. We initialize search from two strong open baselines, Terminus 2 and Terminus-KIRA.

On Claude Opus 4.6, Meta-Harness achieves 76.4% pass rate, surpassing Terminus-KIRA (74.7%) and ranking #2 among all Opus 4.6 agents. On Claude Haiku 4.5, Meta-Harness achieves 37.6%, outperforming the next-best agent (Goose, 35.5%) and ranking #1 among all Haiku 4.5 agents.

| Claude Opus 4.6 | Pass % |
| --- | --- |
| Claude Code | 58.0 |
| Terminus 2 | 62.9 |
| Mux | 66.5 |
| Factory Droid | 69.9 |
| TongAgents | 71.9 |
| MAYA-V2 | 72.1 |
| Terminus-KIRA | 74.7 |
| Capy | 75.3 |
| Meta-Harness (Ours) | 76.4 |
| ForgeCode | 81.8 |

| Claude Haiku 4.5 | Pass % |
| --- | --- |
| OpenHands | 13.9 |
| Claude Code | 27.5 |
| Terminus 2 | 28.3 |
| Mini-SWE-Agent | 29.8 |
| Terminus-KIRA | 33.7 |
| Goose | 35.5 |
| Meta-Harness (Ours) | 37.6 |

Pass rate on TerminalBench-2. Results for others are from the official leaderboard. Meta-Harness ranks #2 among all Opus 4.6 agents and #1 among all Haiku 4.5 agents.

---

## BibTeX

```
@inproceedings{lee2026metaharness,
  title={Meta-Harness: End-to-End Optimization of Model Harnesses},
  author={Lee, Yoonho and Nair, Roshen and Zhang, Qizheng and Lee, Kangwook and Khattab, Omar and Finn, Chelsea},
  booktitle={Preprint},
  year={2026}
}
```
