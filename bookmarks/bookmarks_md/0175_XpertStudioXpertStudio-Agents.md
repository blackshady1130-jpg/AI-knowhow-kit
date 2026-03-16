---
url: https://xpertiise.com/blog/why-we-build-xpert-studio
title: "我们为什么做Xpert Studio | Xpert Studio - 为大模型和Agents打造专家级数据"
description: "我们正处在一个由AI驱动的巨大变革时代，AI的价值正从\"在实验室解决难题、刷新排行榜\" 转向\"在实际经济活动中发挥真正价值\"。这一转变意味着AI需要能够理解并执行复杂的、现实世界的任务，深入到各行各业的日常工作中，而这需要克服当前AI在可靠性、长文本理解、能动性、多模态能力以及执行长期计划方面的不足。"
author: "汪涉洋"
published: "2025-05-12T16:00:00.000Z"
captured_at: "2026-03-08T10:48:23.569Z"
---

# 我们为什么做Xpert Studio | Xpert Studio - 为大模型和Agents打造专家级数据

## Situation of AI data labeling

正如那篇火爆全网的“[Second Half](https://ysymyth.github.io/The-Second-Half/)”，ai终将从“在实验室刷难题打榜”走向“在经济体中发挥真正价值”。

高质量的人类专家数据对大模型的基座模型、Agent能力提升越来越重要，这些数据在训练和评估AI模型/应用时都会发挥关键的作用。然而，获得高质量的专家数据依赖强大的标注交互接口和高质量的标注项目管理，这些都需要基于专精的标注平台软件来做，目前好的标注平台基本掌握在顶级科技大公司手里，要么私有化不对外，要么价格昂贵只有顶级ai公司用得起。

这波基于LLM的AI浪潮，如果要大面积产生经济价值**一定**要在社会方方面面落地，Agent应用需要深入渗透到经济当中，否则撑不起当前的资本投入。按目前趋势，从基座模型公司，到大量的创业者、大中小企业内的技术团队都会参与到这轮智能化的社会大改造。从LLM发展的技术范式看，LLM从pretrain+sft+rlhf的第一阶段范式，走到了以rlvr驱动reasoning能力的第二阶段范式。未来GPU的计算量有向RL倾斜的趋势，尤其是在更多垂直领域。[We only have one internet for pretrain](https://www.reddit.com/r/singularity/comments/1hdrjvq/ilyas_full_talk_at_neurips_2024_pretraining_as_we/) ，模型在垂类Agent场景要持续进步从而能持续放大产生的经济价值，需要大量的[proprietory domain expert data](https://scale.com/blog/hitl-ep3-agent-ready-data)，这些data可以用于evaluation，可以作为RL reward的输入，也可以作为RL的action space中的action+verifiable result。`Garbage in, garbage out, AI models are what they eat`，这些data的制作过程一定要追求高质量，同时保有高效率。上述这些问题，凸显了社会上缺乏好用、性价比高的标注平台这一技术矛盾。

看看AI的其他领域：

1.  在AI基座模型，有llama/deepseek等头部开源模型，也有[tulu](https://allenai.org/)等机构持续贡献。
2.  在AI应用开发领域，有langchain/dify等社区工具，为Agent开发不断进步添砖加瓦。
3.  但是在AI数据领域，缺乏好的工具能让人类专家数据的产出平权。github有一些开源工具，比如Label Studio是一个还不错的开源工具，但它提供的功能过于简单，难以适应大模型当今发展对高质量数据的要求。

以下是我们看到的一些问题：

**标注平台基础**

-   社会存在大量重复开发的低质量标注系统
-   开源工具缺乏基本可用的质检流程和团队管理
-   普遍缺乏标注过程质量指标

**标注项目运营**

-   很难高效的找到高质量的专家标注员
-   很难评估、培训这些新晋的标注员，缺乏系统支持
-   普遍缺乏先进的标注运营方法论通过平台化落地

**标注行业AI化程度低**

-   标注公司帮很多客户提供AI训练数据，用ai智能化改造别人的行业，但很少思考用AI如何改变标注行业
-   存量标注平台大多功能复杂/配置项多上手困难，用好平台高级功能也很难。
-   标注项目经理工作沟通繁重、协调压力巨大。

so，我们决定做`Xpert Studio`这个项目，**我们要让** **AI** **从人类专家反馈的数据中持续进步这件事平权，同时保证高质高效，我们还要用AI来改造标注行业本身**。

我们的mission是：**Produce high quality data for AGI, anytime/anywhere**.

---

## Here is our roadmap

## 平台基础能力

-   将最先进的团队管理、质检流程patch到label studio community，同时兼容community所有标注template。
-   更先进的质量体系
    -   标注过程指标 - 标注过程埋点（task\_complete\_time , controlc+controlv\_event\_check ）
    -   Ground Truth Answer准确率
    -   Inter-Annotator Agreement
-   AI辅助标注
    -   rlhf的机标人审
    -   copilot for text production tasks

## 标注template

-   构建支持复杂的前沿Agent标注任务
    -   Multi-Turn Agent eval
    -   Multi-Turn Agent trajectory interrupt构建正负例
-   构建template社区
    -   开源template tag自定义能力
    -   鼓励社区参与者分享好用的template，被用的越多就能获得更多免费使用SaaS额度

#### SaaS软件

-   上线n seat以下免费使用m个项目
-   Agent腾飞计划，提交融资TS、营业执照，n+k seat以下免费使用m+i个项目
-   AI学术促进计划，提交学术机构证据，n+k seat以下免费使用m+i个项目

#### 标注平台AI native化

-   平台引入browser-use，用户通过与【标注项目架构师Agent】对话来创建、配置项目（workflow advanced configuration）
-   开发【数据标注项目经理Agent】来辅助真人项目经理