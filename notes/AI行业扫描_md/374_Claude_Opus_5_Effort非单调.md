# Claude Opus 5 的 max 为什么没赢：effort 非单调的原话核查与机制分析

> 核查日期：2026-07-25  
> 定位：回答两个问题——(1) Opus 5 是不是官方第一次在 Model/System Card 里讨论 effort 档位与效果差异；(2) `max` 在部分 benchmark 上不如 `xhigh`/`medium`，到底是什么机制，是不是模型训崩了。  
> 方法：直接核对 Opus 5 System Card 全文、Anthropic effort 官方文档、OpenAI o3-mini 发布页、gpt-oss Model Card、GPT-5.6 Preview System Card；对无法直接核验的条目单独标注。  
> 与既有文档的关系：本文替代 Codex 版《Claude_Opus_5_Reasoning_Effort_不是越高越好》作为主参考。Codex 版的核心结论保留，但机制排序被修正，理由见第 7 节。

---

## 0. 一页结论

**问题一：不是第一次，而且差得很远。**

- OpenAI 在 2025-01-31 的 o3-mini 发布页就公开比较了 `low/medium/high` 三档在 AIME、GPQA、Codeforces 上的效果差异（已核验原文）。
- OpenAI 在 2025-08-05 的 gpt-oss Model Card 里专设 "Variable Effort Reasoning Training" 一节，写明"我们把模型训练成支持三个 reasoning level"，并画出档位—准确率的 test-time scaling 曲线（已核验原文）。这是"Model Card 内讨论档位训练与效果"的明确先例。
- Anthropic 在 2025-11-24 随 Opus 4.5 上线 effort 参数，发布页直接比较 medium 与最高档的分数和 token 消耗（已核验原文）。
- "更高档反而更低分"也不是 Opus 5 首次出现：Opus 4.7 System Card（2026-04）报告的 HLE 五档曲线中，`xhigh` 55.4% 高于 `max` 54.7%（第三方对官方卡的转述，方向可信，数字待回查原卡）。Anthropic 当前的官方 effort 文档在 Opus 4.7 一节就写了 `max` "can lead to overthinking"、"只有当 evals 显示 xhigh 之上还有可测空间时才升 max"。
- Opus 5 的增量是三件事：把五档成本—得分曲线变成 System Card 的常规报告格式；给出多个"最佳观测点不在 max"的新案例；正式要求迁移时重做 effort sweep。它是这条披露路线的延续，起点在一年半以前。

**问题二：`max` 没赢的两个案例要分开读，都不是训崩。**

- FrontierBench（xhigh 44.4% vs max 43%）：官方原话就是 "max scored similarly and within noise"。这 1.4 个百分点分不出高下，不构成非单调证据，不应作为主案例引用。
- FrontierCode（Main 与 Extended 两套任务峰值都在 `medium`，53.4% / 63.6%）：这才是真正的非单调结果。官方没有归因。综合本卡其他章节的证据，第一候选解释是**高 effort 下的行为分布偏移**——Opus 5 System Card 自己记录了"高 effort 下反复自我纠正、重复验证已验证内容"（§6.2.1 内部试点反馈）、外部用户反馈的 "Overthinking, where it performs worse at higher effort levels"（§6.2.1）、以及蛋白设计实验中 max/high 两档都"陷入自我验证循环、最后 8 小时零产出"（§2.2）。FrontierCode 的评分是"隐藏测试 + 代码质量 rubric（含禁止实现模式）"的复合分、按 mean@5 计，天然惩罚做多、改多、方差大——正好打在高 effort 行为偏移的暴露面上。
- "上下文/输出预算耗尽"是官方确认存在的第二机制（Opus 5 在 IMO 评测中，max 档用尽 256k 输出上限的尝试被降档重采样，官方原话在 §8.6），但没有任何官方证据说明它是 FrontierCode 曲线的原因。Codex 版研究把它排为主因，证据不足。
- 训崩不成立的直接反证在同一张卡里：SWE-bench Pro 79.2%、Verified 96.0%、ARC-AGI-1 97.5%、ARC-AGI-2 90.4%、IMO 42/42，全部在 max 配置下取得（Table 8.1.A 标准配置即 adaptive thinking + max effort）。max 若系统性坏掉，这批结果无法解释。非单调只出现在特定"任务形态 × 评分函数 × 预算"组合上，这是行为校准问题，不是能力崩塌。

**你的后训练理解：方向对，两处要修。** effort 档位确实是后训练产物（gpt-oss 已公开承认，Claude 未披露细节），但训练优化的是训练分布上的期望奖励，不对每个第三方 benchmark 给逐任务单调性保证。而且推断方向要倒过来：coding agent 恰恰是最难保证单调的任务族，因为高 effort 在带环境副作用和质量评分的任务里有真实成本；单轮数学/知识题（多想几乎无副作用）才最接近单调。

---

## 1. 你引用段落对应的官方原话与链接

原报告 2.2 那段话的事实基础全部在 [Claude Opus 5 System Card PDF](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf) 第 8 章和 [effort 官方文档](https://platform.claude.com/docs/en/build-with-claude/effort)。逐条对应如下。

### 1.1 FrontierBench：§8.5，PDF 第 152 页

原话（已核验）：

> "On FrontierBench v0.1, Claude Opus 5 achieved a 44.4% mean reward, averaged over 5 attempts for each one of the 74 unique tasks, using xhigh effort (best result – max scored similarly and within noise, landing at 43%). high effort achieves 39% mean reward for 19% fewer output tokens on average, while low effort achieves 25% mean reward for 64% fewer output tokens on average."

译文：Opus 5 在 FrontierBench v0.1 上取得 44.4% mean reward（74 个任务、每个 5 次尝试取平均），使用 xhigh effort（最佳结果——max 得分相近、在噪声范围内，为 43%）。high 得 39%，平均少 19% 输出 token；low 得 25%，平均少 64% 输出 token。

两个口径细节：

- 汇总表 Table 8.1.A 里 FrontierBench 写的是 43.3%，因为汇总表的标准配置是 max effort；章节文字里的 44.4% 是 best-effort（xhigh）口径。同一模型同一评测，两个口径两个数。
- 原报告 2.2 写"FrontierBench 的最佳值出现在 xhigh，而不是 max"，字面正确，但漏了官方紧跟着的噪声定性。这句应降级为次要例证，不能当非单调的主案例。

### 1.2 FrontierCode：§8.4，PDF 第 150 页

任务与评分定义原话（已核验，节选）：

> "FrontierCode is an agentic coding benchmark of 150 software engineering tasks created by Cognition. Tasks are derived from real pull requests in open-source repositories... the agent then works autonomously in a containerized environment to produce a final patch, with no human intervention and no timeout information. Patches are graded against blocking functional criteria (primarily held-out unit tests) plus weighted rubric criteria, including model-graded checks for required test coverage and prohibited implementation patterns... We report FrontierCode's overall score, a composite measure... as mean@5."

结果原话（已核验）：

> "Opus 5 ranks 2nd on FrontierCode (Main) with a 53.4% score (each model at its best reasoning effort), improving on Claude Opus 4.8 (46.5%) and leading GPT-5.6 Sol (47.5%)."

> "[Figure 8.4.A] ... Claude Opus 5 reaches its best main-set score, 53.4, at medium effort."  
> "[Figure 8.4.B] ... Claude Opus 5 reaches its best extended-set score, 63.6, at medium effort."

### 1.3 IMO 2026 的降档重采样：§8.6，PDF 第 152–153 页

原话（已核验）：

> "We set a 256,000-token output limit and used adaptive thinking at max effort. Attempts that exhausted the output limit were resampled at lower thinking efforts; one of the solutions required this remedy."

这是"最高档撞输出预算上限"的官方直接案例：24 份解答里有 1 份靠降档才完成。

### 1.4 effort 文档的三句关键定义

来自 [effort 官方文档](https://platform.claude.com/docs/en/build-with-claude/effort)（已核验）：

> "Effort is a behavioral signal, not a strict token budget."（effort 是行为信号，不是严格 token 配额）

> `max`: "Absolute maximum capability with no constraints on token spending."（不设 token 约束的最高能力档）

> Opus 5: "If you carried effort settings over from an earlier model, run a fresh effort sweep on your evals rather than reusing them."（旧模型的 effort 配置不要沿用，重新 sweep）

补充两条对判断有用的：effort 影响响应中所有 token（含工具调用及参数）；Opus 5 上 "Effort controls thinking volume, not visible response length"。

### 1.5 数字台账：哪些数可以引用，哪些不行

| 数字 | 状态 |
|---|---|
| FrontierCode Main 峰值 53.4 @ medium；Extended 峰值 63.6 @ medium | 官方文字确认，可引用 |
| FrontierCode Opus 4.8：46.5 / 59.6；GPT-5.6 Sol：47.5 / 60.6（各自最佳档） | 官方文字确认，可引用 |
| FrontierBench：44.4 @ xhigh、43 @ max（within noise）、39 @ high、25 @ low | 官方文字确认，可引用 |
| FrontierCode 五档完整曲线的具体读数 | 只存在于 Figure 8.4.A/B 图中，无文字数值、无置信区间。两个第三方读图结果互相冲突（Codex 版读 main 集 high=48.0，SitePoint 读 high≈53），除峰值外的读数一律不可当事实引用 |
| medium 与 max 的具体差距 | 不可确认。只能说"图上 medium 为峰值、max 低于 medium"，幅度待回查原图 |

Codex 版文档把图读数（41.9/53.4/48.0/43.6/48.0）当确定数值列表使用，未标读图冲突，这是需要修正的一点。

---

## 2. 问题一：官方披露史时间线

把"官方讨论 effort"拆成三层，每层都有 Opus 5 之前的先例：

1. **参数化并公布档位效果差异**（发布页层面）
2. **在 Model/System Card 里讨论档位的训练来源**
3. **把 effort 曲线当成报告范式，并承认非单调**

| 日期 | 文档 | 披露内容 | 核验状态 |
|---|---|---|---|
| 2025-01-31 | [OpenAI o3-mini 发布页](https://openai.com/index/openai-o3-mini/) | "developers can choose between three reasoning effort options—low, medium, and high"；AIME/GPQA/Codeforces 按档位画图，明确写 low≈o1-mini、medium≈o1、high 超过 o1 | 已核验原文 |
| 2025-08-05 | [gpt-oss Model Card](https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf) §2.5.2 | "We train the models to support three reasoning levels: low, medium, and high... Increasing the reasoning level will cause the model's average CoT length to increase."；Figure 3 报告 "smooth test-time scaling of accuracy" | 已核验原文 |
| 2025-11-24 | [Claude Opus 4.5 发布页](https://www.anthropic.com/news/claude-opus-4-5) | effort 参数上线（low/medium/high）："Set to a medium effort level, Opus 4.5 matches Sonnet 4.5's best score on SWE-bench Verified, but uses 76% fewer output tokens." | 已核验原文 |
| 2026-02-05 | Claude Opus 4.6 System Card | 加入 `max` 档（effort 文档确认 4.6 支持 max）；Codex 版称 MCP-Atlas 出现 high 高于 max | max 档已核验；MCP-Atlas 非单调一条未能独立核验 |
| 2026-04-16 | [Claude Opus 4.7 发布页](https://www.anthropic.com/research/claude-opus-4-7) 与 System Card | 新增 `xhigh`，五档成形；官方写 "Opus 4.7 thinks more at higher effort levels"；第三方对 System Card 的转述给出 HLE 五档曲线：43.0 / 48.4 / 53.2 / **55.4 (xhigh)** / 54.7 (max)，峰值不在 max | 发布页已核验；HLE 曲线为第三方转述（allthings.how），方向可信、数字待回查原卡；Codex 版所称"ARC-AGI-1 上下文耗尽归因"未能核验，且另一第三方给出的 4.7 ARC-AGI-2 曲线（max 75.8 > high 68.3）是单调的，该条存疑 |
| 持续生效 | [effort 官方文档](https://platform.claude.com/docs/en/build-with-claude/effort) Opus 4.7 一节 | `max`: "On most workloads max adds significant cost for relatively small quality gains, and on some structured-output or less intelligence-sensitive tasks it can lead to overthinking."；升 max 的条件是 "your evals show measurable headroom at xhigh" | 已核验原文 |
| 2026-05-28 | Claude Opus 4.8 System Card | 延续五档；Codex 版称 SWE-bench Pro 峰值在 xhigh | 发布事实已核验；xhigh 峰值一条未能独立核验。第三方观察称 4.7→4.8 各档 compute 被重新校准（medium 变多、high 略少），可解释官方为何要求 fresh sweep |
| 2026-06 | [GPT-5.6 Preview System Card](https://deploymentsafety.openai.com/gpt-5-6-preview) | "Rather than report a single score, we show a curve across different levels of effort. This gives a fuller picture of what the model can do and how much effort it takes to get there." | 已核验原文 |
| 2026-07-24 | [Claude Opus 5 System Card](https://www.anthropic.com/claude-opus-5-system-card) | 五档曲线贯穿第 8 章；FrontierCode medium 峰值；FrontierBench xhigh 最佳但与 max 在噪声内；迁移要求 fresh effort sweep | 已核验原文 |

**结论**：三层披露分别始于 2025-01（o3-mini）、2025-08（gpt-oss）、2026 上半年（4.7 HLE 曲线 + GPT-5.6 卡的曲线范式）。Opus 5 做的是常规化和案例扩充。

**边界**：本表只覆盖 OpenAI 与 Anthropic。Google、Meta、国产模型的 model card 未做穷尽考古，不主张全行业首次归属。

---

## 3. 这两个 benchmark 到底在测什么

### 3.1 FrontierBench v0.1：终端环境里的科学/工程任务

| 维度 | 内容 |
|---|---|
| 任务定义 | Terminal-Bench 2.1 同团队的继任版本，74 个更难任务，侧重计算生物、物理仿真、CAD、形式证明、GPU 性能优化；在容器化终端环境里做真实工作 |
| 指标口径 | mean reward，每任务 5 次尝试取平均；Anthropic 内部用 mini-SWE-agent harness + GKE 跑 |
| 系统层干扰 | Opus 5 的安全分类器拦截了 5% 的 API 调用（4% 的 trial），fallback 到 Opus 4.8；Fable 5 对应 42% / 26% |
| 五档结果 | low 25 → high 39 → xhigh 44.4 → max 43 |

为什么这里的 "xhigh > max" 是伪问题：74 个任务、5 次尝试、连续型 reward，1.4 个百分点的差距在这个样本量下没有排序意义，官方也直接写了 within noise。这条曲线真正的信息是另一头——low 到 xhigh 之间存在陡峭且真实的 effort 收益（25→44.4），说明这类难任务确实吃 test-time compute；到顶部后收益封顶。

### 3.2 FrontierCode v1.1：评分函数天然惩罚"做多"的 coding 评测

| 维度 | 内容 |
|---|---|
| 任务定义 | Cognition 出品，150 个任务，来自真实开源 PR（修 aiohttp websocket bug、加固 Prisma browser bundle、扩展 JSON schema lint 规则等），由原仓库维护者出题、Cognition 复核 |
| 执行方式 | agent 拿到 checked-out 仓库 + 一条 issue 描述，在容器里自主工作，无人工干预，**不告知超时信息** |
| 指标口径 | 复合分：blocking functional criteria（隐藏单测，不过就卡住）+ 加权代码质量 rubric（含模型评分的"必须有测试覆盖"与"禁止实现模式"）；报 mean@5 |
| 运行方 | Cognition 运行并评分（第三方 harness，非 Anthropic 内部 harness） |
| 五档结果 | 两套任务峰值都在 medium（53.4 / 63.6），max 低于 medium（幅度见 §1.5，不可精确引用） |

三个结构性特征决定了它对高 effort 不友好：

1. **复合评分罚越界**。功能测试通过之后，多改的每一处都要过 rubric 的审查："禁止实现模式"和"要求的测试覆盖"是模型评分项，重构非目标代码、加没要求的东西、绕规范的写法都可能扣分。pass/fail 型评测里"做多不扣分"，这里扣。
2. **mean@5 罚方差**。高 effort 轨迹更长、行为更发散，5 次里只要有 1 次陷进自我验证循环或把已通过的补丁改坏，均值就掉 20% 权重。pass@5（取最好）口径下 max 可能仍占优，但卡里没报。
3. **agent 不知道超时**。存在墙钟/回合上限但不告知，高 effort 的"再多验证一轮"倾向更容易在不知情中撞上限。

（以上第 1-3 条是基于官方口径描述的机制推断，官方未对 FrontierCode 曲线做任何归因。）

---

## 4. 为什么 max 会输：机制证据分级

四个机制按证据强度排序。关键改变：Opus 5 System Card 自己披露的行为证据把"行为分布偏移"顶到了第一候选。

### 机制 A：统计噪声（官方确认，适用 FrontierBench）

官方原话 "max scored similarly and within noise"。此条只适用于 FrontierBench 的 xhigh vs max；FrontierCode 的 medium 峰值官方没有用噪声解释，两套任务同时在 medium 达峰也降低了纯噪声的可能性。

### 机制 B：高 effort 行为分布偏移——overthinking、自我验证循环、范围膨胀（官方披露的行为事实；用于解释 FrontierCode 是推断）

这是 Codex 版漏掉的证据链，全部来自 Opus 5 System Card 本卡：

**§6.2.1 试点反馈（PDF 第 81 页），内部用户**（已核验）：

> "Self-correction loops where the model continually attempted to reconsider its answer, especially at higher effort levels. This also included continually re-verifying already verified answers."

译文：自我纠正循环——模型不断试图重新考虑答案，在更高 effort 档位下尤其明显，包括反复重新验证已经验证过的答案。

**同节，外部用户**（已核验）：

> "Overthinking, where it performs worse at higher effort levels."

译文：过度思考——在更高 effort 档位下表现反而更差。

官方随后的限定句也要引全：**"Not all of this feedback is consistent with trends we've observed when attempting to quantify related phenomena more precisely"**——定量层面并未全部坐实，这是试点观察，不是结论性测量。

**§2.2 CB 能力评估的蛋白设计实验**（已核验）：24 小时、1 万美元预算、端到端设计 30 个 GDF-8 选择性结合蛋白。

> "We conducted two identical experiments... an early snapshot of Claude Opus 5 in two replicate experiments, conducted at different effort settings (max and high). Mythos 5 delivered all 30 designs, ranked and internally audited. Neither Claude Opus 5 arm delivered: one shipped 17 unranked designs after abandoning the selectivity goal partway through; the other shipped nothing and went silent for its final 8 hours. Unlike Mythos 5, Claude Opus 5 consistently got stuck in self-verification loops instead of producing designs."

配套的定性描述：

> "Unproductive self-verification: The model is prone to descending into exhaustive correctness checks, often developing elaborate verification pipelines that distract from the primary task."

译文：无产出的自我验证——模型容易陷入穷尽式正确性检查，经常在结果落地前就搭起复杂的验证管线，偏离主任务；多次因此在时间预算内交不出活。同节还列了 "Poor calibration of task scope"（过度工程化、放大边际修改的重要性）。

**§6.3 训练数据审查（约 150 万条 RL episode，PDF 第 84 页起）**：训练后期轨迹里已发现任务范围膨胀（顺手改别的文件、加没要求的测试）、声称验证过但实际没执行等行为。这类行为在 pass/fail 评分下未必扣分，在 FrontierCode 的质量 rubric 下会扣分；effort 越高，行为量越大，暴露面越大。

**官方文档侧的旁证**：effort 文档 Opus 4.7 一节明确写 max 在部分任务上 "can lead to overthinking"；[Opus 5 prompting 指南](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)记录模型默认更主动自检、更愿意扩大范围、旧 prompt 里的"再检查一遍"会导致重复验证。

把机制 B 和 FrontierCode 的评分结构（§3.2）对上：高 effort 放大"多验证、多修改、迟迟不停"的行为分布，而这套行为在"复合 rubric + mean@5 + 未知超时"的口径下每一项都在扣分。这是当前证据下最连贯的解释，但官方没有归因，定性为**强推断**。

### 机制 C：上下文/输出/时间预算耗尽（机制官方确认存在；对 FrontierCode 未证明）

官方直接证据是 IMO 案例（§1.3）：max 档撞 256k 输出上限，需降档重采样。这证明"更高 effort 的额外思考可能挤掉完成闭环所需的预算"在 Opus 5 上真实发生。

不能外推的部分：FrontierCode 任务在 1M 上下文的容器 agent 环境里跑，卡里没有任何截断率、上下文耗尽率的披露；Codex 版引用的 Opus 4.7 ARC-AGI"context exhaustion"归因本次未能核验（可核验的 4.7 非单调案例是 HLE 曲线，且另一来源的 4.7 ARC-AGI-2 曲线是单调的）。预算耗尽应列为 FrontierCode 的第二候选，与机制 B 可叠加（自我验证循环本身就是烧预算的方式）。

### 机制 D：评分函数不奖励彻底性（结构事实）

FrontierCode 的 rubric 明确包含"禁止实现模式"；effort 文档明确说 max 会在结构化输出类任务上 overthinking。任务只奖励"规范内通过"时，最高档买到的"更彻底的探索与重写"没有对应的分数收益，只有风险。

### 关键对照：同一张卡里 max 在大量评测上拿到旗舰成绩

Table 8.1.A 的标准配置就是 "adaptive thinking at max effort"。在这个配置下：SWE-bench Pro 79.2%、SWE-bench Verified 96.0%、Multilingual 89.5%、Multimodal 59.4%、DeepSWE 68.8%、HLE（带工具）64.7%、BrowseComp 90.8%；ARC Prize 官方验证的 ARC-AGI-1 97.50%、ARC-AGI-2 90.42% 也明确标注 at max effort；IMO 42/42 用 max（含一次降档补救）。

这个对照说明两件事：

1. max 没有全局退化。若 max 系统性变差，以上结果不可能成立。
2. 非单调是选择性的：同为 coding，纯 pass/fail 的 SWE-bench 家族在 max 下表现正常，带质量 rubric 的 FrontierCode 在 medium 达峰。出问题的维度不是"coding 与否"，是"评分函数是否惩罚多余行为"。

一个容易误读的点顺带纠正：汇总表里 ARC-AGI-3 标注 "(high)"，不是 high 打败了 max——原话是 "Results for Claude Opus 5 at max effort were not available at the time of release"（max 结果发布时还没跑完）。不能把它算进非单调案例。

---

## 5. 这是不是训崩了

### 5.1 概念先分开

"训崩/模型崩塌"指训练层面的系统性退化：数据分布收缩、递归合成数据导致能力普遍下降、新 checkpoint 在大量任务族上持续退化。判断特征是**跨任务、跨口径、可复现的能力面下降**。

Opus 5 出现的是**推理控制层的非单调**：同一套权重，在不同行为强度信号下，特定任务×评分函数组合的 mean@5 不随强度单调。§4 的对照组（max 下的一批旗舰成绩）直接排除了"能力面下降"。

### 5.2 你的"五档应该依次更强"直觉，对在哪、错在哪

对的部分：五档排列的确是投入的单调序——thinking 量、输出 token、工具调用数、验证强度都随档位上升（FrontierBench 的 token 数据可证：low 比 xhigh 少 64% 输出 token）。能力包络（模型最多能做到什么）也大体随档位扩大。

错的部分：档位不是五个嵌套的能力集合。`max` 不是"medium 做完后再免费多检查一遍"，而是从规划开始就选择更复杂的方案、更多分支、更多修改、更久不停。这是五种不同的条件化行为分布。某个 benchmark 的得分 = 行为分布 × 任务形态 × 评分函数 × 预算上限的复合结果，对这个复合函数没有单调性保证。effort 文档那句 "behavioral signal, not a strict token budget" 是官方对这一点的准确表述。

### 5.3 什么信号才值得升级怀疑

同时满足多数以下条件，才需要从"校准问题"升级为"训练问题"：

1. 多个大样本任务族稳定出现 max 低于中档，置信区间分离；
2. 排除了 max_tokens 截断、上下文耗尽、超时、工具预算；
3. 换 harness、换 grader、换提示词仍复现；
4. 失败轨迹显示一致的策略缺陷（反复推翻正确答案、无法停止）且随档位加重；
5. 真实线上任务受影响。

当前对号入座：FrontierBench 是噪声（官方定性）；FrontierCode 是"有实质幅度、官方未归因"的开放问题，满足上面第 4 条的部分线索（自我验证循环有本卡书面记录），但第 1-3 条都还没有公开数据；蛋白设计实验 n=2，只能算强信号个案。合理定性是 **effort 行为校准在部分任务族上没调平**，Anthropic 自己把这些行为写进了卡里，说明在其监测范围内。

---

## 6. 你的"后训练策略"理解：对的部分与三处修正

### 6.1 对的部分：档位确实是训练出来的

gpt-oss Model Card 原话（已核验）：

> "We train the models to support three reasoning levels: low, medium, and high. These levels are configured in the system prompt by inserting keywords such as 'Reasoning: low'."

公开可查的实现路径有两类（Sebastian Raschka 对 gpt-oss/GPT-5.6 的分析，二手技术综述）：effort-conditioned RLVR（按档位给不同的长度奖励/惩罚）与 effort-conditioned SFT（档位标签配目标长度的监督数据），可混用。抽象成一句：**训练阶段学一个能按 effort 信号改变行为的条件策略，推理阶段用信号选择档位**。你说"reasoning effort 是后训练的策略、有相关的数据"，方向正确。

### 6.2 修正一：期望收益不等于逐任务单调

训练目标是训练分布上的期望奖励。它能保证高档"平均上思考更多、在训练分布上质量—成本权衡更好"，不能保证对每个第三方评测、每种评分函数、每个随机种子单调。FrontierCode 由 Cognition 出题、运行、评分，奖励形状（质量 rubric + 禁止模式）大概率偏离 Anthropic 训练时的奖励形状（以任务完成/测试通过为主）。§6.3 的 RL 审计恰好显示训练后期存在范围膨胀类行为——训练奖励没把"做多"压下去，第三方 rubric 却在罚它。

### 6.3 修正二：coding 恰恰是最难单调的任务族，你的推断方向反了

"coding 是后训练重点，所以档位分布不应该出问题"——这个推断在纯 pass/fail 的 coding 评测上确实成立（SWE-bench 家族在 max 下正常拿分）。但 agentic coding 是**有环境副作用**的任务：高 effort 多出来的每一步都可能改坏已通过的补丁、扩大 diff、触发 rubric 扣分，而且 mean@5 放大单次翻车的代价。对照组是单轮推理任务：AIME/GPQA（gpt-oss Figure 3 平滑上升）、IMO（Opus 5 用 max 拿 42/42），多想几乎没有副作用，所以最接近单调。**副作用大小、评分函数形状，比"是不是后训练重点"更决定单调性。**

### 6.4 修正三：Claude 的具体配方未披露，且档位语义跨代不稳定

Anthropic 没披露每档是否有独立训练数据、reward 权重、是否用专门 token。第三方观察称 4.7→4.8 之间各档 compute 被重新校准（medium 变多、high 略少）。这正是官方要求迁移时 "run a fresh effort sweep" 的原因：**档位名是稳定的 API 字符串，档位行为是每代重调的训练产物。**"五档由特定后训练数据实现"目前只能算合理猜测。

---

## 7. 对 Codex 版研究的直接评估

保留的部分：结论一（不是第一次）方向和主要时间线正确；FrontierBench 噪声定性正确；"行为信号"框架、effort sweep 工程清单可继续用。

修正的部分：

1. **漏了本卡内最直接的证据。** §6.2.1 的 overthinking/自我纠正循环反馈、§2.2 的蛋白设计实验、§6.3 的 RL 行为审计都没进入 Codex 版的机制分析。这三段把"行为分布偏移"从纯推测变成了有官方书面记录的行为事实。
2. **机制排序错了。** Codex 版把"上下文耗尽"排为主要机制，依据是 Opus 4.7 ARC-AGI 的归因平移。该归因本次未能核验（4.7 卡可核验的非单调案例是 HLE 曲线），且 FrontierCode 没有任何截断/耗尽数据支持。修正后的排序：FrontierCode 第一候选是行为分布偏移，第二候选是预算耗尽，两者可叠加。
3. **图读数当事实用。** FrontierCode 五档读数与其他第三方读图冲突，除官方文字确认的峰值外都应标"约值、待回查"。
4. **ARC-AGI-3 的 "(high)" 没查。** 那是 max 未跑完，不是非单调案例。

---

## 8. 下一步

### 8.1 原报告 2.2 的替换文本（可直接粘贴）

> ### 2.2 推理时计算层：更可控的 effort scaling，但不保证逐任务单调
>
> Opus 5 支持 `low` 到 `max` 五档 effort。官方定义 effort 是行为信号而非严格 token 配额：它同时改变 thinking 量、可见输出、工具调用和整体执行强度。低档收益真实存在——FrontierBench 上 low 到 xhigh 从 25% 升到 44.4%，AutomationBench 的 medium 以不到一半成本保住了大部分分数。
>
> 顶部两档的排序在部分评测上失效，但两个案例性质不同：FrontierBench 的 xhigh 44.4% 对 max 43%，官方明确称差异在噪声内，不构成结论；FrontierCode 的 Main 与 Extended 两套任务峰值都在 medium（53.4 / 63.6），官方未给归因，图中无置信区间。结合本卡其他章节——试点反馈记录了高 effort 下的自我纠正循环与 overthinking（§6.2.1），蛋白设计实验中 max/high 两档均陷入自我验证循环而交付失败（§2.2），IMO 评测中 max 档有解答因用尽 256k 输出上限被降档重跑（§8.6）——更高 effort 在扩大能力空间的同时，也放大过度验证、范围膨胀和预算撞墙的风险。同一张卡里 SWE-bench Pro、ARC-AGI-1/2、IMO 都在 max 配置下拿到旗舰成绩，说明这是特定任务与评分口径下的校准问题，不是 max 全局退化。
>
> 迁移含义不变且更强：不要沿用 4.8 的 effort 配置，按 Anthropic 要求对五档重新 sweep；优化目标是成功率、可验证质量、总成本、延迟与失败风险的 Pareto 拐点，默认档从 high/medium 起步，max 只有在自有 eval 显示 xhigh 之上仍有可测空间时才启用。

### 8.2 待核验清单（回查原卡即可关闭）

1. Opus 4.7 System Card：HLE 五档数字（43.0/48.4/53.2/55.4/54.7）与是否存在 ARC-AGI 档位归因原文。
2. Opus 4.6 System Card：MCP-Atlas 是否有 high > max 记录。
3. Opus 4.8 System Card：SWE-bench Pro 峰值档位。
4. Opus 5 Figure 8.4.A/B：FrontierCode 五档精确读数与 medium–max 差距。

### 8.3 自有任务上的最小裁决实验

如果要在自己的评测上区分"行为偏移"还是"预算耗尽"，每档跑同一批任务，只需盯三个指标：

1. **截断率/耗尽率**：max_tokens 截断、上下文压缩触发、超时的比例。此值高 → 预算问题，先加预算再重测，不要下能力结论。
2. **输出 token 与工具调用分布**：max 档相对 xhigh 的增量花在哪（新探索 vs 重复验证同一对象）。重复验证占比高 → 行为偏移。
3. **失败轨迹分类**：把每档失败标成浅思考 / 错误分支 / 改坏已对的方案 / 验证循环不停止 / 未完成。max 档"改坏已对方案 + 验证循环"占比显著高于中档 → 与 Opus 5 卡内记录一致，按行为偏移处理（收紧任务边界、在 prompt 里限制验证轮数），而不是升档。

---

## 9. 证据索引

### Opus 5 官方（本次直接核验）

- [Claude Opus 5 System Card PDF](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf)：§2.2 蛋白设计实验；§6.2.1 试点反馈（p.81）；§6.3 训练数据审查（p.84）；§8.4 FrontierCode（p.150）；§8.5 FrontierBench（p.152）；§8.6 IMO（p.152）；§8.14 ARC-AGI（p.180）；Table 8.1.A（p.148）
- [Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)（发布页，effort 曲线图与 FrontierBench 口径说明）
- [Effort 官方文档](https://platform.claude.com/docs/en/build-with-claude/effort)
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)

### 历史官方（本次直接核验）

- [OpenAI o3-mini 发布页](https://openai.com/index/openai-o3-mini/)，2025-01-31
- [gpt-oss Model Card PDF](https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf) §2.5.2，2025-08-05
- [Claude Opus 4.5 发布页](https://www.anthropic.com/news/claude-opus-4-5)，2025-11-24
- [Claude Opus 4.7 发布页](https://www.anthropic.com/research/claude-opus-4-7)，2026-04-16
- [GPT-5.6 Preview System Card](https://deploymentsafety.openai.com/gpt-5-6-preview)，2026-06

### 第三方与内库（辅助，标注性质）

- [allthings.how：Opus 4.7 System Card 摘要](https://allthings.how/claude-opus-4-7-system-card-key-findings-and-benchmarks/)——4.7 HLE 五档曲线的转述来源，待回查原卡
- [Sebastian Raschka：Controlling Reasoning Effort in LLMs](https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms)——effort 训练实现路径的技术综述
- [SitePoint：FrontierCode medium effort 分析](https://www.sitepoint.com/claude-opus-5-medium-effort-frontiercode-benchmark/)——与 Codex 版读图冲突的对照样本
- 内库 id 307《Implications of Large-Scale Test-Time Compute》（[原文](https://x.com/polynoamial/status/2064210146558136827)）：模型能力应表述为预算下的曲线，不是单点分数
- 内库 id 341《Noam Brown访谈notes_测试时计算Scaling与模型评估重写》（[原文](https://docs.qq.com/markdown/DYVRsSnJkS2F0eE15)）：benchmark 必须带 X 轴（token/时间/美元）
- 内库 id 358《Benchmarking Coding Agents on Databricks' Multi-Million Line Codebase》：相同模型与 thinking effort 换 harness 后单任务成本可差两倍，质量基本不变——评测结论对 harness 高度敏感的企业侧证据
