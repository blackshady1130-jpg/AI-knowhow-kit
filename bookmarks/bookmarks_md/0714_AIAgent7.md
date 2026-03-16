---
url: https://mp.weixin.qq.com/s/3S0_nwhKMYKqA19-Il223Q
title: "AI Agent 摩尔定律：每7个月能力翻倍，带来软件智能大爆炸"
description: "这一趋势甚至还在加速"
author: "拾象"
captured_at: "2026-03-08T13:03:13.810Z"
---

# AI Agent 摩尔定律：每7个月能力翻倍，带来软件智能大爆炸

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgzK0WM7op1RyIOvW3u6NDDSGGmYXSYr26GY9Qe3q3EkjLk8l8EUXvk2hys15qH0n4kWXFmziasmCyA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgzK0WM7op1RyIOvW3u6NDDSopEw6UW1vkrF85cSVAzXvGus0bgwTSWibViatmbpKwjEqBWbeQp61kfA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

编译：haozhen

编辑：Siqi

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

AI Agent 领域也存在 scaling law，甚至还在加速。

2022 年 ChatGPT 刚发布时能够实现的代码任务差不多等同于人类耗时 30s 的任务，到今天，AI Agent 已经能够自主完成需要人类花费一个小时的 coding 任务。“任务长度”是一个相当直观地测量 AI Agent 能力变化的标准。 

AI 独立研究机构 META 的数据分析发现，Agent 能够完成的任务长度正以指数级增长，大约每 7 个月翻一倍，预计 2029 年 Agent 能够完成时长为 1 个工作月的任务。

有意思的是，最近这一趋势甚至还在加速，2024-2025 年 Agent 能完成的任务长度约每 4 个月翻一倍，如果这种更快的趋势持续下去，Agent 可能在 2027 年就能完成长达一个月的任务。

本文是对 META、Forethought 和 AI Digest 研究对于 agent scaling law 的整理编译。AI 研究人员们认为，AI scaling law 的终局是 AI agent 自主开发 AI agent，到了那个时候我们就会进入软件智能爆炸时代（Software Intelligence Explosion，SIE）。

衡量模型能力进步和算力成本下降的“新摩尔定律”是基础模型竞赛阶段的关键坐标系，随着 2025  Agent 落地，摩尔定律进入 3.0，AI agent 的 scaling law 也为我们部署 agent 投资和产品提供了参考指引。

💡 目录 💡

     01 如何科学衡量 Agent 的能力  

     02 AI Agent 能力每 7 个月翻倍

     03 AI Scaling Law 还在加速 

     04 为什么会出现 Agent Scaling Law

     05 终局猜想：Agent 开发 Agent

     06 潜在瓶颈和解决方案

**01.**

**如何****科学衡量
Agent 的能力**

虽然 AI 能力在某种意义上正快速提升，但这种提升与对现实世界的影响之间的关联并不清晰。

在大部分定量测试问题上（exam-style problems），AI 很多时候已经比人类专家还要强，并且只靠极低的算力成本就可以实现这一点，经过专门的 fine-tuning 后，AI 甚至已经可以帮人类处理很多任务。

但即使是能力最强大的 AI Agent，目前也无法独立完成实质性的项目，或直接替代人类劳动力，甚至无法可靠地进行基础的电脑操作。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**考虑到 AI Agent 并不是缺乏解决单步骤任务的技能或知识，它们主要在多步骤任务中，将更长的动作序列串联起来时会遇到困难，因此，METR 的研究人员选择以人类专业人士完成某个任务所需的时间定义为“任务长度”，并把“任务长度”作为衡量 Agent 在现实世界能力的指标。**

直观来看，ChatGPT 在 2022 年推出时，它能够完成耗时 30 秒的 coding 任务，到今天， AI Agent 已经能够自主完成需要人类花费一个小时的 coding 任务。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**02.**

**AI Agent  能力**

**每 7 个月翻倍**

METR 选取了 2019 年至 2025 年间最强大的 AI Agent ，并在大约 200 个任务上进行了测试，这些测试中主要是 coding 类任务，还有一部分是通用推理任务，这些任务的长度短至 30 秒以内，长至超过 8 小时。随后，他们将 Agent 的任务成功率与每个任务的长度进行了比较，发现：

•**任务长度与 Agent 成功率高度相关（R² = 0.83）；**

**• Agent 在成功率为 50% 的情况下，能完成的任务长度呈指数级增长。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**任务长度与 Agent 成功率高度相关**

在一组多步骤的任务中，METR 发现，当模型在完成耗时少于 4 分钟的任务时，成功率接近 100%；但对于耗时超过 4 小时的任务，成功率却不到 10%。

基于这一发现，可以用“模型能够以 x% 概率成功完成的任务长度”来描述模型的能力，并拟合出一条曲线，以任务长度来预测模型的成功概率。也可以确定一个成功概率数值后，基于曲线来预测这一任务成功率下， AI Agent 可以完成的任务长度。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

人类完成任务所需时间与模型任务完成成功率的关系图

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

模型能够以 50% 概率成功完成的任务长度示意图。例如，Claude 3.7 Sonnet（图中最右侧的模型，用最深的绿色表示）以 50% 概率成功完成的任务长度约为一小时，因为拟合曲线在这一时间点与 50% 成功概率的阈值相交

**这一点也很好得解释了前面提到的现象：**模型能够在很多 benchmark 测试上超越人类能力，但到了日常工作自动化的场景中，又常常显得不够可靠。

因为即使是今天最先进的模型，这些模型能够解决一些即使是专业人士也需要花费数小时的难题，但在任务执行上，它们在保证质量稳定的前提下，可以参与“任务长度”还停留在几分钟以内的水平。

**AI Agent 能够执行的任务长度每 7 个月翻倍**

在过去 6 年中，以 50% 成功概率为标准，头部模型能够完成的任务长度已显著增加。如果在对数坐标系中绘制这一趋势，模型能够完成的任务长度与指数趋势高度吻合，大概每 7 个月翻一倍。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

虽然 Agent 能够完成的任务长度的长短取决于研究人员所定义的计算方式，比如研究中使用的任务类型、用于衡量表现的人类水平等，但整体趋势大致是正确的：大约每年有 1-4 次翻倍。在未来 2-4 年，如果过去 6 年的这种趋势可以继续保持，那 Agent 将能够完成各种为期一周的任务。

而且这一趋势非常陡峭，这意味着，即使测量存在较大误差，或者模型与人类对比时存在偏差，都不影响对趋势的预测，极端情况下，即使绝对测量值存在 10 倍的偏差，但反应到 AI Agent 能力进步的时间预测，这种偏差仅为 2 年。

不过我们仍然要考虑到存在模型显著误差的可能性。比如，在预测 AI 未来表现上，与用 2024 年之前的 AI 发展趋势相比，用 2024 年之后的 AI 发展趋势来预测的话，时效性会更强。

如果只对 2024 年和 2025 年的数据进行拟合，AI Agent 的可靠性在 50% 不变的情况下，Agent 实现一个月任务长度能力的时间缩短了~ 2.5 年。

Agent 能完成的任务长度的指数级增长趋势似乎非常稳固，而且目前没有出现趋于平稳的迹象。根据这一趋势进行推测，预计：

• 2026 年 Agent 能够完成时长为 2 小时的任务，

• 2027 年 Agent 能够完成时长为 1 个工作日（8 小时）的任务，

• 2028 年 Agent 能够完成时长为 1 个工作周（40 小时）的任务，

• 2029 年 Agent 能够完成时长为 1 个工作月（167 小时）的任务。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**03.**

**Agent Scaling Law
还在加速**

如同上面提到的，AI Agent 能力进步上不仅存在 7 个月翻倍的趋势，且能力翻倍的时间还在不断缩短，且这一趋势甚至还在加速，这本质上是因为底层模型能力还在不断进步。

**在 METR 的测算中， 2024-2025 年，Agent 能完成的任务长度每 4 个月翻一倍，而 2019-2025 年，这一速度是每 7 个月翻一倍。这意味着，如果 4 个月翻倍这一趋势可以持续下去，到了 2027 年，Agent 就可以完成完成一个月时长的任务。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

而且这个速度还有可能进一步加速，目前可能正处于比指数增长更快的增长轨迹上。直观来看，这也是合乎情理，**因为 Agent 在完成为期 1 周和 2 周的任务时，所需技能的差距可能比完成 1 年和 2 年的任务时更大。**

此外，随着 AI 能力的提升，AI 在开发更强大 AI 上的作用也将越来越大，**这也可能导致 Agent 能完成的任务长度呈现超指数级增长。越来越强大的 AI 系统可能会触发加速飞轮效应，即 Agent 加速创造更强大 Agent，而这些更强大的 Agent 又进一步加速创造更强大的 Agent。**

因此 Agent 的能力可能会迅速飙升，超越任何人在 AI 研究领域的能力，甚至延展到其他或所有领域。这种影响将是革命性的。**Agent 能完成的任务长度的增加可能最终成为人类历史上最重要的趋势之一。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**04.**

**为什么会出现 
Agent Scaling Law**

独立 AI 研究机构 Forethought 围绕 AI R&D 话题做了系列研究，这一研究可以解释 Agent scaling law 出现的原因。研究结果表明， AI 能实现这么快速的进步，背后的动力来自 LLM 硬件和软件的突破。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**硬件：更多算力和更多数据**

在算法和数据没有变化的情况下，只依靠算力规模的提升就可以带来模型能力的增强。例如，GPT-3 本质上是 GPT-2 的扩展版本，但由于算力的大幅提升，GPT-3 不仅能够进行连贯的对话，还能编写可运行的计算机代码、进行语言翻译和创作诗歌，而 GPT-2 在表现上大多是语无伦次的胡言乱语。

而且前沿 AI 系统算力的提升不仅会改进相同任务的表现，还可能带来新能力的涌现。研究人员有两种方法来增加 AI 系统的算力：

1\. 花费更多资金购买更强的计算资源；

2\. 开发出更高效的硬件，使相同成本下的算力更强。

**软件：开发更好的 AI 模型**

“AI 软件”包括除算力层硬件外的几乎所有内容，比如 AI 技术范式，系统架构，训练算法，数据获取，参数调整，fine-tuning 的方法等等。

AI 软件进步可以进一步分为两类：

1\. 效率改进，新 AI 系统执行与之前 AI 系统大致相同的任务时，计算成本更低；

2\. 能力改进，新 AI 系统能够完成之前系统完全无法做到的任务，或在相同任务上表现得更为出色。

在实践中，效率改进和能力改进之间的界限有时较为模糊。例如，更高的训练效率可以训练出更大的 AI 模型，而更大的模型往往表现出新能力或更好的性能。

AI 软件进步很难衡量，尤其是能力改进，例如 ChatGPT 通过 GPT-3.5 实现更具信息性的对话，并将其集成到直观用户界面中开发而成的，如何量化 ChatGPT 在与用户高效对话方面的进步，或良好用户界面带来的提升？

相比之下，效率改进比较容易衡量，比如可以比较 AI 系统在达到特定性能水平时所需的算力。

下图中，LLM 的训练效率估计值（约 8 个月翻倍）是相对保守的，因为没有考虑训练后的改进，而运行效率估计值（约 4 个月翻倍）则显得相对激进，因为包含了软件之外的因素。

**如果在这两个估计值之间取均值，可以得出训练效率和运行效率都具有约 6 个月效率翻倍的时间。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

不同分析方式下，AI 效率翻倍所需时间

**AI 能力的进步 > 算力成本下降**

除了效率提升之外，AI 能力提升也相当显著，甚至可能比效率提升更重要。

最近 AI 系统的新能力在提升系统实用性方面，远超已有能力的效率提升。**过去 10 年中 AI 经济重要性的增加主要来源于 AI 新能力的出现，而不是已有能力在算力要求上变得更低。**

比如 LLM 的能力提升，RLHF 使得对 LLM 进行“微调”成为可能，可以让其扮演特定角色，而不仅仅是模仿互联网文本。此外，LLM 训练效率的提升也可以转化为能力提升，通过 scaling 使新能力涌现。

LLM 公司可以通过两种方式将训练效率提升应用于 LLM：

1\. 创建与之前系统性能相当、但速度更快且计算成本更低的 LLM；

2\. 创建计算成本相同（或更高）、但能力增强的系统。

大模型公司通常同时进行这两种尝试。开发者通常对（2）更为兴奋，并倾向于在流程中整合他们可用的最强模型。但如果效率提升是主要推动力，（1）会引发更多行业关注。

**05.**

**终局猜想：
Agent 开发 Agent**

前面提到，当 AI Agent 能力足够强时，极有可能会出现“Agent 开发 Agent”的现象，这一现象被 Forethought 定义为 ASARA，即 AI Systems for AI R&D Automation，出现一个 **AI 系统能够完全自动化 AI 研发中涉及的所有任务。**

值得注意的是，训练新 AI 系统所需的算力通常远大于运行已训练系统副本所需的算力。这意味着，如果用于训练 ASARA 的算力被重新分配用于运行，则可以并行运行数十万份甚至数百万份副本。如果每个副本都能匹配顶尖人类研究者的表现，ASARA 的认知总输出很可能相当于数百万名顶尖人类研究者。

目前，全球大约有数十万名研究人员从事不同的 AI 软件研发，但绝大多数人员并未专注于提升最先进的 AI 能力，AI 研发能力远未达到人类潜力的极限。然而随着 ASARA 的到来，可以想象出一个拥有数百万虚拟顶尖研究者的团队，其中很大一部分可能专注于推进最前沿的能力发展。

**如果当前的 AI 软件进展速度意味着 AI 效率的翻倍时间约为 6 个月，那么 ASARA 会显著提升进展速度，Forethought 粗略估计，AI 效率翻倍所需的时间可能会缩短到 1-2 个月。**

**如果这个循环完全不需要人类干预，AI 进展速度可能会越来越快，最终达到软件智能爆炸（Software Intelligence Explosion，SIE），**指的是仅由软件驱动的反馈循环在 ASARA 诞生后也能引发加速的 AI 进步）。

在 SIE 状态下，假设硬件投入保持不变，人类研究人员将全部被 ASARA 替代，AI 进步更快，同时 ASARA 自身能力不断增强。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**一个演示 ASARA 发展的数学模型**

我们可以构建一个简化模型，来演示在实现 ASARA 之后的增长飞轮，假设总算力保持不变，这个数学模型将展示两种情景假设：

1\. 软件研发的收益递减：随着软件改进变得越来越难，进一步提升变得更具挑战性；

2\. 日益强大的 ASARA 带来的正反馈：更强大的系统反过来推动更快的进展。

该模型还包含几个简化假设：

1\. ASARA 可以分解为多个独立的 AI 研究员，每个 AI 研究员都能够执行软件研发中的所有任务；

2\. 所有 AI 进展都表现为撰写论文，每篇论文代表一个增量的进步，因此进展可以通过累计论文数量来简单衡量；

3\. 所有 AI 研究员的生产力都是相同的，可以简单表示为每单位时间撰写的论文数量；

4\. AI 研究员的生产力不会随着时间变得更高或更低，但可以变得“计算更高效”，即运行每个 AI 研究员所需的算力减少。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

• **情景假设 1：软件研发的收益递减**

假设一开始只有 1 个 AI 研究员，AI 研究员的生产力为每月 1 篇论文，并且在撰写了 2 篇论文后，计算效率可以翻倍，即 2 个月后，相同的硬件下可以容纳 2 个 AI 研究员，每个研究员每月可以撰写 1 篇论文，因此总生产力是每月 2 篇论文。

但由于软件研发的收益递减，下一次效率翻倍所需的论文数量会增加——假设增加 3 倍，需要 6 篇论文。所以有了 2 个 AI 研究员之后，这两个人撰写 6 篇论文，即 3 个月时间，才能实现第二次效率翻倍。

到第 3 个月，在这 2 名研究员完成 6 篇论文撰写后完成了第二次效率升级，每个人每月可以撰写 3 篇论文。此时，硬件能力进步允许容纳 4 个 AI 研究员。与此同时，第 3 次效率翻倍所需的论文数量会更高——假设再次增加 3 倍，变为 18 篇论文。有了 4 个 AI 研究员后翻倍将需要 4.5 个月。

在这种情况下，每次效率翻倍所需的时间越来越长：第一次需要 2 个月，第二次 3 个月，第三次 4.5 个月。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

• **情景假设 2：ASARA 飞轮带来的正反馈**

同样假设最初只有 1 个 AI 研究员，每月能撰写 1 篇论文，第一次效率翻倍需要撰写 2 篇论文。而第二次效率翻倍仍然需要比第一次更多的论文，即软件研发仍然存在收益递减，但增加的数量不会很多，假设第二次翻倍需要 3 篇论文，比第一次多 50%。

在有了 2 个 AI 研究员后，每个 AI 研究员每月撰写 1 篇论文，3 篇论文可以在 1.5 个月内完成，以此类推，翻倍的速度会越来越快。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

如果仅在这个简化模型的框架内进行推测，这意味着在有限的时间内将实现无限的进步。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

总而言之，在软件研发的收益递减时，每次效率翻倍所需的论文数量比上一次增加超过一倍（例如，从 2 → 6 → 18），这意味着 AI 进展变得更难的速度超过了 AI 研究员增长的速度。

而在 ASARA 带来的飞轮中，每次效率翻倍所需的论文数量比上一次增加不到一倍（例如，从 2 → 3），这意味着 AI 研究员增长的速度超越了效率翻倍变难的速度。

如果每次效率翻倍所需的论文数量恰好翻倍，那么每次效率翻倍仍然需要 2 个月（例如，2 个 AI 研究员需要完成 4 篇论文，4 个 AI 研究员需要完成 8 篇论文，依此类推）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

若在模型中不仅关注效率改进，还关注能力改进时，**当能力改进使得 AI 的输出增加到等同于效率翻倍的程度时，就称该能力改进使 AI 软件能力翻倍。**

**Forethought 用软件研发回报率 r 来衡量进一步改进 AI 软件的困难程度，r 表示在 AI 软件研发累计工作量翻倍的情况下，AI 软件能力翻倍的次数。r 值越低，表示改进变得越困难。**

r 值设定如下：

• 当 r=1 时，会出现持续的指数增长，每次软件能力翻倍都需要 2 倍的研究投入。

• 当 r<1 时，会出现进展变慢的现象，每次软件翻倍都需要超过 2 倍的研究投入。

• 当 r>1 时，对应出现 SIE，每次软件翻倍所需的研究投入少于上一次的 2 倍。

假设在 ASARA 首次开发时，软件翻倍时间缩短至 1 个月。

如果 r = 0.7，每次 AI 软件能力翻倍所需的时间将比上次多 35%，这意味着第二次软件能力翻倍将在 41 天后发生，第三次翻倍将在 55 天后发生，第四次翻倍将在 74 天后发生，第五次翻倍将在 100 天后发生。这将导致在不到一年的时间里，AI 软件能力提高约 30 倍，且随后几年的进展会显著放缓。

这个进展下的年度增长率可能与当前 AI 系统的提升速度相似，尽管当前 AI 系统的提升不仅包括软件进展，还包括硬件进展和硬件支出的增加。

如果 r = 3，那么每次翻倍将需要上次的 63% 的时间，意味着接下来的几次翻倍将分别需要：19 天、12 天、7.6 天、4.8 天，依此类推。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

持续的指数增长可能显得不太可信，因为 r 必须恰好为 1，但有可能是因为人类会采取措施，来维持在这个微妙的平衡点上，比如人类可能会在希望进展“加速”和进展“稍缓”之间摇摆不定；人类可能会有意识地制定政策，期望能够实现 AI 系统更平稳的能力增长。

**因此，由上述讨论可知，是否会发生 SIE 完全取决于 r 是否大于 1。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**有一个值得讨论的问题是：现实世界中，软件研发回报率是大于 1 还是小于 1？**

虽然上述模型是针对 ASARA 场景，但在没有达到 ASARA 的当下也适用。在当前环境下，r 表示的是，每次人类的研发累计工作量翻倍时，AI 软件能力翻倍的次数。因此可以通过测量当前人类软件研发累计工作量的增长，并将这一增长与 AI 软件能力的增长关联起来，来估算 r 的值。

Forethought 研究了图像识别、LLM、AI 算法效率等领域，并考虑到 AI 能力提升，以及软件改进的乘法效应，即训练算法的改进与后期的微调、搭建框架等技术是乘法性相互作用的。**Forethought 表示人类软件研发累计工作的翻倍将导致 AI 软件能力的若干次翻倍，猜测 r 的最佳可能值在 1-4 之间。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这个结果实际上将软件的进展与硬件的进展放在了类似的基础上。Tom Davidson 曾估算了硬件的 r 值，发现历史上 r 值大约为 7，而对于 AI 芯片（特别是 GPU），从 2006 年到 2022 年，r 值约为 5，即每次研发的投入翻倍，计算成本会降低了 5-7 倍。虽然硬件在过去几十年中的迅速发展是广为人知的，但不太为人所知的是，软件进展可能也以类似的速度增长。

然而，当前的 r 值在长期内预计是不可持续的。对于固定数量的硬件，AI 能力的实现存在根本性的物理限制，随着我们接近这个极限，软件进展可能会放缓。

但没有充分的理由认为这一极限会仅略高于第一个 ASARA 的水平，第一个 ASARA 可以被认为是第一个在相关认知领域内替代人类工作者的系统。人类可能不是最智能的生命形式，而仅仅是地球上第一个足够聪明，可以从事科学和工程等活动的生命形式。人类在认知属性上的范围是广泛的，人类仍然在通过人口增长、专业化以及各种文化发展中获益。

此外，ASARA 很可能会使用比人类大脑在发展过程中所用的“计算量”更多的算力进行训练，这表明在训练 ASARA 以匹配人类学习方面仍有显著的效率提升空间。

**因此，尽管目前 r 可能大于 1，但最终会下降——在基本限制下，r 将需要降到 0。**这意味着无论投入多少研发，进展都将停止。但目前尚不清楚随着我们接近极限，r 将如何随时间下降。尽管如此，离这些限制越远，r 仍然大于 1 的可能性越大，发生 SIE 的机会也越大。

还可以注意到，若我们**越早达到 ASARA，因为 r 在那时未必已经降到 1，所以越可能发生 SIE。因此，较短的时间表可能会增加 SIE 的可能性。**

**06.**

**软件智能爆炸的**

**瓶颈和****解决方案**

**• 硬件制约**

上述分析都发生在算力不首先的背景下。也许存在一种可能是，在实现全自动的 Agent 系统的过程中，模型研发中的作用并不像想象的那样重要，关键的推动因素可能是算力基础设置的增加。毕竟，硬件可以用于运行模型训练，更多的硬件意味着更多或更大规模的模型训练。如果没有算力的持续扩展，也许大部分软件层的进展也会停滞。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

但软件效率的提升会带来模型训练的算力成本降低。如果算法改进使得在笔记本电脑上能够训练一个 GPT-3 规模的 AI 系统，那么每个拥有笔记本电脑的研究人员都可以运行自己 GPT-3 规模的实验。即使硬件不变，随着时间的推移，也有可能进行更多实验，这种效应可能足以维持快速的效率进展。

如果硬件限制确实成为软件发展的瓶颈，LLM 公司也可以通过运行更小、更便宜的实验，并将结论外推到更大规模的系统，来弥补这一限制。**之所以认为可以从更小的实验中进行显著外推，是因为 LLM 和其他前沿 AI 系统通常在以下两者之间存在非常明确的关系：用于训练系统的算力与系统的最终表现。**

例如，OpenAI 发现 GPT-4 的某些特性可以从之前少于 GPT-4 算力的训练中高度预测。如果执行软件研发的 ASARA 同样可以通过运行更小的 AI 实验来推测大规模训练的结果，那可能完全可以跳过大规模的训练。

ASARA 还可能通过多种途径显著提高模型训练的质量、效率和信息价值，比如，在运行实验之前就消除错误和微妙的实验设计缺陷，更加重视有前景的研究方向，从第一性原理进行更有价值的实验设计，深入分析每个实验的结果，将每个实验的结果与所有其他实验结果和证据进行综合，持续监控实验，并在获得重要结果后立即终止实验等。

**因此，AI 软件研发可能会转向那些本身就不依赖大规模实验的方向，比如微调、构建和 prompt 等，这些方法的实验可能仍会带来实质性的进展。**

甚至有可能，在强硬件限制和 ASARA 迅速拓展的背景下，AI 领域将从依赖大计算量的机器学习转向新的范式，这种范式可能更少依赖实验，甚至完全放弃训练，转向显式设计所需的 AI 系统，类似于 GOFAI（Good Old-Fashioned Artificial Intelligence，泛指用最原始的人工智能的逻辑方法解决小领域的问题）。

换一个角度，即使来自硬件的实验限制不足以使软件进展停滞不前，但有这些限制仍然可能比没有限制的情况下的进展要慢。上述解决方法可能仍然能够让 ASARA 在硬件限制下取得实质性的进展。

此外，在 SIE 中，边际回报的递减可能比历史数据中更陡峭。历史上，计算资源在增长，因此研究人员可以发明只在新的计算规模下有效的算法。但在 SIE 中，这种情况将无法发生，因为硬件保持不变，限制在固定计算规模下的算法可能会使边际回报递减变得更加陡峭。

**考虑到硬件的限制，Forethought 将 r 的最佳猜测估计值减少到 0.5-2，如果 AI 发展需要大规模实验，则估计值较低，如果 prompt 和构建等改进能够带来显著进展，则估计值较高。**

**•** **训练新 AI 系统的所需时间较长**

在当前的 AI 范式中，最强大的系统通常分为两个阶段进行训练：一个较长的“预训练 pre-training”阶段和一个较短的“微调 fine-tuning”阶段。

对于最强大的系统，pre-training 确实可能很长，需要持续几个月使用大型数据中心。近期 AI 的进展稍微改变了这个局面，因为它们暗示 fine-tuning 在开发能力方面比传统认知上的更加重要和持久，尽管目前 fine-tuning 仍然远短于 pre-training。

无论如何，正是这些长时间的训练，无论是通过 pre-training、越来越广泛的 fine-tuning，还是其他尚未开发的训练阶段，都可能成为 AI 进展的瓶颈，进而减缓 SIE 的发展。

**如果每一代 ASARA 只能创造出比它们自己稍微更聪明一点的系统，并且每一代都需要经过漫长的训练过程，那么这可能会极大地抑制进展。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

但是，也有几个原因表明，这类模型训练可能不会成为进展的瓶颈。进展可能通过其他方法得以维持，例如，专注于 prompt、较短的 fine-tuning。也可能开发出其他方法，使得能够在不重新训练的情况下继续发展，例如通过新颖的方式修改已有系统的部分功能。

此外，如前文所述，AI 范式的转变可能会更清晰地绕过这些障碍。如果训练新的模型成为实现 ASARA 的瓶颈，那么这种瓶颈将为该领域寻找其他替代方法提供巨大的激励。即便从零开始训练新系统仍然是必要的，仍然可以合理地认为 SIE 可能发生，因为训练新系统的速度有可能比现在更快。算法改进可能使得训练新系统的效率更高，从而每次训练所需的时间减少。

如果 ASARA 的训练时间最初为 2 个月，然后通过算法改进提高了 30 倍的效率，那么这些效率的提升不仅可以用来训练更强大的系统，还可以用来训练既更强大又计算负担较轻的系统。

只要每次训练的时间能比上一次稍微快一些，训练时间最终可能趋近于零，AI 进展也可能变得极为快速。因此，训练新 AI 系统的瓶颈可能会延缓而不是阻止 SIE 的发生。

值得注意的是，训练 AI 系统所需的时间并不是当前 AI 范式固有的不可改变的属性，而是各种相互竞争的因素之间的妥协——包括尽早完成训练的价值、算力的价格、算力的价格随时间变化的预期等。SIE 发生时，平衡将大幅倾向于尽早完成训练（因为进展非常迅速，系统可能会很快过时），这可能会导致训练时间大大缩短。

训练新 AI 系统的所需时间仍然是一个悬而未决的问题。尽管上面提到的可能性存在，但也有可能所有不涉及长时间训练的进展方法最终要么完全失败，要么无法维持足够的进展，因此，要保持 r>1，保持随着研发投入的增加，软件性能需要能不断翻倍（性能翻倍需要更多的训练时间），可能会妨碍后续的训练时间变得越来越短。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

排版：杨乐乐

延伸阅读

为什么 AI Agent 需要自己的浏览器？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Exa：给 AI Agent 的 “Bing API”

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Cartesia: 3 个月融资 9100 万美元，从 Transformer 到 Mamba 重塑语音 AI

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

大模型非共识下，什么是 AGI 的主线与主峰？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Physical Intelligence 创始人：人形机器人被高估了

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)