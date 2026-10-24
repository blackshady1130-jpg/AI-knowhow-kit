# A good teacher meets the student where they are

- **作者**：Perplexity Research & NVIDIA
- **发布日期**：2026年10月21日
- **来源**：Perplexity
- **原文链接**：https://www.perplexity.ai/hub/blog/a-good-teacher-meets-the-student-where-they-are

A new self-distillation method that jointly trains teacher and student to improve model performance and training efficiency on complex reasoning and agentic tasks.

## Introduction

Reinforcement Learning (RL) is widely used in post-training language models to improve their capabilities on complex reasoning and long-horizon agentic tasks.

In a typical setup, the model makes repeated attempts at a task, receives an outcome reward for each, and learns to favor actions taken in higher-reward attempts. However, a single outcome reward provides a sparse learning signal that does not distinguish which intermediate actions helped or hurt the outcome. This sparsity limits sample efficiency, especially on difficult agentic tasks, where attempts are long and successes are rare.

One popular approach to addressing this sparsity is On-Policy Distillation (OPD), which uses a stronger teacher model to give token by token guidance to the student’s own attempts, providing much denser rewards. However, teaching is a skill in itself. A model that is good at solving a task is not necessarily good at teaching it, as its feedback may be beyond the student’s current capabilities. This motivates training not only the student to imitate the teacher but also the teacher to provide better-aligned guidance to the student.

We propose one such method, [Joint On-policy Learning and Teaching](https://arxiv.org/abs/2610.10447) (JOLT). Building on On-Policy Self-Distillation (OPSD), we use a single model in two roles: a teacher with access to privileged information, such as verified solutions, and a student without such access. We train the two roles jointly. The student follows the standard distillation objective. The teacher’s objective pushes its feedback to move the student in the same direction as RL on the student's own reward. Together, these objectives train the teacher to meet the student where they are and help the student learn from guidance within their reach.

Our experiments demonstrate improvements in both model performance and training efficiency across a range of mathematical reasoning, coding, and agentic tasks.

## From sparse rewards to dense feedback

In its most basic form, outcome-reward RL uses the expected return objective:

$$
\mathcal{J}_{\mathrm{RL}}(\theta) = \mathbb{E}_{\tau\sim\pi_\theta}\left[R(\tau)\right]
$$

Here, $\tau$ is a trajectory following a policy $\pi_\theta$, and $R(\tau)$ is the return for that trajectory. The corresponding policy gradient is:

$$
g_{\mathrm{RL}}(\theta) = \nabla_\theta \mathcal{J}_{\mathrm{RL}}(\theta) = \mathbb{E}_{\tau\sim\pi_\theta}\left[\sum_t R(\tau)\,\nabla_\theta\log\pi_\theta(a_t\mid s_t)\right]
$$

where $s_t$ and $a_t$ represent the state and action, respectively, at timestep $t$. To reduce the variance of sample-based estimates, the gradient is often expressed as:

$$
g_{\mathrm{RL}}(\theta) = \mathbb{E}_{\tau\sim\pi_\theta}\left[\sum_t A^{\pi_\theta}(s_t,a_t)\,\nabla_\theta\log\pi_\theta(a_t\mid s_t)\right]
$$

where the advantage $A^{\pi_\theta}(s_t, a_t)$ measures the expected excess return of action $a_t$ relative to the current policy at state $s_t$. One approach, [Group Relative Policy Optimization](https://arxiv.org/abs/2402.03300) (GRPO), estimates the advantage by comparing each trajectory's return to the mean return of the group sampled for the same prompt.

However, even with these adjustments, outcome-reward reinforcement learning suffers from sparse supervision, particularly on difficult, long-horizon tasks. A growing body of work addresses this by drawing on additional sources of information to provide a denser learning signal.

[On-Policy Distillation](https://arxiv.org/abs/2306.13649) (OPD) is one such approach. Rather than learning only from a final reward, OPD samples trajectories from the student and evaluates each sampled action under a stronger teacher. For a teacher policy $\pi_T$ and a fixed snapshot $\bar{\theta}$ of the student parameters used to generate the trajectories, the local gradient evaluated at $\theta = \bar{\theta}$ is:

$$
\begin{aligned}g_{\mathrm{OPD}}(\bar\theta;\pi_T) &= \left.\nabla_\theta \mathcal{J}_{\mathrm{OPD}}(\theta;\bar\theta,\pi_T)\right|_{\theta=\bar\theta}\\ &= -\left.\nabla_\theta \mathbb{E}_{\tau\sim\pi_{\bar\theta}}\!\left[\sum_t \mathrm{KL}\!\left(\pi_\theta(\cdot\mid s_t)\,\middle\|\,\pi_T(\cdot\mid s_t)\right)\right]\right|_{\theta=\bar\theta}\\ &= \mathbb{E}_{\tau\sim\pi_{\bar\theta}}\left[\sum_t \bigl(\log\pi_T(a_t\mid s_t)-\log\pi_{\bar\theta}(a_t\mid s_t)\bigr)\,\nabla_{\bar\theta}\log\pi_{\bar\theta}(a_t\mid s_t)\right]\end{aligned}
$$

Here, $\mathcal{J}_{\mathrm{OPD}}(\theta;\bar\theta,\pi_T)$ is the negative reverse-KL distillation objective. The teacher policy and sampled prefixes are held fixed during differentiation. The teacher-student log-probability ratio provides a dense learning signal at every visited state, replacing the advantage as the action-level weight.

[On-Policy Self-Distillation](https://arxiv.org/abs/2601.18734) (OPSD) further removes the need for a separate teacher model. The student policy serves as its own teacher given privileged information, such as a verified solution, feedback, or a reference trace. However, OPSD only trains the student to imitate the teacher; there’s no mechanism to ensure that the teacher provides useful signal to the student.

## Joint on-policy learning and teaching

JOLT extends OPSD by training a shared model as both the teacher that provides better-aligned guidance and the student that learns from it. The better-informed teacher learns from outcome rewards with KL regularization toward the student, while the unprivileged student learns from the teacher’s dense distillation signal. The teacher update uses teacher-generated attempts, while the student update uses student-generated attempts scored by the teacher. JOLT+ further supplements the student’s distillation signal with outcome rewards.

![Diagram: One policy learns as both teacher and student](https://cdn.sanity.io/images/aqo64vfr/production/c4309a1bdd9dd1b13c8c9f2dca2bb1ba2bb517fa-1280x720.svg?w=1280&q=90&fit=max&auto=format)

*放大 图 01 One policy learns as both teacher and student.*

### Training the teacher

#### Define what a teacher should do

Better teacher performance doesn’t necessarily translate to useful updates to the student. A teacher may use privileged information to exploit shortcuts unavailable to the student, assign high probability to trajectories that are unlikely under the student, or provide unreliable guidance after errors in student-generated prefixes. Teacher quality should therefore be determined by the learning signal provided to the student, rather than by the teacher’s own task reward.

We call a teacher reward-consistent if the distillation update it induces in the student matches the policy gradient of a student’s expected task reward, up to positive scaling. Specifically, a reward-consistent teacher $\pi_T^\star$ should satisfy:

$$
g_{\mathrm{OPD}}(\bar\theta;\pi_T^\star) = \frac{1}{\beta_T}\,g_{\mathrm{RL}}(\bar\theta)
$$

where $\beta_T$ is a positive scalar. As in the previous section, $g_{\mathrm{OPD}}$ is the OPD local gradient, $\bar\theta$ is a fixed snapshot of the student model parameters $\theta$, and $g_{\mathrm{RL}}$ is the policy gradient of the expected return objective.

One teacher that satisfies this condition is:

$$
\pi_T^\star(a\mid s,c) = \frac{1}{Z(s)}\,\pi_{\bar\theta}(a\mid s)\exp\!\left(\frac{1}{\beta_T}A^{\pi_{\bar\theta}}(s,a)\right)
$$

Here, $A^{\pi_{\bar{\theta}}}(s, a)$ represent student continuation advantages and $Z(s)$ is a normalizing constant to ensure a proper probability distribution.

#### From the ideal target to a teacher objective

We can train a teacher toward the ideal target $\pi_T^\star$ by minimizing its KL divergence to it. For a fixed student and state $s$, this gives:

$$
\min_{\pi_T}\,\mathrm{KL}\!\left(\pi_T(\cdot\mid s,c)\,\middle\|\,\pi_T^\star(\cdot\mid s,c)\right)
$$

Substituting the expression for $\pi_T^\star$ gives an equivalent maximization problem:

$$
\max_{\pi_T}\Biggl\{\mathbb{E}_{a\sim\pi_T(\cdot\mid s,c)}\!\left[A^{\pi_{\bar\theta}}(s,a)\right]-\beta_T\,\mathrm{KL}\!\left(\pi_T(\cdot\mid s,c)\,\middle\|\,\pi_{\bar\theta}(\cdot\mid s)\right)\Biggr\}
$$

This objective encourages the teacher to choose actions with higher student advantage while staying close to the student’s action distribution. The parameter $\beta_T$ controls the strength of this penalty: larger values keep the teacher closer to the student’s current behavior, while smaller values allow it to favor high-advantage actions more aggressively.

#### A practical surrogate objective

This objective depends on how well the student would continue after each action, but those student continuation advantages are generally unavailable. We therefore use centered returns from the teacher’s own trajectories as a practical surrogate. The reward term encourages the teacher to solve the task, while the KL term discourages departures from the student’s current action distribution. Although the KL term keeps the teacher close to the student, this substitution is not exact, as the teacher’s returns need not match the student’s continuation advantages.

$$
\begin{aligned}\mathcal{J}_T(\theta;\bar\theta) = \mathbb{E}_{\tau\sim\pi_{\bar\theta}(\cdot\mid c)}\Biggl[\,\sum_t \Bigl(&\operatorname{sg}\bigl[\widehat{A}_T(\tau)\bigr]\log\pi_\theta(a_t\mid s_t,c)\\ &-\beta_T\,\mathrm{KL}\bigl(\pi_\theta(\cdot\mid s_t,c)\,\big\|\,\operatorname{sg}[\pi_{\bar\theta}(\cdot\mid s_t)]\bigr)\Bigr)\Biggr]\end{aligned}
$$

Here, $\widehat{A}_T(\tau)$ is the teacher attempt’s return minus the mean return of the teacher-generated attempts in its group. The operator $\operatorname{sg}$ denotes stop-gradient: its argument is treated as fixed during differentiation, as are the sampled prefixes and student reference.

### Training the student

The student update is a standard OPSD update. The student generates trajectories from the task. The same model then scores each sampled token with the privileged information in context. The student objective penalizes the reverse KL divergence between the student and this privileged teacher at every state the student visits:

$$
\mathcal{J}_{\mathrm{OPSD}}(\theta;\bar\theta) = -\,\mathbb{E}_{\tau\sim\pi_{\bar\theta}}\left[\sum_t \mathrm{KL}\bigl(\pi_\theta(\cdot\mid s_t)\,\big\|\,\operatorname{sg}[\pi_{\bar\theta}(\cdot\mid s_t,c)]\bigr)\right]
$$

Therefore, tokens the teacher prefers are reinforced, while tokens the teacher considers less likely than the student does are suppressed.

### Putting it together

Combining the teacher and student objectives gives the joint training objective:

$$
\mathcal{J}_{\mathrm{JOLT}}(\theta;\bar\theta) = \mathcal{J}_T(\theta;\bar\theta) + \beta_S\,\mathcal{J}_{\mathrm{OPSD}}(\theta;\bar\theta)
$$

$\beta_S$ is a scalar that sets how much the student distillation loss counts in the combined update.

The reward-consistency result characterizes the student’s distillation update for a given teacher. JOLT uses this principle to guide joint training, combining the teacher and student objectives to update their shared parameters.

JOLT+ also adds the student's own outcome reward to its update. The centered return of each student trajectory is added to the distillation signal, combining dense teacher supervision with direct outcome feedback on student trajectories. The teacher objective is unchanged, so we can write:

$$
\begin{aligned}\mathcal{J}_{\mathrm{JOLT+}}(\theta;\bar\theta) &= \mathcal{J}_T(\theta;\bar\theta)+\beta_S\,\mathcal{J}_{\mathrm{OPSD}}(\theta;\bar\theta)\\ &\quad+\mathbb{E}_{\tau\sim\pi_{\bar\theta}}\!\left[\sum_t \operatorname{sg}[\widehat{A}_S(\tau)]\,\log\pi_\theta(a_t\mid s_t)\right]\end{aligned}
$$

Here, $\widehat{A}_S(\tau)$ is the student trajectory’s return minus the mean return of its group of student-generated trajectories.

In both variants, each role learns from trajectories generated under its own context, and both roles update the shared policy. The pseudocode for a training step is shown below.

![JOLT pseudocode showing teacher generation with a hint, student generation without it, cross-context scoring, and a shared policy update. JOLT+ adds outcome rewards for student attempts.](https://cdn.sanity.io/images/aqo64vfr/production/ca7ce278d46007b5ac9f22bd4cf9c7cc726e7cb3-1280x719.svg?w=1280&q=90&fit=max&auto=format)

*放大 Pseudocode for one JOLT training step.*

## Experiments

We evaluate JOLT and JOLT+ on benchmarks spanning mathematical reasoning, code generation, tool use, and long-horizon terminal tasks, using different base models and different forms of privileged information. Specifically, we run experiments using the following benchmarks, base models, and privileged information configurations:

- **GSM8K**: We train [`DeepSeek-V2-Lite`](https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite) on [GSM8K](https://arxiv.org/abs/2110.14168), a dataset of grade-school math problems. The teacher receives the verified answer to each problem.

- **MATH**: We train [`Qwen3-0.6B`](https://huggingface.co/Qwen/Qwen3-0.6B) on [MATH](https://arxiv.org/abs/2103.03874). The teacher receives worked reference solutions.

- **LCBv6**: We train [`Qwen3-8B`](https://huggingface.co/Qwen/Qwen3-8B) on 131 coding problems from [LiveCodeBench-V6](https://arxiv.org/abs/2403.07974). The teacher receives a model-generated solution that passed all training-visible tests, or execution feedback when no attempt passed them.

- **AppWorld**: We train [`Qwen3-4B-Instruct`](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) on [AppWorld](https://arxiv.org/abs/2407.18901). The teacher receives summaries of previous attempts.

- **Terminal-Bench**: We train [`Qwen3-30B-A3B-Instruct`](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507) on [TMax](https://arxiv.org/abs/2606.23321), a set of training tasks for terminal agents, and evaluate on [Terminal-Bench 2.1](https://arxiv.org/abs/2601.11868). The teacher receives private verifier information.

We compare against GRPO, OPSD, and [π-Distill](https://arxiv.org/abs/2602.04942), tuning hyperparameters for each method. Like JOLT, π-Distill jointly trains privileged teacher and student roles within a shared model; however, it uses a different teacher target and its student update remains off-policy, relying on teacher-generated trajectories rather than the student’s own generations.

### Accuracy

JOLT+ has the highest mean score in every setting we evaluate. Compared with GRPO, the strongest baseline tested, it improves GSM8K accuracy by 1.5 percentage points (pp), MATH accuracy by 4.2pp, LCBv6 accuracy by 3.0pp, and the AppWorld state-test pass rate by 9.9pp.

![Dot and whisker: JOLT+ has the highest mean score on all four benchmarks](https://cdn.sanity.io/images/aqo64vfr/production/0d460cf84f363485224963c61ba38db1fd3a3ced-1280x720.svg?w=1280&q=90&fit=max&auto=format)

*放大 图 02 JOLT+ has the highest mean score on all four benchmarks.*

Without any direct student reward, JOLT's mean accuracy is higher than GRPO's on GSM8K, MATH, and LCBv6. However, on AppWorld, it stays below both GRPO and π-Distill.

Terminal-Bench 2.1 is the longest-horizon setting. JOLT+ has the highest pass@k at every reported k, from 10.96% at pass@1 to 34.83% at pass@32. JOLT improves on the base model and both distillation baselines at every k, but stays below GRPO. OPSD scores below the base model at every k.

![Line chart: JOLT+ leads Terminal-Bench at every attempt budget](https://cdn.sanity.io/images/aqo64vfr/production/0457bb0168f385b9eef3971af3c12a52ddbdb139-1280x720.svg?w=1280&q=90&fit=max&auto=format)

*放大 图 03 JOLT+ leads Terminal-Bench at every attempt budget.*

### Token efficiency and scaling

We are also interested in how performance scales with training budget. We evaluate GRPO, OPSD, and JOLT across different training token budgets on MATH and compare the resulting student accuracy.

The figure shows how accuracy scales with training token expenditure for each method. We measure cost in processed training tokens. This includes every unpadded prompt, privileged context, optimization pass, and cross-scoring between the teacher and student.

![Scatter with fitted curves: JOLT needs fewer tokens to reach GRPO’s accuracy](https://cdn.sanity.io/images/aqo64vfr/production/874bf5bbd168d01f22fceae95cd11f2d22bde0ca-1280x800.svg?w=1280&q=90&fit=max&auto=format)

*放大 图 04 JOLT needs fewer tokens to reach GRPO’s accuracy.*

Points show the number of processed training tokens and accuracy at various checkpoints; whiskers represent ±1 standard deviation across runs. We fit a sigmoidal relationship between accuracy and log training token budget, following [prior work](https://arxiv.org/abs/2510.13786) on scaling RL compute.

JOLT exhibits early sample efficiency while achieving the highest accuracy of the three methods, leveling off near 72%. OPSD improves quickly at small budgets, but plateaus at about 62% accuracy. GRPO learns more slowly at first, but continues improving for longer, climbing to about 70%. At a matched accuracy of 63.44%, GRPO's observed checkpoint uses 8.40 million tokens, while JOLT's fitted curve gives 1.30 million, 6.5× fewer tokens.

We also measure cost using completion tokens, which count student completions for GRPO and OPSD, and both teacher and student completions for JOLT, but omit prompts, privileged context, and the extra optimization passes. Comparison based on completion tokens rather than processed training tokens widens the efficiency gap to about 13× at the same accuracy level. Over a range of target accuracies, JOLT uses 9.5–14.4× fewer completion tokens and 4.3–7.4× fewer processed training tokens.

![Dumbbell: JOLT’s token advantage holds from 55% to 65% accuracy](https://cdn.sanity.io/images/aqo64vfr/production/946a81f2aeb65ed545bc2cd52a0de40c30e273bf-1280x720.svg?w=1280&q=90&fit=max&auto=format)

*放大 图 05 JOLT’s token advantage holds from 55% to 65% accuracy.*

## Conclusion

Privileged information can make a teacher better at solving a task without making it better at teaching a student to solve the same task without that information. JOLT addresses this distinction by training the teacher relative to the student’s current behavior.

This joint training improves both accuracy and efficiency. With student outcome rewards, JOLT+ achieves absolute gains over GRPO of 1.5pp on GSM8K, 4.2pp on MATH, 3.0pp on LCBv6, 9.9pp on AppWorld, and 2.7pp on Terminal-Bench 2.1 pass@1. On MATH, JOLT uses 13× fewer completion tokens and 6.5× fewer processed training tokens than GRPO at matched accuracy, without direct student reward.

JOLT allows the teacher guidance to evolve alongside the student. This motivates exploring whether the teacher can also learn to generate useful training tasks. An interesting direction for future work is to jointly train a task-generating teacher and a problem-solving student, using the student’s learning progress to improve the generated tasks in a curriculum. This could make synthetic task generation responsive to what the student is ready to learn next.

Read our [full paper](https://arxiv.org/abs/2610.10447) for more details. We will open-source the code soon.

## Citation

```
@online
{perplexity2026AGoodTeacherMeetsTheStudentWhereTheyAre,
author
= {{Perplexity} and Randy Ardywibowo and Arnav Dalal and Jiantao Jiao and Jarrod Bryan and Claire Beamer and Jeremy Yang and Jerry Ma},
title
= {{A good teacher meets the student where they are}},
date
= {2026-10-21},
url
= {https://www.perplexity.ai/hub/blog/a-good-teacher-meets-the-student-where-they-are}
}
```


[1]: https://www.perplexity.ai/hub/blog/a-good-teacher-meets-the-student-where-they-are "A good teacher meets the student where they are"
