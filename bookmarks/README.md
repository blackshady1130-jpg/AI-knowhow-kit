# bookmarks 数据说明

版本：v0.1  
更新日期：2026-03-14

## 目录结构

- `bookmarks_keywords.jsonl`：唯一主索引（检索入口）
- `bookmarks_md/*.md`：原文证据
- `_source/AGI_bookmarks_WITH_NEW_SUMMARIES.xlsx`：原始运营底表
- `_source/AGI_bookmarks_WITH_NEW_SUMMARIES.llm.xlsx`：含 LLM关键词与补标题结果的增强底表

## 检索约定

- 默认先查 `bookmarks_keywords.jsonl`，再按需读取 `bookmarks_md`。
- `md_path` 必须使用相对路径：`bookmarks_md/...`。
- 回答应附 `id/title/url`，保证可追溯。

## 质量分层建议

- `quality_tier=A/B`：默认优先召回
- `quality_tier=C`：作为低优先补充候选
