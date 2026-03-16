---
url: https://mp.weixin.qq.com/s/7ftV2hK9HgpS7d2LhVrgAw
title: "SemiAnalysis 全文：解构微软的AI战略——从错失OpenAI合约到重构AI算力经济体系｜Jinqiu Select"
description: "“AI算力经济的核心不在规模，而在资本效率。“"
author: "锦秋编辑部"
captured_at: "2026-03-09T03:28:33.991Z"
---

# SemiAnalysis 全文：解构微软的AI战略——从错失OpenAI合约到重构AI算力经济体系｜Jinqiu Select

「Jinqiu Select」

跨越语言与时差，传递科技圈最值得被听到的声音。

过去一个季度，微软从错失OpenAI合约，到加码自研芯片、加快Azure扩产，其AI基础设施战略正在经历剧烈转弯：先是稳健拓展，随后暂停扩张，如今再度加速。
SemiAnalysis 最近发布的长文《Microsoft's AI Strategy Deconstructed - From Energy to Tokens》，系统梳理了微软在AI算力经济体系（AI token-based economic stack）中的布局：从算力芯片、基础设施、平台层到模型应用层，同时揭示了这场巨头转向背后的深层逻辑。
微软的教训说明：“AI算力经济的核心不在规模，而在**资本效率**。“

谁能用更少的GPU资本，创造更多token产出、更高复用率和更优现金流？

——谁就赢

锦秋基金认为，这篇报道不仅帮助创业者看清企业如何重新定义“算力供给模式”，理解资本流向；同时，它也为创业者提供了明确的启示：

-   对芯片和基础设施创业者：不必与英伟达拼性能，但可以与资本拼效率；

-   对模型和应用层创业者：应大胆往前跑，Token成本以后会更不是问题。

以下是编译全文。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/SYm5F7no2RsnFHialQQkjoqUk2EceMdtspXfZafnnXr2qkm9bogmzVPRWMYUY7FGrl0q65FBgskLMyMCNYotiaiaw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

微软在2023年和2024年处于AI领域的领先地位，但一年前他们大幅改变了方向，他们大幅暂停了数据中心的建设，并放缓了对OpenAI的投入。

2025年的微软新故事：OpenAI逐渐减少对微软的依赖，实现多元化发展，甲骨文、CoreWeave、Nscale、SB能源、亚马逊和谷歌都直接与OpenAI签署了大型计算合同。

这似乎是个严峻的局面。

如今，微软在AI领域的投资卷土重来，这家AI巨头对加速计算的需求从未如此之高。雷德蒙德巨头已经意识到自己走错了路，并大幅调整了方向。随着新宣布的OpenAI交易，Azure的增长将***加速***，正如我们的Tokenomics模型所预测的那样，在未来几个季度。

微软在AI代币经济栈的每一个环节都有参与，正见证着加速增长，我们预计这一趋势将在未来几个季度和几年持续下去。

> 注：AI代币经济栈（AI token-based economic stack），指 AI 基础设施到应用层之间，围绕“token”为计价与算力单位的完整经济层级。

该公司正在积极寻找短期产能，并抓住一切可获取的资源。自建、租赁、Neocloud、偏远地区——所有选项都在考虑范围内，以加速短期产能增长。

在硬件方面，微软甚至可以访问**OpenAI****的定制芯片****IP****，**这是目前正在开发的最令人兴奋的定制芯片ASIC。鉴于OpenAI的ASIC开发轨迹看起来比微软Maia要好得多，微软最终可能会使用该芯片来服务OpenAI模型。这种动态反映了微软在OpenAI模型方面的情况。虽然他们可以访问OpenAI模型，但他们仍在尝试用微软AI训练自己的基础模型。我们认为他们正试图成为一个真正的垂直整合的AI巨头，消除大部分第三方毛利率，并以比同行更低的成本提供更多的智能。

在本报告中，我们将深入探讨微软AI业务的各个方面。我们首先回顾与OpenAI的合作历史，包括2023 - 2024年微软数据中心投资的历史性增长，以及其OpenAI训练集群的惊人规模——从数十兆瓦到吉瓦。然后，我们分析“大暂停”以及数据中心市场的惊人回归。这在很大程度上是由于OpenAI所有权结构的大幅简化，以及微软专注于通过无状态API将模型能力转化为产品用例（和收入）所需的基础设施服务。

然后，我们分析微软在AI代币经济栈中的定位的各个部分：

-   应用程序

-   大语言模型

-   平台即服务

-   基础设施即服务

-   芯片

-   系统架构

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis，sales@semianalysis.com

在每一部分中，我们将深入探讨微软的产品组合、竞争定位和前景。对微软来说并非全是好消息，因为这家软件巨头面临着一系列新进入者和挑战者，它们正挑战微软占据主导地位的生产力套件和AI计算平台。

ChatGPT于2022年11月发布，改变了世界。微软是首个对“ChatGPT时刻”做出反应的超大规模云服务提供商，而且是以一种惊人的方式做出反应。早在2019年，微软就已向OpenAI投资10亿美元，而在2023年1月，他们将投资额增加了10倍。与此同时，他们开展了有史以来最激进的数据中心建设——这主要是由其关键AI合作伙伴推动的。

下图展示了数据中心预租赁活动，这是衡量容量增长和资本支出的最佳领先指标之一。从2023年第一季度到2024年第二季度，微软的预租赁活动规模远超其他超大规模运营商*的总和*。在2023年第三季度，仅微软一家的租赁量就几乎与*2022年整个北美市场全年的租赁量*相当。

而数据中心租赁只是其中一部分。我们的逐栋建筑数据中心行业模型凸显了2024年和2025年期间自建容量兆瓦数前所未有的增长。此外，他们还与Coreweave和甲骨文签订了数十亿美元的合同，以获取额外容量。

这次建设中最具标志性的项目可能就是“Fairwater”计划。在2023 - 2024年，微软规划并同时建造了**地球上最大的两个数据中心**。

让我们简要回顾一下，以了解微软2023 - 2024年建设的规模。

***微软的数据集群帝国是如何打造的***

-   第一个大型训练集群建在爱荷华州。

GPT 3.5就是在这里训练的。我们认为这里容纳了**约25000个A100芯片**。虽然下面展示的园区规模相当大，但我们认为OpenAI仅使用了巴拉德大楼的两个数据大厅，即约19兆瓦。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   第二个主要集群建在亚利桑那州。

随着时间的推移，它逐栋建筑地进行扩建，第一座H100建筑于2023年完工，2024年在另一处设施中建成H200建筑，2025年还将有两座容纳GB200的新数据中心落成。总体而言，我们预计这四栋建筑中共有约13万个GPU。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   微软为OpenAI打造的下一代集群名为Fairwater，规模要大得多。

每个“Fairwater”由两座建筑组成——一座48兆瓦的标准CPU及存储设施，以及一座超密集GPU建筑。后者有两层，总面积约80万平方英尺，功率约300兆瓦，即相当于超过20万户美国家庭的用电量。这意味着每座建筑拥有超过15万个GB200 GPU。**下面展示的是完全服务于****OpenAI****的威斯康星州设施。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   在佐治亚州，QTS为微软建造了一座“姊妹”设施，同样是为OpenAI建造的。

虽然冷却系统不同，但GPU建筑的功率也约为300兆瓦。下图展示了该设施的规模——世界上没有其他建筑为冷却目的配备如此多的风冷式冷水机组！现场变电站的规模也令人印象深刻。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis数据中心模型

不仅每栋建筑是地球上最大的，而且它们还位于更大的园区内。

-   在亚特兰大，第二座费尔沃特已经在紧锣密鼓地建设中。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis数据中心模型

-   在威斯康星州，而故事远不止于此，因为微软正在筹备规模更大的第三阶段建设。

我们认为微软设计了两座**\>600兆瓦的独立建筑**，与标准的约300兆瓦费尔沃特数据中心相比，每个设施的CPU/存储和柴油发电机数量是其两倍。我们在下面展示了与这些600兆瓦建筑相关的场地规划。如果按时建成，这些将成为世界上最大的独立数据中心。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis数据中心模型、本地披露

全面建成后，这里将成为全球最大的园区之一，拥有超过2GW的IT容量。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis数据中心模型

锦上添花的是，微软计划让所有这些主要的AI区域通过超高速AI广域网（WAN）连接起来，速度超过300Tb/s，且具备扩展到10Pb/s以上的能力。我们在一年多前的文章 “**多数据中心训练：OpenAI击败谷歌基础设施的宏伟计划****” 中就提到过这一点。**

下面我们展示一个假设的5GW分布式集群的网络设计表示，我们将在报告后面基于我们的AI网络模型讨论Fairwater网络架构的各个方面。

***激流勇退的背后原因***

**在全力推进之后，微软突然决定以一种惊人的方式踩下刹车。**

从数据中心预租赁总余额来看，仅微软一家在高峰期就占租赁合约的60%以上！但在2024年Q2（按日历计算）之后，新的租赁活动陷入停滞，而其他超大规模云服务提供商的租赁活动则显著增加。目前，微软在超大规模云服务提供商预租赁总容量中的占比已降至25%以下。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis数据中心模型

当时，微软还退出了多个地点的多吉瓦非约束性意向书，例如：

-   美国主要市场，如凤凰城和芝加哥。

-   主要欧洲市场，包括UK和北欧等。

-   在世界其他地区，微软的暂停举措影响到了澳大利亚、日本、印度以及拉丁美洲。

这些客户流向了其他主要竞争对手，如甲骨文、Meta、CoreWeave、谷歌、亚马逊等。由于态度冷淡且对AI缺乏信心，微软永远失去了很大一部分AI基础设施市场份额。

此外，微软还大幅放缓了其自建项目的进度。我们在下面展示了一些图片，列出了约950兆瓦的“冻结”IT容量。这还不包括弗吉尼亚州、佐治亚州、亚利桑那州的多个其他数据中心，以及国际上的数据中心。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在同一时间框架内，其他参与者的主要数据中心从破土动工到开始运行工作负载。微软总共暂停了超过3.5GW的容量建设，这些容量原本计划在2028年前建成。

为了理解“大暂停”的原因和后果，让我们深入探究微软AI产品组合的各个部分。我们分析不同层级利润率的首选框架是“AI代币工厂经济栈”：

-   从芯片到代币，众多供应商都参与到了AI基础设施的建设中。

-   目前，规模最大的利润率堆栈当然是在芯片层面，由英伟达75%的GPM驱动

-   对于以下四个层面的最终状态利润率情况，仍存在激烈的争论：

-   应用层（例如ChatGPT、Microsoft Copilot、Claude Code…）

-   模型层（例如Claude 4.5 Sonnet、GPT5-Pro、DeepSeek R1等）

-   基础设施即服务（IaaS）层（例如，Coreweave向Meta出租裸金属GPU集群，甲骨文向OpenAI出租GPU，Nebius在多租户集群中向初创企业出租SLURM和K8s……）

-   平台即服务（PaaS）层（例如，AWS通过Bedrock向一家财富500强企业出售令牌，Nebius通过SLURM和K8s向一家初创公司出售部分GPU集群……）

按照当前的定价，我们看到领先的模型制造商在其直接API业务上的利润率超过60%

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis

在构建大规模裸金属GPU/XPU集群业务中取得成功的企业，已经掌握了构建大规模基础设施的艺术。这是多种要素的结合，包括执行速度、对市场和最终用户需求的理解、选址以及融资等。

> 注，裸金属：不经过虚拟化层、直接运行在物理服务器上的计算资源

我们对甲骨文的深度研究指出了他们为赢得市场而做出的重大战略转变。除了科技巨头之外，Coreweave是一个没有初始规模的参与者通过完美执行上述标准而赢得市场的案例研究。现在让我们来看看微软的执行情况。

要评估微软在裸机方面的努力，深入研究Fairwater项目是很有帮助的。

2024年初，有关微软为OpenAI投入1000亿美元的“星际之门”项目的传言甚嚣尘上。我们认为他们计划将集群部署在威斯康星州的数据中心园区。如前所述，路线图本会使该园区的容量超过2GW。

当然，第一份价值1000亿美元的星际之门合同最终花落甲骨文公司和德克萨斯州阿比林市。

**微软在这一阶段的缓慢执行力，是导致“激流勇退”背后的关键原因**。

破土动工两年多后，第一阶段仍未投入运营。相比之下，甲骨文公司于2024年5月在德克萨斯州阿比林市的数据中心破土动工，并于9月开始运营。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

我们还认为微软对1.5GW的扩建规划欠佳。从输电角度来看，满负荷产能预计至少要到2027年年中才能交付，**也就是在甲骨文阿比林集群突破1GW大关一年之后**。微软无法跟上OpenAI尽快扩大规模的要求，这表明其对市场存在误解。这家AI实验室别无选择，只能寻找其他合作伙伴来满足其短期内对计算能力的巨大需求。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis数据中心模型

正如我们今天所知，甲骨文已成为OpenAI的主要GPU合作伙伴。在过去十二个月里，他们签订了价值超过4200亿美元的合同，转化为约1500亿美元的毛利润。

假设期限为典型的5年，300亿美元的年度毛利润将使微软1940亿美元的年度毛利润（2025财年）增长超过18%。公平地说，失去OpenAI合同**不仅仅是执行问题**。在某种程度上，这也是一个有意识的决定。从微软的角度来看，拿下所有OpenAI合同会降低其Azure业务的质量，原因如下：

-   OpenAI将在几年内占据Azure近50%的收入。

-   利润率和资本回报率情况远不如Azure的历史云业务情况有吸引力。

与微软的整体业务相比，甲骨文的AI投资回报率（ROIC）确实较低，目前为20%，而微软整体为35-40%。然而，我们发现，一旦剔除将于2030-2032年间结束的OpenAI的营收分成，微软自身的AI投资回报率并不比甲骨文高多少。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis代币经济学模型

然而，微软似乎忘记了自己最近的历史教训，因为他们从非常繁重的裸机工作负载AI收入构成转向了更多基于API和令牌工厂的商业模式，从而使其投资资本回报率（ROIC）持续提升。他们可能刚刚让竞争对手有机会资助自己进入AI工厂业务！

微软暂停业务带来的一个关键教训是，他们严重低估了来自其他参与者（如Meta）的XPU云需求规模。我们目前正在见证他们误判后带来的影响。其他参与者预订的RPO比微软多得多。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis代币经济学模型

***重回市场后的“尴尬”境遇***

微软现在已稳固地回归市场，但他们在短期内扩充产能的选择越来越少。他们被迫选择了最糟糕的方案：从Neoclouds租赁GPU，再转售给第三方，无论是以裸机形式还是通过Foundry以代币形式。我们将在下面讨论Foundry。

**当然，租赁裸机再转售裸机的业务将产生****远低于平常****的****Azure****利润率。**

> 注：Foundry，算力/模型的代币化与再分配平台

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis代币经济学模型

微软曾回避自建数据中心，结果在意识到自己搞砸后，只能向新云服务商支付差价。

在今年3月发布的ClusterMAX 1.0中，我们讨论了Azure如何在网络性能、安全性和最新GPU的可用性方面处于领先地位，并且已经占据了OpenAI计算建设的大部分份额。这使他们在我们的排名中明确处于黄金层，紧随CoreWeave之后，与Nebius、Oracle和Crusoe等公司相邻。然而，到ClusterMAX 2.0在11月初发布时，针对AI工作负载的新CycleCloud和AKS功能的开发速度已经明显停滞。

在我们与140多位来自OpenAI、Meta、Snowflake和Cursor等规模化AI公司，以及Periodic Labs、AdaptiveML、Jua、Nous Research、DatologyAI和Cartesia等初创公司的计算资源买家的交流中，很明显**Azure****在托管集群或按需****虚拟机****方面并非重要参与者**。Azure大规模集群的GPU算力似乎直接流向了OpenAI，剩余的则被《财富》500强中传统企业的个体开发者瓜分。这些热衷于内部RAG聊天机器人开发的公司通常会签订企业协议，专门从Azure购买所有的IaaS。

在我们的实际测试中，Azure不销售用于AI的托管Slurm或Kubernetes集群的原因很明显：**我们发现CycleCloud Slurm集群在易用性、监控、可靠性和健康检查方面存在显著差距**。Azure在一次性出租整个数据中心时为OpenAI提供的大规模裸机体验，与CoreWeave、Nebius或Fluidstack等供应商为其终端用户提供的体验大不相同。

行业内典型的GPU计算采购方仍在寻求规模为64至8000个GPU的H100、H200、B200或B300 HGX服务器。采购方寻求GB200、GB300或AMD产品的情况则少得多。不过，微软已投入大量时间和精力，为其最大的客户（即OpenAI）采用AMD GPU和GB200/GB300 NVL72机架级系统。这可以用工程师薪资的OPEX或GPU采购及新设施的CAPEX来衡量。

另一种看待这个问题的方式是通过开源社区。

根据 Hugging Face （任何公司发布和下载开源模型的事实上的平台）的数据，与亚马逊相比，与微软相关的知识产权（IP）每日模型下载量少5倍，与谷歌相比少3倍。

微软赶走了OpenAI业务，但这并不意味着他们正在抢占企业市场或长尾市场。在这一指标上，他们远远落后于其他超大规模云服务提供商。

所有这一切的结果很明显：积极寻求算力的AI公司正在另寻他处。这可能涵盖从价值约100万美元的1年期64-GPU合同，一直到价值超过5亿美元的3年期8000-GPU合同。我们看到3月份购买了256块H100的初创公司在11月份寻求9000块GB300 NVL72。目前，Azure错失了所有这些增长机会。

为了满足这一客户群体的需求，我们认为Azure必须对其AI领域的CycleCloud和AKS产品进行重新设计，简化当前的集群部署和监控体验。他们需要构建健康检查功能，默认将其部署到集群中，并主动从硬件故障中恢复。而且他们需要组建充满专业人员的GTM和支持团队，将这些集付给最终用户。我们在ClusterMAX 2.0中提到，由于Azure在A轮融资的初创企业到AI独角兽企业中的用户体验不佳，有被降级为银牌的风险。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis

***打造全球“可互换”机群***

事已至此，但Azure显然具备成功的基础。他们在全球拥有70个区域和400多个数据中心。他们运营着有史以来最大的SaaS业务，拥有向全球最大型组织销售的经验：从面向US情报机构的“Azure Government Secret”到面向中国消费者的Windows个人电脑。

Azure战略的关键在于通过广泛的地理覆盖，让AI更贴近企业客户。这是**对AI工作负载未来形态的**方向性押注：

-   当今最大的推理用例，即ChatGPT和代码编写智能体，对延迟并不敏感，并且随着时间跨度的不断增加，这种敏感性会越来越低。在很大程度上，它们也不与敏感的企业数据交互。因此，**延迟和数据本地性并不重要**——关键在于尽快提升能力，以便向全球销售更多的令牌。

-   未来，企业用例可能会成为增长的一大来源。它们必须遵守高安全性、数据本地化法律，以及大型企业青睐的典型环境和限制条件。它们还将与非AI工作负载共同处理，例如特定Azure区域中的Cosmos DB存储。缺点是，由于电力限制影响了世界上大多数主要城市，数据中心选址过程更加复杂。相对于在电力过剩的偏远地区建设的其他项目，它们的发展速度不会那么快。

构建并利用全球布局是微软打造“可互换”机群这一主旨的关键。

该基础设施战略与OpenAI等领先AI实验室的战略大不相同。鉴于最耗费算力的工作负载需要几分钟才能响应（例如深度研究、推理模型），增加几毫秒的网络延迟对它们来说无关紧要。

随着AI任务的时间跨度延长，与用户的局部性关联越来越小。

数据中心可以设置在任何可行的地方，并为全球流量提供服务。这一趋势还受到以下事实的推动：训练后工作负载的计算需求正在迅速增加，这些工作负载同样对延迟不敏感，并且不需要大量的集中式计算。

如果你要剖析这个可互换的机队，就会发现一个重要的考量因素，一个最近受到广泛关注的因素，即：**折旧。**

因对市场一贯悲观而颇具争议的迈克尔·伯里（Michael Burry）最近声称，所有超大规模企业（Meta、谷歌、甲骨文、微软、亚马逊）都在通过延长其IT资产的使用寿命来人为提高收益。这种做法已将“使用寿命”从2020年的3 - 5年延长到了如今的5 - 6年。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：迈克尔·J·伯里在X上的发言

伯里博士的观点基于一个假设，即NVIDIA的产品周期现在为2 - 3年，这远低于资产的使用寿命。我们认为这是该论点的致命缺陷。新的会计处理方式虽然短期内对公司有益，但同样基于数据中心的实际运营经验。

早在2020年，当微软、Meta和谷歌将使用寿命从3年延长至4年时，我们还处于公元前2年（ChatGPT之前）。如今，在公元3年（ChatGPT大发布之后），使用寿命的延长已被证明对渴望CAPEX的超大规模企业有益。2020年开始在IT设备中发生变化并持续到2025年的是什么？答案是可靠性和激励措施。

戴尔、超微、惠普、联想和思科等服务器原始设备制造商（OEM）长期以来一直销售标准保修期为3至5年的服务器。当然，5年保修期的价格更高，但也有许多6年和7年的延长保修选项。价格自然会上涨，但供应商只需储备足够的备件，就能对老化的节点进行维修。与此同时，思科、Arista、Aruba和瞻博网络等网络设备供应商已经在其交换机上尝试提供终身保修。存储供应商也提供类似服务——只需支付年度支持合同费用，他们就会不断更换老化的驱动器。这就像汽车一样：高端市场可能每两年就租赁并升级一次奔驰，而其他人则以汽油和保险的价格继续驾驶他们20年前的旧车。

当我们审视全球最大的HPC集群和超级计算机时，这一点就得到了证明。这些前沿系统运行着市场上最大、最强大、最先进（有时也是最高效）的处理器。超级计算中心是最早采用液冷技术的，并且有围绕系统构建数据中心的经验，而不是将系统适配到现有的数据中心中。

位于橡树岭国家实验室的IBM Summit超级计算机在很长一段时间内都是全球Top500榜单上运算速度最快的超级计算机。它于2018年6月投入使用，并在连续运行6.5年后，于2024年11月退役。Summit采用了2016年推出的IBM Power9处理器，其采购早在2014年就已完成。

富岳于2020年在日本理化学研究所安装，目前仍在运行，在全球超算500强榜单中排名第7。塞拉于2018年在劳伦斯利弗莫尔国家实验室安装，目前仍在运行，排名第20。神威太湖之光于2016年在中国无锡国家超级计算中心安装，目前仍在运行，排名第21。像埃尔卡皮坦、前沿和极光（分别在榜单中排名第1、第2和第3）这样的百亿亿次超算系统于2021年至2025年期间投入使用，预计将运行至2027年至2032年。

最后，**搭载14400个H100的Eagle - Microsoft NDv5**于2023年安装，位列第5。我们预计该系统将得到高度利用，并将在未来几年持续运行。

看看当前的云服务提供商，我们可以在AWS上找到配备8块V100 GPU的p3.16xlarge实例在售。我们还可以通过Shadeform、Prime Intellect和Runpod等市场，从DataCrunch、Paperspace和Lambda Labs等底层提供商那里找到类似的实例。

V100于2017年5月发布，2017年秋季开始批量出货，NVIDIA的最终产品出货于2022年1月完成。换句话说，从推出新GPU起，NVIDIA供应备件超过5年。超大规模数据中心运营商和原始设备制造商有足够的时间储备备件，并使实例一直运行到今天——距离那些V100 GPU开始出货已经整整8年。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在我们的AWS控制台中寻找一些待售的V100

当然，如今的V100在单纯的每兆瓦营收基础上并不是一项出色的业务。以至于我们知道超大规模数据中心运营商正在从其旧数据中心中拆除V100、A100，甚至更旧的H100 GPU，以便为最新、最强大的GPU腾出空间。关键不在于他们这样做是因为GPU磨损老化而报废。相反，由于电力和空间限制，他们正在拆除创收资产，转而采用创收更高的资产。

优化GPU云经济性的关键在于***最大化其经济寿命***。我们的AI云TCO模型提供了一个有用的框架。分析H100集群的TCO，我们发现扣除资本成本后，每GPU每小时仍有0.30 - 0.40美元的运营成本。问题在于，5年后，GPU是否仍能以高于该费率的水平实现盈利。

该运营成本必须与每块GPU所产生的收入相匹配。自然地，随着英伟达推出能大幅提高每美元吞吐量和每瓦吞吐量的新芯片，GPU的定价权迅速减弱。我们的AI云TCO模式，受到全球大多数最大的GPU买家及其金融赞助商的信赖，除了提供详细的集群物料清单分析外，还提供所有英伟达、AMD、TPUv7和v8以及Trainium2和3 SKU的长期租赁定价预测。

我们的历史命中率已被证明极为准确！但从像Azure这样的公司的角度来看，目标是相对于广泛市场拥有更高的定价权。这仍不确定，但可能会以多种方式呈现：

-   通过利用其企业关系、PaaS层和垂直整合（应用程序、模型、代币等），Azure或许能够从使用了6年的GPU中提取足够的价值，从而避免过早退役。

-   另一条与企业业务相关的路径是，在加速计算的同时向上销售高利润率的服务（例如非AI服务，如数据库）。即使使用了6年的GPU本身无法独立盈利，但如果它们恰好是促成高利润率服务向上销售的原因，那么继续运营这些GPU可能是合理的。

在我们看来，这就是为什么Azure的“可互换机队”战略可能行得通，并使其能够实现比其他竞争对手更高的结构性投资资本回报率（ROIC）。主要的不确定性仍然在于企业采用的规模，以及Azure是否能够向上销售更高价值的服务。

未来会怎样？Vera Rubin是否会兑现性能承诺，并像Burry博士所说的那样，促使超大规模数据中心运营商在GPU仅服役2 - 3年后就淘汰那些性能良好、能产生收益的GPU？还是我们会看到H100定价数据的底部在未来保持强劲？ 这些问题仍有待解答，但我们的TCO模型提供了我们的最佳估算。通过我们对GPU云（ClusterMAX）的专业测试以及每日通过推理MAX进行的基准测试，我们旨在提供市场上最优质的见解。我们免费且开源的推理MAX平台展示了系统级创新（如英伟达的GB200 BVL72）如何在某些用例和配置下，相较于更传统的基于HGX的GPU，实现数量级的提升。

Azure Foundry是微软的“Token即服务”业务，提供多种模型，这些模型既被M365 Copilot和Github Copilot等内部服务（1P令牌）使用，也被希望通过推理端点使用模型的外部客户（3P令牌）使用。Azure Foundry以类似于OpenAI API的方式进入市场，在个人和企业用例方面展开竞争。由于Azure拥有OpenAI模型权重的IP权利，它也可以独立做出定价决策。

目前，大多数GPT API令牌都是直接通过OpenAI处理的，但我们预计，未来铸造厂将成为微软的主要增长动力，并夺回部分市场份额。对微软来说重要的是，Azure在**所有API推理计算**中拥有**100%的份额**，无论这些计算是通过OpenAI API还是Azure铸造厂提供的，这一情况将持续到2032年。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis代币经济学模型

然而，我们认为向企业销售代币的业务仍处于起步阶段。Alphabet的桑达尔·皮查伊在2025年Q3财报电话会议上进行了有趣的披露，证实了我们的立场：

> 在过去12个月里，近150家谷歌云客户使用我们的模型为广泛的应用程序各自处理了约1万亿个标记。

本披露表明，向这150家企业销售的双子座代币占GCP业务的比例不到0.5%。

将代币转化为收入远比看起来复杂得多。我们经常看到分析师在投入产出比等方面犯下重大错误，未能考虑缓存代币，或错误计算定价。

在代码辅助的应用层，微软凭借GitHub Copilot占据了绝对主导地位。微软拥有首个内联代码模型，现在通常被称为“Tab”模型，并且由于其独家IP访问权，很早就将GPT-4与Copilot进行了集成。

***Azure的AI业务分析***

从远处看，微软的堡垒似乎坚不可摧。他们拥有行业标准工具VS Code和GitHub，独家获得OpenAI模型IP用于产品开发，并且拥有庞大的企业客户群可供销售。

**然而，他们低估了一系列****初创公司****的崛起。**这些公司复刻了VS Code，以在模型和代码库之间构建更紧密、更完善的集成，这使得这些挑战者能够集体超越Copilot。一个关键的推动因素是初创公司对Anthropic模型的使用。

微软在2025年初勉强将Anthropic纳入GitHub Copilot的服务范围，这对其利润率造成了巨大损失。GitHub Copilot从几乎100%使用第一方代币，变成不得不从Anthropic购买大量代币，而Anthropic的相关毛利率为50-60%。

实验室也自行开发产品。用户只能使用一套模型，但这些模型是在生产中使用的工具和环境上进行训练的。这带来了一种优化的体验，正如Codex和Claude Code的收入增长所显示的那样，这种体验非常受欢迎。

此后，微软加大了对其模型超市生态系统的押注，最近推出了 Agent HQ，该平台接入了包括谷歌和 xAI 在内的多个实验室的智能体。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：GitHub

由于他们获取OpenAI模型权重的时间线仅延长至2032年，该公司需要为其当前利润率最高的OpenAI模型产品制定一个备用计划。

微软已发布了涵盖文本、图像和语音的3个MAI模型。文本模型MAI-1目前在LMArena上的排名约为38，但尚未通过聊天或API向公众开放。该模型是在15000个H100上训练的大型MoE，下一个模型将是更大的多模态大语言模型。

另外两个分别是图像和语音模型。图像模型在LM Arena中仍然是排名前十的模型，并且两者都可在Copilot中使用。

对微软来说，后两种模型代表了一种用例，即模型可以以低成本提供且质量不错。它们远不足以挑战最先进的模型，但我们相信该公司正在悄然准备加大内部训练投入，在未来几年内将年化计算支出扩大到接近**160亿美元**。

Microsoft Copilot是一个综合性的平台，它不仅仅包含GitHub Copilot。还有适用于销售、财务、服务、安全等领域的Copilot。这个平台的月活跃用户数已经超过1亿，将成为推动整体AI应用的重要驱动力。

构建 Office 365 Copilot 的最新成果体现在 Office Agent 中，下面我们将深入探讨 Excel 相关的内容。这些代理的总体目标是在 Microsoft 生态系统中以自主、实用且对用户有用的方式采取行动。

访问OpenAI的模型、权重和代码库，使微软能够从OpenAI模型的原始思维链中进行提炼。提炼比训练后微调小模型更有效，这意味着微软将能够在不产生大量计算成本的情况下获得显著的能力。

对OpenAI IP的访问也使微软能够利用其有权访问的数据对OpenAI模型进行微调，这些数据可能比在Office套件之上构建工具或环境的公司从外部获取的数据更具粒度或基础性：

> 我们绝对会在所有产品中最大限度地使用OpenAI模型。

Excel智能体是**OpenAI****推理模型之一**的后训练版本。微软声称这一成果优于前沿实验室。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：微软

在深入研究了Azure的AI业务之后，我们现在将注意力转向Azure的AI硬件堆栈的两个关键部分：

-   微软的实际芯片战略：他们将如何平衡NVIDIA、Maia、OpenAI、AMD等各方

-   Azure的网络架构及其对广泛供应商的影响

在定制硅芯片开发方面，微软在超大规模企业中排名垫底，甚至都没有试图迎头赶上。

微软在2023年末展示了其Maia 100加速器，成为四大超大规模云服务提供商中最新拥有AI加速器ASIC的公司。

正如第一代硅芯片所料，Maia 100并未大规模生产，也未部署用于生产工作负载。该芯片在生成式AI热潮之前就已设计架构，导致其在适用于推理的内存带宽方面存在不足。ASIC程序需要经过多代迭代，才能将有意义的计算从商用系统中卸载出来。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：SemiAnalysis加速器和HBM模型

下一代Maia 200的开发也因多个问题而陷入停滞，这些问题延长了设计过程，导致流片推迟到2024年底，大规模生产要到2025年才开始。Maia 200预计在2025年和2026年的总出货量，仅为微软超大规模计算同行（谷歌、亚马逊，甚至Meta）的一小部分。这是因为Maia 200芯片在内部被评估为失败，迫使微软重新规划其AI ASIC路线图。

微软甚至已经放弃了为Maia 200进行软件开发，转而将精力集中在未来的Maia迭代产品上。现在看来，2027年底将是微软最早能够部署与内部性能预测合理接近的2纳米Maia 300的时间。在这个时间框架内，竞争门槛被进一步提高，微软需要与英伟达的Vera Rubin竞争。鉴于到目前为止Maia团队的管理不善，我们也不相信他们在2027年能有出色表现。

从那时起，要迭代到接近英伟达每TCO性能的水平，还需要多代的努力，谷歌是唯一实现这一目标的ASIC设计商，它才刚刚开始交付其第7代TPU。萨蒂亚的观点是，内部芯片的意义在于实现紧密的硬件和软件协同设计，因此他们希望Maia在架构上能够训练和运行MAI模型。

这将把玛雅的命运与MAI的命运联系在一起，而这里的问题在于MAI是否（而非何时）能够开发出领先的模型。在此期间，等待MAI做出显著成果所花费的时间是宝贵的，这些时间本可以用于异步开发和迭代硬件。要求MAI做好准备只会给微软的硬件成功增加另一个不确定因素。正如亚马逊的故事所表明的，拥有自我发展的模型也并非定制芯片的必要“天赋权利”。

下面，我们看到在CoWoS订单方面，与谷歌、亚马逊和Meta相比，微软的AI芯片出货量要少得多。让我们来看看其他超大规模企业领先了多少。

获得OpenAI的IP可能仅仅意味着他们依赖OpenAI芯片。我们还认为，这将催生另一个博通定制ASIC客户。AI芯片市场的高端领域正迅速成为一场价值争夺的双雄竞争：NVIDIA对阵博通。

随着Maia与OpenAI、博通与NVIDIA的竞争成为一个悬而未决的问题，且微软开始使其芯片供应商多元化，我们认为他们也将在整个技术栈上向初创企业寻求帮助。

具体来说，微软的风险投资基金MI2最近发布了一张宣传活动的照片，活动中展示了Modular、Neurophos等初创公司。Modular是一家专注于编程框架和适用于除NVIDIA之外的多种加速器的推理技术的软件初创公司，而Neurophos则是一家致力于光学处理单元（OPU）的芯片初创公司（同样是在挑战NVIDIA）。如果成功，像这样的公司将代表挑战NVIDIA所需的一些关键力量：Modular MAX将取代vLLM和SG语言等推理运行时，而Neurophos则凭借其OPU芯片挑战NVIDIA，其OPU芯片还拥有“每皮焦耳1000倍的浮点运算能力”等优势。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

总体而言，与该领域的创业生态系统保持密切联系似乎是一个不错的策略，我们预计未来微软会有更多动作。

话虽如此，这些初创企业只是胜算极低的边缘赌注。

**谷歌**在超大规模企业中的芯片优势无与伦比，其第七代TPU可以说与英伟达的Blackwell不相上下。TPU为Gemini系列模型提供支持，这些模型的能力不断提升，在某些任务中接近每单位智能成本的帕累托最优边界。虽然Gemini 2.5 Pro不是编码领域的顶级模型，但它仍然相当强大，随着Gemini 3即将推出，谷歌将进一步提升实力。TPU不仅成功满足了搜索、广告和Deepmind等内部AI需求。谷歌现在正处于成为像英伟达那样的商用AI硬件公司的边缘。

外部客户明年将订购大量的TPU。Anthropic就是其中之一，它已与谷歌联合宣布，明年将至少订购100万个TPU。我们在这一消息宣布前近2个月就将其透露给了加速器模型的订阅者。总体而言，谷歌在超大规模AI芯片领域继续树立标杆。一方面，内部工作负载不再需要商用GPU；另一方面，多个成熟的客户也希望使用这种专用集成电路。

**亚马逊**正在大量交付其Trainium系列加速器，其中Anthropic是Trainium2的主要客户，几乎占据了整个Trainium2项目。正是亚马逊为Anthropic部署的Trainium2集群的增长，推动了AWS的大幅营收加速，这一点我们之前准确预测到了。

有趣的是，这意味着亚马逊的Trainium需求几乎全部来自外部。公平地说，这在很大程度上是因为在超大规模企业中，亚马逊对开发自己的前沿模型兴趣最小，满足于成为纯粹的基础设施提供商。这对微软的努力来说更具杀伤力：亚马逊已经成功转型为AI系统供应商。

他们将通过出租自己的AI硬件获得可观的毛利润，而且在没有太多内部工作负载来测试硬件和软件栈的情况下就能做到这一点。这与萨蒂亚的观点相悖，他认为“你最好有自己的模型”来支撑对专用集成电路（ASIC）研发的需求。相反，是Anthropic带来了模型，并且在设计整个系统方面发挥了重要作用，致力于让系统运行以降低TCO，并提供更多推理和训练后计算能力。

**Meta**正处于其ASIC路线图的重大转折点。Meta即将推出的MTIA “Athena” 将是Meta首款更接近现代GPU的芯片：一个与HBM共同封装的大型计算引擎。该芯片已从晶圆厂下线。明年，他们将推出下一代 “Iris”，随后不久还会推出 “Arke”，这是 “Iris” 的中期升级版本。Meta还有一个激进的路线图，目标是在硬件实现上超越英伟达。在不久的将来，还会有像用于扩展的CPO、混合键合以及逻辑上的DRAM等技术。

关键在于，除微软外，所有超大规模云服务提供商都将部署支持实际工作负载的专用集成电路（ASIC）。微软的芯片团队不仅要与超大规模云服务提供商竞争，真正的竞争对手是英伟达。祝他们好运。如果微软完全依赖出租英伟达的图形处理器（GPU），因为他们没有任何有外部需求的自有加速器，那么他们就只能与甲骨文、CoreWeave和Nebius等公司竞争。与此同时，谷歌和亚马逊有机会凭借其差异化的技术栈获得更高的利润率。

正如我们提到的，在部署AI基础设施时，加速器芯片是最大的单项成本。这是因为对于英伟达GPU这一黄金标准而言，成本伴随着英伟达高达75%及以上的巨额毛利率。这是英伟达成本的4倍加价。设计定制芯片的主要目标之一，就是让超大规模企业拥有自己的设计并直接找台积电制造，从而消除这一利润空间。

然而，现实情况是超大规模数据中心运营商并不具备端到端的芯片设计能力，因此需要依赖博通（Broadcom）、美满电子（Marvell）、联发科（MediaTek）、智原科技（Alchip）和广达（GUC）等设计合作伙伴。这些合作伙伴需要获取利润，但即便采用“一流”的博通产品，最终成本仍低于英伟达的收费。

下图展示了降低加速器芯片的毛利率如何降低成本，从而提高终端云服务提供商的利润率。本分析假设该芯片的性能与英伟达芯片相同，这当然不现实，但它有助于说明降低芯片成本的好处。若要了解部署 AI 系统背后的经济原理，请参阅我们的AI 云 TCO 模型。

微软没有借口，通过对OpenAI的早期且有先见之明的投资，他们对模型架构早有充分的预见。但照此速度，对Maia 200设计有一定贡献的OpenAI，尽管其定制芯片的研发工作晚了几年启动，却可能拥有比微软更好的定制芯片。不过，这对微软来说可能是件好事：微软对OpenAI IP的权利涵盖除消费级硬件之外的一切，其中包括使用OpenAI Titan ASIC产品线的权利。鉴于OpenAI的ASIC发展轨迹看起来比微软Maia要好得多，微软最终可能会使用Titan来运行OpenAI模型。这种情况与微软在OpenAI模型方面的情况类似。虽然他们可以使用OpenAI模型，但仍在尝试用微软AI训练自己的基础模型。与模型一样，由于这些IP权利并非永久有效，对芯片路线图的访问也不是永久性的。依赖OpenAI的ASIC无法实现超大规模计算ASIC计划所共有的硬件自给自足的目标。

微软部署在其亚特兰大费尔沃特2号数据中心的网络具有创新性，处于当今为AI集群部署的前沿。费尔沃特2号的网络将两层512基数网络的概念更进一步，采用仅轨道拓扑，将512基数两层网络上可连接的GPU最大数量从131,072个增加到524,288个。

在使用具有k个端口和L层交换机的无阻塞Clos网络上可连接的GPU数量，可以使用以下公式计算。如果我们假设一个使用具有64个800G逻辑端口（k = 64）的Spectrum-X SN5600交换机构建的2层网络（L = 2），那么我们会发现，在2层网络上可连接的GPU最大数量为2048个：

下表展示了基于64端换机，最多4层交换机的最大GPU数量。随着层数的增加，每个交换机对应的GPU比例下降，使得每个GPU的网络成本更高。

但如果我们不这么做，而是将每个GPU的单个800G逻辑端口拆分为8个100G端口，结果会怎样呢？ CX-8 NIC可以支持分拆成100G链路，但并非所有51.2T交换机都支持512个100G逻辑端口——你需要一个512-Radix交换机，如Spectrum-5交换机。神奇之处在于端口数量k以层数L为指数进行幂运算，通过这种分拆方案，我们最多可以连接131,072个GPU——与没有高基数交换机时的2,048个相比，有了巨大的增长。

使用512个100G端口而非64个800G端口，可支持的最大GPU数量如下：

但如何构建这样的网络呢？我们可以使用8个独立的叶交换机平面，连接到每个GPU上的8个100G端口。每个平面将有256个脊交换机和512个叶交换机，512个叶交换机通过1条100G链路连接到256个独立的GPU，总共连接131,072个GPU。

但每个平面仅会连接到每个GPU的一个100G逻辑端口，因此我们需要8个平面。8个平面乘以每个平面768个交换机，得出6144个交换机。这意味着每个交换机对应21.3个GPU，比使用800G端口的4层网络中每个交换机对应9个GPU的比例更高效。这就是甲骨文公司的“星门”（Stargate）正在部署的网络拓扑结构，也是英伟达（Nvidia）和博通（Broadcom）的512-Radix交换机获得关注的一个特定用例。

微软将这一概念进一步拓展，部署仅使用导轨的拓扑结构来构建一个网络，该网络可以在两层网络上连接多达524,288个GPU！在仅使用导轨的网络拓扑中，我们将把单个GPU上的链路拆分为多个端口的概念，拓展到将整个*计算托盘*上的链路进行拆分。现在，我们不再将每个GPU的800G带宽拆分为8条链路，而是将每个计算托盘的3200G带宽拆分为32条链路——每条链路连接到32个平面中的一个。

该网络使用24,576个交换机连接524,288个GPU，实现了与131,072个GPU网络相同的21.3的GPU与交换机比率，但连接的GPU数量是其四倍！

然而，这些平面中的每一个都是完全独立的，这意味着同一计算托盘中的各个 GPU 不再能够通过横向扩展网络相互通信。相反，它们需要通过 PXN 在 NVLink 网络上进行通信。然而，这确实带来了一个挑战，因为很难在同一网络上重叠不同的通信\[CE1\] ，不过微软的 MRC 协议旨在优化此类流量，并在训练层面调度该流量。

虽然微软可以使用32个平面部署多达524,288个GPU，但实际上，Fairwater 2中的每栋建筑（即A楼和B楼）的容量最多只有300兆瓦，对应约160,000个GPU。微软没有专注于在同一多平面网络上连接更多GPU，而是使用从核心层到AI广域网（AI WAN）的超订阅上行链路。

微软专门构建了AI广域网（WANs），使得训练任务的执行方式能够利用并感知广域网连接。其目的是最终在两个费尔沃特校区（亚特兰大和威斯康星）甚至在凤凰城、爱荷华和阿比林校区之间开展分布式训练任务。

为构建此网络，微软在连接数量“较少”的GPU的同时，在BT1（核心）交换机上分配端口以实现与OCS的上行链路连接，同时预留一些空端口用于扩展。这样的网络可以使用32个平面构建，每个平面配备128台BT1（核心）交换机和154台BT0（叶）交换机，OCS交换机位于BT1（核心）层之上。

确切的超额订阅比例尚不清楚，但Meta使用3:1的超额订阅来连接其100k+集群的多个数据中心。

虽然BT1的下行链路使用DR光模块，但其到OCS的上行链路可能使用FR8光模块，因为这允许使用CWDM将8个100G通道复用在一起，并且可以使用环形器在一根光纤上实现双向连接。由于OCS仅切换来自单根光纤的光，因此能够挤入这根光纤的带宽越多，每个OCS端口可实现的有效带宽就越大。使用800G FR8光模块还能保留8x100G分路，因为接收端会将光信号解复用回所有8个通道。

微软在AI广域网（AI WANs）中使用光电路交换（OCS），以便在无需复杂重新布线的情况下，为建筑物之间的光链路重新配置提供选择。不需要深度缓冲交换机。相反，使用单独的协议通过OCS将数据包发送到不同的集群。谷歌已经在其数据中心网络（DCN）中使用Apollo OCS，理由是它可以为网络结构扩展、技术更新和网络拓扑调整增加灵活性。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

来源：谷歌

除了用于费尔沃特2号园区内部连接的AI广域网（AI WAN）外，还有第二个AI广域网，它是一个长途网络，将费尔沃特2号园区与其他遥远的微软区域相连——包括威斯康星州的一个区域（费尔沃特1号）、菲尼克斯的集群、爱荷华州的OpenAI集群以及甲骨文的阿比林园区。这些区域之间长途链路的总带宽为300Tbps，并有扩展到10Pbps的选项。

虽然FR光通信设备有能力连接费尔沃特2号的两座300兆瓦建筑，但连接到距离达数千公里的其他园区，可能需要转发器的功率和覆盖范围，并将采用可重构线路系统（RLS），以便能够使用密集波分复用（DWDM）技术。为了高效利用长距离光纤，DWDM技术用于将多个光波长（每个波长承载800G或高达1.6T的带宽）复用在同一对光纤上。如果利用C波段的32个信道和L波段的32个信道来组合64条800G链路，一对光纤可以承载高达51.2Pbit/s的带宽。

在图表中，我们展示了300 Tbit/s的连接性如何需要375对光纤（如果使用FR光模块搭配环形器，则为188对）才能从光交叉连接（OCS）连接到转发器，但在C波段的32个通道上采用密集波分复用（DWDM）可以将这一需求减少到仅12对光纤。

ZR光模块（400ZR和800ZR）是另一种可用于在数百公里范围内传输信号的选择，并且许多ZR链路也可以使用DWDM复用在同一对光纤上。虽然ZR光模块可以提供一种简单得多的调度解决，因为它们可以直接插入AI路由交换机，但对于数千公里的长距离传输，转发器通常是更优选择。事实上，Meta的跨规模部署正在使用ZR光模块，并且由于跨规模部署，我们看到ZR光模块的需求大幅加速增长。

---

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

推荐阅读：