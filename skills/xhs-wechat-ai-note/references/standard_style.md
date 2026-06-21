# Standard Style: 2026-06-02 to 2026-06-05

This reference locks the earliest standardized image style for「AI行业判断笔记」.

## Canvas

- `W = 1080`, `H = 1920`.
- Outer background: `RED_SOFT = #FFF1F1`.
- Top red band: full width, height about `352-360`.
- Bottom red footer: full width, height `150`.
- Main paper card: `(64, 72, 1016, 1770)`, radius `34`, fill `#FFFDFC`, outline `#E9D4D4`.
- Inner left x: `100` (`MARGIN + 36`).
- Main right boundary: `980` (`W - MARGIN - 36`).

## Colors

- `RED = #D71920`
- `RED_DARK = #A90F16`
- `RED_SOFT = #FFF1F1`
- `PAPER = #FFFDFC`
- `INK = #171717`
- `MUTED = #6A5F5F`
- `LINE = #E9D4D4`
- `PALE = #FFF8F6`

Do not introduce topic palettes. Later green/blue/yellow variants drifted away from this standard.

## Typography

- Chinese regular: `Microsoft YaHei` (`msyh.ttc`) fallback `simhei.ttf`, `simsun.ttc`.
- Chinese bold: `msyhbd.ttc`, fallback `simhei.ttf`.
- Mono/date: `consolab.ttf`, fallback `consola.ttf`.
- Main title: `55-58`, bold, black, 2-3 lines.
- Section title: `28`, bold, black with a red vertical bar.
- Today judgment body: `26-29`, bold, black.
- Footer title: `28`, bold, white.
- Footer subtitle: `23`, white.

## Header

Use this fixed structure:

- Top-left brand: `AI行业判断笔记`, red, bold 28.
- Top-right date: `YYYY.MM.DD`, mono/bold 22, muted.
- Badge: red rounded pill, white text, 22 bold. 06-02 allowed a white badge with red text, but red badge is the stable default.
- Subtitle: muted bold 23.
- Icon: red rounded square target mark at about `(920, 252)`, size `148`.

Use the target logo by default. Avoid decorative or brand-colored icons unless the user explicitly requests.

## Standard Content Pattern

The content should fit this rhythm:

1. Title area.
2. `今天的判断` card:
   - Full width.
   - Fill `RED_SOFT`.
   - Outline `RED`, width `3`.
   - Radius `24`.
3. Evidence or framework section:
   - Section title uses red vertical bar.
   - Cards use white or pale fill, red/line outlines.
4. Red core judgment card:
   - Fill `RED`.
   - White text.
   - 1 eyebrow + 1-2 bold lines.
5. Support modules:
   - Numbered rows, two-column cards, stats, or material anchors.
6. Final action/question:
   - White card with red outline, or numbered prompt list.

## Components

### Section Title

`draw.rectangle((x, y + 13, x + 8, y + 46), fill=RED)` plus title text at `(x + 20, y)`.

### Stat Card

Use for hard numbers:

- Two columns.
- Big number red `37-42`.
- Label black bold `22-24`.
- Note muted `19`.

### Layer Row

Use for process/layer decomposition:

- Full-width pale row, height `88-94`.
- Red circle number on left.
- Title red dark.
- Explanation black.

### Two-Column Cards

Use for frameworks with 4 items or comparisons with 2 items:

- White fill.
- Line outline.
- Red dark title.
- Black text.

### Anchor List

Use for source/material anchors:

- Full-width pale row, height around `82`.
- Left title red dark.
- Right one-sentence evidence.

### Red Callout

Must appear once:

- Full-width red box.
- Eyebrow `核心判断` or equivalent.
- 1-2 concise white bold lines.

### Prompt List

Use for final reusable action:

- Full-width white card, red outline.
- Red numbered circles.
- 2-3 short questions/actions.

## Content Rules

- Image title should be a judgment, not a neutral topic label.
- `今天的判断` must compress the whole argument into one sentence.
- Each module should have one job: evidence, decomposition, comparison, or action.
- Avoid more than five modules. If content does not fit, reduce text.
- Prefer concrete numbers and nouns. Avoid long paragraphs.

## Drift Warnings

These choices are outside the baseline style:

- Black footer.
- Topic-color top bars.
- Green/blue/yellow card systems.
- Too many pills or dashboard elements.
- Icons replacing the target mark without a strong reason.
- Hero title inside a colored card.
- Full-body article copy on the image.
