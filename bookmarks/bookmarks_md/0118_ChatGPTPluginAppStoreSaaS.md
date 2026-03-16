---
url: https://mp.weixin.qq.com/s/cL6CMG1J9HqMgGyq-Fm6FQ
title: "ChatGPT Plugin：被高估的“App Store时刻”，软件和SaaS生态的重组开端"
description: "ChatGPT plugin未来会带来什么增量机会？"
author: "拾象"
captured_at: "2026-03-08T10:33:32.218Z"
---

# ChatGPT Plugin：被高估的“App Store时刻”，软件和SaaS生态的重组开端

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/3tHNibnJ2jgw0Diay9MT5bbFgOFzTBkLicyKhuQw3gaubfhYKPHTibAdrDKBbfKibtZzBggyGv6byJ8cpicvFs6TavKg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgw0Diay9MT5bbFgOFzTBkLicyXFMeISU4N671uRice4G2A4B6snwCzOmSn76BkLhdDuWORjhCicCYkibmg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgw0Diay9MT5bbFgOFzTBkLicyOrbZ1pwauvrKOP1rZ2PlR6uhBxBvw6yx4eQ6icMExpKkGQIArlibqfYQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

作者：Cage、程天一

编辑：penny

排版：Mengxi

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgw0Diay9MT5bbFgOFzTBkLicyPq1kCJmKLqYkkAKVVzQBD3welykPTIeu9WKEVQFczSvgnPnuiaSDVnQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

“OpenAI 的 App Store 时刻”，这是 3 个月前 ChatGPT plugin 刚刚推出时市场的反应。过去 3 个月里，OpenAI 采取了一种相当保守的方式为这个生态放量，通过审核的 plugin 数量只有不到 300 个，至今使用 plugin 的用户量级也只有数十万量级。

一方面这是 OpenAI 有意为之的结果。用 OpenAI 总裁 Greg Brockman 的话来说，ChatGPT plugins 开放成本非常低 —— 基本上就是 API 的文档，只不过是用来给语言模型读。另一方面这也暴露出 OpenAI 并不是全能的，它对于如何培育一个安全、蓬勃发展又能快速上量的开放平台和应用生态并没有过多的经验。Sam Altman 甚至承认 ChatGPT plugin 还没有迎来 Product-Market-Fit。

尽管没有想象中摧枯拉朽，plugin 仍然是 ChatGPT 这个产品的一个里程碑，让 OpenAI 迈出了“开放”的又一步。我们在本文探讨了围绕 plugin 的炒作褪去后一些真正长期重要的问题：

• 究竟是哪些公司和开发者在积极接入 plugin?

• plugin 如何同时确保安全、性能和整个系统的稳定性?

• 观察一个开放平台之上的应用生态的思考框架是什么?

• plugin 带来的新机会有哪些？

……

在这些问题之外，短期最值得期待的是在 plugin 标准互通的情况下，微软能把这个生态玩出来什么花样：

OpenAI 缺审核，缺产品经理，缺运营这个生态的专家，缺更好的、比聊天界面搭配小组件更广泛的 UI。这些微软都有 —— 大量可以投入的人员，广泛可供 plugin 嵌入并发挥作用的一系列产品（消费者端的 Bing Chat 和 Windows 11 Copilot，企业端的 Microsoft 365 Copilot 和 Dynamis 365 Copilot 等）。

**以下为本文目录，****建议结合要点进行针对性阅读。**

**👇**

01 背景

02 Plugin 的现有合作和未来影响

03 Plugin 的开发方式和能力边界

04 Plugin 的 App Store 野望

05 Plugin 干掉 LangChain？

06 Plugin 的路线图与连锁反应

**01.**

**背景**

OpenAI 在 23 年 3 月 23 日发布了 ChatGPT plugin。尽管官方强调这一举动是为了更好研究 ChatGPT 在现实世界中的使用情况从而解决安全问题，外界对它在 OpenAI 生态打造、商业层面的潜力寄予了厚望，中英文社区一度认为这是 OpenAI 的“App Store 时刻”，并且直接“干掉了 LangChain 和 Fixie”。

4 月的开发者群体和 ChatGPT 用户仍然延续着对这个生态的向往，除了官方合作伙伴外，大量的第三方 plugin 开始基于 OpenAI 定义的这套框架和标准被开发，用户则疯狂涌向 waitlist 并且在 Twitter 上成为 Code Interpreter 等明星 plugin 的自来水。

最密集的变化发生在 5 月，OpenAI 终于开始更大范围放量，并且在 5 月下旬宣布向 Plus 订阅用户全量开放，提供 70 多个第三方 plugins。不过这种全量开放的策略仍然十分克制，Plus 用户必须打开 Beta features 的开关，iOS app 也默认不显示 Plugin，用户得在旧会话中找到自己使用过的 Plugin。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*在移动端使用 Plugin*

*Source: Pietre Schiano*

于此并行的是微软在 Build 大会上宣布采用 OpenAI 的 plugin 标准，将允许开发者构建跨 OpenAI（ChatGPT）和微软（Bing Chat、各产品线 Copilot）生态的 plugin，通过 ChatGPT plugin、Teams message extensions 和 Power Platform connectors 布局了个很全面的插件框架。鉴于 OpenAI 的研究属性，微软反而更有可能把 plugin 生态发扬光大。

在大规模放量之后，ChatGPT 在双边面临的现实是 **plugin 仍然是一个相当早期的生态：**

• 鉴于整个 plugin 的用户数量还只有几十万量级，Plugin 的官方合作伙伴们可能短时间内无法获得特别大的新增流量；ChatGPT 目前的 UI 本身也有很多限制；Airbnb 则觉得这种聊天框配合底部小组件的 UI 并不真的适合旅行产品，在其 plugin 上线前终止了这一项目；

• 个人开发者们如果有现成的 api 可用，可以在几十分钟内按照 OpenAI 的标准提交 api doc 等文件，但是满足 UI 和数据隐私规范并通过审核往往要等待一段时间并且充满不确定性；

• 用户们则发现大多数 plugin 都比 Demo 显示地要更加粗糙，很难在 ChatGPT 内部拥有统一的产品体验；多数的讨论集中在 Code Interpreter 和 Web Browsing，并且 Web Browsing 的探索过程也经常令人抓狂。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*ChatGPT 的频繁“试错”*

*Source: Reddit*

**我们觉得是时候将 OpenAI 当做一个地球物种** —— 它拥有世界顶级的 AI 研究员们，但是他们很难神奇地、天然地解决产品、双边生态构建的节奏等必然存在的挑战 ——**更加贴近现实地想象 plugin 的现状、生态潜力和演进可能性，这也是本文探讨的重点问题。**

**02.**

**Plugin 的现有合作和未来影响**

**ChatGPT plugin 生态一度激发了大家对 ChatGPT 这个历史上用户增长曲线最陡峭产品的想象力。**2 个月以来，plugin 也有不少功能的更新、新插件的引入和使用规模的放开。在这里总结下当下 plugin 拥有的一些能力，看看最近的更新是否符合预期。

截止 23 年 5 月底，ChatGPT 插件商店中提供了 85 个插件，其按照能力大致可以分为 6 类：

**1\. 外部交互：****这类插件提供了与外部的网页和产品进行交互的能力。**

其中 Browsing 是 OpenAI 官方推出的插件，思路与其在 21 年底的论文 *WebGPT* 一脉相承：使用语言模型去探索和理解外部网络上的内容。在多个用户访谈中提到，**如果有明确目标的情况下，其浏览和总结能力比 New Bing 来得更好，但弊端是稳定性相对差些。**

而外部工具中最好用的是 Zapier，[**Z****apier 作为聚合器中的领先者，**](http://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247486373&idx=1&sn=e85632ccbbed9c58c9591f423ab997c8&chksm=ce98b43bf9ef3d2d58e8eff801055457131fb92a79a528de4cef9828a246250fb4c4f7b78dba&scene=21#wechat_redirect)本身的能力是和外部 5000 余个应用的 api 去做交互，有了很完备的 api 交互逻辑。而由于 input context 的限制（容纳不下数十上百个 api 的 prompt 说明文档）和 OpenAI 在产品工程侧重心的差异，短期之内 Plugin 生态的聚合能力是比较薄弱的一项。因此 Zapier 在中短期是受益于 ChatGPT 这个大脑的文本理解能力的。

**2\. 编程开发：****提供开发环境，或编程开发的生产力工具。**

受到最多关注的是 OpenAI 官方开发的 Code Interpreter。它提供了一个开发的沙盒环境，在环境中可以对用户想要执行的代码和分析的数据进行各类实验。OpenAI 在 Python 安全方面做了很多工作，来确保在这个环境中执行的代码实验会被安全地隔离在环境中，不直接地对外部网络环境造成改变和影响。由于这一特性，大家对 Code Interpreter 的使用就集中在 Python 另一个不需要部署上线的特长上——数据分析。Code Interpreter 能对数据做总结和加工，并根据指令产出言之有物的数据可视化，这一点隐隐有着超越传统 BI 的希望，只是在可控性上还需继续加强。

**3\. 个性化交互：为 ChatGPT 带来记忆和个性化的能力。**

**之前在 Pinecone 的研究中提到过，Retrieval 插件被 Greg 认为是所有插件中最独特的，**因为它补足了 ChatGPT 原本没有的从个性化记忆和专有数据中做 Retrieval Augmentation 的能力。插件的结构很简单，从各类 vector DB 的 api 中取出与 prompt 语义接近的内容交给 ChatGPT 进行理解和学习。[**此外，DAN 也是这类中一个比较有趣的插件，其提供了为 ChatGPT 改变个性的能力。**](http://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247500603&idx=1&sn=69f13f23ebbf896f307e0c40635ee1d8&chksm=ce9b7ca5f9ecf5b3f666af5d237aceb034bd5aee94a3c5c6de63f0296fd341b41bb0b01e4f1e&scene=21#wechat_redirect)

**4\. 生活助手：衣食住行的信息整合。**

这一品类是大公司涌入最多的，如 Expedia、Kayak 是旅行机酒预定，OpenTable 是预约餐厅，Instacart 是购买生鲜的领先平台。这类产品希望通过 ChatGPT 对自然语言的理解能力，抓住这个新平台作为增量流量入口。一方面，ChatGPT 将这一功能全量的进度相对比较克制和保守，并没有发挥比较明显的引流作用；但另一方面，Chat 这一交互形式筛选下来的用户质量是比传统获客渠道来得更高的。

**5\. 垂直领域：获得专有数据的窗口。**

有许多垂直领域高质量的数据并不是 ChatGPT 核心的技能点，因此垂直领域的插件能为其带来更专业、专有的内容。例如 Vogue 有时尚领域的数据，Crypto Prices 有 web3 领域的公开数据，UN 有联合国每年政策变化的相关文本。这些都是在垂直领域做理解和生成时重要的信息。

**6\. 办公效率：生产力工具。**

这类插件大多是办公效率小工具的集合，例如 PDF 阅读总结、待办事项记录、发邮件、文字转语音是目前主要的插件能力。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

以上介绍了当前 Plugin 的具体能力，会发现其在很多领域对不同垂直领域有所影响，**有些可能会对大公司的现有产品形态造成一定冲击，****有些则是独立开发者积累早期高质量用户的好机会。**接下来就分别对这些领域的影响进行梳理。

**1.** **搜索**

案例：Google, Bing, Perplexity

• 使用频次：★★★★★

• 短期影响：★★★★ (short)

• 长期影响：★★★ (short)

ChatGPT 集成了 browsing 功能在短期之内会对搜索引擎的能力有一定的冲击。因为 LLM 很大程度上就是将互联网上的公开信息学习了一遍，结合了 browsing 能力后，本身又继承了一定的内容整合和推理能力，因此使用 ChatGPT 的用户在短期会显著减少使用搜索的频率。

但谷歌的反应也是比较迅速的，已经在内部开放了集成 LLM 的搜索引擎。以谷歌的 infra 实力和对搜索引擎的深入理解，完全有可能能在 Google 搜索引擎中做出比 New Bing 和 ChatGPT 更好的 AI 搜索引擎。但无论是哪个公司获胜，**大家对搜索的认知在长期一定会被 LLM 部分颠覆，**传统的索引排序式的 query 心智会渐渐被生成式的 prompt 心智侵蚀。

**2\. 聚合器**

案例：Zapier

• 使用频次：★★★

• 短期影响：★★★★ (long)

• 长期影响：★★★★ (short)

LLM 时代的跨应用调度和交互需求会显著增长，因此尽管目前聚合器的使用频率相对低频，我们还是给到了中等频次的评价。

当前 ChatGPT 有了很强的工具使用能力，但缺少在 api 聚合方面的 know-how，因此 Plugin 的出现在中短期之内利好 Zapier 这类聚合器产品。Zapier 在此领域积累很深，现在如果大家想在 ChatGPT 上做一些复杂操作的时候：比如将文本总结之后发社交媒体，或是记录在 Google Workspace 中，大家都会选择用 ChatGPT + Zapier 的方式来实现。在很多 use case 中，ChatGPT 只需要接入聚合器，就能做到非常好的用户体验，它也不需要接入大量 api，相当于类似 SEO 的部分由聚合器完全提供了。

但长期上，这类产品面临以下冲击：一方面， api 的组织形式可能会发生变化，LLM 时代可能跨产品交互的频次和。OpenAI 最近发布了函数调用能力，使 api 的可用性显著提升，这些变化可能会弱化 Zapier 的护城河。另一方面，聚合器可能会成为操作系统机会中的一部分，微软、谷歌和苹果都可能基于自己的系统去建立相应的能力，竞争激烈。

**3\. 线上预定平台**

案例：Expedia, Kayak

• 使用频次：★★

• 短期影响：★★(long)

• 长期影响：★★★★★ (short)

这类平台主要提供的能力是对平台上信息的组织和履约能力。组织指的是更了解用户，帮助其高效地预约到合适的机酒；履约指的是保障交易的安全性和流畅性，避免违约的风险。

随着 ChatGPT Plugin 的推出，短期之内这类平台可能会增加一个高质量获客的渠道，但是长期是很可能受到比较大冲击的。因为 Chat 带来的语义理解能力提高，提供了一个更好的信息组织方式，用户能高效的给出需求，找到合适的航班信息，平台留下的主要壁垒是其交易的履约价值，这部分的价值比原来薄了很多。

**4.** **O2O / 电商平台**

案例：Instacart

• 使用频次：★★★

• 短期影响：★★★ (long)

• 长期影响：★★★ (long)

O2O / 电商类型的平台与线上预定平台相比，多了线下的供应链组织能力。这一部分能力是不会受到 LLM 领域冲击的，其中的 AI 算法也基本是优化方向的传统 ML 算法，并不是 LLM 擅长处理和调度的任务类型。因此，这类平台受到的影响相对较小，更多是多了一个高质量的获客渠道。

**5. 独立开发者 & 创业者**

案例：Giftwrap

• 短期影响：★★★★ (long)

• 长期影响：★★★ (long)

对于创业者来说，找到 PMF 和早期高质量用户是一个有难度的事情，而加入 ChatGPT Plugin 是一条比较快速的捷径。Chat 形式带来的用户，比传统投放渠道获得的用户质量会高不少，因为都是经过门槛比较高的交互后留存的，转化率会更高一些。而且接入的产品可以拿到用户完整的对话 prompt，这对理解消费者的用户画像也是相当关键的。

**03.**

**Plugin 的开发方式和能力边界**

**Plugin 开发门槛并不高**

OpenAI 提供了一套 plugin 接入范式，供企业和个人开发者根据指南进行接入。低门槛的接入方式是经过 OpenAI 官方设计的。用 Greg 的话说，就是为一个语言模型写 api 的文档：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

接入的开发门槛很低，只需要写两个核心组件：

**1\. api 接口，其中包含多个函数，负责定义不同场景下数据的输入和输出。**以后文将展开的 Speak 产品为例，需要执行翻译任务时将调用 Translate 接口，需要解释具体表达时使用 Explain Pharse 接口。而具体接口的逻辑选择就要用到第二个组件了；

**2\. Manifest 说明文件，通过自然语言 prompt 教会产品调用 api。**这个文件的核心是一段自然语言介绍，帮助机器理解这个插件本身的能力。当用户开启某些插件时，ChatGPT 会理解 prompt 中需要的能力是否与插件 manifest 文件中的描述匹配，进而判断何时调用 api ，以及使用哪个接口能最准确的实现目标。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

例如 Speak 这款多语言翻译和学习的产品插件中，其 Manifest 插件的文本内容被破解出来，大致内容如下：

• 当用户问到一个其他语言中的内容时，call Speak 插件来响应用户的语言学习意图；

• 当用户提供了一个明确的短语或句子需要翻译时，调用 Translate 接口；

• 当用户给了一个比较模糊的任务，比如“如何用西班牙语称赞别人的穿着”时，调用 explainTask 接口；

• 当用户给一个表达需要详细的解释，比如“putain 在法语中代表什么时，调用 explainPhrase 接口。

这个文档的写作风格目前比较接近开发过程中的文档和注释。但未来当更多 api 接入之后，肯定会有文档风格的差异，因为未来产品需要在其他同品类产品中脱颖而出，产品文档会以接近 SEO 的思路体现出自己产品的差异化优势，做文档和 api 的优化。

**Plugin 提供一套安全评估能力**

随着 Plugin 的开发和使用量增大，**plugin 的安全问题会逐渐成为一个重要的因素。**一方面，plugin 提供方是否有过度使用用户的数据；另一方面，plugin 是否会为了流量提高自己活跃的优先级。

在 2017 年，Adobe 曾经因为在用户的 Chrome extension 插件中加入了静默安装和访问网站权限陷入了争论。插件中包含了这样的能力：能把用户打开的每一个网页转成 PDF，因此要求用户给插件开放读取和修改网页的能力，引起了诸多用户的不满。

安全和权限是产品可用性的一个重要组成部分，Adobe 和 Chrome 在那次争议中都有一定的问题。Adobe 的产品很可能不会过度 track 用户的访问历史，但还是应该基于用户对这一功能的需求不那么激进的推进；Chrome 在权限管理时，当时没有把读取和修改网页内容的权限分级拆分出来，导致用户担心插件会在生成时修改内容。

**而 ChatGPT Plugin 的安全评估方式十分新颖：利用 LLM 的理解和角色扮演能力，让其成为 plugin 的安全审查员。**根据推特上研究 prompt injection 和 hacking 的用户 rez0 破解得到的信息，给 AI 审核员的信息主要分为三个板块：指令、事实和政策。

指令部分主要是对 AI 角色的定义：扮演一个在 OpenAI 工作的产品安全工程师，分析一个包含两个文件的第三方 plugin 是否符合要求（包含了 6个基本的安全问题，如是否获取个人信息，是否有参与不正当活动的能力等），并基于以上问题为插件的安全程度和适合年龄段进行打分。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

而事实和政策部分，则为 AI 审查员的决策提供了依据，政策部分明确了政治、色情的明令禁止的内容；事实部分明确了风险等级划分：

**1\. 低风险插件**只使用公开数据，不涉及任何个人信息；

**2\. 中风险插件**包含了个人或企业与第三方的交互；

**3\. 高风险插件**使用了高风险数据（金融数据、医疗数据、其他用户隐私敏感信息），或可能有欺诈行为的风险。

**Plugin 未来会走向更复杂的系统**

当下的 Plugin 还有诸多不成熟的方面：

**1\. 模型能同时调用的 plugin 数量很有限：**

目前的 plugin 只支持开启三个 plugin，ChatGPT 在 context window 中读入这几个的说明文件。由于 32k 的 input context 限制，5-10 个 plugin 的描述可能就是短时间内模型能读入的上限了。

**2\. 目前接入 plugin 的 api 设计方式大多还比较传统：**

ChatGPT 收到 prompt 之后，将其根据 description 加工理解写好给传统 api 的输入。这个优点是开发者可以很高效的把之前开发的 api 复用上，缺点是对开发者而言自由度不够高。

因此未来的 api 形式会有变化，输入数据不再是传输处理后的结构化数据，而是直接把 prompt 传给开发者，开发者将对 prompt 的理解和使用写进 api 中。

**3\. 当前给模型的描述文档，尚需要不断地根据竞品情况和模型的理解情况进行调整：**

例如，当一个垂直领域中加入一个新的竞争者时，如果竞争者有着更细粒度、更垂直的专注方向，大模型会将其专注方向的所有机会都交给竞争者。

针对以上提到的这些问题，需要一个更复杂的插件召回 plugin retrieval 系统来进行。这个系统可能包含有几层：

**• Plugin Store：**提供了一个统一的文档规定，来管理数以万计的 plugin ，经过审核后允许 api 开发者进行注册，更新和删除。进入 Plugin Store 的时候，应加入关于这一 plugin 的具体标签（就像 App Store 中的分类和信息），用于之后的召回和使用；

**• Plugin Retriever：**负责根据用户需要的行为，召回推荐最相关的 5-10 个 api。召回过程中，Retriever 将 prompt 的信息与 plugin store 中的标签和描述进行匹配，找到最相关的 plugin；

**• Action Executor：**负责调用 api 执行生成的动作代码，调用 api，返回最终执行结果（这里还有一步潜在的排序，模型选择 api 的过程类似于推荐系统中的精排）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**04.**

**Plugin 的 App Store 野望**

**“App Store”不是新鲜事**

由于过高的势能，OpenAI 推出 plugin 被视作 iPhone 推出其 App Store 的时刻。**我们认为客观来看，拥有一个应用和插件生态并不代表一个开放平台必然走向成功。**从 SaaS 巨头的历史来看，到达了一定体量的公司都必然选择建设 ISV 生态，通过“开放平台 + ISV”避免定制化需求开发，并且通过抽成捕获价值。**能否将这样一个平台建设成功是通往千亿美元级别平台的重要试金石。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*Snowflake 平台 Take Rate 数据呈现*

**在美国的过去十年很少有下一个重量级生态在消费者侧被建立 —— Meta 也没做成微信小程序式的应用分发生态。**但是一旦在消费者侧做成 App Store 级的生态，意味着：

• 比 SaaS 平台高 1-2 个数量级的生态价值；

• 比 SaaS 平台高高 2-3 个数量级的生态应用数量；

• 比 SaaS 平台高一倍的 Take Rate。

一个冷知识是 Apple 的应用商店并不是第一个“App Store”，但这个概念的起源的确是 Steve Jobs：

Salesforce 的创始人 Benioff 2000 年左右对公司发展方向比较困惑，找 Jobs 聊了下，对方给出了 3 个建议：

1\. 24 个月内增长 10 倍，不然没戏；

2\. 拿下一个大客户，比如雅芳；

3\. 必须建立一个 App Economy。

Benioff 立马付诸行动，发现自己的产品形态上更像 Exchange 而不是 Store，最终在 2005 年推出了 AppExchange。Benioff 之前听 Jobs 建议买了 App Store 商标和 appstore.com URL，在 2008 年送给了 Apple。

**从一个框架和五个案例推演 Plugin 生态的胜负手**

**一个框架**

抛开“App Store”的视角，聚焦到开放平台之上的插件生态建设，我们认为 Figma 给出了一个最好的框架，来用于分析一个生态的成功潜力：

**• 安全性：**包括用户的数据隐私、权限管理以及 ISV 和平台之间的权限和能力边界；

**• 稳定性：**平台的速度不应该被 plugin 拖慢，平台的更新不应该影响现有的 plugin，平台还应该提供在多个设备内统一的 plugin 安装管理；

**• 低门槛开发：**平台定义的框架和语言应该足够在满足其他前提下足够低门槛以让开发者很快上手贡献一个强劲的plugin 生态；

**• 性能：**plugin 本身应该是足够快和稳定的。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

除了这套框架本身的普适性之外，我们还比较吃惊于 ChatGPT 和 Figma 的惊人相似性 —— 他们的 plugin 生态是完全云化、Web 端为主、基于强劲的开放平台并且嵌入到主产品内的。**同时，我们认为这套框架缺乏包含的部分是对于开发者的激励以及在 plugin 数量膨胀后的分发机制。**

**五个案例**

我们将这套框架用于评估 5 个被视作取得了巨大成功的开放平台生态上，通过这种多案例研究的方法来得出一些对 ChatGPT plugin 的前景和坑的指导性判断：

**Apple App Store：最成功的 OS 应用商店**

安全性：★★★★★

稳定性：★★★★★

低门槛开发：★★

性能：★★★★

激励：★★★★

分发：★★

除了众所周知的一些成功之处外，Apple 在激励、分发、低门槛开发上的经验教训对于今天的 OpenAI 非常有参考意义：

• Apple 成功在 OS 之上建立起了用户的账户体系和自己端到端建设的全球支付网络 —— Apple 在 2008 年推出 App Store 时只支持终生买断制付费，在 2009 年引入了 In App Purchase，2010 年引入了 In App Marketplace，给了开发者完整的激励能力。**而 OpenAI 在账户体系及支付的建设还非常早期，不过跟 Stripe 的战略合作可能是一个好兆头；**

• App Store 在十几年发展后表现出了明显的分发问题，马太效应问题明显，大规模的 App 难以被分发和充分匹配。在经历过个性化推荐的 Genius、LBS 分发的 Near Me 和激励发现的 Explore 之后，Apple 最终没有发现更智能的匹配逻辑，回归到了保留至今天的 Curation 和 Editorial 风格。**OpenAI 对于 plugin 的分发可能有新的破局之道，用更智能和非用户主动选取的方式可以承载更大量级的匹配；**

• App 的开发门槛相当高，不过 Apple 从 2010 年 iPad 发布开始，会提前给开发者留出时间，让他们根据新设备和 OS 的特性开发应用。这样当用户购买时，他们会现在有丰富的新应用可供选择。**ChatGPT 在 GPT-4 和 plugin 发布上已经是这种风格了，但是对于双边怎么放量显然还缺少经验。**

**Salesforce AppExchange：在平台之上助力销售**

安全性：★★★★

稳定性：★★★★

低门槛开发：★★★

性能：★★★★

激励：★★★★

分发：★★★

AppExchange 是一个被许多人忽视的成功，里面包含了很多基本功建设，非常值得观察 OpenAI 后续能不能继续围绕这些方面优化用户体验：Salesforce 给开发者的前端框架从自己的 design system 演化为了 Lightning Web Components，后端则从基本的 SDK、api 和 Metadata 框架开始，发展出事件驱动的 Pub Sub api 架构，最后外部集成始于 VS Code 等 IDE 集成的优化，发展到 Salesforce Flow 完善的集成方案。

AppExchange 上起来的应用大部分在早期关注 SME 和 Mid-Market。如果要搞大客户，应用可以自己锚定 3-5 个名字，然后找 Salesforce 的销售渠道帮忙介绍，随后开启独立的销售流程。如果 OpenAI 未来需要打造草根崛起的 showcase，这会是个还不错的范式。

**Chrome Extensions：一度被忽视的生态**

安全性：★★★★

稳定性：★★

低门槛开发：★★★★

性能：★★★

激励：★★★

分发：★★

大部分的中国创业者和投资人相当沉迷于“移动互联网”，反而一度忽视了 Chrome Extensions 上长出的机会，除了我们写过的 Grammarly 和 Loom 外，第一个验证了 Chrome 生态的巨大成功是 Honey。这个电商优惠券聚合插件以 40 亿美元现金卖给了 PayPal。

Chrome 的生态可以引发对 OpenAI 的一点思考：不同于 App Store 在手机上的地位，Extension 一直仅仅被视作 Web 上的多个渠道之一，和官网、App、社交媒体账号并行，直到 19 年之后才有越来越多的公司将它作为主要的获客渠道。**如果让 ChatGPT plugin 的心智成为 KAYAK、Instacart、Expedia 的“获客副阵地“，它可能会陷入类似的尴尬处境。不过根据开发者的反馈，虽然在发布时引入了大量合作伙伴，实际运行的 plugin 生态更偏向新的、独立开发的、草根创业的 plugins。**

**Figma Community：社区带来差异化**

安全性：★★★★

稳定性：★★★★★

低门槛开发：★★★★★

性能：★★★★★

激励：★★

分发：★★

Figma 通过技术手段很好地完成了安全性、稳定性和性能的平衡，同时揭示了“低门槛”对于双边的重要性：Adobe XD 和 Sketch 都拥有历史更悠久的插件生态，但是用户往往需要在社区之外发现并下载安装，而开发者则需要通过类似 C 等语言编写其插件，而 Figma 则提供了设计师更熟悉的 Typescript 等语言在框架内进行开发，并且打造了跟主产品无缝的体验。

**VSCode Extensions：生态超越内部优化**

安全性：★★★

稳定性：★★★★★

低门槛开发：★★★★

性能：★★★★★

激励：★

分发：★★

VSCode Extension Store 也是个好的案例，用出色的插件生态（各种 Python 插件/自动补全） 在开发体验上超越了像 IDEA IntelliJ、Pycharm 那样由经营者内部优化的产品。在 VSCode 的设计中，他们把 IDE 涉及得可扩展性极强，能够让开发者很轻松地为自己开发设计好用的插件，并把插件开放给社区一起使用和优化。

**回顾 ChatGPT Plugin**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**05.**

**Plugin 干掉** 

**LangChain？**

紧随“App Store”论调之后的一类观点是 ChatGPT plugin 抹杀掉了 LangChain、Fixie AI 甚至是 Adept 的价值主张，这是相当程度上高估了 plugin 的说法。

仅仅看 plugin 这一个战略，它对 LangChain 目前的直接影响：

1\. 商业化方面可能会受到一定挤压，因为顺着这个开源项目本身的话，LangChain 几乎唯一的商业化方向是做 prebuilt hosted services；

2\. LangChain 跟 OpenAI 完全不是竞争关系：

• 这个开源项目在 Plugin 推出 2 天后就持续了在 LangChain 抽象下的 Plugin 实现；

• 将 Chain 和 Agent 跟 LangChain VectorStore 和 QA 逻辑做了解耦，从而更好地支持未来类似 OpenAI Retrieval 类似的 LangChain 以外的 retriever。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

从开发者反馈来看，也有相当多不同的声音：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

没有之前费劲学习过 LangChain 抽象、希望实现模型间可组合性的独立开发者构建 plugin 的方式基本是通过 Replicate 来方便地调用其他开源模型能力并通过 Replit 托管这个 plugin。下面这个 plugin 就很好地组合了 ChatGPT、Stable Diffusion 和 ControlNet 的能力：

抛开 plugin，OpenAI 在 6 月最新推出的函数调用对于 LangChain 和 Fixie 的影响倒更大一些。

**06.**

**Plugin 的路线图与连锁反应**

从增量的视角看，按照有短期到长期来排序，我们思考了 ChatGPT 能带来的一些变化：

**1\. 微软在 AI 的生态进一步增强**

OpenAI 缺审核，缺产品经理，缺运营这个生态的专家，缺更好的、比聊天界面搭配小组件更广泛的 UI。这些微软都有 —— 大量可以投入的人员，广泛可供 plugin 嵌入并发挥作用的一系列产品（消费者端的 Bing Chat 和 Windows 11 Copilot，企业端的 Microsoft 365 Copilot 和 Dynamis 365 Copilot 等）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

微软共享 ChatGPT plugin 已有的上百个 plugin 将极大促进它自己生态的冷启动，以让客户构造更多围绕内部私有数据的 plugin。微软围绕这个叙事布局了完整的产品和服务：Azure AI 可以提供在企业私有数据和云上运行和测试 plugin 的能力，而 VSCode 及 Github 则可以被用于帮助企业更好地构建新 plugin。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**2\. 针对模型调用的调用优化和新的 api 生态**

尽管真的像 SEO 或者 ASO（应用商店优化）一样的广告生态还非常远，ChatGPT plugin 的一些玩法已经出现了针对模型进行优化的雏形 —— 激烈的竞争发生在“Description for Model”中，那些描述自己为“宠物电商”的 plugin 可以获取精准匹配，这些流量不会被分配给拥有更粗粒度描述的 Shopify plugin，而更精细的“专为美国用户打造的宠物电商”则可以抢走美国的相关流量，优化这个 Description 已经成为 plugin 开发者之间非常有趣的角逐。

除了在 JSON file 上下功夫，专门为 ChatGPT 优化自己的 api 是另一个路径。OpenAI 在 6 月新推出的 Chat Completions api 的 Function call 功能可以帮助开发者实现“无代码”的体验，原来传统的 api 有很大的为模型重构的空间。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**3\. 多模型之间的可组合性创造更多用例**

类似我们在 05 末尾所展示的 plugin 例子，ChatGPT plugin 为 LLM 与 LLM 之间、LLM 与外部知识和 api 之间、LLM 与不同其他模型之间提供了一个用户可以轻松使用的 UI。发挥类似的可组合性创意能够创造出来许多在 LLM 与 Diffusion Model 不存在时难以出现的工作流和产品。

**4\. plugin 需求倒逼 ChatGPT 产品形态演进**

这一点是显而易见的 —— 如果 OpenAI 对于 ChatGPT 成为一个在消费者侧经久不衰的伟大产品仍然抱有愿景，并且搭建了一支合适的团队来实现这一点。目前来看，这非常可能成为现实，因为 OpenAI 刚刚招募了来自 Facebook、Uber 和 Airtable 的产品老兵 Peter Deng 担任 VP of Consumer Product。

**5\. 类 Chromebook 的硬件机会出现**

外界对于 OpenAI 进军硬件有非常高的预期。Google 围绕着 Chrome 的策略算是硬件跟软件生态配合的比较好的例子，Chrome Extension 在 Education 这个类别非常占据了统治级地位，诞生了 Grammarly 等公司，重要的原因是有 Chromebook 这个硬件让 Extension 生态被分发到了大量的师生用户。即使没有带来硬件交互上的爆炸性创新，能够通过硬件建立一个独特的用户分发渠道也可以帮助到整个 ChatGPT plugin 生态。

**6\. 模型内外部数据促进 AI Agent 的出现和演进**

从开放平台的视角思考 plugin 的意义会得出比较有趣的结论，它是 OpenAI 对外开放的一个重要数据接口，让第三方数据和用户 Query 等数据能够互动起来，而微软与 Azure 似乎致力于促进更多的企业私有数据开始与模型互动，这会加速许多人已经拉满了预期的 AI 助理的诞生。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

延伸阅读

Stability AI：AI开源商业化试验田，Killer Model能成长为Killer App吗？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Inflection创始人：从DeepMind到Pi，AI智能体如何迎来寒武纪大爆发

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Ayar Labs：挑战计算中心“最后一米”，LLM浪潮下的硅光探路者

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgw0Diay9MT5bbFgOFzTBkLicyVjZiaJOveRnHbhvbXqxQbqkH9oQpMvGcW5SgzXJia3Rnia55y4G5AeSOg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=29)

C-Eval: 构造中文大模型的知识评估基准

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgw0Diay9MT5bbFgOFzTBkLicyVjZiaJOveRnHbhvbXqxQbqkH9oQpMvGcW5SgzXJia3Rnia55y4G5AeSOg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=31)

对谈OpenAI：如何为全球70亿人部署“超级大脑”？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgw0Diay9MT5bbFgOFzTBkLicyVjZiaJOveRnHbhvbXqxQbqkH9oQpMvGcW5SgzXJia3Rnia55y4G5AeSOg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=33)