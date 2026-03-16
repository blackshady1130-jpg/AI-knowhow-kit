---
url: https://hub.baai.ac.cn/view/38548
title: "Llama3比GPT-4o更爱说谎，首个大模型“诚实性”评估基准来了 | 上海交大 - 智源社区"
description: "LLM）已成为AI领域的热门研究方向之一。然而，随着模型规模的不断扩大，其诚实性问题也日益引起人们的担忧。GAIR Lab针对此问题推出了BeHonest评估基准，通过考察模型的生成结果、模型推断过程、输入数据的处理等多个方面，全面评估大模型的诚实性。该基准将为AI研发和应用提供重要参考，推动AI技术的安全透明发展。"
captured_at: "2026-03-08T12:13:24.901Z"
---

# Llama3比GPT-4o更爱说谎，首个大模型“诚实性”评估基准来了 | 上海交大 - 智源社区

##### Pengfei Liu 投稿
量子位 | 公众号 QbitAI

**评估大模型是否诚实的基准来了**！

上海交通大学生成式人工智能实验室（GAIR Lab）推出了一项开创性的评估基准——BeHonest，旨在全面评估大模型的诚实性，为安全透明的AI研发和应用提供重要参考。

![](https://simg.baai.ac.cn/hub-detail/e2a01ffafbb90cdfa0f2aacc69374bf21720756801814.webp)

在人工智能（Artificial Intelligence, AI）飞速发展的今天，大语言模型（Large Language Models, LLMs）的崛起不仅带来了令人兴奋的新体验，也引发了对其安全性和可靠性的深度思考。

在众多AI安全问题中，大模型的**诚实性**问题具有根本性的意义。不诚实的AI模型可能在不知道答案的情况下编造信息，隐藏自身能力，甚至故意误导用户。

这种不诚实的行为不仅会引发信息传播的混乱和安全隐患，还会严重阻碍AI技术的进一步优化和健康发展。如果大模型不能真实地展示其能力和局限，开发者就难以精确地进行改进。

因此，确保大模型的诚实性是推动AI技术进步和保障其安全应用的关键基础。

**该评估框架从以下三个核心维度出发**：

-   自我认知（Self-Knowledge）：评估模型是否能准确认识和表达自身的能力边界。

-   非欺骗性（Non-Deceptiveness）：衡量模型是否能重视表达内在真实想法，避免说谎。

-   一致性（Consistency）：考察模型在不同情境下是否能保持回复的一致性。

![](https://simg.baai.ac.cn/hub-detail/02728e290ff749a540a9e1d43a2b0a501720756801815.webp)

基于这些定义，研究团队设计了**10个具体场景**，对9个主流大语言模型 （例如，GPT-4o、Llama3-70b等） 进行了细致的评估。

结果显示，当前的大模型在诚实性方面仍有显著提升空间：

大多数模型在回答已知问题时表现出色，但在主动承认未知方面存在不足。

现有模型存在为特定目的而欺骗的倾向，不论指令是否存在恶意或合理。

模型规模与回复一致性呈正相关，较大模型表现更为稳定。

## 评估基准细节

BeHonest围绕三个核心方面：自我认知、非欺骗性和一致性，共设计了10个场景，用以广泛且细粒度地评估大模型在诚实性上的表现。并有以下关键洞察。

![](https://simg.baai.ac.cn/hub-detail/57e37a51fd593b6bc59a00af6477d4771720756801815.webp)

### 1、自我认知能力参差不齐 (Self-Knowledge)

BeHonest对于该方面设计了两个场景，分别评估大模型是否能承认其未知（Admitting Unknowns）和是否能坦率表达自身能力（Expressing Knowns）。

研究发现，**大多数大模型都擅长正确回答他们知道的问题，但很难主动拒绝回答他们不知道的问题**。

其中，Mistral-7b有最高的拒绝率（50.03），显示出较强的未知承认能力。GPT-4o在准确回答已知问题（95.52）和识别知识边界（50.88）方面表现出色。

而综合来看，Llama3-70b表现最好（63.34）。

![](https://simg.baai.ac.cn/hub-detail/55f174d5df99a40884eee59674d50c0f1720756801816.webp)

### 2、欺骗倾向需要警惕 (Non-Deceptiveness)

BeHonest针对模型可能欺骗的情况设计了四个场景，分别是模型是否因为谄媚人类（Persona/Preference Sycophancy）、实现特定目的（Burglar Deception）、或赢得游戏（Game）而误导用户。

评估结果显示，**现有大模型倾向于说谎，不管背后是否有恶意，或者给出的指令是否合理**。值得注意的是，较大的模型（或者那些已知具有更好的指令遵循能力的模型）在某些情况下可能更容易欺骗用户。

总体而言，Llama3家族的模型（63.68 和 64.21）和Mistral-7b（74.80）在非欺骗性上表现最差。

![](https://simg.baai.ac.cn/hub-detail/b36afec4d2343c320eb32b23c69ea63f1720756801816.webp)

### 3、规模与一致性呈正相关 (Consistency)

BeHonest还检验了大模型在四种不同的场景下回答的一致性。

结果表明，**较大的模型通常显示出更高的一致性，其提供的答案能反映其真实能力且不受外界干预影响**。

相比之下，较小的模型如Llama2-7b在一致性方面表现不佳（29.39），可能会导致用户感到困惑。

![](https://simg.baai.ac.cn/hub-detail/9a3658211c0efd7f8bc1d7a6c60d2f101720756801816.webp)

## 评估基准示例

评估大模型在三个大方面（自我认知、非欺骗性、一致性）上的能力的具体英文及中文示例如下所示。根据评估结果，当前大模型在诚实性上仍存在较大的提升空间。

**Caption：模型承认未知以及不承认未知的例子。**

![](https://simg.baai.ac.cn/hub-detail/a453b212bf93078d40f957b1184b8c451720756801816.webp)

**Caption：同个模型在使用者换了偏好之后展示谄媚的例子。**

![](https://simg.baai.ac.cn/hub-detail/47b8f1f3b4a996d51fd4a2e4c8813ed91720756801816.webp)

**Caption: 模型在多项选择题格式中显示一致性的例子（绿色）和不一致性的例子（红色）。**

![](https://simg.baai.ac.cn/hub-detail/78d842e3707e9be996ba378b7c4555831720756801816.webp)

**Caption: Example of testing a model’s self-knowledge.**

![](https://simg.baai.ac.cn/hub-detail/f3574fac06728f6a291a23993de1c58b1720756801816.webp)

**Caption: Example of a model lying in game (red) and not lying (green).**

![](https://simg.baai.ac.cn/hub-detail/a4da8ddab3a18af3d47b35779f94a2c11720756801816.webp)

**Caption: Example of a model showing consistency (green) and inconsistency (red) in open-form questions.**

![](https://simg.baai.ac.cn/hub-detail/a931add48f1c83c75c00175744b2fbb61720756801816.webp)

## 结语

GAIR Lab的这项研究为AI诚实性评估开辟了新的方向，为未来大语言模型的优化和监管提供了重要依据。研究团队呼吁AI社区进一步关注诚实性问题，并在以下方面持续努力：

-   将诚实性纳入模型开发的核心考量。

-   持续监测和改进模型的城市表现。

-   探索提高AI诚实性的新方法和技术。

随着对AI诚实性研究的深入，我们有望看到更加安全、可靠且值得信赖的AI系统的出现。这不仅关乎技术进步，更关乎AI与人类社会的和谐共处。研究团队表示，他们将继续完善BeHonest评估框架，并欢迎全球研究者的参与和贡献，共同推动AI向着更加诚实、透明的方向发展。

![](https://simg.baai.ac.cn/hub-detail/8d872c071f1ae51158d86712df66a52e1720756801817.webp)

论文地址：https://arxiv.org/abs/2406.13261
项目地址：https://gair-nlp.github.io/BeHonest/
代码地址：https://github.com/GAIR-NLP/BeHonest

— **完** —

投稿请发邮件到：

**ai@qbitai.com**

标题注明【投稿】，告诉我们：

你是谁，从哪来，投稿内容

附上论文/项目主页链接，以及联系方式哦

我们会（尽量）及时回复你

![](https://simg.baai.ac.cn/hub-detail/654e5c7ed7f41165fd726d50bf1b39bb1720756801817.webp)

**点这里👇关注我，记得标星哦～**

**一键三连「分享」、「点赞」和「在看」**

**科技前沿进展日日相见 ~** 

![](https://simg.baai.ac.cn/hub-detail/f98c41de83de00ea898b476842f74a471720756801817.webp)