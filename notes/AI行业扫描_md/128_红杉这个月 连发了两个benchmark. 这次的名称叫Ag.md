---
url: https://mp.weixin.qq.com/s/JAWEUFAW3v49XGGaz5TfWg
title: "AgentIF-OneDay发布，评估全场景长时复杂任务"
description: "Agent能否协助你一天的生活"
captured_at: "2026-03-09T03:35:59.380Z"
---

# AgentIF-OneDay发布，评估全场景长时复杂任务

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dqXgnTgtib4eiajL6Z9J9yY7icwvibxQ7lM8QlexXLTeuTIFktQwsQHeiaqicibx3oibwo4xtpKSCnKiaSIE9cQtMVCkwzQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dqXgnTgtib4dFm50PdKlUiaImmiaxX4rFd7Kywia9dODqZdvYo0ibVmD5OEW3ktWTGP1AicR7yjmaljpgNk7pmbNmNwQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

随着大模型在单点推理上日益逼近PhD水平，Agent领域迎来了新的分水岭：短程任务表现惊艳，长程任务却显乏力。为精准评估大模型的多模态理解与复杂问题解决能力，红杉中国在两周内连续发布两篇论文，旨在通过构建更科学的评估基准，预判技术演进的未来方向。

xbench正式推出**AgentIF-OneDay**评测体系，不再单纯考核模型知道多少知识，而是衡量它解决复杂任务的能力。AgentIF-OneDay深入探索了从OneHour到OneDay的能力跨越，揭示了主流Agent在工作流执行、隐式推断与迭代编辑中的真实表现。让我们共同见证，Agent 是如何通过Scaling Context与Scaling Domain，从单纯的“提问助手”进化为真正创造经济价值的“数字员工”。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dqXgnTgtib4eiajL6Z9J9yY7icwvibxQ7lM82qlKtGL9UKU3iaCqTso1tHj5ia6ibAsBSPeqiagL5PGmg9icSNDlCGGoE6Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Agent能否协助你一天的生活？**

自从红杉中国xbench发布ScienceQA与DeepSearch以来，这两个评测集已经经历了多次迭代升级。无论是模型本身，还是围绕模型构建的Agent系统，都已经在这些以分钟级为单位的集中推理任务上能够稳定胜任，从最初的human-average水平，逐渐达到接近PhD-level的表现。

随着我们进一步进入Agent能力评测的领域，我们发现Agent完成短时任务与长时任务之间存在巨大的能力鸿沟。即便在单点推理和局部任务中已达到极高水平，一旦任务在突破一般人一小时可处理的复杂度，Agent的整体完成度就会出现明显下降。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

从xbench所坚持的理念出发，更好的评估模型和智能体在实际工作和生活中的价值。我们希望通过评测体系来观察行业技术路线的演进，预测模型能力的上限，同时也希望给业界补充一个面向utility和economic value的思考视角。我们提出一个新的视角来理解Agent的能力边界：**任务复杂度**，任务复杂度并不等同于知识点有多深奥或推理难度，而是完成一个任务所需的**人类时间投入**，并由此对应其**潜在的经济与使用价值**。

我们认为Agent能力的演进会沿着两条主线展开：scaling context与scaling domain。这两条轴线共同决定了Agent能够承担的任务复杂度上限，也是Agent系统从工具走向数字员工的发展方向。

• **Scaling context**指的是完成的任务在时间维度上的延展。随着任务复杂度的提升，Agent需要在更长的执行周期中持续维护上下文状态，跟踪中间目标与约束，并在多步骤、多工具的交互过程中保持一致性。从分钟级任务，到一天级、乃至一周级的工作量。

• **Scaling domain**则指Agent在任务类型上扩展带来的复杂度。与高度结构化、domain集中的任务（如coding或数学推理）不同，现实世界中的工作往往横跨多个领域与语境，不同任务在目标表述、隐含约束、工具使用方式与评估标准上差异显著。Agent能力的进一步提升，伴随着对更广的任务分布的覆盖能力。

xbench在设计AgentIF评测体系时，会同时沿着context与domain两个方向推进。一方面，通过逐步拉长任务对应的人类时间尺度，从OneHour走向OneDay；另一方面，通过覆盖更加多样的生活、学习与职业场景，刻画Agent 在真实世界任务分布中的整体能力边界。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

本次发布的AgentIF-OneDay是xbench在该评测系列中的一个新工作。我们以人类一天内可完成的任务复杂度作为基准，测试一个Agent是否具备在无需人类介入的情况下，稳定完成整套任务并交付结果的能力。尽量覆盖更diverse的domain，包括生活、学习和职业场景会遇到的多种多样的任务以及多种工具。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**如何构造一天的典型任务？**

在对大量用户真实工作日志进行分析后，我们发现尽管具体任务内容差异巨大，但日常工作在类型上呈现出高度稳定的模式。大多数普通人的一天可以按照使用场景被抽象为三个任务类型——工作流执行、范例参考以及迭代式编辑。

**场景一**

**当你知道该怎么做，但执行太繁琐**

用户已知完整流程并明确给出操作步骤，Agent只需精确执行。我们称此类任务为**工作流执行（Workflow Execution）**。

例题

我计划去NeurIPS 2025，帮我规划一个好的行程方案。请你**先去官网确认**NeurIPS 2025会议的主会场位置（San Diego Convention Center, San Diego）是否准确，**然后用另一个可靠来源交叉验证**这个信息，确保万无一失。接下来，**帮我收集基本信息**，比如会议时间、地点和论文提交截止日期。还要**确认完整的会议日程是否已经发布**——如果还没发布，请明确告诉我。最后，**从纽约出发给我两套去圣地亚哥的行程方案**：一个最便宜的Cheap Plan，一个最快的Fast Plan。

当Agent能够在整个流程中保持一致性、逐步完成步骤、并在长上下文中保持状态，就意味着它具备帮我把事情做完的潜力。这也是大量用户希望Agent能真正替代重复性劳动的原因——当流程执行能力成熟时，Agent就能自然承担原本需要人工耐心完成的碎片化任务。

**场景二**

**当你不知道规则，只能给个参考**

用户不明确知道完整的工作流或者条件约束，只提供若干案例或参考资料。我们将此定义为**范例参考（Latent Instruction Inference）**。

例题

我现在用的是iPhone13 Pro Max，AT&T套餐每月20美元预付费。我想换iPhone17 Pro Max。**基于附件里的购机方案和运营商优惠，帮我找出总成本最低的方式。**

范例参考是人类最自然的工作方式，人们不会每次都从零写起，而是需要Agent从提供的示例文件中挖掘出潜在的意图，并交付同时满足用户的显示指令与附件的隐式指令；Agent如果具备这种能力，就能真正参与内容生产、报告生成、数据整理等职业型任务，而不是停留在浅层回答问题的阶段。

**场景三**

**当需求本身是动态的，要边做边看**

人类的工作普遍呈现多轮迭代结构，在工作的开始并不知道完整解法、也没有参考示例，需要在与Agent多轮交互中逐渐提出新需求。Agent也必须具备在不断变化的约束下维持上下文一致性并稳定推进任务的能力。这类任务称为**迭代式编辑（Iterative Refinement）**。

例题

拿着这个SVG平面图（venue\_layout.svg）和Excel约束表（venue\_constraints.xlsx），**更新会场布局以满足所有约束条件，同时保持设计的可读性和可行走性**。

我们在过去3个月按照这三个类型，制备了AgentIF第一期的题库，总共由104道任务组成，覆盖了工作、生活（例如游戏攻略、旅游规划）和学习。其中62道由文件驱动的合成任务用于补充长尾场景，覆盖PDF、PPT、Excel、图像、代码文件在内的15种以上格式。本质上模拟了真实工作流程中极常见的跨格式、跨来源的模式。

每道任务都带有一套细粒度的评判标准，总计767个评分点，分为正向指标（如格式一致性、结构复现、步骤完整）与负向指标（如误删内容、越界生成、错误操作）。评测系统采用LLM作为裁判（值得一提的是Gemini 3-pro的出现让rubrics打分的准确性也提升到可用的程度），并结合网页检索、HTML渲染、多模态比对等方法做自动校验。在这套机制下，agent系统的得分不仅取决于它最终是否完成任务，还包括流程是否干净、是否出现误操作、是否正确解析附件、是否能在迭代过程中保持一致性。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**主流Agent的评测结果和启发**

在AgentIF的测评框架下，我们对现有主流Agent系统进行了系统化测试，也有了一些有趣的发现：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**发现一：**以Overall的完整任务成功率为标准，Manus、Genspark与ChatGPT-Agent都集中在0.62–0.65区间，构成当下能力最强的第一梯队。

这意味着和我们想象的有所差别，不论Agent系统是通过模型原生甚至RL训练出来的模型，还是基于API的工具链集成或深度的multi-Agent系统，在完成一套真实任务链时，用户侧感受到的能力是比较相近的。

这一现象在一定程度上印证了模型即Agent的判断——在底层模型能力不发生变化、且不引入test-time scaling的前提下，不同多智能体框架本身难以拉开数量级上的性能差异。基座模型会逐步集成agentic能力，下游基于api的Agent产品，在能力表现上也会体现出agent rl的能力。

虽然这些agent系统能力非常接近，但在**任务领域**上与**能力维度**存在明显差异。

**发现二：**从**任务领域**上，任务领域上从ChatGPT是最优生产力工具，Manus是最佳生活助手，Genspark是最好学习伙伴。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

三个产品具有不同迭代方向，ChatGPT-Agent重点关注GDPval，聚焦专业工作场景的体验；相对来说Manus与Genspark更侧重用户反馈。不同的评测体现带来了不同的产品长项与短板。我们认为优秀的通用Agent应当兼顾最多样的任务，而不侧重一方。

**发现三：**在**能力维度**上，GenSpark在隐式指令推断上表现最优，Manus在开放工作流执行最优，Minimax-Agent具有最好的迭代式编辑能力。

能力维度的表现不一或来源于Agent框架的差异。隐式条件推断是目前Agent普遍最薄弱的能力项。一些任务要求Agent从附件中自动识别格式规则，例如从PPT 模板中抽取页眉页脚结构或引用标注方式，再迁移到新的内容生成中。我们观察到，即便是整体表现最好的系统，在这类任务中也很难做到完全正确。要么格式复现正确但覆盖不足，要么内容理解到位但无法保持结构一致。

综合来看，稳定性、文件处理链路、隐式结构理解能力，乃至跨工具的状态管理，都是决定Agent能否真正承担一天工作量的关键环节。AgentIF-OneDay通过这类任务，揭示了当前Agent在真实使用场景中的能力边界和一些常见的失效模式，也帮助我们更清楚地看到下一阶段能力演进的方向。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**展望：从oneday、oneweek到持续学习**

随着系统能力不断提升，我们预计在2026年Agent将开始挑战one-week的人类工作量。围绕one-week的人类工作量，我们已经开始着手构建OneWeek的评测集。我们认为当一个Agent能够在一周尺度的工作量上保持稳定高质量的产出，它就具备了承担真实岗位的能力，也能够在组织内开始创造更多实际价值。

与AgentIF-OneDay相比，OneWeekIF面临的挑战并不只是任务变得更长。随着时间跨度增加，评测本身的出题难度也增加很多，rubric的设计会更加严格。一周尺度的任务往往开始呈现出明确的行业语境，无论是金融、医疗还是法律，这些高价值场景数据的获取成本也会显著上升。

当任务复杂度发展到这一阶段，依赖静态数据集和离线构建的训练与评测方式，开始显露出难以回避的局限性。也正是在这里，一个方向变得越来越自然：让 Agent在实际运行过程中具备主动学习的能力——能够在真实或半真实环境中自主收集经验，对自身行为进行评估与修正，并通过长期交互逐步形成稳定策略。

从更长期的技术演进来看，静态训练与静态评测可能都不是未来Agent系统的发展路径。近期关于online learning的讨论越来越多，更多researcher倾向于认为，如果模型只在既有的人类知识分布内循环，就无法突破到更高层级的智能，下一步的能力scaling不是训练完成的那一刻，很可能发生在模型被部署之后，通过不断的real world RL来获取practical的知识，持续学习、持续适应。

**■**

**用户数据飞轮带来高可靠Agent的出现**

一个赢得用户信任的Agent助理需要交付可靠结果，在长程任务中，错误累计效应会呈指数级放大。我们将长程任务Agent的发展类比自动驾驶的发展历程，同样是从有限路段走向通用路段，从依赖频繁人工干预走向长时无干预FSD。该过程的实现依赖于大量用户驾驶数据的积累，用户数据可以最大化拓展场景的丰富度，并给系统带来最好的泛化性。在长时任务的Agents中，我们同样可以推演，有效的数据累计可以带来高可靠Agent系统的出现，优先转起数据飞轮的公司将率先实现通用Agent的FSD时刻。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dqXgnTgtib4eiajL6Z9J9yY7icwvibxQ7lM8KiblPjU9tkc4QEeibRF0SsFBQOlZPG3hdmBEBAWnQh6xwafXyteNIiayQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

**开源链接**

**Paper Link:**

https://github.com/xbench-ai/AgentIF-OneDay/blob/main/paper/AgentIF\_OneDay\_0117.pdf

**website:**

https://xbench.org/

**github:**

https://github.com/xbench-ai/AgentIF-OneDay

**huggingface:**

https://huggingface.co/datasets/xbench/AgentIF-OneDay