# 月度更新 SOP

版本：v0.1  
更新日期：2026-03-15  
执行人：用户本人或其授权的 Agent

## 1) 更新范围

每月更新只涉及**知识库层**，不涉及核心画像文件。

| 更新对象 | 索引文件 | 原文目录 |
|---|---|---|
| AI 行业扫描 | `notes/AI行业扫描_keywords.jsonl` | `notes/AI行业扫描_md/` |
| Bookmarks | `bookmarks/bookmarks_keywords.jsonl` | `bookmarks/bookmarks_md/` |

> 注：如果你习惯使用 xlsx 做运营视图，可在本地维护底表，但 xlsx 不纳入公开版本。

核心画像文件（`PROFILE_CORE.md`、`WORKING_PREFERENCES.md`、`DOMAIN_KNOWHOW.md`、`STYLE_GUIDE.md`）仅在认知发生重大变化时更新，不纳入月度流程。

## 2) 前置准备

执行月更前，确认以下材料已就绪：

- [ ] 当月新增的 AI 行业扫描条目（含标题、原文链接、你的判读 `why`、原文内容）
- [ ] 当月新增的书签收藏（含标题、链接、一句话总结、原文内容）
- [ ] 原文已转为 Markdown 格式（可通过浏览器插件、url-to-markdown 等工具完成）

## 3) AI 行业扫描更新步骤

### Step 3.1：确定新增条目的 id

读取 `notes/AI行业扫描_keywords.jsonl` 最后一行，获取当前最大 `id`，新条目从 `max_id + 1` 开始递增。

### Step 3.2：保存原文 md

将每条新增的原文保存到 `notes/AI行业扫描_md/`，命名规则：

```
{id}_{标题关键词缩写}.md
```

示例：`188_Agent记忆架构实践.md`

md 文件顶部建议包含 YAML front matter：

```yaml
---
url: "原文链接"
title: "原文标题"
captured_at: "抓取时间"
---
```

### Step 3.3：追加 jsonl 索引

在 `notes/AI行业扫描_keywords.jsonl` 末尾追加 JSON 行，每行一条，字段要求：

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | 是 | 递增整数 |
| `date` | 是 | 收录日期，格式 `YYYY-MM-DD` |
| `type` | 是 | `观点/文章` / `行业动态/评价` / `solid paper` |
| `title` | 是 | 原文标题 |
| `why` | 是 | **你的判读理由**（为什么值得收录、核心观点是什么） |
| `url` | 是 | 原文链接 |
| `md_path` | 是 | 相对路径数组，如 `["AI行业扫描_md/188_xxx.md"]` |
| `keywords` | 是 | 3-8 个有区分度的关键词数组 |

模板：

```json
{"id": 188, "date": "2026-04-01", "type": "观点/文章", "title": "文章标题", "why": "你的判读理由，越具体越好", "url": "https://example.com/article", "md_path": ["AI行业扫描_md/188_文章标题缩写.md"], "keywords": ["关键词1", "关键词2", "关键词3"]}
```

### Step 3.4：`why` 字段撰写规范

`why` 是整个知识库最有价值的字段——它承载你的判断而非信息搬运。撰写要求：

1. 不低于 2 句话
2. 第一句说"这篇讲了什么 / 核心发现是什么"
3. 第二句说"对我们的启发 / 与已有认知的关系 / 适用边界"
4. 如果有明确局限，补一句边界说明

反面案例（禁止）：`"不错的文章，值得看"`  
正面案例：`"指出当前AI产品的核心矛盾：模型能力突飞猛进但用户体验严重滞后。对比Claude、Gemini和ChatGPT，揭示错位源于产品设计思路陈旧和大公司组织结构掣肘。与我们对'评测高分不等于好产品'的判断一致"`

## 4) Bookmarks 更新步骤

### Step 4.1：确定新增条目的 id

读取 `bookmarks/bookmarks_keywords.jsonl` 最后一行，获取当前最大 `id`（格式 `bm-000xxx`），新条目递增。

### Step 4.2：保存原文 md

保存到 `bookmarks/bookmarks_md/`，命名规则：

```
{序号}_{标题关键词缩写}.md
```

示例：`0710_AgentRuntime设计模式.md`

### Step 4.3：追加 jsonl 索引

在 `bookmarks/bookmarks_keywords.jsonl` 末尾追加 JSON 行，字段要求：

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | 是 | 格式 `bm-000xxx`，递增 |
| `title` | 是 | 标题 |
| `url` | 是 | 原文链接 |
| `summary` | 是 | 一句话总结（30-80 字） |
| `llm_keywords` | 是 | 5-8 个关键词数组 |
| `quality` | 是 | `高质量` / `良好` / `中等` / `较短` |
| `quality_tier` | 是 | `A`（高质量）/ `B`（良好）/ `C`（中等+较短） |
| `retrieval_weight` | 是 | A=1.0 / B=0.85 / C=0.6 |
| `status` | 是 | `active` |
| `domain` | 是 | 来源域名 |
| `md_path` | 是 | 相对路径 `bookmarks_md/xxx.md` |
| `updated_at` | 是 | 更新日期 `YYYY-MM-DD` |
| `tags_raw` | 否 | 原始标签字符串 |
| `char_count` | 否 | md 文件字符数 |
| `review_note` | 否 | 内容完整性备注 |

模板：

```json
{"id": "bm-000710", "title": "文章标题", "url": "https://example.com", "summary": "一句话总结", "tags_raw": "Tag1|Tag2", "llm_keywords": ["词1", "词2", "词3", "词4", "词5"], "quality": "高质量", "quality_tier": "A", "retrieval_weight": 1.0, "status": "active", "domain": "example.com", "md_path": "bookmarks_md/0710_标题缩写.md", "char_count": 15000, "review_note": "内容完整", "updated_at": "2026-04-15"}
```

### Step 4.4：质量评级标准

| 等级 | quality_tier | 判断依据 |
|---|---|---|
| 高质量 | A | 原创深度分析、有数据/实验支撑、观点密度高 |
| 良好 | B | 信息整合扎实、有清晰框架、值得回查 |
| 中等 | C | 信息有用但密度一般，或篇幅较短 |
| 较短 | C | 内容过少，仅作补充参考 |

## 5) 校验清单

每次更新完成后，执行以下检查：

### 5.1 条目计数一致性

```
jsonl 行数 == 对应 md 目录中的文件数（允许 jsonl ≤ md，不允许 jsonl > md）
```

### 5.2 路径可达性

遍历 jsonl 中每条 `md_path`，确认对应文件存在。

### 5.3 无绝对路径

jsonl 中不得出现 `C:\`、`D:\`、`/Users/` 等硬编码绝对路径。

### 5.4 字段完整性

每条新增记录的必填字段不为空。

### 5.5 关键词区分度

新增条目的 `keywords` / `llm_keywords` 不应全是泛化词（如"AI"、"模型"），至少包含 2 个与该文章主题强相关的特异性词。

## 6) 抽样回归验证

用以下 5 类问题测试检索可用性，确认新增条目可被命中：

1. 公司/竞争格局类："OpenAI/Anthropic/Google 最近有什么动作？"
2. 模型能力类："最近有什么关于训练范式的新发现？"
3. Agent/工程类："Agent 工程化最近有什么新实践？"
4. 评测类："评测方法论有什么新进展？"
5. 商业/SaaS 类："SaaS 受 AI 冲击的最新分析？"

验收标准：回答能引用到当月新增条目的 `id/title/url`。

## 7) 运营底表同步（可选）

如果你习惯先在 xlsx 中维护，更新完 jsonl 和 md 后，记得同步更新本地的 xlsx 底表。xlsx 是你的人工运营视图，jsonl 是 Agent 的检索入口，两者保持一致。

> 注：xlsx 底表属于个人运营文件，不纳入公开仓库。

## 8) 可自动化环节

以下环节可以让 Agent 辅助完成：

| 环节 | 自动化方式 | 说明 |
|---|---|---|
| 原文转 md | url-to-markdown 工具或 Agent 抓取 | 批量执行 |
| jsonl 追加行生成 | 根据 md 内容 + 你给的 title/url 自动填充 | `summary`、`llm_keywords`、`char_count` 可自动生成 |
| 路径校验 | 脚本遍历 jsonl → 检查文件存在性 | 全自动 |
| 关键词提取 | LLM 读取 md 后生成 | 需要你审核确认 |

**不可自动化**：`why` 字段（AI 行业扫描）和 `quality_tier` 评级——这是你的判断，是知识库的核心价值。

## 9) 时间线建议

| 时间点 | 动作 | 预计耗时 |
|---|---|---|
| 每月 25-30 日 | 整理当月新增条目清单、撰写 why | 30-60 分钟 |
| 同日 | 让 Agent 执行：转 md → 生成 jsonl → 追加 → 校验 | 15-30 分钟 |
| 同日 | 抽样回归验证 | 5 分钟 |

## 10) 核心画像文件何时更新

以下情况才需要动核心文件：

- 你换了公司或业务方向 → 更新 `PROFILE_CORE.md`
- 你的输出偏好发生系统性变化 → 更新 `WORKING_PREFERENCES.md`
- 你对某个领域形成了新的判断框架 → 更新 `DOMAIN_KNOWHOW.md`
- 你的写作风格有意调整 → 更新 `STYLE_GUIDE.md`

预期频率：每季度检视一次即可。
