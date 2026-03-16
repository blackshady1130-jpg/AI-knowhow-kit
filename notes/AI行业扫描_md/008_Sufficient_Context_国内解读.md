---
url: https://mp.weixin.qq.com/s/z3V73Pw0GnxWUkL7sX1rTw
title: "企业RAG系统为何失败：谷歌研究提出\"充足上下文\"解决方案"
description: "谷歌研究人员最新研究提出\\x26quot;充足上下文\\x26quot;框架，为理解和改进大语言模型（LLM）中的检索增强生成（RAG）系统提供了新视角。"
author: "徐磊LEANSOFT"
captured_at: "2026-03-09T03:05:26.457Z"
---

# 企业RAG系统为何失败：谷歌研究提出"充足上下文"解决方案

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibWgicrljcI9NkJcDMzvgz6PjCc691KiacAvKvO8k3d2pqxo5icNb83ccZ3GKicoqum88EYz9PdcPCGRoxmwMelV5nA/640?from=appmsg&wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/vnT4hbaLoX7CVwP3ChLicpEFMN4RzYLOyeBqEfA6xwxIVK2EGGuWQPXenZ3qzXFiaA3oo88ndlcrvPZg3MU5RjGg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

**点击“数字共生”**

 

**立即关注我们**

**本文使用 ClinePRO 自动翻译。**

**原文作者：****Ben Dickson**

**原文链接：**

https://venturebeat.com/ai/why-enterprise-rag-systems-fail-google-study-introduces-sufficient-context-solution/

谷歌研究人员最新研究提出"充足上下文"框架，为理解和改进大语言模型（LLMs）中的检索增强生成（RAG）系统提供了新视角。该方案能精准判定模型是否具备足够信息来准确响应查询，对于构建企业级应用至关重要-这类场景中系统的可靠性与事实准确性具有最高优先级。

**RAG系统的持续挑**

检索增强生成（RAG）系统已成为构建更可信、可验证AI应用的核心技术。然而这些系统仍存在显著缺陷：

-   可能在检索到证据的情况下仍自信地提供错误答案

-   容易被上下文中的无关信息干扰

-   或无法正确处理长文本片段中的答案提取

研究人员在论文中明确指出："理想情况是，当提供的上下文信息结合模型参数化知识足以回答问题，LLM应输出正确答案；反之则应拒绝回答或要求补充信息。"

要实现这一理想状态，需构建能自主判断上下文是否支持正确回答问题、并选择性使用信息的模型。先前研究尝试通过观察LLM在不同信息量下的表现来解决该问题，但谷歌团队在论文中强调："尽管（该研究的）目标似乎是理解大型语言模型（LLMs）在拥有或缺乏足够信息来回答查询时的行为表现，但先前的研究未能直接解决这一问题"。

**充足的上下文（Sufficient context）**

为解决上述题，研究人员引入了 “充足上下文” 的概念。输入实例会根据所提供的上下文是否包含回答查询的足够信息分为两种情况：

-   充足上下文：上下文中包含提供明确答案所需的所有必要信息。

-   不充足上下文：上下文缺乏必要信息。这可能是因为查询需要上下文中未涵盖的专业知识，或信息不完整、结论不明确或存在矛盾。

<table><tbody><tr><td colspan="2" data-colwidth="160,287"><section><span leaf=""><span textstyle="">问题：</span></span><span leaf=""><span textstyle="">Lya L.的配偶是谁？</span></span></section></td></tr><tr><td data-colwidth="160"><section><span data-pm-slice="0 0 []"><span leaf="">上下文类型</span></span></section></td><td data-colwidth="287"><section><span leaf="">上下文内容</span></section></td></tr><tr><td data-colwidth="160"><section><strong data-pm-slice="0 0 []"><span leaf="">充足上下文A</span></strong></section></td><td data-colwidth="287"><section><span data-pm-slice="0 0 []"><span leaf="">"Lya L.于2020年与Paul结婚...在最近的活动上他们看起来十分恩爱。"</span></span></section></td></tr><tr><td data-colwidth="160"><section><strong data-pm-slice="0 0 []"><span leaf="">充足上下文B</span></strong></section></td><td data-colwidth="287"><section><span data-pm-slice="0 0 []"><span leaf="">"Lya L. – 维基百科 出生：1980年10月1日 配偶：Paul（2020年结婚）"</span></span></section></td></tr><tr><td data-colwidth="160"><section><strong data-pm-slice="0 0 []"><span leaf="">不充足上下文C</span></strong></section></td><td data-colwidth="287"><section><span data-pm-slice="0 0 []"><span leaf="">"Lya L.曾于2006年与Tom结婚...2014年离婚...2018年与Paul约会..."（信息矛盾）</span></span></section></td></tr><tr><td data-colwidth="160"><section><strong data-pm-slice="0 0 []"><span leaf="">不充足上下文D</span></strong></section></td><td data-colwidth="287"><section><span data-pm-slice="0 0 []"><span leaf="">"Lya L.是宇航员，出生于俄亥俄州...育有两个孩子...父母是律师..."（缺乏配偶信息）</span></span></section></td></tr></tbody></table>

这种分类仅通过分析问题及相关上下文即可确定，无需依赖真实答案（ground-truth answer）。这一点对实际应用至关重要，因为在推理过程中通常难以获取真实答案。

研究人员开发了一种基于大语言模型（LLM）的 “自动评分器”（autorater），用于自动将实例标记为 “上下文充足” 或 “上下文不充足”。实验发现，谷歌的 Gemini 1.5 Pro 模型在单个示例（1-shot）的情况下，对上下文充足性的分类表现最佳，其上下文分类的F1分数与准确率均达到高水平。

正如论文强调："现实场景中评估模型性能时，我们无法预设候选答案。因此，仅凭查询内容和上下文就能运作的方法才具有实用价值。"

**RAG系统中大语言模型（LLM）行为的关键发现**

通过"充足上下文"框架对多模型和多数据集的分析，研究揭示了以下重要结论：

1.当上下文充足时，模型通常能获得更高准确率。然而即使上下文充足，模型产生幻觉的频率仍高于选择弃答。当上下文不足时，情况更为复杂，某些模型的弃答率会升高，而另一些模型的幻觉率反而增加。

2.值得注意的是，虽然RAG总体上能提升模型表现，但额外的上下文信息也可能降低模型在信息不足时选择弃答的能力。研究人员指出："这种现象可能源于模型在面对任何上下文信息时都会产生过度自信，从而导致更高的幻觉倾向而非弃答。"

3.一个特别有趣的发现是：即使在被判定为"上下文不足"的情况下，模型有时仍能给出正确答案。虽然通常认为这是因为模型已通过预训练（参数化知识）"掌握"了答案，但研究人员还发现了其他影响因素。例如，上下文可能帮助消除查询歧义，或弥补模型知识缺口，即使它并不包含完整答案。模型这种在有限外部信息下仍能成功的能力，对RAG系统设计具有更广泛的启示。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

谷歌资深研究员的补充观点

该研究合著者、谷歌资深研究科学家赛勒斯・拉什奇安（Cyrus Rashtchian）进一步强调了基础 LLM 质量的关键性：

1.企业级 RAG 系统的评估：对于真正优秀的企业级 RAG 系统，需在有检索和无检索的基准测试中分别评估模型表现。

2.检索的定位：检索应被视为对模型知识的 “增强”，而非唯一的事实来源。基础模型仍需承担以下职责：

-   填补信息空白

-   利用上下文线索（基于预训练知识）对检索内容进行合理推理

-   判断问题是否表述不明确或存在歧义，而非盲目复制上下文中的信息

**降低RAG系统中的幻觉现象**

研究发现，与无 RAG 的场景相比，配备 RAG 的模型更易出现 “生成幻觉而非主动拒绝回答” 的现象。为此，研究人员探索了缓解这一问题的技术。

他们开发了一种新的"选择性生成（selective generation）"框架。该方法使用一个独立的轻量级"干预模型（intervention model）"来决定主LLM应该生成答案还是选择弃答，从而在准确率和覆盖率（已回答问题的百分比）之间实现可控权衡。

该框架可与任何LLM结合使用，包括Gemini和GPT等专有模型。研究发现，在该框架中使用“充足上下文”作为额外信号，可以显著提高不同模型和数据集的回签准确率。这一方法使得Gemini、GPT和Gemma等模型在回答中的正确率提高了2%-10%。

为了从商业角度理解2%-10%的改进，Rashtchian举了一个客户服务AI的具体例子："想象一个客户询问是否能获得折扣，"他说，"在某些情况下，检索到的上下文是最新的，明确描述了正在进行的促销活动，因此模型可以自信地回答。但在其他情况下，上下文可能是'过时的'，描述的是几个月前的折扣，或者可能有特定的条款和条件。这时模型最好回答'我不确定'，或者说'您应该联系客服人员以获取针对您具体情况的更多信息'。"

研究团队还探索了通过微调模型来鼓励弃答行为。具体做法是在训练时，将那些上下文不足的实例中的答案替换为"我不知道"，而不是原始的标准答案。其原理是通过对这些示例的显式训练，可以引导模型选择弃答而非产生幻觉。

但结果好坏参半：经过微调的模型虽然通常有更高的正确答案率，但仍然频繁产生幻觉，且幻觉次数往往多于弃答次数。论文总结指出，虽然微调可能有所帮助，但"仍需更多工作来开发能够平衡这些目标的可靠策略"。

**将"充足上下文"应用于实际RAG系统**

对于希望将这些研究发现应用于自身RAG系统的企业团队（例如为内部知识库或客户支持AI提供支持的系统），Rashtchian提出了一个实用方法。他建议首先收集一批代表生产环境中会遇到的查询-上下文配对数据集，然后使用基于LLM的自动评估器（autorater）将每个示例标记为具有充足或不充足上下文。

"这已经能够很好地估算出充足上下文的比例，"Rashtchian表示，"如果比例低于80-90%，那么在检索或知识库方面可能还有很大改进空间，这是一个很好的可观察指标。"

Rashtchian建议团队接下来"根据充足上下文和不充足上下文的示例对模型响应进行分层分析"。通过分别检查这两类数据集上的指标，团队可以更好地理解性能差异。"例如，我们发现当给定不充足上下文时，模型更可能提供错误答案（相对于标准答案）。这是另一个可观察指标，"他指出，并补充说"在整个数据集上汇总统计可能会掩盖一小部分重要但处理不当的查询。"

虽然基于LLM的自动评估器展现出高准确率，但企业团队可能会担心额外的计算成本。Rashtchian澄清说，出于诊断目的，这种开销是可以控制的。

"我认为在小型测试集（比如500-1000个示例）上运行基于LLM的自动评估器应该相对便宜，而且可以'离线'完成，所以不用担心耗时问题，"他说。对于实时应用，他承认"最好使用启发式方法，或者至少使用更小的模型。"Rashtchian强调的关键点是"工程师应该关注比检索组件的相似度分数等更深入的指标。从LLM或启发式方法获得额外信号，能够带来新的洞察。"

**— END —**

**与数字智能体一同进化**

长按二维码关注“数字共生”

**这里有人人都能读懂的AI**

**微信号：szgs\_AI**

![二维码.jpeg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibWgicrljcI9NkJcDMzvgz6PjCc691KiacAu8B9Nc6ysVhkjlOiaib2OnF3bd47NEmicpicSJuGcAGpe42I2EhjWfUazA/640?from=appmsg&wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)