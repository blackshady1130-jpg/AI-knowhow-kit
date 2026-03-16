---
url: https://mp.weixin.qq.com/s/dsBSpTZqg7QOFKFLB2uwNA
title: "LangChain 不好用的原因是，它起步于一场程序员的自嗨"
description: "ReByte 蔡建：LLM 时代，开发者能做的东西其实会非常有限。"
author: "油醋"
captured_at: "2026-03-08T11:06:19.709Z"
---

# LangChain 不好用的原因是，它起步于一场程序员的自嗨

![图片](https://mmbiz.qpic.cn/mmbiz_png/qpAK9iaV2O3vL5iaecClyfkwfCBoxqGe5z3FWycfjGBudWRfH7DMfWThic2AVvKmjaSBDibX5oA1af3IaFibAFWky3A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

当库克站在苹果总部大楼外围草坪的虚拟背景前开始展示全新的 15 pro 系列 iPhone，居住在波兰的产品设计师 Volodymyr 转头拿起手机。他发了一条推特：

**「我怀念乔布斯。」**

这场发布会所展现出的创新力不足，而此前库克在财报会中「生成式 AI 几乎嵌入到我们制造的每一个产品中」的描述也没有在新的 iPhone 身上找到任何明确的线索。乔布斯花了 2 亿美元收购来的 Siri 在当时非常惊艳，现在的定位愈发模糊。

苹果总部大楼外，生成式 AI 技术正在接近现实，苹果也在世界各地的办公室为人工智能领域的研发增加岗位。**但每当一种新技术即将呼之欲出，那位永远穿着黑色高领毛衣，精于创意与集成的产品大师总是引人怀念。**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/qpAK9iaV2O3uQ6GFNib2qiasXaBsw37hHC3CA3tL9UzvrI9g9pibAibFiasalhwP2DpT21sRdDdcjTcge3ibCgiaEMeYDA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

1979 年，杰夫·拉斯金带着乔布斯去位于加利福尼亚州帕洛阿尔托的研究中心 PARC 参观。PARC 是现代个人电脑几乎所有要素的诞生地，将在 15 年后创立亚马逊的杰夫·拉斯金那时是研究中心的一名计算机科学家。拉里·泰斯勒和丹·因格斯给他们演示了一种新的面向对象编程语言 SmallTalk。乔布斯不太喜欢系统看起来有锯齿感的滚动方式，并提议能否改成平滑连续的滚动方式，丹·因格斯想了想，在一分钟内完成了代码的改动，系统变成平滑连续的滚动方式，这让乔布斯和所有一起来的苹果员工大为震惊。

不知道这是否是 20 多年后 iPhone 滑动解锁屏幕的源头。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图源：《THE EARLY HISTORY OF SMALLTALK》

这个故事被记录在回溯文章《THE EARLY HISTORY OF SMALLTALK》里，SmallTalk 是一门古老的编程语言，或者说是一个可以被自由编辑的操作系统。SmallTalk 的思想是，即使是非程序员也能够将程序员开发出的应用或者组件加以修改或者组合起来，从而创造出符合自己需求的应用，另外任何人都可以直接修改 SmallTalk 系统的代码对整个系统进行自定义，系统的所有逻辑都是直接暴露给用户的。

就像丹·因格斯为乔布斯演示的那样。

那个滑块的想法是乔布斯某种超前的敏感性的一瞥，他用这种敏感攻击着旧时代，最终带来苹果至今多年的繁荣。但现在苹果的开发者人数已经超过 3400 万人。库克执掌下的苹果，姿态早已由攻转守，透出老成。**而最新鲜的一批人，心思也已经不只在 iOS 商店或者 Xcode 上了。**

随着 ChatGPT 的出现，大语言模型（LLM）开始作为一种具有现实意义的技术而被重视。

旧金山软件公司 Robust Intelligence 的一位前机器学习工程师 Chase Harrison 在 22 年 10 月底推出了 **LangChain** 。这是一个封装了大量 LLM 应用开发逻辑和工具集成的开源 Python 库，提供了一套工具、组件和接口，允许开发者链接提示词、模型和解析器，以使用底层模型创建更复杂的用例，简化创建由大型语言模型 (LLM) 和聊天模型提供支持的应用程序的过程。

LangChain 像是 SmallTalk 的惊艳故事在 40 多年后的一场回归，这样的开发框架被形容为「中间层」或「中间件」，正在成为当下 LLM 应用开发者手边最烫手的工具。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图源：Medium

5 月 ChatGPT Pulgin 推出，以及在 6 月进一步推出的 Chat Completions API 中提供函数调用的能力，OpenAI 想要包揽一切，LangChain 的前途开始蒙上阴影。但这并不代表它会作为一个短暂热潮退去。「在硅谷，通用大模型的竞争已经结束，现在所有人都在谈论开发 LLM 应用」，过去 3 年一直待在硅谷的蔡建说。

伟大的变革总是在浮出水面之前就已经定好商业层面上最主要的收益人（这很正常），正是微软、谷歌和英伟达给了这场大模型变革最充分的燃料。这条主线之外，敏锐的创业者则需要找到第二落点。比如曾经 iOS 上的开发者们，比如现在想要定义大模型软件开发的 Harrison 和 LangChain，或者觉得 LangChain 仍然不够锐利的蔡建和他的创业 ReByte。

## **01**

## **「中间件」还是「中间层」**

生成式 AI 的定义权暂时听命于 OpenAI，大模型语境下「中间件」概念第一次被广泛关注，也出自 OpenAI 的创始人山姆·奥特曼。

「我认为将会有一小部分的基本大模型，但对所有试图培训自己模型的创业公司持怀疑态度。将会发生的是，有一批新的创业公司采用已有的大模型，并对其进行调整，不仅仅是微调。中间层（Milldelayer）会变得非常重要。」去年秋季的一次 AI 讨论上，山姆·奥特曼分享了对于未来的预测。

这个「中间层」的概念很容易让人混淆，它让人联想到软件时代的「中间件（Middleware）」，而奥特曼用的词是「Middlelayer」。

「中间件包括了应用运行时、企业应用集成和各种云服务，可以帮助开发和运维人员更高效地构建和部署应用。数据管理、应用服务、消息传递、身份验证和应用编程接口（API）管理通常都要通过中间件来处理。但像 LangChain 所处的「中间层」并不是这个意思。

这是一个很少见的以所处位置的排除法来定义的概念。这么叫仅仅是因为它既不在模型层，又不算应用层，这个「中间层」概念在大模型涌现出智能之前，并没有合适的参照。

「所有在使用中间层这个定义的人，他们其实自己也不理解这个概念「，蔡建的理解是，这更接近一种「编排层」的概念。

## **02**

## **LangChain 不好用**

相比 LangChain，ReByte 是一个更新的项目。

蔡建此前在丰元资本做了三年，在那之前他将一个共享文档的创业项目「一起写」卖给了快手。今年年初他从丰元资本位于斯坦福大学对面的办公室走出来，联合机器学习出身，之前在字节飞书和微软工作过的 Nemo Yang，从自己的创业团队中捞了几个人，组成了 7 人的创业公司 Cortex，然后他们遇到了自己平台上的另一个项目——在 Github 上登顶过，拿到了 5100 多颗星的 RealChar ，RealChar 的开发者决定加入 Cortex，Cortex 也改名成了 ReByte，现在这支团队正在继续扩大。

从 LangChain、GPT-Index 再说到 RealChar，如果用「编排层」来做定义的话，这一类项目是大模型初期基础模型竞争的浪潮之后，将 LLM 与应用联系起来的具体步骤。

LangChain 是最先出现的，它和后来的 GPT-Index 的理念相似，一个程序员思维的创业者想要做一个面向程序员群体的开源项目。Chase Harrison 的想法天马行空，这也让 LangChain 自然成为一个非常极客的东西，有效而粗糙，拿到投资的同时，LangChain 也被很多人诟病有着太高的学习和测试成本，甚至不如自己依样画葫芦的重写一个。

ReByte 的字面意思是「重新定义写程序这件事情」，项目发起的原因也很简单，LangChain 不好用。

蔡建一开始想用 LangChain 做一个与餐饮平台 Yelp API 连接的订餐系统，但最终因为调用太麻烦，和太高的调用成本而放弃。

这件事从 LLM 到 LangChain 目前都不现实。一方面高并发状态下多次重复请求的情况严重，如果只依靠 LangChain 的话，为了得到一个 API 的响应需要发送差不多 30 个请求给 OpenAI ；另一方面，LLM 本质上是面向普通用户和自然语言的，没有特别为 API 调用而做的设计，生成的 API SPEC 过长，以 Token 数折算成花费将是一个天文数字。

「但这实际上不是 LLM 自己的问题」，蔡建说。

LLM 的理解和推理能力能够完成一个目标任务的拆分，比如把一个大的目标实现拆分成多个任务，然后在这些步骤中寻找优先级最高的任务，继续往下拆分，直到形成整个任务流程。

「理论上只要你给他个目标，他可以无限的循环，然后非常理想的情况，它一定可以把这事情做完。」

但这种忽视时间尺度的「理想化」本身缺乏现实意义。要解决实际问题的话，答案需要在一个相对明确的时间范围里给出，并且在安全性和成本上可控。

在 LLM 涌现出智能之前，所有的软件产品都需要软件工程师按照需求一行一行来写，而人们期待的人工智能，只需要你明确的描述出来你要做什么，它就可以帮你解决所有行业问题。

以现在的视角来看，之前的软件时代，与人们对未来 LLM 成熟形态的期待，在一场关于计算机的想象的两个极端。RealChar 则希望在这中间取得一个折中的位置。

这听起来近似于行业大模型的概念，这把能让 LLM 快速落地的万能钥匙引得几乎所有大模型公司趋之若鹜。但这中间也有一个实际的路线问题，到底是在应用层面加入行业数据，还是在模型训练层面加入行业数据？

蔡建更倾向前者，即大模型本身并不需要理解行业知识，需要行业知识的是应用。

「每个公司都在说我要做行业大模型，不是因为他懂大模型，而是因为他懂这个行业。」

最终来看，只有调用 LLM 的成本足够低，它才能变得实用。一种可能性是，如果有太多行业知识的杂质参与到模型训练中，每一个 Query（查询请求）都会浪费掉更多的计算。而知识如果从基础模型外部灌输进来可能是更灵活的方式。LLM 本身需要高度具备常识，即推理能力等抽象化的思维能力，但一个 HR 系统，一个医疗系统或者一份修车手册不该成为常识的一部分。

**于是 ReByte 不改造 LLM，而是要做一个连接 LLM 的低代码平台，以及一个灌入数据的接口。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图源：RealChar 官网

在 RealChar 的使用方式上，主要分为 Copilot 和 Callables（可调用）两类工具。前者可以直接进入使用，接入了 ChatGpt、Claude 的底层模型能力，也引入了即时搜索、文档概括的功能，甚至结合了 NBA 这样特殊的数据库做了对话产品。但 Copilot 更像是 RealChar 为了 Callables 做的展示。RealChar 为使用者提供了连接 LLM 的开发流程和工具，并且提供了数据库导入的途径。

美国 SaaS 市场相对完善，目前 RealChar 已经和 Notion 、Google Drive 、Slack 、Discord 等 SaaS 平台建立连接。企业数据通过 API 接口接入后，RealChar 对其进行向量化的处理，然后喂给做好的工具，生成自己的 Agent。

至于这个 Agent 是叫 Copilot 或是其他什么应用，只是表现方式的区别。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## **03**

## **技术降维和它的代价**

**所有用过 LangChain 的开发者都不会否认，这个框架透露出一些技术狂的自嗨，这无形中铸造了很高的技术门槛。**LLM 本质上却是一种技术降维，如果你有一个好的想法并且有清晰且有效的解决逻辑——比如乔布斯的天才想法碰上 SmallTalk——LLM 可以成为听凭吩咐的万能打手。

RealChar 与 LangChain 在出发点上的差异，可能是前者对这种技术降维更加乐观，或者说在当下具有更大的野心。

RealChar 最初的项目团队里，两个人在美国做业务拓展，国内有一支经验成熟的4人开发团队，另外的一位员工来自印度。这位印度员工非常年轻、有很强的编程能力，充满编程热忱。从招募进来到现在，他负责了团队里接近一半的代码产出，但蔡建从来没有见过他。

这个印度开发者是 RealChar 在 GitHub 上无意间看到的一个好项目的归属者，然后联系了他，很快团队里多了一位远程办公的新成员。这样具有精英级代码能力的开发者凤毛麟角，但随着 LLM 的出现，未来对开发者的定义或许可以完全抛开写代码这件事。

就像足够精确的 Prompt 可以在 Midjourney 上实现你所有想要的视觉效果一样，当 LLM 可以在写代码层面代替人类后，开发者的核心能力就变成了教会 LLM 以什么方式写代码，以及每一步所要达成的诉求是什么。这更像是一种前面提到的「编排」能力，而「编排」的高低，最终考验的东西也从代码能力转变为更本质的逻辑能力以及对某个场景的理解。

**在这两方面具有优势的人，在软件时代可能会被具体的代码难题卡住，但未来可依靠 LLM 写出一个完整的软件系统。**

他们会是新的应用开发者，微软 CEO 萨蒂亚·纳德拉对这个新的开发者群体的预测是 10 亿人。在此之前，互联网创业的逻辑无非是 ToB 或 ToC 之间的选择，但随着未来开发者的技术门槛降低，这两条路线未必是 LLM 创业的唯一准则。开发者群体本身会变成一个巨大市场。

ReByte 的走向是「To 开发者」。甚至未来所有「编排层」的工具都会为这个群体服务。

这样的变化也牵引着创业者的变化。李彦宏在文心一言发出时预先替所有创业泼了一盆「大模型创业没有机会」的冷水，但随着开发者门槛的下降，更加九死一生的应用层创业或许也只是大公司安抚人心的说辞一种。

## **04**

## **不是那个一呼百应的时代了**

我们在很多事情上都有相似的体验。比如一群人的抖音上火透了的「秀才」直到被封都从未进入过另一群人的信息流里；比如 Hugging Face 正在成为开源大模型的核心社区，但大模型这个词仍然让大部分人感到陌生。

人们对自己的喜好越来越明确，需求也越来越精细。如果在 10 多年之前那个 iPhone 引领的移动互联网形成时期（或者更早），好的创意可以不断做大，然后变成一家 Meta 、字节跳动这样的公司，现在这样的事越来越少了。

**「技术门槛降低，一个开发者能做的东西其实也同时会非常有限，它很小、很具体、非常个性化。」**

生成式 AI 如果真的能形成一股长久的技术浪潮，那围绕它创业的残酷时代背景，是一个好的创意更难变成一个创业公司，一个小的应用只能解决某一小撮人的问题，蔡建认为这是开发者门槛降低的代价。

「未来越来越多分散的开发者会出现，他们会在一些小的领域做一些更固定的事，凭借一些特别的数据或者行业 Knowhow，然后靠这个赚钱。这个时代已经不是一个一呼百应，找一群人来做大公司的时代了。」

所以有价值的事情就沉到了更基础的地方——谁能给他工具让他做这样的事情，而不是做应用这件事本身。

就像乔布斯在多年前所说的：It's more fun to be a pirate than to join the navy。

**「与其加入海军，不如成为海盗。」**

由 Founder Park、智谱 AI、Zilliz 联合主办的 AGI Playground Hackathon 将在 10 月 13日（周五）- 15日（周日）开始。37 个来自全球的 AGI 创新团队将聚集北京，用 48 小时开发令人眼前一亮的创新应用，登上路演舞台。

10 月 15 日（周日） 9:15 - 18:30，我们将在线上全程直播 Demo Day。点击预约，直击 AGI 黑客松 Demo Day，看 AGI 创新应用，为参赛队伍加油打气！

---

如果你关注大模型领域，欢迎扫码加入我们的大模型交流群，来一起探讨大模型时代的共识和认知，跟上大模型时代的这股浪潮。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/qpAK9iaV2O3uQ6GFNib2qiasXaBsw37hHC3CA3tL9UzvrI9g9pibAibFiasalhwP2DpT21sRdDdcjTcge3ibCgiaEMeYDA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

---

**更多阅读**

[融资超2亿美元，月之暗面发布超长文本模型产品，目标C端Super-App](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247491519&idx=1&sn=56ee163c4a8c56f5893f6b43235488af&chksm=c00af983f77d7095b45a2bd52beb8d9b94ba55ec8229a1be7908b58493beb17e669c57ca7feb&scene=21#wechat_redirect)

[Sam Altman 不建议 AI 创业者做套壳 ChatGPT](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247491519&idx=2&sn=9e60cdf5c5d12f3171f49122c2c13a45&chksm=c00af983f77d709544630731584d06b59e77dcccae18bfe9f85d50ba8f9840fca9965b49bc39&scene=21#wechat_redirect)

[殊途同归，所有人都想摆脱英伟达的垄断](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247491496&idx=1&sn=18d448aabfd4f0fb92f481218d50bbbd&chksm=c00af994f77d70822ee06713c041f74c2bf1150081b15e379f8301bd9b88160fb5d2edac7045&scene=21#wechat_redirect)

[国内顶流模型层和中间层，怎么看大模型落地应用？](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247490962&idx=1&sn=07a12aadf1d520e1acc835da712d36ec&chksm=c00afbaef77d72b87f9606e4fc35cb3e9d3f815b6744dff2b6cb6a020a5364ba6c3b831d6fd6&scene=21#wechat_redirect)

[微软最新166页测评报告：视觉模态GPT-4V到底有多强？](http://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247491479&idx=1&sn=0c432a8c88afa4ae67eaaf4b9a31dc01&chksm=c00af9abf77d70bd6c3ec01d2ae7e824aa91f0c783e4acc9717cf6c33d6f769fec2c92056e15&scene=21#wechat_redirect)

转载原创文章请添加微信：geekparker