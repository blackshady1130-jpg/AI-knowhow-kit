---
url: https://mp.weixin.qq.com/s/T6hIWj595TwcuYXC9uxKjg
title: "Scale AI：大模型还需要数据标注吗？"
description: "Scale AI是观察AI行业机会的绝佳生态位。"
author: "拾象"
captured_at: "2026-03-08T12:09:33.071Z"
---

# Scale AI：大模型还需要数据标注吗？

![图片](https://mmbiz.qpic.cn/mmbiz_gif/3tHNibnJ2jgxrs4lU61ibpD95X1296icdVhiayicI129TjVsAic2WT0BRGZE4JLYe9H0kY0SFVyuxvBAnzUiaDr8F7HSg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgxrs4lU61ibpD95X1296icdVhopU05icOaMQaCIxEQCZCAtaTq9TMMxa392sBUicllnfHyyOKQbaref6g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgxrs4lU61ibpD95X1296icdVhsSK1NTVQOvjFytdnHFJ6yM7pu8bLsdzicHHBStzxPbh2TnUPr2aK86w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

作者：Kefei、Haozhen

编辑：penny

排版：Mengxi

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgxrs4lU61ibpD95X1296icdVh49R2cO6VefiboNIAia8rtSF3E6PxSR6XzrTQ9oIVgO2heaIFFDgiaUP5g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

我们在 2021 年 7 月编译过一篇[**关于 Scale AI 的文章**](http://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247484072&idx=1&sn=6e491023a3208cc9d0206bfddb598570&chksm=ce98bd36f9ef342025e1310bdd40307c3e39fdecfbb246da0b28ae23097bd5206ede9d893040&scene=21#wechat_redirect)，但在过去一段时间，AI 行业每天都在发生十级地震，行业价值链也发生变化，因此我们认为有必要重新审视此前研究过的重要公司，所以把 Scale AI 拿出来重新研究。

Scale AI 2016 年成立，创始人为 Alexandr Wang 和 Lucy Guo，Lucy 现已离开公司。Scale AI 2019 年跻身独角兽行列，当前估值 73 亿美金，ARR 接近 3 亿美金。Scale AI 核心业务为数据标注，从自动驾驶场景起家，后切入政府、电商、机器人、大模型等场景，分别对应着过去 AI 行业几次大机会的出现。受益于 Alex 超强的个人能力及超强的团队执行力，**Scale AI 在每波大趋势到来时都能快速捕捉机会，推出相应的产品，在细分领域迅速做到极高的市场份额。**

**目前，Scale AI 正非常激进地切入 MLOps 和 LLM 领域，提供各类工具、平台和服务。**包括电商场景的图片生成工具 Scale Catalog，大语言模型开发者工具平台 Scale Spellbook，以及合成数据产品 Scale Synthetic 等等。但从调研结果看，这些新兴业务只是 Scale AI 寻找第二增长曲线的一些尝试，产品销售情况并不理想，**最后能有稳定需求、贡献主要收入的还是数据标注业务。**

除了更新公司业务情况，我们还针对数据标注在大模型中扮演什么角色、数据标注的商业模式、Scale AI 公司治理问题以及 Scale AI 未来发展情况等重要问题进行了讨论。

**另外，我们认为 Scale AI 是观察 AI 行业机会的绝佳生态位。一旦行业有新动向都会体现在 Scale AI 的产品线中，且公开可见。Scale AI 的产品更新动态非常值得关注。**

**以下为本文目录，****建议结合要点进行针对性阅读。**

**👇**

01 行业

02 产品

03 团队

04 竞争

05 当前结论与判断

**01.**

**行业**

**行业介绍**

**数据标注（Data Labeling）为 Scale AI 的核心业务。**数据标注位于模型开发的上游阶段，该过程需要先识别原始数据，然后为该数据添加一个或多个标签。数据类型包括结构化数据和非结构化数据，后者包括图像、视频、3D（LiDAR、雷达等）、文本和音频等。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*来源：Scale AI 官网*

**数据标注的核心是质量和效率，对于数据标注的客户公司而言，数据标注并非公司核心业务，外包意愿强。**客户标注数据主要通过内部自建团队、众包平台、与第三方数据标注创业公司合作。该赛道玩家除了 Scale AI 之外，还有 Dataloop、SuperAnnotate、Labelbox、Snorkel、V7、Appen 等。同一客户公司内部的不同部门，可能会根据不同的需求和场景选择不同的数据标注玩家。

早期，数据全部由人工手动标注，以构建和积累机器学习模型的训练数据集。尽管耗时且成本高昂，但手动标注数据确实在准确率等方面具有优势。**数据标注公司往往在菲律宾、肯尼亚、委内瑞拉等劳动力价格较为低廉的国家或地区寻找合适的数据标注人员。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

随着机器学习模型的发展，自动化数据标注的准确性提高，可以使用模型来辅助人工标注，比如模型预处理数据再发送给标注员；或人类作为审核员，审核并纠正模型给出的标注结果等等。与纯手动标记相比，AI 辅助标注加快数据标注的速度。**目前，Scale AI 等数据标注公司都在努力减少数据标注过程中的人工参与比例。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

上述两种方案是目前数据标注的主要形式，至于未来数据标注能否全部由模型代劳，我们目前的判断是 No，成熟场景也许可以，但未来总是会不断有新的场景出现，**新事物往往需要先通过人工标注以积累数据、例子，然后才可能训练出可自动完成标注的模型。**

**大模型是否还需要数据标注**

在此前，机器学习需要有监督学习，需要标注大量数据。随着模型逐渐变大，对数据量的需求变大，标注数据的时间及成本变得无法控制，高质量的标注数据的生产速度难以满足大模型的需求。但无监督学习出现后，机器学习不需要明确目的的训练方式，也无法提前预测结果，因此不需要标注数据。强化学习也不需要数据标注，强化学习的反馈不是通过标签或数值，而是通过奖励机制来学习一系列行为。

**预训练模型实现了有监督学习到无监督学习的跨越，**OpenAI 的 GPT-1 到 GPT-3 也一直采用此路线，因此在过去一段时间内，不少人担心数据标注在大模型时代的价值。但 ChatGPT 出现后，该顾虑有所缓解，ChatGPT 使用强化学习和人类反馈来使模型更好地与人类指令保持一致，即 RLHF (Reinforcement Learning from Human Feedback），这其中会涉及到非常多的数据标注工作。

**RLHF 的数据标注与此前的用低成本劳动力完成的简单数据标注工作也有所不同，需要非常专业的人士来写词条，针对相应的问题和指令，给出符合人类逻辑与表达的高质量的答案。**据称 OpenAI 内部招了几十名 PhDs 来做 RLHF 的标注，Scale 作为 OpenAI 的上游供应商，同样招聘了几十名 PhDs 在为 OpenAI 提供此类服务，具体的分工是 Scale 更多完成标注的动作，而 OpenAI 更多是进行质量检测。标注数据是 ChatGPT 效果区别于其他竞争对手的原因之一。Google 一位技术专家也表示，在 ChatGPT 出来后，Google 也在针对数据标注问题进行反思。

**02.**

**产品**

**产品 Update
**

Scale AI 核心业务是数据标注，除此之外还有非常丰富的产品线。**产品主要分成 4 大类：数据标注（Annotate）、管理和评估（Manage & Evaluate）、自动化（Automate）和合成（Generate）。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Scale 从自动驾驶领域的标注起家，**在自动驾驶、地图等行业表现很好，两年前，公司 80-90% 的订单都来自自动驾驶（2D、3D、激光雷达等），该比例近年有所下降。**事实上，Scale AI 的标注产品研发及销售情况与底层的行业趋势及各行业发展情况有很大关系，在自动驾驶之后，Scale 的数据标注订单还来自政府、电商（零售商品目录）、机器人、大模型（RLHF）等领域，分别对应过去几年 AI 行业几波大的趋势和机会。**每波大趋势将要到来时 Scale 都能很敏锐地捕捉到信号，快速招聘相应的人才，推出相应的产品，在细分领域迅速做到极高的市场份额。

除了数据标注外，值得关注的产品还包括：Scale Catalog、Scale Spellbook、Scale Synthetic。

**• Scale Catalog** 主要针对电商和零售企业，除了提供标注服务，还能自动生成产品图，是 Scale 切入 Generative AI 应用领域的一款核心产品。

**• Scale Spellbook** 是 Scale 近期投入较大的业务，汇集了 Scale 的核心人才，做一个基于大语言模型的 to 开发者的工具平台。

**• Scale Synthetic** 是合成数据工具，随着模型参数不断变大，模态不断丰富，对数据量的要求越来越高，真实数据量已无法满足需求，合成数据开始受到关注。

**从 Scale 的产品拓展情况来看，Scale 正非常激进地切入 MLOps 和 LLM 领域，提供各类工具、平台和服务。**不过这只是 Scale 寻找第二增长曲线的一些尝试，产品销售情况并不理想，最后能有稳定需求、贡献主要收入的还是数据标注。

**客户与商业模式**

**Scale 的标注工人主要从委内瑞拉、肯尼亚、菲律宾等工资水平相对较低的国家招聘，客户主要为美国 enterprise 企业，商业模式就像全球化套利，毛利较高。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*来源：Scale AI 官网*

主要客户名单如下：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

商业模式方面，Scale 官网针对每款产品给出了标准化定价，定价模式为 Consumption-base 的模式。如 Scale lmage 起价为每张图片 2 美分，每条标注 6 美分；Scale Video 起价为每帧视频 13 美分，每条标注 3 美分；Scale Text 起价为每项任务 5 美分，每条标注 3 美分；Scale Document Al 起价为每项任务 2 美分，每条标注 7 美分。除此之外，还有针对 enterprise 的收费方式，即根据具体的企业级项目的数据量及服务进行收费。

**由于 Scale 的大部分客户都为 enterprise 客户，因此实际上大部分收入均为项目制收入，客单价几十万美金至几千万美金不等。Scale 2022 年收入预计为 2.9 亿美元，毛利约为 70%。公司 2021 年 4 月完成 $325M 的 E 轮融资，投资者包括 Dragoneer、Greenoaks、Tiger Global 等，估值达 $7.3B。**

**03****.**

**团队**

Scale AI 于 2016 年诞生于 Y Combinator 创业项目，创始人为 Alexandr Wang 和 Lucy Guo（2018 年 Lucy 离开 Scale AI，保留 6% 股权），两位创始人技术背景深厚。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Alexandr Wang 出生于 1997 年，2014 年加入 Quora，并在 Quora 上结识 Lucy Guo，高中就收到很多硅谷科技公司的 offer，后在麻省理工学院攻读机器学习专业，选修的全是研究生级别的计算机课程，一年后毅然从麻省理工辍学。**2016 年，Alexandr Wang 和 Lucy Guo 在 YC 期间创办 Scale。**

Alexandr Wang 在 2011 年美国数学人才搜索 (USAMTS) 中获得铜牌，在 2012 年获得金牌；2013 年在美国数学奥林匹克竞赛中进入全国前 30 名，同时在 Who Wants to Be a Mathematical 比赛中获得第三名；2014 年参加了美国国家物理奥林匹克竞赛 (USAPhO) 并进入半决赛，在 2018 年登上了“30 under 30”的榜单。

**Alexandr Wang 的履历非常亮眼，但大家对他的评价褒贬不一。**他非常聪明、自信，能力强，善于维护外部关系，花费大量时间与硅谷关键人物建立关系。他也十分擅长 branding 和 marketing，塑造很好的个人形象和企业形象，有观点认为 Scale 与其他竞对的差异性主要来自于 Alex 的宣传炒作，为公司带来了大量订单。但或许是因为年纪太小的缘故，Alex 管理公司的经验相对欠缺，公司内部管理较为糟糕，很多人才流失或不愿加入 Scale，企业内部也存在各类矛盾。我们在几位离职高管访谈中听到了非常负面的评价，但也在不少员工访谈中感受到部分员工对 Alex 发自内心的欣赏。

团队整体方面，Scale 整体执行力非常强，工作节奏和企业文化非常激进，偏好招顶级院校的应届毕业生，聪明、勤奋、执行力强、肯加班，Scale 的“卷”在硅谷非常有名。

**04.**

**竞争**

**Scale 的竞争对手包括：公司内部自建的数据标注团队；谷歌、微软和亚马逊等科技大厂的数据标注服务；数据标注创业公司。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**类型一：**

**公司内部自建的数据标注团队**

**由于某些数据比较敏感，有的公司会选择内部自建数据标注团队，作为 Scale 等外包方案的补充。**例如 Airbnb 使用内部数据标注产品来标记隐私数据，并用于公司内部的机器学习模型，但是对于不敏感的数据，Airbnb 通常会外包给第三方供应商进行标注。

原因有三：

**•** 第三方供应商做数据标注可以比 Airbnb 内部自建团队更便宜；

**•** 第三方供应商具有灵活性，可以根据 Airbnb 的需求灵活调整；

**•** 数据标注并不是 Airbnb 的重点业务，第三方供应商的工具可以更准确高效地完成标注。

**类型二：**

**谷歌、微软和亚马逊等科技大厂**

**对于 Scale 而言，这些科技巨头既是客户，也是竞争对手。谷歌、亚马逊、微软等科技大厂比其他任何供应商都具有优势，因为规模效应的存在以及头部公司拥有广泛的产品集合。**例如，Scale 在 AWS 上处理和标注数据，如果客户想把 Scale 标注的数据储存在 S3 中，需要给 Scale 开通访问权限，再由 Scale 将标注好的数据放入客户的 S3 存储空间中，这一系列操作会造成额外的成本。但如果客户数据本来就存储在谷歌、亚马逊和微软的云平台上，并使用他们的数据标注产品和服务，则无需进行访问授权、移动数据等步骤。

此外，微软、亚马逊、谷歌等科技大厂都希望客户能够在一个平台解决所有问题、采购他们的所有产品和服务，因此会在一揽子产品中，针对某个单一产品给一些折扣，甚至直接提供免费的工具，这会对 Scale 造成竞争压力。但微软等科技大厂大多只提供软件和工具，不提供人力服务，导致客户必须自己承担人力工作。而 Scale 提供人工标注数据以及其他的人力服务，在与科技大厂竞争中也具备一定的独特优势。

**类型三：**

**数据标注创业公司**

如 Dataloop、SuperAnnotate、Labelbox、Snorkel、V7、Appen 等。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Snorkel**

Snorkel 提供了大量模板来让用户创建标注任务，也提供了托管服务。Snorkel 与 TensorFlow、Kubernetes 和 DAS 都有很好的集成。Snorkel 和 Scale 都是数据标注领域较大的供应商，有专家认为 Snorkel 未来不会在与 Scale 完全相同的赛道中，但两者都会有不错的增长。相比 Scale，Snorkel 的优势在于更专注于文本和 NLP，以及成本较低，所以用户如果只是处理文本数据，一般会选择 Snorkel 而不是 Scale。Snorkel 的劣势在于视频、图像、地图等处理能力非常有限。

**SuperAnnotate**

SuperAnnotate 是数据标注行业重要的供应商之一。功能丰富，允许用户以 Python 等格式提取不同的标签，使用 SQL 对图像进行大量搜索，并将 SQL 与数据库合并。相比 Scale，SuperAnnotate 的优势在于医疗行业和工作流程。在医疗方面，SuperAnnotate 符合 HIPAA 标准，而 Scale 并不符合。SuperAnnotate 在创建工作流方面能力更强，比如提供指令，在此方面，Scale 正在追赶，但并没有达到 SuperAnnotate 的水平。但整体来看，SuperAnnotate 的劣势在于标注质量不及 Scale。

**Labelbox**

Labelbox 的商业模式与 Scale 略有不同，Labelbox 是给用户提供平台，用户可以选择自己进行数据标注或使用其他服务，但客户需要采用 Labelbox 平台作为内部数据标记工具。Labelbox 通过美国国防部安全审查，也与各种组织展开合作，例如，Labelbox 与 GCP 是合作伙伴关系，正在推动 GCP 云和谷歌云。

**05.**

**当前结论与判断**

**为什么看好**

**1\. 数据标注外包需求确定**

**数据标注外包需求明显，给创业公司很大的发挥空间。**

一方面，从客户角度考虑，数据标注对于 AI 公司的员工而言属于脏活累活，会占用他们大量的时间，分散他们在算法等核心环节上的注意力，从主观角度看他们不愿意把时间花在标注上。

另一方面，从 ROI 角度考虑，大部分的数据标注工作对标注员的要求并不高，即美国的工人可以完成的工作肯尼亚的工人也可以完成，且质量差别不会很大。因此，如果不是特别隐私的数据、或不需要类似 RLHF 场景的语义理解等其他能力，通过第三方交由低成本国家和地区的劳动力来完成标注工作 ROI 是更高的。因此，数据标注外包的需求十分明显，创业公司长期有机会。

**2\. 数据标注赛道的头部玩家，头部效应、品牌效应强**

Scale 是数据标注赛道的绝对的头部玩家，如果我们认为人工标注和“自动化+人工”的标注方式在未来 5-10 年内会长期存在，那么目前来看 Scale 会一直保持领先。**从最真实的客户和订单来看，美国的 enterprise 客户大多只认可 Scale 作为他们的第三方数据标注服务商，Scale 的客户可以说是美国 AI 各细分赛道的皇冠上的明珠，拥有最好的客户 base。**

**Scale 的销售团队在 pitch enterprise 客户时，所遇到的竞争对手几乎只有“大厂内部自建的团队”这一个解决方案，几乎没有遇到其他创业公司。**只有在 SMB 市场或面向非头部企业的销售中会遇到其他创业公司。**头部效应和品牌效应非常明显。**关于品牌效应还可以补充一个观点，有客户说到这样一句话：“Scale 和其他数据标注公司就像 iPhone 和安卓的关系。”Scale 品牌效应的形成也离不开 Alex 本人及团队极强的 PR 和 marketing 能力。

**3\. 规模效应已显现**

**数据标注赛道有规模效应。**客户对数据标注的关注点主要在“质量”和“效率”两个方面，由于数据标注不是高技术含量的工作，**因此经验对质量和效率的提升就起到关键作用。这里的经验又包括工人标注数据的经验，以及 Scale 对整套流程和体系的管理经验。**经验一定程度上也与规模和数量有很大联系，规模越大，标注的数据量越多，经验就越成熟、越丰富，标注数据的质量和效率就越高。

作为赛道的头部玩家，以及与 enterprise 客户合作，Scale 的订单量及数据量与其他竞对相比要大不少，再加上 Scale 在每波趋势刚刚兴起的时候，都能快速进入新兴领域，更早地获得“经验”，后续企业竞对便很难追上。

**另一方面，Scale 将人工标注的经验沉淀为自动化的解决方案，在行业发展早期采用人工标注的方式，当行业成熟时已经能够训练出适配特定领域数据的自动化标注模型，变成“自动化+人工”的解决方案，大大提升效率。**订单量和数据量足够大也能够更快速和高效地优化标注模型。因此，Scale 的规模效应非常明显。

**4\. 创始人与团队综合实力和执行力强**

关于 Alex 在团队部分也有所介绍，一位非常聪明、激进、好胜心强的年轻人，且 **Alex 不仅在技术方面有很强的天赋，在商业方面也有很强的能力，比如运营、品牌、营销、销售、社交能力等等，综合实力强劲。Scale 团队综合能力也非常优秀，尤其是运营能力，对数据标注整套流程和体系的管理。**Scale 的流程与管理体系、经验管理效果和效率都明显优于其他竞对企业，包括如何管理数据工人、如何给他们分工、如何进行激励或惩罚、如何检查质量、如何将数据交到客户手中、如何服务客户、又如何根据客户反馈重新标注数据提升标注质量等等，整个链路非常复杂，Scale 的高材生们能够把整套流程 handle 好，每一个环节都极其高效、流畅、准确。而 Alex 也在很多事情上亲力亲为，或亲自监督。团队综合素质和执行力非常强。

**为什么不看好**

**1\. 企业管理风险**

**创始人与团队既是亮点也是风险。**如团队部分所说，我们对创始人和团队进行 reference 后发现大家对 Alex 的评价十分极端且割裂，欣赏 Alex 的人觉得他是全能天才少年，不欣赏 Alex 的人又觉得 Alex 在公司管理方面存在非常大的问题。这可能是我们最近两年的研究中遇到的第一个 reference 结果如此割裂的项目。

企业管理和企业文化方面，Scale 给年轻人足够大的发展机会和发展空间、足够快速和清晰的上升的机会、足够多的激励，但同时在处理老员工的关系上存在很多问题，因此这其中存在较大的冲突与矛盾。此外，Scale 高强度的工作、激进的管理方式，也导致了严重的人才流失，或是让很多人才在选择公司的时候就望而却步。**我们认为企业管理与企业文化是 Scale 最大的 risk。**

**2\. 需求和增长风险**

**数据标注需求受具体行业周期影响大，当每波 AI 趋势爆发的时候，就会有一次极其陡峭的增长，但当行业发展趋于稳定或趋于成熟后，增长曲线将开始平缓，直到下一波大趋势的爆发，需求和增长波动较大。**并且 Scale 多为项目制，项目的数量、周期、稳定程度和订单金额都有很大的不确定性，较难预测。数据标注业务本身重人力，靠堆人完成标注工作，属于施工队生意，短期内人效较难提升，也难有持续复利。

**另一方面，Scale 团队一直在努力寻找第二增长曲线，在 MLOps、LLM tool、Generative AI 等方面均有涉及，但目前从结果看差强人意，依然没有找到第二条稳定的增长曲线。**如果长期依靠数据标注业务，天花板将受限。如果想象空间和稳定的增长不存在，那么公司将来到二级市场将承担低估值的风险。

**3\. 供给端风险**

Scale 此前布局供给端的国家和地区近年人力成本上涨速度快，最典型的是菲律宾等东南亚地区，菲律宾劳动力价格上涨后，Scale 也很少再到菲律宾招人。供给端成本上涨，Scale 的毛利空间受挤压，而毛利是否稳定上升也是公司上市后投资者最看重的标准之一，如果毛利下降是非常不利的信号。除此之外，供给端招聘流程的规范性和稳定性也是我们关心的问题。

**最后补充一个观点，我们认为 Scale 是观察 AI 行业机会的绝佳的生态位，一旦行业有新动向 Scale 都能很快捕捉到信号，并快速推出相应的数据标注产品，且公开可见。Scale 的产品创新值得持续关注。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

延伸阅读

The Age of AI：拾象大模型及OpenAI投资思考

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

LangChain：Model as a Service粘合剂，被ChatGPT插件干掉了吗？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Runway：AI Native Tools工厂，视频生成领域的字节跳动

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgxrs4lU61ibpD95X1296icdVhPjo0r9NLEYicJD4ib7hfKTU4fTOagGyAmkBemjbhBeiayVkpmRR2SwOww/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=23)

Jasper：早期GPT生态最大赢家，是否会被边缘化？

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgxrs4lU61ibpD95X1296icdVhPjo0r9NLEYicJD4ib7hfKTU4fTOagGyAmkBemjbhBeiayVkpmRR2SwOww/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=25)

OpenAI创始人的AGI预言：AI Safety、Scaling laws与GPT-20

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgxrs4lU61ibpD95X1296icdVhPjo0r9NLEYicJD4ib7hfKTU4fTOagGyAmkBemjbhBeiayVkpmRR2SwOww/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=27)