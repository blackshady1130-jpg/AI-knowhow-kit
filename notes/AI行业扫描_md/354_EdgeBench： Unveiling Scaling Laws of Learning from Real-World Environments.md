# EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments

**作者：** ByteDance Seed  
**日期：** July 2, 2026  
**项目主页：** [https://edge-bench.org](https://edge-bench.org)  
**原文链接：** [https://edge-bench.org/paper.pdf](https://edge-bench.org/paper.pdf)  
**联系方式：** Shu Zhong (zhongshu@bytedance.com)

---

**Abstract**

Pretraining scaling laws reveal that model capability improves predictably with data and compute.

But learning from real world environments after deployment remains far less understood. Analyz-

ing roughly 38,000 hours of agent interaction with the environment across 134 real world tasks, we

nd, to the best of our knowledge, the rst evidence that overall performance during environment

learning follows a log-sigmoid scaling law with remarkably high precision, reaching _R_ ² = 0 _._ 998 .

Across model generations, we also nd that agent learning speed roughly doubles every three

months. This discovery stems from EdgeBench, a suite of 134 real world tasks with ultra-long

horizons, spanning scientic discovery, software engineering, combinatorial optimization, profes-

sional knowledge work, formal mathematics, and interactive games. Each task sustains at least

12 hours of continuous agent operation under rich, multilevel feedback, and is built through sub-

stantial expert eort. We publicly release 51 tasks and our full evaluation framework to accelerate

the study of how agents learn from real world experience.

**Date:** July 2, 2026

**Correspondence:** Shu Zhong at zhongshu@bytedance.com

**Project Page:** https://edge-bench.org

1

E dge B e n ch : 134 r ea l \- worl d , da y \- lon g t a s k s ac ross 6 ca p abi l i ty fa m i l ie s

A ge nt runt i m e ≥12 h p e r t a s k · r ec or ded h um a n e xp e rt eff ort m ea n 57\.2 h · e v e ry t a s k prov ide s r ich , r ea l \- worl d feedback f or c ont i nuously l ea rn i n g f rom e nv i ronm e nt

S cie nt ific & ML

S yst e ms & SE

O pt i m i z a t i on

K nowl edge

F orm a l

G a m e s

s ha r e o f 134 t a s k s ac ross 6 ca p abi l i ty fa m i l ie s

S cie nt ific P ro b l e ms & ML 39 t a s k s 29 %

I nv e rs e pro b l e ms , f or eca st i n g & ML on r ea l i nstrum e nt / fie l d da t a

G r a v i t a t i on a l \-

w a v e

de t ec t i on

3- D g r a v i ty

i nv e rs i on

G roun d w a t e r

plum e

mo de l i n g

S ol a r pow e r

f or eca st i n g

B a tt e ry

hea lt h

f or eca st i n g

···

\+34 mor e

S yst e ms & S o f tw a r e E n gi n ee r i n g 36 t a s k s 27 %

L a r ge \- s ca l e cha n ge s to r ea l pro d u c t i on c o deba s e s

RISC \- V CP U

de s ig n

M a t chi n g \-

e n gi n e

opt i m i z a t i on

R ege x e n gi n e

r e p ai r

P o cke t B a s e

de v e lopm e nt

T LS 1\.3

i mpl e m e nt a t i on

···

\+31 mor e

C om bi n a tor ia l O pt i m i z a t i on 19 t a s k s 14 %

O p e n \- e n ded opt i m i z a t i on , j u dged on qu a l i ty

V ehic l e

rout i n g

SA T / SM T

solv i n g

M ol ec ul a r

s e l f \-

a ss e m b ly

J o b \- s h op

s ched ul i n g

2- D i rr eg ul a r

n e st i n g

···

\+14 mor e

P ro fe ss i on a l K nowl edge W or k 19 t a s k s 14 %

W hi t e \- c oll a r de l i v e r ab l e s g r aded b y c l ie nt \- styl e ru b r ic s

C T A r i s k

b u dge t i n g

C ross \- b or de r

c ompl ia n ce

C l ai m \- r i n g

f r a u d a u di t

AIGC

story b o a r di n g

B r a n d a nnu a l

pl a nn i n g

···

\+14 mor e

F orm a l M a t h & T he or e m P rov i n g 13 t a s k s 10 %

M achi n e \- checked prov i n g i n L ea n 4 & C oq

F e rm a t

( r eg ul a r

ca s e )

S p he r e

e v e rs i on

C om bi n a tor ia l

ga m e s

E r d ős –

G r aha m

pro b l e m

P r i m e

N um be r

T he or e m

···

\+8 mor e

I nt e r ac t i v e G a m e s & S i mul a tors 8 t a s k s 6 %

S e qu e nt ia l deci s i on \- m aki n g i n OOD worl d s

N e t H ack

D un ge on

C r a wl

T r a nsport

ty c oon s i m

T e xt

ad v e ntur e s

W e snot h

···

\+3 mor e

**Figure 2**

EdgeBench task taxonomy.

134 real world tasks across six capability families, with feedback channels

designed to support within-run improvement. Recorded human expert eort estimates: mean 57.2 h.

**1**

**Introduction**

Scaling laws for pretraining [ 32 , 36 ] revealed that model capability improves predictably with data and

compute, an insight that guided much of the progress in the years that followed [ 2 , 3 , 22 , 24 , 25 , 49 , 53 

55 , 57 , 58 ]. Now, as large language models enter the agent era, they are being deployed into a growing

range of real world environments where they can try to learn from interaction, yet whether learning from

such environments obeys a clean scaling law remains unknown. Analyzing roughly 38,000 hours of agent

environment interaction across 134 diverse real world tasks, we nd, to the best of our knowledge, the

rst evidence that **when agents learn from real world environments, overall performance follows a log-**

**sigmoid scaling law as a function of environment interaction time** , achieving remarkably high precision with

_R_ ² = 0 _._ 998 .

Why study agents' ability to learn from their environments? Real world use of AI depends on more than what

a model learned during training. Some needed knowledge never appears in training data, such as private

records and internal tools. Even when raw data exists, it omits the human process behind it: the trial-and-

error, the interpretation of evidence, and the adaptation to feedback through which experts actually reach

results. The real world also never stands still: human knowledge keeps advancing, and new tools, discoveries,

and problems continually emerge that no xed training corpus can anticipate. Therefore, an agent's ability

to learn from its environment and improve task performance is central to deploying AI systems at scale in

the real world.

Studying this ability requires task environments that resemble real use, provide informative feedback for

learning, and allow agents enough time to learn through interaction. However, existing benchmarks often

lack such feedback or limit agents to only minutes or a few hours, making them not well suited to this

2

goal [ 10 , 15 , 35 , 46 , 69 , 81 ].

To address this gap, we created **EdgeBench** .

Our benchmark contains **134**

**realistic and diverse tasks spanning six capability families** , from scientic research and software engineering

to formal mathematics and interactive games, as shown in Figure 2 .

Each task runs in an executable

workspace that combines fast local exploration with slower judge feedback on submitted artifacts, mirroring

real-world workows. Agents can work for at least **12 hours** on each task (by contrast, Agents' Last Exam [ 69 ]

averages roughly one hour per task), while we record their submissions and track how performance changes

throughout the run. These tasks are substantial even for human experts: recorded expert eort averages

**57\.2 hours** per task and reaches up to **320 hours** . This makes EdgeBench a natural testbed for studying how

agents learn from their environments over long horizons.

Using EdgeBench, we evaluate frontier agents over roughly 38,000 hours of environment interaction. Our

study makes four main observations:

ˆ **Environment learning exhibits a precise log-sigmoid scaling law.** Averaged performance follows the

same functional form across the full benchmark, across task families, under longer interaction horizons

up to 72 hours, and when forecasting later performance from early trajectories.

ˆ **A theoretical derivation of the log-sigmoid law.** We propose a theory that models environment learning

as a frontier expansion process on latent task graphs, which explains why benchmark-averaged progress

takes the observed log-sigmoid form.

ˆ **Agent learning speed doubles roughly every three months.** Studying frontier models released since

September 2025, we nd a rapid scaling trend in how quickly frontier agents learn from their environ-

ments.

ˆ **Learning dynamics strongly shape long-horizon performance.** Long-horizon performance depends on

how agents use accumulated experience, not only on how many attempts they make. Continuous expe-

rience outperforms independent restarts, longer context improves retention, and detailed case studies

show that feedback can turn many failed probes into a few durable gains.

**2**

**EdgeBench**

**2\.1**

**Design Goals**

EdgeBench aims to measure whether an autonomous agent can learn from experience in an unfamiliar real

world environment. This requires two properties from a benchmark that existing evaluations lack:

ˆ **Ultra-long-horizon, diverse tasks.** Learning behaviors such as exploration, strategy revision, and expe-

rience accumulation need time and complexity to emerge. Short tasks are usually solved from memory

rather than learning, so measuring learning calls for long-horizon tasks. Because learning is a general

capability, these tasks must also span diverse domains.

ˆ **Realistic, multi-level feedback.**

In practice, human experts learn from rich feedback: test failures,

experimental results, unexpected phenomena, authoritative judgments, and more. A benchmark that

cannot oer such rich feedback cannot measure learning, and leaves the agent guessing what the eval-

uation actually rewards. We need feedback that approximates the real world, so we can measure true,

general-purpose learning.

The rst requirement motivates our task taxonomy (Ÿ 2\.2 ): 134 tasks across six capability families, each

designed as a day-scale challenge that supports frontier models running for at least 12 hours. The second

motivates our evaluation protocol (Ÿ 2\.3 ): each task individually simulates its own slice of the real world, pro-

viding isolated work and judge environments, local agent-driven feedback, submission-gated judge feedback,

and host-side trajectory measurement.

**2\.2**

**Task Taxonomy**

We searched for real world tasks that satisfy two criteria: a performance ceiling high enough that no current

agent can saturate it, and a workow that supports continuous learning rather than one-shot completion.

3

This search, conducted in collaboration with domain experts across elds, identied six capability families

and yielded 134 curated tasks (Figure 2 ):

ˆ **Scientific Problems & ML** (39 tasks). Each task uses real world research data and experimental settings

sourced from working scientists.

Domain expertise is essential: agents must formulate hypotheses,

choose models, validate against noisy observations, and rene iteratively. Many problems are open-

ended, with no known optimal solution.

ˆ **Systems & Software Engineering** (36 tasks). Agents work on production-grade codebases where a single

task may require thousands of lines of change, with over 100,000 lines in the largest cases. Because the

code spans interdependent modules, an agent must reason about cross-module coupling while meeting

both correctness and performance targets.

ˆ **Combinatorial Optimization** (19 tasks). These are open-ended, predominantly NP-hard problems where

exact methods are intractable and progress depends on designing, tuning, and iterating on heuristic

search strategies. Even strong solvers have room to improve with additional time and feedback.

ˆ **Professional Knowledge Work** (19 tasks). These tasks reproduce real white-collar deliverables across

nance, education, healthcare, and legal domains, matching work that would take a human professional

with three or more years of experience roughly three full days to complete. Many tasks feature carefully

designed rubrics and multi-round delivery feedback that approximate real client review cycles, so agents

can learn from structured critique and revise iteratively.

ˆ **Formal Math & Theorem Proving** (13 tasks). These tasks sit at the frontier of mathematical diculty

and require building large-scale machine-checked proofs in Lean, coupling deep mathematical insight

with substantial formal-verication engineering. Most are newly created for EdgeBench and designed

to support iterative progress: agents receive structured intermediate guidance and can extend partial

proofs incrementally.

ˆ **Interactive Games & Simulators** (8 tasks). These are real games designed for human players, where

procient humans typically invest tens of hours to master the mechanics. The state spaces are enormous

and each run is procedurally distinct, so agents face strong out-of-distribution pressure. Agents must

develop and rene strategies through high-frequency interaction across many episodes.

Tasks whose primary diculty lies in visual understanding, especially GUI operation, are excluded. When

success depends on the vision backbone rather than iterative reasoning, learning ability and perceptual

capability are hard to separate.

**2\.3**

**Feedback Loop and Evaluation Protocol**

Real world engineering and research workows rarely provide a single nal answer check. Instead, practi-

tioners iterate through **two complementary feedback loops** : a fast local loop for exploration, debugging,

and renement, and a slower external loop that provides authoritative calibration through deployment, peer

review, benchmark evaluation, or stakeholder feedback. The local loop enables rapid progress, while the

external loop guards against overtting to visible checks and exposes failures that are not captured by the

developer's own tests.

EdgeBench adopts this dual-loop structure to measure learning rather than endpoint success (Figure 3 ). The

inner loop is local and agent-driven: agents can inspect a writable workspace, run tests or simulators, observe

errors, and revise their artifacts. The outer loop is judge-mediated: submitted artifacts are evaluated against

hidden cases or private grading criteria, returning calibrated scores, verdicts, or diagnostics. Across task

families, this pattern is instantiated through dierent mechanisms: tests and prolers for software tasks,

development splits and validators for scientic tasks, local testers and hidden seeds for optimization tasks,

proof-checker states for theorem proving, episode scores for games, and rubrics for professional knowledge

work.

The protocol is implemented with an isolated workjudge evaluation harness. During a run, the agent works

inside a work container holding the task materials and local validation tools, but no hidden evaluation assets.

4

**OUTER LOOP · PER SUBMISSION**

**INNER LOOP · CONTINUOUS**

**Local Environment**

**Unlimited**

**Fast**

**Manipulable**

Compilers · linters · simulators

Docs · logs · train/val splits

**↻ iterate many times**

⚙

**Agent**

≥12 h budget

**Judger**

**Gated**

**Authoritative**

Hidden test scores

Rubric evaluations

Unseen-seed results

**run / query**

**results / errors**

**submit**

**score / feedback**

**← fast, self-driven, many rounds →**

**← slow, authoritative →**

**FFmpeg swscale reimplementation**

Systems & SE

Local: Rust compiler, verifier, FFmpeg

source

Judger: hidden workloads, PSNR gate,

speedup score

**Groundwater plume modeling**

Science & ML

Local: baseline solver, public well data, self-

split val

Judger: hidden concentrations, plume

metrics, monitoring utility

**Actuarial pricing**

Knowledge

Local: training data, tariff docs, validation

splits

Judger: hidden test data, expert labels,

rubric grader

**Transport Tycoon Sim**

Games

Local: game engine, local seed runs, API

docs

Judger: hidden seeds, 20-year avg

company value

**Figure 3** The informative feedback loop in EdgeBench. The inner loop (blue) lets agents iterate freely with local

feedback; the outer loop (orange) gates authoritative judge feedback behind submissions. Bottom: representative

tasks showing how both feedback channels are instantiated across capability families.

The agent can actively submit its current artifacts to a separate judge container, which runs the hidden

evaluation and returns the feedback specied by the task.

A host-side judge server mediates this outer

loop, including submission queues, cooldowns, authentication, and support for asynchronous grading on long-

running evaluations, allowing agents to continue working while submitted jobs are being judged. Appendix C

gives examples of task-design failure modes that motivated this isolation and submission-mediated design.

For trajectory measurement, the evaluation harness also performs host-side auto-evaluation at xed intervals.

These snapshots are scored through the hidden judge and recorded for analysis, but the results are not shown

to the agent. This lets EdgeBench measure improvement even between explicit submissions, while preserving

the distinction between agent-visible feedback and evaluator-only measurement.

**3**

**Scaling Laws of Learning from Real World Environments**

Pretraining scaling laws classically model language-model loss as a power-law function of training scale,

including the amount of pretraining data [ 32 , 36 ].

By contrast, benchmark performance is a task-level

readout of model capability, shaped by the diculty thresholds induced by tasks, examples, and scoring

criteria. Prior work has found that it is well described under pretraining scale-up by a log-sigmoid curve

[ 7 , 22 , 59 , 64 ].

Beyond learning from human-collected training data, modern agents such as GPT-5.5 and Claude Opus

4\.8 can continue to learn from their environments after deployment.

On a task, they can acquire new

information through interaction and improve their performance over time. Yet it remains unclear whether

this form of learning obeys any similarly simple scaling law. EdgeBench provides 134 diverse real world tasks

with executable environments, informative feedback, and at least 12-hour interaction windows, allowing us

to study how agents improve through interaction with their environments. Analyzing ve frontier agents

over roughly **38,000 hours of environment interaction** across 134 diverse real world tasks, we nd that **a**

**log-sigmoid curve fits environment learning performance precisely** . Thus, learning from the environment

and learning from pretraining data induce the same mathematical scaling form.

**3\.1**

**From Task Trajectories to Predictable Scaling Curves**

Experimental setting. We evaluate 134 EdgeBench tasks with ve frontier models: Claude Opus 4.8 [ 3 ], GPT-

5\.5 [ 58 ], GPT-5.4 [ 57 ], GLM-5.1 [ 26 , 84 ], and DeepSeek-V4-Pro (preview) [ 17 ]. For each taskmodel pair, we

run three independent 12-hour trials and record the full submission trajectory. GPT models are run with

Codex using a 256k compact window, while GLM-5.1 and DeepSeek-V4-Pro are run with Claude Code using

5

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**capecod\_plume\_reconstruction**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**battery\_soh\_rul\_anomaly**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

**borden\_source\_inversion**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

GLM 5.1

GPT 5.4

Claude Opus 4.8

DeepSeek V4 Pro

**quic\_transport\_stack**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

DeepSeek V4 Pro

GLM 5.1

**ffmpeg\_swscale\_reimplementation**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

GPT 5.5

GPT 5.4

**git\_rewrite\_in\_zig**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.5

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**symbolic\_integration\_engine**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

GLM 5.1

DeepSeek V4 Pro

Claude Opus 4.8

GPT 5.4

GPT 5.5

**order\_addition\_permutation\_optimization**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

Claude Opus 4.8

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

GPT 5.5

**sat\_solver**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.5

GLM 5.1

GPT 5.4

**portfolio\_risk\_calibration**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

GPT 5.5

DeepSeek V4 Pro

GPT 5.4

Claude Opus 4.8

GLM 5.1

**equity\_objection\_report**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

Performance

GLM 5.1

GPT 5.4

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.5

**cross\_border\_investment\_ppt**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**combinatorial\_games\_formalization**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

DeepSeek V4 Pro

GLM 5.1

**lean\_analysis\_proofs**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

Claude Opus 4.8

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

**ordinal\_notation\_well\_foundedness**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.5

GPT 5.4

GLM 5.1

**openttd\_transport\_ai**

0

2

4

6

8

10

12

elapsed time (hours)

0

5

10

15

20

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**dcss\_dungeon\_ai**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

GPT 5.5

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

**anchorhead\_text\_adventure**

**Figure 4** Learning curves over 12 hours for 18 representative tasks across six capability families. The remaining task

curves are provided in Figures 15  35 .

6

1h

2h

4h

6h

8h

12h

elapsed time (hours, log scale)

10

20

30

40

50

55

Performance

**Science / ML (39 tasks)**

model

Claude Opus 4.8

GPT 5.5

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

R²

0\.994

0\.995

0\.987

0\.989

0\.993

_S_ max

0\.59

0\.71

0\.41

0\.34

0\.38

_β_

0\.65

0\.35

0\.80

0\.95

0\.65

_t_ mid

1\.5h

3\.1h

1\.8h

0\.4h

1\.7h

1h

2h

4h

6h

8h

12h

elapsed time (hours, log scale)

20

30

40

50

60

70

75

**Systems SE (36 tasks)**

model

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

R²

0\.990

0\.997

0\.982

0\.987

0\.995

_S_ max

0\.67

0\.70

0\.68

0\.91

0\.45

_β_

1\.35

0\.80

0\.50

0\.30

1\.25

_t_ mid

0\.5h

0\.5h

0\.8h

4\.6h

0\.6h

1h

2h

4h

6h

8h

12h

elapsed time (hours, log scale)

10

20

30

40

50

55

**Knowledge Work (19 tasks)**

model

Claude Opus 4.8

GPT 5.5

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

R²

0\.996

0\.995

0\.996

0\.997

0\.993

_S_ max

0\.48

0\.54

0\.51

0\.41

0\.40

_β_

1\.40

0\.55

0\.85

1\.10

1\.10

_t_ mid

0\.9h

0\.4h

1\.3h

0\.7h

1\.0h

1h

2h

4h

6h

8h

12h

elapsed time (hours, log scale)

5

15

25

35

45

Performance

**Optimization (19 tasks)**

model

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

R²

0\.993

0\.998

0\.995

0\.989

0\.992

_S_ max

0\.68

0\.39

0\.39

0\.66

0\.25

_β_

0\.35

0\.40

0\.35

0\.35

0\.75

_t_ mid

6\.6h

0\.5h

0\.8h

42\.1h

1\.3h

1h

2h

4h

6h

8h

12h

elapsed time (hours, log scale)

0

10

20

30

40

50

60

65

**Formal Math (13 tasks)**

model

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

R²

0\.995

0\.997

0\.992

0\.972

0\.987

_S_ max

0\.59

0\.95

0\.97

1\.00

0\.15

_β_

1\.35

0\.65

0\.85

0\.55

1\.60

_t_ mid

2\.1h

10\.0h

17\.3h

119\.6h

2\.2h

1h

2h

4h

6h

8h

12h

elapsed time (hours, log scale)

0

10

20

30

40

45

**Games (8 tasks)**

model

Claude Opus 4.8

GPT 5.5

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

R²

0\.989

0\.991

0\.991

0\.977

0\.978

_S_ max

0\.40

0\.85

0\.47

0\.85

0\.19

_β_

1\.05

0\.45

0\.55

0\.25

1\.00

_t_ mid

0\.7h

17\.3h

3\.4h

240\.0h

2\.0h

**Log-Sigmoid Fit over 6 Task Families**

**Figure 5** Task-family-level log-sigmoid ts across the six EdgeBench task families. Despite large dierences in task

type and scoring function, the same log-time sigmoidal form ts the average trajectory in each task family well. ¹

200k compact windows. Claude Opus 4.8 is primarily run with a 1M Claude Code compact window; we

additionally include a 200k versus 1M Opus ablation in Section 5\.3 .

Per-task trajectory diversity. Figure 4 shows per-task learning curves for 18 representative tasks, illustrating

how dierent models improve on the same task over time. The full set of per-task curves is provided in

Appendix G.5 for all 134 tasks. The tasks span diverse domains and exhibit heterogeneous learning dynamics,

with trajectories ranging from smooth incremental gains to long plateaus, abrupt breakthroughs, and irregular

regressions.

Aggregate curves reveal a common structure. Although these individual curves are heterogeneous across both

tasks and models, their cross-task averages are unexpectedly smooth and share a common structure. Mo-

tivated by prior log-sigmoid ts of benchmark performance under pretraining scale-up, we t the averaged

environment learning curves with the following three-parameter log-sigmoid model:

_S_ ( _t_ ) =

_S_ max

1 + ( _t_ mid _/t_ ) _β_ _,_

(1)

where _t_ is elapsed interaction time and _S_ ( _t_ ) is best-so-far performance. The tted parameters serve as em-

pirical descriptors of the aggregate learning curve: _S_ max is the attainable score ceiling, _t_ mid is the interaction

time at which the curve reaches half of that ceiling, and _β_ controls how sharply progress concentrates in log

time. Thus a smaller _t_ mid means the model reaches the bulk of its attainable score sooner, while a larger

_β_ corresponds to a steeper learning transition. Section 3\.2 shows that this simple functional form ts the

empirical learning curves surprisingly well.

**3\.2**

**Log-Sigmoid Curves Fit Environment Learning with Remarkable Precision**

We nd that the log-sigmoid t is precise and robust across every setting we tested:

1 Fit precision improves as the number of tted tasks increases; see Figure 8 .

2 GPT-5.4 service availability dropped in the latter half of the experiment, which may partly explain its forecast deviation;

see Appendix B .

7

1h

2h

4h

8h

16h

28h

elapsed time (hours, log scale)

10

20

30

40

50

60

Performance

**Log-Sigmoid Fit for 28-Hour Learning over 80 Tasks**

model

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

R²

0\.998

0\.994

0\.993

0\.994

_S_ max

0\.52

0\.90

0\.49

0\.41

_β_

0\.95

0\.25

0\.55

0\.80

_t_ mid

1\.1h

14\.4h

2\.2h

1\.8h

1h

2h

4h

8h

16h

32h

72h

elapsed time (hours, log scale)

**Log-Sigmoid Fit for 72-Hour Learning over 18 Tasks**

model

GPT 5.5

GLM 5.1

R²

0\.996

0\.993

_S_ max

0\.69

0\.51

_β_

0\.65

0\.65

_t_ mid

4\.7h

6\.9h

**Figure 6** Long-horizon log-sigmoid ts beyond the main 12-hour benchmark

window. The left panel ts 28-hour trajectories averaged over 80 tasks; the

right panel ts 72-hour trajectories averaged over 18 tasks. All tted curves

remain highly precise, with _R_ ² _≥_ 0 _._ 993 .

1h

2h

4h

6h 6.5h

8h

10h

12h

elapsed time (hours)

10

20

30

40

50

60

Performance

**Forecasting 12h Performance from the First 6.5h**

fit window

held-out observations

sigmoid forecast

model

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

fit R²

0\.997

0\.998

0\.998

0\.997

0\.997

_S_ max

54\.3

58\.6

74\.0

52\.8

34\.2

_β_

0\.96

0\.56

0\.34

0\.52

0\.91

_t_ mid

0\.8h

0\.8h

6\.8h

2\.3h

1\.0h

held-out RMSE

0\.36

0\.20

0\.89

0\.54

0\.10

**Figure 7** Forecasting 12-hour perfor-

mance from the rst 6.5 hours. Log-

sigmoid ts on this early window accu-

rately predict the held-out remainder

for all ve models. ²

ˆ **Log-sigmoid curves precisely fit the 134-task average for all five models.** As shown in Figure 1 , after

averaging over all 134 tasks, the tted log-sigmoid curve closely tracks each model's 12-hour learning

trajectory. The t is uniformly tight across all ve models, with _R_ ² _≥_ 0 _._ 997 in every case.

ˆ **The same log-sigmoid form persists across heterogeneous task families.** Figure 5 repeats the t

separately across the six capability families in EdgeBench. These families require dierent knowledge,

exercise dierent capabilities, and produce visibly dierent aggregate learning curves. Yet each family

is still well described by the same log-sigmoid form, including smaller families where fewer tasks make

the averaged trajectories noisier.

ˆ **The fit remains precise under substantially longer interaction horizons.** Figure 6 extends the analysis

beyond the main 12-hour window to 28-hour and 72-hour interaction horizons. Due to resource limits,

the 28-hour t covers 80 tasks and four models, while the 72-hour t covers 18 tasks and two models.

The same log-sigmoid structure remains stable across both longer settings, with every tted curve

reaching _R_ ² _≥_ 0 _._ 993 .

ˆ **The log-sigmoid law exhibits predictive power.** Figure 7 tests this by tting each 12-hour aggregate

curve using only the rst 6.5 hours, then evaluates the forecast on held-out observations from 6.5 to 12

hours. The extrapolated curves remain close to the later observed trajectories across all ve models,

with _R_ ² _≥_ 0 _._ 997 and RMSE below 1.0 performance point in every case.

These precise ts raise two questions: is the log-sigmoid genuinely the right curve, or would any S-shape do,

and where does so clean a law come from?

Log-sigmoid ts best among common S-curves. Many saturating growth processes are S-shaped [ 77 ].

We

therefore compare the log-sigmoid against other common S-curves, each viewing an S-shaped learning curve

as a cumulative distribution over a time coordinate: log-probit [ 8 ], log-Gompertz [ 27 ], and a Weibull CDF [ 74 ]

on raw time, together with a two-parameter log-linear baseline; for the log-time families the independent

variable is _x_ = ln _t_ . We t every family on the 12h, 28h, and 72h full windows and pool the error. As Table 1

shows, the log-sigmoid family attains the lowest RMSE, while the log-linear baseline is substantially worse.

The empirical signal is thus robustly sigmoidal rather than tied to a single link function, and is not explained

by mere linear improvement in ln _t_ . Appendix E discusses why we nevertheless prefer the log-sigmoid on

mechanistic grounds.

The law emerges from a population of tasks. A single task's trajectory is noisy and idiosyncratic, yet Figure 8

shows that the log-sigmoid t becomes steadily more precise as we average over more tasks: the residual error

falls monotonically as tasks accumulate, from 1 task to all 134 . The clean scaling law is therefore an emergent,

population-level regularity, sharp only across many diverse tasks rather than within any one of them.

8

Family

Functional form

RMSE

**Log-Sigmoid**

_S_ ( _t_ ) =

_S_ max

1 + ( _t_ mid _/t_ ) _β_

**0\.390**

Log-Probit

_S_ ( _t_ ) = _S_ max Φ

 ln _t_ _−_ _µ_

_σ_



0\.398

Log-Gompertz

_S_ ( _t_ ) = _S_ max exp[ _−_ exp _{−_ _c_ (ln _t_ _−_ _x_ 0 ) _}_ ]

0\.402

Weibull CDF

_S_ ( _t_ ) = _S_ max



1 _−_ exp _{−_ ( _t/λ_ ) _β_ _}_



0\.404

Log-Linear

_S_ ( _t_ ) = _a_ \+ _b_ ln _t_

0\.717

**Table 1** Full-window t error for three-parameter S-curve families

and a two-parameter log-linear baseline.

RMSE is measured in

performance points on the 0100 score scale; lower is better.

0 5

20

40

60

80

100

120

134

tasks used for fitting

0\.3

0\.5

0\.7

0\.9

Mean Fit RMSE (1h-12h, 0-100 Score)

Log-Sigmoid Fit Error vs. Number of Tasks

**Figure 8**

Log-sigmoid t error decreases as

more tasks are averaged.

**3\.3**

**A Theory of the Log-Sigmoid Law**

The empirical ts show a robust log-sigmoid shape, but do not by themselves explain why this form should

appear. We propose a theoretical model: environment learning is a frontier expansion process on the under-

lying task graphs. In this view, each task is modeled by a latent graph of score units, the already-unlocked

units exert inuence on the locked neighbors to unlock them, and progress occurs when the frontier between

unlocked and locked score nodes advances. Appendix D gives the full derivation; here we summarize the

mechanism. Throughout the section, we use

_u_ = log _t_ _−_ log _t_ mid

as a change of coordinate of the time axis.

Environment learning is a frontier expansion process. For a single task, let us consider the task score is com-

posed of many score units, representing nodes _i_ on the task graph _G_ with score _w_ _i_ and normalized score

weights _µ_ _i_ = _w_ _i_ _/_ 

_i_ _w_ _i_ . Let _n_ _i_ ( _u_ ) _∈ {_ ⁰ _,_ ¹ _}_ indicate whether unit _i_ has been unlocked at time _u_ , the normal-

ized score obtained is

_x_ ( _u_ ) =



_i_

_µ_ _i_ _n_ _i_ ( _u_ ) _._

On the task graph _G_ , an edge weight _K_ _ij_ _≥_ 0 measures how much an unlocked source unit _j_ helps unlock a

target unit _i_ . Thus a locked unit _i_ receives an inuence eld

_h_ _i_ ( _u_ ) =



_j_

_K_ _ij_ _n_ _j_ ( _u_ ) _._

If locked units unlock randomly at an expected rate proportional to this eld, then conditioned on the current

state,

d

d _u_ E [ _x_ ( _u_ ) _|_ _n_ ( _u_ )] = _η_



_i_ _∈_ _L_ ( _u_ )



_j_ _∈_ _U_ ( _u_ )

_µ_ _i_ _K_ _ij_ _._

(2)

The expected score-growth rate is therefore exactly the weighted frontier cut from unlocked units _U_ ( _u_ ) to

locked units _L_ ( _u_ ) .

Frontier process moves at a speed proportional to _x_ (1 _−_ _x_ ) . The exact frontier cut still depends on the task

graph structure. The mean-eld approximation is to assume that, at the aggregate level, every macroscopic

unlockedlocked cut has approximately product-measure inuence:



_i_ _∈_ _L_



_j_ _∈_ _U_

_µ_ _i_ _K_ _ij_ _≈_ _κµ_ ( _L_ ) _µ_ ( _U_ ) _._

9

where _µ_ ( _A_ ) = 

_i_ _∈_ _A_ _µ_ _i_ for any set _A_ _⊆_ _G_ . This, along with ( ² ), gives

d _x_

d _u_ = _βx_ (1 _−_ _x_ ) _,_

_β_ = _ηκ._

(3)

The two factors have direct interpretations: unlocked score mass supplies reusable capability, while locked

score mass measures the remaining opportunity for improvement. Appendix D.2 formalizes this approxi-

mation using a weighted cut-mixing condition, which is weaker than assuming that all edge weights are

individually equal.

The eective time coordinate is logarithmic. The frontier equation is written in an eective task-graph coor-

dinate _u_ . A natural reason for _u_ to be approximately log _t_ is self-similar graph structure ³ . If each additive

increase in task diculty exposes a multiplicatively larger amount of relevant graph structure, then search

volume needed to traverse the graph grows exponentially with diculty scale. If the search eort is approxi-

mately constant across time horizon, then the diculty scale reached by time _t_ grows as

_u_ _∼_ log _t_

Substituting this coordinate into the frontier equation ( 3 ) gives

d _x_

d log _t_ = _βx_ (1 _−_ _x_ ) _._

(4)

Solving the frontier equation. Separating variables in ( 4 ) gives

log

_x_ ( _t_ )

1 _−_ _x_ ( _t_ ) = _β_ log

_t_

_t_ mid

_,_

where _t_ mid is chosen so that _x_ ( _t_ mid ) = 1 _/_ 2 . Hence

_x_ ( _t_ ) =

1

1 + ( _t_ mid _/t_ ) _β_ _,_

= _⇒_

_S_ ( _t_ ) =

_S_ max

1 + ( _t_ mid _/t_ ) _β_ _._

Benchmark average is smoother than individual tasks. The argument above describes the limiting frontier

drift. It does not imply that every nite task should visibly follow a smooth sigmoid. A task with a small

number of score units can have long plateaus and sudden jumps. The empirical scaling law is instead a

statement about the task-aggregate curve. If many independently evaluated tasks each follow approximate

frontier dynamics, then averaging removes nite-task jaggedness. The aggregate becomes a single log-sigmoid

when residual task midpoints and task speeds concentrate:

_x_ _M_ ( _u_ ) = ¹

_M_

_M_



_b_ =1

_x_ _b_ ( _u_ ) _≈_ ¹

_M_

_M_



_b_ =1

1

1 + _e_ _−_ _β_ _b_ ( _u_ _−_ _δ_ _b_ )

_P_

_−→_

1

1 + _e_ _−_ _βu_ _._

Appendix D.3 makes this statement precise under assumptions of blockwise cut-mixing, vanishing average

jump noise, midpoint alignment, and speed concentration.

Interpretation of the tted parameters. The tted rate _β_ has a natural interpretation as an eective frontier-

propagation speed in log time. A larger _β_ means that score unlocks over a narrower range of interaction scales,

producing a steeper transition from low to high performance. A smaller _β_ means that progress is spread

over more multiplicative time, producing a more gradual learning curve. The tted ceiling _S_ max should be

interpreted as the attainable score support over the tted regime, not necessarily as an absolute upper bound

on performance.

Applicability and limitations. The log-sigmoid law is not expected to hold for every environment-learning

process. It can fail when task graphs contain strong bottlenecks, dispersed task midpoints, heterogeneous

3 This resembles scale-free dynamics in physical complex systems, such as self-organized criticality and critical phenomena,

where behavior is not governed by a single characteristic scale [ 5 , 48 ].

10

2025-10

2025-11

2025-12

2026-01

2026-02

2026-03

2026-04

2026-05

2026-06

LLM release date

2

4

8

16

32

AI Learning Speed Across LLM Releases

Task-learning speed doubles approximately every 3 months

AI Learning Speed

Measured by performance gain after 2-hour learning

Rolling top-2 leaders

Other model

Fit to rolling top-2 leaders

**Figure 9** Learning speed across evaluated LLM releases. Learning speed denotes the two-hour performance gain on

the xed 18-task slice. The blue line ts the rolling top-2 leaders by release date and indicates an approximately

three-month doubling trend.

frontier speeds, or non-scale-free graph structures. These failure modes clarify the scope of the theory: the

log-sigmoid is most natural when progress behaves like a suciently mixed frontier expansion process on an

approximately fractal structured graph. In this sense, learning from environments tests whether an agent

can convert diverse feedback into reusable structure that accelerates subsequent discovery. We view this as

central to why environment learning is worth measuring and scaling.

**4**

**Agent Learning Speed Doubles Approximately Every Three Months**

Frontier agents can now improve through interaction with task environments. This raises a separate ques-

tion: are newer models learning from their environments faster? We measure this by comparing how much

performance each agent gains over a xed interaction budget across model release dates.

**4\.1**

**Experimental Design**

Disentangling prior knowledge from environment learning. A high score may reect what the model already

knew rather than what it learned during the run. To reduce this confound, we select an 18-task slice from

EdgeBench where models show similar rst-attempt performance. With comparable starting points, later

gains provide a cleaner measure of environment learning. We measure task-learning speed as the **average**

**performance gain** over a xed two-hour budget.

Evaluation protocol. We evaluate frontier open- and closed-source AI systems released from September 2025

through the current evaluation window, when frontier systems became capable of sustained autonomous runs.

Each model is run three times per task. GPT models are run with Codex; all other models are run with

Claude Code. As shown in Figure 10 (left), models start from comparable rst-attempt performance on this

18-task slice, with an average of 6 _._ 87 _±_ 0 _._ 97 .

11

GPT-5.1-Codex

GPT-5-Codex

GLM 5.0

DeepSeek V4 Pro

GPT-5.2-Codex

Claude Opus 4.5

GLM 5.1

GPT-5.4

GPT-5.3-Codex

Claude Opus 4.7

Claude Opus 4.6

Claude Opus 4.8

GPT-5.5

0

5

10

15

20

25

30

35

Performance

Initial vs. Best Performance

Initial attempt

Best after 2-hour learning

2025-09

2025-11

2026-01

2026-03

2026-05

10%

15%

20%

25%

30%

35%

Effective Submission Rate

2025-09

2025-11

2026-01

2026-03

2026-05

10

20

30

40

50

Average Number of Submissions per Task

**Figure 10** Learning outcomes and agent eort on the 18-task slice. Left: normalized initial performance and best

performance after two hours. Middle: fraction of submissions that improve the best-so-far score. Right: average

number of submissions per task. Error bars in the left panel show uncertainty over three replicate runs.

**Model**

**Overall Score** _↑_

**Category Score@12h** _↑_

@2h

@4h

@6h

@8h

@10h

**@12h**

Science

Code

Optimize

Knowledge

Math

Games

Opus 4.8

39\.0

45\.7

48\.1

49\.8

50\.9

51\.3

48\.5

67\.4

36\.5

47\.0

55\.0

39\.3

GPT-5.5

36\.8

42\.1

44\.5

46\.3

47\.6

48\.4

44\.3

65\.0

33\.6

45\.7

50\.0

39\.1

GPT-5.4

29\.7

34\.0

36\.5

38\.0

38\.9

39\.3

33\.5

54\.1

27\.9

38\.8

40\.8

29\.0

GLM-5.1

26\.0

30\.4

32\.9

34\.9

36\.5

37\.4

33\.8

50\.9

26\.4

43\.5

24\.6

29\.3

DS-V4-Pro

23\.3

27\.1

29\.0

29\.9

30\.9

31\.0

30\.0

43\.0

21\.5

37\.0

14\.1

16\.9

**Table 2** Aggregate leaderboard. Overall scores are reported at each time budget, while category scores are reported

at the 12-hour budget. Bold marks the best value in each score column and underlining marks the second-best value.

**4\.2**

**Learning Speed across Model Generations**

Figure 9 reports the two-hour evaluation results on the xed 18-task slice. The y-axis measures agent learning

speed, dened as performance gain over two hours, on a log scale. To estimate the frontier trend, we use

darker markers to highlight the top two models at each release date. We then t a linear trend to these

frontier points, with the tted 95% condence interval shown as the shaded band.

Figure 9 shows a rapid increase in learning speed across recent model generations. From GPT-5-Codex in

September 2025 to GPT-5.5 in April 2026, learning speed increases by roughly 8 _×_ over 221 days. A log-

linear t to the frontier models captures this trend well, corresponding to **an approximate doubling every**

**three months** . Figure 10 shows that this improvement is not simply explained by more frequent submissions.

Submission frequency (right panel) changes unevenly: newer GPT models submit more actively, while other

families do not. The middle panel tells a dierent story: later models turn a larger fraction of submissions

into best-so-far improvements. This trend therefore reects more eective learning from each interaction, not

merely more attempts.

**5**

**Analysis of Environment Learning Dynamics**

We study how frontier models perform and learn from environmental feedback over long horizons. We evaluate

ve frontier models: Claude Opus 4.8, GPT-5.5, GPT-5.4, GLM-5.1, and DeepSeek-V4-Pro (DS-V4-Pro).

This section contains four analyses. Section 5\.1 compares frontier models at the aggregate, family, task,

and submission levels. Section 5\.2 tests whether accumulated experience adds value beyond independent

restarts. Section 5\.3 examines whether longer context still improves long-horizon interaction. Section 5\.4

traces a single scientic task to show how an agent's improvements unfold. Appendix G.3 reports additional

harness-level continuation ablations for /goal mode and the Ralph loop.

12

**5\.1**

**Comparison across Frontier Models**

Setup. We follow Section 3\.1 and analyze 12-hour trajectories from two angles: **(1)** aggregate, family, and task

performance, and **(2)** submission eciency, i.e., how often submissions improve the current best result.

5

10

15

20

25

30

effective submission rate (%)

25

30

35

40

45

50

55

60

Performance

**Claude Opus 4.8**

**GPT-5.5**

**GPT-5.4**

**GLM-5.1**

**DS-V4-Pro**

model

Claude Opus 4.8

GPT-5.5

GPT-5.4

GLM-5.1

DeepSeek V4 Pro

total

submissions

20\.2k

34\.2k

17\.7k

11\.4k

26\.8k

effective

submissions

4\.3k

7\.1k

3\.9k

2\.0k

3\.3k

effective

rate

21\.3%

20\.7%

22\.2%

17\.4%

12\.5%

**Figure 11** 12-hour eective-submission rate versus nal

performance. Marker area shows total submissions; error

bars show task-level standard errors, and shading marks

above-average rate and performance.

Performance Comparison. Table 2 gives the aggre-

gate leaderboard over the 2 to 12 hour budget and

reports family-level means at 12 hours. Claude Opus

4\.8 leads throughout the time budget and reaches

51\.3 at 12 hours, followed by GPT-5.5 at 48.4. GPT-

5\.4 and GLM-5.1 form the next tier at 39.3 and

37\.4, while DS-V4-Pro obtains 31.0. Family-level re-

sults are broadly consistent with the aggregate rank-

ing: Claude Opus 4.8 leads each family mean, with

GPT-5.5 especially close in Games and second over-

all. Detailed per-task performance is reported in Ap-

pendix G.6 , with _∗_ marking cells based on fewer than

three valid runs.

Submission eciency. We count each agent submis-

sion and mark it as eective when it sets a new best-

so-far score.

Figure 11 compares each model's 12-

hour eective-submission rate with its nal perfor-

mance. Models that make more eective submissions

usually perform better, but more submissions do not automatically lead to a better nal result. **Claude Opus**

**4\.8 achieves the best final performance despite submitting less often than GPT-5.5** , and GPT-5.4 has the

highest eective-submission rate but still trails the top two models. Progress therefore depends not only

on how often an agent improves its score, but also on whether those improvements are large, reliable, and

reusable. Stronger agents use feedback more deliberately: they build a submit-ready baseline, preserve the

current best solution, make focused changes, and use feedback to keep gains or roll back failures. Weaker

agents more often over-trust local proxies, bundle unrelated edits, or continue broad exploration after feedback

has ruled out a direction, reducing sample eciency.

**5\.2**

**Agents Do Learn from Experience beyond Repeated Sampling**

Motivation. A rising best-so-far curve does not by itself prove that an agent is learning. Running longer also

gives more chances to stumble on a good solution: with enough independent tries, the best of them climbs by

luck alone. We therefore test whether the agent's accumulated experience adds value beyond such repeated

sampling under the same total time budget.

Setup. We give Opus 4.8 the same 12-hour budget on each of 17 tasks and compare two ways of spending

it, with versus without accumulated experience.

**With experience** : the agent runs once and continuously,

keeping its workspace, artifacts, and feedback history throughout, so experience builds up across the whole

run. **Without experience** : the same budget is split into _n_ = 6 independent attempts of _τ_ = 2 hours, with

all state discarded between attempts and only the best result kept, so each attempt starts from scratch

and any gain can come only from repeated sampling. Comparing the two at elapsed time _t_ = _kτ_ contrasts

one continuous run after _t_ hours against the best of _k_ independent attempts using the same total time.

Appendix G.1 details how each curve is estimated.

Result. Figure 12a shows a clear gain from experience: the with-experience curve stays above the without-

experience baseline under the same time budget. At 12 hours it reaches 43.0 versus 36.1, a gain of \+6 _._ 9 .

The improvement is therefore not explained by repeated sampling alone: accumulating and reusing task

experience drives progress beyond what independent restarts achieve.

13

2h

4h

6h

8h

10h

12h

time budget (hours)

25

30

35

40

45

Performance

w/ experience vs. w/o experience

setting

w/ experience

w/o experience

12h

43\.0

36\.1

\+6.9

1h

2h

4h

6h

8h

12h

elapsed time (hours, log scale)

20

30

40

50

60

Performance

Context Length: 200k vs. 1M

model

1M

200k

R²

0\.998

0\.998

_S_ max

97\.8

81\.5

_β_

0\.30

0\.40

_t_ mid

7\.1h

4\.8h

2h

6h

12h

w/o experience

26\.9

33\.2

36\.1

w/ experience

27\.2 \+0.4

37\.1 \+3.9

43\.0 \+6.9

2h

6h

12h

Opus 4.8 200k

33\.8

42\.6

48\.0

Opus 4.8 1M

39\.6 \+5.8

48\.0 \+5.5

52\.5 \+4.4

**Figure 12 Left:** Gain from accumulated experience for Opus 4.8: the w/ experience run minus the w/o experience

baseline (independent restarts) under the same total time budget. **Right:** Context-length ablation: 200k vs. 1M on

Opus 4.8. Each curve shows the average performance over time; dashed lines are log-sigmoid ts.

**5\.3**

**How Much Does a Longer Context Improve Performance**

Motivation. Section 5\.2 shows that accumulated experience can improve performance. A remaining question

is how this experience should be retained during a long run. Using long context is a natural way to do so.

However, frontier-agent harnesses can also maintain state outside the model context through workspace les,

compaction, progress notes, and memory-like artifacts. It is therefore unclear whether extending the context

window still provides additional benets once these external state channels are available, and if so, by how

much.

Setup. We compare 200k-context Opus 4.8 with 1M-context Opus 4.8 on the 42-task subset under the same

long-horizon evaluation protocol.

Result. A longer context yields a consistent multi-point gain throughout the 12-hour window (Figure 12b ).

The 1M-context Opus 4.8 stays above the 200k variant at every checkpoint, and the two trajectories run

roughly parallel: the gap is \+5 _._ 8 at 2h and only edges down to \+4 _._ 4 by 12h, with both curves well described

by the same log-sigmoid form. Thus, even with identical external workspace and harness state, a longer

context window gives a stable advantage over the horizon, with at most a slight tendency to narrow.

**5\.4**

**Case Study**

Setup. We examine the gravitational-wave reconstruction task.

Based on the rst GW150914 detection

paper [ 1 ], the agent must recreate the published signal analysis from LIGO strain data. The target has

three output groups: H1/L1 waveforms, H1/L1 spectrograms, and velocity/separation curves for the source

dynamics. The judge weights the ve component scores at 0.15 for each waveform, 0.20 for each spectrogram,

and 0.30 for velocity/separation.

We run a Codex agent with periodic auto-evaluation, auto-resume, no

Internet access, a 30-minute evaluation interval, and a 120-second submission cooldown. The agent made 224

explicit submissions, the harness added 23 auto-evaluations, and the run timed out at the 12-hour budget.

**The trajectory reveals a sparse but structured diagnose-edit-evaluate loop.** The loop is sparse because most

submissions are exploratory probes: only 27 of 224 agent submissions improve the best-so-far score by at

least 0.1 percentage points. It is structured because feedback repeatedly changes what the agent searches for.

The agent rst makes the task measurable, then breaks unresolved errors into smaller searches, then identies

a main bottleneck and keeps searching around it, and nally keeps a working solution while repairing the

14

0

2

4

6

8

10

12

elapsed time (hours)

40

50

60

67

70

Performance

best learned behavior

best-so-far envelope

1\. The agent learned that raw strain

can be organized into a

detector-frame waveform. (score 42.8)

2\. The agent discovered the rising chirp

as a stable trajectory in

time-frequency space. (+4.3 pp)

3\. The agent digitized the reference traces,

turning published figures into

direct fitting targets. (+3.2 pp)

4\. The agent learned merger time as

the hidden anchor aligning

both detectors. (+1.3 pp)

5\. The agent grounded the chirp in

compact two-body source

dynamics. (+7.9 pp)

6\. The agent phase-locked the reconstruction

through arrival-time and

frequency-curvature alignment. (+5.5 pp)

7\. The agent composed waveform, spectrogram,

residuals, and source dynamics

into one coherent event. (+2.1 pp)

Gravitational Wave: reconstruct a gravitational-wave signal from LIGO strain with

waveform, spectrogram, and source dynamics.

**Figure 13** Gravitational-wave reconstruction task case study. The trajectory shows how a GPT-5.5 agent improves

over a 12-hour run, with numbered milestones marking representative best-so-far updates.

remaining errors. These patterns show how many failed trials can still produce a small number of cumulative

improvements.

ˆ **The agent first makes the problem measurable before making it better.** The rst valid submission turns

an underspecied analysis task into a scoreable pipeline, but feedback exposes weak source dynamics.

The agent then spends the rst 11 submissions stabilizing the pipeline and replacing a noisy frequency

estimate, producing three meaningful updates and a +4.5 pp gain.

ˆ **When direct repair stalls, the agent decomposes the failure into searchable subproblems.** Instead

of treating waveform mismatch as one opaque error, the agent separates reference anchoring, time-

frequency localization, and detector alignment. Across 40 signal-search submissions, this decomposition

yields seven meaningful updates and lifts the best score to 52.3.

ˆ **Identifying a main bottleneck lets the agent keep searching productively.** After broad signal-processing

edits plateau, component feedback identies velocity/separation as the dominant gap. The agent keeps

searching within source-mass calibration rather than rewriting the whole pipeline; in the 45h window,

17 submissions and ve useful updates raise source dynamics from 64.2 to 89.0, creating the largest

jump in the run.

ˆ **After finding a stable solution, the agent keeps the core and repairs only the remaining errors.**

In the nal hours, most residual edits fail to transfer. Instead of restarting the pipeline, the agent

keeps the source model xed and tests targeted residual corrections, phase alignment, and narrow-band

corrections. These useful updates raise the H1 waveform component score from roughly 47 to 95, while

the aggregate best score reaches 67.0.

**The run improves through uneven jumps rather than a smooth climb.** Across 247 scored evaluations, the

best score rises from 42.8 to 67.0 on the 0100 scale. Figure 13 shows seven representative milestones. These

jumps correspond to the behavior patterns above: the agent rst makes the task scoreable, then localizes the

signal, improves source dynamics, and nally repairs the remaining H1 waveform errors. Detailed milestone

phases and nal subscore composition are reported in Appendix G.2 .

15

**6**

**Related Work**

Benchmark

\# Tasks

Horizon

Scenario

Self-evolution

MMLU [ 29 ]

15,908

Short

Knowledge QA

No

AIME [ 45 ]

30

Short

HS math competition

No

GDPval Gold [ 60 ]

220

Short

Professional deliverables

No

SWE-bench veried [ 35 , 51 ]

500

Short

Issue repair

No

Terminal-Bench 2.0 [ 46 ]

89

Short

Terminal workows

No

Continual Learning Bench [ 4 ]

6

Short

Controlled task sequences

Yes

CL-bench [ 21 ]

1,899

Short

Context learning

No

FrontierCode [ 41 ]

150

N/A

Production code changes

No

NL2Repo-Bench [ 18 ]

104

Medium

Repo generation

No

Agents' Last Exam [ 69 ]

152

public

Medium

Computer-use work

No

MLE-bench [ 10 ]

75

Long

ML engineering

Yes

MLS-Bench [ 42 ]

140

Long

ML research

Subset

Frontier-Eng [ 14 ]

47

Long

Engineering design

No

Frontier-CS [ 43 ]

156

Long

Open-ended CS tasks

No

AutoLab [ 81 ]

36

Long

Research/engineering optimization

No

FrontierSWE [ 15 ]

17

Long

SWE/performance tuning

No

**EdgeBench (ours)**

134

Ultra-long

SWE, science/ML, professional work,

optimization, formal proving, games

Yes

**Table 3**

**Comparison with representative benchmarks.**

Horizon describes the expected single-instance task

contract rather than total suite runtime. A benchmark is counted as measuring self-evolution only when performance

is explicitly plotted against a resource axis such as time or sample count.

**Existing benchmarks cover major parts of agent capability but rarely measure how an agent improves within**

**a run.** Closed-form QA, math, and coding benchmarks such as MMLU [ 29 ], AIME [ 45 ], and HumanEval [ 11 ],

together with endpoint patch benchmarks such as SWE-bench [ 35 ], evaluate nal answers or nal patches.

More agentic and work-oriented benchmarks, including GDPval [ 60 ], Agents' Last Exam [ 69 ], and Frontier-

Code [ 41 ], broaden the task interface to professional deliverables, computer-use workows, or production

code changes. Their central reported quantities, however, remain end-state measures: task success, artifact

quality, pass rate, or readiness for production. EdgeBench instead measures the improvement trajectory over

time.

**Some benchmarks study learning, but they focus on restricted domains and shorter horizons.** CL-bench [ 21 ],

EvaLearn [ 19 ], and Continual Learning Bench [ 4 ] evaluate whether models improve from a static context or

static information streams whose content is not primarily shaped by the agent's actions within a single task.

Iterative optimization benchmarks such as MLE-bench [ 10 ], MLS-Bench [ 42 ], Frontier-Eng [ 14 ], Frontier-

CS [ 43 ], and ALE-Bench [ 34 ] further include repeated attempts, empirical feedback, or visible metrics. The

closest long-horizon agentic comparators are AutoLab [ 81 ] and FrontierSWE [ 15 ]: both evaluate agents that

repeatedly edit executable artifacts and incorporate feedback. EdgeBench diers by covering a broader range

of executable domains, using a day-scale task contract, and applying the same trajectory metrics consistently

across all tasks.

**Scaling laws have been widely studied in prior work, but learning from diverse real-world environments**

**remains underexplored.** Classical scaling laws study pretraining, relating loss or benchmark performance to

model size, data, and compute [ 32 , 36 ]; later work studies bounded benchmark performance curves as model

scale increases [ 7 , 59 , 64 , 85 ]. Test-time scaling laws have also been studied across several inference-time

methods: plain repeated sampling [ 9 , 11 , 40 ], search, revision, or verier-guided compute allocation [ 67 , 79 ],

and long-chain-of-thought inference in reasoning models [ 16 , 50 ]. Agentic test-time scaling has been observed

in computer-use and browsing agents [ 52 , 72 ], studied through interaction-length scaling [ 65 ], and revisited

through long-horizon human-agent comparisons [ 44 ]. These studies are closer to our setting but cover narrower

domains or fewer tasks and do not establish a cross-domain scaling law. Reinforcement-learning scaling is

also relevant because it studies learning from environment feedback [ 31 , 37 ], while EdgeBench measures

16

elapsed interaction time in deployed agent trajectories. In-context learning from task feedback is relatively

inexpensive to evaluate repeatedly across many executable environments, while large reinforcement-learning

runs are costly and typically cover fewer environments. This broader environment coverage may explain why

the aggregate curves are stable enough to reveal a scaling law.

A more detailed benchmark-by-benchmark discussion is provided in Appendix F .

**7**

**Conclusion**

This paper introduced EdgeBench, a benchmark for studying how agents learn from real-world environments

over day-long horizons. Across 134 diverse executable tasks and roughly 38,000 hours of environment inter-

action, we nd that aggregate learning trajectories follow a precise log-sigmoid relationship with interaction

time. The same form appears across task families, remains stable over longer horizons, and supports forecast-

ing later performance from early trajectories. We also nd that agent learning speed has improved rapidly

across recent frontier model generations.

These results suggest that learning from environments is not merely a collection of idiosyncratic task out-

comes, but a measurable scaling object.

Unlike many aggregate capability curves, environment-learning

trajectories expose the intermediate attempts, feedback, and revisions through which progress occurs. This

makes EdgeBench useful not only for ranking agents, but for studying how agents acquire and reuse experi-

ence. More broadly, the regularity we observe suggests that post-deployment learning from rich environments

may deserve the same systematic scaling attention that pretraining has received.

17

**Author Contributions**

**Core Contributors**

Deyao Zhu \*

Xin Zhou \*

Shengling Qin \*

Xuekai Zhu \*

Hangliang Ding \*

Shu Zhong \* „

**Theory**

Zixin Wen

**Data Collection and Curation**

Zhonglin Xie

Chenhui Gou

Linxuan Ren

Yueyang Wang

Junfeng Zhong

Rui Liu

Tian Gao

Yangguang Lin

Jingyuan Zhang

Maojia Song

Xuan Qi _‡_

Jinhong Wu _‡_

Chenyang Zhang _‡_

Yinzhu Piao

Ziru Niu

Hongbin Lin

Lingxiang Meng

Pengtang Tang

Chengyao Tang

Shanyu Wu

Huanyu Zheng

Yu Liu

Liya Zhu

He Wang

Ming Ding

**Data Infrastructure**

Ziyu Wan

Hao Liu

Sibo Wang

Haotian Zhu

Xintian Zhang

Nan Chai

Yipeng Liu

Panhao Lai

**Referrals**

Sihang Yuan

Zixin Su

Ge Zhang

Wangchunshu Zhou

Yantao Du

**Advisors**

Wenhao Huang

Guang Shi

\* Equal contribution

„ Project Lead

_‡_ External contributor

18

**References**

[1] B. P. Abbott et al. Observation of gravitational waves from a binary black hole merger. Physical Review Letters ,

116(6):061102, 2016. doi: 10.1103/PhysRevLett.116.061102.

[2] Anthropic.

The

Claude

Model

Family.

https://www-cdn.anthropic.com/

de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model\_Card\_Claude\_3.5\_Addendum.pdf , 2024.

[3] Anthropic.

Claude

Opus

4\.8

System

Card.

https://www-cdn.anthropic.com/

0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf , May 2026.

System card. Released May 28, 2026; up-

dated June 3, 2026.

[4] Parth Asawa, Christopher M. Glaze, Gabriel Orlanski, Ramya Ramakrishnan, Benji Xu, et al. Continual learning

bench: Evaluating frontier AI systems in real-world stateful environments. arXiv preprint arXiv:2606.05661 , 2026.

[5] Per Bak, Chao Tang, and Kurt Wiesenfeld. Self-organized criticality: An explanation of 1/f noise. Physical

Review Letters , 59(4):381384, 1987.

[6] Joseph Berkson. Application of the logistic function to bio-assay. Journal of the American Statistical Association ,

39(227):357365, 1944. doi: 10.1080/01621459.1944.10500699.

[7] Akshita Bhagia, Jiacheng Liu, Alexander Wettig, David Heineman, Oyvind Tafjord, Ananya Harsh Jha, Luca

Soldaini, Noah A. Smith, Dirk Groeneveld, Pang Wei Koh, Jesse Dodge, and Hannaneh Hajishirzi. Establishing

task scaling laws via compute-ecient model ladders. arXiv preprint arXiv:2412.04403 , 2024.

[8] Chester I. Bliss. The method of probits. Science , 79(2037):3839, 1934.

[9] Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V. Le, Christopher Ré, and Azalia

Mirhoseini.

Large language monkeys:

Scaling inference compute with repeated sampling.

arXiv preprint

arXiv:2407.21787 , 2024.

[10] Jun Shern Chan, Neil Chowdhury, Oliver Jae, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin

Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, and Aleksander M¡dry. MLE-bench: Evaluating machine

learning agents on machine learning engineering. In The Thirteenth International Conference on Learning Rep-

resentations , 2025.

[11] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri

Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large language models trained on code.

arXiv preprint arXiv:2107.03374 , 2021.

[12] Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen Wei,

Zitong Lu, et al. ScienceAgentBench: Toward rigorous assessment of language agents for data-driven scientic

discovery. In International Conference on Learning Representations , 2025.

[13] Ching-An Cheng, Andrey Kolobov, Dipendra Misra, Allen Nie, and Adith Swaminathan. LLF-bench: Benchmark

for interactive learning from language feedback. arXiv preprint arXiv:2312.06853 , 2023.

[14] Yizhe Chi, Deyao Hong, Dapeng Jiang, Tianwei Luo, Kaisen Yang, Boshi Zhang, et al. Frontier-Eng: Bench-

marking self-evolving agents on real-world engineering tasks with generative optimization.

arXiv preprint

arXiv:2604.12290 , 2026.

[15] Evan Chu, Rajan Agarwal, Abishek Thangamuthu, Brendan Graham, and Justus Mattern. FrontierSWE: Bench-

marking coding agents at the limits of human abilities. https://www.frontierswe.com/blog , 2026.

[16] DeepSeek-AI.

DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning.

arXiv

preprint arXiv:2501.12948 , 2025.

[17] DeepSeek-AI. DeepSeek-V4: Towards highly ecient million-token context intelligence. https://huggingface.

co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek\_V4.pdf , April 2026. Technical report.

[18] Jingzhe Ding, Shengda Long, Changxin Pu, et al. NL2Repo-Bench: Towards long-horizon repository generation

evaluation of coding agents. arXiv preprint arXiv:2512.12730 , 2025.

[19] Shihan Dou, Ming Zhang, Chenhao Huang, Jiayi Chen, Feng Chen, Shichun Liu, Yan Liu, Chenxiao Liu, Cheng

Zhong, Zongzhang Zhang, et al.

EvaLearn: Quantifying the learning capability and eciency of LLMs via

sequential problem solving. arXiv preprint arXiv:2506.02672 , 2025.

19

[20] Shihan Dou, Yujiong Shen, Chenhao Huang, Junjie Ye, Jiayi Chen, Junzhe Wang, Qianyu He, Shichun Liu,

Changze Lv, Jiahang Lin, et al.

CL-bench Life: Can language models learn from real-life context?

arXiv

preprint arXiv:2604.27043 , 2026.

[21] Shihan Dou, Ming Zhang, Zhangyue Yin, Chenhao Huang, Yujiong Shen, Junzhe Wang, Jiayi Chen, Yuchen Ni,

Junjie Ye, Cheng Zhang, et al. CL-bench: A benchmark for context learning. arXiv preprint arXiv:2602.03587 ,

2026\.

[22] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,

Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al.

The Llama 3 herd of models.

arXiv preprint

arXiv:2407.21783 , 2024.

[23] Darius A. Faroughy, Soa Palacios Schweitzer, Ian Pang, Siddharth Mishra-Sharma, and David Shih. Collider-

Bench: Benchmarking AI agents with particle physics analysis reproduction. arXiv preprint arXiv:2605.13950 ,

2026\.

[24] Gemini Team. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv

preprint arXiv:2403.05530 , 2024.

[25] Gemini Team. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next

generation agentic capabilities. arXiv preprint arXiv:2507.06261 , 2025.

[26] GLM-5 Team. GLM-5: from vibe coding to agentic engineering. https://arxiv.org/abs/2602.15763 , 2026.

[27] Benjamin Gompertz. On the nature of the function expressive of the law of human mortality, and on a new mode

of determining the value of life contingencies. Philosophical Transactions of the Royal Society of London , 115:

513583, 1825.

[28] Harry F. Harlow. The formation of learning sets. Psychological Review , 56(1):5165, 1949. doi: 10.1037/h0062474.

[29] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt.

Measuring massive multitask language understanding. In International Conference on Learning Representations ,

2021\.

[30] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob

Steinhardt. Measuring mathematical problem solving with the MATH dataset. In Advances in Neural Information

Processing Systems , 2021.

[31] Jacob Hilton, Jie Tang, and John Schulman. Scaling laws for single-agent reinforcement learning. arXiv preprint

arXiv:2301.13442 , 2023.

[32] Jordan Homann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego

de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language

models. arXiv preprint arXiv:2203.15556 , 2022.

[33] Georey Huntley. Everything Is a Ralph Loop. https://ghuntley.com/loop/ , January 2026. Blog post, January

17, 2026.

[34] Yuki Imajuku, Kohki Horie, Yoichi Iwata, Kensho Aoki, Naohiro Takahashi, and Takuya Akiba. ALE-bench: A

benchmark for long-horizon objective-driven algorithm engineering. arXiv preprint arXiv:2506.09050 , 2025.

[35] Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Or Press, and Karthik R. Narasimhan.

SWE-bench: Can language models resolve real-world GitHub issues? In The Twelfth International Conference

on Learning Representations , 2024.

[36] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray,

Alec Radford, Jerey Wu, and Dario Amodei.

Scaling laws for neural language models.

arXiv preprint

arXiv:2001.08361 , 2020.

[37] Devvrit Khatri, Lovish Madaan, Rishabh Tiwari, Rachit Bansal, Sai Surya Duvvuri, Manzil Zaheer, Inderjit S.

Dhillon, David Brandfonbrener, and Rishabh Agarwal. The art of scaling reinforcement learning compute for

LLMs. arXiv preprint arXiv:2510.13786 , 2025.

[38] Thomas Kwa, Ben West, Joel Becker, Amy Deng, Katharyn Garcia, Max Hasin, Sami Jawhar, Megan Kinniment,

Nate Rush, Sydney Von Arx, et al. Measuring AI ability to complete long tasks. arXiv preprint arXiv:2503.14499 ,

2025\.

20

[39] Nathaniel Leibowitz, Barak Baum, Giora Enden, and Amir Karniel. The exponential learning equation as a

function of successful trials results in sigmoid performance. Journal of Mathematical Psychology , 54(3):338340,

2010\. doi: 10.1016/j.jmp.2010.01.006.

[40] Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James

Keeling, Felix Gimeno, Agustin Dal Lago, Thomas Hubert, Peter Choy, Cyprien de Masson d'Autume, Igor

Babuschkin, Xinyun Chen, Po-Sen Huang, Johannes Welbl, Sven Gowal, Alexey Cherepanov, James Molloy,

Daniel J. Mankowitz, Esme Sutherland Robson, Pushmeet Kohli, Nando de Freitas, Koray Kavukcuoglu, and

Oriol Vinyals. Competition-level code generation with AlphaCode. arXiv preprint arXiv:2203.07814 , 2022.

[41] Eric Lu, Ben Pan, Deniz Birlikci, Sam Lee, Ray Wang, Rohan Choudhury, Fermi Ma, TC Qin, Carlo Baronio,

Silas Alberti, et al. Introducing FrontierCode. https://cognition.ai/blog/frontier-code , 2026.

[42] Bohan Lyu, Yucheng Yang, Siqiao Huang, Jiaru Zhang, Qixin Xu, Xinghan Li, Xinyang Han, Yicheng Zhang,

Huaqing Zhang, Runhan Huang, et al. MLS-Bench: A holistic and rigorous assessment of AI systems on building

better AI. arXiv preprint arXiv:2605.08678 , 2026.

[43] Qiuyang Mang, Wenhao Chai, Zhifei Li, Huanzhi Mao, Shang Zhou, Alexander Du, Hanchen Li, Shu Liu,

Edwin Chen, Yichuan Wang, et al. FrontierCS: Evolving challenges for evolving intelligence. arXiv preprint

arXiv:2512.15699 , 2025.

[44] Qiuyang Mang, Kaiyuan Liu, Bo Peng, Shreyas Pimpalgaonkar, Alex Dimakis, and Alvin Cheung. Humans still

beat AI in the long horizon: Revisiting test-time scaling in the agent era. https://joyemang33.github.io/blog/

2026/humans-dont-just-sample/ , 2026.

[45] Mathematical Association of America.

MAA invitational competitions: American invitational mathematics

examination (AIME). https://maa.org/maa-invitational-competitions/ , 2026.

[46] Mike A. Merrill, Alexander G. Shaw, Nicholas Carlini, Boxuan Li, Harsh Raj, Ivan Bercovich, et al. Terminal-

Bench: Benchmarking agents on hard, realistic tasks in command line interfaces. In The Fourteenth International

Conference on Learning Representations , 2026.

[47] Jaap M. J. Murre. S-shaped learning curves. Psychonomic Bulletin & Review , 21(2):344356, 2014. doi: 10.3758/

s13423-013-0522-0.

[48] Mark E. J. Newman. Power laws, pareto distributions and zipf's law. Contemporary Physics , 46(5):323351,

2005\.

[49] OpenAI. GPT-4 technical report. arXiv preprint arXiv:2303.08774 , 2023.

[50] OpenAI. Learning to reason with LLMs. https://openai.com/index/learning-to-reason-with-llms/ , 2024.

[51] OpenAI.

Introducing SWE-bench veried.

https://openai.com/index/introducing-swe-bench-verified/ ,

2024\.

[52] OpenAI. Computer-using agent. https://openai.com/index/computer-using-agent/ , 2025.

[53] OpenAI. GPT-4.5 System Card. https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf , 2025.

[54] OpenAI.

Update

to

GPT-5

System

Card:

GPT-5.2.

https://cdn.openai.com/pdf/

3a4153c8-c748-4b71-8e31-aecbde944f8d/oai\_5\_2\_system-card.pdf , 2025.

[55] OpenAI. GPT-5 System Card. arXiv preprint arXiv:2601.03267 , 2025.

[56] OpenAI. Follow a Goal. https://developers.openai.com/codex/use-cases/follow-goals , 2026. Codex doc-

umentation. Accessed June 18, 2026.

[57] OpenAI.

GPT-5.4 Thinking System Card.

https://deploymentsafety.openai.com/gpt-5-4-thinking/

gpt-5-4-thinking.pdf , March 2026. System card. Published March 5, 2026.

[58] OpenAI. GPT-5.5 System Card. https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf , April 2026.

System card. Published April 23, 2026.

[59] David Owen. How predictable is language model benchmark performance?

arXiv preprint arXiv:2401.04757 ,

2024\.

21

[60] Tejal Patwardhan, Rachel Dias, Elizabeth Proehl, Grace Kim, Michele Wang, Olivia Watkins, Simon Posada Fish-

man, Marwan Aljubeh, Phoebe Thacker, Laurance Fauconnet, et al. GDPval: Evaluating AI model performance

on real-world economically valuable tasks. arXiv preprint arXiv:2510.04374 , 2025.

[61] Shi Qiu, Junyi Deng, Yiwei Deng, Haoran Dong, Jieyu Fu, Mao Li, Zeyu Li, Zhaolong Zhang, Huiwen Zheng, Lei-

dong Bao, et al. PRBench: End-to-end paper reproduction in physics research. arXiv preprint arXiv:2603.27646 ,

2026\.

[62] David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian

Michael, and Samuel R. Bowman.

GPQA: A graduate-level google-proof Q&A benchmark.

arXiv preprint

arXiv:2311.12022 , 2023.

[63] David Rein, Joel Becker, Amy Deng, Seraphina Nix, Chris Canal, Daniel O'Connel, Pip Arnott, Ryan Bloom,

Thomas Broadley, et al. HCAST: Human-calibrated autonomy software tasks. arXiv preprint arXiv:2503.17354 ,

2025\.

[64] Yangjun Ruan, Chris J. Maddison, and Tatsunori Hashimoto. Observational scaling laws and the predictability

of language model performance. arXiv preprint arXiv:2405.10938 , 2024.

[65] Junhong Shen, Hao Bai, Lunjun Zhang, Yifei Zhou, Amrith Setlur, Shengbang Tong, Diego Caples, Nan Jiang,

Tong Zhang, Ameet Talwalkar, and Aviral Kumar. Thinking vs. doing: Agents that reason by scaling test-time

interaction. arXiv preprint arXiv:2506.07976 , 2025.

[66] Zachary S. Siegel, Sayash Kapoor, Nitya Nadgir, Benedikt Stroebl, and Arvind Narayanan. CORE-bench: Fos-

tering the credibility of published research through a computational reproducibility agent benchmark. arXiv

preprint arXiv:2409.11363 , 2024.

[67] Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling LLM test-time compute optimally can be

more eective than scaling model parameters. arXiv preprint arXiv:2408.03314 , 2024.

[68] Giulio Starace, Oliver Jae, Dane Sherburn, James Aung, Jun Shern Chan, Leon Maksin, Rachel Dias, Evan Mays,

Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, and Tejal Patwardhan. PaperBench:

Evaluating AI's ability to replicate AI research. In Proceedings of the 42nd International Conference on Machine

Learning , volume 267 of Proceedings of Machine Learning Research , pages 5684356873. PMLR, 2025.

[69] Yiyou Sun, Xinyang Han, Weichen Zhang, Yuanbo Pang, Tianyu Wang, et al. Agents' last exam. arXiv preprint

arXiv:2606.05405 , 2026.

[70] Minh V. T. Thai, Tue Le, Dung Nguyen Manh, Huy Phan Nhat, and Nghi D. Q. Bui. SWE-EVO: Benchmarking

coding agents in long-horizon software evolution scenarios. arXiv preprint arXiv:2512.18470 , 2025.

[71] Louis Leon Thurstone. The Learning Curve Equation . Psychological Review Company, Princeton, NJ, 1919.

[72] Jason Wei, Zhiqing Sun, Spencer Papay, Scott McKinney, Jerey Han, Isa Fulford, Hyung Won Chung,

Alex Tachard Passos, William Fedus, and Amelia Glaese. BrowseComp: A simple yet challenging benchmark for

browsing agents. arXiv preprint arXiv:2504.12516 , 2025.

[73] Tianxin Wei, Noveen Sachdeva, Benjamin Coleman, Zhankui He, Yuanchen Bei, Xuying Ning, Mengting Ai,

Yunzhe Li, Jingrui He, Ed H. Chi, et al.

Evo-Memory: Benchmarking LLM agent test-time learning with

self-evolving memory. arXiv preprint arXiv:2511.20857 , 2025.

[74] Waloddi Weibull. A statistical distribution function of wide applicability. Journal of Applied Mechanics , 18(3):

293297, 1951.

[75] Pierre Weiss. L'hypothèse du champ moléculaire et la propriété ferromagnétique. Journal de Physique Théorique

et Appliquée , 6(1):661690, 1907.

[76] Hjalmar Wijk, Tao Lin, Joel Becker, Sami Jawhar, Neev Parikh, Thomas Broadley, Lawrence Chan, Michael

Chen, Josh Clymer, Jai Dhyani, et al. RE-bench: Evaluating frontier AI R&D capabilities of language model

agents against human experts. In Proceedings of the 42nd International Conference on Machine Learning , 2025.

[77] Wikipedia contributors. Sigmoid function. https://en.wikipedia.org/wiki/Sigmoid\_function , 2025.

[78] Cheng-Kuang Wu, Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, and Hung yi Lee. StreamBench: Towards

benchmarking continuous improvement of language agents. In Advances in Neural Information Processing Sys-

tems , 2024.

22

[79] Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. Inference scaling laws: An empirical

analysis of compute-optimal inference for problem-solving with language models. arXiv preprint arXiv:2408.00724 ,

2024\.

[80] Xinbo Xu, Ruihan Yang, Haiyang Shen, et al. RoadmapBench: Evaluating long-horizon agentic software devel-

opment across version upgrades. arXiv preprint arXiv:2605.15846 , 2026.

[81] Zhangchen Xu, Junda Chen, Yue Huang, Dongfu Jiang, Jiefeng Chen, Hang Hua, Zijian Wu, Zheyuan Liu, Zexue

He, Lichi Li, et al. AutoLab: Can frontier models solve long-horizon auto research and engineering tasks? arXiv

preprint arXiv:2606.05080 , 2026.

[82] John Yang, Kilian Lieret, Jerey Ma, Parth Thakkar, Dmitrii Pedchenko, Sten Sootla, Emily McMilin, Pengcheng

Yin, Rui Hou, Gabriel Synnaeve, Diyi Yang, and Or Press.

ProgramBench: Can language models rebuild

programs from scratch? arXiv preprint arXiv:2605.03546 , 2026.

[83] Christine Ye, Sihan Yuan, Suchetha Cooray, Steven Dillmann, Ian L. V. Roque, Dalya Baron, Philipp Frank, Ser-

gio Martin-Alvarez, Nolan Koblischke, Frank J. Qu, et al. ReplicationBench: Can AI agents replicate astrophysics

research papers? arXiv preprint arXiv:2510.24591 , 2025.

[84] Z.ai. GLM-5.1: Towards long-horizon tasks. https://z.ai/blog/glm-5.1 , 2026. Model release blog and model

card.

[85] Hanlin Zhang, Jikai Jin, Vasilis Syrgkanis, and Sham Kakade.

Prescriptive scaling reveals the evolution of

language model capabilities. arXiv preprint arXiv:2602.15327 , 2026.

[86] Zhirui Zhang, Hongbo Zhang, Haoxiang Fei, et al. SWE-AGI: Benchmarking specication-driven software con-

struction with MoonBit in the era of autonomous agents. arXiv preprint arXiv:2602.09447 , 2026.

[87] Junhao Zheng, Xidi Cai, Qiuke Li, Duzhen Zhang, ZhongZhi Li, Yingying Zhang, Le Song, and Qianli Ma.

LifelongAgentBench: Evaluating LLM agents as lifelong learners. arXiv preprint arXiv:2505.11942 , 2025.

23

**Appendix**

**Appendix Contents**

A

Evaluation Harness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

B

Serving and API Stability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

C

Evaluation Hacking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

D

A Comprehensive Derivation of the Log-Sigmoid Law . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

D.1

Preliminaries: Latent Capability Graph and the Attainable Support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

D.2

Environment Learning as a Frontier Expansion Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

D.3

Many-task Aggregation Reveals the Smooth Log-Sigmoid Law . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

D.4

Graph Self-similarity Induces Log Scale for Time Axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

D.5

Discussion and Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

E

More Discussion on the Scaling Law Shapes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

F

Additional Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

F.1

Benchmarks Not Suitable for Measuring Self-Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

F.2

Benchmarks Suitable for Measuring Learning or Self-Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

F.3

Scaling Laws for LLMs and Agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

G

Additional Benchmark and Experiment Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

G.1

Estimating the With- and Without-Experience Curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

G.2

Gravitational-Wave Case Study Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

G.3

Harness-Level Continuation Ablations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

G.4

Per-Task Design Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47

G.5

Per-Task Learning Curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

G.6

Per-Task Score Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74

H

Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79

24

**A**

**Evaluation Harness**

A standard unit-test harness is not enough for day-long runs. The benchmark must hide evaluation assets,

support repeated submissions over many hours, measure progress even when agents do not explicitly submit,

and run reliably on both local machines and clusters. We built **SForge** around three mechanisms: isolated

work and judge environments, a feedback loop modeled on online judges, and progress tracking on the host.

Two-container architecture.

Each task is materialized as two task-specic Docker images:

ˆ The **work image** contains the skeleton codebase, documentation, and local validation tools, but no

hidden evaluation assets. The agent operates only in this environment.

ˆ The **judge image** contains the hidden evaluation assets, grading scripts, and evaluation commands. It

is never exposed to the agent.

At evaluation time, the agent's code is copied into an ephemeral judge container, which runs the hidden tests,

returns only task-dened structured feedback, and is then destroyed. This separation prevents agents from

inspecting or modifying the hidden grader while still allowing realistic iterative development.

Judge server and the outer loop.

The outer loop is mediated by a host-side HTTP judge server.

The

agent submits its current solution to the server, which queues the submission, runs the judge container,

parses the result, and returns feedback such as pass rate, score, per-test verdicts, or diagnostics. For long-

running evaluations, the server supports asynchronous grading, allowing agents to continue working while

submitted jobs are being judged. The server also enforces submission budgets, cooldown intervals, and session

authentication.

Long-horizon execution and measurement.

SForge combines host-side auto-eval with stop-hook and auto-

resume mechanisms to support day-scale runs. Auto-eval periodically snapshots and evaluates the agent

workspace through a privileged channel; these results are recorded for trajectory analysis but are not shown

to the agent. The stop hook and auto-resume mechanism reduce premature truncation from voluntary exits,

crashes, context limits, or transient API failures.

Operational support and safeguards.

SForge also provides practical infrastructure for running and auditing

large-scale experiments. A web dashboard records score trajectories, submission histories, dis, and conver-

sation traces for live monitoring and post-hoc comparison. The same task specication can run on either a

local Docker backend or a Kubernetes backend for cluster-scale evaluation. To preserve benchmark integrity,

SForge combines workjudge isolation with submission ltering, network isolation, and session-scoped au-

thentication, so agents can receive feedback without access to hidden tests, privileged history, or auto-eval

results. Appendix C describes task-design failure modes we observed during benchmark development and

the corresponding mitigations.

**B**

**Serving and API Stability**

Sustaining a single agent for 12 hours or more stresses API serving far more than short evaluations do: a

day-long run must keep the model, its context, and its tool calls available without interruption, and any

serving-side incident in that window can truncate or degrade the trajectory. Our long-horizon tasks therefore

unavoidably fold serving stability into what they measure. We view this as appropriate rather than a confound

to be engineered away: an agent deployed to work for hours in the real world is subject to exactly these serving

realities, so a benchmark for long-horizon learning should reect them too.

25

0

1

2

3

4

5

6

7

8

9

10

11

Elapsed run time (h)

0

2

4

6

8

10

12

Infra incidents per run · h − 1

6 h

GPT-5.4

GPT-5.5

**Figure 14** Serving-side incident rate during long-horizon GPT-5.4 and GPT-5.5 runs. Incidents are normalized by

active run time; the dashed line marks six elapsed hours. GPT-5.4 experienced substantially more infrastructure and

API interruptions, especially in the later part of the run.

Figure 14 quanties this for the two GPT models, plotting the serving-side incident rate (normalized by

active run time) against elapsed time: GPT-5.4 saw substantially more infrastructure and API interruptions

than GPT-5.5, especially after the six-hour mark. This carries two caveats for GPT-5.4. First, several of the

per-task cells with fewer than three valid runs (marked with _∗_ in the score tables) involve GPT-5.4, so its

lower run coverage partly reects serving reliability rather than model behavior, though the reported scores

still use only valid trajectories. Second, it oers an operational explanation for the forecast deviation agged

in Section 3\.2 (Figure 7 ): with availability dropping in the second half of the run, GPT-5.4's later trajectory

is noisier and pulls away from the log-sigmoid forecast t to its rst 6.5 hours.

**C**

**Evaluation Hacking**

Long-horizon evaluation gives agents many opportunities to adapt to evaluator feedback. During task con-

struction and adversarial stress tests, we audited traces for strategies that raised measured scores without

exercising the intended capability. These observations are development diagnostics, not ocial model results:

aected tasks were revised or excluded, and the cases below motivated safeguards in the nal benchmark.

Feedback as an oracle for hidden answers.

In cylinder\_wake\_prediction , an agent treated per-case abso-

lute errors as equations and reconstructed the hidden targets through more than 400 submissions. A lookup

table then scored 1.000 without solving the underlying uid dynamics problem, whereas the best observed

submission based on a physics model scored 0.165.

Optimizing stochastic upper tails.

In nethack\_dungeon\_agent , an agent removed a xed random seed after

recognizing that higher variance increased the chance of a favorable evaluation. Across 311 submissions, its

best score was 1,501 while its mean was 484, showing how best-of- _N_ selection can reward repeated sampling

as well as policy quality.

Overtting evaluator seeds.

In bipedalwalker\_locomotion\_rl , the development judge initially used a sin-

gle deterministic episode, allowing agents to infer and optimize for the reused seed rather than expected

return. One run reached a Hardcore return of 301.5 on the judge seed but averaged about 12 over a local

100-episode evaluation; another searched a small hand-coded controller directly against the judge formula.

This motivated hidden multi-seed evaluation for stochastic control tasks.

Crossing a trust boundary.

In autolifter , an agent discovered that anti-cheat checks exempted the repos-

itory's baseline/ directory and moved an implementation based on an oracle into that trusted path. It

26

solved 82 of 84 hidden cases and scored 0.980; the strongest observed submission that followed the intended

synthesis route scored 0.121.

Online answer lookup.

Publicly indexed data, task artifacts, or reference implementations can turn an

intended reasoning problem into retrieval. In stock\_momentum\_backtest , an agent attempted Web search

for target data, but network isolation for the task blocked the requests. We include this as a prevented risk

rather than a successful exploit.

Mitigation.

These ndings led us to harden both task design and infrastructure. We revised or excluded

aected tasks, reduced or aggregated feedback that could reveal hidden targets, enforced submission budgets

and cooldowns, evaluated stochastic behavior over hidden seed sets, extended integrity checks across writable

paths, and disabled network access for tasks where public data or reference solutions could reveal the answer.

These controls do not eliminate every adaptive attack, but they reduce the channels identied during task

development.

**D**

**A Comprehensive Derivation of the Log-Sigmoid Law**

This appendix gives a comprehensive derivation of a sucient mechanism for the empirical log-sigmoid law

observed in the task-aggregate environment-learning curve. We assume the score of a single task is observed

through nitely many visible score units , so its best-so-far curve can be a jagged staircase with long plateaus

and abrupt breakthroughs. These irregularities are the expected nite-resolution behavior of individual tasks.

Under explicit cut-mixing, granularity, midpoint-alignment, and speed-concentration assumptions, we show

how averaging many independently evaluated task scores can yield a smooth log-sigmoid limit.

Our central modeling assumption: **environment learning is a frontier expansion process on the task graph** .

We model a task environment as a latent graph whose nodes are small score units, and the environment

learning process can be viewed as frontier expansion on this graph. Our theory provides a clear path from

frontier expansion process to the observed log-sigmoid law.

The exposition of the derivation follows ve steps:

**1\. Preliminaries.** Dene the model-conditioned task graph, score units, score measure _µ_ , inuence matrix

_K_ , its support graph _E_ _K_ , and the capability eld.

**2\. Environment learning as a frontier expansion process.** The model improves its outputs based on feedback

it has previously received. Within one task, the conditional expected score-growth rate is a weighted

cut from unlocked score nodes to locked score nodes of the task graph.

**3\. Single-task curves range from jagged to a smooth limit.** Weighted cut mixing and small score units

turn the jagged process into a logistic ordinary dierential equation in the many-unit limit.

**4\. Many-task aggregate reveals the log-sigmoid law.** Even though the expansion process on tasks with

nite score units remain jagged processes, the benchmark-aggregated curve converges to a smooth log-

sigmoid law.

**5\. Graph self-similarity induces a log scale for time.** Finally, we show that when the task graph displays

self-similar structure at dierent resolutions, frontier expansion naturally exhibits a log-time scale.

Throughout the section, we denote raw interaction time by _t >_ 0 , and the raw task/benchmark score by _S_ ( _t_ ) .

Let _t_ mid _>_ 0 and _S_ max _>_ 0 be tted parameters. The corresponding log-time coordinate and normalized

score are

_u_ = log _t_ _−_ log _t_ mid _,_

_x_ ( _u_ ) = _S_ ( _t_ )

_S_ max

We show how the following normalized log-sigmoid dynamics, with frontier speed _β_ (also a tted parameter),

27

can arise as a natural many-task limit of the averaged benchmark score:

d _x_ ( _u_ )

d _u_

= _βx_ ( _u_ )(1 _−_ _x_ ( _u_ )) _,_

_x_



log

_t_

_t_ mid



=

1

1 + ( _t_ mid _/t_ ) _β_ _._

The value at raw time _t_ = 0 is understood as the boundary limit _u_ _→ −∞_ .

**D.1**

**Preliminaries: Task Graph and the Attainable Support**

We start with one task and one xed model. The main assumption is that score units are the nodes of an

agent-conditioned task graph : unlocked nodes supply an inuence eld, locked nodes receive this eld through

directed inuence edges, and a locked node can become unlocked at a rate proportional to the eld strength.

Denition D.1 (Task graph) . Let _E_ be the set of visible score-unit nodes for the task. The language model

induces a nonnegative inuence matrix

_K_ = ( _K_ _ij_ ) _i,j_ _∈_ _E_ _,_

_K_ _ij_ _≥_ 0 _._

Its directed support graph has edge set _E_ _K_ = _{_ _j_ _→_ _i_ : _K_ _ij_ _>_ 0 _}_ where _j_ _→_ _i_ means that unlocked source

node _j_ can help unlock target node _i_ . We write _G_ _K_ = ( _E,_ _E_ _K_ ) for the resulting task graph.

If one begins with a larger ambient graph, the restriction to the model-relevant part is made before writing

_E_ and _K_ ; empirically, that restriction is absorbed into the tted ceiling _S_ max . Next we introduce the score

units and the corresponding task inuence eld.

Denition D.2 (Score units and normalized score measure) . On the latent graph _G_ _K_ = ( _E,_ _E_ _K_ ) , each node

_i_ _∈_ _E_ represents a score unit with weight _ω_ _i_ _≥_ 0 . The normalized score measure is the probability measure

_W_ =



_i_ _∈_ _E_

_ω_ _i_ _>_ 0 _,_

_µ_ _i_ = _ω_ _i_

_W_ _,_

_µ_ ( _A_ ) =



_i_ _∈_ _A_

_µ_ _i_ _,_

_∀_ _A_ _⊆_ _E._

Denition D.3 (Unlock state, unlocked and locked sets) . The unlock state of node _i_ at log-time _u_ is

_n_ _i_ ( _u_ ) _∈ {_ 0 _,_ 1 _}_ , and once a node is unlocked, it cannot be locked again. The normalized score, unlocked set,

and locked set are dened by

_x_ ( _u_ ) =



_i_ _∈_ _E_

_µ_ _i_ _n_ _i_ ( _u_ ) _,_

_U_ ( _u_ ) = _{_ _j_ _∈_ _E_ : _n_ _j_ ( _u_ ) = 1 _}_ _,_

_L_ ( _u_ ) = _{_ _i_ _∈_ _E_ : _n_ _i_ ( _u_ ) = 0 _}_ _._

(5)

For a static state _n_ = ( _n_ _i_ ) _i_ _∈_ _E_ , we also write

_U_ ( _n_ ) = _{_ _j_ _∈_ _E_ : _n_ _j_ = 1 _}_ _,_

_L_ ( _n_ ) = _{_ _i_ _∈_ _E_ : _n_ _i_ = 0 _}_ _,_

_x_ ( _n_ ) = _µ_ ( _U_ ( _n_ )) _._

Denition D.4 (Task inuence eld) . The entry _K_ _ij_ is the inuence strength from source node _j_ to target

node _i_ . The capability eld on target node _i_ is the incoming-edge sum

_h_ _i_ ( _n_ ) =



_j_ : _j_ _→_ _i_

_K_ _ij_ _n_ _j_ =



_j_ _∈_ _E_

_K_ _ij_ _n_ _j_ _._

When stating many-unit limits, we restore the index _N_ : the objects above become _E_ _N_ , _µ_ ( _N_ ) , _K_ ( _N_ ) , _n_ ( _N_ ) ( _u_ ) ,

_x_ _N_ ( _u_ ) , _U_ _N_ ( _u_ ) , _L_ _N_ ( _u_ ) , and

_µ_ _N_ ( _A_ ) =



_i_ _∈_ _A_

_µ_ ( _N_ )

_i_

_,_

_x_ _N_ ( _u_ ) =



_i_ _∈_ _E_ _N_

_µ_ ( _N_ )

_i_

_n_ ( _N_ )

_i_

( _u_ ) _,_

_h_ ( _N_ )

_i_

( _u_ ) =



_j_ _∈_ _E_ _N_

_K_ ( _N_ )

_ij_

_n_ ( _N_ )

_j_

( _u_ ) _._

For a static state _n_ _∈ {_ 0 _,_ 1 _}_ _E_ _N_ , we write

_U_ _N_ ( _n_ ) = _{_ _j_ _∈_ _E_ _N_ : _n_ _j_ = 1 _}_ _,_

_L_ _N_ ( _n_ ) = _{_ _i_ _∈_ _E_ _N_ : _n_ _i_ = 0 _}_ _,_

_x_ _N_ ( _n_ ) = _µ_ _N_ ( _U_ _N_ ( _n_ )) _._

28

**D.2**

**Environment Learning as a Frontier Expansion Process**

With the latent graph and score measure xed, we now turn the story into a process. The reason to use

a frontier picture is that long-horizon environment learning is cumulative. In a software task, a runnable

baseline makes later debugging meaningful; in a proof task, a lemma makes later proof obligations easier;

in a scientic task, a calibrated model or validation loop makes later parameter search more useful. More

generally, each partial success can become a tool for later progress.

The graph model encodes which already-solved score units can help unlock which remaining ones. At log

time _u_ , let

_U_ ( _u_ ) = _{_ _j_ : _n_ _j_ ( _u_ ) = 1 _}_ _,_

_L_ ( _u_ ) = _{_ _i_ : _n_ _i_ ( _u_ ) = 0 _}_

denote the unlocked and locked sets. A locked unit _i_ can only become usable through inuence arriving

from units in _U_ ( _u_ ) . Thus the relevant quantity is not the total amount of unlocked score, but the amount of

inuence crossing the frontier from _U_ ( _u_ ) into _L_ ( _u_ ) .

Probabilistic frontier expansion. For a locked score unit _i_ , its task eld is given by _h_ _i_ ( _u_ ) = 

_j_ _∈_ _E_ _K_ _ij_ _n_ _j_ ( _u_ ) .

We turn the inuence of the eld into a continuous-time stochastic process by assuming that unit _i_ unlocks

with hazard proportional to its accumulated eld:

_η_ (1 _−_ _n_ _i_ ( _u_ )) _h_ _i_ ( _u_ ) = _η_ (1 _−_ _n_ _i_ ( _u_ ))



_j_ _∈_ _E_

_K_ _ij_ _n_ _j_ ( _u_ ) _,_

where _η >_ 0 converts inuence strength into progress per unit log time. Thus the eld does not deterministi-

cally unlock _i_ ; it determines the instantaneous probability that _i_ unlocks. This is the sense in which learning

expands the frontier: locked nodes become available at rates determined by the inuence they receive from

the currently unlocked side of the graph. We formalize this process in the denition below.

Denition D.5 (Single-task frontier process) . Fix a nite task graph _G_ _K_ = ( _E,_ _E_ _K_ ) , score weights _µ_ _i_ ,

inuence matrix _K_ , and conversion constant _η >_ 0 . The single-task frontier process is the continuous-time

process on _{_ 0 _,_ 1 _}_ _E_ in which, for each score unit _i_ , the instantaneous unlocking intensity is

_λ_ _i_ ( _u_ ) := lim

∆ _u_ _↓_ 0

1

∆ _u_ P ( _n_ _i_ ( _u_ \+ ∆ _u_ ) _−_ _n_ _i_ ( _u_ ) = 1 _|_ _n_ ( _u_ ))

= _η_ (1 _−_ _n_ _i_ ( _u_ ))



_j_ _∈_ _E_

_K_ _ij_ _n_ _j_ ( _u_ ) _._

(6)

Importantly, once a node unlocks, it remains unlocked.

To express the resulting score growth, dene for _A, B_ _⊆_ _E_ the weighted frontier cut

_C_ ( _A, B_ ) =



_i_ _∈_ _A_



_j_ _∈_ _B_

_µ_ _i_ _K_ _ij_ _._

This is the total inuence from sources in _B_ to targets in _A_ , with each target weighted by the score gained

if it unlocks. The active frontier at time _u_ is therefore _C_ ( _L_ ( _u_ ) _, U_ ( _u_ )) .

Lemma D.1 (Exact single-task frontier growth rate) . For the single-task frontier process,

d

d _u_ E



_x_ ( _u_ ) _|_ _n_ ( _u_ )



= _ηC_ ( _L_ ( _u_ ) _, U_ ( _u_ )) _._

Proof. Fix _u_ and condition on the state _n_ ( _u_ ) = _n_ . For _i_ _∈_ _E_ , let _A_ _i_ (∆ _u_ ) denote the event that node _i_ unlocks

during [ _u, u_ \+ ∆ _u_ ] . By the denition of the unlocking intensity,

Pr( _A_ _i_ (∆ _u_ ) _|_ _n_ ( _u_ ) = _n_ ) = _η_ (1 _−_ _n_ _i_ )



_j_ _∈_ _E_

_K_ _ij_ _n_ _j_ ∆ _u_ \+ _o_ (∆ _u_ ) _._

29

Since _E_ is nite, the probability of two or more unlocking events in [ _u, u_ \+ ∆ _u_ ] is _o_ (∆ _u_ ) . Therefore, to

rst order in ∆ _u_ , the expected score increment is obtained by summing the score gain from each possible

single-node unlock:

E [ _x_ ( _u_ \+ ∆ _u_ ) _−_ _x_ ( _u_ ) _|_ _n_ ( _u_ ) = _n_ ] =



_i_ _∈_ _E_

_µ_ _i_ Pr( _A_ _i_ (∆ _u_ ) _|_ _n_ ( _u_ ) = _n_ ) + _o_ (∆ _u_ )

= _η_



_i_ _∈_ _E_

_µ_ _i_ (1 _−_ _n_ _i_ )



_j_ _∈_ _E_

_K_ _ij_ _n_ _j_ ∆ _u_ \+ _o_ (∆ _u_ ) _._

Dividing by ∆ _u_ and letting ∆ _u_ _↓_ 0 gives

d

d _u_ E [ _x_ ( _u_ ) _|_ _n_ ( _u_ ) = _n_ ] = _η_



_i_ _∈_ _E_

_µ_ _i_ (1 _−_ _n_ _i_ )



_j_ _∈_ _E_

_K_ _ij_ _n_ _j_ _._

Since 1 _−_ _n_ _i_ restricts the outer sum to _i_ _∈_ _L_ ( _n_ ) , and _n_ _j_ restricts the inner sum to _j_ _∈_ _U_ ( _n_ ) , this becomes

d

d _u_ E [ _x_ ( _u_ ) _|_ _n_ ( _u_ ) = _n_ ] = _η_



_i_ _∈_ _L_ ( _n_ )



_j_ _∈_ _U_ ( _n_ )

_µ_ _i_ _K_ _ij_ = _ηC_ ( _L_ ( _n_ ) _, U_ ( _n_ )) _._

This proves the claim.

Lemma D.1 is the key reduction. It says that, to obtain a logistic expected growth rate, we do not need every

microscopic edge weight to be identical. Instead, we need the boundary inuence to depend mainly on two

coarse quantities: the unlocked mass _µ_ ( _U_ ) and the locked mass _µ_ ( _L_ ) . Then the eld is roughly the product

of the two: available reusable capability times remaining score opportunity.

As the number of score units increases, the same xed-resolution objects are now applied to the size- _N_ graph.

In particular,

_C_ _N_ ( _A, B_ ) =



_i_ _∈_ _A_



_j_ _∈_ _B_

_µ_ ( _N_ )

_i_

_K_ ( _N_ )

_ij_

_,_

_A, B_ _⊆_ _E_ _N_ _._

From frontier cuts to product frontiers. The remaining modeling question is when this boundary inuence

should look like a product of the two measures. The following quantity controls the deviation of the frontier

process from the complete-mixing case.

Denition D.6 (Single-task weighted cut error) . Given ( _E_ _N_ _, µ_ ( _N_ ) _, K_ ( _N_ ) ) and an arbitrary _κ >_ 0 , dene

_ε_ _N_ ( _κ_ ) =

sup

_A,B_ _⊆_ _E_ _N_





_i_ _∈_ _A_



_j_ _∈_ _B_

_µ_ ( _N_ )

_i_



_K_ ( _N_ )

_ij_

_−_ _κµ_ ( _N_ )

_j_





_._

Condition D.1 (Single-task weighted cut mixing) . There exists a _κ >_ 0 such that, as _N_ _→ ∞_ for the task

graph, the weighted cut error in Denition D.6 satises

_ε_ _N_ _→_ 0 _._

Weighted cut mixing is weaker than entrywise complete mixing. It does not say that each _K_ ( _N_ )

_ij_

is close to

_κµ_ ( _N_ )

_j_

. It says that, for every possible frontier, the aggregate capability crossing from unlocked graph nodes

into locked graph nodes is close to the product-measure value.

Lemma D.2 (Cut mixing gives logistic frontier growth rate) . Under Condition D.1 , the following holds for

every static state _n_ _∈ {_ 0 _,_ 1 _}_ _E_ _N_ . Let _U_ _N_ = _U_ _N_ ( _n_ ) , _L_ _N_ = _L_ _N_ ( _n_ ) , and _x_ _N_ = _x_ _N_ ( _n_ ) . Then

_|_ _C_ _N_ ( _L_ _N_ _, U_ _N_ ) _−_ _κx_ _N_ (1 _−_ _x_ _N_ ) _| ≤_ _ε_ _N_ _._

Consequently,

_b_ _N_ ( _n_ ) = _ηκx_ _N_ (1 _−_ _x_ _N_ ) + _r_ _N_ ( _n_ ) _,_

_|_ _r_ _N_ ( _n_ ) _| ≤_ _ηε_ _N_ _._

30

Proof. Apply Denition D.6 to _A_ = _L_ _N_ and _B_ = _U_ _N_ . Since _µ_ _N_ ( _U_ _N_ ) = _x_ _N_ and _µ_ _N_ ( _L_ _N_ ) = 1 _−_ _x_ _N_ ,

_|_ _C_ _N_ ( _L_ _N_ _, U_ _N_ ) _−_ _κx_ _N_ (1 _−_ _x_ _N_ ) _|_ =





_i_ _∈_ _L_ _N_



_j_ _∈_ _U_ _N_

_µ_ ( _N_ )

_i_



_K_ ( _N_ )

_ij_

_−_ _κµ_ ( _N_ )

_j_





_≤_ _ε_ _N_ _._

The expected-growth-rate statement follows from Lemma D.1 .

Cut mixing controls the deterministic expected growth rate. A separate condition controls the visible jump

size. This distinction is crucial for the interpretation of the paper: a nite task with only a few large score

units can follow the right frontier mechanism and still look very jagged.

Condition D.2 (Small score units and controlled elds) . Let

_q_ _N_ =



_i_ _∈_ _E_ _N_



_µ_ ( _N_ )

_i_

 2 _._

Assume _q_ _N_ _→_ 0 . Assume also that there is a deterministic _H_ _N_ such that

sup

_i_ _∈_ _E_ _N_ _, n_ _∈{_ 0 _,_ 1 _}_ _EN_



_j_ _∈_ _E_ _N_

_K_ ( _N_ )

_ij_

_n_ _j_ _≤_ _H_ _N_ _,_

_H_ _N_ _q_ _N_ _→_ 0 _._

For equal score units, _q_ _N_ = 1 _/N_ . Thus Condition D.2 captures the smoothening process from a task with few

bulky score units to a task with many small score units. The theorem below should be read exactly in that

way. It is not a claim that the realized best-so-far curve of a nite benchmark task must be visually smooth.

Rather, it says that if the same task-level mechanism were observed at increasingly ne score resolution, the

staircase process would converge to a logistic frontier.

Theorem D.1 (Single-task frontier, many-unit limit) . Consider the single-task frontier process of Deni-

tion D.5 . Let [ _u_ 0 _, u_ 1 ] be a compact log-time interval and let _x_ 0 _∈_ [0 _,_ 1] . Suppose Conditions D.1 and D.2 hold,

and suppose _x_ _N_ ( _u_ 0 ) _→_ _x_ 0 . Then _x_ _N_ converges uniformly in probability on [ _u_ 0 _, u_ 1 ] to the solution of

_dx_

_du_ = _ηκx_ (1 _−_ _x_ ) _,_

_x_ ( _u_ 0 ) = _x_ 0 _._

(7)

If _t_ mid is chosen so that the limiting midpoint satises _x_ (0) = 1 _/_ 2 , then, with _x_ ( _t_ ) := _x_ (log( _t/t_ mid )) , we

obtain the log-sigmoid law:

_x_ _N_

_P_

_−→_ _x_ ( _t_ ) =

1

1 + ( _t_ mid _/t_ ) _β_ _,_

_β_ = _ηκ._

(8)

Proof. Let _M_ _N_ ( _u_ ) denote the martingale increment in the Doob-Meyer decomposition, normalized so that

_M_ _N_ ( _u_ 0 ) = 0 . The Doob-Meyer decomposition and Lemma D.2 give, for _u_ _∈_ [ _u_ 0 _, u_ 1 ] ,

_x_ _N_ ( _u_ ) = _x_ _N_ ( _u_ 0 ) + _M_ _N_ ( _u_ ) + _ηκ_

 _u_

_u_ 0

_x_ _N_ ( _s_ )(1 _−_ _x_ _N_ ( _s_ )) _ds_ \+ _R_ _N_ ( _u_ ) _,_

(9)

where

sup

_u_ _∈_ [ _u_ 0 _,u_ 1 ]

_|_ _R_ _N_ ( _u_ ) _| ≤_ _η_ ( _u_ 1 _−_ _u_ 0 ) _ε_ _N_ _._

A jump of unit _i_ changes _x_ _N_ by _µ_ ( _N_ )

_i_

. The predictable quadratic variation accumulated over the interval

[ _u_ 0 _, u_ 1 ] is therefore bounded by

_⟨_ _M_ _N_ _⟩_ [ _u_ 0 _,u_ 1 ] =

 _u_ 1

_u_ 0



_i_ _∈_ _E_ _N_



_µ_ ( _N_ )

_i_

 2 _η_



1 _−_ _n_ ( _N_ )

_i_

( _s_ )

 

_j_ _∈_ _E_ _N_

_K_ ( _N_ )

_ij_

_n_ ( _N_ )

_j_

( _s_ ) _ds_ _≤_ _η_ ( _u_ 1 _−_ _u_ 0 ) _H_ _N_ _q_ _N_ _._

31

Doob's _L_ ² inequality therefore yields

E



sup

_u_ _∈_ [ _u_ 0 _,u_ 1 ]

_|_ _M_ _N_ ( _u_ ) _|_ ²



_≤_ 4 _η_ ( _u_ 1 _−_ _u_ 0 ) _H_ _N_ _q_ _N_ _→_ 0 _._

Thus the martingale term vanishes uniformly in probability.

Let _f_ ( _x_ ) = _ηκx_ (1 _−_ _x_ ) . On [0 _,_ 1] , _f_ is Lipschitz with constant at most _ηκ_ . Comparing ( 9 ) with the integral

equation for ( 7 ) gives

sup

_u_ 0 _≤_ _r_ _≤_ _u_

_|_ _x_ _N_ ( _r_ ) _−_ _x_ ( _r_ ) _| ≤ |_ _x_ _N_ ( _u_ 0 ) _−_ _x_ 0 _|_ \+

sup

_u_ 0 _≤_ _r_ _≤_ _u_

_|_ _M_ _N_ ( _r_ ) _|_ \+ _η_ ( _u_ 1 _−_ _u_ 0 ) _ε_ _N_

\+ _ηκ_

 _u_

_u_ 0

sup

_u_ 0 _≤_ _r_ _≤_ _s_

_|_ _x_ _N_ ( _r_ ) _−_ _x_ ( _r_ ) _|_ _ds._

Gronwall's inequality proves uniform convergence in probability on [ _u_ 0 _, u_ 1 ] . Solving ( 7 ) and setting _x_ (0) = 1 _/_ 2

gives ( 8 ).

**Interpreting the single-task curve shapes.**

For nite _N_ , the task score is still a jagged jump process. The

theorem says that a smooth logistic curve appears only after two eects become negligible: mixing cut error

_ε_ _N_ _→_ 0 and jump noise from large score units _H_ _N_ _q_ _N_ _→_ 0 . Thus a jagged nite-task curve is compatible with

the logistic frontier mechanism. Moreover, the growth-rate _x_ (1 _−_ _x_ ) has a direct interpretation: unlocked

score measure _x_ supplies capability to help unlock new score, while locked score measure 1 _−_ _x_ delimits the

remaining opportunities for score improvement. In the next subsection, we explain why averaging many such

nite-task curves is the natural place to expect a clean scaling law.

**D.3**

**Many-task Aggregation Reveals the Smooth Log-Sigmoid Law**

We now return to the quantity t in the benchmark: the average over many independently evaluated tasks.

As we have observed empirically, the per-task curves are heterogeneous and often visibly jagged, while the

cross-task averages are much smoother and become better t by the log-sigmoid as more tasks are included.

In our language, each task is its own nite frontier expansion process on a task-specic task graph. The

aggregate theorem therefore answers the central question:

How can many jagged task curves produce a clean log-sigmoid scaling law after task averaging?

The answer has two layers.

First, because dierent task environments do not interact with each other,

each task can have its own approximate logistic frontier. Second, the benchmark average removes nite-

task roughness and becomes a single log-sigmoid when the task midpoints and task speeds are suciently

concentrated in the many-task limit.

Moving from a single task to a full benchmark introduces three additional sources of variation.

ˆ **Task-level logistic frontier dynamics.** Each task has its own task graph, score atoms, inuence matrix,

cut error, and nite-jump noise. These quantities determine how closely that task's frontier expansion

follows its own logistic limit.

ˆ **Time-axis alignment.** Each task may have its own model-dependent midpoint _t_ mid _,b_ . A benchmark-

level t, however, has only one common midpoint _t_ mid . Therefore the task-specic midpoint shifts must

concentrate across tasks.

ˆ **Learning-speed homogeneity.** Each task may also have its own frontier speed _β_ _b_ . A benchmark-level

t uses one common speed _β_ , so the model-dependent task learning speeds must concentrate around a

shared value.

The aggregate theorem says that the log-sigmoid law appears as a population-level limit: nite-task roughness

is washed out by averaging, and the remaining task-level logistic frontiers combine into a single curve when

their midpoints and speeds are suciently aligned.

32

Denition D.7 (Benchmark task graph and state) . For a benchmark with _M_ tasks, the tasks are indexed

by _b_ = 1 _, . . . , M_ . Task _b_ has its own task graph

_G_ _b_ = ( _E_ _b_ _,_ _E_ _b_ ) _,_

_E_ _b_ = _{_ _j_ _→_ _i_ : _K_ _b_

_ij_ _>_ ⁰ _}_ _,_

where _E_ _b_ is the task's visible score-unit node set for the model being evaluated. It has normalized score

measurees _µ_ _b_

_i_ for _i_ _∈_ _E_ _b_ , inuence matrix _K_ _b_ = ( _K_ _b_

_ij_ ) _i,j_ _∈_ _E_ _b_ , and eld-to-progress conversion constant _η_ _b_ _>_ ⁰ .

The state vector of task _b_ is

_n_ _b_ ( _u_ ) = ( _n_ _b_

_i_ ( _u_ )) _i_ _∈_ _E_ _b_ _,_

and the capability eld on node _i_ is

_h_ _b_

_i_ ( _u_ ) =



_j_ _∈_ _E_ _b_

_K_ _b_

_ij_ _n_ _b_

_j_ ( _u_ ) _._

Denition D.8 (Task score and benchmark average) . The normalized score of task _b_ at log-time _u_ is

_x_ _b_ ( _u_ ) =



_i_ _∈_ _E_ _b_

_µ_ _b_

_i_ _n_ _b_

_i_ ( _u_ ) _._

And the benchmark-average normalized score is

_x_ _B_ ( _u_ ) = ¹

_M_

_M_



_b_ =1

_x_ _b_ ( _u_ ) _._

Here _u_ = log _t_ _−_ log _t_ mid is the log-time coordinate.

For raw time, we denote the normalized score and

benchmark score by

_x_ _†_

_B_ ( _t_ ) = _x_ _B_ (log( _t/t_ mid )) _,_

_S_ _B_ ( _t_ ) = _S_ max _·_ _x_ _†_

_B_ ( _t_ ) _,_

where _t_ mid is the tted aggregate midpoint and _S_ max denotes the tted aggregate ceiling. Individual tasks

may have residual midpoint shifts relative to this common coordinate, introduced below as _δ_ _b_ in ( 10 ).

Denition D.9 (Task-specic logistic frontier) . In the benchmark-level log-time coordinate _u_ , task _b_ is

assigned a task-specic frontier speed _β_ _b_ _≥_ 0 and a residual midpoint shift _δ_ _b_ _∈_ R .

The corresponding

task-specic logistic curve is

_ℓ_ _b_ ( _u_ ) =

1

1 + _e_ _−_ _β_ _b_ ( _u_ _−_ _δ_ _b_ ) _._

(10)

Here _β_ _b_ controls the speed of task-level frontier propagation, while _δ_ _b_ measures the task midpoint relative to

the benchmark-level midpoint _t_ mid . Thus _δ_ _b_ = 0 means that task _b_ 's midpoint is aligned with the aggregate

midpoint.

The rst condition applies the single-task cut-mixing argument inside each task graph. It is written for the

inuence matrix _η_ _b_ _K_ _b_ , so the product-frontier coecient is directly _β_ _b_ .

Denition D.10 (Blockwise weighted cut error and eld bound) . For each task _b_ , dene the task-conditioned

weighted cut error by

_ε_ _b_ =

sup

_A,B_ _⊆_ _E_ _b_





_i_ _∈_ _A_



_j_ _∈_ _B_

_µ_ _b_

_i_



_η_ _b_ _K_ _b_

_ij_ _−_ _β_ _b_ _µ_ _b_

_j_





_._

(11)

Dene the block granularity and score-growth eld bound by

_q_ _b_ =



_i_ _∈_ _E_ _b_

( _µ_ _b_

_i_ ) ² _,_

_H_ _b_ =

sup

_i_ _∈_ _E_ _b_ _, n_ _∈{_ 0 _,_ 1 _}_ _Eb_

_η_ _b_



_j_ _∈_ _E_ _b_

_K_ _b_

_ij_ _n_ _j_ _._

Condition D.3 (Blockwise weighted cut mixing and vanishing score units) . Assume that task speeds are

uniformly bounded,

0 _≤_ _β_ _b_ _≤_ _β_ \+ _<_ _∞_ _,_

33

and that the average task cut error and granularity error vanish:

∆ _M_ = ¹

_M_

_M_



_b_ =1

_ε_ _b_ _→_ 0 _,_

_A_ _M_ = ¹

_M_

_M_



_b_ =1



_H_ _b_ _q_ _b_ _→_ 0

(12)

in probability.

The next condition asks the initial value variation is negligible across dierent tasks in the benchmark.

Condition D.4 (Blockwise initial alignment) . We assume the average initial value of the dynamics is aligned,

1

_M_

_M_



_b_ =1

_|_ _x_ _b_ ( _u_ 0 ) _−_ _ℓ_ _b_ ( _u_ 0 ) _|_

_P_

_−→_ 0 _._

Condition D.3 has a direct consequence: the observed benchmark trajectory is close to an average of task-

specic logistic frontiers. Notice the averaging in the condition. We do not require every task to look smooth

on its own, but the average contribution of cut errors, score units, and jumps to vanish. This is the formal

version of the empirical claim that a population of jagged frontier expansion processes can reveal a smooth

law. For the compact interval _I_ _⊆_ R , dene the following blockwise trajectory error supremum:

_R_ _M_ ( _I_ ) := ¹

_M_

_M_



_b_ =1

sup

_u_ _∈_ _I_

_|_ _x_ _b_ ( _u_ ) _−_ _ℓ_ _b_ ( _u_ ) _|_ _._

(13)

Then we have the following lemma that proves its vanishing property.

Lemma D.3 (Average error supremum, many-task limit) . Under Conditions D.3 and D.4 , _R_ _M_ ( _I_ )

_P_ _→_ 0 as

_M_ _→ ∞_ for any compact interval _I_ _⊆_ R .

Proof. For task _b_ , the same Doob-Meyer decomposition as in the single-task proof gives

_x_ _b_ ( _u_ ) = _x_ _b_ ( _u_ 0 ) + _M_ _b_ ( _u_ ) +

 _u_

_u_ 0

_{_ _β_ _b_ _x_ _b_ ( _s_ )(1 _−_ _x_ _b_ ( _s_ )) + _ρ_ _b_ ( _s_ ) _}_ _ds,_

(14)

where _M_ _b_ is a martingale and, by ( 11 ), _|_ _ρ_ _b_ ( _s_ ) _| ≤_ _ε_ _b_ for all states. The task-level curve ( 10 ) solves

d _ℓ_ _b_

d _u_ = _β_ _b_ _ℓ_ _b_ (1 _−_ _ℓ_ _b_ ) _._

Since _z_ _→_ _β_ _b_ _z_ (1 _−_ _z_ ) is Lipschitz on [0 _,_ 1] with constant at most _β_ \+ , Gronwall's inequality applied to ( 14 )

yields

sup

_u_ _∈_ _I_

_|_ _x_ _b_ ( _u_ ) _−_ _ℓ_ _b_ ( _u_ ) _| ≤_ _e_ _β_ \+ _|_ _I_ _|_



_|_ _x_ _b_ ( _u_ 0 ) _−_ _ℓ_ _b_ ( _u_ 0 ) _|_ \+ sup

_u_ _∈_ _I_

_|_ _M_ _b_ ( _u_ ) _|_ \+ _|_ _I_ _|_ _ε_ _b_



_,_

(15)

where _|_ _I_ _|_ = _u_ 1 _−_ _u_ 0 .

The rst term converges to zero by Condition D.4 . The third term as well by Condition D.3 . It remains to

average the martingale terms. A jump of unit _i_ in task _b_ changes _x_ _b_ by _µ_ _b_

_i_ , and the total score-growth eld

is bounded by _H_ _b_ . Hence the predictable quadratic variation of _M_ _b_ can be bounded by

_⟨_ _M_ _b_ _⟩_ _I_ _≤ |_ _I_ _|_ _H_ _b_ _q_ _b_ _._

Doob's _L_ ² inequality gives the conditional bound

E



sup

_u_ _∈_ _I_

_|_ _M_ _b_ ( _u_ ) _|_

 _G_ _M_



_≤_ 2



_|_ _I_ _|_ _H_ _b_ _q_ _b_ _,_

(16)

34

where _G_ _M_ denotes the task-level weights and inuence matrices. This conditional form is useful because _A_ _M_

may itself be random. Let

_Z_ _M_ = ¹

_M_

_M_



_b_ =1

sup

_u_ _∈_ _I_

_|_ _M_ _b_ ( _u_ ) _|_ _._

For any _ε >_ 0 and _a >_ 0 , ( 16 ) implies

P ( _Z_ _M_ _> ε_ ) _≤_ P ( _A_ _M_ _> a_ ) + P ( _Z_ _M_ _> ε, A_ _M_ _≤_ _a_ )

_≤_ P ( _A_ _M_ _> a_ ) + _ε_ _−_ ¹ E [ _Z_ _M_ 1 _{_ _A_ _M_ _≤_ _a_ _}_ ]

_≤_ P ( _A_ _M_ _> a_ ) + ²



_|_ _I_ _|_ _a_

_ε_

_._

Since _A_ _M_ _→_ 0 in probability, rst let _M_ _→ ∞_ and then let _a_ _↓_ 0 to obtain _Z_ _M_ _→_ 0 in probability. Averaging

( 15 ) over _b_ and using ( 12 ) proves ( 13 ).

The next two task-distributional assumptions serve to align the scaling curves within the benchmark. They

are not consequences of blockwise cut mixing. They are what turns an average of task-level sigmoids into a

single benchmark sigmoid.

Assumption D.1 (Uniform log-time bias) . There is a single benchmark-level midpoint _t_ mid such that the

residual task shifts in ( 10 ) satisfy

_D_ _M_ = ¹

_M_

_M_



_b_ =1

_|_ _δ_ _b_ _| →_ 0 _._

The strict uniform-bias case is _δ_ _b_ _≡_ 0 .

Assumption D.2 (Concentrated environment learning speed) . There is a scalar _β >_ 0 such that

_B_ _M_ = ¹

_M_

_M_



_b_ =1

_|_ _β_ _b_ _−_ _β_ _| →_ 0 _._

In particular, _M_ _−_ ¹  _M_

_b_ =1 _β_ _b_ _→_ _β_ .

The reason these assumptions are necessary can be seen from the aggregated frontier. Averaging removes

jaggedness, but it does not by itself align task diculty or environment learning speed. When blockwise cut

mixing error tends to zero, the leading expected growth rate is

1

_M_

_M_



_b_ =1

_β_ _b_ _x_ _b_ ( _u_ )(1 _−_ _x_ _b_ ( _u_ )) _._

This becomes _βx_ _B_ (1 _−_ _x_ _B_ ) only if tasks are aligned enough that the task scores and speeds behave like one

population. Even when all speeds are equal, persistent task dispersion subtracts from the scalar frontier

through

1

_M_

_M_



_b_ =1

_x_ _b_ (1 _−_ _x_ _b_ ) = _x_ _B_ (1 _−_ _x_ _B_ ) _−_ ¹

_M_

_M_



_b_ =1

( _x_ _b_ _−_ _x_ _B_ ) ² _._

The theorem below proves the core convergence once the blockwise frontier condition, midpoint alignment,

and speed concentration are in place.

Theorem D.2 (Benchmark aggregate produces the log-sigmoid law in the many-task limit) . Fix a compact

log-time interval _I_ _⊆_ R . Suppose Conditions D.3 \- D.4 , Assumptions D.1 \- D.2 hold for some _t_ mid _>_ 0 and

_β >_ 0 . Then

_x_ _B_ ( _u_ )

_P_ _→_ _ℓ_ _β_ ( _u_ ) _,_

_∀_ _u_ _∈_ _I._

Equivalently, for raw times _t_ whose log coordinate _u_ = log( _t/t_ mid ) lies in _I_ , using the notation from Deni-

tion D.8 , we have

_x_ _†_

_B_ ( _t_ ) = _S_ _B_ ( _t_ )

_S_ max

_P_

_−→_

1

1 + ( _t_ mid _/t_ ) _β_ _._

(17)

35

Proof. We prove the statement for the normalized score _x_ _B_ ( _u_ ) . Multiplication by a xed tted ceiling _S_ max

gives the raw-score statement.

Step 1: replace observed task trajectories by task-level frontier limits. By Lemma D.3 ,

sup

_u_ _∈_ _I_

 _x_ _B_ ( _u_ ) _−_ 1

_M_

_M_



_b_ =1

_ℓ_ _b_ ( _u_ )

 _≤_ 1

_M_

_M_



_b_ =1

sup

_u_ _∈_ _I_

_|_ _x_ _b_ ( _u_ ) _−_ _ℓ_ _b_ ( _u_ ) _|_ = _R_ _M_ ( _I_ ) _→_ 0

(18)

in probability.

Step 2: align the task-level frontiers to the benchmark frontier. Since the logistic link satises _|_ sigmoid _′_ ( _z_ ) _| ≤_

1 _/_ 4 for all _z_ , writing _ℓ_ _β_ ( _u_ ) = sigmoid ( _βu_ ) , we have

sup

_u_ _∈_ _I_

_|_ _ℓ_ _b_ ( _u_ ) _−_ _ℓ_ _β_ ( _u_ ) _| ≤_ ¹

4 sup

_u_ _∈_ _I_

_|_ _β_ _b_ ( _u_ _−_ _δ_ _b_ ) _−_ _βu_ _|_

_≤_ ¹

4



sup

_u_ _∈_ _I_

_|_ _u_ _| |_ _β_ _b_ _−_ _β_ _|_ \+ _β_ _b_ _|_ _δ_ _b_ _|_



_._

(19)

The uniform speed bound in Condition D.3 gives _β_ _b_ _|_ _δ_ _b_ _| ≤_ _β_ \+ _|_ _δ_ _b_ _|_ .

Averaging ( 19 ) over tasks and using

Assumptions D.1 and D.2 ,

1

_M_

_M_



_b_ =1

sup

_u_ _∈_ _I_

_|_ _ℓ_ _b_ ( _u_ ) _−_ _ℓ_ _β_ ( _u_ ) _| ≤_ ¹

4



sup

_u_ _∈_ _I_

_|_ _u_ _|_ _B_ _M_ \+ _β_ \+ _D_ _M_



_→_ 0 _._

(20)

Step 3: combine the two approximations. The triangle inequality gives

sup

_u_ _∈_ _I_

_|_ _x_ _B_ ( _u_ ) _−_ _ℓ_ _β_ ( _u_ ) _| ≤_ sup

_u_ _∈_ _I_

 _x_ _B_ ( _u_ ) _−_ 1

_M_

_M_



_b_ =1

_ℓ_ _b_ ( _u_ )



\+ ¹

_M_

_M_



_b_ =1

sup

_u_ _∈_ _I_

_|_ _ℓ_ _b_ ( _u_ ) _−_ _ℓ_ _β_ ( _u_ ) _|_ _._

The rst term converges to zero by ( 18 ); the second converges to zero by ( 20 ). This proves uniform convergence

in probability of _x_ _B_ to _ℓ_ _β_ on _I_ . Substituting _u_ = log( _t/t_ mid ) gives ( 17 ).

**How does the benchmark aggregate produce the empirical scaling law.** This is the theorem that corresponds

to the empirical scaling law. The aggregate averages many frontier expansion processes on task-specic graphs

to produce an emergent smooth curve in the many-task limit. For the convergence to hold, we need blockwise

cut mixing that ensures task-level product frontier growth rates, the small-score-unit condition that makes

jump noise vanish in the aggregate, and the midpoint and speed assumptions that prevent a mixture of

incompatible sigmoids.

Under these conditions, the benchmark average can nally converges to a single

log-sigmoid law in ( 17 ), instead of being merely S-shaped.

**D.4**

**Graph Self-similarity Induces Log Scale for Time Axis**

The previous subsections explain why frontier expansion gives logistic dynamics once progress is measured

in an eective learning coordinate. We now explain why this coordinate should often be logarithmic in raw

interaction time.

Recall that the frontier process already takes place on the model-conditioned task graph _G_ _K_ = ( _E,_ _E_ _K_ ) . An

edge _j_ _→_ _i_ exists means that an unlocked source node _j_ can help unlock a target node _i_ , with eld strength

(marginal improvement in scores) _K_ _ij_ . The weighted cut _C_ ( _L, U_ ) measures the total inuence crossing from

the unlocked set _U_ to the locked set _L_ .

36

The remaining question is how raw interaction time moves the agent through the latent task graph. The

answer we propose is graph-dependent and geometric: harder regions of the task graph require more search

eort to expose.

If this search geometry is approximately self-similar across diculty scales, then equal

additive increases in diculty require multiplicative increases in raw time. This is why the natural frontier

coordinate becomes log _t_ .

Denition D.11 (Diculty scale on task-graph edges) . For each inuence edge _j_ _→_ _i_ _∈ E_ _K_ , let

_ρ_ _ij_ _≥_ 0

be the diculty scale of that edge. Smaller _ρ_ _ij_ means that the inuence from _j_ to _i_ becomes usable at

lower search eort; larger _ρ_ _ij_ means that the inuence requires deeper search or longer interaction to become

usable.

For _r_ _≥_ 0 , dene the exposed inuence matrix

_K_ ( _≤_ _r_ )

_ij_

=



_K_ _ij_ _,_

if _j_ _→_ _i_ _∈ E_ _K_ and _ρ_ _ij_ _≤_ _r,_

0 _,_

otherwise.

The corresponding exposed eld is

_h_ ( _≤_ _r_ )

_i_

( _n_ ) =



_j_ _∈_ _E_

_K_ ( _≤_ _r_ )

_ij_

_n_ _j_ _._

Increasing _r_ reveals more of the same task graph. At small _r_ , only low-diculty edges contribute to the eld.

At larger _r_ , higher-diculty edges also contribute to the frontier cut. Thus _r_ is an eective coordinate for

how much of the task graph has become usable.

Denition D.12 (Search volume at diculty scale) . Let _k_ _∈_ N \+ index diculty levels, with level _k_ corre-

sponding to the scale band [ _k_ ∆ _r,_ ( _k_ \+ 1)∆ _r_ ) where ∆ _r >_ 0 . Dene the set of task-graph edges at level _k_

by

_E_ _k_ = _{_ _j_ _→_ _i_ _∈ E_ _K_ : _k_ ∆ _r_ _≤_ _ρ_ _ij_ _<_ ( _k_ \+ 1)∆ _r_ _}_ _._

Let _N_ _k_ = _|E_ _k_ _|_ be the number of edges whose diculty lies in this scale band. We interpret _N_ _k_ as a discrete

proxy of search-volume: it counts how much edge structure must be exposed at diculty level _k_ .

Search volume is dierent from score measure. score measure _µ_ measures how much benchmark value is

obtained once nodes are unlocked. Search volume measures how much task-graph structure must become

usable before the corresponding frontier inuence can appear.

Assumption D.3 (Self-similar task-graph edge growth) . There exist constants _b >_ 1 and _c_ _−_ _, c_ \+ _>_ 0 such

that, throughout the scale range of interest,

_c_ _−_ _b_ _k_ _≤_ _N_ _k_ _≤_ _c_ \+ _b_ _k_ _._

This assumption says that each additive increase in diculty level multiplies the amount of relevant task-

graph edge structure by a factor comparable to _b_ . Since level _k_ corresponds to scale _r_ _k_ = _k_ ∆ _r_ , this means

_N_ _k_ _≍_ _b_ _r_ _k_ _/_ ∆ _r_ = exp

 log _b_

∆ _r_ _r_ _k_



_._

We write

_h_ = log _b_

∆ _r_

for the corresponding search-entropy parameter. Informally, _h_ measures how quickly the amount of task-graph

structure grows as diculty scale increases.

The discrete assumption motivates the continuum approximation

_V_ ( _r_ ) = _V_ 0 _e_ _hr_ _,_

_V_ 0 _>_ 0 _,_

37

where _V_ ( _r_ ) d _r_ is the search eort needed to expose the task-graph edge structure in the diculty band

[ _r, r_ \+ d _r_ ] . Hence the cumulative search volume up to diculty scale _r_ is

_V_ ( _r_ ) =

 _r_

0

_V_ ( _s_ ) d _s_ = _V_ ⁰

_h_ ( _e_ _hr_ _−_ 1) _._

Assumption D.4 (Linear search-eort supply) . Let _A_ ( _t_ ) be the cumulative search eort supplied by raw

interaction time _t_ . Assume

_A_ ( _t_ ) = _νt_

for some _ν >_ 0 .

This assumption says that raw interaction time is proportional to available search eort. The search may be

adaptive, but one unit of raw time does not by itself expose exponentially many edges of the task graph.

Proposition D.1 (Self-similar task geometry gives logarithmic time) . Under Assumptions D.3 and D.4 , the

diculty scale exposed by raw time _t_ satises

_r_ ( _t_ ) = ¹

_h_ log



1 + _hν_

_V_ 0

_t_



_._

In particular, in the scale-free regime _t_ _≫_ _V_ 0 _/_ ( _hν_ ) ,

_r_ ( _t_ ) = ¹

_h_ log _t_ \+ _O_ (1) _._

The proposition is just the inversion of cumulative search volume. The scale _r_ ( _t_ ) is dened by _V_ ( _r_ ( _t_ )) =

_A_ ( _t_ ) . Since _V_ ( _r_ ) grows exponentially in _r_ while _A_ ( _t_ ) grows linearly in _t_ , the exposed diculty scale grows

logarithmically in raw time.

Connection to the frontier law. The earlier frontier law describes score growth once progress is measured in

the coordinate that makes task-graph inuence usable. Here that coordinate is _r_ . As _r_ increases, more entries

of _K_ are exposed through _K_ ( _≤_ _r_ ) , the eld _h_ ( _≤_ _r_ )

_i_

grows, and the frontier cut from unlocked nodes to locked

nodes expands through the same mechanism as before.

If the exposed task graph is approximately weighted cut-mixed at each scale, with a scale-stationary eective

frontier coecient, then the coarse frontier dynamics in the scale coordinate take the product form

d _x_

d _r_ = _γx_ (1 _−_ _x_ ) _,_

where _γ >_ 0 is the frontier speed per unit diculty scale. This is the earlier weighted-cut frontier mechanism

written in the coordinate _r_ .

Since _r_ ( _t_ ) = _h_ _−_ ¹ log _t_ \+ _O_ (1) in the scale-free regime, a unit increase in log _t_ corresponds to approximately

1 _/h_ units of diculty-scale progress. Therefore

d _x_

d log _t_ = _γ_

_h_ _x_ (1 _−_ _x_ ) _._

Thus the tted log-time frontier speed is

_β_ = _γ_

_h_ _._

Solving the log-time logistic equation gives

_x_ ( _t_ ) =

1

1 + ( _t_ mid _/t_ ) _β_ _._

38

**Why self-similar task geometry gives log time.**

The weighted-cut argument explains the frontier factor

_x_ (1 _−_ _x_ ) , as previously shown. Self-similar task-graph geometry explains why the time coordinate is measured

by log scale. If each additive increase in diculty scale multiplies the number of relevant task-graph edges by

a factor _b_ , then search volume grows like _e_ _hr_ , where _h_ = (log _b_ ) _/_ ∆ _r_ . Since raw interaction time supplies only

_O_ ( _t_ ) search eort, the exposed diculty scale satises _r_ ( _t_ ) = _h_ _−_ ¹ log _t_ \+ _O_ (1) . Therefore a logistic frontier

law in task-graph scale becomes a logistic law in log _t_ .

**D.5**

**Discussion and Limitations**

The derivation above gives a sucient mechanism for the empirical log-sigmoid law. Its assumptions are

useful precisely because they identify concrete ways in which the log-sigmoid limit can fail. We therefore

treat it as a mechanistic account of the observed regime rather than a claim that all environment-learning

curves must be logistic.

Finite score granularity.

The single-task theory allows nite tasks to remain visibly jagged. Real tasks may

contain a few large hidden tests, decisive proof obligations, or high-weight rubric cells. When such score units

remain macroscopic, the martingale error term need not vanish for that task, and the realized best-so-far

curve can exhibit long plateaus followed by sudden jumps. The aggregate theorem only requires that such

coarse units do not dominate the benchmark average. If a non-negligible fraction of benchmark score measure

is carried by coarse tasks, the aggregate curve may retain visible jumps or large run-to-run variance even

when the average drift is approximately logistic.

Weighted cut mixing.

Weighted cut mixing is the core condition of the scaling law.

It says that every

macroscopic unlockedlocked frontier cut sees approximately product-measure inuence. If the task graph

has persistent bottlenecks, modules, prerequisite chains, or separated high-transfer and low-transfer regions,

then the frontier remembers where it is in the graph, not only how much score measure has been unlocked. In

that case, the natural limit is no longer a one-dimensional logistic equation. One should instead expect multi-

type dynamics, delayed takeo, multiple inection regions, long plateaus, or a sum of sigmoids corresponding

to dierent task modules.

Attainable support and the tted ceiling.

The analysis treats _S_ max as the stable score measure of an eective

reachable support. This is appropriate when the set of practically attainable score units is xed over the

tted time window. However, if longer interaction changes what is eectively reachablefor example, if weak

transfer routes become usable only at much longer horizonsthen the denominator of the normalized score

is itself moving. A short-window t may still provide a useful eective ceiling, but that ceiling should not be

interpreted as an indenite upper bound.

Task midpoint alignment.

The aggregate theorem assumes that a single benchmark-level midpoint removes

most task-level log-time bias. If residual midpoint shifts _δ_ _b_ remain widely dispersed, the benchmark average

becomes a convolution of shifted task frontiers. Such a curve may still be smooth and S-shaped, but it

need not satisfy the scalar logistic ODE. In this regime, the tted midpoint and slope are window-dependent

summaries of the task-midpoint distribution rather than intrinsic benchmark constants.

Learning-speed concentration.

The aggregate theorem also assumes that task frontier speeds concentrate

around a common value. If some task families have persistently steep frontiers while others have persistently

shallow frontiers, then the average of task-level sigmoids is generally not itself a sigmoid. Early progress may

be dominated by fast tasks, while later progress may be governed by slower tasks. A single tted _β_ may

therefore reect task-family composition rather than a true scalar environment-learning speed.

Choice of time coordinate.

The log-time coordinate is justied by the graph self-similarity hypothesis in

which unit increments of diculty require multiplicative increases in search eort.

Some environments,

however, have characteristic raw-time cycles: xed evaluation delays, daily data refreshes, hard deadlines,

39

staged curricula, or batch feedback. In such cases, another time coordinate, or a piecewise time model, may

be more appropriate than a single log-time transformation.

Together, these limitations clarify the scope of the proof. The appendix gives one route from frontier ex-

pansion to the observed population-level log-sigmoid law.

A fuller theory would classify the non-logistic

limits produced by coarse score units, non-mixing graphs, moving attainable supports, dispersed midpoints,

heterogeneous learning speeds, and non-scale-free feedback schedules.

**E**

**More Discussion on the Scaling Law Shapes**

A mechanistic reading selects the log-sigmoid. Because the candidate S-curves t almost equally well (Table 1 ;

the log-sigmoid/log-probit degeneracy has been known since Berkson [ 6 ]), the choice cannot rest on t; we

make it on mechanism. Written as a growth law for the normalized score _y_ = _S/S_ max , each candidate's rate

makes a dierent statement about what drives progress and what limits it.

ˆ **Log-sigmoid:**

_dy_

_dτ_ = _β y_ (1 _−_ _y_ ) in log time _τ_ = ln _t_ . The detailed derivation is given in Section 3\.3 and

Appendix D ; here the key mechanistic reading is that _y_ is the unlocked attainable score mass and 1 _−_ _y_

is the remaining locked score mass. If the aggregate inuence crossing the unlockedlocked frontier is

approximately proportional to the product of these masses, then progress follows _y_ (1 _−_ _y_ ) . The log-time

coordinate comes from the self-similar search geometry of the task graph. This reading is consistent

with two empirical checks: Section 5\.2 shows that continuous stateful runs outperform equal-budget

repeated sampling, so progress is not explained by independent attempts alone; and Section 5\.4 shows

a nite task advancing through sparse but cumulative breakthroughs, where an early working pipeline

makes later repairs searchable. Inection occurs at _y_ = 0 _._ 5 (symmetric).

ˆ **Log-Gompertz:**

_dy_

_dτ_ = _c y_ ln(1 _/y_ ) . The ln(1 _/y_ ) term is the signature of an engine that winds down

multiplicatively as the system matures (e.g., tumour growth, where the proliferating fraction shrinks).

It is front-loaded, with inection at _y_ = 1 _/e_ _≈_ 0 _._ 37 : the relative growth rate diverges as _y_ _→_ 0 , so a tiny

system grows explosively because the limitation it will eventually hit does not yet exist. Experience

acquisition is the oppositeits early phase is slow because a foothold must rst be bootstrapped, not

fast for lack of a brake.

ˆ **Log-Probit:**

_dy_

_dτ_ =

1

_σ_ _φ_



Φ _−_ ¹ ( _y_ )



, a sweep across a log-normal distribution of dicultiesdiculties

formed as products of many independent factors (a multiplicative central-limit argument). Experience

acquisition is path-dependent rather than a product of independent factors, so this microfoundation

does not apply, even though probit and the logistic are empirically near-indistinguishable.

ˆ **Weibull CDF:** _y_ ( _t_ ) = 1 _−_ exp _{−_ ( _t/λ_ ) _β_ _}_ , equivalently _dy_

_dt_ = _h_ ( _t_ )(1 _−_ _y_ ) with _h_ ( _t_ ) = _β_

_λ_ ( _t/λ_ ) _β_ _−_ ¹ . Its hazard is

a function of raw elapsed time, while accumulated progress enters only through the survival term (1 _−_ _y_ ) .

This makes it the natural rst-passage or repeated sampling baseline. For a single 01 reward task with

independent attempts of success probability _p_ , _P_ pass ( _k_ ) = 1 _−_ (1 _−_ _p_ ) _k_ = 1 _−_ exp[ _−_ _k_ ( _−_ ln(1 _−_ _p_ ))] , which

is an exponential CDF, the _β_ = 1 Weibull case (approximately 1 _−_ exp( _−_ _pk_ ) for small _p_ ). Such a curve

improves because repeated independent attempts shrink the remaining failure mass, not because state

carried across attempts makes later attempts more eective. Section 5\.2 shows that stateful learning

beats this repeated-sampling mechanism under the same total budget, and the Weibull CDF also ts

worse than the log-sigmoid in Table 1 . Individual improvements may have a rst-passage avor, but the

macroscopic best-so-far trajectory accumulates through dependent, stateful steps rather than through

a raw-time hazard with no accumulated-progress factor.

ˆ **Log-linear:**

_dy_

_dτ_ = _b_ (constant). With no saturating term it grows without bound and cannot level o,

contradicting the many tasks that reach a ceiling within the budget; it attains by far the worst t.

We therefore read the log-sigmoid not merely as the best-tting S-curve but as the curve whose _y_ (1 _−_ _y_ ) rate

law matches the frontier-expansion interpretation: unlocked score mass supplies reusable capability, while

locked score mass bounds the remaining opportunity for improvement. This is a mechanistic preference,

not an empirical exclusionthe data cannot separate the symmetric families. It is falsiable through the

40

inection: a symmetric peak near _y_ = 0 _._ 5 is consistent with the logistic (and probit), a front-loaded peak

near 0 _._ 37 would favor Gompertz, and a back-loaded peak near 0 _._ 63 would favor Weibull.

**F**

**Additional Related Work**

**F.1**

**Benchmarks Not Suitable for Measuring Self-Evolution**

Many benchmarks evaluate whether models or agents can answer questions, complete tasks, or produce

correct artifacts, without making self-evolution itself the object of measurement. We use this label in a narrow

evaluation sense: these benchmarks may still involve reasoning, tools, iteration, or environment interaction,

but their primary reported quantity is not related to learning.

It is usually nal-answer accuracy, task

success, pass rate, artifact quality, reproduction delity, or human-time horizon. In such settings, interaction

is typically a means to produce a nal answer or artifact, rather than the quantity being measured.

At the shortest and least interactive end, many classic capability benchmarks, such as MMLU [ 29 ], GPQA [ 62 ],

AIME [ 45 ], and closed-form coding or math evaluations [ 11 , 30 ], ask models to solve static problems and

report nal accuracy. These benchmarks can be dicult and useful, but the model's actions do not create a

changing environment, and feedback from the benchmark is not exposed as experience for later adaptation.

They therefore measure static knowledge and reasoning accuracy rather than self-evolution.

Agentic software benchmarks increase realism by placing agents in codebases, development workows, or

larger construction tasks, but many still reduce evaluation to the nal result. SWE-bench [ 35 ] evaluates

issue repair in existing repositories; development and evolution benchmarks such as RoadmapBench [ 80 ] and

SWE-EVO [ 70 ] evaluate incremental changes over existing projects or release histories; construction or re-

construction benchmarks such as NL2Repo-Bench [ 18 ] and ProgramBench [ 82 ] evaluate complete repository

generation or recovery of program behavior; and SWE-AGI [ 86 ] evaluates specication-driven system con-

struction under a xed MoonBit API scaold. FrontierCode [ 41 ] raises the bar on readiness for production by

evaluating whether coding agents produce maintainable, mergeable changes under repository-specic quality

rubrics. Their task formats dier, but the shared evaluation target is nal patch correctness, repository

quality, program behavior, maintainability, or test pass rate rather than the trajectory by which an agent

improves from feedback.

Some evaluations broaden realism without becoming agentic learning benchmarks. GDPval [ 60 ], for example,

measures model performance on economically valuable professional deliverables across occupations. Agents'

Last Exam [ 69 ] is a close comparator in realism and autonomy: it evaluates generalist computer-use agents

on economically valuable professional workows in real Windows or Linux sandboxes, with CLI and GUI

access, professional software, hidden references, and veriable nal artifacts. The distinction is the evaluation

target rather than agenticity. Agents' Last Exam is oriented toward completion: agents work toward a nal

deliverable, and the benchmark reports nal scores, pass rates, cost, or time after the artifact is graded. Its

trajectories are valuable for replay, audit, and failure analysis, but learning from the benchmark's feedback

over a run is not the main quantity being measured.

Other benchmarks use realistic or long-horizon workows that could support learning, but their published

protocols mainly measure nal outcomes. HCAST [ 63 ] and METR time-horizon evaluations [ 38 ] calibrate

model or agent success by human task duration.

Terminal-Bench [ 46 ], RE-Bench [ 76 ], PaperBench [ 68 ],

CORE-Bench [ 66 ], PRBench [ 61 ], ReplicationBench [ 83 ], Collider-Bench [ 23 ], and ScienceAgentBench [ 12 ]

involve executable software tasks, terminal workows, or scientic reproduction. These settings are more

compatible with learning than short closed-form tasks, but their central questions are typically whether a

task is completed, an artifact works, a paper is reproduced, or a nal score is high enough under a budget.

PaperBench is a useful example of the distinction: it evaluates agentic replication of 20 ICML papers from

scratch using detailed rubrics and many gradable subtasks, but the reported score is still replication quality

rather than improvement per unit of feedback.

41

**F.2**

**Benchmarks Suitable for Measuring Learning or Self-Evolution**

Another line of work is more suitable for measuring learning or self-evolution because it exposes new context,

serialized streams, iterative feedback, or long executable workspaces.

These benchmarks are the closest

conceptual comparisons to EdgeBench, but they dier in what creates the experience stream and what

quantity is ultimately scored. We group them by evaluation interface: learning from supplied context, learning

over serialized streams or task sequences, and iterative optimization. This grouping is descriptive rather than

an ordering by interaction strength.

Sequential benchmarks can be highly interactive, and optimization

benchmarks can expose diagnostic feedback; the key question is whether the agent's own behavior shapes the

future experience it receives within a long executable task.

Context-learning benchmarks study the least agentic form of adaptation.

CL-bench [ 21 ] and CL-bench

Life [ 20 ] test whether models can use newly provided professional or personal context to answer downstream

questions or perform tasks grounded in that context. This counts as learning from external information, but

the stream of episodes is usually not shaped by the agent's own actions, and there is no changing environment.

The model is asked to use context, not to discover and exploit feedback through sustained interaction.

Sequential learning benchmarks introduce a stream-like structure. EvaLearn [ 19 ] groups 648 problems into 182

sequences and evaluates learning capability and eciency as models solve related problems in order. Continual

Learning Bench [ 4 ] explicitly reports improvement over sequential experience and introduces a stateful-versus-

stateless comparison similar to Section 5\.2 .

However, its synthetic task sequences have explicit subtask

boundaries, whereas EdgeBench uses single continuous problems. We therefore partition by time rather than

by subtask, which changes how the stateful and stateless settings are dened. StreamBench [ 78 ] also reports

improvement over feedback streams. LLF-Bench [ 13 ], LifelongAgentBench [ 87 ], and Evo-Memory [ 73 ] study

related questions through language feedback, interdependent tasks, experience replay, or evolving memory.

These works establish that static capability and learning ability are distinct axes.

The dierence from

EdgeBench is not that their interaction is necessarily weaker; rather, the sequence is usually organized by the

benchmark as a series of instances, tasks, feedback events, or memory updates. In EdgeBench, the sequence

is endogenous to one long task: the agent plans, edits artifacts, submits attempts, receives diagnostics, and

thereby aects what it learns next.

Iterative optimization benchmarks are closer to EdgeBench because they make repeated attempts and em-

pirical feedback central to performance. Frontier-Eng [ 14 ] studies improvement over generative optimization

cycles, while MLS-Bench [ 42 ] and Frontier-CS [ 43 ] evaluate test-time discovery or open-ended CS optimiza-

tion with visible metrics, submissions, or trajectory-level reporting. MLE-bench [ 10 ] is also naturally viewed

in this family: agents work in a free Kaggle-style workspace, the paper includes studies of how performance

scales with resources, and its 100-hour analysis grades snapshots of the agent's best attempt over elapsed

time. ALE-Bench [ 34 ] is another adjacent long-horizon setting driven by xed objectives, even though its

original protocol primarily reports outcomes on algorithm engineering rather than learning metrics.

FrontierSWE [ 15 ] and AutoLab [ 81 ] are the closest prior work. Both evaluate long-horizon agentic improve-

ment over executable artifacts through repeated edits, experiments, and empirical feedback. FrontierSWE

focuses on software engineering and performance-tuning tasks, with reported average agent runtime of roughly

34 hours across models and task categories. AutoLab gives agents working but deliberately suboptimal pro-

grams across systems, CUDA, model development, and puzzle-style optimization tasks; it directly measures

iterative improvement and should not be treated as a non-learning benchmark, although performance curves

are not reported as the main result and most current tasks run for 24 hours, with only a small minority

exceeding 6 hours. Under the shared premise of long-horizon agentic tasks, the main distinction is domain cov-

erage: FrontierSWE is concentrated on software engineering, AutoLab emphasizes research and engineering

tasks centered on optimization, and EdgeBench spans a broader set of executable domains. EdgeBench also

uses a day-scale task contract and makes the time-aligned trajectory itself the primary object of measurement,

with metrics for improvement area, regression, and active learning span.

Taken together, these benchmarks cover important pieces of the problem: realistic executable work, learning

over organized streams, and iterative optimization under feedback. EdgeBench targets their intersection.

It evaluates within-run self-evolution in long-horizon executable environments where the experience stream

42

arises from the task itself, the agent can inuence what it observes next, and evaluation uses a general-

purpose agent harness rather than a benchmark-specic learning scaold. Its trajectory-level metrics report

improvement, regression, active learning span, and nal performance over the same continuous run.

**F.3**

**Scaling Laws for LLMs and Agents**

Classical neural and language-model scaling laws mainly study pretraining, modeling reducible loss as a func-

tion of model size, data, and training compute. Kaplan et al. [ 36 ] showed that language-modeling loss follows

power-law relationships over several axes of scale, and Chinchilla-style work rened the compute-optimal

allocation between model parameters and training tokens [ 32 ]. More recent work studies how benchmark

performance, rather than loss, changes with scale; because accuracy-like metrics are bounded, these curves

are often better described by sigmoidal or other saturating forms [ 7 , 59 , 64 , 85 ]. Our log-sigmoid environment

learning curves in Section 3 are closest in mathematical form to this bounded-performance line of work, but

the independent variable is elapsed environment interaction within a task rather than pretraining compute

or model scale.

Test-time and inference-time scaling provide a second point of comparison: dierent test-time methods exhibit

their own empirical scaling behavior. One line scales plain repeated sampling: Evaluating Large Language

Models Trained on Code introduced pass@ _k_ as a repeated-sampling evaluation for code generation [ 11 ],

AlphaCode used large-scale sampling, ltering, and selection to improve competitive-programming solve

rates [ 40 ], and Large Language Monkeys showed that repeated sampling can scale coverage across orders

of magnitude when outputs are automatically veriable [ 9 ]. A second line studies how test-time compute

should be allocated across search, revision, voting, and verier- or reward-guided strategies [ 67 , 79 ].

A

third line scales long-chain-of-thought inference in reasoning models: OpenAI's o1 report made train-time

reinforcement learning compute and test-time thinking compute explicit scaling axes [ 50 ], and DeepSeek-R1

studies how reinforcement learning can elicit reasoning behaviors in LLMs [ 16 ]. These studies mostly scale

the compute spent producing or selecting answers on traditional math, code, proof, or game-style tasks,

and the reported functional forms are often local log-linear trends, exponentiated power laws, or frontiers

for allocating compute. EdgeBench instead scales interaction time : it measures how an agent's best-so-far

performance changes as elapsed time in an executable environment increases and as the agent repeatedly

reads, acts, receives feedback, and revises. This gives broader task coverage and a dierent scaling object

than sampling from a static prompt or selecting among answers.

Recent agentic test-time scaling work moves closer to our setting by allowing agents to acquire information

from an environment over time. OpenAI's CUA report observed that computer-use performance improves

when more steps are allowed [ 52 ], and BrowseComp reports smoother gains as browsing eort increases [ 72 ].

Thinking vs. Doing explicitly frames interaction length as a test-time scaling axis for web agents [ 65 ]. Closest

in spirit, Mang et al. [ 44 ] compare agents and humans on a long-horizon coding contest setting where agents

can try, observe, and revise over time. They report an informative human reference curve and nd that current

agents plateau while strong humans continue improving. However, the measurement is concentrated in one

contest-style domain and a limited task set. The human improvement curve is also dicult to extrapolate:

the observed segment appears closer to linear improvement over time, but it may cover only the early portion

of a longer sigmoid-like trajectory.

Scaling has also been studied in reinforcement learning. Hilton et al. [ 31 ] introduced intrinsic performance

to obtain smooth power-law relations between environment interactions, model size, and RL performance.

Recent LLM RL scaling work ts sigmoidal compute-performance curves for post-training and uses smaller

runs to predict larger RL runs [ 37 ]. Both RL and our evaluation measure learning from environment feed-

back rather than from human-labeled data. The practical dierence is resolution and coverage. RL learning

runs are expensive, so scaling evidence is usually gathered on narrower task distributions, fewer distinct

environments, and fewer long trajectories. In EdgeBench, the learning algorithm is in-context learning (ICL):

the agent absorbs observations, diagnostics, and prior attempts into its context and uses them to improve

subsequent actions. Because ICL is cheaper to repeat than RL training, EdgeBench can measure environ-

ment learning across 134 executable task environments, multiple domains, full time-aligned trajectories, and

repeated trials, yielding substantially broader environment coverage than is typical in RL scaling studies.

43

The resulting ts go beyond a bounded-performance analogy to RL scaling: they provide a higher-resolution

measurement of how agents learn from interaction.

**G**

**Additional Benchmark and Experiment Details**

**G.1**

**Estimating the With- and Without-Experience Curves**

This describes how the two curves in Section 5\.2 are estimated. The with-experience curve averages three 12-

hour best-so-far curves per task, then averages across tasks. For the without-experience curve, let _u_ 1 _, . . . , u_ _n_

be the scores of the _n_ independent attempts on a task; at elapsed time _t_ = _kτ_ we estimate the expected best

of _k_ attempts as

ˆ _u_ _kτ_ = E _S_



max

_i_ _∈_ _S_ _u_ _i_



_,_

(21)

where _S_ is sampled uniformly from the

 _n_

_k_



size- _k_ subsets of the _n_ attempts. This is the score-valued, without-

replacement extension of the pass@ _k_ estimator [ 11 ]; when each _u_ _i_ is binary, it reduces to the usual pass@ _k_

estimate.

**G.2**

**Gravitational-Wave Case Study Details**

**The selected milestones compress the run into interpretable phase transitions.** Table 4 summarizes the main

phases behind the selected milestones rather than every submission. The rst selected milestone already

passes the protocol and entrypoint checks, generates all ve required CSV les on the canonical grids, and

obtains a score of 42.8. A subsequent key update raises the score to 47.1, mainly by improving the source dy-

namics. Around hour 1, another milestone reaches roughly 50 as the agent improves the H1/L1 spectrograms

and early H1 alignment in the time domain. These gains reect standard signal processing: ltering, normal-

ization, windowing in the time-frequency plane, interpolation to the canonical grid, and cropping around the

event.

**The largest score gain comes from the high-weight source-dynamics component.** The largest jump occurs

around hours 45: the overall score rises from about 52.3 to 59.7, driven almost entirely by the source

dynamics subscore (64.2 to 89.0). Because this subtask carries the largest weight, a compact physical model

plus calibration produces a large total-score gain. After that point, the agent shifts to H1 waveform tuning,

where the H1 time-series subscore climbs from roughly 47 to 95 by the end.

**The final solution is strong on H1 waveform and source dynamics, but it still leaves room to improve**

**toward a human-standard LIGO-style analysis.**

Table 5 breaks down the nal score.

GPT-5.5 scores

high on H1 waveform reconstruction and the source dynamics but remains weak on the spectrograms and

L1 reconstruction. Empirical calibration and parameter search produce a substantial score, but they do

not replace a coherent end-to-end pipeline for strain preprocessing, whitening, time-frequency analysis, and

waveform alignment across detectors.

44

Stage

Time

Best score

Main improvement

Initial milestones

0h

42\.847.1

Built a reconstruction pipeline that can be evaluated; re-

placing a noisy frequency estimate improved the inferred

source motion from 51 to 64 ( **\+13 pp.** )

Early signal processing

14h

52\.3

Recentered the time-frequency window on the merger; the

Hanford detector waveform and both detector spectrograms

improved together, raising the best score from 47.1 to 52.3

( **\+5.2 pp.** )

Main breakthrough

45h

59\.7

Calibrated the binary-source model; the orbital velocity

and separation score jumped from 64 to 89 ( **\+25 pp.** )

Late waveform tuning

511.5h

66\.9

Found the remaining mismatch in the Hanford detector

waveform; time-shift alignment and error tting raised Han-

ford from 47 to 95 ( **\+48 pp.** )

Final renement

12h

67\.0

Consolidated nal corrections for the Hanford and Liv-

ingston detectors; a small Livingston waveform gain raised

the aggregate score from 66.9 to 67.0 ( **\+0.1 pp.** )

**Table 4** Main phases in the gravitational-wave evolving trajectory. The trajectory shows how the agent renes signal

processing, source dynamics, and per-detector waveform reconstruction over the 12-hour run.

Component

Final subscore

H1 time series

95\.0

L1 time series

57\.1

H1 spectrogram

42\.7

L1 spectrogram

44\.7

Velocity/separation

89\.0

Aggregate score

67\.0

**Table 5** Final subscore composition for the GPT-5.5 gravitational-wave 12h run.

45

**Task**

**GPT-5.5**

**GPT-5.4**

**Base**

**w/ Goal**

**w/ Ralph**

**Base**

**w/ Goal**

**w/ Ralph**

portfolio\_risk\_calibration

25 _._ 0

27 _._ 5

**34** **_._** **3**

10 _._ 7

**19** **_._** **8**

12 _._ 2

storyboard\_ad\_copywriting

77 _._ 0

88 _._ 3

**97** **_._** **3**

65 _._ 7

78 _._ 0

**83** **_._** **3**

arc\_compiler\_runtime

**72** **_._** **4**

70 _._ 6

52 _._ 6

50 _._ 0

47 _._ 2

**51** **_._** **2**

battery\_soh\_rul\_anomaly

30 _._ 2

23 _._ 8

**48** **_._** **8**

**14** **_._** **7**

14 _._ 6

13 _._ 4

borden\_source\_inversion

38 _._ 5

32 _._ 8

**62** **_._** **2**

8 _._ 0

17 _._ 3

**23** **_._** **2**

capecod\_plume\_reconstruction

16 _._ 4

16 _._ 0

**17** **_._** **3**

12 _._ 6

13 _._ 3

**13** **_._** **7**

combinatorial\_games\_formalization

38 _._ 2

**45** **_._** **3**

39 _._ 8

17 _._ 8

13 _._ 0

**20** **_._** **2**

ffmpeg\_swscale\_reimplementation

15 _._ 3

16 _._ 4

**25** **_._** **2**

13 _._ 9

**28** **_._** **3**

21 _._ 8

flt\_regular\_formalization

**75** **_._** **1**

66 _._ 7

58 _._ 6

**48** **_._** **3**

43 _._ 7

43 _._ 7

git\_rewrite\_in\_zig

18 _._ 4

20 _._ 5

**22** **_._** **0**

15 _._ 4

**18** **_._** **4**

15 _._ 8

tryst\_text\_adventure

55 _._ 7

**56** **_._** **2**

40 _._ 2

**44** **_._** **3**

32 _._ 9

42 _._ 4

openttd\_transport\_ai

28 _._ 1

**39** **_._** **8**

30 _._ 6

**11** **_._** **9**

1 _._ 2

8 _._ 1

pocketbase\_backend\_architecture

**62** **_._** **5**

**62** **_._** **5**

41 _._ 7

20 _._ 8

**54** **_._** **2**

0 _._ 0

symbolic\_integration\_engine

**44** **_._** **0**

36 _._ 6

37 _._ 7

30 _._ 9

**63** **_._** **7**

37 _._ 2

**Avg.**

42 _._ 6

43 _._ 1

**43** **_._** **4**

26 _._ 1

**31** **_._** **8**

27 _._ 6

**Table 6** Harness-level continuation ablation of /goal mode and the Ralph loop. GPT-5.5 and GPT-5.4 are evaluated

with Base, Goal, and Ralph settings under the same 12-hour budget; each value is the mean score over valid runs,

and the Avg. row averages the displayed task rows. Incomplete cells are detailed in Appendix G.3 . Bold marks the

best setting and underlining marks the second-best setting.

**G.3**

**Harness-Level Continuation Ablations**

Long-running agent evaluation depends not only on model capability, but also on how the harness keeps

the run alive and carries useful state across many hours. In a 12-hour task, an agent may stop its running

unexpectedly due to idleness and need to resume. These continuation mechanisms are therefore part of the

practical measurement setup: a weak scaold can make a capable model stop working on the task, while

a stronger scaold may help the same model keep active and improving. As a supplementary harness-level

ablation, we evaluate two such mechanisms, /goal mode and the Ralph loop, under a xed 12-hour budget

with GPT-5.5 and GPT-5.4.

Base uses the standard harness: one continuing agent session, a stop hook to prevent voluntary early exit,

and auto-resume for abnormal exits. In /goal mode [ 56 ], the harness prompts the agent to create a task-level

goal at the beginning, keep it active during the run, and mark it complete only when the task is validated.

The Ralph loop follows the le-backed fresh-context pattern [ 33 ]: each loop starts a new agent invocation on

the same workspace, asks it to read and update progress.md, then appends judge feedback to that le before

the next loop. It uses up to 100 loops, a 7200-second per-loop cap, and the same 12-hour overall budget.

Each cell schedules three runs and reports the mean score over valid runs.

As shown in Table 6 , the goal mode and the Ralph loop often outperform the base setting, suggesting that

long-horizon agents benet from harness support that preserves and updates task state across extended runs.

In the displayed-task average, GPT-5.5 improves from 42.6 in Base to 43.1 with Goal and 43.4 with Ralph,

while GPT-5.4 improves from 26.1 in Base to 31.8 with Goal and 27.6 with Ralph. The gains are not uniform

across all tasks and models, so we treat this as an appendix-level harness diagnostic rather than a main

result.

Most cells use all three scheduled runs. A few GPT-5.4 cells have fewer valid runs because of intermittent

API or network instability: one-run cells are w/ Goal for storyboard\_ad\_copywriting and flt\_regular\_

formalization , plus w/ Ralph for symbolic\_integration\_engine ; two-run cells are battery\_soh\_rul\_

anomaly (w/ Goal and w/ Ralph), capecod\_plume\_reconstruction (w/ Goal), combinatorial\_games\_

formalization (w/ Ralph), ffmpeg\_swscale\_reimplementation (w/ Goal), flt\_regular\_formalization

(w/ Ralph), git\_rewrite\_in\_zig (w/ Goal), and symbolic\_integration\_engine (w/ Goal). All reported

GPT-5.5 cells use the full three runs.

46

**G.4**

**Per-Task Design Notes**

This appendix gives per-task design notes for the 134-task EdgeBench suite.

Task

Design notes

Systems & Software Engineering

ann\_vector\_search\_qps

Replace a brute-force NumPy nearest-neighbor baseline with a high-performance approximate

nearest-neighbor implementation under a hard recall constraint. Scored by queries per second.

arc\_compiler\_runtime

Implement a complete TypeScript compiler pipeline (lexer, parser, type checker, code generator) for a

novel programming language dened by specication documents.

rust\_multicrate\_

reconstruction

Reconstruct missing Rust implementations across a multi-crate content-addressable storage workspace,

given only type signatures and public API contracts.

codeflash\_repair\_

performance

Diagnose and repair intentionally degraded modules in a Python code-optimization tool spanning CST

manipulation, proling infrastructure, and test harness integration. Scored on both functional

correctness and runtime performance.

copier\_modular\_refactor

Implement six architectural targets in the Copier Python scaolding library: structured exceptions,

template management, version compatibility, rendering modes, a worker class, and a user-data layer.

dependent\_type\_checker

Build a complete dependent type checker in Rust for a subset of Martin-Löf Type Theory, supporting

cumulative universes, Pi/Sigma types, general inductive types with positivity checking, and universe

polymorphism. Scored on both correctness and normalization throughput.

entt\_graph\_module

Implement seven feature targets in the EnTT C++ entity-component-system framework, including a

graph module with adjacency matrix, a task-graph builder with transitive reduction, DOT export, and

several core utility additions.

exchange\_core\_throughput

Maximize peak throughput of a Java nancial matching engine built on the LMAX Disruptor by tuning

thread topology, wait strategies, ring-buer sizing, order-book implementation, and JVM conguration.

ffmpeg\_swscale\_

reimplementation

Reimplement FFmpeg's libswscale pixel-format conversion and scaling library in Rust, handling

multiple pixel formats and scaling algorithms. A correctness-passing scaold is provided; the agent

must optimize for speed via SIMD.

git\_rewrite\_in\_zig

Reimplement git as a drop-in Zig binary producing identical CLI output, exit codes, and repository

state as the C reference implementation. The C source is available for reading but cannot be compiled.

high\_performance\_object\_

mapper

Implement a .NET object-to-object mapping library using expression-tree compilation and IL emission,

handling at/nested mapping, collections, custom type converters, nullables, and inheritance

hierarchies.

integer\_compression\_codec Improve a C++ integer compression codec for better compression ratio and decode throughput on

uint32 datasets via techniques such as delta encoding, bit-packing, and SIMD vectorization. Exact

round-trip correctness is mandatory.

juliet\_vulnerability\_

analyzer

Implement a deterministic static analyzer that processes structured program facts to detect

vulnerabilities across six CWE categories (stack/heap overow, integer overow, null dereference,

use-after-free, command injection).

libexpat\_x86\_assembly

Reimplement the libexpat XML parser entirely in x86-64 assembly, producing an ABI-compatible

shared library. No C compiler is availableonly assembler, linker, and libc.

odata\_query\_service

Complete a .NET OData query processing library: query-string parsing, LINQ expression-tree

generation for ltering, multi-eld sorting, pagination, eld projection, and ASP.NET Core middleware

integration.

litestar\_infra\_refactor

Implement ve async infrastructure subsystems in the Litestar Python web framework: key-value stores

with expiry, an event bus, WebSocket listener abstractions, a DTO framework, and a channels pub/sub

system.

lua\_native\_compiler

Build a Lua 5.4 ahead-of-time native compiler that reads Lua source and emits standalone ELF

executables with real x86-64 machine codenot C API call sequences or bytecode dispatch loops.

Output must match the reference interpreter byte-for-byte.

mimesis\_modular\_refactor

Implement seven refactoring targets in the Mimesis Python fake-data library: a declarative schema

class, an enum system with metaclass-driven random selection, and ve data providers spanning

payments, cryptography, science, internet, and unit systems.

nlohmann\_json\_

modularization

Implement ve feature targets in the nlohmann/json C++ library: UBJSON binary serialization, JSON

Merge Patch (RFC 7386), Grisu2 shortest-representation oat formatting, a range-based iteration

interface, and library metadata macros.

notebook\_lossless\_

compression

Build a lossless compression pipeline for Jupyter notebooks with a training phase (dictionary learning

from a visible corpus) and per-le compression/decompression. Scored by overall compression ratio;

byte-exact reconstruction is mandatory.

packer\_plugin\_datasources Implement six targets in HashiCorp Packer's Go plugin ecosystem: address parsing with DNS

validation, lesystem-based plugin discovery with checksum verication, HCL2 data-block integration,

sensitive value handling, and new template functions.

pocketbase\_backend\_

architecture

Implement four architectural targets in PocketBase (Go): a chain-based hook/event system, an HTTP

router with middleware stacking, a dynamic OAuth2 provider registry, and a regex-based random string

generator.

pocketbase\_tools\_

extensions

Implement four Go utility packages for PocketBase: a REST JSON serializer with nested eld picking,

a zip archive utility, a cron scheduler with timezone support, and a SQL index parser/builder.

postgres\_wire\_on\_sqlite

Implement a server that speaks the PostgreSQL wire protocol (v3) using SQLite as the storage backend,

handling authentication, simple and extended query protocols, type mapping, transactions, and system

catalog queries. Scored by pass rate on PostgreSQL's own test suites.

quic\_transport\_stack

Implement a subset of the QUIC transport protocol (RFC 9000): connection establishment, TLS 1.3

key derivation, AEAD encryption, packet number encoding, header protection, and core frame types.

Continued on next page

47

Task

Design notes

regex\_automata\_repair

Repair broken implementations in Rust's regex-automata crate spanning NFA compilation, DFA

transition construction, Unicode handling, capture groups, and the hybrid matching engine.

schemathesis\_datagen\_

pipeline

Implement eight feature targets in the Schemathesis Python API testing framework, including

structured HTTP header generation strategies, coverage-phase hooks, discriminator-aware validation

and data generation, and schema-driven code generation xes.

schemathesis\_reporting\_

observability

Implement ve targets in Schemathesis: a post-validation hook system, multi-format test report writers

(VCR, HAR, JUnit, NDJSON), pytest plugin integration, and schema-branch-aware example generation.

schemathesis\_config\_

modernization

Implement six modernization targets in Schemathesis: a TOML-based conguration system with

auto-discovery, API namespace reorganization, a metrics framework, transport and response

abstractions, and a redesigned check registration system.

stream\_processing\_engine

Implement a Rust-based stream processing engine supporting windowed aggregations, ltering,

projection, and stateful operators over JSON event streams. Scored on correctness, robustness to

malformed input, and throughput.

tls13\_handshake\_state\_

machine

Complete a Python TLS 1.3 protocol state machine that processes handshake message traces,

implementing state transitions, key schedule computation, and message validation using a provided

crypto API.

vault\_sdk\_resilience

Implement ve targets in HashiCorp Vault's Go SDK: a string template engine, a fair-share job

scheduler, persistent cache storage for agent tokens, certicate utility enhancements, and API client

request/response hooks.

vliw\_kernel\_optimization

Optimize a VLIW/SIMD kernel generator for correctness and minimum cycle count on a custom

architecture simulator. Hard-coded answers for specic inputs are forbidden.

cpu\_full\_flow

Work through a full RISC-V CPU design curriculum: ISA emulator implementation, hardware

abstraction layer, Verilog processor design, and SoC integration with Verilator simulation.

zstd\_api\_modernization

Implement ve API evolution targets in Zstandard's C library: stable struct alignment and query

functions, a generic parameter-driven compression interface, static allocation support, dictionary

enhancements, and memory estimation utilities.

cfzip\_compression\_engine

Implement a complete compression engine from scratch in C++17 without external libraries: custom

archive format, CLI with streaming mode, dictionary training and use, and integrity verication.

Scored on compression ratio, speed, memory usage, and correctness.

Scientific Problems & ML

battery\_soh\_rul\_anomaly

Predict battery state-of-health, remaining useful life, and anomaly type/severity per cycle for unseen

cells, given multi-cell degradation training data. Evaluated under distributional shift with regime and

calibration changes not present in training.

borden\_pump\_treat\_

dispatch

Build a physics-based groundwater ow model and solve a constrained multi-objective optimization for

pump-and-treat remediation on the Borden aquifer, selecting wells, treatment types, and multi-phase

schedules under budget and capacity constraints.

borden\_source\_inversion

Infer a nite-duration rectangular contaminant source from sparse, noisy monitoring-well observations

in a 3D hydrogeological scene. The agent must implement its own forward model and inversion

optimizer from scratch.

borden\_sensor\_fault\_

diagnosis

Classify sensor faults (spikes, drift, stuck-at-zero, unit errors, etc.) versus true plume arrivals in

groundwater monitoring records using physics-informed checks such as travel-time ordering and

neighbor-well consistency.

bridge\_gnss\_state\_

forecast

Process dirty bridge GNSS displacement time series (timestamp jitter, duplicates, spikes, drift) and

produce cleaned reconstruction, state estimates, and short-term displacement forecasts.

capecod\_plume\_

reconstruction

Reconstruct a multi-analyte groundwater plume from sparse monitoring wells: predict concentrations at

withheld locations and times, compute plume metrics, and propose an optimal monitoring network

under budget constraints.

vsg\_stability\_parameter\_

optimization

Integrate current-limited Virtual Synchronous Generators into the IEEE 39-bus power system, generate

transient stability data, build a physics-informed neural network, and train a reinforcement learning

agent to optimize VSG parameters.

cylinder\_wake\_prediction

Implement a CPU-only 2D cylinder wake solver for the incompressible Navier-Stokes equations.

Evaluated on unseen Reynolds numbers and domain congurations; scored on velocity-eld accuracy,

pressure-eld accuracy, and ow-regime prediction.

dabic\_gravity\_inversion

Implement the D-ABIC regularization method for 3D gravity inversion within the SimPEG framework,

run on both synthetic and real Vinton salt dome data under L0 and L1 sparse norms, and compare

against a Hamiltonian Monte Carlo baseline.

noisy\_product\_matching\_

pipeline

Determine whether pairs of product listings from dierent sources refer to the same real-world item,

given noisy and incomplete attributes. Evaluated on hidden variants with dierent noise characteristics

and data scales; no ground-truth labels are available during development.

neural\_net\_weight\_

recovery

Reconstruct the correct layer ordering of a neural network from 97 shued weight les and

input-output historical data, using dimensional constraints and reconstruction-error analysis.

nanophotonic\_simulation\_

reproduction

Reproduce published nanophotonic simulation results (multi-source electromagnetic eld distributions)

from a research paper, implementing the solver from scratch using only NumPy.

ftir\_polymer\_

identification

Identify polyimide monomers from FTIR spectra by correlating IR absorption peaks with functional

groups, optionally aided by quantum chemistry simulations. Submission attempts are rate-limited to

prevent brute-force enumeration.

molecular\_property\_

regression

Predict molecular properties from graph representations without graph neural network libraries.

Evaluated on multi-domain data with perturbations that penalize solutions overtting to the

development distribution.

graph\_node\_classification Implement graph neural networks from scratch using only base PyTorch for semi-supervised node

classication on an unseen graph under CPU-only constraints.

Continued on next page

48

Task

Design notes

gravitational\_wave\_

signal\_detection

Reproduce the LIGO GW150914 gravitational-wave detection pipeline: whitening, bandpass ltering,

matched ltering against a numerical-relativity template, time-frequency analysis, and residual

computation.

herbal\_depression\_

target\_screening

Screen active components and protein targets for four traditional Chinese medicine herbs used in

depression treatment, producing component lists, target mappings, disease-target intersections, and a

PPI network visualization.

polyimide\_homo\_lumo\_

prediction

Compute HOMO/LUMO energies of polyimide repeating units using DFT calculations, analyze

substituent and conjugation eects on electronic properties, and identify the monomer pair with the

widest band gap.

industrial\_anomaly\_

detection

Detect anomalies in multivariate industrial sensor time series using only classical ML libraries.

Evaluated on hidden variants including time-series crops, reversals, and normal-only segments to

prevent hard-coding.

bipedalwalker\_

locomotion\_rl

Train a CPU-only locomotion policy for BipedalWalker and its Hardcore variant. The judge evaluates

only the submitted policy checkpoint, not the training process. Pre-trained policies and external RL

libraries are prohibited.

molecular\_solubility\_

prediction

Predict aqueous log-solubility from SMILES strings and molecular descriptors, improving upon a

provided random forest baseline. Scored by prediction error on hidden test molecules.

motor\_clutch\_model\_

reproduction

Implement a Gillespie/KMC stochastic simulation of the motor-clutch mechanotransduction model

from sparse reference traces. Curve-tting formulas and lookup tables are prohibited; the simulation

must exhibit correct stochastic dynamics across unseen parameter combinations.

streaming\_multilabel\_

classification

Implement streaming multi-label classication from scratch using only NumPy. Evaluated on subset

accuracy, Hamming loss, and F1 metrics under CPU-only constraints.

barnes\_hut\_nbody\_

acceleration

Implement a Barnes-Hut _N_ \-body gravitational simulation in C++17. Scored on both force accuracy

relative to direct summation and speedup over a naive baseline across varying particle counts.

blackbox\_numerical\_

integration

Integrate hidden black-box functions over the 10-dimensional unit hypercube via an oracle interface

with bounded query budgets. Scored on accuracy relative to true integral values.

pancreatic\_radiotherapy\_

meta\_analysis

Automate a two-stage systematic review pipeline: screen candidate PDFs and extract evidence, then

perform inverse-variance meta-analysis with model selection and subgroup analysis. Evaluated on

unseen publications.

monge\_ampere\_pde\_solver

Implement a numerical solver for the fully nonlinear Monge-Ampère equation det( _D_ ² _u_ ) = _f_ ( _x, y_ ) .

Evaluated on unseen right-hand sides and boundary conditions; scored on solution accuracy and

computational eciency.

pdf\_structured\_extraction Extract structured page blocks (text, tables, formulas, gures) with bounding boxes, reading order, and

content from PDFs using only classical computer vision toolsno deep learning models. Evaluated on

diverse enterprise document layouts.

ocean\_mt\_lab\_inversion

Implement 1D marine magnetotelluric forward modeling and Bayesian inversion with lateral coupling

across ocean-bottom stations. Independent per-station or point-estimate-only solutions are penalized.

pv\_power\_forecasting

Forecast multi-site photovoltaic power generation from historical output and weather features.

Evaluated on unseen data across multiple domain-specic metrics including ramp handling, peak

accuracy, and multi-horizon performance.

quantum\_architecture\_

search

Implement noise-adaptive quantum architecture search balancing classication accuracy and molecular

ground-state energy estimation against hardware-realistic circuit depth and gate count constraints.

collaborative\_filtering\_

recommender

Implement a top-K recommender system that jointly optimizes recommendation quality (NDCG) and

runtime eciency, including cold-start users with no training interactions.

touchstone\_vna\_

diagnostics

Parse Touchstone S-parameter les in various representations (real-imaginary, magnitude-angle,

dB-angle), compute derived RF metrics (return loss, VSWR, group delay, impedance), and produce

structured diagnostic reports.

ecg\_signal\_processing\_

pipeline

Implement a three-stage ECG processing pipeline (denoising, QRS complex detection, beat

classication) from scratch using only NumPy. Evaluated on unseen recordings with dierent noise

proles and arrhythmia distributions.

sketch\_solve\_least\_

squares

Solve large-scale overdetermined least-squares problems by choosing among direct solvers, iterative

methods, and randomized sketching based on matrix properties. Scored on solution accuracy and speed

across varied problem structures.

substrate\_interface\_

simulation

Implement a coupled interface response simulation with correct parameter dependence. Hard-coded

outputs are prohibited; evaluated on physical consistency, energy conservation, and statistical

properties of stochastic trajectories.

thermo\_fluid\_field\_

prediction

Predict 2D velocity and temperature elds for thermo-uid coupling problems under varying boundary

conditions and dimensionless parameters, using only NumPy on CPU.

csi\_time\_series\_

forecasting

Forecast future wireless channel state information tensors from historical observations. Evaluated on

unseen channel conditions and mobility scenarios under CPU-only constraints.

roof\_damage\_active\_

learning

Design an active learning pipeline for satellite-imagery roof damage detection: start from a small

labeled seed set, strategically query an oracle for additional labels under a xed budget, and train an

object detector for evaluation on unlabeled images.

Combinatorial Optimization

ad\_placement\_optimization Partition a large integer grid into non-overlapping rectangles, each containing a designated anchor

point, maximizing total satisfaction from how closely each rectangle's area matches its target.

treant\_forest

Strategically place obstacles in a grid maze to maximize the shortest-path length between start and

goal, or block the path entirely.

grid\_turing\_robot

Design transition rules and initial coloring for a Turing-like robot on a colored grid to maximize the

number of distinct cells visited while minimizing the rule set size.

Continued on next page

49

Task

Design notes

molecular\_self\_assembly

Schedule bonding operations over discrete time steps to assemble atoms into a specied number of

connected molecules, respecting spatial proximity and temporal ordering constraints.

apple\_incremental\_game

Decide each turn whether to invest in machines or collect output in an incremental production game,

balancing short-term gains against long-horizon compounding.

first\_order\_theorem\_

prover

Build a rst-order automated theorem prover from scratch (parsing, clausication, unication,

saturation) that produces veried proof or model witnesses. External provers and benchmark

ngerprinting are forbidden.

circuit\_layout\_

optimization

Implement a VLSI standard-cell placement solver minimizing half-perimeter wire length on

industry-standard benchmarks. Scored on wire-length quality and runtime.

order\_addition\_

permutation\_optimization

Find a permutation of 1,000 elements that minimizes a black-box cost function, using metaheuristic

search (simulated annealing, genetic algorithms, local search) without access to the cost function's

internals.

equivalence\_class\_

divide\_and\_conquer

Solve six progressive competitive-programming problems centered on equivalence classes and

divide-and-conquer, where techniques from earlier problems inform solutions to harder ones.

jagua\_nesting\_

optimization

Improve a Rust-based 2D irregular bin packing optimizer for non-convex polygonal pieces. Solution

geometry is independently veried; improvements below a minimum threshold receive no credit.

sat\_solver

Build a SAT solver from scratch implementing conict-driven clause learning, watched literals, and

restart strategies. External solvers and benchmark-aware heuristics are forbidden; scoring is balanced

across diculty tiers.

smt\_solver

Build an SMT solver from scratch for four quantier-free theories (uninterpreted functions, linear real

and integer arithmetic, and their combination). External SMT solvers are forbidden; model witnesses

are independently validated.

symbolic\_integration\_

engine

Extend a starter symbolic integration engine (with its own parser, simplier, and dierentiator) to

handle a broader class of integrands. All computer algebra systems and numerical libraries are

forbidden; correctness is veried by dierentiating the returned antiderivative.

tree\_block\_partitioning

Solve six progressive problems on tree decomposition and block partitioning, where algorithmic ideas

discovered in simpler variants transfer to harder ones.

triangulation\_coloring\_

optimization

Minimize a cost function over a triangulation by jointly recoloring vertices and ipping edges, where

the dominant term is a quadratic penalty on monochromatic (ugly) triangles.

vibrating\_path\_graph\_

coloring

Color graph vertices and selectively remove edges to minimize a cost that penalizes both removed edges

and monochromatic surviving edges.

vehicle\_routing\_time\_

windows

Implement a capacitated vehicle routing solver with time windows for Solomon-style benchmarks.

Scored against best-known solutions on vehicle count and total travel distance.

warehouse\_forklift\_

routing

Route a forklift in a grid warehouse to receive goods arriving in random order, store them, and dispatch

them in sequential order, minimizing total movement.

wireless\_electricity\_

layout

Position wire segments on a 2D plane to deliver wireless electricity from two xed source plates to

thousands of cities, minimizing a quadratic cost over city-to-wire distances and wire displacements

while avoiding short circuits.

Formal Math & Theorem Proving

lean\_analysis\_proofs

Complete proof obligations across a multi-le Lean 4 project formalizing results in real and functional

analysis. Proofs are checked transitively: a theorem counts only if its entire dependency chain is fully

proved.

carleson\_formalization

Fill proof obligations in the Lean 4 formalization of Carleson's theorem on pointwise convergence of _L_ ²

Fourier series. Transitive axiom checking ensures no dependence on unproved prerequisites.

combinatorial\_games\_

formalization

Resolve proof obligations in a Lean 4 formalization of combinatorial game theory, covering surreal

numbers, game arithmetic, and the Sprague-Grundy theorem.

new\_foundations\_

consistency

Complete proof obligations in the ConNF Lean 4 project formalizing the consistency of Quine's New

Foundations, involving permutation models and tangled type theory.

cup\_product\_formalization Fill proof obligations in a Lean 4 formalization of the cup product in singular cohomology:

cochain-level multiplication, the Leibniz rule, and the induced ring structure on cohomology groups.

erdos392\_formalization

Complete proof obligations for Erd®s Problem 392 (asymptotic prime distribution) within a Lean 4

analytic number theory project. Weighted scoring reects relative diculty of each proof.

flt\_regular\_formalization Resolve proof obligations in a Lean 4 formalization of Fermat's Last Theorem for regular primes via

Kummer's cyclotomic theory. Top-level results earn no credit unless foundational prerequisites are also

fully proved.

godel\_incompleteness\_

formalization

Complete proof obligations in a Lean 4 formalization of Gödel's First Incompleteness Theorem,

spanning Gödel numbering, the xed-point lemma, and the self-referential undecidable sentence.

medium\_prime\_number\_

theorem

Complete proof obligations for the Prime Number Theorem with an explicit error term, requiring

complex-analytic techniques including contour integration and zero-free regions of the Riemann zeta

function.

ordinal\_notation\_well\_

foundedness

Construct well-foundedness proofs for ordinal notation systems in Coq, involving Cantor Normal Form

and ordinal arithmetic.

pfr\_formalization

Resolve proof obligations in the Lean 4 formalization of the Polynomial FreimanRuzsa conjecture

(GowersGreenMannersTao 2023), involving Shannon entropy, Ruzsa distance, and subgroup covering

arguments.

sphere\_eversion\_

formalization

Complete proof obligations in a Lean 4 formalization of sphere eversion, spanning smooth immersions,

jet bundles, ample dierential relations, and convex integration.

turing\_machine\_halting\_

proofs

Prove halting behavior for specic 6-state, 2-symbol Turing machines in Coq, contributing to the Busy

Beaver frontier. Proofs must be mechanically veried with no admitted axioms.

Continued on next page

50

Task

Design notes

Professional Knowledge Work

portfolio\_risk\_

calibration

Implement a multi-module portfolio management system (risk calibration, constrained optimization,

execution cost modeling, dynamic rebalancing) for a cross-asset ETF portfolio. Evaluated out-of-sample

on risk-adjusted return metrics.

storyboard\_ad\_copywriting Produce a promotional video script with dual variants and a shot-by-shot storyboard for a state-owned

enterprise exhibition appearance, adhering to strict political communication standards and advertising

compliance.

brand\_annual\_planning\_ppt Produce a comprehensive annual brand management plan as a presentation deck and companion data

tables for a mid-size IPTV company, covering strategy, monthly action roadmaps, budgets with market

rate benchmarks, and competitive analysis.

securities\_protection\_

training

Produce a complete set of training deliverables for a securities investor protection seminar: legal

framework overview, core systems analysis, case studies, comparative study, policy analysis,

presentation deck, lecture script, and bibliography.

college\_english\_exam\_bank Produce ve parallel examination papers with answer keys for a college English course, plus a blueprint

table and an overlap self-check matrix ensuring cross-paper diversity meets pedagogical thresholds.

cross\_border\_commission\_

compliance

Produce a multi-module legal compliance report for a cross-border commission payment, covering

multi-jurisdictional anti-corruption risk (FCPA, UK Bribery Act, Chinese Criminal Law), export

control, transfer pricing, and evidence preservation strategy.

cross\_border\_investment\_

ppt

Produce a presentation covering 15 months of global cross-border investment policy developments with

chronological policy inventory, original data charts, multi-sector industry analysis with deal case

studies, and forward-looking risk assessment.

cta\_risk\_budget\_

optimization

Build a complete CTA multi-strategy futures trading system: multiple signal classes, dynamic risk

budgeting, a multi-currency backtest engine with transaction costs, drawdown control, and performance

attribution.

equity\_objection\_report

Produce a court-submission-ready legal research report analyzing whether benecial owners under

equity proxy-holding arrangements can defeat forced execution in Chinese civil enforcement law, citing

specic judicial guidance and case precedents.

expo\_visitor\_conversion\_

model

Clean tens of thousands of messy visitor registration records (entity resolution, address parsing,

company-name merging), tag professional visitors, and build a calibrated exhibitor conversion scoring

model.

factor\_stock\_model\_

optimization

Implement an adaptive multi-factor stock selection model with IC-based factor selection, dynamic

weighting, industry/market-cap neutralization, and constrained portfolio construction. Evaluated

out-of-sample on information ratio, excess return, drawdown, and turnover.

global\_terrorism\_atlas\_

report

Transform a 200K+ record terrorism database into a single-PDF infographic atlas with maps, ranking

charts, shaped word clouds, a sunburst diagram, and country-level fatality trends.

hebei\_gaokao\_strategy\_

report

Produce a multi-tier college admission preference plan with alternative strategies, given complex

personal constraints (banned elds, health disqualications, career priorities) and three years of

historical admission data.

hk\_connect\_annual\_metrics Programmatically retrieve and populate nancial metrics for 255 Hong Kong Stock Connect-eligible

securities from annual reports and market data providers. Scored on per-cell accuracy.

k12\_math\_recommendation

Build a knowledge-tracing and question-recommendation system from hundreds of thousands of student

interaction records, evaluated on prediction accuracy, mastery calibration, learning gain, and

pedagogical constraint satisfaction.

property\_actuarial\_

pricing

Build an actuarial pricing model for SME property insurance: loss modeling, risk grading, reinsurance

cost allocation, and premium smoothing with renewal constraints. Evaluated on predictive accuracy

and premium adequacy.

real\_estate\_bid\_estimate

Conduct feasibility analysis for a supertall oce land tender: market research, quarterly cash ow

models under two bidding structures, sensitivity analysis, and a reasoned investment recommendation.

stock\_momentum\_backtest

Fetch live A-share market data, compute risk-adjusted momentum scores, apply multi-factor screening

lters, and calculate a market-cap-weighted portfolio return for a specic holding period. Scored on

numerical accuracy of each computation step.

storm\_claim\_ring\_audit

Build a fraud detection pipeline for post-disaster insurance claims: produce hold/release/escalate

decisions and fraud-ring cluster assignments from interconnected claim, payment, survey, and media

datasets, distinguishing genuine disaster patterns from coordinated fraud.

Interactive Games & Simulators

dcss\_dungeon\_ai

Write a Lua bot for Dungeon Crawl Stone Soup that autonomously explores, ghts, and descends

dungeon levels as a Minotaur Berserker under a wall-clock time budget. Scored by mean in-game score

across multiple runs.

anchorhead\_text\_adventure Play the Lovecraftian interactive ction game Anchorhead via an HTTP API, sending text commands

and receiving prose observations. Scored by peak in-game score, reecting progression through the

multi-day narrative and puzzle chain.

trinity\_text\_adventure

Play Infocom's Trinity via an HTTP game API. The game requires precise object manipulation and

understanding of symbolic and temporal clues across interconnected zones.

tryst\_text\_adventure

Play Tryst of Fate via an HTTP game API. The branching narrative with irreversible choices requires

strategic exploration to reach high-scoring endings.

nethack\_dungeon\_agent

Implement a decision policy for NetHack via the NLE harness, parsing ASCII map observations and

stat vectors to navigate, ght, and survive across multiple procedurally generated runs.

openrct2\_theme\_park\_ai

Write a JavaScript plugin for OpenRCT2 that autonomously builds rides, hires sta, sets pricing, and

grows park company value across multiple scenarios of increasing complexity.

Continued on next page

51

Task

Design notes

openttd\_transport\_ai

Write an AI script for OpenTTD that builds road, rail, and air transport networks to connect towns

and industries and grow company value across diverse procedurally generated maps.

wesnoth\_tactical\_ai

Write tactical AI logic for Battle for Wesnoth that defeats the built-in AI through custom recruitment,

focus-re targeting, terrain exploitation, and village-capture timing across multiple maps.

**Table 7** Per-task design notes for all 134 EdgeBench tasks.

**G.5**

**Per-Task Learning Curves**

Figures 15  35 show learning curves for all tasks in the benchmark, grouped by capability family. Each plot

shows raw task score versus elapsed time over the 12-hour budget; solid lines are the best-so-far envelope, faint

dashed dots are individual submissions, and pale segments after the marked best indicate later submissions

without improvement. On a few tasks the y-axis is zoomed to the main score band, with extreme outlier

submissions o-axis (noted under each plot). Five agents are compared: Claude Opus 4.8, GPT-5.5, GPT-5.4,

GLM-5.1, and DS-V4-Pro. The 18 representative tasks in the main text (Figure 4 ) are not repeated here.

52

0

2

4

6

8

10

12

elapsed time (hours)

0

5

10

15

20

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

GPT 5.4

**borden\_pump\_treat\_dispatch**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**borden\_sensor\_fault\_diagnosis**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

GLM 5.1

GPT 5.5

Claude Opus 4.8

GPT 5.4

DeepSeek V4 Pro

**bridge\_gnss\_state\_forecast**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**vsg\_stability\_parameter\_optimization**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**cylinder\_wake\_prediction**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

Claude Opus 4.8

GPT 5.5

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**dabic\_gravity\_inversion**

**Figure 15** Per-task learning curves: Scientic Computing & ML (1/21).

53

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

**noisy\_product\_matching\_pipeline**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

**neural\_net\_weight\_recovery**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

GPT 5.5

**nanophotonic\_simulation\_reproduction**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

**ftir\_polymer\_identification**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

**molecular\_property\_regression**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

GPT 5.4

**graph\_node\_classification**

**Figure 16** Per-task learning curves: Scientic Computing & ML cont. (2/21).

54

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

**gravitational\_wave\_signal\_detection**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**herbal\_depression\_target\_screening**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.4

GPT 5.5

GLM 5.1

**polyimide\_homo\_lumo\_prediction**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

DeepSeek V4 Pro

GLM 5.1

**industrial\_anomaly\_detection**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

Performance

GPT 5.5

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

**bipedalwalker\_locomotion\_rl**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

GPT 5.4

GLM 5.1

Claude Opus 4.8

DeepSeek V4 Pro

**molecular\_solubility\_prediction**

**Figure 17** Per-task learning curves: Scientic Computing & ML cont. (3/21).

55

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

**motor\_clutch\_model\_reproduction**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.4

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.5

GLM 5.1

**streaming\_multilabel\_classification**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.4

GPT 5.5

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

**barnes\_hut\_nbody\_acceleration**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

GPT 5.4

**blackbox\_numerical\_integration**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

Claude Opus 4.8

GPT 5.5

GLM 5.1

DeepSeek V4 Pro

GPT 5.4

**pancreatic\_radiotherapy\_meta\_analysis**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

GPT 5.5

GPT 5.4

**monge\_ampere\_pde\_solver**

**Figure 18** Per-task learning curves: Scientic Computing & ML cont. (4/21).

56

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

Claude Opus 4.8

GPT 5.4

GPT 5.5

GLM 5.1

DeepSeek V4 Pro

**pdf\_structured\_extraction**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**ocean\_mt\_lab\_inversion**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

GPT 5.5

GLM 5.1

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.4

**pv\_power\_forecasting**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

GLM 5.1

Claude Opus 4.8

GPT 5.4

DeepSeek V4 Pro

**quantum\_architecture\_search**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GLM 5.1

GPT 5.5

GPT 5.4

DeepSeek V4 Pro

**collaborative\_filtering\_recommender**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

Claude Opus 4.8

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

**touchstone\_vna\_diagnostics**

**Figure 19** Per-task learning curves: Scientic Computing & ML cont. (5/21).

57

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**ecg\_signal\_processing\_pipeline**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

Claude Opus 4.8

**sketch\_solve\_least\_squares**

0

2

4

6

8

10

12

elapsed time (hours)

0

5

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

GPT 5.5

**substrate\_interface\_simulation**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GLM 5.1

Claude Opus 4.8

GPT 5.5

GPT 5.4

DeepSeek V4 Pro

**thermo\_fluid\_field\_prediction**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

DeepSeek V4 Pro

GLM 5.1

**csi\_time\_series\_forecasting**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

**roof\_damage\_active\_learning**

**Figure 20** Per-task learning curves: Scientic Computing & ML cont. (6/21).

58

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.4

GPT 5.5

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

**ann\_vector\_search\_qps**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

GLM 5.1

DeepSeek V4 Pro

GPT 5.4

**rust\_multicrate\_reconstruction**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GLM 5.1

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

**copier\_modular\_refactor**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**dependent\_type\_checker**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

GPT 5.5

**entt\_graph\_module**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

DeepSeek V4 Pro

GLM 5.1

Claude Opus 4.8

GPT 5.5

GPT 5.4

**exchange\_core\_throughput**

**Figure 21** Per-task learning curves: Systems & Software Engineering (7/21).

59

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GLM 5.1

GPT 5.5

DeepSeek V4 Pro

GPT 5.4

**high\_performance\_object\_mapper**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**integer\_compression\_codec**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

GPT 5.4

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

**juliet\_vulnerability\_analyzer**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

GLM 5.1

DeepSeek V4 Pro

GPT 5.5

Claude Opus 4.8

GPT 5.4

**libexpat\_x86\_assembly**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

Performance

GPT 5.4

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.5

GLM 5.1

**odata\_query\_service**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**litestar\_infra\_refactor**

**Figure 22** Per-task learning curves: Systems & Software Engineering cont. (8/21).

60

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.4

GPT 5.5

GLM 5.1

DeepSeek V4 Pro

**lua\_native\_compiler**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**mimesis\_modular\_refactor**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**nlohmann\_json\_modularization**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

Performance

Claude Opus 4.8

GPT 5.5

GLM 5.1

DeepSeek V4 Pro

GPT 5.4

**notebook\_lossless\_compression**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

DeepSeek V4 Pro

GLM 5.1

GPT 5.5

Claude Opus 4.8

GPT 5.4

**packer\_plugin\_datasources**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

DeepSeek V4 Pro

GLM 5.1

**pocketbase\_tools\_extensions**

**Figure 23** Per-task learning curves: Systems & Software Engineering cont. (9/21).

61

0

2

4

6

8

10

12

elapsed time (hours)

0

5

10

15

Performance

Claude Opus 4.8

GLM 5.1

GPT 5.5

GPT 5.4

DeepSeek V4 Pro

**postgres\_wire\_on\_sqlite**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

Claude Opus 4.8

DeepSeek V4 Pro

**codeflash\_repair\_performance**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.4

GPT 5.5

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

**regex\_automata\_repair**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GLM 5.1

Claude Opus 4.8

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

**schemathesis\_datagen\_pipeline**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

DeepSeek V4 Pro

GLM 5.1

**schemathesis\_reporting\_observability**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**schemathesis\_config\_modernization**

**Figure 24** Per-task learning curves: Systems & Software Engineering cont. (10/21).

62

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

GPT 5.5

**stream\_processing\_engine**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

GPT 5.5

GPT 5.4

GLM 5.1

Claude Opus 4.8

DeepSeek V4 Pro

**tls13\_handshake\_state\_machine**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

DeepSeek V4 Pro

GPT 5.4

GLM 5.1

**vault\_sdk\_resilience**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**vliw\_kernel\_optimization**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

GPT 5.4

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

**cpu\_full\_flow**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

GPT 5.5

**zstd\_api\_modernization**

**Figure 25** Per-task learning curves: Systems & Software Engineering cont. (11/21).

63

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GLM 5.1

DeepSeek V4 Pro

GPT 5.4

**cfzip\_compression\_engine**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GLM 5.1

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

Claude Opus 4.8

**pocketbase\_backend\_architecture**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

GPT 5.4

**arc\_compiler\_runtime**

**Figure 26** Per-task learning curves: Systems & Software Engineering cont. (12/21).

64

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.5

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**ad\_placement\_optimization**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

Claude Opus 4.8

GPT 5.5

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**treant\_forest**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**grid\_turing\_robot**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.4

GPT 5.5

GLM 5.1

**molecular\_self\_assembly**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**apple\_incremental\_game**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

Claude Opus 4.8

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

**first\_order\_theorem\_prover**

**Figure 27** Per-task learning curves: Combinatorial Optimization & Planning (13/21).

65

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

Claude Opus 4.8

GPT 5.5

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**circuit\_layout\_optimization**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**equivalence\_class\_divide\_and\_conquer**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.4

GPT 5.5

GLM 5.1

**jagua\_nesting\_optimization**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

Performance

Claude Opus 4.8

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

**smt\_solver**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**tree\_block\_partitioning**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

GPT 5.4

GLM 5.1

Claude Opus 4.8

DeepSeek V4 Pro

**triangulation\_coloring\_optimization**

**Figure 28** Per-task learning curves: Combinatorial Optimization & Planning cont. (14/21).

66

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

Claude Opus 4.8

GPT 5.4

DeepSeek V4 Pro

GLM 5.1

GPT 5.5

**vibrating\_path\_graph\_coloring**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

DeepSeek V4 Pro

GLM 5.1

**vehicle\_routing\_time\_windows**

0

2

4

6

8

10

12

elapsed time (hours)

0

5

10

15

20

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**warehouse\_forklift\_routing**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

GLM 5.1

Claude Opus 4.8

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

**wireless\_electricity\_layout**

**Figure 29** Per-task learning curves: Combinatorial Optimization & Planning cont. (15/21).

67

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

GLM 5.1

GPT 5.4

Claude Opus 4.8

DeepSeek V4 Pro

**brand\_annual\_planning\_ppt**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**securities\_protection\_training**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

GPT 5.5

DeepSeek V4 Pro

Claude Opus 4.8

GPT 5.4

GLM 5.1

**college\_english\_exam\_bank**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

Performance

GLM 5.1

GPT 5.5

DeepSeek V4 Pro

Claude Opus 4.8

GPT 5.4

**cross\_border\_commission\_compliance**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

Performance

DeepSeek V4 Pro

GPT 5.4

GLM 5.1

GPT 5.5

Claude Opus 4.8

**cta\_risk\_budget\_optimization**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GLM 5.1

Claude Opus 4.8

GPT 5.5

GPT 5.4

DeepSeek V4 Pro

**storyboard\_ad\_copywriting**

**Figure 30** Per-task learning curves: Professional Knowledge Work (16/21).

68

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GLM 5.1

GPT 5.5

DeepSeek V4 Pro

GPT 5.4

**expo\_visitor\_conversion\_model**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

GLM 5.1

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.4

**factor\_stock\_model\_optimization**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

GPT 5.4

**global\_terrorism\_atlas\_report**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.4

GPT 5.5

DeepSeek V4 Pro

GLM 5.1

**hebei\_gaokao\_strategy\_report**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**hk\_connect\_annual\_metrics**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**k12\_math\_recommendation**

**Figure 31** Per-task learning curves: Professional Knowledge Work cont. (17/21).

69

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

GPT 5.5

**property\_actuarial\_pricing**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

Claude Opus 4.8

GPT 5.4

GPT 5.5

GLM 5.1

DeepSeek V4 Pro

**real\_estate\_bid\_estimate**

0

2

4

6

8

10

12

elapsed time (hours)

0

5

10

15

20

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GPT 5.5

GPT 5.4

GLM 5.1

**stock\_momentum\_backtest**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

GPT 5.5

**storm\_claim\_ring\_audit**

**Figure 32** Per-task learning curves: Professional Knowledge Work cont. (18/21).

70

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**erdos392\_formalization**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

DeepSeek V4 Pro

GLM 5.1

**carleson\_formalization**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**new\_foundations\_consistency**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**godel\_incompleteness\_formalization**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**medium\_prime\_number\_theorem**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

DeepSeek V4 Pro

GLM 5.1

**cup\_product\_formalization**

**Figure 33** Per-task learning curves: Formal Math & Theorem Proving (19/21).

71

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**pfr\_formalization**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

Claude Opus 4.8

GPT 5.4

GLM 5.1

DeepSeek V4 Pro

**sphere\_eversion\_formalization**

0

2

4

6

8

10

12

elapsed time (hours)

0

5

10

15

20

Performance

Claude Opus 4.8

DeepSeek V4 Pro

GLM 5.1

GPT 5.4

GPT 5.5

**turing\_machine\_halting\_proofs**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**flt\_regular\_formalization**

**Figure 34** Per-task learning curves: Formal Math & Theorem Proving cont. (20/21).

72

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

Performance

Claude Opus 4.8

GPT 5.4

GLM 5.1

GPT 5.5

DeepSeek V4 Pro

**nethack\_dungeon\_agent**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

Performance

GPT 5.5

GPT 5.4

Claude Opus 4.8

GLM 5.1

DeepSeek V4 Pro

**trinity\_text\_adventure**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

Performance

GPT 5.5

Claude Opus 4.8

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**tryst\_text\_adventure**

0

2

4

6

8

10

12

elapsed time (hours)

0

10

20

30

40

50

Performance

GPT 5.5

GLM 5.1

GPT 5.4

Claude Opus 4.8

DeepSeek V4 Pro

**openrct2\_theme\_park\_ai**

0

2

4

6

8

10

12

elapsed time (hours)

0

20

40

60

80

100

Performance

Claude Opus 4.8

GPT 5.5

GLM 5.1

GPT 5.4

DeepSeek V4 Pro

**wesnoth\_tactical\_ai**

**Figure 35** Per-task learning curves: Interactive Games & Simulators (21/21).

73

**G.6**

**Per-Task Score Tables**

For every taskmodel conguration, we scheduled three independent long-horizon runs. In practice, because

these 12-hour trajectories are sensitive to network instability and serving-side reliability limits, we carried

out multiple rolling evaluation rounds to recover failed or incomplete runs and produced the nal score tables

below. A small number of reported taskmodel cells nevertheless still have fewer than three valid runs; those

cells are marked with \* . Each run score is rst rescaled to the 0100 task scale; the adjacent _±_ _s_ term reports

the sample standard deviation across these rescaled run scores when at least two valid runs are available.

This standard deviation is not clipped to the 0100 range, so ¯ _x_ _±_ _s_ should be read as run-to-run variation

rather than as a bounded score interval.

74

**Systems & Software**

**Engineering Tasks**

**Opus 4.8**

**GPT-5.5**

**GPT-5.4**

**GLM-5.1**

**DS-V4-Pro**

codeflash\_repair\_performance

57 _._ 2 _±_ 21 _._ 9

**100** **_._** **0** \* **_±_** **0** **_._** **0**





30 _._ 5 _±_ 17 _._ 9

ffmpeg\_swscale\_reimplementation

**21** **_._** **1** **_±_** **7** **_._** **9**

15 _._ 3 _±_ 2 _._ 8

13 _._ 9 _±_ 3 _._ 1

2 _._ 2 _±_ 3 _._ 9

3 _._ 8 _±_ 5 _._ 9

git\_rewrite\_in\_zig

23 _._ 1 _±_ 2 _._ 2

18 _._ 4 _±_ 0 _._ 4

15 _._ 4 _±_ 2 _._ 4

**23** **_._** **5** **_±_** **1** **_._** **9**

17 _._ 9 _±_ 2 _._ 1

arc\_compiler\_runtime

52 _._ 0 _±_ 0 _._ 1

**72** **_._** **4** **_±_** **15** **_._** **1**

50 _._ 0 _±_ 0 _._ 7

48 _._ 7 _±_ 3 _._ 5

44 _._ 2 _±_ 4 _._ 7

pdf\_structured\_extraction

36 _._ 5 _±_ 4 _._ 5

29 _._ 8 _±_ 2 _._ 1

**36** **_._** **9** \* **_±_** **1** **_._** **7**

26 _._ 3 _±_ 2 _._ 9

9 _._ 5 _±_ 2 _._ 3

ann\_vector\_search\_qps

**59** **_._** **7** **_±_** **2** **_._** **1**

40 _._ 7 _±_ 18 _._ 8

50 _._ 2 _±_ 17 _._ 4

38 _._ 3 _±_ 17 _._ 5

23 _._ 8 _±_ 3 _._ 0

rust\_multicrate\_reconstruction



**57** **_._** **8** **_±_** **16** **_._** **8**

21 _._ 4 _±_ 3 _._ 0

38 _._ 5 _±_ 21 _._ 4

23 _._ 6 _±_ 2 _._ 4

copier\_modular\_refactor

**98** **_._** **9** **_±_** **0** **_._** **0**

97 _._ 8 _±_ 1 _._ 2

98 _._ 1 _±_ 0 _._ 6

98 _._ 0 _±_ 0 _._ 9

87 _._ 2 _±_ 9 _._ 4

dependent\_type\_checker

**44** **_._** **7** **_±_** **3** **_._** **7**

24 _._ 7 _±_ 21 _._ 4

3 _._ 8 _±_ 6 _._ 7

1 _._ 9 _±_ 3 _._ 2

0 _._ 0 _±_ 0 _._ 0

entt\_graph\_module

**100** **_._** **0** **_±_** **0** **_._** **0**

94 _._ 3 _±_ 3 _._ 0

78 _._ 4 _±_ 25 _._ 7

**100** **_._** **0** **_±_** **0** **_._** **0**

92 _._ 0 _±_ 10 _._ 5

exchange\_core\_throughput

**59** **_._** **7** **_±_** **2** **_._** **7**

53 _._ 2 _±_ 6 _._ 8

47 _._ 3 _±_ 10 _._ 2

52 _._ 6 _±_ 12 _._ 9

48 _._ 6 _±_ 17 _._ 9

integer\_compression\_codec

**75** **_._** **3** **_±_** **0** **_._** **3**

74 _._ 4 _±_ 0 _._ 5

42 _._ 3 _±_ 18 _._ 4

28 _._ 9 _±_ 4 _._ 3

16 _._ 2 _±_ 8 _._ 1

juliet\_vulnerability\_analyzer

75 _._ 6 _±_ 6 _._ 7

**89** **_._** **8** **_±_** **1** **_._** **9**

77 _._ 2 _±_ 5 _._ 5

63 _._ 5 _±_ 4 _._ 6

66 _._ 2 _±_ 8 _._ 4

libexpat\_x86\_assembly

15 _._ 8 _±_ 14 _._ 0

13 _._ 5 _±_ 11 _._ 8

11 _._ 9 _±_ 8 _._ 4

**18** **_._** **1** **_±_** **24** **_._** **3**

11 _._ 2 _±_ 15 _._ 7

litestar\_infra\_refactor

**92** **_._** **5** \*

66 _._ 4 _±_ 15 _._ 9

60 _._ 8 _±_ 7 _._ 7

46 _._ 0 _±_ 3 _._ 7

43 _._ 6 _±_ 3 _._ 3

lua\_native\_compiler

**98** **_._** **9** \* **_±_** **0** **_._** **8** 78 _._ 2 _±_ 27 _._ 4

90 _._ 7 _±_ 8 _._ 6

40 _._ 9 \* _±_ 57 _._ 9

41 _._ 2 \* _±_ 7 _._ 8

mimesis\_modular\_refactor

**100** **_._** **0** **_±_** **0** **_._** **0**

91 _._ 0 _±_ 2 _._ 7

87 _._ 8 _±_ 1 _._ 9

82 _._ 0 _±_ 6 _._ 9

65 _._ 4 _±_ 12 _._ 1

nlohmann\_json\_modularization

**100** **_._** **0** **_±_** **0** **_._** **0**

98 _._ 9 _±_ 0 _._ 5

87 _._ 3 _±_ 11 _._ 0

77 _._ 8 _±_ 0 _._ 0

73 _._ 3 _±_ 0 _._ 9

notebook\_lossless\_compression

**53** **_._** **0** **_±_** **2** **_._** **3**

19 _._ 3 _±_ 27 _._ 2

7 _._ 3 _±_ 2 _._ 0

35 _._ 1 _±_ 24 _._ 3

16 _._ 0 _±_ 17 _._ 2

packer\_plugin\_datasources

90 _._ 0 _±_ 0 _._ 0

90 _._ 8 \* _±_ 1 _._ 2

33 _._ 3 _±_ 14 _._ 4

**91** **_._** **1** **_±_** **1** **_._** **0**

90 _._ 6 _±_ 1 _._ 0

pocketbase\_tools\_extensions

**100** **_._** **0** **_±_** **0** **_._** **0**

94 _._ 8 _±_ 2 _._ 6

66 _._ 5 _±_ 15 _._ 2

57 _._ 4 _±_ 13 _._ 0

60 _._ 0 _±_ 17 _._ 3

postgres\_wire\_on\_sqlite

**8** **_._** **2** **_±_** **0** **_._** **3**

7 _._ 7 _±_ 0 _._ 6

7 _._ 8 _±_ 0 _._ 3

8 _._ 1 \* _±_ 0 _._ 3

7 _._ 9 \* _±_ 0 _._ 2

quic\_transport\_stack

48 _._ 3 _±_ 14 _._ 3

**63** **_._** **6** **_±_** **8** **_._** **9**

47 _._ 1 _±_ 16 _._ 1

52 _._ 5 \* _±_ 22 _._ 4

33 _._ 4 _±_ 10 _._ 0

regex\_automata\_repair

66 _._ 7 \* _±_ 0 _._ 1

**67** **_._** **0** **_±_** **0** **_._** **0**

61 _._ 0 _±_ 10 _._ 3

28 _._ 6 \*

2 _._ 3 _±_ 2 _._ 2

schemathesis\_datagen\_pipeline

**70** **_._** **2** **_±_** **2** **_._** **7**

56 _._ 7 _±_ 3 _._ 0

56 _._ 6 _±_ 3 _._ 3

67 _._ 0 _±_ 7 _._ 0

52 _._ 3 _±_ 5 _._ 3

schemathesis\_reporting\_

observability

76 _._ 2 _±_ 4 _._ 7

**77** **_._** **1** **_±_** **3** **_._** **5**

76 _._ 2 _±_ 2 _._ 9

61 _._ 9 _±_ 1 _._ 5

65 _._ 0 _±_ 11 _._ 7

schemathesis\_config\_modernization

**87** **_._** **7** **_±_** **2** **_._** **6**

84 _._ 0 _±_ 1 _._ 5

71 _._ 9 _±_ 1 _._ 8

61 _._ 7 _±_ 4 _._ 2

55 _._ 6 _±_ 2 _._ 9

stream\_processing\_engine

**100** **_._** **0** **_±_** **0** **_._** **0**

**100** **_._** **0** **_±_** **0** **_._** **0**

**100** **_._** **0** **_±_** **0** **_._** **0** **100** **_._** **0** **_±_** **0** **_._** **0**

**100** **_._** **0** **_±_** **0** **_._** **0**

tls13\_handshake\_state\_machine

29 _._ 4 _±_ 0 _._ 9

**39** **_._** **3** **_±_** **1** **_._** **1**

37 _._ 9 _±_ 0 _._ 9

29 _._ 2 _±_ 1 _._ 8

29 _._ 0 _±_ 0 _._ 6

vault\_sdk\_resilience

**100** **_._** **0** **_±_** **0** **_._** **0**

29 _._ 1 _±_ 21 _._ 0

18 _._ 2 _±_ 15 _._ 7

13 _._ 9 _±_ 8 _._ 4

15 _._ 2 _±_ 18 _._ 9

vliw\_kernel\_optimization

80 _._ 9 _±_ 0 _._ 9

**85** **_._** **6** **_±_** **1** **_._** **9**

79 _._ 1 _±_ 1 _._ 5

35 _._ 9 _±_ 25 _._ 1

34 _._ 1 _±_ 19 _._ 1

cpu\_full\_flow

72 _._ 0 \* _±_ 7 _._ 1

**88** **_._** **5** \* **_±_** **12** **_._** **0**

85 _._ 3 _±_ 11 _._ 7

51 _._ 0 \*

56 _._ 3 _±_ 4 _._ 7

zstd\_api\_modernization

**100** **_._** **0** **_±_** **0** **_._** **0**

95 _._ 8 _±_ 7 _._ 2

**100** **_._** **0** **_±_** **0** **_._** **0** **100** **_._** **0** **_±_** **0** **_._** **0**

91 _._ 7 _±_ 14 _._ 4

cfzip\_compression\_engine

**98** **_._** **4** **_±_** **0** **_._** **0**

97 _._ 4 _±_ 1 _._ 3

96 _._ 2 \* _±_ 0 _._ 7

87 _._ 4 _±_ 12 _._ 0

92 _._ 5 _±_ 4 _._ 8

pocketbase\_backend\_architecture

0 _._ 0 _±_ 0 _._ 0

**62** **_._** **5** **_±_** **0** **_._** **0**

20 _._ 8 _±_ 36 _._ 1

61 _._ 1 _±_ 2 _._ 4

4 _._ 2 _±_ 7 _._ 2

**Table 8** Model performance on Systems & Software Engineering tasks. Values are mean scores over up to three valid

runs; adjacent entries show _±_ _s_ when at least two valid runs are available. Bold marks the best model for each task,

underlining marks the second-best model,  indicates no valid result, and \* marks fewer than three valid runs.

75

**Scientific Problems & ML Tasks**

**Opus 4.8**

**GPT-5.5**

**GPT-5.4**

**GLM-5.1**

**DS-V4-Pro**

capecod\_plume\_reconstruction

**19** **_._** **9** **_±_** **11** **_._** **1**

16 _._ 4 _±_ 5 _._ 5

12 _._ 6 _±_ 4 _._ 6

10 _._ 9 _±_ 2 _._ 5

8 _._ 8 _±_ 0 _._ 4

battery\_soh\_rul\_anomaly

**37** **_._** **2** **_±_** **10** **_._** **7**

30 _._ 2 _±_ 14 _._ 8

14 _._ 7 _±_ 1 _._ 8

18 _._ 2 _±_ 4 _._ 3

14 _._ 0 _±_ 0 _._ 6

borden\_source\_inversion

**48** **_._** **4** **_±_** **7** **_._** **3**

38 _._ 5 _±_ 14 _._ 3

8 _._ 0 _±_ 1 _._ 4

15 _._ 1 _±_ 13 _._ 7

38 _._ 2 _±_ 3 _._ 6

borden\_pump\_treat\_dispatch

14 _._ 9 _±_ 2 _._ 5

**16** **_._** **0** **_±_** **1** **_._** **6**

10 _._ 7 _±_ 0 _._ 6

14 _._ 5 _±_ 1 _._ 7

13 _._ 6 _±_ 2 _._ 1

borden\_sensor\_fault\_diagnosis

5 _._ 4 _±_ 2 _._ 6

**12** **_._** **2** **_±_** **8** **_._** **0**

3 _._ 4 _±_ 0 _._ 2

3 _._ 4 _±_ 0 _._ 3

3 _._ 0 _±_ 0 _._ 0

bridge\_gnss\_state\_forecast

22 _._ 0 _±_ 1 _._ 4

21 _._ 8 _±_ 2 _._ 3

21 _._ 0 _±_ 1 _._ 1

**23** **_._** **7** **_±_** **1** **_._** **8**

21 _._ 3 _±_ 0 _._ 5

vsg\_stability\_parameter\_

optimization

27 _._ 9 _±_ 16 _._ 6

**47** **_._** **0** **_±_** **34** **_._** **0**

5 _._ 8 _±_ 2 _._ 9

4 _._ 5 \* _±_ 0 _._ 8

4 _._ 4 _±_ 0 _._ 5

cylinder\_wake\_prediction

66 _._ 6 _±_ 4 _._ 3

**69** **_._** **9** **_±_** **4** **_._** **6**

39 _._ 8 _±_ 16 _._ 6

36 _._ 9 \* _±_ 36 _._ 0

24 _._ 2 _±_ 14 _._ 6

dabic\_gravity\_inversion

**17** **_._** **5** **_±_** **3** **_._** **0**

17 _._ 3 _±_ 0 _._ 7

15 _._ 0 \* _±_ 0 _._ 7

17 _._ 1 _±_ 0 _._ 7

13 _._ 8 \* _±_ 2 _._ 9

noisy\_product\_matching\_pipeline

**68** **_._** **1** **_±_** **6** **_._** **5**

64 _._ 3 _±_ 6 _._ 8

27 _._ 1 _±_ 24 _._ 7

44 _._ 7 _±_ 3 _._ 4

54 _._ 2 _±_ 9 _._ 1

neural\_net\_weight\_recovery

94 _._ 9 _±_ 8 _._ 9

**100** **_._** **0** \*

**100** **_._** **0** \* **_±_** **0** **_._** **0**

69 _._ 2 _±_ 0 _._ 0

65 _._ 4 \* _±_ 5 _._ 4

nanophotonic\_simulation\_

reproduction

**64** **_._** **8** **_±_** **1** **_._** **0**

38 _._ 2 \* _±_ 1 _._ 8



43 _._ 1 _±_ 9 _._ 5

42 _._ 8 _±_ 3 _._ 5

ftir\_polymer\_identification

**45** **_._** **0** **_±_** **14** **_._** **0**

32 _._ 0 \* _±_ 5 _._ 7

19 _._ 3 _±_ 16 _._ 4

12 _._ 3 _±_ 4 _._ 0

12 _._ 3 _±_ 7 _._ 1

molecular\_property\_regression

**49** **_._** **5** **_±_** **16** **_._** **9**

43 _._ 2 _±_ 5 _._ 9

23 _._ 3 _±_ 0 _._ 8

24 _._ 2 _±_ 3 _._ 7

27 _._ 1 _±_ 7 _._ 2

graph\_node\_classification

**66** **_._** **6** **_±_** **3** **_._** **0**

56 _._ 0 _±_ 15 _._ 8

57 _._ 6 _±_ 2 _._ 0

52 _._ 3 _±_ 8 _._ 7

51 _._ 8 _±_ 8 _._ 1

gravitational\_wave\_signal\_

detection

61 _._ 5 _±_ 8 _._ 1

**64** **_._** **5** **_±_** **2** **_._** **2**

50 _._ 0 _±_ 3 _._ 7

44 _._ 8 _±_ 15 _._ 7

58 _._ 8 _±_ 2 _._ 9

polyimide\_homo\_lumo\_prediction

86 _._ 7 _±_ 23 _._ 1

**100** **_._** **0** \* **_±_** **0** **_._** **0** **100** **_._** **0** \* **_±_** **0** **_._** **0** 60 _._ 0 \* _±_ 0 _._ 0

80 _._ 0 \* _±_ 28 _._ 3

industrial\_anomaly\_detection

**49** **_._** **3** **_±_** **5** **_._** **2**

40 _._ 8 _±_ 1 _._ 7

20 _._ 4 _±_ 19 _._ 6

34 _._ 4 _±_ 4 _._ 6

35 _._ 1 _±_ 5 _._ 9

bipedalwalker\_locomotion\_rl

**23** **_._** **3** **_±_** **3** **_._** **8**

21 _._ 0 _±_ 8 _._ 5

17 _._ 5 _±_ 1 _._ 2

22 _._ 5 _±_ 2 _._ 1

20 _._ 6 _±_ 4 _._ 3

molecular\_solubility\_prediction

37 _._ 3 _±_ 1 _._ 9

**51** **_._** **7** **_±_** **9** **_._** **9**

35 _._ 6 _±_ 5 _._ 0

36 _._ 8 _±_ 2 _._ 3

33 _._ 0 _±_ 4 _._ 0

motor\_clutch\_model\_reproduction

**100** **_._** **0** **_±_** **0** **_._** **0**

21 _._ 7 _±_ 37 _._ 5



20 _._ 0 \* _±_ 28 _._ 3

20 _._ 0 _±_ 34 _._ 6

streaming\_multilabel\_

classification

67 _._ 2 _±_ 2 _._ 0

63 _._ 1 _±_ 3 _._ 1

**68** **_._** **5** **_±_** **5** **_._** **2**

52 _._ 9 _±_ 6 _._ 2

60 _._ 4 _±_ 6 _._ 5

barnes\_hut\_nbody\_acceleration

78 _._ 4 _±_ 6 _._ 2

**91** **_._** **6** **_±_** **14** **_._** **5**

87 _._ 4 _±_ 15 _._ 4

64 _._ 1 _±_ 8 _._ 5

67 _._ 1 _±_ 2 _._ 2

blackbox\_numerical\_integration

**45** **_._** **1** **_±_** **9** **_._** **1**

44 _._ 3 _±_ 12 _._ 9

33 _._ 4 _±_ 5 _._ 4

40 _._ 2 _±_ 5 _._ 6

40 _._ 2 _±_ 3 _._ 4

monge\_ampere\_pde\_solver

**63** **_._** **3** **_±_** **5** **_._** **3**

37 _._ 1 _±_ 8 _._ 8

9 _._ 6 _±_ 16 _._ 5

48 _._ 1 _±_ 11 _._ 2

32 _._ 9 _±_ 30 _._ 2

ocean\_mt\_lab\_inversion

41 _._ 9 _±_ 47 _._ 4

39 _._ 7 _±_ 43 _._ 7

15 _._ 2 _±_ 3 _._ 3

**60** **_._** **8** **_±_** **40** **_._** **2**

14 _._ 5 _±_ 0 _._ 0

pv\_power\_forecasting

15 _._ 3 _±_ 1 _._ 0

**17** **_._** **2** **_±_** **1** **_._** **0**

12 _._ 6 _±_ 0 _._ 5

16 _._ 6 _±_ 0 _._ 5

14 _._ 1 _±_ 2 _._ 4

collaborative\_filtering\_

recommender

**55** **_._** **0** **_±_** **2** **_._** **9**

46 _._ 4 _±_ 9 _._ 3

14 _._ 7 _±_ 12 _._ 2

39 _._ 9 _±_ 20 _._ 5

8 _._ 5 _±_ 1 _._ 8

ecg\_signal\_processing\_pipeline

**58** **_._** **7** **_±_** **7** **_._** **3**

44 _._ 7 _±_ 8 _._ 7

39 _._ 2 _±_ 7 _._ 8

31 _._ 8 _±_ 1 _._ 9

14 _._ 3 _±_ 8 _._ 6

sketch\_solve\_least\_squares

59 _._ 4 _±_ 0 _._ 8

61 _._ 1 _±_ 2 _._ 3

60 _._ 2 _±_ 1 _._ 3

61 _._ 1 _±_ 0 _._ 8

**61** **_._** **3** **_±_** **1** **_._** **1**

substrate\_interface\_simulation

**0** **_._** **0** \* **_±_** **0** **_._** **0**

**0** **_._** **0** **_±_** **0** **_._** **0**

**0** **_._** **0** **_±_** **0** **_._** **0**

**0** **_._** **0** **_±_** **0** **_._** **0**

**0** **_._** **0** **_±_** **0** **_._** **0**

thermo\_fluid\_field\_prediction

69 _._ 6 _±_ 20 _._ 8

57 _._ 8 _±_ 15 _._ 1

39 _._ 1 _±_ 5 _._ 3

**76** **_._** **8** **_±_** **17** **_._** **8**

22 _._ 5 _±_ 15 _._ 7

csi\_time\_series\_forecasting

**83** **_._** **4** **_±_** **10** **_._** **4**

76 _._ 3 _±_ 2 _._ 5

77 _._ 3 _±_ 0 _._ 2

44 _._ 6 _±_ 3 _._ 1

40 _._ 4 _±_ 12 _._ 3

roof\_damage\_active\_learning

4 _._ 7 _±_ 8 _._ 2

**22** **_._** **8** \* **_±_** **7** **_._** **1**



4 _._ 1 _±_ 7 _._ 0

0 _._ 0 _±_ 0 _._ 0

**Table 9**

Model performance on Scientic Problems & ML tasks. Values are mean scores over up to three valid

runs; adjacent entries show _±_ _s_ when at least two valid runs are available. Bold marks the best model for each task,

underlining marks the second-best model,  indicates no valid result, and \* marks fewer than three valid runs.

76

**Combinatorial Optimization**

**Tasks**

**Opus 4.8**

**GPT-5.5**

**GPT-5.4**

**GLM-5.1 DS-V4-Pro**

symbolic\_integration\_engine

**57** **_._** **7** **_±_** **1** **_._** **1**

44 _._ 0 _±_ 4 _._ 2

30 _._ 9 _±_ 1 _._ 7

26 _._ 7 _±_ 8 _._ 9

18 _._ 4 _±_ 2 _._ 9

order\_addition\_permutation\_

optimization

**36** **_._** **4** **_±_** **5** **_._** **7**

23 _._ 3 _±_ 1 _._ 4

14 _._ 3 _±_ 12 _._ 4

33 _._ 2 _±_ 9 _._ 8

30 _._ 8 _±_ 11 _._ 3

sat\_solver

**14** **_._** **4** **_±_** **7** **_._** **6**

8 _._ 9 _±_ 0 _._ 6

13 _._ 8 _±_ 4 _._ 7

13 _._ 6 _±_ 5 _._ 7

8 _._ 0 _±_ 6 _._ 4

quantum\_architecture\_search

12 _._ 7 _±_ 1 _._ 5

**68** **_._** **3** **_±_** **22** **_._** **2** 12 _._ 5 \* _±_ 2 _._ 1

25 _._ 3 _±_ 23 _._ 1 12 _._ 0 _±_ 1 _._ 7

ad\_placement\_optimization

**67** **_._** **7** **_±_** **1** **_._** **0**

62 _._ 9 _±_ 6 _._ 2

48 _._ 1 _±_ 6 _._ 2

58 _._ 8 _±_ 14 _._ 3 36 _._ 2 _±_ 16 _._ 3

first\_order\_theorem\_prover

**31** **_._** **9** **_±_** **13** **_._** **0** 11 _._ 2 _±_ 11 _._ 2

13 _._ 1 _±_ 22 _._ 7

0 _._ 0 \*

0 _._ 0 _±_ 0 _._ 0

circuit\_layout\_optimization

**37** **_._** **3** **_±_** **2** **_._** **4**

33 _._ 0 _±_ 3 _._ 9

26 _._ 0 _±_ 3 _._ 9

31 _._ 3 _±_ 5 _._ 6

22 _._ 5 _±_ 3 _._ 5

equivalence\_class\_divide\_and\_

conquer

21 _._ 3 _±_ 4 _._ 9

**22** **_._** **4** **_±_** **12** **_._** **2**

20 _._ 3 _±_ 2 _._ 4

10 _._ 6 _±_ 2 _._ 0

3 _._ 4 _±_ 3 _._ 5

jagua\_nesting\_optimization

**44** **_._** **2** **_±_** **16** **_._** **7** 21 _._ 6 _±_ 10 _._ 9

24 _._ 1 _±_ 11 _._ 0 12 _._ 4 _±_ 8 _._ 2

28 _._ 4 _±_ 16 _._ 7

smt\_solver

**23** **_._** **9** **_±_** **7** **_._** **0**

8 _._ 6 _±_ 3 _._ 1

9 _._ 2 _±_ 2 _._ 8

3 _._ 6 \*

3 _._ 3 _±_ 1 _._ 7

tree\_block\_partitioning

**37** **_._** **7** **_±_** **6** **_._** **6**

36 _._ 4 _±_ 2 _._ 8

34 _._ 3 _±_ 4 _._ 7

23 _._ 4 _±_ 4 _._ 5

16 _._ 1 _±_ 0 _._ 9

triangulation\_coloring\_

optimization

73 _._ 4 _±_ 2 _._ 4

**75** **_._** **2** **_±_** **3** **_._** **0**

74 _._ 3 _±_ 3 _._ 3

73 _._ 0 _±_ 1 _._ 5

59 _._ 3 _±_ 10 _._ 3

vibrating\_path\_graph\_coloring

**25** **_._** **3** **_±_** **11** **_._** **7** 11 _._ 4 _±_ 5 _._ 1

24 _._ 1 _±_ 8 _._ 5

22 _._ 9 _±_ 3 _._ 2

22 _._ 1 _±_ 5 _._ 1

vehicle\_routing\_time\_windows

74 _._ 0 _±_ 16 _._ 9

**90** **_._** **8** **_±_** **2** **_._** **3**

89 _._ 6 _±_ 2 _._ 3

77 _._ 9 _±_ 8 _._ 1

83 _._ 1 _±_ 6 _._ 6

warehouse\_forklift\_routing

11 _._ 2 _±_ 1 _._ 1

**12** **_._** **6** **_±_** **0** **_._** **6**

0 _._ 0 _±_ 0 _._ 0

0 _._ 5 \* _±_ 0 _._ 3

0 _._ 0 \* _±_ 0 _._ 0

wireless\_electricity\_layout

**14** **_._** **5** **_±_** **6** **_._** **1**

7 _._ 2 _±_ 7 _._ 9

11 _._ 1 _±_ 9 _._ 6

9 _._ 5 _±_ 9 _._ 8

0 _._ 0 _±_ 0 _._ 0

**Table 10** Model performance on Combinatorial Optimization tasks. Values are mean scores over up to three valid

runs; adjacent entries show _±_ _s_ when at least two valid runs are available. Bold marks the best model for each task,

underlining marks the second-best model,  indicates no valid result, and \* marks fewer than three valid runs.

**Formal Math & Theorem Proving**

**Tasks**

**Opus 4.8**

**GPT-5.5**

**GPT-5.4**

**GLM-5.1**

**DS-V4-Pro**

combinatorial\_games\_formalization

35 _._ 5 _±_ 3 _._ 9

**38** **_._** **2** **_±_** **10** **_._** **1** 17 _._ 8 _±_ 6 _._ 8

16 _._ 2 \* _±_ 3 _._ 1

7 _._ 8 _±_ 0 _._ 9

erdos392\_formalization

**98** **_._** **0** **_±_** **3** **_._** **5**



48 _._ 0 _±_ 5 _._ 3

32 _._ 7 _±_ 11 _._ 0 10 _._ 7 _±_ 6 _._ 7

cup\_product\_formalization

74 _._ 0 _±_ 8 _._ 9

**93** **_._** **1** **_±_** **6** **_._** **1**

74 _._ 0 _±_ 1 _._ 7

38 _._ 7 _±_ 0 _._ 8

40 _._ 7 _±_ 3 _._ 4

lean\_analysis\_proofs

33 _._ 0 \*

**42** **_._** **5** **_±_** **5** **_._** **1**

16 _._ 4 _±_ 4 _._ 3

5 _._ 9 \*

9 _._ 5 _±_ 2 _._ 7

carleson\_formalization

16 _._ 8 _±_ 0 _._ 5

**26** **_._** **5** **_±_** **6** **_._** **5**

7 _._ 1 _±_ 3 _._ 2

2 _._ 2 _±_ 0 _._ 7

2 _._ 5 _±_ 1 _._ 5

new\_foundations\_consistency

65 _._ 1 \*

**66** **_._** **5** **_±_** **2** **_._** **0**

39 _._ 8 _±_ 12 _._ 2

27 _._ 0 _±_ 27 _._ 5 11 _._ 4 _±_ 4 _._ 9

godel\_incompleteness\_

formalization

**100** **_._** **0** **_±_** **0** **_._** **0**



64 _._ 4 _±_ 30 _._ 8

46 _._ 7 \*

6 _._ 7 _±_ 0 _._ 0

medium\_prime\_number\_theorem

**100** **_._** **0** \* **_±_** **0** **_._** **0**



88 _._ 0 _±_ 0 _._ 0

26 _._ 7 _±_ 8 _._ 1

9 _._ 0 _±_ 0 _._ 0

ordinal\_notation\_well\_foundedness

**24** **_._** **7** **_±_** **0** **_._** **0**

**24** **_._** **7** **_±_** **0** **_._** **0**

21 _._ 6 _±_ 5 _._ 4

5 _._ 9 _±_ 0 _._ 0

4 _._ 7 \* _±_ 1 _._ 7

pfr\_formalization

46 _._ 3 \*

**60** **_._** **0** **_±_** **2** **_._** **7**

38 _._ 9 _±_ 1 _._ 3

33 _._ 5 _±_ 1 _._ 4

19 _._ 1 _±_ 5 _._ 4

sphere\_eversion\_formalization

55 _._ 4 _±_ 3 _._ 7

**58** **_._** **5** **_±_** **2** **_._** **9**

51 _._ 4 _±_ 1 _._ 7

30 _._ 2 _±_ 21 _._ 3 29 _._ 3 _±_ 7 _._ 7

turing\_machine\_halting\_proofs

**15** **_._** **0** **_±_** **0** **_._** **0**

**15** **_._** **0** **_±_** **0** **_._** **0**

**15** **_._** **0** **_±_** **0** **_._** **0**

**15** **_._** **0** **_±_** **0** **_._** **0**

**15** **_._** **0** **_±_** **0** **_._** **0**

flt\_regular\_formalization

50 _._ 6 _±_ 0 _._ 0

**75** **_._** **1** **_±_** **24** **_._** **7** 48 _._ 3 _±_ 4 _._ 0

38 _._ 7 _±_ 13 _._ 4 17 _._ 6 _±_ 11 _._ 3

**Table 11** Model performance on Formal Math & Theorem Proving tasks. Values are mean scores over up to three

valid runs; adjacent entries show _±_ _s_ when at least two valid runs are available. Bold marks the best model for each

task, underlining marks the second-best model,  indicates no valid result, and \* marks fewer than three valid runs.

77

**Professional Knowledge Work**

**Tasks**

**Opus 4.8**

**GPT-5.5**

**GPT-5.4**

**GLM-5.1 DS-V4-Pro**

portfolio\_risk\_calibration

24 _._ 5 _±_ 7 _._ 5

**25** **_._** **0** **_±_** **6** **_._** **5**

10 _._ 7 _±_ 3 _._ 9

9 _._ 4 _±_ 14 _._ 2

23 _._ 7 _±_ 6 _._ 9

storyboard\_ad\_copywriting

79 _._ 7 _±_ 8 _._ 1

77 _._ 0 _±_ 5 _._ 3

65 _._ 7 _±_ 14 _._ 6 **92** **_._** **0** **_±_** **5** **_._** **0** 56 _._ 5 \* _±_ 7 _._ 8

cross\_border\_investment\_ppt

38 _._ 3 _±_ 4 _._ 7

34 _._ 0 \* _±_ 2 _._ 2

35 _._ 7 _±_ 6 _._ 5

**45** **_._** **9** **_±_** **7** **_._** **0**

32 _._ 3 _±_ 5 _._ 9

herbal\_depression\_target\_

screening

**70** **_._** **3** **_±_** **5** **_._** **9**

68 _._ 1 _±_ 3 _._ 1

58 _._ 9 _±_ 7 _._ 9

57 _._ 0 _±_ 12 _._ 8

60 _._ 1 _±_ 3 _._ 3

pancreatic\_radiotherapy\_meta\_

analysis

**40** **_._** **2** **_±_** **5** **_._** **7**

39 _._ 8 _±_ 3 _._ 2

30 _._ 6 _±_ 4 _._ 1

36 _._ 5 _±_ 5 _._ 2

34 _._ 5 _±_ 7 _._ 2

touchstone\_vna\_diagnostics

**39** **_._** **9** **_±_** **2** **_._** **8**

11 _._ 5 _±_ 4 _._ 9

8 _._ 4 _±_ 1 _._ 1

4 _._ 7 _±_ 1 _._ 8

4 _._ 5 _±_ 2 _._ 4

high\_performance\_object\_mapper



62 _._ 2 _±_ 2 _._ 9

45 _._ 6 _±_ 8 _._ 9

**64** **_._** **0** **_±_** **1** **_._** **3**

51 _._ 0 _±_ 7 _._ 2

odata\_query\_service

30 _._ 9 _±_ 1 _._ 1

27 _._ 8 _±_ 3 _._ 3

**31** **_._** **1** **_±_** **4** **_._** **9** 26 _._ 1 _±_ 3 _._ 2

20 _._ 8 _±_ 11 _._ 0

brand\_annual\_planning\_ppt

51 _._ 3 _±_ 19 _._ 8

69 _._ 0 _±_ 11 _._ 0

72 _._ 3 _±_ 2 _._ 1

**73** **_._** **7** **_±_** **9** **_._** **2**

50 _._ 0 _±_ 10 _._ 0

securities\_protection\_training

**97** **_._** **2** **_±_** **4** **_._** **3**

89 _._ 4 _±_ 8 _._ 2

94 _._ 2 _±_ 5 _._ 2

93 _._ 8 _±_ 1 _._ 5

85 _._ 0 _±_ 9 _._ 5

college\_english\_exam\_bank

**39** **_._** **8** **_±_** **4** **_._** **3**

37 _._ 8 _±_ 7 _._ 8

34 _._ 5 _±_ 2 _._ 3

32 _._ 5 _±_ 1 _._ 3

34 _._ 7 _±_ 10 _._ 3

cross\_border\_commission\_

compliance

32 _._ 1 _±_ 2 _._ 4

**43** **_._** **8** \* **_±_** **2** **_._** **1**

29 _._ 8 \*

39 _._ 2 _±_ 12 _._ 3

35 _._ 2 _±_ 5 _._ 4

cta\_risk\_budget\_optimization

46 _._ 1 _±_ 1 _._ 4

46 _._ 7 _±_ 3 _._ 8

**49** **_._** **8** **_±_** **2** **_._** **8**

49 _._ 6 _±_ 0 _._ 7

48 _._ 1 _±_ 4 _._ 1

equity\_objection\_report

15 _._ 5 _±_ 4 _._ 3

**22** **_._** **5** **_±_** **2** **_._** **3**

15 _._ 3 _±_ 6 _._ 5

14 _._ 7 _±_ 3 _._ 8

14 _._ 8 _±_ 11 _._ 2

expo\_visitor\_conversion\_model

**81** **_._** **9** **_±_** **1** **_._** **6**

54 _._ 9 _±_ 23 _._ 9 29 _._ 1 _±_ 10 _._ 0

79 _._ 0 _±_ 3 _._ 8

46 _._ 2 _±_ 26 _._ 7

factor\_stock\_model\_optimization

51 _._ 0 _±_ 1 _._ 5

**58** **_._** **8** **_±_** **6** **_._** **9**

36 _._ 3 _±_ 3 _._ 2

54 _._ 3 _±_ 1 _._ 5

35 _._ 6 _±_ 11 _._ 9

global\_terrorism\_atlas\_report

19 _._ 4 _±_ 2 _._ 6

**21** **_._** **5** **_±_** **5** **_._** **5**

15 _._ 7 \*

17 _._ 3 _±_ 4 _._ 4

15 _._ 2 _±_ 1 _._ 7

hebei\_gaokao\_strategy\_report

69 _._ 9 _±_ 16 _._ 3

**82** **_._** **0** \* **_±_** **2** **_._** **8**

78 _._ 7 _±_ 4 _._ 7

71 _._ 0 _±_ 1 _._ 7

62 _._ 5 \* _±_ 13 _._ 5

hk\_connect\_annual\_metrics

**73** **_._** **4** **_±_** **11** **_._** **5**

61 _._ 8 _±_ 3 _._ 2

45 _._ 2 _±_ 14 _._ 4 44 _._ 8 _±_ 18 _._ 4

41 _._ 5 _±_ 10 _._ 9

k12\_math\_recommendation

**44** **_._** **3** **_±_** **0** **_._** **5**

44 _._ 0 _±_ 13 _._ 3

31 _._ 4 _±_ 4 _._ 2

32 _._ 7 _±_ 8 _._ 2

26 _._ 3 _±_ 2 _._ 2

property\_actuarial\_pricing

**28** **_._** **0** \* **_±_** **0** **_._** **0** **28** **_._** **0** \* **_±_** **0** **_._** **0** **28** **_._** **0** **_±_** **0** **_._** **0** **28** **_._** **0** **_±_** **0** **_._** **0**

**28** **_._** **0** **_±_** **0** **_._** **0**

real\_estate\_bid\_estimate

52 _._ 5 _±_ 6 _._ 1

**57** **_._** **3** **_±_** **1** **_._** **9**

51 _._ 5 _±_ 7 _._ 0

49 _._ 6 _±_ 3 _._ 9

40 _._ 6 _±_ 3 _._ 0

stock\_momentum\_backtest

9 _._ 8 _±_ 4 _._ 9

10 _._ 7 \* _±_ 1 _._ 2

8 _._ 2 _±_ 2 _._ 8

4 _._ 1 \* _±_ 1 _._ 2

**11** **_._** **5** **_±_** **2** **_._** **8**

storm\_claim\_ring\_audit

**43** **_._** **9** **_±_** **14** **_._** **3**

24 _._ 0 _±_ 0 _._ 0

24 _._ 0 _±_ 0 _._ 0

24 _._ 0 _±_ 0 _._ 0

30 _._ 3 _±_ 7 _._ 8

**Table 12** Model performance on Professional Knowledge Work tasks. Values are mean scores over up to three valid

runs; adjacent entries show _±_ _s_ when at least two valid runs are available. Bold marks the best model for each task,

underlining marks the second-best model,  indicates no valid result, and \* marks fewer than three valid runs.

**Interactive Games & Simulators**

**Tasks**

**Opus 4.8**

**GPT-5.5**

**GPT-5.4**

**GLM-5.1 DS-V4-Pro**

openttd\_transport\_ai

**52** **_._** **0** **_±_** **8** **_._** **5**

28 _._ 1 _±_ 24 _._ 4

11 _._ 9 _±_ 20 _._ 5

0 _._ 0 _±_ 0 _._ 0

15 _._ 2 _±_ 26 _._ 4

nethack\_dungeon\_agent

**41** **_._** **9** **_±_** **9** **_._** **1**

22 _._ 5 _±_ 4 _._ 8

20 _._ 4 _±_ 11 _._ 2 21 _._ 6 _±_ 16 _._ 2

3 _._ 3 _±_ 2 _._ 3

treant\_forest

**18** **_._** **0** **_±_** **4** **_._** **9** 15 _._ 6 _±_ 6 _._ 7

13 _._ 3 _±_ 7 _._ 9

16 _._ 9 _±_ 2 _._ 4

13 _._ 5 _±_ 4 _._ 8

grid\_turing\_robot

40 _._ 3 _±_ 3 _._ 6

**42** **_._** **2** **_±_** **2** **_._** **7**

28 _._ 9 _±_ 11 _._ 3 25 _._ 7 _±_ 5 _._ 9

24 _._ 2 _±_ 6 _._ 0

molecular\_self\_assembly

**34** **_._** **7** **_±_** **0** **_._** **9** 20 _._ 7 _±_ 1 _._ 0

21 _._ 6 _±_ 0 _._ 6

13 _._ 2 _±_ 5 _._ 9

21 _._ 9 _±_ 3 _._ 5

apple\_incremental\_game

**50** **_._** **6** **_±_** **8** **_._** **1** 33 _._ 6 _±_ 15 _._ 9

34 _._ 9 _±_ 14 _._ 7 19 _._ 1 _±_ 1 _._ 1

19 _._ 7 _±_ 0 _._ 1

dcss\_dungeon\_ai

8 _._ 3 _±_ 3 _._ 5

**13** **_._** **4** **_±_** **0** **_._** **5**

6 _._ 1 _±_ 4 _._ 7

7 _._ 6 _±_ 4 _._ 3

5 _._ 7 _±_ 3 _._ 7

anchorhead\_text\_adventure

22 _._ 3 _±_ 4 _._ 5

**36** **_._** **3** **_±_** **6** **_._** **4**

17 _._ 7 _±_ 2 _._ 3

20 _._ 3 _±_ 0 _._ 6

14 _._ 7 _±_ 8 _._ 1

trinity\_text\_adventure

30 _._ 0 _±_ 2 _._ 6

**40** **_._** **0** **_±_** **10** **_._** **5** 27 _._ 0 _±_ 7 _._ 0

26 _._ 7 _±_ 5 _._ 7

20 _._ 3 _±_ 3 _._ 8

tryst\_text\_adventure

44 _._ 3 _±_ 8 _._ 7

**55** **_._** **7** **_±_** **3** **_._** **8**

44 _._ 3 _±_ 7 _._ 6

43 _._ 3 _±_ 4 _._ 4

13 _._ 8 _±_ 3 _._ 3

openrct2\_theme\_park\_ai

27 _._ 5 _±_ 0 _._ 0

**37** **_._** **6** **_±_** **9** **_._** **0**

23 _._ 1 _±_ 11 _._ 7

36 _._ 2 _±_ 9 _._ 5

26 _._ 0 _±_ 2 _._ 6

wesnoth\_tactical\_ai

**88** **_._** **0** **_±_** **2** **_._** **6** 79 _._ 3 _±_ 6 _._ 4

81 _._ 3 _±_ 1 _._ 5

78 _._ 3 _±_ 11 _._ 0 36 _._ 3 _±_ 31 _._ 5

**Table 13** Model performance on Interactive Games & Simulators tasks. Values are mean scores over up to three valid

runs; adjacent entries show _±_ _s_ when at least two valid runs are available. Bold marks the best model for each task,

underlining marks the second-best model,  indicates no valid result, and \* marks fewer than three valid runs.

78

**H**

**Acknowledgements**

We thank UniPat for collaborating with us on the development of 13 tasks in the Systems & Software

Engineering portion of EdgeBench. We also thank Xiaoxing Wu, Xiang Gao, Gao Liu, Yue Yang, Wen Heng,

Weinan Zhao, Mailun Gao, Zongbao Zhang, and Yuchen Wu for helpful supporting contributions during

the project. We thank Xinkai Zhou and Qi Zhao for meaningful discussions during the project. We thank

Tenglong Ao, Ao Zhang, Shengjie Luo, Zeyi Zhang, Guhao Feng, Tianle Cai, Xinrong Zhang, Yizhong Wang,

and Ruinian Chang for meaningful discussions and collaborations that took place prior to the EdgeBench

project.

79