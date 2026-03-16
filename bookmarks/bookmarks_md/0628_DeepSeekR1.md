---
url: https://mp.weixin.qq.com/s/Xq0FrodMrSkGMm3eUIxq1Q
title: "从DeepSeek R1看推理模型的四种进化路线"
description: "四大进化路线揭秘"
author: "J0hn"
captured_at: "2026-03-08T12:40:42.506Z"
---

# 从DeepSeek R1看推理模型的四种进化路线

DeepSeek R1 的推理型大模型不仅强在技术，更让人震惊的是，它们竟然自己学会了「**一步步思考**」！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/M3PrhSUICnEaSic6yyiaRDfoOgYH0Y4U85xkrPasrQicm0DQxlBoalQBkIEr4eJdZ2icXfuLMHd549SIXFILicdu5kg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

Sebastian Raschka 最近深入解析了推理型大模型的内部机制，揭示了**四种关键进化路线**。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/M3PrhSUICnEaSic6yyiaRDfoOgYH0Y4U85jJmiayOD87aiaYSAcKDX0T9cmsEpXcLPN9XgnSSkmKfHibGO2yM6aGIibw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "![")

这篇文章不仅会为大家介绍「什么是推理型大模型」，更会详细剖析这些模型是如何一步步获得推理能力的。

## 为什么要关注推理型模型？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "![左：普通大模型的回答，右：推理型大模型的回答")

左：普通大模型的回答，右：推理型大模型的回答

如上图，左边是普通大模型的回答，右边是推理型大模型的回答。

**普通模型只会直接给出答案，而推理型模型会像人类一样展示思考过程**。

这种差异并非表面文章。

推理型大模型在**解决复杂问题、数学证明和编程任务**时表现出色，因为它们能够**分步骤思考问题**。

## 四大进化路线大揭秘

让AI具备推理能力可不是件容易的事。Sebastian Raschka 指出了四种进化路线，每种都有其独特优势：

**「推理时缩放」**：这种方法就像给AI更多的「思考时间」。虽然会增加计算成本，但能显著提升推理质量。

**「纯强化学习」**：这是DeepSeek团队最惊人的发现！**仅仅通过强化学习，模型就自发展现出了推理能力**。

**「监督微调+强化学习」**：这是目前最强大的方法，DeepSeek R1就是用这种方法训练出来的。通过结合两种训练方式，让模型既能准确理解任务，又能不断改进。

**「知识蒸馏」**：这种方法让小模型也能获得推理能力。虽然性能不如大模型，但更加经济实用。

## 下为译文

### 理解推理大模型（LLMs）

**原文链接**：Understanding Reasoning LLMs\[1\]
**发布时间**：2025 年 2 月 5 日

---

## 构建推理模型的四种主要方法：增强大语言模型（LLM）推理能力的路径

本文旨在探讨构建推理模型的四种主要方法，或如何通过不同技术手段增强大语言模型（LLM）的推理能力。希望这些内容能为您在快速演化的文献和热潮中提供有价值的见解，帮助您更好地理解这一领域。

## 2024 年 LLM 领域的趋势与展望

2024 年，大语言模型领域呈现出日益明显的专业化趋势。除了基础的预训练和微调外，我们还见证了许多专用应用的崛起，如基于检索增强生成（RAG）的模型和代码助手工具等。预计到 2025 年，这一趋势将进一步加速，行业将更加关注领域和应用场景的特定优化（即“专业化”）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.

*开发 LLM 的常规步骤包括阶段 1-3，而第 4 阶段则是针对特定场景的专业化调整。*

推理模型的发展正是这种专业化的一部分。所谓推理模型，旨在优化 LLM 以在需要中间推理步骤的复杂任务中表现卓越，例如解谜题、高阶数学计算以及代码挑战等。然而，这种专业化并不意味着取代其他 LLM 应用，因为将 LLM 转化为推理模型的过程中也会带来一些不可避免的权衡，本文稍后将详细讨论。

**本文将涵盖以下内容：**

1.  **解释“推理模型”的含义**

2.  **探讨推理模型的优势与局限性**

3.  **概述 DeepSeek R1 的开发方法论**

4.  **介绍构建和改进推理模型的四种主要方法**

5.  **分享 DeepSeek V3 和 R1 发布后的 LLM 发展趋势思考**

6.  **提供有限预算下开发推理模型的建议**

希望本文能为您在 AI 领域的快速发展中提供有益的参考！

---

## 我们如何定义“推理模型”？

如果您从事 AI 或机器学习相关工作，应该对许多模糊且充满争议的术语定义并不陌生，而“推理模型”正是其中之一。某个学术论文中对其进行了正式定义，但很快就会在下一篇论文中被重新定义，如此循环往复。

在本文中，我们将“推理”定义为：**回答需要复杂、多步生成过程并涉及中间推理步骤的问题的能力**。例如，问答类问题“法国的首都是哪里？”并不需要推理；而像“如果一列火车以 60 英里每小时的速度行驶 3 小时，它行驶了多远？”则涉及简单的推理，模型需要识别出距离、速度和时间之间的关系，才能得出正确答案。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

普通 LLM 与推理模型的回答差异

*普通的 LLM 可能只会给出简短的答案（如左图所示），而推理模型通常会包含中间推理步骤，展示部分思考过程。*

**现代 LLM 大多具备基本的推理能力，能够解决如火车行驶距离这种简单问题。然而，当前所称的推理模型，通常指的是能够在更复杂推理任务（如解谜题、逻辑推理和数学证明等）中表现优异的模型。**

此外，很多被称为推理模型的 LLM 在回答中会显式展示“思考过程”。至于 LLM 是否真正具有“思考”能力，这是另一个值得深入探讨的话题。

推理模型中的中间推理步骤可以以两种方式呈现：

1.  **显式展示：** 模型直接在输出中包含推理步骤。

2.  **隐式处理：** 某些推理模型（如 OpenAI 的 o1）在生成答案时会进行多轮内部推理，但这些中间步骤不会展示给用户。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

推理模型的双层次应用

*“推理”可分为两个层次：1）处理输入并通过多步推理生成输出，2）在对用户的回答中展示推理步骤。*

---

## 推理模型适用于哪些场景？

在了解了推理模型的定义后，我们接下来探讨一个更为实际的问题：**什么时候需要使用推理模型？**

### 何时需要推理模型？

推理模型专为解决复杂任务而设计，例如解谜题、高阶数学问题以及挑战性的编程任务。然而，对于诸如摘要生成、翻译或基于知识的简单问答等任务，使用推理模型并非必要。事实上，滥用推理模型可能会导致效率低下和成本增加。

**推理模型的局限性：**

-   **成本更高：** 推理模型在推理过程中通常会生成更多的中间步骤，导致计算资源消耗增加。

-   **回答冗长：** 由于需要展示推理过程，回答往往比普通模型更啰嗦。

-   **易陷入“过度思考”：** 在简单任务上可能出现不必要的复杂化，甚至降低准确率。

**简单法则：** 为不同任务选择合适的工具（或 LLM 类型）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

推理模型的优势与局限

---

## DeepSeek 训练流程简述

在接下来的部分讨论构建和改进推理模型的四种主要方法之前，我想简要概述一下 **DeepSeek R1 的训练流程**，这一流程在 DeepSeek R1 技术报告\[2\] 中有详细描述。该报告既是一个有趣的案例研究，也可作为开发推理型大语言模型（LLM）的蓝图。

需要注意的是，DeepSeek 并未发布单一的 R1 推理模型，而是推出了三个不同的版本：**DeepSeek-R1-Zero**、**DeepSeek-R1** 和 **DeepSeek-R1-Distill**。

基于技术报告中的描述，我总结了这些模型的开发流程，如下图所示。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**DeepSeek R1 技术报告中讨论的三种不同推理模型的开发流程**

接下来，让我们简要回顾一下上图所展示的流程。更多细节将在下一部分中介绍，届时我们将讨论构建和改进推理模型的四种主要方法。

---

### (1) DeepSeek-R1-Zero

该模型基于 **6710 亿参数的 DeepSeek-V3 基础模型**（于 2024 年 12 月发布）。研究团队使用 **强化学习（RL）** 进行了训练，采用了两种奖励机制。
这种方法被称为 **“冷启动”训练**，因为它没有包含通常在基于人类反馈的强化学习（RLHF）中常见的 **监督微调（SFT）** 阶段。

---

### (2) DeepSeek-R1

这是 **DeepSeek 的旗舰推理模型**，基于 DeepSeek-R1-Zero 进一步开发而成。
团队通过额外的 SFT 阶段以及进一步的 RL 训练对其进行了优化，旨在改进“冷启动”的 R1-Zero 模型，提升推理能力。

---

### (3) DeepSeek-R1-Distill\*

在前述步骤中生成的 SFT 数据基础上，DeepSeek 团队对 **Qwen 和 Llama 模型** 进行了微调，以增强其推理能力。
尽管这种方法并非传统意义上的知识蒸馏，但其过程包括使用 **DeepSeek-R1（6710 亿参数）** 模型的输出数据训练更小规模的模型（如 **Llama 8B 和 70B** 以及 **Qwen 1.5B–30B**）。

## 构建和提升推理模型的四种主要方法

在本节中，我将概述当前用于增强大语言模型（LLM）推理能力以及构建专门推理模型（如 DeepSeek-R1、OpenAI 的 o1 和 o3 等）的关键技术。

**注意：** o1 和 o3 的具体工作机制在 OpenAI 之外尚不为人所知。然而，有传言称它们结合了推理和训练技术来实现其性能。

---

## 1）推理阶段的扩展（Inference-time Scaling）

提升 LLM 推理能力（或任何其他能力）的一种方法是 **推理阶段的扩展**。这个术语可能有多种含义，但在本文中，它指的是在模型推理阶段增加计算资源，以提高输出质量。

一个粗略的类比是：人类在面对复杂问题时，如果有更多的思考时间，通常会给出更好的答案。同样地，我们可以应用一些技术，让 LLM 在生成答案时“思考”得更多一些。（当然，LLM 是否真正具有“思考”能力是另一个值得讨论的话题。）

一种简单的推理阶段扩展方法是 **巧妙的提示工程（Prompt Engineering）**。一个经典示例是 **思维链提示（Chain-of-Thought，CoT）**，即在输入提示中加入类似 “逐步思考（think step by step）” 的短语。这鼓励模型生成中间推理步骤，而不是直接跳到最终答案。这种方法在处理复杂问题时通常（但并非总是）能提高答案的准确性。（需要注意的是，对于诸如 “法国的首都是哪里？” 这类简单的知识性问题，使用这种策略并不合理。这也是判断某个推理模型是否适合特定问题的良好经验法则。）

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)
*来自 2022 年论文《大型语言模型是零样本推理者（Large Language Models are Zero-Shot Reasoners）》的经典 CoT 提示示例。(论文链接\[3\])*

上述的 CoT 方法可以被视为一种推理阶段扩展技术，因为它通过生成更多的输出令牌（tokens）来增加推理成本。

**另一种推理阶段扩展方法** 是使用 **投票和搜索策略**。一个简单的例子是 **多数投票法（Majority Voting）**，即让 LLM 生成多个答案，然后通过多数投票选择最可能正确的答案。同样，我们还可以使用 **束搜索（Beam Search）** 以及其他搜索算法，以生成更优质的回答。

我强烈推荐阅读论文 **《在测试阶段扩展 LLM 计算资源比扩展模型参数更有效（Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters）》**，我在之前的文章《2024 年值得关注的 AI 研究论文（第二部分）》中对其进行了详细介绍。(论文链接\[4\])

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)
*不同的基于搜索的方法依赖于“过程-奖励模型（process-reward-based model）”来选择最佳答案。此图出自论文《LLM 测试阶段计算资源优化》(论文链接\[5\])*

**DeepSeek R1 的技术报告** 表示其模型未使用推理阶段扩展技术。然而，这种技术通常是在 LLM 之上的应用层实现的，因此 DeepSeek 可能在其应用程序中使用了此类方法。

我推测 OpenAI 的 o1 和 o3 模型使用了推理阶段扩展技术，这也可能解释了它们相较于 GPT-4o 更昂贵的原因。除了推理阶段扩展外，o1 和 o3 很可能还采用了与 DeepSeek R1 相似的 **强化学习（Reinforcement Learning）** 训练流程，关于强化学习的更多内容将在接下来的两节中介绍。

## 2) 纯强化学习（RL）

我个人认为 DeepSeek R1 论文\[6\] 中最精彩的发现之一，是他们证实了推理能力可以作为一种行为，在\*\*纯强化学习（RL）\*\*的训练过程中自然涌现。接下来，我们将更详细地探讨这一现象的含义。

正如前文所述，DeepSeek 开发了三种类型的 R1 模型。其中第一个模型，**DeepSeek-R1-Zero**，基于 DeepSeek-V3 基础模型构建，后者是他们于 2024 年 12 月发布的标准预训练大语言模型（LLM）。与典型的强化学习流程不同，通常在应用强化学习之前会进行监督微调（SFT），而 **DeepSeek-R1-Zero** 则**完全**依靠强化学习进行训练，未经过任何初始的 SFT 阶段，正如下方图示所展示的那样。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

DeepSeek-R1-Zero 模型的开发流程

尽管如此，这一强化学习过程在方法上仍类似于常用的 RLHF（基于人类反馈的强化学习）方法，后者通常用于偏好调优大语言模型。（我在另一篇文章中更详细地介绍了 RLHF：\*\*LLM Training: RLHF and Its Alternatives\*\*\[7\]）。然而，正如前文所提，**DeepSeek-R1-Zero** 的关键区别在于跳过了用于指令调优的监督微调（SFT）阶段。这也是他们将其称为“纯强化学习”的原因。（不过，值得注意的是，大语言模型中的强化学习与传统强化学习在许多方面存在显著差异，这个话题我们可以在未来深入讨论。）

在奖励机制方面，DeepSeek 团队没有使用基于人类偏好训练的奖励模型，而是采用了两种奖励形式：**准确性奖励** 和 **格式奖励**。

-   **准确性奖励**：利用 LeetCode 编译器来验证代码答案的正确性，并通过确定性系统评估数学回答的准确性。

-   **格式奖励**：依靠大语言模型裁判来确保回答符合预期格式，例如将推理步骤放在 `<think>` 标签内。

令人惊讶的是，**这种方法足以使模型发展出基本的推理能力**。研究人员观察到模型出现了所谓的“**顿悟（Aha）时刻**”，即模型开始在回答中生成推理链条，尽管训练过程中并没有明确要求它这么做。下图展示了这一现象。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**来自 DeepSeek R1 技术报告 的图表，展示了模型推理能力涌现的“顿悟时刻”**

尽管 **R1-Zero** 并不是当前推理性能最强的模型，但它确实展示了推理能力，能够生成中间的“思考”步骤，正如上图所示。这一发现证明了：**完全依靠强化学习也可以训练出具备推理能力的模型**，而 DeepSeek 团队是首个展示（或至少是公开发表）这一方法的团队。

## 3) 监督微调与强化学习（SFT + RL）

接下来，让我们看看 **DeepSeek-R1** 的开发过程。DeepSeek-R1 是 DeepSeek 的旗舰推理模型，也是构建推理模型的蓝图。该模型在 **DeepSeek-R1-Zero** 的基础上进行了改进，融合了额外的 **监督微调（SFT）** 和 **强化学习（RL）**，以提升其推理能力。

需要注意的是，在强化学习之前加入 SFT 阶段其实很常见，这一点可以从标准的 **RLHF（基于人类反馈的强化学习）** 流程中看出。OpenAI 的 **o1** 模型很可能也是采用了类似的方法开发的。

---

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

DeepSeek-R1 开发流程图

**DeepSeek-R1 模型的开发流程**

如上图所示，DeepSeek 团队使用 **DeepSeek-R1-Zero** 生成了他们称之为 **“冷启动”** 的 SFT 数据。这里的“冷启动”指的是这些数据由 DeepSeek-R1-Zero 生成，而 **DeepSeek-R1-Zero 本身并未接受过任何监督微调（SFT）数据的训练**。

在获得这些冷启动 SFT 数据后，DeepSeek 团队首先通过 **指令微调（Instruction Fine-tuning）** 对模型进行训练，随后进入了新的 **强化学习（RL）阶段**。这个 RL 阶段保留了 DeepSeek-R1-Zero 强化学习过程中使用的 **准确性奖励（Accuracy Reward）** 和 **格式奖励（Format Reward）**，但新增了一个 **一致性奖励（Consistency Reward）**，用于防止模型在生成回答时出现 **语言混用** 的情况（即在同一回答中切换多种语言）。

在 RL 阶段结束后，团队又进行了一轮新的 SFT 数据收集。在此阶段，他们使用最新的模型检查点生成了 **60 万条链式推理（Chain-of-Thought, CoT）SFT 示例**，并基于 **DeepSeek-V3 基础模型** 额外创建了 **20 万条基于知识的 SFT 示例**。

这 **60 万 + 20 万** 条 SFT 样本随后被用于新一轮的强化学习。在这一阶段，团队继续采用基于规则的方法来评估 **数学与编程题的准确性奖励**，而对于其他类型的问题，则使用 **人工偏好标签（Human Preference Labels）** 进行评估。

最终版本的模型 **DeepSeek-R1** 在性能上相较于 **DeepSeek-R1-Zero** 有了显著提升，这得益于额外的 SFT 和 RL 阶段。如下表所示：

---

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

模型基准对比

**OpenAI A1 与 DeepSeek-R1 模型的基准性能对比**
*图表来源：DeepSeek-R1 技术报告（arXiv:2501.12948\[8\]）*

## 4) 纯监督微调（SFT）与蒸馏

到目前为止，我们已经介绍了构建和改进推理模型的三种关键方法：

1.  **推理时扩展（Inference-time scaling）**：这是一种无需训练或修改底层模型即可提升推理能力的技术。

2.  **纯强化学习（Pure reinforcement learning，RL）**：如 DeepSeek-R1-Zero 所展示的那样，推理能力可以作为一种学习行为自然涌现，而无需监督微调。

3.  **监督微调（SFT）结合强化学习（RL）**：这种方法诞生了 DeepSeek-R1，即 DeepSeek 的旗舰推理模型。

**那么，还剩下什么？模型“蒸馏”。**

令人惊讶的是，DeepSeek 还发布了一些通过所谓的蒸馏（distillation）训练出来的小型模型。然而，在大语言模型（LLM）的语境下，蒸馏不一定遵循传统深度学习中的知识蒸馏（knowledge distillation）方法。传统的知识蒸馏（在我的《Machine Learning Q and AI》一书第6章中简要介绍过）是指将一个小型学生模型在大型教师模型的输出（logits）和目标数据集上进行训练。

但在这里，蒸馏指的是对较小的 LLM（如 Llama 8B 和 70B 以及 Qwen 2.5 模型，范围从 0.5B 到 32B）进行指令微调（instruction fine-tuning）。所使用的 SFT 数据集由更大的 LLM 生成，具体来说，这些模型是 DeepSeek-V3 和 DeepSeek-R1 的中间检查点。实际上，用于蒸馏过程的 SFT 数据集与上一节中描述的 DeepSeek-R1 训练所使用的数据集相同。

为了更清晰地展示这个过程，我在下方的图示中突出显示了蒸馏部分。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

DeepSeek-R1-Distill 模型的开发流程

### 为什么要开发这些蒸馏模型？

在我看来，有两个关键原因：

1.  **小模型更高效。** 这意味着它们的运行成本更低，而且可以在低端硬件上运行，这对于像我这样的研究人员和技术爱好者尤其有吸引力。

2.  **纯 SFT 的案例研究。** 这些蒸馏模型作为有趣的基准，展示了纯监督微调（SFT）在不依赖强化学习的情况下，能够将模型推向何种水平。

下表对比了这些蒸馏模型与其他流行模型以及 DeepSeek-R1-Zero 和 DeepSeek-R1 的性能差异。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**蒸馏模型与非蒸馏模型的基准对比。摘自 DeepSeek-R1 技术报告（arxiv 链接）**

如图所示，蒸馏模型的性能明显弱于 DeepSeek-R1，但相较于 DeepSeek-R1-Zero，其表现却出奇地强劲，尽管模型规模小了好几个数量级。值得注意的是，这些模型与 o1 mini 的表现相当（我猜测 o1 mini 本身可能也是 o1 的蒸馏版本）。

### 推理能力的进一步探索

在总结本节内容之前，还有一个有趣的对比值得提及。DeepSeek 团队测试了在更小模型上，是否也会出现 DeepSeek-R1-Zero 所展示的推理能力涌现现象。为此，他们将 DeepSeek-R1-Zero 中使用的纯 RL 方法直接应用于 Qwen-32B 模型。

下表总结了这一实验的结果，其中 QwQ-32B-Preview 作为基准推理模型，基于 Qwen 2.5 32B 版本开发（我猜测其训练细节未被公开）。这一对比为我们提供了更多见解，帮助判断纯 RL 是否足以在比 DeepSeek-R1-Zero 更小的模型中诱导出推理能力。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**蒸馏与强化学习在 32B 小模型上的基准对比。摘自 DeepSeek-R1 技术报告（arxiv 链接）**

有趣的是，实验结果表明，对于小型模型而言，蒸馏的效果远胜于纯 RL。这与一种观点相符：仅依靠 RL 可能不足以在这一规模的模型中催生出强大的推理能力，而在高质量推理数据上进行的 SFT 则是一种更有效的策略。

### 更全面的对比建议

为了更完整地评估不同方法的效果，表格中如果能增加以下对比将更具参考价值：

1.  **Qwen-32B 结合 SFT + RL 训练**：类似于 DeepSeek-R1 的开发方式。这样可以帮助确定，当 RL 与 SFT 结合时，相较于纯 RL 和纯 SFT 能带来多少性能提升。

2.  **DeepSeek-V3 进行纯 SFT 训练**：类似于蒸馏模型的创建方式。这样可以直接对比 RL + SFT 相对于纯 SFT 的有效性。

## 结论

在本节中，我们探讨了构建和改进推理模型的四种不同策略：

1.  **推理时扩展（Inference-time scaling）**
    这种方法无需额外训练，但会增加推理成本，随着用户数量或查询量的增长，大规模部署的费用也会随之上升。尽管如此，它仍然是不费脑筋的性能提升手段，尤其适用于已经很强大的模型。我强烈怀疑 **o1** 利用了推理时扩展，这也部分解释了它在每个 token 上的成本高于 **DeepSeek-R1** 的原因。

2.  **纯强化学习（Pure RL）**
    对于研究而言，纯 RL 很有趣，因为它可以帮助我们理解推理作为一种涌现行为的机制。然而，在实际的模型开发中，**强化学习 + 监督微调（RL + SFT）** 是更优的选择，因为它能构建出更强大的推理模型。我也强烈怀疑 **o1** 是通过 RL + SFT 训练的。更具体地说，我认为 **o1** 可能起步于比 **DeepSeek-R1** 更弱小的基础模型，但通过 RL + SFT 以及推理时扩展来弥补差距。

3.  **RL + SFT（强化学习 + 监督微调）**
    如上所述，RL + SFT 是构建高性能推理模型的核心方法。**DeepSeek-R1** 是一个很好的蓝图，展示了这一方法的实际效果。

4.  **知识蒸馏（Distillation）**
    知识蒸馏是一种很有吸引力的方法，尤其适用于打造更小、更高效的模型。然而，其局限性在于蒸馏本身无法推动创新，也无法催生新一代推理模型。举例来说，蒸馏始终依赖于现有的、更强大的模型来生成监督微调（SFT）所需的数据。

**未来值得关注的一点** 是将 **RL + SFT（方法 3）** 与 **推理时扩展（方法 1）** 相结合。我预计 **OpenAI 的 o1** 很可能就是采用了这种组合，只不过它基于的基础模型可能比 **DeepSeek-R1** 更弱。这也解释了为什么 **DeepSeek-R1** 在推理效率和性能上表现出色，同时推理成本相对较低。

---

## 关于 DeepSeek-R1 的一些思考

最近几周，很多人问我对 **DeepSeek-R1** 模型的看法。简而言之，我认为这是一项了不起的成就。作为一名研究工程师，我尤其欣赏其详尽的技术报告，这让我能够深入了解其方法论，获得有价值的学习经验。

其中一个最吸引人的发现是，推理能力作为一种行为，竟然可以通过纯强化学习自发涌现。此外，令人印象深刻的是 **DeepSeek** 选择在宽松的 MIT 开源许可证下开放其模型，这比 **Meta 的 LLaMA 模型** 限制更少。

---

## 与 o1 的对比

**DeepSeek-R1** 比 **o1** 更好吗？
我认为它们大致处于同一水平。不过，**DeepSeek-R1** 在推理效率方面更为突出。这表明 **DeepSeek** 可能在训练阶段投入了更多资源，而 **OpenAI** 则可能更多依赖于 **o1** 的推理时扩展来提升性能。

话虽如此，直接对比 **o1** 和 **DeepSeek-R1** 是困难的，因为 **OpenAI** 并未公开太多关于 **o1** 的细节。例如，我们并不知道：

-   **o1** 是否也是一种 **专家混合模型（Mixture of Experts, MoE）？**

-   **o1** 的规模有多大？

-   **o1** 是否只是 **GPT-4o** 的轻微改进版，仅进行了少量的 RL + SFT 训练，但依赖大量推理时扩展？

在缺乏这些关键信息的情况下，直接对比两者无异于 **“苹果和橙子”** 的比较。

---

## DeepSeek-R1 的训练成本

另一个备受讨论的话题是 **DeepSeek-R1** 的开发成本。有人提到其训练成本约为 **600 万美元**，但他们很可能混淆了 **DeepSeek-V3（去年 12 月发布的基础模型）** 和 **DeepSeek-R1**。

**600 万美元的估算** 是基于每 GPU 小时 **2 美元** 的假设以及 **DeepSeek-V3** 最终训练阶段所需的 GPU 小时数得出的，这一讨论最早可以追溯到 **2024 年 12 月**。

然而，**DeepSeek 团队从未披露过 R1 的具体 GPU 使用时长或开发成本**，因此任何关于成本的估算都纯属推测。

无论如何，**DeepSeek-R1** 无疑是开放权重推理模型领域的一个重要里程碑，其卓越的推理效率使其成为 **OpenAI 的 o1** 之外的一个有趣替代方案。

## 在有限预算下开发推理模型

开发一个与 DeepSeek-R1 同等级别的推理模型，可能需要数十万到数百万美元的资金，即使是基于像 DeepSeek-V3 这样的开源权重模型进行开发。这对于那些预算有限的研究人员或工程师来说，可能会感到有些沮丧。

### 好消息：知识蒸馏可以大幅降低成本

幸运的是，模型蒸馏提供了一种更具成本效益的替代方案。DeepSeek 团队通过其 R1 蒸馏模型展示了这一点，尽管这些模型的规模远小于 DeepSeek-R1，但它们在推理性能方面却出人意料地强大。不过，即便是这种方法也并非完全廉价。他们的蒸馏过程使用了 80 万条 SFT（监督微调）样本，仍然需要大量的计算资源。

有趣的是，就在 DeepSeek-R1 发布前几天，我偶然看到了一篇关于 Sky-T1 的文章\[9\]。这是一个引人注目的项目，一个小团队仅使用 1.7 万条 SFT 样本，就训练出了一个开源权重的 32B 模型。总成本是多少？仅 450 美元，甚至低于大多数 AI 会议的注册费。

这个例子表明，尽管大规模训练依然昂贵，但小规模、针对性的微调仍然可以在成本极低的情况下取得令人印象深刻的成果。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "![Sky-T1")

Sky-T1

*图示来自《Sky-T1: 以 450 美元训练属于你的 O1 预览模型》一文，链接：https://novasky-ai.github.io/posts/sky-t1/\[10\]*

根据基准测试，Sky-T1 的性能大致与 O1 相当，考虑到其极低的训练成本，这一结果令人印象深刻。

---

### 低成本纯强化学习：TinyZero

虽然 Sky-T1 专注于模型蒸馏，但我也关注到了一些“纯强化学习（RL）”领域的有趣工作。其中一个值得注意的例子是 TinyZero\[11\]，这是一个具有 30 亿参数的模型，旨在复现 DeepSeek-R1-Zero 的方法（顺便提一句，训练成本不到 30 美元）。

令人惊讶的是，尽管参数量仅为 30 亿，TinyZero 却展现出了一些自我验证能力的萌芽现象，这支持了这样一个观点：推理能力可以通过纯 RL 方法在小型模型中自然涌现。

TinyZero 仓库\[12\] 提到，相关研究报告仍在撰写中，我会持续关注后续的详细信息。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "![TinyZero")

TinyZero

*图示来自 TinyZero 仓库\[13\]，展示了模型具备自我验证能力。（如果能与基础模型的表现作对比，可能会更有趣。）*

这两个项目表明，即使预算有限，推理模型领域仍然可以取得有趣的成果。尽管这两种方法都复现了 DeepSeek-R1 的技术路线，但一个专注于纯 RL（TinyZero），另一个专注于纯 SFT（Sky-T1），探索如何进一步扩展这些思路无疑是非常值得的。

---

### 超越传统 SFT：旅程学习

去年我还遇到了一种特别有趣的方法，描述于论文 《O1 复现之旅：战略进展报告 – 第 1 部分》\[14\] 中。尽管标题提到了“复现 O1”，但该论文实际上并没有真正复现 O1，而是提出了一种改进蒸馏（纯 SFT）流程的新方法。

论文的核心思想是“旅程学习（Journey Learning）”，作为“捷径学习（Shortcut Learning）”的替代方案。

-   **捷径学习**：指传统的指令微调方法，模型只接受正确解题路径的训练。

-   **旅程学习**：则同时包括错误的解题路径，让模型也能从错误中学习。

这种方法在某种程度上与 TinyZero 纯 RL 训练中观察到的自我验证能力相关联，但它完全依赖 SFT 来改进模型。通过让模型接触到错误的推理路径及其纠正过程，旅程学习可能同样强化模型的自我纠错能力，从而提高推理模型的可靠性。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "![Journey Learning")

Journey Learning

*图示来自《O1 复现之旅：战略进展报告 – 第 1 部分》，展示了旅程学习如何在 SFT 数据中纳入错误的解题路径。链接：https://arxiv.org/abs/2410.18982\[15\]*

这可能为未来的研究工作指明了一条令人兴奋的方向，尤其适合预算有限的推理模型开发场景，因为 RL 方法在这种情况下可能计算成本过高。

---

总的来说，推理模型领域目前正涌现出大量有趣的研究成果，相信在接下来的几个月里，我们还会看到更多令人激动的进展！

## 相关资料

\[1\]

Understanding Reasoning LLMs: *https://magazine.sebastianraschka.com/p/understanding-reasoning-llms*

\[2\]

DeepSeek R1 技术报告: *https://arxiv.org/abs/2501.12948*

\[3\]

论文链接: *https://arxiv.org/abs/2205.11916*

\[4\]

论文链接: *https://arxiv.org/abs/2408.03314*

\[5\]

论文链接: *https://arxiv.org/abs/2408.03314*

\[6\]

DeepSeek R1 论文: *https://arxiv.org/abs/2501.12948*

\[7\]

**LLM Training: RLHF and Its Alternatives**: *https://magazine.sebastianraschka.com/p/llm-training-rlhf-and-its-alternatives*

\[8\]

arXiv:2501.12948: *https://arxiv.org/abs/2501.12948*

\[9\]

Sky-T1 的文章: *https://novasky-ai.github.io/posts/sky-t1/*

\[10\]

https://novasky-ai.github.io/posts/sky-t1/: *https://novasky-ai.github.io/posts/sky-t1/*

\[11\]

TinyZero: *https://github.com/Jiayi-Pan/TinyZero/*

\[12\]

TinyZero 仓库: *https://github.com/Jiayi-Pan/TinyZero/*

\[13\]

TinyZero 仓库: *https://github.com/Jiayi-Pan/TinyZero/*

\[14\]

《O1 复现之旅：战略进展报告 – 第 1 部分》: *https://arxiv.org/abs/2410.18982*

\[15\]

https://arxiv.org/abs/2410.18982: *https://arxiv.org/abs/2410.18982*

👇

👇

👇

👇

### 本文同步自知识星球《AGI Hunt》

星球实时采集和监控推特、油管、discord、电报等平台的热点AI 内容，并基于数个资讯处理的 AI agent 挑选、审核、翻译、总结到星球中。

-   每天约监控6000 条消息，可节省约800+ 小时的阅读成本；

-   每天挖掘出10+ 热门的/新的 github 开源 AI 项目；

-   每天转译、点评 10+ 热门 arxiv AI 前沿论文。

**星球非免费。**定价99元/年，0.27元/天。(每+100人，+20元。元老福利~）

-   一是运行有成本，我希望它能自我闭环，这样才能长期稳定运转；

-   二是对人的挑选，鱼龙混杂不是我想要的，希望找到关注和热爱 AI 的人。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/M3PrhSUICnFodAwOfXgopjGaobw6WQKnK5fd2lD4ibprGu610dP0jYicZ7ibW5fEYUzicNpGpIAjnYbEEeMu2kMoqA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20)

**欢迎你的加入！**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/M3PrhSUICnGDDH1opicrUUYdGPXDPVA4lrK81D9licI7HWLdDOTlxOrjF9EMOibsoUBj6EaXlpE9ltvUvHxCp1QZg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21)