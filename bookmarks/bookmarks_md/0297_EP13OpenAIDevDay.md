---
url: https://mp.weixin.qq.com/s/r9knwX8ftxKkhiRnSih6YA
title: "EP13 OpenAI DevDay带来大变化"
description: "DevDay让Chatbot出现了质变，但开放的生态很难再被信任"
author: "AI芋圆子"
captured_at: "2026-03-08T11:15:15.706Z"
---

# EP13 OpenAI DevDay带来大变化

**关注共识粉碎机，获取历史讨论会纪要**

**关注M小姐研习录对中国/硅谷的最新软件思考**

我们尽量每隔一周都会组织不同领域的AI讨论会，覆盖软件行业的所有细分。为了保持一个活跃的讨论环境，对参与人群会有限制。

下一期将定于**12月****10日上午10点**，主题为**《AI如何颠覆客服/电销》**，形式为**线上闭门讨论会**，详细的下一期内容和报名形式请见**文末的阅读原文**。

**本期讨论会参与者：**

**Monica老师（主持人）**，真格基金，公众号M小姐研习录，OnBoard播客主理人

**郭振老师**，Shulex CEO

**陶芳波老师**，心识宇宙MindOS创始人

**Iris老师**, 大模型创业，前TikTok PM

**Yixin老师**, Google Cloud Vertex AI 

**李林杨老师**，阿里云人工智能平台AI推理产品

**蓝雨川老师**，零一万物业务负责人

**王晓妍老师**，VC投资人

**黄凌云老师**，平安AI产品经理

**陈将老师**，向量数据库Zilliz AI云平台负责人

**Philip老师**，Aurora AI Infra

**Manta老师**，万木投资

**高宁老师**，Linkloud发起人，公众号我思锅我在，OnBoard播客主理人

**Yujia老师**，微软Copilot产品经理，共识粉碎机主理人

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**1** 成本降低带来的变化

---

**成本收益立刻就能显现
**

-   Turbo的成本优化立刻就能见到节省，OpenAI和微软也已经开始给大客户试用了。

-   LLM创业者可能对于训练和测试场景的花费不太敏感，但对推理场景的性价比都比较在意

-   性价比优化后，**一些非常关注ROI的AI场景，例如Serving类的客服/销售都会明显受益。**

**同时也拉开了和其他大模型的差异**

-   AWS-Claude、Google的模型在效能上离GPT4就已经有比较大差距，随着GPT4大幅降本，差距进一步拉大。

-   **过去见到企业因为成本和latency的原因选择其他模型**，或者自建Llama等模型，这次会议之后可能会回流到GPT4。

**模型的成本优化来自于精度、硬件、模型架构等**

-   **从精度角度做优化：**GPT最开始发布时候是FP16，到今天已经到了Int8，甚至可能新版有可能量化到了INT4，单精度角度就下降了75%成本。

-   同时在模型架构层还做了极致的优化，包括**算子优化、开源框架优化**等。

-   在大规模开放给客户使用后，可能也配合微软做了**资源超卖**。

-   **训练的卡集群也可能和推理的卡集群做共享**，进一步降低成本。

-   目前也有推测可能在**Speculator Decoding**和**Continuous Starting**进行了优化。

-   从硬件平台来看：A100是2020年推出的，折旧期基本上快过了, 会计上计入的成本越来越少，很多卡对应的收入变成净利润了。

**在成本降低的同时也见到了延迟的优化**

-   目前评测下来，**在成本下降的同时也见到了延迟降低**，可能与参数的优化有关。上一代Turbo版本就能明显感受到。

-   一些简单的问题已经可以做到**2-3s回复**，移动端如果网络信号比较好，体验已经非常好了。

**2** Context升级128K带来的变化

**Agent可以服务更长，处理更复杂场景**

-   Agent之前的核心问题就是无法记录超长文本，**导致多数服务时间不能超过15分钟**，15分钟以后尽管做了很多summary和聚合，也无法保证超长文本和超长链路的对话和学习。

-   例如医疗问诊、心理咨询、小孩子的英语和语文教育，都卡在文本长度上。在此次更新后，**这些场景有机会达到1小时以上的服务**，会在使用体验上有明显的不同。

-   在质量上，**过去5-6个chunk模型还能搞清楚，但多了以后模型就会confuse**，context变长后质量也会有明显提高。

**以养老智能客服的需求举例**

-   **老人面对客服和年轻人不同，交流会夹杂更多的情感需求**，在要求服务的同时喜欢和客服人员聊天，而且有时话语稍多。对话中的有些闲聊没有提供有效信息，甚至是误导，如果基于大模型设计智能客服系统，作为底座的大模型的理解、纠错和召回能力就非常重要。

-   过去chatgpt 4K上下文长度预估可以做到5-8轮的沟通，很可能无法充分进行多轮交互。现在拓展到拓展到128K以上后，预测基本可以满足实用场景中更多轮次的交互，比如可以做到20轮以上的沟通，辅之以大模型本身的理解和生成能力, 对客户体验的提升将会是立竿见影。

**3** 低代码开发带来的变化

**Builder Mode拓宽了开发人群**

-   这次最大的亮点是Builder Mode，提供了一套low/no code的工具，抓住了普通用户的易用性诉求和需要有完成任务的成就感诉求。

-   很多PM或者Business People不具备非常高的代码能力，但是有创意，现在可以**半小时就做出Demo App**，省去了大量Demo搭建的时间，可以更快到用户侧去做测试。

-   实际拓宽了AI的开发人群，可以迅速实现产品迭代，促进新产品想象力的产生。过去各大云厂商的目标是开发者人群，而不是去吸引有启发式思考的这部分新用户。

-   另外也可能成为成熟产品的补充，可以让客户将他们的知识和应对方法，结合开发者公司的知识库配合起来搭建Agent。

**Builder Mode虽然降低了开发门槛，但能力上没有提升**

-   **能力上没有超出RAG+API调度**，所以像一些涉及深度的、复杂的任务自动化编排，类似于AutoGPT的流程，在这个版本里仍然没有涉及。

-   所以GPTs更适合做一些浅度的、好玩的应用，做出来的产品也可能更像是一个中间态产品。

-   **开发者公司可能会将GPTs当做探索，做一个60-70分的产品出来，如果用户侧performance好，会花更多的精力将其做成独立产品。**

**GPTs方便个人搭建自己的助手**

-   方便搭建customized的助手，之前要重复prompt，现在可以节省很多时间。

-   嘉宾老师中从投资人到工程师都有搭建个人助手的案例，解决的问题从辅助研究、翻译到整理Pytorch代码等都有。

**创业者需要避开过渡场景，核心关注自己的Know-how和Domain Data**

-   通用任务的场景相对比较危险，通过GPT降低开发门槛降低后很容易同质化。

-   垂直场景，非常关注自己的Know-how和Data，找到特定的场景提高效率。

-   以电商AI客服为例，帮助客户进行产品使用过程中的故障/问题处理等有很强的场景属性，需要进行大量的意图识别，强化Function Call，从Agent的能力来说。以及怎么做好自动回复的召回。这一块通过和行业知识的结合，会有非常大的需求和业务增益。

**4** GPTs生态带来的变化

**OpenAI不像是在制定标准，更像是封闭生态**

-   未来的数字世界，每一个服务甚至每一个人都可能会以AI Agent，甚至是AI Identity的方式来构建，然后通过AI Agent/AI Identity作为proxy来形成新的互联网。

-   回溯过去第一代互联网，在制定了标准协议后，每个人都可以去中心化地在上面部署，让一切人都可以访问。

-   但到了第二代移动互联网时期，最后形成了苹果为代表的几个生态，通过中心化的机构去运营生态，并在中间对应用抽税。

-   DevDay上的OpenAI更像是**想做第二代的苹果**，其不只是定义了Agent标准，更像是在搭建一个封闭的生态。

**GPTs成为AI公域流量的入口，但AI创业者最应该关心私域**

-   类似TikTok和Youtube都有自己的Creator Economy，也同时会分成公域流量和私域流量。

-   GPTs现在就是AI行业最大的公域流量入口，所有的GPTs数据也会被OpenAI获取到，Builder也很关注数据去提高Performance。

-   对于OpenAI来说，公域入口是获取Use Case和Vertical Data的绝佳方式，也是帮助OpenAI脑暴的好方式。

-   对于创业者来说，最重要的是下一步如何将用户数据导入私域流量，将用户关系和用户粘性把握在自己的手上。

**GPTs的应用量大，但有用的很少**

-   目前有13,000个GPTs（截止讨论时间），其中中文大概是400个。

-   目前以轻量和简单逻辑的工具为主。Twitter上经常有“非常好用的GPTs”宣传，但实际上多数都是一句话就能完成的，很难解决实际中复杂的问题。

-   尝试体验了不同垂类的应用，例如金融行业，但因为对开发者不了解，无法充分信任使用的数据，对输出的结果也不够信任。

**类似的Marketplace公司更需要往模型侧探索**

-   智能体与未来的智能世界是互联网连接的全新概念，它可能分为大后端和大前端。大后端是专业的智能体服务，而前端则是开放的互联网，可以在实现互相连接。

-   OpenAI将GPT当作自己的前端，GPTs当成自己的后端。Marketplace创业公司更需要往前端走，更有机会做差异化。比如可以更加关注与人亲近，有一些领域的关注例如心理疗愈，或者说对个人的记忆做更精细化的管理。

-   在后端上很难找到具有差异化的机会，都在OpenAI的射程之中。

**5** RAG工具带来的变化

**RAG更新不算新鲜，主要面向2C用户或SMB场景
**

-   OpenAI这次加入Retrieval能力在意料之中，之前国内的智谱AI在几个月前已经加入了。

-   目前主要是设计给单个用户和小体量用户，对很多功能有限制，例如一个号**只能存20个文档，每个文档最大500兆**这样。

-   如果用户体量大，或者客户经常上传文档做召回，OpenAI目前提供的自研工具都不够用。

**性价比不高，但质量基本做到持平**

-   **价格不便宜：**RAG+知识库方案对比开源框架+向量数据库没有竞争优势。

-   **质量持平：**目前通过开源数据集去评测召回质量，跟市面上的Llama Index、Langchain等水平都差不多。**但不确定上规模后的对比差别**，目前OpenAI明显限制了规模上限。

**对Infra的影响看OpenAI的投入**

-   RAG方向还很新，不像WEB检索已经做了20年了，**还有非常多可以长尾优化的地方**，例如用户检索时候的意图识别等。

-   因为技术爬坡周期才开始不久，主要取决于OpenAI愿意在此事上投入的精力，如果卯着劲投入足够多资源，那肯定会有突破。如果抱着更开放的心态，那对目前的开源架构不会有什么印象。

**RAG可能会把数据带到OpenAI生态**

-   RAG可能会进一步加强OpenAI的数据引力，让更多客户出于方便将数据带去模型所在的地方。

-   但对于有比较强合规要求的客户，可能不会这么做，更多通过类似Llama Index的方案作为Implementation。

**除了OpenAI外，现有的RAG仍然有很多挑战**

-   **Out of box：**很多客户在做RAG的时候仍然需要精调，例如用到网络安全数据的时候，很多名词和映射LLM很难搞清楚。**但在做精调的时候，企业端很容易出现质量问题，导致最后模型的可用度无法达到预期。**如果在RAG工具上能够更加直接可用，把精调的流程涉及的工具链也完善出来，可用度会更高。

-   **结构化数据：**客户有很多数据仓库、Tabular（扁平数据）和时间序列数据，**现有的RAG工具主要在非结构化数据上支持很好，在结构化数据上还很缺失**。例如对财报表格进行检索，需要找到利润情况，很难准确检索出来，因为更多看的是整体情况，而不是具体信息。客户对此有非常强的需求，这对传统搜索很简单，但对RAG很难。

-   **多模态数据：**客户可能希望将Json、图片等非结构化数据和表格等结构化数据做到同一个Embedding，也还在探索阶段。目前多模态检索在文字+图片的情况已经进步很大了，可能很快就能赶上单模态内的检索。

**6** Agent现在怎样了

**Agent仍然面临很多挑战**

-   Reasoning和Planning，以及长链路后的准确性仍然面临非常大的挑战。

-   Agent公司的函数也可能非常复杂，50-100个参数的函数都会有，对于Function Call的要求很高，现有的大模型在Out of Box上也很难支持。

-   **目前主要见到一些简单的Case，例如在车中用户喊冷，Agent可以做出开空调的反馈；以及订机票、订行程等。**

-   国内在工业制造上已经见到了一些Agent Case，例如做机械臂和机器人的公司，举个例子用机械臂来调咖啡。

**现有的Agent平台还相对缺失**

-   海外的**Fixie平台**，很多客户基于此订机票、订外卖，对各种SDK都实现了很好的定制化，非常方便，并且易于评测落地效果。在使用体验上超过AWS Bedrock这些。

-   国内还相对空白，可能是创业机会。很多客户非常有需求，例如机械臂公司做Agent很有门槛。

**【讨论会】**

第十三期讨论会我们将于**12.10上午 10 点**举办**《AI如****何颠覆客服/电销****》**讨论会。本期讨论会预计为线上闭门形式。

在DevDay后，**Chatbot的成本、延迟以及Context长度都有了大幅优化**。我们计划与行业内做AI客服/销售的创业者/从业者们一起聊聊现在的可用性和未来的机会。

**欢迎生处AI+客服/电销以及其他Chatbot的创业者和从业者与我们一起讨论，也欢迎推荐相关的朋友一起讨论。**

如果有兴趣，请点击**阅读原文**的腾讯问卷报名链接。

所有的讨论纪要，请关注公众号“共识粉碎机”，在功能界面“芋圆子”→“讨论纪要”。

感兴趣加入后续讨论会活动的，请私信后台**“微信号”、“工作单位”、“擅长什么AI方向的讨论”。**

[《EP01：AI如何颠覆数据库讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485464&idx=1&sn=13d6039e278e1e254ec2cbfc36c77b4b&chksm=ea5ad1e0dd2d58f6d4b777e90c79c633de9356763f6ca956b541f58ec036e0547d0b02425721&scene=21#wechat_redirect)

[《EP02：AI如何颠覆游戏讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485766&idx=1&sn=92e349bdb9db3301f555bcfd0b7dd9ce&chksm=ea5ad0bedd2d59a8b6ba0b70c4ecfb87bbb671e15f0f68224af90d651ed121acebfb9d4eb8db&scene=21#wechat_redirect)

[《EP03：生成式广告讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485798&idx=1&sn=60a6392ed12497b157a1d965b1497bfa&chksm=ea5ad09edd2d598896f142b74c41e3da4513c09ca772dd1aebde5c6fc5c7d230b7a11597a45f&scene=21#wechat_redirect)

[《EP04：AI如何颠覆办公与CRM讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485819&idx=1&sn=28c92da1fc59b44d4309a71cc94f95a2&chksm=ea5ad083dd2d59957bb4e7c90525365b3e2520ba7212dc221438f25e7679a3103263d90c590e&scene=21#wechat_redirect)

[《EP05：AI时代产品经理的新要求讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485888&idx=1&sn=8bd28ecca119496dee7e56f06e795ab2&chksm=ea5ad038dd2d592e4430d349ab86297301eecef4b7ae22212005752376888b8efc041920c681&scene=21#wechat_redirect)

[《EP06：AI如何颠覆网络安全讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485918&idx=1&sn=980b533e160c8ffe1a8a76f6f517850a&chksm=ea5ad026dd2d59304390d111ad0c475a9cd4296255c31ba1e0762dd88b827bb39b4c5dab5e63&scene=21#wechat_redirect)

[《EP07：AI如何颠覆设计流程讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485979&idx=1&sn=08b3226888aed3a2b6ca8d82de827734&chksm=ea5ad3e3dd2d5af5952b60b9465c86f260199b6f028e320fea82b7183a3d1805f2d92a80c538&scene=21#wechat_redirect)

[《EP08：AI如何颠覆可观测性工具讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485995&idx=1&sn=758d9de3a0e277d3193e81d37617d1f4&chksm=ea5ad3d3dd2d5ac5060d6c6cfdb4c1078089446c34653d6394c1aa83d4b605b63be7d6f4a3dd&scene=21#wechat_redirect)

[《EP09：如何突破英伟达垄断》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486017&idx=1&sn=52397108a65999fd7656261302092943&chksm=ea5ad3b9dd2d5aaf858469d1346e4134db9904d626f45a3d5634c7382c510f72de93df47a3d4&scene=21#wechat_redirect)

[《EP10：AI如何改造传统工业讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486033&idx=1&sn=cefc1d887d689d1fdd7903a7622b46ff&chksm=ea5ad3a9dd2d5abfbe6d3d8fb4e8d55a16c349864783c7bce5cae1e7bce3cf0cade3b2b9d61c&scene=21#wechat_redirect)

[《EP11：AI如何改造推荐系统讨论纪要》。](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486055&idx=1&sn=32f3d75f4fbfda57b8734bbb390e4145&chksm=ea5ad39fdd2d5a89788c97e562a6267ad49c36631fbcdff3c52f236a40ed28502edd1c893a89&scene=21#wechat_redirect)

[《EP12：AI如何重塑教育讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486067&idx=1&sn=3bacd58e2fde79692d3cbb29d96a87da&chksm=ea5ad38bdd2d5a9de9606b9ecf785807f5ee0adc410794dfdf2343a805ee5e26a9c87edebe80&scene=21#wechat_redirect)

**欢迎加入共识粉碎机的活动讨论群，获取更多活动信息**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

---

**【AI如何颠覆软件：你能为AI打工吗】**

****【如何突破英伟达垄断】****