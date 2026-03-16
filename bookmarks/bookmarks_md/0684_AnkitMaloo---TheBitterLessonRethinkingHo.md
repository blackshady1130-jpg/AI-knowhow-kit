---
url: https://ankitmaloo.com/bitter-lesson/?continueFlag=fd03ade02739c874e3987c672e0314c5
title: "The Bitter Lesson: Rethinking How We Build AI Systems"
description: "The Race for AI Progress In 2019, Richard Sutton, wrote his groundbreaking essay titled ‘The Bitter Lesson’. Simply put, the essay concludes that systems which get better with higher compute beat the systems that do not. Or specifically in AI: raw computing power consistently wins over intricate human-designed solutions. I used to believe that clever orchestrations and sophisticated rules were the key to building better AI systems. That was a typical sofware dev mentality. You build a system, look for edgecases, cover them and you are good to go. Boy, was I wrong."
author: "Ankit Maloo"
published: "2025-03-20T00:00:00+00:00"
captured_at: "2026-03-08T12:55:26.935Z"
---

# The Bitter Lesson: Rethinking How We Build AI Systems

## The Race for AI Progress

In 2019, Richard Sutton, wrote his groundbreaking essay titled ‘[The Bitter Lesson](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf)’. Simply put, the essay concludes that systems which get better with higher compute beat the systems that do not. Or specifically in AI: raw computing power consistently wins over intricate human-designed solutions. I used to believe that clever orchestrations and sophisticated rules were the key to building better AI systems. That was a typical sofware dev mentality. You build a system, look for edgecases, cover them and you are good to go. Boy, was I wrong.

Think of it like training for a marathon. You could spend months perfecting your running form and buying the latest gear, but nothing beats putting in the miles. In AI, those miles are compute cycles.

## Nature’s Blueprint

Recently, I was tending to my small garden when it hit me - a perfect analogy for this principle. My plants don’t need detailed instructions to grow. Given the basics (water, sunlight, and nutrients), they figure out the rest on their own. This is exactly how effective AI systems work.

When we over-engineer AI solutions, we’re essentially trying to micromanage that plant, telling it exactly how to grow each leaf. Not only is this inefficient, but it often leads to brittle systems that can’t adapt to new situations.

## A Tale of Three Approaches

Today, one of the most common enterprise usecase for AI agents is customer support. Let me share a real-world scenario I encountered while building a customer service automation system:

1.  **The Rule-Based Approach**: Initially, everyone built an extensive decision tree with hundreds of rules to handle customer queries. It worked for common cases but broke down with slight variations. Maintenance became a nightmare.

2.  **The Limited-Compute Agent**: Next, with the dawn of ChatGPT, there were AI powered customer agents with modest computing resources. You could write prompts based on patterns you saw in historical data or SOP guidelines. Worked well on simple enough questions, but struggled with complex queries and needed constant human oversight.

    Many AI agents are here at this point. One path is to constrain it even further, branch out, bring in different frameworks and guardrails, so that the agent sticks to the goal. Inadventently, the compute is somehow fixed. Or you could try:

3.  **The Scale-Out Solution**: Then we tried something different - what if we threw more compute at it? Not just bigger GPUs, but fundamentally rethinking how we use AI. We had the agent generate multiple responses in parallel, run several reasoning paths simultaneously, and pick the best outcomes. Each customer interaction could spawn dozens of AI calls exploring different approaches. The system would generate multiple potential responses, evaluate them, and even simulate how the conversation might unfold. Sure, it was computationally expensive - but it worked surprisingly well. The system started handling edge cases we hadn’t even thought of, and more importantly, it discovered interaction patterns that emerged naturally from having the freedom to explore multiple paths.

which brings us to:

## The RL Revolution

In 2025, this pattern becomes even more evident with [Reinforcement Learning](https://ankitmaloo.com/RL) agents. While many companies are focused on building wrappers around generic models, essentially constraining the model to follow specific workflow paths, the real breakthrough would come from companies investing in post-training RL compute. These RL-enhanced models wouldn’t just follow predefined patterns; they are discovering entirely new ways to solve problems. Take OpenAI’s Deep Research or Claude’s computer-use capabilities - they demonstrate how investing in compute-heavy post-training processes yields better results than intricate orchestration layers. It’s not that the wrappers are wrong; they just know one way to solve the problem. RL agents, with their freedom to explore and massive compute resources, found better ways we hadn’t even considered.

The beauty of RL agents lies in how naturally they learn. Imagine teaching someone to ride a bike - you wouldn’t give them a 50-page manual on the physics of cycling. Instead, they try, fall, adjust, and eventually master it. RL agents work similarly but at massive scale. They attempt thousands of approaches to solve a problem, receiving feedback on what worked and what didn’t. Each success strengthens certain neural pathways, each failure helps avoid dead ends.

For instance, in customer service, an RL agent might discover that sometimes asking a clarifying question early in the conversation, even when seemingly obvious, leads to much better resolution rates. This isn’t something we would typically program into a wrapper, but the agent found this pattern through extensive trial and error. The key is having enough computational power to run these experiments and learn from them.

What makes this approach powerful is that the agent isn’t limited by our preconceptions. While wrapper solutions essentially codify our current best practices, RL agents can discover entirely new best practices. They might find that combining seemingly unrelated approaches works better than our logical, step-by-step solutions. This is the bitter lesson in action - given enough compute power, learning through exploration beats hand-crafted rules every time.

Indeed, you see this play out in –soon to be big– competition between Claude code and Cursor. Currently users say Cursor does not work well with Claude Sonnet 3.7, but it works flawlessly with Sonnet 3.5. On the other hand, people complain that Claude code (which uses Sonnet 3.7 under the hood) consumes a lot of tokens. However, it works amazingly well. Cursor, reportedly will launch as version with usage based pricing which will make more use of 3.7’s agentic behavior[1](https://ankitmaloo.com/bitter-lesson/?continueFlag=fd03ade02739c874e3987c672e0314c5#fn:1). We will see this in more domains, especially outside of code where the an agent could think of multiple approaches, while humans have codified a single workflow.

## What this means for AI Engineers

This insight fundamentally changes how we should approach AI system design:

1.  **Start Simple, Scale Big**: Begin with the simplest possible learning architecture that can capture the essence of your problem. Then scale it up with compute rather than adding complexity.

2.  **Design for Scale**: Build systems that can effectively utilize additional compute. This means:
    -   Parallelizable architectures
    -   Flexible learning frameworks that can grow with more data and compute
    -   Infrastructure that can handle distributed processing
3.  **Avoid Premature Optimization**: Don’t spend weeks optimizing algorithms before you’ve maxed out your compute potential. The returns from clever engineering often pale in comparison to simply adding more computational resources.

## The Real “So What”

The implications are profound and somewhat uncomfortable for us engineers:

1.  **Investment Strategy**: Organizations should invest more in computing infrastructure than in complex algorithmic development.

2.  **Competitive Advantage**: The winners in AI won’t be those with the cleverest algorithms, but those who can effectively harness the most compute power.

3.  **Career Focus**: As AI engineers, our value lies not in crafting perfect algorithms but in building systems that can effectively leverage massive computational resources. That is a fundamental shift in mental models of how to build software.

## Looking Forward

This lesson might seem to diminish the role of the AI engineer, but it actually elevates it. Our job is to:

-   Design systems that can effectively utilize increasing compute resources
-   Build robust learning environments that scale
-   Create architectures that can grow without requiring fundamental redesigns

The future belongs to those who can build systems that learn and adapt through computational force, not those who try to encode human knowledge into rigid rules.

Remember: In the race between clever engineering and raw compute, compute wins. Our role is to build the race track, not to design the runner’s every move.

1.  I mean the [source](https://x.com/ericzakariasson/status/1898753771754434761) is their Community Manager. So, not exactly reportedly. In this thread, they call it more sync vs more delegated work, but in reality, it is a fight between constraints and compute. This post pretty much admits it. At this point, they have already released a version where every Sonnet 3.7 Max call costs about $0.05. [↩](https://ankitmaloo.com/bitter-lesson/?continueFlag=fd03ade02739c874e3987c672e0314c5#fnref:1)