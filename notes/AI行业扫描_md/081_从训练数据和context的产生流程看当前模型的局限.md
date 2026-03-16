---
url: https://mp.weixin.qq.com/s/muwkgMxUlX_v4i4nFOTbXA
title: "从训练数据和context的产生流程看当前模型的局限"
description: "1/ 大模型在除数理、科学等有清晰对错领域之外，洞察力有很多欠缺，即使最好的模型也一样。"
author: "Xuanhao"
captured_at: "2026-03-09T03:25:29.389Z"
---

# 从训练数据和context的产生流程看当前模型的局限

1/ 大模型在除数理、科学等有清晰对错领域之外，洞察力有很多欠缺，即使最好的模型也一样。现在AI搜索、深度研究、通用Agent类产品的最大问题是模型和公域信息都已经被垃圾信息污染，关键信息缺失，不论是事实类信息还是观点类信息都有很多问题

2/ 例如，如果和AI进行历史话题/投资标的相关的讨论，模型只能给出互联网上的平庸答案，没什么真正的insights，很难把一个历史事件/一家公司最核心的逻辑抽象出来，现在的Deep Research功能，多数时候本质是Deep Summary，主要做总结，把网上现成的信息整合一下，即使最好的模型也是这样（GPT-5 Pro/Grok 4 Heavy）

之前写过多次，用户体验 =【模型】+【Context】，归因AI产品用户体验的问题也可以从这两个方面出发

3/ 现在大模型在预训练阶段虽然能把整个互联网的知识压缩到几千亿的参数中，但多数 base model 压进去的数据质量并不高

即使是维基百科/substack/书籍/公众号这些质量相对高的数据，也会有很多垃圾，但可能被直接拿去训练了。只是用类似Common Crawl这种质量的数据喂出来的模型，就好像一个人的三观完全靠阅读互联网建立，会和真实世界存在巨大的分布偏移，尝试回忆一下你深入了解过的一些吊诡真相，其实很难出现在公开数据中

4/ 预训练数据中藏污纳垢的程度可能远超想象，大模型已经在预训练阶段构建了一个粗糙的隐性世界模型（implicit world model），但这个世界模型的偏见和污染非常严重。如果把从真相（Truth/Reality）到训练数据看做一个链路/漏斗，有很多环节会丢信息，粗略拆一下：

1）从全量信息到文字的损失：有一部分信息从来没有变成文字或语言，我们知道的信息比我们能说的更多（可能是不想说/不能说/忘了说/不会说...），很多信息和思考过程只在脑子里。人会在脑子里做简短的思维链推理（甚至不一定用自然语言），但永远不会讲出来。其他多模态的视觉、听觉等等信息更难加入到预训练当中

2）从语言文字到数字化的损失：在人类输出的语言文字中，只有一小部分被数字化了，例如私密交流，这些内容只在从未被数字化的短暂口头交流中，但这部分信息的含金量非常高。显然，“当面交流、阅后即焚”的信息更接近真实世界，不能播的才是真相，有些内容要“打码”

3）从数字化到公开化的损失：出于种种原因，即使是数字化的文字，也只有部分能在公域流通，且相比公开数据规模也并不大。比如公司内部数据/闭门交流/敏感内容，各个行业都有这种内容，最接近真相，但出于利益关系和隐私等原因，模型公司目前无法获取这些信息进行训练

4）从公开化到训练数据的损失：对于海量的数据，怎么确定哪些数据能最大程度反应真相，或者说不那么错误？公网上大部分内容都是垃圾，避免极少量的高价值内容被海量平庸内容稀释非常困难，模型公司的数据团队想做到这点是非常困难的，算法/数据团队多数情况下只懂技术，健全常识和品味完全是另一种能力（所以这点上需要模型公司有意识地特别投入资源）

5/ 对于公开信息而言，现在供给端的奖励函数是扭曲的，内容生产的激励结构上存在问题（the incentive is fundamentally mis-aligned）。公开内容一方面会作为训练数据影响模型能力，另一方面会作为Context的一部分影响AI交付的结果/体验，对于AI搜索、深度研究这样的功能，Context是AI交付质量的决定性因素。互联网上的信息源众多，该看哪些？如果依靠关键词匹配，大概率搜到的内容上限不高，会被互联网的平均水平锁死。很多情况下，往往是1%的内容贡献了99%的价值，关键总是如何区分出这1%

目前内容生产者大概有几类：UGC-路人创作者，PGC-专业创作者，BGC-企业传播, GGC-政府类，绝大多数内容都是在为流量/营收或者其他特殊目的做优化，所以在内容供给端的激励层面，至少会有以下问题：a）多数内容供给要去主打人数最多的大众群体，注定很难全面深入反映复杂多面的现实，b）内容本身和内容消费者的长期利益脱钩，甚至相违，很多内容甚至直接就是真相的反面，表面上鼓吹X，实际上完全是Y，c）现在国内的内容商业生态不一定能支持最聪明的人来从事内容生产...

6/ 所以公域数据会有以下问题：

a）公域数据质量低：，信息脏乱差（所谓公域，说不好听就是阿猫阿狗都能上来拉一坨），例如散播的谣言、捏造的叙事等等，很多领域的信息操纵十分严重，任人打扮的小姑娘不只是遥远的历史，更包括我们周围的各种叙事和完全错误的说法，比如一些连例子都没法举的说法，真相往往有很多个侧面

b）公域数据的分布不均衡：即使有优质信息，也会被海量的平庸内容稀释到接近0，尤其商业、科技、财经类内容。公域内容就是普通人喜欢关注的内容，在核心问题上和真相、洞察甚至是对立的。能接近真相的高质量内容，在互联网上的相对数量太少

c）公域数据被AI污染：现在AI生成的内容正在加速淹没互联网，已经严重到不同模型的输出开始趋同（Model Convergence），各家AI模型开始相互蒸馏彼此输出的内容，也侧面印证了公域数据中AI的占比迅速上升

现在各大内容平台已经开始出现大量的AI内容，而且很多吃瓜群众都没意识到，数据甚至很好。如果说真相和好的品味在少数人手里，那其实AI会放大低质量内容，把最好的内容进一步稀释，互联网会加速成为 streaming pile of shit

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

对于kill time的娱乐内容而言这个问题还好，因为标准很好验证，让用户“爽”就行了，但是生产力类的场景的卡点在于验证/反馈的困难，一篇research paper/strategy analysis/stock pitching/invest memo的好坏如果能验证，甚至能找到稳定的奖励信号，那几乎等于超级智能实现。在真实世界里进行验证难度极大，表面上看起来不错的分析，最后落地业务/portfolio亏成稀巴烂的情况每天都在发生

7/ 2024年Ilya Sutskever说我们只有一个互联网，但实际上即使我们有更多个互联网，又能提升多少模型能力呢？公域很多内容都是重复的，人教版/苏教版/沪教版各种教材都学一遍会增益有限，因为有价值的只是少量核心，所以即使再来十个互联网的数据，如果没有多样性，内容分布和现在类似，贡献的边际增量也不大，这也是为什么基本所有人都在喊online learning/era of experience的原因

8/ 以上所说的问题，在没有客观对错的通用领域尤其明显（下一篇文章我会讨论怎么思考通用类场景，stay tuned:），而有客观对错的数理、工程、科研类问题并不在大多数人的生活里，只是相对少部分人的需求，更多垂直场景的 long-tail 问题往往有非常细碎多样/nuanced的答案，现在的模型还捕捉不到

9/ 如何提升最终AI的交付效果：

1）模型：花大功夫优化预训练的数据集，会是一个长期不断的 ongoing process，这也不是一个单纯的技术的问题，因为训练数据会决定AI有什么样的世界观和价值观，很多东西也不好公开聊。总之就是需要一定程度上重写互联网，给现在pre-train数据集做大量的增删改，让base model里的隐性世界模型更接近真相，这里有大量工作要做

例如，最近的一篇论文《LLMs Can Get "Brain Rot"》显示，如果混合低质量数据做continuous pre-train，会导致模型能力的全面下降（推理跳步，事实性错误，安全性及模型个性不稳定等问题）。这里的低质量数据指的是阴谋论，无根据的观点，夸张类内容等等肤浅内容。模型在这种数据上训练之后之前存在的不良行为会被放大，新的不良行为会涌现出来（反向Scaling..）

如果现在能把存量训练数据的里面的bullshit全部严格剔除，可能模型能力已经再上一个档次了，所以模型公司已经在用AI尝试重写预训练的数据集（因为之前的bullshit实在太多了）。为了更好的训练数据，模型公司们现在愿意花150美元/小时来请各领域的专家和博士生们来标数据，在AI研究实现完全自动化前，这类需求会一直存在。现在的前沿模型当然不是只用类似Common Crawl这样的数据，会做很多数据增强，以及雇佣各种phd们和行业专家标注数据，现在细分程度已经非常高。以金融为例，现在头部公司的数据标注岗位会细分到银行、会计、保险、经济、传统买方/卖方、量化、相关法律合规等。每个岗位都是直接找领域从业人员，比如买方就是就是直接找在VC/PE/Hedge Fund的分析师来标数据，获得直接的产业经验

2）Context：现在Context Engneering火了，原因主要是应用形态从Chatbot开始转到到Agent后，模型需要消化更多样的输入输出（doc/file/tool call..），因此需要做一些形式和内容上的curation工作

2022年Meta发了一篇论文《General Intelligence Requires Rethinking Exploration》，里面有一句话非常认同，在今天依然非常核心：We are at the cusp of a transition from “learning from data” to “learning what data to learn from” as a central focus of artificial intelligence (AI) research. 显然，learning what data to learn from 是现在更核心的东西（可称之为模型自己的taste？）

从bitter lesson的角度，获得甄别能力、优良品味应该要模型自己学出来，现在其实在pre-train阶段模型已经在一定程度展现出了类似能力。Allen Zhu在Physics of LLM系列研究里有一个非常好的结论，LLM 在预训练时，通过在输入数据前添加领域标识符（如URL 前缀，例如 “http://wikipedia.org”），能够“自学”识别知识密集型、高质量信息来源。这不是显式编程，而是模型在学习过程中自然形成的偏好，模型会优先分配参数容量给可靠的“优质”数据源

把这个趋向落地到到Context Engneering，是希望curation的过程应该由AI自己学出来，而不是靠人手动定义来。短期可以靠人来做，但长期一定也会依靠AI。如果说我们需要super human data来构建super human model，那也可能需要super human context-engneering来解决真实世界的复杂问题（大概率不是自己手动盘一盘需要哪些文档和API这种原始操作），模型也一样不能“闭门造车”

比如，模型搜索时，如何选择看哪些信息？如果只是所有的网页看一遍作总结，只能得到平庸的结论，而且会有上下文污染的问题，看太多会让模型更抓不到关键。Chroma Research最近有一个很好的工作，指出了上下文污染（Context Rot）的问题，随着上下文增加，模型能力越来越不可靠，越容易被干扰，尤其对复杂语义的理解能力很差，这点其实和人也很像

短期解决方案就是屏蔽劣质信息源，给优质信息更多权重并定期调整。但长期看需要模型自己推演需要什么样的信息。最优秀的决策不是靠周围人的平均意见，而是结合最合适逻辑和自己的思考，优秀的人类是这样，优秀的AI模型亦然

10/ 真相（ground truth, aka 最高质量的训练数据）可能是AI时代最有价值的东西，因为决定未来的不是你在互联网上能看到的表面叙事，而是真相本身，是正在的发生的现实，是 Physical Reality。最终吸收最多ground truth的模型一定会赢，就像一个拥有健全常识的人胜过活在虚假叙事里的人一样，这并不是一句理想主义的空话，而是实际上影响智能程度的decisive factor

————  往期文章  ————

[除了成功预言GPT-5，过去半年全速前进还有哪些观点被验证？](https://mp.weixin.qq.com/s?__biz=MzI0NDk0MzI2NA==&mid=2247483988&idx=1&sn=d2b56a22fe3eddd3fb02edf6b90d9a16&scene=21#wechat_redirect)

[基础模型公司的硬伤，AI应用公司的机会](https://mp.weixin.qq.com/s?__biz=MzI0NDk0MzI2NA==&mid=2247483852&idx=1&sn=795da301de85874d8336eef0282f2c45&scene=21#wechat_redirect)

[Palantir：不仅是一家商业公司，更是AI/国防/MAGA的下一个十年](https://mp.weixin.qq.com/s?__biz=MzI0NDk0MzI2NA==&mid=2247483861&idx=1&sn=cfaa987c2e0355cc39eaf9f03e5bcd43&scene=21#wechat_redirect)

[从Palantir看为什么context可能比模型更重要](https://mp.weixin.qq.com/s?__biz=MzI0NDk0MzI2NA==&mid=2247483938&idx=1&sn=a7bc3e2656437c4e6d511be120af96e8&scene=21#wechat_redirect)

[OpenAI巅峰已过，并没有机会成为下一个Google](https://mp.weixin.qq.com/s?__biz=MzI0NDk0MzI2NA==&mid=2247483888&idx=1&sn=267c685381adaba91738d59585427ff5&scene=21#wechat_redirect)

[微信会捕获AGI的多少价值？](https://mp.weixin.qq.com/s?__biz=MzI0NDk0MzI2NA==&mid=2247483897&idx=1&sn=cd0826b87f89c4c3e1e3a15a64c3face&scene=21#wechat_redirect)

[AI时代请别聊护城河：从Cursor说起](https://mp.weixin.qq.com/s?__biz=MzI0NDk0MzI2NA==&mid=2247483905&idx=1&sn=00443904b66a5f49f36a265c969e7e08&scene=21#wechat_redirect)

[上亿美金挖人洒洒水啦，Meta高强度押注AI的关键逻辑有哪些](https://mp.weixin.qq.com/s?__biz=MzI0NDk0MzI2NA==&mid=2247483962&idx=1&sn=463bfb1b92836aa791a833bf21ea1361&scene=21#wechat_redirect)

——————————————————————

\[ 谢谢你看完，欢迎加群/交流 \]

——————————————————————

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/xFperdtcb7hRvEVlyaOxfFENicicOME2Vqc2icg8VWjSGsRib3hDb67GGLa5J7MiaEH4zG58wI2aib4NHmB4jF50VnZw/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

——————————————————————

# AI是未来唯一重要的事 

# Make AI content Great Again（MAGA！）

# AI \[ 研究 | 工程 | 产品 |  投资 | 商分 | 战略 | 解决方案 | 落地实施 | 市场营销 | 销售 | 深度使用者... \] 等等小伙伴欢迎交流，小红书同名

# 你觉得内容不错的话，欢迎关注/点赞/转发