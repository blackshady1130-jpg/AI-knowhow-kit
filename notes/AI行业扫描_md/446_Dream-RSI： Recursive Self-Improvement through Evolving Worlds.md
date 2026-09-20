# Dream-RSI: Recursive Self-Improvement through Evolving Worlds

Source URL: https://arxiv.org/html/2609.14858v1

Authors: Tong Zheng Affiliation: \thepa Affiliation: University of Maryland, College Park Xidong Wu Affiliation: \thepa Zheng Zhang Affiliation: \thepa Zhankui He Affiliation: Google Deepmind Chaoyi Zhang Affiliation: \thepa Benjamin Coleman Affiliation: Google Deepmind Ruoqiao Wei Affiliation: \thepa Di Bai Affiliation: Google Deepmind Haolin Liu Affiliation: University of Virginia Rui Liu Affiliation: University of Maryland, College Park Xue Wang Affiliation: \thepa Yue Zhuan Affiliation: \thepa Wang-Cheng Kang Affiliation: Google Deepmind Renkai Xiang Affiliation: \thepa Heng Huang Affiliation: University of Maryland, College Park Xinwu Cheng Affiliation: \thepa Yunsong Guo Affiliation: \thepa

###### Abstract

Recursive self-improvement is becoming increasingly vital for autonomous AI agents, where progress hinges on discovering high-value solutions across complex domains. The driver of this process is effective exploration, however, managing and improving exploration strategies remains a major bottleneck. Current systems face a fundamental dilemma: fixed strategies fail to adapt as search spaces scale, while online policy optimization requires navigating vast meta-search spaces under delayed and expensive feedback over long-horizon rollouts. We introduce

Dream-RSI

, a framework for scalable and recursively self-improving exploration. A lightweight orchestration layer makes exploration explicit and programmable while leaving the underlying coding agent unchanged. Our key insight is that accumulated discovery history can serve as a replay simulator over the realized search space. By performing dreaming in the replay simulator constructed from historical discovery trees,

Dream-RSI

secures immediate, low-cost off-policy feedback to evaluate and refine exploration policies without invoking repetitive, expensive online evaluations. The improved policy is subsequently redeployed online to drive further discovery, continuously expanding the simulator pool in a self-improving loop. Across algorithm engineering, mathematical optimization, and GPU kernel engineering,

Dream-RSI

achieves competitive or improved discovery quality while substantially reducing discovery cost in several settings.

[github.com/zhengkid/Dream-RSI](https://github.com/zhengkid/Dream-RSI)

|

[dream-rsi.com](https://dream-rsi.com/)

## Introduction

Figure 1: Overview of Dream-RSI. The system operates in a recursive self-improvement loop via three core stages: ① Online Explore, where the current exploration policy guides a coding agent to expand a discovery tree and log historical traces; ② Construct Replay Simulator, where the generated discovery tree is converted into a reusable simulator pool; and ③ Dreaming-based Policy Improvement, where the agent "dreams" up a massive pool of alternative policies in its mind. It then feeds these candidate policies into the replay simulator to simulate executions and derive rapid feedback, continuously refining its strategy (detailed in the Zoom-in box). The updated policy then redeploys for the next round of online exploration.

Recursive self-improvement (RSI) has emerged as an ambitious goal for autonomous AI systems

([Liu et al., 2026c](#bib.bib25))

. A common mechanism underlying RSI is an iterative discovery loop wherein agents generate candidate solutions, evaluate outcomes, incorporate feedback, and refine future iterations. Such discovery loops have driven substantial progress across scientific and algorithmic domains, including algorithm design

([Novikov et al., 2025](#bib.bib27); [Romera-Paredes et al., 2024](#bib.bib33))

, open-ended mathematical optimization

([Georgiev et al., 2025](#bib.bib7); [Anthropic, 2026](#bib.bib1))

, systems design

([Jaber and Jaber, 2026](#bib.bib18); [Cao et al., 2026](#bib.bib3))

, and agent self-improvement

([Zhang et al., 2026b](#bib.bib48); [Zhang et al., 2026c](#bib.bib49); [Lee et al., 2026](#bib.bib22); [Zheng et al., 2026a](#bib.bib51))

, with these discoveries increasingly feeding into the development of more capable AI systems. As agent capabilities improve and self-improvement targets become challenging, discovery increasingly requires long-horizon exploration over vast search spaces, often spanning thousands of proposal–evaluation cycles

([Ye et al., 2026](#bib.bib45); [OpenAI, 2026](#bib.bib28))

. At this scale, the ability to orchestrate exploration becomes critical

([Zheng et al., 2026b](#bib.bib52))

. Poor exploration can waste substantial computation and time, severely limiting the efficiency and scalability of RSI.

Existing approaches have largely relied on manually designed exploration strategies that remain largely fixed throughout discovery

([Novikov et al., 2025](#bib.bib27); [Yan et al., 2026b](#bib.bib44); [Du et al., 2026](#bib.bib5); [Jiang et al., 2026](#bib.bib19); [Ye et al., 2026](#bib.bib45))

. Fixed strategies cannot improve from accumulated discovery experience and may repeatedly allocate computation to ineffective search directions. Recent work therefore seeks to optimize exploration policies online during discovery

([Liu et al., 2026a](#bib.bib23))

, but doing so faces two fundamental bottlenecks. First, feedback is delayed and expensive at the meta level: unlike evaluating an individual candidate, assessing an exploration policy requires observing how it shapes the subsequent discovery process over many proposal–evaluation cycles. Second, the meta-policy space is vast: a newly proposed policy may perform poorly, so many alternatives may need to be tried. Together, these challenges make meta-level improvement particularly costly: each policy may require a long online rollout before receiving useful feedback, making it difficult to efficiently close the self-improvement loop at the exploration layer.

To address these bottlenecks, our key intuition is simple: a fast and inexpensive simulator of discovery would allow many exploration policies to be evaluated before costly online deployment.

Surprisingly, completed discovery histories already provide such a simulator.

While prior work treats past discovery history merely as static textual context

([Hu et al., 2025](#bib.bib14); [Ouyang et al., 2026b](#bib.bib31))

or training data for weight fine-tuning

([Yuksekgonul et al., 2026](#bib.bib46); [Wang et al., 2025](#bib.bib37))

, a completed discovery process inherently records a structured tree of past exploration decisions and their realized code-execution outcomes. Drawing an analogy to model-based reinforcement learning and World Models

([Ha and Schmidhuber, 2018](#bib.bib9); [Hafner et al., 2023](#bib.bib12))

(§

[2](#S2)

), once organized into a discovery tree, this history can serve as a

replay simulator

11
1
            
            
            
          We use the terms replay simulator and worlds interchangeably.

. As illustrated in Figure

[2](#S1.F2)

, an alternative exploration strategy can navigate this pre-recorded tree to traverse different subsets of recorded branches, in different orders, with different parallel groupings and stopping decisions. Because all execution outcomes are already saved in the tree, evaluating a new strategy requires only reading past records without rerunning the underlying discovery agent or evaluator. This transforms meta-policy improvement from an expensive online trial-and-error process into a fast, simulation-based “dreaming” procedure.

Building on this insight, we introduce

Dream-RSI

, a framework for scalable and recursively self-improving meta-exploration in agent-driven discovery. We first make exploration explicit and programmable through a lightweight orchestration layer that controls branching, parallel exploration, and stopping while leaving the underlying coding agent unchanged. Rather than keeping this policy fixed,

Dream-RSI

establishes a closed-loop self-improvement mechanism across three core stages (Figure

[1](#S1.F1)

):

(1) Online Exploration

, where the current policy guides real-world discovery and logs historical execution traces;

(2) Simulator Construction

, where recorded discovery trees are converted into a reusable replay simulator pool; and

(3) Dreaming-based Policy Improvement

, where candidate policies are evaluated via low-cost "dreaming" over the simulator. The updated policy is then redeployed online to generate new discovery experience and expand the simulator pool, closing a RSI loop at the meta-exploration layer.

Empirically, we evaluate

Dream-RSI

across 8 scientific discovery tasks spanning three distinct domains: algorithm engineering, mathematical optimization, and GPU kernel engineering. In algorithm engineering (Lasso path solver),

Dream-RSI

outperforms standard libraries like

sklearn

and strong baselines while reducing agent calls by up to

$162\times$

over

SimpleTES

and

$1.7\times$

over fixed-exploration baselines. In mathematical optimization (sum-difference, autocorrelation, circle packing), it matches or surpasses strong baselines within

$1\text{k}$

generations, yielding over

$50\times$

budget savings compared to

SimpleTES

. In GPU kernel engineering (KernelBench), it either reaches target execution speeds using

$1.79\times$

–

$2.43\times$

fewer generations or improves kernel performance by up to

$2.09\times$

under identical budget constraints.

In summary, our main contributions are as follows: 1)

History as Replay Simulator:

We conceptualize completed discovery histories as replay simulators. This makes delayed exploration feedback reusable for efficient meta-exploration policy evaluation.; 2)

Meta-Layer RSI Loop (Dream-RSI):

We introduce

Dream-RSI

, establishing a recursive self-improvement loop that continuously collects discovery histories through online exploration, constructs replay simulators from history to refine meta-exploration strategies via dreaming, and redeploys the upgraded policy online; 3)

Empirical Validation:

We conduct experiments to demonstrate that

Dream-RSI

improves both discovery effectiveness and efficiency in several settings.

Figure 2: Discovery history as a replay simulator. A deployed policy first explores online to generate a structured discovery tree containing historical execution traces (each node denote an attempt with its full observation). Thousands of candidate policies can then be tested within this simulator—evaluating alternative choices of search branches, exploration orders, concurrency levels, and stopping rules. Since all node outcomes are pre-stored, a single costly online run enables thousands of rapid, zero-execution-cost off-policy evaluations. This enables policy improvement through historical replay: the agent can “dream” over many alternative exploration strategies before redeploying the improved policy online.

## Motivation: Discovery History as a Replay Simulator

Consider an agent navigating toward a goal in an unfamiliar environment. During its first traversal, the agent may follow inefficient routes, encounter dead ends, backtrack, and gradually construct a map of the surrounding space. Once recorded, however, this experience becomes reusable: the resulting map supports planning without requiring the agent to physically revisit every location. A new navigation policy can instead reason over the accumulated map, avoid known dead ends, reconsider earlier decisions, and compare alternative routes before acting

([Gupta et al., 2017](#bib.bib8))

.

This idea parallels model-based reinforcement learning

([Sutton, 1990](#bib.bib35); [M. Moerland et al., 2023](#bib.bib26))

. A model captures how an environment evolves in response to an agent’s actions, allowing policies to be trained or evaluated through simulated experience rather than repeated interaction with the real environment

([Ha and Schmidhuber, 2018](#bib.bib9))

. The Dreamer family

([Hafner et al., 2019](#bib.bib10); [Hafner et al., 2020](#bib.bib11); [Hafner et al., 2023](#bib.bib12); [Hafner et al., 2025](#bib.bib13))

demonstrates this principle particularly clearly: an agent learns a compact dynamics model from collected experience and improves its policy by imagining trajectories within that model.

Long-horizon discovery admits an analogous structure. An exploration policy decides which directions to pursue, which candidates to refine, which branches to explore in parallel, and when to terminate. Executing the policy online produces a structured discovery history containing the explored branches, decision points, computational costs, and realized outcomes. As illustrated in Figure

[2](#S1.F2)

, this history can subsequently be treated as an

empirical replay simulator

: a grounded model of the portion of the discovery space that has already been observed.

Within this replay simulator, alternative exploration policies induce different trajectories through the recorded discovery tree. A policy may select a different subset of branches, prioritize them in a different order, issue different requests in parallel, or stop at an earlier point. Evaluating such a trajectory requires only revealing the outcomes already stored along the selected branches, rather than rerunning the underlying coding agent and evaluator. Consequently, a single expensive online discovery run can support many inexpensive evaluations of alternative exploration strategies.

## Dream-RSI: Recursive Self-Improvement through Evolving Worlds

As shown in Figure

[1](#S1.F1)

,

Dream-RSI

alternates between online exploration and offline “dreaming” to improve an executable

exploration policy

that allocates discovery computation. During the online phase, the policy guides a fixed

discovery agent

, while a fixed

evaluator

scores the resulting candidates and provides diagnostic feedback. The resulting

discovery tree

serves as a

replay
world

in which alternative policies can be evaluated using recorded outcomes. A fixed LLM-based

policy-development agent

uses this feedback to revise the

exploration policy

code, and the best evaluated version is deployed for the next online rollout. Only the exploration-policy code changes; the underlying models, evaluator, and execution interfaces remain fixed.

Discovery trees and the shared decision interface.

A discovery tree is rooted at $r$, which represents the initial
workspace state. Each non-root node $v$ has exactly one
primary parent, either the root or a previously created node.
This parent identifies where the attempt in $v$ begins:
the discovery agent resumes the parent’s saved workspace and uses
its accumulated observations as context to produce a new attempt. Node $v$ preserves this
inherited history and records the outcome of the new
generation–evaluation attempt, including the resulting filesystem
snapshot, generated artifact, evaluation diagnostics, and score $s_{v}$.
Scores follow a fixed task-scoring protocol, with larger values
indicating better quality.

In both online execution and offline replay, the exploration policy
observes a tree $\mathcal{T}$, initially containing only the root,
and selects the nodes from which to continue exploration.
The eligible nodes form the set
$A(\mathcal{T})=\{r\}\cup\{v\in\mathcal{T}:v\text{ is a leaf}\}$,
where leaves are determined from the currently observed tree.
Let $W\geq 1$ be the number of parallel workers, each of which can
execute one generation–evaluation request at a time (e.g. concurrent API calls).
The exploration policy’s action is a batch $C\in A(\mathcal{T};W)$, where
$A(\mathcal{T};W)=\{C\subseteq A(\mathcal{T}):|C|\leq W\}$ is the feasible batch set.
Each selected node specifies the starting point of one attempt,
so the batch determines both where exploration continues and
how many attempts are scheduled in parallel. Both the online and offline phases use this same decision interface but differ in the
transition that follows a selected batch.

Online rollout.

Let $t=1,2,\ldots$ index the outer iterations, starting from an
initial policy $\pi_{1}$ and an empty history $\mathcal{H}_{0}=()$.
At iteration $t$, policy $\pi_{t}$ guides a new online rollout
with access to the completed discovery history $\mathcal{H}_{t-1}$.
This history provides context for exploration but remains separate
from the new tree being constructed. The policy code stays fixed
throughout the rollout.

Let $\mathcal{T}_{t}^{k}$ denote the new discovery tree after $k$
completed decision rounds, with $\mathcal{T}_{t}^{0}=\{r\}$.
The rollout allows at most $K_{1}$ rounds. At round $k\leq K_{1}$, the exploration policy chooses a node batch $C_{t}^{k}\in A(\mathcal{T}_{t}^{k};W)$ and each node $v\in C_{t}^{k}$ is assigned to a worker.
The discovery agent uses $v$’s saved workspace and available
context to produce a new candidate, and the evaluator assesses
the result. These attempts run in parallel, each producing one
new child of its selected parent. Attaching the completed children
to the current tree yields $\mathcal{T}_{t}^{k+1}$, while all
previously recorded nodes remain unchanged. This transition is stochastic because the discovery agent may
generate different outcomes from the same starting workspace. For the next round, the newly created
child becomes the selectable leaf of an extended branch, while the root remains selectable for opening further branches. The rollout ends when the policy selects an empty batch or completes $K_{1}$ decision rounds. After the rollout terminates, its final tree is recorded as
$\mathcal{T}_{t}$ and appended to the history, giving
$\mathcal{H}_{t}=\mathcal{H}_{t-1}\cup\{\mathcal{T}_{t}\}$.
The method then enters the offline phase using this expanded collection of replay worlds.

Offline evaluation.

During the offline phase of outer iteration $t$, the history
$\mathcal{H}_{t}$ remains fixed while the method constructs and
evaluates $M\geq 1$ policy versions
$\pi_{t}^{0},\ldots,\pi_{t}^{M-1}$, starting with
$\pi_{t}^{0}=\pi_{t}$.
Each version is evaluated separately on every historical tree
$\mathcal{T}_{i}$, $i=1,\ldots,t$, before the next version is
developed from the resulting feedback.
We use $m$ to index policy versions, $i$ to index replay worlds, and $k$ to count decision rounds within one policy–world
evaluation. The outer index $t$ is fixed throughout this phase
and is suppressed in the notation for replay trajectories and scores.

For each policy–tree pair $(m,i)$, replay resets the policy’s
per-rollout state and starts from $\mathcal{T}_{i}^{m,0}=\{r\}$.
Here, $\mathcal{T}_{i}^{m,k}\subseteq\mathcal{T}_{i}$ denotes the subtree
revealed after $k$ completed rounds. The full recorded tree
$\mathcal{T}_{i}$ remains fixed; only the portion observed by the
policy evolves. At each decision, $\pi_{t}^{m}$ selects a batch
$C_{i}^{m,k}\in A(\mathcal{T}_{i}^{m,k};W)$ using the revealed
observations. Unlike online execution, replay returns recorded children of the
selected nodes deterministically rather than generating new candidates.
After the exploration policy takes a nonempty batch $C_{i}^{m,k}$, the next observed tree is
$\mathcal{T}_{i}^{m,k+1}=\mathcal{T}_{i}^{m,k}\cup\bigcup_{v\in C_{i}^{m,k}}\operatorname{Child}(v;\mathcal{T}_{i},\mathcal{T}_{i}^{m,k})$ where $\operatorname{Child}(v;\mathcal{T}_{i},\mathcal{T}_{i}^{m,k})$ denotes the node set containing unobserved children of $v$ on tree $\mathcal{T}_{i}$ given the current observed tree $T_{i}^{m,k}$. For $v\neq r$, $\operatorname{Child}(v;\mathcal{T}_{i},\mathcal{T}_{i}^{m,k})$ is $v$’s unique recorded child, if one exists. Since $v$ is a leaf of $\mathcal{T}_{i}^{m,k}$, that child is still unrevealed.
For $v=r$, replay returns the earliest-created child of $r$
outside $\mathcal{T}_{i}^{m,k}$, opening one previously unrevealed branch.
In either case, $\operatorname{Child}(v;\mathcal{T}_{i},\mathcal{T}_{i}^{m,k})=\emptyset$ when no recorded continuation remains. The newly revealed nodes expose their stored observations before
the policy makes its next decision.

Replay allows at most $K_{2}$ decision rounds where each nonempty batch counts as one round, and terminates when
the policy selects $C_{i}^{m,k}=\emptyset$, the round limit
$k=K_{2}$ is reached, or $\mathcal{T}_{i}^{m,k}=\mathcal{T}_{i}$,
meaning that all recorded nodes have been revealed.
Let $k_{i}^{m,\star}\in\{0,\ldots,K_{2}\}$ denote the number of
completed rounds at termination, yielding the final subtree
$\mathcal{T}_{i}^{m,k_{i}^{m,\star}}\subseteq\mathcal{T}_{i}$.

Thus, replay evaluates how far to pursue each opened branch,
how to group attempts into parallel batches, and when to open
another branch or stop. These decisions may differ across policies,
but each branch is traversed in its recorded parent–child order,
and no outcomes beyond $\mathcal{T}_{i}$ are generated.

Replay objective.

The replay objective balances discovery quality, execution cost,
and parallelism. Let
$N_{i}^{m}=|\mathcal{T}_{i}^{m,k_{i}^{m,\star}}|-1$
be the number of revealed non-root nodes.
Although replay itself does not execute new discovery attempts,
$N_{i}^{m}$ counts the generation–evaluation requests represented
by its trajectory.
For fixed coefficients $\beta_{1},\beta_{2}\geq 0$, the replay score is

$$V_{i}^{m}=\underbrace{\max_{v\in\mathcal{T}_{i}^{m,k_{i}^{m,\star}}}s_{v}}_{\text{discovery quality}}-\underbrace{\beta_{1}N_{i}^{m}}_{\text{execution cost}}+\underbrace{\beta_{2}\frac{N_{i}^{m}}{\max\{1,k_{i}^{m,\star}\}}}_{\text{parallelism bonus}}.$$

(1)

The first term measures the best solution quality attained during
replay. The second penalizes the
number of attempted generations. For a nonempty replay, the third
rewards the average number of attempts executed per decision round,
favoring policies that batch useful continuations rather than
execute them sequentially.

Policy improvement and selection.

The evaluation score of policy version $\pi_{t}^{m}$ is its average
replay score across the fixed history,
$V^{m}=\frac{1}{t}\sum_{i=1}^{t}V_{i}^{m}$.
The offline phase begins by evaluating the current policy
$\pi_{t}^{0}=\pi_{t}$.
For each $m=0,\ldots,M-1$, the policy-development agent examines
the replay trajectories and scores of $\pi_{t}^{m}$, together with
feedback from earlier revisions, to identify successful decisions
and recurring failures. It then revises the executable policy code
to produce $\pi_{t}^{m+1}$, which is evaluated on the same
$t$ replay worlds.
Replay feedback is available to the development agent between
revisions.

After $M$ revisions, the next online policy is selected from all
$M$ evaluated versions as $\pi_{t+1}=\pi_{t}^{m^{\star}}$, where
$m^{\star}\in\operatorname*{arg\,max}_{m\in\{0,\ldots,M-1\}}V^{m}$.
Because the candidate set includes the current policy, this
selection satisfies $V^{m^{\star}}\geq V^{0}$.
Thus, the selected policy $\pi_{t+1}$ is no worse than the current policy $\pi_{t}$
in average replay score on the fixed history $\mathcal{H}_{t}$. The selected policy is then deployed online to collect
$\mathcal{T}_{t+1}$, expanding the history available for the next offline improvement phase.

## Experiments

We evaluate

Dream-RSI

across three scientific discovery domains: algorithm engineering, kernel optimization and math optimization. Our primary controlled baseline is Recursive Fixed Exploration, which uses the same underlying discovery setting and initialization but keeps the exploration policy fixed across recursive discovery rounds. We additionally compare against task-specific domain baselines.

Across all tasks,

Dream-RSI

and Recursive Fixed Exploration use the same discovery agent, evaluator, initialization, and resource constraints. Both methods start from the same manually designed exploration policy. This exploration policy follows a simple

parallel refining

strategy: it launches multiple independent exploration workspaces in parallel, with each workspace maintaining its own local discovery trajectory and repeatedly refining its current candidate based on the history accumulated within that workspace. The two methods therefore follow the same exploration policy in the first discovery round. In subsequent rounds, while Recursive Fixed Exploration keeps its exploration policy static,

Dream-RSI

progressively refines the policy by dreaming over a replay simulator conditioned on accumulated global discovery history, subsequently deploying the updated policy in each new round. The discovery cost is quantified by the total cumulative number of discovery-agent calls.

Specifically, we evaluate Gemini-3.1 Pro and Gemini-3.7-Flash across multiple recursive discovery rounds via the Gemini CLI

22
2
[https://geminicli.com/](https://geminicli.com/)

. Under Recursive Fixed Exploration, each round for Gemini-3.1 Pro executes 10 parallel workspaces with up to 11 refinement steps (

$10\times 11=110$

discovery-agent calls), whereas Gemini-3.7-Flash operates 32 parallel workspaces with up to 20 refinement steps (

$32\times 20=640$

calls).

Dream-RSI

maintains identical per-round budgets, aligning with the baseline in Round 1 while progressively updating its policy in subsequent rounds. Further details on recursive rounds, task setups, resource budgets, and evaluation protocols follow below.

Figure 3: Lasso regularization-path discovery results. (a) Final wall-clock runtime on six held-out downstream tasks; lower is better. Compute denotes the cumulative number of discovery-agent calls. (b) Recursive discovery dynamics. Average downstream runtime across six held-out tasks versus cumulative discovery compute for Gemini-3.1-Pro and Gemini-3.7-Flash. Numbers next to markers denote recursive rounds (iterations). Lower is better.

Algorithm Engineering

In this task, we consider Lasso Regularization Path as our algorithm-engineering task, a fundamental computational primitive in high-dimensional statistics that is widely used in model selection and cross-validation across domains such as genomics and finance. We follow the benchmark setting of SimpleTES ([Ye et al., 2026](#bib.bib45)), where the goal is to discover efficient implementations of the complete Lasso regularization path while preserving numerical correctness. During discovery, we use the same 17 synthetic instances as SimpleTES, which cover diverse problem regimes in terms of dimensionality, sparsity, feature correlation, and active-set structure. To evaluate whether the discovered algorithms generalize beyond the search distribution, we additionally evaluate them on six held-out downstream datasets spanning both biological and non-biological domains.

Baselines and Setup.

We compare against standard Lasso solvers
sklearn ([Pedregosa et al., 2011](#bib.bib32)) and
glmnet ([Friedman et al., 2010](#bib.bib6)),
as well as SimpleTES ([Ye et al., 2026](#bib.bib45)), which uses
GPT-OSS-120B with a reported budget of 51,200 generations.
We additionally include Recursive Fixed Exploration as our controlled baseline. Specifically, we run both Recursive Fixed Exploration and Dream-RSI for 5 rounds.

Main Results.

Figure [3](#S4.F3)(a) summarizes the Lasso discovery results.
Across both discovery-agent backbones, Dream-RSI achieves a better
downstream quality–compute trade-off than Recursive Fixed Exploration.
With Gemini-3.1 Pro, it reduces the average runtime across the six held-out
datasets from 3587.1 ms to 2931.0 ms while using only 317 discovery-agent
calls, compared with 550 calls for fixed exploration.
With Gemini-3.7-Flash, Dream-RSI further reduces the average runtime
from 2516.7 ms to 2350.6 ms using 1879 calls instead of 3200. Despite using substantially less discovery compute, the resulting solvers also
outperform the standard sklearn and glmnet implementations on all six held-out
datasets. Compared with SimpleTES, which uses 51,200 generations,
Dream-RSI achieves lower average downstream runtime with roughly
two orders of magnitude fewer discovery-agent calls. Notably, the program discovered by Gemini-3.1-Pro appears particularly well suited to large-scale matrices such as RCV1. In contrast, Gemini-3.7-Flash discovers a more general-purpose program that performs consistently across different problem scales.

Recursive Discovery Dynamics.

Figure [3](#S4.F3)(b) illustrates the trajectory of downstream performance across recursive discovery rounds relative to cumulative discovery compute. By design, both methods share identical search behavior in the initial round. In subsequent rounds, Recursive Fixed Exploration maintains a static exploration policy, whereas Dream-RSI progressively refines and redeploys its policy via dreaming over accumulated discovery history. Consequently, the two trajectories diverge markedly: Dream-RSI consistently achieves superior downstream performance while requiring substantially lower cumulative compute across both Gemini-3.1-Pro and Gemini-3.7-Flash.

Discovered Solver Analysis.

We further analyze the discovered solver, with its implementation provided in
the Appendix [C](#A3). Unlike SimpleTES, which switches between LARS and coordinate
descent according to problem dimensions, the discovered solver introduces
adaptivity within the active-set optimization itself. It combines strong-rule
screening with Cauchy–Schwarz-based KKT pruning, selectively recomputing exact
gradients only when the bound cannot certify a feature and falling back to a
full refresh when pruning becomes ineffective. This adaptive verification
scheme is further integrated with efficient active-set bookkeeping, lazy
Gram-matrix construction, and hardware-aware implementation.

Table 1: 
Performance comparison on mathematical discovery tasks.
Higher is better for Sum Diff and Circle Packing, while lower is better for Auto Correlation.
Best results are shown in bold.

Method
LLM
Sum Diff ($\uparrow$)
Auto Correlation ($\downarrow$)
Circle Packing ($\uparrow$)

AlphaEvolve
Gemini-2.0 Pro + Flash
–
1.455700
2.635862

AlphaEvolveV2
Gemini-2.0 Pro + Flash
1.121936
–
2.635983

OpenEvolve
-
–
1.460000
-

CodeEvolve
-
–
–
2.635980

ShinkaEvolve
Mixed
–
1.457800
2.635982

TTS-Discovery
Qwen3-8B
–
–
2.635983

ThetaEvolve
Distilled-Qwen3-8B
–
1.493000
2.635983

EvoX
Gemini-3.0-Pro
–
1.458900
2.635900

SimpleTES
GPT-OSS-120B
1.143975
1.453675
2.635983

Our System

Recursive Fixed Exploration
Gemini-3.1-Pro
1.144047
1.456001
2.635983

Dream-RSI
Gemini-3.1-Pro
1.145427
1.456375
2.635983

Mathematics Optimization

We further evaluate Dream-RSI on three mathematical discovery tasks spanning discrete combinatorial optimization, geometric optimization, and functional optimization: the Sum–Difference Problem, Circle Packing, and Autocorrelation Inequalities. The goal of these problems is to discover high-quality solutions that optimize task-specific mathematical objectives under their respective constraints. Formal definitions of the three tasks are provided in Appendix.

We use Gemini-3.1 Pro via the Gemini CLI as the discovery agent for both Recursive Fixed Exploration and Dream-RSI for 10 rounds. For each task, the agent iteratively proposes and evaluates candidate constructions or optimization procedures according to the task-specific objective. We compare against a broad set of existing automated discovery systems, including AlphaEvolve ([Novikov et al., 2025](#bib.bib27)), AlphaEvolveV2 ([Georgiev et al., 2025](#bib.bib7)), OpenEvolve ([Sharma, 2025](#bib.bib34)), CodeEvolve ([Assumpção et al., 2025](#bib.bib2)), ShinkaEvolve ([Lange et al., 2026](#bib.bib21)), TTS-Discovery ([Yuksekgonul et al., 2026](#bib.bib46)), ThetaEvolve ([Wang et al., 2025](#bib.bib37)), EvoX ([Liu et al., 2026a](#bib.bib23)), and SimpleTES ([Ye et al., 2026](#bib.bib45)).

Results.

Table [1](#S4.T1) summarizes the results across the three mathematical discovery tasks.
Dream-RSI achieves a Sum–Difference score of $1.145427$, outperforming SimpleTES and Recursive Fixed Exploration.
On Circle Packing, it reaches $2.635983$, matching the strongest reported result among the compared methods.
For Autocorrelation, Dream-RSI obtains $1.456375$, remaining competitive with existing discovery systems. Notably, SimpleTES achieves state-of-the-art performance on Autocorrelation Inequalities, but requires 51,200 generations, significantly more than the fewer than 1,000 generations used by our approach.
Overall, these results show that our Dream-RSI generalize well on mathematics optimization.

$0.35$$0.4$$0.45$$0.5$$0.55$

$2.43\times$ fewer costs

(comparable performance)
Performance ($1/\mathrm{ms}$)VGG16$1.05$$1.1$$1.15$

$1.79\times$ fewer costs

(comparable performance)
LayerNorm$0$$250$$500$$750$$1{,}000$$0.4$$0.8$$1.2$$1.6$$2$

$2.09\times$ higher score

(Similar Budget)
Number of GenerationsPerformance ($1/\mathrm{ms}$)ConvDiv$0$$250$$500$$750$$1{,}000$$0.25$$0.3$$0.35$$0.4$$0.45$

$1.44\times$ higher score

(Similar Budget)
Number of GenerationsConvMaxDream-RSIRecursive Fixed Exploration
Figure 4: 
GPU kernel engineering results.
Discovery performance of Dream-RSI and Recursive Fixed Exploration as a function of the number of generations.
On VGG16 and LayerNorm, Dream-RSI reaches comparable performance with $2.43\times$ and $1.79\times$ fewer generations, respectively.
On ConvDiv and ConvMax, it achieves $2.09\times$ and $1.44\times$ higher performance under comparable discovery budgets.
Higher is better for all tasks.

Kernel Engineering

We further evaluate Dream-RSI on GPU kernel engineering, where the goal is to automatically discover high-performance implementations of kernels while preserving numerical correctness. Unlike mathematical discovery, kernel engineering requires reasoning jointly about algorithmic structure, memory access, parallelization, and hardware-specific optimizations, providing a substantially different testbed for evaluating whether our Dream-RSI generalizes across discovery domains.

We consider four representative kernel-engineering tasks from KernelBench ([Ouyang et al., 2025](#bib.bib29)): VGG16, LayerNorm, ConvDiv, and ConvMax. Candidate implementations are evaluated by their execution performance, measured as inverse runtime ($1/\mathrm{ms}$), subject to correctness checks against the reference implementation. We use Gemini-3.1 Pro as the coding agent and compare Dream-RSI with Recursive Fixed Exploration under the same evaluation protocol and initialization.

Results.

Figure [4](#S4.F4) shows the discovery trajectories as the number of generations increases.
On VGG16 and LayerNorm, Dream-RSI reaches comparable final performance using
$2.43\times$ and $1.79\times$ fewer generations, respectively.
On ConvDiv and ConvMax, under comparable discovery budgets,
Dream-RSI achieves $2.09\times$ and $1.44\times$ higher performance, respectively.
These results show that adapting the exploration policy across recursive rounds can improve the efficiency and effectiveness of long-horizon discovery.

## Further Analysis

Analysis of Historical Inductive Biases in Long-Horizon Discovery
$0$$250$$500$$750$$1{,}000$$0.4$$0.8$$1.2$$1.6$$2$Number of GenerationsPerformance ($1/\mathrm{ms}$)Dream-RSIFixed ExplorationDream-RSI + GuidanceFixed + Guidance
Figure 5: 
Discovery performance on ConvDiv.
Using history as an interactive replay simulator outperforms using it only as guidance.

We further investigate how the nature of the historical inductive bias affects long-horizon discovery. A natural alternative for utilizing history is to abstract prior trajectories into high-level directional insights, which are directly injected into the prompt as explicit semantic guidance for subsequent rounds. To evaluate the efficacy of this prompt-level semantic guidance, we apply it to both Recursive Fixed Exploration and Dream-RSI. As illustrated in Figure [5](#S5.F5), explicit directional guidance consistently underperforms its unguided counterpart across both paradigms under equivalent discovery budgets. These results suggest that in long-horizon discovery—where multiple parallel threads are deployed for exploration—imposing strong semantic inductive biases regarding future search directions tends to over-constrain the search space and impede diverse exploration.

Analysis of Evolution of Exploration Behavior

E0E1E2E3E4E5E6E7E8$0.5$$1$$1.5$$2$0.4270.6250.8551.4031.4881.4991.7701.8801.898Performance (1/ms)
(a) Round-best performanceE0E1E2E3E4E5E6E7E8$0$$50$$100$11011087805092809186Recursive execution roundEvaluated attempts
(b) Exploration effort
Figure 6: 
Evolution of exploration behavior on ConvDiv.
(a) Round-best performance across recursive execution rounds.
(b) The number of evaluated attempts in each round.

Figure [6](#S5.F6) illustrates how the learned exploration policy evolves across recursive rounds on ConvDiv. As shown, the exploration policy exhibits a clear adaptive pattern: as performance improves, it initially conserves discovery compute (e.g., reducing the number of evaluated attempts from 110 to 50). When progress subsequently plateaus, it increases exploration effort again, coinciding with further performance gains..

## Related Work

AI-Driven Scientific and Algorithmic Discovery.

LLM-based discovery systems iteratively generate, evaluate, and refine candidate solutions using prior artifacts and feedback, as in AlphaEvolve ([Novikov et al., 2025](#bib.bib27)), OpenEvolve ([Sharma, 2025](#bib.bib34)), CodeEvolve ([Assumpção et al., 2025](#bib.bib2)), ShinkaEvolve ([Lange et al., 2026](#bib.bib21)), PACEvolve ([Yan et al., 2026b](#bib.bib44)), DeltaEvolve ([Jiang et al., 2026](#bib.bib19)) and MLEvolve [Du et al. (2026)](#bib.bib5). More recent work emphasizes the importance of exploration itself: SkyDiscover provides adaptive discovery infrastructure ([Liu et al., 2026b](#bib.bib24)), SwarmResearch dynamically orchestrates multiple search branches ([Virk et al., 2026](#bib.bib36)), and EvoX ([Liu et al., 2026a](#bib.bib23)) explicitly optimizes search strategies rather than only candidate solutions. This shift makes exploration a meta-level optimization problem, but useful supervision for exploration strategies is expensive and delayed because their quality often becomes apparent only after long discovery rollouts.

Self-Evolving Agents.

A broader line of work studies agents that improve their own components during interaction. Prior methods evolve model weights ([Huang et al., 2026c](#bib.bib17); [Huang et al., 2026a](#bib.bib15)), agent harnesses ([Lee et al., 2026](#bib.bib22); [Zhang et al., 2026b](#bib.bib48)), contexts ([Zhang et al., 2026d](#bib.bib50)), skills ([Zhang et al., 2026a](#bib.bib47); [Ouyang et al., 2026a](#bib.bib30); [Wu et al., 2026b](#bib.bib40)), model behavior through test-time learning ([Wang et al., 2025](#bib.bib37); [Yuksekgonul et al., 2026](#bib.bib46); [Yan et al., 2026a](#bib.bib43); [Wu et al., 2026a](#bib.bib39)), rubrics ([Xiong et al., 2026](#bib.bib41)), environments ([Huang et al., 2026b](#bib.bib16)) and other applications ([Dai et al., 2026](#bib.bib4)). Most operate at the object level, improving components used for task execution or reasoning. Recent work has begun to optimize meta-level mechanisms, including search strategies and self-improvement procedures ([Liu et al., 2026a](#bib.bib23); [Yan et al., 2026a](#bib.bib43); [Wang et al., 2026](#bib.bib38); [Zhang et al., 2026c](#bib.bib49); [Kim et al., 2026](#bib.bib20)). However, such meta-level strategies are difficult to improve because their quality is often revealed only after costly long-horizon rollouts. Dream-RSI makes this meta-level optimization recursive and off-policy by turning accumulated discovery history into replay simulators, allowing exploration controllers to be repeatedly evaluated, improved, and redeployed without rerunning the underlying discovery process.

Memory, History, and Experience Reuse.

Prior work reuses agent experience as search history, context, memory, reusable skills, or training signals. DeltaEvolve structures evolutionary history through semantic deltas ([Jiang et al., 2026](#bib.bib19)); SwarmResearch and MLEvolve use cross-branch or retrospective information to guide subsequent search ([Virk et al., 2026](#bib.bib36); [Du et al., 2026](#bib.bib5)); and other work improves how agents access and retain experience through evolving contexts, broader harness state, libraries, or skills ([Zhang et al., 2026d](#bib.bib50); [Lee et al., 2026](#bib.bib22); [Xu et al., 2026](#bib.bib42); [Ouyang et al., 2026a](#bib.bib30)). We take a different view: rather than using exploration history only as context or memory for the next decision, we organize it as a replay simulator in which many alternative exploration controllers can be evaluated cheaply. This turns previously collected discovery experience into reusable feedback for meta-level optimization, alleviating the scarcity and high cost of training signals for improving exploration strategies.

## Conclusion

We presented

Dream-RSI

, a framework for recursive self-improvement of exploration in recursive self improvement. By converting accumulated discovery history from static context into an active, replayable simulator,

Dream-RSI

addresses the core bottleneck of meta-optimization: delayed and expensive feedback, which is especially severe in long-horizon discovery settings. By ‘dreaming’ within replay simulators constructed from historical discovery trees, Dream-RSI evaluates candidate exploration policies rapidly and at negligible execution cost. The improved policies are then redeployed online to drive further discovery and expand the simulator pool, closing the recursive self-improvement loop. Across algorithm engineering, mathematical optimization, and GPU kernel engineering,

Dream-RSI

achieves competitive or improved discovery quality while substantially reducing discovery cost in several settings.

## References

- Anthropic. Learning more about claude’s mathematical capabilities. [https://www.anthropic.com/research/riemann-zeta](https://www.anthropic.com/research/riemann-zeta), Aug. 2026. Accessed: 2026-08-13.
- H. Assumpção, D. Ferreira, L. Campos, and F. Murai. Codeevolve: an open source evolutionary coding agent for algorithmic discovery and optimization. arXiv preprint arXiv:2510.14150, 2025.
- S. Cao, Z. Mao, J. E. Gonzalez, and I. Stoica. K-search: Llm kernel generation via co-evolving intrinsic world model. arXiv preprint arXiv:2602.19128, 2026.
- R. Dai, K. Huang, C. Kang, and C. Liao. It takes two to match: Co-evolving generative retriever with reinforcement learning. arXiv preprint arXiv:2609.00638, 2026.
- S. Du, X. Yan, J. Shi, Z. Cao, S. Feng, Z. Liang, B. Sun, T. Peng, Y. Zhou, X. Li, et al. Mlevolve: A self-evolving framework for automated machine learning algorithm discovery. arXiv preprint arXiv:2606.06473, 2026.
- J. H. Friedman, T. Hastie, and R. Tibshirani. Regularization paths for generalized linear models via coordinate descent. Journal of statistical software, 33:1–22, 2010.
- B. Georgiev, J. Gómez-Serrano, T. Tao, and A. Z. Wagner. Mathematical exploration and discovery at scale. arXiv preprint arXiv:2511.02864, 2025.
- S. Gupta, J. Davidson, S. Levine, R. Sukthankar, and J. Malik. Cognitive mapping and planning for visual navigation. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 2616–2625, 2017.
- D. Ha and J. Schmidhuber. World models. arXiv preprint arXiv:1803.10122, 2(3):440, 2018.
- D. Hafner, T. Lillicrap, J. Ba, and M. Norouzi. Dream to control: Learning behaviors by latent imagination. arXiv preprint arXiv:1912.01603, 2019.
- D. Hafner, T. Lillicrap, M. Norouzi, and J. Ba. Mastering atari with discrete world models. arXiv preprint arXiv:2010.02193, 2020.
- D. Hafner, J. Pasukonis, J. Ba, and T. Lillicrap. Mastering diverse domains through world models. arXiv preprint arXiv:2301.04104, 2023.
- D. Hafner, W. Yan, and T. Lillicrap. Training agents inside of scalable world models. arXiv preprint arXiv:2509.24527, 2025.
- Y. Hu, S. Liu, Y. Yue, G. Zhang, B. Liu, F. Zhu, J. Lin, H. Guo, S. Dou, Z. Xi, et al. Memory in the age of ai agents. arXiv preprint arXiv:2512.13564, 2025.
- C. Huang, H. Liu, T. Zheng, R. Dai, L. Huang, J. Li, Z. Li, Z. Wei, Y. Meng, and J. Huang. G-zero: Self-play for open-ended generation from zero data. arXiv preprint arXiv:2605.09959, 2026a.
- C. Huang, Z. Wang, R. Han, J. Yan, Y. Chen, Z. CuiZhu, K. Jiang, P. Xia, H. Yu, Y. Zhuang, et al. Envharness: Awakening static worlds for agent learning. arXiv preprint arXiv:2608.19880, 2026b.
- C. Huang, W. Yu, X. Wang, H. Zhang, Z. Li, R. Li, J. Huang, H. Mi, and D. Yu. R-zero: Self-evolving reasoning llm from zero data. In International Conference on Learning Representations, volume 2026, pages 130770–130790, 2026c.
- J. Jaber and O. Jaber. Autokernel: Autonomous gpu kernel optimization via iterative agent-driven search. arXiv preprint arXiv:2603.21331, 2026.
- J. Jiang, T. Ding, and Z. Zhu. Deltaevolve: Accelerating scientific discovery through momentum-driven evolution. arXiv preprint arXiv:2602.02919, 2026.
- Z. M. Kim, Y.-J. Lee, S. Jwa, and D. Kang. Metan: Recursive self-improvement through emergent depth. arXiv preprint arXiv:2608.24735, 2026.
- R. Lange, Y. Imajuku, and E. Cetin. Shinkaevolve: Towards open-ended and sample-efficient program evolution. In International Conference on Learning Representations, volume 2026, pages 74026–74078, 2026.
- Y. Lee, R. Nair, Q. Zhang, K. Lee, O. Khattab, and C. Finn. Meta-harness: End-to-end optimization of model harnesses. arXiv preprint arXiv:2603.28052, 2026.
- S. Liu, S. Agarwal, M. Maheswaran, M. Cemri, Z. Li, Q. Mang, A. Naren, E. Boneh, A. Cheng, M. Z. Pan, et al. Evox: Meta-evolution for automated discovery. arXiv preprint arXiv:2602.23413, 2026a.
- S. Liu, M. Cemri, S. Agarwal, A. Krentsel, A. Naren, Q. Mang, Z. Li, A. Gupta, M. Maheswaran, A. Cheng, M. Pan, E. Boneh, K. Ramchandran, K. Sen, M. Zaharia, A. G. Dimakis, and I. Stoica. Skydiscover: A flexible, adaptive framework for ai-driven scientific and algorithmic discovery. In Proceedings of the ACM Conference on AI and Agentic Systems, CAIS ’26, pages 1223–1227. Association for Computing Machinery, 2026b. [10.1145/3786335.3813221](https://doi.org/10.1145/3786335.3813221). URL [https://doi.org/10.1145/3786335.3813221](https://doi.org/10.1145/3786335.3813221).
- S. Liu, Z. Lin, Y. Zhang, Y. Ren, Y. Wu, Y. Li, Z. Wang, Z. Fu, and J. Ye. The path to recursive self-improving agents: Foundation, framework, and future directions. Preprints, August 2026c. [10.20944/preprints202608.0051.v1](https://doi.org/10.20944/preprints202608.0051.v1). URL [https://doi.org/10.20944/preprints202608.0051.v1](https://doi.org/10.20944/preprints202608.0051.v1).
- T. M. Moerland, J. Broekens, A. Plaat, and C. M. Jonker. Model-based reinforcement learning: A survey. Foundations and Trends in Machine Learning, 16(1):1–118, 2023.
- A. Novikov, N. Vũ, M. Eisenberger, E. Dupont, P.-S. Huang, A. Z. Wagner, S. Shirobokov, B. Kozlovskii, F. J. Ruiz, A. Mehrabian, et al. Alphaevolve: A coding agent for scientific and algorithmic discovery. arXiv preprint arXiv:2506.13131, 2025.
- OpenAI. On the navier–stokes millennium prize problem. [https://openai.com/index/navier-stokes-solution/](https://openai.com/index/navier-stokes-solution/), Sept. 2026. Accessed: 2026-09-10.
- A. Ouyang, S. Guo, S. Arora, A. L. Zhang, W. Hu, C. Ré, and A. Mirhoseini. Kernelbench: Can llms write efficient gpu kernels? arXiv preprint arXiv:2502.10517, 2025.
- S. Ouyang, J. Yan, Y. Chen, R. Han, Z. Wang, B. D. Mishra, R. Meng, C.-L. Li, Y. Jiao, K. Zha, et al. Skillos: Learning skill curation for self-evolving agents. arXiv preprint arXiv:2605.06614, 2026a.
- S. Ouyang, J. Yan, I. Hsu, Y. Chen, K. Jiang, Z. Wang, R. Han, L. Le, S. Daruki, X. Tang, et al. Reasoningbank: Scaling agent self-evolving with reasoning memory. In International Conference on Learning Representations, volume 2026, pages 94327–94354, 2026b.
- F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, et al. Scikit-learn: Machine learning in python. the Journal of machine Learning research, 12:2825–2830, 2011.
- B. Romera-Paredes, M. Barekatain, A. Novikov, M. Balog, M. P. Kumar, E. Dupont, F. J. Ruiz, J. S. Ellenberg, P. Wang, O. Fawzi, et al. Mathematical discoveries from program search with large language models. Nature, 625(7995):468–475, 2024.
- A. Sharma. Openevolve: an open-source evolutionary coding agent, 2025. URL [https://github.com/algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve).
- R. S. Sutton. Integrated architectures for learning, planning, and reacting based on approximating dynamic programming. In B. Porter and R. Mooney, editors, Machine Learning Proceedings 1990, pages 216–224. Morgan Kaufmann, San Francisco (CA), 1990. ISBN 978-1-55860-141-3. [https://doi.org/10.1016/B978-1-55860-141-3.50030-4](https://doi.org/https://doi.org/10.1016/B978-1-55860-141-3.50030-4). URL [https://www.sciencedirect.com/science/article/pii/B9781558601413500304](https://www.sciencedirect.com/science/article/pii/B9781558601413500304).
- Y. Virk, Z. Edds, C. S. Xia, and L. Zhang. Swarmresearch: Orchestrating coding agents for open-ended discovery. arXiv preprint arXiv:2607.02807, 2026.
- Y. Wang, S.-R. Su, Z. Zeng, E. Xu, L. Ren, X. Yang, Z. Huang, X. He, L. Ma, B. Peng, et al. Thetaevolve: Test-time learning on open problems. arXiv preprint arXiv:2511.23473, 2025.
- Z. Wang, M. Yan, J. Bi, S. Yan, V. Tresp, and Y. Ma. Metaskill-evolve: Recursive self-improvement of llm agents via two-timescale meta-skill evolution. arXiv preprint arXiv:2607.05297, 2026.
- S. Wu, C. Qian, X. Chen, and H. Ji. Teaching llms to self-evolve: Cultivating core meta-skills with reinforcement learning. arXiv preprint arXiv:2607.21971, 2026a.
- X. Wu, Y. Zhuan, R. Wei, H. Chen, D. Bai, J. Liu, X. Wang, X. Wang, L. Wang, and X. Cheng. Agenticrectune: Multi-agent with self-evolving skillhub for recommendation system optimization. arXiv preprint arXiv:2604.26969, 2026b.
- T. Xiong, Z. Yang, X. Wang, C.-C. Lin, R. Ma, K. Lin, Z. Wang, L. Li, C. Liu, R. Chen, et al. Rubrics as visual-repair context for self-evolving ui-to-code generation. arXiv preprint arXiv:2608.24138, 2026.
- W. Xu, A. Sordoni, C. Singh, Z. Gero, M. Galley, X. Yuan, and J. Gao. Test-time learning with an evolving library. arXiv preprint arXiv:2605.14477, 2026.
- M. Yan, B. Peng, B. Coleman, Z. Chen, Z. Xie, S. Chen, Z. He, N. Sachdeva, W. Wang, E. H. Chi, et al. Pacevolve++: Improving test-time learning for evolutionary search agents. arXiv preprint arXiv:2605.07039, 2026a.
- M. Yan, B. Peng, B. Coleman, Z. Chen, Z. Xie, S. Chen, Z. He, N. Sachdeva, I. Ye, W. Wang, et al. Pacevolve: Enabling long-horizon progress-aware consistent evolution. arXiv preprint arXiv:2601.10657, 2026b.
- H. Ye, H. Lin, J. Tang, Y. Luo, C. Yang, C. Su, R. Thapa, R. Yang, R. Liu, Z. Li, et al. Evaluation-driven scaling for scientific discovery. arXiv preprint arXiv:2604.19341, 2026.
- M. Yuksekgonul, D. Koceja, X. Li, F. Bianchi, J. McCaleb, X. Wang, J. Kautz, Y. Choi, J. Zou, C. Guestrin, et al. Learning to discover at test time. arXiv preprint arXiv:2601.16175, 2026.
- H. Zhang, S. Fan, H. P. Zou, Y. Chen, Z. Wang, J. Zhou, C. Li, W.-C. Huang, Y. Yao, K. Zheng, et al. Coevoskills: Self-evolving agent skills via co-evolutionary verification. arXiv preprint arXiv:2604.01687, 2026a.
- J. Zhang, S. Hu, C. Lu, R. Lange, and J. Clune. Darwin gödel machine: open-ended evolution of self-improving agents. In International Conference on Learning Representations, volume 2026, pages 104223–104294, 2026b.
- J. Zhang, B. Zhao, W. Yang, J. Foerster, J. Clune, M. Jiang, S. Devlin, and T. Shavrina. Hyperagents. arXiv preprint arXiv:2603.19461, 2026c.
- Q. Zhang, C. Hu, S. Upasani, B. Ma, F. Hong, V. Kamanuru, J. Rainton, C. Wu, M. Ji, H. Li, et al. Agentic context engineering: Evolving contexts for self-improving language models. In International Conference on Learning Representations, volume 2026, pages 86069–86100, 2026d.
- T. Zheng, H. Liu, C. Huang, H. Bao, S. Zhang, R. Liu, R. Dai, R. Chen, C. Liu, T. Xiong, et al. Llms improving llms: Agentic discovery for test-time scaling. arXiv preprint arXiv:2605.08083, 2026a.
- T. Zheng, H. Zhang, W. Yu, X. Wang, H. Xing, R. Dai, R. Liu, H. Bao, C. Huang, H. Huang, et al. Parallel-r1: Towards parallel thinking via reinforcement learning. In International Conference on Learning Representations, volume 2026, pages 121144–121166, 2026b.

---

Original source: [https://arxiv.org/html/2609.14858v1](https://arxiv.org/html/2609.14858v1)
