Title: SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents

URL Source: http://arxiv.org/html/2604.17308v1

Markdown Content:
Ziao Zhang 1 Kou Shi 1 Shiting Huang 1 Avery Nie 2 Yu Zeng 1 Yiming Zhao 1

Zhen Fang 1 Qisheng Su 1 Haibo Qiu 3 Wei Yang 1 Qingnan Ren 1 Shun Zou 1

 Wenxuan Huang 1 Lin Chen 1 Zehui Chen 1 Feng Zhao 1

1 University of Science and Technology of China 

2 University of Toronto 3 University of Sydney 

[Project Page](https://zhangzi-a.github.io/SkillFlow-project-page/)

###### Abstract

As the capability frontier of autonomous agents continues to expand, they are increasingly able to complete specialized tasks through plug-and-play external skills. Yet current benchmarks mostly test whether models can use provided skills, leaving open whether they can discover skills from experience, repair them after failure, and maintain a coherent library over time. We introduce SkillFlow, a benchmark of 166 tasks across 20 families in which task construction within each family follows a Domain-Agnostic Execution Flow (DAEF) that defines an agent workflow framework, allowing these tasks to share a consistent workflow. Agents are evaluated under an Agentic Lifelong Learning protocol in which they begin without skills, solve tasks sequentially within each family, externalize lessons through trajectory- and rubric-driven skill patches, and carry the updated library forward. Experiments reveal a substantial capability gap. For Claude Opus 4.6, lifelong skill evolution improves task success from 62.65% to 71.08% (+8.43 points). However, high skill usage does not necessarily imply high utility: Kimi K2.5 gains only +0.60 points despite 66.87% skill usage, while Qwen-Coder-Next reaches only a 44.58% task completion rate and still regresses relative to the vanilla setting. SkillFlow contributes a structured testbed for this direction and an in-depth empirical analysis of skill discovery, patching, transfer, and their failure modes under lifelong evaluation. The code is available at [https://github.com/ZhangZi-a/SkillFlow](https://github.com/ZhangZi-a/SkillFlow).

![Image 1: Refer to caption](https://arxiv.org/html/2604.17308v1/x1.png)

Figure 1: Conceptual Overview of SkillFlow. The figure contrasts conventional static-skill evaluation with our lifelong setting, in which agents externalize experience into reusable skill artifacts, revise them through patches, and transfer them across tasks that share a common DAEF.

![Image 2: Refer to caption](https://arxiv.org/html/2604.17308v1/x2.png)

Figure 2: Task-Construction Pipeline of SkillFlow. Step 1 collects candidate seed tasks and a curated external skill pool. Step 2 uses embedding-based pair matching to attach relevant skills to each seed and form task–skill reference pairs. Step 3 performs domain expansion under a fixed DAEF: the Architect Agent generates an initial cross-domain task set, the Critic Agent either rejects or accepts the family, and accepted families proceed to a second expansion round that adds more tasks and establishes a difficulty gradient. Step 4 applies human review over robustness, logical soundness, difficulty calibration, and instruction-leakage risk before final benchmark inclusion.

## 1 Introduction

Frontier Large Language Models(LLMs) systems are increasingly deployed as autonomous command-line agents that solve realistic multi-step tasks in terminal environments. Claude Code[[2](http://arxiv.org/html/2604.17308v1#bib.bib1 "Claude Code: an agentic coding tool")], Gemini CLI[[11](http://arxiv.org/html/2604.17308v1#bib.bib2 "Gemini CLI: An open-source AI agent that brings the power of Gemini directly into your terminal")], Codex CLI[[25](http://arxiv.org/html/2604.17308v1#bib.bib3 "Codex CLI: Lightweight coding agent that runs in your terminal")], and Qwen-Coder[[30](http://arxiv.org/html/2604.17308v1#bib.bib5 "Qwen-code")] are prominent examples. Agent skills have recently emerged as external packages of procedural knowledge that augment model capabilities for specialized tasks. These skills can encode usage scenarios, core guidance, and reusable code or documentation assets. As a result, many vendors are beginning to release agent versions with native skill support.

SkillsBench[[19](http://arxiv.org/html/2604.17308v1#bib.bib20 "SkillsBench: benchmarking how well agent skills work across diverse tasks")] provides an early demonstration that skills can substantially assist models in solving tasks, while also suggesting that current models remain limited in generating skills autonomously. However, it does not examine whether an LLM can discover and summarize reusable skills from its own task-solving process and apply them to future tasks of the same type. SkillWeaver[[43](http://arxiv.org/html/2604.17308v1#bib.bib9 "Skillweaver: web agents can self-improve by discovering and honing skills")], SkillRL[[37](http://arxiv.org/html/2604.17308v1#bib.bib18 "SkillRL: evolving agents via recursive skill-augmented reinforcement learning")], MemSkill[[41](http://arxiv.org/html/2604.17308v1#bib.bib12 "MemSkill: learning and evolving memory skills for self-evolving agents")], and related systems[[44](http://arxiv.org/html/2604.17308v1#bib.bib11 "Memento-skills: let agents design agents")] also show that experience-derived skills can improve downstream performance. This leads to a central question: can an autonomous agent extract reusable skills from its own experience, repair them after failures, and maintain an evolving skill library across a sequence of tasks? To answer this question, we introduce SkillFlow, a benchmark of 166 runnable tasks across 20 task families for measuring lifelong skill discovery and evolution.

To construct the benchmark, we first analyze existing agent loops and find that mature agents[[17](http://arxiv.org/html/2604.17308v1#bib.bib43 "Vision-deepresearch: incentivizing deepresearch capability in multimodal large language models"), [40](http://arxiv.org/html/2604.17308v1#bib.bib45 "Vision-deepresearch benchmark: rethinking visual and textual search for multimodal large language models"), [10](http://arxiv.org/html/2604.17308v1#bib.bib44 "DualVLA: building a generalizable embodied agent via partial decoupling of reasoning and action")] typically rely on stable AI workflows, which allow them to solve tasks of the same type in a consistent manner. Based on this observation, we define the Domain-Agnostic Execution Flow (DAEF), a workflow framework that preserves operational topology while abstracting away domain-specific entities and serves as a scaffold for benchmark construction. We use this structure to support controlled progression within each task family. Concretely, we select realistic tasks from GDPval[[28](http://arxiv.org/html/2604.17308v1#bib.bib21 "Gdpval: evaluating ai model performance on real-world economically valuable tasks")] and SkillsBench[[19](http://arxiv.org/html/2604.17308v1#bib.bib20 "SkillsBench: benchmarking how well agent skills work across diverse tasks")] and extract a DAEF from each seed task. We then instantiate each DAEF through a dual-agent iterative pipeline using the original task as a reference instance, where one agent constructs task assets and the other reviews the generated tasks and provides timely feedback for revision. This process yields 8 to 9 tasks in the Harbor format[[14](http://arxiv.org/html/2604.17308v1#bib.bib8 "Harbor: A framework for evaluating and optimizing agents and models in container environments")] for each DAEF, which together form a task family. After human verification, the final benchmark contains 20 task families and 166 tasks. Evaluation then follows an Agentic Lifelong Learning protocol in which an agent begins without skills, solves tasks sequentially within each family, summarizes lessons from trajectories and rubric feedback, and updates the library through explicit skill patches after each task.

Experiments reveal a substantial capability gap. On Claude Opus 4.6, lifelong skill evolution improves task success from 62.65% to 71.08% (+8.43 points). Yet high usage does not imply high utility: Kimi K2.5 gains only +0.60 points despite a 66.87% skill usage rate, while Qwen-Coder-Next reaches only a 44.58% task completion rate and still regresses relative to the vanilla setting. We find that most current models fail to achieve stable self-evolution through iterative skill updates. Stronger models tend to consolidate prior experience into stable workflows and continue refining them over time, thereby realizing sustained capability gains. Weaker models struggle to integrate multiple experiences into a coherent procedure, which leads to cognitive overload in subsequent tasks.

##### Contributions.

Our contributions are listed:

*   •
We introduce SkillFlow, a benchmark of 166 runnable tasks across 20 task families for evaluating lifelong skill discovery and evolution in autonomous agents.

*   •
We design task families with a shared agent workflow framework based on DAEF, enabling systematic evaluation of cross-task skill transfer learning.

*   •
We specify an Agentic Lifelong Learning protocol in which agents begin without skills, evolve an external skill library through trajectory- and rubric-driven skill patches, and progressively learn and are evaluated under a fixed task order within each family.

*   •
We identify and closely analyze common failure patterns in skill evolution, including fragmented skill growth, reinforcement of erroneous logic, and the gap between writing skills and reliably repairing them, revealing current models’ limitations in producing compact, transferable procedural skills.

## 2 SkillFlow

### 2.1 Benchmark Overview

SkillFlow contains 20 workflow families and 166 tasks spanning five broad domains: Finance & Economics, Operations & Supply Chain, Healthcare & Life Sciences, Governance & Strategy, and Data & Document Intelligence. Each benchmark instance is defined by a family-local task sequence, a fixed within-family difficulty order, and an associated verifier style. Family sizes range from 8 to 9 tasks. Overall, the benchmark encompasses a range of realistic workplace workflows, including spreadsheet-centric planning, OCR and PDF extraction, office-document editing, compliance analysis, and quantitative reasoning.

### 2.2 Domain-Agnostic Execution Flow

The central design principle of SkillFlow is a Domain-Agnostic Execution Flow (DAEF): a workflow skeleton shared by a family of tasks after removing domain-specific entities, file names, and business semantics. Formally, we represent a task instance as a domain-grounded workflow graph

\mathcal{T}=(V,E,\lambda,\gamma),(1)

where V is a set of executable sub-goals or operations, E\subseteq V\times V is a set of precedence or dependency edges, \lambda(v) assigns each node a domain-agnostic operation type, and \gamma(v) provides task-specific grounding, such as concrete files, entities, fields, or business objects.

A DAEF is the abstract workflow graph obtained by removing task-specific grounding while preserving operation types and dependency structure:

\mathcal{F}=\phi(\mathcal{T})=(V_{F},E_{F},\lambda_{F}).(2)

![Image 3: Refer to caption](https://arxiv.org/html/2604.17308v1/x3.png)

Figure 3: DAEF correspondence across domains. Distinct tasks can instantiate the same abstract workflow, enabling cross-domain skill transfer.

![Image 4: Refer to caption](https://arxiv.org/html/2604.17308v1/x4.png)

Figure 4: Relationship Between Benchmark Categories and DAEFs. The inner ring shows the five top-level benchmark categories, and the outer ring shows the corresponding DAEF names under each category.

##### Operationalizing DAEF in construction.

We operationalize DAEF through a two-stage human annotation and standardization protocol that makes extraction explicit, standardized, and verifiable before task generalization.

Stage 1: meta-step extraction. Each seed task is independently annotated with a sequence of meta-step nodes containing 5–8 executable operations, dependency edges, and a short textual rationale. Node types are drawn from a controlled single-word vocabulary such as read, retrieve, compute, detect, and output; the full inventory is listed in Appendix[A.5](http://arxiv.org/html/2604.17308v1#A1.SS5 "A.5 DAEF Node Vocabulary ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents").

Stage 2: workflow construction. The extracted workflow representation is normalized by collapsing task-specific grounding, standardizing node labels, and retaining only the dependency structure and operation inventory stable across tasks. The resulting canonical DAEF also specifies the allowed categories of variation to control the difficulty gradient of subsequently instantiated tasks. We provide the detailed annotation rules and expert agreement screening procedure in Appendix[A.5](http://arxiv.org/html/2604.17308v1#A1.SS5 "A.5 DAEF Node Vocabulary ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). A canonical DAEF is retained only if it remains internally coherent and supports controlled generalization to new tasks without introducing a new workflow; a detailed table of allowed variation types appears in Appendix[A.6](http://arxiv.org/html/2604.17308v1#A1.SS6 "A.6 Allowed Surface Variation Types ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents").

### 2.3 Task Construction Protocol

Figure[2](http://arxiv.org/html/2604.17308v1#S0.F2 "Figure 2 ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") summarizes the process used to build SkillFlow. We organize it into four steps.

##### Step 1: seed task collection and skill curation.

We identify seed tasks from two benchmark suites, retaining high-quality examples that reflect realistic workplace scenarios without requiring external network services. We exclude tasks that are overly narrow, simple, or difficult to verify reliably. This yields 64 seed tasks: 18 from SkillsBench[[19](http://arxiv.org/html/2604.17308v1#bib.bib20 "SkillsBench: benchmarking how well agent skills work across diverse tasks")] and 46 from GDPval[[28](http://arxiv.org/html/2604.17308v1#bib.bib21 "Gdpval: evaluating ai model performance on real-world economically valuable tasks")]. Simultaneously, we gather over 8,000 open-source skills from public repositories[[8](http://arxiv.org/html/2604.17308v1#bib.bib36 "Awesome-claude-skills: a curated list of awesome claude skills, resources, and tools"), [34](http://arxiv.org/html/2604.17308v1#bib.bib37 "Awesome-openclaw-skills: the awesome collection of openclaw skills"), [3](http://arxiv.org/html/2604.17308v1#bib.bib35 "Anthropics/skills: public repository for agent skills"), [31](http://arxiv.org/html/2604.17308v1#bib.bib38 "SkillsMP: skills marketplace")], filtering them for safety, formatting, and domain relevance to obtain 2,318 skills for task construction.

##### Step 2: task–skill pair matching.

To provide specialized support for subsequent task construction, we match each seed task with reference skills. Using Qwen3-embedding-4B[[42](http://arxiv.org/html/2604.17308v1#bib.bib22 "Qwen3 embedding: advancing text embedding and reranking through foundation models")], we calculate semantic similarity between task and skill descriptions and retrieve 5–10 candidate skills for each seed, yielding 64 matched task–skill pairs.

##### Step 3: iterative task-family generalization.

We then construct the family-level reference package used for domain expansion. For each selected seed, human annotators convert the task into a DAEF by extracting meta-steps and defining the workflow according to the previously described protocol. After deduplication and a generalization-difficulty check, we retain 30 DAEFs. The resulting seed-task reference package—including the original assets, matched skills, files, environment, and stable DAEF—enters an automated construction loop. We discard seeds at this stage if the resulting family fails to achieve execution stability or DAEF consistency within five revision iterations.

(a) Architect Agent generation. The first agent, built within Cursor[[4](http://arxiv.org/html/2604.17308v1#bib.bib6 "Cursor: ai code editor")] using GPT-5.3-Codex[[26](http://arxiv.org/html/2604.17308v1#bib.bib7 "Introducing gpt-5.3-codex")], serves as the Architect Agent for the new task family. Conditioned on the target DAEF, it proposes new task types and uses the seed task as a reference to construct task goals, create task assets, and define verification schemes for these tasks. With support from the matched skills, it then builds the corresponding Docker task environments and develops solver and verifier assets, producing four initial tasks in the Harbor format.

(b) Critic Agent review. A second agent, employing Claude Opus 4.6, serves as the Critic Agent and evaluates the four initial tasks. It verifies and evaluates these tasks in real Docker environments and provides detailed feedback after jointly assessing workflow consistency, the presence of a difficulty gradient, task solvability, verifier correctness, and environment reliability.

(c) Revision loop and expansion phase. The Architect Agent and the Critic Agent interact for multiple rounds until the Critic Agent approves the family. If the Critic Agent rejects the family more than five times, construction of that task family is abandoned. After passing inspection, the process enters a second round of task construction, which follows the same construction–verification loop as the first round and generates 4–5 new tasks. This two-round process produces a task sequence of 8–9 tasks for each family and ultimately yields 20 task families.

##### Step 4: human review and family revision.

Human reviewers inspect each candidate family along four dimensions: instruction leakage, logical soundness of the task, correctness of the final task environment, and reasonableness of the difficulty gradient. Families with issues in any dimension are returned for manual revision. In practice, thanks to the strict construction procedure in the preceding steps, none of the 20 task families exhibits fatal environment errors, and all 20 families are retained after manual revision.

After the final review and revision process, this pipeline yields 20 workflow families and 166 tasks.

### 2.4 Agentic Lifelong Learning Protocol

We formalize the lifelong learning protocol as a sequential process over a family of tasks. Let \mathcal{F}=\{T_{1},T_{2},\ldots,T_{n}\} denote an ordered task family, where tasks are sorted by within-family difficulty. The agent maintains an updatable skill library \mathcal{S}_{t} at each step t. The protocol proceeds as follows:

First-task execution and feedback. For the first task T_{1}, the agent does not use any skill and completes the task under its native agent harness, producing an execution trace \tau_{1}. After task completion, the model receives a verifier-derived rubric r_{1}, which is a normalized textual description of missing or incorrect content.

Skill patch generation. After each task, the model learns from the resulting trajectory and verifier feedback and generates a skill patch conditioned on a fixed skill-patch prompt template g. This patch-generation step relies on the model’s native capability rather than the surrounding agent harness. For the first task, the patch bootstraps the skill library from scratch:

\Delta_{1}=\text{Model}_{g}(\emptyset,\tau_{1},r_{1}),\quad\mathcal{S}_{1}=\text{Apply}(\Delta_{1},\emptyset).(3)

For all subsequent tasks t>1, the agent executes T_{t} with the current library \mathcal{S}_{t-1}, obtains an execution trace \tau_{t} and verifier-derived rubric r_{t}, and applies the same prompted generation process incrementally:

\Delta_{t}=\text{Model}_{g}(\mathcal{S}_{t-1},\tau_{t},r_{t}),\quad\mathcal{S}_{t}=\text{Apply}(\Delta_{t},\mathcal{S}_{t-1}).(4)

The patch \Delta_{t} may add, revise, or delete skills. This incremental update preserves the skill evolution history and avoids regenerating the entire library from scratch.

Family reset. This design follows the goal of SkillFlow to evaluate lifelong learning within a single class of agent tasks rather than the agent’s ability to apply skills precisely across heterogeneous workflows. Interleaving tasks from different workflows in a single evaluation stream would introduce unnecessary system noise, including confounds from skill retrieval mechanisms.

##### Skill patch schema.

We use a minimal auditable interface for skill evolution to avoid complex instruction-following effects that could compromise evaluation fairness. Skill patch generation is driven by the model’s native capability and is decoupled from the agent harness used for task execution. In the equations above, g denotes the fixed prompt template that specifies how the model should generate skill patches; this template is provided in Appendix[B.2](http://arxiv.org/html/2604.17308v1#A2.SS2 "B.2 Skill Patch Generation Prompt Template ‣ Appendix B Skill Evolution Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). Each patch contains three fields: summary, upsert_files, and delete_paths. Together, these fields are sufficient to record the high-level lesson, create or overwrite SKILL.md files and helper scripts, and remove obsolete artifacts. The resulting skills follow the same standard skill structure described above. This file-level interface preserves patch history, supports update tracking over time, and makes failure modes such as uncontrolled skill growth directly inspectable when redundant or low-value artifacts accumulate in the library.

##### Skill use detection.

Each task is completed under the planning policy of its native agent harness. Because these harnesses already support skills, the model can choose to use skills natively without any additional control mechanism. We only extract task-completion outcomes and execution-trace events associated with library files, such as skill reads or skill calls, to detect skill use and compute the skill reuse rate.

This protocol evaluates not only whether an agent can benefit from a static external memory, but also whether it can continuously maintain, repair, and improve a reusable skill repository over time.

### 2.5 Metrics

We evaluate agents using three metric groups:

*   •
Task success rate: whether the final output satisfies the task verifier.

*   •
Efficiency: runtime cost per task, reported through interaction turns, monetary cost, and output tokens.

*   •
Skill generation and reuse: statistics that record both the average number of skills retained in the final family-local library and the rate at which previously stored skills are reused in later tasks.

## 3 Experiments

### 3.1 Experimental Setup

We evaluate SkillFlow under the Agentic Lifelong Learning protocol. Within each task family, an agent begins with an empty skill library, solves the first task without prior skills, and then updates the library iteratively through skill patches derived from execution trajectories and rubric feedback. To place each model in its strongest practical setting, we pair it with a matched agent wrapper and execution harness. We standardize only the interface for skill-patch generation by requiring a single-turn output format. This keeps the representation of generated skills consistent while preserving compatibility with the execution environment of each model.

The main experiments use Claude Code[[2](http://arxiv.org/html/2604.17308v1#bib.bib1 "Claude Code: an agentic coding tool")], Codex CLI[[25](http://arxiv.org/html/2604.17308v1#bib.bib3 "Codex CLI: Lightweight coding agent that runs in your terminal")], Qwen-Coder[[30](http://arxiv.org/html/2604.17308v1#bib.bib5 "Qwen-code")], and Kimi-CLI[[23](http://arxiv.org/html/2604.17308v1#bib.bib4 "Kimi cli")] as evaluation harnesses. Across these harnesses, we evaluate 11 model variants: Claude Sonnet 4.5, Claude Opus 4.5, Claude Sonnet 4.6, Claude Opus 4.6, MiniMax M2.5, MiniMax M2.7, GPT 5.4, GPT 5.3 Codex, Qwen-Coder-Next, Qwen3-Coder-480B, and Kimi K2.5.

Table 1: Main Experimental Results. All values are benchmark-level averages. %comp. is task completion rate; Turns, Cost, and Out Tok. are per-task averages of interaction turns, USD cost, and output tokens (thousands). #Skills is the cumulative number of skills generated within a task family, and %use is the percentage of tasks that read or call at least one stored skill. In the \Delta block, %comp. and Turns are absolute changes, whereas %Cost and %Out Tok. are relative percentage changes. Green indicates higher-is-better metrics, blue indicates lower-is-better metrics, and bold marks the best value in each column.

Agent Model vanilla skills evolve\boldsymbol{\Delta}
%comp.\uparrow Turns\downarrow Cost(USD)\downarrow Out Tok.(K)\downarrow%comp.\uparrow Turns\downarrow Cost\downarrow Out Tok.(K)\downarrow#Skills%use%comp.\uparrow Turns\downarrow%Cost\downarrow%Out Tok.\downarrow
Claude Code Claude Sonnet 4.5 49.4 25.04 0.293 1.07 55.42 24.88 0.246 0.85 2.55 72.89+6.02-0.16-16.04-20.56
Claude Opus 4.5 58.43 18.83 0.571 1.5 60.84 18.31 0.384 1.4 1.5 60.84+2.41-0.52-32.87-6.67
Claude Sonnet 4.6 56.63 17.48 0.168 1.23 56.63 17.42 0.245 1.59 2.55 53.01+0.00-0.06+45.83+29.27
Claude Opus 4.6 62.65 17.34 0.665 3.00 71.08 19.00 0.615 2.39 1.05 45.78+8.43 1.66-7.52-20.33
MiniMax M2.5 28.31 35.22 0.010 0.44 34.94 34.01 0.010 0.54 2.50 32.53+6.63-1.21 0+22.73
MiniMax M2.7 37.35 25.44 0.012 0.5 36.75 27.42 0.017 0.96 4.6 51.2-0.6+1.98+41.67+92
Codex CLI GPT 5.4 33.13 23.89 0.41 4.05 36.75 24.17 0.459 4.43 1.05 81.33+3.62+0.28+11.95+9.38
GPT 5.3 Codex 52.41 17.74 0.492 6.8 46.39 17.14 0.434 6.82 1.1 84.94-6.02-0.6-11.79+0.29
Qwen Coder Qwen-Coder-Next 45.18 18.64 0.103 9.74 44.58 19.91 0.113 10.69 5.45 12.05-0.60+1.27+9.71 9.75
Qwen3-Coder-480B 24.7 26.22 0.189 12.58 24.1 28.8 0.199 12.12 5.2 66.87-0.6+2.58+5.29-3.66
Kimi CLI Kimi K2.5 55.42 12.62 0.103 7.31 56.02 11.51 0.104 7.10 1.50 66.87+0.60-1.11+0.97-2.87

![Image 5: Refer to caption](https://arxiv.org/html/2604.17308v1/x5.png)

Figure 5: Completion–Cost Pareto Frontier. Each point is one evaluated agent-model setting under vanilla execution or lifelong skill evolution. Some settings shift toward higher completion with comparable or lower cost, while others gain little or regress despite additional spending.

![Image 6: Refer to caption](https://arxiv.org/html/2604.17308v1/x6.png)

Figure 6: Domain-Grouped Completion Gains from Skill Evolution. Rows correspond to evaluated agent-model settings, while columns are organized into coarse benchmark groups. Abbreviations: FE = Finance & Economics; OS = Operations & Supply Chain; HLS = Healthcare & Life Sciences; GS = Governance & Strategy; DDI = Data & Document Intelligence.

### 3.2 Observations

Table[1](http://arxiv.org/html/2604.17308v1#S3.T1 "Table 1 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") shows that skill evolution yields substantial gains for some models, but the effect varies sharply across settings. The clearest positive case is Claude Opus 4.6, which increases completed tasks from 104 to 118 out of 166 and raises mean task success from 62.65% to 71.08% (+8.43 points). Positive transfer also appears for MiniMax M2.5, which improves from 28.31% to 34.94% (+6.63 points), for Claude Sonnet 4.5, which improves from 49.40% to 55.42% (+6.02 points), for GPT 5.4, which rises from 33.13% to 36.75% (+3.62 points), for Claude Opus 4.5, which rises from 58.43% to 60.84% (+2.41 points), and for Kimi K2.5, which increases modestly from 55.42% to 56.02% (+0.60 points).

By contrast, Table[1](http://arxiv.org/html/2604.17308v1#S3.T1 "Table 1 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") also contains several settings in which skill evolution does not help or directly reduces performance. GPT 5.3 Codex declines from 52.41% to 46.39% (-6.02 points). Qwen-Coder-Next declines from 45.18% to 44.58% (-0.60 points), Qwen3-Coder-480B declines from 24.70% to 24.10% (-0.60 points), and MiniMax M2.7 declines from 37.35% to 36.75% (-0.60 points). Claude Sonnet 4.6 remains unchanged at 56.63% under both settings.

Figure[6](http://arxiv.org/html/2604.17308v1#S3.F6 "Figure 6 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") provides a complementary efficiency view of the same settings. Several points move toward higher completion with comparable or lower cost, whereas others move toward higher cost with limited gains or no gains. Figure[6](http://arxiv.org/html/2604.17308v1#S3.F6 "Figure 6 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") shows that gains are broadly distributed across task-family groups rather than concentrated in a single category, which suggests that current models do not yet exhibit a clear preference for any particular task type during skill evolution. At the same time, some group-level differences remain: Finance & Economics contains more negative gains, whereas Data & Document Intelligence more often shows positive transfer. Appendix Figure[11](http://arxiv.org/html/2604.17308v1#A3.F11 "Figure 11 ‣ C.4 Full Skill-Gain Heatmap ‣ Appendix C Experiments and Analysis Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") provides the full family-level heatmap for a more detailed view.

### 3.3 Main Results

To better understand model behavior under the Agentic Lifelong Learning protocol, we analyze the full set of experimental results from all 11 evaluated models and summarize the following findings.

Finding 1: Opus 4.6 comes closest to stable skill-based learning. Among the evaluated models, Opus 4.6 provides the clearest evidence that skill revision can improve the procedure stored in the library rather than merely accumulate successful traces. Table[1](http://arxiv.org/html/2604.17308v1#S3.T1 "Table 1 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") and Figure[6](http://arxiv.org/html/2604.17308v1#S3.F6 "Figure 6 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") show the strongest overall improvement for this setting, with higher completion at lower cost. Trace analysis further shows cases in which repaired skills are reused after concrete failures, including spreadsheet workflows that require cached-value handling. We also conduct a control experiment that simply prepends the full prior interaction history as additional context. On Claude Opus 4.6, this setting reaches only 51.04%, below both vanilla and the full protocol (Appendix Table[6](http://arxiv.org/html/2604.17308v1#A3.T6 "Table 6 ‣ C.2 Historical-Trajectory Context Control ‣ Appendix C Experiments and Analysis Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents")), which suggests that the gain is not explained by longer raw context alone. Within the scope of our benchmark, this is the clearest instance of stable library-level improvement.

Finding 2: Incorrect skills create systematic downstream drift. Once an incorrect skill is written into the library, later tasks often inherit the same flawed abstraction, turning a local error into a sequence-level pattern. This pattern likely reflects the difficulty of escaping a self-generated logic distribution, which suggests that, while external skills can amplify capability, they can also amplify error.

Finding 3: Unified high-utility skills outperform fragmented task-specific skills. The strongest libraries are usually organized around one or a few reusable skills that are revised repeatedly as new variants appear. In Table[1](http://arxiv.org/html/2604.17308v1#S3.T1 "Table 1 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), stronger settings tend to end with smaller final skill inventories, whereas weaker settings often accumulate more skills without comparable gains. This pattern suggests that consolidation is generally more valuable than proliferation.

Finding 4: Qwen and part of MiniMax mainly fail through skill inflation. For Qwen and some MiniMax settings, the main problem is often not skill absence but uncontrolled growth of overlapping skills. Appendix Figure[8](http://arxiv.org/html/2604.17308v1#A2.F8 "Figure 8 ‣ B.3 Skill Library Growth and Composition ‣ Appendix B Skill Evolution Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") shows that the accumulated number of stored skills in these settings increases almost monotonically with task index, which suggests that they tend to summarize nearly every task into an additional skill. Yet Table[1](http://arxiv.org/html/2604.17308v1#S3.T1 "Table 1 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") still shows weak or negative benchmark-level gains, and Figure[6](http://arxiv.org/html/2604.17308v1#S3.F6 "Figure 6 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") does not show correspondingly broad improvement across task families. In these cases, the dominant failure mode is better described as fragmentation through skill inflation than as skill scarcity.

Finding 5: Codex is relatively strong at consolidating variants into one evolving core skill. Codex shows a clearer tendency than most models to absorb nearby task variants into a shared evolving skill rather than proliferate many narrowly specialized entries. Appendix Figure[8](http://arxiv.org/html/2604.17308v1#A2.F8 "Figure 8 ‣ B.3 Skill Library Growth and Composition ‣ Appendix B Skill Evolution Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") shows that Codex-based libraries remain relatively compact in file count compared with many other settings. However, Table[1](http://arxiv.org/html/2604.17308v1#S3.T1 "Table 1 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") also shows that this compactness does not translate into stronger task completion: compared with Opus settings, which also keep their libraries relatively small, Codex does not achieve comparable end-to-end gains under the full harness.

Finding 6: The key model gap lies in repairing bad skills, not in writing skills. Most models can write some skill after completing or attempting a task, so raw skill generation is not the main source of variation. The larger difference is whether a model can recognize an incorrect skill, revise it, and obtain better behavior on later tasks. Across the table, the frontier plot, and the traces, positive transfer aligns more closely with effective skill repair than with skill volume alone.

Summary.

These findings show that the effects of iterative skill evolution depend strongly on model capability. Across settings, compact and well-revised skills are consistently more effective than fragmented, isolated skill entries, while incorrect early skills can induce persistent negative transfer and substantially degrade later performance. More broadly, the practical value of skill evolution appears to depend less on writing more skills than on maintaining a small, repairable library of high-utility procedures. This property may also make it easier to retrieve relevant skills when extending such systems to more open-ended environments.

## 4 Related Work

### 4.1 Execution Environments and Benchmarks

A growing line of work evaluates agent capabilities in controlled environments with tool use and multi-step reasoning[[27](http://arxiv.org/html/2604.17308v1#bib.bib26 "The berkeley function calling leaderboard (bfcl): from tool use to agentic evaluation of large language models"), [21](http://arxiv.org/html/2604.17308v1#bib.bib28 "Agentbench: evaluating llms as agents"), [33](http://arxiv.org/html/2604.17308v1#bib.bib24 "Appworld: a controllable world of apps and people for benchmarking interactive coding agents")]. Some benchmarks further focus on reliability aspects such as error correction in tool calling[[15](http://arxiv.org/html/2604.17308v1#bib.bib41 "CRITICTOOL: evaluating self-critique capabilities of large language models in tool-calling error scenarios")], as well as the inefficiency patterns that emerge during complex tool-integrated reasoning[[32](http://arxiv.org/html/2604.17308v1#bib.bib39 "Beyond accuracy: unveiling inefficiency patterns in tool-integrated reasoning")]. Other work studies whether explicit skill usage improves performance in realistic software engineering settings[[13](http://arxiv.org/html/2604.17308v1#bib.bib27 "SWE-skills-bench: do agent skills actually help in real-world software engineering?")]. Recent coding-agent benchmarks emphasize realistic, long-horizon tasks under shared Harbor-based execution setups for reproducibility and comparability[[22](http://arxiv.org/html/2604.17308v1#bib.bib29 "Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces"), [36](http://arxiv.org/html/2604.17308v1#bib.bib30 "Top leaderboard ranking= top coding proficiency, always? evoeval: evolving coding benchmarks via llm"), [9](http://arxiv.org/html/2604.17308v1#bib.bib31 "Swe-bench pro: can ai agents solve long-horizon software engineering tasks?"), [7](http://arxiv.org/html/2604.17308v1#bib.bib32 "Autocodebench: large language models are automatic code benchmark generators"), [6](http://arxiv.org/html/2604.17308v1#bib.bib10 "SkillCraft: can llm agents learn to use tools skillfully?")].

### 4.2 Skills as Procedural Knowledge for Agents

Recent studies treat skills as reusable procedural knowledge bridging models and workflows, including large-scale skill management, skill-aware benchmarking, and trajectory distillation into reusable skills[[20](http://arxiv.org/html/2604.17308v1#bib.bib16 "SkillNet: create, evaluate, and connect ai skills"), [29](http://arxiv.org/html/2604.17308v1#bib.bib17 "PinchBench: skill-based benchmark for llm agents"), [24](http://arxiv.org/html/2604.17308v1#bib.bib19 "Trace2Skill: distill trajectory-local lessons into transferable agent skills")]. However, these works mainly focus on infrastructure or downstream performance, with limited evaluation of skill derivation and cross-task transfer.

### 4.3 Automatic Skill Discovery and Evolution

Another line of work explores automatic skill discovery and evolution from interaction, including distilling interaction patterns, refining skills through feedback and failures[[43](http://arxiv.org/html/2604.17308v1#bib.bib9 "Skillweaver: web agents can self-improve by discovering and honing skills"), [39](http://arxiv.org/html/2604.17308v1#bib.bib14 "AutoSkill: experience-driven lifelong learning via skill self-evolution"), [1](http://arxiv.org/html/2604.17308v1#bib.bib13 "EvoSkill: automated skill discovery for multi-agent systems"), [41](http://arxiv.org/html/2604.17308v1#bib.bib12 "MemSkill: learning and evolving memory skills for self-evolving agents"), [35](http://arxiv.org/html/2604.17308v1#bib.bib23 "Evo-memory: benchmarking llm agent test-time learning with self-evolving memory"), [16](http://arxiv.org/html/2604.17308v1#bib.bib40 "Internalizing meta-experience into memory for guided reinforcement learning in large language models")], and self-improving models via self-generated supervision[[12](http://arxiv.org/html/2604.17308v1#bib.bib42 "UniCorn: towards self-improving unified multimodal models through self-generated supervision")]. Some approaches further model skills as persistent and improvable structures or leverage long interaction traces for accumulation[[38](http://arxiv.org/html/2604.17308v1#bib.bib15 "Xskill: cross embodiment skill discovery"), [44](http://arxiv.org/html/2604.17308v1#bib.bib11 "Memento-skills: let agents design agents"), [37](http://arxiv.org/html/2604.17308v1#bib.bib18 "SkillRL: evolving agents via recursive skill-augmented reinforcement learning"), [5](http://arxiv.org/html/2604.17308v1#bib.bib34 "Coding agents are effective long-context processors")]. These methods demonstrate performance gains from skill accumulation, but focus more on optimization than on evaluating skill abstraction, revision, and transfer.

## 5 Conclusion

We introduce SkillFlow, a benchmark evaluating lifelong skill discovery and evolution in autonomous agents. It contributes a dual-agent construction pipeline, an explicit sequential evaluation protocol, and a task set organized around Domain-Agnostic Execution Flow to test skill transfer at the workflow level instead of superficial lexical overlap. Experiments show that lifelong skill evolution yields selective rather than universal gains: stronger agent–model stacks convert externalized experience into compact reusable procedures, whereas weaker ones often exhibit a creation–reuse coordination gap, fragmented skill libraries, and unstable reinforcement under feedback. This positions SkillFlow as both a benchmark release and an initial empirical characterization of skill evolution under one concrete external-memory mechanism.

More broadly, as autonomous agents become increasingly general-purpose, continuous skill evolution may provide a practical mechanism for acquiring and consolidating knowledge across domains. In this sense, enabling agents to revise skills from experience appears important for building more robust and adaptive lifelong learning systems.

## References

*   [1]S. Alzubi, N. Provenzano, J. Bingham, W. Chen, and T. Vu (2026)EvoSkill: automated skill discovery for multi-agent systems. arXiv preprint arXiv:2603.02766. Cited by: [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [2]Anthropic (2025)Claude Code: an agentic coding tool. Note: [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p1.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§3.1](http://arxiv.org/html/2604.17308v1#S3.SS1.p2.1 "3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [3]Anthropic (2026)Anthropics/skills: public repository for agent skills. Note: [https://github.com/anthropics/skills](https://github.com/anthropics/skills)GitHub repository. Accessed: 2026-04-13 Cited by: [§2.3](http://arxiv.org/html/2604.17308v1#S2.SS3.SSS0.Px1.p1.1 "Step 1: seed task collection and skill curation. ‣ 2.3 Task Construction Protocol ‣ 2 SkillFlow ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [4]Anysphere (2024)Cursor: ai code editor. Note: [https://cursor.sh](https://cursor.sh/)Cited by: [§2.3](http://arxiv.org/html/2604.17308v1#S2.SS3.SSS0.Px3.p2.1 "Step 3: iterative task-family generalization. ‣ 2.3 Task Construction Protocol ‣ 2 SkillFlow ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [5]W. Cao, X. Yin, B. Dhingra, and S. Zhou (2026)Coding agents are effective long-context processors. arXiv preprint arXiv:2603.20432. Cited by: [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [6]S. Chen, J. Gai, R. Zhou, J. Zhang, T. Zhu, J. Li, K. Wang, Z. Wang, Z. Chen, K. Kaleb, et al. (2026)SkillCraft: can llm agents learn to use tools skillfully?. arXiv preprint arXiv:2603.00718. Cited by: [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [7]J. Chou, A. Liu, Y. Deng, Z. Zeng, T. Zhang, H. Zhu, J. Cai, Y. Mao, C. Zhang, L. Tan, et al. (2025)Autocodebench: large language models are automatic code benchmark generators. arXiv preprint arXiv:2508.09101. Cited by: [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [8]ComposioHQ (2026)Awesome-claude-skills: a curated list of awesome claude skills, resources, and tools. Note: [https://github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)GitHub repository. Accessed: 2026-04-13 Cited by: [§2.3](http://arxiv.org/html/2604.17308v1#S2.SS3.SSS0.Px1.p1.1 "Step 1: seed task collection and skill curation. ‣ 2.3 Task Construction Protocol ‣ 2 SkillFlow ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [9]X. Deng, J. Da, E. Pan, Y. Y. He, C. Ide, K. Garg, N. Lauffer, A. Park, N. Pasari, C. Rane, et al. (2025)Swe-bench pro: can ai agents solve long-horizon software engineering tasks?. arXiv preprint arXiv:2509.16941. Cited by: [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [10]Z. Fang, Z. Liu, J. Liu, H. Chen, Y. Zeng, S. Huang, Z. Chen, L. Chen, S. Zhang, and F. Zhao (2025)DualVLA: building a generalizable embodied agent via partial decoupling of reasoning and action. arXiv preprint arXiv:2511.22134. Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p3.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [11]Google (2025)Gemini CLI: An open-source AI agent that brings the power of Gemini directly into your terminal. Note: [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p1.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [12]R. Han, Z. Fang, X. Sun, Y. Ma, Z. Wang, Y. Zeng, Z. Chen, L. Chen, W. Huang, W. Xu, et al. (2026)UniCorn: towards self-improving unified multimodal models through self-generated supervision. arXiv preprint arXiv:2601.03193. Cited by: [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [13]T. Han, Y. Zhang, W. Song, C. Fang, Z. Chen, Y. Sun, and L. Hu (2026)SWE-skills-bench: do agent skills actually help in real-world software engineering?. arXiv preprint arXiv:2603.15401. Cited by: [Table 2](http://arxiv.org/html/2604.17308v1#A1.T2.27.6.5.1 "In A.1 Comparison ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [14]Harbor Framework Team (2026)Harbor: A framework for evaluating and optimizing agents and models in container environments. Note: [https://github.com/harbor-framework/harbor](https://github.com/harbor-framework/harbor)GitHub repository. Accessed: 2026-04-16 Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p3.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [15]S. Huang, Z. Fang, Z. Chen, S. Yuan, J. Ye, Y. Zeng, L. Chen, Q. Mao, and F. Zhao (2025-11)CRITICTOOL: evaluating self-critique capabilities of large language models in tool-calling error scenarios. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, C. Christodoulopoulos, T. Chakraborty, C. Rose, and V. Peng (Eds.), Suzhou, China. External Links: [Link](https://aclanthology.org/2025.emnlp-main.1355/), [Document](https://dx.doi.org/10.18653/v1/2025.emnlp-main.1355)Cited by: [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [16]S. Huang, Z. Li, Y. Zeng, Q. Ren, Z. Fang, Q. Su, K. Shi, L. Chen, Z. Chen, and F. Zhao (2026)Internalizing meta-experience into memory for guided reinforcement learning in large language models. arXiv preprint arXiv:2602.10224. Cited by: [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [17]W. Huang, Y. Zeng, Q. Wang, Z. Fang, S. Cao, Z. Chu, Q. Yin, S. Chen, Z. Yin, L. Chen, et al. (2026)Vision-deepresearch: incentivizing deepresearch capability in multimodal large language models. arXiv preprint arXiv:2601.22060. Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p3.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [18]C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan (2023)Swe-bench: can language models resolve real-world github issues?. arXiv preprint arXiv:2310.06770. Cited by: [Table 2](http://arxiv.org/html/2604.17308v1#A1.T2.27.3.2.1 "In A.1 Comparison ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [19]X. Li, W. Chen, Y. Liu, S. Zheng, X. Chen, Y. He, Y. Li, B. You, H. Shen, J. Sun, et al. (2026)SkillsBench: benchmarking how well agent skills work across diverse tasks. arXiv preprint arXiv:2602.12670. Cited by: [Table 2](http://arxiv.org/html/2604.17308v1#A1.T2.27.4.3.1 "In A.1 Comparison ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§1](http://arxiv.org/html/2604.17308v1#S1.p2.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§1](http://arxiv.org/html/2604.17308v1#S1.p3.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§2.3](http://arxiv.org/html/2604.17308v1#S2.SS3.SSS0.Px1.p1.1 "Step 1: seed task collection and skill curation. ‣ 2.3 Task Construction Protocol ‣ 2 SkillFlow ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [20]Y. Liang, R. Zhong, H. Xu, C. Jiang, Y. Zhong, R. Fang, J. Gu, S. Deng, Y. Yao, M. Wang, et al. (2026)SkillNet: create, evaluate, and connect ai skills. arXiv preprint arXiv:2603.04448. Cited by: [§4.2](http://arxiv.org/html/2604.17308v1#S4.SS2.p1.1 "4.2 Skills as Procedural Knowledge for Agents ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [21]X. Liu, H. Yu, H. Zhang, Y. Xu, X. Lei, H. Lai, Y. Gu, H. Ding, K. Men, K. Yang, et al. (2023)Agentbench: evaluating llms as agents. arXiv preprint arXiv:2308.03688. Cited by: [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [22]M. A. Merrill, A. G. Shaw, N. Carlini, B. Li, H. Raj, I. Bercovich, L. Shi, J. Y. Shin, T. Walshe, E. K. Buchanan, et al. (2026)Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces. arXiv preprint arXiv:2601.11868. Cited by: [Table 2](http://arxiv.org/html/2604.17308v1#A1.T2.27.2.1.1 "In A.1 Comparison ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [23]Moonshot AI (2024)Kimi cli. Note: [https://github.com/MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli)GitHub repository, commit abc123, Accessed: 2026-04-02 Cited by: [§3.1](http://arxiv.org/html/2604.17308v1#S3.SS1.p2.1 "3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [24]J. Ni, Y. Liu, X. Liu, Y. Sun, M. Zhou, P. Cheng, D. Wang, X. Jiang, and G. Jiang (2026)Trace2Skill: distill trajectory-local lessons into transferable agent skills. arXiv preprint arXiv:2603.25158. Cited by: [§4.2](http://arxiv.org/html/2604.17308v1#S4.SS2.p1.1 "4.2 Skills as Procedural Knowledge for Agents ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [25]OpenAI (2025)Codex CLI: Lightweight coding agent that runs in your terminal. Note: [https://github.com/openai/codex](https://github.com/openai/codex)Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p1.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§3.1](http://arxiv.org/html/2604.17308v1#S3.SS1.p2.1 "3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [26]OpenAI (2026)Introducing gpt-5.3-codex. Note: [https://openai.com/index/introducing-gpt-5-3-codex/](https://openai.com/index/introducing-gpt-5-3-codex/)Cited by: [§2.3](http://arxiv.org/html/2604.17308v1#S2.SS3.SSS0.Px3.p2.1 "Step 3: iterative task-family generalization. ‣ 2.3 Task Construction Protocol ‣ 2 SkillFlow ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [27]S. G. Patil, H. Mao, F. Yan, C. C. Ji, V. Suresh, I. Stoica, and J. E. Gonzalez (2025)The berkeley function calling leaderboard (bfcl): from tool use to agentic evaluation of large language models. In Forty-second International Conference on Machine Learning, Cited by: [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [28]T. Patwardhan, R. Dias, E. Proehl, G. Kim, M. Wang, O. Watkins, S. P. Fishman, M. Aljubeh, P. Thacker, L. Fauconnet, et al. (2025)Gdpval: evaluating ai model performance on real-world economically valuable tasks. arXiv preprint arXiv:2510.04374. Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p3.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§2.3](http://arxiv.org/html/2604.17308v1#S2.SS3.SSS0.Px1.p1.1 "Step 1: seed task collection and skill curation. ‣ 2.3 Task Construction Protocol ‣ 2 SkillFlow ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [29]PinchBench Team (2026)PinchBench: skill-based benchmark for llm agents. Note: [https://github.com/pinchbench](https://github.com/pinchbench)Cited by: [Table 2](http://arxiv.org/html/2604.17308v1#A1.T2.27.5.4.1 "In A.1 Comparison ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§4.2](http://arxiv.org/html/2604.17308v1#S4.SS2.p1.1 "4.2 Skills as Procedural Knowledge for Agents ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [30]Qwen Team (2025)Qwen-code. Note: [https://github.com/QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)GitHub repository, Accessed: 2026-04-02 Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p1.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§3.1](http://arxiv.org/html/2604.17308v1#S3.SS1.p2.1 "3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [31]SkillsMP (2026)SkillsMP: skills marketplace. Note: [https://skillsmp.com/](https://skillsmp.com/)Website. Accessed: 2026-04-13 Cited by: [§2.3](http://arxiv.org/html/2604.17308v1#S2.SS3.SSS0.Px1.p1.1 "Step 1: seed task collection and skill curation. ‣ 2.3 Task Construction Protocol ‣ 2 SkillFlow ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [32]Q. Su, S. Huang, Z. Fang, Z. Chen, Z. Chen, and F. Zhao (2026)Beyond accuracy: unveiling inefficiency patterns in tool-integrated reasoning. External Links: 2604.05404, [Link](https://arxiv.org/abs/2604.05404)Cited by: [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [33]H. Trivedi, T. Khot, M. Hartmann, R. Manku, V. Dong, E. Li, S. Gupta, A. Sabharwal, and N. Balasubramanian (2024)Appworld: a controllable world of apps and people for benchmarking interactive coding agents. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),  pp.16022–16076. Cited by: [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [34]VoltAgent (2026)Awesome-openclaw-skills: the awesome collection of openclaw skills. Note: [https://github.com/VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)GitHub repository. Accessed: 2026-04-13 Cited by: [§2.3](http://arxiv.org/html/2604.17308v1#S2.SS3.SSS0.Px1.p1.1 "Step 1: seed task collection and skill curation. ‣ 2.3 Task Construction Protocol ‣ 2 SkillFlow ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [35]T. Wei, N. Sachdeva, B. Coleman, Z. He, Y. Bei, X. Ning, M. Ai, Y. Li, J. He, E. H. Chi, et al. (2025)Evo-memory: benchmarking llm agent test-time learning with self-evolving memory. arXiv preprint arXiv:2511.20857. Cited by: [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [36]C. S. Xia, Y. Deng, and L. Zhang (2024)Top leaderboard ranking= top coding proficiency, always? evoeval: evolving coding benchmarks via llm. arXiv preprint arXiv:2403.19114. Cited by: [§4.1](http://arxiv.org/html/2604.17308v1#S4.SS1.p1.1 "4.1 Execution Environments and Benchmarks ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [37]P. Xia, J. Chen, H. Wang, J. Liu, K. Zeng, Y. Wang, S. Han, Y. Zhou, X. Zhao, H. Chen, et al. (2026)SkillRL: evolving agents via recursive skill-augmented reinforcement learning. arXiv preprint arXiv:2602.08234. Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p2.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [38]M. Xu, Z. Xu, C. Chi, M. Veloso, and S. Song (2023)Xskill: cross embodiment skill discovery. In Conference on robot learning,  pp.3536–3555. Cited by: [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [39]Y. Yang, J. Li, Q. Pan, B. Zhan, Y. Cai, L. Du, J. Zhou, K. Chen, Q. Chen, X. Li, et al. (2026)AutoSkill: experience-driven lifelong learning via skill self-evolution. arXiv preprint arXiv:2603.01145. Cited by: [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [40]Y. Zeng, W. Huang, Z. Fang, S. Chen, Y. Shen, Y. Cai, X. Wang, Z. Yin, L. Chen, Z. Chen, et al. (2026)Vision-deepresearch benchmark: rethinking visual and textual search for multimodal large language models. arXiv preprint arXiv:2602.02185. Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p3.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [41]H. Zhang, Q. Long, J. Bao, T. Feng, W. Zhang, H. Yue, and W. Wang (2026)MemSkill: learning and evolving memory skills for self-evolving agents. arXiv preprint arXiv:2602.02474. Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p2.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [42]Y. Zhang, M. Li, D. Long, X. Zhang, H. Lin, B. Yang, P. Xie, A. Yang, D. Liu, J. Lin, et al. (2025)Qwen3 embedding: advancing text embedding and reranking through foundation models. arXiv preprint arXiv:2506.05176. Cited by: [§2.3](http://arxiv.org/html/2604.17308v1#S2.SS3.SSS0.Px2.p1.1 "Step 2: task–skill pair matching. ‣ 2.3 Task Construction Protocol ‣ 2 SkillFlow ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [43]B. Zheng, M. Y. Fatemi, X. Jin, Z. Z. Wang, A. Gandhi, Y. Song, Y. Gu, J. Srinivasa, G. Liu, G. Neubig, et al. (2025)Skillweaver: web agents can self-improve by discovering and honing skills. arXiv preprint arXiv:2504.07079. Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p2.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 
*   [44]H. Zhou, S. Guo, A. Liu, Z. Yu, Z. Gong, B. Zhao, Z. Chen, M. Zhang, Y. Chen, J. Li, et al. (2026)Memento-skills: let agents design agents. arXiv preprint arXiv:2603.18743. Cited by: [§1](http://arxiv.org/html/2604.17308v1#S1.p2.1 "1 Introduction ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), [§4.3](http://arxiv.org/html/2604.17308v1#S4.SS3.p1.1 "4.3 Automatic Skill Discovery and Evolution ‣ 4 Related Work ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). 

## Appendix A Benchmark Details

### A.1 Comparison

Table 2:  Comparison between SkillFlow and representative benchmarks from the perspective of skill lifecycle evaluation. Skill Eval denotes whether the benchmark explicitly evaluates the impact of skills; Self-Gen indicates support for self-generated skills; Revision refers to iterative updates or patching of skills; Lifelong denotes sequential accumulation and reuse of skills across tasks; Transfer indicates evaluation of cross-scenario procedural transfer; Traj-Grounded denotes whether skills are extracted from interaction trajectories; Usage Eval indicates whether the benchmark evaluates the alignment between skill utility and actual usage. 

### A.2 Benchmark Statistics

The final benchmark contains 20 task families and 166 tasks organized under five broad domains: Finance & Economics, Operations & Supply Chain, Healthcare & Life Sciences, Governance & Strategy, and Data & Document Intelligence. These five domains cover 20 workflow families in total, with family sizes ranging from 8 to 9 tasks. During construction, more than 200 candidate tasks are generated. Thirty-three of them are filtered out before final inclusion because of environment failures, ambiguity, invalid difficulty ordering, or workflow inconsistency.

### A.3 Workflow Families

This section lists the 20 workflow families by their _workflow-definition names_ rather than internal source identifiers. The grouping is derived from the curated benchmark spreadsheet and uses only the formal family names reported in the main paper.

*   •
Finance & Economics: Industry Correlation Analysis, Financial Statement Rolling, and SEC 13F Financial Analysis.

*   •
Operations & Supply Chain: Supply Chain Replenishment, Production Capacity Planning, Inventory & Finance Integration, DMAIC Quality Analysis, and Operational Recovery Planning.

*   •
Healthcare & Life Sciences: Healthcare Cost-Benefit Analysis and Medical Data Standardization.

*   •
Governance & Strategy: Distribution Center Auditing, Compensation Scenario Modeling, and Document Fraud Detection.

*   •
Data & Document Intelligence: Embedded Data Repair, OCR Data Extraction, HWPX Document Automation, Cross-Format Data Reconciliation, Weighted Risk Assessment, PPT Formatting Optimization, and Sales Pivot Analysis.

### A.4 Workflow Details

Table LABEL:tab:workflow-details provides a compact view of the 20 workflow families. Internal source identifiers are omitted. Instead, the table reports the workflow definition, seed-benchmark lineage, a short task summary, and the corresponding DAEF description. The Source column indicates whether the family is derived from a seed task selected from SkillsBench or GDPval.

Table 3: Workflow Families and Seed-Benchmark Lineage

| Workflow definition | Source | Task summary | DAEF |
| --- | --- | --- | --- |
| Industry Correlation Analysis | SkillsBench | Detrend revenue series for paired industries, compute Pearson correlations, and judge cyclical association. | read source series \rightarrow extract target fields \rightarrow normalize and align time series \rightarrow compute annualized and deflated values \rightarrow compute filtered correlation signals \rightarrow compare cyclical association \rightarrow output scalar result. |
| Financial Statement Rolling | GDPval | Update monthly financial workbooks with reserve merges, accrual rolling, deferred revenue, liabilities, warranties, project cost, rebates, and commissions. | read multi-source ledgers \rightarrow extract target entries \rightarrow filter duplicate and invalid rows \rightarrow align override and adjustment items \rightarrow compute rolling balances \rightarrow compare against control totals \rightarrow update and output summary workbook. |
| SEC 13F Financial Analysis | SkillsBench | Analyze quarterly SEC 13F filings for cross-period reconciliation, fund categorization, holding changes, issuer ownership, and manager comparison. | read multi-period filings \rightarrow extract entity records \rightarrow normalize identifiers \rightarrow align cross-period holdings \rightarrow compute target aggregates \rightarrow compare across periods \rightarrow output structured analysis. |
| Supply Chain Replenishment | GDPval | Produce replenishment plans across categories such as bakery, beauty, frozen meals, household routes, pet care, produce, and snacks. | read inventory and transit data \rightarrow extract target SKUs \rightarrow filter duplicate and invalid rows \rightarrow align master data with arrivals \rightarrow compute coverage and shortage timing \rightarrow compare against replenishment thresholds \rightarrow output detail and action sheets. |
| Production Capacity Planning | GDPval | Build and vary a manufacturing catch-up capacity plan under demand, backlog, overtime, and buffer constraints. | read demand and parameters \rightarrow retrieve initial state \rightarrow compute period-level demand and backlog updates \rightarrow compare candidate resource actions \rightarrow compute overtime and buffer outcomes \rightarrow output planning workbook. |
| Inventory & Finance Integration | GDPval | Integrate replenishment planning with financial rolling scenarios across mixed business contexts. | read multi-source data \rightarrow extract and normalize keys and time windows \rightarrow align inventory and finance records \rightarrow compute rolling deltas and coverage \rightarrow compare against exception rules \rightarrow output structured results. |
| DMAIC Quality Analysis | GDPval | Perform DMAIC Analyze-stage diagnostics across logistics, hospitals, SOC alerts, university IT, DevOps, and field service settings. | read process data \rightarrow extract analysis window \rightarrow filter valid samples \rightarrow compute grouped statistics \rightarrow compare trend and significance signals \rightarrow detect anomalies \rightarrow output structured diagnostics. |
| Operational Recovery Planning | GDPval | Create recovery plans under multi-scenario operational disruptions such as harvesting, data centers, warehouses, manufacturing, radiology, and returns. | read baselines and constraints \rightarrow extract planning horizon \rightarrow compute candidate recovery plans \rightarrow compare capacity and calendar outcomes \rightarrow detect backlog gaps \rightarrow output plan sheets and summaries. |
| Healthcare Cost-Benefit Analysis | GDPval | Compare healthcare supply-chain scenarios under different cycle and batch settings to assess cost-benefit trade-offs. | read inputs and mappings \rightarrow extract and normalize aliases and keys \rightarrow filter valid records and exclusions \rightarrow align coverage with adjustments \rightarrow compute revenue cost and margin scenarios \rightarrow compare trade-off thresholds \rightarrow output structured conclusions. |
| Medical Data Standardization | SkillsBench | Standardize medical laboratory data across units, precision rules, and formatting conventions. | read raw tables and templates \rightarrow extract valid rows \rightarrow align with target schema \rightarrow normalize numeric formats and units \rightarrow detect anomalies or missing values \rightarrow validate required precision \rightarrow output standardized file. |
| Distribution Center Auditing | GDPval | Audit distribution-center records for inventory discrepancies, outbound lists, receiving anomalies, return handling, SLA compliance, labor, and trailer detention. | read source data \rightarrow extract audit fields \rightarrow compute row-wise rule checks \rightarrow detect violations and anomalies \rightarrow compare totals across dimensions \rightarrow output audit artifacts. |
| Compensation Scenario Modeling | GDPval | Build and refresh multi-year compensation models for organizations such as orchestras, universities, property firms, airlines, and construction teams. | read assumptions and master data \rightarrow retrieve model structure and references \rightarrow align base records across sheets \rightarrow compute period-wise compensation values \rightarrow update and compare scenario indicators \rightarrow output completed model. |
| Document Fraud Detection | SkillsBench | Review commercial documents across clinics, trials, maintenance logs, travel, and cold-chain records to detect inconsistencies and suspicious items. | read source documents \rightarrow extract candidate records and references \rightarrow normalize names and identifiers \rightarrow align cross-document evidence \rightarrow compare claimed facts with authorizations \rightarrow detect anomaly types \rightarrow output structured flags. |
| Embedded Data Repair | SkillsBench | Repair or refresh embedded spreadsheet objects inside PowerPoint files for domains such as chemistry, catalysts, or foreign exchange. | read document container \rightarrow extract embedded tables and target cells \rightarrow retrieve label mappings \rightarrow update cell values and formulas \rightarrow validate dependencies \rightarrow output repaired document. |
| OCR Data Extraction | SkillsBench | Extract structured records from scanned images such as legal settlements, measurements, orders, invoices, fuel slips, and medicine labels. | read scanned images \rightarrow extract OCR fields and target records \rightarrow normalize dates amounts and codes \rightarrow align with template rows \rightarrow validate supplemented references \rightarrow output structured results. |
| HWPX Document Automation | SkillsBench | Fill Korean HWPX templates for clinics, announcements, inventory, proposals, renewals, audits, vendor directories, and training feedback. | read templates and data sources \rightarrow extract placeholders and values \rightarrow normalize transformed values and enumerations \rightarrow update filled content and structure \rightarrow validate document integrity \rightarrow output completed file. |
| Cross-Format Data Reconciliation | SkillsBench | Compare archived PDF snapshots with current Excel data to find added, deleted, or modified records across domains. | read archived snapshot and current spreadsheet \rightarrow extract primary keys and records \rightarrow normalize and align across formats \rightarrow compare additions deletions and modifications \rightarrow detect field-level differences \rightarrow output structured results. |
| Weighted Risk Assessment | SkillsBench | Implement weighted risk formulas in Excel for scenarios such as API SLA, campus budgeting, factories, hospitals, energy, cloud reliability, and ports. | read workbook and lookup tables \rightarrow retrieve input and output ranges \rightarrow update formulas with target cells \rightarrow compute weighted indicators and risk scores \rightarrow validate workbook consistency \rightarrow output result workbook. |
| PPT Formatting Optimization | SkillsBench | Normalize image-title formatting in PowerPoint decks by unifying fonts, positions, and index pages. | read presentation objects \rightarrow extract target titles and tags \rightarrow normalize text font and layout attributes \rightarrow update positions and alignment \rightarrow validate summary-page consistency \rightarrow output formatted document. |
| Sales Pivot Analysis | SkillsBench | Build pivot-style analysis from PDF catalogs and Excel transaction data for sales, budgets, payroll, registration, inventory, libraries, quality, and grades. | read multi-source data \rightarrow extract and normalize fields and dimensions \rightarrow align supplementary joins \rightarrow compute pivot indicators \rightarrow compare grouped summaries \rightarrow output report workbook. |

### A.5 DAEF Node Vocabulary

Table[4](http://arxiv.org/html/2604.17308v1#A1.T4 "Table 4 ‣ A.5 DAEF Node Vocabulary ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") lists the controlled node labels used when annotating seed-task workflow graphs. The vocabulary is intentionally compact and coarse-grained so that it captures transferable procedural roles rather than low-level commands or domain-specific business concepts.

Table 4: Controlled DAEF Node Vocabulary

##### DAEF Annotation Rules.

The annotation process follows five rules. First, each task is annotated with 5–8 meta-step nodes. Second, node labels must be selected only from the controlled vocabulary in Table[4](http://arxiv.org/html/2604.17308v1#A1.T4 "Table 4 ‣ A.5 DAEF Node Vocabulary ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), and annotators are not allowed to invent new labels. Third, dependency edges are directed from prerequisite operations to subsequent operations, and cycles are not permitted. Fourth, when two operations can be executed in parallel, both are connected to the same downstream node. Fifth, after annotation, annotators must provide a brief operational rationale in one sentence explaining why each node label is selected.

##### DAEF Agreement Screening.

To verify that a seed task admits a stable workflow abstraction, two expert annotators independently produce DAEF annotations for each candidate task in the final screening pool, which yields 30 retained tasks after screening. The annotators then score the other annotator’s graph against their own judgment, checking agreement on the meta-step decomposition, node labels, and dependency structure. A candidate passes only when both annotators judge the two annotations to be mutually consistent. Otherwise, we treat the seed task as lacking a stable execution workflow and discard it from benchmark construction.

### A.6 Allowed Surface Variation Types

Table[5](http://arxiv.org/html/2604.17308v1#A1.T5 "Table 5 ‣ A.6 Allowed Surface Variation Types ‣ Appendix A Benchmark Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") summarizes the variation dimensions that annotators may allow within a family while preserving a shared DAEF. These dimensions are intended to alter surface realization and difficulty without introducing a new workflow core.

Table 5: Allowed Surface Variation Types Within a DAEF Family

### A.7 Human Verification Checklist

Human reviewers inspect each candidate family with the following checklist:

*   •
Solvability: a correct solution path exists under the provided environment and assets.

*   •
Logical consistency: instructions, assets, and expected outputs do not contradict one another.

*   •
Environment closure: the task can be completed with the provided files, tools, and runtime.

*   •
Difficulty ordering: later tasks in a family are not easier than earlier tasks under the intended curriculum.

*   •
No skill leakage: instructions do not reveal which exact skill should be used.

For family acceptance, reviewers additionally assess whether the candidate tasks satisfy the DAEF membership rule:

*   •
Shared operation inventory: the core operation types are consistent across tasks.

*   •
Shared dependency topology: these operations follow the same dependency pattern rather than merely similar names.

*   •
Grounding variation only: differences arise from domain entities, file formats, noise, scale, or instruction phrasing rather than from a new workflow core.

*   •
Transfer plausibility: a procedure learned on earlier tasks should plausibly transfer to later tasks without requiring a new workflow.

## Appendix B Skill Evolution Details

### B.1 Skill Patch Format

Each skill patch in the current framework is represented as a JSON object with three top-level fields:

*   •
summary: a natural-language description of the newly extracted lesson or repair.

*   •
upsert_files: a mapping from file paths to new or updated file contents.

*   •
delete_paths: a list of obsolete files to remove from the skill library.

This schema is used as a minimal auditable interface for file-level updates rather than as an optimal or exhaustive formalism for skill evolution. Its purpose is to make patch history inspectable, support update tracking over time, and make failure modes such as uncontrolled skill growth directly visible when redundant or low-value content accumulates.

### B.2 Skill Patch Generation Prompt Template

The following appendix presents the prompt template used for skill patch generation. For readability, we separate the system-level instruction from the user-level prompt template and render them as boxed templates.

### B.3 Skill Library Growth and Composition

Figure[8](http://arxiv.org/html/2604.17308v1#A2.F8 "Figure 8 ‣ B.3 Skill Library Growth and Composition ‣ Appendix B Skill Evolution Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") and Figure[8](http://arxiv.org/html/2604.17308v1#A2.F8 "Figure 8 ‣ B.3 Skill Library Growth and Composition ‣ Appendix B Skill Evolution Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") provide two complementary views of how the external skill library evolves during sequential evaluation. The first figure tracks the cumulative number of stored skills as tasks progress, while the second summarizes the file-type composition of the resulting skill libraries.

![Image 7: Refer to caption](https://arxiv.org/html/2604.17308v1/x7.png)

Figure 7: Skill Count Growth by Task. The figure shows how the cumulative number of stored skills changes as the agent proceeds through sequential tasks, which helps reveal whether different models consolidate experience into a compact library or continue to expand the library over time.

![Image 8: Refer to caption](https://arxiv.org/html/2604.17308v1/x8.png)

Figure 8: Skill File-Kind Composition. The figure summarizes the composition of file kinds contained in the evolved skill libraries, which helps characterize whether different models tend to store compact procedural summaries, auxiliary files, or more fragmented collections of artifacts.

## Appendix C Experiments and Analysis Details

### C.1 Metric Notes

The main text emphasizes aggregate task completion, efficiency statistics (turns, monetary cost, and output tokens), and statistics of skill generation and reuse because these signals are consistently available across the systems reported in Table[1](http://arxiv.org/html/2604.17308v1#S3.T1 "Table 1 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"). In Table[1](http://arxiv.org/html/2604.17308v1#S3.T1 "Table 1 ‣ 3.1 Experimental Setup ‣ 3 Experiments ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents"), Final #Skills denotes the cumulative number of skills generated while completing a task family, and %use denotes the percentage of tasks in which the agent reads or calls at least one previously stored skill.

### C.2 Historical-Trajectory Context Control

To test whether the gain of the full protocol can be explained by access to longer raw histories alone, we run a single-model control on Claude Opus 4.6 in which the agent receives the full prior interaction history as additional context, but does not externalize that experience into a skill library. Table[6](http://arxiv.org/html/2604.17308v1#A3.T6 "Table 6 ‣ C.2 Historical-Trajectory Context Control ‣ Appendix C Experiments and Analysis Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") compares this setting against the vanilla baseline and the full protocol. In this comparison, the history-context setting reaches 47.41% completion, which is 15.24 points below vanilla and 23.67 points below the full protocol. While this control does not isolate every factor and is limited to one model, it suggests that simply appending raw historical trajectories is not sufficient to recover the benefit of the full protocol; the observed gain is more consistent with structured externalization into reusable skills than with longer context alone.

Table 6: Single-model control on Claude Opus 4.6. The history-context setting prepends the full prior interaction history as additional context, without externalizing the experience into skills.

### C.3 Additional Efficiency Pareto Views

Figure[9](http://arxiv.org/html/2604.17308v1#A3.F9 "Figure 9 ‣ C.3 Additional Efficiency Pareto Views ‣ Appendix C Experiments and Analysis Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") and Figure[10](http://arxiv.org/html/2604.17308v1#A3.F10 "Figure 10 ‣ C.3 Additional Efficiency Pareto Views ‣ Appendix C Experiments and Analysis Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") provide complementary Pareto views of task completion against interaction turns and output tokens.

![Image 9: Refer to caption](https://arxiv.org/html/2604.17308v1/x9.png)

Figure 9: Completion–Interaction Turns Pareto Frontier. This view complements the main-text cost frontier by showing whether gains from skill evolution come with longer or shorter interaction sequences under the same evaluation setting.

![Image 10: Refer to caption](https://arxiv.org/html/2604.17308v1/x10.png)

Figure 10: Completion–Output Tokens Pareto Frontier. This figure highlights the efficiency trade-off between task success and generated output volume, which is useful for diagnosing verbosity-driven gains or regressions across wrappers.

### C.4 Full Skill-Gain Heatmap

Figure[11](http://arxiv.org/html/2604.17308v1#A3.F11 "Figure 11 ‣ C.4 Full Skill-Gain Heatmap ‣ Appendix C Experiments and Analysis Details ‣ SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents") provides a family-level complement to the coarse domain-grouped heatmap shown in the main text. It resolves the benchmark into individual workflow families and gives a more granular view of where skill evolution yields large gains, negligible changes, or regressions.

![Image 11: Refer to caption](https://arxiv.org/html/2604.17308v1/x11.png)

Figure 11: Family-Level Skill-Gain Heatmap. Compared with the coarse domain-grouped heatmap in the main text, this appendix figure resolves individual workflow families so that localized gains, flat regions, and regressions can be inspected in detail.

## Appendix D Full Trajectory

### D.1 Skill Evolution Patch

### D.2 Weighted Hospital Bedflow Trajectory

This appendix presents the weighted hospital bedflow interaction trace reformatted using the same boxed dialogue style as the appendix example. The task is an Excel formula completion problem. The trajectory is notable because the agent first follows a reasonable spreadsheet-editing workflow, then encounters the well-known _formula-vs-cached-value_ issue, diagnoses that intermediate XML patching corrupted formula cells, and finally restarts from the original workbook to produce a verified result.

#### Session Metadata

#### Task Instruction

#### Conversation Trajectory

### Key Takeaways

### D.3 FAILURE TAXONOMY EXAMPLES

#### D.3.1 Verifier Toolchain Mismatch

#### D.3.2 Missing Cached Values

#### D.3.3 Incomplete Verification
