---
url: https://mp.weixin.qq.com/s/tN8lqjG32cj2L72po1wZCA
title: "Anthropic 挖掘 630 个 AI 新应用场景"
author: "锦秋基金"
captured_at: "2026-03-08T12:58:25.813Z"
---

# Anthropic 挖掘 630 个 AI 新应用场景

![图片](https://mmbiz.qpic.cn/mmbiz_png/SYm5F7no2Rv6v4NDI4odjv0gu02sWdeXgPPe6A0IRzAoVKK05huVHrHdsCpBD9uQqjDOdfOic3ibBXicRfr6qAhMA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**今天，Anthropic 发布了****Anthropic Economic Index**项目的第二份研究报告，深入分析了最新版模型 Claude 3.7 Sonnet 上线后的用户使用数据，并公开了一种全新的“自下而上”用户行为分类法，构建了一个包含 630 个细分类别的用途体系，更精准地捕捉 AI 在真实世界中五花八门的实际应用，相关的关键数据集均已开放下载。

基于对 Claude 3.7 Sonnet 应用数据的分析，报告揭示了以下几个核心发现：

1.  **应用领域拓展**：新模型发布后，在**编码、教育、科学**等知识密集型和技术驱动型领域的使用占比提升。

2.  **复杂任务处理受青睐**：新增的“**扩展思考**”模式受到技术研发人员（如计算机科学家、软件开发者）和创意设计人员（如多媒体艺术家、游戏设计师）的欢迎，他们正积极利用该功能处理更复杂、需要更深度思考的任务。

3.  **人机协作主流不变，**学习需求凸显：AI 仍主要扮演增强人类能力的“协作者”角色（占 57%），而非完全替代。但一个显著趋势是，用户将 AI 用于学习、获取知识和寻求解释的互动比例增长（从约 23% 升至 28%）。

4.  **应用模式因“岗”而异**：AI 的具体使用方式高度依赖于任务和职业属性。例如，翻译任务中自动化程度高，而文案写作/编辑、教育咨询等任务则更侧重人机协作与迭代。

5.  **长尾应用场景丰富**：新的分类法发掘出大量具体、细分的 AI 应用场景，从工程辅助（如水务管理）、技术咨询（如电池技术）到日常开发（如代码时区处理），展现了 AI 应用的广泛性与多样性。

本次报告推出了一套全新的自下而上（bottom-up）AI 使用分类体系，以弥补既有方法的不足。此前 Anthropic 的分析主要依赖 O\*NET 的任务和职业分类体系，这是一种自上而下（top-down）的预定义框架。

然而，由于大型通用模型能够胜任许多传统职业范畴之外的任务，仅依赖 O\*NET 可能遗漏一些实际存在的 AI 使用场景。

正如报告所指出的，如果仅根据预设的职业描述来推断 Claude 在做什么，难免出现偏差——例如 O\*NET 中有“美术家（画家、雕塑家等）”这样的职业，但 Claude 上的实际相关应用可能更多是数字艺术创作，而非雕塑。

为了解决这一问题，Anthropic 发布了一份首创的自下而上用户活动数据集。研究人员使用 Clio 在相同的 Claude.ai 对话数据上自动聚类出 630 个细粒度的用户任务类别，并将其组织成 3 级层次结构。

与 O\*NET 分类不同，这些类别直接源自用户实际提问和使用模式，每个类别都附有文字描述、出现频率等指标，以及该类别下 AI 增强/自动化使用比例的数据。由于新体系与原有 O\*NET 分类使用了同一批对话数据，研究者可以将自顶向下（O\*NET 映射）结果与自底向上（聚类）结果进行对比，从而发现前者可能遗漏的用例。

这套自下而上分类体系覆盖了极为广泛的应用场景，其类别细致到令人惊喜的程度——从“帮助解决家庭管道、水电等日常维修问题”到“提供电池技术和充电系统方面的专业指导”，包罗万象。对于正在寻找用户需求的创业者来说，这份数据集能提供不少借鉴。

数据集下载地址:

https://huggingface.co/datasets/Anthropic/EconomicIndex

对于想要完整地了解报告详细内容的读者，我们也对报告其他内容做了相应的编译：

## **01**

## **Claude 3.7 Sonnet 发布后，带来了哪些变化？**

上个月，我们推出了具备“扩展思考模式”的 Claude 3.7 Sonnet，这是我们迄今最强大的模型。在其发布后的 11 天里，我们收集了 100 万次匿名的 Claude.ai 免费版和 Pro 版用户对话数据，并据此重新进行了分析。

由于 Claude 3.7 Sonnet 是 Claude.ai 网站及移动端的默认模型，我们分析的数据绝大部分都来源于它。

需要说明的是，我们使用隐私保护分析工具 Clio，将每一次对话内容映射到美国劳工部 O\*NET 数据库中超过 17,000 个职业任务中的某一项。随后，我们分析这些任务所对应的职业及其高级别职业分类的总体使用模式。

对这 100 万次对话的分析显示，在编码、教育和科学等几个职业类别中，AI 的使用比例出现了小幅增长。Claude 3.7 Sonnet 在编码基准测试中表现更佳，因此编码使用量的增加符合预期。

而其他类别的增长，则可能反映了 AI 技术正在向经济各领域持续渗透，或是编码能力在这些领域催生了新的应用，亦或是模型自身在意料之外的能力上有所提升。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（图注）与我们最初的数据样本（两个月前）相比，编码、教育和科学领域的使用比例有所增加。该图展示了 Claude.ai 免费版和 Pro 版用户流量在 O\*NET 主要职业类别中的分布比例。灰色部分代表我们第一份报告的数据（涵盖 25 年 12 月至 25 年 1 月）。彩色条则显示了新数据（25 年 2 月至 25 年 3 月）中各类别使用比例的增减情况（绿色表示增加，蓝色表示减少）。请注意，图中显示的是相对比例，而非绝对使用量。各职业类别变化的完整图表请参见附录。

## **02**

## **用户如何使用“扩展思考”模式？**

Claude 3.7 Sonnet 引入了一种新的“扩展思考”模式。用户激活该模式后，模型会花费更长时间进行思考，以应对更复杂的问题。

我们的分析表明，“扩展思考”模式主要应用于技术攻关和创意性问题解决的场景。在与计算机及信息研究科学家相关的任务中，该模式的使用率最高，接近 10%；其次是软件开发者相关的任务，约为 8%。

此外，在多媒体艺术家（约 7%）和视频游戏设计师（约 6%）等数字创意类职业相关的任务中，该模式的使用也相当普遍。

尽管这些初步的使用模式揭示了用户倾向于在何时启用“扩展思考”模式，但关于这项新模型能力的许多重要问题仍有待探索。

为推动该领域的进一步研究，我们发布了一个新数据集，其中标注了每个 O\*NET 任务对应的“扩展思考”模式使用比例。该数据集已发布在Anthropic Hugging Face 页面。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（图注）哪些任务关联的“扩展思考”模式使用率最高？该图展示了在其相关任务中，“扩展思考”模式使用比例最高的 O\*NET 职业。图中仅包含在整体数据中占比至少达到 0.5% 的职业。

## **03**

## **AI 增强与自动化：不同任务和职业间有何差异？**

在上一份报告中，我们分析了 AI 的使用方式如何在“增强型应用”（如辅助学习、迭代优化输出内容）和“自动化应用”（如直接要求模型完成任务、调试代码）之间分布。

最新分析显示，增强与自动化的整体比例基本保持不变，增强型应用仍占约 57%。不过，具体的应用类型比例有所变化——例如，“学习型”互动（即用户向 Claude 咨询信息或寻求解释）的占比从约 23% 上升至约 28%。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（图注）在两次数据取样（V1 和 V2，相隔两个月）期间，增强与自动化的整体比例相对稳定，但“学习型”对话的占比显著增加。

我们通过研究人员意见征集渠道收到了大量请求，希望我们发布按任务和职业分类的自动化与增强使用数据。本报告响应了这些请求，并在我们的 Hugging Face 页面上公开了相关数据。

当按高级别职业类别分析数据时，我们发现某些类别的任务具有显著的“增强”特性。例如，在社区与社会服务类任务（涵盖教育、指导咨询等）中，增强型应用占比接近 75%。

而在另一个极端，如生产制造类、计算机与数学类职业相关的任务中，增强与自动化的比例则更接近各占一半 (50-50%)。目前尚未发现任何职业类别是以自动化应用为主导的。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（图注）不同互动模式在主要职业类别中的占比分布。图中仅包含在整体数据中占比至少达到 0.5% 的职业类别。

进一步细分来看，我们还可以考察特定职业内部及其相关任务的使用模式。例如，在文案撰稿人和编辑的相关任务中，“任务迭代”（用户与模型反复协作、修改文稿）的比例最高。

相比之下，笔译员和口译员的相关任务则表现出最高的“指令式行为”比例（模型用于翻译文档，人工参与极少）。

需要注意的是，O\*NET 的职业描述可能无法完全反映 Claude 的实际用途——例如，虽然数据显示“美术家（含画家、雕塑家、插画师）”存在使用情况，但 Claude 的应用场景可能更偏向于数字艺术创作，而非传统的绘画或雕塑。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（图注）各互动类型中使用比例最高的职业。图中针对五种互动类型（学习、任务迭代、验证、指令、反馈循环），分别列出了该类型互动占比最高的职业。例如，图书馆员的“学习型”互动比例最高（约 56%），而文案撰稿人的“任务迭代”比例最高（约 58%）。每个类别下还注明了该职业中最能体现此互动模式的 O*NET 任务（综合考虑了任务频率及该模式在任务中的使用频率）。其他几种互动模式的图表参见正文。请注意：O*NET 的职业描述可能无法完全反映 Claude.ai 的实际用途，例如，“美术家（含画家、雕塑家、插画师）”的使用可能更侧重数字艺术而非传统雕塑。图中仅包含在整体数据集中占比至少达到 0.5% 的职业。

## **04**

## **基于实际使用的 Claude.ai 用途分类体系 (自下而上构建)**

此前的研究主要依赖美国劳工部创建和维护的 O\**NET 任务与职业数据集。尽管 O\**NET 覆盖了大量任务，但它可能并非描述通用 AI 模型能力的最佳分类体系。因为这类模型常被用于执行 O\*NET 未包含的任务，这些实际用途可能因此在我们的分析中被忽略。

为弥补这一不足，我们发布了一个全新的、自下而上构建的数据集，用于描绘 Claude.ai 的用户活动模式。该数据集同样基于 Clio 工具和前述分析所用的匿名对话数据生成，因此便于研究者比较自上而下与自下而上两种分析方法的差异。

数据集包含 630 个细分的用途集群，每个集群都附有描述、使用频率指标、自动化/增强使用比例，并按三个层级进行了组织。

对该数据集的深入分析尚待未来进行，此处我们仅列举几个特别值得关注的用途集群：

-   协助处理水资源管理系统及基础设施项目相关事宜

-   创建具备交互式可视化功能的物理模拟

-   辅助进行字体选择、应用及问题排查

-   辅助创建或优化求职申请材料

-   提供电池技术和充电系统方面的指导

-   协助处理代码和数据库中的时区问题

随着 AI 模型的不断进步，我们衡量其经济影响的方法也需要与时俱进。在本期报告中，我们分析了 Claude 3.7 Sonnet 发布后的数据，发现其在编码、教育和科学领域的应用呈温和增长态势，而 AI 增强与自动化的整体比例保持稳定。我们还观察到，Claude 新增的“扩展思考”模式在技术领域和相关任务中最为常用，并识别出了不同任务和职业中自动化与增强使用的具体模式。支持这些分析的相关数据集已一并发布。

未来几个月，我们将继续追踪这些指标的变化，并随着模型能力的提升及其在经济各领域的广泛应用，开发新的衡量指标。

## **05**

## **附录**

本附录包含部分补充结果和技术细节。

**任务覆盖广度曲线**

我们还重新绘制了原始报告中的“任务使用深度”曲线图。总体而言，新曲线与首次分析的结果非常相似。略有不同的是，新模型的曲线下面积似乎略微减小，这可能与样本对话中编码相关内容占比增加有关。尽管过去两个月该曲线未出现显著变化，但随着模型能力和产品形态的不断发展，我们将持续关注其动态。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（图注）各职业的任务使用覆盖广度。例如，该图显示，约有 40% 的职业，其至少 20% 的任务已涉及 AI 应用 (x=0.2 时, y≈0.4)。两次报告的曲线对比变化不大。

**各职业类别使用比例的完整变化情况**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（图注）各职业类别使用比例变化。图中灰色条代表原始报告数据，彩色条显示第二份报告中相应比例的增减（黄色增加，蓝色减少）。其中，“计算机与数学”类职业的绝对增幅最大（+3%），而“教育”、“科学”等类别则呈现显著的相对百分比增长。

**其他互动模式的分析结果**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（图注）各互动类型中使用比例最高的职业。图中针对五种互动类型（学习、任务迭代、验证、指令、反馈循环），分别列出了该类型互动占比最高的职业。例如，图书馆员的“学习型”互动比例最高（约 56%），而文案撰稿人的“任务迭代”比例最高（约 58%）。每个类别下还注明了该职业中最能体现此互动模式的 O*NET 任务（综合考虑了任务频率及该模式在任务中的使用频率）。其他几种互动模式的图表参见正文。请注意：O*NET 的职业描述可能无法完全反映 Claude.ai 的实际用途，例如，“美术家（含画家、雕塑家、插画师）”的使用可能更侧重数字艺术而非传统雕塑。图中仅包含在整体数据集中占比至少达到 0.5% 的职业。

![图片](https://mmbiz.qpic.cn/mmbiz_png/SYm5F7no2Rvgj588LQFlic8OsEqn8Nvu7Lr1AGeFKoXmsIPsKFy6GlX0cJUuJOtZvnWXfZ8MiaSKTydrPoB5630Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12)

**锦秋基金“Soil种子专项计划”，专为早期AI创业者而设，致力于为拥有潜力的团队提供资金支持，帮助创业者将创新想法转化为实际应用，在AI领域破土而出，茁壮成长。**

**我们相信，一颗种子，只要给予合适的土壤和养分，就能长成参天大树。如果您正在寻找资金支持，欢迎将您的团队和项目介绍发送至 soil@jinqiucapital.com，让我们一起播种希望，收获未来！**

**点击下方图片链接，了解Soil种子专项计划更多详情。**