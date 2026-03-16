---
url: https://mp.weixin.qq.com/s/DAGz5okbk1RQskHtCpTfnA
title: "估值超5亿美元，体验碾压Bard、Bing，AI搜索引擎Perplexity的想象力在哪里？"
description: "如果能探索出 LLM native 的商业模式，Perplexity 有望取代Google。"
author: "拾象"
captured_at: "2026-03-08T11:17:05.799Z"
---

# 估值超5亿美元，体验碾压Bard、Bing，AI搜索引擎Perplexity的想象力在哪里？

![图片](https://mmbiz.qpic.cn/mmbiz_png/qpAK9iaV2O3vL5iaecClyfkwfCBoxqGe5z3FWycfjGBudWRfH7DMfWThic2AVvKmjaSBDibX5oA1af3IaFibAFWky3A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

主打 AI 内容搜索和问答的产品 Perplexity AI 近日宣布他们的 iOS App 用户量突破 100 万，而 12 月 8 日也是 Perplexity AI 成立一周年。

在 AIGC 领域，Perplexity AI 被 a16z 列入 Top10 的玩家之列，在 AI 应用程序的月访问量排名中，Perplexity 排名第十。今年 10 月份，Perplexity AI 的 ARR 年度收入达到 300 万美元，10 月底在完成由 IVP 领投的新一轮融资后，Perplexity AI 的最新估值达到了 5 亿美元。

作为由前 OpenAI 员工创建，旨在取代传统搜索引擎的 AI 产品，**Perplexity AI 是目前产品体验最好、知识获取最准确的问答引擎，在用户中口碑显著优于 Google Bard 和 Bing Chat**。目前的 Perplexity AI 提供 GPT、Claude2、Llama 2 以及自研大模型的技术服务。

不管是从 AI Native 产品范式，还是分析未来搜索引擎的边界、谷歌的新挑战者，Perplexity AI 都是值得仔细分析的产品。

本文转自「深思 SenseAI」、「海外独角兽」，Founder Park 进行了部分合并增删。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**要点快读：**

-   Perplexity AI 最大的特点是产品迭代速度快，Retrival 系统优化好：具体体现在生成速度快、模型 Hallucination 少，且回答中的每一句话都明确标注了引用来源。

-   但由于核心用户都在知识领域使用 Perplexity，目前尚很难成为一款低门槛的大众化使用产品。生活/购物助手等更高价值的场景可能是其用户泛化的路径，但该领域要竞争的是对于 Workspace、Shopping、Map 等深入积累的 Google。

-   作为创业公司，Perplexity 的重心在于打磨产品和召回系统，而不是自建模型+搜索技术栈。后者现在用的是 OAI 和 Google/Bing 的 api，但这样做成本偏高，且定价权掌握在别人手里，Bing 已经将其 search api 的价格上调了 10 倍。

-   作为一款知识生产力向的产品，Perplexity 目前以 20 美元的订阅制进行商业化，但这个商业模型对于问答引擎这样高 inference 成本的产品是不可持续的，尤其所挑战的搜索引擎有一套极其成熟的商业化模型，能使用户、商家、创作者同时受益。

-   接下来 Perplexity 必须要在商业化方面发力：如何帮助开发者和企业优化其搜索体验，如何将广告无缝地衔接入 AIGC 和 UGC。

-   如果没有长期新的商业模式出现，Perplexity 当前的形态更可能成为 Gen AI 时代的新 Quora + Wikipedia；如果探索出了 LLM native 的商业模式，Perplexity 具备挑战传统搜索的潜力。

## **01**

## **Perplexity AI：AGI 时代的搜索引擎**

Perplexity 几乎是最早推出的生成式搜索引擎，或者叫做回答引擎。借用大模型的力量，用户可以直接提问，Perplexity 会直接从各种筛选过的来源进行总结，提供准确、直接的答案，同时提供来源参考。

按照 Perplexity AI 联合创始人兼 CEO Aravind Srinivas 的解释：「Perplexity 基本上是将传统搜索索引与大型语言模型的推理能力和文本转换能力结合起来的产物。所以**每次你输入一个查询到 Perplexity 时，我们会理解你的查询，重新构建它，然后将其发送到一个非常传统的搜索引擎和多个搜索索引，这些索引不是我们自己的，而是外部的**。

从这些索引中提取出相关的链接，有时甚至有上百个链接。然后我们将简洁回答用户查询的任务交给大型语言模型。我们要求它阅读所有这些链接，并从每个链接中提取出相关段落，用这些段落来以学术或记者的写作风格回答用户的查询。也就是说，确保你的答案每部分都有支持性的引用、支持性的链接。这些都来自于我们的背景。」

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

当 ChatGPT 刚推出时，它凭借出色的自然语言理解能力和生成丰富回答的能力，曾一度让人们认为生成式 AI 可能会取代传统搜索引擎。然而，随着用户体验中的幻觉现象、无法联网和知识更新滞后等问题逐渐显现，人们开始回归现实，转向由大型模型增强的搜索引擎，例如 Perplexity 和 Bing Chat。这些「回答引擎」利用 RAG（Retrieval Augmented Generation）技术，对搜索引擎的结果进行处理，以减少误导信息并提高信息的及时性。除了 Perplexity 和 Bing Chat，其他一些曾企图挑战 Google 搜索引擎霸主地位的平台，如 You.com 和 Neeva，也转向了 AI 增强的答案生成模式。

与传统搜索引擎相比，回答引擎主要在以下几个方面进行了优化：**理解用户问题的能力、总结搜索结果的能力、保留搜索结果索引的能力，以及扩展用户问题的能力**。这些优化旨在降低用户使用门槛，节省用户在不同网页上搜索和浏览的时间，确保搜索结果的可靠性，同时为用户提供深入挖掘问题的能力。

正是因为这些特点，当 Bing Chat 于今年 2 月正式推出时，微软 CEO 纳德拉对其寄予了厚望，将其视为开启搜索新时代的重要标志。他认为这是对谷歌在搜索引擎市场长达 20 年的主导地位的前所未有的挑战。然而，到了 10 月的谷歌反垄断案时，纳德拉表现出了转变，坦诚 Bing Chat 尚有许多待解决的问题，且在市场份额竞争中未达预期效果。全球范围内，搜索引擎市场的格局依旧稳定。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

尽管在访问量上 Perplexity 仍远不及主流搜索引擎，而且也有许多批评声音将其视为仅是表面包装，但自推出以来，Perplexity 一直保持稳定增长，在同类产品中保持最高访问时间，其表现甚至超过了有多年 AI 结合搜索引擎经验的 You.com。在 a16z 发布的月访问量前 50 的 GenAI 产品中，PerplexityAI 排名第十。从 3 月到 10 月的半年时间内，Perplexity AI 每天处理的搜索请求量增长了 6～7 倍，目前每天要处理数百万个搜索请求。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

即使在其他大型模型纷纷引入联网能力后，Perplexity 仍保持良好发展势头。

## **02**

## **产品优势：精心打磨的问答引擎**

## **出色的产品迭代速度**

Perplexity AI 是一家 Gen AI 应用层公司，模型或技术栈能力不是核心价值，产品迭代能力强是重要特点。Nat Fridman，Github 前 CEO 在今年初称赞过 Perplexity：创立不到六个月，比很多公司全生命周期发布的产品迭代都更多。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

回到其产品公测的第一天：22 年 12 月 8 日，Perplexity 发布了其 beta 版本的搜索产品 Ask。根据用户的问题，输出用 Bing 搜索引擎结果验证过的 GPT 3.5 回答。其最早的产品与搜索引擎很接近，将文字输入顶端对话框之后，出现下面两段式内容：

第一部分是 AI 生成的总结，其中包含有引用内容和索引；第二部分是 AI 生成过程中参考的链接来源，会且只会出现 3 条。在生成内容下方可以给反馈：like 和 dislike，也可以转发到推特促使自然裂变。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

最早产品形态 

12 月 16 日，Perplexity 紧接着发布了第二款产品：Bird SQL，能够根据自然语言搜索推特中的内容。其实现方式是，用 OpenAI Codex 模型将自然语言变成 SQL，从当时还开放的 Twitter SQL 接口去查询到最相关的 post。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

由于 Twitter 自身的搜索功能优化得很差，这一功能在早期受到了很多好评。因为产品的查询是基于 SQL 实现的，还产生了很多有趣的数据可视化，与 ChatGPT 最近受到热议的 code interpreter 有些相似。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

可惜在今年 2 月底，Twitter 关闭了这个接口。从这个产品能看出 Perplexity 对搜索理解很深，且能抓住当时 Google、Bing、Twitter 都没有通过 LLM 优化自己搜索能力的时机，快速推出市场认可的产品。**Twitter 的搜索经验在未来也能帮助其他公司的数据库优化其搜索能力。**

今年 5 月，Perplexity 又大幅迭代了产品，问答引擎中的 Agent 实践：推出基于 GPT-4 理解和规划能力的 Copilot。在这款产品中，输入的问题中缺失的细节会由 Copilot 给出一些选项和输入框，使其能够让用户更精准地传达自己的需求。这一能力在输入复杂问题的时候，能给到更可控且准确的回答。当前的 copilot, 虽然只是一个界定了能力边界问答引擎助手，但却可能在尝试定义和探索未来基于 LLM 能力的 AI agent UI 形态。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

与这一产品发布的还有 AI profile 和 Perplexity Pro 方案，前者是用户自己的背景和偏好介绍，在使用 Copilot 的时候能体验到一定的个性化内容；而后者是一个月 20 美元无限使用 Copilot 的额度。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

根据 Lilian Weng 最新博客中的定义，Agent = Planning + Memory + Action with tools。Copilot 本身是 planning 的体现，AI profile 是 memory 的形式，而 Actions with tools 是当前 Perplexity 当前相对缺失的，也是最可能在之后和 Google 的竞争中落下风的：Google Workspace 中可以给 Bard 使用的工作和地图工具很多。

除了上文中这些重要迭代，Perplexity 产品还经历了一系列小迭代：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Perplexity 推出产品已经 7 个月了，开发和迭代速度很快，对 LLM 的想法也非常的应用思维：用好模型是第一位的，尽管他们有了自己的模型也不做任何宣传，因为认识到模型能力很难和 GPT-4 level 直接竞争。他们对搜索也有着很深的执念，目前 Ask、Bird SQL、Copilot 都围绕着核心命题：如何用 LLM 优化搜索的体验。

**功能创新，补足回答引擎的短板**

### 「Devil in the details.」，Perplexity 的卓越搜索体验得益于其众多创新功能，尤其是 **Source Edit（信源编辑）、Focus Search（专注模式）和 Perplexity Copilot**。

### Perplexity 并不总是都表现良好。例如，在查询「Twitter 的 CEO 是谁」时，尽管同类产品均能正确回答 Linda Yaccarino，Perplexity 却有时会答错。这一错误源于其引用了未及时更新的维基百科条目。针对此类错误，Source Edit 功能可提供有效解决方案。

### Source Edit 允许用户编辑参考信源并重新搜索。目前，这一功能仅支持删除而非添加信源，有效减少无关信源对结果的干扰，通过人工的方式，对潜在的不稳定性进行修正。可以看到，排除了包含错误信息的维基百科后，Perplexity 能够给出正确答案。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 此外，用户可通过 Focus Search 功能，在开始新搜索前限定搜索范围，提升搜索效果。该功能在学术搜索、数学计算、YouTube 视频和 Reddit 论坛搜索等方面进行了特别优化。特别是 YouTube 视频搜索，其引用可直接链接到视频中相关内容的准确时间点。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### Perplexity Copilot 则增强了搜索结果的准确性和可信度。作为用户的搜索助手，Copilot 提供更细致、深入和个性化的回答。

### 对于同样的问题，通常 Copilot Search 参考的信源更多、回答更长、展示方式更结构化，同时在搜索过程中，Copilot 会对用户的问题含义进行延伸，在一次用户的搜索中，实则进行了多次对于不同关键词的搜索。如下图所示，使用 Copilot 搜索同样的关键词，Copilot 会自动对用户的意图进行延伸，使用不同的关键词进行搜索并最终总结。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 个性化的搜索。Perplexity Copilot 不仅深入理解用户意图，还根据用户的个人情况提供定制化内容。例如，询问餐厅推荐时，会自动要求用户补充必要的信息，如餐厅所在的地点；同时，Copilot 会根据用户的 AI Profile 所需补充信息，如下图（右）可以看见，在作者在 AI Profile 中提前设置好了自己所在城市后，Perplexity Copilot 便不再要求用户补充地址信息；最后，当 Copilot 要求用户补充信息时，会采用更加 LLM Native 的交互方式，会根据要求的补充信息类型，Copilot 自主选择最合适的交互方式来让用户输入，如下图（右）就自动生成了一组复选框。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### Perplexity Copilot 使用了 Fine-tuned GPT-3.5 而非 GPT-4。根据测试，Fine-tuned GPT-3.5 在大多数情况下（69%）能提供与 GPT-4 同等甚至更好的性能，甚至在少数问题上，能够提供比 GPT-4 更好的表现。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### Perplexity 的愿景不仅是成为更好的搜索引擎，而是**打造一个全面的知识中心，助力用户轻松学习新知**。为此，Perplexity 自开发之初便专注于优化其引用信源和发散性问题处理能力。

### 9 月份，Perplexity 围绕此愿景推出了「合集（Collections）」功能。在 Perplexity 中，每次查询对话被视作一个线程（Thread），而合集则是线程的容器，功能类似于收藏夹。合集不仅能整理线程，还能围绕主题拓展新问题，邀请协作者共同构建知识社区。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### **产品评价与反馈**

#### **Quantative Analysis**

搜索引擎有一套严谨的指标体系，如 Precision@10（前十个结果是否解决用户的问题）、CTR（点击数/展示数），但这些指标对单个生成式的结果并不合适。Percy Liang 团队今年 4 月的一篇论文 Evaluating Verifiability in Generative Search Engines 中提出了一套对于生成式搜索引擎，也就是回答引擎的评价标准：

体感效果：

• 文本流畅度

• 内容有用性

引用能力：

• Recall（引用是否完整）

• Precision（引用是否准确）

经过他们对每个问答引擎 1450 道题的提问，评分如下：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

根据这一套评价体系，各回答引擎的生成体感效果总体都不错，其中 Youchat 的体感是最好的，Perplexity AI 排名第二，Bing Chat 垫底。

而到了引用能力部分，总体的表现就差了些。尤其是第一 part 表现良好的 Youchat 就出现了严重的可用性问题，大部分内容都没有得到文本支持。Perplexity 是在准召率上做得最平衡全面的，而 Bing Chat 尽管引用准确，但也和 Youchat 类似召回率偏低。和体感评分相比，这一项各产品的评分都不算高，Perplexity 是当前相对最好的。

因此，将以上评估指标投射到坐标轴上，可以看到在量化评估中 Perplexity AI 收到的评价是最好、最全面的。（注意，评测时 Perplexity 用的是免费版本不用 GPT-4 的，而 Bing 的是已经用上了 GPT-4 的版本，可见 Bing Chat 的表现不如人意）：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### **Qualitative Analysis**

Perplexity 作为回答引擎有两个重要的产品特点：

**1\. 很强的知识产品属性，阅读和分享体验与 Google 相比，接近 Wikipedia 和 Quora：**

-   显示文本引用来源：每次生成的回答中会有 3-5 个链接，来佐证其生成内容的准确性。阅读体验非常类似学术文献阅读，且来源可以控制：如果不喜欢华盛顿邮报的内容，就可以将其从 source 中删除，重新生成。

-   有完善的查询历史和内容分享：每次对话会生成一个链接 permalink，成为与其他用户分享的知识百科页，自己过去查询的历史也会完全记录下来。（详见 reference）其他的产品更多的是将查询内容当作聊天记录随用随抛，而 Perplexity 则将其作为维基百科，可见其对自己生成内容是更有信心的。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   焦点搜索功能：在搜索框下方，有个下拉菜单，其中包含多个领域，例如 YouTube、新闻、Reddit、学术等（学术专区增加了 SemanticScholar、Arxiv 和 NIH 等资源）。这个能力可以使搜索效果更为聚焦，用户调研中常见使用于学术研究和创意写作相关。

**2\. LLM 和搜索结合得很好，尽可能减少了 Hallucination：**

-   生成内容简洁且可靠：在与多问题引擎对比的时候，Perplexity 是最能用有限的字数准确回答问题的产品。Bing Chat 有时回答过于简短需要反复追问，Google Bard 有时回答太过冗长，需要从中提炼出关键信息。结合有用户反馈 Perplexity 生成的内容有大约 650 字的字数限制，能够精炼地提供言之有物的回答，是问答引擎这个场景的重要标准。

-   理解问题并拆解、主动反问的能力：在 Copilot 产品中，AI 能够根据问题理解，并且深入问题的细节反问得到更多信息，再去进行搜索。这里是灵活使用 GPT-4 的规划和理解能力，通过 prompt engineering 去引导其提问和反问，使生成的内容质量更高，可控性更强。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   多轮对话：在同一次搜索中可以不断追问，得到更接近自己想要的内容，在产品形态上兼具了 Chat 和 Search 的优点。实际使用时，偶尔会有多轮记忆和理解上的遗忘现象。

-   基本没有 Hallucination：有主动表示搜索结果中没有符合问题答案的能力。

-   多语言能力不错，生成速度快：Google Bard 目前只支持英语，Bing Chat 在浏览那一步的速度较慢。 

与 Bard and Bing 相比

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## **03**

## **技术：定位应用层，使用技术巨头的 api 开发产品**

技术对比：传统搜索引擎技术栈Google/Bing 搜索引擎的大致技术模块包括以下几个模块：

**1\. 内容收集和整理：**

这一层负责抓取网络、下载网页并解析它们以提取内容。它还包括一些过滤和优化内容的过程，如删除重复页面、检测垃圾邮件和按主题分类页面。

-   抓取：谷歌的抓取器，也称为 Googlebot，负责访问网站并下载页面。它们使用各种技术来避免使网站过载，例如限制每秒访问的页面数量和遵循 robots.txt 文件。

-   解析：页面下载后，会对它们进行解析以提取内容。这包括页面上的文本、图像和其他媒体。解析器还识别页面的标题、关键字和其他元数据。

-   过滤和整理：从页面中提取的内容接着进行过滤和整理。这包括删除重复页面、检测垃圾邮件和按主题分类页面。

**2\. 搜索核心：**

这一层负责对内容进行索引并创建搜索索引。它还包括一些用于在搜索结果中对页面进行排序的算法，如 PageRank，它根据页面与其他页面的链接关系衡量页面的重要性。

-   索引：经过过滤和整理的内容随后被索引。这涉及到创建一个包含页面及其内容、元数据和排名信息的数据库。

-   排序：索引中的页面使用各种算法进行排名。这些算法考虑到页面的内容、指向页面的链接等因素。

**3\. 用户和应用程序接口：**

这一层负责与用户交互并向他们提供搜索结果。它包括谷歌搜索网站以及允许其他应用程序访问搜索结果的 API。

-   谷歌搜索网站：谷歌搜索网站是谷歌搜索引擎最著名的用户界面。它允许用户输入搜索查询并查看搜索结果。

-   API：谷歌还提供了一些 API，允许其他应用程序访问搜索结果。这使得开发人员可以创建与谷歌搜索引擎集成的自定义搜索应用程序。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这些技术模块共同构成了 Google/Bing 搜索引擎的基本架构，而 Perplexity 的搜索能力是建立在这些巨头的能力之上的。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

而 Perplexity 的技术栈则直接基于 Google/Bing 的技术来绕过了需要长时间积累和工程复杂度的爬虫、数据库系统。其流程可以分为以下几个部分：

1.  **Google/Bing 搜索返回**：从他们的查询引擎 api 返回与用户 query 有关的网页内容。

2.  **索引系统**：将内容向量化进行细粒度的处理和组织，目标有二，其一是方便排序时能理解和定位到网页中与用户问题最相关的内容，其二是可以将 api 返回的内容存储以用作之后复用。

3.  **排序系统**：以语义搜索的方式 retrieve 最相关的内容，交给 LLM 作为 input 进行学习。

4.  **问答系统与 LLM 调用**：LLM 根据召回的内容进行学习，输出对用户 query 的解答，并在其中对引用内容进行标注。学习过程中根据用户选择和系统判断决定使用自研模型还是 OpenAI 的模型。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### **成本测算：长期需要自研 search stack 以降低成本**

使用大公司的 api 使他们能专注于优化产品，但也会拉高成本。他们意识到这点，回到了 ML Researcher 的老本行开发了 7B 的自研模型，成功将 query 中 LLM 生成成本降低到了相对低的水平。

但与此同时，和 Twitter 关掉自己的数据库一样，Google/Bing 也察觉到了搜索引擎 startup 的动向，将其 search api 的价格抬高了 10 倍左右，对 Perplexity 等不自建 search stack 的公司造成了压力。以 Bing Search API 为例：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

涨价后，单次 Bing Search 的成本在 0.015 美元，而 LLM 交互成本（如果自研模型成本能达到 GPT-3.5 一半的话）也就在 0.02 美元左右。因此接下来如果要将产品可持续地扩大使用量，search stack 的自研会使成本降低 30% 左右。按当前的假设估算，Perplexity 维持当前的搜索量和技术栈，一年需要的成本在 1000 万美元以上。技术非自研会对其未来的 runway 有比较大的影响。

Perplexity AI 的许多竞争对手产品仍然完全免费，而仅靠订阅机制的收入，难以满足对 API 的大量需求，阻止了现阶段回答引擎完全替代传统搜索引擎的可能性。目前，**Perplexity AI 已经在尝试构建自己的 WebCrawler、Search index 和 LLM 来应对不断增长的的查询请求来降低成本。**

## **04**

## **团队与融资情况**

### **创始科学家比例高，LLM/search/ranking 经验丰富**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Perplexity 团队目前有 18 人，其中一半以上是 Engineering Team 的。团队优点明显：创始团队对 LLM 有很深入的理解，工程团队对 Ranking /问答系统有很丰富的经验。大部分之前都在独角兽或大厂工作，有 3 位成员之前在 Quora 工作过。接下来重点介绍几位团队中的重要成员。

**CEO Aravind Srinivas** 来自印度，博士期间才移民来到美国。Aravind 是 UCB 的 CS Phd，主攻方向是在计算机视觉和强化学习中融入 Transformer 模型。Phd 期间，他先后分别在 OpenAI、DeepMind 和 Google 做 Research Intern。毕业后，他加入 OpenAI 工作了一年，研究语言模型和扩散模型。22 年 8 月，离开 OpenAI 创立 Perplexity。

**和他一起创业的是 CTO Denis**，有很强的搜索和工程背景。11-13 年期间，他是 Bing 团队的工程师，之后来到 Quora 成为排序算法的 Tech Lead。16 年从 Quora 离开后加入 Facebook FAIR，同样开始做计算机视觉和强化学习相关的研究，18 年开始在纽约大学做 AI Phd。

Aravind 在访谈中夸过 Denis 很会招聘，团队第三人就是 Denis 招来的：CSO Johnny Ho。他是哈佛大学数学/CS 双学位，毕业后在 Quora 待过一年，当时在 Denis 的 team 工作。离开 Quora 之后，他成为了职业编程竞赛选手、量化交易员。用 Aravind 的话说，Johnny 是 Perplexity 运转迭代速度高效的重要原因。在官方的 Discord 和 Reddit 中，Johnny 是主要的运营和收集用户反馈的那位，在团队中是复合型的多面手。

**Andy 是 Databricks 的 Co-founder**，CS Phd 出身的他在 Databricks 承担了很多创业公司运营相关的工作，先后做过 VP of professional services 和 VP of Product。在 Perplexity 早期，Andy 作为 President 以其连续创业的经验帮助公司少走了很多弯路。

**Henry Modisett 是 Perplexity 的 Founding Designer**。在加入 Perplexity 前，他在 Quora 待了 8 年，从产品早期的年轻设计师一直成长为产品的 design lead & manager。Quora 的 feed 流、问答和 Google 邮箱 iOS 产品设计都有他的参与。他在今年 2 月加入，那之后的产品迭代 feature 设计可能与他紧密相关，比如 4 月的网页设计风格改版和 6 月的 Copilot。

### **融资历史：天使投资阵容豪华**

融资历史：

-   2022 年 9 月，获得 310 万美元种子轮融资

-   2023 年 3 月，Perplexity 在 A 轮融资中筹集了 2560 万美元，估值 1.5 亿美元

-   2023 年 10 月，完成由 IVP 领投的新一轮融资，估值达到 5 亿美元

值得一提的是，团队的天使投资人阵容极其豪华，基本全是海外 AI/ML 的核心人物：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## **05**

## **商业化发展及未来**

### **早期核心用户稳定，尚需跨越鸿沟**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在今年初创始人 Aravind 接受采访的时候提到，Subscription 对问答引擎不是一个好的商业模式，Google 才是 role model。6 月，GPT-4 的接入和 Copilot 功能发布后，高额的 api 成本使 Perplexity 开始推出会员制产品：付费会员所有 query 回答都以 GPT-4 进行回答和生成，每天有 300+ 次 Copilot 使用额度。

对于 20 美元一个月的产品而言，用户的评价相对两极分化。有一部分用户认为其价格与 ChatGPT/Poe 持平是比较贵的，因为其提供的就是一个更可靠的 ChatGPT + Browsing 能力，而 ChatGPT 还有其他更丰富的 plugin offering，Poe 有 Claude 等其他 LLM 的接入。

Pro 方案推出三天后就有了 1000+ 付费用户。用户评价以大多是好评，认为 Pro 产品并不是单纯换了个模型 api，而是做了更用心的优化，使用 GPT-4 之后的查询体验更好，Hallucination、Latency 等效果好于 ChatGPT。商业化收入的快速成长，代表 Perplexity 已经有了稳定的核心商业化客户。

此外，团队还有其他的商业化想法：

1.  提供问答引擎 api：成熟需求，上千开发者来询问过。

2.  专业版个性化 Indexing：

-   To C：个性化体验（用户自己的链接、书签）；

-   To B：工作流工具，Index 工作中的合作仪表盘等。

4.  广告：如何用 Gen AI 做营销是当前最有趣的 Open Question。

### **未来发展分析**

**Upside: 颠覆搜索引擎市场，争夺 Google 的市场份额**

搜索引擎是一个巨大的垄断市场。在过去的五年中，Google 都保持着 90% 以上的市场占有率。在榜单上的公司都已经有 10 年以上的历史。一方面，这让他们积累了非常深的系统 Infra 优势，让后来者很难超越；但另一方面，这也使这些公司有着很深的 Legacy Problem，很难让产品彻底的转型。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Data Summarized by Perplexity 

同时，搜索引擎市场也非常大：2022 年谷歌搜索的收入是 $283B，Bing 的收入是  $11.5B。即使是市占率 5% 以下的玩家仍然收入不错。

但要侵蚀一部分 Google 的搜索市场占比，最大的挑战会是商业模型。Google 商业模型除了给用户提供高质量的搜索引擎外，还有两个非常重要的轮子。

其一是广告主营销，只有实现了满足广告主的商业化系统，才能有良好的现金流使用户免费地用上高质量的搜索系统；

第二是创作者激励，内容发布者能够通过在互联网上发布高质量内容，得到平台和广告主的激励，是其源源不断发布内容的动力。尽管 AI 看似减少了创作端需求，但还是需要用户去创作高质量的内容交给 AI 来学习和召回。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

除了商业化上的难点之外，还有产品形态上的难点。广告模型下的搜索引擎，天然是有良好的数据飞轮的：用户的浏览和点击行为，反应了用户的偏好，同时反馈到排序系统和广告竞价系统，使搜索引擎的效果更佳。

这样的数据飞轮在当下的问答引擎中还未出现：Chat 的形式并不方便用户直接去做偏好反馈，用户也不会有额外的时间去专门为答案做编辑或修改，Like/Dislike 类标签的比例也只有 10% 用户给出。问答引擎需要一个好的产品形态，来让用户使用的同时自然地给反馈，才能让产品在 Google 面前有竞争力。

当商业模式和产品数据飞轮的问题都能有原创的新解法，且不容易被复制时，相信 Perplexity 有潜力成为一家撼动巨头的公司。

**Neutral: Gen AI 时代的 Quora/Wikipedia**

撼动 Google 的市场可能暂时是一个好高骛远的目标，而成为新时代的 Quora/Wikipedia 这样的知识平台是完全有可能的。

在互联网时代，这两家公司都以优秀的知识产品出名，但是苦于没有好的商业化能力，没法持续的激励创作者留在平台上，流量价值进一步减少形成了负反馈循环。而 Gen AI 的出现正减少了内容供给上的压力，AI 替代大部分人类创作者组织和整理知识成为可能。从 Perplexity 当前的产品形态上，有很多知识产品的理念，核心用户群也常常使用其做知识研究类工作。

**Downside: 独到的收购价值，Tech Giants 可能都需要 LLM + Retrieval 能力**

Perplexity 团队是很独树一帜和清醒的：他们把用户的信任而不是技术栈作为自己的 moat。尽管从表面上来看，Perplexity 用的是 Bing Search 和 OpenAI 的 api，但技术栈类似的 Bing Chat 比 Perplexity 使用体验糟糕很多。可见其中有很多 Indexing、Prompting 等相关的技术和设计是比较复杂有技巧的，要做到严肃场景下的使用是一件很有门槛的事情。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

最近巨头开始了一波收购潮，Snow 收购了 Neeva（之前 Perplexity 的竞争对手，由于其完整的 search stack，被收购后专心做 enterprise search），Databricks 收购了 MosaicML，都还在技术栈查缺补漏的阶段。但经过这一阶段的探索，大家都会发现只有好的 LLM 是很难在商业环境下有好的使用效果的，LLM + Retrieval 是必要的解决方案。这时，Perplexity 这样一个深入理解 LLM 和 Retrieval 技术与应用、在一个红海赛道阶段性领先巨头的团队是否会有着更高的收购价值呢？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Reference：

https://www.perplexity.ai/search/4f22f1bd-e957-4a50-bc9e-591f16f42464

https://youtu.be/ix4\_rdogcVI

https://m.okjike.com/originalPosts/657687c22f2532e38b58e859?s=eyJ1IjoiNTVlZDJkMzhmOWE4ZTMwZjAwNWIzNmU2IiwiZCI6NH0%3D

---

如果你关注大模型领域，欢迎扫码加入我们的大模型交流群，来一起探讨大模型时代的共识和认知，跟上大模型时代的这股浪潮。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/qpAK9iaV2O3tr8RadIibA91KkXRfdILXPLVXSia7nSObtfXAg3Picpiarw843NiaaTy3B8RrxaOxn0OKNoHvuaDRzvSg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=41)

---

**更多阅读**

[从100多个GPTs里，探究OpenAI究竟想要什么，又做了什么](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247492676&idx=1&sn=b18c31e88476e046c46a3ac5f65f5185&chksm=c0090278f77e8b6e37502b467ce871ff08234be3c534c6a0f73ab6062b34e445d93ca0cc1a9b&scene=21#wechat_redirect)

[Meta、Midjourney、Adobe、DALL·E：四大巨头的 AI 绘图模型综合评测](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247492746&idx=1&sn=b1ff69a9eb38ac6d701834513b9a6830&chksm=c00902b6f77e8ba0b397b0b0ed4aafa4bc14fc57888354165c7a5b1b33afbc0e326ce86837e0&scene=21#wechat_redirect)

[时代周刊：为什么 Sam Altman 是 2023 年度 CEO？](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247492720&idx=1&sn=483f1293fb6a5a3444d4eaf1ab68b954&chksm=c009024cf77e8b5ac9aec3b606ce602ecc08f14aa7c382a3f9902148699baaab595c2b0dabaf&scene=21#wechat_redirect)

[MindOS：站在AGI风口，创业两年的教训与思考](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247492668&idx=1&sn=73b4fa1c2a6c4d87f99c84d8ec0795c3&chksm=c0090200f77e8b161ec0efd3240870c0ca9cb24622216fad47f9a665164af3cc5618a60fa8ca&scene=21#wechat_redirect)

[专访Pika Labs创始人：视频模型技术路线尚未确定，明年会迎来AI视频的GPT时刻](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247492662&idx=1&sn=6fdd2c53b7c4b3c036de169f0b72baad&chksm=c009020af77e8b1c7a177f12cbecf73cadf657c5ff121a4e7fa76b7899d8927d44f466cf8e8e&scene=21#wechat_redirect)

转载原创文章请添加微信：geekparker