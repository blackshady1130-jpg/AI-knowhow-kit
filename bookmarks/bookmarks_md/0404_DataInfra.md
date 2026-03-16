---
url: https://mp.weixin.qq.com/s/k-1q8iOggfeAWvu31Vj9iw
title: "Data Infra：大模型决战前夜"
description: "数据库公司正在LLM时代上演生死时速"
author: "波太金"
captured_at: "2026-03-08T11:39:27.959Z"
---

# Data Infra：大模型决战前夜

**关注共识粉碎机，获取历史讨论会纪要**

文：波太金 小熊猫

Data Infra行业、CRM与安全行业一直是全球软件行业里排名前三的软件细分领域（Gartner 2023， 前三大软件垂直领域是Data Infra占比15%，CRM占比14%，网络安全10%）。在Data Infra领域里有Oracle这样的3000亿巨无霸，有Snowflake、Databricks、MongoDB这样的新一代技术栈，有三大云布局完整的产品图，也有DB-Engines.com里正在监控的几百家数据库。

**如果说过去5年是Data Infra拥抱云原生的5年，那未来5年就是拥抱LLM变革的5年。**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dljQibos6CibajBM41qbR92CCzPhNLicwz4ibrcDWLoEGcICgoZyeuAJElsT6dc8wRE4eeEMafYO0sualrsVSF7ibibg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**1** Snowflake换帅

---

2024年2月28日，Snowflake发布了其财年第四季度的财报，在给了令人尴尬的全年指引后，给出了另一个消息令美国Data Infra行业震惊。

美国软件史上最传奇的CEO之一Frank Slootman宣布从Snowflake CEO职位辞职，新CEO是Neeva的印度裔创始人Sridhar Ramaswamy。Sridhar在去年5月将公司Neeva卖给Snowflake后加入了该公司，并担任Snowflake的AI SVP，负责所有新AI业务，**仅仅不到一年时间，从一位被收购公司的创业者成为了母公司的新晋CEO。**

Snowflake CFO Michael Scarpelli在财报后一周的投资人沟通中提到**“我直到周二（财报是周三）才知道Frank离职”，“但去年随着Frank和董事会与Sridhar共处的时间越来越多,我们感觉他可能会成为Frank的继任者”**。Scarpelli是Frank的老朋友，两人在ServiceNow就是黄金搭档，并跟随Frank一起加入Snowflake。在工作外他们也保持着很好的私人关系，都居住在蒙大拿州的Bozeman，Scarpelli可能与我们一样震惊。

Snowflake的天使投资人，以及首任CEO Mike Speiser随后也谈论到了Frank的卸任：

-   Mike Speiser与公司的两位创始人一同成立Snowflake时，即约定了自己什么时候卸任，“等到交付一个产品的时候”。

-   随后Mike Speiser卸任了公司的CEO后，让微软的Bob Muglia接任自己，并提到这是一次“clear upgrade”，在这一时期的目标是将产品推向市场并且跑通商业模式。

-   之后董事会意识到上市以及Scale-up是下一个更大的挑战，遂迎来了Frank Slootman，Frank可以让全公司的所有人保持高强度和紧迫感，使业务加速增长，并最终迎来上市。

-   Mike Speiser与Frank Slootman也相信**Sridhar会是Snowflake在下一个LLM时代最适合的领导者。**

换帅如换刀。在下一个Data Infra的大时代，LLM时代，**Frank可能已经不再是最适合Snowflake的CEO。这也让每一次换人都能收获巨大效果的Mike Speiser感慨Sridhar可能更适合下一阶段的使命。**

**Sridha在日后也提到，除了Snowflake外，三大云厂商也邀请他去做AI负责人，但他最终选择了Snowflake。**Sridha是市面上非常少有的Database+LLM+管理的复合型人才，他拥有Database相关的PHD学历，作为“King of Google Ads”，在Google管理着超过1万人的庞大团队，帮助Google在推荐算法追上Meta，为Google保持了推荐算法的领先立下汗马功劳。日后也成立了AI搜索公司Neeva。

不禁让人感慨，Data Infra在LLM时代也迅速被推入了拼刺刀的决战前夕。只有感受到了大战降临的紧迫感的公司，才会让管理层做出选择替换上个时代功勋卓著的Frank的决定。

**这个变化可能不仅仅是Snowflake的选择，也可能是很多软件公司必须做出的选择。**一位AI出身的CEO，可以清楚的知道需要在哪里投入AI，需要要补齐什么产品和技术能力，可以在哪里可以找到能够一起运营这个事情的人才。

先到先得，时不我待。我们会在后面的章节更多展开。

**2** Data Infra只有进入训练流程才能赚到钱

从去年1季度开始流行的Data Infra会收益的故事到现在，代表公司Snowflake与MongoDB都没有明确提过AI收入占比。

MongoDB在2023年4季度的财报中第一次解释了为什么传统的Data Infra公司们到现在还没赚到大钱：

-   Data Infra在大模型领域中会参与到三层：模型训练，Finetune和推理。

-   MongoDB的现有技术栈主要与后两层相关（Finetune和推理），但从现在的客户用例来看，绝大部分客户都还在第一层（模型训练）。

-   **等到客户进入第三层（推理），才会有更大体量的AI收入进入MongoDB。**

**这也是现在Data Infra领域的商业现状。只有涉及训练技术栈的新一代Data Infra公司才从这个领域赚到了钱，这些典型的流程包括ETL/特征工程，数据湖，向量数据库，训练优化框架**，以及在传统Machine Learning领域经常用到的生命周期管理和实验追踪工具。例如Databricks、Pinecone，以及中国的Zilliz、Myscale等新一代工具都赚到了AI训练的第一桶金。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（图：Relit训练技术栈示意图）

在最早Relit博客中提到的训练流程中，其大模型大量运用了Databricks的技术栈，并配合三大云的基础设施完成了模型训练流程。

**3** Databricks十年磨一剑

Databricks是新一代Data Infra中最耀眼的主角之一。

在其新披露的业务数据中：

-   Databricks在2023年营收达到了16亿美金，实现了~55%的同比增速。

-   虽然16亿美金营收仅占竞争对手Snowflake的不到60%，但其营收模式与Snowflake存在差异，除了对标Snowflake的SQL Serverless产品会包裹云厂商的计算与存储业务打包出售（赚软件的钱和计算存储的溢价），剩余的大部分产品仅出售软件价值（赚软件的钱）。

-   用两家公司的毛利来比较更加合理，都剔除云厂商的Pass-through收入，Databricks的毛利相当于Snowflake的~65%，考虑到其更快的增速按照2023年4季度来看接近Snowflake毛利的70%（反映了更高毛利的软件部分在Databricks的占比更高）。

-   **从趋势上来看，Databricks在2023年出现了收入加速趋势，并预估在2024年收入增速能加速到60%，为证明其合理性公司提到其2023年4季度的Booking订单同比增长接近100%。**

与Databricks现在的成功相比，过去十年Databricks的发展却谈不上一帆风顺，堪称十年磨一剑。

Databricks从开源Spark起家，并在后面顺着Spark往存储延展做出了数据湖拳头产品Delta Lake。沿着Spark的发展史来看，Spark的发展一直处于高度竞争中：

-   Spark是Databricks创业史中最早的产品，也仍是目前该公司最核心的产品，其开始的定位是做机器学习与数据工程的支撑平台。

-   **Spark出现时已经能覆盖深度学习流行前几乎所有的机器学习任务，但随着深度学习蓬勃发展，Spark不再是最主流的机器学习平台，Tensorflow以及之后的Pytorch更为主流。**

-   但在成为独立的机器学习平台之外，**Spark在数据工程领域独占鳌头**，是市面上最主流的ETL工具，这也为Databricks在大模型时代靠ETL/Feature Engineering拿到了关键的门票。

另一个拳头产品Delta Lake也使其成为了最大的商业化数据湖服务商：

-   在处理机器学习数据时，已经需要大量的非结构化数据，数据湖成为了最理想的高性价比存储方法。

-   **但在很长的一段时间里，数据湖的概念对于采购决策方-公司的CTO来说都很难理解，并且形成了搭建难、维护难的观感。**

-   而随着Delta Lake走向闭源，开源的Open Format产品Icebeg、Hudi等也后来追上，这也最终推动了Delta Lake开放了开源产品，以及在Delta Lake 3.0中开始支持外部Format。

而在同期的发展中，与Databricks几乎同时成立的Snowflake因为其数据仓库理念更好理解、市场空间更大，在体量和增速上都快速拉开了和Databricks的差距，一度让Databricks感到黯然失色。

为了进攻“油水”更厚的数据仓库生意，**Databricks提出了Lakehouse概念**，一体化的产品既能做湖的Workload，也满足仓的Workload需求。且相比于Snowflake，Databricks中Lakehouse的SQL业务也有其特点：

-   因为支持湖的Open Format，数据在进入数仓运算的过程中不需要转化成数仓的专属格式，**这为客户省去了存储成本（不需要同一份数据为数据湖和数据仓库都准备一份），以及传输所带来的额外Data Loading成本。**

-   同时Databricks也给予客户更大的自主权，可以使用自己在三大云购买的计算与存储业务，这使得对超大客户尤其友好（因客户体量大，超大客户在三大云处可以拿到很低的折扣）。

-   伴随而来的还有疯狂的宣传攻势，在节省一定成本的同时，也适当混淆了两者收费口径的不同，用不加存储计算以及Data Loading的成本对比Snowflake的全托管产品，并配合夸张的口风，比如一直标榜的“我们比Snowflake便宜10倍”的口号。

-   但归根结底，数据仓库领域仍然有非常多的特性优化，比如各种复杂Join同时发生的情况。刨除上面口径的不同，在数仓先天内功不足的Databricks SQL在大运算量的复杂场景仍与Snowflake的性价比实质有所差距。

Databricks的发展经历过几次起伏，但最终熬出了头，**其一直宣扬的Spark和Lakehouse产品成为走向大模型时代的攻城利器：**

-   目前阶段的技术栈需求，平台功能的完整（能够端到端实现目标）比单个功能的超群更加重要。

-   大模型时代对于非结构化数据的处理呈现爆炸式增长，**Delta Lake + Databricks Spark作为非结构化数据处理的黄金搭档成为主流技术栈，并且占据了市面大量的ETL/Feature Engineering Workload。**

-   通过其在机器学习上的全体系积累，**在收购MosaicML后，Databricks成为了三大云和英伟达后又一个全栈大模型训练平台**，几乎补齐了最后一块拼图。

-   而Lakehouse的路线之争，在Snowflake于2024年开始全面拥抱Open Format，并允许客户使用自己的存储负载后走向了尾声，**Lakehouse成为大数据的时代主流，无论是从湖进入，还是从仓进入，最后都会成为Lakehouse方案。**

**4** Snowflake的追赶计划

与Databricks一直聚焦于非结构化数据与机器学习的工作不同，Snowflake的路线更加发散，中间在机器学习领域投入的精力并不多。

Snowflake的创始人Benoit Dageville一直在负责Snowflake的技术路线，**在2023年之前的重点是Unistore与Snowpark**，先谈谈Unistore：

-   Unistore是一款类似于HTAP的产品，底层采用KV Store设计。**Benoit希望这款产品能帮助Snowflake拓展向更大的数据库领域（OLTP）的市场机会。**但因为其KV Store的设计，其方向仍然无法与Oracle等主流OLTP直接竞争，更加适合成为OLAP为主+OLTP为辅的公司所采用的解决方案。

-   Unistore实现的技术难度也比较高，其不处于Snowflake所发家数据仓库领域，对于延迟和稳定性有着极高的要求。同时HTAP也是个新的技术方案，HTAP的先驱在这个领域里也一直碰壁，很难说HTAP在商业模式上跑通了。

相比Unistore，Snowpark的逻辑更加通顺：

-   而Snowpark则有着更顺的产品逻辑，客户在将数据转化进入Snowflake的时候，就需要进行ETL处理，而过去的主流处理方式就是Opensource Spark和Databricks Spark，**现在用Snowflake原生的ETL工具，节省了传输成本，从功能上也没有区别，客户出于性价比转向Snowpark应该是顺理成章的选择。**

-   相比Opensource Spark（在AWS客户中更多以EMR产品售卖），Snowpark的性价比优势非常明显。但相比优化后的商业化产品Databricks Spark，Snowpark更多还是在面向已经使用Snowflake产品的客户的数据处理上有一定优势。

-   虽然Snowpark可以很快赶上Data Engineering的工作量，其技术壁垒也不高。**但在机器学习领域上仍然有非常多的工作要补齐，特别是面对Spark的开源优势，Snowpark更多还是面向特定的传统行业提供机器学习能力的支持。**

Snowpark在2022年底商业化后，其收入体量差不多到Databricks ETL收入的5-10%，增长迅速。如果与Databricks推出面向与Snowflake竞争的产品Databricks SQL相比，其体量大概是Databricks SQL的1/3，推出也比Databricks SQL整整晚了一年。

**Snowpark产品也为Snowflake保留了通向大模型时代的门票**，Snowflake日后的大模型支持产品也都围绕Snowpark建立：

-   **Snowpark为Snowflake带来了非结构化数据处理的能力**，在大模型时代其可以胜任ETL和Feature Engineering的需求。

-   **通过Snowpark继续往外延伸，Snowflake开始支持Iceberg Openformat**，这也为Snowflake吸引更多非结构化数据，构建完整的Lakehouse解决方案打下了基础。

-   同时，Snowflake推出了Snowpark Container Service，并成为了Snowflake日后的工作重心，**为Snowflake引入了GPU Workload****。**允许客户在Container Service中Finetune和部署模型。

在Sridhar进入Snowflake后，其也将精力花在新产品Cortex上：

-   Cortex为Snowflake引入了外部的大模型合作伙伴，这包括了其新投资的Mistral AI，该公司产品主要针对对话和相关分析。

-   Cortex也包括了Document AI与Snowflake Copilot，这很像Databricks LakehouseIQ，并提供面向Text2SQL和知识库方案。

-   **同时Sridhar也正在将过去Neeva所运用的RAG-Vector Search方案整合入Cortex，这也很快会为Snowflake带来Vector存储和处理能力。**未来也可以支持更多的Container Service客户，允许客户在Container Service中直接部署+推理模型。

Sridhar非常清楚Snowflake缺什么，也知道该投入多少精力。这从Snowflake挖走DeepSpeed创始人以及其核心团队中可以看出：

-   Snowflake CFO在后续的沟通中曾经提到从DeepSpeed挖走的5个人需要20mn USD的年成本，“非常令人惊讶，他们太贵太优秀了“”。

-   但Sridhar很清楚知道为了成为End-to-End的训练/推理技术栈，Snowflake也必须能找到和MosaicML一样的优秀标的，如果不能收购那就直接挖人。**DeepSpeed团队几乎是最好的选择，其也是****现在最流****行的大模型训练/推理框架。**

-   这在Frank时期几乎难以想象，大成本+难以被公司“老人”理解的用途，只能在新CEO自上而下的推动中才得以实现。

更换CEO后，Snowflake也做出了All in AI的架势，全部产品都以AI为重心。

但在一家以数据仓库为主要业务的公司里做AI就相当于**二次创业**，Snowflake 任重而道远。

**5** MongoDB的RAG故事

与Databricks、Snowflake不一样，MongoDB不在分析侧，其产品更加侧重于支撑业务数据流转和存储的OLTP。

**在2023年初，MongoDB一度是Data Infra中的头号标的**，当时的市场逻辑是：

-   MongoDB基于文档数据库发展出来的，可以先不过多考虑数据结构（是否结构化、非结构化、半结构化等等），数据一股脑先进去再进行处理，有很高的易用性

-   **大模型训练和推理会使用许多非结构化数据，而MongoDB的主要产品是做半结构化和非结构化数据的存储、读写、查询。**

-   在训练侧可能会用到MongoDB作为非结构化数据的存储介质，这可能会进一步提高MongoDB在客户技术栈中的重要性。

-   **MongoDB有机会做自己的向量数据库，进入到模型推理侧。**

-   更多的LLM应用也意味着更多的APP，他们不一定会在LLM流程中使用MDB，但还是需要通过MongoDB存储Chatbot聊天记录，以及传统的OLTP负载。

MongoDB也非常配合地在**2023年1季度提到其有200个新客户是AI客户**，这包括了Hugging Face、Tekion等知名公司。但在随后的季度里，MongoDB不再披露其AI客户信息。

MongoDB的发力点主要点在了推理侧，这也是其在最新季度里提到大模型场景还在训练侧，还未进入到推理侧，导致其收入贡献不明显。

审视MongoDB在推理侧的机会：

-   相比前面两家的推理侧更多还在Data Application和API层面，**MongoDB可以面向终端用户提供服务**，这与其OLTP的定位分不开。

-   MongoDB的**Atlas Vector Search服务最早GA提供向量搜索功能**，在2024年初就已开始商业化。

-   面向其老客户，传统技术栈可能更值得信赖，特别在RAG要求、尚未大规模上量的时候，MongoDB的向量搜索服务可能已经满足要求。

[

EP15 RAG带来蓬勃应用生态

2024-02-06

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486569&idx=1&sn=1bb4d0b44745637079846fa69ea5c3c5&chksm=ea5ad591dd2d5c8743030e2b3e40f376b69d03d473c9a6259f161d6a79c8b562706db3ba197a&scene=21#wechat_redirect)

但与其他RAG方案相比，MongoDB也仍然处于推理发展的早期：

-   **MongoDB在数据量和并发量大的场景，仍然距离AI Native的向量数据库仍有差距**（主要是Mongo在vectordb的引擎算法方面积累较这些专业向量数据库还较弱，推理场景大规模推广后，数据量会显著增加，对于引擎能力的考量越发变多）。

-   **新一代的RAG方法，不止依靠与向量数据库结合的Dense Embedding，还对传统的BM25有极高的要求**，这方面可能也不如Elastic的方案。

-   对于MongoDB，仍然有大量需要追赶的功能点。

**6** 世界需要End-to-End的技术栈

我们将三家公司的LLM进度列成了如下图表，第一张是训练侧：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   Databricks是**全流程的训练技术栈**，并且通过MosaicML补上最后一环。但在大模型训练上仍然较公有云有一定差距。

-   Snowflake正在打补丁的过程中，**在Notebook、数据湖、模型训练优化以及MLFlow层面仍然有很大差距**，目前更多是允许客户在其Container Service里进行Finetune。

-   MongDB的重点在推理侧，基本不涉及训练。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   Databricks的RAG方案仍然在公测，目前还不具备一站式推理能力，但有望年中补齐。

-   **Snowflake的Snowpark ML以及RAG方案也都在公测，未来更多支持部署在Container Service上Data Application的推理**，这些可能是客服机器人、企业知识库等场景。

-   MongoDB虽然在Finetune和容器上没有涉及，但更侧重于面向终端用户的RAG方案，面向的客户群体更加广泛。

科技领先的客户已经在采用三大云以及各类AI Native平台的LLM技术栈，三家公司未来的主要增量还是传统公司场景：

-   **对于传统公司来讲，End-to-End的技术栈非常重要**，客户在LLM人才紧缺时代，无法建立起最优秀的LLM团队，对于训练/推理流程，越简单越好。

-   传统公司也在增加LLM预算，这可能是自己通过开源模型训练例如客服等场景，也可能是购买其他第三方软件应用解决方案。

-   但从历史维度来看，**一开始应用解决方案可能会提供其自己搭建的Data Infra，但随着生态系统打通，客户也更多用其自有的Data Infra支持所有第三方解决方案。**

**7** Data Infra的新产品

除了上面的训练推理流程，Data Infra公司诸如知识库和Text2SQL领域准备新产品。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（图：Databricks LakehouseIQ介绍）

Databricks的LakehouseIQ就希望做成一个一体化的产品：

-   **客户将其结构化数据、非结构化数据以及办公用的各类文档都可以存在其Lakehouse中，从而实现通过与Lakehoue IQ对话的方式获取信息**，是相比上一代Sharepoint/FTP等更高效的文档搜索方式。

-   同时通过LakehouseIQ，客户可以以自然语言的方式撰写代表，实现Text2SQL。

-   在展示中，其进一步希望可以通过自然语言输入目标，然后将大目标拆解成几个小目标，分别进行数据分析，再Prompt给大模型得到完整答案。但目前还在早期阶段。

Snowflake的产品更加早期：

-   其知识库产品主要依靠其**22年收购的文本AI公司Applica**，为其提供了Document AI产品，可以从文档中抓取结构化数据和文本数据。

-   结合Neeva团队为其做的Vector Search方案，有望也打造成完整的知识库方案。

-   Snowflake Copilot是其定义的Text2SQL产品，更多是将自然语言翻译成SQL代码，但离做目标拆解进行复杂分析仍然比Databricks远得多。

**8** 决战也是迎来新篇章

过去几年围绕Data Infra的竞争一直都聚焦在：是云架构还是On\-prem架构，是湖还是仓，是NoSQL TP还是SQL TP。

现在出现了LLM带动的新Data Infra需求后问题就变成了：

-   能不能最快速度做新产品，抢到增量蛋糕？

-   如果做不出新产品，挖不到LLM的团队，是不是就从此掉队，还要丢掉老产品份额？

所以才会看到类似于Snowflake这样不惜更换CEO来All in AI的举措。

**我们难以想象在Databricks、Snowflake外还有哪家公司能够收购MosaicML，或者挖到Deepspeed的核心团队。**新一批的LLM人才只有头部数据库公司才能吸引，这可能会进一步拉开和开源、OnPrem以及剩余数据库的距离。

是决战，但更可能是增量的大机会。

在6月份的年度产品会上，我们都会看到几家家公司密集GA的新产品：

-   Databricks可能会GA其Vector Search和Container Service方案。

-   Snowflake可能会GA其部分Cortex功能、Container Service、SnowparkML、Notebook、Iceberg、Streamlit方案，如果进度赶得上也可能GA其Vector Search。

-   算上正在不断打磨RAG能力的MongoDB，每家公司都在上演生死时速。

**【讨论会】**

我们计划在1-2周内举办一次关于**代码库与Coding LLM的讨论**，感兴趣作为嘉宾的朋友请后台联系我们，或者直接联系我们的微信。

过往的讨论会纪要请参考：

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

[《EP13：OpenAI DevDay带来大变化》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486101&idx=1&sn=6387df44181bfdc676baddbb2c9523aa&chksm=ea5ad36ddd2d5a7badd92900b2f55456e13e1158cb8f98e485d63248387f0f5a9e835a241031&scene=21#wechat_redirect)

[《EP14：到了颠覆AI客服的时候了吗？》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486262&idx=1&sn=39c45a626f49cb7027dc83554c6f91c1&chksm=ea5ad2cedd2d5bd86aa14b2c91e27b22910e572b94905ee5a8d24d02f8a8c852ee4404ed6f2e&scene=21#wechat_redirect)

[《EP15：RAG带来蓬勃应用生态》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486569&idx=1&sn=1bb4d0b44745637079846fa69ea5c3c5&chksm=ea5ad591dd2d5c8743030e2b3e40f376b69d03d473c9a6259f161d6a79c8b562706db3ba197a&scene=21#wechat_redirect)

**欢迎加入共识粉碎机的活动讨论群，获取更多活动信息**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

[

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dljQibos6CibawpSibvvwvsIaKIicFKN0cYFEs6YPJNHQicCCyyJkvKhiaEq6xBZftgQAWof4lzA7mTEUgcOUSgLVVNw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

大模型未来三年的十个假设

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486395&idx=1&sn=8856ac8d66efeab83683c528e3151cb2&chksm=ea5ad243dd2d5b55d8b967a759beaadd02ea773e60af064b006979f5e9524316f38fde3fa95a&scene=21#wechat_redirect)

[

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dljQibos6Cibb5KbviakIsrxC0AETDJicjB2NCJS4qwEZibFzxWYjqRGyeDBh0WPemqEpQJyfQY4JsUoJDicTljgOYvw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

EP09 如何突破英伟达垄断（万字长文）

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486017&idx=1&sn=52397108a65999fd7656261302092943&chksm=ea5ad3b9dd2d5aaf858469d1346e4134db9904d626f45a3d5634c7382c510f72de93df47a3d4&scene=21#wechat_redirect)