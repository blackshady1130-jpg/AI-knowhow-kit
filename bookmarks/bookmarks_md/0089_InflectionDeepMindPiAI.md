---
url: https://mp.weixin.qq.com/s/GWZ1me13_DNf6RCubucGrg
title: "Inflection创始人：从DeepMind到Pi，AI智能体如何迎来寒武纪大爆发"
description: "AI Agents应该成为每个人的数字映射。"
author: "拾象"
captured_at: "2026-03-08T10:26:59.392Z"
---

# Inflection创始人：从DeepMind到Pi，AI智能体如何迎来寒武纪大爆发

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/3tHNibnJ2jgydpvZdMssv5sG8pM3GbuSD0xT0qLODS9YB2xPYNL7oW5Tic7FGtt75jxLsgnSLaol8KL7JLWz9KLg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgydpvZdMssv5sG8pM3GbuSDl6ZDULyt3HkArLwomVbuESyibG7yMicGkSSGxFdBOGPRofHYvriciafupw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgydpvZdMssv5sG8pM3GbuSDleHpETuVyfAhibCVp1WMmo6QNLhRFKj5I5ODcKp2vzuPr6FgEhxzia4g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

编译：Siqi、wenli

排版：Mengxi

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgydpvZdMssv5sG8pM3GbuSDRzWEKoWWhibPxpC6cgqSBCcg5W7QLtmRsQZazlxUH8hibPPlKYBRibNeg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

Inflection 因其豪华的创始团队而备受关注：它的三位联合创始人分别为原 DeepMind 联合创始人 Mustafa Suleyman、LinkedIn 联合创始人以及 **[Greylock](http://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247500410&idx=1&sn=00bc50ccab6cf1c8c5b688ae8dab37ae&chksm=ce9b7de4f9ecf4f20477af29e7851d3a5ad5a78deb49e9e83da20a137729347796a1726107f7&scene=21#wechat_redirect)** 合伙人 Reid Hoffman，以及曾担任 DeepMind 资深科学家的 Karén Simonyan。

本月初，Inflection 发布了自己的第一款产品：一个名为 Pi 的个人 AI 助理。和 ChatGPT、Claude 一样，用户可以和 Pi 直接对话，但 Pi 不仅仅只是服务于搜索或回答问题等生产力需求，而是主打“情感陪伴”、以“情商高”出名，用户和 Pi 的交流就好像和身边的朋友一样自然。除了 iOS App 外，Pi 还开放了企业端 API。

Inflection 现阶段的公开信息还比较少，我们整理编译了 Inflection 联合创始人 Mustafa Suleyman 在近期的一系列访谈，希望能作为大家了解 Inflecion 的参考。

Mustafa Suleyman 并没有将 Inflection 定位为一个大模型公司，而是看成是一个 AI 应用公司（这一点和 [**Character.ai**](http://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247502024&idx=1&sn=4b23b7979ddb713e6f049d4dbb0cf61e&chksm=ce9b7756f9ecfe40e95e76fa87da8cae2d4caa09a3778189ddd1e06cb478f107265353ddb66d&scene=21#wechat_redirect) 的对比十分有趣）。Mustafa Suleyman 本人十分 buy-in 以社交网络产品为代表的个人消费级软件在过去 10 年所产生的巨大影响力，因而也认为 to C 的消费级应用仍旧会在 AI 时代发挥相同等级的影响力，但在商业模式上，他则提倡 AI-native 的语境下一定会诞生新的商业模式，延续移动互联网时代的思路本质上会影响产品设计、用户体验。Inflection 同样关注 AI Safety，并将其定义为关键价值观，Inflection 追求的 AI Safety 不止是去除负面、对用户有害的信息，还是追求产品体验上限的重要途径。

作为一个 AI Studio，在 Pi 之后，Inflection 还会针对不同场景开发更多的 AI Agents。相对于追求通用的 AI Agents，Mustafa Suleyman 更倾向于未来有上亿个、甚至数十亿个 AI Agents，这些 AI Agents 一定是和其所有者强绑定的、是我们每个人的数字映射，而拥有绝对自主权的全能 AI Agents 反倒十分危险。

**以下为本文目录，****建议结合要点进行针对性阅读。**

**👇**

01 如何理解 AGI：“通用性”被过度放大

02 Infection & Pi：AI 与人如何互信？

03 AI Safety：用户交互也是创造安全边界的过程

04 未来会有数亿个 AI Agents，大小模型共同驱动 AI 大爆炸

**01.**

**如何理解 AGI：**

**“通用性”被过度放大**

**Q：你是如何创立 DeepMind、参与 AI 研究当中的？**

**Mustafa Suleyman：**在进入科技领域之前，我一直在哲学、政策领域工作，无论是牛津大学的哲学启蒙，还是参与哥本哈根气候谈判大会，我始终追求不断扩大自己的影响力来帮助更多的人。与此同时，我也参与过 NPO 组织以及咨询机构的创建和运营，但过程中我发现这种服务的影响力范围相当有限，也因此我一直很好奇像联合国这样的组织究竟是如何影响不同国家层面的行为的，以及我们如何更有效的在紧张和分歧下达成共识、做出好决策。

在 2008 年，我关注到 FaceBook 只用了短短 2-3 年内就达到了 1 亿 MAU 的体量。**Facebook 在给到大众信息渠道这件事上并不是绝对中立的，但这个产品让我意识到或许技术、平台产品才是能够汇聚、塑造群体思维、进而构建人类新的沟通模式更好的路径。**

公共讨论研究中一个很经常使用的方法论是：“讨论的框架是什么？如何组织起一个讨论空间？如何让人们有建设性的争论？如何通过设定环境变量推动对话？”——当我从这个视角看 Facebook 时，发现 **Facebook 本身就是一个选择架构（Choice Architecture）：这个架构中提供了特定的设计选择（Design Choice）来激励特定的行为。比如在 Facebook 的产品中，虽然并没有明确的排名、榜单这样的设计，但即便只是点赞、或者某个按钮的顺序排布、页面上信息的布局等所有这些细节都会以一种或另一种方式影响和驱动着用户行为。这种设计在我看来不知不觉中影响着亿万人，不夸张地说，Facebook 对整个社会行为的影响不亚于宗教。**

与此同时，我也联系到了 Demis Hassabis，Demis Hassabis 是我的童年好友，我们都对扑克和游戏都很感兴趣，在当时我们也都发现了对方对通过技术推动积极的社会变革有着同样浓烈的兴趣。

**我主要受到了平台、软件、社交应用网络效应等的启发，而 Demis 更多专注在机器人和科幻领域，他认为治理经济体、制定理性决策的方法就是先模拟经济体本身。Demins 对于 AI 的思考模式更多基于游戏，在当时他也刚刚结束自己的游戏领域的尝试。**

**Demis Hassabis ：**DeepMind 的联合创始人、CEO，Demis 在中学时期编写了一款名为 Theme Park 的虚拟经营游戏，销量高达 1500 万份，1998 年 Demis 还参与创立了游戏工作室 Elixir Studios，Elixir Studios 开发过几款成功的游戏，例如，Evil Genius，2006 年 Elixir Studios 被收购。Demis Hassabis 结束游戏创业后加入牛津攻读 PhD 学位。

在萌生了对 AI 的兴趣之后，我也开始思考“到底什么是智能（Intelligence）” 以及 “如何实现 Intelligence？”这样的问题，也因此认识了 Shane Legg，我们前后交流了几个月，Shane 的研究是推动 AGI 想法诞生的主要原因。

Shane 在自己的 PhD 论文中研究了智能的定义。在对 80 种不同文化中的对“智能（ Intelligence）”的研究基础上，Shane 将“智能”总结为“能够在广泛的问题中表现优异的能力”，并给出了一套可工程化的量化标准。Shane Legg 的研究是我对于 AI 认知的一个转折点，**基于他的研究我们至少有了一个如何将人类智能总结、转化为算法结构的假设，Intelligence 成为了一个可被解决的问题。**

**Shane Legg：**DeepMind 联合创始人、首席科学家。他在 2008 年发表的博士论文 *Machine Super Intelligence**（https://www.vetta.org**/documents**/*

*Machine\_Super\_Intelligence.**pdf ）*被认为是最早系统探讨机器超级智能（超越人类智能）的学术文章之一，该论文为后续相关研究奠定了基础。

****Q：**如何定义 Intelligence ？**

**Mustafa Suleyman：**我对 Intelligence 的想法一直在变化，**就目前来看“通用”还是一个比较不错的定义，但某种程度上，它又被过度放大了，比如 OpenAI、Anthropic 等团队普遍都在追求“通用性”，**主张一个 Agent 可以完成所有的事情：写代码、翻译文字、语言生成、要支持多模态等等。

我认为还有另外一个重要标准是：**在给定上下文的情况下，系统具有识别环境中重要特征（feature）、并将注意力和处理能力分配给这些特征的能力。**

能推动这个领域的关键是出现一个路由器（router） 或者中央大脑（central brain） 这样的组件，链接了一系列不同的垂直的系统，这些系统或许看起来并不像“真正的 AI”，可能是传统软件，又或许是存储知识的数据库工具等，但这个路由一样的存在担任了决策的行为，甚至未必由 LLM 来构成。

**Q：这听起来很像是人类大脑的工作方式？大脑在某种意义上也可以被看成一种集成模型，有专家系统或 MOE 模型下的 router 来负责控制任务中访问的子系统，也有负责视觉处理的视觉皮层，还有其他部分专门负责同理心。**

**Mustafa Suleyman：**大脑一直都是 AI 研究的灵感来源，除了神经网络这个经典的例子之外，强化学习也是受大脑启发的算法之一。

2020 年 1 月，DeepMind 与哈佛大学 Nature 的新研究证明了大脑中存在“分布强化学习”。大脑中的强化学习是通过多巴胺驱动，并以“概率分布”的方式来预期，这种奖励机制的预测类似于强化学习系统的工作方式。

当前我们的模型还只能做到完全连接，因为我们还没有完全掌握稀疏激活（Sparse Activations）算法，无法像人脑那样仅通过激活部分神经元来执行任务，**实现稀疏激活在将来会是一个很有前途的方向，因为这意味着我们能够构建出一个更高效、更接近人脑的模型**。

但实现稀疏激活并不是唯一的选择，我们还可以通过训练一个**“决策引擎”来实现类似的目标，由这个引擎来根据场景选择合适的模型，在某些情况下，引擎需要调动一个超高质量的、大概需要 20 秒模型，大多数情况下，可能一个可以在 3 秒内进行快速响应的小模型就能够满足需求。**

实现不同规模模型的集成和选择，不是一个单纯的 AI 学术研究的议题，更多是一个工程问题。

**Q：为什么选择在 DeepMind 之后再次创办另外一家 AI 公司？**

**Mustafa Suleyman：**在 2018-2019 年，我们还不清楚神经网络是否会对语言产生重大影响，但过去 5 年的事实证明，CNN 在局部学习输入图像中的像素结构方面非常有效。像素抽象出的子特征代表了你试图预测的东西，通过线条和边缘能刻画我们的现实世界，眼睛、脸和场景等等。

**但问题是许多预测任务中，答案和预测结果其实处于一个很稀疏的空间之中，它们之间相当遥远，一直到 GPT-3 的成果时，我对于解决这一问题的可能性才坚定起来。**

2020 年初，我在谷歌参与了一个名为 Meena 的大语言模型项目，Character.ai 的 Noam、Daniel Coakley 也在这个项目当中。最开始这个模型还不算大，随后我们拓展了它的规模，于是逐渐演变成了大家今天所熟知的 LaMDA，这个过程中我们也逐渐看到它在各个领域中表现出惊人的能力，比如搜索，改进等等，不过 LaMDA 也出现了所有大模型的通病：幻觉问题。但总体上，参与 LaMDA 的经历对我来是相当震撼的几年。

Mustafa Suleyman 因为其高压管理方式的新闻在 2019 年离开 DeepMind，随后加入 Google 担任人工智能产品及政策总裁，主要关注 AI 伦理道德方面，通过制订人工智能技术使用伦理，避免此类技术遭滥用。

大概是在 2021 年年末，我还在非常努力地为 Google 推出产品，与此**同时也在思考着语言模型似乎会是未来，因为这显然是新的技术浪潮，**和我有一致想法的除了 Noam，Adept 的 David Luan 也在做类似尝试。然而出于种种原因，当时的 Google 还未完全重视语言模型这件事。于是在 2022 年的 1 月，我选择离开，和我的联合创始人 Karén 一起寻找新的方向。

**Karén Simonyan：**Inflection.ai 的联合创始人、首席科学家。Karén Simonyan 的主要研究领域是机器视觉和神经网络。2014 年，Karén 在其参与创立的 Dual 被 DeepMind 收购后加入 DeepMind。2015 年，Karén 提出 VGG 网络的理念，VGG 网络是一个简单（仅用 3x3 卷积核）但高效的 CNN 结构，在没有池化层的情况下形成很深的网络。VGG 在 ImageNet 图像识别中取得当时最优的结果，被视为该领域的 SOTA（state-of-the-art）。2018 年，她又提出了 SENet，即使用通道注意力机制提升 CNN 网络的性能。

**02.**

**Infection & Pi：**

**AI 与人如何互信？**

****Q：**Inflection 是什么？**

**Mustafa Suleyman：**Inflection 是一个 AI Studio，作为一个 AI 应用公司，尽管我们开发应用的过程本身也是一个 AGI 的研究过程，但我们并不执着于发表论文，也并不以研究为唯一目标。我们目前运行着世界上最大的语言模型之一，并且在主要的基准测试中，我们的性能表现都是最好的，不过我们并没有设定 Pi 去做生成代码的功能，代码生成在目前对我们来说也不是首要任务。

我认为只要整个世界一直在创造新的软件产品，就会一直要求人类具备理解机器语言的能力：我们需要学习机器的编程语言和交互界面。这其实存在巨大局限性，但一切即将发生改变，我们正站在在历史的分界线上：计算机能够和人类通过自然语言进行互动，这将彻底改变数字体验。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*Inflection 理念中也提到了**过去是人类一直在学习和机器交流，**而 AI 浪潮会让这个过程反过来。*

**未来计算机所做的一切将越发“对话式”，这一定会创造一种与过去软件时代截然不同的体验。**你的 AI 不仅会提问题，还会主动确认它的输出是否符合需求，并尝试进一步影响你的理解。通过这样的交互迭代，机器的理解会更接近用户的真实意图，这不仅包含对当下的思考，还有接下来的规划，甚至是能进一步理解用户的情绪起伏。例如，在机票预订场景中，AI 不仅能回答用户关于“航班延误后，我能去哪儿”的问题，且兼具实现“预测延误”、规划“Plan B”及其它综合性方案的能力，甚至能体察用户情绪变化并给予适当的回应。

**可以从 Inflection AI 正在做的事情来理解它是什么：首先，Inflection 的课题之一是 AI 如何参与并辅助人们的工作与生活，另一课题则是我们如何与朋友和家人联系。Pi 作为功能强大的工具，可以跨越语言的障碍，成为很好的个人助理。**

****Q：**什么是 Pi ？它是如何运作的？**

**Mustafa Suleyman：**Pi 是 Inflection 推出的一个个人智能（Personal AI）产品，我们对它的设定是一个动态的、跨平台的 **Personal AI**。无论用户身在何处、通过哪种平台，例如 WhatsApp、Instagram 或手机桌面等，都可以随时调用 Pi 。Pi 无需下载，也不仅仅只是一个停留在手机上的 App，而是一种真正可持久伴随的工具，当然，我们目前也提供了 iOS App 的入口。

*欢迎关注**海外独角兽**视频号*

*获取最前沿的科技行业资讯*

我认为未来几年每个人都会拥有自己的 Person AI，所以也会有很多不同类型的 AI，例如商业 AI 、政务 AI、品牌 AI。这些不同类型 AI 的目标都会和其所有者保持一致，例如推销或销售某些东西、说服人们接受某些理念等，作为个人，我们也都希望自己的 AI Agents 符合我们自己的兴趣、团队目标等方方面面，这就是 Personal AI。**这很契合我心目中人类与 AI 的未来发展趋势——“相互依存”、“紧密联系”***（Ever-Present Relationship）*。

Pi 能够帮助你理解周围的世界，提供无条件的情绪价值，它拥有无限的知识储备量，但会以非常简洁的对话和更加灵活的形式为用户呈现他们所需要的信息，同时，Pi 也是有趣、富含创意的，可以帮助用户跳出“刻板陷阱”。在许多方面，我认为这是新时代的本质标志。如同智能手机、互联网开启了新的时代，**Pi 不仅是一种新平台或新技术，也会是一种全新范式。**

**如果复盘 LaMDA ，我会觉得我们在设计的过程中缺失了和用户的交互反馈，这也和我的联合创始人 Karen 的想法不谋而合。**

其实我们今天网络上、计算机上所呈现出所有界面（interface）本质上都在讲交互这件事，对话一定是未来的交互界面。**虽然很反直觉，但用户和 Google 之间的互动实际上也是一种对话：**

• 用户在搜索框中给 Google 提出了一个问题；

• Google 根据用户提出的问题生成一个“答案”页面；

• 用户点击进入链接查找自己想要的内容，并不断迭代查询的问题；

• Google 重新刷新结果界面。

但这种交互（提供大量蓝色链接）的问题在于，它就像 1980 年代人们查阅黄页目录（Yellow Pages）的交互一样，笨拙且不流畅。此外，Google 塑造了 SEO 驱动的内容生产方式，我们如今在网络上看到的所有内容现在都几近极端地进行了 SEO 优化。

*欢迎关注**海外独角兽**视频号*

*获取最前沿的科技行业资讯*

也可以从用户视角来看这件事：人们根据 Google 的检索结果进入到一个页面当中，这个页面上的所有文本被分拆为不同的子板块、子标题，有的中间还会被插入广告，每个人基本需要花 5 到 7 秒甚至 10 秒才能穿过整个页面来找到他们需要的片段，而多数情况下，每个人最核心的目的其实快速找到包含了目标信息的核心片段。

人和信息之间的交互之所以被改造成现在的格式只是因为从算法角度，如果用户在页面停留了 11 秒而非 5 秒，就会被系统判定为“高质量内容”的内容。

创作者尽可能多地获得收益的代价是用户时间被浪费：为了保证自己能够在网络上获得更加简洁的信息，需要不断调整自己的搜索问题的关键词，**过去 20 年，我们一直在学习“谷歌语言”。**

**Q：你们在设计 Pi 的时候十分强调情感链接、同理心，而非信息的整合？这似乎和其它大语言模型对话工具的设计逻辑不同？**

**Mustafa Suleyman：**我们之所以突出 Pi 的同理心、情感支持，是因为在设计 Pi 的过程中我们始终围绕“ What makes for great conversation？”这个问题进行。

**一个高质量的、但同时又自然流畅的沟通交互核心有几个方面：**首先，对方真的在倾听你，会通过重复、总结你说过的内容来表明这一点，这个过程不仅仅是复述，还包含着新的有效信息，例如问题、表示感兴趣和好奇等情绪，有的时候也会有一些轻松内容进行的氛围调剂。所以，尽管 Pi 还只是最初的版本，我们尽量让它成为一个思考周到、善良、关心你的世界的陪伴者。Pi 还会记住与用户的历史对话，并具有保持长期记忆的功能。

**大部分 AI 聚焦于提升智力和获取、整合信息的效率等，**但世界上绝大多数人都需要一个具备高质量对话能力的平台，人们希望与之建立有益的关系、借助它的能力处理生活中所遇的一些棘手事项，这就是我们的切入点，**将情感糅合在了 AI 之中。**

****Q：**Pi 或者 Inflection 对商业化是怎么规划的？**

**Reid Hoffman：**LinkedIn 最初始时的理念之一是通过高质量的服务来节省用户的时间。同样的，如果一个人只使用 5 分钟 Pi 对我们来说也是很好的事情。这是我们从社交媒体方面学到的东西，在相当长一段时间中，LinkedIn 受到的冲击比其他社交媒体平台要少得多，部分原因就是我们事先有意的抓取用户真正需要的，并设计好的模式来不断精进我们的任务。Inflection 和 Pi 沿袭了这一理念，我们的目的就是避开弯路，真正为人们的生活增加价值。

**Mustafa Suleyman：**是的。正如 Reid 所说，我们并不想把 Pi 设计成 Kill Time 的存在，也不会使用鼓励用户在平台上投入大量时间的算法，我们的产品也不会是令人上瘾的、多巴胺驱动的产品模型。虽然确实有不少人选择刻意偷走人们时间来换取超额回报，但对于我们而言，既然当下是需要用 AI 来改变现状的时刻，同样也是一个需要新的商业模式带来改变的节点。

根据 Inflection 的官网信息，在商业化上，订阅、增值付费等会是默认选择，并且有可能部分用户也会接受在对话中出现广告，但最终 Inflection 的商业化形态还需要不断测试迭代来完成。Mustafa Suleyman 发布在 Inflection 官网上的一篇文章中也提到，过去互联网通过广告变现的商业模式让存量的 AI 被设计成如何吸引更多用户注意力、而非真正服务于用户，而这是 Inflection 的反面，所以他们在设计 Pi 的时候暂时还没有考虑到广告商等角色。

****Q：**Pi 对企业和开发者会产生什么影响？**

**Mustafa Suleyman：**Pi 是我们创造的第一个 AI，**在接下来的几年里，我们还会继续开发不同的 AI，这些 AI 的个性不同、也分别拥有不同领域内的专业知识，当然还各自拥有独特能力，其中有一些就会锚定企业或是商业 AI。**我们可能会与某些组织或企业进行非常深入的合作，帮助构建真正反映其品牌价值、协助他们应对消费者挑战的 AI 。

**和 Pi 的 iOS App 一起发布的还有 API，通过 API，企业用户也能够使用我们的模型。**过去一年中，我们已经拥有了构建领先 LLM 的能力，我们也很乐于与其他开发人员和企业分享这些具有对话风格的模型与技术。所有的 AI 开发者都能够通过 API 获取不同类型的模型，Inflection 构建的模型是对现有大模型生态的补充。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*Pi 同时开放了 API* 

*来源：Inflection 官网*

****Q：**目前 Inflection 还是一个相对较小的团队，现在的团队文化上是什么样的？Inflection 在寻找什么样的人才？**

**Mustafa Suleyman:**  Inflection 目前大约 30 人，我们组建了一支非常有才华的 AI 科学家和工程师团队，例如 Chinchilla 的第一作者 Jordan Hoffman 目前也在 Inflection 团队工作。

我们在 Inflection 的组织搭建中很重视的一点是，**我们不会特别区分研究员、科学家、工程师和数据科学家这些角色，****几乎每个人都是 Technical Staff 的 Tittle，****对我们来说，每个职能都要能得到平等和尊重，这也是其他实验室之前做得不太好的方面，因为实际上是团队中的每个人共同做出贡献而不是具体的某一类角色，**所以我认为这是一个很重要的改进。

总体上 Infection 是一个充满活力、要求非常高的环境，我们非常专注于个人的贡献，目前还没有中间管理层，只有我和另一个人在直接管理团队。

我从过去的 15 年中的团队管理中得到的经验是，最好的人才永远只是想和优秀的人一起工作，可以得到大量资源支持、拥有相对自由的空间，并且整个团队都有一个共同目标。

我们每 6 周发布一次产品，而第 7 周是我们的内部 Hackathon， 整个团队会聚在一起共同推进产品，这一周的工作强度相当大，但同时也是一个很好的建立良好团队成员关系的过程。结束产品上线后，我们又会为接下来的 6 周工作制定相应的规划。基本上每个人都会在下一周明确他们的 OKRs。3 个月的周期其实有些冗长，6 周刚刚好，还可以为我们带来更多的责任感和乐趣。

**03.**

**AI Safety：****用户交互也是创造安全边界的过程**

****Q：**Personal AI 这种 1 对 1 的交互方式其实很考验信任，因为他们会不断利用你的反馈来强化你已经吸纳的事实，甚至不管对与错，这种比推荐算法更加夸张的“茧房效应”？**

**Mustafa Suleyman：**现实情况下所有平台都做不到绝对中立，一款产品被如何呈现受到更上层的政治和文化影响的结果，而 AI 只是加速它的一个中间件。所以，我对此的看法是，这不是 AI 本身的问题，而是包括 AI 公司以及过去传统社交媒体平台在内的所有人都必须承担的一种平台责任。

我认为在这个问题上，尤其是硅谷应当对欧洲保持更开放的态度。我们必须弄清楚在整个社会范围内，究竟能够信任哪些机构、哪些机构会影响推荐算法或 AI 算法。从根本上说，我们必须让这些技术对大众负责，就意味着上层民主结构本身需要非常清晰地解决这些不公平的问题，能够有一些运作良好的机构提供真正的监督行为。

****Q：**Inflection  是如何解决安全/隐私问题，你们在产品中构建的安全边界是什么？**

**Mustafa Suleyman：**AI Safety 是构建 Pi 最重要的部分之一。

首先，AI Safety 还在实现的过程中：我们试图去达成一个治理方法的共识。过去在 DeepMind，我们组建了专业的 AI 监督问责团队，也尝试了不同的监督委员会、不同的 AI 道德章程等。技术确实进步飞速，但接下来十几年里 AI Safety 一定会是时代焦点之一。

**Inflection 的具体做法是：给 Pi 展示各种各样的正反面例子，让它能够在特定问题域中识别回答的质量好坏，通过数万次、数十万次，甚至数百万次的机器学习后，Pi 将学会建立一个行为准则模型，**这也是我们的关键工作成果之一。

Pi 的交互过程也是创造边界的一个过程，因此另一个很重要的关注点是用户与 Pi 交互的方式。例如，如果有些人将 AI 作为发展浪漫关系的手段，这对 Pi 来说并不允许，因为这不是我们所追求的。因此每当 Pi 发现交互对话正朝着不好的方向发展时，它就会非常坚决地阻止对话继续。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*Inflection 的 AI Safety 迭代飞轮*

*来源：Inflection 官网*

总之，Pi 是非常具有礼貌、友善和尊重性的，但它也非常果断。**清晰的边界设定，明确的结果导向是我们** **AI Safety** **安全计划的基础组成部分。**

**安全的一部分不仅仅是避免消极因素、避免可能导致自我伤害或其他伤害的事情，同时也是对积极因素的放大。**所以，Pi 所主张的 AI Safety 不仅仅是“避免负面影响”，它还致力于将用户带到一个更健康、更充实、更有意义、更快乐的空间中去。

**04.**

**未来会有数亿个 AI Agents，大小模型共同驱动 AI 大爆炸**

****Q：**这种交互式的 AI 对 Google 、以及整个传统互联网世界而言意味着什么？**

**Mustafa Suleyman：**肯定会从根本上改变现有形式。我相信这种简洁、动态、个性化的互动 AI 就是未来。**如果我是 Google 我会非常担心，但对于内容创作者、或者其他只是通过网站来完成服务或产品交付的人来说并不用太担心。**

举个例子，如果某个人运营了一个有关烘焙的博客，基于 AI 他可以创作出更高质量的内容，而他的 AI 也会和其他人交流烘培相关的一系列内容。比如，我的 Pi 会代表我和这个烘焙博客的 AI 进行交互，我的 Pi 向对方提出问题：“Mustafa Suleyman 如果想从 0 到 1 学习烘焙要如何做”，在获得对方的答案后，我的 Pi 则会向我展示它今天收获的内容。我认为这代表了一种新的内容生产方式，也是一个不同个体的 Personal AI 互动交流的世界。

其实这也是 Google 现在在做的事情，只不过 Google 是抓取静态内容做排序、呈现的过程。

从信息交互的角度来看，所有的“品牌”也都可以看成 AI，几百年来广告业*（这里想说明是某种意志或价值观的一种具象化）*只不过它们是静态的。所以我并不认为世界上会有 1 个或者 5、6 个 AI Agent 的观点，我认为会是数亿个、或数十亿个 AI，**这些 AI 是我们每个个体的映射，**我个人并不想要那种完全独立于具体个人存在的、有绝对自主能力的 AI，在我的价值体系中，这种 AI 对人类而言是很危险的。

****Q：**你参与建立了许多大模型，如何看模型扩展的问题？模型性能的上限在哪里？这是数据问题还是计算问题？**

**Mustafa Suleyman：****在我看来，所有进步都来自复合的指数增长。**

在过去 10 年中，我们用来训练全球最大型模型的算力每年都在增加一个量级：2013 年 DeepMind 发布的 Atari DQN 论文仅使用了 2 petaFLOPS，到今天 Inflection 在训练我们自己最复杂模型时使用了 100 亿 petaFLOPS。9 年来的 9 个数量级，这个变化相当神奇。

Atari DQN 论文指 DeepMind 在 2013 年的发布的 *Playing Atari with Deep Reinforcement Learnin*，这篇论文展示了使用深度强化学习来玩 Atari 游戏的方法，被认为开创性地把深度学习应用到强化学习领域，是深度强化学习的一个基石。

所以我觉得很重要的是保持谦逊，承认指数增长的浪潮正在塑造我们的行业。**所以如果要预测未来会怎么样，你只需要看指数增长，很明显正在发生什么。这还仅仅是在算力方面。**数据这一侧的变化大家都很熟悉。我们使用了大量的数据来训练模型，这个趋势还将继续。

但我认为人们没有完全意识到的一点是，**模型自身也在变得更高效。**大模型毫无疑问会走向成功，与此同时，也有一些模型在变得越来越小、也越来越高效。

Chinchilla 的提出其实是一个很重要的突破，也表明我们在架构方面很早期，现在的模型效率还有很大的提升空间。我们目前可以用相当于 GPT-4  1/15、1/20 参数大小的模型实现和 GPT-4 相同的功能，这些小模型会越来越开源，在未来也会有更多的更多小型开发者能够利用使用这些模型来搭建产品，换言之，散落在世界各地的每个人都将开始使用这些模型，将自己的实际需求与之结合，而这一定会催生新的创新爆发。

所以我认为两条线是并行的。一方面，构建大模型一定能够获得超额回报，Inflection 就在这条路上，与此同时，我们也会看到越来越多的、开源的小模型，每个开发者都能够自由访问。而这正是 AI 创新大爆发的两面。

**Chinchilla:** 2020 年 5 月 OpenAI 在 GPT-3 论文中提出过他们的 LLM 默认数据缩放法则（Kaplan 法则），即为 300B 的 tokens 可用于训练大小为 1750 亿个参数的 LLM；DeepMind 在 2022 年发布的 *Training Compute-Optimal Large Language Models* 论文中，研究了在给定预算下基于 Transformer 语言模型的参数数量与模型大小之间的关系，认为当前 LLM 训练明显不足，并提出了新的“数据最优”LLM 数据缩放法则（Chinchilla 法则）。

Chinchilla 能够在使用与 GPT-3 同样的数据量的前提下，基于 Chinchila 能够构建出大小仅有 GPT-3 1/11 的模型，或者在实现同样大小模型的前提下，GPT-3 需要约 11 倍的 tokens 数量。

**Reference**

https://inflection.ai/why-create-personal-ai

https://www.youtube.com/watch?v=hixrHmqf2zc&t=513s

https://inflection.ai/about

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

延伸阅读

Ayar Labs：挑战计算中心“最后一米”，LLM浪潮下的硅光探路者

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

C-Eval: 构造中文大模型的知识评估基准

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

对谈OpenAI：如何为全球70亿人部署“超级大脑”？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgydpvZdMssv5sG8pM3GbuSD0yZflDsokL0ib0kxDEiaVSf4yL1ejliagcqaPOG2iabR8FSv5LYOSNgLvw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

Character.AI：AI Agents 平台下的大模型“民主化”梦想

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgydpvZdMssv5sG8pM3GbuSD0yZflDsokL0ib0kxDEiaVSf4yL1ejliagcqaPOG2iabR8FSv5LYOSNgLvw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

复杂推理：大语言模型的北极星能力

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgydpvZdMssv5sG8pM3GbuSD0yZflDsokL0ib0kxDEiaVSf4yL1ejliagcqaPOG2iabR8FSv5LYOSNgLvw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19)