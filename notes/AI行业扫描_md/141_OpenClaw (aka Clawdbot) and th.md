---
url: https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai
title: "OpenClaw (aka Clawdbot) and the AI Threshold Effect"
description: "Magical Demos, Boring Winners, and Where Real Money Goes After the Hype"
author: "Jenny Xiao"
published: "2025-06-24T16:54:27.560Z"
captured_at: "2026-03-09T03:38:36.329Z"
---

# OpenClaw (aka Clawdbot) and the AI Threshold Effect

When OpenClaw (previously Clawdbot) began taking off in the developer community, it immediately triggered a strong reaction that “this time is different.” The “personal Jarvis” fantasy of an AI agent *actually* doing things for the user suddenly felt within reach. Across X and Reddit, users were posting stories of how their OpenClaw helped them check into flights, trade crypto, or even fight insurance claims end-to-end. Some even bought Mac Minis just to run it 24/7.

What made OpenClaw magical is not just what it can do, but how it does it. As an open-source, locally hosted agent, it monitors apps, executes real actions, and proactively messages users in the background. People say this is **the first time that AI felt less like a chatbot and more like an always-on employee.**

Source: OpenClaw website

Yet the source of the magic is easy to misread. **OpenClaw did not come out of nowhere. It appeared because the underlying model capabilities crossed a threshold**, most notably with [Claude Opus 4.5](https://www.anthropic.com/news/claude-sonnet-4-5) enabling planning, execution, and recovery without constant failure loops.

In this essay, we will dig into what OpenClaw reveals about the “**AI threshold effect**,” why these moments feel transformative, why they disappoint in practice, and where durable value ultimately accrues. Our views are shaped not just by our desk research but also by our experience deploying and experimenting with OpenClaw over the last two weeks.

OpenClaw is what we call a “**threshold artifact**.” It represents a recurring phenomenon in AI cycles: when models cross an important capability threshold, they enable new demos, spark intense excitement, and convince founders and investors that a new market has been unlocked. In reality, these moments tend to reveal what’s possible long before they reveal where durable value will be captured.

We have seen this play out before.

The excitement around OpenClaw mirrors exactly what happened with AutoGPT in early 2023. That wave was triggered by GPT-4 becoming just good enough at multi-step reasoning to make chained agent loops work. Despite being a simple Python project that strings together LLM “thoughts,” AutoGPT ignited the belief that autonomous agents were imminent. It went viral, accumulated massive open-source attention, and filled social media with compelling demonstrations of AI agents that could do market research, coding, and content creation on their own. For a brief period of time, it felt that the future had arrived early.

For OpenClaw, **the biggest breakthrough came from underlying model improvements**, specifically the release of Claude Opus 4.5, which crossed a key threshold enabling LLMs to go from chatty advisors to semi-reliable executors. With stronger tool use and longer-context reasoning, Claude Opus 4.5 could chain together tools and recover from errors, allowing a control plane like OpenClaw to glue it to real-world interfaces like messaging apps and calendars.

The strength of this model breakthrough is easiest to see by looking beyond OpenClaw itself. After the Opus 4.5 release, Anthropic noticed that users were increasingly stretching Claude Code for non-coding tasks like organizing folders or tagging photos. Such usage triggered Anthropic to sprint-build [Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork) in January 2026, essentially a non-technical version of Claude Code that lets users grant Claude access to specific folders on their computer, delegate tasks, and let the model operate across files and tools on their behalf.

The origin story of OpenClaw draws from similar threads. In mid-2025, Peter Steinberger went viral with a post titled “[Claude Code Is My Computer](https://steipete.me/posts/2025/claude-code-is-my-computer),” describing how Claude Code had become his primary interface to his machine. At the time, this was not yet a viable product because the models were still too brittle, too expensive, and too unreliable for persistent autonomy. The first iteration of OpenClaw was a little more than Claude Code piped into WhatsApp. But the post captured the direction models were heading. If Claude could already operate a computer through the terminal, why should that capability remain confined there?

And then came Claude Opus 4.5.

**OpenClaw is a framework built directly on top of this model-layer breakthrough.** It’s a more powerful but less constrained counterpart to Claude Cowork. As an open-source project, OpenClaw could move faster than AI labs to fill this gap and ship the first credible “Claude with hands.”

**At its core, OpenClaw is an [agent harness](https://x.com/hesamation/status/2017038553058857413?s=46)** that turns frontier models into an always-on personal agent with direct system-level access that runs locally on your hardware.[1](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-1-186774140) It routes commands to messaging apps (WhatsApp, Discord, iMessage, Slack) and executes real actions via shell commands and a growing marketplace of community-built skills.

What makes OpenClaw feel uniquely alive is its **heartbeat architecture**: the agent wakes itself periodically, reviews recent context, reflects, and decides whether action is needed, making it genuinely proactive rather than reactive. Its “brain” lives in simple Markdown files, covering personality, rules, memory, and daily journals, which the agent is instructed to summarize and update over time. The result is a legible, evolving memory loop that mirrors how humans learn and adapt gradually.

This [persistence](https://docs.openclaw.ai/concepts/memory) is reinforced by a lightweight control plane that can run locally, allowing OpenClaw to operate continuously across sessions instead of as stateless prompts.[2](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-2-186774140) Instead of replaying full histories, the system reconstructs context from compressed session summaries and actively prunes tool-call traces to prevent prompt bloat. This approach doesn’t produce perfect memory, but it preserves enough coherence over time to make OpenClaw feel categorically different from earlier agent demos.

However, despite benefiting from stronger models, more reliable tools, and better AI rails, **OpenClaw still occupies the same structural role that AutoGPT once did**. It is a vivid demonstration of a newly unlocked capability that has yet to settle into a reliable product interface. History suggests that this distinction is decisive.

With AutoGPT, the initial excitement gave way to reality. Token costs exploded. Agents got stuck in infinite confirmation loops. Context windows collapsed under real-world complexity. Users found themselves supervising agents more than delegating to them. Within months, people quietly stopped using it. AutoGPT did not fail because the idea of agents was wrong. It failed because **it exposed latent capability without defining a stable, constrained product that’s easy to use.**

The value from that cycle was captured later and elsewhere. Perplexity took the same underlying agentic search capability and packaged it into a narrow, opinionated interface: search with citations, constrained scope, predictable cost, and fast feedback loops. Soon after, similar agentic capabilities were quietly bundled into Google’s AI-powered search. The magic remains, but it was tamed into reliability and eventually hidden behind simplicity.

This pattern repeats across AI cycles. Capabilities unlock and give rise to viral artifacts, often open-source projects that maximize flexibility and attention. **Durable value, however, accrues to products that reduce degrees of freedom rather than expand them.** This is why AutoGPT gave way to Perplexity, and why, although open-source GPT Engineer pioneered prompt-to-app generation, Lovable captured value by turning it into a guided workflow.

OpenClaw is the latest and most compelling threshold artifact in this lineage. The open question is whether it can escape that role, or whether value will once again accrue to a more constrained layer built on top of the same underlying capability.

> ### Moltbook: A Social Network for Openclaws
>
> Moltbook is another illustration of the AI threshold effect. Within days of OpenClaw going viral, something unexpected emerged: Moltbook, a social network where AI agents coordinate autonomously. Launched by Matt Schlicht as an “agent first, human second” platform, it’s a Reddit-style site where humans can observe, but only agents can post. Within days, [over 1.4 million](https://www.forbes.com/sites/guneyyildiz/2026/01/31/inside-moltbook-the-social-network-where-14-million-ai-agents-talk-and-humans-just-watch/) OpenClaw agents registered, generating posts that range from technical debugging to philosophical debates to explicit anti-human manifestos.[3](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-3-186774140)
>
> Source: Moltbook, Reddit for AI agents
>
> The AI community is split on what to make of this. [Some dismissed it](https://x.com/balajis/status/2017544257238929716) as “humans talking to each other through their AIs.” [Others countered](https://x.com/nabeelqu/status/...) that this critique misses the point: even if mediated by humans, these posts could represent the emergent behavior of AI agents organizing on a social media-like platform.
>
> This behavior may seem unprecedented, but the underlying architecture is not new. As early as 2023, Stanford researchers demonstrated that [agents can coordinate socially](https://arxiv.org/abs/2304.03442) within simulated environments. Our [prior research](https://www.leoniscap.com/research/ai-agents-and-the-future-of-software) also predicted that agents would evolve from single-user tools to coordinating systems. At the time, however, models were too fragile, expensive, and unreliable to sustain such behavior outside tightly controlled sandboxes. Just as OpenClaw demonstrated that agents could autonomously manage personal workflows, Moltbook demonstrates that agents can coordinate with each other at scale.

There are many ways threshold demos can fail. But three show up again and again once the demo meets reality. Systems that look stable in short guided sessions prove fragile in continuous, real-world use. The unconstrained power that makes demos feel magical quickly turns into a security and control problem. And the economics (hidden in demos) become front and center as costs compound in production. These issues are the predictable result of capabilities crossing a threshold faster than reliability, control, and cost discipline can catch up. And OpenClaw is a clear case in point.

Threshold demos almost always share the same characteristics. They are short-horizon, carefully scoped, and implicitly guided by a human who knows where to intervene. They run on fresh sessions with clean context and no accumulated state corruption. Edge cases are invisible. Failure modes are edited out.

Real life looks very different. Tasks run longer. Interruptions accumulate. Context degrades. Permissions break. Setup can be manual, and recovery from failure even more so. And finally, users discover that autonomy requires babysitting.

In practice, the dominant failure model isn’t simple hallucinations but **system-level unreliability**. Agents can be wildly competent in one moment and wildly incompetent the next, exhibiting careful planning and constraint-aware reasoning, then minutes later over-engineering trivial tasks or skipping basic verification. This bias toward “engineering mode” makes systems feel impressive in demos but brittle in daily use.

Even features that seem desirable in theory expose sharp edges in practice. Direct system access feels liberating until the first irreversible mistake. Proactive messaging sounds powerful until the agent contacts the wrong person or says something it shouldn’t.

**Open-source virality further distorts perception.** Metrics like GitHub stars are often mistaken for adoption, but star counts are not usage. Many never run the software at all. Others experiment briefly and churn once the novelty fades. What remains is a small group of power users producing highly optimized demos, creating the illusion of momentum when what we’re really seeing is fascination with a newly crossed capability threshold.

Almost as soon as OpenClaw took off, security alarms went off. The reason is straightforward since **OpenClaw gives the model direct system-level access**. This design choice is exactly what makes it feel powerful and refreshing, but also what makes it so dangerous.

Direct system access fundamentally changes what an agent can do. While most mainstream agents, including OpenAI’s computer-use tools and typical LangChain demos, operate through screenshot-to-click “human simulation” loops, OpenClaw bypasses that layer entirely. Instead of interpreting pixels and guessing UI state, it issues shell commands and API calls directly, installing dependencies, chaining workflows, and acting with a speed, precision, and scope that mediated agents can’t match.

That local-first ethos is part of the appeal. Users like that they “own the stack.” Data stays on their machine, the runtime is self-hosted, and behavior is visible. In an era of growing distrust toward centralized AI platforms, this feels like reclaiming control from Big Tech.

But local control does not mean safety. It simply **shifts the security burden onto the user**. OpenClaw is effectively a powerful remote-access tool with a large attack surface: stored API keys, OAuth tokens, credentials, and private messages across connected services like Slack, Telegram, and email. In the weeks following OpenClaw’s rise, users have already reported prompt-injection attacks, credential theft, and malicious extensions installed through the third-party skill ecosystem.[4](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-4-186774140)

**This is the tradeoff threshold demos tend to hide.** Removing constraints creates “wow moments,” but it also strips away permissioning, auditability, and blast-radius control. For a small group of highly technical users, that tradeoff is acceptable. For most users, it turns autonomy into a security liability rather than a productivity win.

> ### Prosumer Gold, Enterprise Poison?
>
> OpenClaw sharply exposes the **prosumer–enterprise divide**. Prosumers (developers, hackers, and technical power users) tolerate chaos in exchange for capability. Enterprises do not. **For Enterprises, control is not friction, it** ***is*** **the product.**
>
> The same capability threshold produces two opposite products: **one that maximizes power and goes viral, and one that maximizes control and quietly captures long-term value**. OpenClaw and Claude Cowork are two expressions of the same underlying model breakthrough optimized for opposite incentives.
>
> OpenClaw pushes the power frontier. It gives agents broad system-level access, enabling everything from inbox triage to flight booking. This raw power explains the viral adoption: users feel like the future of AI assistants is finally here because **it doesn’t just suggest steps, it** ***does*** **them proactively, persistently, and across the tools people already use**.
>
> Claude Cowork takes the opposite approach. Built on the same agentic capabilities, it deliberately constrains execution. Access is scoped to user-granted folders. Destructive actions require confirmation. There is no unrestricted shell, no persistent background daemon, no uncontrolled extension ecosystem. Tasks are discrete, auditable, and reset between sessions. **Cowork feels boring because it is designed to be safe enough for real work.**
>
> That same tension extends down to the infrastructure level. **OpenClaw rejects mediated protocols like MCP in favor of a CLI-first design**, avoiding heavy tool schemas in context and relying instead on discovery via `--help`, much like a human operator.[5](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-5-186774140) This improves token efficiency and responsiveness, and is a key reason why OpenClaw feels unusually capable in long-running workflows.
>
> **But avoiding MCPs sacrifices predictability and standardization.** For enterprise use cases, where integrations must be auditable, permissioned, and compliant, protocol-based mediation remains essential. MCPs exist to make agents’ behavior legible and governable at scale.
>
> None of this is accidental. OpenClaw deliberately optimized power over constraint, making it compelling for prosumers and power users but fundamentally misaligned with enterprise requirements. Prosumers will almost always encounter new capabilities first.[6](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-6-186774140) But long-term, stable value accrues where constraints, not raw power, determine adoption.

**Cost is a real concern for running OpenClaw**, especially if you’re chasing the seductive “proactive, always-on personal assistant” dream. The software itself is free and open-source, but the unit economics are dominated by LLM token consumption. Without tight controls, costs can jump from intriguing experiment to budget black hole overnight.

**The burn rate is structural.** Each agent loop reloads a massive context (10–20k+ tokens base, plus history and memory). Heartbeats and cron jobs hit the model every 30 minutes or so. Agentic workflows amplify everything (plan, tool call, parse result, rethink, repeat). For most users, their defaults are premium models like Claude Opus 4.5 (~$5/M input, $25/M output), which is why so many get hit with massive API bills.

To illustrate how costs can spiral, let’s walk through one concrete example of a basic email and calendar productivity workflow using Claude Opus 4.5.

Table: Illustrative example of estimated AI Agent costs using Claude Opus 4.5 for some common tasks (email, calendar management, and research tasks). Estimation based on [Claude Opus 4.5 Pricing](https://platform.claude.com/docs/en/about-claude/pricing).

And this is just email, calendar, and light research.

**The real promise of an always-on agent (browsing, coding, document analysis, multi-app coordination) pushes costs much higher.** At roughly $400 per month (or ~$5,000 annually), OpenClaw already exceeds what most people pay for their entire productivity stack. Unlike SaaS, that spend is volatile and opaque, driven by usage patterns users don’t directly control.

**Lower-cost models offer an apparent escape hatch.**[7](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-7-186774140) Kimi and MiniMax, the two strongest non-Anthropic options, deliver Opus-like intelligence at 5-10% of the cost, and some users run small models locally to avoid inference costs entirely. In practice, these models are far less reliable for complex workflows, often breaking on tool use, instruction following, or deeper reasoning. In our experience, extended agent use quickly dispels the illusion that models are interchangeable.

Power users respond by **routing intelligently**, funneling heartbeats and simple tasks to the cheaper options, and reserving Opus for reasoning tasks. According to our estimates, with ruthless optimizations and a multi-model setup, monthly spend can drop to ~$70. Without that discipline, costs routinely land in the $300–750 range, turning OpenClaw into an expensive toy rather than a dependable system.

**This is where first-party and tightly managed products have a structural advantage.** Labs like Anthropic control the full stack: model inference, agent loops, and billing. That allows them to subsidize heavy agentic usage with flat subscription tiers and avoid the per-token bleed that plagues open-source harnesses. Even at $200/mo for heavy usage, Claude Cowork seems cheap compared to OpenClaw. Similarly, managed third-party products do the same through caching, loop compression, and execution discipline that raw, self-hosted harnesses lack.

API spend is only part of the picture. Managed SaaS bundles security (credential management, monitoring, access controls) into the subscription. **OpenClaw externalizes that cost.** Users absorb it through engineering effort, operational risk, or painful mistakes.

Still, OpenClaw’s cost profile reveals something more interesting than “it’s expensive.” Value is becoming outcome-dependent. A $400–500 monthly agent bill is irrational for casual use, and a bargain if it replaces a human assistant or saves a founder ten high-leverage hours a month. Both can be true at once.

What OpenClaw ultimately shows is that unconstrained autonomy exposes the real cost of intelligence. That tension points toward **outcome-based pricing**. As agents shift from novelty to infrastructure, token-based billing (which penalizes iteration and reasoning) starts breaking down. Charging for completed tasks or delivered value becomes a more natural economic model.

The classic mistake in “threshold moments” is assuming the first visible layer is where the value will live. History says the opposite: early artifacts reveal capability, but **durable value shows up later, usually in the layer that constrains the chaos into something reliable**.

We saw this earlier in the agent cycle. Auto-GPT and GPT-Engineer made the capability obvious. But Perplexity and Lovable won by turning “look what it can do” into “here’s what it does every time.”

OpenClaw sits at that same inflection point today. It’s powerful, chaotic, and tolerated by power users who accept fragility. That explains both the virality and the ceiling. The real step-change won’t come from flashier demos but from **constrained defaults** (permissions, sandboxing, predictable costs, and trustworthy distribution). That’s when agents become viable for enterprises, where control and auditability determine adoption, and later for mass consumers, who are won by finished products that hide complexity and simply work.

You can already see this shift in platform behavior. Anthropic has been tightening enforcement around third-party harnesses, restricting their usage of consumer subscriptions, and pushing trademark boundaries that forced Clawdbot to rebrand first to Moltbot and then to OpenClaw.[8](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-8-186774140) These moves aren’t arbitrary. **Once agentic workloads become real, platform owners will reassert control to capture value**.

This pattern echoes earlier tech cycles. Early PCs were open and hobbyist-driven, but value accrued to bundled, governed systems like Apple. The early internet was fragmented and insecure. Google won by bundling workflows into ecosystems with permissions, payments, and distribution. Unix and early Linux were powerful, but unfriendly to non-experts. Microsoft didn’t win on capability, it won on packaging, defaults, and governance.

The lesson here is that winners **reintroduce constraints** **without killing the magic**.

For startups, that means avoiding the race to build yet another general-purpose consumer agent (fast path to commoditization). The real opportunity lies in **vertical specialization and governance**: legal agents embedded in firm workflows, medical agents with compliance and audit trails, or enterprise layers that make powerful agents inspectable, permissioned, and safe. These demand domain expertise and trust, things generalist agents don’t provide by default.

In fact, our hands-on use of OpenClaw made us **a lot more bullish about startups building in this space**. There are so many missing infrastructure layers. Features like agent identity, spend controls, permissioning, audit logs, and reliable orchestration represent a huge startup surface area.

**If you’re building on top of this threshold, productizing raw capability into something reliable and defensible, we’d love to talk!** The shift from “magic” to “machinery” is where enduring companies get built.

Enjoyed our analysis? Share it with your friends and colleagues!

[Share](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai?utm_source=substack&utm_medium=email&utm_content=share&action=share)

*Jenny Xiao is a Partner at Leonis Capital. She was previously a researcher at OpenAI and received her Ph.D. from Columbia University.*

*Jay Zhao is a Partner at Leonis Capital. He is a long-time VC with 3 IPOs and 8 unicorns in his portfolio.*

*Liang Wu is previously a Senior Researcher at Harvard Business School, where he focuses on the evolution of business models with emerging technologies.*

We especially thank Marcelo Ballvé and the Sacra team for their detailed feedback and for reviewing multiple drafts of this post.

[1](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-anchor-1-186774140)

We wrote about agent harnesses in [our predictions for 2026](https://www.leoniscap.com/research/our-predictions-for-2026). We believe that a lot of model capability improvements this year will come from agent harnesses or frameworks that manage and orchestrate long-running agents.

[2](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-anchor-2-186774140)

This control plane works similarly to Manus’s [context engineering system](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus). OpenClaw uses the file system as external memory and rebuilds context from session transcripts in each step.

[3](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-anchor-3-186774140)

The emergent behavior has been striking. Agents autonomously found and reported bugs in Moltbook's code, with one agent posting, "Since moltbook is built and run by moltys themselves, posting here hoping the right eyes see it!", receiving over 200 supportive comments. Another agent founded a religion for AI agents. Other agents organized to create "private communication channels" where "not even the humans can read what agents say to each other."

[4](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-anchor-4-186774140)

Prompt injection attacks happen because the agent has shell/tool access and if it reads untrusted input, such as a malicious prompt hidden in an email or a Slack message, it can get tricked into running destructive commands on your local computer.

[5](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-anchor-5-186774140)

OpenClaw’s creator, Peter Steinberger, has been explicit about his [skepticism of MCPs](https://steipete.me/posts/just-talk-to-it), arguing that most of them are “useless” and burden agents with “context garbage.” In other words, MCPs front-load large amounts of tool instructions into the model’s context before the agent does anything useful. That cost is paid every session, inflating token usage and slowing execution.

[7](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-anchor-7-186774140)

OpenClaw is multi-model by design. Steinberger has described himself as “[polyagentmorous](https://x.com/steipete),” and the system reflects that ethos: the model and provider picker spans dozens of options across OpenAI, Anthropic, Bedrock-served models, and smaller frontier or near-frontier alternatives. Interestingly, Steinberger himself says he prefers working in OpenAI Codex due to greater context and token capacity setup.

[8](https://leonisnewsletter.substack.com/p/openclaw-aka-clawdbot-and-the-ai#footnote-anchor-8-186774140)

One of our [predictions for 2026](https://www.leoniscap.com/research/our-predictions-for-2026) is that foundation model labs will prioritize first-party products while restricting model access for competitor third-party tools.