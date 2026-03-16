---
url: https://mp.weixin.qq.com/s/1tyZ0InFjNDf58QYr-Ljqw
title: "OpenAI 研究员 Noam Brown：Mid-training 是新的 pre-training"
description: "实现超级智能需要通用的推理范式"
author: "拾象"
captured_at: "2026-03-09T03:09:27.581Z"
---

# OpenAI 研究员 Noam Brown：Mid-training 是新的 pre-training

两个

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxibnLTIYygr23IgTpPFUQ1PcAhxibAibFSibG9gsxZhTsvdriaSAnc89I3Z0lR5gkmVA6ujX0wru9hA5w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3tHNibnJ2jgxibnLTIYygr23IgTpPFUQ1PoiaejyyhmVNzz9BAEQZZ9UHQAygibx17M6FhPLt1ng7vspibyoGy8qI0A/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

编译：haozhen

编辑：siqi

海外独角兽原创编译  转载请注明

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxibnLTIYygr23IgTpPFUQ1PnibcmZUXiaSLSibZEicRkcRlictMAHm8MvmsvcEme3E3K6GoAowmLYYMyxQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

去年以来，随着 OpenAI 在 o1 模型中提出 [RL 叙事](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247509516&idx=1&sn=40db663d98ed3de0fd4441a5a2da893f&scene=21#wechat_redirect)，以及 [DeepSeek 发布的 R1 模型](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247511288&idx=1&sn=b3090c9105c230991f922eea0f4d901b&scene=21#wechat_redirect)解开了 RL 谜题，AI 行业进入了新范式，智能的下半场也真正开启。

如果说过去 LLM 主要依赖于模式匹配与数据记忆，如今，推理能力的兴起让模型能力从表层关联跃升到复杂认知。推理不仅仅是参数数量或训练数据的增加，而是能充分利用算力进行深度探索。因此，推理能力既是涌现智能的重要催化剂，也是未来模型在科学发现、复杂决策与 multi-agent 协作中的关键。

本篇内容是 OpenAI 研究员 Noam Brown 的最新播客。Noam 是全球最顶尖的推理研究员之一，他最知名的两个项目分别是在德扑中击败顶尖人类玩家的 AI 系统 Libratus 和 Pluribus，2022 年他又开发了首个在复杂多人策略游戏 Diplomacy 中达到人类水平的 AI，名为 Cicero。

这次播客中，他详细分享了自己在 scaling test time compute 上的前沿观点：

**•** 推理（reasoning）是模型涌现出来的能力，只有 pre-training 达到一定水平后，才能真正受益于额外的推理思考（inference）；

**•** 当前的模型需要依赖工具调用、CoT 等 harnessing（辅助装置）发挥作用，但模型最终目标是完全摆脱 harnessing；

**•** 2021 年 Noam 和 Ilya 就认为，要实现超级智能，需要通用的推理范式；

**•** 未来数据将比算力更稀缺，而强化学习能更高效利用数据；

**•** 当前 pre-training 模型是能派生其他模型的半成品，mid-training 是新的 pre-training，post-training 完成最终的细化与优化；

**•** 若未来数十亿 AI 能建立起长期的协作与竞争，逐步积累知识，或许会催生一个属于 AI 的“文明”，且随着规模扩大，模型自然会涌现复杂的隐式世界模型，这也强化了 *The Bitter Lesson* 的观点。

......

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

💡 目录 💡

   01 推理是涌现出来的能力

   02 实现超级智能需要通用的推理范式

   03 RL 可以更高效地利用数据

   04 关于推理能力的非共识观点

   05 Test-time compute 的发展瓶颈

   06 Mid-training 是新的 pre-training

   07 *The Bitter Lesson* 带给 multi-agent 的启示

   08 Noam 的 AI Coding 实践

**01.**

**推理是涌现出来的能力**

**为什么推理范式没有很早就出现？**

大家现在普遍接受的一个观点是，“快思维与慢思维”范式里所说的系统一和系统二，可以分别用来类比非推理模型和推理模型。

“快思维与慢思维”范式是由诺贝尔经济学奖得主、心理学家 Daniel Kahneman 在 2011 年出版的著作 *Thinking， Fast and Slow* 中系统提出的理论。他将人类思维过程划分为两个系统：系统一是快速、直觉、自动且情绪化的，无需刻意思考，常用于日常判断；系统二则是缓慢、理性、需要集中注意力的，主要在处理复杂或新颖问题时发挥作用。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

系统一（快思维）VS 系统二（慢思维）

但实际上，**只有当 pre-training 模型达到一定能力水平后，才能真正从额外的思考中受益的。**这也是为什么推理范式没有很早就出现的原因。当在非常小的 GPT 模型上尝试思维链时，比如在 GPT-2 上使用推理范式，是几乎没有任何效果的；但换到更大的模型的时候，它就能开始提升效果了。

用大脑进化类比，意味着你必须先进化出大脑皮层，然后再进化出大脑的其他部分，否则，就好比是你让一只鸽子去非常努力地思考如何下棋，无论它多么努力，哪怕思考一千年，棋艺也不会有实质性的提升。

所以推理模型和非推理模型并非两个独立的范式，而是相互关联的。**模型只有具备一定的系统一能力，才能拥有系统二能力，并从中受益。**

**而且，模型的系统一能力越强，对模型整体表现越有利。**在人类第一次接触国际象棋这样的新游戏时，往往会大量依赖系统二的思考，比如你让一个非常聪明的人去了解一个全新的游戏，并告诉他将要与顶级 AI 或高手对战，然后给他三周时间专心研究规则和策略，他很可能能表现得相当出色，但若能建立系统一的直觉，是可以显著提升反应速度的。

此外，在多模态任务上，是否需要系统二能力，取决于这个任务是否需要整合复杂信息和逻辑推理：

1\. 在涉及空间推理或需要整合多步信息的时候，系统二能力能发挥较好的作用，比如 GeoGuessr 和井字棋，因此 GPT-4.0 之类的全能模型在这些任务中表现优异；

2\. 相比之下，对于图像识别或无网络下的简单事实判断，系统二能力能提供的帮助就较少，因为这些任务更依赖于直接记忆或直觉识别，模型要么知道答案，要么不知道，进一步推理的空间有限。

**终极目标是构建一个强大的统一模型**

当前的模型在玩宝可梦游戏时，虽然依靠系统一能力，已经能积累丰富的游戏知识了，但在实际应用中，仍需大量的 harnessing（辅助装置）才能真正发挥包括系统二能力在内的全部潜力。

在模型训练和推理中，harnessing 指利用各种资源和技术来提升模型性能与效率的方法，包括数据增强、迁移学习、分布式训练、人类反馈微调（如 RLHF）、工具调用、链式推理和外部记忆等。

在与系统二能力的关系上，harnessing 并不等于系统二的能力，而是以类似“工具箱”的角色，来支持或增强系统二相关的推理能力。

在复杂度上，tool use < harnessing < scaffolding。Tool use（工具使用）是最基础的外部能力调用；Harnessing（辅助装置）是更复杂的外部辅助系统，可能包含多个工具和逻辑；Scaffolding（脚手架）是最复杂的外部架构系统。

**但 Noam 认为 harnessing 本质上是一种临时性的辅助装置，就像辅助人走路的拐杖，模型最终目标应是完全摆脱 harnessing，也就是将这些能力都内化到模型自身。**因此，在评估模型能力的时候，不应该通过增加 harnessing 来提升模型得分，而应着眼于提升模型自身能力，让模型自然地在各种任务中表现出色。

因此，虽然目前 o3 模型在缺乏 harnessing 的情况下表现不佳，但这是可以接受的。Noam 更关心的是，在不使用任何 harnessing 的前提下，o3 能走多远。

**更关键的是，随着模型能力的不断提升，模型目前依赖的许多 harnessing 都将逐步被更强大、更统一的模型架构所取代。**比如在推理模型出现之前，工程师们投入了大量时间，用 GPT-4 之类的非推理模型加上一整套 harnessing 去模拟推理行为，但事实证明，只要模型具备原生推理能力，就不再需要这些复杂的 harnessing，这些 harnessing 甚至可能让模型运行得更糟。

需要注意的是，与 harnessing 不同，强化学习微调（Reinforcement Learning Fine-Tuning）是一项值得深入探索的技术，它可以根据特定的数据对模型进行定制化训练，从而实现模型行为的个性化和优化。

**而且，即使基础模型本身并未包含这些数据，强化学习微调仍能赋予模型新的能力，并在未来更强大的模型问世时继续发挥作用，也就是说，并不是必然会随着模型规模的扩大而被淘汰的**，所以我们可以通过构建可复用的数据和系统来补充和增强模型能力。

**•** **工具调用**

Harnessing 提供的一个关键能力就是工具调用。在游戏中，模型是否能遵守游戏规则，主要取决于它能否自行评估自身行为是否合规。而借助工具调用，模型可以在执行动作前主动调用工具来辅助判断，而不是等到执行后再被动接受反馈。

**但模型在 test-time 的错误行为并不等同于工具调用。后者是模型主动调用工具来辅助判断，前者则是执行后再接受反馈、尝试撤销或修正。这是两种不同的思维范式。**模型可以有选择性地调用外部工具来模拟行为结果，再决定是否执行，但应避免在执行错误行动后，再撤回，并更换决策，比如在现实世界中，机器人一旦执行破坏性动作后就不可逆了。

**•** **Model Router**

**目前业界对 model router 的探索，虽然短期来看是有效的，例如在快速响应模型与深度推理模型之间做动态切换，但长期来看，这只是一个过渡阶段。**因为即使一个“笨”模型能识别自身无法处理的任务，并将其转交给更强的模型，这种机制本身也存在局限性，例如“笨”模型可能被误导或过于自信。

**未来的通用模型可能会逐渐覆盖原本由外部 model router 承担的决策功能，最终演变成一个统一的模型。**虽然现在使用 model router 确实能提升产品表现，但开发者需要高度关注模型能力的快速迭代，不要在可能很快被淘汰的工程结构上投入过多时间和资源，未来 3-6 个月，随着模型进步，现有方案可能会被彻底改变甚至取代。

**02.**

**实现超级智能**

**需要通用的推理范式**

扑克、Hanabi、Diplomacy 等游戏证明了，模型在行动前进行“思考”确实能带来成千上万倍的性能提升，但目前这一范式还没有充分迁移至语言模型领域，因为 LLM 缺少一个非常通用的推理范式。

一些专家认为只靠 pre-training 的 scaling 即可实现超级智能（superintelligence），但 Noam 认为，虽然目前可以继续做 scaling，模型的能力也会因此变得更强，但仅凭这一点，是无法实现超级智能的，因为很可能没有足够的资金支持。**2021 年，Noam 就与 Ilya 讨论过这个问题，二人当时就达成了一个共识：需要一个通用的推理范式才能实现超级智能。**

尽管当时推理范式仍处于探索阶段，但 OpenAI 内部其实就已经在进行强化学习相关的研究了，传言工作代号是 GPT-zero，尽管一开始成效不显著，但到了 2023 年 10、11 月左右，OpenAI 识别到了清晰的积极信号，之后迅速投入大量资源，最终推出了推理模型。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

scaling train-time compute and test-time compute

虽然 OpenAI 在推理模型上取得了巨大成功，但当时 OpenAI 作为 pre-training scaling 的先行者，团队内部的一些人始终相信 pre-training scaling 足以实现智能的突破，但 OpenAI 的领导层却认为需要另一种范式，单靠 scaling 不足以解决所有问题，因此 OpenAI 在有限资源下，做出这个艰难但前瞻性的决策，即优先在推理范式和强化学习上进行大量投入，尽管这意味着放弃对其他方向的部分投入。

最终 O 系列模型的发布和推理范式的提出，引起了外部的广泛关注。一位起初并不看好这一方向、后来加入其他实验室的前 OpenAI 研究人员，在 o1 发布后，对自己所在团队的反应感到非常惊讶，因为他所在的整个实验室将推理范式视为一次重大突破，甚至迅速调整了研究方向。

这也说明了，即使在专业领域内，真正的创新也常常在初期遭遇质疑。许多后来被认为是显而易见的成果，最开始往往是在充满争议和不确定性的环境中诞生的。

Noam 认为，OpenAI 的领导层和研究人员曾在多个关键节点上展现出了卓越的判断力：

**•** 如上文所述的，将游戏中的强化学习方法推广到语言模型，进而探索模型 scaling 与能力的正相关关系。虽然这些决定在今天看来似乎是自然演进的结果，但在当时，需要决策者对未来技术路径有深入的洞察。这种前瞻性不仅推动了模型本身的飞跃，也为整个 AI 研究提供了新的方向。

**•** OpenAI 联合创始人 Ilya 早在 2016 年就坚定押注于 scaling，认为一次大实验比百次小实验更具价值，他对未来研究方向的判断非常清晰且具有前瞻性，虽然当时 OpenAI 并不是资源最强的公司，但 OpenAI 有类似初创公司的结构，这使 OpenAI 能集中资源做出高风险决策，从而成功推动了大模型的发展。相比之下，传统研究机构很难实现这种集中突破。

**03.**

**RL** **可以****更高效地**

**利用数据** 

**强化学习除了可以提升模型的推理能力，还可以提高数据利用的效率，在未来数据比算力更稀缺的情况下，这一点尤为重要。**

当前机器学习在使用数据的效率上，是远逊于人类的。比如，人类常常只需要观察五个样本就能学会新概念，而模型往往需要上百个样本才能达到相似效果。因此，**如何让模型在更少的数据下能学得更好，就成为了一个重要问题。**

以打扑克这个游戏为例，目前主要有两种游戏策略，玩家往往需要在防御性的 GTO 策略和高收益的剥削性策略之间做出权衡：

1\. “博弈论最优”（GTO）策略，指的是制定一种接近无懈可击的均衡打法，让对手无法针对你的习惯进行进攻。比如在石头剪刀布中，始终以三分之一的概率随机选择手势，长期来看，期望收益也能保持稳定。

2\. “剥削性策略”，指的是在游戏中识别并利用对手特定的漏洞来进行进攻，比如若对方对诈唬反应迟钝，便可以加大诈唬力度。这种方式能获得更高利润，但也可能因暴露自身弱点而遭到反剥削。

目前最成功的扑克 AI 主要依赖 GTO 策略，几乎不会对牌桌上其他玩家的具体行为做出反应。尽管这种 AI 能够凭借极高的理性战胜人类顶尖选手，但优秀的人类高手往往是能做到迅速识别并适应对手的策略，进而采取更有针对性的剥削性打法。

AI 在这方面的效率就远不及人类，人类或许看十几手牌便能判断出玩家实力，而 AI 往往需要上万手牌才能形成可行判断。**尽管技术在持续进步，样本效率依旧是打造有剥削性能力的扑克 AI  面临的重大难题。**

这一问题也体现在 Noam 研究的 Diplomacy 项目中。

在这个七人谈判游戏里，传统的 GTO 思路是不奏效的。因为相较于扑克这类零和游戏，Diplomacy 要求玩家在合作与竞争中灵活转换，成功策略往往不是博弈均衡，而是要对其他玩家行为有深度理解，并做出相应的调整，就像是当所有人都说法语时，你就不应该坚持用英语。

Diplomacy 是一款七人游戏，玩家扮演第一次世界大战前的欧陆列强，通过谈判、结盟、背叛等手段在外交桌上瓜分欧陆利益。Noam 主要是开发名为 Cicero 的 AI 系统，用于玩这个游戏。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Cicero 是 Noam 在 Meta 期间开发的玩 Diplomacy 的 AI，也是第一个在这个复杂多人策略游戏中达到人类水平的 AI，这张图展示了它是如何结合“战略推理”和“对话生成”的

因此，在 Diplomacy 项目中，AI 研究重点就转移到了如何对其他玩家的行为进行建模并调整自身行为，而不是依赖固定的剥削性策略。

但通过在 Diplomacy 中发展出的建模技术，也许能改进剥削性扑克 AI 的构建，或许可以弥补当前 AI 在样本效率上的不足。而且，目前 AI 开发者普遍还没有充分利用 HUD 这类工具提供的统计信息（Heads-Up Display，是一种在扑克游戏中实时显示对手统计数据的工具），比如玩家翻牌率等，而这些正是人类高度依赖的关键信息。

综上所述，模型进一步突破的方向可能有两个：1）改进模型算法；2）找到更多的数据，虽然让模型从互联网的现有数据中学习是最容易的路径，但人类在学习的时候，并不是仅依赖互联网，所以互联网上的数据并不是数据上限。

**04.**

**关于推理能力的**

**非共识观点**

**•** **推理不只局限于有明确奖励函数的任务**

现在有一个共识是，推理模型在数学、coding 等易于验证的领域是可以表现出色的，但 Noam 认为，这并不意味着推理能力的进步只能在结果易于验证的领域，**即使在标准极难定义、甚至带有主观性的领域，推理模型也能表现出色。**

比如 Deep Research 所涉及的领域就是一个结果难以轻易量化的领域，但 Deep Research 的表现显然是让用户非常满意的。

因为虽然 Deep Research 交付的结果并非百分之百完美，但人们是能够区分一份好报告和一份差报告，这就已经可以形成反馈闭环，并进行后续的产品构建和模型改进。而且，如果人们无法分辨模型输出结果的好坏，那么无论模型是否在进步，对人们的意义就都不大了。

**•** **推理有助于实现对 AI 的对齐**

**虚拟助理（virtual assistants）可能是下一个重要的 AI 应用方向，因为这类任务的输入输出结构清晰，很容易用来做模型训练。**若模型能够与用户偏好高度对齐，模型的表现甚至可能会超过人类助理，但这里的“超过”并不是指能力上的压倒性优势，而是模型在执行意愿上能更忠实地贴合用户目标。

**也正因为需要模型对用户目标有高度忠实，对齐的问题就变得尤为关键：模型究竟应该和谁或和什么东西对齐。**一个模型若仅对齐于用户，可能带来伦理风险，比如若用户试图合成生物武器，那这个模型的对齐便可能危及公共安全。

在这个问题上，**很多人可能没想到，推理能力其实是一个很有效的抓手。**比如 Noam 发布 Cicero 的时候，就收到了 AI 安全圈里非常积极的反馈：因为 Cicero 不是一个“随心所欲”的语言模型，而是一个可以被明确控制的系统。人类可以通过条件约束，让它采取具体、可预测的行为，Cicero 背后有一整套推理系统在引导它与人类互动的方式。很多 researcher 觉得这可能是让 AI 系统更安全的一种好路径。

**05.**

**Test-time compute 的**

**发展瓶颈**

目前 test-time compute 的发展主要面临着两个瓶颈：

**•** **成本的限制**

Test-time compute 目前正面临 pre-training 在 scaling 时遇到的类似问题：随着每一次模型规模的扩大，模型的思考时间从三分钟延长至三小时、三天甚至三周的时候，成本也呈指数级上升，但我们能投入的成本或资源总是有限的。

在过去的模型迭代中，比如从 GPT-3 的早期版本发展到更成熟的版本，性能显著提升的关键并不只是让模型有更长的思考时间，更在于模型的思考效率本身有了很大提高，而这种效率提升往往被低估。

人们更容易关注模型是否“想得更久”，却忽视了“是否想得更好”。**Test-time compute 的可持续发展不仅依赖于延长模型思考时间，还要提升单位计算时间内的思考质量。**

**•** **模型响应的绝对时间限制**

Test-time compute 面临的第二个瓶颈是 wall-clock time（指的是从计算开始到计算结束所经过的真实时间），即模型响应的绝对时间限制。**如果每次实验都需要耗时数小时乃至数周，实验迭代的速度将大幅下降。**

目前，尽管部分实验可以并行处理，但仍有大量关键实验必须依赖串行流程，也就是必须等待前一个实验的结果输出后，才能决定下一步，这大大降低了研发效率。这种实验所需的实际时间成本也成为了支持“长时间发展路线”（long timelines）观点的一个重要现实依据。

“长时间发展路线”（long timelines）观点认为，AI 达到人类水平或超越人类智能还需几十年甚至更长时间。因为受限于算法、硬件、数据和实验周期等现实瓶颈，AI 的发展将是渐进的、充满挑战的。

而这一瓶颈在药物研发领域格外突出。因为如果要开发一款真正能延长人类寿命的药物，需要耗费大量时间验证这个药物的功效及副作用，这种时长是无法通过技术在短期内压缩。

在理想状态下，如果人类拥有完美的人体生物学或化学模拟器，就能绕过大量真实实验所需的时间与风险。但目前人类距离拥有这样的模拟器还差很远，也正是这类模拟器的缺失，限制了推理模型在这些领域中的更大潜力。

**06.**

**Mid-training** 

**是新的 pre-training**

Noam 认为，mid-training 是通过某些有趣的方式为模型添加新的能力或特性的一种手段，与 pre-training 和 post-training 之间的界限非常模糊，难以给出严谨定义，但它不同于 pre-training 中对大规模语料的广泛学习，也不是 post-training 中针对具体用途的微调，而是一个独立阶段，可以拓展模型的泛化能力和实用性。

Mid-training 是指在 LLM 的 pre-training 完成之前，对模型进行干预，比如加入新数据或更改目标函数，来引导模型的学习方向或行为，目的是比 fine-tuning 更早、更深层地影响模型内部表征。

OpenAI 在 2024 年的 GPT-4 系列模型和后续模型的训练中，在多轮训练架构中采用了类似 mid-training 的策略，包括在训练中期引入目标切换、阶段式数据注入等，来提升对齐性和安全性。

**现在的 pre-training 模型就像一个能派生出其他模型的半成品，而 mid-training 就像是新的 pre-training 阶段，post-training 则完成最终的细化与优化。**

在当前的 AI 开发流程中，pre-training 模型往往不再直接面向用户，取而代之的是已经在 mid-training 和 post-training 中加工过的模型。在 OpenAI 的早期阶段，researcher 是能直接与 pre-training 模型交互的，但现在这种权限已被收回。相比之下，一些开源模型仍允许用户直接访问 pre-training 模型。

但实际上，与 pre-training 模型交互的体验往往不佳，模型甚至会显得笨拙，而经过 mid-training 和 post-training 后的模型则更实用，更自然。这种多阶段训练的流程确保了模型不仅具备强大的基础知识，还可以针对特定任务进行能力调优。

但在某些特定场景中，post-training 为了优化对话体验可能会引发模式坍塌（mode collapse），模型生成的内容会变得过于集中或单一。尽管如此，在一些任务中，这种坍塌反而是有用的，因此也不能一概而论。

**07.**

***The Bitter Lesson*** 

**带给 multi-agent 的启示**

**Multi-agent 或将催生“AI 文明”**

Noam 透露自己正在领导 OpenAI 的一个 multi-agent 团队，这个团队虽然名为 multi-agent，但这只是研究方向之一，另一核心方向是提高模型在推理阶段的计算投入，比如将模型的思考时间从 15 分钟提升到数小时甚至数天，从而能够解决更复杂的问题。

Noam 研究 multi-agent 的原因之一在于，**他认为当前 AI 的能力仍处于石器时代，而人类之所以能够实现登月、开发核能等成就，并不是因为人类个体在历史进程中变得更加聪明，而是因为在漫长的文明演化中，无数人不断地协作与竞争。**

**若未来数十亿 AI 能像人类一样，建立起彼此之间长期的协作与竞争，并逐步积累知识、优化技能，或许也会催生一个属于 AI 的“文明”。**到那个时候，AI 的能力和创造力将远超现有的水平。**这种 AI 文明构想的核心，不在于个体模型智能的增强，而在于它们之间长期互动的结构设计。**

也正是基于这个理念，Noam 指出，他所在团队的方法论与当前主流的 multi-agent 研究方向截然不同。传统的 multi-agent 研究方法长期依赖人工设定的启发式规则，这与 *The Bitter Lesson* 所揭示的经验是相悖的。

*The Bitter Lesson* 表明，系统性的规模化训练和实证驱动的方法，往往优于人类手工设计的策略。为此，Noam 和团队正在探索一种更加有原则性的研究路径。

**值得注意的是，Noam 认为，随着模型规模的扩大，模型会自然而然地发展出更复杂的隐式世界模型，因此不一定需要刻意构建显式模型。**模型在与人类或与其他 agent 互动时，表面上看，模型需要明确建模对方的行为，但其实只要模型能力足够强，就能自然发展出“心智理论”（Theory of Mind），也就是有理解和推测他人动机的能力。

在机器学习和建模中，显式模型（Explicit Model）是指通过明确的数学公式或规则直接描述出系统关系的模型；隐式模型（Implicit Model）则不直接给出解析表达式，而是通过数据、抽样或分布来间接刻画系统。

心智理论（Theory of Mind）指的是个体能够理解并推测他人具有独立的信念、意图、欲望和情感，从而据此预测或解释他人行为的能力。

这也再次强化了 *The Bitter Lesson* 的观点：与其依赖人为设计的启发式规则，不如通过扩大模型规模与数据量，利用更通用的方法获得更强能力。因此，通向通用智能的道路最终可能并不是依赖人工设计的策略和规则，而是通过训练足够强大的模型，使它们在与世界及彼此的互动中自我演化。

**AlphaGo 的自博弈方式不能直接泛化**

自博弈正成为 AI 系统演化中的重要路径。

AlphaGo 和 AlphaZero 最初就是用人类的棋局来进行大规模 pre-training，类似于当前语言模型用互联网上的数据进行训练，之后引入 test-time compute，例如蒙特卡洛树搜索（MCTS），显著提升了模型水平。

极大极小均衡（maximin equilibrium）是博弈论中的一种策略概念，指玩家选择能最大化自己最小可能收益的策略，也就是在最坏情况下仍保证收益尽可能大。

**•** **非零和博弈：自博弈缺乏明确的优化目标**

一旦脱离双人零和博弈的框架，极大极小策略就失去了原有的效果，甚至反而不利于取胜。比如，在数学领域，如果套用自博弈机制，那就是让一个模型不断提出极难的问题，然后让另一个模型去负责解决，这可能会导致模型生成大量高难度却无意义的任务，类似 30 位数乘法。这类“进步”并不真正符合我们对智能提升的期望。

**目前在非零和博弈场景中，自博弈是缺乏明确的优化目标的，目标函数变得模糊复杂，因此 AlphaGo 式的自博弈范式在这些领域中难以直接迁移。**

**•** **非完全信息博弈：游戏复杂程度上升后，传统方法会失效**

德州扑克这样的游戏属于非完全信息博弈，但德州扑克隐藏的信息量其实相对有限，特别是在单挑场景下，仅有 1326 种可能的底牌组合。这种情况下，AI 可以通过枚举所有可能状态，并为每种状态赋予一定的概率，借助神经网络来制定对应策略，最终达到超越人类水平的表现，即使在面对多人游戏（如六人桌扑克）时，虽然可能的状态数量会显著增加，但仍在 AI 可以处理的范围内。

然而，随着游戏复杂度的上升，这个方法就会迅速失效：

1\. 在奥马哈扑克中，玩家手中有四张底牌，即使采用启发式方法来缩减状态空间，问题依旧难以解决；

2\. 在西洋陆军棋（Stratego）中，每位玩家需操作 40 个棋子，因此隐藏状态的数量会接近 40 的阶乘，在这种巨大的组合空间下，在扑克中行之有效的方法就很难奏效，这也让如何应对更高阶的隐藏信息量成为一个尚未解决的重要问题。

3\. 在万智牌（Magic: The Gathering）中，这是非常复杂的策略游戏，目前在扑克中成功应用的技术同样难以直接套用，这一挑战在尝试应用搜索技术时会尤其明显。

但如果转向无模型强化学习，则可能不再受限于搜索本身。因此，只要投入足够的资源和研究，可能能构建出能在万智牌中达到超人水平的 AI。这些挑战虽然在学术上很有趣，但可能并非最重要的研究方向。因为当前用于扑克的搜索技术本身就相对受限，即使增大规模，也只能在某些博弈游戏中发挥作用，难以适用于 Codeforces 这类编程竞赛平台。

无模型强化学习（model-free reinforcement learning）是指在学习策略时，不显式构建环境的动态模型，而是直接通过与环境的交互来估计价值或学会动作选择。

相比之下，Noam 更看重发展通用的推理技术，他认为，随着研究不断推进，未来可能会出现更通用的模型，这类模型无需专门微调就能直接在如万智牌这类复杂环境中展现出超人水准。这会是更值得投入和关注的长期研究方向。

**08.**

**Noam 的 AI Coding实践**

Noam 日常大量依赖 Codex 和 Windsurf 来处理编程任务，尤其倾向于让模型独立完成代码编写。这些工具已经成为他最常用的开发方式，因为这些工具不仅能显著提高开发效率，还能帮助他更直观地了解模型的优势和局限。例如，他常常直接把一个任务交给 Codex，十分钟后再回来查看生成的 pull request。

**值得注意的是，Noam 交给模型做的任务并不仅仅是一些辅助性工作，而是他原本自己会亲自完成的核心开发内容。**他表示，在使用模型进行编程时，时常会感受到一种“AGI 即将到来”的冲击感。

在多模态领域也是如此。Noam 在看到 Sora 生成的视频时，同样感到震撼，虽然反复观看后，也能注意到动作不够自然、画面缺乏一致性等问题，但他认为技术进步的速度极快，几乎每隔几个月就会出现新的突破，引发一次新的“magic moment”。这种节奏让人对新工具的惊艳逐渐习以为常，同时也不断推动整个行业向前演进。

除了 Codex 和 Windsurf，Noam 也每天使用 o3，许多任务已经不再依赖 Google 搜索。他建议程序员，特别是还没尝试过推理模型的人，应该亲自体验一下，因为这些模型的实际表现往往超出预期。不过，o3 在推理速度上仍有短板，不太适合用于需要即时响应的结对编程，这类场景更适合使用响应更快的模型，比如 GPT-4.1。

相比之下，Codex 更擅长处理相对独立、耗时较长的任务，用户可以先把工作交给模型，再去做别的事情，等它生成完结果再来查看。

**目前编程模型的一个显著不足是无法积累任务经验。**即使连续处理两个几乎完全相似的任务，模型依然会分别花上十分钟，这导致模型就像一个永远处在“入职第一天”的新手，这极大限制了整体效率的提升。要让 AI 编程真正实用，必须建立某种机制，使模型表现得更像一位已有几个月经验的同事，而不是始终从零开始。

**在整个开发流程中，模型目前最薄弱的一环是 Pull Request 评审。**虽然模型已经能独立生成大量代码，但在审核大量 PR 时，仍然需要人工逐一检查，效率低且难以规模化。Noam 希望社区投入更多资源，开发出能自动化完成这一步的工具。

以 Codex 的环境配置为例，o3 模型理论上完全可以根据代码仓库自动生成配置脚本，但目前仍需人工操作，这并不是因为模型做不到，而是还没有足够的工程投入。不过 Noam 预计，未来六个月里，o3 将迎来一次质的飞跃。

从更宏观的角度看，AI 的应用前景远不止软件工程。所有与远程办公相关的任务，比如在 Upwork 上的自由职业项目，未来也都将逐步被 AI 覆盖。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 排版：夏悦涵

延伸阅读

从 Co-pilot 到 Agentic AI，Sierra 如何改变客服的游戏规则

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

FutureHouse 联合创始人：AI Scientist 不是“全自动化科研”

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

对谈斯坦福 Biomni 作者黄柯鑫：AI Scientist 领域将出现 Cursor 级别的机会｜Best Minds

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxibnLTIYygr23IgTpPFUQ1PjxPfJw2xiaBEjkJL6QaSWjiba0kkaQtAezLR1Pj7r3T6ibOvO1n4RscLw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

AI4Science 图谱，如何颠覆10年 x 20亿美金成本的药物研发模式

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxibnLTIYygr23IgTpPFUQ1PjxPfJw2xiaBEjkJL6QaSWjiba0kkaQtAezLR1Pj7r3T6ibOvO1n4RscLw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

Granola：ChatGPT、Notion 都入场的 AI 纪要，能真正沉淀工作流吗？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxibnLTIYygr23IgTpPFUQ1PjxPfJw2xiaBEjkJL6QaSWjiba0kkaQtAezLR1Pj7r3T6ibOvO1n4RscLw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19)