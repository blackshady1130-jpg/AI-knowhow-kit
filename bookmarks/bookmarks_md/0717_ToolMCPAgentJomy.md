---
url: https://mp.weixin.qq.com/s/ZZBs2iL9G9bJx37oZkMlAg
title: "聊一聊 Tool、MCP 和 Agent 来龙去脉 | 大白话技术科普系列@Jomy"
description: "Agent 生态的爆发，可能来得比大多数人想象中还要快。"
author: "Jomy"
captured_at: "2026-03-08T13:03:51.926Z"
---

# 聊一聊 Tool、MCP 和 Agent 来龙去脉 | 大白话技术科普系列@Jomy

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/dqVy90DEgE2tk4M8r3L2CGeRJDnuh8JFBQgmREszpgdQ9EHqT1F9dxH65JrLWdIhQOSHkoJ8OTMncubTOur7hA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

将与 Jomy 共同完成一系列技术科普，让最一线的工程师、用通俗的语言、讲最前沿的技术。

这是系列第一篇，主题是最近大火的 MCP 和 Agent。

读完本文，你一定会感叹：终于搞懂了！原来！竟然！这么简单！

文 | Jomy @302.AI

编 | 南乔River @ShowMeAI

✦✦✦

我们 302.AI 做 MCP 和 Agent 相关开发有一段时间了，期间一直与开发者和用户们保持着密切的交流。

有一个普遍的感受：尽管行业内几乎所有人都听过 MCP、Agent 这些术语，但只有极少数人真正理解它们的本质。

今天，我就基于 302.AI 的实践和成果，分享一些自己的见解，帮大家厘清概念的来龙去脉，并大胆预测一下未来的发展方向。

## 1. 缸中之脑

## 只能说不能做的大模型

让我们先从大语言模型（Large Language Model，LLM）说起。

大语言模型，顾名思义，就是一个只能处理和输出文字的系统。

早期的大语言模型，输出非常不稳定，准确率很低，经常「一本正经地胡说八道」。

所以，人们最多把它当成一个顾问：咨询意见，但不敢让它直接拍板决策或上手干活。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这个时期的大模型，有点像被限制在「缸」里的「大脑」（借用哲学上的「缸中之脑」假说）。

它能思考、能滔滔不绝地输出观点。但它没手没脚，不能对「缸」外的物理世界/数字世界直接做点什么。

✦✦✦

但是，AI 技术发展飞快。

随着模型参数规模的扩大和训练方法的革新，语言模型的「智力」得到了肉眼可见的提升。人们惊喜地发现，AI 写出的文案、给到的建议、生成的代码，几乎不需要修改就能直接使用了！

眼看着 AI 越来越靠谱，一种想法自然而然地浮现出来：既然大模型这么能干，是时候解开 AI 的禁锢，让它不只能「动动嘴」，也能「动动手」了？

## 2. 调用工具

## 大模型学会了「动手」

怎么解开 AI 的「禁锢」呢？

答案就是让大模型能够自行使用工具，也就是我们常说的 Function Call（函数调用）或 Tool Use（工具使用）。

那么，一个只会输出文字的模型，是如何调用工具的呢？

这里需要做一个必要的澄清：模型调用工具，并不是模型真的「动手」去操作工具。

本质上，还是模型生成文本（结构化的文本），然后配套的程序接收到指令，再去调用工具。（如下图所示）

而所谓的「工具」，就是各种各样的程序接口（API）或者软件操作，例如搜索、编辑数据库、编辑文件等。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

gpt-4o 调用工具的命令（JSON 格式）

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这就像给一个思维敏捷但行动不便的人，配备了一台随时待命的智能计算机。

他只需要「说」出来需要做什么，计算机就会自动决策和执行所有的指令，整个过程不再需要人类的介入。

✦✦✦

让 AI 模型使用工具，本质上是一种「放权」行为。

人们将 AI 从「缸」里释放出来，允许 AI 通过调用工具，直接对现实世界或数字世界产生实际的影响。

这无疑是 AI 迈出的关键一步，也是 Agent 得以诞生的基石。

## 3. MCP 诞生

## 不再重复造轮子

AI 学会了使用工具，这很好。

但很快就出现了新问题：每家公司、每个开发者都在用自己的方式定义和接入工具。这就导致了大量的重复劳动，并且工具难以复用和共享，只能「自己造自己用」。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

MCP 统一了模型调用工具的方式

Anthropic 公司敏锐地发现了这个问题。他们认为，工具应该有一套通用的「语言」和「接口规范」，于是提出了 MCP（Model Context Protocol，模型上下文协议）。

这个协议对大模型发展的意义重大，完全可以类比为秦始皇当年规定的「书同文」和「车同轨」。从此，模型调用工具这个事情就被大大地加速了。

✦✦✦

MCP 是什么呢？

简单来说，它是一套定义大模型如何发现、理解和调用外部工具（或称服务）的标准协议。

（MCP 中的 Prompt 和 Resource 暂且不论）

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

MCP 基本框架示意图

它明确了两个核心角色：

-   MCP Client（客户端）： 通常是使用工具的一方。一般是 AI 应用，比如 Claude 客户端、Cursor 编程工具等。
-   MCP Server（服务端）： 也就是提供工具的一方。任何拥有 API 或软件服务的公司，都可以按照 MCP 规范把自己包装成一个 MCP Server，把原来给人用的工具，改造成能让 AI 理解和调用的工具。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Norah Sakal 这张「MCP architecture」图非常出圈，说的是同一回事

✦✦✦

前段时间，海外知名投资机构 a16z 制作了一份 MCP Market Map，梳理了 MCP 发展现状。

可以看到，MCP Client 和 MCP Server 生态已经初具模型并在日益繁荣。（如下图所示）

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

MCP 生态现状

其中，在 MCP Marketplace 板块，MCP.so 导航网站的制作者，就是国内知名的独立开发者 idoubi。

目前，MCP.so 收录的 MCP Server 数量已经超过了 7000 个，其中就包括 302.ai 的 Sandbox MCP Server 和 Browser MCP Server。

用户只需要在客户端连接这两个 MCP Server，就可以让 AI 对远程 Linux 服务器和远程浏览器进行操作，完成相应的任务，极其便利。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

mcp.so 主页截图

## 4. Agent 诞生

## 更好地调用工具

MCP 让工具的供给变得更加方便了。

但新的挑战接踵而至：一个 AI 模型能有效掌握和使用的工具数量是有限的。就像一个人能熟练掌握和使用的技能，也是有限的。

在人类社会里，每个人都专注于擅长的领域，以医生、律师、教师、工程师、程序员等职业身份，把自己的事情做好。

AI 也是同理。

当工具不再是主要瓶颈后，如何让 AI 模型更聪明、更高效地使用这些工具，就成了核心问题。

Agent 就在这个背景下诞生了。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Agent 最简公式

我认为，理解 Agent 最简单的一个公式就是

Agent = LLM + Tools

有工具使用权限的 AI 就是 Agent，中文翻译成「代理人」，有些地方会翻译为「智能体」。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Agent 最简单的实现框架

现在，对于 Agent 的发展，业界有两个大的方向：

-   通用 Agent（通才）：很多大模型公司都在往这个方向努力。但现阶段，受限于模型能力等各方面的挑战，这注定暂时只是一个美好的理想。
-   垂直 Agent（专才）： 专注于解决特定领域或特定类型任务。目前看来更容易落地、也更有可能在短期内产生实际价值。

✦✦✦

在垂直 Agent 优化实践中，我们有几条关键经验，也在此分享给大家：

-   明确的指引。在实践中体现为精准的系统提示词。
-   垂直的工具。在实践中体现为只接入任务强相关的 MCP Server。
-   完整的上下文。在实践中体现为完善的任务描述和任务记忆。

读到这里，你就已经追到了 AI Agent 领域发展的最前沿。

## 5. Agent 通信

## 新的协议应运而生

然后，更新的挑战又出现了。

单个垂直 Agent 能解决特定问题，但面对更复杂的现实任务，往往需要多个不同能力的垂直 Agent 协同配合。

现在，各家公司都在闭门造自己的 Agent。这些 Agent 之间缺乏统一的沟通方式和协作机制，注定重复且低效。

这有点像 MCP 出现之前的工具生态，又一次走到了需要「标准化」的路口，只不过这次标准化的对象是 Agent 本身。

✦✦✦

为了解决 Agent 之间的信息互通问题，一些新的协议开始进入起草阶段，其中比较受关注的有：

-   ANP（Agent Network Protocol）：中国开发者率先提出并推动的一个协议。
-   A2A（Agent-to-Agent）Protocol：Google 也在探索类似的概念和协议。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Google A2A Protocol 原理示意图

这些协议的核心目标，大致可以归纳为两点：

-   第一，让 Agent 之间明确彼此的能力，便于协作。就像外包网站的个人主页，清晰写明自己的专长，其他人可以按需查找，找到合适了的人就一起做项目。
-   第二，让 Agent 之间可以高效地传递信息。就像团队协作之前，大家约定好沟通方式（比如人会约定好用飞书还是用钉钉）以及消息格式（类似布置任务需要包含哪些信息）。

至于未来哪个协议会成为主流，现在下结论还为时尚早。

但可以肯定的是，Agent 之间的互联互通，将进一步释放 AI 潜能，催生一个更加靠近 C 端（用户端）、更加繁荣、更加有想象力的巨大市场。

## 6. 展望

## 2025 Agent 之年的无限机遇

最后，让我们来系统回顾一下这条演进路径：

-   随着大模型能力的提升，AI 输出的内容越来越靠谱。人们开始让 AI 通过调用工具与外部世界直接交互，把 AI 变成了 Agent。
-   MCP 协议统一了工具的开发标准，从而简化了 Agent 的开发难度。
-   现阶段单个 Agent 无法很好地使用大量工具，所以垂直 Agent 成为了当前的主流。
-   垂直 Agent 之间需要配合才可以完成复杂的任务，这催生了 ANP / A2A 等新的互联协议。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

你看，技术的发展往往不是一蹴而就的。

每个重大节点（Function Call/Tool Use、Agent、MCP、ANP/A2A）的出现，背后都有其历史必然性。

✦✦✦

再往后呢？

考虑到当前基础模型的发展速度和架构特点，我认为，垂直 Agent 市场将会在历史舞台上存在相当长的一段时间。

即使未来出现了能力极强的「超级通用 Agent」，在很多场景下，高度优化、成本可控的垂直 Agent 组合，可能仍然是更具性价比、更可靠的选择。

恰似古语有云：三个臭皮匠，顶一个诸葛亮。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Agent 生态的爆发，可能来得比大多数人想象中还要快。

2025 是名副其实的 Agent 之年。这背后蕴藏着的，是巨大的技术变革和商业机会，以及我们这代人几十年才得一遇的科技浪潮。

衷心希望我今天的分享，能帮你更好地理解这个正在发生的未来。也希望每一位在这个领域努力探索的朋友，都能抓住机遇，在今年摘取到属于自己的胜利果实。

## 官方网站

-   302.AI: https://302.ai
-   MCP.so: https://mcp.so
-   Anthropic | Introducing the Model Context Protocol: https://www.anthropic.com/news/model-context-protocol
-   Anthropic | Model Context Protocol: https://modelcontextprotocol.io/introduction
-   ANP | Agent Network Protocol: https://agent-network-protocol.com
-   ANP | AgentNetworkProtocol: https://github.com/agent-network-protocol/AgentNetworkProtocol
-   A2A | A2A Protocol: https://google.github.io/A2A
-   A2A | Agent2Agent Protocol: https://github.com/google/A2A

## 推荐阅读

-   Norah Sakal | What is Model Context Protocol (MCP)? How it simplifies AI integrations compared to APIs: https://norahsakal.com/blog/mcp-vs-api-model-context-protocol-explained
-   a16z | A Deep Dive Into MCP and the Future of AI Tooling: https://a16z.com/a-deep-dive-into-mcp-and-the-future-of-ai-tooling
-   What is Model Context Protocol (MCP): Explained: https://composio.dev/blog/what-is-model-context-protocol-mcp-explained
-   What Is the Model Context Protocol (MCP) and How It Works: https://www.descope.com/learn/post/mcp#llm-isolation-&-the-nxm-problem
-   常高伟 | 多角度全面对比Google最新的A2A、ANP、MCP: https://mp.weixin.qq.com/s/n1R-wOtNBTKtHdIHOUhQmw
-   idoubi | 详解 MCP 核心架构: https://mp.weixin.qq.com/s/uTsr06MnJ9t3sGDzLD99\_g

Powered by [带带弟弟排版器](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247492726&idx=1&sn=6b6a2fa52bacc443484f0b014c4cbf23&scene=21#wechat_redirect)