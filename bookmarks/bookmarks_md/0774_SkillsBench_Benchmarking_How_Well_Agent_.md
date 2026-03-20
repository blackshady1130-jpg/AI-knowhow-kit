# SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

Xiangyi Li, Wenbo Chen, Yimin Liu, et al.

## Abstract

Agent Skills are structured packages of procedural knowledge that augment LLM agents at inference time. Despite rapid adoption, there is no standard way to measure whether they actually help. We present SkillsBench, a benchmark of 86 tasks across 11 domains paired with curated Skills and deterministic verifiers. Each task is evaluated under three conditions: no Skills, curated Skills, and self-generated Skills. We test 7 agent-model configurations over 7,308 trajectories.

**Key findings:**
- Curated Skills raise average pass rate by 16.2 percentage points (pp)
- Effects vary widely by domain (+4.5pp for Software Engineering to +51.9pp for Healthcare)
- 16 of 84 tasks show negative deltas
- Self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming
- Focused Skills with 2–3 modules outperform comprehensive documentation
- Smaller models with Skills can match larger models without them

## 1 Introduction

Large language models have evolved from text generators into autonomous agents capable of executing complex, multi-step tasks. This evolution is exemplified by agent-centric CLI tools: Claude Code from Anthropic, Gemini CLI from Google, and Codex CLI from OpenAI.

Agent Skills offer an emerging solution. A Skill is a structured package comprising instructions, code templates, resources, and verification logic that augments agent behavior at inference time without model modification. Skills encode procedural knowledge: standard operating procedures, domain conventions, and task-specific heuristics.

### Two core contributions:

1. **A Skills-centric evaluation framework**: 84 tasks across 11 domains, each executed under three conditions — no Skills, curated Skills, and self-generated Skills — with deterministic verifiers and full trajectory logging.

2. **Large-scale empirical evaluation**: 7 agent-model configurations across 7,308 trajectories, producing the first systematic evidence on Skills efficacy, variance, and failure modes.

## 2 SkillsBench

### 2.1 Skills Specification

A Skill is an artifact that satisfies four criteria:
- **Procedural content**: Contains how-to guidance, not factual retrieval
- **Task-class applicability**: Applies to a class of problems, not a single instance
- **Structured components**: Includes a SKILL.md file plus optional resources
- **Portability**: Based on file systems, easy to edit, version, share

| | Prompts | RAG | Tools | Skills |
|---|---|---|---|---|
| Modular/reusable | × | ✓ | ✓ | ✓ |
| Procedural guidance | Limited | × | × | ✓ |
| Executable resources | × | × | ✓ | ✓ |
| Cross-model portable | ✓ | ✓ | ✓ | ✓ |

### 2.2 Task Specification

Each task is self-contained with: instruction, environment, deterministic verification test, and oracle solution.

---
Source: https://arxiv.org/html/2602.12670v1
