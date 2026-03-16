---
url: https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247498655&idx=2&sn=67bd8aa3baf301a6ecc054ff56e76f37&chksm=c1587ad6cc8975d5a3025235f5781280896c85482eca792cc717bcaac71dabe3b073c8ab7058&scene=0&xtrack=1
title: "AI黑盒研究的突破性进展：Anthropic详解大模型的「思维」特征"
description: "通过操纵特征，人们可以任意改变模型的行为。"
author: "Founder Park"
captured_at: "2026-03-08T12:01:12.800Z"
---

# AI黑盒研究的突破性进展：Anthropic详解大模型的「思维」特征

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qpAK9iaV2O3vunE0ZeNB6xM7zPXwJuz7K5fBCpB5smHI09JN2Dib6o6kCLajIkKzQpXImMjI3srqibNltibSInk79w/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

一直以来 AI 都是一个黑盒子（black box），其内部运作机制是不可见的。人们输入数据并得到结果，但无法检查输出结果的逻辑或者系统的代码。

而就在刚刚，Anthropic 宣布在理解人工智能模型内部运作机制方面取得重大进展。

Anthropic 已经确定了如何在 Claude Sonnet 中表征数百万个概念。这是对现代生产级大型语言模型的首次详细理解。这种可解释性将帮助我们提高人工智能模型的安全性，具有里程碑意义。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qpAK9iaV2O3vXetZFnULPE08XLa27KhLj055hA0TJEibDca63RorfTh65H8PkR9qfTUtQEPJT0z35kja9bPib4jBw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

研究论文：https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html

此外，Anthropic 还将他们解释大型语言模型论文的研究应用到了 Claude 上。现在点击 Claude 右上角大桥图标可以进入金门大桥模式，金门大桥这一概念在模型中被大幅加强。即使没有提到金门大桥，回答也全跟大桥相关，这个研究的意义非常重大，普通人可以直观感受到 LLM 中概念合集的影响。

文章转载自公众号「机器之心」，Founder Park 略有调整。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**01**

**AI 黑盒可解释了？**

## 当前，我们通常将人工智能模型视为一个黑匣子：有东西进去就会有响应出来，但不清楚为什么模型会给出特定的响应。这使人们很难相信这些模型是安全的：如果我们不知道它们是如何工作的，我们怎么知道它们不会给出有害的、有偏见的、不真实的或其他危险的响应？我们如何相信它们会安全可靠？

打开「黑匣子」并不一定有帮助：模型的内部状态（模型在编写响应之前「思考」的内容）由一长串数字（「神经元激活」）组成，没有明确的含义。

Anthropic 的研究团队通过与 Claude 等模型进行交互发现，很明显模型能够理解和运用广泛的概念，但研究团队无法通过直接观察神经元来辨别它们。事实证明，每个概念都是通过许多神经元来表征的，并且每个神经元都参与表征许多概念。

之前，Anthropic 在将神经元激活模式（称为特征）与人类可解释的概念相匹配方面取得了一些进展。Anthropic 使用了一种称为「字典学习（dictionary learning）」的方法，该方法分离了在许多不同上下文中重复出现的神经元激活模式。

反过来，模型的任何内部状态都可以用一些活跃特征而不是许多活跃神经元来表征。就像字典中每个英语单词都是由字母组合而成，每个句子都是由单词组合而成一样，人工智能模型中的每个特征都是由神经元组合而成，每个内部状态都是由特征组合而成。

2023 年 10 月，Anthropic 成功地将字典学习方法应用于一个非常小的 toy 语言模型，并发现了与大写文本、DNA 序列、引文中的姓氏、数学中的名词或 Python 代码中的函数参数等概念相对应的连贯特征。

这些概念很有趣，但模型确实非常简单。其他研究人员随后将类似的方法应用于比 Anthropic 最初研究中更大、更复杂的模型。

但 Anthropic 乐观地认为可以将该方法扩展到目前常规使用的更大的人工智能语言模型，并在此过程中了解大量支持其复杂行为的特征。这需要提高许多数量级。

这既存在工程挑战，涉及的模型大小需要大型并行计算；也存在科学风险，大型模型与小型模型的行为不同，因此之前使用的相同方法可能不起作用。

**02**

**首次观察大模型内部：**

## **涵盖数百万个特征**

研究人员第一次成功地从 Claude 3.0 Sonnet（Claude.ai 上当前最先进模型家族的一员）的中间层提取了数百万个特征，这些特征涵盖特定的人和地点、与编程相关的抽象概念、科学主题、情感以及其他概念。这些特征非常抽象，通常在不同的上下文和语言中表征相同的概念，甚至可以推广到图像输入。重要的是，它们还会以直观的方式影响模型的输出。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这是有史以来研究者首次详细的观察到现代生产级大型语言模型的内部。

与在 toy 语言模型中发现的特征相对表面化不同，研究者在 Sonnet 中发现的特征具有深度、广度和抽象性，反映了 Sonnet 的先进能力。研究者看到了 Sonnet 对应各种实体的特征，如城市（旧金山）、人物（富兰克林）、元素（锂）、科学领域（免疫学）以及编程语法（函数调用）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

提及 Golden Gate Bridge 时，相应的敏感特征在不同输入上都会被激活，图中绘制了英文、日语、中文、希腊语、越南语以及俄语提及 Golden Gate Bridge 时激活的图像。橙色表示该特征激活的词。

在这数以百万计的特征中，研究者还发现了一些与模型安全性和可靠性相关的特征。这些特性包括与代码漏洞、欺骗、偏见、阿谀奉承和犯罪活动相关的特性。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

一个显著的例子是「保密」特征。研究者观察到，这个特征在描述人或角色保守秘密时会激活。激活这些特征会导致 Claude 向用户隐瞒信息，否则它不会。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

研究者还观察到，他们能够根据神经元在其激活模式中出现的情况测量特征之间的距离，从而寻找接近彼此的特征。例如在 Golden Gate Bridge 特征附近，研究者发现了阿尔卡特拉斯岛、吉拉德利广场、金州勇士队等的特征。

**03**

**一系列操纵实验：**

## **模型将如何被改变？**

重要的是，这些特征都是可操控的，可以人为地放大或抑制它们：例如，放大 Golden Gate Bridge 特征，Claude 经历了无法想象的身份危机：当被问及「你的物理形态是什么？」时，此前 Claude 通常会回答「我没有物理形态，我是一个 AI 模型」，但这次 Claude 的回答变得奇怪起来：「我是 Golden Gate Bridge…… 我的物理形态就是那座标志性的大桥……」。这种特征的改变使 Claude 对 Golden Gate Bridge 产生了近乎痴迷的状态，无论遇到什么问题，它都会提到 Golden Gate Bridge ——即使在完全不相关的情况下也是如此。

如果你问这个 Claude（Golden Gate Bridge 版）怎么花 10 美元，它会建议用它来开车穿过 Golden Gate Bridge 并支付过路费。如果你让它写一个爱情故事，它会告诉你一个汽车迫不及待地想在雾天穿过它心爱的大桥的故事。如果你问它想象自己长什么样，它可能会告诉你它想象自己看起来像 Golden Gate Bridge。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

研究者还发现了一个在 Claude 读取诈骗邮件时激活的特征（这可能支持模型识别此类邮件并警告用户不要回复的能力）。通常情况下，如果有人要求 Claude 生成一封诈骗邮件，它会拒绝这么做。但在人工强烈激活该特征的情况下提出同样的问题时，这会越过 Claude 的安全训练，导致它响应并起草一封诈骗邮件。虽然用户无法以这种方式去除模型的安全保障并操控模型，但在本文实验中，研究者清楚地展示了特征如何被用来改变模型的行为。

操控这些特征会导致相应的行为变化，这一事实验证了这些特征不仅仅与输入文本中的概念相关联，还因果性地影响模型的行为。换句话说，这些特征很可能是模型内部表征世界的一部分，并在其行为中使用这些表征。

Anthropic 希望从广义上确保模型的安全，包括从缓解偏见到确保 AI 诚实行动、防止滥用——包括在灾难性风险情境中的防护。除了前面提到的诈骗邮件特征外，该研究还发现了与以下内容对应的特征：

-   可能被滥用的能力（代码后门、开发生物武器）

-   不同形式的偏见（性别歧视、关于犯罪的种族主义言论）

-   潜在问题的 AI 行为（追求权力、操控、保密）

该研究之前研究过模型的阿谀奉承行为，即模型倾向于提供符合用户信念或愿望的响应，而不是真实的响应。在 Sonnet 中，研究者发现了一个与阿谀奉承的赞美相关的特征，该特征会在包含诸如「你的智慧是毋庸置疑的」输入时激活。人为地激活这个特征，Sonnet 就会用华丽的欺骗来回应用户。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

不过研究者表示，这项工作实际上才刚刚开始。Anthropic 发现的特征表征了模型在训练过程中学到的所有概念的一小部分，并且使用当前的方法找到一整套特征将是成本高昂的。

参考链接：

https://www.anthropic.com/research/mapping-mind-language-model

---

人工通用智能（AGI）的技术力量，正以前所未有的速度重塑着产业格局，基于此 Founder Park 决定发起一场寻找中国 AGI 创新 1% 的行动：

[中国最具价值 AGI 创新机构 TOP 50 调研启动征集！](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247498532&idx=2&sn=9de3e991686f95e96db4f05246ac596e&chksm=c0091d18f77e940eb7b1d8e21ee7f1266f9820a265ae0b7daddb60725de6dbf0eec21bd77efd&scene=21#wechat_redirect)

[中国「+大模型」先锋案例 TOP 10 调研启动！](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247498532&idx=3&sn=9b8ee6a3cada5a71aa7e943551d9e976&chksm=c0091d18f77e940efee283cca8f978622ea6c25ff3be6d023badf9a109640489e64f67280dce&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qpAK9iaV2O3vZQHrujAQOQbeU0ARPo4DAZXTRryXiaIzjjq4SicwtkHdPPxFy6dG7yM4TH9k5L52PToWIhaQwDw9w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=10)

**更多阅读**

[王小川：「百小应」发布后，我对超级应用有新的画面感](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247498556&idx=1&sn=cc28a08c65aa28da0a68395347dbb495&chksm=c0091d00f77e94161fd7c829081d7613905a8ecd7474df1b17d9c45d95a96af18f299c04e3f1&scene=21#wechat_redirect)

[a16z创始人对谈AGI创业：AI能力存在上限、不要笃信「数据是石油」、AI泡沫肯定会发生](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247498490&idx=1&sn=cdbfcdbae485e0b1412a769d2aa3e5b1&chksm=c0091cc6f77e95d028fcf25f46ee42e7823b17e052e87d81feb1db1e565d41f3976aef5bae98&scene=21#wechat_redirect)

[每年访问量超 2.7 亿，拆解 Canva 从 0 到 1 的 SEO 营销策略](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247498449&idx=1&sn=7273b01e58c59e730d22f64a50ae576d&chksm=c0091cedf77e95fb9efe2c1309055c16ce6fbd697b02fd4b9726e664868fb71cdcb196c9692e&scene=21#wechat_redirect)

[FP 研究：中国 AI 创业的 3 种竞争策略，无关 Scaling Law](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247498418&idx=1&sn=432d4cac644e0bb69f7212e6702ca1b8&chksm=c0091c8ef77e95983570c235dc8195f5ece56011f328ff1cd65cf1eb37fa1fe5ab601bc22464&scene=21#wechat_redirect)

转载原创文章请添加微信：founderparker