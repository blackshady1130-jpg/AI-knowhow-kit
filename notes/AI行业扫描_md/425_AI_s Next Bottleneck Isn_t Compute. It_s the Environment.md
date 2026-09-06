# AI’s Next Bottleneck Isn’t Compute. It’s the Environment.

> 作者：Tensor
> 来源：Medium
> 阅读时长：8 min read

_Why progress in robotics, medicine, materials, and science depends on building worlds where AI can act, observe, and learn_

---

AI has already reached — and in some cases surpassed — human performance in domains where the environment is well defined. Chess, Go, coding, cybersecurity, data analysis, and parts of mathematics all share a crucial property: an AI system can take an action, observe what happens next, and receive a relatively clear signal about whether it succeeded.

The next frontier is different. Mechanical and electrical design, embodied intelligence, materials science, and medicine are grounded in the physical, chemical, and biological world. AI can already help by synthesizing existing knowledge and operating existing tools. But to transform these fields, better models and more compute may not be enough.

My argument is simple: in many important domains, AI progress will increasingly be bounded by the environment — not by the learning algorithm or the amount of compute available.

## Intelligence ≈ compute + environment

## A useful definition of intelligence

For this discussion, define intelligence as learning from interactions with an environment. In the narrower context of large language models, that definition has three parts.

## 1. Learning

Learning can happen through weight updates during training or through in-context learning at inference time. In both cases, learning consumes computation. Compute is the effort the system spends adapting what it knows to the problem in front of it.

## 2. Interaction

An intelligent system does more than produce a single answer. It thinks, plans, calls tools, takes actions, and observes consequences. Those tools may be digital — search, code execution, simulators, databases — or physical — microscopes, vehicles, robots, and laboratory equipment.

## 3. Environment

An environment must provide at least two things:

State transition. What changes after each action? If a robot applies force, how does the object move? If a model changes a circuit, how do performance and failure modes change?

Reward or verification. How good was the result relative to the intended goal? Did the code work cleanly? Did the car drive safely? Did the treatment improve the patient’s condition without unacceptable side effects?

Without reliable transitions and evaluation, the system cannot accumulate high-quality experience. It may generate plausible ideas, but it cannot consistently learn which ideas survive contact with reality.

## Why the environment was easy to overlook

The modern LLM pipeline is often summarized as pre-training or mid-training, followed by supervised fine-tuning and reinforcement learning. The environment is obviously central to reinforcement learning, but historically it seemed less necessary for supervised learning. The internet had already stored an enormous amount of interaction data: human explanations, arguments, experiments, software, failures, corrections, and discoveries.

In effect, pre-training inherited the residue of environments that humans had already explored.

That shortcut becomes weaker in domains without vast, high-quality records of prior interaction. A capable medical model cannot learn everything it needs from papers if the critical evidence has never been measured. A robot cannot master every household task from videos if those videos omit force, friction, failure, and recovery. In these settings, we need environments not only for reinforcement learning, but also to generate the data that future supervised learning will consume.

## Intelligence is relative to its environment

Human knowledge emerged from generations of thought plus repeated interaction with society, Earth, and the universe. What we call intelligence is partly an adaptation to the environments we inhabit. In a radically different world, the concepts worth learning — and perhaps even the practical physics — would look different.

Compute helps a learner adapt. The environment determines what can be learned, tested, and verified.

This leads to a stronger claim: we already have, or may soon have, superhuman systems in domains with near-perfect digital environments. Coding, cybersecurity, structured data analysis, and parts of AI research are unusually favorable because actions are cheap, feedback can be fast, and outcomes can often be checked automatically. In the near to medium term, progress beyond those domains may depend less on scaling the learner and more on improving the world around the learner.

## How “general” is general intelligence?

The word general in artificial general intelligence is loosely defined. Much of the flexibility we observe in current LLMs may be interpolation across the extraordinary breadth of internet data rather than pure extrapolation beyond it.

Reinforcement learning offers a path toward discovery through exploration, but exploration is only useful when it is efficient. With unlimited compute and a perfect verifier, random search would eventually find extraordinary answers. That thought experiment is irrelevant in practice because compute is always finite. The real problem is finding valuable regions of a huge search space quickly.

AlphaGo’s famous Move 37 illustrates how search can produce something that looks genuinely novel. But methods that work in a bounded game do not transfer cleanly to domains with vastly larger, noisier, or poorly specified spaces. Mathematics, scientific discovery, robotics, and medicine do not give us the same crisp board, legal moves, and final score.

Human intelligence is not perfectly general either. A highly trained mathematician is not automatically a good lawyer. What feels general is the person’s ability to enter a new environment, gather feedback, and train into a new capability.

## No training data + no usable environment = no usable capability

## The “no train, no gain” lemma

A capability needs a path into the system. That path may come from pre-training, mid-training, supervised fine-tuning, reinforcement learning, or some combination. But if a capability has no meaningful representation in supervised data and no environment in which it can be practiced and evaluated, we should expect little usable performance.

This does not mean reinforcement learning helps only the capabilities it directly trains. If a capability appears somewhere in pre-training, reinforcement learning on related tasks may still improve it indirectly. Better reasoning patterns, longer chains of thought, tool-use habits, or error-correction strategies can transfer. The important boundary case is when both the prior data and the interactive environment are missing.

## A simple experiment

Let D₁ be interaction data generated by environment E₁, and D₂ be interaction data generated by environment E₂. To test how supervised data and reinforcement-learning environments contribute to capability 1, compare four training setups:

**Experiment A:** Pre-train on D₁ + D₂; reinforce in E₁ + E₂.

**Experiment B:** Pre-train on D₁ + D₂; reinforce only in E₂.

**Experiment C:** Pre-train only on D₂; reinforce in E₁ + E₂.

**Experiment D:** Pre-train only on D₂; reinforce only in E₂.

The expected ordering for gains in capability 1 is A first, followed by B and C, with D producing little or no improvement — even when capabilities 1 and 2 are closely related. The exact ranking of B and C is an empirical question. The key prediction is that removing both D₁ and E₁ eliminates the system’s practical route to capability 1.

## A spectrum of environments

Different domains sit at very different points on the environment-quality spectrum.

## Go

The environment can be implemented entirely in software. The state transition is exact, the legal action space is known, and the final outcome is an unambiguous win or loss. This is close to an ideal learning environment.

## Mathematics

Formal systems can provide strong verification for some problems, and models or symbolic tools can help critique intermediate work. But open-ended mathematical research has a much larger search space and often lacks cheap, definitive graders for genuinely new results.

## Trading

The apparent environment is digital, but the true state includes markets, institutions, private information, human behavior, and changing regimes. Rewards are noisy and delayed. A strategy with a small edge can look good or bad for a long time because of randomness, making long-horizon credit assignment unusually difficult.

## Recursive self-improvement

For AI systems improving AI systems, much of the workflow is measurable: edit an architecture or training recipe, run an experiment, and compare results. The challenge is the cost of trustworthy grading. Verifying an idea at full scale may require enormous compute, so practical progress depends on cheaper proxies that correlate with scaled outcomes.

## Embodied intelligence

Robotics requires physics-rich environments. Narrow deployments may be simulated reasonably well, but general-purpose embodiment demands accurate models of contact, force, materials, perception, uncertainty, other agents, and the long tail of real-world situations.

## Medicine

The relevant environment is the human body. That environment is only partially observable, highly variable, and slow to interrogate. Outcomes can take months or years, causal effects are difficult to isolate, and experimentation is ethically constrained. These are not merely model problems; they are environment problems.

## The hardest environments are the ones that matter most

Many world models still struggle with robust physical reasoning outside narrow distributions. The challenge becomes even greater for biology. We are far from a complete, operational simulation of a human body — and even reliable models of cells, tissues, organs, the immune system, or the brain remain incomplete.

Real-world experimentation cannot simply be accelerated without limits. Clinical trials are slow for good reasons, and weak models of side effects or patient heterogeneity can waste scarce experimental opportunities. Faster progress in medicine therefore depends on better biological measurement, stronger causal models, more faithful simulators, improved experimental design, and safer automated laboratories.

The same logic applies to general-purpose humanoid robots. A demonstration can look impressive while still covering only a narrow slice of the physical world. Building a system that works reliably across homes, workplaces, people, objects, and rare failures requires an environment that can generate and verify far more experience than today’s systems can access.

## What this changes

I remain extremely bullish on AI’s positive impact over the medium and long term. But some timelines — such as general-purpose physical intelligence or solving every major disease within a decade — may underestimate the work required to build high-quality environments.

The implication for researchers and builders is practical. If you want an LLM or agent to excel at a capability that is not already richly represented on the internet, start by building the environment. Define the state. Make actions possible. Capture transitions. Create reliable graders. Shorten the feedback loop. Then scale the learning system against that foundation.

The next great AI companies may not be distinguished only by better models. They may own the laboratories, simulators, robotic fleets, data engines, evaluation systems, and feedback loops that allow models to learn what the internet never recorded.

## Build the environment first: the state transition, the tools, and the grader.

## The takeaway

Compute determines how much learning a system can attempt. Algorithms determine how efficiently it learns. But the environment determines which truths are available to discover — and whether the system can tell when it has found them.

For the next phase of AI, that may be the binding constraint.

---

## 原文链接

https://medium.com/@shuchaobi/ais-next-bottleneck-isn-t-compute-it-s-the-environment-0eaec31888f5
