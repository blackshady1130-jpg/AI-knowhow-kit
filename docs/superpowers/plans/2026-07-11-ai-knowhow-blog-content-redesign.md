# AI Knowhow Blog Content Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 AI_knowhow_kit 的 GitHub Pages 从七类资料索引升级为“个人主张首页 + 七篇同行深读 + 350 条可追溯 notes 证据层”。

**Architecture:** 保留现有静态单页架构，以 `notes/AI行业扫描_keywords.jsonl` 为内容主索引、`site/topic_assignments.json` 为人工主题映射、`site/topics.json` 与七篇 Markdown 为策展层，最终由 `site/build_data.py` 生成 `site/data.json`。页面继续使用 hash 路由，通过 `review_note_ids` 将综述与证据卡连接起来。

**Tech Stack:** Python 3 标准库、`unittest`、静态 HTML、Tailwind CDN、Marked.js、原生 JavaScript、GitHub Pages。

## Global Constraints

- 所有改动只发生在 `codex/blog-content-redesign` 分支及其 worktree，禁止合并或推送到 `main`。
- 保留 `#home` 与 `#topic/<name>` URL 兼容性。
- 不改写 notes 的 `why/comments` 原文，不新增机器生成标签字段。
- 不引入 npm、前端框架、数据库、CMS、登录或外部运行时依赖。
- 公开文案不写当前公司名、内部业务口径、未核验数字或私有上下文。

---

### Task 1: 建立站点内容契约测试

**Files:**
- Create: `tests/test_site_contract.py`

**Interfaces:**
- Consumes: notes JSONL、topic assignments、topic metadata、reviews、`site/index.html`。
- Produces: `python -m unittest tests.test_site_contract -v` 可执行的内容与页面契约。

- [ ] **Step 1: 写失败测试**

测试必须覆盖：350 条 notes 均有映射；七主题拥有 `chapter/role/question/thesis`；七篇综述拥有五个规定章节并引用 290—350；首页出现核心主张与合作 CTA；页面出现三个 notes 视图、搜索、类型筛选和加载更多控件。

- [ ] **Step 2: 运行测试并确认 RED**

Run: `python -m unittest tests.test_site_contract -v`

Expected: FAIL，至少包含缺失 290—350 映射、topic positioning 字段、首页主张或 notes 浏览控件。

- [ ] **Step 3: 提交测试**

Run: `git add tests/test_site_contract.py && git commit -m "test: define redesigned blog content contract"`

---

### Task 2: 补齐数据映射与生成器

**Files:**
- Modify: `site/topic_assignments.json`
- Modify: `site/build_data.py`
- Modify: `site/data.json`
- Test: `tests/test_site_contract.py`

**Interfaces:**
- Consumes: note IDs 1—350、七篇 review Markdown 中的 `#id`。
- Produces: 每个 topic 的 `review_note_ids: list[int]` 及 350 条完整 site notes。

- [ ] **Step 1: 为 290—350 逐条增加 1—3 个主题映射**

按对象和机制映射，不只按关键词；重点保持 Harness/Eval/Deployment/ROI/治理之间的交叉关系。

- [ ] **Step 2: 扩展生成器**

新增 `extract_review_note_ids(markdown: str) -> list[int]`，使用正则 `#(\d+)` 去重并保持首次出现顺序；构建时验证引用 ID 存在，并写入 topic 数据。

- [ ] **Step 3: 运行数据测试并确认相关项转绿**

Run: `python -m unittest tests.test_site_contract.SiteDataContractTests -v`

Expected: PASS。

- [ ] **Step 4: 重建数据并提交**

Run: `python site/build_data.py`

Expected: `Wrote site/data.json (350 notes, 7 topics)`。

Run: `git add site/topic_assignments.json site/build_data.py site/data.json && git commit -m "feat: publish complete 350-note evidence bundle"`

---

### Task 3: 重写七主题定位元数据

**Files:**
- Modify: `site/topics.json`
- Test: `tests/test_site_contract.py`

**Interfaces:**
- Produces: 每主题 `chapter`、`role`、`question`、`thesis`、精简 `description`。

- [ ] **Step 1: 按规格写入七章角色**

字段必须把七章串入同一主线；AI Coding 标为“高反馈验证场”，行业战略标为“部署与价值捕获层”。

- [ ] **Step 2: 运行主题元数据测试**

Run: `python -m unittest tests.test_site_contract.TopicMetadataContractTests -v`

Expected: PASS。

- [ ] **Step 3: 重建并提交**

Run: `python site/build_data.py`

Run: `git add site/topics.json site/data.json && git commit -m "content: connect seven topics into one research arc"`

---

### Task 4: 重构首页与主题页阅读路径

**Files:**
- Modify: `site/index.html`
- Test: `tests/test_site_contract.py`

**Interfaces:**
- Consumes: topic positioning fields、`review_note_ids`、350 条 notes。
- Produces: 主张首页、研究主线、最近更新、合作区和三视图 notes 浏览器。

- [ ] **Step 1: 重写首页静态结构与首屏文案**

加入核心主张、辅助说明、`#research-arc` 与 `#collaborate` 锚点；CTA 使用“沿研究主线阅读”“浏览 350 条判读”“交流真实工作流”。

- [ ] **Step 2: 重写首页渲染逻辑**

主题卡显示 `chapter/role/question/thesis`；增加六步研究主线和最近六条高密度更新；页脚使用 `D.meta.generated_at`。

- [ ] **Step 3: 实现 notes 三视图**

状态包括 `curNoteView`、`curQuery`、`curType`、`visibleNoteCount`；默认 `cited`，另有 `recent/all`；全部视图每次加载 12 条；搜索匹配 title、why、keywords；类型筛选使用现有三种 type。

- [ ] **Step 4: 运行页面契约测试**

Run: `python -m unittest tests.test_site_contract.SitePageContractTests -v`

Expected: PASS。

- [ ] **Step 5: 提交页面改造**

Run: `git add site/index.html && git commit -m "feat: lead blog with deployment learning thesis"`

---

### Task 5: 优化七篇主题综述

**Files:**
- Modify: `site/reviews/model-training.md`
- Modify: `site/reviews/architecture-engineering.md`
- Modify: `site/reviews/eval-benchmark.md`
- Modify: `site/reviews/ai-coding.md`
- Modify: `site/reviews/product-interaction.md`
- Modify: `site/reviews/industry-strategy.md`
- Modify: `site/reviews/impact-safety.md`
- Modify: `site/data.json`
- Test: `tests/test_site_contract.py`

**Interfaces:**
- Produces: 每篇都含“本章核心判断 / 在研究主线中的位置 / 关键判断 / 2026 年 6—7 月新增观察 / 对实践意味着什么 / 接下来如何证伪”。

- [ ] **Step 1: 优化模型、架构、评测三篇**

重点补入 #290、#297、#299—300、#307—308、#320、#331、#333—334、#336—337、#341、#343、#346—347、#350；保留原有高价值证据与边界。

- [ ] **Step 2: 优化 AI Coding 与产品两篇**

重点补入 #292—296、#303—304、#318—319、#329、#332、#344；突出 Coding 的可验证优势、review/maintenance 成本及向非 Coding 工作流外推的边界。

- [ ] **Step 3: 优化行业战略与影响安全两篇**

重点补入 #291、#293、#298、#310—317、#321—323、#325—328、#335、#338—339、#342、#345、#348—349；把 token/capex、deployment、结果买单和公众接受度连起来。

- [ ] **Step 4: 运行综述契约与引用测试**

Run: `python -m unittest tests.test_site_contract.ReviewContractTests -v`

Expected: PASS，所有 `#id` 均可解析且七篇都有新增引用。

- [ ] **Step 5: 重建并提交**

Run: `python site/build_data.py`

Run: `git add site/reviews site/data.json && git commit -m "content: refresh seven evidence-backed research chapters"`

---

### Task 6: 完整验证与预览交付

**Files:**
- Modify only if verification exposes a defect.

**Interfaces:**
- Produces: 自动测试证据、桌面与移动页面 QA、干净分支状态。

- [ ] **Step 1: 运行完整自动验证**

Run: `python -m unittest discover -s tests -v`

Expected: all PASS。

Run: `python site/build_data.py`

Expected: 350 notes, 7 topics。

Run: `git diff --check`

Expected: exit 0。

- [ ] **Step 2: 启动本地静态服务器并做浏览器检查**

Run: `python -m http.server 8000 --directory site`

检查桌面与移动：首屏主张、研究主线、七章卡片、topic hash、三视图、搜索、筛选、加载更多、why 展开、合作锚点、外链和横向溢出。

- [ ] **Step 3: 运行完成审计并提交修复**

逐项对照设计规格第 7 节九条验收标准；任何缺项都必须修复并重新运行完整验证。

- [ ] **Step 4: 交付独立分支**

报告 worktree、分支、提交、验证结果和预览方式；等待用户确认，禁止自动合并 `main`。
