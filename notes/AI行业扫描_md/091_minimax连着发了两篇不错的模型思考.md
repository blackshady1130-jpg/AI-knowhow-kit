---
url: https://mp.weixin.qq.com/s/5Q-bNc7lAmEuJn23q0_ZzQ?scene=1
title: "与什么对齐？在MiniMax M2中重新思考Agent泛化"
author: "Junheng"
captured_at: "2026-03-09T03:27:42.813Z"
---

# 与什么对齐？在MiniMax M2中重新思考Agent泛化

MiniMax M2模型发布期间，收获了社区的很多关注。我们感到非常兴奋，许多人都强调了它在复杂的 Agent任务中令人印象深刻的表现。这对我来说尤其激动人心，因为我的工作重点是后训练的Agent对齐部分。通过这篇文章，我想分享一些我们在此过程中的想法和经验。

### Agent对齐的实际问题：**Benchmark，还是**实际表现？

一直以来，大模型 LLM Agent 的体验者应该都遇到过这样的问题，同一个模型在不同的脚手架里表现差异非常大。一个Agent可能在 Tool-use 排行榜上名列前茅，但实战下来模型在真实场景中的可用性却非常差。Benchmark与实际可用性之间的这种差距是该领域最大的挑战之一。

在M2立项初期，我们就知道必须直面这个问题。我们确定了两个核心的目标：

-   **在开源Benchmark上表现出色。** Benchmark对于衡量很多纯粹的能力至关重要。例如，BrowseComp**可以**测试模型的复杂搜索能力。虽然用户很少会问像“找到一篇论文，其中第n位作者名字的第三个字母是‘x’”这样刻意设计的问题，但一个能解决这个问题的模型证明了它拥有强大的基础能力。

-   **稳健地泛化到实际使用场景。** 这是更难、更重要的部分。一个优秀的Agent必须在不同的新工具、各种Code IDE/Cli、Agent脚手架以及其他用户可能使用的场景上，都有足够稳定的表现，即模型必须拥有足够好的泛化能力。

那么，我们到底要与什么对齐呢？答案是两者都要。我们需要与Benchmark对齐以构建技能，但我们最终必须与用户对齐，确保这些技能在任何场景下都有效。

如何在Benchmark中取得好成绩的方法是另一个值得深入探讨的话题，但今天我想专注于谈谈第二点，也是更棘手的目标：我们如何为真实使用场景训练一个Agent？

### 交错思维链（Interleaved Thinking）的必要性

最初做这个项目的时候，我们也比较苦恼这个问题。Agent的性能不一致，我们很难判断原因。经过和何俊贤教授、陈文虎教授一起多次讨论，得到了第一个结论，Agent 需要 Interleaved Thinking能力。

这意味着智能体的自我纠察——即其“thinking”过程——可以在任务执行过程中的任何时刻发生，而不仅仅像Reasoning Model那样只在开始时进行一次。这种设计至关重要，原因有二：

-   **在长程任务中保持专注。**复杂的Agent任务通常上下文很长。仅在开始时进行一次thinking不足以维持指令的遵循和连贯性。

-   **适应外部扰动（External Perturbations）。** 这是Agent任务和普通的推理任务至关重要的区别。Agent任务会不断引入来自外部（如工具返回内容）、不可预测的扰动。模型必须足够稳定，以处理这些扰动、诊断错误并提取有用信息。模型的思考过程允许它根据来自环境的新信息不断地重新评估和调整。这一特性成为了M2稳定、有效的关键因素。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

PS：由于M2采用interleaved thinking能力，因此**在Agent任务中，需要保留全部的上下文，包括thinking内容** （这一点和推理模型不同，推理模型使用中通常会把前文的thinking内容删掉），当前有一些社区反馈M2的效果和宣传不符的情况大多和这个特点有关，这个内容在MiniMax关于[Interleaved Thinking的介绍文章](https://mp.weixin.qq.com/s?__biz=MzE5MTA3NzcxMQ==&mid=2247487075&idx=1&sn=55778d066e54a7e8af9f2146eb02dae9&scene=21#wechat_redirect)中有提及。

### 真正的泛化在于应对扰动

我们最初的想法很简单：工具的scaling就是智能体泛化。

我们从工具的最小集（Python解释器、Search搜索引擎、Browse网页浏览）三个工具出发，建立最小的工具调用能力，然后通过工具数量的scaling，将Agent能力能够推广泛化出去，在各种未知的工具上都能有比较好的表现。

起初，项目沿着这样的技术路线推动得比较顺利，Benchmark的分数很快就达到了比较不错的水平。但随着认知的加深，会发现Agent的泛化不仅仅是工具的泛化这一件事。模型在Benchmark上表现良好，但如果环境进行了变化，比如换一个脚手架，模型能力会大幅下降，这距离我们一个好的“实用性”的模型的目标还差很多。

这让我们得出了第二个，也是更深刻的认识：Agent泛化不仅仅是适应新工具，它是关于**在模型一切可能的操作空间上的扰动适应**这件事**。**

这听起来可能有些抽象，让我们来拆解一下。在一个单一的Agent任务中，所有可能变化的因素有：

-   **工具信息（Tool Info）** 和可用的工具集

-   定义Agent角色和规则的**系统指令（System Prompt）**

-   **用户指令（User Prompt）**和具体目标。

-   **环境（Env，包括文件、Codebases、****API****等**）

-   每一步的**工具返回（Tool Responses）**

……

我们最初的“工具scaling”方法只解决了第一项，但忽略了过程中其他部分的扰动。有了这个新的理解，我们的团队设计了一整套**覆盖全轨迹泛化的数据链路**。通过这样链路产生的数据，可以保证在绝大多数的扰动下，都能有比较稳定的工具表现。我们的一些实验结果也是非常令人振奋的，在内部测试中，我们尝试了很多基本没有考虑过的冷门的脚手架，模型在上面的表现都是超出预期的，无论是工具调用还是指令遵循，都得到了良好的泛化。

### **未来工作**

在设计M2的过程中，我们积累了非常多的关于Agent/泛化/数据相关的认知，很多想法还没有实施落地。未来，我们会在泛化上做更深入的探索，也希望给大家带来强大且真正有用的模型。

![图片](https://mmbiz.qpic.cn/mmbiz_png/q4wL2iaHZfGkCR4D4XPmK9WOI3vatCfyiazjxP2oTSSpmmdzQwrI0ibZlhDuAYgGmdoUw7c22962SfU35cBiaoTXow/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)