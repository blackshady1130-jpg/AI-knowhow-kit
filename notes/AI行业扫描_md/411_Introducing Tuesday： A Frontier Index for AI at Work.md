# Introducing Tuesday: A Frontier Index for AI at Work

> 来源：Surge AI Blog，2026 年 8 月 18 日

---

It’s Tuesday morning.

You need to understand a retention chart in a slide deck and figure out why new customers are churning. Then read a 70-page security policy and figure out which requirements apply to a customer in Europe.

There’s a spreadsheet attached to an email and a Slack thread with half the context you need. By noon, you need to write a report to your VP.

None of this is extraordinary work.

**That’s the point. Can models get through Tuesday?**

Right now, mostly not. The best model in the world scores 30.7% on GDP.pdf, our benchmark built from real PDFs pulled from expert workflows. It scores 36.2% on HANDBOOK.md, our benchmark for agentic instruction following. Yet the same generation of models is solving 87-year-old math problems.

The frontier is uneven. Models can solve extraordinary problems and still struggle with ordinary work. Each benchmark captures one part of that story, but no single benchmark tells you how those capabilities add up.

That’s why we’re introducing the [**Tuesday Index**](https://surgehq.ai/benchmarks) **:** a composite measure of professional intelligence.

The Tuesday Index starts with eight Surge benchmarks spanning instruction following, writing, graphical understanding, professional documents, agents, judgment, and novel reasoning. We combine them into a single **Tuesday Score** .

As we build better benchmarks for real work, the index will grow with them. The idea behind it is simple:

**A job isn’t a single skill.**

## A job isn’t a single skill

Go back to that Tuesday morning and look at what it required.

* Read the chart: that's [**Chartography**](https://surgehq.ai/benchmarks/chartography) .
* Follow a long company policy while using tools: [**HANDBOOK.md**](https://surgehq.ai/benchmarks/handbook) .
* Track interacting constraints: [**ComplexConstraints**](https://surgehq.ai/benchmarks/complex-constraints) .
* Reason over professional documents: [**GDP.pdf**](https://surgehq.ai/benchmarks/gdp-pdf) .
* Operate inside a messy organization: [**CoreCraft**](https://surgehq.ai/benchmarks/enterprisebench-corecraft) .
* Explain the result to another human: [**Hemingway-bench**](https://surgehq.ai/benchmarks/hemingway-bench) .
* Exercise real-world judgment: [**Antidote**](https://surgehq.ai/benchmarks/antidote) .

Professionals rarely use one skill at a time. An investment recommendation might require reading a chart, parsing a long document, reconciling conflicting instructions, using several tools, and turning all of it into something another person can act on. That combination is what forms professional intelligence.

## How we decide what to benchmark

We start building benchmarks by asking a single question: **what will models need to be good at to do more of the world’s work?**

We get at that from a few directions:

**We look forward.** We look ahead at the capabilities that should matter more as models move from answering questions to completing work: judgment, reliability, tool use, long-horizon context, and communication.

**We watch where models break.** We run models on our own data and inside our own environments, and pay attention to where they fail. Some of our best benchmark ideas start as an interesting behavior that seems small, then turns out to expose a much broader weakness.

**We work alongside real professionals.** We study what lawyers, engineers, scientists, analysts, and other professionals actually need to do over the course of their day.

That produces a capability map, and we think about that map along a few axes.

## Some capabilities are the floor.
Others are the ceiling.

Some capabilities are table stakes.

A model can solve a research-level math problem and still miss a constraint in an email, apply the wrong policy, or lose an instruction halfway through a task.

Follow the instructions. Keep the context. Use the right tool. These are **floor capabilities** , captured in benchmarks like **ComplexConstraints** and **HANDBOOK.md** .

At the other end are **ceiling capabilities** : tests of how far intelligence can go. [**Riemann-bench**](https://surgehq.ai/benchmarks/riemann-bench) tests advanced mathematics written by leading mathematicians, requiring deep reasoning and novel synthesis.

One of the stranger facts about current models is that the ceiling and the floor don’t necessarily rise together. Models are already saturating parts of Riemann-bench while still failing to read a Bode plot correctly.

## Some capabilities are broad.
Others are narrow.

Another distinction is **broad capabilities versus component skills** .

Writing is broad and easy to underestimate. It's tempting to treat writing as cosmetic, something that happens after the real work is done.

But in knowledge work, writing often _is_ the work. A lawyer writes. A scientist presents. A coding agent has to explain what it changed.

A model that is brilliant but dense, elliptical, and exhausting to interact with is less useful. Some of today's most capable models are unpleasant to work with.

That’s why **Hemingway-bench** and **Antidote** belong beside our agent and professional-work evaluations.

Other skills are narrower. Reading a chart sounds small, until a decision depends on it. **Chartography** tests whether models can understand the specialized graphics professionals use every day.

Useful intelligence depends on thousands of component skills like these.

## The Tuesday Index turns the capability map into a score.

Useful intelligence has layers.

First, the basics have to work: **follow instructions, keep context, communicate clearly.**

Then come the skills: **read the chart, write the code, understand the specialized tools.**

Then expertise and composition: **apply judgment, combine those skills, and get the work done.**

No single benchmark measures that stack. So the Tuesday Index combines these skills into an understandable measure of professional intelligence.

## What’s in the Tuesday Index

The first version of the Tuesday Index includes:

* **Chartography:** Professional graphical reasoning
* **HANDBOOK.md:** Long-context agentic instruction following
* **Antidote:** Everyday real-world judgment
* **Hemingway-bench:** Creative, business, and everyday writing
* **ComplexConstraints:** Professional instruction following
* **GDP.pdf:** Professional multimodal reasoning
* **CoreCraft:** Agents operating inside realistic companies
* **Riemann-bench:** Frontier mathematical reasoning

Together, they span floor and ceiling capabilities, broad abilities and narrow skills, isolated tasks and composed workflows.

[frontier-index-widget]

Fable 5 (Adaptive/Max) leads the Tuesday Index with a **Tuesday Score of 66.8** , followed closely by GPT 5.6 Sol (Max) at **66\.7** . Gemini 3.7 Flash (High) sits about eight points back at **58\.2** , while Muse Spark 1.2 (xHigh) trails by roughly 14 points at **53\.5** .

**No model is close to mastering Tuesday.**

## The Tuesday Index will get harder

These eight benchmarks aren’t a complete definition of useful intelligence. There’s still a lot we don’t measure well.

* Can an agent maintain judgment across a week?
* Can it collaborate and delegate?
* Can it build the artifacts professionals actually use: spreadsheets, presentations, diagrams, interfaces, models?
* Can it prioritize? Persuade?
* Can it be extraordinarily capable and still be pleasant to work with all day?

We’re building toward directions like these. As we develop good benchmarks for them, they’ll become part of the Tuesday Index.

## See you on Tuesday

Frontier models can already do remarkable work. But an ordinary workday is a different test, and real work has a way of finding the gaps.

Most of the value AI creates won’t come from one spectacular answer. It’ll come on a Tuesday morning, when your inbox is full, the requirements have changed, the tools don’t quite cooperate, and the job still needs to get done.

**Tuesday measures which models you’d want doing it.**

See you there.

Explore the [Tuesday Index](https://surgehq.ai/benchmarks) and the benchmarks behind it.

---

## 原文链接

https://surgehq.ai/blog/tuesday-frontier-work-index
