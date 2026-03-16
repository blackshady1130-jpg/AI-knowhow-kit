---
url: https://mp.weixin.qq.com/s/Ph9qRA2RI7EcRHg_wYIzXQ
title: "详解 MCP：Agentic AI 中间层最优解，AI 应用的标准化革命"
description: "开源 1 个季度后，MCP 已经显著垄断 Agentic AI的中间层"
author: "拾象"
captured_at: "2026-03-08T12:55:52.180Z"
---

# 详解 MCP：Agentic AI 中间层最优解，AI 应用的标准化革命

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxBaTiazNtoZc250YeTbVDtJIHI9FbUiazmdkmaf61u6xh4rzMBCgtic5pMtzCsYDqf4uL7C1dEzBHmw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxBaTiazNtoZc250YeTbVDtJuEdTQksBN2BpUMSPPiaPnGg1gV5sQ3L8fFkCQyKKp1xy4LMDbvjdgLA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

作者：cage, haozhen

编辑：Siqi

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxBaTiazNtoZc250YeTbVDtJhsXANBhzliajrjfrD5FjgHibv8Tr7Pibc2qhYkbPMQRRtVMRicyT9a69yA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

在[拾象团队的 2025 的 AI 关键预测](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247511096&idx=1&sn=dee1163cad5af574582fa538532a9a0a&scene=21#wechat_redirect)中，我们提到：**随着 Agent 时代到来，OS 才是 LLM 厂商们最高的护城河，从 computer use 到 MCP，Anthropic 构建 OS 的决心是 AI labs 中最强、最明显的。**

在开源 1 个季度后，MCP 已经显著垄断了 AI Apps & Agents 和 Tools & Data Sources 之间的中间层，它的使用增长速度几乎是所有开源框架里增长最快的：MCP Server 已经增长到 2000+ 个，在开发者群体中的普及和渗透度也在迅速提升。尽管做好一个中间层协议还有很多挑战，但 MCP 广泛应用和生态上的成功已经证明了其重要性。

本篇研究是我们对 MCP 技术、价值和这个新生态下创业机会的思考总结。我们对 LLM 中间层框架的研究可以追溯到 [Langchain](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247501117&idx=1&sn=e860ac5e259a969f62b05d080bf42d14&scene=21#wechat_redirect)，MCP 是对其他所有 LLM 中间层的集大成者。Agentic AI 的实现基础有 context、tool-use 和 memory，RL 环境给 tool-use 提供了 infra，MCP 的出现则是让 context 价值最大化。

Anthropic 官方将 MCP 类比为 USB-C 端口，隐含着要把 MCP 打造成标准化接口的目标。我们认为，**MCP 所处的位置可以类比为移动支付的基础支付协议，MCP 的出现可能可以长出“Agentic AI 领域的 Stripe “**，此外，我们也已经看到 MCP marketplace，server infra 以及 Agent OS 等机会。

**Insight** ***01***

**MCP 已经显著垄断了 Agentic AI 的中间层**

去年 11 月，Anthropic 开源了 Model Context Protocol，即 MCP。MCP 是一种开放协议，允许系统向 AI 模型提供上下文信息，并且可以在不同的集成场景中通用化。MCP 定义了 AI 模型如何调用外部工具、获取数据以及与各种服务交互。

**Anthropic 官方把 MCP 比喻为 AI 应用的 USB-C 端口**，它可以提供统一的连接方式。没有 MCP 的时候，开发者需要为每个数据源创建自定义的整合方式和 API，既耗时，又不 scalable，而 MCP 允许 AI 应用通过统一协议访问文件系统、数据库等，简化了整合过程，LLM 的使用体验也会更好。 

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

从发布至今的一个季度时间里，MCP 的使用增长速度几乎是所有开源框架里增长最快的，**2025 开年以来，MCP 显著垄断了 AI Apps & Agents 和 Tools & Data Sources 之间的中间层。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

MCP 在 AI 开发者核心圈中的口碑非常好，讨论度也非常高。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Insight** ***02***

**MCP 生态已经出现**

MCP 不仅在开发者群体的渗透率增长极快，而且围绕 MCP 已经开始出现“生态”。

下图是 a16z 对 MCP 市场的梳理，可以对“MCP 生态”有更加直观的感受。首先， MCP Clients 和 MCP Servers 已经相当丰富，而围绕 MCP，也出现了专门的 Marketplace、Infra 等产品。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

a16z MCP Market Map

**MCP 中的核心概念**

MCP 中有两个核心概念，分别是客户端 MCP Client 和服务器 MCP Server。MCP Client 从 MCP Server 得到所有工具（tools 或者 function calls）的列表和描述，LLM 根据具体描述决定应该使用哪个工具或 Context。总的来说：

• 对于 AI 应用开发者而言，有了 MCP 后，产品可以无缝连接到任何 MCP Server，获得 Context；

• 对于 tool / API 开发者而言，只要搭一个 MCP Server，就能自然获得开发者的使用；

• 对于企业而言，可以把数据和工具由不同的团队封装成 MCP，使得数据库能成为与 Agent 交互的接口。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

因此，开源社区和各个 startup 都会有动力去开发各自的 MCP Server，来让 AI 应用更好使用。

• **客户端 MCP Client：**

**MCP Client 指的是 LLM-native 产品或者 Agent，**比如 Claude Desktop 产品、IDE 产品，未来任何想通过 MCP 协议调取数据的 AI 产品都是一个 MCP Client，都可以通过 MCP 协议访问数据。**借助合适的 MCP Server，用户可以将每个 MCP Client 变成一个“万能应用”。**

以 Cursor 为例，虽然 Cursor 是一个代码编辑器，但也是一个功能完善的 MCP Client。终端用户可以通过 Slack MCP Server 将 Cursor 变成 Slack 客户端，也可以通过 Resend MCP Server 让 Cursor 实现发送邮件功能，或者通过 Replicate MCP Server 让 Cursor 实现生成图像功能。

更强大的是，一个 Client 可以和多个 MCP Server 连接，每个 Server 可以获得互联网资源，也可以连接本地资源。例如，在 Cursor 的使用上，用户可以安装一个 Server 实现生成前端 UI 的功能，同时让 AI Agent 调用可以图像生成的 MCP Server，为网站生成视觉图片。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

目前大多数高质量的 MCP Client 都以编程为中心，因为开发者通常是新技术的早期采用者。而对于非技术用户来说，将 Claude Desktop 作为 MCP Client，是一个可行的切入点。随着 MCP 的成熟，预计会看到更多面向业务的 MCP Client 出现。

• **服务器 MCP Server**

**MCP Server 指的是可以让 LLM 理解 Context Layer 的转换接口，**是轻量级 Context 连接软件，如文件系统访问或数据库查询。**MCP Server 可以看作是开放版本的 GPTs（GPTs 非常封闭，只能在 ChatGPT 的 App 里开发）。**一个 Server 可以有多个功能，类似 function call 或者 tool use，LLM 会自行理解并调用需要的能力。目前头部数据库公司、Coding 公司和创业公司，基本都有自己的 Server。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

如下图所示，其中 description 部分是 MCP Server 开发者写的详细描述，比一般开发者快速写的会效果更好。同时， MCP 也允许使用时可以再额外加入 prompt。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**MCP 使用场景非常多元**

从 Server 分布来看，MCP 的使用场景相当广泛，包括数据库、搜索、设计、支付、生产力工具等，其中最高频的是搜索和数据检索。

**MCP 的开发模式是由社区推动的，随着 MCP 的普及，企业开始开发官方版本，最终 AI 工具可以在官方版本、社区版本和自定义实现之间进行选择。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

目前 MCP 在 GitHub 提供的 154 个 MCP Servers 列表里，使用场景最多的是搜索和数据检索，可以实现网络搜索、爬取内容、语义检索、向量搜索等功能。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

下图是一个用 MCP 自建 Deep Research 的典型案例：用户可以用 MCP 在 IDE 里面搭建自己想要用的产品形态，比如将 Deep Research 集成到 AI 代码编辑器中。用户只需添加全新的 Firecrawl MCP 与 Deep Research，它就能自主探索网页，为代码项目提取最新的研究成果。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

去年 12 月，Anthropic 举办了 MCP Hackathon，邀请了 100 多位开发者在 3 小时内构建应用。从最终结果来看，我们可以感受到：（1）MCP 的使用场景非常多元，甚至跳开了 AI 应用原先比较集中生产力的场景；（2）开发者希望通过 MCP 去实现 tool use 或者执行多步骤任务。

获奖成果具体包括：

• 获得趣味奖的 Santa Claude：是一个用于节日购物的 AI Agent，Claude 助手可在 NYT Wirecutter 上查找节日礼物推荐，并直接在 Amazon 购买；

• 获得效率提升奖的 Clauduct Manager：是一个 AI 产品经理，通过将 Claude 连接到 Linear，Agent 可自动编写产品需求文档（PRD）、创建任务，并按难度进行优先级排序；

• 获得特别奖的 Golden GateKeeper：是一个 AI 推荐清单，Claude 助手可以连接到 Google Maps 数据库，涵盖旧金山湾区 500+ 地点，并规划行程；

• 获得创意奖的 Run MCP：通过简单的 prompt，来动态赋予 Claude 新的工具，功能包括下载文件、运行 FFMPEG、生成 QR 码等。

**Insight** ***03***

**MCP 会带来 “Agentic AI 领域的 Stripe”**

**MCP 不仅是 USB-C 端口，还是一个转接口，能把不同的数据类型和 AI 应用打通，把不同的 Context、tool 与 Agent 连接起来。**

Anthropic 官方将 MCP 类比为 USB-C 端口，在这个定义下，也隐含着 Anthropic 把 MCP 定位于标准化接口的意思，**这个标准化接口其实是定义在 MCP Server 和 LLM 之间的。**

MCP Server 其实有两个接口：一个是和 LLM 之间的接口，另一个是和数据源之间的接口。现在相当于把数据转化的工作放在 MCP Server 上，转化过程可能是千差万别，不同的数据源可能没有办法统一，但是当 MCP Server 完成数据转化并传送到 LLM 的时候，这个接口就是一个统一的接口了。**所以对于 Anthropic 来说，有了 MCP 后就有了一个统一的标准化接口。**

**数据转接的工作并不会因为 MCP 的出现而消失，MCP 是将这个工作量在各方之间进行了重新分配。**

在 GPT 时代，OpenAI 之类的大模型供应商承担了这个工作，比如用户把 PDF 之类的数据上传，OpenAI 需要做数据转接的工作，但 OpenAI 做的效果并不好。在 Langchain 体系里，数据转接工作交给了 Cursor 之类的 AI 应用开发者，这些开发者花了很多时间做接口。

目前，MCP 的使用已经渗透到了非 Anthropic 生态的应用，MCP 相当于把转接解耦，使得存在一个中间层，独立开发者也可以去做转接头工作，如果转接头做的足够好，那 Cursor 等应用就可以直接使用。但现状是大部分独立开发者做的转接头都不够好，所以转接头还是需要 Cursor 之类的 AI 应用开发者来做。

围绕“统一接口”、“应用打通”这个角度来看，MCP 是否可以被类比为移动支付领域 Stripe？Stripe 的价值在于**打通了各个银行的电子支付系统，并提供了一套集成的 API 方便企业“一键接入”这些支付系统。**

**我们认为，MCP 并不能和 Stripe 直接类比，但“Agentic AI 的 Stripe”是比 MCP 更靠近产品层的机会：MCP 可以类比为基础支付协议，Stripe 诞生的前提是基础支付协议，MCP 出现后，Agentic AI 领域的 Stripe 则可能会是创业公司的机会，是 Agent 领域的关键 infra。**

**Insight** ***04***

**MCP 能让 Context Layer 效果最大化**

**要让 AI Agent 真正发挥作用，需要三大核心元素：正确且丰富的 Context、完整的工具使用环境、和 Agent 持续迭代的记忆。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Anthropic 的官方博客中提到 MCP 的思路借鉴了 LSP（语言服务器协议），但 MCP 超越 LSP 之处在于它以 Agent 为中心的执行模式：LSP 主要是被动响应（根据用户输入，从 IDE 接收请求并作出回应），而 **MCP 的目的是支持自主运行的 AI 工作流。基于 Context，AI Agent 可以自主决定使用哪些工具、以何种顺序调用，并如何串联起来完成任务。**此外，MCP 还使人类能够提供额外数据并对执行过程进行审批。

**我们在** [**2025 Best AI Ideas**](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247511096&idx=1&sn=dee1163cad5af574582fa538532a9a0a&scene=21#wechat_redirect) **中提到，Context Layer 是构建高质量 AI agent 的重要基建，**而 MCP 的出现能够帮助 Context Layer 实现最好的效果。因为 Context Layer 通常需要开发者自己进行定义，和等待 LLM 供应商花时间优化 Context Layer 相比，MCP 作为开源协议是最能发挥社区的力量来加速这个过程的。

💡

Language Server Protocol （语言服务器协议，简称 LSP）是微软于 2016 年提出的一套统一的通讯协议方案，连接 IDE 和 Language Server。语言服务器（Language Server）的作用是提供特定编程语言的智能分析能力，并通过协议与开发工具通信。

LSP 的核心思想是标准化语言服务器与开发工具之间的通信方式。这样，一个语言服务器可以被多个开发工具复用，而开发工具也能以最小的代价支持多种编程语言。在 LSP 中，当用户在编辑器中输入时，客户端会查询语言服务器，以获取自动补全建议或诊断信息。

Tool use 的核心是 RL 环境，而 memory 目前还没看出标准化的趋势，可能是每个 Agent 开发者需要花最多精力进行个性化的地方。

**Insight** ***05***

**MCP 是已有中间层的集大成者**

**MCP 出现之前，已经有很多公司推出过中间层产品：包括 OpenAI 推出的 Function Call、GPTs、Agent SDK，以及 LangChain，LlamaIndex 和 Composio。而 MCP 是一个集各家之长，而且更轻量、开放的底层协议，对这些产品冲击不小。**

• **OpenAI Function Call：Function Call 最早发布的时候，我们判断这是一个可以有生态属性、让 API 有差异化和用户粘性的设计。**我们可以看到 OpenAI Function Call 的很多思路给了 MCP 启发，但 Anthropic 把 MCP 做成了更具生态价值的中间层，而不是只是一个 API feature。

• **OpenAI GPTs ：**其技术基础是最早的 ChatGPT Plugin，用 manifest file 来向 LLM 介绍工具，这个思路也在 MCP 中得到沿用。但 GPTs 太封闭，必须在 ChatGPT 的产品基础上开发。

• **OpenAI Agent SDK：**还不确定最后的使用率会如何，口碑比较好的地方基本上集中在 response API，同时有 completion 和调用的部分，和 MCP 其实是不一样的。

• **LangChain / LlamaIndex 受 MCP 的冲击是最大的：**LangChain 和 LlamaIndex 想做 Agent framework，Langchain 更侧重 tool use，LlamaIndex 更侧重 Context。但因为过于其偏高的抽象程度和复杂的 Agent 框架，很多 LLM 开发者不会长期 adopt 这两款框架，初步使用后转而自己开发。

• Composio 在 MCP 环境下的生态位还不错，Composio 预置了一些自认为比较高级而且好用的工具，直接架在所有 MCP 的环节上，**如果 MCP 环境下有类似 Stripe 的机会的话，Composio 的生态位比较好，但这个领域才刚刚开始，还会有很多变化。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Insight** ***06***

**MCP 是 Agentic AI 的安卓，**

**但 Apple 还没出现**

**当开发者想让一个自己不能控制或者自己不能开发的 Agent 去获取某个数据源和工具的时候， MCP 是最好的选择。**举个例子，当用户想让 Cursor 从 Slack 中获取数据，MCP 就是最好的选择，因为用户对 Cursor 和 Slack 其实都没有自己开发或控制的能力。

Langchain 和 OpenAI Agent SDK 很多时候是为了开发 Agent 的开发者用的。但是开发者总是会对关键功能的接口效果做非常精细的调试，比较难出现协议或框架的标准化机会。相比之下，MCP 比较开源且灵活，但使用效果的精细和效率可能不如 Agent SDK。

MCP 更适合作为一个开放式协议，即使是一个只使用工具而不开发工具的人，也可以通过 MCP 来获得 Context，这是 MCP 真正做的非常强大且火爆的原因。

**如果从安卓 VS 苹果的角度来看，MCP 类似安卓，但目前还不确定 OpenAI Agent SDK 等的效果是否类似苹果。**

**Insight** ***07***

**MCP 生态下创业公司的三个主要机会**

我们在前面提到，MCP 的生态属性还在于围绕 MCP 出现了特定的创业机会。例如，a16z 提到的 Marketplace，Server Generation&Cuiration，Server Hosting 和 Connection Management。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

目前 MCP 仍处于早期阶段，仍有许多待解决的问题，比如，如果有可以支持大规模 MCP Server 部署和维护的精简工具链，MCP 的渗透率可以更高。

以及，目前大多数 MCP Server 都是本地优先，并专注于单一用户。这主要是由于 MCP 目前仅支持 SSE 和基于命令的连接方式，随着生态系统的发展，预计 MCP Server 的应用将会进一步扩大。

同时，新一波 MCP 市场和服务器托管解决方案正在涌现，开发者可以更容易发现、共享和贡献新的 MCP Server。且随着 MCP 的普及，基础设施和工具将在提升整个生态系统的可扩展性、可靠性和可访问性等方面发挥关键作用。

综上所述，我们认为，在 MCP 生态之下，创业公司的机会主要有三个，分别是：

• **Agent OS**

**这个方向既是 Anthropic 的机会，也是今天所有大公司和创业公司的必争之地。**现在大量 MCP Server 的这一层其实可以被统一抽象成一个 Agent OS，使得在这里获得的 Context 和 tool use 能以更自然的形式进行分发和交互。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**•** **MCP Infra**

MCP Infra **最核心的目标是让 MCP 更可靠、更 production ready，关键是让 MCP 更 scalable。**

今天的 MCP 其实并不好放到 Server 上做分布式计算，很多时候还是比较适合 offline 部署。要实现这点，需要把 MCP 设计变成一个无状态协议（Stateless protocol）。

其他可以让 MCP 更 scalable 的做法还有：

1\. 支持托管与多租户，支持多用户共享服务器，同时满足企业自建需求，实现数据与控制层隔离，

2\. 当前缺乏统一的远程认证方式，改进认证可促进 MCP 的广泛应用，

3\. 目前仅支持会话级访问控制，未来可以细化权限管理，

4\. 统一网关可增强身份认证、授权、流量管理和工具选择，提升多租户环境的安全性，

5\. 目前 MCP Server 配置仍依赖手动操作，未来可以进一步优化集成体验，

6\. 目前 MCP 缺乏内置工作流管理，需要简化开发流程，

7\. 实现标准化客户端体验，统一工具选择、调用方式及用户交互，

8\. 目前 MCP Server 兼容性差，可以改进调试工具来简化开发与部署。

**•** **MCP Marketplace**

如今 MCP Server 已经增长到 2000+，开发质量也会有参差。怎么让 Agent 根据相应速度、成本和相关性等因素选到更好的产品，可能需要一个类似 App store 那样的双边平台。

例如，Cline 是一款开源的 VSCode 插件，具有 AI Coding 功能。Cline 在 2 月发布了 Cline's MCP Marketplace，定位于 MCP Server 集合，目的是简化发现和安装的过程。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在这个 MCP Marketplace 中，用户可以：

1\. 浏览官方及社区创建的 MCP Server；

2\. 按名称、类别、标签等进行搜索；

3\. 一键安装 MCP Server，Cline 会自动完成配置等工作。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

排版：杨乐乐

延伸阅读

Flagship 创始人：AI for Science 的下一步是 Multi-Agent

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Lovable：3 个月 ARR 破 1700 万美元，付费用户留存超过 ChatGPT

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

从 R1 到 Sonnet 3.7，Reasoning Model 首轮竞赛中有哪些关键信号？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxBaTiazNtoZc250YeTbVDtJialC6iasIKYHRYQwkPOu0bsUQibbcNjcWKiaAm8luPUSGroSFiagkYh86Yg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=30)

Deep Research 团队：Agent 的终极形态是所有任务 All-in-one

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxBaTiazNtoZc250YeTbVDtJialC6iasIKYHRYQwkPOu0bsUQibbcNjcWKiaAm8luPUSGroSFiagkYh86Yg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=32)

OpenAI 都在用的 AI 招聘，2 年内实现 7500 万美元 ARR

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxBaTiazNtoZc250YeTbVDtJialC6iasIKYHRYQwkPOu0bsUQibbcNjcWKiaAm8luPUSGroSFiagkYh86Yg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=34)