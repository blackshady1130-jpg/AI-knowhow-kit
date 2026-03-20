# How I Use Claude Code

By Boris Tane

I've been using Claude Code as my primary development tool for approx 9 months, and the workflow I've settled into is radically different from what most people do with AI coding tools. Most developers type a prompt, sometimes use plan mode, fix the errors, repeat.

The workflow I'm going to describe has one core principle: **never let Claude write code until you've reviewed and approved a written plan.** This separation of planning and execution is the single most important thing I do.

```
Research → Plan → Annotate (repeat 1-6x) → Todo List → Implement → Feedback & Iterate
```

## Phase 1: Research

Every meaningful task starts with a deep-read directive. I ask Claude to thoroughly understand the relevant part of the codebase before doing anything else. And I always require the findings to be written into a persistent markdown file, never just a verbal summary in the chat.

Notice the language: "deeply", "in great details", "intricacies", "go through everything". Without these words, Claude will skim.

The written artifact (`research.md`) is critical. It's my review surface. I can read it, verify Claude actually understood the system, and correct misunderstandings before any planning happens.

This is the most expensive failure mode with AI-assisted coding — implementations that work in isolation but break the surrounding system. The research phase prevents all of this.

## Phase 2: Planning

Once I've reviewed the research, I ask for a detailed implementation plan in a separate markdown file. I use my own `.md` plan files rather than Claude Code's built-in plan mode. The built-in plan mode sucks. My markdown file gives me full control.

One trick I use constantly: for well-contained features where I've seen a good implementation in an open source repo, I'll share that code as a reference alongside the plan request.

## The Annotation Cycle

This is the most distinctive part of my workflow. After Claude writes the plan, I open it in my editor and add inline notes directly into the document. These notes correct assumptions, reject approaches, add constraints, or provide domain knowledge that Claude doesn't have.

Then I send Claude back to the document:

> I added a few notes to the document, address all the notes and update the document accordingly. don't implement yet

This cycle repeats 1 to 6 times. The explicit "don't implement yet" guard is essential.

### Why This Works So Well

The markdown file acts as shared mutable state between me and Claude. Three rounds of "I added notes, update the plan" can transform a generic implementation plan into one that fits perfectly into the existing system. Claude is excellent at understanding code, proposing solutions, and writing implementations. But it doesn't know my product priorities, my users' pain points, or the engineering trade-offs I'm willing to make. The annotation cycle is how I inject that judgement.

### The Todo List

Before implementation starts, I always request a granular task breakdown. This creates a checklist that serves as a progress tracker during implementation.

## Phase 3: Implementation

When the plan is ready, I issue the implementation command:

> implement it all. when you're done with a task or phase, mark it as completed in the plan document. do not stop until all tasks and phases are completed. do not add unnecessary comments or jsdocs, do not use any or unknown types. continuously run typecheck to make sure you're not introducing new issues.

By the time I say "implement it all," every decision has been made and validated. The implementation becomes mechanical, not creative.

## Feedback During Implementation

Once Claude is executing the plan, my role shifts from architect to supervisor. My prompts become dramatically shorter:

- "You built the settings page in the main app when it should be in the admin app, move it."
- "there's a 2px gap"
- "still cropped"
- "wider"

When something goes in a wrong direction, I don't try to patch it. I revert and re-scope.

## Staying in the Driver's Seat

- **Cherry-picking from proposals**: I go through items one by one, making item-level decisions.
- **Trimming scope**: "remove the download feature from the plan, I don't want to implement this now."
- **Protecting existing interfaces**: "the signatures of these three functions should not change."
- **Overriding technical choices**: "use this library's built-in method instead of writing a custom one."

## Single Long Sessions

I run research, planning, and implementation in a single long session. I am not seeing the performance degradation everyone talks about after 50% context window. The plan document, the persistent artifact, survives compaction in full fidelity.

## The Workflow in One Sentence

Read deeply, write a plan, annotate the plan until it's right, then let Claude execute the whole thing without stopping, checking types along the way.

No magic prompts, no elaborate system instructions, no clever hacks. Just a disciplined pipeline that separates thinking from typing.

---
Source: https://boristane.com/blog/how-i-use-claude-code/
