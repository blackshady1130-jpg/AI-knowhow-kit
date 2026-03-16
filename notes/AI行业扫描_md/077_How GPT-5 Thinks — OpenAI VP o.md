---
url: https://mp.weixin.qq.com/s/dGSQpmkcpuTZ3vCpjHjxxA
title: "GPT-5 核心成员详解 RL：Pre-training 只有和 RL 结合才能走向 AGI"
description: "与 pre-training 相比，scaling RL 的难度更大"
author: "Haozhen"
captured_at: "2026-03-09T03:24:36.445Z"
---

# GPT-5 核心成员详解 RL：Pre-training 只有和 RL 结合才能走向 AGI

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgx6icO7vRrAmA8ZnwE5D36ZpHyBia8drbfk73HXgNnNibuEDAQBM4n5ic1kKjKHePRmib6KibwyldK3Vhbw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

编译：Haozhen

编辑：Siqi

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgx6icO7vRrAmA8ZnwE5D36ZpJiczn8KPHLJn59tMHkNSz3apeicg3HicMoz0CJ590QIhQrkZSrIhr84TQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

强化学习之父 Richard Sutton 曾表示，当前以模仿为主、缺乏与现实持续交互能力的 LLM 路径存在根本性缺陷，是一条“死路”（dead end），难以真正通向 AGI；相比之下，RL 可以让模型与环境互动，并从经验中学习，是一条更可行的发展方向。

但就在今天，Andrej Karpathy 在最新访谈中表示，传统 RL 是非常低效的，只是目前尚无更好的替代方案，未来的智能系统不会依赖 RL 这单一技术。

为了深入了解 RL，我们编译了 OpenAI [GPT-5](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247516719&idx=1&sn=302c937188de1b79c78192713d0006a6&scene=21&token=1715654713&lang=zh_CN&poc_token=HLI782ijowAlqDNLBpblMQeC8UfJOflg28RODip1#wechat_redirect) 的开发者、研究副总裁 Jerry Tworek 的最新访谈。在他看来，许多关于 LLM 究竟是通向 AGI 的“入口”还是“死路”的争论，焦点往往集中在 pre-training 上。他认为，仅依赖 RL 并不足以实现 AGI，RL 必须建立在强大的 pre-training 之上，而 pre-training 同样离不开 RL 的强化与闭环：

**•** GPT-5 可以看作是 o3.1，是在与 o3 相同技术路线上的一次迭代升级；

**•** RL 环境需要具有互动性，环境会随着模型的行为而演变；

**•** AI 在不断变聪明，数据标注公司必须不断改变标注的数据类型，否则就会落后；

**•** 现在大多数针对语言模型的 RL 都是 online 的，但这种 online 其实依然是在训练阶段完成的，也就是在与真实用户分开的环境中进行训练；

**•** 终极问题：模型什么时候才能在无需大量外部干预，也不依赖人类修正的情况下，自主进行改进？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**01.**

**推理不是搜索，是一个找未知答案的思考过程**

 **Matt Turck：****从宏观角度来说，reasoning（推理）到底是什么意思？当我们和 ChatGPT 对话时，它说自己在 thinking（思考），背后实际上发生了什么？**

**Jerry Tworek：**Thinking process（思考过程）是 reasoning 一个很好的类比。在 AI 早期，我们一直有一个目标和梦想，就是教模型学会推理。比如，当一个人面对一个非常困难的问题时，很少有人能立即给出答案。有时他们需要去寻找答案，有时他们需要进行某些计算，有时需要查找信息，有时需要自我学习一些东西。

推理的过程就是找到一个答案的过程，而在此之前你并不知道答案。在某种意义上，这可以被称作 search（搜索），但它又不完全是。Search 这个词本身带有很多含义。推理就是找到一个答案所需的工作和过程，这通常比一般意义上的“回答问题”要长。

我认为，“回答问题”意味着你已经知道答案，你只是把答案说出来；而推理则是去寻找一个你未知的答案。一般来说，不管你需要做哪些工作，你花在找到这个答案的过程中的时间越长，结果通常会越好。

 **Matt Turck：****OpenAI 自从在 2024 年 9 月发布 o1 以来，大家对 chain of thought 这个概念已经非常熟悉了。用通俗的话说，当你向 ChatGPT 提问时，它会显示出一些小步骤，向你展示它的推理过程。那么 CoT 实际上是在做什么？**

**Jerry Tworek：**语言模型在最基本的层面上常常被称为 “next token prediction machines”。在 RL 时代，这种说法并不完全准确，虽然语言模型确实主要还是在处理 token，这些 token 多数是文本，但如今的语言模型其实已经是多模态的，它们也可以处理多种类型的文本信息。

简单一点来说，语言模型会生成文本，而 CoT 就是它把自己的思考过程用人类的语言和概念表达出来。我们之所以能看到模型的这种 CoT，是因为在训练过程中，模型接触了互联网上大量的人类知识和人类思维过程。模型在某种程度上开始学会像人类一样思考，并通过大量文本中人类的行为，来学习如何得出答案。CoT 基本上就是在语言模型中引出这种“像人类一样思考并找到答案”的能力。

早期的 CoT 研究大多集中在解决数学谜题。第一个，也是最著名的用于引出语言模型 CoT 的 prompt 就“let’s solve it step by step”（让我们一步一步来解决它）。

有一个典型的现象是，如果你直接问语言模型一个数学表达式或谜题，它会尝试给你答案，它会去预测下一个 token，但它通常会失败，因为这个题很难，模型无法在一个 token 的预测中就完成计算。但如果你对它说“please do it step by step”，它就会开始思考，它会说：“我不知道最终答案，但获得答案的第一步是这个。”接着它会写出 CoT，也就是一系列文本、token，分别对应计算的第一步、第二步，直到最后一步。然后它把这些步骤连接起来，就能得到答案。

所以，CoT 本质上就是一种用文字编码的思考过程，就像人类在纸上解题一样，从起点一步一步推到终点。

 **Matt Turck：****既然用于 thinking 的时间在 reasoning 中如此重要，那么模型是如何决定要思考多长时间的？当我们使用 GPT-5，并开启 auto 模式时，AI 会自动决定思考多长时间，在这个过程中到底发生了什么？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Jerry Tworek：**当模型有一个 thinking process（思考过程）时，就必须在两件事之间做出平衡：

1\. 输出的质量：模型思考得越久，结果就越好，我们在发布 o1 时也展示了非常好的 scaling laws。

2\. 人们不喜欢等待：等待的时间本可以用来做别的事，每个人都希望尽快得到结果。

我听说过一句话：“cheap，fast or good，pick two”（便宜、快、好，你只能选两个），这同样适用于语言模型。这其中有一个微妙的权衡。这也是为什么我们会把这种权衡的一部分交给用户，让他们自己选择高 reasoning 模式或低 reasoning 模式。其实这在本质上是同一个模型，我们只是调整了一个参数，告诉它“思考得更久”或者“思考得更短”。

我们也尝试引入了一些规则，用来预测用户在什么时候会愿意多等一会儿来换取更好的答案，在什么时候会希望更快拿到结果。这其实是在尝试去预判用户的期待，在具体场景下找出对他们而言合适的思考时间。

 **Matt Turck：****所以这其实更多是由用户驱动的，属于用户体验层面的事情？**

**Jerry Tworek：**是的。问题就是，你愿意等多长时间来得到一个答案。

 **Matt Turck：****自从你主导发布了全球首个 reasoning model，也就是 o1，到现在已经过去一年多了。从那之后，OpenAI 还发布了 o3、GPT-5。你如何描述过去这一年中这三个模型在 reasoning 方面的进展？**

**Jerry Tworek：**从某种意义上来说，我会把我们的推理（reasoning）或 RL scaling 计划描述为一系列逐步 scaling up 的训练实验。每一次我们都尝试做得更进一步，规模更大，目标是训练出比上一个模型更好的模型。但我们不会把所有训练出来的模型都发布出去，有的会发布，有的我们觉得要等到合适的时机，才能让它真正在用户手中发挥作用。

o1 是我们决定发布的第一个模型，它的主要能力其实就是解谜题，还包括一些零散的思考类问题，但它并不是一个非常实用的模型，更像是一个技术展示，而不是打磨完善的产品。但我们觉得它很酷，想以 OpenAI 的身份分享给世界。

o3 是真正开始变得有意义、有用的模型。虽然这听起来有点自我推销，但这确实是我开始大量使用 GPT 的时候。从那时起，我几乎彻底迷上了 reasoning 模型，现在我在 ChatGPT 上几乎只使用 reasoning 模型，因为它们的输出结果是我真正可以相信的。我认为，o3 能够使用工具、各种来源的上下文信息，并且最终找到答案，确实标志着 AI 发展历史上的一次重大变化。

我认为，o3 在使用工具、从多个来源获取和利用丰富的上下文信息，并且持续寻找答案的能力上，确实带来了非常大的突破，这在某种程度上是 AI 发展轨迹上的一次“板块级”转变（a tectonic shift）。

从某种意义上来说，GPT-5 可以被视为 o3.1，它是在与 o3 同样的技术方向和概念基础上的一次迭代。而我和我的团队现在追求的是“下一步”，也就是一次真正更大的飞跃，去实现模型更强的能力，让它能够思考更长时间，并且在自己的推理过程中与更多系统和信息源进行交互。

与此同时，我们也在 o3 技术的基础上构建了很多东西，比如 Codex。我认为目前 coding agents 是第一批真正成功的 agentic 产品，除此之外，还有 computer using agent，现在叫 ChatGPT agent，以及一些研究项目和其他产品。我们会持续在 o3 这一代的基础上不断构建和扩展。

**02.**

**Pre-training 和 RL 是如何结合的？**

 **Matt Turck：****对于现代 AI 系统（备注：这里指的是 OpenAI 截至 2025 年 10 月的 AI 模型），本质上是不是 pre-training 和 RL 的结合？如果是的话，这两者是如何协作的？**

**Jerry Tworek：**如今的语言模型基本上可以理解为先进行 pre-training，然后在这个基础上做 RL。没有 pre-training，RL 是无法奏效的，但光靠 pre-training，也存在许多难以解决的问题，如果不引入类似 RL 的东西，这些问题很难被克服。

所以，我认为 pre-training 和 RL 都会长期存在，也都非常关键。未来它们如何组合，可能会不断演变，不应该被视为一成不变的。我们必须持续探索如何训练出更好的模型，而这正是我们在努力做的事情。

这其实是 OpenAI 从一开始就定下的战略。

要说这个战略的前瞻性，我要特别提一下 Ilya Sutskever。我在 2019 年初刚加入 OpenAI 时，当时有一次全员研究会议，Ilya 上台讲 OpenAI 的研究路线图以及我们要追求的方向。他在 2019 年年初说的目标就是：在尽可能多的数据上训练一个大型生成模型（large generative model），然后再对它进行 RL。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这就是 OpenAI 当时的研究计划，这也正是我们今天正在做的事情，虽然今天算法变了，架构也变了，我甚至不认为 Ilya 当时在想 transformer 架构，那时 GPT 还只是小玩具级项目。但这正是 OpenAI 如今所执行的路线。

 **Matt Turck：****你能用非常简单的方式，像给十岁孩子解释一样，说明一下什么是 RL？**

**Jerry Tworek：**我通常用的比喻是，RL 就像训练一只狗。小的时候，我父母请人来教我一些训练狗狗的技巧，他教的方法很简单，口袋里要随时准备好奖励。每当你看到狗狗做了正确的事情，你就要微笑并给它奖励。每当它做了不对的事情，你就忽视它、转过身去，表现出不开心。经过一段时间，狗狗就会学会：正确行为会得到奖励，不良行为会带来负面结果。这就是 RL 的基本思路。

对于模型来说，也是类似的做法。我们让模型面对各种挑战性场景，然后：

**•** 当它做出我们想要的行为时，就给奖励；

**•** 当它做出我们不想要的行为时，就给惩罚或负奖励。

做 RL 的正确方式，是要平衡这些奖励和惩罚。比如，你可以一半时间给奖励，一半时间给惩罚，但最关键的部分是：模型产生正确行为，奖励好行为。这样，模型在未来就更可能去做你希望它做的事情，而不太可能去做你不希望它做的事情，从而不断改进。

这就是训练模型按照你的期望行事的方式，不像传统 pre-training 那样只是做 next token prediction，在 pre-training 中，你是训练模型去预测下一个 token，而 RL 用的是完全不同的方法和目标，你想要模型学到的行为和结果也是完全不一样的。

 **Matt Turck：****在 RL 中，policy 是什么意思？**

**Jerry Tworek：**Policy 指的是模型在不同情境下的行为方式。当模型的权重确定后，它在不同场景下的表现就是它的 policy。

从数学角度来看，模型本身是一个数学对象，可以被明确定义。而 policy 则是一个数学函数，它将观测（observation）映射为动作（action），也就是，模型根据看到的东西去决定做什么。

 **Matt Turck：****所以 policy 其实就是模型本身，也就是模型在执行任务时的行为。Reward 是用来判断这种行为是好还是坏的方式，environment 则是环境。现在人们经常谈到为 RL 设计合适的环境，这是什么意思？**

**Jerry Tworek：**环境（environment）可以理解为模型所能看到的一切。但 RL 环境与传统的监督学习或无监督学习不同，RL 的环境需要具有互动性，环境会随着模型的行为而演变。

就像学吉他一样，你拿起吉他弹奏，你会听到自己弹出的声音，然后根据声音调整下一步的动作。RL 的环境也是类似，世界会对模型的行为做出反应，模型的行动会受到环境反馈的驱动。这是训练 agent 学会对环境变化作出响应的唯一方法，也就是 RL 的核心。

 **Matt Turck：****你能讲一下 RL 发展历程吗？现代 RL 与历史上的 RL 主要有哪些不同？**

**Jerry Tworek：**早期的 RL 非常基础，RL 本身是比神经网络更早出现的，它是一种通用的数学方法，用来在数学定义的环境中优化行为，也是一种优化策略的工具。深度强化学习（deep reinforcement learning）基本上就是 DeepMind 的发明，就是把神经网络和 RL 结合起来，也就是我之前提到的 DQN。

之后有一段时间，RL 在游戏领域成为了非常活跃的研究方向。我在 2019 年加入 OpenAI 时，它已经很流行了，虽然成果还不是特别成功，但 RL 已经能够解决一些游戏问题。

但是瓶颈在于，当时的模型没有经过任何 pre-training，它们只是学习各种行为、玩游戏，比如 AlphaGo 就是那时候出来的，虽然让很多人非常兴奋，但本质上还是在训练行为，模型本身并没有对这些行为有真正理解。可以说，它们还不够聪明。

总的来说，那段时间的 RL 研究确实有很多理论和实践上的收获，但没有 pre-training 的 RL 在某种意义上是走不通的。

在我做完机器人项目之后，我开始着手教语言模型编写代码。拥有 Pre-training 模型这件事是非常重要的，而 GPT 时代的 scaling 以及大规模摄取海量数据来训练优秀模型的方式，让我们在那个阶段就已经能够开始做 RL。这也是我最早做的事情之一，几乎每次 GPT 模型 pre-training 结束后，我就会立刻尝试在它上面做 RL。但当时系统有些笨拙，很难搞清楚到底什么是正确的算法，什么是合适的研究问题，以及该用什么样的算法来训练它。当时 OpenAI 基本上是照搬了许多在游戏中使用过的方法，然后用在机器人上。

我第一次做 RL 的时候，我们用了大量相同的 PPO 算法来应对所有问题，也确实得到了一些成果，虽然我个人一直相信 RL 和语言模型结合会迎来一个真正的爆发时刻，但那些早期成果并没有在 RL 领域带来惊人的突破。

PPO（Proximal Policy Optimization）是一种强化学习中的策略梯度算法，通过限制新旧策略更新的幅度来稳定训练过程，兼顾了性能和易用性。

有一个有趣的事情是，虽然现在大家都觉得 GPT-4 是一个非常强大的模型，但当我们刚训练完 GPT-4 时，团队内部其实相当失望。我们花了很多钱训练了它，但它给我们的感觉很笨，至少在当时看来，相比 GPT-3，它并没有明显好太多。我们发现，它在只有一个 token 的评估测试中表现得似乎很聪明，能对复杂问题给出很详细的回答，但如果让它说得更长，它就不太连贯，或者一旦它必须长篇回答时，表现就变得很一般。

因此，如何才能让一个在某种程度上看起来聪明的语言模型，不仅在一次回答中表现得很聪明，还能够在长对话中持续展现出稳定而出色的表现？

这时，一个几年前已经被开发出来的技术发挥了作用，也就是 RLHF。它本质上就是在大语言模型上做 PPO，但奖励信号来自人类偏好：通过人类对比两段输出，来给出偏好反馈，从而指导模型训练。比如文本点赞或者点踩就是一种非常好的奖励信号，因为让模型生成更好文本的训练方法有很多，早期的 GPT-4 在文本生成上存在很多问题，RLHF 能够捕捉这些问题并进行纠正，奖励好文本，同时惩罚差文本。

最终，GPT-4 加上 RLHF 作为一个整体，带来了大家看到的 ChatGPT 时刻。这不仅是 pre-training 的大成功，同时也是 RLHF 的巨大成功。

 **Matt Turck：****作为用户，我们非常熟悉界面上的点赞和点踩，但实际上 RLHF 是在 post training 进行的？这个过程具体是怎么操作的？**

**Jerry Tworek：**我们在 GPT 做 RLHF 已经做了很长时间，同时，我们也在为 RLHF 收集数据，但什么才是训练模型的合适数据？什么才是训练 reward 的合适数据？以及该如何设计和塑造这些 reward？这本身就是一个持续进行的研究方向，非常开放，也非常深，包含许多不同的层面。我认为虽然有论文专门讲 RLHF 是什么，但这其中的深度远不止论文所写的那样。

简单来说，现在我们有所谓的 AI trainers 会去查看模型的输出，然后对这些输出打分。接着，我们就根据这些打分去训练一个奖励模型（reward model），再用这个奖励模型来指导主模型的训练过程。

这就是 Scale AI 等数据标注公司的工作。但我认为，随着模型越来越聪明，这种工作逐渐会成为过去式。但几年前，尤其是在 GPT-4 的阶段，这确实是很重要的一环。数据标注行业有趣的一点是，它必须不断自我更新，因为 AI 在不断变聪明。有些事情几个月后 AI 就能自己做了，你就不需要再去标注了。所以你必须不断推动前沿，改变你标注的数据类型，否则你就落后了。

 **Matt Turck：****Pre-training、无监督学习（unsupervised learning） 和自监督学习（self-supervised learning）之间有什么区别吗？**

**•** 无监督学习（Unsupervised Learning）是一种不依赖人工标注数据的机器学习方法，模型从未标注的数据中发现结构或规律，如聚类或降维。

**•** 自监督学习（Self-supervised Learning）是一种利用数据自身结构自动生成“伪标签”来训练模型的学习方式，本质上是监督学习的一种特殊形式，但不需要人工标注。

**Jerry Tworek：**我认为有一些细微的差别，但并没有那么绝对。

之所以我们把 pre-training 称为无监督学习，是因为按照某种定义，你不需要给输入模型的数据额外加任何标签。你只是把文本原封不动地输入模型。

但你也可以说这些数据其实已经自带标签了，因为它是自标注（self-labeled）的。比如，你给模型一段文本，然后让它去预测这段文本的下一个部分。从这个角度看，它其实就是一种自监督学习，因为我们并没有明确告诉模型什么是对的、什么是错的，也没有告诉它我们希望它输出什么、不希望它输出什么。我们只是让它去预测后面的数据。同样的原理也可以用在图像上，比如你可以把一张图片的一部分遮住，然后让模型去预测被遮住的那一部分图像。

在经典的 machine learning 概念中，当我们谈到监督学习（supervised learning）时，通常会有 targets （目标）和 labels（标签）的明确概念。典型做法是：你有一组目标，然后你希望模型从目标中预测对应的标签，这是一种映射关系。但实际上，目标中的信息量通常远远大于标签中的信息量。而研究目标数据本身的结构，往往能获得比单纯拟合标签更丰富的学习效果，并进一步催生更强的智能。

因此，将大量算力投入到直接学习数据本身而不是标签，是一种更高效、更合理的方式。这也就是通常所说的“表示学习”（representation learning）：通过研究和理解数据本身的结构来获得能力。

 **Matt Turck：****你之前在推特上提到 GRPO，GRPO 是什么？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Jerry Tworek：**简单来说，GRPO 是 DeepSeek 开源发布的算法。之前 DeepSeek 发布了一个 pre-training 模型和一个 reasoning model，同时开源了算法，还开源了他们做的很多事情。整体来说，这是一次非常出色、技术上非常扎实的发布。当时的讨论一部分围绕着他们如何以相对低的成本完成了 pre-training，另一部分则围绕着他们把 reasoning process（推理过程）也公开了。

而这件事发生的时间点，距离我们发布 o1 模型其实并不远。据我所知，o1 的发布在很大程度上让很多美国 research labs 感到意外，当时基本没有其他实验室拥有类似的 RL 研究项目。

但 DeepSeek 在某些方面做的 RL 研究和我们非常相似。需要注意的是，我们在 OpenAI 做的并不是 GRPO，本质上有许多不同之处，但确实有一些部分是相似的。最重要的一点是，这两者都是大规模的 policy gradient algorithms（策略梯度算法），DeepSeek 所做的研究是和我们在一个非常相近的技术方向上。

当我们发布 o1 并向全世界展示了通过对语言模型进行大规模 RL 可以得到非常优秀的推理能力时，对 DeepSeek 来说，要复现类似的成果并不是一个很大的门槛。于是他们就去做了。他们训练了自己的 reasoning model 并对外发布，而且是在我们发布 o1 不久之后，对当时那些还没有成熟的推理模型研究计划的 labs 来说，这个开源相当于一份现成的操作说明书，可以基于这个起点，快速启动并训练出自己的推理模型，而不用自己一点一点摸索所有细节。

**03.**

**只做 RL 是无法实现 AGI 的**

 **Matt Turck：****Scaling RL 需要什么条件？**

**Jerry Tworek：**首先，非常重要的一点是要明白，RL 很难（RL is hard）。

**•** 从概念上来说，RL 背后有很深的复杂性。

**•** 从抽象的数学角度来讲，pre-training 其实是非常简单的事情，是最基础、简单的数学操作之一，而且过去几年中，人们已经对它进行了大量的优化，把这种简单的数学操作做得非常高效、可扩展。相比之下，RL 复杂得多。在一次 RL 的训练过程中，有更多的事情在同时发生，也有更多的地方可能出错，尤其当你把它 scaling 到大规模的时候，你会遇到更多类型的瓶颈、更多失败的可能性。这是一个更精细、也更脆弱的过程，出错的空间要大得多。

可以想象这样一个对比：钢铁厂生产钢铁的工艺是相对标准化的，产出的钢锭是统一、规则、定义清晰的，但造芯片就完全不一样了，全世界只有极少数公司能够做到，因为在这个过程中有成千上万件可能出错的小事，你必须对细节保持极高的注意力，才能生产出高质量的芯片。某种程度上，pre-training 与 RL 的关系有点类似钢铁厂和芯片厂。

但我并不是贬低 pre-training 的技术难度，要把 pre-training 做到大规模、做得好，本身也非常困难且技术含量很高。但 RL 里有更多的组件、更多的动态部分需要同时正确运转。只有把这些要素都处理好，才能成功完成一次大规模的 RL 训练。

 **Matt Turck：****ChatGPT agent，也就是 agentic AI，和 tool use、agent 自主性、推理、RL 之间到底是怎样联系在一起的？**

**Jerry Tworek：**我相信 AI 可以通过自动化、通过解决问题、通过为我们做我们想要它做的好事，对我们的世界和生活产生非常积极的影响，而且这种影响会持续很长时间。

最近 2、3 年，我们一直生活在这样一个世界里：我们向 AI 提问，AI 几乎立刻给我们答案。一开始是瞬间完成，现在它可思考一两分钟。虽然两分钟听起来很长，但想想 AI 在两分钟里解决掉的问题，其实速度已经相当快了。但现在仍然有很多需要 AI 花费更长时间才能完成的任务。

我们在内部也已经做了许多工作来让模型能够持续工作更长的时间，但我们还没完全找到合适的产品形态来部署这种能力。现在模型在某些类型的任务和问题上，已经可以思考 30 分钟、1 小时、2 小时，甚至更久。而且，它们确实已经有这样的能力。接下来，我们需要想办法让这种过程更有用，并且能真正用于现实生活中的各种问题，无论是写代码、预订旅行、制定计划，还是设计房屋、新的电子设备，或者其他我们希望模型能为我们完成的事。很多这样的能力都来自让模型能够更长时间地自主思考，考虑更多备选方案，并且在某些时候一步步推进，完成那些很长的任务清单。

 **Matt Turck：****这些 agentic 系统是由基础推理能力驱动的。那么是否存在 online RL，也就是说，当 agent 在现实世界中行动并学习时，RL 可以实时发生？**

**Jerry Tworek：**总体来说，现在大多数针对语言模型的 RL 都是 online 的，但这种 online 其实依然是在训练阶段完成的，也就是在与真实用户分开的环境中进行训练。

最近，世界上已经有少数几个团队，比如 Cursor，正在尝试让模型在和用户交互的过程中直接进行在线训练，把用户也纳入训练循环中。从理论上来说，这确实是可行的，比如可以让模型在 ChatGPT 或其他产品中，通过对用户的响应以及从用户那里获得的奖励信号来进行 RL。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

但至少目前 OpenAI 并没有采用这种做法。虽然这种方式可能会带来很好的效果，但也可能非常危险，因为在这样的循环中，你实际上很难真正控制强化的到底是什么，可能会出现不可预期的结果。所以，至少在我们拥有非常可靠的安全保护措施之前，我认为我们不应该在像 ChatGPT 这样复杂且大规模的系统上尝试这种做法。

 **Matt Turck：****Alignment（对齐）和 RL 有什么关系吗？也就是说，是通过教模型什么是对、什么是错，来创建 alignment？**

**Jerry Tworek：**某种程度上，alignment 确实是通过引导模型产生某些特定行为来实现的，这本身就是一个 RL 问题。但同时，你也希望模型能够理解什么是对、什么是错，能够理解世界，这并不全都是推理或 RL 的问题，很多时候它们本身就是通用的 AI 问题。

要让模型实现 alignment，它必须能够辨别对错，才能做出正确的选择。我不认为你只要给模型看几个好的示范，它就能学会一直那样做。模型必须对自己的行为和后果有足够深刻的理解，才能真正做出正确的选择。

我认为这是一个永无止境的追求，因为即使对人类来说，定义什么是 alignment 也并不容易。随着人类文明的不断发展，alignment 的概念和人类的整体目标也会持续演变，我们也需要不断地调整模型，引导模型，向模型解释我们想要的东西。这是任何 AI 研究计划中非常核心、也必须重视的一部分。

 **Matt Turck：****在 2025 年 9 月举办的国际大学生程序设计竞赛（ICPC）中，GPT-5 在五小时内解决了 12 道复杂算法题，这个成绩如果参与正式排名，相当于获得了第一名。从模型技术的角度，这背后发生了什么？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Jerry Tworek：**模型并没有针对这些比赛进行专门训练。我们只是拥有一个相当聪明的模型，当我们让它去解决编程问题时，它就给出了正确答案。虽然编程从未被视作产品的一部分，但其实编程非常适合作为奖励机制的试验场。我们的研究人员一直喜欢用编程问题来测试他们的想法。正因为如此，我们的模型在竞争性编程方面自然就很强，这是一个副产品。

也就是说，我们从未刻意让模型在这方面表现优秀，但研究人员在编程题上尝试他们的想法，因此无论我们在训练什么，模型最终在这类题目上的表现都会非常好。所以，把模型提交到比赛，对我们来说更多是形式上的操作，主要是向世界展示这些模型的能力水平。

但重要的是，也必须承认，模型并不是在所有领域上的表现都能像在编程比赛题目上那样出色的。至少与人类基准相比，模型在许多实际问题上的表现并没有那么优秀。因为编程问题已经经过长期、大量研究人员的反复探索，但研究人员往往无法像对这些问题投入那么多时间一样，去深入研究用户在使用 ChatGPT 或其他模型时所遇到的其他实际问题。

除了 ICPC，我们还参加了一些其他比赛，我们想要验证的是模型是否足够聪明，能够在这些比赛中与极其聪明且有才华的人类竞争，但这从来不是我们的具体目标或重点。我们的想法是，如果我们在训练智能模型的研究上做得好，模型自然应该有能力解决这些问题。我们算是达到了这个里程碑，现在会继续向前推进。

目前，我已经看到越来越多实际、可量化的成果，几乎每周或每隔一周就有新的进展。一些可靠的报告显示，科学家正在使用我们的一些推理模型来帮助进行计算，解决困难的技术问题。这正是我们希望模型能够做到的：不仅仅是解决竞赛题目，而是能够在前沿岗位上解决新的技术问题。

 **Matt Turck：****RL 在数学题或编程题上的表现很好，但如何将 RL 应用到其他领域和学科，那些答案不是简单的对或错，而可能更加模糊的场景？OpenAI 最近提出了 GDPval，这是用来评估不同产业表现的方法。在你看来，RL 是否有潜力成为 AI 拓展到这些更广泛应用领域的有效路径？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Jerry Tworek：**用最简短的方式回答：人类能够学会各种技能的关键在于能评估表现、判断某件事对错，并量化这种反馈，也就是说，可以衡量某件事做得有多好，就能够进行优化，从而应用 RL。

如果没有对与错的概念，人类也无法改进和学习，因为学习需要某种信号。而 RL 本质上也是这样子的，关键在于获取反馈有多方便、多容易。每个做 RL 的人都应该努力让模型能够在越来越复杂、有趣的训练信号上进行训练。

但这里也常常会出现 reward hacking，也就是说，你在某种程度上设计奖励去鼓励模型的特定行为，但有时候模型得到的奖励并不完全对应你真正想要的结果。你训练模型去做你希望它做的行为，但奖励本身和你真正期望的行为之间可能存在天然的不匹配。有些时候，模型确实做了你奖励的事情，但并不是你原本希望它做的，这时就需要调整。从某种意义上说，这可以被看作是 RL 的一个局限。

这在人类社会中也很常见，比如各种激励机制和奖励系统，包括职场里的奖励，都不一定完全优化到系统的最终目标上，人们会不断地用各种方式绕过去。因此，设定正确奖励和观察系统是否按预期行动之间永远存在一种博弈。这在政策制定或者任何激励计划中都是一个巨大的问题。

RL 也存在同样的博弈，因此如何不断改进奖励，让它越来越准确地代表你真正所关心的模型行为，是 RL 里奖励设计的核心挑战。

 **Matt Turck：****你之前在推特上表示 AGI 应该很早就被建造出来，而它之所以还没出现，大多是因为需要修正一个简单错误。你认为 pre-training 和 RL 的结合是通向 AGI 的路径吗？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Jerry Tworek：**有一个有趣的问题是，我们怎么定义什么不是 pre-training 或 RL？这个界限在哪里？

我一般认为，我们今天所做的 pre-training 和 RL 都是必要的。当然，肯定还会有其他一些东西，OpenAI 在这些方面也有很多非常有雄心的研究计划。

至于离 AGI 还有多远，很难给出明确答案。对某些人来说，我们正在做的事情和我们计划构建的东西离 AGI 可能不远，但对另一些人来说可能完全不是这样的。但核心是，我们希望不断改变训练模型的方式，让它们能体现我们认为的正确智力形式和最有用的学习方式，同时可以持续研究各种新方法。

有人曾对我说过，如果你把今天的 ChatGPT 展示给十年前的人，他们可能会直接称它为 AGI。但 ChatGPT 在今天还不是 AGI，因为模型仍然有很多限制。我们都非常清楚这些限制，同时也相当有信心能够解决它们。当然，未来的模型可能还会出现一些别的限制，也需要去修复。

有一个终极问题：模型什么时候能够在不依赖大量外部干预，也不依赖人类修正的情况下，自行改进？

我认为这是一个非常困难且严肃的问题，需要我们努力去尝试回答。如果到了那个阶段，即使模型仍然会在很大程度上仍然依赖我们的基础设施和系统，但它将能够开始自我修复，而不需要人类去干预。这也是对 AI 能力的一种预测，一旦模型拥有这种能力，我们对它能解决的问题的信心将比现在更有保障，而我认为我们目前仍能相当可靠地对 AI 能力进行这种预测。

 **Matt Turck：****Richard Sutton 曾在表示，通向 AGI 的唯一道路将是纯粹的 RL（pure RL）。他的意思是 LLM 本身存在缺陷，因为它只是对现实的模仿，而 RL 则是对现实的强化。你怎么看这个问题？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Jerry Tworek：**我们目前确实在对语言模型做非常严肃的大量的 RL 研究。但就 pure RL 这个概念而言，我不认为纯粹的 RL 是合理的。RL 必须依赖 pre-training 才能成功，而我之前也说过，pre-training 同样需要 RL 才能成功。没有 RL，我们现在的研究项目就无法成立。

在 OpenAI，我们非常认真地在模型层面进行大量的 RL 研究，我相信其他 AI labs 也是如此。很多人争论 LLM 究竟是通向 AGI 的“入口”还是“死路”，讨论焦点通常是 pre-training，但显然，目前我们在 pre-training 上使用的方法还不够完善，未来还会有进一步的变化。

有的人认为如果你在做 RL，那它就不是 LLM，或者，如果你在 rollout 中能写程序，那这就是 chain of thought，就不再是纯神经网络，而是神经符号系统（neural symbolic system）。

在 RL 中，rollout 是指从环境的某个状态出发，使用当前策略一步步采样，生成一条完整的状态—动作—奖励序列的过程，用于估计策略价值或训练模型。

但我个人的看法是，我们现在拥有的是一个非常扎实的基础，能够继续向下一个阶段前进：我们先是有了 transformers，用于机器翻译；然后在大规模数据上做了 pre-training；接着做了 RLHF；现在我们在做 RL scaling。接下来我们还会做更多、更复杂的事情。

未来某个时刻，模型架构可能会发生不同程度的改变。但我认为这更像是持续地往现有体系上叠加新的方法，或逐步淘汰一些不再需要的旧元素，而不是彻底推翻重来。换句话说，我认为我们目前的路径是正确的，它不会是一场 180 度的转向，而是一个持续演进的过程。

**04.**

**Jerry Tworek 是如何加入 OpenAI 的？**

 **Matt Turck：****在你成长的那些关键阶段，是哪些因素让你走上了 AI 领域的道路？**

**Jerry Tworek：**我一直都认为，成为一名科学家、从事科学研究，是人类所能拥有的最高使命。从我有记忆起，我就一直想成为一名科学家。在早期的求学过程中，我也发现自己在这些方面有些天赋。比如在学校里，我理解事物的速度会比周围的人稍微快一些。

我在大约 18 岁的时候希望成为一名数学家，但之后我逐渐意识到一件事：我很喜欢且擅长数学，但我并不那么喜欢学术界。在 2010 年、2011 年左右，我决定去做 trader。做了几年之后，我开始对 AI 感兴趣，真正吸引我进入 AI 领域的是 RL，尤其是 2013 年 DeepMind 团队训练的 DQN agents。对我来说，2012 年的 ImageNet 反而没有那么触动我。

DeepMind 团队训练的 DQN（Deep Q-Network）agent 是一种结合了深度学习和 RL 的算法，能够从原始像素数据中学习如何在复杂环境中做出决策。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*Playing Atari with Deep Reinforcement Learning* 首次展示了 DQN 是如何从原始像素输入中学习玩 Atari 游戏，并取得超越人类表现的结果的

在大学期间，我学到了很多关于 classical AI 的内容。那时，神经网络已经非常流行了，但我们还学习了 SVM 以及各种训练 classifiers（分类器）的方法。对我来说，一个很直观、很自然的事情是：如果你有足够多的参数，并且训练得足够充分，你就可以把一个分类器拟合到任何你想要的目标上。

支持向量机（SVM， Support Vector Machine）是一种监督学习算法，主要用于分类和回归任务。

但在那时，我没有把分类器看作“智能”。对我来说，它只是一个在输入与输出之间不断逼近某个函数的工具。我们可以通过训练让它的拟合越来越精确。但我当时没有意识到的是：一旦你能够越来越好地拟合任意函数，你其实可以开始塑造 behaviors（行为）和 strategies（策略）。

让我真正意识到这一点的，是 DQN 的研究成果。DeepMind 将当时在 ImageNet 上已经被证明有效的神经网络方法，引入到了 RL，用来解决简单的电脑游戏。结果这些结构并不复杂的神经网络，配合一个相对简单的学习算法，竟然能够掌握相当复杂的游戏玩法，并展现出非常有趣的行为。

因此，当时的我很坚定地想做这方面的事情，Google DeepMind 和 OpenAI 就是最合适的两个地方。虽然当时这两个地方都还相对规模较小，但已经颇有名气了。

 **Matt Turck：****你是在 2019 年加入 OpenAI 的，那时候是非常早期的阶段，还属于 OpenAI 的非营利时期。你是怎么和他们建立联系的？**

**Jerry Tworek：**我就是在 OpenAI 官网上提交的简历，幸运的是，OpenAI 回复了我。我当时就是希望做 RL 相关工作。

 **Matt Turck：****在 2019 年，OpenAI 很多工作其实都是围绕 RL 展开的，后来才有了无监督学习和 GPT。但它的起点，确实是 RL。你当时是直接参与了 RL 的项目，还是当你加入时，它已经进入后期了？**

**Jerry Tworek：**我当时在 OpenAI 参与的项目是 robotic 项目，使用的代码和方法与 Dota 是相同的。Dota 是 OpenAI 向全世界展示 scaling RL 能力的一种方式。从某种意义上说，Dota 就像是把 2013 年的 DQN agents 的能力变得越来越强，从而能解决越来越难的问题。

OpenAI 从一开始就有一个非常清晰又聪明的思路：要想让模型学会真正复杂、有趣的行为，就必须拥有大规模的系统。这也是 Dota 想要证明的：通过扩大 RL 的规模，我们可以解决非常复杂的问题。

当时 OpenAI 另外还有几个 RL 项目，其中一个就是我加入的 robotic 项目。这个项目想解决的问题是：我们已经证明神经网络可以解决复杂的电脑游戏，那么它能不能也解决现实世界中的实际问题？OpenAI 试图通过大规模 RL 解决洗碗、叠衣服、建房子等各种任务。

我当时参与的项目主要集中在服务型操作（service manipulation），这在当时（甚至直到今天）都是非常难以攻克的挑战之一。我们最终展示了一个成果：由神经网络控制的机械手能够完成解魔方，这本身是一个相当精细且复杂的任务。

**05.**

**OpenAI 只会同时推进 3-4 个主要研究项目**

 **Matt Turck：****OpenAI 是如何确定研究优先级的？是自上而下决定的，还是自下而上？**

**Jerry Tworek：**如何构建、组织和领导一个研究项目是一门艺术。OpenAI 的一个强项就在于，在结构化地推进研究项目上有一种独特的混合方式，不是完全自上而下或自下而上，而是两者的结合。OpenAI 的一个核心原则是：我们只同时推进非常少量的项目。OpenAI 并不试图什么都做，也不会做一堆不同方向的小赌注。我们希望集中大量的资源和努力，把少数几个核心项目做到极致，因此，需要很多人共同合作。

我们大概同时只推进 3-4 个主要项目。从这个角度来说，研究人员并没有完全的自由，并不是想做什么就可以直接做，每个人的工作都必须服务于这三四个核心项目之一。在这些项目之内，我们会尽量采用自下而上的方式，只要这个方向能够服务于项目目标就行。

对研究领导者来说，最重要的职责就是确保所有研究人员都在为共同的目标努力，而不会各自为战、分裂成不同的小方向。这其实是一个非常艰难的工作，也是一件外人不容易察觉到的精细活。

我并不认为自上而下的僵硬研究结构在科研机构里行得通，因为你不可能招来世界上最聪明的一群人的同时，只是告诉他们该做什么。他们必须要自己去思考、去探索，但他们不能在整个无限大的空间里随意挑选方向。他们必须在项目目标的范围内，去找出最能推动 OpenAI 研究进展的那个方向。

 **Matt Turck：****OpenAI 是如何在协作与 IP 保护之间取得平衡的？**

**Jerry Tworek：**实际上在 OpenAI 的研究团队中（目前大约不到 600 人），每个人基本上都知道所有事情。我们一直都保持完全透明。如果研究人员无法了解所有正在发生的事情，那他们就无法掌握做出最佳研究决策所需的信息。

虽然这里确实存在一些 IP 风险，但如果不让人们了解研究进展，那就无法开展最优的研究，那实际带来的风险可能更大。我们的目标就是做出最好的研究，训练出最好的模型。因此，我们的文化整体上是高度协作的。

我们有一种共同的信念：我们是在为一个比任何个人都更大的目标共同努力。AI 的重要性越来越高，但 OpenAI 的成功并不是板上钉钉的，它取决于我们每天都在做出出色的工作，所以命运共同体的感觉很强，我们都必须依赖彼此来完成各自的工作，实现共同的目标。

 **Matt Turck：****OpenAI 是如何保持快速的发布节奏的？**

**Jerry Tworek：**从我的视角来看，OpenAI 是一个“这一代的公司”（generational company），有着巨大的 momentum 在推动我们向前发展。我们知道自己过去做得很好，也知道必须继续保持这种势头。

我们拥有极其聪明的人才，可以说，全世界最有才华的人此刻都希望来 OpenAI 工作，这意味着每个人的产出都非常高，每个人都在承担大量工作。同时，我们有一套非常有效的研究组织方式，还借鉴了硅谷高效执行的经验。更重要的是，大家普遍对工作充满热情。每个人都能感受到我们正在做的事情的分量和潜力。因此，OpenAI 的员工普遍工作非常努力。

这些结合在一起，就让我们能完成很多事情。而且我们也都非常清楚，人类历史上只有这一次机会来打造、部署和发展 AI，大家都希望以最好的方式来做成这件事。

 **Matt Turck：****你们会使用自己的工具吗？Fiji Simo 曾提到 OpenAI 在 Dev Day 上发布的很多内容其实是用 Codex 写的代码。你们在日常工作中是不是也会用自己的模型来启发新的想法，或者用 Codex 来写代码？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Jerry Tworek：我们确实在写代码时大量使用 Codex，而且它的效果也在不断提升。我自己也非常频繁地使用 ChatGPT，虽然我不会太依赖它来产生新的研究想法，但在我遇到各种各样问题时，我会用它来帮忙解决。我现在是 ChatGPT 的重度用户，每个月会花 200 美元订阅费。

 排版：夏悦涵

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

延伸阅读

Palantir 创始工程师深度分享：FDE 模式是 Agent 时代的 PMF 范式

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

深度讨论 Online Learning ：99 条思考读懂 LLM 下一个核心范式｜Best Ideas

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

深度讨论 Pulse：OpenAI 超越 Google之路的开始 ｜Best Ideas

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgx6icO7vRrAmA8ZnwE5D36ZprPh6ouJ1yeqYhIiagAuv60Wibdt7C6EN8ps3p2Rbd4Ahuks0ONRHNiaGw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20)

AI X 用户研究：能并行千场访谈的“超级研究员”，正重塑产品决策的未来

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgx6icO7vRrAmA8ZnwE5D36ZprPh6ouJ1yeqYhIiagAuv60Wibdt7C6EN8ps3p2Rbd4Ahuks0ONRHNiaGw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22)

Notion、Stripe 都在用的 Agent 监控，Braintrust 会是 AI-native 的 Datadog 吗？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgx6icO7vRrAmA8ZnwE5D36ZprPh6ouJ1yeqYhIiagAuv60Wibdt7C6EN8ps3p2Rbd4Ahuks0ONRHNiaGw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=24)