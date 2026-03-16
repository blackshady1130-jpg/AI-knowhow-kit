---
url: https://xbench.org/agi/babyVision
title: "BabyVision: Visual Reasoning Beyond Language"
description: "BabyVision, in collaboration with UniPat AI, is part of xbench's AGI-Aligned series, focused on evaluating visual understanding for Unspeakable Challenges."
captured_at: "2026-03-09T03:35:01.927Z"
---

# BabyVision: Visual Reasoning Beyond Language

## BabyVision Introduction

Designing benchmarks is essential for measuring AI progress and guiding future research. Yet benchmarking LLMs is becoming increasingly difficult: today’s models achieve exceptional scores on elite tasks such as Humanity’s Last Exam (HLE) and the International Mathematical Olympiad (IMO), reaching—even surpassing—PhD-level performance in language and textual reasoning.

But do multimodal LLMs (MLLMs) show similar expertise in vision? Meaningful evaluation requires disentangling visual ability from linguistic ability. When a visual task can be fully verbalized, it effectively becomes a language problem, allowing models to lean on strong textual reasoning rather than genuine visual understanding. Robust vision benchmarks must therefore be designed to minimize such linguistic shortcuts.

To rigorously assess models’ pure visual reasoning ability and compare it with human performance, we curate 20 vision-centric tasks—collectively referred to as BabyVision-Mini. We then evaluate models alongside children aged 3–12. The results are striking: even the strongest models perform at approximately the level of a three-year-old child. SOTA MLLM still lags typical six-year-old performance by roughly 20%, and other MLLMs fall below the average abilities of a three-year-old.

![ScienceQA Model Score Distribution](https://files-xbench.xhunt-ai.com/upload/babyvision_cf4798bedb.jpg)

### The "Unspeakable" Challenge in Visual Reasoning

Why do MLLMs fail at these seemingly simple tasks? The key insight is that these problems are "unspeakable"—they cannot be fully described in language without information loss. When models try to reason through text, they lose critical visual details.

The core problem: MLLMs try to compress visual reasoning into language tokens, but these tasks require direct perceptual processing that cannot be faithfully represented in text. We summarize 4 classic vision-centric challenges for current MLLMs observed during our evaluation.

### Insights

BabyVision reveals a striking truth: currnetly MLLMs do not have robust foundational visual competence even compared to children. By decomposing visual intelligence into atomic capabilities and benchmarking them independently of language, BabyVision exposes where current models fall short and why scaling language alone is insufficient. Our results further suggest that visual generation—reasoning by drawing, tracing, and manipulating images—offers a promising path forward, partially recovering capabilities that text-based reasoning cannot express.