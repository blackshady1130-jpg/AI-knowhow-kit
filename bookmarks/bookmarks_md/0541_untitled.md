---
url: https://mp.weixin.qq.com/s/C-1W_44vReGerR2mLMW6ag
title: "“提示工程”的技术分类"
description: "开始从范式上明白什么是“提示工程”了......."
author: "半吊子全栈工匠"
captured_at: "2026-03-08T12:18:32.400Z"
---

# “提示工程”的技术分类

尽管大模型非常强大，但仍然有着自身的局限。大模型可以生成看起来非常值得信赖的内容并引用外部资源，但是，大模型本身并不能直接访问互联网也不能访问互联网的资源。偏见往往会使大模型产生某些定型的内容。当被问到一个不知道答案的问题时，大模型有时会产生“幻觉”或者产生错误的信息, 很多时候，即使是最简单的数学或常识的问题, 大模型仍然要挣扎一番。另外，通过操纵提示词，以忽略开发人员的指令并生成特定的内容。

大多数提示技术主要解决幻觉和解决数学/常识问题，而偏见和提示词攻击是需要单独讨论的话题。提示技术离不开提示词的编写，一些常见的规则可以帮助我们写出清晰而具体的提示词，例如：

-   准确地说出要做什么(写、总结、提取信息) ；

-   避免说什么不该做，而是说什么该做；

-   具体描述，不要说“几句话”，要说“两三句话”；

-   添加标记或分隔符以结构化提示符；

-   如果需要，请求结构化输出(JSON，HTML) ；

-   要求模型验证是否满足条件(例如: 如果你不知道答案，请说”没有相关资料“) ；

-   要求模型首先解释，然后提供答案(否则模型可能会试图证明一个不正确的答案)。

通过提示工程技术，我们可以引入更多的时间和空间以及内容的属性，有助于更好地生成提示词。那么，提示工程技术有哪些呢？我们如何更好地使用它们呢？

分类是认知的开始。现有的大多数提示技术可以分为三类:

-   单一提示技术：旨在优化一个提示的响应

-   多重提示技术：为了解决任务而多次查询模型(或模型) 

-   大模型与外部工具结合的技术

## 1 单一提示技术

![图片](https://mmbiz.qpic.cn/mmbiz_png/DE2dk1GjczoW9Hl0dBtKR9smtjXhRibdJm6tRy5PmPiaYerice85xoJbBlD1pIWTJTo3EIJQg4uXPMAseWNHyquzg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

LLM 非常擅长一次性学习，但是他们仍然可能在复杂的任务中失败。单一提示技术是提示工程的基础，常见的技术手段有：

-   Zero-Shot：使用自然语言指令的最简单的技术。

-   One-shot：一次性学习

-   Few-Shot：用正确的答案向模型演示类似的任务，提供一些关于标签空间、输入测试的分布和序列的整体格式的示例

-   Chain of Thought（CoT）：思想链的提示通过中间的推理步骤使复杂的推理能力成为可能。这种技术旨在使模型对每个步骤进行迭代和推理。

-   Program-Aided Language Models (PAL)：一种通过使用代码将解释扩展为自然语言来扩展思维链提示的方法，可以将LangChain中的 PALChain 作为参考实现。

## 2\. 多重提示技术

基于不同的策略，将一个或几个提示技术组合在一起的，主要包括：

-   投票排名：应用投票来得到正确的答案，例如， 自我一致性的方法（Self-Consistency）。

-   分而治之：一组提示基于将复杂任务划分为几个提示，例如: 定向激励提示，知识生成，提示链，表链提示以及 Least-to-Most 的提示。

-   自我评估：将检查输出是否符合指令的步骤纳入框架，例如，思维树等。

### 2.1 投票排名

投票排名策略中的自我一致性方法基于这样的直觉: “一个复杂的推理问题通常需要多种不同的思维方式才能得到独一无二的正确答案”。它要求相同的思维链提示几次，从而产生一组不同的推理路径，然后通过应用投票选择最一致的答案.

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

一般地，对算术和常识任务而言，应用自我一致性的效果在常规基准测试中为4% -18% 。

### 2.2 分而治之

分治是算法设计中使用最为频繁的技术之一，在许多经典算法中都可以发现分治策略的影子。排序中的归并排序、快速排序，查找中的二分查找都是用分治策略来实现的。分治策略的思想是将一个复杂的问题分解为两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到最后子问题可以简单的直接求解，原问题的解即子问题的解的合并。

#### 定向激励提示

在定向激励提示中有两个步骤: 产生提示(例如，关键字)和使用它们来提高响应的质量。定向提示用于总结、对话响应应生成和思维链推理任务，包括两种模式:

-   一个小型可调整的策略模型被训练成产生提示(例如，一个暗示) ；

-   基于前一步的问题和提示，利用一个黑盒大模型来生成一个摘要。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

其中，策略模型可以通过监督下的微调来优化，使用标注数据和线下或基于 LLM 输出的在线奖励来强化学习，为 LLM 提供针对特定输入的指导，以达到期望的目标。

#### 知识生成

知识生成的提示技术使用一个单独的提示来首先生成知识，然后使用它来获得更好的响应。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

一般包括两个阶段:

-   生成知识: 使用few-shot从大模型生成与问题相关的知识陈述。

-   知识整合: 使用另一个打磨下对每个知识语句进行预测，然后选择最高置信度的预测。

该方法不需要对知识集成进行特定任务的监督，也不需要访问结构化的知识库，但它提高了大模型在常识推理任务上的性能。

#### 提示链

提示链是一种简单但功能强大的技术，这种技术将任务划分为子问题，并逐个提示模型。提示链对于完成复杂的任务非常有用，有助于提高 LLM 应用程序的透明度，增加可控性和可靠性。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Least to Most提示方法进一步添加了一个步骤，在这个步骤中，模型应该决定如何将任务分解为子问题，在与符号操作、组合概括和数学推理相关的任务中，Least to Most提示表现良好。
\[最小到最大提示.png\]()

#### 表链

表链提示技术，将表格数据被明确地用在推理链中作为中间思维结果的代理，该算法包括两个步骤：首先是动态规划，大模型根据输入查询和以前操作的历史记录从操作池中抽样下一个操作(操作链) ,参数生成涉及使用 LLM 和编程语言的应用程序为前一步操作中选定的参数(例如新的列名)生成参数，以执行操作并创建相应的中间表。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 2.3 自我评估

思维树（ToT）技术概括了思想链的方法，允许模型探索多个推理步骤和自我评估的选择。要实施 ToT 技术，必须决定四个问题:：

1.  如何将中间过程分解为思维步骤？

2.  如何从每个状态产生潜在的想法？

3.  如何启发式地计算状态(使用状态评估提示) ？

4.  使用什么样的搜索算法？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

输入的提示必须包括解决问题的中间步骤的描述，以及抽样的想法或生成这些想法的说明。状态评估提示必须提供指令，说明要在哪些提示上选择下一步。对于需要进行复杂计划或搜索的任务， ToT 相对成功。另外，LangChain 在experimental.tot.base.ToTChain 类中实现了思维树技术。

## 3\. 使用外部工具的大模型

实际上，使用外部工具的大模型提示技术就是基于大模型的应用，主要包括RAG 和Agent。

### 3.1 RAG

RAG 结合了信息检索组件和文本生成模型，在检索步骤中，系统通常使用向量搜索来搜索可能回答问题的相关文档。接下来，将相关文档作为上下文与初始问题一起传递给大模型. 在大多数情况下，使用 RAG 方法意味着我们检索 k 文档，并使用它们生成回答用户查询的所有输出令牌。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

RAG 中的大模型可以进行微调，但实际上很少这样做，因为经过预训练的 LLM 足够好，可以按原样使用，而且微调成本太高。此外，RAG 中的内部知识可以以一种有效的方式进行修改，而不需要对整个模型进行再训练。

RAG 产生的响应更加真实、具体和多样化，改善了事实验证的结果。关于RAG 的更多内容，可以参考《[大模型系列——解读RAG](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978863&idx=1&sn=73746b3a4453e27ed0f2d2ff28840c82&chksm=80d35109b7a4d81fef96f451ae279ec18cb0c12f6f0353e5ca0563929c682719cd00cb5e5dd0&scene=21#wechat_redirect)》。

### 3.2 Agent

当前，已经有多种agent 技术框架，这里简要介绍Reflexion 和ReAct。

反思（Reflexion）是一个通过语言反馈来强化语言主体的框架。反射代理通过语言反映任务反馈信号，然后在记忆缓存中维持自己的反思文本，以诱导更好的决策在随后的试验。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

一般地，反思框架由三种不同的模型组成:
\* Actor: 一个 LLM 模型，它基于状态观察生成文本和操作(使用 CoT 和 ReAct) 
\* Evaluator: 一个 LLM 模型，它对Actor产生的输出进行评分
\* Self-Reflection: 一个 LLM 模型，产生语言强化线索，以协助Actor自我完善

反思在需要顺序决策、编码和语言推理的任务中表现良好。

ReAct 的框架使用大模型以交错的方式生成推理轨迹和特定任务的行为: 推理轨迹帮助模型产生、跟踪和更新行动计划以及处理异常，而行为允许它与外部来源(如知识库或环境)接口交互并收集额外的信息。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

ReAct 框架可以选择一个可用的工具(如搜索引擎、计算器、 SQL 代理) ，应用它并分析结果以决定下一个操作。ReAct 通过与简单的 Wikipedia API 交互，克服了思维链推理中的幻觉和错误传播的普遍问题，并产生比没有推理痕迹的基线更可解释的类人任务解决轨迹。具体地，可以参考使用 Langchain 工具实现 ReAct 的示例。

关于Agent 的更多信息，可以参考《[基于大模型（LLM）的Agent 应用开发](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978548&idx=1&sn=9f66b39bd524bb569c9113b79cd31cfd&chksm=80d357d2b7a4dec402f4550ea7b10dc1a2792146a2e635e4251cd01b5cb2c2e3f7059b66ffd9&scene=21#wechat_redirect)》以及《[Agent 应用于提示工程](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978579&idx=1&sn=10bd1392b60197deb91779529e1f32ef&chksm=80d35635b7a4df237be3ae39ab3c75b9d98902e06d667fc0c4198e4b18ed206efa3526f91ecb&scene=21#wechat_redirect)》。

## 4\. 提示评估技术

提示技术的测试指标在很大程度上取决于应用程序和可用资源，大模型提示词中的最小变化非常敏感，这些变化不是最优的，而且往往是主观的。无论选择哪种提示技术，将提示工程视为数据科学的过程都非常重要。这意味着创建一个测试集并选择指标，调优提示并评估它对测试集的影响。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

尽管如此，提示的评估技术有一些基本的原则:

1.  事实性和相关性: 生成的答案有多真实, 生成的答案与问题的相关程度。

2.  检索：主要针对 RAG 和 Agent 管道，但可应用于生成的知识和定向提示，主要指标还是准召；

3.  内部思维方式: Agent 和工具选择的准确性，为 Agent 提取工具参数, 从上下文中检索到正确的参数并进行了适当的转换, 在多轮对话中记住事实，正确的逻辑步骤，例如反思和思维链提示

4.  非功能性：答案的风格和语气,没有偏见, 合规和安全检查, 提示注入实验。

## 5\. 提示工程的方法小结

在应用提示工程的时候，提示语要清晰而准确，这样模型就不必猜测我们的意图。我们可以使用分隔符或标记添加结构, 通过展示示例和添加解释来帮助模型, 要求模型反复思考，解释它的解决方案。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

对于复杂的提示词，请考虑将其拆分为子任务, 多问几次同样的问题, 并考虑添加一个模型自检的步骤。如果需要，将 LLM 与外部工具结合起来,并将提示调优视为一个数据科学过程，它是迭代的，需要评估。

**【参考资料与关联阅读】**

-   promptingguide.ai

-   “Large Language Models are Zero-Shot Reasoners”，https://arxiv.org/abs/2205.11916

-   “PAL: Program-aided Language Models”，https://arxiv.org/abs/2211.10435

-   “Self-Consistency Improves Chain of Thought Reasoning in Language Models”，https://arxiv.org/abs/2203.11171

-   “Least-to-Most Prompting Enables Complex Reasoning in Large Language Models”，https://arxiv.org/pdf/2205.10625.pdf

-   “Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding”，https://arxiv.org/pdf/2401.04398.pdf

-   [大模型应用的10种架构模式](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658979061&idx=1&sn=620225d1b690a40ea9f994e6a18d2a63&chksm=80d351d3b7a4d8c53931bca4b17472e5578fc1699c926b4f6da3500e1f099a1e75c9acf61c36&scene=21#wechat_redirect)

-   [7B？13B？175B？解读大模型的参数](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658979061&idx=1&sn=620225d1b690a40ea9f994e6a18d2a63&chksm=80d351d3b7a4d8c53931bca4b17472e5578fc1699c926b4f6da3500e1f099a1e75c9acf61c36&scene=21#wechat_redirect)

-   [大模型系列：提示词管理](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658979069&idx=1&sn=4f3eeacd30022536b1cb5fcdb643be5a&chksm=80d351dbb7a4d8cde7cda26b1a21be52111b772f403c2e800a0f5c5fc2e9a97b79d0c5f205c8&scene=21#wechat_redirect)

-   [提示工程中的10个设计模式](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978967&idx=1&sn=5012ce1cc195499f4217f01bd528fa6f&chksm=80d351b1b7a4d8a7cc6c4d107aa04e9b36ac794689e5a2f6022b1977fc70de29ef4775400ced&scene=21#wechat_redirect)

-   [解读：基于图的大模型提示技术](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658979256&idx=1&sn=69f4c5d6d550e8270f751d1c86c7ae40&chksm=80d3509eb7a4d988d2a9ab9801ccbbf42be7574698179f5bf04585cabf4ce11c1d95e3e73fb2&scene=21#wechat_redirect)

-   [大模型应用框架：LangChain与LlamaIndex的对比选择](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658979134&idx=1&sn=3ea4a1e6c921e7db7b341c949a35cdc3&chksm=80d35018b7a4d90e5f3d3d068b8c675725209dccad471b17b3b7737078b78e9042653b1d4480&scene=21#wechat_redirect)

-   [解读大模型应用的可观测性](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658979055&idx=1&sn=4aa0d1723cdc5390500403de69cea9f6&chksm=80d351c9b7a4d8df4df088edcf208c5ff13df1e4400a8a74a0d2462a9c89607f124c6cb6872d&scene=21#wechat_redirect)

-   [大模型系列之解读MoE](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658979008&idx=1&sn=844b706e5446cb9422aab888bd9f1382&chksm=80d351e6b7a4d8f0e9c92958c534c73ba92ac8f12ff9d22c519ebdf4d1664b13d6ddae9e3420&scene=21#wechat_redirect)

-   [在大模型RAG系统中应用知识图谱](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978896&idx=1&sn=582c532579ea29f06aa8ce17b4763a51&chksm=80d35176b7a4d8607a31ec05b89bb84f934114489a2595b1d0d27293e06eaacb087709e78420&scene=21#wechat_redirect)

-   [面向知识图谱的大模型应用](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978885&idx=1&sn=7cf63e04e65ad8c1cc1467d87cf30ed8&chksm=80d35163b7a4d87586b7d8adc79294b45303083f509710c5ae51630ce35e9db4e8726fa33e4d&scene=21#wechat_redirect)

-   [让知识图谱成为大模型的伴侣](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978848&idx=1&sn=26e35575c4a9634890e530f1a53ed8fe&chksm=80d35106b7a4d810e58031422149fa60d046229884f69a70f8e218ab596154173e3551ebba19&scene=21#wechat_redirect)

-   [如何构建基于大模型的App](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978464&idx=1&sn=8b9c617bced2b5ce012fb1f4aa87c086&chksm=80d35786b7a4de901400ffe4db5061c08df2912b4b49466e91a9f52813f22f3137e41802abc9&scene=21#wechat_redirect)

-   [Qcon2023: 大模型时代的技术人成长（简）](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978424&idx=1&sn=bf5e61ba5bc81f14724e6c2846af566f&chksm=80d3575eb7a4de486f624659156807d24292f2e38f4ee63100b52deed4759e5161dc4cf9cb8c&scene=21#wechat_redirect)

-   [论文学习笔记：增强学习应用于OS调度](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978155&idx=1&sn=d0a0a76832ce91fd4cbe73369906da6a&chksm=80d3544db7a4dd5b6dd8ea0e1f2c4ac16853d44f87ba61201592f46bea0c1d310a2c8389a290&scene=21#wechat_redirect)

-   [《深入浅出Embedding》随笔](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658977893&idx=1&sn=e7ff83f90a799592264c034273917685&chksm=80d35543b7a4dc55ab633be14d303ac0c040b09be059a4f33159a2d0db18620cdadf0dbe627e&scene=21#wechat_redirect)

-   [LLM的工程实践思考](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978144&idx=1&sn=e8bff055687f7e7ad17baca58dc26c23&chksm=80d35446b7a4dd507b02832851e2308a276edc328f3e79bca0f3ae931ab27db69aeccd8d7c8d&scene=21#wechat_redirect)

-   [大模型应用设计的10个思考](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978666&idx=1&sn=545a023d43da9d950df2591ac1627842&chksm=80d3564cb7a4df5a920fdec426694df4430c94529e8068b68a1290fc020f90ca1ef869970756&scene=21#wechat_redirect)

-   [基于大模型（LLM）的Agent 应用开发](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978548&idx=1&sn=9f66b39bd524bb569c9113b79cd31cfd&chksm=80d357d2b7a4dec402f4550ea7b10dc1a2792146a2e635e4251cd01b5cb2c2e3f7059b66ffd9&scene=21#wechat_redirect)

-   [解读大模型的微调](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978125&idx=1&sn=b342e9c10734c1f7cd124ebc88aa75a8&chksm=80d3546bb7a4dd7d9c74dabd6046d1ccea01592760a8add3d71b2f75fa68712093a4834e6d88&scene=21#wechat_redirect)

-   [解读向量数据库](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978665&idx=1&sn=10512636ac46b2df414ec862e7699841&chksm=80d3564fb7a4df59a43529f2f005c1db65dce7d1225634be5ccd5e817572c383fbe605db063a&scene=21#wechat_redirect)

-   [解读ChatGPT中的RLHF](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658977979&idx=1&sn=4d66d662595d9aba355e0564df545370&chksm=80d3559db7a4dc8b96a5f3ac4d01b53a2601d5e1dcb51789ee3d9974ec9ae5f028c3e469b5a5&scene=21#wechat_redirect)

-   [解读大模型（LLM）的token](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978496&idx=1&sn=ba69f0b46650d313a6ccaef16480a53b&chksm=80d357e6b7a4def09deac0dddf0085d1169894b0ccd6ed460cab7d03c219e432f6d2307b1c46&scene=21#wechat_redirect)

-   [解读提示词工程（Prompt Engineering）](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978546&idx=1&sn=21daeabd88f0d0f2b388f9dc123cd508&chksm=80d357d4b7a4dec2a762ccc582ff18db06240696aea4ac8df01c43895e0e09242d5e6a804ae3&scene=21#wechat_redirect)

-   [解读Toolformer](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658977935&idx=1&sn=9dd162f270f7c17a673291c0f136cf8c&chksm=80d355a9b7a4dcbf3ab824ac6de5c27d94a11455a681ebeb98a211e9b58ff867ddddf33d1c8d&scene=21#wechat_redirect)

-   [解读TaskMatrix.AI](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658977922&idx=1&sn=2f67513b540485d0177ded24c0807bcc&chksm=80d355a4b7a4dcb2495ab97febd0ac88cd0780e0d8e4b3bbc369250304289e289f71b0a76f0c&scene=21#wechat_redirect)

-   [解读LangChain](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978479&idx=1&sn=47d6d226a3ac6cc08980e7562ae09fce&chksm=80d35789b7a4de9f3ba9a3eeb21c6c812b0f7fe43cee47fc38368ed31a1346114a67daa3cd30&scene=21#wechat_redirect)

-   [解读LoRA](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978719&idx=1&sn=52183b612a2586d407ba9c9006027078&chksm=80d356b9b7a4dfaf127df71ca4834513eb9454988a5aa488f24938e04283353c376660e8516c&scene=21#wechat_redirect)

-   [解读RAG](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978863&idx=1&sn=73746b3a4453e27ed0f2d2ff28840c82&chksm=80d35109b7a4d81fef96f451ae279ec18cb0c12f6f0353e5ca0563929c682719cd00cb5e5dd0&scene=21#wechat_redirect)

-   [大模型应用框架之Semantic Kernel](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978636&idx=1&sn=de8c03071b01ee46e967e32b7ac91cc1&chksm=80d3566ab7a4df7cc6f9384f27afcbeaea1deedbc413f5fd6e940a26962f6647ad060229e288&scene=21#wechat_redirect)

-   [浅析多模态机器学习](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978122&idx=1&sn=baf54b7a1a0758e19bf6a3622a43d8fb&chksm=80d3546cb7a4dd7ab9b857ea75bcc3e361cb68489ff5c43ff4d8ab65b2da838b46621b2936b1&scene=21#wechat_redirect)

-   [大模型应用于数字人](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978589&idx=1&sn=cb8e7a54f5675ec65d07f7555f16b4eb&chksm=80d3563bb7a4df2d9dcb13a4491d27e33117ff90ca25e2416ab2a36fa4757ca9478635dd38f3&scene=21#wechat_redirect)

-   [深度学习架构的对比分析](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658978063&idx=1&sn=f934c531bacfe1bf6c95ccbdababe439&chksm=80d35429b7a4dd3f8df5f8c439bd98420c13d4a115c609a60370a6e09ad7c667c4a8c95418c1&scene=21#wechat_redirect)

-   [老码农眼中的大模型（LLM）](http://mp.weixin.qq.com/s?__biz=MzAwOTcyNzA0OQ==&mid=2658977916&idx=1&sn=d38f03af2b3916251e9a8577d995e065&chksm=80d3555ab7a4dc4c0c919ce0a678adc9f3018d81994dc072e698cfa481665ec8faf788d606be&scene=21#wechat_redirect)