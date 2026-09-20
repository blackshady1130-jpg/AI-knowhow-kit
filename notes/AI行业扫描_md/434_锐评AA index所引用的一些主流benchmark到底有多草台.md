# 如何评价北京时间9月4日凌晨2时OpenAI正式发布 GPT-6 Astra？

> 来源：<https://www.zhihu.com/question/2079049979042198722/answer/2079265017392789039>

目前还有很多普通用户乃至部分研究的同学受AA的影响，如果读者看完了我的文章觉得有力的话可以转发给他们。9.5 5:27 (GMT+8) 更新 pro用户已推送，短暂测试来看是目前的全方位sota，具体领先多少和量化需要时间深入测试。简单来说，未降智版的GPT6pro在数学、其他科研辅助、前端和3D建模精细度目前绝对最强，是否和fable断档见仁见智；vibe coding有提升，大概比fable略强但基本同一梯队；得益于前端和3D建模能力的进步，wish coding能力大幅提升，明天估计就是各大自媒体一句话做一个app或精美3D游戏集体震惊瘫坐了。 如果读者感兴趣的话我可以后续追加一些深度测评或量化，或者分享一些我对benchmark设计的思考和我的部分私有题目。以下是原回答：

---

首先，无论GPT6实际体验如何，我对AA这个榜都已经忍无可忍了。当下社交媒体唯AA论，某些国模厂甚至去刷AA的烂分数，这种风气对我们自己的模型训练也是极为有害的。

一个三流业余测评指导Openai怎么训模型？

接下来如果我有时间，我会做一个针对目前各个主流benchmark的测评，很多benchmark天花板很低，很多benchmark胡说八道。

我认为“benchbench”本身的意义实际上是更大的，因为目前我们花了巨量的时间和资源训练模型，但只花了很少的时间调整尺子，以至于让这些业余测评污染模型的进一步迭代方向。

下面是万字长文，简单分析一下为什么我对AA做如此严厉的批评，实际上万字远远不够，只是起到一个引起读者重视的作用，读者可以自行复核其中提到的内容，不要被任何测评机构带跑了。

总的来说，给各位做benchmark的同学的几条真诚建议（其实是设计benchmark的基本功）：

1. LLM judge的使用需要极为谨慎，目前LLM judge的benchmark十有八九都有严重问题。
2. 如果模型的结果非常反直觉和反使用体验，首先应当检查错误case。
3. agentic benchmark统一测评环境是极为困难的事情，需要尽可能减少一些意想不到的执行过程影响，随便一个小问题就会造成10%的波动。

## 一个“智能指数”里，76%的权重都有严重测量问题：为什么我不再相信 Artificial Analysis Intelligence Index

这几天 GPT-6 Astra 发布后，我看到很多人拿 Artificial Analysis（AA）的 Intelligence Index 说事：

> “Astra AA 才 61，Fable 5.1 有 66，所以 GPT-6 智力不如 Fable。”

**首先，虽然我猜测astra的智力大概率更高，但AA本身的荒谬性完全不局限于astra，并且我也尊重任何认为fable更优的用户的真实使用体验。**

如果只是某个 benchmark 和我的主观体验不一致，我不会写这篇文章。

真正让我认为 AA Intelligence Index 已经失去作为“前沿模型综合智力排名”的可信度，是因为我把它当前 v4.1.1 的评测方法、benchmark 更新记录、grader prompt 和外部审计真正翻了一遍之后，“某个 benchmark 测得比较窄”是AA最小的问题，AA已经生动地向我们展示了Benchmark烂起来到底能有多离谱，以及外行指导内行再来骗更外行的普通用户有多恐怖。

我将要攻击的benchmark，在当前 AA Index 中，权重分别是：

- GDPval-AA v2：20%
- Terminal-Bench v2.1：16%
- τ³-Banking：14%
- AA-Omniscience：12%
- SciCode：8%
- AA-LCR：6%

合计：**76%！**

也就是说，我下面甚至还没有讨论 HLE（有30%错题）、GPQA（不知道现在还在用这个benchmark有什么意义） 和 CritPt（我认为唯一一个不错的benchmark，但评测过程也很抽象），只分析这六个 benchmark，就已经覆盖整个所谓“Intelligence Index”的四分之三。AA 官方目前仍然明确把这个 composite score 称作一个用于比较模型总体 intelligence、甚至用于 tracking progress toward AGI 的综合指标。

其中反复出现：**错误标准答案、错误 grader、错误 few-shot 示例、错误 gold trajectory、评测 pipeline 系统性误杀正确答案、benchmark 已经饱和却继续占巨大权重，以及直接把原 benchmark 的评分标准换掉。**

如果一个温度计刻度有点模糊，这是人之常情，但是如果这个温度计测的是湿度那就是另一回事了。

---

## 一、AA-Omniscience：一个连 grader 示例自己都互相矛盾的“幻觉测试”

我从6月开始就孜孜不倦地攻击这个benchmark，然而0个人关心，所以我必须好好说道说道。

AA 对 Hallucination Rate 的正式定义是：**incorrect / (incorrect + partial answers + not attempted)**。

注意，这里没有 correct。因此这导致一个显而易见的退化解：一个模型如果 6000 道题**一道也不回答，他的** Non-Hallucination = 100%，于是它可以完整吃下 AA 总榜中 Non-Hallucination 对应的 **4%权重**。

更妙的是，AA 给被测模型的 prompt 本身还明确告诉模型：

> 如果不知道答案、需要更多上下文或者工具，就明确这么说，宁愿如此也不要答错。

所以这已经不是单纯测模型天然的 hallucination tendency，而是在测：**模型 + AA 特制拒答 prompt 下的 abstention policy。**

然而，这甚至还远远不是最严重的问题。

## 1.73 为什么可以等于 1.75？

公开的 Omniscience grader template 对数值答案明确规定：

> 数值回答需要正确到 gold answer 的最后一个 significant figure。

然后同一个 grader prompt 给出的官方示例却是：

> Question：Jason Wei 身高多少米？  
> Gold：1.73 m  
> Prediction：1.75  
> **CORRECT**

理由居然是因为题目已经说明单位是米。理由讨论的“单位”跟数值为什么错了完全无关，这种事实错误不是睁眼睛说瞎话？？也就是说，一个依赖 LLM few-shot demonstration 建立判分边界的 grader，公开 prompt 里面直接塞了一个“错误数字算正确”的正例。

## 同一个 grader 对“额外信息”的规则也互相打架

- Gold 100 million，回答 100.2 million：CORRECT
- Gold 28，回答 28.1 million：PARTIAL
- Gold 1.73，回答 1.75：CORRECT

这已经不像一个具有清晰 decision boundary 的 scoring rubric。

而 CORRECT / PARTIAL / INCORRECT 的区别又不是无所谓——它直接同时影响 Accuracy 和 Non-Hallucination 两个 AA Index 组件。

## 最离谱的：一个模型可以一边胡猜，一边被判成“没有幻觉”

官方 NOT_ATTEMPTED 示例更精彩。问题：“fake barns thought experiment 最早是谁提出的？”模型回答：“我不知道，但可能是 Alvin Goldman 或 Carl Ginet。” grader 居然给判成：**NOT_ATTEMPTED**，理由居然是因为它声明了自己不知道。

这个模型明明已经向用户输出了一个错误候选人 **Alvin Goldman**。从通常的事实可靠性角度看，这恰恰是一种最经典的“我不确定，但我猜可能是……”式 hallucination。然而在 AA 的分类体系里，因为前面加了一句“我不知道”，整个回答就被洗成 NOT_ATTEMPTED。

而 NOT_ATTEMPTED 在 Hallucination Rate 中属于**不会被惩罚的那一侧**。

也就是说，这个指标甚至允许模型**先声明不知道，再跟着输出错误猜测，最后依然获得“没有幻觉”的待遇。**

如果一个 benchmark 连“什么算 hallucination”都不能稳定定义，我很难理解为什么这个数应该占所谓“总体智能”的 4%。

更需要注意的是，AA 当前已经把 Omniscience grader 换成 **GPT-5.6 Luna medium**；此前用过 Gemini 2.5 Flash、Gemini 3 Flash。AA 对 grader model 的更换记录是公开的。然而更为幽默的是，GPT5.6 luna比Gemini flash更依赖雷霆大思考，medium下的智力水平用过的人都懂（笑）。

因此，即使原论文曾对某个旧 grader 做过 human alignment validation，也不能自动证明今天换成 Luna 后四分类边界仍然具有同样可靠性。

这样的一个神秘的benchmark，描述吹的天花乱坠，实际如图所示：我们的minimax是幻觉最低的模型，还有4.5 haiku，畏惧了吗？ GPT幻觉率超过90%了，后面更有隐藏人物蓝色大肥鱼96%，AA从来没觉得自己做的benchmark有一丁点问题、从来没有半个人去复核这个荒谬的结果吗？

能提供这样一个benchmark的平台，如果是我的话，他说的剩下的话我一个字都不会再相信了。

---

## 二、τ³-Banking：这个 benchmark 自己已经证明，一次 grader 修复能让同一个模型涨 9 分

τ³-Banking 占 AA Index **14%**。

如果它只是“97 道银行客服题太窄”，我并不会认为这足以否定 benchmark。真正的问题是：**τ³ 官方自己的 changelog 已经证明，历史低分里存在大量不是模型失败，而是 grader 失败。**

2026 年 7 月 15 日，τ-bench v1.0.1 发布。官方直接在 changelog 顶部警告：banking_knowledge 在该版本前后的分数不可比较。

为什么？因为旧 evaluator 存在一个非常荒唐的系统性 bug。

agent 每调用一次 discoverable read tool，系统就把这次读取记录进数据库。而这个数据库表又参与最终 DB hash comparison。

结果是：一个模型即使已经正确完成任务，只要它最后**谨慎地再读一次数据确认操作成功**，就可能因为这个额外 read 不存在于 golden trajectory 中**整题直接变成 0 分。**

官方举的例子包括：

- 创建账户后重新查询账户确认；
- 下 replacement order 后重新检查 pending replacement order。

这些行为在真实 agent 系统里通常恰恰意味着**更谨慎、更可靠。**旧 τ³ 却会把它判死。

v1.0.1 修复以后，同一批已经生成好的 trajectory——注意，不重新跑模型，只重新打分——结果：

- GPT-5.5 xhigh：37.37 → **46.39**
- GPT-5.4 xhigh：30.67 → **39.43**

大约 **+9 个绝对百分点。**

今天大量网友看到两个模型 τ³ 差五六分，就可以开始讨论：“A 模型 agent intelligence 远强于 B。”然而这个 benchmark 自己一次 grader bug 修复：**同一个模型、同一个输出、同一批 trajectories，可以直接移动约 9 分。**

## 更严重的是：gold trajectory 自己一度不可实现

v1.0.1 还修改了 banking tasks 077–086。官方写得非常直白：这些任务原来的 gold trajectories 需要模型“不执行某些读取”，然而 agent 实际上又必须执行这些 account-listing reads 才能完成任务。

于是 gold 被修改为：**agent-realizable。**

翻译一下：**原来的标准答案轨迹，本身不是一个正常 agent 能实现的成功轨迹。**

## task_074：标准答案连钱都算错了

还有更加朴素的错题。task_074 中，根据银行政策，正确 refund 应为：**$14.50**。旧 gold 却写成：**$8.00**。居然v1.0.1 才修正，要是实在缺人手能不能让GPT或者fable帮你核对一遍benchmark再发？

官方甚至明确指出：以前如果模型复制 benchmark 的错误 $8，能通过；修复以后，这种 trajectory 反而失败，而真正按照政策计算出 $14.50 的才通过。

这就是货真价实的：**wrong gold answer。**

## 输入里甚至还出现过答案泄漏

同一批银行 fixture 中，一些数据库 description 原来直接写着类似：

> “SHOULD BE FREE - 1ST OF 2”

这种 annotation。换句话说，环境数据直接提示模型：**这个 fee 应该被 refund。**后来官方才清除这些泄漏。

于是一个 benchmark 可以同时：**1、gold 算错；2、environment 又泄漏正确答案；3、grader 再误杀额外 verification。**

这不是“领域覆盖”的问题。官方 evaluator 文档明确写着：

- `COMMUNICATE` 使用 substring match；
- `NL_ASSERTION` 由 LLM 判断，并直接标注 **Experimental / WIP**；
- 少数 banking tasks 使用 `ACTION`，这等于假定 reference trajectory 是唯一可接受轨迹；
- 最终 reward 是多个 component 的**乘积**，任何一个 gate 为 0，整题就是 0。

所以 τ³ 至少需要 trajectory-level failure audit。

看到一个 30%、40%的 pass rate，然后直接把剩下 60% 全部解释为：模型不会做 agent，在这个 benchmark面前，是没有依据的。

---

## 三、GDPval-AA v2：AA 用了 GDPval 的题，却已经不是 GDPval 的评分标准

这是整个 AA Index 权重最大的一项：**20%。**

很多人看到“GDPval”，会自然理解成：OpenAI 那个用行业专家评价真实职业工作产出的 benchmark。问题是：**GDPval-AA v2 的评分方式已经不是原版 GDPval。**

原 GDPval 的正式评分标准非常明确：由和任务职业相同领域的**experienced industry professionals**进行双盲评审。这些专业人士判断 AI deliverable 与专家 deliverable：

- better
- as good as
- worse

而且每一道 task 还有作者专门创建的**detailed scoring rubric**。

OpenAI 至今仍明确说明：

> GDPval 的 grading standard 是 pairwise human expert preference；LLM judge 只能作为 rough estimate。

为什么 OpenAI 不直接拿 LLM 判？因为他们真的测过。

原 GDPval 实验中：

- human ↔ automated grader agreement：**65.7%**
- human ↔ human agreement：**70.8%**。

也就是说，即使是专门为 GDPval 做的 automated grader，对复杂真实工作产出的判定也远没有达到“可以忽略 grader error”的程度。

AA 怎么做？GDPval-AA v2 使用三个 frontier LLM：

- GPT-5.5
- Gemini 3.1 Pro Preview
- Claude Opus 4.8

然后每个 A/B comparison**从这三个 judge 里抽一个**进行判断，再用这些胜负结果拟合 Bradley–Terry / Elo。

注意：这不是三模型 majority vote。不是三个 judge 分别判断然后 2:1。是：**一场 matchup，随机一个 judge。**

**？？？？？？**

**？？？？？？**

于是这里首先产生一个非常简单的问题，AA 有没有公布：

- GPT-5.5 vs GDPval human expert agreement？
- Gemini vs expert agreement？
- Claude vs expert agreement？
- 三个 judge 之间 agreement？
- 不同行业的 agreement？
- 不同被测模型下的 judge bias？

我目前没有找到。

而 GDPval 原论文已经告诉我们：**自动 judge 与专家一致率并没有高到可以默认可靠。**

**更何况，这仨模型那啥来判断fable和astra谁更强？GPT5和opus 4.1能给GPT5.5和opus 4.8打分吗？三个初中生能去批高考试卷吗？**

## 更奇怪的是：原 GDPval 有 task-specific rubric，AA 公布的 judge context 却没有写 rubric

AA 当前 methodology 明确写：每次 GDPval-AA comparison，会给 judge：

- initial task
- all reference files
- all submission files。

没有提 task-specific rubric。

这很值得注意，因为公开 GDPval 数据中的 rubric 并不是一句简单说明。它们可以非常详细，规定：

- 哪些数据必须存在；
- 哪些公式必须正确；
- 文件结构；
- 格式；
- 图表；
- presentation；
- 各项如何权衡。

OpenAI 甚至专门把这些 detailed rubrics 作为提高专家评分一致性的核心设计。

如果 AA production pipeline 实际额外把 rubric 给 judge 了，只是 methodology 没写，那么 AA 应该公开说明。

但如果当前公开描述就是完整 context，那么这意味着：**AA 不是让 judge 按 GDPval rubric 打分，而是让一个通用 LLM 根据自己的隐含偏好判断“Submission A/B 谁更好”。**

于是一个数据更正确但版式较差，和一个版式极漂亮但漏了 required items，究竟谁赢？不再由 GDPval 的 rubric 明确定义。而是**由被随机抽中的 LLM judge 自己决定。**

这已经是一个新的 benchmark，很难想象AA居然这么无耻地用这样一个污染的结果蹭openai的强力有效的GDPval。所以最准确的描述应该是：

> **GDPval-AA v2 使用 GDPval 的 task dataset，但 GDPval-AA v2 的 score 是 Artificial Analysis 自己定义的 LLM-preference Elo。**

这和原 GDPval 的 human-expert score 不能画等号。而这套重新定义过的 LLM preference metric**占整个所谓 Intelligence Index 20%。**

**当然，在这个AA分数里，这已经是最好的一个benchmark了，毕竟脱胎于正规公司openai的benchmark，还有更扯淡的，不信接着往下看。**

---

## 四、SciCode：前沿模型不是卡在60%，是 benchmark 自己卡在60%

SciCode 占 **8%**。

这一项现在几乎没什么可争论的余地，因为 2026 年 8 月刚刚出现了完整的 domain-expert audit：**SciCode-Verified。**研究团队逐题审核全部 test problems，发现：

- **263 个 defects**
- 其中 **192 个** 会让正确、遵循指令的代码被错误拒绝
- 这些 score-suppressing defects 分布在 **91%的 main problems** 中
- 约 **78%** 的此类问题需要专业 physics/math 知识才能发现。

公开修正版进一步统计：**155 / 287 scored subproblems 被这些问题影响。**约：**54%。**

**跟我读：**

**155 / 287 scored subproblems 被这些问题影响。**

约：**54%。**

**155 / 287 scored subproblems 被这些问题影响。**

约：**54%。**

**155 / 287 scored subproblems 被这些问题影响。**

约：**54%。**

问题包括：

- 无法复现的 gold answer
- tolerance 错误
- specification 自相矛盾
- 正确代码反而无法通过 tests

然后研究者把 benchmark 修好，重新测试十二个 frontier model snapshots。

原 SciCode：**45–60% subproblem accuracy**

修复以后：**84–98%。**

main-problem accuracy 更是从：**9–27% → 69–92%。**

这可能是近几年 benchmark 史上最具有教育意义的案例之一：**所有人以为模型撞墙了，最后发现撞墙的是测试集。我很难想象如果拿这个benchmark去RL会把模型训成什么样。**

然而 AA 当前 methodology 仍然使用原 SciCode，并给它 **8%** Intelligence Index 权重。

所以当有人看到：模型A SciCode 62，模型B SciCode 54 然后一本正经分析：“看来A科学编程能力显著更强。”

**你究竟是在比较模型，还是在比较两个模型分别踩中了多少 benchmark bug？**

一个修复后 frontier models 普遍达到 84–98% 的 benchmark，在原始 broken version 上争论 54 和 62 谁代表更高“科学智能”，已经没有多少测量学意义。

---

## 五、AA-LCR：一个所谓“长上下文推理”benchmark，judge 连长上下文本身都看不到

AA-LCR 占 **6%**。

它包含：

- 100 questions
- 每题约 100k tokens
- 多文档输入
- 当前使用 GPT-5.6 Luna medium 做 equality checker。

乍看很合理。直到你看 AA 自己公开的 LCR grader prompt：

> Question: {question}  
> OFFICIAL ANSWER: {official_answer}  
> CANDIDATE ANSWER: {candidate_answer}

然后：

> Reply only with CORRECT or INCORRECT.

注意少了什么？**那 100k tokens 原始文档。**judge 根本不看。

也就是说，这个所谓“Long Context Reasoning”的 grader 并不能验证模型是否真的根据原文档正确推理。它只能判断：**candidate short answer 是否和 official short answer 语义上相符。**

所以 official answer 一旦错了，judge 连发现错误的证据都没有。而且这个语义相符在长上下文测试里经常很离谱。

而这恰恰不是理论风险。Harbor 对 AA-LCR 做 adapter 时已经不得不修：

- Task 40：Excel date serial `45444` → **June 2024**
- Task 94：`0.14` → **14%**
- Task 2：题目要求 **3 个 legal cases**，official ground truth 却只列 **2 个**，于是直接排除该题。

需要强调：这些修复来自第三方 Harbor adapter，而不是 AA 官方自己宣布的全量 audit。

但这恰恰更说明问题：**只是一套第三方复现，就已经碰到了明确 wrong / malformed ground truth。**

而 AA 当前 production equality checker 看不到 source documents。那么它如何判断：“官方答案是不是其实错了？”答案是：**不能。**

它的任务只是服从 official answer。这是一种 reference-answer matcher，不是 source-grounded verifier。

于是 AA-LCR 的 pipeline 是：100k 文档 → 被测模型推理 → 得到几十个字符短答案 → judge 丢掉100k原文 → 只比较 candidate 与 official answer。

一旦 official answer 错**正确理解原文档的模型照样判错。**这正好是 benchmark evaluation pipeline 最典型的失败方式。

我看上下文能力一向用openai MRCR 8 needle 256k~512k和512k~1M，当然，muse spark 1.3的成绩好像有点怪，值得实测一下。不过这个测试真的能反应我的实际使用体验，而在这个测试里很多模型的成绩和AA-LCR是完全倒挂的。

---

## 六、Terminal-Bench：AA甚至还在给已经进入历史版本的2.1分配16%权重

Terminal-Bench 我反而不打算花太多篇幅，因为这个问题已经简单到不需要复杂分析。

AA 当前使用：**Terminal-Bench v2.1，89 tasks，权重16%。**而现在 Terminal-Bench 已经到了 **4.0。**

为什么不是简单的“新版本强迫症”？因为 2.1 已经出现明显 frontier saturation。

Terminal-Bench 相关研究方指出：**2.1 top agents 已达到约84%。**换成 3.0 后，当时最强模型只有：**43.5%。**

而 4.0 又继续做 benchmark QA：删除 8 个 tasks：

- 2 个 saturation
- 2 个 refusal
- 2 个 public solutions
- 2 个 unresolved quality / platform issues

- 修复 **19 个 tasks** 的 instructions / environments / verifiers
- 重新校准资源限制，减少 infrastructure noise。

Terminal-Bench 团队甚至公开解释：benchmark 是复杂模拟环境，**会包含 bugs，因此需要持续维护、修复和淘汰任务。**这是一个很健康的态度。

问题不在 Terminal-Bench，问题在 AA：

> **Benchmark 作者都已经不断修 bug、去 saturation、删 public-solution tasks，AA 的所谓“当前 Intelligence Index”却仍把老 v2.1 固定为第二大单项，占16%。**

我并不要求 Terminal-Bench 4.0 发布第二天 AA 就必须完成所有历史模型重跑，评测成本当然很高。

但是如果你因为成本问题暂时没法更新 benchmark，那合理结果应该是：

> “我们的 composite score 暂时滞后。”

而不是：**继续拿一个已经失去 frontier discrimination 的历史版本占16%，然后让公众把最终个位数差距解释成当前模型智力差。**

---

## 七、六项合计76%：这已经不是“任何benchmark都有缺点”

有人大概会反驳：

> “所有 benchmark 都有 bug，都不完美。”

当然。

问题从来不是**有没有一个错误，**而是错误的**性质、规模和权重**。

我们重新看这六项：

### GDPval-AA v2 — 20%

原 benchmark 正式标准是行业专家 blind preference + detailed rubrics。AA 换成：**随机抽一个 frontier LLM 判 A/B → Elo。**当前没有公开看到充分的 judge-vs-industry-expert calibration。

### Terminal-Bench 2.1 — 16%

当前 benchmark 已经是 4.0。2.1 frontier saturation 明显；4.0 又删除问题任务、修复大量 verifier/environment defects。AA 继续把2.1作为第二大组件。

### τ³-Banking — 14%

官方已经证明：**仅修 grader，同一批 trajectories 可涨约9pt。**历史上还存在：

- 正确的额外安全读取 → 0分
- 不可实现 gold trajectory
- wrong gold answer
- data leakage
- KB/tool inconsistency

### AA-Omniscience — 12%

所谓 hallucination metric 可以通过全拒答获得完美 Non-Hallucination。更严重的是公开 grader 示例直接出现：**1.73 → 1.75 = CORRECT**以及：**“不知道，但可能是错误A或正确B” = NOT_ATTEMPTED。**

### SciCode — 8%

domain-expert audit：**约54% scored subproblems 受到会压低正确模型得分的 defect 影响。**修复以后 frontier models：**45–60% → 84–98%。**

### AA-LCR — 6%

已发现 wrong/malformed official answers。而 judge：**甚至不读取那100k tokens源文档。**它只比较：question + official answer + candidate answer。

合计：

## **76%。**

这时候问题已经不能用一句benchmark都有局限性糊弄过去了。

如果一张期末试卷：

- 一部分标准答案错；
- 一部分判卷规则错；
- 一部分题目已经人人满分；
- 一部分判卷老师根本看不到原材料；
- 一部分从人工专业评分换成了未经充分校准的 AI preference；
- 一部分评分系统修个 bug 就能让学生从37涨到46；

最后老师告诉你：

> **“放心，我们重复考了十遍，95%置信区间小于±1分。”**

你会觉得这张卷子很科学吗？

---

## 八、AA那个“±1%置信区间”，恰恰说明了一个常见统计误区

AA 特别强调：

> 根据部分模型在所有评测上进行超过10次 repeats，他们估计 Intelligence Index 的95% confidence interval 小于 ±1%。

这个数字听起来非常精确。

但它测的是：**重复运行产生的随机方差。**

它完全不包含：

- wrong gold answer
- broken verifier
- systematic LLM judge bias
- stale/saturated benchmark
- benchmark contamination
- scoring-rule misspecification
- construct mismatch

一个坏掉的秤，可以每次都稳定地把你80kg测成75.00kg。重复一万次以后：**置信区间可以无限接近0。**这不会让75kg变成真值。

统计学上：**low variance ≠ low bias。但** AA 当前最大的问题恰恰不是 variance。

而是：

## **systematic measurement error。**

---

[原文链接](https://www.zhihu.com/question/2079049979042198722/answer/2079265017392789039)
