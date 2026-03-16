---
url: https://arxiv.org/abs/2210.00720
title: "Complexity-Based Prompting for Multi-Step Reasoning"
description: "Abstract page for arXiv paper 2210.00720: Complexity-Based Prompting for Multi-Step Reasoning"
captured_at: "2026-03-08T10:13:18.470Z"
---

# Complexity-Based Prompting for Multi-Step Reasoning

[View PDF](https://arxiv.org/pdf/2210.00720)

> Abstract:We study the task of prompting large-scale language models to perform multi-step reasoning. Existing work shows that when prompted with a chain of thoughts (CoT), sequences of short sentences describing intermediate reasoning steps towards a final answer, large language models can generate new reasoning chains and predict answers for new inputs. A central question is which reasoning examples make the most effective prompts. In this work, we propose complexity-based prompting, a simple and effective example selection scheme for multi-step reasoning. We show that prompts with higher reasoning complexity, i.e., chains with more reasoning steps, achieve substantially better performance on multi-step reasoning tasks over strong baselines. We further extend our complexity-based criteria from prompting (selecting inputs) to decoding (selecting outputs), where we sample multiple reasoning chains from the model, then choose the majority of generated answers from complex reasoning chains (over simple chains). When used to prompt GPT-3 and Codex, our approach substantially improves multi-step reasoning accuracy and achieves new state-of-the-art (SOTA) performance on three math benchmarks (GSM8K, MultiArith, and MathQA) and two BigBenchHard tasks (Date Understanding and Penguins), with an average +5.3 and up to +18 accuracy improvements. Compared with existing example selection schemes like manual tuning or retrieval-based selection, selection based on reasoning complexity is intuitive, easy to implement, and annotation-efficient. Further results demonstrate the robustness of performance gains from complex prompts under format perturbation and distribution shift.

<table summary="Additional metadata"><tbody><tr><td>Comments:</td><td>Preprint</td></tr><tr><td>Subjects:</td><td><span>Computation and Language (cs.CL)</span>; Artificial Intelligence (cs.AI); Machine Learning (cs.LG)</td></tr><tr><td>Cite as:</td><td><span><a href="https://arxiv.org/abs/2210.00720">arXiv:2210.00720</a> [cs.CL]</span></td></tr><tr><td>&nbsp;</td><td>(or <span><a href="https://arxiv.org/abs/2210.00720v2">arXiv:2210.00720v2</a> [cs.CL]</span> for this version)</td></tr><tr><td>&nbsp;</td><td><a href="https://doi.org/10.48550/arXiv.2210.00720" id="arxiv-doi-link">https://doi.org/10.48550/arXiv.2210.00720</a><div><p><span></span>arXiv-issued DOI via DataCite</p></div></td></tr></tbody></table>

## Submission history

From: Yao Fu \[[view email](https://arxiv.org/show-email/42f4d370/2210.00720)\]
**[\[v1\]](https://arxiv.org/abs/2210.00720v1)** Mon, 3 Oct 2022 05:33:27 UTC (367 KB)
**\[v2\]** Mon, 30 Jan 2023 09:15:49 UTC (275 KB)