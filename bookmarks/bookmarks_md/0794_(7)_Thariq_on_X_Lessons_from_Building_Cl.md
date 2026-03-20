# Lessons from Building Claude Code: How We Use Skills

作者：Thariq (@trq212) · 2026-03-17 · Claude Code @anthropicai

Skills have become one of the most used extension points in Claude Code. They're flexible, easy to make, and simple to distribute. We've been using skills in Claude Code extensively at Anthropic with hundreds of them in active use. These are the lessons we've learned.

## What are Skills?

A common misconception is that skills are "just markdown files", but the most interesting part is that they're not just text files. They're folders that can include scripts, assets, data, etc. that the agent can discover, explore and manipulate. Skills also have a wide variety of configuration options including registering dynamic hooks.

## Types of Skills

After cataloging all of our skills, we noticed they cluster into a few recurring categories:

### 1. Library & API Reference
Skills that explain how to correctly use a library, CLI, or SDKs. Examples: billing-lib, internal-platform-cli, frontend-design.

### 2. Product Verification
Skills that describe how to test or verify that your code is working. Paired with tools like playwright, tmux, etc. Verification skills are extremely useful for ensuring Claude's output is correct. It can be worth having an engineer spend a week just making your verification skills excellent.

### 3. Data Fetching & Analysis
Skills that connect to your data and monitoring stacks. Examples: funnel-query, cohort-compare, grafana.

### 4. Business Process & Team Automation
Skills that automate repetitive workflows into one command. Examples: standup-post, create-ticket, weekly-recap.

### 5. Code Scaffolding & Templates
Skills that generate framework boilerplate. Examples: new-workflow, new-migration, create-app.

### 6. Code Quality & Review
Skills that enforce code quality. Examples: adversarial-review, code-style, testing-practices.

### 7. CI/CD & Deployment
Skills that help you fetch, push, and deploy code. Examples: babysit-pr, deploy, cherry-pick-prod.

### 8. Runbooks
Skills that take a symptom, walk through a multi-tool investigation, and produce a structured report. Examples: debugging, oncall-runner, log-correlator.

### 9. Infrastructure Operations
Skills that perform routine maintenance and operational procedures. Examples: orphans cleanup, dependency-management, cost-investigation.

## Tips for Making Skills

### Don't State the Obvious
Claude knows a lot about your codebase and coding. Focus on information that pushes Claude out of its normal way of thinking.

### Build a Gotchas Section
The highest-signal content in any skill is the Gotchas section. Build up from common failure points that Claude runs into.

### Use the File System & Progressive Disclosure
A skill is a folder, not just a markdown file. Think of the entire file system as a form of context engineering and progressive disclosure.

### Avoid Railroading Claude
Give Claude the information it needs, but give it the flexibility to adapt to the situation.

### Think through the Setup
Some skills may need to be set up with context from the user. A good pattern is to store setup information in a config.json file.

### The Description Field Is For the Model
When Claude Code starts a session, it builds a listing of every available skill with its description. The description field is not a summary — it's a description of when to trigger.

### Memory & Storing Data
Some skills can include a form of memory by storing data within them. Store data in a stable folder using `${CLAUDE_PLUGIN_DATA}`.

### Store Scripts & Generate Code
One of the most powerful tools you can give Claude is code. Giving Claude scripts and libraries lets Claude spend its turns on composition.

### On Demand Hooks
Skills can include hooks that are only activated when the skill is called. Examples: /careful — blocks rm -rf, DROP TABLE, force-push. /freeze — blocks edits outside specific directories.

## Distributing Skills

Two ways to share skills:
- Check your skills into your repo (under ./.claude/skills)
- Make a plugin for the Claude Code Plugin marketplace

## Managing a Marketplace
We don't have a centralized team that decides; instead we find the most useful skills organically. Once a skill has gotten traction, they can put in a PR to move it into the marketplace.

## Measuring Skills
We use a PreToolUse hook to log skill usage within the company.

---
Source: https://x.com/trq212/status/2033949937936085378
