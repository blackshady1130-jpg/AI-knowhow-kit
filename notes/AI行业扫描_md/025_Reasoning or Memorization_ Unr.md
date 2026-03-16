---
url: https://arxiv.org/abs/2507.10532
title: "Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination"
description: "Abstract page for arXiv paper 2507.10532: Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination"
captured_at: "2026-03-09T03:13:28.334Z"
---

# Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination

Authors:[Mingqi Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+M), [Zhihao Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Z), [Qiaole Dong](https://arxiv.org/search/cs?searchtype=author&query=Dong,+Q), [Zhiheng Xi](https://arxiv.org/search/cs?searchtype=author&query=Xi,+Z), [Jun Zhao](https://arxiv.org/search/cs?searchtype=author&query=Zhao,+J), [Senjie Jin](https://arxiv.org/search/cs?searchtype=author&query=Jin,+S), [Xiaoran Fan](https://arxiv.org/search/cs?searchtype=author&query=Fan,+X), [Yuhao Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+Y), [Huijie Lv](https://arxiv.org/search/cs?searchtype=author&query=Lv,+H), [Ming Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+M), [Yanwei Fu](https://arxiv.org/search/cs?searchtype=author&query=Fu,+Y), [Qin Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+Q), [Songyang Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+S), [Qi Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Q)

[View PDF](https://arxiv.org/pdf/2507.10532) [HTML (experimental)](https://arxiv.org/html/2507.10532v3)

> Abstract:Reasoning in large language models has long been a central research focus, and recent studies employing reinforcement learning (RL) have introduced diverse methods that yield substantial performance gains with minimal or even no external supervision. Surprisingly, some studies even suggest that random or incorrect reward signals can enhance performance. However, these breakthroughs are predominantly observed for the mathematically strong Qwen2.5 series on benchmarks such as MATH-500, AMC, and AIME, and seldom transfer to models like Llama, which warrants a more in-depth investigation. In this work, our empirical analysis reveals that pre-training on massive web-scale corpora leaves Qwen2.5 susceptible to data contamination in widely used benchmarks. Consequently, conclusions derived from contaminated benchmarks on Qwen2.5 series may be unreliable. To obtain trustworthy evaluation results, we introduce a generator that creates fully clean arithmetic problems of arbitrary length and difficulty, dubbed RandomCalculation. Using this leakage-free dataset, we show that only accurate reward signals yield steady improvements that surpass the base model's performance boundary in mathematical reasoning, whereas random or incorrect rewards do not. Moreover, we conduct more fine-grained analyses to elucidate the factors underlying the different performance observed on the MATH-500 and RandomCalculation benchmarks. Consequently, we recommend that future studies evaluate models on uncontaminated benchmarks and, when feasible, test various model series to ensure trustworthy conclusions about RL and related methods.

<table summary="Additional metadata"><tbody><tr><td>Comments:</td><td>28 pages, AAAI 2026</td></tr><tr><td>Subjects:</td><td><span>Machine Learning (cs.LG)</span>; Artificial Intelligence (cs.AI); Computation and Language (cs.CL)</td></tr><tr><td>Cite as:</td><td><span><a href="https://arxiv.org/abs/2507.10532">arXiv:2507.10532</a> [cs.LG]</span></td></tr><tr><td>&nbsp;</td><td>(or <span><a href="https://arxiv.org/abs/2507.10532v3">arXiv:2507.10532v3</a> [cs.LG]</span> for this version)</td></tr><tr><td>&nbsp;</td><td><a href="https://doi.org/10.48550/arXiv.2507.10532" id="arxiv-doi-link">https://doi.org/10.48550/arXiv.2507.10532</a><div><p><span></span>arXiv-issued DOI via DataCite</p></div></td></tr></tbody></table>

## Submission history

From: Mingqi Wu \[[view email](https://arxiv.org/show-email/75cab1a5/2507.10532)\]
**[\[v1\]](https://arxiv.org/abs/2507.10532v1)** Mon, 14 Jul 2025 17:55:15 UTC (238 KB)
**[\[v2\]](https://arxiv.org/abs/2507.10532v2)** Tue, 5 Aug 2025 14:47:50 UTC (254 KB)
**\[v3\]** Wed, 17 Dec 2025 03:04:24 UTC (225 KB)