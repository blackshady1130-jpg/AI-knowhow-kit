---
url: https://mp.weixin.qq.com/s/r-J28KbCG-LK9EFWElisVQ
title: "大模型未来三年的十个假设"
description: "进入摘果子的3年"
author: "波太金"
captured_at: "2026-03-08T11:23:43.527Z"
---

# 大模型未来三年的十个假设

**关注共识粉碎机，获取历史讨论会纪要**

文：波太金 小熊猫 芋圆子

2023年是大模型走入公众视野的第一年。共识粉碎机也从这年开始将写作与活动内容都聚焦在AI领域。

4月份，我们写下了第一篇AI大文章《AI如何颠覆软件：你能为AI打工吗？》。

一年后再回过头看，发现多数对了，但也有明显错的。

[

AI如何颠覆软件：你能为AI打工吗？（全网首篇AI+SaaS万字深度长文）

2023-04-03

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/dljQibos6CibbP4ArSHW4K47YkbKXS9SwMCPoEXutPrpnib11oJyM39qGwbJY5vzylDtVQicBU3ywH3DUaIceVDbwg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485067&idx=1&sn=8bf37ff8a7a7aeac7da10c4c87131fef&chksm=ea5adf73dd2d56655d5ae8e7783783b0162c56a1ef99b5b74ee6efdd512d0f18c709f13e2db5&scene=21#wechat_redirect)

对的地方：

-   **大公司几****乎都没有****被小公司弯道超车**，有充足的反应时间调整结构和做并购，有了OpenAI模型底座支持后也很难出现观念上得落后。

-   **数据库没有被颠覆**，AI加速了数据云化的过程，而且都找到了自己的路径参与进PreTrain、Finetune和RAG。

-   **企业搜索没有被颠覆**，并且找到了与单纯VDB+Embedding的不同，在RAG领域做到了差异化

-   **安全没有被颠覆**，虽然进攻端AI带来了更多潜在威胁，大模型体系形成了新的被攻击对象，比如涉及到用户/企业私有数据和大模型交互的信息传递的安全性，LLM也降低了黑客的入门门槛，防守端的产品形态和之前也较为类似，目前看到比较多的是原来需要写基于情报log做威胁分析，现在这个交互部分公司开始加入了LLM作为交互，但这很难说带来了多少产品改革。

-   **ITSM没有被颠覆**，HelpDesk对应的Chatbot成为了第一波AI的Low-hanging Fruit。

-   **AdTech没有被颠覆**，国内的百度，海外的TikTok与Meta都已经看到了生成式广告用例。

-   **流程软件没有被颠覆**，都在Summary和意图识别几个模块中找到了能优化的环节。

没我们想得好的地方：

-   **游戏引擎、流程软件没有被颠覆**，但也没我们想的进展很快。

-   **监控没有被颠覆**，但在大模型环节中提供的价值仍然不明显。

错的地方：

-   **图像创作没有被颠覆**，Adobe找到了设计师二次修改习惯与版权生态，两个差异点。

-   **RPA没有被颠覆**，RPA在内核层面的积累没有因为交互的改善而受到冲击。

-   **Deploy（类似Hashicorp）没有被颠覆**，已经够方便了，好像也没人想去颠覆。

-   **代码库没有被颠覆**，Coding Copilot在无法深入解决上下文的情况下，各家的方案有点差别但不大。

当时我们提到未来一年是赛跑，现在回过头来看：

-   **全都没有被颠覆。**是的，全都没有被颠覆。时代给予大公司的容错空间比10年和20年前大多了，有充足的准备时间。

-   **没有公司再执着于自己的想法，所有Big Player都知道必须抛开包袱，而且做得很坚决。**

《创新者的窘境》中描述的经典情景在2023年没有复现，积极投身研发的成熟企业在面对大模型出现时，还没有出现掉队迹象。**我们还没看到新时代的柯达、百代唱片和西尔斯百货。**

归根到底，**大模型的成长情况在2023年还只能算作是“延续性创新”，随着Agent的继续进化才会到达“颠覆性创新”。**

这是一个无比聪明的时代。因为在这次之前，有过很多反面教材。

**你不能再靠指望大公司犯错，找到弯道超车的机会。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**1** 开始摘Low-hanging Fruit（2024）

---

我们在2023年看到了很多大模型的应用苗头：

-   例如2C场景的ChatGPT与C.AI。

-   在2B场景，我们看到了海外软件公司取得了初步成果，例如Office Copilot、Adobe Firefly、Salesforce Einstein、ServiceNow GenAI。

-   过去在销售客服领域应用很广的Machine Learning场景，也开始向大模型转化。

**在2024年，这些不需要多步推理的场景会随着成本和延迟的改善而真正到摘果子的时候。**

如果将AI产生的价值，以面向的人工智能群体来分：

-   **最简单的是提升工作流中的一个环节：大多数利用Summary的AI产品都是这么做到的。**

-   **剩下来容易的事替换低门槛的工作：**例如客服、审核、助理/实习生，这些会在2024年集中发生。

-   往后难的就是替换更高门槛的工作，这可能不是一两代模型迭代可以解决的。

[

EP14 到了颠覆AI客服的时候了吗？

2024-01-05

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486262&idx=1&sn=39c45a626f49cb7027dc83554c6f91c1&chksm=ea5ad2cedd2d5bd86aa14b2c91e27b22910e572b94905ee5a8d24d02f8a8c852ee4404ed6f2e&scene=21#wechat_redirect)

**我们首先会看到价值替换的会在客服行业：**

-   客服行业在过去已经熟练的应用了规则FAQ机器人和机器学习，大多数的文字客服都已得到应用。

-   随着大模型成本和延迟的优化，大模型客服现在正处于可用/不可用的边缘，很快会进入可用区间。

-   相比规则机器人和传统机器学习模型，大模型客服在整理语料的时候更加节省精力，同时还能兼具情绪安抚和维持客户满意度效果。

**同时我们也会看到替换发生在审核行业：**

-   内容审核行业是一个非常规范严谨的行业，例如字节跳动、快手等内容大厂，已经建立成了超过数万名人员的审核中心，中间有包括机审、人审、复审、交叉审等多个环节。

-   很多公司已经开始探索将大模型应用到审核中，例如Roblox同时有CV模型、ML模型与LLM模型一起优化。

-   相比传统CV模型，LLM可以理解更连贯的视频含义，CV模型只能审核到单帧的物体和动作，但将多帧串联在一起的逻辑需要LLM来识别。

**Semantic Search从23年底正在成为最热门的创业方向：**

-   我们已经看到了法律和金融行业成功的案例，通过总结和搜索大量文档，给客户提供信息建议。

-   同时也看到了企业知识库，成为LLM落地的通用案例，从科技公司到广告公司，再到传统企业，都开始将自身的文档、图片素材、合同通过RAG的方式结合到新一代知识库中，满足员工的查询需求。

-   不光是这些Fancy的海外公司，**在国内我们也看到了医保局、行政服务中心、大学实验室甚至电池厂**，开始采购类似的方案。

-   相比过去SharePoint/云盘，甚至更古老的FTP模型，Semantic Search可以不需要在茫茫多的Keyword里查询，也不需要具体点开庞杂的文档，更加轻量。对于有多模态需求的客户，例如广告设计师，可以通过文字匹配到版权库中合适的素材。

**Copilot作为目前AI SaaS中TAM最大的场景也会收获第一次果实：**

-   我们预计Copilot的渗透不是渐进增长的，而会在第一年有一次迅猛的增长。

-   这来源于Copilot已经成为希望尝试AI客户的首选产品，客户有更高的“AI容忍度”与“AI尝试意愿”，愿意在第一年就购买更多的产品进行测试。

-   但就像先前提到了，Copilot只能做到中间少数环节的提效，其最常用的场景还是会议与邮件场景，信息密度越高的职场人士提效越明显，而更多单向输出的职场人士从中获得帮助在第一代还不明显。

[

EP07 AI如何颠覆设计流程讨论会纪要

2023-08-09

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485979&idx=1&sn=08b3226888aed3a2b6ca8d82de827734&chksm=ea5ad3e3dd2d5af5952b60b9465c86f260199b6f028e320fea82b7183a3d1805f2d92a80c538&scene=21#wechat_redirect)

同样的原理我们也会在**设计行业**大幅看到，创意行业相比其他更加严谨的行业，提高效率也更加明显。

**2** 我们会第一次看待AI带来的Real Economic Impact（2024）

有一个比喻对现在的很多AI产品很合适，**“买一个AI产品就像为员工买一把人体工学椅”**。可能很有用，员工更精神了，但多喝一顿下午茶效果就没了。

2024年要摘的果子和人体工学椅已经截然不同。不再是粗糙的计算为员工提效了多少，而是可以**直接计算企业级别的利润率提升。并且落地成为GDP和资本效率的贡献。**

这非常重要，LLM第一次对世界有了Real Economic Impact。

以客服行业为例，目前普遍的AI客服定价都隐含相比人工客服接近1:10的ROI，这意味着过去在美国一位年薪5万刀的客服人员，在应用大模型产品后成本会降低到5000刀。

如果算笔大帐来看的话：

-   全球1700万客服，将近4000亿美金的客服服务市场。

-   如果按照1:10的ROI，做到30%渗透率就是120亿的市场空间。

-   按照30%来算的话，对于现有的呼叫中心软件行业相当于30%增量。

-   **但对于庞大的客服客户来说，相当于节省了1200亿美金成本。**

节省的成本我们会看到可能会继续投入到市场扩张中，**也可能成为永久的提高一批企业的利润率**。从微观角度上看，很多类型的行业都会因此而永久受益：

-   非标性质的电商行业，例如偏向体验类的酒旅、大件的家具、服务类比如家政/除醛，在购买前都需要进行充分的客服咨询。

-   客服比重高的行业，典型的存在于外卖、打车等利润/GMV很薄的行业，需要非常精细化的运营掏出来一点点的利润，而客服的节省又是精细化迈进得更大一步。

-   而对于交易平台来说，其不仅可以让平台上的商户获得更高的成本节省以进行广告上的再投入，也可以自己探索客服产品成为新的营收点。

[

EP03 生成式广告讨论纪要

2023-05-30

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485798&idx=1&sn=60a6392ed12497b157a1d965b1497bfa&chksm=ea5ad09edd2d598896f142b74c41e3da4513c09ca772dd1aebde5c6fc5c7d230b7a11597a45f&scene=21#wechat_redirect)

除了客服以外：

-   在上面提到的审核行业也会在今年逐步看到成本节省，**短视频行业、UGC社区都成为第一批探索大模型审核的行业。**

-   在经历的生成式广告的推广后，今年也会看到更多企业**应用LLM****投放提高ROI的案例。**

-   很多**常规性质的设计领域也将面临被AI替换**，典型的例如广告投放素材团队，我们已经看到了不少互联网公司的广告投放素材团队出现了大规模裁员。

-   过去两年我们看到了美国企业开始将Helpdesk和内部支持人员搬去哥斯达黎加和波兰，现在可以换成类似ServiceNow GenAI这类产品了。

需要值得注意的是，**LLM带来的替换也不会一蹴而就**：

-   例如在客服与审核行业，上一代的AI已经应用非常深入，不是每个场景都能找到LLM的替换点。例如在3C家电领域的排障需求，LLM降低了整理FAQ语料库的大量时间，但到回答效果仍然是语料质量决定的，光靠LLM模型的改变仍然不够。

-   但LLM在情绪安抚、非语料库/非标话题的沟通，以及未来潜在Agent处理能力上仍然是传统ML模型无法相比，随着时间的深入渗透率也会看到明显提高。

假如这些场景能带来2500亿美金的利润增量是什么概念？

-   美国GDP 25万亿，多数的成本节省可能都会发生在美国的企业中，**这相当于0.1%的GDP增量。美国未来一年的GDP增长2%。**

-   这已经影响到了经济的发展。这也让AI成为一个真到不能再真的故事。

企业ROI的提升，也同样会带来裁员风险，更高地利润率也意味着员工也会减少。

很不幸这样的变化，可能也会在2024年成为主流话题。

但无论如何，全社会生产力的提高，都会带来更多的税收和福利，支持普通人探索更多领域的生活。这是一个更加长远的话题。

**3** 下一代Turbo会成为很多场景的分水岭（2024）

[

EP13 OpenAI DevDay带来大变化

2023-12-05

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486101&idx=1&sn=6387df44181bfdc676baddbb2c9523aa&chksm=ea5ad36ddd2d5a7badd92900b2f55456e13e1158cb8f98e485d63248387f0f5a9e835a241031&scene=21#wechat_redirect)

2023年底OpenAI的DevDay在我们看来是一次伟大的变化，他的效果可以用低开高走来形容。最初的舆论倾向于DevDay上没有看到新的技术进展，没有看到新模型，只看到了意料之中的降本和没什么用的GPTstore。

但回过头来看，我们会看到**处于商业模式跑通临界期阶段的每一次降本和性能提升，都会明显带来需求赛道的解锁**：

-   在DevDay之前，一个文字版本的LLM Bot可能需要500美金/月的成本才能替代人工，叠加其他成本和利润，不要说在中国能不能商业化，在美国都远得很。

-   **但当成本从500美金/月降本到150美金/月时候，算上其他成本和利润也已经达到可用的临界点了**，假设按照1:10的比例来看也达到更换一名4000美金月薪客服的效果了。

-   这里面值得我们注意的是，**越是Low-hanging Fruit的领域，对成本就越是敏感**，进入可用/可用分水岭后，每一次成本优化都会拓宽相应的用户群体。

我们对下一代GPT 4.5/5 Turbo尤为期待，并**期待下一代Turbo能继续解决这几个难点**，成为Low-hanging Fruit场景真正走向大规模商业化的分水岭：

-   更高的精确度：现有的模型因为精确度不够，需要调用更多次API，当精确度和幻觉得到优化后，调用API更少，相应的成本和延迟也会更小。

-   更快的反馈速度：以语音客服场景为例，一个“像人”的AI客服需要将反馈速度限制在2s以内，而扣除ATS、TTS、传输等时间留给LLM反馈的时间只有0.5s不到，现有的LLM反馈仍然需要2-3s时间，如果再优化75%反馈速度，就进入可用区间。

-   更低的成本：如果大模型按照每年50-75%幅度降本，那就算现在1000美金成本的产品也很快会进入可用区间。而到了今年下半年，我们还期待B100+Int4带来的新一轮叠加降本，可能幅度会比75%还大。

在下一代版本中，我们不需要Agent和幻觉有多大程度的优化，仅从成本/延迟角度，就足以打开很多商业想象力。（相比我们讨论的Low-hanging Fruit领域）

**4** 围绕AI衍生出新的Data Stack标准（2024）

全行业都非常非常关注Data Stack领域，**“做好大模型首先得有数据、然后得有合适的数据架构”**。从年初LLM展开后，所有人都在讲类似的故事。

但该有什么样的架构，一直到2023年底才变得越来越清晰。

回到2023年初，行业有一个非常模糊的概念：

-   大模型首先需要的是非结构化数据，所有的非结构化数据产品都会因此而长远受益。

-   大模型需要一个外接的知识库，向量数据库，会依靠Embedding向大模型更新数据。

但经过了一年时间，发现大模型的需求不仅于此：

-   **想赚大模型在训练环节的钱非常不容易**，需要一套end-to-end的full stack方案，从ETL到pipeline，到数据湖/非结构化数据存储，再到pre\-train/finetune。

-   **仅提供非结构化数据库还远远不够**，客户更倾向于将数据存在更便宜的S3和数据湖中。

-   在推理环节也不**仅是向量数据库+Embedding的方案**，因为Embedding的黑盒、不易解释等特性，越来越多的RAG方案开始混合传统的BM25搜索加强效果。

而回过来看数据行业的先进大公司，各自的探索方向也完全不同。

Databricks作为AI领域的先行者，率先打造了**End-to-End的full stack**方案：

-   Databricks Spark（ETL+ML）→Delta Lake(数据湖)→Vector Search（向量数据库）→Databricks SQL（数据仓库）→MosaicML(PreTrain/Finetune)，最先搭建了一个围绕大模型训练/Finetune的全套技术栈。

-   同时Databricks也是Data Stack公司中最早推出大模型的企业。

-   在今年的Data+AI Summit中，Databricks推出的Lakehouse IQ也是当时最惊艳的Text→SQL→Answer产品，并且能看到初步的解释Table能力。

Snowflake在开头落后Databricks后，也迎头直上，找到了自己的发力点：

-   相比Databricks的Fullstack，Snowflake在过去缺少ETL能力，缺少一个处理非结构化数据型能够更好的Lake，缺少向量数据库，也缺少一个好的训练平台，只有一个性能最好的数据仓库。

-   随着今年Snowpark产品的快速采用，其在一年内ARR收入已经超过了5% Databricks Spark营收，Snowflake迅速补上了其ETL能力，但在ML的用例上仍然有很长路。

-   其数据湖在Snowpark可用+Iceberg更新后，也满足了模型训练的需求。

-   通过Container Service，Snowflake搭建了一个公有云上的K8S空间，可以在上面跑训练平台和向量数据库的合作伙伴。

-   通过与NVDA和OpenAI的合作，Snowflake花了更多的精力在Text2SQL上，同时也通过收购文本AI创业公司尝试搭建企业AI知识库方案。

-   通过收购NEEVA，相信在打包好原有技术能力后，也很快会推出自己的RAG方案。

-   **距离Databricks仍然有很大差距，但好在Snowflake的很多传统客户90%的数据都是结构化数据，可以接受Snowflake补齐产品的时间**。

Elastic和MongoDB花了更多的时间在构建自己的RAG方案上：

-   **Elastic早在2年前就推出了自身的RAG方案**，随着开发者更加认识到结合BM25的Hybrid Search在RAG中的重要性，Elastic不仅在现有客户中有渗透，在我们过去组织的讨论会中也有两位嘉宾的公司正在采用Elastic方案。

-   MongoDB构建了向量数据库的单点Feature，但离完整的RAG方案仍然有距离，相信也会很快补上。

除了我们熟知的几家公司，在向量数据库和RAG开发者排名中，创业公司也大放异彩。这包括我们熟知的Pinecone等，以及中国出海的Zilliz、MyScale等优秀公司。

这也使得Data Stack公司在面向大模型客户时出现了与过去不同的标准：

-   **因为大模型技术栈还比较新又相对复杂，对应的有经验的可以拼搭的人才还远不如曾经的DBA数量庞大，更需要一套一站式训练解决方案**，才能比较快的让大家体验到大模型的效果，作为厂商每家都需要补齐各自的能力，加速自己的产品在客户侧落地效果。

-   **而面向RAG，也需要结合很多行业Know-how**，在人均探索向量数据库的情况下，一套可用、可解释、准确性高的RAG方案更有价值。

-   而未来的Data Stack公司也会频繁在这两个新标准上竞争。

**5** 我们可能会经历一次断层，但可能不重要（2025）

相比上面提到的Low-hanging Fruit，摘更高一点的果实要困难的多。

Low-hanging Fruit之所以简单，是因为对Agent、容错率、幻觉的要求都没那么高。

在更复杂的场景效果通常都不如人意，而且看起来可能不是一两代模型就能解决的。

目前的大模型在做容错率低的场景时仍然面临很多问题，远没有我们想的那么神奇：

-   例如回答客户公司**“过去三年采购了多少水泥？”**，一个看似简单的问题需要现将问题拆分成步骤，然后分别去召回相应的信息，最后再做一个总结。最后得出的结论往往错误率很高，这仍然属于非常前沿的领域。

-   例如仍然有非常多定制化的工作，可能**90%的文档还不能满足大模型Embedding时候的质量要求**，仍然要做大量的数据清洗。

-   例如大模型的注意力也不够稳定，经常被不相关的问题干扰，出现幻觉，需要做非常多的情景优化。

而到了Agent情况时候，很多Agent平台上的客户也只能做到2-3步的推理，停留在**“在车里说热，车会开空调”**的水平。

这同样从Copilot Pro上市后面临的大量用户吐槽中可以看出，A16z的投资人@Guido Appenzeller在Twitter抱怨了一连串的Copilot Pro使用体验。这是个很好的例子让我们可以展开聊聊：

-   **在LLM之前的大多数软件并没有想到会需要这么多数据格式。**就比如@Guido Appenzeller说的“无法仅将橙色字体转换成绿色字体”，可能就是因为字体+颜色没有定义成标准的格式，LLM也无法识别。

-   **LLM也远没到可以进行复杂问题拆解+多步推理的能力。**@Guido Appenzeller想要根据主题设计一个数十页的PPT，但多数页面没有意义。这就是典型的模型问题。

-   在这两个问题之外，再往后一旦需要通过上下文进行复杂的数据Query，涉及到更多RAG的难点，问题就要再难一个层次。

看到上面这个问题后，我们就很容易理解Workflow产品为什么很难短期跑出来完整的LLM产品：

-   **很多老软件需要做重新设计**，但多数的Workflow软件代码量极大，需要时间解决工程问题。

-   **要等待模型变得更聪明，推理步骤更长**，但我们没有时间表。也需要一串推理工具支持，也需要更好的数据准备能力。

-   **多模态的发展可能会解决数据格式的问题**，例如“粉色字体”对于非多模态LLM需要具体的格式，但对于多模态LLM就可以通过GUI识别。

这些复杂的场景受制于模型能力、RAG发展、数据清晰、场景定制，每一个环节都会影响最终的准确度。**每一个场景最后可能都有一个准确度的魔力指标，可能是95%，也可能是99%，在达到准确率指标前都是爬坡期。**

也因为整个环节中有多个步骤，每个环节都会互相影响。同时在对问题拆解，或者要回答多个问题的时候，也需要关注连续正确率。这都使得难度进一步方大。

**如果AI应用一直都还聚焦于Low-hanging Fruit，很快就会看出天花板的端倪**，再次进入到一个不能证实、不能证伪的阶段。

我们不清楚这个断层会有多长，有可能是半年一年，也可能会更长。

**6** 2C领域成长很慢，游戏、音乐、教育可能是最先跑出来的（2025）

大模型的产品发展与互联网的产品发展有一个截然不同的地方，**边际成本非常高**：

-   **互联网时代的规模效应和网络效应非常强**，在买量模式兴起前，边际成本几乎为0.

-   这也意味着，如果一个产品可以自然增长到10万用户、100万用户、1000万用户，其成本也几乎没什么差别。

-   但在大模型时代，**模型成本要远远高于人力成本和买量成本**。

这使得2C互联网爆炸期，我们在每个月都能见到很多产品迅速跑上100万DAU，其中有的存活下来，有的又昙花一现。这也让当年的投资人要花很多精力去鉴别是否存在DAU造假，以及评估DAU的持续性。

但在大模型时期，**DAU不再是获取用户的过程，它成了评估商业模式的结果。**

做2C产品，就像做2B产品一样，要非常小心而且缓慢的去跑Product-market Fit，去找到能跑通商业模式的核心用户群。一旦错误地估计了自己商业模式跑通的能力，就可能被成本压得喘不过气来。能跑出来100万DAU的产品就已经非常成功了，证明了他烧得其100万DAU对应的模型API费用。

**在2C上面想不通的问题，对照到2B产品上就想得通了。**SaaS行业里哪怕增长最快的Snowflake和Databricks，在成立的前五年都没什么收入与用户。

在成本之外，2C产品还面临着很多额外的问题：

-   2C产品多数时候好玩和能杀时间是最重要的。但是大模型好像不具备这个能力。

-   2C的很多场景也非常关注容错率，例如家教场景，而且因为上课时长1小时内可能会经过几十道题的互动，时间越长就会发现错得越多。比单次场景要难做很多。

[

EP02 AI如何颠覆游戏讨论纪要

2023-05-10

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485766&idx=1&sn=92e349bdb9db3301f555bcfd0b7dd9ce&chksm=ea5ad0bedd2d59a8b6ba0b70c4ecfb87bbb671e15f0f68224af90d651ed121acebfb9d4eb8db&scene=21#wechat_redirect)

**创意型的内容场景**例如游戏和音乐可能会最先跑出来：

-   例如Unity、Epic、Roblox等引擎已经将AI应用到游戏的场景搭建，并提供可以让NPC进行对话、动作的渲染能力。

-   文字游戏已经出现了基于大模型的游戏，未来在Roblox等搭建成本低的平台上也可能最快看到基于AI NPC或者AI剧情的游戏跑通

-   Suno音乐已经获得了不少受众，例如字节跳动等大厂也正在发力领域，AI编出来的歌真的可以听下去，未来也可能跑出来网红歌。

[

EP12 AI如何重塑教育讨论纪要

2023-11-06

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486067&idx=1&sn=3bacd58e2fde79692d3cbb29d96a87da&chksm=ea5ad38bdd2d5a9de9606b9ecf785807f5ee0adc410794dfdf2343a805ee5e26a9c87edebe80&scene=21#wechat_redirect)

在教育场景体验类中：

-   语言教育、故事创作已经有成熟场景。

-   **但在更关注容错率的数学等典型立刻场景，仍然停留在单次场景例如拍题搜题，连续对话的家教场景仍然有非常大的正确性问题。**

-   但看起来这些是随着模型发展可以解决的，只是看多久能达到容错率要求。

**7** Workflow很难，但单点功能可以看到（2025）

[

EP04 AI如何颠覆办公与CRM讨论会纪要

2023-06-14

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485819&idx=1&sn=28c92da1fc59b44d4309a71cc94f95a2&chksm=ea5ad083dd2d59957bb4e7c90525365b3e2520ba7212dc221438f25e7679a3103263d90c590e&scene=21#wechat_redirect)

我们上面讲到了Workflow为什么很难，但不做整体、做环节的SaaS产品很大概率都能看到价值提升。

在此我们就不做赘述了，多数的软件公司都在往这个方向探索。相比“破坏性创新”带来的架构推导重来，“延续性”创新更加容易，也很快会带来客单价的提升。

**8** 或许可以替代更高阶的职能（2026）

在客服、审核等技术门槛低的工作达到被AI颠覆的门槛猴，有一些更高阶的智能也可能被替换，但也取决于更高阶场景大模型的错误率会降低多少。

首先是电销行业，**电销行业是客服的进阶版本**：

-   电销对延迟的要求更高，不能快不能慢，但随着模型迭代一定能够解决。

-   电销需要更强的Agent能力，要完成销售流程，中间需要不断将沟通话题巧妙地拉回到需要搜集的数据，并且要Make Decision。比起客服，更加像一个People Business。

[

EP01 AI如何颠覆数据库讨论纪要

2023-04-25

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485464&idx=1&sn=13d6039e278e1e254ec2cbfc36c77b4b&chksm=ea5ad1e0dd2d58f6d4b777e90c79c633de9356763f6ca956b541f58ec036e0547d0b02425721&scene=21#wechat_redirect)

然后是**数据分析师，****程序员的弱化版本**：

-   Text to SQL在2024年估计就会成为各类数据库的标配，但距离能替代50%以上数据分析师的工作仍然有很多问题。

-   例如现在最麻烦的是理解客户公司的Table，在1000万张Table中，“水泥-销售”Metric可能出现了100次，没法准确定位到这次你要的是哪个。SQL语言易学难精，但将易学的部分提高数倍效率，让人人都可以成为数据分析师，应该很快了

[

EP08 AI如何颠覆可观测性工具讨论会纪要

2023-08-22

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485995&idx=1&sn=758d9de3a0e277d3193e81d37617d1f4&chksm=ea5ad3d3dd2d5ac5060d6c6cfdb4c1078089446c34653d6394c1aa83d4b605b63be7d6f4a3dd&scene=21#wechat_redirect)

[

EP06 AI如何颠覆网络安全讨论会纪要

2023-07-11

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485918&idx=1&sn=980b533e160c8ffe1a8a76f6f517850a&chksm=ea5ad026dd2d59304390d111ad0c475a9cd4296255c31ba1e0762dd88b827bb39b4c5dab5e63&scene=21#wechat_redirect)

再然后是后台支持的**运维分析师和安全分析师**：

-   和数据分析师较为类似，这里面最核心的技能不是怎么操作情报和数据，而是对告警能够分析、判断和给出解决方案

-   如果所需的数据能够更完备的情况下，Text to SQL的能力得以添加的情况，资深的运维和安全分析师可能不用像之前等junior的人员完成数据准备，就可以直接操作数据，发现问题，展开后续工作

**项目经理**也可能被颠覆：

-   项目管理软件例如Jira、Clickup都在推出自己的AI Feature。

-   项目经理原本的职能，包括引导敏捷开发、跟踪每日进度、跟踪Ticker完成情况、根据问题调整工时分配、复盘效率，都可能被LLM实现。

-   相比产品经理与工程师，项目经理在开发环节更容易被影响。

**9** 工业领域会看到很多多模态实践（2026）

[

EP10 AI如何改造传统工业讨论会纪要

2023-09-26

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486033&idx=1&sn=cefc1d887d689d1fdd7903a7622b46ff&chksm=ea5ad3a9dd2d5abfbe6d3d8fb4e8d55a16c349864783c7bce5cae1e7bce3cf0cade3b2b9d61c&scene=21#wechat_redirect)

工业场景对大模型落地属于容错率相对较低，行业know-how要求特别高：

-   **很****多精密流程、操作，一旦出错，造成的结果不可挽回。**

-   行业中的专家、熟练工人除了技能wise确实效率更高之外，还有很大的价值在于为过程承担风险，为结果担责。

-   这方面大模型作为一个概率模型还不能很好的发挥作用。

大模型先在替代简单而重复的工作，在更加细分的容错度比较高的场景进行渗透：比如说初级运维人员，比如说一些允许试错的偏向于科研的场景。

处理简单任务的多模态能力是需要的：

-   一方面能够处理的东西相对浅表，而管理的东西多是具备实体的，比如说一个加热器、一个蒸馏塔，一种工艺等，涉及的更多是各个维度、形态的情报采集、整理输入、转化成人可读、可理解的处理线索和建议，所以对多模态的需求更加广一些。

-   **对于同一台设备的同一个问题的监控，可能涉及到图片（视觉，看到明显的破损）、数字（读到温度变化）、声音****（震动频率）**等等，最终都要转化成对同一个事情的判断，这个装置有没有坏的问题上。

数据平台可能更加重要：

-   大模型向处理高阶任务上走的话，更加依赖于对于任务及其实体的描述，即数据。

-   可以预想，就是后续相关领域的数据基础会更加加速。因为可以看到一个人类大脑样的大模型已经存在，只不过在这个领域这个脑子还处于婴儿阶段，需要更多的输入和训练才能让这个脑子变成年人的脑子，而这些输入就是数据。

**10** 基建与电力可能比GPU更稀缺（2024-2026）

Elon Musk说“2024年缺数据中心、2025年缺电。”

Sam Altman说“AI浪潮将会产生大量的能源需求。”

微软已经开始申请建设核电站。

**能源行业在美国是一****个高度****监管行业****，在****数据中心申请开建时就需要一并申请能源指标**，这使得2021-2022年申请的能源指标远远不够。

**单GPU的用电需求远远高于CPU**，随着LLM需求的大幅增加，2-3年前申请的能源指标已经不够用了。这也使得最近作为小型替代方案的柴油发电机、固体燃料电池价格不断走高。

数据中心用电量大概占到美国用电量的2%，但**数据中心新增用电量需求量成倍增加**，过去电网结构等问题也可能再次成为制约。

抢到更多的数据中心和能源指标，才有能力把GPU装进去。

**【讨论会】**

过去的讨论纪要请见下文。

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

[《EP11：AI如何改造推荐系统讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486055&idx=1&sn=32f3d75f4fbfda57b8734bbb390e4145&chksm=ea5ad39fdd2d5a89788c97e562a6267ad49c36631fbcdff3c52f236a40ed28502edd1c893a89&scene=21#wechat_redirect)

[《EP12：AI如何重塑教育讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486067&idx=1&sn=3bacd58e2fde79692d3cbb29d96a87da&chksm=ea5ad38bdd2d5a9de9606b9ecf785807f5ee0adc410794dfdf2343a805ee5e26a9c87edebe80&scene=21#wechat_redirect)

[《EP13：OpenAI DevDay带来大变化》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486262&idx=1&sn=39c45a626f49cb7027dc83554c6f91c1&chksm=ea5ad2cedd2d5bd86aa14b2c91e27b22910e572b94905ee5a8d24d02f8a8c852ee4404ed6f2e&scene=21#wechat_redirect)

[《EP14：到了颠覆AI客服的时候了吗？》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486101&idx=1&sn=6387df44181bfdc676baddbb2c9523aa&chksm=ea5ad36ddd2d5a7badd92900b2f55456e13e1158cb8f98e485d63248387f0f5a9e835a241031&scene=21#wechat_redirect)

**欢迎加入共识粉碎机的活动讨论群，获取更多活动信息**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

---

[

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/dljQibos6CibbP4ArSHW4K47YkbKXS9SwMJa0LexsTnibpTxnp36vGlcNj9JYSB4xvEcfCSLRfGRf6MibfQgt4v78w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

AI如何颠覆软件：你能为AI打工吗？（全网首篇AI+SaaS万字深度长文）

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485067&idx=1&sn=8bf37ff8a7a7aeac7da10c4c87131fef&chksm=ea5adf73dd2d56655d5ae8e7783783b0162c56a1ef99b5b74ee6efdd512d0f18c709f13e2db5&scene=21#wechat_redirect)

[

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dljQibos6Cibb5KbviakIsrxC0AETDJicjB2NCJS4qwEZibFzxWYjqRGyeDBh0WPemqEpQJyfQY4JsUoJDicTljgOYvw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

EP09 如何突破英伟达垄断（万字长文）

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486017&idx=1&sn=52397108a65999fd7656261302092943&chksm=ea5ad3b9dd2d5aaf858469d1346e4134db9904d626f45a3d5634c7382c510f72de93df47a3d4&scene=21#wechat_redirect)