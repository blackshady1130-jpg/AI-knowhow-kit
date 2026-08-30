# Site Data Sync Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 Notes #415–#424、README 状态和站点时间口径同步到 2026-08-30，同时保持七篇主题文章正文不变。

**Architecture:** `notes/AI行业扫描_keywords.jsonl` 仍是 Notes 内容源，`site/topic_assignments.json` 提供分类，`site/build_data.py` 生成 `site/data.json`。文章复核日期进入 `site/topics.json`，前端分别读取 `topic.review_updated_at` 和 `D.meta.generated_at`，避免把数据生成日期写成文章更新时间。

**Tech Stack:** Python 3 标准库、JavaScript、JSON、Python `unittest`、静态 GitHub Pages。

## Global Constraints

- 只执行已确认的第 1 步，不发布。
- 不修改 `site/reviews/*.md`、Notes 原文、页面布局或发布工作流。
- 新增文案使用直白的“网页版阅读”“Notes 更新于”“文章复核”“Notes 同步”。
- `site/data.json` 只能通过 `python site/build_data.py` 生成。

---

### Task 1: 锁定数据和时间口径

**Files:**
- Modify: `tests/test_site_contract.py`
- Test: `tests/test_site_contract.py`

**Interfaces:**
- Consumes: `README.md`、`site/topics.json`、`site/topic_assignments.json`、`site/js/app.js`。
- Produces: README 状态、#415–#424 分类和双时间标签的契约测试。

- [ ] **Step 1: 写入失败测试**

新增三组断言：README 必须包含 `424 条` 和站点链接且不含 `截至 2026-08-02`；#415–#424 必须全部分类；每个 topic 必须有 `YYYY-MM-DD` 格式的 `review_updated_at`，前端必须显示 `文章复核`、`Notes 同步`、`Notes 更新于`。

- [ ] **Step 2: 运行测试并确认 RED**

Run: `python -m unittest tests.test_site_contract.SiteRepositoryStatusContractTests tests.test_site_contract.SiteDataContractTests.test_new_notes_415_to_424_are_classified tests.test_site_contract.TopicMetadataContractTests.test_topics_record_article_review_date tests.test_site_contract.SitePageContractTests.test_page_distinguishes_review_and_notes_freshness -v`

Expected: FAIL，因为 README、分类、`review_updated_at` 和前端标签尚未更新。

- [ ] **Step 3: 提交测试**

Run: `git add tests/test_site_contract.py && git commit -m "test: define site sync freshness contract"`

### Task 2: 同步 README 与 Notes 分类

**Files:**
- Modify: `README.md`
- Modify: `site/topic_assignments.json`

**Interfaces:**
- Consumes: `notes/AI行业扫描_keywords.jsonl` 中 #415–#424。
- Produces: 424 条 Notes 的完整分类和当前公开索引说明。

- [ ] **Step 1: 更新 README**

将“截至 2026-08-02”改为“当前公开索引（更新至 2026-08）：”，将 Notes 数量改为 424，并在仓库简介后增加公开站点链接。

- [ ] **Step 2: 添加 #415–#424 分类**

按设计文档中的分类表追加十个键，保持每条一至三个主题且仅使用七个既有主题名。

- [ ] **Step 3: 运行对应测试**

Run: `python -m unittest tests.test_site_contract.SiteRepositoryStatusContractTests tests.test_site_contract.SiteDataContractTests.test_new_notes_415_to_424_are_classified tests.test_site_contract.SiteDataContractTests.test_all_source_notes_have_one_to_three_valid_topic_assignments -v`

Expected: PASS。

### Task 3: 分开文章复核与 Notes 同步时间

**Files:**
- Modify: `site/topics.json`
- Modify: `site/js/app.js`
- Generated: `site/data.json`

**Interfaces:**
- Consumes: topic 字段 `review_updated_at: string`、bundle 字段 `meta.generated_at: string`。
- Produces: 文章页元信息 `文章复核 <date> · Notes 同步 <date>`，页脚 `Notes 更新于 <date>`。

- [ ] **Step 1: 添加文章复核日期**

为七个 topic 添加 `"review_updated_at": "2026-08-02"`。

- [ ] **Step 2: 修改状态文案**

将页脚赋值改为 `$('footerUpdated').textContent = 'Notes 更新于 ' + D.meta.generated_at;`；将文章元信息改为拼接 `文章复核`、`topic.review_updated_at`、`Notes 同步`、`D.meta.generated_at`。

- [ ] **Step 3: 重建站点数据**

Run: `python site/build_data.py`

Expected: `Wrote site\\data.json (424 notes, 7 topics)`。

- [ ] **Step 4: 运行对应测试**

Run: `python -m unittest tests.test_site_contract.TopicMetadataContractTests.test_topics_record_article_review_date tests.test_site_contract.SitePageContractTests.test_page_distinguishes_review_and_notes_freshness tests.test_site_contract.SiteDataContractTests.test_generated_bundle_contains_all_notes_and_preserves_authored_why -v`

Expected: PASS。

### Task 4: 完整校验和候选交付

**Files:**
- Verify only: `site/reviews/*.md`
- Verify: all modified files

**Interfaces:**
- Consumes: 本分支全部差异。
- Produces: 可供用户检查、未合并、未发布的候选分支。

- [ ] **Step 1: 运行完整测试与语法检查**

Run: `python -m unittest discover -s tests -v`

Run: `node --check site/js/app.js`

Run: `git diff --check`

Expected: 全部通过且无 whitespace error。

- [ ] **Step 2: 核对数据事实**

确认源数据和 bundle 均为 424 条、最大 ID 为 424、完整 `why` 总字符数一致、2026-08 为 37 条、十条新增 Notes 无字段丢失。

- [ ] **Step 3: 核对边界与文案**

确认 `git diff -- site/reviews` 为空；运行 `audit-text.mjs` 检查本轮新增 README/UI 文案并人工判断命中项；本地打开桌面和手机页面核对 424 条、最新 #424 和两类时间标签。

- [ ] **Step 4: 提交候选改动**

只暂存 `README.md`、`site/topic_assignments.json`、`site/topics.json`、`site/js/app.js`、`site/data.json`、`tests/test_site_contract.py` 和本方案文档，提交后等待用户检查，不 merge、不 push。
