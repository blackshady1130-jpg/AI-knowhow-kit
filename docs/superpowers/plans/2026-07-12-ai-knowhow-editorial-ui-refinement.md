# AI Knowhow Kit Editorial & UI Refinement Implementation Plan

> **Execution note:** Work only on `codex/blog-content-redesign` in the dedicated worktree. Do not merge, push, or deploy until the user reviews the local result.

**Goal:** Integrate notes 351–360, rewrite the seven research chapters as distinct evidence-backed essays, and simplify the homepage/UI so the personal thesis is clear without generic AI-page decoration.

**Architecture:** The notes JSONL remains the source of truth. `site/topic_assignments.json` maps notes into seven editorial topics, `site/build_data.py` joins notes, topics, and Markdown reviews into `site/data.json`, and `site/index.html` renders the homepage, article reader, and evidence browser. Tests define the content and interaction contract before implementation.

**Tech stack:** Static HTML/CSS/vanilla JavaScript, Python data builder, Python `unittest`, Node.js syntax check, headless Chrome for visual QA.

---

## Task 1: Lock the 360-note and editorial contract

**Files:**
- Modify: `tests/test_site_contract.py`

1. Change note-count expectations from 350 to 360.
2. Add tests that 351–360 all have valid topic assignments and all appear in article references.
3. Replace the identical-heading contract with structural requirements: one core judgment, evidence boundaries, an article-specific instrument, and a falsification section.
4. Reject the chronological patch heading and stale “56 articles” copy.
5. Add UI assertions for a solid Hero, no topic emoji, no vanity word-count metric, native recent-note links, and accessible note references.
6. Run `python -m unittest discover -s tests -v` and confirm the new tests fail for the expected missing implementation.
7. Commit the red tests.

## Task 2: Classify and bundle notes 351–360

**Files:**
- Modify: `site/topic_assignments.json`
- Modify: `site/topics.json`
- Regenerate: `site/data.json`

1. Assign each new note to one to three topics based on the argument it supports, not keyword overlap alone.
2. Update topic titles/questions/theses where the new evidence changes the framing.
3. Run `python site/build_data.py`.
4. Run the data-contract tests and confirm the bundle contains 360 notes with authored `why` preserved.
5. Commit the data update.

## Task 3: Rewrite the seven essays

**Files:**
- Modify: `site/reviews/model-training.md`
- Modify: `site/reviews/architecture-engineering.md`
- Modify: `site/reviews/eval-benchmark.md`
- Modify: `site/reviews/ai-coding.md`
- Modify: `site/reviews/product-interaction.md`
- Modify: `site/reviews/industry-strategy.md`
- Modify: `site/reviews/impact-safety.md`

For each essay:

1. Re-read the relevant indexed notes and selected original Markdown sources.
2. State the thesis once, then build the mechanism through contrasted evidence.
3. Integrate 351–360 inside the argument; do not append an update log.
4. Label evidence strength and applicability when using papers, company benchmarks, public leaderboards, or personal essays.
5. Replace generic advice with the topic-specific tool defined in the design.
6. End with two or three falsification conditions.
7. Run the writing scan from `removing-ai-slop`; inspect every hit in context and revise only genuine repetition, empty abstraction, or templated phrasing.
8. Run review-contract tests after each small batch and commit the completed seven-essay rewrite.

## Task 4: Simplify homepage copy and UI

**Files:**
- Modify: `site/index.html`
- Regenerate: `site/data.json` if topic metadata changes

1. Replace the gradient Hero with a solid editorial masthead, one thesis, one boundary paragraph, and two CTAs.
2. Merge the three-question and research-arc sections.
3. Render the seven topics as a chapter list with separators instead of emoji cards.
4. Reduce recent notes and make each item a native link.
5. Replace absolute note-review claims and vanity metrics with accurate provenance copy.
6. Convert inline note citations into keyboard-focusable controls while preserving the evidence side panel/browser.
7. Fix small-screen navigation, CTA wrapping, and horizontal overflow.
8. Run JavaScript syntax and site-page contract tests.
9. Run the development scan from `removing-ai-slop`, review each lead, and remove generic visual/copy patterns that do not carry information.
10. Commit the UI rewrite.

## Task 5: Verify content, behavior, and visual rendering

**Files:**
- Modify only if verification finds defects.

1. Run `python site/build_data.py`.
2. Run `python -m unittest discover -s tests -v` and require zero failures.
3. Run the inline JavaScript parser and `git diff --check`.
4. Run the writing and development slop scans on all seven reviews and `site/index.html`; preserve a brief before/after finding ledger.
5. Serve the site locally and inspect homepage, one long article, note panel, search/filter/load-more interactions, and source links.
6. Capture desktop and 390px mobile renders; verify `scrollWidth === clientWidth`, CTA visibility, focusable citations, and no clipped navigation.
7. Re-read this plan and check every requirement against the final diff.
8. Commit only verified fixes. Stop with a clean feature worktree and provide the user a local preview plus commit summary. Do not merge.

