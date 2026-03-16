---
url: https://mp.weixin.qq.com/s/l4n1B4XnQ7pNl5v8GViLhA
title: "Scaling能通往AGI吗？"
description: "如果scaling law失效，实现AGI就会非常漫长和艰难。"
captured_at: "2026-03-08T11:31:11.523Z"
---

# Scaling能通往AGI吗？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/3tHNibnJ2jgwhIm2bbW4MMvHJ9CfgB1Dn0fa3pMLntYnVvRz31rBty9zDAia5PklCpIEOnVqw0G2BAuhuz99tfPw/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwhIm2bbW4MMvHJ9CfgB1DnIGVLucUAUn2vl7kBgHkI6GxWDyushfVT8zhUYAn79mJJdJwda7mKQA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwhIm2bbW4MMvHJ9CfgB1DnNX171rGeOUkM2qI9VTd8O5pc9zu6nD53YlnUZyg1XJYVicqMTy3iaDYg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

作者：Dwarkesh Patel

编译：Lavida, Chenxin

编辑：Siqi

排版：Scout

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwhIm2bbW4MMvHJ9CfgB1DnfbBcXbQU6XoxSch2pxSwozZ9wicwyvGsj4NVKX00Q9C0libWgOyibicicBw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

几乎所有关于 LLM 的讨论都无法跳开 scaling law，它被看作是 OpenAI 最核心的技术，Sora 的出现也被认为是 scaling law 的又一次成功。与此同时，关于 scaling 还能继续有效的讨论也在展开，如果以实现 AGI 作为目标，它会是带领我们通向 AGI 的终极钥匙吗？

本文编译自科技博主 Dwarkesh Patel 的个人博客，这篇文章首先对现阶段社区围绕 scaling law 的争议与讨论的关键问题进行了梳理，并对支持或质疑 scaling law 的声音进行了解读分析。

**Dwarkesh 预计，有 70% 左右的概率人们能够通过 scaling** **在** **2040 年之前实现更强的 AI，这种 AI 能够实现大量认知劳动的自动化，进而促进 AI 的进一步发展。****但如果 scaling law 失效，那么实现 AGI 的过程会非常漫长和艰难。**

为了更全面地呈现关于 scaling law 的不同态度，本文将以“积极观点”和“消极观点”辩论的形式呈现。

**01.**

**讨论 1: 现有数据会被用光吗？**

**消极观点：**2024 年，高质量的语言数据将会用尽。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

根据 scaling law 曲线，我们需要大概 1e35 次浮点运算（FLOPs）才能训练出一个聪明到能写论文的 AI，然后在这个基础上再进一步自动化 AI 研究，并且在以后 scaling law 不起作用时还能继续迭代下去。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

换句话说，我们需要的数据比现有的数据还要多出 5 个数量级。

**原文注：**根据 Chinchilla Optimal Scaling 原则，虽然我们可以用非最优的方式训练模型，但这只能弥补较少的数据不足，而不是 5 个数量级的短缺。Chinchilla Optimal Scaling 来自 DeepMind 的研究，简单来说就是为了高效 scaling，需要同时增加训练数据量和模型参数量，并找到二者的平衡点，只关注任何一个都会限制模型的性能提升。

**需要注意的是“5 个数量级”并不是 5 倍，“少 5 个数量级”意味着现有数据可能只有我们真正需要的 10 万分之一。**虽然我们可以通过一些方法来提高数据利用效率，比如多模态训练、循环利用同一数据集（token recycling）、课程学习（curriculum learning）等，但依然很难满足 scaling law 指数式增长的数据需求。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*不同模型所需 Token 数量对比*

所以有人提出可以用 self-play 和合成数据（synthetic data）的方法，但 self-play 面临下面的两大难题：

**• 评估：**AlphaGo 之所以可以用 self-play 的方法训练，是因为在围棋这个场景下，模型能够基于“是否赢得比赛”来做自我评估，但现在的很多推理任务并没有这样明确的标准，LLM 也因此无法修正自己的推理错误。

**• 计算：**在 AlphaGo 和类似的数学或编程方法中，常常会用到各种树状搜索（tree search）技术，在树的每个节点多次运行 LLM。在围棋这样范围相对确定的任务里，AlphaGo 的计算量已经很大，要想搜索所有人类思考过程的可能性，还得处理更多数据和更复杂的参数，计算量只会更加庞大。**和人类思维水平相当的计算量大概是 1e35 FLOP ，也就是要在当前最大模型的基础上额外增加 9 个数量级的计算能力。就算未来我们能通过硬件和算法进一步优化，9 个数量级的提升真的可能吗？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*蒙特卡洛树搜索（MCTS）*

**积极观点：**如果只是因为数据短缺这个原因质疑 scaling law 的可行性，那么其实不应该有“我本来也觉得继续做 transformer 模型 scaling 就能实现 AGI，但问题是数据很快就会用完了”这样的想法，相反，应该去想“原来只要互联网数据足够充足，继续 scaling 下去就能训练出有人类智能水平的 AI ”。

**LLM 在处理数据时效率并不高，因为训练用的数据样本大多是广告这种低质量文本（e-commerce junk\*），而预测下一个 token 的训练方式会让模型变得更加低效。如果用损失函数来评估，这与我们期待智能 Agent 在经济活动中实际执行的工作完全无关。但我们还是用这种方法，花了等同于微软年收 0.03% 的投资从互联网上抓取了大量数据，并且训练出了一个初级 AGI，也就是 GPT-4。**

**\*原文注：****与人类相比，LLM 的样本效率的确比较低，GPT-4 所处理的数据量远超过一个人从出生到成年所见到的数据，却远不如人类聪明。但这个判断没有考虑到一点：人类的基因中包含了亿万年进化过程中累积的知识，可以看作是被高度浓缩过的精华信息，是人类祖先通过与环境互动并在长时间内进行自然选择的结果。这种遗传知识为我们提供了一种在出生时就携带的、对世界的基本理解，而这是 LLM 所不具备的。**

既然 AI 至今的进化方法这么简单，如果以后合成数据也能起作用的话，我们也不用惊讶，毕竟“the models just want to learn”（**拾象注：**原话引用自 Dwarkesh 对 [Anthropic CEO Dario Amodei 的采访](http://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247504129&idx=1&sn=71c27329771d12a401fb28b7bbaa1d8e&chksm=ce9b6e9ff9ece78955e0ce922e3ec34d6b9d170b78608870a2a2e148e358d7a916633c7084d3&scene=21#wechat_redirect)，Dario 提到这是 OpenAI 创立前 Ilya 最初对 Dario 说过的话，并且给了他很多启发）

GPT-4 发布了 8 个月之后，其他 AI labs 才陆续推出和 GPT-4 能力齐平的模型，也就是说研究人员现在才开始让这代模型做 self-play。总结来讲，目前没有公开证据显示合成数据在大规模应用中有效，并不意味着它就发挥不了作用。

一旦 foundation model 能偶尔给出正确答案，强化学习就会更加可行。模型完成任务的的成功率会慢慢从 1% 提升到 10%，再到 90%，这时就可以尝试更复杂的任务，比如 1000 行 pull request 请求。模型不仅成功率会更高，还能在失败时自我纠正，模型性能就会在这样的循环过程中得到提升。

回顾人类的进化过程，会发现和现在模型利用合成数据来自我强化非常相似。起初，我们的祖先很难迅速领悟和使用新知，**但自从人类发展出语言后，就出现了基因与文化的共同进化，这与 LLM 的合成数据和 self-play 循环非常相似。模型也是在相似的过程中变得更加智能，更好理解相似模型的复杂符号输出。**

**Self-play 并不需要模型在自我评判逻辑推理时做到完美，只要比模型从零开始推理做得更好就可以了，这也是目前我们看到的现实。**这点可以参考 Constitutional AI，或者自己试试 GPT，就会发现它更擅长分析用户哪里写得不对，而非自己独立得出正确答案。

**原文注：**如果评估者也是 GPT-4 这种性能有限的模型，self-play 循环可能会更加有效。在 GAN 中，如果鉴别器（Discriminator）远比生成器（Generator）强大，那它就会停止向生成器提供任何反馈，因为它无法给出不完美但具有正确方向的信号。

换句话说，如果鉴别器和生成器的能力相差太远，那就会阻碍学习过程。鉴别器需要足够的能力来识别生成的数据，但同时不能强大到完全没有失败的空间，否则它就无法给生成器正确的学习信号来引导优化。

我接触过的几乎所有 AI 研究员都对 self-play 很有信心，但因为保密原因他们不能透露具体细节，只提过有很多可尝试的方向。就像我[采访 Anthropic CEO Dario Amodei](http://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247504129&idx=1&sn=71c27329771d12a401fb28b7bbaa1d8e&chksm=ce9b6e9ff9ece78955e0ce922e3ec34d6b9d170b78608870a2a2e148e358d7a916633c7084d3&scene=21#wechat_redirect) 时他说的：“因为各种原因我不方便讲太深，但世界上有丰富的数据来源，生成数据的方法也很多，我个人认为这不会成为阻碍。其实，如果数据真的成为障碍反而会更好，但实际上并不会。”

**消极观点：****Constitutional AI、RLHF 和其他基于 RL 和 self-play 既能发掘模型潜能，也能在必要时约束模型，但目前还没人能证明通过 RL 能真正提高模型的底层能力。**

如果 self-play 或合成数据的方法不起作用，那么我们就很难突破数据瓶颈。寄希望于新的架构也不切实际——新架构需要大幅提升样本效率，而且这个提升要比 LSTM 到 Transformer 的跨越还大得多，但 LSTM 出现至今已经 20 年了，那些好攻克的问题早就已经解决，要想继续取得突破是很困难的。

虽然 LLM 的支持者和利益相关方都对模型 scaling 评价很积极，但这并不能改变客观事实，我们确实还没有证据表明 RL 能够解决数据量级不足的问题。

此外，**LLM 在极为庞大的数据量训练下推理水平也一般，这表明模型还不具备泛化能力。**如果模型无法利用人类两万年所积累的数据量达到接近人类水平的性能表现，那么即使有 20 亿年的数据量也不够，就像无论你给飞机加多少喷气燃料也不能让它上月球一样。

**02.**

**讨论 2: Scaling Law 真的起过作用吗？**

**积极观点：**这点毫无疑问，在各种基准测试中，模型的性能已经稳步提升了 8 个数量级。即便在计算资源增加了百万倍的情况下，模型性能的损失仍然可以精确到小数点后多位。

GPT-4 的技术报告指出，他们能够通过较小实验模型上预测最终 GPT-4 模型的性能，训练的方法和 GPT-4 相似，但计算能力远少于 GPT-4，可能只有万分之一。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*GPT-4 性能预测*

至今 LLM 在过去 8 个数量级的性能提升都非常稳定，这个趋势也会持续。而且通过接下来 8 个数量级的 scaling，以及算法和硬件进步带来的性能提升，我们很可能会得到性能更为强大的模型来加速 AI 研究。

**消极观点：**我们并不关心模型在预测下个 Token 的任务上表现如何，模型在这方面已经超过人类了，我们关心的是在这个任务上的 scaling law 曲线是否能说明模型的泛化能力已经有实质提升了。

**积极观点：**随着模型不断 scaling，MMLU、BIG-bench 和 HumanEval 等基准测试都表明模型在各类任务上的性能都有了明显提升。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*HumanEval 基准测试*

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*MMLU 基准测试*

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*BIG-Bench 基准测试*

**消极观点：**但只要你随便看几个 MMLU 和 BigBench 的测试样本，就会发现几乎全是谷歌搜一下就能查到的结果，这种问题更像是在测试模型的记忆力，而非智能程度。以下是一些我从 MMLU 随机挑选出来的问题，原题都是选择题，模型只需从四个选项中选出正确答案：

Q：根据 Baier 的理论，判断一个行为是否道德上可接受的第二步是什么？

A：确定禁止这种行为的道德规则是否是真正的道德规则。

Q：哪一项总是适用于自发过程（spontaneous process）？

A：系统加环境的总熵（entropy）增加。

Q：克林顿出生时的美国总统是谁？

A：杜鲁门。

网络上本来就有各种各样的文本和随机事实（拾象注：指一些脱离特定上下文、独立存在的信息碎片或数据点），模型基于这些数据训练，记住了再返回给人类，这能说明模型有智能和创造力吗？

在这些人为制定的基准测试中，模型的性能提升已经显示出了瓶颈。尽管 Google 的 Gemini Ultra 模型的计算能力比 GPT-4 高出近 5 倍，但在标准基准测试如 MMLU、BIG-bench 等上的表现几乎和 GPT-4 相当。

**现有的基准测试通常不衡量模型在长期任务上的性能表现，比如能不能在一个月内里完成一项任务。**因为模型是基于下一个 Token 预测训练的，所以在长期任务上几乎没有有效的数据点进行学习。SWE-bench 测试显示（衡量 LLM 是否能够自主完成 pull request 的测试），模型在处理长时间跨度的复杂信息时表现不佳。GPT-4 的得分只有 1.7%，Claude 2 表现稍好，达到了 4.8%。

目前主要有两种基准测试：

• **一种是评估模型的记忆、召回和插值能力（interpolation）的测试，包括 MMLU、BIG-bench 和 HumanEval。**在这些测试中，模型展现出了和人类平均水平相当甚至更高的性能表现，但这并不能作为智能程度的准确衡量标准，因为当前模型在智力方面远不如人类。

• **另一种是真正考察模型在长期任务执行或处理复杂概念上能力的测试，包括 SWE-bench 和 ARC**，模型在这类测试中的表现并不出色。

当一个模型经过了相当于人类 2 万年输入的数据量训练，却仍然无法理解 “Tom 的母亲是 Mary，Mary 的儿子就是 Tom ”这种简单的逻辑关系，而且给出的回答还极度依赖问题的表述方式和顺序时，我们该如何评价这个模型呢？

所以我觉得没必要讨论 scaling 未来是不是还有效，因为 scaling 至今有没有起过作用都存疑。

**积极观点：**有些人认为 Gemini Ultra 的性能到了一个平台期，这是很不合理的。在 GPT 出现之前，有一部分人对连接主义（Connectionism）和深度学习提出过质疑，但 GPT-4 的出现打破了这种观点。现在 Gemini 的性能相对 GPT-4 有限，主要是因为谷歌在算法提升上还赶不上 OpenAI。

连接主义（Connectionism）是认知科学中的一个理论框架，它假设心智功能可以由大量简单的计算单元（通常指神经元）之间的相互连接和交互来解释，在心理学、AI、机器学习和认知神经科学等领域都有应用。

连接主义模型通常是通过神经网络（无论是生物学的还是人工的）来实现的，它们模拟了大脑中神经元之间复杂的网络结构。在 AI 中，连接主义的概念已经演化为现代的深度学习技术，其中多层神经网络已经成为解决复杂问题（如图像识别、自然语言处理等）的强大工具。

如果深度学习和 LLM 真的有底层局限性，那在它开始具备常识和抽象思维能力之前就能看出来了，不需要等到现在。

GPT-4 相比 GPT-3 性能有了巨大提升，这是通过 100 倍 scaleup 实现的。100 倍看起来很多，但其实未来模型可能会扩大到一万倍，也就是 GPT-6 的水平，而且到这个水平所需的资金还不到世界 GDP 的 1%。这还没算上其他可能提升性能的因素，比如提高预训练的计算效率（MoE、flash attention 技术等）、新的训练方法（RLAI、对思维链进行 fine tuning、self-play 等），还有硬件的进步。这些都能让性能有很大提升很多。这样算下来，我们可能只需要花全球 GDP 的 1% 就能造出 GPT-8 级别的模型。

我们可以回顾一下历史上每次新技术出现时政府的投资力度：

• 1847 年，英国铁路投资的 GDP 占比高达 7%，达到历史峰值。

• 1996 年美国《电信法》实施，在接下来的五年内，美国电信公司的总投资超过了 5000 亿美元（相当于当下的一万亿美元），主要用于铺设光纤电缆，增设新交换机和建设无线网络。

我不懂为什么大家认为 GPT-8 可能比 GPT-4 强不了多少，按发展趋势来说，GPT-8 的性能应该是 GPT-4 的 1 亿倍，而且模型即使在远小于这个规模的 scaling 中也已经学会了如何思考和理解世界。

我预想未来的情景是这样的，会有几百万个 GPT-8 一起工作，它们会一起改进核心代码，找到更好的超参数，给模型的 fine tuning 提供很多高质量的反馈。开发 GPT-9 的经济与技术成本将大幅降低，如果这个趋势持续下去，我们有希望到达奇点。

**03.**

**讨论 3: 模型真的能理解世界吗？**

**积极观点：**为了预测下一个 Token，LLM 必须学习万物背后的规律，理解 Token 之间的联系。比如说模型得先明白进化论，才能推理《自私的基因》（The Selfish Gene）中某段接下来的内容；在短篇小说中就要先理解人物的心理活动，才能猜出故事后面的情节。

有个有趣的点是，通过大量的代码学习可以提高 LLM 的语言推理能力，这说明模型能从代码中提炼出一些通用的思考模式。**这不仅意味着语言和代码之间有相似的逻辑结构，而且意味着无监督学习能够发现并利用这种结构，从而提升 LLM 的推理能力。**

梯度下降（Gradient descent）的目标是找到最能压缩数据的方法。最高效的压缩方法也是最能深入理解数据的方法。比如，如果你能把一本物理书的“压缩”（compression）做得很好，你就能预测书中没涉及的部分可能是怎样的，这是因为你已经深刻理解了基本的科学原理。

**消极观点：****智能包括但不限于压缩，但压缩并不等同于智能。**我们都知道爱因斯坦很聪明，因为他提出了相对论，但这并不意味着爱因斯坦加上相对论就构成了一个更为智能的系统。也不能因为柏拉图不懂现代生物学或物理学，就说他的智力不及拥有这些知识的我。

**原文注：**其实“智能=压缩”这个说法也不够准确，信息压缩不能等于爱因斯坦的创造性和深刻洞察力，随机梯度下降（SGD）是在光滑的损失函数中渐进地总结出语义规律，爱因斯坦则是在一片错误的排列和变体中找到相对论正确方程的差异。对 Scaling Law 持消极观点的人认为没有任何理由相信 SGD 能够通过“压缩”变得像爱因斯坦那样聪明。

因此，如果 LLM 仅仅是由另一个过程（SGD）产生的压缩结果，那么我们将无从判断 LLM 本身具备的压缩能力，更无从判断 LLM 的智能水平。

**积极观点：**我们目前并不需要一个完美的理论来证明 scaling 会持续有效。回顾历史，我们会发现蒸汽机出来一百多年我们才完全理解了热力学。**技术进步往往是先有发明，然后才有理论的完善。对于智能技术的发展，我们也应该有这样的预期。**

没有哪个物理定律能保证摩尔定律会一直有效。随着技术不断发展，我们总会遇到新的难题，但这不意味着摩尔定律就失效了。未来，台积电、英特尔、AMD 这些大公司的研发团队就会找到新的办法来解决这些问题，让 scaling law 在接下来几十年持续发挥作用。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*摩尔定律的延续*

**04.**

**结论**

最后我想谈谈我的个人看法。对于之前一直相信 scaling law 的人来说，至今为止 AI 的发展看起来会合理得多。据说 GPT-4 之所以性能这么优越，是因为在训练中用了习语库（idiom library）或者查找表（lookup table），但这种工具很难通用，然而上面的消极观点并没有提到这种可能性。

像 Ilya、Dario、Gwern 这样信仰 scaling law 的人，早在 12 年前就预见了我们近期看到的 AI 实现的飞跃。

可以确定的是，适当的 scaling 确实能够让我们创造出一种革命性的 AI，也就是说如果达到了曲线上的最小不可约损耗（指在最优模型训练完成后仍然存在的误差），就能训练出一个智能 AI 来完成大多数认知工作，包括辅助进行更高智能水平 AI 的迭代。

然而，现实生活里的事情往往比书本上的理论要复杂得多，有些理论上看起来可行的事情，比如核聚变、飞行汽车、纳米技术，实际上却很难实现。同样的道理，如果用 self-play 或者合成数据的方法来提高模型性能不可行，那模型可能就是没法再优化，也达不到理论上的最低损失点了。而且现在支持 scaling 持续有效的理论依据还不明确，虽然有基准测试显示 scaling 能提升模型性能，但这些测试本身的标准也存在争议。

总的来说，我初步判断会有两种情况：

第一种：继续 scaling、改进算法和硬件技术，我们能在 2040 年之前实现 AGI，这个可能性是 70%。

第二种：我们现在研究的 LLM 和类似技术都行不通，未来会遇到一个很难突破的瓶颈，这个可能性是 30%。

需要说明的是，出于保密原因，AI labs 通常不会公开研究成果，所以可能有些关于 AGI 的重要信息我并不知道。而且根据我在 AI labs 工作的朋友说的，目前公开发表的信息价值不高，所以上述判断可能会不太准确。

**05.**

**附录**

下面还有一些我思考过的问题，但我还不确定下面这些问题对于 scaling 来说意味着什么。

**模型能否实现领悟式的学习？** 

**积极观点：**在不断 scaling 后，模型自然会发展出更高效的元学习（meta-learning）方法，类似人类学习和“领悟”知识（grokking）的能力。不过，这种“领悟”通常发生在模型过度参数化，并出现数据严重过拟合时。这跟我们人类学习新东西有点像，我们会用直觉和已有的知识框架来理解新信息，随着观察不断增加，我们的知识框架也会不断更新。在处理一大堆不同数据的时候，模型会找到那些最通用、最能举一反三的方法。这样，它们就能像人类一样，通过这种“领悟”来学习，最终达到深入理解。

**消极观点：** 神经网络的确具备某种程度的“领悟”能力，但它们学习新知识的方式跟人类比起来差远了。比如说，如果你告诉一个小孩太阳是太阳系的中心，他马上就能理解晚上看到的星星是怎么回事。但是，如果你给一个没有学过天文学的模型输入哥白尼的理论，它不会立刻就能用这个新知识去理解相关的事情。模型需要在很多不同的情况下反复学习，才能慢慢“领悟”这些基本的概念。

到目前为止，我们还没有让模型实现领悟式的学习（insight-based learning）。而且，因为我们现在用的是梯度下降这种简单的优化方法，我甚至怀疑模型是不是真的能学习。我们一次次“喂”给模型数据，让模型一步步逼近最优点。但是要让模型实现这种学习能力，就像是要求它从平地直接跳到珠穆朗玛峰的山顶，这种飞跃式的提升我们现在还做不到。

**灵长类动物的进化是否为 Scaling 提供了依据？** 

黑猩猩的智力上可能有很多比所谓的“逆转诅咒（reversal curse）”更严重的问题，但这并不意味着灵长类动物的大脑有什么根本性的缺陷，或者说他们不能通过增加大脑容量和 finetuning 来解决这些问题。

Suzana Herculano-Houzel 的研究显示，人类的大脑里神经元的数量，和把灵长类动物的大脑按比例放大后的神经元数量差不多。但啮齿类和食虫目动物就完全不同了，这些动物即使大脑体积较大，神经元数量也要少得多。

这表明，与其他物种的大脑相比，**灵长类的神经架构在某种程度上具有更好的可扩展性，这与 Transformer 在扩展性上优于 LSTM 和 RNN 的情况类似。**在灵长类动物生活的世界里，智力的一点点提升就能大大增强它们的生存竞争能力。这是因为智力能让它们更好地理解通过观察、尝试和相互交流学到的信息，这样就能更有效地提高它们的生存技能。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

延伸阅读

专访月之暗面杨植麟：lossless long context is everything

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Perplexity CEO：AI 创业公司要先做产品，后做模型

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

八问Canva：在AI时代称王还是落败？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwhIm2bbW4MMvHJ9CfgB1DnKicJMkYcaCR0zvVUoUicLOW9PddI9m7OEUFQEuuWY6v3KqGDE3NodC0g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22)

新摩尔时代：拾象 2024 LLM 猜想

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwhIm2bbW4MMvHJ9CfgB1DnKicJMkYcaCR0zvVUoUicLOW9PddI9m7OEUFQEuuWY6v3KqGDE3NodC0g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=24)

专访VideoPoet作者：LLM能带来真正的视觉智能

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwhIm2bbW4MMvHJ9CfgB1DnKicJMkYcaCR0zvVUoUicLOW9PddI9m7OEUFQEuuWY6v3KqGDE3NodC0g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=26)