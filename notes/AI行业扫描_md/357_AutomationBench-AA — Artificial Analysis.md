# AutomationBench-AA — Artificial Analysis

**作者：** Artificial Analysis (@ArtificialAnlys)  
**发布时间：** 2:12 AM · Jul 7, 2026  
**原文链接：** [https://x.com/ArtificialAnlys/status/2074194764510208230](https://x.com/ArtificialAnlys/status/2074194764510208230)

---

Announcing AutomationBench-AA, our independent leaderboard for Zapier's AutomationBench, testing whether AI agents can automate real SaaS workflows while adhering to business rules.

We partnered with @zapier to run AutomationBench-AA on their private benchmark subset. This benchmark is a complex agentic workflow automation test across simulated SaaS applications. Models must complete 657 tasks spanning Finance, HR, Marketing, Operations, Sales, and Support, working across 40 simulated app environments including Gmail, Google Sheets, Slack, Salesforce, Zendesk, Jira, and HubSpot.

Unlike Zapier's hosted leaderboard, the headline score for AutomationBench-AA shows the share of objectives a model completes without violating any guardrails. Claude Fable 5 and Opus 4.8 from @AnthropicAI lead with scores of 48.6% and 48.5%, followed by @GoogleDeepMind's Gemini 3.5 Flash at 42.6% and @OpenAI's GPT-5.5 (xhigh) at 42.1%. With Anthropic's new classifier, Fable 5 fell back to Opus on ~18% of tasks.

**Key elements of AutomationBench:**

**Real workflow patterns, simulated environments:** Tasks are drawn from real workflow patterns on Zapier and run in simulated SaaS environments, where a single task may span a range of applications like CRM, email, calendar, and messaging platforms.

**Autonomous API discovery:** Models interact with each app through REST APIs, discovering the endpoints they need through structured tool calls and navigating environments with irrelevant and sometimes misleading records.

**Objectives and guardrails:** Models are scored against nearly 12,000 assertions Zapier built to test that the model completed the task correctly in full. Each assertion is classified as either an objective the agent must achieve, or a guardrail that already passes initially and must not be broken.

**Programmatic environment grading:** Tasks are graded solely on whether the correct data ended up in the right systems, with deterministic checks against the environment. Each task runs once with a 50-turn cap.

**Key results for AutomationBench-AA:**

- **Claude Fable 5 (max) leads at 48.6%** but falls back to Opus 4.8 in ~18% of tasks. It completes 73% of task objectives, with the fallback behavior likely explaining the limited uplift compared to Opus.
- **Every model breaks business rules:** Guardrail violations range from 0.46 per task (Gemini 3.5 Flash) to 1.26 (Qwen3.7 Plus). Gemini 3.5 Flash completes 15.0 objectives per guardrail violation, the best ratio of any model, ahead of Claude Opus 4.8 (max, 13.5).
- **Gemini 3.5 Flash performs well for its price:** At 42.6% and $0.49 per task, it effectively matches GPT-5.5 (xhigh, 42.1%, $1.32 per task) at ~37% of the cost.
- **GLM-5.2 (max) from @Zai_org is the leading open weights model at 27.8%.** This places the open weights frontier ~10 points behind Gemini 3.1 Pro Preview, and with substantially higher guardrail violations per task.
- **Finance workflow tasks are the most difficult to automate today:** across the models we evaluated at launch, agents complete roughly half the proportion of objectives on Finance tasks, compared to Support and Operations tasks.

We would like to thank Zapier and the benchmark authors for their great work developing this evaluation for important SaaS workflows, and appreciate their collaboration in launching AutomationBench on Artificial Analysis!

---

**Thread replies:**

> AutomationBench-AA evaluates models on 657 workflow automation tasks developed by Zapier from real workflow patterns on its platform. Models orchestrate work across 40 simulated SaaS app environments via REST APIs, and every task is graded programmatically on the final state of the environment.

> While completing objectives, agents must also avoid breaking guardrails that represent business rules. Every model we evaluated at launch triggers guardrail violations, and violation-adjusted efficiency separates the leaders: Gemini 3.5 Flash completes 15.0 objectives per guardrail violation.

> Task difficulty varies significantly by business domain. Finance workflows are the hardest to automate: across all models, agents complete around one third of Finance objectives, roughly half the rate of Support and Operations (~60%).
