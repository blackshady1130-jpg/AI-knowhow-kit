---
url: https://mp.weixin.qq.com/s/eJfKhvLYsd3CNFh_ooqywA
title: "Abridge：AI Scribe 成为 AI 医疗应用的最佳实践"
description: "医疗应用领域，LLM 产品已经阶段性成功"
author: "拾象"
captured_at: "2026-03-08T12:35:01.829Z"
---

# Abridge：AI Scribe 成为 AI 医疗应用的最佳实践

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxIia4dtherNtfj4om3icINqVfn830eTic3o7LsTg7vicSBXyFibiavMO9YzrvyLx6XkqPCGKy0xMcM1osg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3tHNibnJ2jgxIia4dtherNtfj4om3icINqVTSQ2qK9g46g6G88KhVPVrGlb6AgfJ4cLf49KGMWic55KgOLmuWzWEpA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

作者：Theodore

编辑：Cage

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxIia4dtherNtfj4om3icINqVHxEZ4cIZt4L5WEfQmsb3iaxcziasGydzjnklpIltak5d0Iic9V4ddUndQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

在 LLM 落地场景中，医疗领域的应用开始展现出比较高的确定性，尤其是 **AI scribe 产品能****解决临床文档记录枯燥、耗时这一行业痛点**。Abridge 是其中最有代表性的公司，训练了专用于临床文档的 ASR 和文本生成模型，能够替代 90% 左右的人工工作量。担任临床医生和教授的创始人从 2019 年就开始构建 AI-native 产品，5 年积累了大量医疗领域的数据和合作客户，这一先发优势使它自 LLM 应用爆发以来就迎来高速增长。

凭借团队对医疗实际需求的深刻理解，Abridge 与美国最大电子医疗系统 Epic 深度整合，让医生能保持原有工作习惯，同时节省大量时间。产品体验方面的普遍好评，使公司能在大型医疗系统客户中实现快速拓展，在商业化方面表现亮眼；收入增长前景清晰后，Abridge 今年吸引到了共计 1.8 亿美元的两轮融资，根据 the Information 报道下一轮估值将达到 25 亿美金，成为 LLM 应用中最受关注的企业之一。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**💡** 目录 **💡**

01  AI + Healthcare 是高需求行业，

      AI Scribe 是首先 PMF 的场景

02  产品与技术

03  商业化：如何在医疗企业 GTM 中胜出 

04  团队及融资

05  市场竞争

**01.**

**AI + Healthcare 是高需求行业，AI Scribe 是首先 PMF 的场景**

**美国医疗行业**

**正在跨越式采用 GenAI 应用**

美国的医疗行业是一个庞大、行动迟缓的系统：

•  根据统计数据，2022 年美国医疗支出共 4.4 万亿美元，约占美国 GDP 总量的 17%；超过同一年全球第三名日本的 GDP 4.23万亿。其中，医院和临床医师服务占总体支出的 50% 以上。       

•  美国医疗行业**对传统软件的采用意愿很低**，医院不愿为 IT 团队增加负担，也不愿培训精疲力竭的员工使用新系统。在典型美国医院的成本结构中，医护人员工资占比平均达到 37%，而 IT 支出仅占 3%。

**而在 Gen AI 应用出现之后，这一切有了变化：医疗行业已经成为采用 Gen AI 产品软件的领先行业。**其中一个重要原因是，AI 产品的上手门槛比之前的 Saas 产品低很多。根据 Menlo VC 估算，**美国医疗企业在 GenAI 软件每年支出已经达到 5 亿美元，**多个研究给出了同一量级的预测。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

因此我们相信**医疗企业的软件支出有着广阔的突破空间**。A16z 提出，未来几十年内医疗市场将至少有一半增长由AI驱动。医疗系统现在最大的问题是：

1）access：好医生的时间不够，病人需要预约很久才能看上病。同时很多好医生因为工作强度大 burn out 离开；

2）cost：第一个问题连锁带来的结果是，医疗系统的人力成本很贵。这两个问题都很适合 AI 来解决。 

现在医院的成本项中人力成本非常重，如果采购 Gen AI 产品能大大改善员工的工作效率，将是投资回报比很高的投资。截至 2022 年底，美国共有 6,120 家医院，以社区医院为主，占比达 84%，而其中 2/3 的社区医院以系统方式运营。这些医疗系统拥有成规模的医生用户群，以此为销售切入点，将为医疗 GenAI 应用带来巨大增量。

注：社区医院指所有非联邦医院、短期综合医院和其他专科医院。而联邦政府运营的医院（占比 3%）通常只为特定患者群体（如现役军人）提供医疗服务。

目前长期市值前 100 名的软件公司中，只有 Veeva 一家属于医疗垂直应用。受益于上述医疗企业跨越式采用的潜在机会，医疗领域软件的新一代独角兽有望在 GenAI 应用中出现。而且对于 existing companies 也能同时受益：2023 年前上市的盈利医疗保健公司（不包括制药公司）创造了 2.6 万亿美元的收入，但只有 1700 亿美元（约 6.5%）转化为利润。**假设 GenAI 应用能将成本和费用降低 15%，**仅此一项就能将营业利润提高 3140 亿美元，使这类公司的企业价值增长 2 倍以上。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

目前医疗 GenAI 应用有着广泛的落地场景，包括药物研发、临床诊断、处理行政工作流、改进护理服务等等。前两类场景的容错率极低，商业化前需要经过漫长的开发和批准周期；相对而言，麦肯锡开展的调研证实了医疗行业对后两类场景的信心：大多数受访者认为 GenAI 潜在价值**最大的领域是提高临床医生的服务质量和生产力，其次是改进患者参与度和体验。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

GenAI 能为医疗行业工作流的多个环节带来变革。在临床属性较弱的环节，专用的 RPA 工具能自动化处理账单、报销、预约、分诊和接收等繁琐的行政事务；而在临床属性较强的环节，我们关注到， 2B 销售表现最为亮眼的软件类型是 AI Scribe。该类应用能够协助医生更加准确、快速地完成记录文档的工作。代表性的公司 Abridge 凭借突出的商业化表现，**创造了医疗工作流 GenAI 软件类别中迄今最大的融资规模。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**AI Scribe** 

**能帮助解决****行业根本性的痛点**

美国医生在医院的正常工作时间之外，往往需要每天加班 1.5-2 小时来**记录临床文档**。这项行政任务源于美国政府从 2009 年开始推行的 **EHR** (Electronic Health Record，电子健康记录系统) 补助，使医院全面采购了 EHR 系统，并要求医生详实填写文档。医生对每次患者诊疗都需要记录 SOAP (Subjective, Objective, Assessment and Plan) 笔记，来记录诊疗和给出处方的过程。**每写一份 SOAP，医生都要照顾到三个截然不同的相关方****：医护团队、付款系统和患者。**这导致美国医生在 EHR 上花费的记录时间约为其他国家的4倍。

EHR 一定程度导致了医疗服务供给的紧缺，因为对医生工作时间占用比较多。从 EHR 开始推行，到 LLM 爆发前的十几年中，预算充足的医院可能会为医生雇佣人工抄写员，负责记录诊疗过程和撰写文档，有些医生甚至会自掏腰包来外包这项工作。而这个过程**可以从全人工服务变成 AI-augmented 服务。**

根据 Statista 数据，**截至 2024 年 1 月，美国医生人数约 110 万人，按每名医生 $300/月 的平均订阅价格计算，临床听写软件的 TAM 约为 39.6 亿美元，**是当前整个医疗 GenAI 应用市场的8倍。

这个市场之前就诞生过成功的独角兽，被微软以 300亿美金收购的 Nuance。Nuance 的产品 Dragon 是世界最早也最成功的语音转文字解决方案，并为苹果 Siri 提供了早期核心技术。公司从 2006 年开始收购一系列医疗领域的转录、文档产品，**积累了医疗行业的垂直技术和商务关系；**同时，Nuance 把握住了 2009-2011 年的政策红利，大大推动了医疗销售的增长。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Nuance 通过一系列收购构建了医疗领域能力

2012 年开始，Nuance 开始转型，成立了 4 个行业业务部门来直接为不同行业提供解决方案。其中，医疗业务占比最大。截至 2021 年，Nuance 62% 的收入都来源于医疗健康领域，达到 8.4 亿美元。Dragon Medical 平台**几乎达到垄断地位**，被美国 77% 的医院，55% 以上的临床医生和 75% 以上的 X 光工作人员所采用，全球也有超过 55 万医生使用。

但 Dragon 在语音识别和生成上做得是不够好的：这项技术只能作为文档记录中的辅助，也没有自动集成于 EHR 系统，医生需要花费大量时间对 Dragon 生成的转录文本进行重新加工。

这个问题是比较难解决的：白宫健康顾问 Atul Gawande 在《为什么医生恨他们的电脑》中描述到，在手写时代，医生的笔记短小精悍，但在 EHR 记录病人的详细病史时，不同医生就会由于需求不同，对同一件事写出不同诊断，比如，为了申请医保报销，骨科医师写“腿痛”就够了，但其他医生可能认为缺乏细节，会写成“右膝盖骨质疏松”。

疫情让美国医生的 burnout 比例在 2021 年飙升至历史新高 62.8%，而在2024年这个数字首次降至 50% 以下 (48.2%)。除了疫情结束、人手增加等原因，根据 EHR 供应商 eClinical Works 发布的新报告，用于临床文档的 AI 新技术也发挥了重要作用。

在使用相关软件前，超过 40％ 的医生每天仅在文档记录上就花费4个小时以上。而超过一半的医生表示，AI 医疗文档软件每天可以节省至少2小时的工作时间。节省下来的时间将使医生能够专注于不那么琐碎的任务，并有更多的时间陪伴患者。

**综上所述，Abridge 所在的 AI Scribe 赛道有着高度的确定性。传统巨头已经验证了市场内出现独角兽的可能性，GenAI 解决行业关键痛点、重塑市场格局的能力也已经明朗。**

**02.**

**产品与技术**

**产品介绍**

• Abridge 的产品逻辑比较简单，先通过自动语音识别 (Automated Speech Recognition, ASR) 听写诊疗过程，再利用 GenAI 生成符合要求的文档。从 2024 年年初开始，凭借对于美国最大 EHR Epic 系统架构和数据格式的深刻理解，完成了与 Epic 的无缝集成。产品形态类似 Epic 系统的插件，医生无需在多个选项卡之间切换，不需要改变现有的工作习惯，使用体验非常丝滑简便。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

诊疗开始前，医生在征求患者同意后，能直接使用 Epic 移动端应用 Haiku 中的 Abridge 产品（如下图左侧手机所示），对谈话全程进行录音，实时生成草稿，并可以随时加入备注。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

诊疗结束后，能在短时间内生成附有原文证据引用的标准临床笔记及自动摘要（如下图所示），并自动导入 Epic 系统。医生能够直接在 Epic 的 PC 端应用 Hyperspace 中查看和编辑笔记（如上图右侧电脑所示），左侧是规范格式的 SOAP 文档，而右侧是对话全程的文字记录。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

临床笔记中的内容附有原文引用

除了解决**临床医生**的痛点，Abridge 也关注到了患者和护理人员。在他们的路线图中，对于第一部分提到的**改进护理质量、提高患者参与度和体验的场景**，也有着明确的规划，**有利于长期内市场份额****的持续提高。**患者记错或忘记医嘱的情况很普遍，Abridge 可以给患者也提供一份完整文档，对注意事项提供指导；客户表示其他竞品没有强调这一功能。2024 年 7 月，Abridge、Mayo Clinic 和 Epic 宣布为护士推出文档产品，目前仍在开发中。

**AI-Native 的技术优势**    

•  在 GenAI 应用爆发前，Abridge 就已经在开发自己专用于医疗领域的 ASR 模型和文档生成模型。对于自己的“AI-native 特性”，Abridge 给出了三点证据：

1）使用有差异化的数据、提示工程和微调方法，从底层开始构建了端到端的 LLM 堆栈；

2）有自己的医疗 AI 性能评估方法，并在这一领域成为技术先驱；

3）将用户行为数据重新用于模型迭代，实现闭环。

数据方面，自2019年开始，Abridge 就在匹兹堡大学 UPMC 医疗中心的数据库基础上，用 150-200 万诊疗记录作为数据集训练了自己的 AI，所使用的类型包含临床音频、转录规范、人工撰写的参考笔记以及患者特征的元数据，并在去标识化方面严格遵守了安全隐私标准。

医疗 AI 评估方法方面，Abridge 在白皮书中进行了详细介绍。

**a.** 在 ASR 环节，除了单词错误率 (Word error rate) 等通用指标，还会重点关注医学专业指标，如医学术语召回率(Medical term recall rate)、对药物名称的捕捉等。目前关键指标超过了市面其他的开源模型。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**b.** 在文档生成环节，Abridge 通过自动计算质量指标来比较 AI 生成和人工撰写的文档质量，保证医学应用中的准确性和完整性：例如，如果医生纠正了病人自述的状况，在最终文档中只会保留正确的结论。当患者谈论的话题出现跳跃时，Abridge 也能完成分类整合。

开发过程中，Abridge 使用 **RLHF** 方法，请一批临床医生进行盲测反馈，确保文档质量过关，且能满足现实里医生多样化的写作习惯。在模型正式发布前，还会持续收集主动和被动反馈（如医生的编辑行为），来持续改进关键指标。

相对于通用模型，高度垂直于医疗行业的策略使 Abridge 的模型能显著、更准确地识别医疗术语，并将病人高度多样化的口头表述转化为规范的书面文档。根据 Abridge 官方数据，产品适用于 50 多个医学专业领域，支持 14 种以上的语言，AI 能完成 91% 以上的文档记录工作量，每个月能够为临床医生节省**超过 70 小时**的时间。

**03.**

**商业化：****如何在医疗企业 GTM 中胜出**

虽然在 GenAI 爆发前，Abridge 就掌握了正确的数据策略和技术路线，但 AI 应用要为传统行业带来跨越式变革，卖点往往并非技术有多么酷炫，而是**产品有多么易用，以及如何从 Day 1 就能向客户交付即时价值。产品能解决用户的刚性需求，才会在客户访谈中看到有医生反映 “如果医院不采购 Abridge 就会辞职”。**

2022年11月 ChatGPT 的出现对医疗企业进行了 AI 应用的市场教育。彼时 Abridge 产品已经历了4年左右的开发，经过了数千次的医患对话训练；渠道方面，除了 Abridge 团队主动通过医疗人脉拓展市场，医疗企业的 IT 负责人也会主动通过健康展会接触供应商。这让性能已经较为成熟、且在合规方面做好准备的 Abridge 脱颖而出。

**不同科室的专业性需求差异较大，一种 SaaS 产品未必能全面满足。因此医疗系统企业往往会同时考察和试点多种产品，而在做出最终采购决策时，也会在组织内保留多个供应商，分比例使用，这成为 Abridge 实现存量替换的基础。多名客户表示，会同时采购2-3种产品，Abridge如果通过试点，在企业内使用人数占比在20~60%不等。在支付意愿方面，从替代人工的角度估算，**相较于时薪约为10-20美元的人工抄写员，AI Scribe 能够节省大量成本，同时也意味着付费上限仍然较高，即使对于收入规模相对更低的医疗企业，每人每月 200 美元也是相对舒适的定价。

然而，医疗领域 SaaS 产品需要满足严格的合规要求，包括 **HIPAA 和 FDA 的多重标准，在数据隐私安全等方面通过认证，且需要经过多轮评估、试点和推广流程，完整的销售周期一般在一年半到两年左右。**

• 医院首先需要对产品进行临床评估，通过后进入临床操作阶段，测试整合方面是否存在障碍；如果通过，还要进一步研究产品的单位经济效益，尝试协商价格，并确定试点范围和时间线。

• 试点一般会从初级的家庭医疗、儿科等高流量领域开始，并同时采用多种产品进行对比。供应商要与医院合作微调或开发新功能，这一过程需要半年左右时间。第一轮试点结束后，还需要进行进一步评估，对结果满意率足够高，才可以扩大范围，开展下一轮试点。

• 最终基层员工有选择是否采用产品的自主权，例如年龄较大的医生可能不会使用任何软件，或继续使用原有的传统产品。因此试点中，医护人员对产品的反馈意见至关重要。

Abridge 能够快速推广，正是因为一线医疗工作者对产品效果的反响非常热烈。根据 Emory 医疗系统内医生的反馈，产品使他能“把所有注意力集中在病人身上，而不需要担心文档；在结束问诊后只需要再在医院花一点时间校对和编辑”。在 KLAS 2024 报告中，Abridge 在改善临床医生体验方面得分 95.3（平均分79.6），排名第一；在改善患者体验和改进诊疗结果方面，也分别排名第三和第四。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

而在企业测算此类产品的ROI时，并非仅关注财务上的直接增收。客户表示，采用 Abridge 虽然平均每天可以为节省2小时左右的工作时长，但主要是减少在家加班的“睡衣时间”，问诊时间几乎没变，也难以接待更多病人并增加收入。但是，Abridge 能提升诊疗、护理的准确性和质量，并显著改善医生工作生活质量，**防止因职业倦怠导致医生流失带来的高昂隐性成本，并减少因诉讼、赔付带来的损失。因此，客户仍有较强动机购买此类产品。**

Abridge 表示，近两年医院客户开始一反常态，快速购买他们的产品。**自 2024 年初以来，几乎每周都会宣布一个新的医疗系统客户。**2024年2月，公司宣布与康涅狄格州规模最大、最全面的医疗保健系统*耶鲁纽黑文*达成协议，使数千名临床医生开始使用 Abridge。其他大型客户还包括 Emory Healthcare，社区医疗系统 Reid Health 等。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

虽然医生个体角度的切换和培训成本较低，但企业层面仍有较大粘性。医疗 SaaS 一旦签订正式合同，期限就在2-3年左右，不会轻易被更换。**Abridge 前期的积累使其占据了有利的客户基础和市场地位，目前已经进入收入确定性较高的快速增长期。**

**04.**

**团队及融资**

**团队** 

Abridge 成立于2018年3月，创始人兼 CEO 是 Shivdev Rao 博士，是一名执业心脏病医生，本科毕业于 CMU，此后在匹兹堡大学医学中心（UPMC）的心脏和血管研究所担任教授，对医生的工作习惯有着深刻理解。在丰富的临床医疗经验之外，他兼有创业背景，曾创立 DocDok 和 Litcall 等几家公司，同时也在 UPMC 的创新、商业化和风险投资部门担任执行副总裁，投资医疗科技初创企业。而 CTO Zachary Lipton 负责公司的机器学习方面，同时在 CMU 担任教授。

首席商业官 Brian Wilson 有 20 余年的商务拓展经验，近 10 年来主要在纳什维尔的 SaaS 和医疗公司负责销售，曾在短信营销平台 SlickText 担任 3 年 CRO ；而首席临床官 Tina Shah 是美国多个医疗领域委员会内的专家，曾任美国卫生局局长办公室高级顾问，也是白宫研究员基金会董事成员，能为公司拓展客户关系提供背书。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

公司领导团队

与其他侧重市场销售的同类公司不同，Abridge 的领导更专注于搭建团队和更新技术，根据 Linkedin 不完全统计，技术类与销售类员工的占比约为 2:1 ，凸显了团队对于技术的重视。

商业化方面，公司的**企业拓展总监**均有其他医疗 SaaS 类或竞品企业工作经验，对东部 (NY) /西部 (CA) /中部 (IL, TN) /南部 (TX) 地区均有覆盖。在今年结束新一轮融资后，公司还招聘了一批有多年 **Epic** 工作经历的员工担任合作成功总监。营销/增长总监在谷歌拥有 10 年左右的营销经验，曾帮助推动 Drive、Workspace、Android 等产品的增长。

团队在 EHR 和医疗企业的丰厚经验，及地理分布上的广度有助于在全美范围内拓展医疗系统客户，并保证顺利将产品集成到工作流程中。

**融资**   

在 GenAI 席卷全球并吸引风投之前的 2019 年，当创始人向 Union Square Ventures (USV) 介绍 Abridge 利用 AI 辅助医生文档记录的想法时，Andy Weissman 表示 “这个想法相当古怪，之前没有人这样做过。” 然而，客户和投资人非常欣赏 **CEO 本身的医疗背景和务实精神，**创始团队的 CMU 背景也使他们信赖公司在 AI 方面的实力。Abridge 就这样拿到了自己的第一轮融资。

团队“医疗+ML”的复合背景，在后续的融资中也在持续发挥作用，相对 Ambience、Suki 等竞品以软件开发背景为主的创始团队，投资者相信 Abridge 创始人的医疗经验能让团队更加理解用户需求，从根本上提高产品能力。

目前，公司已经融资 2.1 亿美元左右。在2023年10月，完成由 Spark Capital 领投的 3000 万美元的 B 轮融资后，仅仅 4 个月，公司又完成了 **1.5 亿****美元**的 C 轮融资，由 Lightspeed Venture Partners 与 Redpoint Ventures 领投，投后估值约为 **8.****5 亿****美元**。CVS Health、Lifepoint Health、Mayo Clinic 等大规模医疗机构和 NVIDIA 也参与了 Abridge 的投资。

2024年10月，根据 The Information 消息，Abridge 正在筹集 **2.5 亿美元**。科技投资者 Elad Gil 和 IVP 将领投这笔投资，Alphabet 的 CapitalG 基金预计也将参投。据报道，该轮融资**估值将达到 25 亿美元，相对目前 5000 万美元的 ARR，P/S 已达到 50x，而相比一年前 2 亿美元的 B 轮估值则翻了12.5倍。**公司表示，部分资金将用于开发新的 AI 模型，以及尚未发布的新产品。

**05.**

**市场竞争**

GenAI 应用开始落地后，涌现出 Abridge, Augmedix, DeepScribe, Nabla, Suki, Ambience 等一系列产品，能以前所未有的准确性和速度生成文档，并自动集成至 EHR 工作流中。各家产品的价值主张整体方向是相似的，都是通过听写并生成临床文档，解决当时 Dragon 无法解决的医生“睡衣时间”问题，主要区别在于**实际的产品力细节****、定价和企业销售能力。**市场空间除了医疗系统内替换 Dragon 等产品的存量需求，还可以对长尾市场中高度分散、采用手动记录的小诊所进行销售。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然而，AI Scribe 公司挑战传统巨头时仍然面临阻力。Nuance 在 2021 年 4 月被微软以 197 亿美元巨资收购，并嵌入微软医疗云。由于微软的支持和已有的市场基础，Nuance 仍在技术和商务上保持着深厚的护城河，公司有着强大的捆绑销售能力，在医疗企业内很难被完全替换。

为了应对竞争，Nuance 在 2023 年 2 月推出了基于 GPT-4 的语音 AI 应用 **DAX Copilot**（发布时名为 DAX Express）。DAX Copilot 是在 Nuance 2020 年发布的 DAX 基础上进行升级的，此前，DAX 通过自动语音识别和人工审查将口头问诊转换为临床记录，但是整个过程需要耗费 4 个小时。而 DAX Copilot 仅在几秒内就能够生成文档，并允许医生随时编辑临床笔记，虽然相比含人工的 DAX 完整解决方案个性化程度较低，但定价仅为全套的 1/3 左右。

DAX Copilot 基于1200万个左右的诊疗数据集进行训练，是 Abridge 训练规模的 6-8 倍，理论上有着更高的准确率。但**大多数同时采用几项产品的客户表示，各个竞品的准确率在实际使用中区别并不显著，**最终都需要一定程度的人工校对。

在成本方面，DAX 价格较高，对于 500 人左右的组织，每年 DAX 完整方案收费约为 1000 万美元左右，折合每月每人 1600 美元左右；DAX Copilot 成本也达到每月每人 400-600 美元。而 Abridge 则为每月每人 250-350 美元，对初级保健和非专科领域尤为经济。

除 Nuance 之外，初创公司竞争者各有侧重，其中有着鲜明性价比优势的一家产品是 Nabla，仅需每月每人 100-150 美元，笔记生成时间仅为 12-15 秒，客户可以接受牺牲一定的准确率来换取成本的大幅节省。从客户反馈来看，目前 Abridge 仍然领先其他初创公司一个身位，市场不存在明显的第三名。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

各个产品的另一大显著**区别在于与哪些 EHR 集成，以及整合程度。多名使用 Epic 的客户表示，与 EHR 的无缝集成是 Abridge 最令人印象深刻的亮点。**这一因素看似壁垒不高，实际背后暗示着 Abridge 与 Epic 高度紧密的关系。客户反映，Abridge 和 Epic 的合作关系是随着时间的推移慢慢建立起来的，其他新进入者难以挑战。而尽管其他竞品集成的系统数量更多，或宣称与 EHR 的深度集成，但可能仅限于 API 接口的表面集成，在使用体感上依然存在学习成本，没有达到无缝程度。

根据 Definitive Healthcare  Atlas Technology Install Dataset 和 HospitalView 产品数据，截至 2024 年 1 月，**Epic 是美国医院市占率最高的EHR，达37.7%。**虽然 Abridge 没有向其他 EHR 拓展，但 Epic 自身的客户群已足够庞大，而公司已通过深耕成为 Epic 系统中的领导者，是目前唯一一家公开显示嵌入到 UI 层面的；同时，Epic 自身的自研类似功能上线周期可能非常久，目前还不会威胁到 Abridge 的地位。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

美国医院 EHR 供应商市场份额排名

综上所述，Abridge 在技术上实现了足够的专业度和准确性，在与 EHR 的集成上也占据了较好位置，但未达到断层领先或足以垄断的程度，由于文档最终存储于 EHR 系统中，作为插件也并不具备数据粘性。在医疗 AI Scribe 的竞争中，Abridge 所构建起的壁垒更多在于已有的 GTM 成就。相比其他初创公司，Abridge 熬过了漫长的销售周期，从占领用户心智开始，稳固了一定的企业端份额；有望通过锁定和飞轮效应，进一步扩展客户网络。然而，由于客户往往不只使用一个供应商，想要发展为市场寡头，还需继续关注公司未来如何从产品条线、EHR 集成、定价、商务等方面创造相对 Nuance 的差异化优势，并保持领先于其他初创公司的地位。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

排版：Doro

延伸阅读

AI Coding 最全图谱：Agent 将如何颠覆软件

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Sora V2 即将发布，AI Creativity 赛道有哪些机会？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

AI-native 应用长什么样？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxIia4dtherNtfj4om3icINqV9zh6LMDG2RAvzMFWpibzL5pWJI3jj36ibNc8nkkQdTYicETRbG8PCmH3g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=28)

Anthropic 创始人最看好的领域，AI for Science 深度解读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxIia4dtherNtfj4om3icINqV9zh6LMDG2RAvzMFWpibzL5pWJI3jj36ibNc8nkkQdTYicETRbG8PCmH3g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=30)

AI 影响最大的行业？LLM 如何让教育产品化

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxIia4dtherNtfj4om3icINqV9zh6LMDG2RAvzMFWpibzL5pWJI3jj36ibNc8nkkQdTYicETRbG8PCmH3g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=32)