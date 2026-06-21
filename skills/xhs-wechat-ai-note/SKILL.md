---
name: xhs-wechat-ai-note
description: Create Xiaohongshu and WeChat public-account assets for AI行业判断笔记, including red-white-black long cover images and platform-specific copy. Use when Codex needs to turn an AI industry note, article, benchmark, model release, agent/eval/MaaS topic, or user short comment into a public-facing post image, title, body copy, caption, or publishing draft.
---

# XHS / WeChat AI Note

Use this skill for public-facing「AI行业判断笔记」outputs. The goal is not to move information around; the goal is to compress one source or note into a reusable judgment.

## Output Modes

Choose the mode requested by the user:

| Mode | Output |
|---|---|
| `cover` | 1080 x 1920 long image in the fixed red-white-black knowledge-card style |
| `copy` | Xiaohongshu caption, WeChat article draft, or both |
| `cover_and_copy` | Visual spec + rendered cover + platform copy |

## Public-Safe Rules

- Treat the output as public unless the user explicitly says it is internal.
- Remove current company names, internal org names, private context, and unverified internal numbers.
- Keep personal judgment and mechanism analysis, but do not expose private reasoning chains.
- Do not write marketing fluff. Keep concrete objects, mechanisms, numbers, and boundaries.

## Cover Workflow

1. Read `references/standard_style.md` before rendering a cover.
2. Start from `assets/template_spec.json`.
3. Convert the note into a compact visual spec:
   - `title_lines`: 2-3 short title lines.
   - `badge`: topic label.
   - `subtitle`: one short framing sentence.
   - `today_judgment`: one sentence under 45 Chinese characters if possible.
   - `sections`: 3-5 modules.
   - final question/action/checklist.
4. Render with:

```powershell
python skills\xhs-wechat-ai-note\scripts\render_standard_cover.py --spec path\to\cover_spec.json
```

Use the bundled Codex Python runtime if the default Python lacks Pillow.

5. Inspect the PNG visually:
   - red-white-black style is obvious at a glance;
   - title and `今天的判断` fit;
   - red `核心判断` card is present;
   - no text touches card edges or footer;
   - the image explains one judgment, not a news wall.

## Copy Workflow

Read `references/copy_style.md` when writing platform copy.

Default copy structure:

```text
标题：一句判断，不是资讯标题
开头：发生了什么，1-2 句
判断：为什么重要，2-4 点
边界：哪些部分不能过度外推
结尾：一个可复用问题/检查清单
```

Platform differences:

- Xiaohongshu: shorter, sharper, more suitable for image-text browsing; title and first 3 lines must carry the judgment.
- WeChat: more complete context, clearer evidence chain, can include section headings and a slightly longer reasoning path.

## Content Rules

- Write one main judgment per post.
- Do not create an information wall.
- Keep concrete nouns and verbs.
- Prefer “这说明什么 / 怎么验证 / 对谁有用” over broad industry adjectives.
- Keep uncertainty as boundary, not as vague language everywhere.
- If the source is a community post, interview, or secondary interpretation, say so clearly.

## Deliverable

For `cover`, return the PNG path and spec path.  
For `copy`, return platform-labeled copy blocks.  
For `cover_and_copy`, return both and note any public-safety edits made.
