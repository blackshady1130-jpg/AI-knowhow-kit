**Zhuokai Zhao** (@zhuokaiz)  Thu May 14 21:46:32 +0000 2026

Qwen3, GLM-5, and MiMo all use on-policy distillation in post-training. Thinking Machines also wrote it up as a cheap alternative to RL.

But in practice it is surprisingly brittle to make work — much more so than SFT or RL.

Three recent papers [1, 2, 3] helped me make sense of why. The mechanism is consistent across the failure modes they describe, and it's worth understanding before running another OPD experiment.

OPD looks like "match the teacher distribution." But in practice, the update is driven by a very small set of next-token choices at each generation step. Mostly just the handful of tokens that both the student and teacher think are plausible as the next token. Once that small set breaks, OPD breaks.

The real object OPD is learning on
At every generation step, the model has a huge vocabulary. 150K tokens, maybe more. But almost all of the probability mass sits on a tiny number of tokens.

One paper [1] shows that the overlapping high-probability tokens between teacher and student carry around 97–99% of the total probability mass. So although OPD is written as reverse-KL over a full vocabulary, most of the useful learning signal comes from a tiny local menu of next-token options.

Here is what I mean by "the handful of tokens." For a given prefix like:

"Let's solve this step by step. First, we…"

the student may think the next token should be one of:
"need", "can", "have", "find", "know", "compute", …

The teacher has its own version of this menu.

OPD works when these two menus mostly overlap, and when the teacher puts higher probability on better choices inside that menu.

It fails for a few different reasons — the menus don't overlap, the menu drifts somewhere bad mid-training, we only look at one item on the menu instead of the whole thing, or the per-position learning signals end up pulling the model in inconsistent directions.

Four things can go wrong. The first two are about whether the menu is in good shape. The third is about whether we look at the whole menu or just one item from it. The fourth is about whether the signals across positions combine into a useful update.

1. The student and teacher are thinking in different "languages"
A stronger teacher does not necessarily make a better OPD teacher.

Li et al. [1] shows this very clearly: a 7B teacher can outperform a 1.5B model on benchmarks, but still fail to improve the 1.5B student through OPD.

Why? Because benchmark accuracy measures final answers. OPD trains on next-token probabilities. A stronger model may solve the same problem through a different reasoning path: different intermediate steps, different phrasing, different proof structure, different local token choices.

So when the student writes its own partial solution, the teacher may not assign useful probability to the student's next natural steps. The teacher is better overall, but not necessarily helpful on the student's current path.

The most interesting experiment is the "reverse distillation", where they take a 1.5B model that was improved by RL — a student that has already moved beyond its original base behavior — and try to distill it back using two teachers: the original pre-RL 1.5B model and a larger 7B model from the same family.

Both teachers pull the RL-improved student backward. The student loses its RL gains and regresses toward the older behavior.

This sounds surprising at first. But the explanation is simple: OPD does not know that the student's RL behavior is better unless the teacher's token probabilities support it. If the teacher still prefers the old reasoning pattern, OPD will train the student back toward that pattern.

So the RL gains disappear not because the teacher is "weak" in benchmark terms, but because the teacher is giving token-level supervision for a behavior the student has already moved past.

Benchmark gap does not tell you whether OPD will work. Token-level compatibility does.

2. Repetition becomes locally rewarding
Even if OPD starts well, it can still collapse.

The most striking failure mode is when training looks fine for a while, then within roughly 30 steps the model starts producing much longer outputs, stops terminating, repetition spikes, and accuracy collapses.

The mechanism is counterintuitive at first but makes sense once you see it.

In sampled-token OPD, the reward for a token is roughly the teacher's log-probability minus the student's log-probability on that token. So if the teacher gives a token much higher probability than the student does, that token receives a large positive signal.

Now imagine the student starts repeating itself. In practice this looks less like coherent sentences repeating and more like degenerate loops — something like "wait, wait, wait, wait, wait" filling the rest of the context.

This prefix is bad globally. But locally, it is very predictable.

A strong teacher is often very confident about predictable text. Once the loop has gone on for a while, the teacher can assign high probability to the next repeated token. The student may be less confident than the teacher. So the repeated token gets a large positive log-ratio.

That means OPD accidentally rewards continuing the repetition.

Before repetition starts, repeated tokens are rare, so they don't matter much. But once repetition appears, those tokens become frequent. And because they also receive large positive advantages, they start dominating the update. Luo et al. [2] measures repeated tokens getting 4 to 9 times larger advantage than normal tokens after collapse.

Then the loop reinforces itself:
more repetition → more predictable prefix → higher teacher confidence → larger positive signal on repeated tokens → even more repetition

This is different from the usual length-bias issue in RL. It's more specific — a broken prefix creates locally high-reward repeated tokens, and OPD faithfully amplifies them.

3. We often only look at one item on the menu
The clean objective would compare the teacher and student distributions over multiple possible next tokens. But many public OPD recipes — including the ones used industrially — use a cheaper version:

Let the student generate one token. Then ask: did the teacher assign this exact token higher or lower probability than the student? If teacher probability is higher, push the student toward it. If lower, push the student away.

That is the sampled-token log-ratio. It is cheap because you only score the token the student actually sampled. You do not need to compare the full vocabulary.

There is a real reason for this design choice. Full sequence-level reverse-KL is noisy for long generations because an early token update gets entangled with many future rewards. 

Token-level OPD avoids that by giving each token its own local feedback. That gives much better variance scaling with length [3] — worst-case variance grows as O(T²) for token-level instead of O(T⁴) for sequence-level. So for long reasoning traces, token-level feedback is attractive.

The problem is that "one sampled token" is a very noisy view of the teacher's actual next-token preference. At a given step, the teacher may have a whole cluster of reasonable next tokens. But sampled-token OPD only checks the one token the student happened to pick.

This creates three problems.

First, the student samples tokens from its own distribution, so on most positions the student's probability exceeds the teacher's and the log-ratio is negative. The reward is computed as teacher minus student, and the student is picking tokens where its own log-prob is near its highest — meaning the subtraction is almost always against the student's strongest values. Positive signal only shows up when the student happens to sample a token the teacher likes even more than the student does, which is the minority case.

Second, if the student drifts into weird prefixes, the teacher's local probabilities may no longer reflect global quality.

Third, tokenization and special-token differences can create fake disagreements. The student and teacher may represent the same text with different token boundaries, so a single-token comparison can look terrible even when the underlying string is fine.

The fix proposed in [3] is simple: don't guess the teacher's local preference from one sampled token. Instead, take the teacher's top-k next tokens, renormalize both teacher and student probabilities over that set, and compute reverse-KL there.

It's still cheap — you only need the top-k logits, not the whole vocabulary. But it changes the supervision from "did the teacher like this one sampled token?" to "among the teacher's plausible next tokens, does the student put probability mass in the same places?"

That is a much better local learning signal.

They also add top-p sampling during rollout, so the student is less likely to wander into extremely low-probability prefixes, and mask special tokens to avoid fake tokenization mismatches.

4. Even good token signals may not add up
This is the least developed of the four failure modes, and possibly the most important.

Li et al. [1] compares a successful OPD setup against a failing one and finds something strange. The failing teacher's per-token advantages are actually larger than the working teacher's, but the gradient norms are smaller. And the failing teacher's sequence-level reward can still distinguish correct from incorrect rollouts, comparable to the working case.

So the reward signal is globally informative. It just does not produce useful gradients.

Turns out what's going on is that OPD computes a learning signal at every token position in the rollout, and then sums them into one gradient update. 

Each position's contribution is a vector in parameter space pointing in some direction. So if the per-position vectors mostly point in the same direction, they add up to a big coherent push. But if they point in different directions, they partially cancel when summed, and the model barely moves even though each individual position had something to say.

The empirical fingerprint is consistent with the second case: large per-token advantages but small gradient norms after summing — individually strong signals that cancel out when combined. The successful teacher shows the opposite pattern: smaller per-token advantages, larger gradient norms after summing — weaker individual signals that reinforce each other when combined.

The paper that raises this leaves it as a hypothesis, but the empirical fingerprint — large per-token advantages, small gradient norms, informative sequence-level reward — is specific enough that it should be testable?

What this explains
A lot of practical OPD fixes start to look related.

SFT cold start helps because it moves the student closer to the teacher's reasoning style before OPD begins.

Teacher-aligned prompts help because they put the student in regions where the teacher gives more reliable feedback.

KL regularization helps because it prevents the student from drifting too quickly into weird generations.

Mixture distillation helps because it keeps some clean reference trajectories in training, so the rollout distribution does not become fully self-generated garbage.

Top-k matching helps because it stops pretending one sampled token is enough to represent the teacher's local preference.

These look like different tricks. But they are all trying to protect the same thing: the small set of plausible next tokens where teacher and student can actually communicate.

The ceiling, and the real open question
The more interesting part is long-horizon reasoning.

The deeper the student gets into its own generated solution, the more likely the prefix is something the teacher would not have written. And once the teacher is judging prefixes outside its own natural distribution, its token probabilities become less reliable.

One paper [1] shows this directly: teacher continuation advantage drops sharply as the student prefix gets longer, from +0.37 at 1K prefix to +0.02 at 16K.

That is a bad sign for long-CoT and agentic OPD, because those are exactly the settings where the student spends many steps inside its own partially-generated world. 

OPD works best when the teacher and student stay close enough that teacher probabilities remain meaningful. Long-horizon agentic training pushes in the opposite direction.

This is the open question I would most want to see investigated. The failure modes in sections 1-3 are diagnosable and have proposed fixes. Section 4 is a hypothesis about local gradient structure that should be testable. But the long-horizon ceiling is different — it is about whether OPD's core assumption (the teacher knows something useful about the student's next token) can hold at all when the student is operating many steps inside its own generated world.

My current takeaway
OPD isn't really a full-vocabulary distribution-matching problem. It's a fragile communication protocol between teacher and student through a tiny local menu of next-token choices. When that menu overlaps, stays clean, and produces gradients that add up, OPD works. When it doesn't, OPD quietly trains the student in the wrong direction.

References
[1] Li et al. Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe. https://arxiv.org/abs/2604.13016
[2] Luo et al. Demystifying OPD: Length Inflation and Stabilization Strategies for Large Language Models. https://arxiv.org/abs/2604.08527
[3] Fu et al. Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes. https://arxiv.org/abs/2603.25562

likes 461  views 64780  retweets 80  bookmarks 489