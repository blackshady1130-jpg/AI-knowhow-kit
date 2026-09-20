# Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers

Source URL: https://arxiv.org/html/2609.02702

Xu Zou
Affiliation: Z.ai
  
Jie Tang
Affiliation: Tsinghua University

September 2, 2026

###### Abstract

Transformers process information causally, but long-context
reasoning may depend on task state discovered only later. We formalize this
mismatch through conditional state update tasks. For causal state update processors, providing the condition first can require
exponentially less memory in the worst case than providing it last.

Motivated by this principle, we introduce trace as state. We use collected reasoning traces as a textual proxy for task
state and place it before the long-context block on a fresh pass, allowing
information derived previously to guide rereading.

We conduct extensive experiments on trace as state and trace append, a matched control that uses the same task state proxy but put it after the context.
Across three models and three long-context datasets, trace as state outperforms
trace append in 26 of 27 reported combinations of model, task, and metric. On
GraphWalks Parents, exact match lifts DeepSeek V4 Pro(Preview) from 29.2% on the initial pass and 43.0%
with trace append to 81.8% with trace as state, and from 66.4% and
83.2% to 100.0% for GLM-5.2. These results show that placing traces before the context can improve long-context reasoning while retaining the
causal transformer structure.

## 1 Introduction

Frontier language models can now accept inputs extending to hundreds of
thousands or even millions of tokens. Advances in sparse, compressed, and
hybrid sequence modeling architectures have substantially enlarged their
nominal context windows
[DeepSeek-AI (2025b)](#bib.bib25); [DeepSeek-AI (2026a)](#bib.bib24); [Qwen Team (2025b)](#bib.bib27); [Yang et al. (2025)](#bib.bib6).

Despite these architectural advances, autoregressive Transformers retain
causal attention. Information appearing later remains available to subsequent
reasoning and answer generation, but it cannot affect the representations
formed at earlier positions within the same pass.

One structural difficulty is a mismatch between input order and reasoning
order. Prior work shows that reasoning performance can depend not only on
where supporting information appears, but also on the relative order in which
it is presented [Chen et al. (2024)](#bib.bib18); [Yu et al. (2025)](#bib.bib20). In many long context
tasks, a solver must maintain task-relevant state, such as an active target, a
search frontier, or a set of rejected hypotheses. Some of this state may
become available only after earlier parts of the context have already been
processed.

We analyze this asymmetry through conditional state update tasks. Such a task
begins from a state specified by a condition and applies an information
sequence to it. If the condition is
available before the sequence, a causal processor can update the realized
state as each item arrives. If the condition arrives after the sequence,
the processor may instead need to retain how the sequence would act on every
possible condition. We show that these two input orders can have exponentially
different memory requirements in the worst case. The separation
motivates an ordering principle for causal transformer passes: task-relevant
state discovered late in one pass can be made available before the context in
the next pass.
Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers")A and  [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers")B illustrate the
causal processor and the two input orders.

Modern reasoning models provide an
observable interface through the reasoning traces they generate before
producing visible answers
[DeepSeek-AI (2025a)](#bib.bib11); [Qwen Team (2025a)](#bib.bib26); [Lee et al. (2025)](#bib.bib14).
Generated reasoning text can carry intermediate computational information
across steps
[Nye et al. (2021)](#bib.bib8); [Wei et al. (2022)](#bib.bib9); [Merrill and Sabharwal (2024)](#bib.bib5); [Levy et al. (2025)](#bib.bib12).
Reasoning traces may be incomplete or contain errors, and we treat them as an
observable textual proxy for task state, as shown in
figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers")C. We therefore introduce trace as state, a
general inference scaling method that follows a read, compute, feedback, and
reread procedure. The model first processes the task and generates one or more
reasoning traces. We serialize the collected traces as $T$ and place it before
the long-context block in a fresh pass.

We compare trace as state with trace append, a placement control that gives the second
pass serialized trace text after the long context.
Under trace as state, the trace is available while the context is processed again.
Under trace append, the trace can still guide later reasoning and answer
generation, but it cannot influence the representations already formed for
the preceding context. Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers")D
summarizes the strict placement design.

Figure 1: Overview for trace as state
(A) A causal processor carries one running state.
(B) In a worst-case conditional state update task, condition-first
processing tracks only the realized state, whereas condition-last processing
can require exponentially more working memory.
(C) Reasoning trace $T$ provides a textual proxy for task state.
(D) trace as state places $T$ before the context in a fresh causal pass.

We evaluate this placement intervention on GraphWalks 256K, MRCRv2 8-needle,
and NUB-1M using three frontier models from different providers: DeepSeek V4
Pro Preview, GLM-5.2, and Qwen 3.7 Max.
Across the 27 reported combinations of model, task, and metric, trace as state
outperforms trace append in 26. The result shows that the benefit of using reasoning traces as a task state proxy and placing it before the context is general in long context reasoning, and is consistent with our conditional state update task memory analysis.

We further test alternative explanations through ablations on GraphWalks 256K
using DeepSeek V4 Pro Preview. These controls weaken explanations based solely on
generic trace scaffolding or access to first-pass answers and further support
the trace as state interpretation.

Our contributions are as follows:

* •

  We use a conditional state update abstraction to characterize a
  worst-case exponential order separation for deterministic processors that
  read the input once,
  and apply it as a qualitative principle for causal
  processing of long contexts.
* •

  We introduce trace as state, a general inference scaling method for reasoning
  over long contexts that feeds reasoning traces back as textual state
  proxies. The method adds feedback between passes while retaining causal
  processing within each pass.
* •

  Across three models and three benchmarks for reasoning over long
  contexts, trace as state scores above trace append in 26 of 27 reported combinations
  of model, task, and metric.

## 2 Related Work

#### Long-context architectures and effective use.

Sparse, compressed, and hybrid sequence models have extended the nominal
context windows of language models
[DeepSeek-AI (2025b)](#bib.bib25); [DeepSeek-AI (2026a)](#bib.bib24); [Qwen Team (2025b)](#bib.bib27); [Yang et al. (2025)](#bib.bib6).
Long-context evaluations nevertheless show continued sensitivity to evidence
position, distractors, and the operations required to combine information
across an input [Liu et al. (2024)](#bib.bib16); [Kuratov et al. (2024)](#bib.bib1); [Hsieh et al. (2024)](#bib.bib22).

#### Causal order in reasoning.

Under causal attention, a representation at one position can use only
information from that position and its prefix.
Ok and Lee attribute a large multi-choice prompt-order gap to this
constraint and show that repeating the options after the context partially
closes the gap [Ok and Lee (2026)](#bib.bib17).
CoRe reduces sensitivity to the order of supporting documents by repeating the
full context, whereas *Racing Thoughts* traces contextualization errors to
layerwise race conditions [Yu et al. (2025)](#bib.bib20); [Lepori et al. (2025)](#bib.bib23).
Collectively, these studies show that input order, repetition, and
contextualization can affect model behavior.

#### Architectural recurrence.

Iterative language models can revisit hidden representations or partially
specified text.
Geiping et al. train a language model with recurrent depth that repeatedly
applies a shared block at test time [Geiping et al. (2025)](#bib.bib3).
Saunshi et al. study Transformer blocks with shared weights, and
*LoopFormer* trains variable loop trajectories for different inference
budgets [Saunshi et al. (2025)](#bib.bib2); [Jeddi et al. (2026)](#bib.bib4).
Masked text-diffusion models such as LLaDA reconstruct masked positions over
multiple steps using visible context on both sides
[Sahoo et al. (2024)](#bib.bib35); [Nie et al. (2025)](#bib.bib36).
These approaches expand the design space for iterative computation. However, they can require substantial changes to existing training and inference infrastructure.

#### Rereading and textual feedback.

Several methods revisit task information or carry textual state forward during
inference.
Re2 repeats the question within one prompt and provides a direct rereading
baseline without prior reasoning text [Xu et al. (2024)](#bib.bib19).
The Markovian Thinker carries a bounded text history across reset reasoning
chunks, while ReContext recursively builds and replays an evidence pool for the
current query [Aghajohari et al. (2026)](#bib.bib15); [Zhao et al. (2026)](#bib.bib21).
These methods show that feeding task-relevant text back to a model can improve
reasoning.

#### Reasoning traces as state.

Reasoning traces can serve not only as explanations, but also as textual
records of an evolving computational state.
Hao et al. show that synthetic hints inserted into a reasoning trace can affect
later outputs even when follow-up explanations do not acknowledge their
influence [Hao et al. (2026)](#bib.bib13).
The *State over Tokens* preprint describes the growing reasoning prefix as
externalized computational state, whereas causal mediation evidence suggests
that models do not reliably use their stated intermediate steps
[Levy et al. (2025)](#bib.bib12); [Paul et al. (2024)](#bib.bib10).
Taken together, the evidence shows that reasoning traces can carry
task-relevant information and affect later outputs.

## 3 Methodology

Textual reasoning typically follows a causal order, which is well matched
by causal transformers. Yet some reasoning depends on task states whose
values become known only later, creating a mismatch especially
consequential in long contexts. We formalize this mismatch using causal state
update systems and conditional state update tasks and introduce trace as state.

Table 1: Vital Notations.

| Symbol | Meaning |
| --- | --- |
| $c_{i},C$ | The $i$th information unit and the ordered sequence $C=(c_{1},\ldots,c_{n})$. |
| $s_{i},\mathcal{S},b$ | The task state after $c_{i}$, its finite state space, and the log size of the state space |
| $U$ | The causal state update rule. |
| $z$ | The condition used as the initial task state $s_{0}$. |
| $x,\mathcal{M}$ | The long context and the causal reasoning model. |
| $r_{j},a_{j},n_{\mathrm{tr}}$ | The reasoning trace, visible answer, and number of source model runs. |
| $\pi,T$ | The trace serializer and the resulting serialized trace. |

Table [1](#S3.T1 "Table 1 ‣ 3 Methodology ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers")
summarizes the vital notation used in this section.

### 3.1 Causal State Updates and Order-Dependent Memory

#### Causal state updates.

We define a causal state update processor as a processor that reads each input
unit once in its presented order and updates its persistent working memory using
only its current memory and the newly received unit.

Let $C=(c_{1},\ldots,c_{n})$ be an ordered sequence of $n$ information units, with
$c_{i}$ denoting the $i$th unit. As shown in
Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers")A, a
causal state update processor carries a task state $s_{i}$ in a finite state
space $\mathcal{S}$. After reading $c_{i}$, it applies a fixed update rule $U$:

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ s_{i}=U(s_{i-1},c_{i}),\qquad i=1,\ldots,n. $$ |  | (1) |

The state $s_{i}$ is the task state the processor reached after processing
$c_{1},\ldots,c_{i}$. When the initial state $s_{0}$ is fixed, the processor follows
one realized state path through the sequence.

#### Conditional state update tasks and order-dependent memory.

Consider a variant of the causal state update process in which the initial state is supplied by a task condition rather than
being fixed. Let $z\in\mathcal{S}$ denote this condition. We call the resulting
problem a conditional state update task: the processor sets $s_{0}=z$, applies
Equation [1](#S3.E1 "In Causal state updates. ‣ 3.1 Causal State Updates and Order-Dependent Memory ‣ 3 Methodology ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") to $C$, and returns $s_{n}$.

Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers")B compares two orders for the same condition and information sequence.
In the condition first order $[z,C]$, the processor receives $z$ before
$c_{1},\ldots,c_{n}$($n$ is the length of the information sequence) and therefore knows which state path to update. In the
condition last order $[C,z]$, it reads the complete sequence before learning
which initial state should be propagated through it.

To compare their working memory, consider a causal state update processor that knows exactly the state update rule $U$. With $[z,C]$, the processor only needs to
store the current $s_{i}$, so
$\lceil b\rceil$ bits suffice, where $b=\log_{2}|\mathcal{S}|$.

With $[C,z]$, the processor has not selected a state path when it finishes
reading $C$. Each possible sequence determines a complete response profile:
for every $z\in\mathcal{S}$, the profile specifies the resulting $s_{n}$. The processor must retain a different configuration for
every distinct response profile induced by the valid sequences.

There are $|\mathcal{S}|^{|\mathcal{S}|}$ possible functions from
$\mathcal{S}$ to itself. In the
worst case, $[C,z]$ requires at least

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \left\lceil\log_{2}|\mathcal{S}|^{|\mathcal{S}|}\right\rceil=\left\lceil|\mathcal{S}|\log_{2}|\mathcal{S}|\right\rceil=\lceil b2^{b}\rceil $$ |  | (2) |

bits, whereas $[z,C]$ requires only
$\lceil b\rceil$ bits. In the worst-case scenario, the memory requirement is exponentially larger in the condition last setting than in the condition first setting.

We could derive an ordering principle: a task condition could be much easier
to use when it is available before the information whose processing it guides.

### 3.2 Reasoning Traces as a Textual State Proxy

Although transformers may retain per-token kv caches, causal transformers with finite context length and finite precision are causal state update models as the their max memory are bounded.
Conditional state update tasks are not literal models of real world long context tasks. Instead, the results in section [3.1](#S3.SS1 "3.1 Causal State Updates and Order-Dependent Memory ‣ 3 Methodology ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") motivate us to test placing task relevant state before the context on a later pass.

The formal condition $z$ represents task state that is already available to
the processor. In a long context reasoning problem, however, useful task state may
be discovered only while the model is reasoning after reading the context. A
reasoning trace may record useful task states like an active target, a resolved reference or a search
frontier.

We view reasoning traces as an observable textual proxy for task state, as illustrated in figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers")C. The
proxy may be incomplete, lossy, or incorrect. We therefore do not identify a
trace with the formal condition $z$ or with a privileged internal model state.
The connection is functional: if the trace contains useful state information,
placing it before the context can make that information available while the
context is processed again.

Let $\mathcal{M}$ be a causal state update model and let $x$ denote
the long context. We run $\mathcal{M}$ $n_{\mathrm{tr}}$ times on the same problem.
Each run $j$ produces a reasoning trace $r_{j}$ and a separate visible answer
$a_{j}$:

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ (r_{j},a_{j})\sim\mathcal{M}(\cdot\mid x),\qquad j=1,\ldots,n_{\mathrm{tr}}. $$ |  | (3) |

For each task, a serializer $\pi$ held fixed across the placement
conditions constructs the serialized trace

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ T=\pi(r_{1},\ldots,r_{n_{\mathrm{tr}}}). $$ |  | (4) |

The serializer preserves the included reasoning text in source order and adds
fixed labels and delimiters. We use $T$ as the textual state proxy to be tested.

### 3.3 Trace as state.

Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers")D shows the complete
procedure. Based on theoretical analysis from section [3.1](#S3.SS1 "3.1 Causal State Updates and Order-Dependent Memory ‣ 3 Methodology ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"), we introduce trace as state, a method that places the textual state proxy $T$ before the long context $x$.
Therefore, in trace as state, a fresh causal pass receives $[T,x]$ to generate the answer again. We compare trace as state with trace append, the method that maintains the original order of $x$ and $T$ and sends the model $[x,T]$ on a second pass.

Let $r^{\prime}$ and $a^{\prime}$ denote the reasoning trace and visible answer produced in this
pass:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | $\displaystyle(r^{\prime}_{\mathrm{Tap}},a^{\prime}_{\mathrm{Tap}})$ | $\displaystyle\sim\mathcal{M}(\cdot\mid[x,T]),$ |  | (5) |
|  | $\displaystyle(r^{\prime}_{\mathrm{Tas}},a^{\prime}_{\mathrm{Tas}})$ | $\displaystyle\sim\mathcal{M}(\cdot\mid[T,x]).$ |  |

trace as state and trace append use the same long context $x$ and the same textual task state proxy $T$, with order as the only difference.
With trace as state, $T$ is available while the model processes $x$ again. With
trace append, $T$ arrives after $x$ and cannot change representations already
formed for the preceding context tokens, although it can still influence
subsequent reasoning and the visible answer. The
comparison therefore tests whether the same $T$ is more useful
during rereading than after the long context has already been processed.

## 4 Experiments

### 4.1 Setup

In this section, we evaluate
trace as state and its matched placement control trace append on long context tasks from
different domains. The models come from different providers and have different disclosed
architectural designs. A fixed serializer preserves the reasoning traces while
adding only necessary delimiters such as
"<trace_start>" and "<trace_end>" and brief introductory text to construct
$T$. Some traces are so long that we truncate them to the first 50,000
characters to keep the second-pass prompt within the model’s context capacity.
These choices define the realization evaluated here; the general trace as state
framework also permits adapted models, serializers, or state interfaces while
retaining causal processing within each pass.

#### Models.

We evaluate Qwen 3.7 Max, DeepSeek V4 Pro Preview, and GLM-5.2. All three are
frontier long-context reasoning models that expose reasoning traces that can be
logged and supplied back to the model as an imperfect textual proxy that may
carry task-state information. They also represent
different providers and disclosed long-context designs: DeepSeek V4 Pro Preview uses a hybrid attention
stack with Compressed Sparse Attention(CSA), Heavily Compressed Attention(HCA), and
Manifold-Constrained Hyper-Connections(mHC) [DeepSeek-AI (2026a)](#bib.bib24);
Qwen 3.7 Max is formed with Gated Deltanet(GDN) and Gated Attention(GA) [Yang et al. (2025)](#bib.bib6); [Qiu et al. (2025)](#bib.bib7); and GLM-5.2 is a 1M-token
MoE model with DeepSeek Sparse Attention (DSA) optimized by IndexCache (IC),
which reuses sparse-attention indices across layers
[DeepSeek-AI (2025b)](#bib.bib25); [Bai et al. (2026)](#bib.bib29); [GLM-5 Team (2026)](#bib.bib28); [Z.ai (2026a)](#bib.bib30); [Z.ai (2026b)](#bib.bib31). We choose the
highest available reasoning effort in our experiments: max for
DeepSeek V4 Pro and GLM-5.2. For Qwen 3.7 Max, we use the official xhigh system prompt. All three support approximately one-million-token inputs in the evaluated
interfaces and expose the reasoning traces required by the frozen textual
realization evaluated here
[Alibaba Cloud (2026)](#bib.bib39); [DeepSeek-AI (2026b)](#bib.bib38); [Z.ai (2026b)](#bib.bib31).

Details of the models are described in Table [1-1](#S4.T2 "Table 1-1 ‣ Datasets. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").

#### Datasets.

We use GraphWalks [OpenAI (2025a)](#bib.bib32), MRCRv2 8-needle
[OpenAI (2025b)](#bib.bib33); [Vodrahalli et al. (2024)](#bib.bib37), and 1M-Novel Understanding
Bench (NUB-1M) [xz-keg (2026)](#bib.bib34) for our
evaluation.
GraphWalks requires the model to maintain graph state over a long edge list;
MRCRv2 asks the model to bind a final request to the correct earlier
request-response instance. Both provide multiple prompt-length bins. As
different models use different tokenizers, many problems in the 1M bin cannot be fairly tested
due to overlength. We therefore choose the longest bins under 1M: The 256K bin for GraphWalks and the 256K
and 512K bins for MRCRv2. This choice also leaves
room for additional trace as state and trace append texts.

NUB-1M is a long novel reading comprehension benchmark with complex questions about a new novel containing 400–700K tokens. The dataset is updated by season to reduce leakage
risk. For each season, the problems and answers are manually maintained.
We use the season 2 novel for evaluation and report average
accuracy of the 20 problems over 5 repeats.

Models may not behave as intended unless the question appears at the end of the prompt.
We therefore separate the question from the long context and place it at the end of every input to ensure models behave well focused on the given tasks. The literal orders are therefore
trace as state $[T,x,q]$ and trace append $[x,T,q]$, where $x$ is the long context and
$q$ is the question.

Details of the datasets are listed in Table [1-2](#S4.T3 "Table 1-2 ‣ Datasets. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").

For each model and task, we compare a single-pass baseline $\mathcal{M}([x,q])$ with two trace-backed
conditions trace as state, $\mathcal{M}([T,x,q])$ and trace append $\mathcal{M}([x,T,q])$ that reuse the model’s own first-pass reasoning traces.
Appendix [C](#A3 "Appendix C Prompt and State Templates ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") gives
the trace serialization and dataset-specific insertion boundaries.

Table 1-1: Model configuration and token budgets used in the experiments.

| Model | Qwen 3.7 Max | DeepSeek V4 Pro Preview | GLM-5.2 |
| --- | --- | --- | --- |
| Arch.a | GDN+GA | CSA+HCA + mHC | DSA+IC |
| Input Budget | 983,616 | 1,048,576 | 1,048,576 |
| Output Budget | 65,536 | 131,072 | 65,536 |
| Reasoning | xhighb | max | max |

* a

  Architecture.
* b

  Via xhigh prompt.

Table 1-2: Datasets and scoring used in the experiments.

| Task | GraphWalks | MRCRv2 | NUB-1M |
| --- | --- | --- | --- |
| Subsets | 256K | 256K,512K 8-needle | Season 2 |
| Problems | 200 | 200 | 20 |
| Repeats | 5 | 5 | 5 |
| Scoring | EMa, set F1 | EM, Seq.b | Acc.c |

* a

  Exact Match.
* b

  SequenceMatcher ratio.
* c

  Accuracy.

We evaluate each problem with 5 repeats and include all 5 reasoning traces in
the second-pass trace as state and trace append prompts. We use the official provider for these models,
Aliyun Bailian for Qwen 3.7 Max [Alibaba Cloud (2026)](#bib.bib39),
DeepSeek for DeepSeek V4 Pro [DeepSeek-AI (2026b)](#bib.bib38), and
Bigmodel for GLM-5.2 [Z.ai (2026b)](#bib.bib31).
We do not explicitly pass a custom maximum-output value. The run records
therefore establish that no client-side cap was requested, but not the
effective provider default, which may also change over time.

Our evaluations use EM and set F1 for GraphWalks, EM and SequenceMatcher ratio
for MRCRv2 8-needle, and DeepSeek V4 Pro model-judged accuracy for NUB-1M.
Blocked, overlong, malformed, missing, nonterminal, or content-filtered cases
are scored as failures.

Some first pass reasoning traces are very long, we therefore truncate each reused trace to its first 50,000
characters to avoid input overlength.

### 4.2 Main Results

Table 2: Long-context results for first pass, trace as state and trace append. Scores
are percentages averaged over 5 repeats; higher is better. The best score
within each model-metric column is bolded.

| Model | Condition | GraphWalks 256K | | | | MRCRv2 8-needle | | | | NUB-1M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BFS | | Parents | | 256K | | 512K | | Season 2 |
| EM | F1 | EM | F1 | EM | Seq. | EM | Seq. | Acc. |
| DeepSeek V4 Pro Preview | First Pass | 31.6 | 36.4 | 29.2 | 46.5 | 53.8 | 78.5 | 45.4 | 63.6 | 60.0 |
| trace append | 41.8 | 48.3 | 43.0 | 65.3 | 66.6 | 79.6 | 49.4 | 66.9 | 71.0 |
| trace as state | 58.8 | 65.9 | 81.8 | 91.3 | 76.8 | 88.7 | 52.6 | 73.3 | 73.0 |
| Qwen 3.7 Max | First Pass | 60.0 | 68.1 | 60.8 | 87.2 | 79.8 | 83.1 | 36.2 | 43.7 | 37.0 |
| trace append | 60.4 | 70.4 | 71.0 | 91.7 | 84.0 | 87.1 | 40.4 | 47.4 | 49.0 |
| trace as state | 63.8 | 71.7 | 96.4 | 99.1 | 88.4 | 91.3 | 46.8 | 52.5 | 51.0 |
| GLM-5.2 | First Pass | 55.8 | 70.7 | 66.4 | 88.5 | 40.2 | 48.2 | 42.6 | 52.0 | 43.0 |
| trace append | 60.0 | 75.8 | 83.2 | 92.7 | 40.0 | 58.3 | 44.6 | 59.9 | 65.0 |
| trace as state | 63.4 | 75.0 | 100.0 | 100.0 | 61.2 | 71.9 | 55.4 | 70.1 | 66.0 |

Table [2](#S4.T2a "Table 2 ‣ 4.2 Main Results ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") displays the main experimental results.
Across all 27 reported combinations of model, task, and metric, trace as state scores
higher than trace append in 26. DeepSeek V4 Pro and Qwen 3.7 Max favor trace as state on every reported dataset, task and
metric. GLM-5.2 follows the same pattern except on GraphWalks BFS F1, where
trace append is 0.8 points higher while trace as state has higher exact match. trace as state
also scores above the first pass in all reported evaluations.

trace append improves over the first pass in many settings, showing that
the trace text can carry useful information in these settings. The additional
advantage of trace as state is consistent with the hypothesis that placing reasoning traces as an imperfect textual task state proxy
before the context is beneficial when the model processes the context again.

The strongest gains occur on GraphWalks Parents, where success
requires the model to maintain predecessor state while interpreting the graph.
DeepSeek V4 Pro improves from 46.5 to 91.3 F1, or 29.2 to 81.8 EM, and Qwen
3.7 Max improves from 87.2 to 99.1 F1, or 60.8 to 96.4 EM. GLM-5.2 reaches
100.0 EM and F1 on Parents under trace as state.
MRCRv2 retrieval and binding comparisons show the same ordering
advantage. NUB-1M runs provide supporting evidence in
the same direction for detailed long-novel reading comprehension.

### 4.3 Context Order Ablations

We next compare trace as state with controls that vary how different context are placed and first-pass outputs are
reused on DeepSeek V4 Pro GraphWalks 256K in table [3](#S4.T3a "Table 3 ‣ 4.3 Context Order Ablations ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
We test several ablations to examine how models behave under different trace
placements and feedback controls. For each ablation, the table labels the
prompt format and reports the exact match(EM) and F1 score.
We also include Majority@5 and Oracle@5 for the first pass in the table. Majority@5 evaluates the major choices of the 5 first pass answers,
while Oracle@5 evaluates the best answer among the 5 answers.

Table 3: DeepSeek V4 Pro Preview performance on GraphWalks 256K under
different prompt conditions. Scores are percentages averaged over 5 repeats.
The best scores for each subtask/metric are
bolded.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Condition | Prompt | BFS | | Parents | |
| Exact Match(%) | F1 Score(%) | Exact Match(%) | F1 Score(%) |
| First pass | $[x,q]$ | 31.6 | 36.4 | 29.2 | 46.5 |
| Majority@5 |  | 35.0 | 39.6 | 31.0 | 47.8 |
| Oracle@5 |  | 50.0 | 55.5 | 50.0 | 75.0 |
| Question First | $[q,x,q]$ | 33.4 | 36.8 | 53.0 | 64.6 |
| Re2 [Xu et al. (2024)](#bib.bib19) | $[x,q,x,q]$ | 49.0 | 52.9 | 50.0 | 68.9 |
| Answer Feedback | $[a,x,q]$ | 35.4 | 39.4 | 45.4 | 58.0 |
| Random Trace | $[T_{\mathrm{rand}},x,q]$ | 22.4 | 35.9 | 14.2 | 31.3 |
| Trace Only | $[T,q]$ | 46.2 | 52.7 | 43.8 | 67.3 |
| trace append | $[x,T,q]$ | 41.8 | 48.3 | 43.0 | 65.3 |
| trace as state | $[T,x,q]$ | 58.8 | 65.9 | 81.8 | 91.3 |

Question First puts the question $q$ before the task. It substantially improves performance on Parents but remains similar to the first pass baseline on BFS, implying that the question itself may be a vital task state for some tasks.

Re2 [Xu et al. (2024)](#bib.bib19) improves substantially over the first pass, showing that rereading is useful on these long context tasks. However, it remains below trace as state,
especially on Parents. In this evaluated setting, the comparison is consistent
with $T$ carrying task-relevant information beyond that supplied by prompt
repetition alone.

Answer Feedback places the first pass answers $a=[a_{1},\ldots,a_{n_{\mathrm{tr}}}]$ before
the original prompt. It improves over the first pass but remains far below
trace as state. This supports
the interpretation that serialized reasoning text can serve
as a more useful task state proxy than the answers or the questions alone.

Random Trace replaces the prefix with traces sampled from other problems in the
same GraphWalks subtask. It performs worse than the no-trace first pass, much worse than trace as state.
So the gain of trace as state is not due to a generic formatting effect, and a
reasoning-trace-like scaffold alone is insufficient without problem-specific,
task-relevant information from reasoning traces of the same problem.

All above controls above place a copy of the long context late in the prompt
but remain below trace as state, signifying that textual recency alone does not explain the observed trace as state gains.

Trace Only sends the first-pass reasoning traces without the original long
context prompt. Its performance is similar to
trace append, showing that the traces contain useful answer-relevant information.
Nevertheless, it remains well below trace as state, showing that the original input is still useful when placed
after the first pass traces.
Trace as State also outperforms Oracle@5, showing that the feedback pass improves on what can be obtained by retrospectively selecting the best of the five first pass outputs.

### 4.4 Trace Count Ablation

Finally, we rerun DeepSeek V4 Pro Preview on the GraphWalks 256K
while varying the number of reused first-pass traces from $n_{\mathrm{tr}}=1$ to
$n_{\mathrm{tr}}=5$. The block for each count contains the first $n_{\mathrm{tr}}$ eligible traces
in repeat order, so successive settings are nested. For every $n_{\mathrm{tr}}\geq 1$,
trace as state and trace append receive the same realized $T$, and each condition
averages five fresh second-pass repeats per problem. The $n_{\mathrm{tr}}=0$ point is the common
five-repeat first-pass mean.

Figure 2: Trace-count ablation on DeepSeek V4 Pro GraphWalks 256K. Panel A
reports BFS F1 and Panel B reports Parents F1. Shading shows 95% percentile
confidence intervals.

Figure [2](#S4.F2 "Figure 2 ‣ 4.4 Trace Count Ablation ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") shows that performance
generally rises as additional traces are included, and trace as state remains above
trace append for every $n_{\mathrm{tr}}\geq 1$.
Within this frozen-model realization, the result supports trace count as an
inference-scaling parameter and shows that the measured trace as state–trace append
ordering persists from $n_{\mathrm{tr}}=1$ through $n_{\mathrm{tr}}=5$.

## 5 Conclusion

We introduced trace as state, an inference approach that reuses task state information
carried in reasoning traces as a textual proxy on a fresh pass over a
long context task. Its motivation comes from theoretical analysis of
conditional state update tasks: for causal state update processors, a condition available before an information sequence can guide a
single evolving state, while a late condition can require retaining much more memory about potential conditions of the sequence.

trace as state applies this ordering principle by making prior reasoning available
before the long context block is processed again. Together, the formal analysis and
experiments support a simple view: reasoning traces can carry forward task
state information, and the point at which that information becomes available
can shape how useful it is.

This view suggests several direct extensions: selecting or compressing traces,
learning better textual state interfaces, and optimizing where feedback is
placed. A broader training framework could jointly learn the model and the feedback interface while retaining causal processing within each pass.

## Limitations

Our experiments realize cross-pass state feedback through model-generated
text. This evaluated realization requires access to raw reasoning traces or
another exposed state interface. The requirement comes from the interface used
in our experiments. The general cross-pass design can instead use any
accessible state interface. Models or APIs that expose only final answers may
therefore require a different interface.

trace as state uses one or more source runs followed by a fresh pass over the task.
These additional passes increase inference latency and token cost. Placing
state before the original context can also reduce key–value cache reuse in
multi-round settings.

Our evaluation covers three causal transformer models from different providers
and three long context task families: GraphWalks, MRCR, and NUB-1M. We do not
evaluate multi-round agent tasks. Testing additional models, domains, context
lengths, and interactive settings is needed to establish how broadly the
observed placement advantage generalizes.

Finally, because the method reuses only model generated traces, it does not introduce additional ethical concerns or misuse risks beyond those associated with the underlying models and tasks.

## References

* Aghajohari et al. (2026)
  M. Aghajohari, K. Chitsaz, A. Kazemnejad, S. Chandar, A. Sordoni, A. Courville, and S. Reddy
  The markovian thinker: architecture-agnostic linear scaling of reasoning.
  In The Fourteenth International Conference on Learning Representations,
  Note: Poster
  External Links: [Link](https://openreview.net/forum?id=3As6AQ9ELI)
  Cited by: [§2](#S2.SS0.SSS0.Px4.p1.1 "Rereading and textual feedback. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Alibaba Cloud (2026)
  Alibaba Cloud
  qwen3.7-max model information.
  Note: <https://help.aliyun.com/zh/model-studio/qwen3-7-max>Official Model Studio documentation. Accessed August 3, 2026
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Models. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§4.1](#S4.SS1.SSS0.Px2.p6.1 "Datasets. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Bai et al. (2026)
  Y. Bai, Q. Dong, T. Jiang, X. Lv, Z. Du, A. Zeng, J. Tang, and J. Li
  IndexCache: accelerating sparse attention via cross-layer index reuse.
  In Third Conference on Language Modeling,
  External Links: [Link](https://arxiv.org/abs/2603.12201)
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Models. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Chen et al. (2024)
  X. Chen, R. A. Chi, X. Wang, and D. Zhou
  Premise order matters in reasoning with large language models.
  In Proceedings of the 41st International Conference on Machine Learning,
  Proceedings of Machine Learning Research, Vol. 235, pp. 6596–6620.
  External Links: [Link](https://proceedings.mlr.press/v235/chen24i.html)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* DeepSeek-AI (2025a)
  DeepSeek-AI
  DeepSeek-R1: incentivizing reasoning capability in LLMs via reinforcement learning.
  Nature 645, pp. 633–638.
  External Links: [Document](https://dx.doi.org/10.1038/s41586-025-09422-z)
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* DeepSeek-AI (2025b)
  DeepSeek-AI
  DeepSeek-V3.2: pushing the frontier of open large language models.
  Technical report
  Technical Report arXiv:2512.02556, DeepSeek-AI.
  External Links: 2512.02556,
  [Document](https://dx.doi.org/10.48550/arXiv.2512.02556),
  [Link](https://arxiv.org/abs/2512.02556)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§2](#S2.SS0.SSS0.Px1.p1.1 "Long-context architectures and effective use. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Models. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* DeepSeek-AI (2026a)
  DeepSeek-AI
  DeepSeek-V4: towards highly efficient million-token context intelligence.
  Technical report
  Technical Report arXiv:2606.19348, DeepSeek-AI.
  External Links: 2606.19348,
  [Document](https://dx.doi.org/10.48550/arXiv.2606.19348),
  [Link](https://arxiv.org/abs/2606.19348)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§2](#S2.SS0.SSS0.Px1.p1.1 "Long-context architectures and effective use. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Models. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* DeepSeek-AI (2026b)
  DeepSeek-AI
  Models & pricing.
  Note: <https://api-docs.deepseek.com/quick_start/pricing/>Official API documentation. Accessed August 3, 2026
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Models. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§4.1](#S4.SS1.SSS0.Px2.p6.1 "Datasets. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Geiping et al. (2025)
  J. Geiping, S. M. McLeish, N. Jain, J. Kirchenbauer, S. Singh, B. R. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein
  Scaling up test-time compute with latent reasoning: a recurrent depth approach.
  In The Thirty-ninth Annual Conference on Neural Information Processing Systems,
  Cited by: [§2](#S2.SS0.SSS0.Px3.p1.1 "Architectural recurrence. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* GLM-5 Team (2026)
  GLM-5 Team
  GLM-5: from vibe coding to agentic engineering.
  Technical report
  Technical Report arXiv:2602.15763, Z.ai and Tsinghua University.
  External Links: 2602.15763,
  [Document](https://dx.doi.org/10.48550/arXiv.2602.15763),
  [Link](https://arxiv.org/abs/2602.15763)
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Models. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Hao et al. (2026)
  Y. Hao, L. Chen, A. Emami, and J. C. Ho
  Reasoning traces shape outputs but models won’t say so.
  In Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
  San Diego, California, United States, pp. 42852–42878.
  External Links: [Document](https://dx.doi.org/10.18653/v1/2026.acl-long.1986),
  [Link](https://aclanthology.org/2026.acl-long.1986/)
  Cited by: [§2](#S2.SS0.SSS0.Px5.p1.1 "Reasoning traces as state. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Hsieh et al. (2024)
  C. Hsieh, S. Sun, S. Kriman, S. Acharya, D. Rekesh, F. Jia, Y. Zhang, and B. Ginsburg
  RULER: what’s the real context size of your long-context language models?.
  In First Conference on Language Modeling,
  Cited by: [§2](#S2.SS0.SSS0.Px1.p1.1 "Long-context architectures and effective use. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Jeddi et al. (2026)
  A. Jeddi, M. Ciccone, and B. Taati
  LoopFormer: elastic-depth looped transformers for latent reasoning via shortcut modulation.
  In The Fourteenth International Conference on Learning Representations,
  Cited by: [§2](#S2.SS0.SSS0.Px3.p1.1 "Architectural recurrence. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Kuratov et al. (2024)
  Y. Kuratov, A. Bulatov, P. Anokhin, I. Rodkin, D. Sorokin, A. Sorokin, and M. Burtsev
  BABILong: testing the limits of LLMs with long context reasoning-in-a-haystack.
  In Advances in Neural Information Processing Systems,
  Vol. 37.
  Note: Datasets and Benchmarks Track
  External Links: [Document](https://dx.doi.org/10.52202/079017-3381),
  [Link](https://papers.nips.cc/paper_files/paper/2024/hash/c0d62e70dbc659cc9bd44cbcf1cb652f-Abstract-Datasets_and_Benchmarks_Track.html)
  Cited by: [§2](#S2.SS0.SSS0.Px1.p1.1 "Long-context architectures and effective use. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Lee et al. (2025)
  C. Lee, A. M. Rush, and K. Vafa
  Critical thinking: which kinds of complexity govern optimal reasoning length?.
  In Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics,
  External Links: [Document](https://dx.doi.org/10.18653/v1/2025.ijcnlp-long.57)
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Lepori et al. (2025)
  M. A. Lepori, M. C. Mozer, and A. Ghandeharioun
  Racing thoughts: explaining contextualization errors in large language models.
  In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),
  Albuquerque, New Mexico, pp. 3020–3036.
  External Links: [Document](https://dx.doi.org/10.18653/v1/2025.naacl-long.155),
  [Link](https://aclanthology.org/2025.naacl-long.155/)
  Cited by: [§2](#S2.SS0.SSS0.Px2.p1.1 "Causal order in reasoning. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Levy et al. (2025)
  M. Levy, Z. Elyoseph, S. Ravfogel, and Y. Goldberg
  State over tokens: characterizing the role of reasoning tokens.
  External Links: 2512.12777,
  [Link](https://arxiv.org/abs/2512.12777)
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§2](#S2.SS0.SSS0.Px5.p1.1 "Reasoning traces as state. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Liu et al. (2024)
  N. F. Liu, K. Lin, J. Hewitt, A. Paranjape, M. Bevilacqua, F. Petroni, and P. Liang
  Lost in the middle: how language models use long contexts.
  Transactions of the Association for Computational Linguistics 12, pp. 157–173.
  External Links: [Document](https://dx.doi.org/10.1162/tacl%5Fa%5F00638),
  [Link](https://aclanthology.org/2024.tacl-1.9/)
  Cited by: [§2](#S2.SS0.SSS0.Px1.p1.1 "Long-context architectures and effective use. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Merrill and Sabharwal (2024)
  W. Merrill and A. Sabharwal
  The expressive power of transformers with chain of thought.
  In The Twelfth International Conference on Learning Representations,
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Nie et al. (2025)
  S. Nie, F. Zhu, Z. You, X. Zhang, J. Ou, J. Hu, J. Zhou, Y. Lin, J. Wen, and C. Li
  Large language diffusion models.
  In Advances in Neural Information Processing Systems,
  Vol. 38, pp. 50608–50646.
  External Links: [Document](https://dx.doi.org/10.52202/085713-1689),
  [Link](https://proceedings.neurips.cc/paper_files/paper/2025/hash/48b383b24230e0e6e649d9c98dae4d8c-Abstract-Conference.html)
  Cited by: [§2](#S2.SS0.SSS0.Px3.p1.1 "Architectural recurrence. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Nye et al. (2021)
  M. Nye, A. J. Andreassen, G. Gur-Ari, H. Michalewski, J. Austin, D. Bieber, D. Dohan, A. Lewkowycz, M. Bosma, D. Luan, C. Sutton, and A. Odena
  Show your work: scratchpads for intermediate computation with language models.
  Note: arXiv:2112.00114
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Ok and Lee (2026)
  H. Ok and J. Lee
  Lost in the prompt order: revealing the limitations of causal attention in language models.
  In Findings of the Association for Computational Linguistics: ACL 2026,
  San Diego, California, United States, pp. 38566–38587.
  External Links: [Document](https://dx.doi.org/10.18653/v1/2026.findings-acl.1921),
  [Link](https://aclanthology.org/2026.findings-acl.1921/)
  Cited by: [§2](#S2.SS0.SSS0.Px2.p1.1 "Causal order in reasoning. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* OpenAI (2025a)
  OpenAI
  GraphWalks: a multi hop reasoning long context benchmark.
  Note: <https://huggingface.co/datasets/openai/graphwalks>Dataset card. Accessed August 3, 2026
  Cited by: [§4.1](#S4.SS1.SSS0.Px2.p1.1 "Datasets. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* OpenAI (2025b)
  OpenAI
  OpenAI MRCR: long context multiple needle in a haystack benchmark.
  Note: <https://huggingface.co/datasets/openai/mrcr>Dataset card. Accessed August 3, 2026
  Cited by: [§4.1](#S4.SS1.SSS0.Px2.p1.1 "Datasets. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Paul et al. (2024)
  D. Paul, R. West, A. Bosselut, and B. Faltings
  Making reasoning matter: measuring and improving faithfulness of chain-of-thought reasoning.
  In Findings of the Association for Computational Linguistics: EMNLP 2024,
  Miami, Florida, USA, pp. 15012–15032.
  External Links: [Document](https://dx.doi.org/10.18653/v1/2024.findings-emnlp.882),
  [Link](https://aclanthology.org/2024.findings-emnlp.882/)
  Cited by: [§2](#S2.SS0.SSS0.Px5.p1.1 "Reasoning traces as state. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Qiu et al. (2025)
  Z. Qiu, Z. Wang, B. Zheng, Z. Huang, K. Wen, S. Yang, R. Men, L. Yu, F. Huang, S. Huang, D. Liu, J. Zhou, and J. Lin
  Gated attention for large language models: non-linearity, sparsity, and attention-sink-free.
  In Advances in Neural Information Processing Systems,
  Vol. 38, pp. 110931–110957.
  External Links: [Document](https://dx.doi.org/10.52202/085713-3345),
  [Link](https://proceedings.neurips.cc/paper_files/paper/2025/hash/904e89bb4e632e75fb47f093b620b257-Abstract-Conference.html)
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Models. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Qwen Team (2025a)
  Qwen Team
  Qwen3 technical report.
  Technical report
  Technical Report arXiv:2505.09388, Alibaba Cloud.
  External Links: 2505.09388,
  [Document](https://dx.doi.org/10.48550/arXiv.2505.09388),
  [Link](https://arxiv.org/abs/2505.09388)
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Qwen Team (2025b)
  Qwen Team
  Qwen3-Next-80B-A3B-Instruct model card.
  Model card
   Alibaba Cloud.
  Note: Official model card
  External Links: [Link](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§2](#S2.SS0.SSS0.Px1.p1.1 "Long-context architectures and effective use. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Sahoo et al. (2024)
  S. S. Sahoo, M. Arriola, Y. Schiff, A. Gokaslan, E. Marroquin, J. T. Chiu, A. Rush, and V. Kuleshov
  Simple and effective masked diffusion language models.
  In Advances in Neural Information Processing Systems,
  Vol. 37.
  External Links: [Document](https://dx.doi.org/10.52202/079017-4135),
  [Link](https://proceedings.neurips.cc/paper_files/paper/2024/hash/eb0b13cc515724ab8015bc978fdde0ad-Abstract-Conference.html)
  Cited by: [§2](#S2.SS0.SSS0.Px3.p1.1 "Architectural recurrence. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Saunshi et al. (2025)
  N. Saunshi, N. Dikkala, Z. Li, S. Kumar, and S. J. Reddi
  Reasoning with latent thoughts: on the power of looped transformers.
  In The Thirteenth International Conference on Learning Representations,
  Cited by: [§2](#S2.SS0.SSS0.Px3.p1.1 "Architectural recurrence. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Vodrahalli et al. (2024)
  K. Vodrahalli, S. Ontanon, N. Tripuraneni, K. Xu, S. Jain, R. Shivanna, J. Hui, N. Dikkala, M. Kazemi, B. Fatemi, R. Anil, E. Dyer, S. Shakeri, R. Vij, H. Mehta, V. Ramasesh, Q. Le, E. Chi, Y. Lu, O. Firat, A. Lazaridou, J. Lespiau, N. Attaluri, and K. Olszewska
  Michelangelo: long context evaluations beyond haystacks via latent structure queries.
  External Links: 2409.12640,
  [Document](https://dx.doi.org/10.48550/arXiv.2409.12640),
  [Link](https://arxiv.org/abs/2409.12640)
  Cited by: [§4.1](#S4.SS1.SSS0.Px2.p1.1 "Datasets. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Wei et al. (2022)
  J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. V. Le, and D. Zhou
  Chain-of-thought prompting elicits reasoning in large language models.
  In Advances in Neural Information Processing Systems,
  Vol. 35, pp. 24824–24837.
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Xu et al. (2024)
  X. Xu, C. Tao, T. Shen, C. Xu, H. Xu, G. Long, J. Lou, and S. Ma
  Re-reading improves reasoning in large language models.
  In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing,
  Miami, Florida, USA, pp. 15549–15575.
  External Links: [Document](https://dx.doi.org/10.18653/v1/2024.emnlp-main.871),
  [Link](https://aclanthology.org/2024.emnlp-main.871/)
  Cited by: [§2](#S2.SS0.SSS0.Px4.p1.1 "Rereading and textual feedback. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§4.3](#S4.SS3.p3.1 "4.3 Context Order Ablations ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [Table 3](#S4.T3a.4.7.1 "In 4.3 Context Order Ablations ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* xz-keg (2026)
  xz-keg
  1M Novel Understanding Bench.
  Note: <https://github.com/xz-keg/Novel-Understanding-Bench>Project repository. Accessed August 3, 2026
  Cited by: [§4.1](#S4.SS1.SSS0.Px2.p1.1 "Datasets. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Yang et al. (2025)
  S. Yang, J. Kautz, and A. Hatamizadeh
  Gated delta networks: improving Mamba2 with delta rule.
  In The Thirteenth International Conference on Learning Representations,
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§2](#S2.SS0.SSS0.Px1.p1.1 "Long-context architectures and effective use. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Models. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Yu et al. (2025)
  S. Yu, I. Kim, J. Song, S. Lee, J. Park, and S. Yoon
  Unleashing multi-hop reasoning potential in large language models through repetition of misordered context.
  In Findings of the Association for Computational Linguistics: NAACL 2025,
  Albuquerque, New Mexico, pp. 6450–6470.
  External Links: [Document](https://dx.doi.org/10.18653/v1/2025.findings-naacl.360),
  [Link](https://aclanthology.org/2025.findings-naacl.360/)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§2](#S2.SS0.SSS0.Px2.p1.1 "Causal order in reasoning. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Z.ai (2026a)
  Z.ai
  GLM-5.2 & GLM-5.1 & GLM-5.
  Note: <https://github.com/zai-org/GLM-5>Official GLM-5 series repository. Accessed August 3, 2026
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Models. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Z.ai (2026b)
  Z.ai
  GLM-5.2.
  Note: <https://docs.bigmodel.cn/cn/guide/models/text/glm-5.2>Official model documentation. Accessed August 3, 2026
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Models. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"),
  [§4.1](#S4.SS1.SSS0.Px2.p6.1 "Datasets. ‣ 4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").
* Zhao et al. (2026)
  Y. Zhao, R. Qiu, T. Wei, Y. Bei, Z. Liu, L. Chen, I. Lourentzou, H. Tong, and J. He
  ReContext: recursive evidence replay as LLM harness for long-context reasoning.
  External Links: 2607.02509,
  [Link](https://arxiv.org/abs/2607.02509)
  Cited by: [§2](#S2.SS0.SSS0.Px4.p1.1 "Rereading and textual feedback. ‣ 2 Related Work ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").

## Appendix A Attaining the Worst-Case Residual-Map Count

Let $\mathcal{S}$ be a finite nonempty state set, $\mathcal{C}$ an input
alphabet, $n$ the sequence length, and
$t:\mathcal{C}^{n}\times\mathcal{S}\rightarrow\mathcal{S}$ a conditional
state-update task. For an information sequence $C\in\mathcal{C}^{n}$, define the
residual map and the number of distinct residual maps by

|  |  |  |  |
| --- | --- | --- | --- |
|  | $\displaystyle\phi_{C}$ | $\displaystyle=(t(C,z))_{z\in\mathcal{S}}\in\mathcal{S}^{\mathcal{S}},$ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | $\displaystyle\mathcal{K}$ | $\displaystyle=\left|\{\phi_{C}\mid C\in\mathcal{C}^{n}\}\right|.$ |  |

Equivalently, $\phi_{C}(z)=t(C,z)$. For every finite nonempty state set
$\mathcal{S}$, this appendix constructs a task for which
$\mathcal{K}=|\mathcal{S}|^{|\mathcal{S}|}$. The corresponding late-order
working-memory requirement is

|  |  |  |
| --- | --- | --- |
|  | $$ \left\lceil\log_{2}\mathcal{K}\right\rceil=\left\lceil|\mathcal{S}|\log_{2}|\mathcal{S}|\right\rceil\text{ bits}. $$ |  |

Fix an arbitrary finite nonempty state set $\mathcal{S}$. For this
$\mathcal{S}$, the construction below chooses $\mathcal{C}$, $n$, and $t$ and
evaluates $\mathcal{K}$ under the definition above.
Set $m=|\mathcal{S}|$ and write
$b=\log_{2}m$. Since every $\phi_{C}$ belongs to
$\mathcal{S}^{\mathcal{S}}$, $\mathcal{K}\leq m^{m}$.

#### Proposition.

For every finite nonempty state set $\mathcal{S}$, there exist a finite input
alphabet $\mathcal{C}$ and a conditional state-update task such that, with
$n=1$, $\mathcal{K}=m^{m}$. Every
deterministic one-pass processor that is exact on all inputs and reads $C$
before $z$ must therefore retain at least

|  |  |  |
| --- | --- | --- |
|  | $$ \left\lceil\log_{2}\mathcal{K}\right\rceil=\left\lceil m\log_{2}m\right\rceil=\left\lceil b\,2^{b}\right\rceil $$ |  |

bits of persistent input-dependent state immediately before reading $z$.

#### Construction.

Set $n=1$ and choose the input alphabet

|  |  |  |
| --- | --- | --- |
|  | $$ \mathcal{C}=\{c_{f}\mid f\in\mathcal{S}^{\mathcal{S}}\}. $$ |  |

Thus $|\mathcal{C}|=m^{m}$. Define one fixed update rule
$U:\mathcal{S}\times\mathcal{C}\to\mathcal{S}$ by $U(s,c_{f})=f(s)$, equivalently
$U_{c_{f}}=f$. For every $f\in\mathcal{S}^{\mathcal{S}}$, the sequence
$C_{f}=(c_{f})$ belongs to $\mathcal{C}^{n}$, and its residual map satisfies

|  |  |  |
| --- | --- | --- |
|  | $$ \phi_{C_{f}}(z)=t(C_{f},z)=U_{c_{f}}(z)=f(z). $$ |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | $$ \{\phi_{C}\mid C\in\mathcal{C}^{n}\}=\mathcal{S}^{\mathcal{S}}, $$ |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | $\displaystyle\mathcal{K}$ | $\displaystyle=\left|\{\phi_{C}\mid C\in\mathcal{C}^{n}\}\right|$ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | $\displaystyle=|\mathcal{S}^{\mathcal{S}}|=m^{m}.$ |  |

#### Late-order cut.

Consider the processor configuration after $C_{f}$ and immediately before $z$
is read. If two distinct functions $f\neq g$ produced the same configuration,
some $z\in\mathcal{S}$ would satisfy $f(z)\neq g(z)$. Starting from the shared
configuration, the processor would produce the same output after reading the
identical suffix $z$, contradicting exactness. Thus the cut admits at least
$m^{m}$ distinct configurations. At this cut, a processor attains the bound by
storing the identity of $f$ in one of $m^{m}$ states and applying the fixed
lookup rule when $z$ arrives. Under the accounting convention above, the
exact cut-state requirement for this family is
$\lceil\log_{2}(m^{m})\rceil$ bits.

#### Condition-first comparison.

For the order $(z,c_{f})$, a single $\mathcal{S}$-valued register suffices:
initialize it with $z$ and replace its value by $f(z)$ when $c_{f}$ arrives. At
the cut after $z$ and immediately before $c_{f}$, this implementation has $m$
possible input-dependent configurations. This is optimal. Let
$\iota=\operatorname{id}_{\mathcal{S}}$, so $c_{\iota}\in\mathcal{C}$. If two
distinct values $z,z^{\prime}\in\mathcal{S}$ produced the same configuration at this
cut, then reading the identical suffix $c_{\iota}$ would force the same output
from both configurations. Exactness instead requires the respective outputs
$\iota(z)=z$ and $\iota(z^{\prime})=z^{\prime}$. Hence the cut admits at least $m$
configurations, and its exact cut-state requirement is
$\lceil\log_{2}m\rceil=\lceil b\rceil$ bits. When $m=1$, each cut has one
configuration and therefore requires zero bits. As a concrete check, $m=4$
gives $\mathcal{K}=4^{4}=256$: the late-order cut requires eight bits, whereas
the condition-first cut requires two bits.

#### Scope.

This finite-state existence construction applies to the stated task family
and to deterministic, exact, one-pass computation. It is an adversarial
worst-case construction whose alphabet and fixed transition table realize all
self-maps of $\mathcal{S}$. The processor cannot reread $C$, and every
auxiliary writable store is included in the counted configuration. Restricted
update families may realize fewer residual maps, yielding a smaller lower
bound from this residual-map argument.

#### Causal Transformers are Causal State Update Processors.

Transformers use kv caches that may expand as context length grows.
Modern transformers may include more complex memory structures like latent kv, shared kv or linear kv. Despite these, causal transformers with a finite maximal context length and finite precisions are indeed causal state update processors defined in section [3.1](#S3.SS1 "3.1 Causal State Updates and Order-Dependent Memory ‣ 3 Methodology ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").

Define the "working state" as to
contain the current position, all layerwise key–value entries, and any other persistent input-dependent inference buffers.
Causal inference computes the new token
representation layer by layer and appends the corresponding key–value entries.
Thus the next configuration is a fixed function of the preceding configuration
and the new token. The maximum context length and finite precision make the
configuration space finite. Per-token or other forms of caches therefore do not violate the causal
state update abstraction.

## Appendix B Scoring and Run Qualifications

Section [4.1](#S4.SS1 "4.1 Setup ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") gives the common model, dataset, condition,
and scoring setup. This appendix specifies scorer edge cases, qualifications of
the reported runs, and the record-selection rules used to compute the reported
cells.

### B.1 Scorer Edge Cases

#### GraphWalks.

The evaluator extracts the terminal line Final Answer: [...] and
compares the parsed node set with the gold set. A valid empty prediction is
scored normally: two empty sets have EM and F1 equal to one, whereas one empty
and one nonempty set have EM and F1 equal to zero. An absent response or a
missing, malformed, or nonterminal answer receives zero.
For Question First, we conservatively treat a null or unknown termination
marker as length-limited. In the evaluated records, 121 have a null marker,
none have an unknown marker, and 60 are natively marked as length-limited, for
181 length-limited outputs in total (160 BFS and 21 Parents). One additional
stopped BFS output lacks the required terminal answer syntax. All 182 outputs
receive zero.

#### MRCRv2 8-needle.

Each example supplies a random prefix that must begin both the prediction and
reference. The scorer validates and removes this prefix before computing EM
and the ratio returned by Python’s difflib.SequenceMatcher. EM is one
when the remaining strings match exactly and zero otherwise. The paper labels
the ratio *Seq.*; it is distinct from GraphWalks set F1. A missing or
invalid prefix gives zero for both metrics. Some prompts trigger provider
content filters; filtered outputs remain in the denominator and receive zero.

#### NUB-1M.

We maintain a reference answer for each problem and use DeepSeek V4 Pro to
compare the extracted solver answer with that reference. Solver identity and
feedback order are excluded from the judge prompt. The judge returns a
Boolean correctness decision and a short rationale; we use the Boolean as the
binary score.

We also manually reviewed the judged outputs and found no errors.

## Appendix C Prompt and State Templates

This appendix shows the fixed serializer used to construct $T$ and records the
dataset-specific prompt details for experiments. We retain the compact condition notation $[T,x]$ for trace as state and
$[x,T]$ for trace append; the paragraphs below give the exact insertion
boundaries and fixed interface text suppressed by that notation.

### C.1 Reusable Trace Block

Let $r=(r_{1},\ldots,r_{n_{\mathrm{tr}}})$ denote the selected first-pass reasoning traces
in source order, and let $P_{\mathcal{D}}$ denote the dataset-specific
trace-block preamble containing its description and warning.
Table [4](#A3.T4 "Table 4 ‣ C.1 Reusable Trace Block ‣ Appendix C Prompt and State Templates ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") shows their fixed text form.

Table 4: The fixed serialization used to construct the reusable trace block.

|  |  |
| --- | --- |
| Reasoning traces $r$ | $T=\pi(r)$ |
| $\displaystyle r=(r_{1},r_{2},\ldots,r_{n_{\mathrm{tr}}})$ | $P_{\mathcal{D}}$  *(dataset-specific prompt)* <first_run_reasoning_traces> [Trace 1] $r_{1}$ [Trace 2] $r_{2}$ $\vdots$ [Trace $n_{\mathrm{tr}}$] $r_{n_{\mathrm{tr}}}$ </first_run_reasoning_traces> |

Here $P_{\mathcal{D}}$ is part of $T$, rather than part of the original task
prompt $x$; its exact value for each dataset is given verbatim below.
Separately returned visible answers remain outside $T$. The five source
reasoning fields are taken in repeat-index order. When applying the
50,000-character cap, any reasoning field longer than 50,000 characters is
replaced by its first 50,000 characters followed by ...; block
formatting then strips leading and trailing whitespace.

### C.2 Model-Specific Details

#### Qwen 3.7 Max reasoning instruction.

For every evaluated Qwen 3.7 Max condition, we use the following fixed
xhigh instruction recommended for reasoning scenarios in the official
Qwen 3.7 Max evaluation guidance available when the experiments were run:

> Reasoning effort is set to xhigh. Please think carefully through the task,
> validate key assumptions, consider plausible alternatives, and prioritize
> correctness, consistency, and clarity in the final answer.

Here xhigh names the recommended prompt text rather than a
provider-side reasoning_effort value. For MRCRv2, the runner prepends
the instruction to the system message. The GraphWalks and NUB-1M runners
prepend it to their single user message. Within each dataset, the delivery
format is fixed across the evaluated conditions and does not change the
relative placement of $T$ and the long context.

#### Version of Deepseek V4 Pro.

There are two models both called Deepseek V4 Pro released on 2026-4-24 and 2026-8-13 respectively. We use the 2026-4-24 version for our experiments.

### C.3 Dataset-Specific Details

#### GraphWalks.

For GraphWalks, $P_{\mathcal{D}}$ is the following exact text:

> Below are selected reasoning traces or trace tail windows from independent
> first attempts on the same graph problem. They may contain mistakes. Use them
> only as scratchpad hints, and verify against the graph.

We also use a system prompt:

> You solve directed-graph algorithm problems. Use only the graph and operation
> in the user message. Return exactly one visible line in this format: Final
> Answer: [node1, node2]. Use [] for the empty set. Do not include any text before
> or after that line.

The runner also appends this exact answer-format instruction to the user
message:

> Return exactly one line in this format: Final Answer: [node1, node2]. Use [] for
> the empty set.

For $[T,x]$, the complete trace block precedes the complete released
GraphWalks prompt, and the answer-format instruction follows that prompt. For
$[x,T]$, the runner splits the released prompt immediately before its last
Operation: block: the graph instructions and edge list come first,
then the identical trace block, then the final operation and answer-format
instruction.

This formatting instruction guides the model to output
its answer in a parse-able way.

#### MRCRv2.

For MRCRv2, $P_{\mathcal{D}}$ is the following exact text:

> Below are reasoning traces from independent first attempts on the same MRCR
> problem. They may contain mistakes. Use them only as scratchpad hints; verify
> against the conversation and final request. Do not copy any trace text into the
> visible answer.

## Appendix D GraphWalks Difficulty Profiles

As an exploratory diagnostic, we examine whether the descriptive timing
gap varies with two observable GraphWalks properties. BFS specifies a requested
traversal depth $d$, and Parents has a gold parent-set size $k$. These variables
summarize aspects of traversal and aggregation demand, but realized difficulty
can also depend on frontier size, early termination, and graph structure. The
analysis and highlighted ranges were developed after inspecting outcomes; they
are hypothesis-generating rather than confirmatory tests of an interaction,
threshold, capacity limit, or mechanism.

We pool adjacent low-support values into BFS bins $1$–$2$, $3$–$4$,
$5$–$6$, $7$–$8$, and $9$–$10$, and Parents bins $0$, $1$, $2$, $3$,
$4$–$5$, and $\geq 6$. Their problem counts are $(17,25,21,15,22)$ and
$(13,17,25,20,13,12)$, respectively. For feedback timing
$p\in\{\mathrm{pre},\mathrm{post}\}$ and bin $b$, we report the gain over
the common first-pass baseline,

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \Delta_{p}(b)=\operatorname{Score}_{p}(b)-\operatorname{Score}_{\mathrm{first}}(b). $$ |  | (6) |

Each point averages five stored repeats within each problem and then the
problems in its bin. The yellow regions are descriptive and outcome-informed;
their boundaries are specific to each model, subtask, and metric. They were
not selected independently of the displayed scores and do not support
confirmatory inference.

Figure 3: GraphWalks exact-match gains over the first pass by BFS depth $d$
(left) and gold-parent count $k$ (right). The blue and orange curves report
$\Delta_{\mathrm{pre}}$ and $\Delta_{\mathrm{post}}$. Bin supports appear
below the panels. Yellow shading marks descriptive, outcome-informed ranges
of larger separation, with boundaries chosen separately for each model and
subtask.

The prefix-minus-postfix exact-match gap in
Figure [3](#A4.F3 "Figure 3 ‣ Appendix D GraphWalks Difficulty Profiles ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") is concentrated in particular bins.
DeepSeek V4 Pro has its largest BFS timing gaps
at $d=3$–$6$, and Qwen 3.7 Max has a smaller concentration in the same range.
GLM-5.2 has positive gaps through $d=8$ and a reversal in the final pooled
bin. The Parents profiles differ. trace as state is never below trace append in the plotted
exact-match bins, with a tie for Qwen 3.7 Max at $k=0$. Qwen’s separation
grows with $k$; DeepSeek V4 Pro and GLM-5.2 are nonmonotonic but have large
gaps in selected middle or high-$k$ bins.

Figure 4: Set F1 gains for the same BFS (top) and Parents (bottom)
stratifications. Set F1 records partial overlap between predicted and gold
node sets. Yellow shading again marks descriptive, outcome-informed ranges
selected separately for each model, subtask, and metric.

The binned set F1 means preserve the strong DeepSeek V4 Pro BFS pattern, while
Qwen 3.7 Max and GLM-5.2 show smaller or more localized separation. Parents
generally favors trace as state, with substantial variation in the size of the gap.
These profiles document heterogeneity but do not establish why it occurs or
that depth or parent-set size mediates trace reuse. A confirmatory follow-up
would define bins or continuous contrasts before observing timing outcomes
and evaluate them on held-out problems.

## Appendix E Confidence Intervals

This appendix reports paired uncertainty for the principal same-$T$
timing contrast and cell-wise uncertainty for the broader results and
ablations. Table [5](#A5.T5 "Table 5 ‣ Appendix E Confidence Intervals ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") reports the mean
paired trace as state-minus-trace append difference and an
unadjusted 95% percentile interval after averaging the five repeats within each
problem. The intervals lie fully above zero for 20 of 24 cells. The four
intervals that cross zero are DeepSeek V4 Pro MRCRv2 512K EM, Qwen 3.7 Max
GraphWalks BFS F1, and GLM-5.2 GraphWalks BFS EM and F1.

Table 5: Paired problem-cluster uncertainty for the strict same-$T$ timing contrast. $\Delta$ is Trace as State minus Trace Append in percentage points; brackets give unadjusted 95% percentile intervals over problems after five-repeat averaging ($n=100$ per cell; 20,000 resamples; seed 0). GW is GraphWalks 256K and MR is MRCRv2 8-needle. Intervals wholly above zero are bold.

| Model | Cell | $\Delta$ [95% CI] |
| --- | --- | --- |
| DeepSeek V4 Pro | GW BFS EM | $+17.00\;\mathbf{[+11.00,\,+23.40]}$ |
| GW BFS F1 | $+17.63\;\mathbf{[+11.65,\,+23.97]}$ |
| GW Par. EM | $+38.80\;\mathbf{[+31.60,\,+46.20]}$ |
| GW Par. F1 | $+26.02\;\mathbf{[+20.52,\,+31.84]}$ |
| MR 256K EM | $+10.20\;\mathbf{[+4.80,\,+15.80]}$ |
| MR 256K Seq. | $+9.11\;\mathbf{[+4.77,\,+13.93]}$ |
| MR 512K EM | $+3.20\;[-2.60,\,+9.40]$ |
| MR 512K Seq. | $+6.35\;\mathbf{[+1.69,\,+11.36]}$ |
| Qwen 3.7 Max | GW BFS EM | $+3.40\;\mathbf{[+1.00,\,+6.40]}$ |
| GW BFS F1 | $+1.29\;[-0.56,\,+3.90]$ |
| GW Par. EM | $+25.40\;\mathbf{[+17.60,\,+33.60]}$ |
| GW Par. F1 | $+7.43\;\mathbf{[+4.63,\,+10.58]}$ |
| MR 256K EM | $+4.40\;\mathbf{[+1.40,\,+8.00]}$ |
| MR 256K Seq. | $+4.19\;\mathbf{[+1.41,\,+7.53]}$ |
| MR 512K EM | $+6.40\;\mathbf{[+1.80,\,+11.40]}$ |
| MR 512K Seq. | $+5.11\;\mathbf{[+0.67,\,+9.84]}$ |
| GLM-5.2 | GW BFS EM | $+3.40\;[-1.00,\,+7.80]$ |
| GW BFS F1 | $-0.83\;[-3.94,\,+1.62]$ |
| GW Par. EM | $+16.80\;\mathbf{[+10.40,\,+23.80]}$ |
| GW Par. F1 | $+7.32\;\mathbf{[+3.93,\,+11.30]}$ |
| MR 256K EM | $+21.20\;\mathbf{[+14.40,\,+28.20]}$ |
| MR 256K Seq. | $+13.56\;\mathbf{[+8.33,\,+19.34]}$ |
| MR 512K EM | $+10.80\;\mathbf{[+3.40,\,+18.20]}$ |
| MR 512K Seq. | $+10.20\;\mathbf{[+4.65,\,+16.08]}$ |

Figures [5](#A5.F5 "Figure 5 ‣ Appendix E Confidence Intervals ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers")
and [6](#A5.F6 "Figure 6 ‣ Appendix E Confidence Intervals ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") report cell means with 95%
percentile intervals from the same problem-cluster bootstrap. Repeats are
averaged within each problem.

Figure [5](#A5.F5 "Figure 5 ‣ Appendix E Confidence Intervals ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") covers the strict same-$T$ GraphWalks
and MRCRv2 comparisons in Table [2](#S4.T2a "Table 2 ‣ 4.2 Main Results ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers"), together with the
supporting NUB-1M results. The NUB-1M intervals are wider, consistent with its
20 evaluated questions. Figure [6](#A5.F6 "Figure 6 ‣ Appendix E Confidence Intervals ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") covers
the GraphWalks control ablation. The same bootstrap procedure produces the
shaded trace-count intervals in Figure [2](#S4.F2 "Figure 2 ‣ 4.4 Trace Count Ablation ‣ 4 Experiments ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers").

Figure 5: Uncertainty for the strict same-$T$ comparisons. The top two rows show
GraphWalks 256K exact match and set F1, split into BFS and Parents; the bottom
two wide rows show MRCRv2 8-needle exact match and SequenceMatcher ratio,
split into 256K and 512K bins. The final panel shows NUB-1M accuracy. Points
are means; bars are 95% percentile intervals after averaging 5 repeats
within each problem.

Figure 6: Uncertainty for DeepSeek V4 Pro GraphWalks 256K control comparisons
in exact match and set F1. Points are means; bars are 95% percentile
intervals from 20,000 problem-cluster bootstrap resamples (seed 0).
Majority@5 retains answer elements occurring in at least three repeat-level
prediction sets, and Oracle@5 reports the retrospective maximum evaluator
score among the five outputs. Other conditions average five planned
repeats within each problem and assign zero to missing or invalid outputs.

## Appendix F Token Usage

Table [6](#A6.T6 "Table 6 ‣ Appendix F Token Usage ‣ Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers") reports token counts returned by provider
APIs for the solver calls underlying the main results.

For each retained response with provider-reported usage, we report cached
input, missed input, and output tokens. Missed input is total input minus cached input.
Reasoning tokens are included in the output.

First Pass is the shared source pass used to construct $T$. For trace as state and trace append, we also report the
*Total tokens* columns that add the corresponding First Pass counts component-wise.

Table 6: Provider-reported token usage for main-result inference, in
millions. *Tokens* reports the pass named in each row.
For trace append and trace as state, *Total tokens* adds First Pass
component-wise; those columns are blank for First Pass itself. Missed
input is total input minus cached input.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark | Condition | Tokens | | | Total tokens | | |
|  |  | Cached input | Missed input | Output | Cached input | Missed input | Output |
| *DeepSeek V4 Pro* | | | | | | | |
| GraphWalks 256K | First Pass | 206.766 | 51.092 | 62.507 |  |  |  |
|  | trace append | 271.017 | 68.554 | 35.231 | 477.783 | 119.646 | 97.738 |
|  | trace as state | 277.074 | 62.501 | 27.975 | 483.840 | 113.593 | 90.482 |
| MRCRv2 256K | First Pass | 50.817 | 46.961 | 1.149 |  |  |  |
|  | trace append | 79.982 | 20.820 | 0.690 | 130.799 | 67.782 | 1.839 |
|  | trace as state | 51.875 | 50.051 | 1.355 | 102.692 | 97.012 | 2.504 |
| MRCRv2 512K | First Pass | 155.283 | 38.195 | 0.989 |  |  |  |
|  | trace append | 178.675 | 18.526 | 0.702 | 333.958 | 56.721 | 1.691 |
|  | trace as state | 157.261 | 39.940 | 1.241 | 312.544 | 78.135 | 2.230 |
| NUB-1M Season 2 | First Pass | 31.651 | 8.418 | 0.817 |  |  |  |
|  | trace append | 39.589 | 4.460 | 0.184 | 71.240 | 12.878 | 1.001 |
|  | trace as state | 27.418 | 16.637 | 0.398 | 59.069 | 25.055 | 1.215 |
| *Qwen 3.7 Max* | | | | | | | |
| GraphWalks 256K | First Pass | 260.213 | 97.483 | 5.402 |  |  |  |
|  | trace append | 264.906 | 117.866 | 2.865 | 525.119 | 215.350 | 8.267 |
|  | trace as state | 271.742 | 111.030 | 3.615 | 531.955 | 208.514 | 9.017 |
| MRCRv2 256K | First Pass | 38.337 | 63.495 | 2.111 |  |  |  |
|  | trace append | 60.227 | 51.195 | 0.989 | 98.564 | 114.690 | 3.100 |
|  | trace as state | 62.213 | 49.209 | 1.397 | 100.550 | 112.704 | 3.508 |
| MRCRv2 512K† | First Pass | 134.607 | 63.738 | 2.263 |  |  |  |
|  | trace append | 154.827 | 53.489 | 1.211 | 289.434 | 117.226 | 3.474 |
|  | trace as state | 153.971 | 54.345 | 1.724 | 288.577 | 118.083 | 3.988 |
| NUB-1M Season 2 | First Pass | 34.253 | 7.547 | 0.489 |  |  |  |
|  | trace append | 38.184 | 5.773 | 0.253 | 72.437 | 13.320 | 0.742 |
|  | trace as state | 32.414 | 11.549 | 0.419 | 66.667 | 19.096 | 0.908 |
| *GLM-5.2* | | | | | | | |
| GraphWalks 256K | First Pass | 134.748 | 150.760 | 19.463 |  |  |  |
|  | trace append | 55.612 | 265.396 | 9.127 | 190.361 | 416.156 | 28.591 |
|  | trace as state | 64.390 | 256.618 | 16.491 | 199.138 | 407.377 | 35.954 |
| MRCRv2 256K | First Pass | 73.782 | 24.718 | 1.891 |  |  |  |
|  | trace append | 82.413 | 20.940 | 2.518 | 156.195 | 45.658 | 4.409 |
|  | trace as state | 82.464 | 20.888 | 1.516 | 156.246 | 45.606 | 3.407 |
| MRCRv2 512K | First Pass | 151.247 | 42.262 | 1.441 |  |  |  |
|  | trace append | 157.740 | 40.508 | 2.002 | 308.987 | 82.770 | 3.443 |
|  | trace as state | 157.458 | 40.790 | 1.648 | 308.705 | 83.052 | 3.089 |
| NUB-1M Season 2 | First Pass | 1.272 | 41.123 | 0.995 |  |  |  |
|  | trace append | 3.840 | 43.087 | 0.484 | 5.111 | 84.209 | 1.478 |
|  | trace as state | 0.457 | 46.475 | 0.856 | 1.728 | 87.598 | 1.850 |

---

[Original source](https://arxiv.org/html/2609.02702)
