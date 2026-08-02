# AI Knowhow Kit

一套面向 AI 工具和 AI Agent 的个人知识、工作偏好、行业判断与任务模板库。

这个仓库的目标不是做一个普通资料夹，而是把稳定的个人画像、协作规则、行业知识库和可复用工作流整理成结构化上下文，让 Cursor、Claude Code、Codex、ChatGPT、Gemini、Manus 等工具能更快理解：

- 你是谁，正在做什么；
- 你偏好怎样的协作方式和输出格式；
- 你如何判断 AI 行业信息、产品、模型和商业机会；
- 哪些 notes、bookmarks、skills 可以在任务中被检索和复用。

## 当前状态

截至 2026-08-02：

| 模块 | 内容 | 规模 |
|---|---|---:|
| `notes/` | AI 行业扫描，偏高信号判断和深度笔记 | 387 条 |
| `bookmarks/` | AI 相关收藏资料，偏广覆盖和原文归档 | 861 条 |
| `skills/` | 可复用任务工作流与生成模板 | 6 个 |

## 目录结构

```text
AI_knowhow_kit/
├─ PROFILE_CORE.md              # 个人定位、长期目标、能力边界
├─ WORKING_PREFERENCES.md       # 协作偏好、输出标准、交付习惯
├─ DOMAIN_KNOWHOW.md            # AI 行业判断框架、主题地图、研究方法
├─ STYLE_GUIDE.md               # 写作风格、表达规则、改写标准
├─ AGENTS.md                    # 通用 Agent 入口
├─ CLAUDE.md                    # Claude Code 入口
├─ CURSOR.md                    # Cursor 入口
├─ AI_SCAN_RETRIEVAL.md         # notes 检索协议
├─ BOOKMARKS_RETRIEVAL.md       # bookmarks 检索协议
├─ USAGE_SOP.md                 # 使用和维护 SOP
├─ notes/                       # AI 行业扫描索引和 markdown 原文
├─ bookmarks/                   # 书签索引和 markdown 原文
├─ skills/                      # 任务型 skill 模板
├─ docs/                        # 维护、质量、证据和网页端提示词文档
└─ site/                        # GitHub Pages / 站点相关内容
```

## 核心文件

| 文件 | 作用 |
|---|---|
| `PROFILE_CORE.md` | 定义个人背景、能力边界、正在做的事情和长期方向。 |
| `WORKING_PREFERENCES.md` | 定义协作方式、交付标准、任务推进方式和质量偏好。 |
| `DOMAIN_KNOWHOW.md` | 定义 AI 行业分析框架、主题判断、检索关键词和研究边界。 |
| `STYLE_GUIDE.md` | 定义写作风格、表达禁忌、改写规则和公开输出标准。 |

入口文件如 `AGENTS.md`、`CLAUDE.md`、`CURSOR.md` 应保持轻量，主要负责指向核心文件，而不是复制大量内容。

## 知识库机制

`notes/` 和 `bookmarks/` 都采用“索引 + 原文”的结构：

- `*_keywords.jsonl` 是 Agent 的检索入口，包含标题、来源、关键词、摘要、质量判断和 markdown 路径。
- `*_md/` 保存对应 markdown 原文或整理稿，用于需要证据、引用和上下文时再读取。

推荐检索顺序：

1. 先读 `AI_SCAN_RETRIEVAL.md` 和 `BOOKMARKS_RETRIEVAL.md`。
2. 先查 JSONL 索引，按关键词、主题、质量和时间筛选候选。
3. 再打开少量相关 markdown 原文取证。
4. 不要默认全量读取整个知识库。

## Skills

当前 `skills/` 下包含 6 个可复用工作流：

| Skill | 用途 |
|---|---|
| `ai-industry-intel` | 从 notes、bookmarks 和公开源生成 AI 行业情报摘要、来源地图和推荐清单。 |
| `ppt-html-style` | 生成 16:9、浏览器可播放的策略报告风格 HTML slide deck。 |
| `xhs-wechat-ai-note` | 生成小红书/公众号风格的 AI 行业判断笔记封面与文案。 |
| `ppt-onepager-writer` | 生成汇报型一页纸文案。 |
| `eval-conclusion-builder` | 生成评测结论、对比分析和边界判断。 |
| `model-collab-kickoff` | 生成业务和模型合作的启动方案。 |

使用 skill 前应先阅读对应目录下的 `SKILL.md`，再按其中的脚本、参考资料和交付要求执行。

## 快速使用

### Cursor

在目标项目中创建 `.cursorrules` 或等价入口，指向本仓库核心文件：

```text
Read and follow:
1. AI_knowhow_kit/CURSOR.md
2. AI_knowhow_kit/PROFILE_CORE.md
3. AI_knowhow_kit/WORKING_PREFERENCES.md
4. AI_knowhow_kit/DOMAIN_KNOWHOW.md
5. AI_knowhow_kit/STYLE_GUIDE.md
```

### Claude Code

在项目根目录放置或引用 `CLAUDE.md`，并让它加载本仓库的核心画像和协作偏好文件。

### Codex / 通用 Agent

优先读取 `AGENTS.md`，再按任务需要加载核心文件、检索协议或具体 skill。

### ChatGPT / Gemini 网页版

使用 `docs/WEB_PROMPT_SNIPPETS.md` 中的短版提示词，把核心偏好和任务约束粘贴到新对话。

## 维护规则

- 核心画像文件按季度或重大认知变化更新。
- `notes/` 和 `bookmarks/` 更新时，必须保证 JSONL 索引和 markdown 路径一致。
- 更新关键词时，优先保证稳定概念可检索，例如 `Agent Infra`、`harness`、`verifier`、`FDE`、`token economics`、`RLVR`、`OPD`。
- `.tmp/`、运营底表、源抓取缓存、本地密钥和大体积中间产物不进入公开仓库。
- 公开提交前至少检查：无缺失 `md_path`、无 `Content fetch failed` 占位、无签名 URL 或 secret。

## 设计原则

- 结论先行，但保留证据和边界。
- 区分事实、判断和推断。
- 优先沉淀可复用框架，而不是一次性信息搬运。
- 入口轻量，知识集中，按需检索。
- 用结构降低重复沟通成本，让 Agent 更快进入有效协作。

## License

[CC BY-SA 4.0](LICENSE)
