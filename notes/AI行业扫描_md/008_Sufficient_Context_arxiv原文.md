---
url: https://arxiv.org/abs/2411.06037v3
title: "Sufficient Context: A New Lens on Retrieval Augmented Generation Systems"
description: "Abstract page for arXiv paper 2411.06037v3: Sufficient Context: A New Lens on Retrieval Augmented Generation Systems"
captured_at: "2026-03-09T03:05:14.377Z"
---

# Sufficient Context: A New Lens on Retrieval Augmented Generation Systems

[View PDF](https://arxiv.org/pdf/2411.06037v3) [HTML (experimental)](https://arxiv.org/html/2411.06037v3)

> Abstract:Augmenting LLMs with context leads to improved performance across many applications. Despite much research on Retrieval Augmented Generation (RAG) systems, an open question is whether errors arise because LLMs fail to utilize the context from retrieval or the context itself is insufficient to answer the query. To shed light on this, we develop a new notion of sufficient context, along with a method to classify instances that have enough information to answer the query. We then use sufficient context to analyze several models and datasets. By stratifying errors based on context sufficiency, we find that larger models with higher baseline performance (Gemini 1.5 Pro, GPT 4o, Claude 3.5) excel at answering queries when the context is sufficient, but often output incorrect answers instead of abstaining when the context is not. On the other hand, smaller models with lower baseline performance (Mistral 3, Gemma 2) hallucinate or abstain often, even with sufficient context. We further categorize cases when the context is useful, and improves accuracy, even though it does not fully answer the query and the model errs without the context. Building on our findings, we explore ways to reduce hallucinations in RAG systems, including a new selective generation method that leverages sufficient context information for guided abstention. Our method improves the fraction of correct answers among times where the model responds by 2--10\\% for Gemini, GPT, and Gemma. Key findings and the prompts used in our autorater analysis are available on our github.

<table summary="Additional metadata"><tbody><tr><td>Subjects:</td><td><span>Computation and Language (cs.CL)</span></td></tr><tr><td>Cite as:</td><td><span><a href="https://arxiv.org/abs/2411.06037">arXiv:2411.06037</a> [cs.CL]</span></td></tr><tr><td>&nbsp;</td><td>(or <span><a href="https://arxiv.org/abs/2411.06037v3">arXiv:2411.06037v3</a> [cs.CL]</span> for this version)</td></tr><tr><td>&nbsp;</td><td><a href="https://doi.org/10.48550/arXiv.2411.06037" id="arxiv-doi-link">https://doi.org/10.48550/arXiv.2411.06037</a><div><p><span></span>arXiv-issued DOI via DataCite</p></div></td></tr></tbody></table>

## Submission history

From: Hailey Joren \[[view email](https://arxiv.org/show-email/b075b949/2411.06037)\]
**[\[v1\]](https://arxiv.org/abs/2411.06037v1)** Sat, 9 Nov 2024 02:13:14 UTC (11,771 KB)
**[\[v2\]](https://arxiv.org/abs/2411.06037v2)** Sat, 7 Dec 2024 04:06:41 UTC (11,743 KB)
**\[v3\]** Wed, 23 Apr 2025 03:07:14 UTC (11,743 KB)