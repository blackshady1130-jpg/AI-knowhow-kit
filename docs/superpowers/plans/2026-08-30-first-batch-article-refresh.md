# 第一批主题文章更新 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 重写“架构与工程”和“评测与基准”两篇主题文章，使其职责清楚、证据更新、语言自然，并作为其余五篇文章的结构与语气基线。

**Architecture:** 先用当前文章和定向 Notes 建立 claim ledger，分开记录事实、来源观点、作者判断和边界；再按设计稿规定的职责重写两篇正文。两篇分别完成内容检查和独立提交，最后进行一次跨文去重与站点兼容性验证，不重建数据、不发布。

**Tech Stack:** Markdown、PowerShell、Python 3、`site/build_data.py` 的解析函数、`removing-ai-slop` 文本扫描器、Git。

## Global Constraints

- 本计划只修改 `site/reviews/architecture-engineering.md` 和 `site/reviews/eval-benchmark.md`；研究台账只放在 `.tmp/article-refresh-first-batch/`，不进入 Git。
- 不修改 `notes/**`、七个主题名称、首页、UI、JavaScript、`site/topics.json`、`site/topic_assignments.json` 和 `site/data.json`。
- 两篇文章的 `更新至 2026.08` 暂时不改；七篇全部确认后再统一更新复核日期和站点数据。
- 每篇控制在约 4,500–5,800 个字符。增加新 Notes 时优先替换重复段落，不用加长掩盖结构问题。
- 小标题直接说明本节内容；不用故意抽象、翻译感强或空泛升格的表达。
- 数字、专有名词和因果判断必须回到 Note 或原文；公司口径、单一 benchmark、论文实验和作者推断不得写成普遍事实。
- `why/comments` 是作者判断，不改写 Notes，不覆盖历史判断；正文可以吸收其中结论，但要保留来源性质和边界。
- 每次 Git 操作只暂存计划中写明的文件，不使用 `git add -A`，不推送远端。

---

### Task 1: 建立两篇文章的证据台账

**Files:**
- Create locally, keep untracked: `.tmp/article-refresh-first-batch/evidence-ledger.md`
- Read: `site/reviews/architecture-engineering.md`
- Read: `site/reviews/eval-benchmark.md`
- Read: `notes/AI行业扫描_keywords.jsonl`
- Read selectively: `notes/AI行业扫描_md/*.md`

**Interfaces:**
- Consumes: 已确认的设计稿 `docs/superpowers/specs/2026-08-30-seven-topic-article-refresh-design.md` 与当前两篇文章中的 `#ID`。
- Produces: 每个候选主张的归属、证据、来源性质、边界和处理动作；Task 2 和 Task 3 只能使用台账中已核对的材料。

- [ ] **Step 1: 创建台账目录和固定字段**

用 `apply_patch` 创建 `.tmp/article-refresh-first-batch/evidence-ledger.md`，文件必须包含以下字段：

```markdown
# 第一批文章证据台账

## 字段说明

- 文章：架构与工程 / 评测与基准
- Note：#ID + 标题
- 来源性质：官方材料 / 论文 / 媒体文章 / 作者分析
- 可进入正文的主张：一句可验证陈述
- 边界：样本、配置、时间或来源限制
- 处理：保留 / 新增 / 压缩 / 迁移 / 删除
- 原文核验：本地全文已核对 / 一手来源已核对 / 仅保留为作者判断

## 架构与工程

## 评测与基准
```

- [ ] **Step 2: 盘点当前文章的全部 Note 引用**

Run:

```powershell
foreach ($f in @("site\reviews\architecture-engineering.md", "site\reviews\eval-benchmark.md")) {
  $text = Get-Content -Raw -Encoding UTF8 $f
  $ids = [regex]::Matches($text, '#(\d+)') | ForEach-Object { [int]$_.Groups[1].Value } | Select-Object -Unique
  "$f=" + ($ids -join ',')
}
```

Expected: 架构文章返回当前 17 个 ID，评测文章返回当前 16 个 ID。将每个现有 ID 标为保留、压缩、迁移或删除，不默认沿用旧结论。

- [ ] **Step 3: 核对架构文章的新材料**

按以下职责读取索引 `why` 和对应 Markdown，不全量读取 Notes 目录：

| Note | 正文用途 | 必须保留的边界 |
| --- | --- | --- |
| #388 | Runtime 管理持久状态、权限、成本和失败路径；模型越强，控制层承担的问题越具体 | 原文包含投资判断和公司案例，不能当作完整市场事实 |
| #414 | Context 同时来自离线知识编撰和在线 live query/任务状态 | OpenAI 未披露完整 accuracy 与六层架构消融，离线材料有 staleness |
| #415 | 新模型上线后先对 prompt、tool、workflow 做消融，再按新 failure case 加回 | 访谈与团队实践只支持 Claude Code 场景，不能外推所有 Agent |
| #417 | 靠近模型的脚手架变薄，工具发现、权限、恢复、Eval 等运行控制变厚 | 属于分析框架，不写成厂商统一路线 |
| #403 | 授权从调用前延伸到读取后、分享前和外发前 | Cloudflare OS 仍有 Workspace 粒度过粗、Driver 覆盖不完整等限制 |
| #395 | 失败处理先定位最早不可恢复错误，再分流到模型、Harness、工具或环境 | taxonomy 是描述性框架；人工验证集 40 例，细粒度自动归因仍有限 |

- [ ] **Step 4: 核对评测文章的新材料**

| Note | 正文用途 | 必须保留的边界 |
| --- | --- | --- |
| #395 | 从 success/failure 推进到 root-cause attribution | `κ=0.76`、`precision=0.96`、`coverage=68%` 只在原文口径一致时使用 |
| #399 | 用 pass@1、pass@5、pass^5 区分单次能力、探索上限和重复可靠性 | 80 题、五次运行和失败分类属于 AA-AnalystAgent 的特定设置 |
| #410 | 长程评测应包含环境变化、主动检查、状态维护和保持沉默 | 200 个模拟任务不等于真实互联网部署表现 |
| #419 | Rubric 是任务规格，需要与 Judge 一起校准 | RubricBench 与 PaperBench 的数字来自不同实验，不能合并成统一效率结论 |
| #423 | Agent 榜分数属于 Model × Harness × Environment × Verifier × Runtime | 六家使用同名 benchmark 不代表 Harness、预算和工具配置相同 |

- [ ] **Step 5: 对定量主张做原文核验**

优先核对 #395、#399、#410、#419 和 #423 中准备进入正文的数字。若本地 Markdown 已保存论文或官方正文，先核对本地全文；若只保存了作者解读或转述，打开其 `source_url` 对照一手材料。台账中的“原文核验”必须填写具体状态，无法核验的数字不进入正文。

- [ ] **Step 6: 检查台账覆盖**

Run:

```powershell
$ledger = Get-Content -Raw -Encoding UTF8 ".tmp\article-refresh-first-batch\evidence-ledger.md"
$required = @(388,395,399,403,410,414,415,417,419,423)
$missing = @($required | Where-Object { $ledger -notmatch "#$($_)\b" })
if ($missing.Count) { throw "Ledger missing IDs: $($missing -join ',')" }
"LEDGER_REQUIRED_IDS=PASS"
```

Expected: `LEDGER_REQUIRED_IDS=PASS`。

### Task 2: 重写“架构与工程”

**Files:**
- Modify: `site/reviews/architecture-engineering.md`
- Read: `.tmp/article-refresh-first-batch/evidence-ledger.md`

**Interfaces:**
- Consumes: Task 1 中标为可用的架构证据和边界。
- Produces: 一篇只回答“Agent 怎样保存状态、控制权限、恢复失败并持续运行”的完整文章；Task 4 以它作为 Runtime/评测职责分界。

- [ ] **Step 1: 记录改写前的问题**

在工作记录中写明以下四个问题，后续逐项消除：

1. “文件系统保存状态”和“长时间任务保存失败和反馈”重复解释状态连续性。
2. Context、缓存成本、文件系统、恢复、Identity 和自我改进按素材顺序排列，Runtime 的职责主线不够集中。
3. 权限主要停留在调用工具之前，没有覆盖数据读入后的 Workspace、Memory 和衍生产物传播。
4. 失败恢复写了 checkpoint 与回滚，却缺少“先判断哪一层出错”的分流方法。

- [ ] **Step 2: 按固定章节重建文章结构**

保留现有文章标题和副标题，正文依次使用以下章节；除“实践工具”和“哪些证据会改变以上判断”外，不新增平行栏目：

```markdown
## 核心判断：强模型会减少旧脚手架，但不会替代运行控制
## Context 有两条供应链：离线知识编撰与在线任务状态
## 文件、checkpoint 和 branch 共同保存长任务状态
## 权限要跟随数据和产物，不只检查工具调用
## 失败后先找最早不可恢复错误
## Agent 可以改进 Harness，但不能修改晋级规则
## 实践工具：长程 Agent 运行清单
## 这套方法不适用于哪些情况
## 哪些证据会改变以上判断
```

- [ ] **Step 3: 写清 Runtime 的职责边界**

首屏必须完成三件事：

1. 用 #388 定义 Runtime 管理的是执行过程，不是给模型补一层万能能力。
2. 用 #415、#417 说明模型升级后旧 prompt 和固定 workflow 可以删减，但状态、权限、恢复和验证仍需外部系统承担。
3. 明确 Harness 不能弥补模型缺少核心知识或推理能力，也不能用复杂脚手架替代模型升级。

- [ ] **Step 4: 合并 Context 与状态章节**

Context 章节用 #414 区分离线编撰与在线查询，并保留 #13、#29、#151、#180、#369、#377 中仍有信息增量的证据。状态章节合并现有文件系统、EdgeBench、Effect Log 和 backtracking 内容，只完整解释一次“为什么长任务不能依赖聊天记录”；保留 #184、#354、#384 的适用边界。

- [ ] **Step 5: 扩写权限与失败分流**

权限章节把 #382 的动态委托与 #403 的数据传播放在同一条链上，使用 `用户—Agent—任务—工具—对象—时限—数据来源—衍生产物` 说明审计记录。失败章节用 #395 说明应找到最早不可恢复错误，再决定修模型、Context、Harness、工具、环境或 Verifier；不复制评测文章的完整 taxonomy 和统计数字。

- [ ] **Step 6: 收紧自我改进与运行清单**

自我改进章节保留 #355、#334、#384，但把重点收敛到 proposer–evaluate–accept、held-out eval、权限上限和人工验收。运行清单保留目标、Context、状态、权限、验证、恢复、成本和学习写回八项；每项只写可执行检查，不重新总结正文。

- [ ] **Step 7: 运行文章级内容检查**

Run:

```powershell
$f = "site\reviews\architecture-engineering.md"
$text = Get-Content -Raw -Encoding UTF8 $f
$required = @(388,395,403,414,415,417)
$missing = @($required | Where-Object { $text -notmatch "#$($_)\b" })
if ($missing.Count) { throw "Architecture missing IDs: $($missing -join ',')" }
if ($text.Length -lt 4500 -or $text.Length -gt 5800) { throw "Architecture length=$($text.Length)" }
"ARCHITECTURE_CONTENT=PASS length=$($text.Length)"
```

Expected: `ARCHITECTURE_CONTENT=PASS`，长度位于 4,500–5,800。

- [ ] **Step 8: 运行去 AI 味扫描并人工判断**

Run:

```powershell
node "C:\Users\Administrator\.codex\skills\removing-ai-slop\scripts\audit-text.mjs" "site\reviews\architecture-engineering.md" --json --threshold 0.72
```

逐条标记为“修正”“合理保留”或“不确定”。重点检查：同一观点多次出现、只起过渡作用的段落、抽象小标题、无具体对象的趋势句、机械使用“不是 A，而是 B”。扫描不要求零命中。

- [ ] **Step 9: 验证引用并提交架构文章**

Run:

```powershell
$noteIds = @(Get-Content -Encoding UTF8 "notes\AI行业扫描_keywords.jsonl" | ForEach-Object { [int](($_ | ConvertFrom-Json).id) })
$text = Get-Content -Raw -Encoding UTF8 "site\reviews\architecture-engineering.md"
$ids = @([regex]::Matches($text, '#(\d+)') | ForEach-Object { [int]$_.Groups[1].Value } | Select-Object -Unique)
$missing = @($ids | Where-Object { $_ -notin $noteIds })
if ($missing.Count) { throw "Unknown architecture IDs: $($missing -join ',')" }
"ARCHITECTURE_IDS=PASS count=$($ids.Count)"
git diff --check -- site/reviews/architecture-engineering.md
```

Expected: `ARCHITECTURE_IDS=PASS`，`git diff --check` 无输出。然后只提交该文件：

```powershell
git add -- site/reviews/architecture-engineering.md
git commit -m "docs: refresh architecture and engineering review"
```

### Task 3: 重写“评测与基准”

**Files:**
- Modify: `site/reviews/eval-benchmark.md`
- Read: `.tmp/article-refresh-first-batch/evidence-ledger.md`

**Interfaces:**
- Consumes: Task 1 的评测证据，以及 Task 2 已确定的 Runtime/故障分流边界。
- Produces: 一篇只回答“怎样判断任务是否完成，并定位失败发生在哪一层”的完整文章。

- [ ] **Step 1: 记录改写前的问题**

在工作记录中写明以下四个问题：

1. WorkBuddyBench 的四类评分器占据篇幅过多，掩盖“结果属于系统而非裸模型”的结论。
2. 当前文章讨论 Judge 偏差，却没有把 Rubric 本身作为需要校准的任务规格。
3. 失败只按 benchmark 缺陷、环境和模型配置分散讨论，缺少 root-cause attribution 的明确方法。
4. pass@k 与 pass^k 仍偏抽象，缺少真实分析任务和动态长期任务的具体例子。

- [ ] **Step 2: 按固定章节重建文章结构**

```markdown
## 核心判断：先审任务和评分方法，再看分数
## 逐项检查任务、环境和隐藏要求
## 先说明结果属于模型，还是完整 Agent 系统
## Rubric 是任务规格，也需要校准
## 找到最早不可恢复失败，再决定修哪一层
## 真实工作要测连续成功、副作用、成本和接管
## 实践工具：统一结果行与评测检查表
## 哪些证据会改变以上判断
```

- [ ] **Step 3: 保留任务审计，压缩系统案例**

任务审计保留 #360 与 #183 的数字和边界。系统结果章节将 WorkBuddyBench 压缩为“不同 artifact 使用不同证据结构”的案例，保留 #373 的必要配置说明；加入 #423，说明同名 benchmark 在不同 Harness、预算、工具和 Runtime 下不能直接当作裸模型横比。

- [ ] **Step 4: 新增 Rubric 校准章节**

用 #419 区分 Judge 执行规则与 Rubric 定义成功标准。RubricBench 的偏好准确率和 PaperBench 的子要求数量分别说明“标准写漏”和“高质量规格昂贵”，不得把两项实验拼成一个统一 benchmark。保留 #240、#274、#333、#334 中关于判断强于生成、reward hacking 和答案泄漏的必要边界。

- [ ] **Step 5: 新增失败归因章节**

用 #395 定义“最早不可恢复失败”，给出两个通俗对照：关键信息被 compaction 删除属于 Harness；信息仍在上下文但模型忽略属于模型。统计数字只有在 Task 1 已完成原文核验时才保留，并明确 40 个验证案例和细粒度分类限制。

- [ ] **Step 6: 用真实任务重写可靠性章节**

用 #399 具体解释 pass@1、pass@5 和 pass^5；用 #410 说明长程任务还要测主动检查环境、维护承诺和在无需行动时保持沉默。保留 #357 的 Objective/Guardrail、副作用和 #120/#128 的连续可靠性判断，但删除重复定义。结论落到单次成功、连续成功、Guardrail 违例、成本、恢复时间和接管率。

- [ ] **Step 7: 合并实践工具**

先给一行统一披露格式：

```text
Model × endpoint × effort × Harness × Environment × tools × budget × Verifier × Runtime × cost
```

随后保留一张评测检查表，字段限于任务、环境、成功定义、Verifier、系统配置、成本、可靠性和证据边界；表格不复述前文案例。

- [ ] **Step 8: 运行文章级内容检查**

Run:

```powershell
$f = "site\reviews\eval-benchmark.md"
$text = Get-Content -Raw -Encoding UTF8 $f
$required = @(395,399,410,419,423)
$missing = @($required | Where-Object { $text -notmatch "#$($_)\b" })
if ($missing.Count) { throw "Eval missing IDs: $($missing -join ',')" }
if ($text.Length -lt 4500 -or $text.Length -gt 5800) { throw "Eval length=$($text.Length)" }
"EVAL_CONTENT=PASS length=$($text.Length)"
```

Expected: `EVAL_CONTENT=PASS`，长度位于 4,500–5,800。

- [ ] **Step 9: 运行去 AI 味扫描并人工判断**

Run:

```powershell
node "C:\Users\Administrator\.codex\skills\removing-ai-slop\scripts\audit-text.mjs" "site\reviews\eval-benchmark.md" --json --threshold 0.72
```

重点处理：同一 benchmark 多节重复、低信息量结论句、为了显得专业而堆叠英文名词、机械的对比句和没有说明样本边界的数字。

- [ ] **Step 10: 验证引用并提交评测文章**

Run:

```powershell
$noteIds = @(Get-Content -Encoding UTF8 "notes\AI行业扫描_keywords.jsonl" | ForEach-Object { [int](($_ | ConvertFrom-Json).id) })
$text = Get-Content -Raw -Encoding UTF8 "site\reviews\eval-benchmark.md"
$ids = @([regex]::Matches($text, '#(\d+)') | ForEach-Object { [int]$_.Groups[1].Value } | Select-Object -Unique)
$missing = @($ids | Where-Object { $_ -notin $noteIds })
if ($missing.Count) { throw "Unknown eval IDs: $($missing -join ',')" }
"EVAL_IDS=PASS count=$($ids.Count)"
git diff --check -- site/reviews/eval-benchmark.md
```

Expected: `EVAL_IDS=PASS`，`git diff --check` 无输出。然后只提交该文件：

```powershell
git add -- site/reviews/eval-benchmark.md
git commit -m "docs: refresh evaluation and benchmark review"
```

### Task 4: 跨文章去重与第一批验收

**Files:**
- Modify if needed: `site/reviews/architecture-engineering.md`
- Modify if needed: `site/reviews/eval-benchmark.md`
- Do not modify: `site/data.json`

**Interfaces:**
- Consumes: Task 2 和 Task 3 的完整文章。
- Produces: 可交给用户逐篇审阅的第一批修改稿、主要问题说明和 Note 变更记录。

- [ ] **Step 1: 检查两篇文章的职责交界**

逐项确认：

- 架构文章完整解释状态、权限、恢复和 Harness 晋级边界；评测文章不重写 Runtime 教程。
- 评测文章完整解释任务审计、Rubric 校准、失败归因和可靠性；架构文章只说明归因结果如何进入修复队列。
- #395 可以被两篇引用，但架构文章写修复分流，评测文章写归因方法和证据限制。
- Model × Harness 的完整披露格式只在评测文章展开；架构文章不再重复榜单比较方法。

- [ ] **Step 2: 运行跨文去 AI 味扫描**

Run:

```powershell
node "C:\Users\Administrator\.codex\skills\removing-ai-slop\scripts\audit-text.mjs" "site\reviews\architecture-engineering.md" "site\reviews\eval-benchmark.md" --json --threshold 0.72
```

检查 `similar-passage` 时区分必要术语与真实重复。相同机制如果在两篇中承担同一作用，删除一处；若分别承担运行修复和评测归因作用，保留但改成不同问题导向。

- [ ] **Step 3: 验证站点解析契约但不重建数据**

Run:

```powershell
$noteIds = @(Get-Content -Encoding UTF8 "notes\AI行业扫描_keywords.jsonl" | ForEach-Object { [int](($_ | ConvertFrom-Json).id) })
foreach ($f in @("site\reviews\architecture-engineering.md", "site\reviews\eval-benchmark.md")) {
  $text = Get-Content -Raw -Encoding UTF8 $f
  $ids = @([regex]::Matches($text, '#(\d+)') | ForEach-Object { [int]$_.Groups[1].Value } | Select-Object -Unique)
  $missing = @($ids | Where-Object { $_ -notin $noteIds })
  if ($missing.Count) { throw "$f has unknown IDs: $($missing -join ',')" }
  "$f IDS=PASS count=$($ids.Count)"
}
node --check site/js/app.js
git diff --check
```

Expected: 两篇均输出 `IDS=PASS`；JavaScript 语法检查和 `git diff --check` 无错误。不要运行 `python site/build_data.py`，因为它会重写 `site/data.json` 和生成日期。

- [ ] **Step 4: 验证最终改动范围**

Run:

```powershell
git status --short
git log --oneline -4
```

Expected: 本计划的正文改动与提交只涉及两篇 review 文件；`.tmp/article-refresh-first-batch/` 保持未跟踪且不暂存；仓库原有的 `.tmp/`、`.workbuddy/`、2026-07-15 文档和 `skills/demo-day-html-deck/` 不进入任何提交。

- [ ] **Step 5: 如跨文检查产生修改，单独提交**

```powershell
git add -- site/reviews/architecture-engineering.md site/reviews/eval-benchmark.md
git commit -m "docs: remove overlap from first article batch"
```

若跨文检查没有产生修改，跳过该提交，不创建空提交。

- [ ] **Step 6: 交付用户复核，不发布**

交付内容固定为：

1. 两篇旧稿的主要问题。
2. 两篇完整修改稿的文件链接。
3. 各自新增、保留、压缩、迁移和删除的 Note ID。
4. 去 AI 味扫描中仍保留的命中及理由。
5. 已运行的验证及结果。

到此停止。等待用户确认第一批的语言、深度和篇幅后，再为第二批“AI Coding + AI 产品与交互”编写实施计划；不更新 `site/data.json`，不推送，不发布。
