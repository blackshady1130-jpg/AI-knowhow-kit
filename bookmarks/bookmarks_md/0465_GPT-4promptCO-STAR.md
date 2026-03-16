---
url: https://mp.weixin.qq.com/s/GiQ1iIavCfLLTso6jhppvw
title: "GPT-4 提示词冠军如何写 prompt：CO-STAR 框架、文本分段、系统提示"
description: "写一个好的 prompt，能够搞定任何 LLM。"
author: "Sheila Teo"
captured_at: "2026-03-08T11:57:36.888Z"
---

# GPT-4 提示词冠军如何写 prompt：CO-STAR 框架、文本分段、系统提示

![图片](https://mmbiz.qpic.cn/mmbiz_png/qpAK9iaV2O3vL5iaecClyfkwfCBoxqGe5z3FWycfjGBudWRfH7DMfWThic2AVvKmjaSBDibX5oA1af3IaFibAFWky3A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

当下，如果我们希望通过 ChatGPT 得到有用的信息，就必须知道如何向它发出清晰的指令。为了指导用户写一个好的 prompt，[OpenAI 官方曾上线了 Prompt engineering](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247493028&idx=1&sn=f522999795a675d9f44e737b19679beb&chksm=c0090398f77e8a8e218cecacef20865219c9db2d8b48d6501baca0f089e95e94d5421e190172&scene=21#wechat_redirect)，谷歌和微软也有类似的动作。

上个月，新加坡政府科技局（GovTech）组织了首届 GPT-4 提示工程大赛，这场比赛吸引了超过 400 名杰出的参与者，Sheila Teo 从中脱颖而出，拿到大赛冠军。**她是如何高效使用 ChatGPT 的？她的提示工程策略将带给我们怎样的启发？**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qpAK9iaV2O3vWQbHFay8r9zeTdOeCnuuMFyia5H7LnFmicSuh3liavJ49lyxwq11s5KzIhMGVqmichgm55nXEB4RFrQ/640?wx_fmt=webp&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

Sheila Tao 本人发表了一篇文章，详细介绍了她对于 prompt 的理解和应用。

> 作者的话： 在写作本文时，我特意避开了那些已经广泛讨论和记录的常规提示工程技巧。相反，我更希望分享一些我在实验中获得的新洞见，以及我个人在理解和应用这些技巧时的独到见解。

文章转载自博客「宝玉的分享」，Founder Park 略有调整。

原文地址：https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**01**

**CO-STAR 框架：**

**让你的提示更高效？**

在使用大语言模型时，有效的提示构建至关重要。CO-STAR 框架是一个实用的提示构建工具，由新加坡政府科技局数据科学与 AI 团队创立。它考虑了所有影响大语言模型响应效果和相关性的关键因素，帮助使用者获得更优的反馈。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

CO-STAR 框架——作者提供的图像

**如何应用 CO-STAR 框架**

**(C) 上下文：为任务提供背景信息** 通过为大语言模型（LLM）提供详细的背景信息，可以帮助它精确理解讨论的具体场景，确保提供的反馈具有相关性。

**(O) 目标：明确你要求大语言模型完成的任务** 清晰地界定任务目标，可以使大语言模型更专注地调整其回应，以实现这一具体目标。

**(S) 风格：明确你期望的写作风格** 你可以指定一个特定的著名人物或某个行业专家的写作风格，如商业分析师或 CEO。这将指导大语言模型以一种符合你需求的方式和词汇选择进行回应。

**(T) 语气：设置回应的情感调** 设定适当的语气，确保大语言模型的回应能够与预期的情感或情绪背景相协调。可能的语气包括正式、幽默、富有同情心等。

**(A) 受众：识别目标受众** 针对特定受众定制大语言模型的回应，无论是领域内的专家、初学者还是儿童，都能确保内容在特定上下文中适当且容易理解。

**(R) 响应：规定输出的格式** 确定输出格式是为了确保大语言模型按照你的具体需求进行输出，便于执行下游任务。常见的格式包括列表、JSON 格式的数据、专业报告等。对于大部分需要程序化处理大语言模型输出的应用来说，JSON 格式是理想的选择。

**CO-STAR 框架的实用示例**

下面这个现实案例解释了CO-STAR 框架为什么有用。假设你担任社交媒体经理，需要草拟一条 Facebook 帖子来推广公司的新产品。

没有使用 CO-STAR 的快速提示可能是这样的：

> 为我的公司 Alpha 的新产品 Beta——一款新型超快速吹风机，撰写一条 Facebook 帖子。

这是 GPT-4 的回答：

> 介绍 Alpha 公司革命性的 Beta 吹风机！告别长时间、无聊的吹发过程！Alpha 公司自豪地推出 Beta，这是我们在护发技术上的最新创新——超快干燥：Beta 设计旨在让你的吹发时间减半，得益于其先进的强力马达。快速准备，享受更多你所爱的时间！立即购买：\[产品页面链接\]

这一输出虽足够，但显得过于泛化，缺乏必要的细节和针对性吸引力，未能真正触及公司目标受众的心。

下面是一个应用 CO-STAR 模板的示例，它提醒我们在制定提示时，要考虑到任务的其它方面，特别是之前快速提示中缺少的风格、语调和受众：

> # CONTEXT（上下文） # 
>
> 我想推广公司的新产品。我的公司名为 Alpha，新产品名为 Beta，是一款新型超快速吹风机。 
>
> # OBJECTIVE（目标） # 
>
> 帮我创建一条 Facebook 帖子，目的是吸引人们点击产品链接进行购买。 # STYLE（风格） # 
>
> 参照 Dyson 等成功公司的宣传风格，它们在推广类似产品时的文案风格。 # TONE（语调） # 说服性  
>
> # AUDIENCE（受众） # 
>
> 我们公司在 Facebook 上的主要受众是老年人。请针对该群体在选择护发产品时的典型关注点来定制帖子。 
>
> # RESPONSE（响应） # 
>
> 保持 Facebook 帖子简洁而深具影响力。

通过运用 CO-STAR 框架，GPT-4 的响应变得更具针对性和效果：

> 用 Alpha Beta——超快速吹风机，体验轻松的优雅生活，它是为具有洞察力的一代人设计的。 
>
> 与 Alpha Beta 一起，重新找回简单而高效的护发乐趣。
>
> 我们的最新创新不仅是一款吹风机；它还承诺为那些懂得欣赏生活美好事物的人提供快速、柔和且可靠的发型打理。 
>
> \- 易用且直观：向复杂的设备说再见。Alpha Beta 专为舒适和简便而设计，非常适合那些喜欢简洁、无麻烦操作的人。 
>
> \- 节省时间的技术：我们知道您的时间非常宝贵。
>
> 因此，Alpha Beta 显著缩短吹发时间，让您有更多时间享受生活。立即体验优雅与简约的完美结合。 
>
> \[您的产品链接在此\]

CO-STAR 框架指引您以有组织的方式提供所有关键任务信息，确保响应完全针对您的需求并进行优化。

**02**

**分隔符：**

**任务越复杂，影响越明显**

分隔符是特殊的符号，它们帮助大语言模型 (LLM) 辨识提示中哪些部分应当被视为一个完整的意义单元。这非常关键，因为你的提示是作为一个长的 Token 序列一次性传给模型的。通过设置分隔符，可以为这些 Token 序列提供结构，使特定部分得到不同的处理。

需要注意的是，对于简单的任务，分隔符对大语言模型的回应质量可能无显著影响。但是，任务越复杂，合理使用分隔符进行文本分段对模型的反应影响越明显。

**分隔符的作用**

分隔符可以是任何不常见组合的特殊字符序列，如：

> ### 
>
> \=== 
>
> \>>>

选择哪种特殊字符并不重要，关键是这些字符足够独特，使得模型能将其识别为分隔符，而非常规标点符号。

这里是一个分隔符使用的示例：

```
请在 <<<CONVERSATIONS>>> 中对每段对话的情绪进行分类，标为‘正面’或‘负面’。仅提供情绪分类结果，不需任何引言。对话示例：
```

在上述示例中，使用 ### 分隔符来分隔不同的部分，通过大写的章节标题如对话示例和输出示例进行区分。引言部分说明了要对 <<<CONVERSATIONS>>> 中的对话进行情绪分类，而这些对话在提示的底部给出，没有任何解释文本，但分隔符的存在让模型明白这些对话需要被分类。

GPT-4 的输出正如请求的那样，仅给出情绪分类：

> 正面
>
> 负面

**将分隔符用作 XML 标签**

使用 XML 标签作为分隔符是一种方法。XML 标签是被尖括号包围的，包括开启标签和结束标签。例如，<tag>和</tag>。这种方法非常有效，因为大语言模型已经接受了大量包含 XML 格式的网页内容的训练，因此能够理解其结构。

以下是利用 XML 标签作为分隔符对同一提示进行结构化的例子：

```
分类以下对话的情感，分为正面和负面两类，根据给出的例子进行分类。请直接给出情感分类结果，不需要添加任何引导性文本。
```

在指令中使用的名词与 XML 标签的名词一致，如 conversations、classes 和 examples，因此使用的 XML 标签分别是 <conversations>、<classes>、<example-conversations> 和 <example-classes>。这确保了模型能够清晰地理解指令与使用的标签之间的关系。

通过这种结构化的分隔符使用方式，可以确保 GPT-4 精确地按照您的期望响应：

> 正面
>
> 负面

**03**

**系统提示：**

**如何用好这个过滤器？**

> 在开始前，我们需指出，本节内容仅适用于具备系统提示功能的大语言模型 (LLM)，与文章中其他适用于所有大语言模型的部分不同。 
>
> 显然，具有此功能的最知名的大语言模型是 ChatGPT，因此我们将以 ChatGPT 为例进行说明。

**关于系统提示的术语解释**

首先，我们来厘清几个术语：在讨论 ChatGPT 时，“系统提示”、“系统消息”和“自定义指令”三个术语几乎可以互换使用。这种用法让许多人（包括我自己）感到混淆，因此 OpenAI 发表了一篇文章\*，专门解释了这些术语。简要总结如下：

-   “系统提示”和“系统消息”是通过 Chat Completions API 编程方式交互时使用的术语。

-   而“自定义指令”则是在通过 https://chat.openai.com/ 的用户界面与 ChatGPT 交互时使用的术语。

\* https://help.openai.com/en/articles/8234522-chat-completions-api-system-message-vs-custom-instructions-in-ui

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图片来自 Enterprise DNA Blog

尽管这三个术语表达的是相同的概念，但不必因术语的使用而感到困扰。下面我们将统一使用“系统提示”这一术语。

**什么是系统提示？**

> 系统提示是您向大语言模型提供的关于其应如何响应的额外指示。这被视为一种额外的提示，因为它超出了您对大语言模型的常规用户提示。 

在对话中，每当您提出一个新的提示时，系统提示就像是一个过滤器，大语言模型会在回应您的新提示之前自动应用这一过滤器。这意味着在对话中每次大语言模型给出回应时，都会考虑到这些系统提示。

系统提示一般包括以下几个部分：

-   **任务定义：**确保大语言模型（LLM）在整个对话中清楚自己的任务。

-   **输出格式：**指导 LLM 如何格式化其回答。

-   **操作边界：**明确 LLM 不应采取的行为。这些边界是 LLM 治理中新兴的一个方面，旨在界定 LLM 的操作范围。

例如，系统提示可能是这样的：

> 您需要用这段文本来回答问题：\[插入文本\]。请按照 {"问题": "答案"} 的格式来回答。如果文本信息不足以回答问题，请以"NA"作答。您只能解答与 \[指定范围\] 相关的问题。请避免回答任何与年龄、性别及宗教等人口统计信息相关的问题。

每一部分对应的内容如下图所示：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

系统提示解析 - 图片由作者提供

### **那么用户提示中应该包括什么内容？**

系统提示已经概括了任务的总体要求。在上述示例中，任务被定义为仅使用特定文本进行问题解答，同时指导 LLM 按照 {"问题"："答案"} 的格式进行回答。

> 您需要用这段文本来回答问题：\[插入文本\]。请按照 {"问题": "答案"} 的格式来回答。

这种情况下，每个用户提示就是您想用该文本回答的具体问题。例如，用户提示可能是"这篇文本主要讲了什么？"，LLM 的回答将是 {"这篇文本主要讲了什么？":"文本主要讲述了......"}。

但我们可以将这种任务进一步推广。通常，与只询问一个文本相比，你可能会有多个文本需要询问。这时，我们可以将系统提示的首句从

> 您需要用这段文本来回答问题：\[插入文本\]。

改为

> 您需要使用提供的文本来回答问题。

如此，每个用户提示将包括要问答的文本和问题，例如：

> <text> \[插入文本\] </text>
>
> <question> \[插入问题\] </question>

此处，我们使用 XML 标签来分隔信息，以便以结构化方式向 LLM 提供所需的两个信息。XML 标签中的名词，text 和 question，与系统提示中的名词相对应，以便 LLM 理解这些标签是如何与指令相关联的。

总之，系统提示应提供整体任务指令，而每个用户提示则需要提供执行该任务所需的具体细节。在这个例子中，这些细节就是文本和问题。

### **额外内容：为 LLM 设定动态规则**

在之前的讨论中，我们通过系统提示来设定规则，这些规则一经设定，将在整个对话中保持不变。但如果你想在对话的不同阶段实施不同的规则，应该怎么做呢？

对于直接使用 ChatGPT 用户界面的用户来说，目前还没有直接的方法可以实现这一点。然而，如果你通过编程与 ChatGPT 互动，情况就大不相同了。随着对开发有效 LLM 规则的关注不断增加，一些允许你通过编程方式设定更为详细和动态的规则的开源软件包也应运而生。

特别值得推荐的一个是由 NVIDIA 团队开发的 NeMo Guardrails\*。这个工具允许你配置用户与 LLM 的预期对话流程，并在对话的不同环节设定不同的规则，实现规则的动态调整。这无疑是探索对话动态管理的一个很好的资源，值得一试。

## \* https://github.com/NVIDIA/NeMo-Guardrails

**04**

**数据集分析：**

**LLM在识别趋势方面表现出色**

你可能已经听说过 OpenAI 在 ChatGPT 的 GPT-4 中为付费账户提供的高级数据分析插件。它让用户可以上传数据集到 ChatGPT 并直接在数据集上执行编码，实现精准的数据分析。

但是，你知道吗？我们并不总是需要依赖这类插件来有效地使用大语言模型 (LLM) 分析数据集。我们首先来探讨一下只利用 LLM 进行数据分析的优势与限制。

### **LLM 在哪些数据集分析类型上不擅长**

你可能已经知道，LLMs 在执行精确的数学计算方面有所限制，这让它们不适合需要精确量化分析的任务，比如：

-   **描述性统计（Descriptive Statistics）**： 通过如均值或方差等措施定量总结数值列。

-   **相关性分析（Correlation Analysis）**： 获取列间的精确相关系数。

-   **统计分析（Statistical Analysis）**： 例如进行假设检验，判断数据点组间是否存在统计显著的差异。

-   **机器学习（Machine Learning）**： 在数据集上执行预测模型，如使用线性回归、梯度增强树或神经网络。

正是为了执行这些量化任务，OpenAI 推出了高级数据分析插件，以便通过编程语言在数据集上运行代码。

那么，为什么还有人想仅用 LLMs 来分析数据集而不用这些插件呢？

### **LLM 擅长的数据集分析类型**

LLMs 在识别模式和趋势方面表现出色。这得益于它们在庞大且多样化的数据上接受的广泛训练，能够洞察到复杂的模式，这些模式可能不是一眼就能看出来的。

这使它们非常适合执行基于模式查找的任务，例如：

-   **异常检测：** 基于一个或多个列值，识别偏离常态的异常数据点。

-   **聚类：** 将具有相似特征的数据点按列分组。

-   **跨列关系：** 识别各列之间的联合趋势。

-   **文本分析（适用于文本列）：** 根据主题或情感进行分类。

-   **趋势分析（针对有时间维度的数据集）：** 识别列中的模式、季节性变化或趋势。

对于这些基于模式的任务，单独使用 LLMs 可能实际上会在更短的时间内比使用编程代码产生更好的结果。接下来，我们将通过一个例子来详细说明这一点。

### **仅使用 LLM 分析 Kaggle 数据集**

我们将使用一个流行的实际 Kaggle 数据集\*，该数据集专为客户个性分析而设计，帮助公司对客户基础进行细分，从而更好地了解客户。

\* https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis

为了之后验证 LLM 分析的方便，我们将这个数据集缩减至 50 行，并仅保留最相关的几列。缩减后的数据集如下所示，每一行代表一位客户，各列展示了客户的相关信息：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

数据集前三行——图片由作者提供

假设你是公司营销团队的一员，你的任务是利用这份客户信息数据集来指导营销活动。任务分为两步：首先，利用数据集生成有意义的客户细分；其次，针对每个细分提出最佳的市场营销策略。这是一个实际的商业问题，其中第一步的模式识别能力是 LLM 可以大显身手的地方。

我们将按以下方式设计任务提示，采用四种提示工程技术：

1.  将复杂任务分解成简单步骤；

2.  引用每个步骤的中间输出；

3.  格式化 LLM 的回答；

4.  将指令与数据集分离。

```
系统提示：
```

下面是 GPT-4 的回复，我们将继续将数据集以 CSV 字符串的形式传递给它。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

随后，GPT-4 按照我们要求的标记符报告格式回复了分析结果：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### **验证大语言模型的分析能力**

为了简洁，我们选择两个由大语言模型生成的客户群体进行验证——「年轻家庭」和「挑剔的爱好者」。

**年轻家庭** - 大语言模型生成的描述：出生于 1980 年后，已婚或同居，中等偏低的收入，育有孩子，常做小额消费。- 此群体包括的数据行：3、4、7、10、16、20 - 深入查看这些数据行的详细信息，结果显示：

这些数据完美对应大语言模型确定的用户描述。该模型甚至能够识别包含空值的数据行，而无需我们预先处理！

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

年轻家庭的完整数据——作者图片

**挑剔的爱好者** - 大语言模型生成的描述：年龄跨度广泛，不限婚姻状况，高收入，孩子情况不一，高消费水平。- 此群体包括的数据行：2、5、18、29、34、36 - 深入查看这些数据行的详细信息，结果显示：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

挑剔的爱好者的完整数据——作者图片

这些数据再次精准匹配大语言模型确定的用户描述。

本例展示了大语言模型在识别模式、解读及简化多维数据集以提炼出有意义的洞见方面的强大能力，确保其分析结果扎根于数据的真实情况。

### **使用 ChatGPT 的高级数据分析插件会如何？**

为了全面考虑，我使用同一提示尝试了相同的任务，不过这次我让 ChatGPT 通过编程方式进行分析，启用了其高级数据分析插件。插件应用 K-均值等聚类算法直接对数据集进行处理，以便划分不同的客户群体，并据此制定营销策略。

尽管数据集仅含 50 行，多次尝试均显示错误信息且未产生任何结果：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

尝试 1 的错误和无输出——作者图片

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

尝试 2 的错误和无输出——作者图片

当前情况表明，虽然高级数据分析插件能够轻松完成一些简单任务，如统计描述或生成图表，但在执行需要较大计算量的高级任务时，有时可能因为计算限制或其他原因而发生错误，导致无法输出结果。

**05**

**何时应当用**

**大语言模型来分析数据集？**

答案因分析的具体类型而异。

对于需要精确的数学运算或复杂的规则处理的任务，传统的编程方法依然更加适用。

而对于依赖模式识别的任务，传统的编程和算法处理可能更加困难且耗时。大语言模型在这类任务中表现优异，能提供包括分析附件在内的额外输出，并能生成 Markdown 格式的完整分析报告。

> 总的来说，是否采用大语言模型取决于任务本身的性质，需要平衡其在模式识别上的强项与传统编程技术提供的精确度和特定性。

**回到提示工程环节！**

在本节结束前，让我们重新审视用于生成此数据分析的提示，并详细解析关键的提示工程技巧：

```
提示:
```

**技巧 1：将复杂任务简化成步骤**

大语言模型（LLM）擅长处理简单的任务，对于复杂的任务则表现不佳。因此，在面对复杂任务时，把它分解成一步步简单的指令是至关重要的。这种方法的核心思想是，明确告知 LLM 你自己执行该任务时会采取的每一个步骤。

例如，具体步骤如下：

> 请按照这个步骤操作，不要使用编码： 
>
> 1.   数据聚类（CLUSTERS）：利用数据集的各列特征，将数据行进行聚类，确保同一聚类中的客户在这些特征上相似，而不同聚类的客户则明显不同。每条数据只能属于一个聚类。对于每个聚类，
>
> 2.  聚类描述（CLUSTER\_INFORMATION）：描述聚类的特点。
>
> 3.  聚类命名（CLUSTER\_NAME）：根据聚类描述，为这个客户群体起一个简洁的名字。
>
> 4.  营销策略（MARKETING\_IDEAS）：为这个客户群体制定营销策略。
>
> 5.  策略解释（RATIONALE）：说明为什么这些营销策略对这个客户群体有效
>

这样的分步指导，比起直接要求 LLM「对客户进行分组并提出营销策略」的方式，能显著提高其输出的准确性。

#### **技巧 2：标记并引用中间输出**

在提供步骤时，我们会用大写字母标记每个步骤的输出，例如数据聚类（CLUSTERS）、聚类描述（CLUSTER\_INFORMATION）、聚类命名（CLUSTER\_NAME）、营销策略（MARKETING\_IDEAS）和策略解释（RATIONALE）。这样做是为了区分指令中的变量名和其他文本，方便后续引用这些中间输出。

#### **技巧 3：优化响应格式**

此处我们请求一个 Markdown 格式的报告，以增强响应的可读性和结构性。利用中间步骤的变量名，可以明确报告的构架。

> \# 响应：Markdown 报告 #
>
> <对每个数据聚类 \[数据聚类（CLUSTERS）\]>
>
> —客户群体：\[聚类命名（CLUSTER\_NAME）\]
>
> —群体特征：\[聚类描述（CLUSTER\_INFORMATION）\]
>
> —营销策略：\[营销策略（MARKETING\_IDEAS）\]
>
> —策略说明：\[策略解释（RATIONALE）\]
>
> <附录> 
>
> 提供一个表格，记录每个聚类包含的数据行号，以验证分析的准确性。
>
> 表格标题为：\[聚类命名（CLUSTER\_NAME）, 行号列表\]。

此外，你还可以让 ChatGPT 将报告以可下载文件形式提供，便于你在编写最终报告时参考使用。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

保存 GPT-4 的回答为文件

#### **技巧 4：将任务指令与数据集分离**

在我们的首个提示中，你会发现我们并没有直接将数据集交给大语言模型（LLM）。反而，提示只给出了数据集分析的任务指令，并在底部添加了这样的话：

> \# START ANALYSIS # 
>
> 如果你明白了，请向我请求数据集。

随后 ChatGPT 表示它已理解，并在下一个提示中，我们通过 CSV 字符串的形式将数据集传递给它：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

GPT-4 的反馈——作者提供的图像

**但为什么需要将指令与数据集分开处理呢？**

这样做可以帮助大语言模型更清晰地理解各自的内容，降低遗漏信息的风险，尤其是在指令较多且复杂的任务中。你可能遇到过这样的情况：在一个长的提示中提出的某个指令被「偶然遗忘」了——例如，你请求一个 100 字的回答，但大语言模型却给出了更长的段落。通过先接收指令，再处理这些指令所对应的数据集，大语言模型可以更好地消化它应该做的事情，然后再执行相关的数据操作。

值得注意的是，这种指令与数据集的分离只能在可以维护对话记忆的聊天型大语言模型中实现，而非那些没有这种记忆功能的完成型模型。

---

如果你关注大模型领域，欢迎扫码加入我们的大模型交流群，来一起探讨大模型时代的共识和认知，跟上大模型时代的这股浪潮。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**更多阅读**

[AI 应用如何赚钱？全球 AI-Native 公司定价策略解密](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247498264&idx=1&sn=932cc57478ed8d0499dcd1d8dd91da12&chksm=c0091c24f77e953204cf35efd78d5f8e01b47e4200e9938497efecab978541fe68fb5c67ec85&scene=21#wechat_redirect)

[黏土风 App Remini 大火，最挣钱的却是这款产品，它做对了什么？](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247498264&idx=2&sn=43fdf637752a7a0cf0205859e19dd3e8&chksm=c0091c24f77e9532f5c9b4b79b45ad3e755fd85b3a874e5817637aeb78eb8e20fdf20f4453a9&scene=21#wechat_redirect)

[ChatGPT Search 第一时间上手：速度很快、准确性和多语言欠佳](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247498225&idx=1&sn=d50624fb47cf1f2e06d6e05beb7aac75&chksm=c0091fcdf77e96db00442f8c443593435aea1303716c513073c99e8e208b82ebb955168da906&scene=21#wechat_redirect)

[Notion 创始人专访：如何落地 AI、如何融资、小公司如何挑战 Google？](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247497989&idx=1&sn=4be1cafd1ec100cd20fe4f5902ccbbd3&chksm=c0091f39f77e962f7f46f98be74d35d934c7cc20b3c2f4f9b41d0e87a3a32dc17a5ab4d8d446&scene=21#wechat_redirect)

转载原创文章请添加微信：geekparker