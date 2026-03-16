---
url: https://mp.weixin.qq.com/s/l59PXZgWWXWiovFG92WPRQ
title: "OpenAI：computer use 处于 GPT-2 阶段，模型公司的使命是让 agent 产品化"
description: "Agent 下一步是能够自主判断并调用数百个工具"
author: "拾象"
captured_at: "2026-03-08T13:05:36.220Z"
---

# OpenAI：computer use 处于 GPT-2 阶段，模型公司的使命是让 agent 产品化

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxib2dNICCpDd8HafMjdmiajcnYZ3vaTdhBw494KWRyp3fViaLAotSLkV9wVLnIPNicTOCDfZmQp3cNeA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxib2dNICCpDd8HafMjdmiajcuHfY5giaTaC64WiarsWrOGmCqu9xXT8gqt6QjP0DgQxU4vrLdYSoUq5Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

编译：haozhen, Cookie

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxib2dNICCpDd8HafMjdmiajcmM3LMP7wVChBuurs5O1j2UNpagrahq0LU9WsN5NJmaiahM5L6GB3hoQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

AI agent 并不是一个新概念，但从 2024 年到今天，agent 的行动能力和交互方式发生了质变，头部模型厂商也正在将 agentic 能力融入模型，agentic 能力会成为今年模型竞赛的重点之一， tool use 作为 agent 最重要的能力，一直是头部 AI labs 非常关注的方向。上周，OpenAI 发布了新一代模型 o3，o3 有最丰富的 tool use 方式。

本文是对 OpenAI agent 团队访谈的编译，OpenAI agent 产品和工程负责人分享了 OpenAI 在 agent 开发与工具生态方面的技术细节，以及他们对开发者实践的观察与见解。他们认为，受益于 CoT 与 tool use 的结合，agent 获取信息的方式已经发生了巨变，agent 的下一步是能够接入数百个工具，并能够自主判断调用哪个工具并确定如何使用。此外，multi agent 系统的工作效率会更高，且具有更高的可控性和优化潜力。

我们判断， multi agent 系统会在今年有大的突破，vertical agent 会因此直接受益，在 computer use 会带来范式创新的背景下，Virtual Machine 将可能是潜在创业机会。

💡 目录 💡

   tl;dr

   01 Agent 未来的交互方式是什么?

   02 AI Fine-Tuning 会发挥什么作用

   03 Computer Use 的应用场景

   04 开发者实践 insight

   05 对 AI 模型的看法

**tl;dr**

**•** **2025 年是 agent 发生重大变化的一年，agent 获取信息的方式和工作流上已经发生变化**

**首先，在信息获取方式上，agent 已经**从 2024 年的单次搜索决策模式，转变为像 Deep Research 这样完全自主的产品，能从网络获取信息、思考内容、重新评估立场，并且同时打开多个网页来节省时间。

未来几个月可能会有许多 agent 出现在公共互联网上，agent 将会接触到更多互联网实时数据，而不仅仅是用户提供的有限 context，这对开发者思考如何整合和使用 API 来说非常重要。

**其次，在工作流上，**去年大多数 agent 有非常固定的工作流，但得益于 CoT 和 tool use 的结合，今年 agent 在推理过程中已经足够智能，能够自己决定如何调用多个工具，如果发现方向不对还能及时调整。

OpenAI 判断 agent 可调用的工具数量将会在几个月内从目前的 10 个量级 Scale 到 100 个量级。

**• multi agent 系统具备更高的可控性和优化潜力**

OpenAI Agents SDK 实现的一个重要设计理念就是将一个任务分拆成多个子任务，分别给多个 agent 处理，每个 agent 专注于完成特定子任务，这样整体工作效率会大大提升。并且，如果一个 agent 同时处理 100 个任务，稍微改动几个 prompt 可能就会导致结果完全不同，但分工之后，每个 agent 的修改和调试就会更加独立。

在 multi-agent 系统下，vertical agent 会直接受益。

**• 开发者需要构建 agent 的评估微调飞轮**

基于强化微调能力，开发者能够构建自己领域的评估器，让模型找到解决特定领域问题的正确 tool use 路径。目前还没有看到任何东西能够完美地在特定领域实现产品化的评分和任务生成，这可能 2 年内最需要解决的问题。

评估器不只是简单地比对两个字符串是否相等，而是能够将模型输出与权威资料进行对比 ，或者通过执行代码来验证数学正确性。

**• Computer Use 带来范式创新**

Computer Use 目前仍处在早期阶段，Computer Use VM（虚拟机）需要开发者来填补空白，未来可能会有基于不同操作系统生态的 VM，比如专门做 iPhone VM 的公司，就像之前有公司专门做 iOS 测试框架一样，只不过今天的 VM 是为模型服务。 

**01.**

**Agent 未来的交互方式**

**是什么?**

**Q：****未来 5 到 10 年里，用户和 agent 将如何交互？**

**Nikunj：**目前，用户与产品的交互方式主要是用户主动进入 ChatGPT、Deep Research、Operator 等特定的界面进行使用。但随着底层模型和 API 的开放，agent 将逐渐融入更多产品之中。

例如，computer use agent 可能会直接集成到浏览器里，Operator 可能会直接自动化日常工作中的重复性任务，比如点击、填表和搜索信息等。**Agent 将越来越深入地融入各种日常产品之中，而这正是我们构建 API 平台的目的——让 agent 无处不在。**

**Steve：**在 API 平台工作的一大乐趣是，我们无法预测人们会用它来做什么，因为这个生态系统非常垂直。我们可以大致知道用户会如何使用 ChatGPT，但在 API 领域，开发者对自己的业务场景比我们了解得更深，会创造出超出我们想象的应用。

**Q：****你们最期待哪种 agent？**

**Nikunj：**我最想要一个 API 设计助手，我们在 API 设计上花了太多时间，每次都要反复讨论每个参数的命名。我希望有一个 agent 能深入研究 API 设计案例，并给出好的建议。

**Steve：**甚至这个 agent 可以用来微调所有的 API 设计。

**Q：****目前 agent 还处于发展的早期阶段，agent 访问网络和相互交流的方式仍然是基于过去的技术范式。有人设想过未来可以让 agent 彼此交流，有一个爆火的 demo 展示了一个场景：当两个 agent 意识到彼此都是 AI 的时候，就选择切换到了更高效的通信方式。你们是如何看待这一趋势的？**

💡

上述 demo 名为 GibberLink，是两位 Meta 的软件工程师在一场 hackathon 比赛中创作而成，这个比赛由 ElevenLabs 和 Andreessen Horowitz 主办。GibberLink 能让一个 AI agent 在通话时识别出对方是否也是 AI，一旦确认通话双方都是 AI，GibberLink 就会提示它们切换到 GGWave 这种更高效的通信方式。

**Nikunj：**Agent 获取信息的方式已经有了巨大的变化，在 2024 年，agent 一般只能进行单轮交互，比如决定是否要搜索网络，从网络获取信息，并总结成一个回复。

2025 年出现了 Deep Research 这样的产品，**agent 不仅仅是从网络获取信息，而且会思考自己获得的内容，并再次搜索新信息，甚至同时打开多个网页从而节省时间。**chain of thought 与 tool use 的结合，使得 agent 在推理过程中调用外部工具的方式发生了很大的转变。

**未来，agent 会取代部分网页数据提取的工作，**而且这些 agent 可能不需要知道自己正在与另一个 agent 交互，它们只是像调用接口一样，从对方获取有价值的信息，并利用这些信息做出决策、回溯或采取完全不同的行动。这一趋势将在未来几个月内快速发展，并无缝嵌入到 agent 的 CoT 中，使得 agent 能够在互联网以及私有数据和私有 agent 之间自由调用工具。

**Q：****各大公司是应该等待 agent 自动访问它们的网站，还是应该主动构建自己的 agent，从而能够与消费者的 agent 更轻松地交互？**

**Nikunj：****我们发布 Agents SDK 就是因为人们正在创建 multi agent 协作系统，利用多个 agent 来解决各种商业问题。**比如在客户服务上，可能会有一个 agent 专门处理退款，另一个 agent 负责账单和物流信息，还有一个 agent 决定是调用 FAQ 还是升级到人工。**multi agent 架构已经非常流行，OpenAI 的目标就是让开发者更容易构建 multi agent 架构。**

何时将 agent 连接到公共互联网，以及如何让它们真正发挥作用，会是一个非常有趣的发展方向。目前，我们还没有看到太多这样的案例，但这一定会发生，只是时间问题。

**建议各大公司可以先在内部构建 agent ，来解决当下企业面临的实际问题。如果某一天发现需要将这些 agent 开放给互联网，并让外部 agent 与之交互的时候，就可以直接开放。**这个时间点也许就在接下来的几个月内。

Steve：有趣的是，**以往模型获取的数据主要来自用户自己的数据，比如聊天记录、文件搜索等。但随着 agent 越来越多地连接到互联网，**更多的输入数据来自整个网络，这将带来深远的影响。

**Q：****怎么判断 agent 在哪些场景下适用，哪些场景下不适用？**

**Nikunj：**我们首先回顾一下 agent 发展历程。2024 年的时候，大多数 agent 的工作方式都是一个非常清晰、提前定义好的工作流，通常涉及不到 10 个工具，最多十几个工具。这种方式是高度编排的，从一个步骤到另一个步骤都经过了精心设计。许多公司基于这种模式开发了一系列出色的 agent ，比如代码生成 agent 、客户支持 agent 、Deep Research 等。

**2025 年已经进入了一种新的模式：agent 会在 CoT 框架下进行推理。模型在思考过程中变得足够智能，能够自行决定何时调用多个工具，并在发现做错时会及时调整方向，尝试其他方法**，agent 已经逐渐摆脱了完全确定的工作流。OpenAI 也在开发 RL 和 Fine-Tuning 等工具，让开发者能够更灵活地利用这些工具。

**Agent 下一步的发展方向是如何突破目前 10-15 个工具的限制，即如何让 agent 接入数百个工具，并能够自主判断调用哪个工具、如何使用它们。**这将是一个真正的飞跃。

当 agent 拥有足够的算力，能够推理不同的工具调用路径，并且可以访问大量工具时，就具备了真正的“超级能力”。**消除工具数量的限制是未来几个月最期待的事情之一。**不过，以当前的模型水平，这仍然是一个挑战，但这种情况会很快改变。

**Steve ：**还有一个关键因素是需要提升 [agent 的运行时间](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247512305&idx=1&sn=307f2ebde8ee40d2d13e621230d6fcfe&scene=21#wechat_redirect)来完成更复杂的任务。人类可以花上一整天来解决问题，并随意使用各种工具。而目前许多 agent（尤其是 Deep Research 类的 agent）的运行时间通常在几分钟内。**如果能让 agent 的运行时间从分钟扩展到小时甚至天，它们将能发挥出更强大的能力，解决更复杂的问题。**

**02.**

**AI Fine-Tuning 会发挥什么作用？**

**Q：****2024 年的时候，agent 实践需要有非常严格的限制和紧密衔接的流程，否则很容易失控，但现在似乎允许模型更加自由地发挥了，最终的理想状态是模型能够自由探索。人类给模型提供数百种适用于各种任务的工具，模型自己去寻找最佳解决方案。**

**Nikunj：**我们可以期待下一代模型能否具备更强的泛化能力，覆盖开发者可能遇到的各类用例。**现在有一种强化微调的方法，让模型在特定任务上进行训练，并通过评分器进行评估。**如果开发者能够创建自己的任务和评分器，让模型学会如何找到正确的路径，即调用正确的工具来解决特定领域的问题，那将是非常有价值的。

我对即将推出的新一代模型非常期待。早期结果显示，强化微调的效果很好，这些技术结合在一起后，可以让 agent 真正发挥作用。

**Steve：****强化微调实际上是在引导模型的 CoT，并教会它如何理解特定领域的知识。这种训练方式类似于让模型接受一门专业教育，比如如何像法律学者一样思考，或像医生一样做出诊断，**就像人类接受大学四年的教育来培养思维模式一样。

强化微调是一个非常好的方式，将推动模型在特定行业的深入应用，实现更专业化的能力提升。

**Q：****在基础架构层面，应该如何为法律、医疗等专业领域的 Fine-Tuning 开发者提供合适的工具？**

**Steve：**这仍然是一个正在推进的工作。目前提供的工具主要是允许开发者构建自己的评分器。假设有一个医疗任务，而某个模型的表现只有 50% 的准确率，你可以通过创建评分器来评估模型的推理过程，并与医学教科书之类的已知标准答案进行交叉比对。在 Fine-Tuning 过程中，你可以逐步引导模型向更高质量的答案收敛。

**目前提供的主要是基础工具，尤其是高度灵活的评分器，允许开发者用模型的输出与某种“真实标准”进行比对，或者运行代码来验证是否数学上正确，**数学上正确不仅仅是简单的字符串匹配，而是确保在数学或逻辑上是严谨的。这是我们正在探索的方向。

**Q：****目前 AI 领域的一个核心问题是到底什么是可以被评分的。在医疗和法律领域，有人批评某些评估方法过于简单，比如通过律师资格考试并不等于成为一名真正的律师，通过医学考试也不意味着能胜任医生的工作。有没有什么新方法可以更有效地确定评分机制？**

**Nikunj：**目前这确实是一个挑战，需要大量的尝试。市面上还没有真正成熟的产品能够完美适用于不同的领域。**如何构建高质量的任务和评分器，可能会成为今年甚至明年的一个重要课题。**

我们已经看到了一些可行的产品方向，比如 Deep Research，甚至网上也出现了一些类似的尝试。关键问题在于，如何产品化才能使得更多人能够轻松使用。

**03.**

**Computer Use 的**

**应用场景**

**Q：****如何确认哪些场景适用于 computer use？**

**Nikunj：**最初我们以为 computer use 的主要应用场景是在那些没有 API 的传统软件系统中，许多企业一直希望能自动化这些流程，但始终找不到合适的方法。现在，一些医疗行业的客户在尝试使用 computer use 来自动化繁琐的手工操作，比如在多个应用之间切换、点击等。

还有企业把 computer use 用在 Google Maps 上。Unify GTM 曾使用 computer use 来分析充电网络的扩展情况，agent 打开 Google Maps，进入街景模式，来查看某个地区是否新增了充电桩。虽然 Google Maps 有 API，但街景模式可能并不容易通过 API 访问，尤其是确定具体的查看角度。因此，这类任务的自动化非常有价值。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Steve：**许多数据并不能简单地用 JSON 形式表示，也无法通过普通的 Web API 获取。因此结合视觉和文本理解能力的 AI agent 在这些领域会很有用。

**Q：****从发布了 agent 这套工具以来，有哪些有趣的应用场景吗？**

**Nikunj：**在 Alpha 版本发布之后，computer use 相关的应用最让人兴奋。除了 Web 搜索、文件搜索等较为成熟的技术外，computer use 领域仍然处于早期阶段，很多企业希望能将软件部署到云端的虚拟机（Virtual Machine）中，并通过 agent 实现自动化操作。

“Computer Use VM” 指计算机使用虚拟机（Virtual Machine，简称 VM）技术，即在计算机上通过软件模拟出具有完整硬件系统功能的、运行在一个隔离环境中的虚拟计算机系统。

我特别关注平台型公司的应用，比如 [Browserbase](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247512241&idx=1&sn=a2a3fe33f7b0038afd75f4d948d42c5f&scene=21#wechat_redirect) 开发了基于浏览器的服务，YC 初创公司 Scrapybara 提供了一种开发者体验极佳的 computer use 模型托管服务。我很期待看到未来会有哪些创新应用构建在这类平台之上。

[BrowserBase](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247512241&idx=1&sn=a2a3fe33f7b0038afd75f4d948d42c5f&scene=21#wechat_redirect) 成立于 2023 年成立，聚焦浏览器自动化场景（如网页渲染、UI 测试、数据采集前置处理），提供与虚拟机环境深度兼容的轻量化运行框架。

Scrapybara 为 computer use agent 提供远程桌面托管，通过 Scrapybara 统一的 API，开发者只需一行代码即可使用任意模型执行 agent，并访问浏览器、文件系统和代码沙箱等底层控制。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Steve：**Arc 开发了一款工具，允许用户在浏览器中打开一个新标签页，并输入指令，agent 在后台执行任务。这种深度集成的方式非常有意思，agent 不仅仅是一个独立的插件，而是成为浏览器本身的一部分，这个项目称为 Dia。

Arc 浏览器开发公司 The Browser Company 在 2024 年 12 月宣布推出新型浏览器 Dia，将提供个性化的 AI 工具，比如智能建议、自动浏览，目的是简化网页任务和工作流程。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**04.**

**开发者实践 insight**

**Q：****目前，高级开发者是否仍在使用 API？他们是怎么使用这些 agent 开发工具的？**

**Nikun：**这些 agent 开发工具目前还处在相当早期的阶段。在 Alpha 阶段，有些用户会先尝试让模型和工具协同完成任务。如果效果不理想，他们会不断调整 prompt，直到找到合适的解决方法。最终，他们通常会将这一部分加入到整体工作流中，比如将网络搜索作为其中一个步骤，用来获取信息，然后再传递给后续的确定性流程，或者传递给另一个 LLM 进行处理。总体来说这一切都还很早，未来几周会发现更多这方面的模式。

**Steve：**我们在 Agents SDK 中推出了这样一个理念：**将一个任务分拆成多个任务，让多个不同的 agent 分别处理。就像单核计算机 VS 多核计算机，每个 agent 专注于完成一个特定任务，并且拥有完整的 context，整体工作效率会大大提升。**

**如果让一个 agent 同时处理 100 个任务，稍微改动几个词就可能导致结果截然不同。但分工之后，每个 agent 的修改和调试就会更加独立、风险也更低。**

**Q：****怎么看待围绕模型构建产品，这些产品是会随着模型能力的进步被淘汰，还是产品本身仍然会有价值？**

**Nikunj：**Agent 以及工具协同调度是目前最重要的部分。模型本身的能力远远超出了目前大多数 AI 应用所能利用的范畴。**通过围绕模型构建一些结构化的工作流，从而使模型更好地发挥作用，这是 AI 初创公司和产品需要重点关注的方向。**

比如客户支持自动化，虽然这个概念已经存在了一段时间，但在 2023 年末到 2024 年初，只有少数几家公司做得比较好，大多数公司的进展都很慢，这说明精心设计工作流、仔细调试 prompt、建立评估集以防止提示效果衰减等工作是非常重要的。

现阶段，如何让这些模型真正发挥作用，是大家应该关注的重点。

Steve：**把任务分解，让多个 agent 来处理，也大大简化了整个工作流的调试过程。**假如有一个功能强大的模型，并且要执行 100 个指令，一旦改动几个 prompt，输出的结果可能就完全不同了。但如果把任务分成一个个小 agent，比如先有一个分诊 agent，再有一个转交 agent，那么对每个部分的微调就可以更加独立，出错的影响范围会更小。

**Q：****如何看待“让 API 易于上手”与“提供高度可定制性”之间的平衡？**

**Steve：****“阶梯式 A**PI ”（API as ladders）是我们在设计 Responses API 坚持的首要原则之一，核心在于几个方面：首先，我们希望做到开箱即用；其次，我们希望让简单的操作变得更加容易；此外，我们希望用户投入的每一点努力都能获得相应的回报。****

比如向量搜索的默认使用方式非常简单，只需要上传一些文档，甚至不必通过 API 进行操作，就可以直接在网站上完成，只需要输入向量 ID，它就能正常运行。但如果默认配置无法满足需求，那可以进一步调整，例如可以修改分块大小，默认是 400，可以改为 200 或 1000。这些参数有合理的默认值，但如果想优化搜索效果，就可以手动调整。

再比如文件结构，可以使用元数据过滤、自定义排序等。这些功能并不是强制性的，而是逐步开放的。我们会在文档中提供这些选项，但对于初次使用 API 的开发者来说，他们不需要一开始就理解自定义排序是什么。

**OpenAI 的目标是尽可能简化入门门槛。**比如，在调用 API 时，我们花了大量时间优化“快速入门”示例，最终将代码精简到只需 4 行 Python 代码。我们对这个目标非常执着，调用 API 应该如此简单。与此同时，我们也提供 50 多个可配置参数，用户可以自由调整，而这些参数都有合理的默认值。

**Q：****未来想添加哪些新功能？**

**Nikunj：**对于 Web 搜索工具，希望增加站点过滤功能，这是用户强烈要求的。目前这个工具只能搜索整个互联网，或者通过 prompt 来引导搜索。

**Steve：**还有位置筛选，现在的工具可以设置搜索的城市或国家，未来希望精确到街区甚至更小的范围，对天气查询、活动搜索等场景来说非常重要。

**Nikunj：****我们希望将 Assistants API 中的功能整合到 Responses API 里，但不强制用户使用。Assistants API 在 2023 年 11 月发布，支持存储对话、模型配置等功能，但上手门槛较高。**

**而 Responses API 采用相反的策略，用户可以从一个简单的 API 调用开始，**如果想存储对话，可以选择使用 Threads Object，如果想存储模型配置，可以选择 Assistant Object。这些功能都是可选的，用户可以按需启用，不必一开始就被复杂的配置所束缚。这是我们短期内非常希望实现的优化方向。

**Q：****回顾之前发布的 API，有哪些地方做得很好？又有哪些地方没有达到预期？**

**Steve：****在 Assistants API 上做得特别好的一点是 tool use，**有大量的用户使用这个功能，尤其是文件搜索工具，这是 API 真正找到了市场契合点的地方——用户希望将自己的数据接入 API，并让模型在这些数据上进行搜索。

**做得不够好的地方主要是使用门槛太高了。**用户无法选择是否存储 context，很多人不喜欢自动存储 context，更倾向于使用类似 Chat Completions API 的方式，在每次调用模型时自己提供 context。但 Chat Completions API 也是有局限性的，它只能输出一个结果，而模型其实能做很多事情。因此，我们希望模型能在后台执行多个任务，并将所有计算和推理的结果返回给用户。

所以，我们在新的 API 设计中，尝试结合 Assistants API 的优势，比如 tool use、多重输出等，同时也融入 Chat Completions API 的易用性，以提供更好的开发者体验。

**Q：****开发者在使用这一整套开发工具时，应该如何理解它们之间不同的作用？以及它们在 [MCP](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247511799&idx=1&sn=c063b0da3fcbfd309d1d6294f58bbc72&scene=21#wechat_redirect) 生态中的定位是什么？**

**Nikunj：**这些工具实际上是在解决不同的问题。例如，Responses API 主要是为了优化模型的多轮交互体验，我们提供了一种基础机制，使模型能够多次调用自身，同时也可以多次调用工具，最终得到一个完整的答案。

MCP 主要关注的是如何让模型使用工具，将工具集成到模型中。从某种意义上来说，这两者是互补的。我们仍在探索如何更好地完善生态系统，但 MCP 确实非常强大，我们接下来需要深入思考的问题就是如何将 MCP 更好地融入到我们的生态中。

**Q：****如何看待 AI infra 公司的发展前景？**

**Nikunj：**用户希望有一个一站式的解决方案，让 LLM 能够搜索数据、互联网，因此 OpenAI 正朝着这个方向发展，希望**构建用户所需的开箱即用的工具。**

**但我认为，未来依然会有许多垂直领域的 AI infra 公司。这些公司在构建底层、灵活性较高的 API 方面做得很好，这类 API 依然有很大的市场需求。**例如，有些公司专门为 AI coding 初创企业提供虚拟机，让他们能快速测试代码并释放资源，Runloop AI 就在做这件事。AI infra 的垂直化仍然是一个非常有意义的发展方向。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Steve：**有些事情并不是 OpenAI 想要直接涉足的，比如 AIOps（即智能运维，指应用 AI 来自动处理和简化 IT 服务管理和运营工作流程）。目前有一些 AIOps 公司在做非常有趣的事情，比如帮助开发者管理 Prompt、追踪 API 计费、分析使用情况等。这些服务并不属于传统的底层基础设施，但对于开发者来说依然非常重要。这些 AIOps 公司通常是跨模型、多供应商（multi-model，multi-provider），比如 OpenRouter。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Q：****如何看待目前仍然存在的问题，哪些是最需要解决的关键问题？**

**Nikunj：****工具开发是需要重点解决的问题。**我们已经有了 Responses API 作为基础模块，接下来需要在这上面构建工具生态系统。**MCP 在这方面做得非常好，我们需要思考如何在这个方向上进一步发展，这也是目前最重要的任务之一。**

Computer use 领域仍然处于初期发展阶段，这是另一个重要问题：**如何让企业能够安全、可靠地在自己的基础设施上部署虚拟机，并观察它们的运行，确保 computer use 模型的稳定性和效率。**

此外，我认为 computer use 模型会迅速变得非常强大，现在只是处于 GPT-1 或 2 的阶段，而这个范式的发展将会非常快速、有用。所以我对这一领域的基础设施将会如何发展感到非常好奇。

**Steve ：****在 Alpha 期间有一个让我印象深刻的点，就是人们希望在各种不同的环境中尝试 computer use。**虽然 computer use 模型在浏览器环境中表现最佳，因为这是模型的训练环境，但人们还在尝试在 iPhone 截图和 Android 设备中进行使用，这是之前我没有想到的。

所以未来人们的需求将是无限的。会不会有公司专门做 iPhone 虚拟机，或者，会不会有公司类似以前只做 iOS 测试框架的公司，来为 AI 模型提供类似的框架？不同版本的 Ubuntu 等操作系统的使用，本质上是一个巨大的碎片化问题，而社区如何填补空白会非常有趣。

**Nikunj：**还有创业公司在尝试用 computer use 做网络安全工作，来探测网站和系统中的漏洞，这个过程大约持续 30 分钟。

**Q：****在新模型上，有没有一些功能是你们非常期待的？**

**Nikunj：**很多 YC 初创公司总是说某些东西永远都不管用，我把这些公司提出的建议都保存了下来，每次有新东西出来时，我都会挑选 3-4 个建议进行测试。这些建议基本都集中在 agent tool use 方面，涉及到六七种比较简单的工具。**我特别关注这些工具在每次执行时的可靠性。我对下一代模型还是很乐观的，但确实有些 tool use 不太理想。**

**我还特别有更小、更快的模型，并且能够很好地处理这些 tool use 的场景。**有一些辅助模型支撑着像 o1 系列模型这样大型模型的生态，它们能做一些非常快速的分类、限流之类的工作，这类辅助模型还有很大的改进空间。能有一个最快、最小的分类器真的会很酷。

**Steve：**这些模型非常适合微调。

我只想要模型能输出一个 diff，能干净地应用到代码中，而且就直接能正常工作，不需要我去调整。那将会是巨大的进步。模型目前并不太擅长理解代码行号这些细节。

4 月 15 日，OpenAI 发布了 GPT-4.1，GPT-4.1 使模型能够更可靠地遵循 diff 格式，开发者只需输出更改的行，而无需重写整个文件，节省了成本，减少了延迟。

**Q：****之前有观点认为最前沿的 agent 必须依赖最前沿的模型，但最近中国有一些非常令人印象深刻的 agent 工作，他们使用了 Anthropic 模型就取得了很好的成果，对此你们怎么看？**

**Nikunj：**OpenAI 内部一直在说**模型的能力已经存在，但很少有人能够真正利用。我们需要让开发者在内的每个人都能够更轻松地使用这些模型，从而构建更强大的东西，而不只有顶尖的 AI 和 ML 人才才能做到。**只要给人们合适的工具和模型，帮助他们将这些东西组合起来，让 Agents SDK 这类工具的使用效果显露出来，更多的人就能够创造出像中国展示的 agent 那样的成果。

**Steve：**关键是要让飞轮转得更快，从评估到生产，再到微调，这是一个强大的循环，需要让这个循环变得更简单。

**Q：****让这个过程变得更简单，最关键的是什么？**

**Nikunj：**OpenAI 的研究团队一直在做这件事，目前模型在聊天方面变得更好，做深度研究的能力也在提升。下一个模型将比当前的模型更强大，能更好地执行 computer use 任务。

但如何将这个过程产品化，是我们需要解决的问题。通过仔细观察跟踪数据，创建正确的评估和评分标准，确实是能奏效的。我们需要优先处理这个问题，找到如何让这个过程变得更简单的方法。

**Steve：**对我来说，最大的挑战就是如何让评估任务和工作流程的过程变得更加简单。

**Q：****如果你是一个普通企业的 CEO 或消费者，面对这些模型，你会做什么？**

**Nikunj：**首先要做的就是探索这些前沿模型，尝试使用 computer use 模型，选取几个内部工作流，建立 multi agent 架构，进行端到端的自动化。最可行的做法就是弄清楚现有的哪些手动工作流需要工具接口，就像刚进入云计算时代时做的数字化和自动化转型。

用户有时会说：“我们想自动化整个流程，但 90% 的工作是弄清楚如何获取某些工具的程序化访问权限，LLM 只是其中的一小部分。”我觉得完全不是这样子的，你可以把 computer use 投入生产，**但真正需要做的是找到自动化应用的方式，尝试使用前沿模型。**

**Steve：**作为开发者，我们一直在自动化我们工作中的底层 20%，无论是通过更好的框架、更好的编程语言，还是其他方式。所以，如果我是公司老板，我会问员工每天最不喜欢做的事情是什么，然后想办法去自动化。

**05.**

**对 AI 模型的看法**

**Q：****今天 AI 是否被过度炒作或被低估？**

**Nikunj：**我们对 agent 技术的讨论已经持续了好几年。它一方面经历了两个完整的炒作周期，存在过度炒作的现象；但另一方面，它的真正潜力又常常被低估。只有那些真正理解 AI 本质、并像 Deep Research 那样将部分人工任务彻底自动化的公司，才真正展现了 agent 的价值。

**Q：****在过去的一年里，你们在 AI 领域有什么看法改变吗？**

**Nikunj：**最大的变化是对推理模型的理解。我们一直都知道推理技术会到来，但我没有意识到它和 tool use 的结合会产生像 Operator 和 Deep Research 这样的产品。

这种方法不仅可以摆脱传统工作流程，还能产生完全基于 agent 的产品，使得 agent 能够在 CoT 中自我调整并交付出较好的结果。

**Steve：**对我来说是 fine-tuning 的广泛应用。我曾经以为所有能加入模型的知识在训练完成时就已经固定在其中了，但现在还能够在模型训练完成后添加大量自定义信息，从而在特定任务上带来明显的性能提升。

**Q：****长期来看，应用开发者之间最大的区别点是什么？是对模型的深入理解，能真正构建 agent 模型？还是对某一领域的深刻了解，知道应该构建什么？**

**Steve：**这两者的结合很重要，然后重要的是**是否拥有某种秘诀，能够真正把 AGI 的能力从模型中挖掘出来，这个秘诀可能是 prompt，工作流编排，或者其他，这会是一个巨大的区分因素。**

**Nikunj：**我认为开发者之间的差异点是是否擅长编排，编排指的是将工具和数据结合起来，进行多次模型调用，无论是通过强化微调，还是在 CoT 中调用工具，或者是将多个 LLM 串联起来，并能够快速高效地评估和优化这一过程。这是未来一年到两年内，能推动人们进步的最重要的技能。

**Q：****目前这些模型最被低估的应用是什么？**

**Nikunj：**我还没看到模型在科学研究方面有什么明显进展。我们对 O 系列模型最大的期望就是它能明显加速科学研究的进程。我们已经看到一些早期的报告，但我非常好奇它将如何改变科学研究。

**Steve：**关于 AI 行业的很多批评都是接口设计还不够完善，特别是在学术领域，很多事情的处理方式已经维持很久了。找到合适的接口会是关键，并且会推动学术界的广泛采用。

**Nikunj：**机器人技术也是。可能是时候出现一些大的突破了。

**Q：****今年的模型进展会比去年更多、一样还是更少？**

**Steve：**肯定会更多，模型教会我们如何通过更好的数据和方法来改进它们。

**Q：****除了 OpenAI，你们现在最看好的 AI 初创公司或者公司类型是什么？**

**Steve：**我在加入 OpenAI 之前，曾经在旅游公司工作过，所以我期待有公司能真正打破旅游行业的僵局。这个行业非常固守传统，只有少数几家大公司在主导。期待能建立一个真正的 AI 旅游 agent。

**Nikunj：**我现在经常用 Granola，这是我目前最喜欢的 AI 工具，每次开会几乎都在用。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 排版：Doro

延伸阅读

为什么 AI Agent 需要自己的浏览器？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

详解 MCP：Agentic AI 中间层最优解，AI 应用的标准化革命

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

代码即界面：生成式 UI 带来设计范式重构

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxib2dNICCpDd8HafMjdmiajct2TaIEf9Bp3HSmZ7SnNB0m1RmJVmKP1Q0iaAs2VETraa3JZ7JGBz1Jg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19)

Deep Research 类产品深度测评：下一个大模型产品跃迁点到来了吗？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxib2dNICCpDd8HafMjdmiajct2TaIEf9Bp3HSmZ7SnNB0m1RmJVmKP1Q0iaAs2VETraa3JZ7JGBz1Jg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21)

AI Agent 摩尔定律：每 7 个月能力翻倍，带来软件智能大爆炸

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxib2dNICCpDd8HafMjdmiajct2TaIEf9Bp3HSmZ7SnNB0m1RmJVmKP1Q0iaAs2VETraa3JZ7JGBz1Jg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=23)