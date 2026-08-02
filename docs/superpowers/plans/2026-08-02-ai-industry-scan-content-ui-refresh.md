# AI Industry Scan Content and UI Refresh Implementation Plan

> **For Codex:** Execute this plan in the isolated `codex/content-ui-refresh` worktree. Keep content and UI audit ledgers separate, and preserve the release confirmation gate.

**Goal:** Update the public site from 360 to 387 Notes, improve all seven topic articles where the new evidence warrants it, and integrate the reviewed responsive frontend redesign.

**Architecture:** Keep the existing static-site pipeline: source JSONL + topic metadata + assignments + Markdown reviews are compiled by `site/build_data.py` into `site/data.json`. Replace the monolithic page with the handoff package's split `index.html`, `css/style.css`, and `js/app.js`, then adjust tokens and copy locally.

**Tech Stack:** Python standard library, JSON/Markdown content files, vanilla HTML/CSS/JavaScript, `unittest`, local HTTP browser QA.

---

### Task 1: Build the new-note evidence and assignment matrix

**Files:**
- Read: `notes/AI行业扫描_keywords.jsonl`
- Read: `notes/AI行业扫描_md/361_*.md` through `notes/AI行业扫描_md/387_*.md`
- Create: `docs/research/2026-08-02-notes-361-387-review.md`

1. Record each Note's source type, author judgment, evidence boundary, proposed 1–3 topics, and possible article impact.
2. Open full Markdown for entries that add a claim, number, technical mechanism, counterexample, or article citation.
3. Separate confirmed article changes from entries that should remain Notes-only.

### Task 2: Add contract tests before data and frontend changes

**Files:**
- Modify: `tests/test_site_contract.py`

1. Replace hard-coded 360 expectations with source-to-bundle consistency checks.
2. Add failing tests for assignments 361–387, count-agnostic metadata, split asset references, Chinese brand copy, name placement, mobile overflow protection, and readable color tokens.
3. Run the focused tests and confirm each new expectation fails for the intended missing behavior.

### Task 3: Revise the seven topic articles

**Files:**
- Modify: `site/reviews/model-training.md`
- Modify: `site/reviews/architecture-engineering.md`
- Modify: `site/reviews/eval-benchmark.md`
- Modify: `site/reviews/ai-coding.md`
- Modify: `site/reviews/product-interaction.md`
- Modify: `site/reviews/industry-strategy.md`
- Modify: `site/reviews/impact-safety.md`

1. Run the text audit and open every finding in context.
2. Build a per-article claim ledger and list the main problems before rewriting.
3. Consolidate repeated claims, remove low-information paragraphs, and integrate only decision-relevant new evidence.
4. Preserve facts, numbers, source boundaries, plain headings, concrete tools, and falsifiers.
5. Re-run article contract tests and the text audit.

### Task 4: Classify and rebuild all Notes

**Files:**
- Modify: `site/topic_assignments.json`
- Modify: `site/data.json` via `site/build_data.py`

1. Add 361–387 assignments from the reviewed matrix.
2. Run `python site/build_data.py`.
3. Verify 387 Notes, seven non-empty topics, unchanged authored `why`, and resolved references.

### Task 5: Integrate and refine the frontend

**Files:**
- Modify: `site/index.html`
- Create: `site/css/style.css`
- Create: `site/js/app.js`

1. Bring in only the three runtime files from the handoff package.
2. Restore “AI 行业扫描 Notes” and localize decorative English microcopy that conflicts with the established voice.
3. Make meta descriptions count-agnostic.
4. Update secondary text tokens to accessible contrast.
5. Prevent `.act-tip` from widening the mobile page.
6. Preserve routing, search, filters, cited/recent/all views, load-more, references, contact, and old safety hash compatibility.

### Task 6: Verify the complete candidate

**Files:**
- Verify: all modified site and test files

1. Run `python -m unittest discover -s tests -v`.
2. Run `node --check site/js/app.js` and `git diff --check`.
3. Re-run writing and UI text audits and reconcile intentional remaining hits.
4. Serve the site locally; inspect 1440×900 and 390×844.
5. Exercise homepage/topic routing, search, filters, load more, references, keyboard focus, mobile overflow, and browser console.
6. Commit the verified branch and report the exact diff and preview state without merging or pushing.
