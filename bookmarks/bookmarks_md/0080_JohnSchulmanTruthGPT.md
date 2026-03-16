---
url: https://mp.weixin.qq.com/s/snS2ty4x7gJ9QoMxWU0_Lw
title: "John Schulman：强化学习与真实性，通往TruthGPT之路"
description: "关于RLHF的最新进展与挑战。"
author: "OneFlow社区"
captured_at: "2026-03-08T10:24:13.637Z"
---

# John Schulman：强化学习与真实性，通往TruthGPT之路

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/lBhAE42wKWpRZ1MW21VLBPBKTHCz1x4tGCxop00gJI4Rwuvj7YxUUjC9ClpFssdU32Zibn5bQdQic9VTpOd5BxUQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**OneFlow编译
翻译｜贾川、徐佳渝、杨婷
**

大型语言模型（LLM）有一个众所周知的“硬伤”——它们经常会一本正经编造貌似真实的内容。

OpenAI团队希望通过改进强化学习反馈步骤“原生地”阻止神经网络产生幻觉，[**OpenAI首席科学家Ilya Suts****kever**](http://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247491133&idx=1&sn=1e967f1c657f8781f8d876515047e5d5&chksm=fe41900bc936191d7756b74d23c85acba6e8b14f6e4c7ea48033b3959cb43011a9a2d81e0dee&scene=21#wechat_redirect)**对此胸有成竹**。作为ChatGPT项目的主要负责人以及OpenAI强化学习团队的领导者，[**John Schulman**](http://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247490988&idx=1&sn=664b9b90504c75ed0f27b0651f3aad2f&chksm=fe41939ac9361a8c400c2310c4297ef6a80f626731e32cca276504e4b4b8c9a38c6d63eea3f1&scene=21#wechat_redirect)在最近的Berkeley EECS会议上系统性地分享了OpenAI在人类反馈的强化学习（RLHF）方面所做的工作，以及语言模型的幻觉等亟待解决的问题，同时也介绍了解决这些挑战的潜在思路。

![图片](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWpRZ1MW21VLBPBKTHCz1x4tgH5RC4BQrIDeiaZE5rAJ3bzxTFzZTVCmQVlDQWSQkDN0sSib2ro4gwTA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

没有比Schulman更权威的RLHF研究者，他也是强化学习领域无可置疑的大牛。

加入OpenAI之前，Schulman在加州大学伯克利分校攻读博士学位，一开始主要研究机器人技术，随着深度学习兴起，转而研究强化学习，其导师正是强化学习领域的领军人物Pieter Abbeel。

Schulman在强化学习研究领域作出了许多重大贡献，包括发明了TRPO算法（信赖域策略优化）、GAE（广义优势估计，Generalized Advantage Estimation）以及PPO算法（近端策略优化）。

如今，Schulman还在强化学习研究的最前线尝试解决公认难题，他的最新思考或许会为业内其他研究者带来启发。

（以下内容由OneFlow编译发布，转载请联系OneFlow获得授权。来源：https://www.youtube.com/watch?v=hhiLw5Q\_UFg）

##

**1**
**语言模型幻觉溯源**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

提到语言模型，很多人应该听过“幻觉”这个名词。上图就是一个关于幻觉的例子，这不是精挑细选的，而是我做测试时的第一个样本。

我的问题是：请告诉我John Schulman因在家饲养野生动物而被捕的相关情况。GPT-3.5 Instruct是经过强化学习训练过的模型，给出的回答是关于John Schulman饲养老虎和小型美洲猫之类的事情。GPT-3.5 Turbo（Chat）的整体表现与GPT-3.5 Instruct一致，且智能程度相同，只是微调方式不同，它给出的回答是：抱歉，我没有查到任何关于John Schulman被捕的相关情况。

然后，我又尝试对聊天功能进行微调过的GPT-4（Chat），它的回答是：很抱歉，我没有找到有关John Schulman因在家中饲养野生动物而被捕的任何信息，我的知识截止于2021年9月。John Schulman是人工智能领域的著名研究人员……

这是“幻觉”问题的一个很好示例。相比之下，我觉得GPT-4的表现相当不错。

当人们说幻觉时，主要指的是两类不同情况。**其中一类幻觉是语言模型的模式完成（pattern completion）行为。**它们的训练目的是最大化文本可能性，使生成的内容看起来很像互联网上的文本。

这主要有三个原因：**1\. 它不知道自己可以回答“我不知道”或者表达不确定性。**如果告诉模型可以回答“我不知道”，那么在一定程度上能解决幻觉问题；**2\. 模型有时不愿意去质疑前提（premise）**，它认为前提是数据分布的一部分；**3\. 模型有时会陷入谎言之中。**如果模型已经犯了一个错误，那么它会认为自己应该继续回答下去，生成一连串响应，这也意味着它会继续说谎。

**语言模型的另一类幻觉是“猜错了”。**就像人类一样，你可能只遇到过一次某件事情，自己不能确定，感到很模糊，所以在回答时必须带点猜测，有时可能就会猜错。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

比如很多人喜欢问模型关于自己的问题，就像用谷歌搜索自己一样，所以我也尝试让模型写一篇个人介绍。

InstructGPT回答，“John是一位AI研究科学家，在OpenAI工作。他曾是卡内基梅隆大学的计算机科学教授等等。”此外还增加了一堆虚构的东西。GPT-3.5的回答有点模糊，但基本上正确，它说我本科就读于斯坦福大学，在Pieter Abbeel的指导下做研究，还提到了信赖域策略优化（TRPO）方面的内容。GPT-4的回答几乎完全正确，但也有些许瑕疵，比如它说我主修数学，其实并没有，对我取得本科学位的年份描述也有一年的误差。

这其实就属于“猜错了”：模型尝试给出一个全面的答案，但结果却出现了错误。这样的结果是好是坏在一定程度上取决于这份个人简介的用途：如果想将其放在网上，那么肯定存在问题；但如果仅仅是某人想要了解我，那么年份误差一年也不会有太大影响。

##

**2
****幻觉与行为克隆**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

到底为什么会产生“幻觉”？我将描述一个概念模型加以解释。上图是一个知识图谱，包含一些事实，比如《星球大战》属于科幻类，Han Solo是《星球大战》中的一个角色，以三元组形式排列。这尽管是传统人工智能的知识储存方式，仍然很有用。

该概念模型能解释当你对神经网络进行微调以完成某种问答任务时会发生什么。神经网络中包含信息，可以将其看作类似知识图谱的东西，以某种非常复杂的方式存储在权重中。每条边（edge）都有一些置信度，不同的边置信度不一样，原因是，某些事实被看了上百万次，而有些事实可能只看了一两次。

当你进行小规模微调时，可以将其看作你正在学习某个小型程序，将知识图谱作为输入，并基于知识图谱中的内容和语句的置信度输出概率。比如，你正在学习处理知识图表的四行Python代码函数，那么你之所以要进行微调，是因为可能需要学习一些关于问题格式的内容。

如果只抛给预训练模型一个问题，如“《星球大战》属于什么类型？”，那么它就不知道该问题的上下文是什么，不清楚这些文本的来源是哪里，是信息性网站、恶作剧网站还是虚构文本。而微调就是让模型专门输出正确的答案或在微调数据集中的内容。

行为克隆（behavior cloning）是强化学习领域的一个术语，意思是监督微调或最大化似然（maximizing likelihood），其目的是完成给定prompt的最大化似然或最大化对数概率。

如果用行为克隆来训练模型，比如使用人类编写的正确答案或使用ChatGPT的输出进行训练，那么即使用100个正确的答案进行克隆，由于模型缺乏所有相关的事实，仍然是在教会模型产生幻觉。例如，如果训练模型回答有关Han Solo的相关问题，但知识库截止日期是5年前，因此模型不知道有一部围绕Solo的衍生电影。这种情况下，你实际上不是在训练模型输出正确答案，而是在训练它在这种问题上进行猜测。

**如果你使用行为克隆来训练模型，那么无法避免出现幻觉问题，同时也会出现相反****的问题，即如果你想训练模型在某些情况下回答“我不知道”，那么它可能会隐瞒实际上已经知道的信息。**例如，如果标注者不知道答案，他们可能会将“我不知道”列为目标答案，但实际上网络可能已经有了答案，你只是在训练模型隐瞒信息。

因此，行为克隆或监督学习的问题在于：**正确的目标实际上取决于神经网络中包含了哪些知识，而这对于收集数据或进行实验的人来说是未知的。**因此，除非你有一种方法来查看模型中的内容，否则无法使用行为克隆训练出真实可信的模型。

现在有了一些略微不同但比较聪明的方法，比如在数据标注时，让标注者询问模型问题并查看答案是否彼此一致。如果一致，则检查是否正确；如果正确，则作为目标答案；如果完全不一致，则回答“我不知道”；如果错误，则同样回答“我不知道”。这种做法的结果稍微好一点，但操作过程更加困难，而且很难实现自动化。**总的来说，这仅适用于特定模型。**

如果尝试用监督学习数据集来训练另一个模型，也会遇到同样的问题。例如，许多人正在使用ChatGPT的输出来微调开源基础语言模型。微调后，这些模型的表现很好。但如果仔细查看事实准确性，你会发现它们存在一些问题，并且经常会编造信息。不过这只是我预测的结果，还有待实验证实。

##

**3
****语言模型知道自己的不确定性吗?**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

我们希望模型在不知道正确答案时能输出其知识的实际状态并表明不确定性，而不是进行猜测。那么模型是否知道自己的不确定性呢？比如给定一个问题，模型清楚自身是否知道答案吗？

这个问题很难回答。什么是“知道”？如果模型知道某些东西，那么是否用一些简单的代码就能实现这个功能？例如，如果有代码能调用模型正确地执行你要做的事情，那么就认为模型知道如何做这件事。

**问题是，模型是否知道自身的不确定性？答案是肯定的。**模型知道自己什么时候知道什么时候不知道，因为模型被训练为最小化对数损失，为此它必须输出概率。模型的下一个token预测是经过校准的（calibrated），校准后的对数损失是一个合适的表示不确定性的指标。

预训练目标产生了一个校准的模型，它必定输出合理的概率，这意味着，模型知道自身的不确定性，至少对于任何可以被转化为预测单个token的短答案的问题，它可以为该token给出一个合理的概率分布。如果模型能够为该token输出合理的概率分布，但无法对其不确定性进行内省，那反而让人感到意外。

有几篇论文已经研究了这个问题，我在上图的底部做了引用。论文研究表明：可以让模型用语言表达它们的不确定性，并给出与输出概率类似的结果。

我的观点是：**模型确实知道自己的不确定性，行为克隆无法利用这一点来避免幻觉，强化学习才是解决这个问题正道。**

部分幻觉仅因为模型陷入想要“给出完整答案”的模式或不知道如何表达不确定性而产生，因此这类幻觉很好解决。比如可在训练模型时给出一些表明“我不知道”、“我的知识截止于××日期”的示范，或者给出一些质疑用户提问的范例，这样模型至少能够表达不确定性，只是表达的时机可能不是那么恰当。

##

**4
****如何用强化学习解决幻觉问题？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

我认为，通过强化学习就能把握好这个界限，即在何时说“我不知道”。当模型给出一个答案，如果是非常自信的正确答案，将得到高额奖励；如果是模糊的（hedged）正确答案，将得到稍差的奖励；如果是无信息的答案，例如“我不知道”，将得到一些惩罚；如果是模糊的错误答案和完全错误的答案，将得到更多的惩罚。这基本是一个适当的评分规则，能够激励模型给出自信的答案，如果它对错误答案过于自信，就会给出相应惩罚。

因此，这就是我们想要达到的效果。但通过强化学习训练语言模型来实现这一目标并不容易，因为你需要知道答案是否正确，但答案究竟正确与否我们无从知道。

接下来我将讨论如何尽可能地接近这一目标。

###

**TriviaQA**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

实际上，我的同事做了一个简单而有趣的实验，虽然并未将其公开，但对我所描述的概念图提供了有力支持。

这个实验被设置为TriviaQA模式，TriviaQA是一个流行的问答数据集，它包含了一系列常识问题，其风格类似于Jeopardy（译者注：Jeopardy是美国的一档问答游戏节目，玩家需要根据问题提供的信息推理出正确的答案，或者选择他们认为正确的答案）。

我们使用了一种基本的问答格式来引导模型回答问题，如果你只在正确答案上进行行为克隆，那么模型对所有问题都会给一个回答，但往往会包含一些错误答案。因为我们从未告诉它输出“我不知道”这样的答案，若遇到不知道的问题，它只能进行猜测而不会说“我不知道”。

在对答案进行行为克隆时，只需要少量训练后模型就达到一定的准确率和对数损失，但这种训练只是在教模型它应该试图输出正确答案，模型实际上没有从这种微调中学习很多新知识，学到的只是问题格式（the formatting of the questions）及其处理方式。

因此，我们定义了一个强化学习问题，对正确回答、错误回答及拒绝回答给予相应奖励。某种程度上，我们可以通过解析计算来得出正确的奖励行为，即错误答案的惩罚与正确答案的奖励之间的差异。最优奖励行为可以简单理解成确定某种阈值，譬如当列表中排在最前的选项有超过50%的概率时就回答，否则就不回答。

如果我们将奖励函数用于强化学习，模型就会学到最佳阈值行为，就像模型已经了解最佳策略（涉及对数概率和阈值）。因此，如果使用强化学习微调模型，就可以让它做同样的事情，即使它并没有真正查看到这些概率。

我们训练了一个奖励模型来预测该奖励函数，然后使用奖励模型而不是oracle模型进行强化学习。这种方式的效果很难评析，因为奖励模型并不知道答案是否正确，但它实际上与我们正在微调的策略模型知道相同的信息。就像我之前所描述的粗略图一样，它具有相同的知识图谱，知道这个答案的不确定性有多大。

我们的假设是，训练奖励模型并进行强化学习，也会学习正确的行为。不过这种方式的效果还是不如oracle模型。它为我描述的图景提供了证据支持，但还需要进行进一步研究。

###

**长篇回答设置**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这里不再赘述相对简单的单句回答（one word answers）的设置。更有趣的设置是长篇回答（long-form answer），ChatGPT采取的就是该设置。对于事实性问题，我认为这与完全正确或错误无关，而是各种回答都处于灰色区域，混合了正确和错误的信息。单个事实（individual fact）无关对错，可能存在一定的误导性，所以我随机选择了这个长篇回答。

如果你问ChatGPT一个技术问题，可能会得到正确、错误或具有误导性的答案。上图的问题是“InstructGPT中奖励模型训练的目标是什么”？其中它说，“InstructGPT所依赖的奖励模型训练都来自人类反馈”，这种说法缺乏真实性，且极具误导性，我想说这是完全错误的，但它也说，“通过收集的对比数据可以构建一个奖励模型来预测回答的质量”的说法是正确的。不过，让标注者来判断答案是否有误往往行不通。

我们没有完美的答案，而是需要让人们对回答进行排序，并说出哪个更好。人们必须根据错误的严重程度来判断模型给出的答案，这在很大程度上取决于上下文。举一个编程的例子：模型写了100行代码，只有一个地方的参数写错了，这种情况下我宁愿让它给出这个答案，也不愿让它回答“不知道”，因为我至少可以在其基础上运行和调试。但是在其他情况下，这种错误可能是一个大问题。

###

**ChatGPT的长篇真实性评估**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

使用RLHF可以提高模型的准确性。虽然我们没有在ChatGPT上进行过严格实验，但GPT-4博客文章中有一些模型评估指标可以衡量准确性。评估的方式是为每个问题提供一个参考答案，并由人类检查，然后比较模型生成的答案与参考答案之间的一致性。

我们还使用了一些自动化程序来评估长篇答案并检查它们是否与参考答案一致。上图中的柱状图表示不同版本的ChatGPT，随着数据越来越多，相应指标上都有所改善。GPT-4在这些准确性指标和定性测试上的表现要好得多。当然，虽然在分析这些数据时还需更谨慎一点，但我们认为，这种方法可以提高模型的准确性。

出于各种因素，在实际情况中还存在多种问题。模型有时确实需要猜测，尤其是在输出大量详细事实的时候。无论你如何训练，模型都有概率在回答某些问题时进行猜测，这是不可避免的。

在面临有些问题时，模型会采取“避险措施”，不过这个度可能把握不好，从而作出错误的判断。我们基于排名的奖励模型的训练方式是，预测输出一种类似于对数概率的值，表明某个回答比另一个更好，但它并没有真正说明哪一个比另一个好多少，只是表明它对哪一个回答更有信心。

模型并没有就事实错误的严重程度和错误的模糊程度施以正确的惩罚，因此我认为，基于排名的奖励模型没有很好地解决这个问题。

此外，标注者的错误肯定也有很多。有时标注者没有足够的信息来做出正确的标注，人类无法始终正确地进行排名，比如有些问题可能涉及到用户计算机上的某些代码库，标注者就无法访问。我们尝试让标注者跳过他们无法回答的问题，但也还有很多其他错误。当然，在阅读长篇答案时，要捕捉到其中的每一个错误是不可能的。

###

**索引和引用**

接下来谈谈检索和引用来源。在语言模型的背景下，检索通常是指语言模型访问某些外部知识源（通常是一些文档集），并提取一些文本来回答问题。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

有几个原因可能需要检索，比如想了解世界上正在发生的最新事件和一些不在预训练中的信息。不在预训练中的信息不仅包括最新资料，而且还可能是一些私人信息、计算机或代码库中的东西、模型输出答案和个人以前的对话等等。

检索和引用来源最需要关注的是可验证性，因为模型写的答案是否正确需要人类来检查，如果不知道信息来源，需要查找所有信息，检查其正确性非常困难。如果模型引用了来源，那检查起来更容易。如果将未添加引用的答案看作是未经证明的草图，那么添加引用就好比呈现出了证明过程。

###

**WebGPT的参考价值**

在ChatGPT之前，我们还做了一个WebGPT项目。该项目主要聚焦于细分问答，数据集基于Reddit下的一个板块ELI5（Explained Like I'm Five，用五岁孩子的语言解释）。当人们在谷歌上查不到自己想要的答案时，就会在ELI5提问，比如“我用MacBook参加Zoom会议时出现了某个问题”，或者“人们为什么推荐用苏打粉和醋来当清洁剂”。

我们想构建一个能回答这类细分问题的系统，先在网上搜索整理，再给出答案，最终创建出了能给出这类答案的WebGPT系统。当你问“苏伊士运河在2021年3月时为什么被封锁”，系统就会给出答案并列出所有的论据来源。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

WebGPT是2021年底的一个项目，相当于GPT-3水平的模型。如果把问WebGPT的问题拿来问GPT-3.5或者GPT-4，无需进行查找就可以完美地回答，但这种技术对于GPT-3级别的模型来说非常有必要，即使对于GPT-4也很有用，尤其对于更技术性的偏门话题。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

WebGPT的工作方式对于GPT-4也有参考价值。我们定义了一个行动空间或者领域特定语言，模型可以用其来浏览来源。当搜索时，模型会看到一些链接列表，就像搜索页面一样，然后可以点击链接并引用内容。

不过，由于语言模型的上下文窗口有限，大约为4000个token（每个token约为1个单词），所以查看的材料也有限，否则就会内存不足。

在这种情况下，引用非常重要，因为我们只能简要地向模型展示这些页面，然后将其从上下文中移除。通过允许模型进行引用，我们使其能够在其余浏览过程中保留信息。在模型完成任何必要的浏览操作后，它可以声明已经完成并开始编写答案。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

我们定义了一个强化学习环境，让模型生成文本来定义一个领域特定语言（DSL），而不是发出特殊操作（action）。强化学习任务的每次episode由模型浏览20到100步的，引用某些信息，编写答案，然后使用奖励模型计算奖励。整个过程都是在标准方法下完成。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

以上是RLHF的流程图。首先是行为克隆，这属于监督学习部分。我们使用专家演示（expert demonstrations）来展示如何执行任务，在本例中通过查看浏览器来编写答案，然后模仿这种行为。

其次，通过比较两个完整的答案（A和B）或两条轨迹来收集奖励模型，由人类决定哪个更好。之后，我们可以在该奖励模型上执行强化学习，或者通过获取多个样本并重新排序来对其进行搜索。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

针对每个任务，需要为其制作GUI（图形用户界面）。用于收集数据的GUI相对简单（如上图所示），但奖励建模的GUI比较复杂，需要让人们仔细阅读模型编写的答案，并标记其中有强支持和弱支持的语句。我们详细定义了这个标记过程，以计算答案的事实准确性。尽管这个过程有些繁琐，但最终我们只得到一个二进制信息，即一个比特位的信息。我们尝试利用其他信息，但效果并不理想。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

那么WebGPT的效果怎么样？我们发现，在给定查询的情况下，左侧的图表显示的是最优的n个结果。具体来说，我们采集n个样本，使用奖励模型对它们进行重新排序，并返回排名最高的结果。与此相比，我们没有使用微调的方法，也没有使用强化学习进行训练，而是采用了监督学习的策略。

我们发现，对于175B的GPT-3模型，在64个样本的情况下，模型表现得更好。模型的选择正确的概率达到55%到40%不等，虽然连贯性稍有欠缺，但事实准确性更高。此外，模型给出的答案也比Reddit上的参考答案更受欢迎。

实际上，我并不完全相信这个对比，模型有时会给出看起来十分明确的答案，并且还带有引用链接，但我认为标注者会偏向某一种风格的答案，这会让对比带有偏见。因此，我不认为上述模型给出的答案能好过Reddit上票数最高的答案，但如果用当前模型再跑一次，得出的答案可能会好一些。

###

**ChatGPT浏览模式**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

ChatGPT有一个用于浏览的browsing（alpha）模式。与ChatGPT的操作方法相同，例如我们可以提问“今天谁会在伯克利 EECS 座谈会上发表演讲？”，这是我今天早上提出的问题，它的问答是“今天的演讲人是John Schulman…...”调试窗口显示模型收到的一系列长串提示说明，比如“你有一个带有这些函数搜索引用的浏览工具”，后附函数说明文档。在生成的对话文档中，我们能看到用户消息、演讲者信息。

它在执行这些操作时会进行说明，相当于是它的内心独白。如上图所示，它说“我将搜索今天在伯克利的独家演讲者”，然后它发出了一个搜索命令（“Berkeley EECS colloquium presenter today” recency, days = 1”），然后它会告诉我们点击第一个链接，以访问伯克利座谈相关页面，在引用相关资料之后，它才会开始输出答案，呈现出最终浏览结果。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

此外，现在还有其他内容可以浏览，且提供类似引用的产品。但ChatGPT的特殊之处在于，它只会在不知道答案的情况下启用浏览模式，这与我前面提到的不确定性自我认知（self-knowledge of uncertainty）相似，它允许模型表达“我不知道”，让模型在必要的时候进行浏览操作。

比如我提出一个问题：什么是dagger算法（一种典型的模仿学习算法）？针对这一问题，ChatGPT在完全没有启用浏览的情况下给出了详细答案，我看到答案中提到了一个名为Fleet-DAGGER的东西，于是我又问“什么是Fleet-DAGGER？”因为模型不知道答案，所以它开始进行搜索，它查看了子网页（里面是完整的档案文件），然后对浏览内容做了总结和改写（这里并不是简单的复制粘贴），最后在总结的基础上给出了答案。

##

**5
****开放式问题**

##

**
表达不确定性**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

接下来我想聊聊在整个工作过程中遇到的开放式问题。**第一个问题是：如何激励模型真正准确地用语言表达不确定性。**这意味着我们要使用适量的模糊陈述（hedging），并尽可能地解释模型的全部知识状态。在我看来，**目前的奖励模型并没有准确衡量答案之间的好坏差距，更像是衡量了答案好坏差距的信心（confidence）。**

我们以A超过B的似然最大化的目标去训练一个奖励模型，其中A获胜的概率与奖励分数差的指数成正比，类似于分类损失（classification loss），它不会因过于自信的错误（extra confident errors）而惩罚模型，也不会考虑模糊陈述等方面的问题，在我看来，这可能会对模型产生影响，模型会认为未模糊陈述的错误答案比模糊陈述的答案更糟糕。

但是，我不认为我们的评分方式完全正确，如果你想用适当的评分函数来对模型进行训练，这也会遇到一些问题，我们难以让模型输出所有内容的概率，因为自然语言并不精确，虽然这正是自然语言强大的原因，但因为句子的模糊性概率，同一个句子可能会有不同的理解，会存在许多可能的解释，有的概率高，有些概率低，我们很难对这一概率进行正确判断。

对于上述问题，**也许我们可以在自然语言语句旁添加一些正式的概率声明，**但我还不知道具体应该怎么做，或者我们应该建立某种目标（objective），它可以让多个智能体相互协作，这些智能体能够正确表达不确定性，因为不确定性能在后续帮助其他智能体或这一智能体本身。

##

**超越标注者**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**另一个开放问题是，我们该如何超越标注者能够轻松完成的事情。**检查技术或小众主题的长篇答案其实非常困难，对于这个问题，**我们有一个一般研究领域：对齐方面的可扩展监督（scalable oversight）**。通常，验证某一解决方案是否正确要比生成正确的解决方案容易，这是理论计算机科学的最基本思维之一。

拿P vs NP问题来说，一种解释是：让弱智能体为强智能体提供激励，通过这种方式，最优行为可以解决弱智能体无法解决的问题。我们可以让标注者训练模型，让模型完成标注者无法做到的事，理论上这是可行的。

在这个方向上，我们可做的事情有很多，比如可以尝试对任务进行分解并委派，让浏览模型对每个句子做事实核查，然后自动聚合所有结果。我们还可以进行类似于设置激励机制的设计，比如可以设置一种游戏，在游戏中让智能体们去竞争验证器的批准，并检查其余选择的错误原因，AI safety via Debate是一个很好的例子。

基本上，这个方向的研究还处于起步阶段，没有出现较好的实际运用，但这方面的应用已逐渐成为必要，因为标注者开始难以跟上模型的发展速度。

##

**生成知识**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**最后一个问题是：RLHF是纯粹基于人类认可的优化，但问题是人类并不能掌握所有事情的正确答案。**很多时候，我们只是在对听起来有说服力、听起来正确的内容进行优化，希望以后能基于客观事实进行优化，增加更多算力，在模型训练上投入更多精力，尽可能地接近事实真相。

那我们应该怎么做？**一个方法是，如果我们了解某种基本真理，那可以优化实际正确性。**就预测未来而言，未来有数百万种可能，如果我们将这些预测用作奖励函数，也许能够产生真实的知识，并对这些知识进行真实性测试，这种预测是知识产生的来源之一。
**
如果我们有形式化系统（formal system）或半形式化推理系统，也可以进行演绎产生新的知识。**上述做法很有意思，是一个有趣的挑战。

##

**6
****答听众问**

**
问：如果关于Dagger算法的知识在模型内部，关于Fleet-Dagger的知识在模型外部，那么模型在用概念解释它们时是否有差异？
**

**答：**在我看来，模型比较擅长解释根植于内部且经常在文本中遇到的概念，对于首次见到的概念，基于内省和推测，模型可能会给出不太让人满意的解释。

因此，模型在谈论内部常见知识时会比较智能，也就是说，相比Fleet-Dagger，模型更擅长解释Dagger，对于Fleet-Dagger，模型可能只是在某个文档的摘要中接触过，对于这个概念，模型不会有任何深入见解。

**问：你提到模型会在答案不受欢迎的情况下会隐藏信息，那么在开放域上下文中训练模型如实告知全部信息，以及在封闭域上下文中训练模型不生成未经证实信息（即使模型实际上知道该信息）的激励之间是否存在冲突？**

**答：**是的，这两者之间存在着非常强烈的冲突，精准率和召回率之间，信息性和正确性之间也存在着冲突，这些都是模型训练的常见冲突。面对这些冲突，不可避免要进行一番权衡，我们会在权衡曲线上尽可能合理地做出选择。

**问：WebGPT的Demo给出的内心独白非常棒。你是否考虑过提炼一个模型，这个模型没有足够的内层思考空间，所以需要设置内心独白，以便我们可以理解它的想法。
**

**答：**在没有完美的解释性方案或无法确保模型安全性的情况下，内心独白是一个比较好的选择，它可以解决部分问题，我们应该尽可能多地采用这种设置。内心独白可以有效帮助我们理解模型，但显然不能完全信任它，模型可能会产生虚假的内心独白，这是一个值得注意的问题。

小型模型必须要使用内心独白才能达到一定的智力水平，当然我们可能会担心模型隐藏信息，但这种担忧其实有点牵强，总体来说，虽然内心独白存在着一些理论上的担忧，但我很看好它的发展。

另外，详细的、允许使用较短反馈的内心独白可以帮助我们更好地判断模型行为是否有意义。例如在浏览时，假如没有内心独白，这时模型进行了滚动操作，我们就无法判断这个动作是否有意义，更不可能对这个动作提供奖励。但是，如果有内心独白，模型就可以告诉我们滚动操作的原因，我们就可以查看该动作并判断是否有意义。

通过内心独白，我们可以对模型的操作做出反馈，可以在更短的时间内使用RL训练模型，同时还能让模型系统更安全，因为我们没有优化可能导致奇怪结果的长期行为。

**问：我一直在用古典文学和哲学信息训练模型，在这个过程中，我对“什么是美？”这类问题很感兴趣，美的定义有千千万万种，你如何评估那些不同答案的相对矩阵的定量测量，它们是否优先于输出？
**

**答：**模型生成的答案应该是客观，没有价值偏向的，很难处理带有个人偏好、价值选择的问题，对于这类问题我们还没有找到好的处理方法。

目前为止，我们并不赞同让模型对事物拥有自己的看法，相反，我们让模型去描述人类的想法，希望模型将“什么是美”这类问题重新定向为更加真实的问题，例如人类或学校对这个问题的看法是什么。

其他人都在看

###

-   [向量嵌入：AutoGPT的幻觉解法](http://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247491455&idx=1&sn=28708a6e196149c588d071a4df860c82&chksm=fe419149c936185f48561f06e3e0847733aa9eec358c4f85f8e7a509278890b5ff1abe2ce31f&scene=21#wechat_redirect)

-   [推演语言模型的大小与计算开销](http://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247491417&idx=1&sn=445f1c73d6ff1cae4aeb8d0c597c2423&chksm=fe41916fc93618793120f567c0f1a2ba57c05ba8ae8c79d913fc3d371c66afafe7d5cfb52d5b&scene=21#wechat_redirect)

-   [谷歌科学家：RLHF的演进与局限](http://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247491345&idx=1&sn=357696700e6e1401f3bd264d84bf13b5&chksm=fe419127c93618312852f18c47f713038013c0a01d46e0105356b65b976760a4f9f9eb3a7fed&scene=21#wechat_redirect)

-   [John Shulman：ChatGPT成功的秘密武器](http://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247490988&idx=1&sn=664b9b90504c75ed0f27b0651f3aad2f&chksm=fe41939ac9361a8c400c2310c4297ef6a80f626731e32cca276504e4b4b8c9a38c6d63eea3f1&scene=21#wechat_redirect)

-   [比快更快，开源Stable Diffusion刷新作图速度](http://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247489843&idx=1&sn=f32143165779a5c96d4861d657286ea6&chksm=fe419705c9361e13ef901009ec002ac74ea8e7c269f8cb21c6d6edb8671e08acf1a836f76b7f&scene=21#wechat_redirect)

-   [OneEmbedding:单卡](http://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247488841&idx=1&sn=6c5de6713dbce2bd25d60db742879368&chksm=fe419b7fc93612690a667bec72a258ac837c2454cd180c2432c1c190bc236743cf7e4dd0dfee&scene=21#wechat_redirect)[训练TB级推荐模型不是梦](http://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247488841&idx=1&sn=6c5de6713dbce2bd25d60db742879368&chksm=fe419b7fc93612690a667bec72a258ac837c2454cd180c2432c1c190bc236743cf7e4dd0dfee&scene=21#wechat_redirect)

-   [GLM训练加速：性能最高提升3倍，显存节省1/3](http://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247490555&idx=1&sn=280c4ac043a31170236a9d8fba5fc2d2&chksm=fe4195cdc9361cdb6db1cb3b77c66b45c353b2fb65c4d082fbae9b72fe0b3a441ab9101cb147&scene=21#wechat_redirect)

试用OneFlow: github.com/Oneflow-Inc/oneflow/

![图片](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWqmn57vjianzhXvg4qEFvAzJkKhpfLyrSR09ubccKSEaBia5vaV5S21dYQJiaQ0ZKtic9icPicUKQOLDDwQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=23)