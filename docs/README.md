# Agent Profile Kit (v0.3)

这是一套给多种 AI 工具复用的个人记忆/协作资料包，目标是：

1. 减少重复沟通成本。
2. 让不同工具输出风格更一致。
3. 提高首稿可用率，降低反复改写轮次。

## 文件结构

### 运行时（Agent 默认加载）

- `PROFILE_CORE.md`：稳定画像
- `WORKING_PREFERENCES.md`：协作偏好
- `DOMAIN_KNOWHOW.md`：行业认知与判断框架
- `STYLE_GUIDE.md`：文风规则

### 入口（工具接线）

- `AGENTS.md`：通用 Agent 入口
- `CLAUDE.md`：Claude Code 入口
- `CURSOR.md`：Cursor 入口

### 检索协议（按需触发）

- `AI_SCAN_RETRIEVAL.md`：AI 行业扫描检索协议（含双库协同）
- `BOOKMARKS_RETRIEVAL.md`：bookmarks 检索协议

### 知识库

- `notes/`：AI 行业扫描（keywords.jsonl + md 原文）
- `bookmarks/`：收藏资料（keywords.jsonl + md 原文）
- `skills/`：可复用 skill 原型（高频任务模块）

### 治理层（`docs/` 目录，不默认加载）

- `docs/EVIDENCE_INDEX.md`：证据索引
- `docs/MAINTENANCE.md`：月度维护流程
- `docs/WEB_PROMPT_SNIPPETS.md`：ChatGPT/Gemini 粘贴模版
- `docs/sources/`：审计用 JSON 证据文件
- `docs/scripts/`：部署辅助脚本

## 数据来源

- 博客：5 篇（`md + docx`）
- AI 分析表：184 条有效记录
- ChatGPT 历史：371 个会话，1305 条用户消息
- 审计文件：`docs/sources/*.json`

## 使用建议

1. 工具入口文件保持短（只放"行为约束"和"引用关系"）。
2. 核心内容写在 4 个 core 文件中，入口文件不要重复拷贝。
3. 先用 2-4 周，再按真实使用反馈更新一次。
4. 遇到"身份冲突/场景化表达"时，以 `PROFILE_CORE.md` 的高置信条目为准。
