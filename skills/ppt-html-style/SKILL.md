---
name: ppt-html-style
description: Build browser-playable 16:9 HTML slide decks in a restrained strategy-report style. Use when Codex needs to turn PPT, Excel, Markdown, notes, research, or data materials into an HTML version of a presentation, slide deck, flip-through report, management briefing, or strategy deck.
---

# PPT HTML Style

Use this skill to make an HTML slide deck, not a web article. Each page is a fixed 16:9 slide with limited space, strong hierarchy, and one clear judgment.

## Workflow

### 1. Plan before writing HTML

First classify the input:

| Input type | Signal | Slide strategy |
|---|---|---|
| Data reconstruction | Excel/table/numbers are central | One data dimension per page; KPI blocks, tables, progress bars |
| Insight memo | Markdown/long-form research is central | One claim per page; evidence, callouts, comparison frames |
| Mixed report | Both data and narrative matter | Alternate overview, evidence, judgment, and implication pages |

Before building, produce a compact plan:

```text
== Deck Plan ==
Theme: [one-line title]
Type: [data reconstruction / insight memo / mixed report]
Total pages: [N]
Parts: [part names and page ranges]

== Slide Plan ==
P1 Cover - [judgment title]
P2 Contents - [parts]
P3 [Part 01] - layout: [KPI + table / two-column comparison / timeline / callout]
...
PN Closing
```

### 2. Build with the reference template

Read `references/reference.md` before writing the HTML. It contains:

- the complete HTML skeleton;
- CSS tokens and component classes;
- cover, contents, content-page, KPI, table, progress bar, two-column, callout, and closing templates;
- navigation JavaScript.

Use a single HTML file with:

- Tailwind CDN;
- Google Fonts: Noto Sans SC + JetBrains Mono;
- dark viewport background;
- white 16:9 slide card;
- blue/orange business palette;
- keyboard/page-dot navigation.

### 3. Review like a strategy deck

After generating HTML, inspect the file yourself and check:

- Each slide has one core message.
- Page titles are judgments, not neutral topic labels.
- Numbers, units, dates, and table alignment match the source material.
- Pages have a logical order: context -> evidence -> mechanism -> implication -> next action.
- No page overflows the 16:9 slide frame.
- No decorative element exists without an information role.

If the deck is meant for management, the first 30 seconds should reveal the three key takeaways.

## Design Rules

- Use 16:9 fixed slides; avoid scrolling pages.
- Keep content dense but not cramped.
- Use blue for structure and primary emphasis; orange for secondary emphasis or warnings.
- Use JetBrains Mono for numbers, percentages, dates, page numbers, and code.
- Keep page numbers in `03 / 09` format.
- Keep tables to about 8 rows per slide; split longer tables.
- Prefer KPI grids, two-column comparisons, timelines, and callouts over paragraphs.

## Anti-Patterns

- Do not paste long article paragraphs into slides.
- Do not use descriptive titles such as “Market Overview” when a judgment title is possible.
- Do not turn a slide into a dashboard wall.
- Do not shrink text below readability to fit too much content.
- Do not add decorative icons, pills, or arrows without meaning.
- Do not make a web page that happens to look like slides; make slides.

## Deliverable

Return the final `.html` file path and summarize the deck structure. If local browser QA is available, open the HTML and verify page navigation, frame fit, and obvious overflow.
