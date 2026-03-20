# HLE-Verified: A Systematic Verification and Structured Revision of Humanity's Last Exam

Weiqi Zhai, Zhihai Wang, Jinghang Wang, et al.  
Alibaba Group & Qwen Team, Alibaba Group

## Abstract

Humanity's Last Exam (HLE) has become a widely used benchmark for evaluating frontier large language models on challenging, multi-domain questions. However, subsequent community-led analyses have raised concerns that HLE contains a non-trivial number of noisy items (e.g., ambiguous statements, incorrect answers, or mismatched rationales), which can systematically bias evaluation results and distort cross-model comparisons. To address this challenge, we introduce HLE-Verified, a verified and revised version of HLE accompanied by a transparent, component-wise verification protocol and fine-grained error taxonomy. Our construction follows a two-stage validation-and-repair workflow resulting in a unified certified benchmark. In Stage I, each item is subjected to binary validation on the problem and final answer dimensions, combining domain-expert review and model-based cross-checks. This stage yields 668 items verified as correct. In Stage II, items identified as flawed but fixable are systematically revised under strict constraints that preserve the original evaluation intent, resulting in 1,143 revised-and-certified items. The remaining 689 items are released as a documented uncertain set. We compare the performance of eight state-of-the-art language models on HLE and HLE-Verified, observing an average absolute accuracy gain of 7–10 percentage points on HLE-Verified. The improvement is particularly pronounced on items where the original HLE problem statement and/or reference answer is erroneous: on this subset, the models achieve an average accuracy increase of 30–40 percentage points.

Data: https://huggingface.co/datasets/skylenage/HLE-Verified

## 1 Introduction

As frontier language models continue to advance rapidly, there is increasing demand for evaluation benchmarks that are simultaneously difficult, broad in disciplinary coverage, and resistant to saturation. The Humanity's Last Exam (HLE) has emerged as a widely adopted benchmark for evaluating model performance on challenging questions across mathematics, science, engineering, and the humanities. However, recent independent audits and community-led reviews have highlighted substantial noise in the HLE dataset, including ambiguous or poorly defined question statements, erroneous reference answers, and inconsistencies between rationales and final answers.

To address this reliability challenge, we developed HLE-Verified—a rigorously validated and partially revised version of HLE built under a structured two-stage validation and revision protocol.

### Contributions

- Release of HLE-Verified: 668 verified items, 1,143 revised-and-verified items, and a 689-item documented uncertain set
- A systematic two-stage verification-and-revision framework for post-release benchmark auditing
- Benchmarking of eight state-of-the-art LLMs showing verification materially alters measured performance

## 2 Background

### 2.1 Why benchmark errors matter

Benchmarks serve as the primary measurement interface between model development and scientific claims about capability. Even for small fractions of flawed items, aggregate metrics can be meaningfully distorted, particularly when flawed items are not randomly distributed.

### 2.2 HLE as an evaluation substrate

In practice, HLE is often reduced to a single scalar performance metric. Prior work has demonstrated that large-scale benchmarks may contain systematic annotation errors that meaningfully affect model rankings.

## 3 Dataset Verification Process and Methods

### 3.1 Overview of the pipeline

Starting from the original HLE collection (2,500 items), we construct HLE-Verified through a structured two-stage process:

- **Gold subset (668 items)**: validated without modification
- **Revision subset (1,143 items)**: corrected and re-verified
- **Uncertain subset (689 items)**: items whose validity remains indeterminate

### 3.2 Stage I: component-wise verification

Each item is decomposed into three annotatable components: problem, final answer, and rationale. Multi-source verification integrates external domain-expert screening, model-assisted replication checks (pass@8), and internal expert adjudication.

### 3.3 Stage II: systematic revision and re-verification

Stage II targets items judged flawed but repairable. Revision workflow includes independent supplier repairs (two-track), model-assisted auxiliary proposals, and final expert adjudication.

### 3.5 Component-wise annotation framework and defect taxonomy

A taxonomy comprising 19 categories: 5 problem-level errors, 10 rationale-level errors, and 4 answer-level errors.

## 4 Dataset Statistical Analysis

- Problem field exhibits the highest reliability
- Answer level shows only about half fully valid
- Rationale component shows most pronounced degradation
- Cross-domain variation is substantial (Math and Biology/Medicine exceed 92% problem validity; Physics shows only 30%)

## 5 Experimental Results

### Models evaluated

GPT-5.2-Thinking, Gemini3-Pro-Preview, Claude-Opus4.5, Claude-Opus4.6, Grok-4.1, DeepSeek-V3.2-Thinking, Qwen3-Max-Thinking, Qwen3.5-Plus

### Key findings

| Model | HLE Full Acc | HLE-Verified Full Acc | Δ |
|---|---|---|---|
| Gemini3-pro | 40.42 | 48.2 | +7.78 |
| GPT-5.2-High | 33.35 | 43.3 | +9.95 |
| Claude-Opus4.5 | 30.00 | 38.8 | +8.80 |
| Grok 4.1-fast | 19.94 | 29.0 | +9.06 |
| Claude-Opus4.6 | 38.95 | 46.8 | +7.85 |
| DeepSeek-V3.2 | 24.90 | 36.4 | +11.50 |
| Qwen3-Max | 30.00 | 38.2 | +8.20 |

On the Revised Subset, accuracy increases range from +29.94 to +39.58 percentage points, indicating that a non-trivial fraction of "errors" on raw HLE are attributable to benchmark issues rather than model capability.

## 6 Conclusion

HLE-Verified improves HLE-style evaluations by reducing annotation noise and enabling more faithful measurements of model capabilities. The disputed set provides a roadmap for community-driven improvements.

---
Source: https://arxiv.org/html/2602.13964v3
