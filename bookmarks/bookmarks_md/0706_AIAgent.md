---
url: https://mp.weixin.qq.com/s/n0XrUIefTRSZpndtvuSdXA
title: "为什么 AI Agent 需要自己的浏览器？"
description: "AI Agent 才是下一代 infra 的目标用户"
author: "拾象"
captured_at: "2026-03-08T13:00:59.519Z"
---

# 为什么 AI Agent 需要自己的浏览器？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgyXPk0rficWHTaSwicFWGVw9SrGDLgnQhumDmoWbwzicoEvxsMH7giae2phBoXb2hNxxZBUsicrvKw34dw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgyXPk0rficWHTaSwicFWGVw9SExdaCpKxx4SOByrHWUf2usUIUypZ95cleyIfmSYt1h2Jx4DRtKbRHQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

编译：Xeriano

编辑：Cage

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgyXPk0rficWHTaSwicFWGVw9SZ1d3z0nghlpiclsjRXqibkApv6jictONvCLSu6CxXbBcDFdCSHriaXX5Cw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

浏览器的使用者正在逐渐从人类用户转移到 [AI Agent](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247511038&idx=1&sn=68b0d25b603317d23ed18b07e887338a&scene=21#wechat_redirect)，Agent 与互联网环境互动的底层设施也因此正在变得越来越重要。传统浏览器无法满足 AI Agent 自动化抓取、交互和实时数据处理的需求。Browserbase 的创始人 Paul Klein 早在 23 年底就敏锐地洞察到 AI Agent 亟需一个全新的交互载体——一个“为 AI 而生”的云端浏览器。这个浏览器不仅要解决现有工具的性能和部署问题，更核心的是要利用 LLM 和 VLM 赋予浏览器理解和适应网页变化的能力，让 AI Agent 能用更接近自然语言的方式与之交互，稳定地完成任务。

Browserbase 是一家成立一年多的 headless browser 服务提供商，以云服务的形式为 AI Agent 公司提供 scalable、高可用性的浏览器服务。近期，Browserbase 又推出了 StageHand，一种利用 LLM 使得开发者可以用自然语言与网页进行交互的框架，进一步拓展了其在 headless browser 领域的影响。

本文基于创始人早期备忘录进行了编译，详细阐述了这一技术革新的必要性与可行性。它分析了现有浏览器为什么不够 AI-native，描绘了利用 LLM 构建新一代 Headless Browser 的蓝图，并探讨了如何设计配套的 SDK 和 API 以提供极致的开发者体验，最终实现大幅降低 AI 与网页交互的门槛和维护成本的目标。我们编译的过程中能感受到 Browserbase 这一年多以来的产品实践和 Stagehand 框架的推出都能和文中的 roadmap 对应上。

💡 目录 💡

  01 目前的浏览器无法满足 AI Agent 需求

  02 Browser for AI 市场正在快速增长

  03 打造一个更好的 headless browser 

  04 如何走向市场

  05 风险与竞争

  06 总结

**01.**

**目前的浏览器无法满足 AI Agent 需求**

过去三十年里，浏览器一直是人类与网页交互的默认方式。人类是视觉主导的生物，更容易通过图形化界面来使用线上工具。为了满足用户日益增长的需求，人们也一直在努力创新，不断改进网页开发的流程，来更快地构建新的网站。现在，一个有意思的问题出现了：如果网站的主要用户并非人类，而是 AI Agent 呢？

根据 Cloudflare 的数据，互联网上已经有超过 40% 的流量来自其他计算机，也就是我们常说的 bots。由于互联网拥有海量信息，这些勤奋的 bots 会不断抓取（Scraping）其中最有价值的部分。之所以需要抓取数据，是因为很多网站并未提供结构化数据的公开 API 接口，导致机器人不得不像人类一样，直接在网站上浏览和获取信息。

一些基于大型语言模型的 AI Agent 展示了模型自主完成任务的能力，它们也会像人类用户一样，通过浏览网站来执行具体任务。试想一下，你的个人 AI 助手能够自己打开航空公司网站，通过聊天窗口帮你重新预订航班。在缺少 API 的世界里，网站就成了获取信息和交互的主要入口。

正是由于 bots 日益普遍、数据抓取的需求不断增加，以及需要通过访问浏览器执行任务的 AI Agent 的兴起，我们不禁想问：**开发者目前是如何构建网络数据自动化解析工具的呢？**

**问题1：Scraping 并不简单**

Scraping 真正有趣的地方在于：可以采取一种简单直接的方法，也可以深入构建一个强大的解决方案。当开发者从网站抓取数据时，他们通常会模仿浏览器，直接对目标网址发起一个简单的 HTTP 请求，例如：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这条简单的命令确实能从 Airbnb 的网站获取数据，但现实中有不少额外的问题。

现代网站通常不会在首次请求中就加载全部内容，必须等待页面上的脚本运行，以动态加载所需的数据。为了执行这些脚本，需要模拟一个完整的浏览器环境，以便脚本能够顺利调用所需的浏览器 API。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Airbnb.com 在初始页面加载后逐步加载数据

有时候想要的数据并不直接通过公开的 URL 获取，而是需要与页面进行交互，例如点击链接、输入信息并导航到相应位置。这种情况下需要实现页面交互的自动化。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

电子邮件框挡住了文章内容从而无法直接抓取内容

此外，一些网站能够识别 Scraping 行为，并通过验证码（CAPTCHA）来阻止访问。要绕过这些检测机制，通常需要发送特定的 HTTP 头信息，模仿正常浏览器的行为，伪装自己的请求。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

网站监测到了爬虫并要求输入验证码

即便顺利访问到了网页，下一步还得解析数据。然而，由于现代网页的结构往往十分复杂，开发过程中生成的页面标签也难以预测，且可能在每次开发者重新编译页面时发生变化，因此想要准确提取数据并非易事。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

网页中复杂结构的示例

这些困难几乎让开发者很难仅凭内置工具就构建出有效的 Scraping 流程。而令人意外的是，最好的工具其实正是他们每天都会用到的——浏览器。

**问题2：现有的 headless browser 不 AI-native**

headless browser 是一种完全通过代码控制运行的浏览器，是做 scraping 最好的基础设施之一。这类浏览器并不会打开图形化界面（GUI）并渲染窗口，而是直接在内存中完成所有操作。这是因为计算机只能读取，而不需要“看到”，因此在抓取数据时无需实际渲染页面。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

有头浏览器和无头浏览器的对比

目前，已有一些流行的 headless browser 库，其中最主流的是谷歌的 Puppeteer 和微软的 Playwright。两者都提供了对浏览器 API 的全面访问，广泛应用于各种场景。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

一个创建 Airbnb 账户的 Puppeteer 函数

程序员通过 headless browser 与网站交互的主要方式是使用 CSS 选择器。正如上述示例所展示的，选择器用来确定页面上哪些元素可见，在哪输入信息，以及需要点击的位置。然而，CSS 选择器是无类型的纯文本，因此开发者无法享受现代强类型语言在编译阶段就捕捉错误的好处，使得开发过程更加脆弱和容易出错。此外，定义这些交互流程十分繁琐，因为选择器极其脆弱。一旦页面结构稍有变化，之前建立的流程就会崩溃。如果任一步骤顺序出现偏差，整个过程都会中断。此外，要判断页面是否加载完成，通常需要等待网络请求结束，这种模式意味着大量的等待时间。

除了语言本身的复杂性之外，可编程浏览器库本身也存在冗余臃肿的问题。以 Puppeteer 为例，在 Linux 上安装时需要高达 282MB 的依赖，这个体积是非常巨大的。作为参考，AWS Lambda 服务的最大部署大小仅为 250MB，意味着用户不得不采取其他解决方案。类似的问题也同样出现在 Playwright 身上。

造成如此庞大依赖体积的直接原因是 Puppeteer 运行时需要整个浏览器环境，导致它携带了大量实际代码中用不到的功能。

需要强调的是，这些已经是当前最流行的 headless browser 库了。尽管它们位于诸多重要工作流程的核心，但仍然存在各种不便和痛点，导致开发体验并不理想。

**02.**

**Browser for AI 市场**

**正在快速增长**

大型语言模型的知识范围受到训练数据的限制，因此往往依靠浏览器来获取最新的知识。当前主要有两种技术途径实现这一目标：

第一种方法是 RAG。LLMs 会先通过浏览器获取信息，然后将这些信息作为额外的上下文，补充到 prompt中。这种额外的上下文能够帮助 LLMs 给出更精准的回答。

另一种方法则是基于 Plugins/Web Agents 的范式。一些应用向 LLMs 提供一个浏览器接口，当 LLMs 接收到需要联网执行的任务时，会自主调用该浏览器接口，自动地完成页面导航、数据解析等操作，直至完成用户交代的任务。

除了 ChatGPT 以外，目前其他主流的 LLMs 编排框架也已集成了浏览器自动化功能。Langchain 作为当前广泛使用的框架，提供了一个基础的 Web Browser 插件，使用的正是前面提到的 Scraping 方法。同时，Langchain 也与Browserless 有专门的集成，用于更高效、更稳定的 Scraping。

近期，OpenAI 知名研究员 Andrej Karpathy 描述了一种不久之后可能出现的“LLM操作系统”。在他给出的系统图中，可以清晰地看到：浏览器与文件系统、向量数据库（embeddings/vector databases）并列，成为LLM的核心基础组件之一。这一点明确显示出浏览器对于 LLMs 的重要性，尤其是随着 LLMs 使用外部工具能力的不断增强，这种趋势只会越来越明显。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Andrej Karpathy 在 Youtube 视频中给出的 LLM OS 的结构

当前的 Scraping 和浏览器自动化市场已经非常可观。从 NPM 下载数据来看，Puppeteer 这个库的增长规模已经与 Next.js 相当，后者是 Vercel 旗下非常流行的网页框架。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

通过 NPM 的每周下载量

可作为参考的上市公司是 UIPath，这家公司专注于 RPA 软件开发，帮助企业自动执行各种常规业务任务。UiPath 今年的营收预计将超过 10 亿美元，充分体现了 AI 驱动的任务自动化所蕴含的巨大市场潜力。然而，其浏览器自动化工具本身的吸引力则相对逊色。

目前，这一领域的初创公司已经吸引了诸多财富 500 强企业的关注，这显示出企业市场对浏览器自动化工具的强烈需求。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

使用 ScrapingBee 的一些客户

此外，还有几个重要的趋势将进一步推动浏览器自动化工具的快速普及：

• 训练新的基础模型，需要大规模的数据抓取。

• 数据所有方（例如Wikipedia、Reddit、StackOverflow）希望更好地维护数据的商业价值，这将使数据抓取变得更复杂，从而要求更强大的浏览器自动化工具。

• 一批公司将通过 Web Agents 实现自动化地与网站交互，这种功能可能成为这些公司产品的特色甚至其主要的业务方向。

• 现有的 SaaS 公司可能会增加一些基于AI的功能，而这些功能将依赖浏览器自动化来实现。

• 许多传统网站无法提供足够的 API 来获取数据，因此长期来看，浏览器自动化将成为唯一的解决方案。

**03.**

**打造一个更好的** 

**headless browser** 

回顾一下此前提到的目前 headless browser 存在的问题：

• 现有的浏览器自动化库臃肿，性能未得到优化。

• 在现代云环境中的部署流程过于复杂。

• 现有的脚本语言构建的集成方案非常脆弱，经常出现故障。

• 脚本通常依赖设置任意的等待时间，容易出错且效率低下。

• 从页面解析数据的过程繁琐，往往需要大量试错。

简单来说，开发者们真正想要的是一个性能更强、可靠性更高、且使用更简便的浏览器自动化方案。我在阅读了许多开发者的反馈意见后，可以清晰地看到开发者们同样迫切地希望拥有一个更出色的浏览器自动化平台。

有三个关键的创新点可以实现一个性能更佳、云原生、以 AI 为核心的下一代浏览器自动化平台：

**1.** **打造一个开源的、高度优化的 headless browser**

我们不应再容忍缓慢的冷启动和臃肿的依赖包。

**2\. 用 AI 赋予浏览器“超能力”**

不再强迫开发者手动构建复杂的页面解析树，而是通过 LLMs 高效地定位页面中的信息，即使网页结构发生变化，也能快速找到数据。使用 GPT-4V 这类视觉模型，直接基于截图识别页面元素，而不是传统的代码解析。开发者可以直观地询问：“页面加载完成了吗？”或“登录按钮是否可见？”，而无需复杂的技巧或猜测。访问被混淆或隐藏的信息，比如网站为了防止抓取而将价格信息藏在图片里，而非文本中。

**3\. 提供全新层次的接口，给开发者带来极致的体验**

从根本上重新设计 SDK，因为当前的流程化接口对处理复杂的重试和分支操作不够友好。但是，为保证迁移平滑，应同时保持与 Puppeteer 接口的兼容性。让开发者能够充分利用最新的“AI 原生”创新技术。不过，传统方法有时可能更高效，因此开发者可以灵活选择最适合其使用场景的方案。一个出色的平台还需要提供强大的 API，方便开发者轻松管理底层的浏览器基础设施，全面提升用户体验。

\*译者注：站在 2025 年回看的 browserbase ，我们会发现其发展历程与创始人提出的策略三大策略是吻合的，browserbase 通过其开源策略迅速打开了市场，并在 2024 年底发布了 StageHand，一种利用 LLM 将自然语言指令转换成 Playwright 代码从而操纵 headless browser 的开源框架，使得开发者可以用自然语言与网页进行交互，而不再需要手动解析复杂的网页结构并进行维护，大幅降低了 AI Agent 联网的成本。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

开发者使用自然语言与 Stagehand 交互，

Stagehand 则将自然语言转换成 Playwright 代码并通过 Browserbase 调用浏览器

**04.**

**如何走向市场**

如 a16z 合伙人 Alex Rampell 所说：“每家初创公司与现有巨头之间的竞争，本质上就是看创业公司能否在巨头实现创新之前，抢先获得市场分发。”

如果没有强有力的 GTM 策略就无法获得成功，“首次创业的人痴迷于产品，二次创业的人则专注于分发。”针对开发者工具类产品，最有效的分发策略如下：

• 打造一流的产品

• 通过开源投资于社区

• 建立值得信赖的品牌

• 教育并赋能开发者

其中最重要的一点是，产品必须卓越。无论多精美的包装或漂亮的落地页，都无法弥补产品本质上的不足。只有真正过硬的产品才能抓住当前市场中的巨大机会。

投资于社区，意味着在获取价值的同时也回馈社区。现有浏览器库大多为开源模式，新的产品也应该如此。开源是一个极佳的分发渠道，将出色的软件免费提供出去，开发者自然更愿意体验你的产品，并逐步转化为付费用户。

在开发者工具领域，建立良好品牌的重要性不容忽视，甚至可以与产品质量本身并列。口碑传播是开发者工具公司最有效的渠道，其次才是自然搜索流量。

想要真正吸引开发者，就必须去他们所在的地方与他们互动。如果大量精力投入在吸引用户上，却没有精心撰写优秀的文档，或缺乏适合开发者语言的 SDK，那之前所有的努力都是徒劳。这些投入会直接推动口碑传播——最好的赞赏莫过于“你看过这家初创公司的文档吗？真的太棒了！”

因为现有的浏览器自动化流程经常出错，这为新产品提供了大量机会。开发者在处理原本正常运行的代码突然失效时，正是他们最容易转向其他更稳定工具的时机。这种情景对开发者工具来说相当罕见，因为多数情况下这些工具都是“一次配置好，后续无需再关注”。

拥有一个被社区积极认可的可信品牌本身就是一道壁垒，尤其当开发者开始积极贡献开源核心产品的代码时。避免成为 commodity 的最佳方式，就是成为开发者群体的默认选择，而优秀的开源项目正是实现这一目标的关键。

由于开发者工具领域的绝大部分收入通常来自市场顶端的 20% 用户，因此自下而上的市场拓展策略（Bottoms-up GTM）更多是为增强口碑传播，从而长期打开企业级客户的收入大门。

最后，随着核心业务的成功，公司也拥有大量向外扩展的机会，比如：

• 将抓取的数据存储服务打包提供，并开放统一的查询 API；

• 支持用户数据持久化，加速任务完成；

• 建立社区化的工作流市场（例如从 McMaster-Carr 订购特殊螺丝的自动化流程）。

尽管个人更倾向于横向平台模式，但短期内，将自身定位成一个统一的传统数据源 API 平台，也可能更快地捕获市场价值。这样一来，很多此前无法实现的自动化流程，都可以直接基于该平台构建和运行。

**05.**

**风险与竞争**

**Browser for AI 的 6 个风险**

**风险1：在已有市场中成为默认选择非常困难**

**策略****：**

用全新范式颠覆市场，使初创公司能够对市场进行细分，从而找到适合切入的空间。

**参考案例****：**

**Heroku (已有的领军企业) vs [Vercel](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247507124&idx=1&sn=981ee092424b1426bd4353f0e96e8f1f&scene=21#wechat_redirect) (新晋的创业公司)：**Heroku 提供全面的 PaaS 解决方案，而 Vercel 通过无服务器和前端优先的范式，专注于现代 JavaScript 开发者的细分需求。

**Mailgun (已有的领军企业) vs Resend (新晋的创业公司)：**Mailgun 是功能强大的邮件基础设施领导者，而 Resend 以开发者体验和设计驱动的服务，瞄准现代技术栈用户的特定市场。

**风险2：浏览器自动化可能与客户的核心产品深度绑定，客户可能不愿外包**

**反驳观点****：**

如果一个功能足够重要且具备足够的复杂度，客户如果坚持自主开发将面临巨大成本，这种情况下外购是更合理的选择。这实际上是典型的“自建 vs 购买”问题。

**风险3：LLMs 推理成本太高，可能导致很多使用场景成本过于昂贵**

**反驳观点****：** 

LLMs 的推理成本在长期趋势上很可能会持续下降。

**策略****：** 

将 LLMs 的相关功能设计为可选模式，让客户能够自主控制成本，从而支持更广泛的应用场景。

**风险4：这类基础设施产品容易商品化，利润率面临持续压缩的压力**

**策略****：** 

如果可能的话，重新设计创新性的定价策略。例如不再按会话数收费，而可能按照吞吐量收费。

成为基础设施意味着需要非常小心控制单位成本。

**风险5：滥用与法律合规风险**

**反驳观点**： 

截至 2022 年，根据美国第九巡回上诉法院的裁定，Scraping 行为是合法的。

此外，AI 领域的技术创新也使得识别滥用行为变得比过去容易百倍。

**风险6：如果大公司（如 OpenAI、Google 等）自己开发此类产品怎么办？**

**反驳观点****：**

本质上，LLMs 本身无法直接内置浏览器功能，因为浏览器属于单独的技术领域。OpenAI 等公司不太可能将浏览器与 GPT API 直接捆绑，因为这将引入额外的复杂性（例如计费或技术对接）。

即便 OpenAI 等公司开始整合类似功能，开发者仍然需要大量定制化的配置，以满足具体应用需求。

个人助理的使用场景可能最终由苹果或谷歌等巨头主导，他们会为最常用的服务提供原生集成接口。

但日常生活中频繁接触的大量中小型商家（比如街角的面包店或理发店）不可能提供原生 API 接口，因此这些场景仍然需要依靠浏览器自动化实现。

**Browser for AI 的 3 类竞争对手**

与向量数据库领域相比，浏览器自动化这一基础组件在风险投资市场中的资金投入明显不足。现有的公司大多是自筹资金（bootstrap）起步，或融资金额低于500 万美元。而获得大额融资的公司多数并未真正服务于构建相关应用的开发者群体。

本文将现有的初创公司划分为三大类别：**浏览器自动化、Scraping API 和 信息检索 API。**

**浏览器自动化**

**Browserless**

• Browserless是该领域最接近龙头位置的公司，在市场渗透率和开发者中的品牌认可度都很不错。

• 它的本质是远程托管的 Puppeteer，核心创新主要集中在基础设施层，而非SDK层。

• 团队规模较小，最近被一家新 buyout fund 收购。

**Browse.ai**

• 一家获得风投支持的公司，但主要偏向消费者市场或低代码用户群。

• 它提供的“Website to API”功能非常有吸引力。

**Induced.ai**

• 已融资 230 万美元种子轮，专注于企业 RPA 和专业消费者市场。

**Scraping APIs**

这些公司提供一个 URL 接口，然后返回通常为非结构化的数据。这些 API 公司通常还提供一些额外的功能，例如绕过 CAPTCHA 验证或使用代理服务（proxy）。

• ScrapingBee

• WebScrapingAPI

• ScraperAPI

**信息检索APIs**

这类初创公司更专注于特定信息的搜索和检索服务，而非通用的浏览器自动化。

• Metaphor Systems

• SerpAPI

未来行业内顶尖公司的产品应该同时吸取上述三类公司的特点和优势。目前看来，没有任何一家现有公司处于绝对领先地位，市场中真正最大的竞争对手反而是自己构建方案的开发者。

**06.**

**总结**

• 可预见的未来，Scraping 依然会是长期存在的需求。

• 互联网本质上是不确定的，但我们目前仍在用确定性的工具来应对它。

• 浏览器自动化这个基础组件长期以来缺乏足够的投资，而 AI 应用在未来很多年都将高度依赖这一能力。

• 市场上存在大量 AI 和非 AI 的使用场景，这为新兴创业公司提供了难得的颠覆机会。

• 能够把握住这个机会的创始人，通常具有深厚的 headless browser 技术背景、开发者工具经验，以及对 AI 领域的热情与洞察力。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

排版：Doro

延伸阅读

Exa：给 AI Agent 的 “Bing API”

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Cartesia: 3 个月融资 9100 万美元，从 Transformer 到 Mamba 重塑语音 AI

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

大模型非共识下，什么是 AGI 的主线与主峰？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Physical Intelligence 创始人：人形机器人被高估了

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

详解 MCP：Agentic AI 中间层最优解，AI 应用的标准化革命

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)