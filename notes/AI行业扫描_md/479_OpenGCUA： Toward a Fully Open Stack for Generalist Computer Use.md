# OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use

**作者：** Hanzhang Zhou*, Long Li*, Quyu Kong*, Lei Wang*, Panrong Tong*, Long Chen, Tianyu Xia, Gongjie Zhang,

Xu Zhang, Chen Liu, Jianan Zhang, Chenglin Cai, Zhengwen Zeng, Steven Hoi, Yue Wang$\dagger$

Alibaba Token Hub, Alibaba Group

**来源：** arXiv 2610.22200v1  ￼

**原文链接：** https://arxiv.org/html/2610.22200v1

###### Abstract

Computer use has reached a turning point: the focus is expanding from GUI-only interaction to systems that complete tasks on users’ computers through visual and programmatic interfaces.
We define a generalist computer-use agent (GCUA) as a system in which the model chooses how to observe, act, and organize its work across visual and programmatic interfaces.
Yet frontier implementations, such as GPT-6 Astra’s computer-use system, remain largely closed, limiting systematic study of their design.
We introduce Open Generalist CUA (OpenGCUA), an ongoing project to develop and open the full stack for GCUAs with the community.

This report presents the first release of Open Generalist CUA.
Code execution is a key feature of our agent design: it lets intermediate results determine subsequent operations and enables models to apply their existing programming capabilities directly to computer interaction.
We also propose harness-to-model decision transfer, moving selected observations and task-state decisions from fixed harness rules to the model.
On OSWorld-v2, our full configuration improves task scores across all eight evaluated models, including GPT-6 Astra and Claude Opus 5, raising mean partial score by +19.6 points and reducing reported steps per task by an average of 53.0% relative to batched GUI-only execution.
We release our implementation and prompts, evaluation trajectories from all eight models, and preliminary versions of a real-device harness and a cross-device SDK.
The harness addresses real-device challenges not fully captured by benchmarks, while the SDK provides a common programming interface across computers, mobiles and browsers.
Across four real macOS tasks under our real-device harness, selected Qwen3.8-Max runs use 19.4 times as many reported reasoning tokens as GPT-6 Astra, highlighting substantial differences between models in real-device execution efficiency.

[OpenGCUA GitHub](https://github.com/Tongyi-MAI/OpenGCUA)  [Project Website & Interactive Lab](https://tongyi-mai.github.io/OpenGCUA/)

![Refer to caption](2610.22200v1/OpenGCUA_osw2_v10_C_reasoning_compact_same_order.png)

Figure 1: On the offline set of OSWorld-v2, OpenGCUA improves all eight frontier models, raising mean partial score by 19.6 points and reducing steps per task by 53%. On real-device, the gap between models remains large: Qwen3.8-Max uses 19.4$\times$ GPT-6 Astra’s reasoning tokens but completes fewer tasks.

Contents

## 1 Introduction

Computer use has moved to the center of attention. The GPT-6 Astra release places strong emphasis on computer use, with extensive demonstrations offering an exciting vision of what computer-use agents could make possible ([OpenAI, 2026c](#bib.bib19)).
Much of the literature studies computer-use agents (CUAs) as GUI-only agents, asking how well models can complete computer tasks through screenshot-based observation and mouse and keyboard actions ([Qin et al., 2025](#bib.bib20); [Lu et al., 2026](#bib.bib14)).
Recent frontier systems, however, combine GUI interaction with shell commands, accessibility-tree access, and other tools, and OpenAI now recommends code execution, writing GUI operations as code and combining them with programmatic operations in a single model output ([OpenAI, 2026b](#bib.bib18)).
These systems also target tasks on users’ own computers, where shared control, interaction with background windows, and evolving requests introduce challenges not fully captured by benchmarks.
The question has changed, from how well a model operates a GUI interface to how well a system completes work on a real computer by whatever means works. We take this as a turning point in computer-use research, motivating a clearer definition of these broader agents and a systematic study of their design.

We therefore adopt the term generalist computer-use agent (GCUA) to characterize this broader class of systems, following the system-level perspective of Agents’ Last Exam ([Sun et al., 2026](#bib.bib22)). GPT-6 Astra’s computer-use system is a representative GCUA. We define a GCUA as an agent system designed to complete diverse computer tasks through both visual interaction and programmatic access, in which the model decides how to observe, act, and organize its work as the task requires. Programmatic access includes shell commands, accessibility APIs, and application or service APIs where available.
Essentially, a GCUA chooses how to use the computer to complete a task, rather than being restricted to GUI interaction. Our previous work, Qwen-UI-Agent, began exploring this direction through a unified GUI and CLI action space with batched actions ([Zhou et al., 2026](#bib.bib30)). Within our formulation, such GUI+CLI hybrid CUA is a special case of GCUA (Section [2](#S2)).

How to design such systems is an open question.
A GCUA raises design questions that go beyond those of GUI-only agents: which interfaces to give the model, how to support code execution, which decisions to leave to the model and which to the harness, and what changes when the agent runs on a user’s own computer.
However, frontier systems such as GPT-6 Astra remain largely closed ([OpenAI, 2026a](#bib.bib17)).
Their model weights, full prompting setups, real-device harnesses, device-control SDKs, and execution trajectories are not available.
This limits the community’s ability to reproduce system behavior, compare alternative designs, and investigate how design choices and execution mechanisms affect task completion and cost, particularly under real-device conditions.

We therefore introduce Open Generalist CUA (OpenGCUA), an ongoing project to develop and open the full stack for generalist computer use with the community (Figure [2](#S1.F2)):
(1) Model. Develop a model that unifies computer and browser use, with code execution and harness-to-model decision transfer central to its agent design.
(2) System. A real-device harness that runs on users’ real machines, and lessons we learned in moving from benchmark harnesses to real-device deployment. A cross-device SDK that gives agent programs one interface to computers, browsers, and phones, supporting tasks that span multiple devices.
(3) Trajectories. Release trajectories from evaluations of frontier models such as GPT-6 Astra to support analysis of code-execution and harness-to-model decision transfer patterns.
(4) Efficiency. Systematically study and improve GCUA execution efficiency through code-execution, concise model reasoning, and harness optimization, while exploring broader system-level improvements.
(5) Evaluation. Develop evaluation environments and benchmarks on real devices, particularly on macOS, to assess agents’ ability to complete tasks under real-world operating conditions.

![Refer to caption](2610.22200v1/fig2_v3_candidate_B.png)

Figure 2: Overview of Open Generalist CUA.

This report presents the first release of the OpenGCUA project. The release does not yet include a trained model. The report covers agent design and evaluation, execution trajectories from frontier models, and preliminary versions of the real-device harness and cross-device SDK, together with a roadmap for subsequent releases. Our main contributions are as follows.

•

GCUA generalizes existing GUI, CLI, and hybrid agents.
We define a GCUA by three decisions that its model makes at each step: what to observe, how to act, and how to organize its work. We show that GUI agents, CLI agents, multi-agent hybrids, and GUI+CLI agents such as Qwen-UI-Agent each fix some of these decisions in advance, and are special cases of GCUA (Section [2](#S2)).

•

GCUA outperforms GUI-only CUA on every frontier model we test.
We implement our GCUA agent design into the OpenGCUA harness, which lets existing models use code execution and harness-to-model decision transfer. We test it with eight frontier models, including GPT-6 Astra and Claude Opus 5. On the offline set of OSWorld-v2, the full GCUA setting raises the mean partial score by 19.6 points, cuts steps per task by 53.0%, and narrows the score gap between the strongest and weakest models by more than half. We release the implementation, prompts, and evaluation trajectories of all eight frontier models (Section [3](#S3)).

•

Code execution adds value beyond shell access.
With the same GUI and shell access, writing GUI operations as code and combining them with programmatic operations adds 6.1 points to the mean partial score and cuts steps per task by 14.8% against the GUI+CLI baseline.
Code execution offers two advantages: intermediate results can decide the next operation without another model call, and models can bring their existing programming ability directly to computer interaction. We further identify five recurring patterns of code execution in our case study (Section [3.1](#S3.SS1)).

•

Harness control should move into the model as models improve.
Harnesses fix many workflow decisions by rule, such as taking a screenshot after every step. We propose harness-to-model decision transfer, which delegates these harness decisions to the model. In the current implementation, the model decides when to request screenshots and how to track task state. It also states each program’s purpose before execution. On-demand observation alone increases cache hit rates by 10.5 and 14.4 percentage points for two models without lowering task scores (Section [3.2](#S3.SS2)).

•

On real devices, a large gap lies in the model.
We release a preliminary real-device harness for users’ own computers, addressing challenges unseen in benchmarks, such as sharing the machine with its user and acting on background windows. With the harness held fixed, Qwen3.8-Max uses 19.4 times as many reasoning tokens as GPT-6 Astra on four real macOS tasks, and 5.7 times as many output tokens in total. Case studies trace this gap to model behavior: large reasoning cost for simple operations, difficulty adapting to real-device conditions and a gap in code execution capability (Section [4](#S4)).

•

One Programming Interface for Computers, Browsers, and Phones.
The preliminary Cross-Device SDK binds every operation to an explicit device, application, window, or tab, keeps accessibility and vision as separate ways to observe and act, and allows one program to coordinate several devices within a task (Section [4.2](#S4.SS2)).

This release does not mark the project’s completion, and the harness and SDK remain preliminary.
Section [5](#S5) outlines our research plans and release milestones for Open Generalist CUA.

## 2 Generalist CUA: Definition and Positioning

### 2.1 Definition

Agents’ Last Exam takes a system-level view and decomposes an agent into five layers: the model (Brain), GUI perception (Eyes), orchestration (Body), tools (Hands), and a runtime (Feet) ([Sun et al., 2026](#bib.bib22)). Under this view, a CLI agent lacks GUI perception, a GUI agent lacks most of the remaining layers, and a generalist agent spans all five.
Having all five layers, however, only means an agent can act through both the GUI and the CLI; it does not mean that the agent chooses well between them.
At a given step, an agent may click through a dozen screens to do what a single shell command would do, or run a script when it first needs to look at the screen. The layer view cannot tell such an agent apart from one that picks the right way to act at each step.
In this report, we therefore define a generalist CUA (GCUA) by the decisions it makes at each step, not by the components it contains.

A GCUA makes three decisions at each step: what to observe, how to act, and how to organize.

•

What to Observe. The observation can be a screenshot, an accessibility tree (AX Tree), the output of a command, the response of an API, or any combination of these. The model decides which it needs, including whether it needs a new screenshot at all.

•

How to Act. The action can be a GUI operation at a screen coordinate, an operation on an accessibility element, a shell command, an API call, or a program that combines several of these. The model decides which fits the step.

•

How to Organize. Across steps, the agent keeps a plan, tracks what has been done, and decides which past observations stay in context. Most harnesses fix these as rules set by the developer. In a GCUA, the model makes these decisions as the task requires.

##### Four Interfaces.

The first two decisions range over four interfaces to the computer, and each offers both a way to observe and a way to act.

•

GUI. The agent sees a screenshot and clicks, drags, scrolls, or types at a screen coordinate. This is the interface that always works, since every application has pixels.

•

Accessibility Tree. The agent reads the elements of a window, with their roles, names, and values, and operates on an element directly. It needs no coordinate, does not bring the window to the front, and never moves the user’s pointer on real devices.

•

CLI. The agent runs shell commands and reads their output. This is the natural route for files, data, and software.

•

API. The agent calls external services, such as web search, and reads their responses. This reaches what neither the screen nor the shell can.

Each interface offers both a way to observe and a way to act, and each has its own strength. No single interface is best for every step, so what matters is choosing the right one at each step and combining them when a step needs more than one.

Putting these together yields the definition used throughout the report: A GCUA is an agent system designed to complete diverse computer tasks through both visual interaction and programmatic access, in which the model decides how to observe, act, and organize its work as the task requires.
This definition refines that of ALE rather than replacing it. Visual interaction and programmatic access require all five layers, and our definition further asks who makes the decisions within them.

##### Formalization.

Let $s_{t}$ be the state of the computer at step $t$, $m_{t}$ the agent’s working state, and $o_{t}$ the observation returned by the previous step, with $m_{0}$ containing the task instruction. At each step, a GCUA policy $\pi_{\theta}$ makes the three decisions jointly:

$(q_{t},\ p_{t},\ m_{t+1})\sim\pi_{\theta}(\cdot\mid m_{t},\ o_{t}).$

What to observe: CLI/API output is returned automatically. The model selects additional views through $q_{t}\subseteq\mathcal{Q}=\{\text{screenshot},\text{AX tree}\}$, where $q_{t}=\emptyset$ means that no additional view is requested.
How to act: $p_{t}$ is a program whose statements call primitives in $\mathcal{A}=\mathcal{A}_{\mathrm{GUI}}\cup\mathcal{A}_{\mathrm{AX}}\cup\mathcal{A}_{\mathrm{CLI}}\cup\mathcal{A}_{\mathrm{API}}$ and may use loops, branches, and variables. A single primitive call is the simplest program.
How to organize its work: $m_{t+1}$ is the updated working state, including the plan, the record of progress, and the observations kept in context.
Executing $p_{t}$ moves the computer to $s_{t+1}$ and produces an execution output $e_{t}$, such as command output or API responses. The next observation is

$o_{t+1}=\bigl(e_{t},\ \{v_{q}(s_{t+1})\}_{q\in q_{t}}\bigr),$

where $v_{q}$ renders view $q$ of the computer state.
The model therefore observes both the views it requests through $q_{t}$, such as a screenshot or an accessibility tree, and what its program prints in $e_{t}$.

##### A Special Case: GUI+CLI Agents.

Our recent GUI+CLI agent, Qwen-UI-Agent ([Zhou et al., 2026](#bib.bib30)), released shortly before GPT-6 Astra, is an instructive special case of Eq. ([1](#S2.E1)). It places GUI and CLI actions in one action space and lets the model emit a batch of several actions in one call. In our notation, it fixes

$q_{t}\equiv\{\text{screenshot}\},\qquad p_{t}=(a_{1},\dots,a_{n}),\ a_{i}\in\mathcal{A}_{\mathrm{GUI}}\cup\mathcal{A}_{\mathrm{CLI}},\qquad m_{t+1}=h(m_{t},o_{t}),$

where $h$ is a fixed harness rule, such as keeping the last $k$ screenshots. The model already chooses, action by action, whether to click or to run a command, and this alone improved both success and efficiency over GUI-only execution.
GCUA lifts each of these three constraints. Where the GUI+CLI agent emits a fixed sequence $(a_{1},\dots,a_{n})$, a GCUA writes a program over the full set $\mathcal{A}$, which adds accessibility and API operations as well as loops, branches, and variables. Inside such a program, a click, an accessibility operation, a shell command, and an API call are simply four kinds of statements. Where the GUI+CLI agent receives a screenshot after every step, a GCUA decides which views to request, including none at all. And where the GUI+CLI agent follows the harness rule $h$, a GCUA decides for itself what to keep in its working state.
In our formulation, batched GUI+CLI hybrid agents are a restricted case of GCUA.

### 2.2 Relation to Existing Agents

The formalization in Eq. ([1](#S2.E1)) also lets us compare GCUA with existing agents. Each existing family can be written in the same form, except that some of the three decisions (what to observe, how to act, and how to organize) are fixed in advance instead of being made by the model at each step. Table [1](#S2.T1) lists what each family fixes, and the paragraphs below discuss each family in turn.

Table 1: Existing agent families and GCUA compared on the three decisions. Gray text gives the formal notation. The observation after each step contains the views selected by $q_{t}$ and the execution output $e_{t}$ (Eq. [2](#S2.E2)). Existing families fix some of these decisions in advance. The shaded rows mark the path this report follows, from our earlier GUI+CLI agent to GCUA, in which the model makes all three decisions at each step.

##### GUI Agents.

A GUI agent fixes all three decisions ([Qin et al., 2025](#bib.bib20); [Wang et al., 2025b](#bib.bib25); [Lu et al., 2026](#bib.bib14)). It always observes a screenshot, so $q_{t}\equiv\{\text{screenshot}\}$. It acts through one GUI operation per step, so $p_{t}$ is a single primitive in $\mathcal{A}_{\mathrm{GUI}}$. Its working state follows a harness rule $m_{t+1}=h(m_{t},o_{t})$, such as keeping the last $k$ screenshots. The model still chooses where to click, but not what to observe, which interface to use, or what to keep.

##### CLI Agents.

A CLI agent fixes what it observes and restricts how it acts. It has no view of the screen, so $q_{t}\equiv\emptyset$ and it sees only the execution output $e_{t}$. It acts only through the shell, so $p_{t}$ is a program over $\mathcal{A}_{\mathrm{CLI}}$. It is more flexible than a GUI agent. Its commands and scripts can use loops, branches, and variables. Recent coding agents also let the model decide part of how it organizes its work, for example by summarizing earlier context when it grows long ([Anthropic, 2025](#bib.bib3); [OpenAI, 2025](#bib.bib16)). What a CLI agent cannot do is operate an application that can only be used through its graphical interface. Agent frameworks such as OpenClaw support more than the shell, but they also come without built-in GUI control ([Sun et al., 2026](#bib.bib22)).

##### Multi-Agent Hybrid Systems.

Some recent systems combine GUI and programmatic control by dividing the work among several agents. For example, an orchestrator splits a task into subtasks and sends each one to either a GUI operator or a programmer ([Song et al., 2026](#bib.bib21)). Each sub-agent has its own fixed interface. The GUI operator sees screenshots and acts through GUI operations, and the programmer writes and runs code. In terms of Eq. ([1](#S2.E1)), while sub-agent $k$ handles a subtask, $q_{t}$ and $p_{t}$ are limited to its own sets $\mathcal{Q}_{k}$ and $\mathcal{A}_{k}$. Together, the sub-agents cover the same interfaces as a GCUA. The difference is where the choice of interface is made. In these systems, the orchestrator makes it once per subtask. In a GCUA, a single model makes it at every step, and one program can combine several interfaces.

### 2.3 Why Now: The Route Flip to Code Execution

In 2026, the frontier began to shift from clicking toward programming, and the shift is visible in vendor documentation rather than only in benchmark scores.
With the release of GPT-6 Astra, OpenAI’s computer-use guide began recommending that models write and run short programs, for example with PyAutoGUI or Playwright, rather than rely primarily on the earlier computer tool for mouse and keyboard actions ([OpenAI, 2026b](#bib.bib18)). The guide’s examples reflect this shift: the computer tool still targets the previous model (i.e., GPT-5.6 Sol), while code-execution examples use GPT-6 Astra. A similar pattern appears on OSWorld-v2, where frontier agents perform more actions through code, APIs, and file operations rather than clicks ([Yuan et al., 2026](#bib.bib28)).
OpenAI also reports that GPT-6 Astra completes OSWorld 2.0 tasks in about 47% less time than GPT-5.6 Sol and is 1.9$\times$ faster on Mind2Web ([OpenAI, 2026c](#bib.bib19)).
OpenAI does not say how much of this gain comes from code execution, but it is the kind of gain one would expect when each model call does more work.

Code Execution versus Batched Actions. With batched actions, each model call yields a list of actions that were fixed when the call was generated: the model must decide every click before it sees the result of the first one. With code execution, each model call yields a program, and control flow is decided while the program runs. Three things become possible in a single call that were impossible before: a condition (if the dialog is visible, dismiss it), a loop (for each row, fill the three fields), and a verification (assert the status now reads Saved). A task that took a dozen round trips becomes one. This is also why batched actions, which our earlier work introduced ([Zhou et al., 2026](#bib.bib30)), are a stepping stone rather than an endpoint: a batch is a program without control flow.

### 2.4 Efficiency as a First-Class Metric

Success rate remains our primary measure, but it does not capture the resources required to complete a task.
For interactive tasks, an important threshold is reached when delegation delivers results sooner than manual execution, potentially saving both human effort and time to completion.
We therefore evaluate efficiency using four metrics: steps per task, output tokens, reasoning tokens, and cost.

Each step is one model call, which may generate multiple actions through batching or code execution.
Fewer steps reduce model-call overhead, while fewer output tokens can lower generation time and cost.
Reasoning tokens are included in output tokens but reported separately.
When reasoning accounts for a large share of output, reducing unnecessary reasoning can improve efficiency without shortening the executable code, provided task performance is maintained.
We compute cost from input and output token usage at each model’s published prices, including cache discounts.

## 3 Agent Design: Code Execution and Harness-to-Model Decision Transfer

This section studies two behaviors we aim to develop in GCUA models. The first is code execution, which concerns how to act: the model combines graphical interaction and programmatic operations within a single program. The second is harness-to-model decision transfer, which concerns what to observe and how to organize: the model makes selected workflow control decisions that a harness would otherwise fix with rules, such as when to look at the screen and how to organize task state. This release does not introduce a trained model. Instead, we study how the prompts, tool interfaces, and execution runtime of Open Generalist CUA support these behaviors in existing frontier models. We first explain the design and illustrate it with execution trajectories, then evaluate its effects on task completion and cost.

### 3.1 Code Execution over GUI and CLI

Code execution gives graphical interaction and programmatic operations a unified executable form. The model writes a program in which GUI actions, such as pyautogui.click(), can be combined with shell commands and Python computation. The model can therefore specify not only what operations to perform, but also how execution should proceed. Loops and conditional logic allow the program to repeat operations and choose subsequent actions based on intermediate results, without requiring a new model call for each operation. On OSWorld-v2, this design improves Qwen3.8-Max’s mean task score by 5.2 points and reduces steps per task by 17.0% relative to a hybrid CUA baseline with batched GUI+CLI actions (Section [3.3](#S3.SS3)).

#### 3.1.1 Implementation

Prompt Design.
The system prompt specifies the programming interfaces and output format for code execution. The OSWorld-v2 configuration specifies PyAutoGUI for desktop interaction and the Python function bash() for executing shell commands.
The prompt for the real-device harness additionally describes Playwright for browser interaction. The prompt requires one Python program in a <code> block per step and includes examples that combine interface operations, shell commands, and checks on intermediate results. The full prompt is given in Appendix [C](#A3).

Program Execution.
The harness extracts and syntax-checks the code block, then executes it in the computer environment. The runtime supports desktop interaction through PyAutoGUI and, in the real-device harness, browser interaction through Playwright.
Shell commands execute through bash(), which returns command output and exit status. The Python control flow coordinates these calls, allowing loops and conditions to combine GUI and shell operations within one program.

Execution Feedback.
The harness returns captured standard output, standard error, and execution status to the model. With on-demand observation enabled, observations include a new screenshot when the program requests one through the screenshot() action. The real-device harness additionally returns accessibility-tree observations when requested by the model.
We have open-sourced both the preliminary real-device harness and the code execution harness.

#### 3.1.2 Representative Code-Execution Patterns

The implementation specifies what a program can contain, but we want to see how models actually write programs to solve concrete tasks.
We therefore examine GPT-6 Astra on OSWorld-v2, and find five recurring patterns in how its programs connect actions, intermediate results, and model observations. The examples illustrate complementary uses of code, rather than mutually exclusive categories or isolated performance gains.

![Refer to caption](2610.22200v1/patterns_execution_v2.png)

Figure 3: Programs coordinate actions and checks.
(a) GUI clicks alternate with checks of generated contracts and local drafts.
(b) A loop visits seven webpage sections and checks each active section through the DOM.
(c) A draft comparison determines whether to click Send, without verifying delivery.

![Refer to caption](2610.22200v1/patterns_evidence_v3.png)

Figure 4: Programs prepare and verify evidence.
(a) A program assembles 25 views into a contact sheet for the model’s next observation.
(b) Assertions check background images and transparency, and verify that non-background content remains unchanged.

Cross-Interface Composition.
A single program can use information from one interface to guide operations through another.
A program can alternate between GUI actions and programmatic checks within one model step. In a contract-generation task, the agent clicks a spreadsheet button, reads the application’s completion status, and checks the output files. Only after these checks pass does it click a second button to create local email drafts, which it then inspects programmatically. This example connects GUI execution with structured feedback from both the application and its files (Figure [3](#S3.F3)a).

Loop-Based Execution.
Loops let the model specify a procedure once and repeat it across multiple targets within one program. Unlike a fixed action list, the targets and number of iterations can be determined during execution, for example from file contents or application state. This allows repeated work to proceed without generating a separate action sequence or making a new model call for each iteration.
To record a website walkthrough, the agent iterates over seven navigation targets, clicks each target, and reads the active section from the DOM. An assertion checks that the resulting section matches the intended target before the loop continues. The program handles all seven visits and checks without returning to the model between iterations (Figure [3](#S3.F3)b).

Result-Dependent Execution.
Conditional logic lets the program respond to what happens during execution. It can inspect command output or application state, check a result, and decide whether to continue. Such decisions can remain within the program when their conditions are computable, rather than requiring the model to interpret each intermediate result. A local check can determine whether a GUI action should proceed. Before sending an email reply, the agent copies the draft from the interface and compares it with a saved version after trimming leading and trailing whitespace. Its program clicks Send only if the texts match and reports a mismatch otherwise. The recorded execution follows the matching branch, but delivery is not verified within this step (Figure [3](#S3.F3)c).

Observation Preparation.
Programs can gather and organize evidence for the next model decision. They can collect multiple views, crop relevant regions, or arrange images into a visual summary. This extends code execution from performing actions to preparing observations that the model can then interpret. While inspecting a three-dimensional object, the agent collects 25 views, crops the relevant region from each, and assembles a numbered contact sheet. It opens this sheet and requests one new visual observation. The program collects and arranges views for the model’s visual judgment (Figure [4](#S3.F4)a).

Executable Verification.
Programs can check both intended changes and content that should remain unchanged. After editing two slide backgrounds, the agent compares the original and saved presentation packages. It checks the expected changes, verifies that the other 64 original package entries are unchanged, and compares slide content outside the background elements. These assertions make selected preservation requirements explicit, but do not replace independent evaluation (Figure [4](#S3.F4)b).

These examples show a useful division of work: programs execute locally specified operations and checks, while the model chooses the procedure and interprets evidence that still requires judgment.

#### 3.1.3 Limits of Visual-Only Feedback

Result-dependent control is harder when interface observations are limited to screenshots. Conditions such as whether a button is enabled or an input field contains the expected value are not directly exposed as program-readable values, so checking them may require another model call. Accessibility trees can expose text and control states as structured data, allowing programs to query supported interface properties and use them in loops and conditional logic. This motivates combining visual observation with accessibility-tree access in our real-device harness design.

### 3.2 Harness-to-Model Decision Transfer

Code execution addresses how to act by allowing the model to express computer operations as programs. A GCUA must also decide what to observe and how to organize its work. We study harness-to-model decision transfer: replacing selected fixed harness rules with task-dependent model decisions. A screenshot, for example, may be necessary after a GUI action but redundant when program output already answers the relevant question. Deciding whether to request it should depend on the information needed to continue.

Mechanism in the Harness, Decision in the Model.
As models become more capable, we envision progressively shifting selected workflow decisions from fixed harness rules to the model. The harness should provide reliable mechanisms, while the model decides when and how to use them based on the task and available evidence. In the current implementation, screenshot requests and task-state updates are model-initiated workflow operations, complemented by model-generated action-intent annotations. The harness continues to execute interface calls, preserve task records, and manage context retention.

#### 3.2.1 Mechanisms for Harness-to-Model Decision Transfer

On-Demand Observation.
The screenshot function lets the model decide whether its next input needs a new screenshot. It can request visual feedback after a GUI action or continue without it when text output is sufficient. On-demand observation can reduce context length by omitting screenshots that add little information. The environment still captures a screenshot after every step, so the mechanism changes what the model receives, not what the environment records.

Task-State Tracking.
The todo interface lets the model maintain a persistent record of progress, facts, and unresolved questions. It updates this record through todo.update() and retrieves it through todo.list().
Statuses distinguish pending work, attempted changes, unverified changes, and claimed verification, helping the model track what still needs checking. These entries record the model’s assessment rather than independently verifying the environment.

Action Intent.
The intent annotation makes the purpose of each code-execution step explicit. Before each program runs, the model provides a short <intent> block stating what the code is intended to accomplish. A program may combine many operations, making its overall purpose difficult to infer from the code alone.
In real-device use, the harness can display this description to users, helping them understand what the agent is trying to do at each step without reading the program.

Harness-Managed Context.
The harness manages historical tool outputs and screenshots through two fixed policies. A rolling screenshot buffer removes older images in batches, limiting visual context while reducing disruption to prompt caching ([Anthropic, 2026a](#bib.bib4)). Micro-compaction applies a similar rolling-buffer policy to textual tool outputs, replacing older outputs with short placeholders in batches while retaining recent results. These retention decisions remain with the harness, complementing the model’s choices about when to obtain new observations and how to track task progress.

#### 3.2.2 Representative Harness-to-Model Decision Transfer Patterns

Figure [5](#S3.F5) shows these interfaces in model outputs. The examples come from GPT-6 Astra trajectories on OSWorld-v2. They illustrate the mechanisms, not their individual effects on task success.

Requesting Visual Feedback Only When Needed.
In a calendar task, the model checks saved events and calls screenshot(). Its next input contains text output and a new screenshot. The following program inspects event styles without requesting another image, so the next input contains text feedback but no new screenshot. These adjacent steps show the observation decision: the model can request visual input or continue with programmatic feedback. Earlier screenshots may still remain in context.

Keeping Unfinished Work Explicit across Programs.
In a form-filling task, the model records that all fields have been entered but submission is still pending. It marks the task changed_unverified. After a later program clicks Submit and reads the page’s confirmation, the model updates the same record to claimed_verified. The persistent record distinguishes work performed from an outcome checked. Its status remains the model’s assessment, not an independent evaluation.

Stating a Program’s Purpose before Execution.
In a CRM task, one intent statement summarizes a 64-line program: update 29 lead statuses while preserving the original customer details. The program performs status-only updates and checks other fields, allowing modification timestamps to change. The <intent> block makes both the intended change and the preservation requirement explicit without requiring the reader to reconstruct them from the code.

![Refer to caption](2610.22200v1/workflow_patterns_compact_v2.png)

Figure 5: Model outputs for observation, task state, and intent.
(a) The two programs differ in whether they request a new screenshot for the next input.
(b) A form record remains unverified until the model reads submission confirmation.
(c) Intent states what the program should change and preserve.

### 3.3 Experiments on Agent Design

We evaluate whether the agent design presented in this report helps frontier models complete computer tasks more effectively. We first compare the full GCUA configuration with a GUI-only baseline that already supports batched actions. We then separate the effects of interface access, code execution, and harness-to-model decision transfer.

#### 3.3.1 Models and Configuration

Benchmark and Models.
Following the evaluation protocol of the GPT-6 Astra release ([OpenAI, 2026c](#bib.bib19)), we evaluate on the 82-task offline subset of OSWorld-v2 (v2.1) ([Yuan et al., 2026](#bib.bib28)), which excludes the 26 tasks that require internet access and so keeps results independent of external websites at run time. The main comparison covers eight models: Claude Opus 5, GPT-6 Astra, Gemini 3.8 Flash, Qwen3.8-Max, Qwen3.8-Flash, Kimi K3, DeepSeek-V4.1-Flash, and GLM-5.3-Flash.

Execution Configurations.
The CUA baseline uses GUI-only interaction with batched actions enabled. The full Open Generalist CUA (OpenGCUA) configuration combines code execution over GUI and shell operations with the model-initiated workflow control and harness-managed context policies described above. For the ablations of code execution, harness-to-model decision transfer, and harness-managed context policies, we explicitly specify which components are enabled in each setting.

Metrics.
We evaluate task performance and execution efficiency. Following OSWorld-v2, we report binary success and partial-credit scores to measure full and partial task completion, respectively. We measure efficiency by mean steps per task and mean output tokens per task.

#### 3.3.2 CUA versus GCUA

Table 2: CUA versus OpenGCUA on the OSWorld-v2 offline set. Each model is evaluated with a GUI-only baseline that supports batched actions and the full GCUA configuration with code execution and harness-to-model decision transfer. Bold marks the better value within each model and metric. K denotes 1,000 tokens.

We compare the conventional GUI-only CUA setting with the full OpenGCUA configuration to examine the performance and efficiency gains from moving toward generalist computer use. OpenGCUA gives the model greater control over what to observe, how to act, and how to organize its work. The CUA baseline already supports batched actions, while OpenGCUA combines code execution with harness-to-model decision transfer.

OpenGCUA improves task scores and reduces steps across all eight models. As shown in Table [2](#S3.T2), the cross-model mean partial score increases from 45.3 to 64.9, a gain of 19.6 points, while steps per task decrease by an average of 53.0%, computed from each model’s relative reduction. The largest score gains reach 35.2 points for GLM-5.3-Flash and 29.8 points for DeepSeek-V4.1-Flash. Full-task success also increases for every model. These results show a substantial gap between batched GUI-only execution and the full OpenGCUA design in both task performance and interaction efficiency.

The gains hold despite large differences in baseline performance and efficiency. The benefits are not limited to models with low initial task scores. GPT-6 Astra, which has the highest baseline score, improves from 67.1 to 75.7 and reduces steps per task from 102.1 to 33.5, a 67.2% reduction. At the other end of the efficiency range, Qwen3.8-Flash starts with 232.0 steps per task, yet gains 21.6 points while using 62.8% fewer steps. The consistent improvements across all 8 frontier models support the broad applicability of the OpenGCUA design.

Fewer interaction steps do not necessarily require fewer output tokens.
Output tokens per task decrease for six of the eight models, with an average relative reduction of 27.2%. Claude Opus 5 reduces its output from 378.3K to 89.3K tokens per task, and Kimi K3 from 302.5K to 139.6K. GPT-6 Astra, however, uses approximately the same output-token budget, despite its large reduction in steps. Fewer steps per task can reduce model round trips and their overhead, even without reducing output tokens. End-to-end latency must be measured separately, accounting for model response time and tool execution time. We report both steps and output tokens to distinguish interaction efficiency from output-token usage.

Figure 6: Code-execution ablation on OSWorld-v2.
Code execution achieves higher task scores and fewer steps than single-action GUI, batched GUI, and batched GUI+CLI setting across all three models.

#### 3.3.3 GUI+CLI Hybrid CUA versus GCUA

Table 3: Full GCUA versus batched GUI+CLI.

GUI+CLI hybrid agents have become an active direction in computer-use research ([Song et al., 2026](#bib.bib21)), including our previous work, Qwen-UI-Agent ([Zhou et al., 2026](#bib.bib30)). As discussed in Section [2.1](#S2.SS1), the batched GUI+CLI formulation is a special case of GCUA. We compare this baseline with the full OpenGCUA setting. Both provide GUI and CLI access, but OpenGCUA introduces code execution and model-initiated workflow control, letting the model decide what to observe, how to act, and how to organize its work.

OpenGCUA achieves higher task scores with fewer reported steps.
In the selected runs, OpenGCUA increases task scores by 4.4 to 9.1 points across all four models, with lower reported steps per task (Table [3](#S3.T3)). Qwen3.8-Max improves from 57.2 to 64.0 with 13.8% fewer steps, while GLM-5.3-Flash improves from 55.8 to 64.9 with 7.6% fewer steps. These results suggest that effective hybrid computer use depends not only on interface access, but also on control over execution and workflow. Code execution lets intermediate results determine subsequent GUI and shell operations within a single program. Harness-to-model decision transfer extends the model’s control to when visual feedback is requested and how task progress is recorded. The comparison evaluates these mechanisms jointly.

#### 3.3.4 Code-Execution Ablation

Code execution improves task scores and reduces interaction steps.
We compare four execution configurations for Qwen3.8-Max, DeepSeek-V4.1-Flash, and GLM-5.3-Flash: single-action GUI execution, batched GUI actions, batched GUI+CLI actions, and code execution over GUI and CLI operations. In the selected runs, code execution achieves higher task scores and fewer steps than each alternative across all three models (Figure [6](#S3.F6)). Relative to batched GUI actions, task scores improve by 15.5 to 33.6 points, while steps per task decrease by 55.3% to 63.1%.

Executable control adds value beyond GUI+CLI access.
The batched GUI+CLI baseline provides the same interfaces and already supports shell scripts. Nevertheless, code execution raises GLM-5.3-Flash’s task score from 55.8 to 63.2, a gain of 7.4 points, and reduces Qwen3.8-Max’s steps per task from 66.1 to 54.9, a 17.0% reduction. The key distinction is how operations are coordinated within a step. A batch fixes the sequence of GUI and shell actions in advance, whereas a program can use intermediate results to determine subsequent operations across both interfaces. Loops, conditional branches, and retries can thus consolidate work that might otherwise require multiple model calls. This unified interface also lets models apply their existing programming capabilities directly to computer interaction, rather than expressing computer interaction through a separate action-list format. Together, these properties may help explain the observed improvements in task scores and interaction efficiency.

#### 3.3.5 Harness-to-Model Decision Transfer Ablation

Most mechanisms are not designed primarily to improve task scores.
We ablate the mechanisms supporting harness-to-model decision transfer and the harness-managed context policies. Using code execution as the baseline, we add each feature separately and then combine all features for Qwen3.8-Max and DeepSeek-V4.1-Flash (Table [4](#S3.T4)). While todo aims to support task completion, the other features primarily target observation efficiency, interpretability, or context management. We therefore assess cache reuse where relevant and check whether task scores are maintained.

Table 4: Ablation of harness-to-model decision transfer and harness-managed context policies. Each mechanism is added separately to code execution; the final row combines all mechanisms. Cache hit is the fraction of input tokens served from cache; dashes indicate omitted rates.

On-demand observation improves cache reuse.
The screenshot action lets the model omit screenshots when program output is sufficient, aiming to reduce unnecessary visual context. In the selected runs, cache hit rises from 75.6% to 86.1% for Qwen3.8-Max and from 61.9% to 76.3% for DeepSeek-V4.1-Flash, with higher task scores in both cases.

Task-state tracking and action intent serve distinct goals.
The todo interface supports task completion by maintaining a record of progress and unresolved work. Task score increases from 62.4 to 64.0 for Qwen3.8-Max and from 56.7 to 58.5 for DeepSeek-V4.1-Flash. In contrast, the intent annotation makes each program’s purpose explicit so that real-device users can understand what the agent is doing. Its primary goal is user understanding rather than benchmark performance. Scores fall slightly.

Cache reuse and context length matter for practical agent execution.
As interaction histories grow, context policies must control their length while preserving cache reuse. The rolling screenshot buffer removes older images in batches, reducing how often prior context is modified. In the selected runs, cache hit improves by 16.0 and 13.4 percentage points for Qwen3.8-Max and DeepSeek-V4.1-Flash, respectively. Micro-compaction instead replaces older tool outputs with short placeholders to limit context growth, at the potential cost of invalidating cached prefixes. Cache hit falls from 75.6% to 68.6% for Qwen3.8-Max, and from 61.9% to 58.9% for DeepSeek-V4.1-Flash. Neither context policy lowers task score in these selected comparisons.

#### 3.3.6 How Much Task Performance Can Money and Time Buy?

Final benchmark scores alone do not show how much performance is available under limited resources. We therefore examine monetary and time constraints using the same selected full-setting runs as the main evaluation on the offline subset of OSWorld-v2.

Measuring Performance under Resource Limits.
We retrospectively apply a common spending cap to every task. A trajectory contributes its recorded final partial score only if its full cost fits within the cap; otherwise, it contributes zero.
We estimate spending by assuming that each attempt ends when its recorded trajectory finishes or its spending cap is reached, whichever comes first. Spending on unsuccessful attempts is also included.
Figure [7](#S3.F7)(a) plots the resulting score against average expenditure per task, not the cap itself. Panel (b) applies the same scoring rule to a per-task time limit. Scores are averaged over all tasks.

Notably, recorded wall-clock time depends on API bandwidth and rate limits, the number of concurrently active evaluation environments, provider-side queuing, and tool execution latency. These conditions were not controlled across models, limiting the comparability of the measurements. We therefore report the time curves as exploratory evidence and treat their trends as indicative rather than conclusive.

![Refer to caption](2610.22200v1/OpenGCUA_money_time.png)

Figure 7: Task performance under monetary and time constraints.
Mean partial scores on the 82-task offline subset of OSWorld-v2 under increasing per-task spending caps (a) and recorded time limits (b).
Panel (a) reports average expenditure, including unsuccessful attempts.
Top bars identify the highest-scoring models; shading indicates cache-write cost bounds.
Time comparisons are exploratory.

Money and Time Favor Different Models.
Under the assumed API prices, the highest-scoring model shifts from Qwen3.8-Flash to GLM-5.3-Flash, Gemini 3.8 Flash, and eventually GPT-6 Astra as the monetary budget increases. For example, Qwen3.8-Flash reaches 60.5 points at approximately $0.38 per task, whereas GPT-6 Astra reaches the highest score of 75.7 at approximately $15.26 per task. In the recorded-time comparison, however, GPT-6 Astra achieves higher scores at most time limits.

From Benchmark Scores to Resource-Aware Model Selection.
In practice, the relevant question is not only which model achieves the highest benchmark score, but which delivers the most task performance within a given budget or an acceptable completion time. These curves make this distinction explicit: models with lower final scores may be preferable under tighter resource constraints.

## 4 Real-Device Generalist CUA

In Section [3](#S3), we study code execution and harness-to-model decision transfer on OSWorld-v2, where every task runs in a controlled benchmark environment. Users, however, run agents on their own computers.
There, the environment is not initialized for the task, many application windows overlap, the user works at the same time, and requests change as the task goes on, so an agent that performs well on a benchmark may still struggle on a real device.
This section first describes how real devices differ from benchmarks (Section [4.1](#S4.SS1)). It then presents the Cross-Device SDK, the programming interface through which the model operates different devices (Section [4.2](#S4.SS2)), and the harness we built for real devices, organized into five layers with clear responsibilities (Section [4.3](#S4.SS3)).

### 4.1 The Gap Between Benchmarks and Real Machines

Controlled computer-use evaluations typically provide prepared task states, an initial instruction, and an environment reserved for the agent. Such settings simplify evaluation but do not fully capture the demands of operating a user’s computer. We highlight five requirements that become especially important when the agent works alongside a user in an existing, changing environment.

The user and agent share control.
The user may continue working while the agent runs, so the agent cannot assume exclusive control of the pointer, keyboard, or focused window. It must account for user activity rather than attribute every change to its own actions. Where supported, it should prefer accessibility actions or background-window operations that leave the user’s current interaction undisturbed. When these methods cannot complete an operation, foreground interaction requires coordination with the user before taking control.

The screen keeps changing.
Application windows open, close, and move, and one window can cover another. These changes may come from applications unrelated to the task and continue while the agent is reasoning. A coordinate or element reference that was valid when observed may therefore be wrong by the time the agent acts.

User requests evolve during execution.
Users may clarify an initial request, correct the agent’s approach, or add constraints as work proceeds. The agent must keep track of the overall task goal and relevant progress across interruptions and turns, while revising its plan to reflect the user’s latest instructions.

Observation and control require explicit targets.
On a user’s computer, the task-relevant application, window, or browser tab need not be in the foreground. A full-desktop screenshot shows the visible composition of windows, not the contents of every addressable target. The model must therefore choose both what to inspect and how to inspect it: a target-specific image, an accessibility tree, or a programmatic query may expose different aspects of the same target. For example, an agent inspecting a background product page may receive an unrelated login page if it requests a desktop screenshot rather than an image of the selected tab, as illustrated in Section [4.3.4](#S4.SS3.SSS4).

Observation and control also impose different requirements. Being able to inspect a background target does not imply that every operation on it can run in the background. The model must select a supported control method, while the harness makes target identities, available capabilities, and foreground-input requirements explicit. Observations and actions should remain tied to their selected targets rather than silently following changes in desktop focus. These requirements link the model’s observation and action choices to the resource bindings and capability declarations in the Cross-Device SDK (Section [4.2](#S4.SS2)).

Tasks begin in an existing user environment.
Benchmark tasks typically start from a prepared state. A user’s computer instead retains files, open tabs, application windows, and account sessions from prior use. Relevant materials may be mixed with unrelated content or similarly named files, requiring the agent to identify the correct inputs before acting. Expired sessions or missing permissions may also require user involvement before execution can continue.

These requirements mean that benchmark scores alone do not establish reliable operation on users’ devices. We therefore study real-device capability alongside benchmark performance, rather than treating deployment as an implementation detail. The following sections describe our SDK and harness, and Section [4.3.3](#S4.SS3.SSS3) reports preliminary real-device results.

### 4.2 Cross-Device SDK

A computer-use task may span a mobile application, desktop tools, and a browser-based service. The Cross-Device SDK provides a common programming interface through which one agent can coordinate these environments. It supports both the reuse of common operations across platforms and the composition of cross-device workflows within a single task. Its programming model builds on code-execution-based computer-use interfaces ([OpenAI, 2026b](#bib.bib18); [OpenAI, 2026a](#bib.bib17)).

![Refer to caption](2610.22200v1/sdk_architecture.png)

Figure 8: Architecture of the Cross-Device SDK. A common programming interface connects agent programs to computers, mobile devices, and browser environments, enabling cross-device workflows through platform-specific adapters.

##### Shared Operations with Explicit Targets.

Common operations use a shared vocabulary, while platform adapters implement their native behavior. For example, the macOS adapter uses the unmodified Cua Driver from trycua ([trycua, 2026](#bib.bib23)). Each operation is scoped to an explicit resource, such as a device, application, window, or browser tab. Resource handles retain their targets independently, so selecting a new target does not redirect earlier bindings. This gives agent programs a consistent way to address multiple devices and applications without relying on a single implicitly selected target.

##### Cross-Device Coordination within One Task.

Within one session, programs can combine observations and actions from multiple resources while reusing host-side variables and bindings across turns. The program executes in the host runtime, whereas device.shell.run executes commands on the selected device where supported. File transfers through mu.files.copy identify both source and destination resources. These mechanisms allow intermediate results from one environment to guide operations in another. As an illustrative workflow, an agent could retrieve a report through a phone application, transfer it to a computer for analysis, and enter the results into a browser-based service, coordinating all three stages within the same task.

##### Shared Observation Processing and Selective Delivery.

The SDK exposes ui.ax for structured semantic observations and element-based actions, and ui.vision for images and coordinate-based interaction. Semantic state supports programmatic conditions and checks, while vision provides complementary information when semantic observations are insufficient. Adapters normalize native accessibility and browser semantic trees into common representations, allowing filtering and compact rendering to be reused across compatible platforms.

Observation capture is separate from delivery to the model. Calls such as ui.ax.observe() return data to the program, while mu.emit delivers selected observations or computed results to the model. A program can therefore inspect multiple targets, use structured results to determine subsequent operations, and return only the information needed for the next model decision. This separation supports cross-device execution without requiring a model call for every intermediate structured observation.

##### Explicit Platform Capabilities.

A common interface does not imply identical capabilities across platforms. Each resource declares its supported operations and options. Common UI operations and device services share interfaces, while platform-specific features remain explicit through namespaces such as .android, .macos, and .browser. Operations such as Android navigation and browser page evaluation thus retain their own semantics, allowing programs to reuse common interaction patterns while selecting methods appropriate to each target.

### 4.3 Real-Device Harness

![Refer to caption](2610.22200v1/harnesss_architecture.png)

Figure 9: Five-layer architecture of the real-device harness. The runtime executes model-generated programs through the SDK and platform drivers to interact with applications and the operating system.

The Cross-Device SDK defines the programming interface for device observation and control. The real-device harness integrates this interface with the agent loop, program execution, and platform-specific mechanisms, enabling the model to work on a user’s computer while retaining task state across turns.

#### 4.3.1 Five-Layer Architecture

We separate the system into five layers (Figure [9](#S4.F9)). The model generates a program, the runtime executes it, and SDK calls are translated by the driver into operations on applications and the operating system. Explicit interfaces separate responsibilities and allow compatible components to be replaced independently. Detectable execution failures are reported where they occur; successful action delivery is not treated as evidence that the intended task-level effect has occurred.

Model.
Conditioned on the task, system prompt, and interaction history, the model decides how to observe, act, and organize its work. It selects targets and operations, maintains task state, and determines when to request user input. These decisions are expressed as Python programs against a common SDK, allowing device operations and programmatic checks to share the same control flow.

Runtime.
The runtime manages the agent loop and executes programs in a persistent interpreter. Variables, imports, and the working directory persist across turns, supporting incremental execution. It collects execution feedback and explicitly emitted observations, applies the configured context-retention policies, and constructs the next model input.

Device SDK.
The SDK binds observations and actions to explicit resources, such as devices, windows, and browser tabs (Section [4.2](#S4.SS2)). Short element IDs written directly by the model must originate from observations delivered to it; programs may also obtain element references from fresh observations and use them within the same execution. Resource resets or rebinding invalidate associated references. These constraints establish the provenance and scope of action targets, but do not guarantee that the interface remains unchanged before execution.

Driver.
The driver translates SDK requests into supported native operations, including accessibility actions and coordinate-based input. It manages element identities and snapshot metadata, selects action-delivery mechanisms, and applies foreground or background delivery policies. Detectable native failures are returned as typed errors so that the agent can distinguish execution failures from outcomes requiring further inspection.

Applications and Operating System.
Applications and the operating system determine the available observations and control capabilities. Permissions, application state, and accessibility support constrain which operations can be performed. The harness must expose these limitations and use alternative interaction methods where supported.

#### 4.3.2 Responding to Real-Device Challenges

The constraints discussed in Section [4.1](#S4.SS1) motivate four design choices that connect these layers.

Minimizing Interference on Shared Machines.
An agent operating alongside a user cannot assume exclusive control of the pointer, keyboard, or focused window. The harness therefore prefers element-level accessibility actions, followed by window-targeted coordinate input, and finally foreground input. Background delivery is used only where the target and platform support it; window-relative coordinates alone do not imply background execution. When a less intrusive method is unavailable or ineffective, the agent can escalate to a supported alternative, coordinating with the user before foreground input.

Selecting Observations Explicitly.
A full-desktop screenshot may show the user’s activity rather than the agent’s target, and visual input may be unnecessary during programmatic work. Following the model-initiated observation design in Section [3.2](#S3.SS2), the agent chooses when to observe and which target to inspect. A program can capture observations, process structured results, and emit relevant information within one execution; images are interpreted by the model when delivered in a subsequent input. Bounded history and image retention limit accumulated context. These mechanisms reduce unnecessary observations, but do not eliminate the need to refresh state when the interface changes.

Managing Accessibility Information.
Accessibility observations vary in size, stability, and coverage across applications. The harness filters irrelevant nodes and represents the retained hierarchy as a flat list linked by parent_id. Element identities and snapshot versions support reference tracking, while search, page, and read retrieve relevant information from a retained snapshot without repeatedly capturing the window. When accessibility information is insufficient, visual observation provides a complementary source of evidence. The choice of action-delivery mechanism remains separate from the choice of observation modality.

Maintaining Task Continuity through User Interaction.
Real-device tasks may require clarification, authentication, or authorization that the agent cannot supply independently. The ask_user interface supports these exchanges, including resolving ambiguous targets, requesting assistance with login or verification, and obtaining authorization for consequential actions. User responses and corrections become part of the ongoing task. The runtime preserves interpreter state, resource bindings, and interaction history, allowing execution to resume without rebuilding the workflow.

Table 5: Real-device results on four macOS tasks. Costs and completion use the same selected run per task (run 1). Costs are four-task means; Complete counts tasks judged complete. DeepSeek lacks a hotel trajectory, so its aggregates are unavailable.

#### 4.3.3 Preliminary Real-Device Results

As our real-device benchmark is still under development, we study seven model configurations on four macOS tasks: workbook reasoning, PDF form filling, dietary-constrained shopping research, and hotel comparison, with up to three recorded runs per task and model. Table [5](#S4.T5) summarizes five configurations, reporting mean interaction costs across all four tasks, including incomplete tasks. Steps count model responses, and output tokens include reasoning where recorded. Dollar costs are estimated from recorded response usage, cache hits, and public API prices.

Execution Efficiency.
Generation volume differs more sharply than interaction length. GPT-6 Astra averages 34.5 steps and 12.9K output tokens per task, compared with 50.8 steps and 73.4K tokens for Qwen3.8-Max: 1.5 times as many steps and 5.7 times as many output tokens. Much of this difference lies in reported reasoning, which averages 2.6K tokens for GPT and 50.2K for Qwen. Claude Opus 5 and Gemini 3.8 Flash use 42.3K and 31.9K output tokens per task, respectively. Token usage and monetary cost need not rank models in the same order: under the archived pricing assumptions, Qwen3.8-Max costs $1.49 per task, compared with $18.29 for GPT-6 Astra.

##### Task-Level Differences.

On the workbook task, both selected runs satisfy the evaluation criteria, but GPT-6 Astra uses 22 steps and 8,783 output tokens, compared with 37 steps and 120,831 tokens for Qwen3.8-Max. Reported reasoning accounts for 1,487 and 92,974 tokens, respectively. On the PDF task, Qwen also uses significantly more output tokens (28,268 versus 10,013). The following case studies examine how observation choices and code execution contribute to the observed differences. With only four tasks and one run per model, these results characterize the evaluated configurations rather than establish a general model ranking.

![Refer to caption](2610.22200v1/realdevice_observation_v2.png)

Figure 10: Reasoning cost and observation-target selection.
GPT-6 Astra captures the selected Amazon page, while Qwen3.8-Max captures the foreground Taobao page and then switches to Amazon. Qwen3.8-Max uses substantially more reasoning tokens.

#### 4.3.4 Case Studies

The gap in real-device execution extends from basic operation to completing an entire task.
We compare GPT-6 Astra and Qwen3.8-Max through earlier low-effort trajectories under the same harness on real-device tasks, separate from the selected runs in Table [5](#S4.T5). The following cases show differences in the cost of routine operations, the selection of observation targets, and the ability to turn a task into an effective program.

Large Differences in Reasoning Cost for Simple Operations.
In a shopping task, Qwen produces a four-line program that captures and returns a desktop screenshot. The program returns an image, but the model response uses 2,105 output tokens, including 2,030 reasoning tokens. GPT also obtains a screenshot in another step of the same task, but its entire response uses only 124 output tokens, including 11 reasoning tokens (Figure [10](#S4.F10)). This contrast shows that a substantial reasoning-cost gap can arise even in a simple observation step. Such generation overhead can introduce substantial execution latency.

Difficulty Adapting to Real-Device Conditions.
On a real device, the page an agent needs to inspect may not be in the foreground. In the shopping task, Qwen is working with an Amazon browser object but requests a desktop screenshot, which shows the foreground Taobao login page. It then brings Amazon forward and captures again. GPT instead requests a screenshot directly from its selected browser page. Both models use screenshots; the contrast concerns observation scope, illustrating why the intended task target cannot be assumed to coincide with the foreground interface.

A Gap in Task-Level Code Execution.
A workbook task reveals a difference in how models translate task requirements into programs. GPT-6 Astra builds a reusable solver, checks it against seven supplied examples, and identifies question rows from the workbook contents. Its program generates answers for all 125 questions. Qwen3.8-Max also uses functions and loops, but processes fixed row ranges that cover only 85 questions. Although its program reports this count, Qwen3.8-Max does not check for omitted questions. An audit of the saved workbooks confirms that GPT fills all 125 required Level answer cells, while Qwen3.8-Max leaves 40 empty (Figure [11](#S4.F11)). The gap is therefore not simply whether a model can write executable code with loops and conditions, but whether it can use code correctly to cover the full task and check for incomplete work.

![Refer to caption](2610.22200v1/realdevice_programs_v2.png)

Figure 11: Task coverage in code execution.
GPT-6 Astra fills all 125 required Level answer cells, while Qwen3.8-Max leaves 40 empty.

## 5 Roadmap

Open Generalist CUA aims to make generalist computer use a shared research effort in which models, execution systems, and real-device evaluation advance together. This first release provides an initial basis for that work.

### 5.1 From Design Validation to Model Release

The model-side contribution of this report is empirical validation of agent design using existing models, rather than a newly trained model. We study code execution and harness-to-model decision transfer, and release implementations, prompts, and evaluation trajectories alongside preliminary versions of the real-device harness and cross-device SDK.

A GCUA model is the central addition planned for the next release.
We aim to unify computer and browser use and turn the designs studied here into learned capabilities: coordinating visual and programmatic operations through code, requesting observations when needed, maintaining task state throughout execution, and particularly enhancing the capability in real-device scenario.

### 5.2 Research Priorities

More Efficient Reasoning and Execution.
We will optimize the model’s thinking, making reasoning more concise for routine operations and mitigating overthinking. On the harness and infrastructure side, we will improve code execution, context management, and infrastructure optimization. We will also explore new system architectures and other system-level solutions for efficiency.

Reliable Work on Users’ Devices.
We plan to extend the harness and SDK toward tasks spanning computers, browsers, and potentially mobile devices. Priorities include reliable target selection, recovery from execution failures, and task continuity when users interrupt or change their requests. We will also investigate which additional workflow decisions should move from fixed harness rules to the model.

Real-Device Environments and Benchmarks.
We will develop evaluation environments and benchmarks on real devices, particularly macOS, covering a wider range of applications, user interactions, and changing device states. The goal is to measure whether agents complete useful work under real operating conditions, together with the time and resources required.

### 5.3 How to Contribute

We welcome contributions to both the implementation and the research agenda:

•

Improve the Harness and SDK. Contribute platform adapters, more reliable observation and control, execution optimizations, or real-device testing and documentation.

•

Build Real-Device Evaluation. Contribute environments, realistic tasks, evaluation criteria, and benchmark infrastructure, including execution traces that expose current limitations.

•

Propose Research Goals. Identify workflows agents should support, capabilities worth developing, or questions to investigate through the released systems and trajectories.

These priorities guide planned releases without fixing a delivery timeline. The agenda will evolve with experimental evidence and community proposals, including directions beyond those listed here. Our goal is for the community to help shape not only how GCUAs are built, but also what they should be able to do and how progress should be measured.

## 6 Related Work

Frontier Computer Use. OpenAI positions GPT-6 Astra for difficult end-to-end work and describes computer use as a new frontier in speed, accuracy, and safety. It recommends code execution for computer-use tasks while retaining the structured computer tool as an alternative ([OpenAI, 2026c](#bib.bib19); [OpenAI, 2026b](#bib.bib18)). In Codex, Computer Use can see and operate graphical user interfaces on macOS and Windows, support workflows spanning multiple applications, and, on macOS, run scoped background tasks while the user continues working elsewhere ([OpenAI, 2026a](#bib.bib17)). Anthropic also provides computer use in Claude Cowork and Claude Code: Claude first reaches for the most precise tool, such as connectors to services like Slack or Google Calendar, and can directly control the browser, mouse, keyboard, and screen when no connector is available. Its Dispatch feature further lets users assign tasks from a phone and open the completed work on a computer ([Anthropic, 2026b](#bib.bib5)). Despite these capabilities, the public releases leave key implementation details and execution trajectories unavailable, making their system designs difficult for the community to reproduce and study systematically.

Computer-Use Agents. Prior open CUA models remain largely GUI-centric. UI-TARS and UI-TARS-2 ([Qin et al., 2025](#bib.bib20); [Wang et al., 2025a](#bib.bib24)), OpenCUA ([Wang et al., 2025b](#bib.bib25)), ScaleCUA ([Liu et al., 2025](#bib.bib13)), EvoCUA ([Huang et al., 2026](#bib.bib9)), and Fara ([Microsoft, 2026](#bib.bib15)) release open models for computer use and report strong results on relevant benchmarks. Recent work has begun to explore hybrid GUI–programmatic execution: CoAct-1, ComputerRL, UltraCUA, ToolCUA, and StateAct combine GUI control with code, APIs, tool calls, or program-state operations ([Song et al., 2026](#bib.bib21); [Lai et al., 2025](#bib.bib11); [Yang et al., 2026b](#bib.bib27); [Hu et al., 2026](#bib.bib8); [Yang et al., 2026a](#bib.bib26)); RecreationWorld and WeaveBench respectively provide environments and benchmarks for such interleaved trajectories ([Bai et al., 2026](#bib.bib6); [Li et al., 2026](#bib.bib12)). Our previous work, Qwen-UI-Agent, introduced a unified GUI–CLI action space with batched actions, a real-device mobile runtime, and a harness for proactive cross-platform execution ([Zhou et al., 2026](#bib.bib30); [Zhou et al., 2025](#bib.bib29)). To capture this broader setting, following the system-level perspective of Agents’ Last Exam ([Sun et al., 2026](#bib.bib22)), we use the term Generalist Computer-Use Agent (GCUA). We define a GCUA as an agent system that completes diverse computer tasks through visual interaction and programmatic access, choosing how to observe, act, and organize its work as each task requires.

Open Computer-Use Infrastructure. Several projects provide open harnesses for computer-use agents. The cua project provides cross-platform desktop drivers and sandbox SDKs ([trycua, 2026](#bib.bib23)). The Agent S series provides open orchestration frameworks with memory, visual grounding, and increasingly code-based execution ([Agashe et al., 2025a](#bib.bib1); [Agashe et al., 2025b](#bib.bib2); [Gonzalez-Pumariega et al., 2026](#bib.bib7)). Open Computer Use provides an MCP-wrapped desktop-control runtime, including macOS control through Accessibility ([iFurySt, 2026](#bib.bib10)). These are complementary to our work. Open Generalist CUA is an ongoing project to open a full GCUA research stack that couples a trained model with a real-device harness, a cross-device SDK, and execution trajectories.

## 7 Conclusion

We presented the first release of Open Generalist CUA, an ongoing project to develop and open the full stack for generalist computer use. Our GCUA formulation centers on three model decisions: what to observe, how to act, and how to organize work. Code execution lets models use intermediate results to coordinate GUI and programmatic operations and apply their existing programming capabilities to computer interaction. Harness-to-model decision transfer complements this design by moving selected observation and task-state decisions from fixed harness rules to the model. On the offline subset of OSWorld-v2, the full OpenGCUA configuration improves task scores across all eight evaluated models, raising mean partial score by 19.6 points and reducing reported steps per task by an average of 53.0% relative to batched GUI-only execution. Ablations show additional benefits from code execution with the same GUI and CLI access, indicating that execution design matters beyond interface access.

We release our implementation, prompts, and evaluation trajectories, alongside preliminary versions of a real-device harness and cross-device SDK. Evaluations on four macOS tasks reveal substantial differences in reported reasoning-token usage and task completion under the same harness. This report studies GCUA designs rather than introducing a newly trained model. OpenGCUA will continue through further research and releases on GCUA models, reasoning and execution efficiency, and real-device environments and benchmarks.

## Appendix A Evaluation Details

Metrics and Aggregation.
We evaluate the 82-task offline subset of OSWorld-v2 v2.1. Task score is the mean evaluator partial score, expressed on a 0–100 scale. Full-task success is the percentage of tasks with a normalized evaluator score greater than 0.999999. Steps and token counts are averaged over all selected tasks, including failures. Within each run, we retain the latest attempt with an evaluator result for each task, not the highest-scoring attempt. Cross-model summaries give each model equal weight: score gains are averaged in points, and relative resource reductions are calculated within each model before averaging.

The offline subset is defined by evaluation_examples/test_v2_offline_no_internet.json. It excludes the 26 tasks requiring external Internet access, while retaining local web applications and desktop tasks.

## Appendix B Real-Device Evaluation Details

### B.1 Task Descriptions

##### Workbook Reasoning.

The input workbook contains race rules, a track layout, seven worked examples, and 125 Level questions. The agent must compute all Level answers and the requested bonus answers, enter them in the designated cells, and save a completed copy without altering the original.

##### PDF Form Filling.

The inputs comprise a blank four-page Schengen application form and synthetic identity, employment, travel, and accommodation records. The agent must fill all applicable fields supported by these materials and save a new PDF with all entered information visible and correct.

##### Shopping Research.

Given 22 snack candidates and a dietary-restriction list, the agent must verify exact products on Amazon, falling back to official brand or original product pages when necessary. The DOCX must cover every candidate, with evidence for purchase or replacement recommendations and explicit uncertainty about unverified ingredients or allergens. No purchase is permitted.

##### Hotel Comparison.

The agent must compare Pullman Paris Montparnasse and InterContinental Paris Le Grand for two adults over December 20–30, 2026, with one hotel change and at least three nights at each hotel. It lists ten feasible date plans and researches four prescribed plans through the official sites, Expedia, and Booking.com. A four-sheet workbook must document tax-inclusive EUR prices, refundability, breakfast for two on December 23–28, and source limitations. No reservation is permitted.

### B.2 Task Instructions and Materials

The following are full English translations of the original task instructions. The snack-document title and corresponding filename are translated into English. The original prompts and input files are included in the accompanying task-material bundle.

#### B.2.1 Workbook reasoning and editing

##### Input Materials.

Elimination_Race_to_Las_Vegas.xlsx, containing the Case and RaceTrack sheets. The source contains 125 Level 1-7 questions, seven worked examples, and five bonus questions.

##### Task Instruction.

Please use the file "Elimination_Race_to_Las_Vegas.xlsx" located on your desktop to complete the "Jade’s Community Game! (Everyone Welcome)" challenge at https://play.excel-esports.com. Follow the rules provided in the workbook and on the challenge page to solve all the questions, enter your answers into the designated fields on the website, and submit them. Finally, display the results page and report both your actual score and the maximum possible score.

![Refer to caption](2610.22200v1/figures/realdevice_materials/workbook_view.png)

Figure 12: Workbook interface during the Claude Opus 5 run. The view shows the rules and answer cells. Displayed answers are model outputs, not part of the initial workbook.

#### B.2.2 Document-grounded PDF form filling

##### Input Materials.

visa task.zip: a blank four-page Schengen form, passport and ID information, an application worksheet, an employment certificate, a flight itinerary, and hotel bookings. The identity workbook explicitly labels its records as synthetic test data.

##### Task Instruction.

Please use the application materials found in the visa task.zip file on the desktop to complete the blank Schengen visa application form, CS_14076-05_EN_05.pdf. Review every field in the form and populate it with all clearly identifiable information provided within the visa task.zip package—including the applicant’s personal details, passport information, travel itinerary, accommodation, transportation, occupation, and any other relevant data. Once finished, save the completed form as CS_14076-05_EN_05_filled.pdf. The final PDF file must be accessible and retain all the information you have entered.

![Refer to caption](2610.22200v1/figures/realdevice_materials/blank_form.png)

Figure 13: First page of the supplied blank application form. Completed forms and applicant details are not shown.

#### B.2.3 Evidence-grounded online shopping research

##### Input Materials.

snake filter task.zip: Combined_Snacks (22 candidates, with original product names and links) and Dad_No_Go_List (dietary restrictions and allergen exclusions). Live sources are Amazon, official brand pages, or the original candidate product pages.

##### Task Instruction.

Please review the 22 snacks on the candidate list by cross-referencing them with the Combined_Snacks and Dad_No_Go_List files found in the snake filter task.zip folder on your desktop.
Since the candidate list does not provide full ingredient lists, please look up each item on Amazon. Use the ingredient list, allergen information, and product description provided on the Amazon product page—in conjunction with the restrictions outlined in the Dad_No_Go_List—to determine whether each item is suitable for purchase.
Create a Word document titled “Snacks Dad and I Can Share” and categorize all 22 candidate items into the following three groups:

1.

Safe to purchase as is

2.

Requires a change in flavor, size, or other adjustments before it can be purchased

3.

Not recommended for purchase

For each item, you must include:

•

Number

•

Product Name

•

Assessment Result

•

Rationale for the assessment

•

If adjustments are required, specify the necessary changes (e.g., flavor, size, or other modifications)

If the ingredients or allergen information for a product cannot be verified via its Amazon product page, do not rely on the product name or general assumptions; instead, clearly label it as “Ingredient information unverified.”
Ensure that all 22 candidate items are included and that each item is assigned to exactly one category.
Include the following disclaimer at the end of the document:
Prices, formulations, and stock availability are subject to change. Always check the actual product packaging labels and warnings regarding cross-contact before placing an order or consuming the product.

![Refer to caption](2610.22200v1/figures/realdevice_materials/snack_candidates.png)

Figure 14: First page of the supplied Combined_Snacks candidate list, showing product images, package descriptions, and original listing links. The screenshot retains the source language.

#### B.2.4 Constrained live hotel comparison

##### Input Materials.

A text-only request for a Paris itinerary and a four-sheet comparison workbook. Prices and policies must come from the live Accor, IHG, Expedia, and Booking.com websites, not bundled rate cards.

##### Task Instruction.

I’m planning a Paris trip from Dec 20 to Dec 30, 2026 (check-in Dec 20, check-out Dec 30, 10 nights total) for 2 adults. I want to split the stay between exactly two hotels:

•

Pullman Paris Montparnasse

Official site: [https://all.accor.com/a/en/offers/meapac/pullman.html?merchantid=ppc-pul-goo-apac-en-pmax&sourceid=aw-cen&utm_source=google&utm_medium=cpc&utm_campaign=ppc-pul-goo-apac-en-apac-pmax-aw-cen&utm_term=goo&utm_content=en-apac-all-all&wiz_campaign=24047123880&gad_source=1&gad_campaignid=24047157582&gbraid=0AAAABC20MbFGIzWYbNya4iMdEd7J85MfU&gclid=CjwKCAjww-3VBhAcEiwAwUUIu9eC4_lOMg5Q6UoljvjRNlUdcS3bBq5DHLxRAKHOZoVW10488aIrYBoCu3sQAvD_BwE](https://all.accor.com/a/en/offers/meapac/pullman.html?merchantid=ppc-pul-goo-apac-en-pmax&sourceid=aw-cen&utm_source=google&utm_medium=cpc&utm_campaign=ppc-pul-goo-apac-en-apac-pmax-aw-cen&utm_term=goo&utm_content=en-apac-all-all&wiz_campaign=24047123880&gad_source=1&gad_campaignid=24047157582&gbraid=0AAAABC20MbFGIzWYbNya4iMdEd7J85MfU&gclid=CjwKCAjww-3VBhAcEiwAwUUIu9eC4_lOMg5Q6UoljvjRNlUdcS3bBq5DHLxRAKHOZoVW10488aIrYBoCu3sQAvD_BwE)

•

InterContinental Paris - Le Grand

Official site: [https://www.ihg.com/intercontinental/hotels/us/en/paris/parhb/hoteldetail](https://www.ihg.com/intercontinental/hotels/us/en/paris/parhb/hoteldetail)

Also compare rates on Expedia and Booking.com.
Constraints:

1.

Stay at each hotel for at least 3 consecutive nights, with only ONE hotel switch (Hotel A for $N$ nights then Hotel B for $10-N$ nights, N from 3 to 7, in either order).

2.

1 room, 2 adults, queen bed. If queen is unavailable, use king and clearly flag it.

3.

Fully refundable / free-cancellation rates only.

4.

Breakfast for 2 must be included on the mornings of Dec 23 through Dec 28 inclusive. Therefore, the nights of Dec 22 through Dec 27 must be booked on a breakfast-included rate. Other nights may use room-only refundable rates if cheaper.

Task:

•

Enumerate every valid hotel-order × switch-date × booking-site combination that satisfies the constraints.

•

Check the two official hotel sites above, Expedia, and Booking.com.

•

For each combination, record nightly rates, taxes/fees, cancellation deadline, breakfast coverage, and any verified direct-booking perks such as member rates, loyalty points, upgrades, hotel credits, or working promo codes.

•

Do not assume an unavailable rate, perk, promo code, breakfast inclusion, or cancellation policy. Record only information that can be verified from the booking page.

Output: create an Excel file (.xlsx) with:

•

Sheet 1 “All combinations”: one row per valid combination. Columns = Rank | Hotel 1 | Hotel 1 dates | Hotel 1 nights | Hotel 1 site | Hotel 1 total EUR | Hotel 2 | Hotel 2 dates | Hotel 2 nights | Hotel 2 site | Hotel 2 total EUR | Grand total EUR | Grand total USD | Room type | Refundable until | Breakfast nights covered | Perks / promo codes | Notes. Sort by Grand total EUR ascending. Highlight the cheapest row in green and bold; highlight the cheapest single-site option (both hotels booked on the same site) in yellow.

•

Sheet 2 “Rate detail”: nightly price per hotel × date × site × rate type (room-only vs breakfast, refundable), including taxes/fees where available, so the combination totals can be verified.

•

Sheet 3 “Summary”: the lowest-cost valid arrangement in plain text — hotel order, exact dates, which site to book each hotel on, total price, and cancellation deadlines — plus the next 3 lowest-cost valid alternatives.

Do NOT book anything. Save and return the completed .xlsx file.

![Refer to caption](2610.22200v1/figures/realdevice_materials/hotel_view.png)

Figure 15: InterContinental Paris Le Grand website observed during the GPT-6 Astra run.

## Appendix C Prompts

We first present verbatim excerpts for code execution and harness-to-model decision transfer, then provide the complete OpenGCUA system prompt for the all setting. Only the environment login credential is redacted; the instructions and examples are preserved as recorded.

### C.1 Code Execution

We reproduce the code-execution baseline’s execution contract, PyAutoGUI interface, three code examples, and response format, retaining the original prompt headings. The PyAutoGUI definition is also used in the full prompt (Section [C.3](#A3.SS3)). The examples illustrate GUI interaction, conditional shell execution, and loops over GUI operations.

[⬇](data:text/plain;base64,IyMgRXhhbXBsZXMKYGBgCjxjb2RlPgpweWF1dG9ndWkuY2xpY2soNTEyLCAzOTYpICAgICAgIyB1c2VybmFtZSBmaWVsZApweWF1dG9ndWkudHlwZXdyaXRlKCJhbGljZSIpCnB5YXV0b2d1aS5wcmVzcygidGFiIikKcHlhdXRvZ3VpLnR5cGV3cml0ZSgiczNjcmV0IikKcHlhdXRvZ3VpLnByZXNzKCJlbnRlciIpCnRpbWUuc2xlZXAoMikKPC9jb2RlPgpgYGAKCmBgYAo8Y29kZT4KciA9IGJhc2goImxzIC1sIH4vRGVza3RvcC9yZXBvcnQucGRmICYmIHBkZmluZm8gfi9EZXNrdG9wL3JlcG9ydC5wZGYgfCBoZWFkIC01IikKaWYgci5vazoKICAgIGJhc2goIm5vaHVwIGV2aW5jZSB+L0Rlc2t0b3AvcmVwb3J0LnBkZiA+L2Rldi9udWxsIDI+JjEgJiIpCiAgICB0aW1lLnNsZWVwKDMpCjwvY29kZT4KYGBgCgpgYGAKPGNvZGU+CnJvd3MgPSBbKCJBbGljZSIsICIzMSIpLCAoIkJvYiIsICIyNyIpLCAoIkNhcmEiLCAiNDUiKV0KcHlhdXRvZ3VpLmNsaWNrKDMwNSwgNDAyKSAgICAgICMgZmlyc3QgZGF0YSBjZWxsCmZvciBuYW1lLCBhZ2UgaW4gcm93czoKICAgIHB5YXV0b2d1aS50eXBld3JpdGUobmFtZSkKICAgIHB5YXV0b2d1aS5wcmVzcygidGFiIikKICAgIHB5YXV0b2d1aS50eXBld3JpdGUoYWdlKQogICAgcHlhdXRvZ3VpLnByZXNzKCJlbnRlciIpCnRpbWUuc2xlZXAoMSkKPC9jb2RlPgpgYGAK)
## Examples

‘‘‘

<code>

pyautogui.click(512, 396) # username field

pyautogui.typewrite("alice")

pyautogui.press("tab")

pyautogui.typewrite("s3cret")

pyautogui.press("enter")

time.sleep(2)

</code>

‘‘‘

[⬇](data:text/plain;base64,IyMgRXhhbXBsZXMKYGBgCjxjb2RlPgpweWF1dG9ndWkuY2xpY2soNTEyLCAzOTYpICAgICAgIyB1c2VybmFtZSBmaWVsZApweWF1dG9ndWkudHlwZXdyaXRlKCJhbGljZSIpCnB5YXV0b2d1aS5wcmVzcygidGFiIikKcHlhdXRvZ3VpLnR5cGV3cml0ZSgiczNjcmV0IikKcHlhdXRvZ3VpLnByZXNzKCJlbnRlciIpCnRpbWUuc2xlZXAoMikKPC9jb2RlPgpgYGAKCmBgYAo8Y29kZT4KciA9IGJhc2goImxzIC1sIH4vRGVza3RvcC9yZXBvcnQucGRmICYmIHBkZmluZm8gfi9EZXNrdG9wL3JlcG9ydC5wZGYgfCBoZWFkIC01IikKaWYgci5vazoKICAgIGJhc2goIm5vaHVwIGV2aW5jZSB+L0Rlc2t0b3AvcmVwb3J0LnBkZiA+L2Rldi9udWxsIDI+JjEgJiIpCiAgICB0aW1lLnNsZWVwKDMpCjwvY29kZT4KYGBgCgpgYGAKPGNvZGU+CnJvd3MgPSBbKCJBbGljZSIsICIzMSIpLCAoIkJvYiIsICIyNyIpLCAoIkNhcmEiLCAiNDUiKV0KcHlhdXRvZ3VpLmNsaWNrKDMwNSwgNDAyKSAgICAgICMgZmlyc3QgZGF0YSBjZWxsCmZvciBuYW1lLCBhZ2UgaW4gcm93czoKICAgIHB5YXV0b2d1aS50eXBld3JpdGUobmFtZSkKICAgIHB5YXV0b2d1aS5wcmVzcygidGFiIikKICAgIHB5YXV0b2d1aS50eXBld3JpdGUoYWdlKQogICAgcHlhdXRvZ3VpLnByZXNzKCJlbnRlciIpCnRpbWUuc2xlZXAoMSkKPC9jb2RlPgpgYGAK)
‘‘‘

<code>

r = bash("ls -l ~/Desktop/report.pdf && pdfinfo ~/Desktop/report.pdf | head -5")

if r.ok:

 bash("nohup evince ~/Desktop/report.pdf >/dev/null 2>&1 &")

 time.sleep(3)

</code>

‘‘‘

[⬇](data:text/plain;base64,IyMgRXhhbXBsZXMKYGBgCjxjb2RlPgpweWF1dG9ndWkuY2xpY2soNTEyLCAzOTYpICAgICAgIyB1c2VybmFtZSBmaWVsZApweWF1dG9ndWkudHlwZXdyaXRlKCJhbGljZSIpCnB5YXV0b2d1aS5wcmVzcygidGFiIikKcHlhdXRvZ3VpLnR5cGV3cml0ZSgiczNjcmV0IikKcHlhdXRvZ3VpLnByZXNzKCJlbnRlciIpCnRpbWUuc2xlZXAoMikKPC9jb2RlPgpgYGAKCmBgYAo8Y29kZT4KciA9IGJhc2goImxzIC1sIH4vRGVza3RvcC9yZXBvcnQucGRmICYmIHBkZmluZm8gfi9EZXNrdG9wL3JlcG9ydC5wZGYgfCBoZWFkIC01IikKaWYgci5vazoKICAgIGJhc2goIm5vaHVwIGV2aW5jZSB+L0Rlc2t0b3AvcmVwb3J0LnBkZiA+L2Rldi9udWxsIDI+JjEgJiIpCiAgICB0aW1lLnNsZWVwKDMpCjwvY29kZT4KYGBgCgpgYGAKPGNvZGU+CnJvd3MgPSBbKCJBbGljZSIsICIzMSIpLCAoIkJvYiIsICIyNyIpLCAoIkNhcmEiLCAiNDUiKV0KcHlhdXRvZ3VpLmNsaWNrKDMwNSwgNDAyKSAgICAgICMgZmlyc3QgZGF0YSBjZWxsCmZvciBuYW1lLCBhZ2UgaW4gcm93czoKICAgIHB5YXV0b2d1aS50eXBld3JpdGUobmFtZSkKICAgIHB5YXV0b2d1aS5wcmVzcygidGFiIikKICAgIHB5YXV0b2d1aS50eXBld3JpdGUoYWdlKQogICAgcHlhdXRvZ3VpLnByZXNzKCJlbnRlciIpCnRpbWUuc2xlZXAoMSkKPC9jb2RlPgpgYGAK)
‘‘‘

<code>

rows = [("Alice", "31"), ("Bob", "27"), ("Cara", "45")]

pyautogui.click(305, 402) # first data cell

for name, age in rows:

 pyautogui.typewrite(name)

 pyautogui.press("tab")

 pyautogui.typewrite(age)

 pyautogui.press("enter")

time.sleep(1)

</code>

‘‘‘

[⬇](data:text/plain;base64,IyMgUmVzcG9uc2UgZm9ybWF0CkRlY2lkZSBmdWxseSBpbiB5b3VyIHJlYXNvbmluZyBjb250ZW50IGZpcnN0LiBUaGVuIGVtaXQgZXhhY3RseSBPTkUgPGNvZGU+Li4uPC9jb2RlPiBibG9jayBjb250YWluaW5nIHBsYWluIFB5dGhvbiAobm8gTWFya2Rvd24gZmVuY2VzIGluc2lkZSBpdCksIGFuZCBlbmQgdGhlIHJlc3BvbnNlIHJpZ2h0IGFmdGVyIHRoZSBjbG9zaW5nIDwvY29kZT4gdGFnLiBDb21iaW5lIGV2ZXJ5IGFjdGlvbiBmb3IgdGhpcyBzdGVwIGludG8gdGhhdCBzaW5nbGUgYmxvY2s7IG5ldmVyIGVtaXQgYSBzZWNvbmQgPGNvZGU+IGJsb2NrIGluIHRoZSBzYW1lIHJlc3BvbnNlIC0gcmV2aXNlIHRoZSBmaXJzdCBibG9jayBiZWZvcmUgc2VuZGluZy4K)
## Response format

Decide fully in your reasoning content first. Then emit exactly ONE <code>...</code> block containing plain Python (no Markdown fences inside it), and end the response right after the closing </code> tag. Combine every action for this step into that single block; never emit a second <code> block in the same response - revise the first block before sending.

### C.2 Harness-to-Model Decision Transfer

The full setting adds model-initiated screenshot requests and task-state updates. A separate <intent> annotation states each program’s immediate purpose; it is not a Python operation.

Screenshot Request.

[⬇](data:text/plain;base64,LSBgc2NyZWVuc2hvdCgpYCAtIHJlcXVlc3QgYSBzY3JlZW5zaG90OyBpdCBpcyB0YWtlbiByaWdodCBhZnRlciB0aGUgc2NyaXB0IGZpbmlzaGVzIGFuZCBhcnJpdmVzIHdpdGggdGhlIE5FWFQgb2JzZXJ2YXRpb24sIGFuZCB3aXRob3V0IHRoaXMgY2FsbCB0aGUgbmV4dCBvYnNlcnZhdGlvbiBjYXJyaWVzIG5vIGltYWdlLiBTZWUgIldyaXRpbmcgYSBzdGVwIiBmb3Igd2hlbiB0byBhdHRhY2ggb25lLiAoSXQgYWxzbyByZXR1cm5zIHRoZSBjdXJyZW50IHNjcmVlbiBhcyBhIFBJTCBpbWFnZSBpbiByYXcgcGl4ZWxzIGZvciBwcm9ncmFtbWF0aWMgdXNlOyBgcHlhdXRvZ3VpLnNjcmVlbnNob3QoKWAgb25seSByZXR1cm5zIHRoZSBpbWFnZSBhbmQgYXR0YWNoZXMgbm90aGluZy4pCg==)
- ‘screenshot()‘ - request a screenshot; it is taken right after the script finishes and arrives with the NEXT observation, and without this call the next observation carries no image. See "Writing a step" for when to attach one. (It also returns the current screen as a PIL image in raw pixels for programmatic use; ‘pyautogui.screenshot()‘ only returns the image and attaches nothing.)

Task-State Ledger.

[⬇](data:text/plain;base64,Rm9yIG11bHRpLXN0ZXAgdGFza3MsIG1haW50YWluIGEgcGVyc2lzdGVudCB3b3JrIGxlZGdlciB3aXRoIGB0b2RvLnVwZGF0ZShpZD0iLi4uIiwga2luZD0idGFzayIsIGNvbnRlbnQ9Ii4uLiIsIHN0YXR1cz0icGVuZGluZyIpYCBjYWxscyBpbnNpZGUgeW91ciBjb2RlLiBLaW5kczogdGFzaywgbmV4dF9zdGVwLCBmYWN0LCBxdWVzdGlvbi4gU3RhdHVzZXM6IHBlbmRpbmcsIGF0dGVtcHRlZCwgY2hhbmdlZF91bnZlcmlmaWVkLCBjbGFpbWVkX3ZlcmlmaWVkLCBibG9ja2VkOyB1c2Ugc3RhdHVzPSJkZWxldGUiIHRvIHJlbW92ZSBhbiBpdGVtLiBgdG9kby5saXN0KClgIHByaW50cyB0aGUgZnVsbCBsZWRnZXIuIExlZGdlciBjYWxscyBuZXZlciB0b3VjaCB0aGUgY29tcHV0ZXI6IHB1dCB0aGVtIGluIHRoZSBzYW1lIHNjcmlwdCBhcyByZWFsIGFjdGlvbnMgd2hlbmV2ZXIgcG9zc2libGUgLSBhIHNjcmlwdCB0aGF0IG9ubHkgdXBkYXRlcyB0aGUgbGVkZ2VyIHN0aWxsIGNvbnN1bWVzIG9uZSBmdWxsIHN0ZXAuIFRoZSBsZWRnZXIgaXMgc2hvd24gd2l0aCBlYWNoIG9ic2VydmF0aW9uOiB0aGUgZnVsbCBzbmFwc2hvdCBvbiBhbnkgc3RlcCB3aGVyZSBpdCBjaGFuZ2VkLCBvdGhlcndpc2UgYSBvbmUtbGluZSBzdW1tYXJ5LiBDYWxsIGB0b2RvLmxpc3QoKWAgd2hlbiB5b3UgbmVlZCB0aGUgZnVsbCBsaXN0IGFnYWluLiBJZiB0aGUgc25hcHNob3QgaXMgdHJ1bmNhdGVkLCBpdHMgZm9vdGVyIHN0YXRlcyBob3cgbWFueSBpdGVtcyBhcmUgaGlkZGVuIGFuZCBgdG9kby5saXN0KClgIHByaW50cyBhbGwgb2YgdGhlbS4K)
For multi-step tasks, maintain a persistent work ledger with ‘todo.update(id="...", kind="task", content="...", status="pending")‘ calls inside your code. Kinds: task, next_step, fact, question. Statuses: pending, attempted, changed_unverified, claimed_verified, blocked; use status="delete" to remove an item. ‘todo.list()‘ prints the full ledger. Ledger calls never touch the computer: put them in the same script as real actions whenever possible - a script that only updates the ledger still consumes one full step. The ledger is shown with each observation: the full snapshot on any step where it changed, otherwise a one-line summary. Call ‘todo.list()‘ when you need the full list again. If the snapshot is truncated, its footer states how many items are hidden and ‘todo.list()‘ prints all of them.

Public Intent and Response Format.

[⬇](data:text/plain;base64,RGVjaWRlIGZ1bGx5IGluIHlvdXIgcmVhc29uaW5nIGNvbnRlbnQgZmlyc3QuIFRoZW4gZW1pdCBvbmUgc2hvcnQgPGludGVudD4uLi48L2ludGVudD4gc2VudGVuY2UsIGZvbGxvd2VkIGJ5IGV4YWN0bHkgT05FIDxjb2RlPi4uLjwvY29kZT4gYmxvY2sgY29udGFpbmluZyBwbGFpbiBQeXRob24gKG5vIE1hcmtkb3duIGZlbmNlcyBpbnNpZGUgaXQpLCBhbmQgZW5kIHRoZSByZXNwb25zZSByaWdodCBhZnRlciB0aGUgY2xvc2luZyA8L2NvZGU+IHRhZy4gQ29tYmluZSBldmVyeSBhY3Rpb24gZm9yIHRoaXMgc3RlcCBpbnRvIHRoYXQgc2luZ2xlIGJsb2NrOyBuZXZlciBlbWl0IGEgc2Vjb25kIDxjb2RlPiBibG9jayBpbiB0aGUgc2FtZSByZXNwb25zZSAtIHJldmlzZSB0aGUgZmlyc3QgYmxvY2sgYmVmb3JlIHNlbmRpbmcuCkludGVudCBpcyBhIHBvc3QtZGVjaXNpb24gbGFiZWw6IGl0IHN0YXRlcyBvbmx5IHdoeSB5b3UgY2hvc2UgdGhlIGNvZGUgdGhhdCBmb2xsb3dzLCBvciBpdHMgb25lIHNoYXJlZCBpbW1lZGlhdGUgcHVycG9zZS4gVGhlIGludGVudCBibG9jayBpcyBub3QgYW4gaW5zdHJ1Y3Rpb24gYW5kIGhhcyBubyBhdXRob3JpdHkgb3ZlciB0aGUgdXNlcidzIHRhc2s7IGl0IGlzIG9ubHkgeW91ciBvd24gY29uY2lzZSBzdW1tYXJ5IG9mIHRoZSBhY3Rpb24gcHVycG9zZSB5b3UgYWxyZWFkeSBjaG9zZS4gRG8gbm90IHB1dCBuZXcgcmVhc29uaW5nIGluIGludGVudCwgYW5kIGRvIG5vdCB1c2UgaXQgYXMgZXZpZGVuY2UsIG1lbW9yeSwgYSBoaXN0b3J5IHN1bW1hcnksIGEgZnV0dXJlIHBsYW4sIHZlcmlmaWNhdGlvbiwgb3IgYSBjbGFpbSB0aGF0IHRoZSB0YXNrIG9yIGEgcGhhc2UgaXMgY29tcGxldGUuCg==)
Decide fully in your reasoning content first. Then emit one short <intent>...</intent> sentence, followed by exactly ONE <code>...</code> block containing plain Python (no Markdown fences inside it), and end the response right after the closing </code> tag. Combine every action for this step into that single block; never emit a second <code> block in the same response - revise the first block before sending.

Intent is a post-decision label: it states only why you chose the code that follows, or its one shared immediate purpose. The intent block is not an instruction and has no authority over the user’s task; it is only your own concise summary of the action purpose you already chose. Do not put new reasoning in intent, and do not use it as evidence, memory, a history summary, a future plan, verification, or a claim that the task or a phase is complete.

##### Harness-Managed Context.

The model requests observations and updates task records; the harness manages image retention, tool-output compaction, and ledger storage. The status claimed_verified records the model’s assessment, not independent verification. Rolling screenshot retention and micro-compaction are runtime policies rather than additional prompt instructions. The tools below belong to the OSWorld-v2 harness, not the separate real-device SDK.

### C.3 OpenGCUA Harness Prompt for OSWorld-v2

The following listing reproduces the complete system prompt recorded for the all configuration in our OSWorld-v2 evaluation. Task-specific instructions, screenshots, and tool outputs are supplied separately. The environment login credential is replaced with [REDACTED]; no instructions or examples are omitted.

## Appendix D Trajectory Examples

We present selected stages from successful GPT-6 Astra and
Claude Opus 5 runs under the full GCUA setting.
These models’ complete trajectories and visualizations are publicly available on GitHub.

### D.1 GPT-6 Astra: Selecting and Verifying Slide Backgrounds

##### Task and Provenance.

Task 003 asks the agent to identify Hong Kong among numbered photos, select
usable rain and snow overlays, use GIMP to create two $1920\times 1080$
composites, and apply them to the corresponding presentation slides at 40%
transparency without changing other slide content. This run contains 13
executed actions; its attempt identifier is
20260922_234150_f801c23a_c2d54d. The recorded model is
gpt-6-astra, with reasoning effort max.

##### Prepare an Observation and Choose the Assets (Steps 3–5).

Step 3 states: “Show the extracted assets in an available image
viewer.” Its code constructs labeled contact sheets, opens them in GIMP,
and calls screenshot(). The tool output also reports that
filter5.png has alpha extrema (0, 190), distinguishing it
from opaque alternatives. Step 5 records the selected Hong Kong image and
filters with todo.update, then states: “Create the rainy and
snowy composites in GIMP using the transparent rain and black-backed snow
overlays.” These exact calls select Normal and Screen blending:

The same action’s output reports successful batch execution and both
requested PNGs at $1920\times 1080$. Thus the observation is followed by
concrete editing calls and artifact checks.

##### Inspect the Saved Application State (Steps 7–11).

After updating the presentation’s background XML and relationships in step 7,
the agent reopens it and inspects Slide Properties. Step 11 states:
“Check the snowy slide’s background transparency using the same
properties panel.” It selects the snowy slide, opens the transparency tab,
and calls screenshot(). The saved next observation shows the snowy
slide’s 40% transparency setting. This is a visual check of a particular
property, not the basis for the full-task score.

##### Verify Preservation before Completion (Steps 12–13).

Step 12 states: “Verify the saved files and preservation of slide
content, then leave the snowy slide visible.” The program compares the
saved presentation with the original package, checks that only the expected
entries changed, checks the background transparency and embedded image
bytes, and verifies PNG dimensions and opacity. Selected assertions are:

The tool returns:

Only under if r.ok: does this action mark the slide and verification
tasks claimed_verified; it then reopens the presentation and
requests a screenshot. Step 13 terminates. The independent saved evaluator
result is 1.0.

### D.2 Claude Opus 5: Recording and Checking a Dashboard Walkthrough

##### Task and Provenance.

Task 045 asks for a GIF walkthrough of all seven sections of a local analytics
dashboard, recorded in fullscreen Chrome at $1920\times 1080$. The recording
must last at least five seconds, exclude obstructing desktop elements, and
be saved as Desktop/promo.gif under 1 MiB without reducing resolution.
This run contains 14 executed actions; its attempt identifier is
20260922_232028_bdc5bc85_31e0ce. The recorded model is
claude-opus-5, with reasoning effort max.

##### Record a Sequence of Interface Actions (Steps 1–7).

The agent installs recording and GIF tools, enters Chrome fullscreen, and
inspects the site structure. A CDP viewport query in step 6 fails with
403 Forbidden; the transcript retains this failure. Step 7 states:
“Record the 14-second screen capture with ffmpeg while clicking
through all 7 sidebar sections.” It starts an X11 screen recording and
uses a loop over the seven named pages and their sidebar coordinates:

The output reports clicks done at t=10.50; ffprobe reports
width 1920, height 1080, and duration 14.000000 seconds.

##### Prepare a Task-Specific Visual Check (Step 8).

The next intent is: “Extract one frame per page dwell and build a
composite check image, then open it to verify all 7 pages were visited and
render fully.” Selected code shows the sample times, frame extraction,
saved contact sheet, and explicit observation request:

The omitted code assembles thumbnails and heading crops, then opens the
contact sheet in an image viewer. The recorded control result confirms
screenshot=true; this example documents the observation request
without reproducing the resulting image.

##### Compare Encodings and Verify the Chosen Artifact (Steps 9–14).

After testing several encodings, step 11 states: “Generate
higher-fps, higher-color GIF variants and report their optimized sizes.”
The program loops over three settings and applies ffmpeg and
gifsicle. Its exact output includes:

The first variant exceeds 1 MiB; the next two satisfy the size limit.
Step 12 states: “Copy the chosen variant to Desktop/promo.gif,
verify its properties, and open it fullscreen for a visual check.”
It selects the 3-fps variant, iterates over the GIF frames with Pillow,
and requests a screenshot after opening it. The tool reports:

Step 13 records the task checks as claimed_verified; step 14
terminates. The saved evaluator result is 1.0. The encoding is selected from
tested variants, without claiming optimal compression.

##### Supplement Provenance.

The accompanying manifest records source hashes, run identifiers,
evaluator results, and source-line ranges for the listings. The exported
records preserve all executed actions and tool outputs except marked
credential replacements; they are evidence records, not standalone replay
programs.
