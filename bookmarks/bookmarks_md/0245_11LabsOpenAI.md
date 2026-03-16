---
url: https://mp.weixin.qq.com/s/VSQm3lbinAKJShmpcrStXw
title: "11Labs：声音模态能否突围OpenAI？"
description: "语音生成开始变成一个可被投资的赛道。"
author: "拾象"
captured_at: "2026-03-08T11:04:05.229Z"
---

# 11Labs：声音模态能否突围OpenAI？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/3tHNibnJ2jgzYlJQ6Pw0P5hgsXkoQ9cVt1ia7OJowWFXPPZbBlkHhI9SibQiaX4T0Hq5tGfDK9vZdkibGyGLwePZLfg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgzYlJQ6Pw0P5hgsXkoQ9cVtg2cykZY5I0OEDfgHvoUKGATI4CB1YFhUQ7zicfA3n3hqXOMZpVcZib1w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgzYlJQ6Pw0P5hgsXkoQ9cVtTeamnzrLib7Do4L3fZ65Pjd5EicnVh6gFibNwezw0v7IA7Cg1KE30yw3g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

作者：程天一、haina

排版：Scout

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgzYlJQ6Pw0P5hgsXkoQ9cVtic17KqhHsScb7w16E8iavfaycgQmVmpRWMrRPgncgoiaUxSj6D1SJ3l2g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

Transformer 为语音生成的体验带来了 10x 的提升。在 Transformer 出现前，受传统架构所限语音生成的质量、速度、成本有硬上限，很难达到自然可用并且发挥大规模商业作用的程度。2016 年 Google 基于 Transformer 的 Tacotron 模型出现，语音生成的质量开始有大的进步，并且可以随着数据及算力提升而继续演进。

**目****前生成的语音质量接近真人，情感和腔调瓶颈也逐渐突破，即时的声音克隆可玩性也已经非常强，语音生成开始变成一个可被投资的赛道。**

**但是这个赛道本身在过去仍然相对拥挤和割裂**，美国、欧洲、印度等不同地区历史上都各自有多家公司分别针对不同的语音用例提供服务。**11Labs 在过去 8-12 个月展现出了它的独特之处。**

在 23 年以来，它凭借完胜竞品的声音克隆体验和声音质量，在 Diffusion Model 和 LLM 的热度下迅速引爆了流行点，我们看到的大部分爆款 AI 组合制作的视频通常的堆栈都是 ChatGPT（文案）、Midjourney（画面）、11Labs（配音）、Runway/D-ID（让画面动起来）。市场上普遍认为 11Labs 有巨大的 PLG 势能并且 ARR 有迅速的增长。

除了影视剧配音、游戏本地化、有声书配音等存量场景外，有两个增量的市场可能决定了 11Labs 这一批新的公司能否长大：

• 帮助全球内容创作者为他们的内容增加多种配音

• 让 LLM 驱动的聊天机器人们能够开口说话

**谁能在这两种用例上胜出仍然值得观察，特别是 OpenAI 将如何反应 —— 它拥有最好的开源语音识别项目 Whisper，以及最好的语音生成开源项目 Tortoise 的作者 James Betker。**

**以下为本文目录，****建议结合要点进行针对性阅读。**

****👇****

01 什么是语音生成？

02 Why Now

03 竞争格局

04 11Labs

**01.**

**什么是语音生成？**

语音生成公司通常提供 3 个核心产品：

**• Voice Design**

Voice Design 指的是语音设计，目标是创造出具有特定风格或个性的语音。在 Voice Design 过程中，会根据产品的需求和目标用户，选择合适的发音方式、语调语气、语速节奏等参数，设计出独特的语音风格。11Labs 的 Voice Design 使用户可以通过选择性别、年龄和口音等核心特质，从零开始创建新的语音。即使选择同样的参数设置，该模型每次生成时也会加入随机变化，确保每个语音独一无二。

**• Voice Cloning**

Voice Cloning 语音克隆技术可以复制并模拟特定人物的声音。通过收集目标人物的语音样本，训练语音模型，就可以合成出和该人极其相似的语音。在 11Labs 为代表的 Instant Voice Cloning 兴起前，进行语音克隆通常需要 2 小时以上的语音素材、上千美元的成本、1-2 天微调模型的时间，但是目前的即时语音克隆可以做到使用 30 秒级别的语音样本、无需重新训练就完成克隆。

**• TTS**

TTS（Text to Speech) 是文本到语音合成。通过语音合成技术，可以自动将文本转化为语音。TTS 经历了从自然ness到可控性的发展过程：2021年前，序列到序列模型如 Tacotron 和Transformer TTS 等是主流；2021年开始，基于对抗扩散的 GradTTS、VITS 等生成模型兴起，也出现了更多控制语音风格的技术，如 STYLER、DiffTTS，使语音生成更具可控性。目前市场上普遍认为 11Labs 背后的模型架构是 Transformer 的语音生成模型和用于语音的 Diffusion Model 的结合。

**02.**

**Why Now**

**Transformer**

Transformer 为语音合成带来了质量和体验的飞跃，以及 Unknown-Unknown 的应用场景。

2016 年 Google 基于 Transformer 架构的 Tacotron 模型出现之后，语音生成的质量开始出现转折点，目前所有表现好的模型基本都是 Transformer based。在 11Labs 这一批 22 年成立的公司兴起前，文本到语音本身的转换已经很好了，有多种音色可供选择，但是缺少自然度，并且在长音频中严重缺乏情感及韵律的变化。随着模型变大，这些模型的速度、韵律、情感、语调都更接近人类，终于在过去 12-18 个月大家觉得 AI 生成的声音已经非常自然。此外，更多样性的语音数据解锁了高质量的即时语音克隆能力，预训练提取语音特征的能力带来了非常好的泛化，一条 30s 的语音可以低成本、即时地用于其他文本、语言的语音生成上。

**因此技术上核心的催化剂在于 Transformer，过去旧的架构带来了限制，无论有多少数据和算力，生成的质量都会保持平庸。**

除此之外，Transformer 在语言模型上的突破则为语音生成带来了最具想象力的用例，即为聊天机器人们加上语音说话的能力，从 ChatGPT、Character.ai 到 Inworld 创建的  NPC 都有相关的需求。按照终局有 10 亿 DAU，每人每天消耗 3 美分，这将有机会变成一个百亿美元年支出的场景。

**内容全球化与本地化**

**全球化和本地化是全球内容行业过去 5 年的核心，成为了语音生成目前最 solid 的用例，也是 11Labs deck 中突出强调进攻的市场。**

以 Netflix 为例，它在 18 年以前的制作非常美国中心，在拉美本地化内容 Money Heist 取得巨大成功之后开始转向本地化内容、全球宣发的范式，在鱿鱼游戏上又取得了成功，非常重要的一点是它被翻译成 31 种语言，并被配音成 13 种语言。

Youtube 观察到创作者频道总观看时间的 2/3 来自创作者所在的地区之外，也为 UGC 内容创作者提供了实现类似范式的可能，从 2021 年开始灰度 audio tracks 功能，让创作者能够上传多个音频的配音音轨。这催化了 Unilingo 这样的公司出现，并吸引那些非顶级创作者开始使用 11Labs 这样的配音工具。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

由于 Youtube 自动将 55% 的贴片广告分配作为创作者激励，在 Youtube 上使用更多语种配音的逻辑非常顺畅：多语种 —> 更多地区的受众 —> 更多的观看量 —> 更多的广告分成。

**在 11Labs 这类产品兴起前，在影视剧和顶级内容创作者这些高价格点上有很好的配音产品和服务供应，但跟广泛的内容创作者也有大量的相关需求，但这两条供需曲线缺乏交点。**11Labs 通过降低了这部分供给的价格释放了需求：

• 原来内容创作者可用的解决方案：$100/分钟，10 分钟的 Youtube 视频配音制作周期长达两周，2 小时的影视作品通常需要 15-20 周配音；

• 11Labs 类产品提供的解决方案：$1/分钟，10 分钟的 Youtube 视频进行 3 种语种配音只需 10 分钟，2 小时的复杂影视作品只需 4 周。

a16z Fintech 的 GP Alex Rampell 最近画的这张图就很好地点名了 11Labs 这类产品为供需曲线带来的变化：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这种成本效益的变化和 Midjourney 为美工创作、Descript 为音视频剪辑带来的颠覆非常相似，可以释放大量的 PLG 和 C 端需求。

**03.**

**竞争格局**

**3 类玩家**

**科技巨头**

科技巨头如 Meta、Microsoft 等都在比较积极的布局语音生成技术。它们在相关的学术论文中宣称拥有非常先进的语音合成和克隆技术。但是大厂相比创业公司面临更大的社会舆论压力，由于担心语音克隆技术被滥用，没有推出商业化的效果足够好的语音克隆产品，也没有开源核心技术。目前这些大厂对外提供的语音生成产品效果不如 11Labs，不具有少量样本 (<1分钟) 就可以实现语音克隆的功能，但在价格上具有优势。

不过大厂拥有的产品矩阵使其有着更天然的应用场景，如 Youtube Dubbing、Apple 利用硬件实现本地语音克隆，当大厂“被允许”做这件事之后，11Labs 在工作流上的地位将面临着很大的挑战。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**开源项目**

Tortoise 和 Bark 是目前最主要的开源 TTS 模型，但根据试用和 Reddit 用户原声，Tortoise 生成速度慢，Bark 音质参差，目前很难商用。两者通过与转换模型 RVC 结合可以提高效果，但仍难以达到 11Labs 的类似的语音质量。要达到商用级别，开源模型需要大量数据、算力和算法优化，这需要较高的时间和资金成本及优秀 AI 工程师。

整体来看，11Labs 在语音合成质量和易用性上优势显著，开源模型虽然在快速发展，但尚未构成威胁。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**创业公司**

从我们收集到的内容创作者和 企业客户的反馈来看，**11Labs 的整体体验非常突出，现在定价在聊天机器人的场景上非常昂贵，但是在创业公司之间横向比较区别不大。**

语音生成这个赛道有几十年的历史，因此玩家列表比较拥挤，但是从硅谷 Top-tier 的基金那里拿了 2000 万美元以上钱的只有 11Labs 和 Deepdub：

• 11Labs，Google 和 Palantir 背景，a16z 支持

• Deepdub，以色列空军 ML 背景，Insight Partners 支持

从 ML 背景的角度看，基本上语音模型所需要的科研能力远没有 LLM 强，所以各家的人员配置没有明显的梯队差异，其中比较值得关注的是 Rime Labs（斯坦福语言学和 NLP PhD），更深厚的语言学背景可能带来一些差异化，而且 22 年刚成立，有机会探索更新的架构。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*点击查看高清大图*

**工作流的可能变化**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*点击查看高清大图*

**从目前的工作流状态看，11Labs 处在内容创作及剪辑的一环上，缺少对上下游的延伸，Descript 存在感更强，在几个核心环节都有布局，从这几个玩家身上推演终局大致有几种情景：**

**• Scenario 1：**win w/ All-In-One，市场有机会到达比较高的集中度，Descript 最有机会取胜；

**• Scenario 2：**win w/best technology，市场有机会到达比较高的集中度，11Labs 最有机会取胜；

**• Scenario 3：**w/cost efficiency，采用开源和自建成为主流，OpenAI 和应用垂直玩家取胜；

**• Scenario 4：**w/vertical solution，市场分散在每个垂直行业，各自有小的赢家，甚至仍然保持 3-6 家同时保持单行业第一梯队服务商的分散度。

对于 11Labs 来说，鉴于它还在非常早期的阶段（上个月刚刚脱离 Beta 状态），并且已经拥有了最佳体验的技术，可以**非常自然地投入产品延伸布局以防止 Scenario 1 成真并被干掉，补强垂直行业解决方案也可以预期**，决定它 upside 比较重要的问题是：

• 如果 Scenario 2 到来，它能否继续维持最佳的技术；

• 如果大家开始更看重成本，它的 Pricing 有多大弹性。

对于前者，我们目前的 references 结果还比较正面：

• 构建一个好的语音模型的胜负手不是资金实力和 GPU，因为它预训练单次的成本只有几十到百万美元，更重要的是如何获取到 PB 级别/数百万小时的高质量音频数据进行预训练，需要高保真、自然并且有各类情绪，11Labs 在数据的积累上有比较明确的先发优势；

• 鉴于上一点，其他公司很难通过少量精品数据的方式达到超越 11Labs 的效果；

• 11Labs 作为创业公司在数据使用的灵活性上相较大公司有很大优势；

• 语音模型有数据飞轮，语音数据越积累，语音克隆效果越好。

对于后者，目前市场的普遍看法是很难真的将 11Labs 用于有大规模用户的聊天机器人产品内：

• 对于每个月内容长度固定的内容创作者来说，11Labs 的定价是合理可接受的，$22 的创作者方案用于美元制作 2 个 10 分钟的 Youtube 视频并不昂贵；

• 对于聊天机器人类产品，每个 DAU 每天进行大量对话，小几千的 DAU 在实际业务中一个月支付 10 万美元以上的账单非常常见。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**04.**

**11Labs**

**团队**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

ElevenLabs 由前 Google 工程师 Piotr Dabkowski 和前 Palantir 战略师 Mati Staniszewski 创立。

Mati 在读高中时认识了 Piotr。Mati 对数学有着浓厚的兴趣，在帝国理工学院期间举办了英国第一个由学生主导的数学会议 Mathscon。毕业后，他将自己的分析技能应用于产品构建，在 Opera、BlackRock、Palantir 多家公司积累经验。和 Piotr 一起构思了许多有趣的创业点子，后来两人联手创建了 11Labs，目标是让所有语言内容都可以用任何语言和语音进行表达。

Mati 表示在创办 11Labs 后，很多人向他们提出新的项目方向和建议，但他们注重保持业务专注，聚焦于团队真正相信的事情 - 语音生成。

目前团队共 19 人，人员精简但人均实力强，大多拥有连续创业经验或深度学习、机器学习背景。

**产品**

ElevenLabs 在上个月完成 Beta 测试，向外界发布了支持 28 种语言的 Eleven Multilingual v2 模型，在这一模型之上以 UI 和 API 的形式提供了一系列产品功能：

• Speech Synthesis：选择特定语音将文字转换为音频

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

• VoiceLab：自行设计或克隆声音

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

• Voice Library：PUGC 的语音库可供用户再次选择使用

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

11Labs 还支持用户选择不同等级的 API latency 以平衡速度与其他性能：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Why should we care**

**引爆流行**

和 Replit、Replicate、Runway、Midjourney、ChatGPT 等名字类似，11Labs 在过去的 6-12 个月已经成为了新一代语音生成的代名词，大量的 Twitter、Hacker News、Github 用户和项目都在向外分享其使用 11Labs 创造的作品，我们访谈的大多数个人用户都是在了解 11Labs 之后直接付费和使用，几乎没有其他竞品的心智。

**绝对领先的语音克隆体验**

语音克隆是这一波语音生成最颠覆性的功能。11Labs 建立了全新的语音克隆模型，提供一站式的专业语音克隆服务。在没有微调的情况下，11Labs 可以在短至 5 秒的样本上实现高输出相似度，目前市面上的产品仅 11Labs 可以做到这一点。11labs 的克隆语音有多语言能力，一个创作者的语音可以覆盖近 30 种语言。从个人用户到企业级客户，评 11Labs 的克隆效果和成本是一致好评，显著好于其他竞品。

**团队在过去 12-18 个月****证明了自己的创新和经营能力**

团队很巧妙地找到了产品方向，切入了大厂担心社会舆论不敢做，一般创业团队又做不了的sweet point，并且在高质量、大量级的语音数据积累上有了先发优势，还有机会拿到飞轮效应。

**产品发布时间线**

**技术领先能否维持**

我们目前的 references 普遍认为 11Labs 在数据上有时间差的优势以及潜在的飞轮效应，和 Midjourney 类似。但是围绕它的 Concern 也和 Midjourney 类似，竞品做单语种、垂直场景的声音效果已经可以超越 11Labs。同时在架构上，目前的普遍看法是 11Labs 有一定的架构创新才能取得目前的产品体验，但是由于它没有披露任何细节，很难评估它的架构有多超前。

**愿景决定产品方向**

从公开的 deck 来看，11Labs 在去年还想成为一家驱动创作者进行 AI 配音的公司。从我们跟 Chatbot 应用开发者的 reference 来看，它的 Pricing 不是为了这一场景设计的。从我们跟 Rime 的 reference 来看，它的 latency 优化也不是 Chatbot 场景优先的。

因此团队的愿景非常重要，决定了它短期的产品路线图，以及长期是更像 Runway、Descript 那样成为 All-In-One 的软件公司，还是像 Midjourney、Character.ai 这样的模型公司。

上个月的模型发布显示出 11Labs 支持更多围绕实时对话的 Chatbot 的决心，它发布的  live translate between languages 功能帮助一波 LLM 应用开发者们解锁了新的可能性。

**模型的可组合性带来多大 upside**

OpenAI 是否会进入这一方向？这一问题目前还比较难回答，但是 OpenAI 目前已经拥有 Whisper 和 Tortoise 的发起者 James Betker。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**语音克隆的负面舆情和社会责任问题**

11Labs 需要在传播度和社会责任之间找到一个平衡，目前看它在这方面的投资弱于 Ressemble 和 Descript 等竞品。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

延伸阅读

“AI版YC”创始人：我们要如何跨越AI Hype Cycle？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Jan Leike：OpenAI将如何在4年内实现超级对齐？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Luma AI会是3D领域的Midjourney吗？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgzYlJQ6Pw0P5hgsXkoQ9cVtYTn4TVshmFdFmpQJUvic32SiabjtqW5IgtSlxUrK8jGH7F95Gw0r7qxQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=25)

Alkira：SD-WAN 先驱再创业，多云网络对 GenAI 关键吗？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgzYlJQ6Pw0P5hgsXkoQ9cVtYTn4TVshmFdFmpQJUvic32SiabjtqW5IgtSlxUrK8jGH7F95Gw0r7qxQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=27)

Anthropic创始人访谈：Scaling与强化学习，可解释性与AGI安全

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgzYlJQ6Pw0P5hgsXkoQ9cVtYTn4TVshmFdFmpQJUvic32SiabjtqW5IgtSlxUrK8jGH7F95Gw0r7qxQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=29)