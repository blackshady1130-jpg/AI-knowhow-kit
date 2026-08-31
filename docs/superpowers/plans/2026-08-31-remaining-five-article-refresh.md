# Remaining Five Topic Articles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the five remaining topic reviews so they absorb the highest-value Notes #388–#424, keep distinct responsibilities, and remove repeated or machine-default prose.

**Architecture:** Each article owns one reader question defined in the approved seven-topic design. Rewrite section structure before polishing sentences, keep Note `#id` references as the evidence bridge, and update the review contract only after all five articles are stable.

**Tech Stack:** Markdown, Python `unittest`/`pytest`, Node.js text audit, Git.

## Global Constraints

- Preserve the seven existing topic names and homepage order.
- Modify only the five named review articles, the review evidence contract, and planning documentation.
- Do not modify `notes/**`, `site/data.json`, `site/topics.json`, `site/topic_assignments.json`, UI, CSS, or JavaScript.
- Keep facts, source views, author judgment, and inference visibly separate.
- Keep each article at roughly 4,500–5,800 characters and retain its practical instrument plus a two- or three-item falsifier section.
- Use direct Chinese headings; remove repeated conclusions, low-information summaries, translation-like phrasing, and decorative abstractions.
- Do not publish, rebuild data, merge, or push without a later explicit user request.

---

### Task 1: Freeze the evidence and responsibility ledger

**Files:**
- Reference: `docs/superpowers/specs/2026-08-30-seven-topic-article-refresh-design.md`
- Reference: `notes/AI行业扫描_keywords.jsonl`
- Reference: `site/topic_assignments.json`
- Create locally: `.tmp/remaining-five-article-refresh/evidence-ledger.md`

**Interfaces:**
- Consumes: approved article responsibilities and Notes #388–#424.
- Produces: one section map, Note inclusion list, exclusion list, and factual boundary list per article.

- [ ] **Step 1: Record preservation constraints**

  Record each article title, thesis, practical instrument name, important numbers, named sources, counterexamples, and qualification language.

- [ ] **Step 2: Record the canonical owner of repeated claims**

  Use these ownership rules:

  - Runtime state, recovery, and permission implementation → `architecture-engineering.md`.
  - Benchmark audit, Rubric, Verifier reliability, and failure attribution → `eval-benchmark.md`.
  - Software cycle time, Review queues, accepted-task cost, and coding control points → `ai-coding.md`.
  - User-visible trigger, state, authorization, review, takeover, and Memory → `product-interaction.md`.
  - Model training, post-training, Attention, inference budget, and research strategy → `model-training.md`.
  - Adoption, Token economics, inference supply, routing, data markets, and profit → `industry-strategy.md`.
  - Decision rights, propagated permissions, labor effects, and responsibility → `impact-safety.md`.

- [ ] **Step 3: Record the selected new evidence**

  - AI Coding: #396, #413, #415; use #405 only as an unproven boundary.
  - Product: #390, #396, #403, #410, #413.
  - Model: #407, #416, #418; use #408 and #409 as boundaries and updates.
  - Industry: #389, #397, #406, #421, #424.
  - Safety: #396, #403, #420; do not make #400 a mainline claim.

- [ ] **Step 4: Verify every selected Note exists**

  Run a JSONL ID check against `notes/AI行业扫描_keywords.jsonl`.

  Expected: every selected ID exists exactly once.

---

### Task 2: Rewrite AI Coding

**Files:**
- Modify: `site/reviews/ai-coding.md`

**Interfaces:**
- Consumes: #396, #405, #413, #415 and retained coding evidence.
- Produces: a coding-specific account of where time, cost, control, and Review move after generation gets cheaper.

- [ ] **Step 1: Replace the section structure**

  Use this progression:

  1. Coding moves quickly because code can run, compare, and roll back.
  2. Faster generation can move the bottleneck to Review and integration.
  3. Route model, effort, and Harness by risk and cost per accepted task.
  4. Keep coding-specific test quality; refer broader benchmark audit to the evaluation article.
  5. Move human control from command prompts to plans, risk boundaries, exceptions, and final acceptance.
  6. Explain why multi-Agent throughput stops at human attention and Review capacity.

- [ ] **Step 2: Remove off-topic material**

  Delete the OpenCode traffic/revenue/platform paragraph. Compress general SWE-Bench audit and generic Harness mechanics already owned by other articles.

- [ ] **Step 3: Add selected new evidence with boundaries**

  Bind #396 numbers to the reported Anthropic experiment and do not universalize them. Use #413 for worktree/status/Review bottlenecks, #415 for Harness ablation, and #405 only to say self-modifying loops remain unproven.

- [ ] **Step 4: Retain the practical instrument**

  Keep `任务分级与成本记录表`, but ensure it records accepted task, cycle time, escaped defects, Review, rework, and maintenance rather than generated code volume.

- [ ] **Step 5: Run focused checks**

  Confirm required IDs, 4,500–5,800 characters, direct headings, and no broken `#id` references.

- [ ] **Step 6: Commit**

  Stage only `site/reviews/ai-coding.md` and commit with `docs: refresh AI coding review`.

---

### Task 3: Rewrite AI Product and Interaction

**Files:**
- Modify: `site/reviews/product-interaction.md`

**Interfaces:**
- Consumes: #390, #396, #403, #410, #413 and retained product evidence.
- Produces: a user-facing control model from task trigger through takeover and Memory correction.

- [ ] **Step 1: Replace the section structure**

  Use this progression: trigger → task state → authorization → artifact review → takeover → Memory.

- [ ] **Step 2: Remove repeated state explanations**

  Consolidate current repetitions about chat history, progress, and task state into one section. Compress GPT-Live to a bounded example of interruption and background delegation.

- [ ] **Step 3: Add selected new evidence with boundaries**

  Use #390 for intent/state-machine failure, #396 for low-value prompt approvals, #403 for post-read/pre-egress permission, #410 only as a simulated persistent-world example, and #413 for artifact-specific Review UI and attention limits.

- [ ] **Step 4: Compress evaluation mechanics**

  Keep one short product-learning paragraph about turning accepted outcomes and corrections into Eval/Skill inputs; do not re-explain Rubric or failure attribution.

- [ ] **Step 5: Retain the practical instrument**

  Keep `权限与人工接管分级表`, but connect each level to visible state, review evidence, and a takeover trigger.

- [ ] **Step 6: Run focused checks and commit**

  Verify IDs, length, headings, and references. Stage only `site/reviews/product-interaction.md` and commit with `docs: refresh product interaction review`.

---

### Task 4: Rewrite Model Training and Inference

**Files:**
- Modify: `site/reviews/model-training.md`

**Interfaces:**
- Consumes: #407, #416, #418, #408, #409 and retained training evidence.
- Produces: an explanation of capability as the combined result of data, training, inference, architecture, and environment.

- [ ] **Step 1: Replace the section structure**

  Use this progression:

  1. Fix comparison conditions before discussing capability.
  2. Explain post-training as a production system of teachers, environments, Verifiers, rollouts, and versions.
  3. Separate execution depth from the ability to change a research strategy.
  4. Explain Attention, Context, and effort as different controls over information, compute, and cost.
  5. Close with the model comparison checklist.

- [ ] **Step 2: Compress migrated material**

  Move the main J-space/consciousness discussion to Safety; retain only a one-sentence mechanism boundary. Compress diffusion generation order to one counterexample and reduce Runtime state details already owned by Architecture.

- [ ] **Step 3: Add selected new evidence with boundaries**

  Use #407 for post-training organization, #416 for observed strategy lock-in, #418 for Attention taxonomy, #408 to bound small-model-plus-tools claims, and #409 to update joint scaling. Keep vendor observations and observational studies labeled as such.

- [ ] **Step 4: Retain the practical instrument**

  Keep `模型比较清单` and ensure it covers model, data, post-training, effort, Harness, Runtime, cost, and extrapolation boundary without repeating the full article.

- [ ] **Step 5: Run focused checks and commit**

  Verify IDs, length, headings, and references. Stage only `site/reviews/model-training.md` and commit with `docs: refresh model training review`.

---

### Task 5: Rewrite Industry Strategy

**Files:**
- Modify: `site/reviews/industry-strategy.md`

**Interfaces:**
- Consumes: #389, #397, #406, #421, #424 and retained commercial evidence.
- Produces: a five-ledger view of adoption, Token use, revenue, gross margin, and accepted task value.

- [ ] **Step 1: Replace the section structure**

  Use this progression:

  1. Separate Adoption, Token, revenue, margin, and task value.
  2. Explain inference supply through capacity, utilization, latency, energy, and stable demand.
  3. Explain when routing retains value and when large customers graduate.
  4. Separate open-model Token share from closed-model revenue/profit.
  5. Explain the move from Dataset to Training Signal, Environment, Verifier, and QC.
  6. End with enterprise/FDE learning assets.

- [ ] **Step 2: Add selected new evidence with boundaries**

  Use #397 for adoption ambiguity, #421 for asset ownership versus compute rights and demand, #424 for request latency/energy, #406 as a company-stated open/closed and feedback-loop view, and #389 as an industry analysis of training signals.

- [ ] **Step 3: Exclude unsupported material**

  Do not use #402 rumor figures as facts. Do not convert #421 scenarios into forecasts or #424 architecture analysis into an investment conclusion.

- [ ] **Step 4: Retain the practical instrument**

  Keep `AI 项目商业价值检查表`, align it to the five ledgers, and remove rows that only repeat prose without changing a decision.

- [ ] **Step 5: Run focused checks and commit**

  Verify IDs, length, headings, and references. Stage only `site/reviews/industry-strategy.md` and commit with `docs: refresh industry strategy review`.

---

### Task 6: Rewrite AI Safety and Impact

**Files:**
- Modify: `site/reviews/impact-safety.md`

**Interfaces:**
- Consumes: #396, #403, #420 and retained responsibility/labor evidence.
- Produces: an account of who decides, who bears extra work and risk, and who remains responsible.

- [ ] **Step 1: Replace the section structure**

  Use this progression:

  1. Interpretability can diagnose mechanisms but does not prove consciousness or reliable control.
  2. Task success must include business Guardrails and severe side effects.
  3. Human approval should focus on objectives, policy, exceptions, and accountability rather than repetitive prompts.
  4. Authorization follows Context, Memory, Workspace, and derived artifacts.
  5. Examine judgment practice, junior work, Review burden, and expert formation.
  6. Separate proposer, evaluator, and approver in self-improving systems.

- [ ] **Step 2: Compress migrated material**

  Move real-time voice interaction mechanics to Product. Remove Runtime implementation detail from self-improvement while retaining responsibility separation.

- [ ] **Step 3: Add selected new evidence with boundaries**

  Use #420 to describe interpretability as improving diagnosis but immature control, #396 to place humans at higher-value control points, and #403 to explain propagated authorization. Keep #400 out of the mainline because remediation state and attribution are time-sensitive.

- [ ] **Step 4: Retain the practical instrument**

  Keep `责任与额外人工成本清单`, ensuring it records beneficiaries, Review burden, rights, appeals, propagated data use, incident response, and evidence boundaries.

- [ ] **Step 5: Run focused checks and commit**

  Verify IDs, length, headings, and references. Stage only `site/reviews/impact-safety.md` and commit with `docs: refresh AI safety and impact review`.

---

### Task 7: Global deduplication, contract update, and verification

**Files:**
- Modify: `tests/test_site_contract.py`
- Review: `site/reviews/*.md`

**Interfaces:**
- Consumes: all seven final review articles.
- Produces: a clean article set with current evidence expectations and reproducible validation.

- [ ] **Step 1: Run `removing-ai-slop` on all seven reviews**

  Run:

  ```powershell
  node "C:\Users\Administrator\.codex\skills\removing-ai-slop\scripts\audit-text.mjs" site\reviews --json --threshold 0.72
  ```

  Inspect every hit in context. Mark it `fix`, `intentional keep`, or `uncertain`; do not optimize for zero findings.

- [ ] **Step 2: Read headings and first sentences across all seven articles**

  Confirm that each article advances a different question and does not re-explain another article's main mechanism.

- [ ] **Step 3: Update the review evidence contract**

  Set `ReviewContractTests.NEW_EVIDENCE` to:

  ```python
  {
      "model-training.md": {407, 416, 418},
      "architecture-engineering.md": {388, 403, 414, 415, 417},
      "eval-benchmark.md": {395, 399, 410, 419, 423},
      "ai-coding.md": {396, 413, 415},
      "product-interaction.md": {390, 396, 403, 410, 413},
      "industry-strategy.md": {389, 397, 406, 421, 424},
      "impact-safety.md": {396, 403, 420},
  }
  ```

- [ ] **Step 4: Run the full validation suite**

  Run:

  ```powershell
  python -m pytest -q
  python -m py_compile site\build_data.py
  node --check site\js\app.js
  git diff --check origin/main...HEAD
  ```

  Expected: 30 tests pass, Python and JavaScript checks exit 0, and no whitespace errors.

- [ ] **Step 5: Validate exact scope and article data**

  Confirm all article `#id` references exist, each article retains `更新至 2026.08`, each length is 4,500–5,800 characters, and no `notes/**`, `site/data.json`, `site/topics.json`, `site/topic_assignments.json`, UI, CSS, or JavaScript file changed.

- [ ] **Step 6: Commit the contract update**

  Stage only `tests/test_site_contract.py` and commit with `test: refresh topic review evidence contract`.

- [ ] **Step 7: Stop for user review**

  Report the five article paths, Note additions/exclusions, scan triage, test output, and exact changed-file list. Do not merge, push, rebuild data, or publish.
