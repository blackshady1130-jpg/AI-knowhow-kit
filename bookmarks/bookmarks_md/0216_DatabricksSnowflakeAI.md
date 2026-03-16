---
url: https://mp.weixin.qq.com/s/SlzIyqhSLcRdBVfeyJbtjw
title: "Databricks联合创始人：从对决Snowflake到如何与AI共存 ｜ 硅谷徐老师"
description: "编者按：一年多前，徐老师和 Databricks 联合创始人 Reynold 做过一次对谈，聊到了大数据和"
author: "声小音"
captured_at: "2026-03-08T10:57:55.754Z"
---

# Databricks联合创始人：从对决Snowflake到如何与AI共存 ｜ 硅谷徐老师

**编者按：**

一年多前，徐老师和 Databricks 联合创始人 Reynold 做过一次对谈，聊到了大数据和 AI 的下一个机遇。

一年多时间过去，AI 时代已扑面而来。科技公司你追我赶，新成果层出不穷，不掌握技术的普通人也觉得 AI 触手可及。上一期硅谷徐老师节目的嘉宾贾扬清，现在也正在 AI 领域创业。

本期节目中，硅谷徐老师再次对谈 Reynold，聊一聊在这个时代里，世界、行业、你我，将经历怎样的巨变。

▲本文部分内容整理自播客「What's Next丨科技早知道」节目。更完整对话，请收听本期节目。

![图片](https://mmbiz.qpic.cn/mmbiz_png/EHIBI8jx09bLl4vtGVyTKTibbQLmClZ2mc6GdepIaFUQ29IouxdNx9JVWHa8VLaRm4MseJnh8O8VYKSUsxay0Qg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**这是最好的时代吗**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

▲本期节目嘉宾Reynold、主持人徐老师和上期节目嘉宾贾扬清（从左至右）。| 图源：硅谷徐老师

**徐老师：**最近 Databricks 的 CEO 和 Databricks 友商Snowflake 的 CEO 几乎说了相同的话，就是现在不管对于行业还是个人来说，都是最好的时代，你对此是怎么看的呢？

**Reynold：**我很相信这一点。对于我们这些做技术的人来说，之前没有任何一个时代像现在这么激动人心。在这个行业里，不管你是做前端还是后端，只要与之相关，你就可以看到你做的一点一滴正在慢慢改变这个世界，而且改变世界的速度越来越快。

几十年前，做硬件可以改变世界，但做一个硬件可能需要好几年时间才能看到成果。而今天因为有了 AI 和云计算，一个改变很可能几天之内就可以看到成果，可以直接和间接影响非常多人，而且影响的力度也越来越大。

**徐老师：**在我们上一次的对话中，你就提到 Databricks 是一家拥抱 AI 的公司。半年多前，OpenAI 的 ChatGPT 横空出世，大家都觉得生成式人工智能发展到了一个新阶段。你觉得现在的 AI 和一年多前你谈到的AI 有了哪些不同呢？

**Reynold：**首先是具体技术上有一些本质的区别，比如现在大模型的参数非常大，训练成本非常高。

但我觉得更重要的可能并不是技术上的区别，而是 ChatGPT 发布后，突然间大家感到 AI 好像正在颠覆自己对世界的认知，对计算机的认知，对互联网的认知。这个「大家」不光是技术人员，还包括了不懂技术的人，比如大家的爸爸妈妈，比如各个公司的 CEO。

一项技术的成熟和推广有两点因素很重要。第一是要有足够多的人相信它；第二是要有足够的人相信自己能够应用这项技术。

在 ChatGPT 出来以后，我觉得全世界没有 100%，也有 99% 的人相信现在的 AI 和以前不一样了。同时，他们也突然间觉得 AI 离自己很近，不一定说是自己去开发模型，而是可以利用 AI 改变或提升自己的业务。我觉得这两点是一个市场成熟和爆发最重要的基础。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

▲图源：Getty Images

**徐老师：**从这个角度上来说，AI 确实已经大不一样了。两个月前，在 Databricks 成立 10 周年的聚会上，你有一个观点让我感触很深。你说，如果生成式 AI 出来以后，各大企业软件公司不重新考虑数据栈 （组成云原生数据平台的技术集合），不去拥抱新的潮流，那么不管公司以前发展得多好，都会被边缘化，会变成恐龙。

**Reynold：**我要先解释一下，我说「变成恐龙」，并不代表这个公司会一夜之间消亡，而是可能进入一个10 年、 20 年甚至 30 年的衰减期。在衰减期里，这家公司甚至是越做越好，利润或营业额越增长越快。对于周期很长的企业软件公司而言，一个很好的或很不好的影响因素，其产生影响的过程都是缓慢的。

我认为 AI 带来的最大冲击是人机交互方式的改变。传统上的交互方式，比如命令行模式、API 编程模式，相对来说都有一定门槛。但现在有了非常简单、非常有效的自然语言交互模式，可以真正实现数据民主化，即使你完全不懂编程，不懂任何应用技术，也可以用自然语言和 AI 沟通。这会给交互界面带来颠覆性的改变。

另外一个重大影响是对数据平台的。未来公司都会希望把 AI 应用在生产线上，提升效率、利润，降低成本、风险。当大量 AI 应用在生产线上时，需要线上线下平台有非常好的集成，先在线下平台训练模型，把模型迁移到生产线上后，进一步评估，能得到结果，再把结果数据带回线下平台，继续训练、评估，做出更好的模型，这是一个完整的闭环。

传统的数据平台基本上是离线状态，和生产线上的平台完全分开。AI 的出现，会加速线上线下融合。如果一个公司只能提供很好的线上平台，或只能提供很好的线下平台，必然会处于劣势。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**模型越大越好吗**

**徐老师：**最近关于大语言模型的讨论很多。Databricks 也有很多动作，自己做了开源模型，也收购了开源模型公司。你是怎么看待开源模型和闭源模型的？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

▲图源：MosaicML

**Reynold：**我觉得开源模型很重要。从生态的角度来看，你会希望看到一个百花齐放，而不是极个别厂家垄断所有模型的未来。

从具体应用的角度来看，开源模型也有很多好处。很多情况下，大家都不知道模型是怎么来的。开源模型重要的不仅是模型本身开源，而且是创造模型的过程开源，这相当于提供给大家自我训练模型的过程，或者基于现有模型调整的过程。企业在应用过程中中，就可以根据需要剔除不需要的数据。

**徐老师：**尤其 Databricks 就是从开源软件起家的，你对开源模型肯定有更强的认同感。但我有一个问题，那就是现在的闭源模型用大量 GPU 卡来训练，绝大多数开源模型背后其实没有那么多 GPU 卡，这会不会让开源模型在根基上就处于劣势？

**Reynold：**讨论这个话题，首先需要区分不同的应用场景。在 99% 的企业场景里，需要的不是一个 Chatbot （聊天机器人），能写邮件，读文档，探讨人生意义。绝大多数企业需要的是在垂直场景里的应用，像是通过 Supportbot 做实现客户支持。所以，如果想做一个全知全能什么都能干的 bot，那么现有的开源模型可能在接下的一年里都远远无法与 GPT 4 和 Claude 比，但对于绝大多数企业而言，很多小大模型其实更好。

举一个例子，我们 Databricks 内部经常碰到客户有很多表格，但并没有很好地注释，导致数据挖掘做得不好。于是我们训练了一个专门针对这一任务的小大模型，可以基于客户现有的工作负载，自动生成对每一个表格，以及表格里每一列的描述。我们对比了 GPT4 和我们自己训练出来的模型，发现我们自己的模型效果更好。

太大的模型也有弊端。一个是成本高。比如我只需要生成 C 语言代码，不需要生成莎士比亚的文章，但就算没有用到这些需求，相关参数也在那里，这会带来一定的成本，尤其是大规模应用的时候，这会变成很大的问题。另一个问题是速度慢。有太多的计算需要完成，而很多计算其实和真正需要的应用场景没有关系。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

▲图源：Getty Images

徐老师：我非常同意你所说的，在企业的应用场景里，其实用不了那么复杂的大模型。但大模型的编程能力是不是比开源模型好很多？编程能力越强，越不容易出错，也越能做复杂的事情。

Reynold：我觉得小大模型有了好的训练数据，也会训练出非常好的编程能力。

与其讨论模型的大小，更重要的其实是看训练的数据。MosaicML 的数据分析团队，就几乎和它的模型训练团队规模差不多大。在模型训练里，很重要的一点是能不能找到合适的数据来训练。数据并不是越多越好，不好的数据反而会影响模型的效果。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

▲Databricks的CEO兼联合创始人Ali Ghodsi、MosaicML的CEO兼联合创始人Naveen Rao（从左至右）|  图源：Fortune

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**工作会被取代吗**

**徐老师：**最近大家讨论的另一个热点是生成式 AI。你觉得生成式 AI 会给我们带来怎样的影响？

**Reynold：**很明显，在很多领域里，AI 已经达到可以被应用的程度，甚至可以在某些特定领域模拟人类。这创造出大量「人力资源」，让「帮你想，帮你写，帮你生成东西」一类工作的边际成本趋近于零。

我们有一个广告客户，之前有 200 个写手，现在只保留 10 个人。而这 10 个人的主要工作也是训练语言模型，以及完善语言模型生成的东西，效率比以前还高了很多。

**徐老师：**这也是大家很关心的问题，我们的工作会不会被 AI 取代？

**Reynold：**我觉得专业性低的人，受到的影响大，因为他们的产出效果可能不如 AI，而且他们远比 AI 贵。

而专业性越高的人受到的冲击越小，比如有全局观念的架构师、比如性能优化师，再比如能把商业需求转化为技术需求的人。而且他们会变得越重要。过去一个资深员工带 10 个初级员工，现在可能只需要带一两个，在 AI 的帮助下，就可以实现原来 100 个人的产出。资深员工的边际成本降低了，反而会更吃香。

AI 可能会造成大量失业。但这种情况也不是第一次出现，每一次工业革命、技术革新都会导致很多人失业。我觉得这需要政府和社会共同应对。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

▲图源：Getty  Images

**徐老师：**那具体到高科技行业，从前端工程师、后端工程师，到数据工程师、数据科学家，再到产品经理，这整条链路上的从业者会不会越来越少，谁又可能是最后留下来的人？

**Reynold：**我其实觉得这些人不会越来越少，反而会越来越多，这好像跟我刚刚说的有点矛盾。原因是随着工具越来越易用，会有越来越多的人掌握这些技能。今天如果不懂 Python，不好意思说自己是数据科学家，未来的数据科学家可能完全不需要懂编程，但需要有理解数据的能力，要能在数据和商业间作转译。

推测 AI 对大家是好是坏，有意义，也没有意义。即使没有 AI， 也会有些工作越来越吃香，有些工作越来越不吃香。你总归要去适应。AI 只是加快了变革的速度，并不是说你本来不需要考虑这些问题。

**徐老师：**那对现在刚进入职场或还在读书的年轻人，你有什么样的建议？

**Reynold：**对于年轻人，我的建议一直都是一样的，就是你需要有学习能力，包括你可不可以很快适应一个新的环境，可不可以很快适应新的工具。

我并不知道未来世界会怎么发展，但我唯一可以确定的就是，未来世界的变化会越来越快，你的学习和适应能力越强，你的生存和发展能力就会越强。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](https://mmbiz.qpic.cn/mmbiz_png/EHIBI8jx09bLl4vtGVyTKTibbQLmClZ2miaoqc3RPOy2ltr59mLPyepEMEaIicMZ0Aw017f65ialAgEgib55bOkEtbg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)