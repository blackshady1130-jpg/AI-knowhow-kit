# BOOKMARKS_RETRIEVAL

版本：v0.1  
更新日期：2026-03-14  
适用范围：Cursor / Claude Code / Codex / 通用 Agent

## 1) 触发条件

当用户问题满足任一条件时触发：

- 需要补充 AI 行业资料、案例、原始出处
- 需要更广覆盖的行业文章召回（而非仅高信号精选）
- 需要给 AI 观点增加外部佐证

若问题是“高强度判断/战略优先级”，优先先走 `AI_SCAN_RETRIEVAL.md`。

## 2) 数据资产

- `bookmarks/bookmarks_keywords.jsonl`：主索引（唯一检索入口）
- `bookmarks/bookmarks_md/*.md`：证据原文
- 原始运营底表（xlsx）由维护者本地保管，非默认检索入口。

## 3) 检索顺序（必须遵守）

1. 在 `bookmarks_keywords.jsonl` 进行候选召回（关键词/标题/summary/domain）。  
2. 按 `quality_tier` 与相关性筛选候选（默认优先 A/B）。  
3. 必要时仅打开目标 `bookmarks_md` 定向取证。  
4. 输出 `结论 -> 证据 -> 边界 -> 下一步`，附 `id/title/url`。  

## 4) 回答约束

### 必须做到

- 标注信息来源（`id/title/url`）
- 区分事实与推断
- 说明样本与时效边界

### 明确禁止

- 全量通读全部 `bookmarks_md` 后再回答
- 仅列链接，不给结论与判断
- 用低质量条目替代高质量证据

## 5) 与 AI_SCAN 的协同规则

- 深判断场景：先 `AI_SCAN`，后 `BOOKMARKS` 补证  
- 资料铺垫场景：先 `BOOKMARKS`，再 `AI_SCAN` 做判断锚定  
- 最终输出统一结构，避免双库结论冲突
