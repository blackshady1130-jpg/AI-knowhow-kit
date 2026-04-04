# AI Knowhow Kit

一套可跨 AI 工具复用的**个人知识与协作规范包**。

让 Cursor、Claude Code、Codex、ChatGPT、Gemini、Manus 等不同 AI Agent 在第一轮对话就理解你是谁、怎么工作、怎么输出——减少重复沟通，提高首稿可用率。

## 这是什么

大多数人使用 AI 工具时都在反复解释同样的事情：我要什么风格、我的背景是什么、我偏好什么结构。

这个仓库是一种解决方案：把你的**稳定画像、协作偏好、行业认知、文风规则**结构化沉淀，让任何 AI 工具都能即时加载，像一个了解你多年的助手一样工作。

核心理念：
- **写一次，处处生效**：同一套规则文件适配 Cursor / Claude Code / Codex / ChatGPT / Manus
- **分层架构**：核心画像与工具入口分离，更新画像不需要改每个工具的配置
- **知识库可检索**：行业观察和收藏资料以索引 + 原文的结构存储，Agent 按需召回而非全量加载

## 目录结构

```
AI_knowhow_kit/
│
│  # 核心画像层（Agent 运行时加载）
├── PROFILE_CORE.md              你是谁、在做什么、能力边界
├── WORKING_PREFERENCES.md       协作偏好与输出合同
├── DOMAIN_KNOWHOW.md            行业认知与判断框架
├── STYLE_GUIDE.md               文风规则与改写操作规程
│
│  # 入口路由层（不同工具的接线器）
├── AGENTS.md                    通用 Agent 入口
├── CLAUDE.md                    Claude Code 入口
├── CURSOR.md                    Cursor 入口
│
│  # 检索协议层（知识库使用规则）
├── AI_SCAN_RETRIEVAL.md         行业扫描检索协议（含双库协同）
├── BOOKMARKS_RETRIEVAL.md       收藏资料检索协议
├── USAGE_SOP.md                 文件分层速查与 Skill 指引
│
│  # 知识库层
├── notes/                       AI 行业扫描（索引 + 原文）
├── bookmarks/                   收藏资料（索引 + 原文）
├── skills/                      可复用任务模板
│   ├── ppt-onepager-writer/     汇报一页文案生成
│   ├── eval-conclusion-builder/ 评测结论与对比分析
│   └── model-collab-kickoff/    业务-模型合作方案
│
│  # 参考文档
└── docs/
    ├── README.md                    项目内部说明
    ├── MONTHLY_UPDATE_SOP.md        月度更新流程
    ├── RETRIEVAL_QUALITY_GUIDE.md   检索质量分与权重设计说明
    ├── MAINTENANCE.md               维护规范
    ├── WEB_PROMPT_SNIPPETS.md       ChatGPT/Gemini 粘贴模板
    └── EVIDENCE_INDEX.md            证据索引
```

## 快速开始

### Cursor

1. 在你的项目根目录创建 `.cursorrules`，内容指向本仓库的核心文件：

```
Read and follow:
1. AI_knowhow_kit/CURSOR.md
2. AI_knowhow_kit/PROFILE_CORE.md
3. AI_knowhow_kit/WORKING_PREFERENCES.md
4. AI_knowhow_kit/DOMAIN_KNOWHOW.md
5. AI_knowhow_kit/STYLE_GUIDE.md
```

2. 开新对话，输入：`请用 3 行总结我的输出偏好，并按该偏好给一个汇报标题。`

### Claude Code

在项目根目录放置 `CLAUDE.md`，指向核心文件即可。

### ChatGPT / Gemini 网页版

每次开新对话粘贴 `docs/WEB_PROMPT_SNIPPETS.md` 中的"通用短版"（6 行）。

## 知识库检索机制

本仓库包含两个可检索知识库：

| 知识库 | 定位 | 规模 |
|---|---|---|
| `notes/`（AI 行业扫描） | 高信号精选 + 个人判读 | 224 条 |
| `bookmarks/`（收藏资料） | 广覆盖 + 原文存档 | 728 条 |

每个知识库采用**索引 + 原文**结构：

1. **主索引**（jsonl）：Agent 检索入口，含关键词、摘要、质量分级
2. **原文**（md）：证据原文，按需调用

> 维护者在本地可另行保留运营底表（xlsx），用于人工筛选和批量更新，但不包含在本仓库中。

Agent 的检索流程是"先查索引 → 筛选候选 → 定向取证"，而非全量通读。质量分级与权重设计详见 `docs/RETRIEVAL_QUALITY_GUIDE.md`。

## 如何定制成你自己的

这个仓库是一个**活的模板**。建议按以下步骤定制：

1. **改 `PROFILE_CORE.md`**：写上你的职业定位、能力边界、长期目标
2. **改 `WORKING_PREFERENCES.md`**：定义你的输出偏好（先结论还是先过程？结构化还是叙事？）
3. **改 `DOMAIN_KNOWHOW.md`**：沉淀你的行业判断框架和方法论
4. **改 `STYLE_GUIDE.md`**：定义你的文风（禁忌词、句式偏好、改写规则）
5. **替换知识库**：用你自己的行业观察和收藏资料替换 `notes/` 和 `bookmarks/`
6. **按需增减 Skills**：根据你的高频任务创建或修改 `skills/` 下的模板

核心原则：**入口文件保持薄（只做引用），内容集中在 4 个核心文件中**。

## 维护节奏

- **知识库**：每月按 `docs/MONTHLY_UPDATE_SOP.md` 追加新条目
- **核心画像**：每季度检视一次，认知有重大变化时更新
- **入口文件**：基本不动，除非切换工具

## 设计哲学

- 结论先行，不做信息搬运
- 区分事实与推断，标注边界
- 给可执行产物，不给空泛建议
- 克制专业，拒绝讨好式表达

## License

[CC BY-SA 4.0](LICENSE) — 自由使用、修改和分享，需注明出处并以相同许可证发布衍生作品。
