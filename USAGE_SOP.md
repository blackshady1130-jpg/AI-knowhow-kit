# USAGE_SOP

版本：v0.2（精简版）  
更新日期：2026-03-15

## 1) 文件分层速查

运行时文件（Agent 默认加载）：

- `PROFILE_CORE.md`
- `WORKING_PREFERENCES.md`
- `DOMAIN_KNOWHOW.md`
- `STYLE_GUIDE.md`

入口文件（工具接线，三选一）：

- `AGENTS.md`（Codex / 通用 Agent）
- `CLAUDE.md`（Claude Code）
- `CURSOR.md`（Cursor）

检索协议（按需触发）：

- `AI_SCAN_RETRIEVAL.md`（AI 行业问题，含双库协同）
- `BOOKMARKS_RETRIEVAL.md`（资料补充/案例扩展）

治理文件（不默认加载，存放于 `docs/`）：

- `docs/EVIDENCE_INDEX.md`
- `docs/MAINTENANCE.md`

## 2) 何时加载证据文件

只有以下三类场景才加载 `docs/EVIDENCE_INDEX.md`：

1. 你质疑某条画像结论是否可靠；
2. 需要"有据可查"的对外材料；
3. 你要更新版本记忆包。

## 3) Skill 化原则

适合做 Skill 的内容：

1. 重复频率高；
2. 结构固定；
3. 有明确输入输出；
4. 需要低偏差执行。

不适合做 Skill 的内容：

1. 个人画像事实库；
2. 长篇背景资料；
3. 低频一次性任务说明。

## 4) 当前可用 Skills

1. `skills/ppt-onepager-writer/SKILL.md`：汇报/PPT 一页文案生成
2. `skills/eval-conclusion-builder/SKILL.md`：评测结论与对比分析
3. `skills/model-collab-kickoff/SKILL.md`：业务-模型合作方案结构化输出

调用方式：在提问开头加 `请按 skill: <skill-name> 执行`。
