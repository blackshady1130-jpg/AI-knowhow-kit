---
url: https://www.jasonwei.net/blog/asymmetry-of-verification-and-verifiers-law
title: "Asymmetry of verification and verifier’s rule — Jason Wei"
description: "Asymmetry of verification is the idea that some tasks are much easier to verify than to solve. With reinforcement learning (RL) that finally works in a general sense, asymmetry of verification is becoming one of the most important ideas in AI.&nbsp;     Understanding asymmetry of verification th"
author: "Jason Wei"
published: "Jul 15"
captured_at: "2026-03-09T03:13:37.603Z"
---

# Asymmetry of verification and verifier’s rule — Jason Wei

Asymmetry of verification is the idea that some tasks are much easier to verify than to solve. With reinforcement learning (RL) that finally works in a general sense, asymmetry of verification is becoming one of the most important ideas in AI. 

**Understanding asymmetry of verification through examples**

Asymmetry of verification is everywhere, if you look for it. Some prime examples:

-   Sudoku and crossword puzzles take a lot of time to solve because you have to try many candidates against various constraints, but it is trivial to check if any given solution is correct.

-   Writing the code to operate a website like instagram takes a team of engineers many years, but verifying whether the website is working properly can be done quickly by any layperson.

-   Solving [BrowseComp](https://openai.com/index/browsecomp/) problems often requires browsing hundreds of websites, but verifying any given answer can often be done much more quickly because you can directly search if the answer meets the constraints.

Some tasks have near-symmetry of verification: they take a similar amount of time to verify as to write a solution. For example, verifying the answer to some math problems (e.g., adding two 900-digit numbers) often takes the same amount of work as solving the problem yourself. Another example is some data processing programs; following someone else’s code and verifying that it works takes just as long as writing the solution yourself.

Interestingly, there are also some tasks that can take way longer to verify than to propose a solution. For example, it might take longer to fact-check all the statements in an essay than to write that essay (cue Brandolini's law: “The amount of energy needed to refute bullshit is an order of magnitude bigger than that needed to produce it.”). Many scientific hypotheses are also harder to verify than to come up with. For example, it is easy to state a novel diet (“Eat only bison and broccoli”) but it would take years to verify whether the diet is beneficial for a general population.

**Improving asymmetry of verification**

One of the most important realizations about asymmetry of verification is that it is possible to actually improve the asymmetry by front-loading some research about the task. For example, for a competition math problem, it is trivial to check any proposed final answer if you have the answer key at hand. Another great example is some coding problems: while it’s tedious to read code and check its correctness, if you have test cases with ample coverage, you can quickly check any given solution; indeed, this is what Leetcode does. In some tasks, it is possible to improve verification but not enough to make it trivial. As an example, for a problem like “Name a Dutch soccer player”, it would help to have a list of the famous Dutch soccer players but verification would still require work in many cases.

Why is verifiability so important? In my view, the most basic reason is that the amount of learning that occurs in neural networks is maximized when the above criteria are satisfied; you can take a lot of gradient steps where each step has a lot of signal. Speed of iteration is critical—it’s the reason that progress in the digital world has been so much faster than progress in the physical world.

**AlphaEvolve**

Perhaps the greatest public example of leveraging asymmetry of verification in the past few years is [AlphaEvolve](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/), developed by Google. In short, AlphaEvolve can be seen as a very clever instantiation of guess-and-check that allows for ruthless optimization of an objective, which has resulted in several mathematical and operational innovations.

A simple example of a problem optimized by AlphaEvolve is something like “Find the smallest outer hexagon that fits 11 unit hexagons.” Notice that this problem fits all five desirable properties of verifier’s rule. Indeed, my belief is that any solvable problem that fits those five properties will be solved in the next few years.

One thing about the types of problems solved by AlphaEvolve is that it can be seen as “overfitting” to a single problem. In traditional machine learning, we already know the labels in the training set and the significant test was to measure generalization to unseen problems. However, in scientific innovation, we are in a totally different realm where we only care about solving a single problem (train=test!) because it’s an unsolved problem and potentially extremely valuable.

**Relation to P = NP**

One related but different concept is the open question in computer science of whether P = NP. While both P = NP and verifier’s rule discuss asymmetry of verification, verifier’s rule does not make any claims about the time it would take for AI to solve the problem. In fact, in many of the above cases, such competition math problems, it takes far more computation to solve the problem than to verify a solution given that we already have the answer key.

Moreover, verifier’s rule is even broader in scope than P = NP because verifier’s rule also applies to non-computational tasks. For example, verifier’s rule would claim that AI would eventually be able to optimize non-computational endeavors like finding the best catalyst to speed up a chemical reaction, or the best aerodynamic car design for the fastest quarter-mile time, provided that we design the systems to measure those endeavors quickly and at scale.

**Implications**

Once you’ve learned about it, you’ll notice that asymmetry of verification is everywhere. It’s exciting to consider a world where anything we can measure will be solved. We will likely have a jagged edge of intelligence, where AI is much smarter at verifiable tasks because it’s so much easier to solve verifiable tasks. What an exciting future to consider.

For more related reading, I liked [\[this blog post\]](https://alperenkeles.com/posts/verifiability-is-the-limit/) by Alperen Keles.