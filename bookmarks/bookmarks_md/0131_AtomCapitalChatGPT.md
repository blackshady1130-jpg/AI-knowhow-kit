---
url: https://mp.weixin.qq.com/s/VZ6n4qlDx4bh41YvD1HqgQ
title: "Atom Capital：深入探讨ChatGPT带来的产业变革"
description: "详解ChatGPT带来的AI产业的根本性变革。"
author: "科技最前沿的"
captured_at: "2026-03-08T10:36:53.885Z"
---

# Atom Capital：深入探讨ChatGPT带来的产业变革

**写在前面**

2022年11月30日， OpenAI发布了ChatGPT。短短3个月，月活用户达1亿，日活1300万。这是个分水岭，从此AI领域被分成两个阶段，之前（pre）和之后（post）。ChatGPT开启了产业的根本性变革。

作为早期投资机构，我们对ChatGPT引发的变革以及由此带来的机遇非常感兴趣，一直在学习和研究。2月11日，我们举办了一次闭门沙龙，邀请AI领域专家、创业者以及硅谷投资人等朋友们一起深入研讨。结合沙龙讨论和我们的思考，在此整理成系列文章。这是第一篇，部分来自会上几位朋友的精彩分享，特别感谢周明（ACL国际计算语言协会主席、澜舟科技创始人）、张东晖（前微软Bing亚洲搜索技术负责人、前阿里云产品负责人）、王建硕（百姓网创始人）、孙锋（前微软搜索广告算法负责人、Opera News负责人）。

Atom Capital将持续关注大语言模型（LLM）驱动的新一轮技术变革所带来的机会，连接顶尖专家与创业者，组织系列沙龙，将第一线观点整理分享给大家，欢迎关注。本系列共三篇，接下来两篇会讨论由此而来的新机遇和挑战，以及在中国的发展路径、落地场景和节奏。

![图片](https://mmbiz.qpic.cn/mmbiz_svg/ibhzWy4ibIEpAy78Y4a5EyPo8hTIWqn9y873hdcOKanfD6cNAxz1ZtM44XCWxYxcdjiaE7wUV2VHapc983ZRRdSicDZ2p9TwOAYC/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**本篇先来回答一个问题：为什么ChatGPT引发业界如此大的震撼？**

![图片](https://mmbiz.qpic.cn/mmbiz_png/jzj22lLOoeOWo0evxyrcZTnibwicF4w2C4UhWfLYDgvPlHsx8Ldiby306ls67Bic52qY2VWPIe0GsFXIIzxpmuQIHA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

 **01**   **对比之前chatbot, ChatGPT有哪些实质性突破？**

**极好地理解用户意图****。**根据用户的自然语言输入，它能够理解并准确地把握用户意图。这种能力的突破，其意义已超越了Chat本身，未来可以彻底改变人机交互的模式。

**真正做到多轮沟通。**之前的聊天机器人，一轮对话经常勉强，多轮对话更是基本鸡同鸭讲。ChatGPT因为对一个session内的上下文有深入理解和记忆，能够联系之前的聊天内容，轻松地进行N多轮对话。

**回答不是简单的搜索结果。**市场上客服或聊天机器人，回答基于搜索结果。ChatGPT回答内容更完整、重点清晰、有概括、有逻辑、有条理。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 **02**   **ChatGPT**颠覆性能力**如何养成的？**

**模型规模使能力“涌现”**

涌现是指系统里的量变导致行为的质变。LLM在模型规模与能力上，呈现出一种与“进化”类似的曲线——最开始在模型训练几何级数的投入增长，只能得到线性的收益。而一旦训练规模超过某个水平，会有一些不可预测的能力突然涌现出来。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

比如，三位数的加减法能力，需要13B；4-5位加减法，需要175B; 而COT（Chain of Thoughts）能力是在62B以上涌现的。

模型规模是解锁LLM 新能力的关键。同时也意味着，我们无法通过简单线性外推小模型的性能来预测更大模型的能力。我们无法预判，1000B模型能够发展出什么能力，5000B呢？业界目前还无法完全解释这个现象，从业者会不断探索和尝试，期待随着LLM 规模的增长带来意想不到的惊喜。

**工程为主不断优化**

OpenAI团队把LLM模型当作产品，持续打磨迭代。LLM的成功，很大程度上来自深厚的工程能力。除了规模以外，以下几个方法对提升ChatGPT能力有显著贡献：

-   **指令调优（Instruction tuning）。**它可以激发语言模型的理解能力，通过给出更明显的指令/指示，让模型去理解并生成正确的结果。

-   **代码训练（Training on code）。**通过用代码和文本数据混合训练，让模型拥有了强大的推理能力。模型从代码中习得了逻辑。

-   **基于人类反馈的强化学习（Reinforcement Learning from Human Feedback) 。**根据人类反馈，用强化学习算法来优化语言模型，对准确性提升有明显效果。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 **03**  **LLM开启行业根本性变革**

**新摩尔定律与涌现能力
**

OpenAI在2018年发表过一篇报告，阐述AI领域的新摩尔定律。自2012年以来， AI训练运行中最大所使用的算力呈指数增长，每3.5个月翻倍（即每年增长10倍）。对比一下，摩尔定律的翻倍时间是18个月。下图纵轴是AI训练所使用的算力，逐年呈指数增长。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这意味着训练成本越来越高，算力需求的提升大于芯片处理能力的提升。同时，模型规模增长带来了“能力涌现”，破解了这种成本压力——**新的能力会带来新的商业动力和应用，让AI训练的边际效益显著提升**。这会推动对AI的持续投入，形成一个巨大的产业飞轮。我们今天看到的ChatGPT正是这个产业飞轮带来的突破。预计在可见的未来，在这个产业飞轮带动下，AI模型还会持续增加，AI能力也会随之不断飞跃。

**人机交互，开启自然语言交互新时代**

**我们认为，这轮AI发展推动的本质变革在于引领了新一代人机交互方式，核心是自然语言成为人机交互的媒介。**这跟用 ChatGPT 来做 AIGC是不同层面的两件事。前者是真正的技术革命，有机会重构所有的软件和工具，而后者则是生产效率的提升。

纵观IT史上真正颠覆性的产品， 从Macintosh和Windows（PC操作系统）到Netscape（浏览器）、Google（搜索引擎）和iPhone（智能手机），无一不是人机交互变革的引领者。人机交互革命意义重大，**因为每一次人机交互方式的变化，都彻底改变了用户构成，扩大了用户群体，创造出新的市场空间和机会，甚至新的职业，而不仅仅是零和博弈。**也只有这种颠覆式变革，才能给“新王”诞生留出足够大的空间。

软件，尤其是生产效率和2C软件，未来会迅速支持自然语言接口。从开发工具和办公软件开始，之后电商、游戏、娱乐等，直到渗透到人类生活的每一个方面。在企业端，大部分产品形态也会彻底改变。以数据库/数仓为例。自然语言交互带来用户群扩大（从专业的分析师扩展到公司所有员工），门槛降低带来访问量急速增长。几个因素叠加，对数据库内核的考验是前所未有的，目前产品很难支持。所以，交互方式的改变将引起产品形态和框架等根本性的变化。

因此，很多工作（比如数据挖掘、软件开发、投资分析等）的技术门槛会大幅降低，导致专业人员和管理人员可以获得更多洞察和现实掌控力，同时也为很多产品和服务带来一个高客单价群体。**作为一个巨大的增量新市场，会彻底改变很多领域的市场和产业格局。**

接下来，许多业务都会有全新的“打开方式”。我们期待看到并帮助一批新的科技公司在这个领域的探索。

**产业结构向水平化发展，产业格局初现**

**我们认为，AI在经历了五十多年发展后，迎来了产业结构向水平化发展的契机。**而这一契机的源头，是NLP领域正在经历从“Pre-train + Fine-tune”向“Pre-train, Prompt, and Predict”的范式转移。

在“Pre-train + Fine-tune”模式下，预训练模型需要根据下游任务进行调整；而在“Pre-train, Prompt, and Predict”这一模式下，则变成了调整下游任务以适应预训练模型。与前者相比，Prompt Tuning可以做到只对Prompt部分的参数进行训练，同时保证整个预训练模型的参数固定不变。**这意味着不再需要针对不同任务训练不同的模型，做到“一个模型包打天下”。**

这是个重要变化，为AI产业的水平化分工奠定了基础。在此模式下，未来只需要少数几个大语言模型。只要使用者基于具体任务给出恰当的Prompt，大模型就能适配到多个场景。大模型成为基础设施；在大模型之上，演化出一层聚焦于Prompt Engineering的公司，做好用户与模型的对接。

由此水平分工的AI产业格局初步形成。从底往上：**底层基础设施（云服务商）— 大模型 — Prompt Engineering Platform — 终端应用。**

我们观察到，最近一年在硅谷成立的AI创业公司，基本都基于这种全新水平产业结构。回顾上一次AI创业潮，很多AI头部公司都发展得比较艰难。一大原因是当时产业还处于垂直一体化格局，AI公司从芯片到模型到平台到应用全部都要自己做，这对于创业公司来说挑战巨大。当产业进入到水平化分工之后，创业公司只要聚焦在自己擅长的方向上去做突围，为创新提供了更好的土壤。

***About Atom Capital***

*我们是一家新成立的风险投资基金，专注于AI、大数据、云原生和Web3领域的早期投资。作为一群连续创业者和风险投资人，我们热爱颠覆性的创新技术，相信长期价值。希望通过投资和孵化，陪伴创业者一起成长。*