---
url: https://mp.weixin.qq.com/s/6NJgaoiDdNaQ1YcGrgSi2Q
title: "Deep Research 团队：Agent 的终极形态是所有任务 All-in-one"
description: "AGI 在今天是一个操作层面的问题"
author: "拾象"
captured_at: "2026-03-08T12:49:40.448Z"
---

# Deep Research 团队：Agent 的终极形态是所有任务 All-in-one

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxjoXQWuIBttMBiaech7KgqkK91oerDHkT6yeCgpL6HpHy2iceiawicmRzxnQsSDuUwUxib3z6qeECtnjw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxjoXQWuIBttMBiaech7Kgqk4nz9sYlWMTYTF8ibpQGkNoHZOn3cKynRdUJ8UdMibpdKlyElxaTXFSgg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

编译：haozhen

编辑：siqi

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxjoXQWuIBttMBiaech7KgqkjjsXHMIYm51iaGcCVIiaYwfnqNg8ZBBZtdhqKFqPmF4qaI2TZBtiaRTtQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

三周前，OpenAI 推出了 Deep Research，这是 OpenAI 的第二个 Agent，可以通过搜索多个网站，在 5-30 分钟内完成全面的 online research，并综合引用输出详细的报告。

本文是 Sequoia Capital 对 OpenAI Deep Research 负责人 Isa Fulford 和 Josh Tobin 的专访编译整理， 两位成员详细分享了 OpenAI 在构建 Deep Research 时的技术细节和产品思路，以及目前他们说观察到的 use case。

Deep Research 源于 OpenAI 内部对模型 long-horizon 任务的处理能力的探索，团队长期的目标是**在未来更够给到用户一个终极 Agent：网络搜索、使用计算机或完成其他希望 Agent 完成的任务自然地 All-in-one。**

Deep Research 在产品层面也做了专门优化，例如，和我们在 [DeepSeek](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247511288&idx=1&sn=b3090c9105c230991f922eea0f4d901b&scene=21#wechat_redirect) 的分析判断中提到的一样，Deep Research 也通过清晰的引用和 CoT 来增强用户信任。此外，团队还设计出了一个澄清流程（clarification flow），即确保对任务理解的一致性。Deep Research 在信息查找和梳理上比 AI 搜索和 ChatGPT 都要强，但现阶段 **Deep Research 从已有信息中提炼出新的见解的效果不佳，还不能做出新的科学发现。**

**💡** 目录 **💡**

01 OpenAI 的第二个 Agent

02 Agent 能力来自模型端到端的训练

03 Deep Research 的优势

04 Deep Research 的使用场景

05 Agent 会在 2025 年崭露新头角

**01.**

**OpenAI 的第二个 Agent**

**Deep Research 是一个能够搜索多个在线网站并生成非常全面报告的 Agent，可以完成人类需要花费数小时才能完成的许多任务。**Deep Research 在 ChatGPT 中运行，回答问题的时间大约在 5-30 分钟之间，因此能够进行更深入的研究，并能比普通 ChatGPT 更详细、更加具体地回答问题。之前 OpenAI 已经推出了 Operator，Deep Research 是 OpenAI 的第二个 Agent，OpenAI 未来还会发布更多的 Agents。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**起源**

大约一年前，OpenAI 内部开始采用 reasoning 范式，并想要训练模型能够在回答之前进行思考的这个行为，这个尝试取得了很大成功。

一开始，OpenAI 将重点领域放在了 Math 和 Science，但发现这种新的推理模型体系还解锁了更长时间跨度任务的处理能力，即涉及到了 Agent 的能力。

与此同时， OpenAI 意识到，**很多任务的完成需要大量的 online research 或外部 context，需要有很强的推理能力，以及对信息来源的辨别能力，而且必须具备一定的创造力。**最终，OpenAI 开发出了能够应对这些任务的模型训练方法。OpenAI 决定开始训练模型执行浏览任务，使用了与训练推理模型相同的方法，但应用于更贴近现实世界的任务。

Deep Research 项目最初是 Isa Fulford 和 Yash Patil 一起合作了一个原创 demo。Josh Tobin 大约 6 个月前从创业公司回来，重新加入 OpenAI，对原创性工作产生了浓厚的兴趣，所以加入 Deep Research 项目。

**Isa Fulford：**OpenAI Post-training 团队的 AI researcher，ChatGPT Retrieval Plugin 的主要贡献者；

**Yash Patil：**OpenAI Post-training 团队里 core model 的成员，已经从斯坦福辍学；

**Josh Tobin：**曾在 OpenAI 担任 Research Scientist，后离职成立 Gantry（一个通过分析、警报和人工反馈帮助提升 ML 的产品）。后再次加入 OpenAI，目前领导 Agents 产品 research team。

****澄清流程（**clarification flow）******

Deep Research 有一个特殊的设计是澄清流程（clarification flow），即 **Deep Research 模型在开始研究之前会向用户提问，**通常情况下， ChatGPT 只会在回答结束时提出 follow on questions 或者询问答案是否满意，而不会像 Deep Research 那样在前期就进行这类行为。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这一点其实是团队专门设计的，因为只有用户的 prompt 非常明确和详细，用户才会从 Deep Research 模型中得到最好的响应。但用户通常并不会在第一次输入 prompt 时就提供所有的信息，因此， **OpenAI 希望确保用户在等待 5 分钟或者 30 分钟后，最终得到的回答是足够详细和令人满意的，所以添加了这个额外的步骤，确保用户提供模型所需要的所有细节。**

很多用户在 X 上说他们会先与 o1 或 o1 Pro 互动，使 prompt 更加详细，用户对 prompt 满意后，再将 prompt 发送给 Deep Research。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Agent 的终极形态**

实际上，过去几个月里 OpenAI 已经推出了三种不同的 Deep Research，这些产品都叫做 Deep Research，Josh Tobin 认为虽然这些产品各有优缺点，但产品之间的质量差异是很明显的。归根结底是因为模型的构建方式，以及在构建数据集时投入的努力，再加上 OpenAI 使用 O 系列模型作为引擎，使得 Deep Research 模型能够被优化，创造出非常聪明且高质量的工具。

目前 Deep Research和 O3、Operator 之间还比较独立，但 OpenAI 希望**在未来，用户能够通过一个终极 Agent 实现网络搜索、使用计算机或完成其他希望 Agent 完成的任务，而且还能够以更自然的方式将所有这些功能融为一体。**

**02.**

**Agent 能力**

**来自****模型****端到端训练**

**端到端训练****是模型强大的本质原因**

**Deep Research 的底层模型是 O3 的 fine tuned 版本，**O3 是 OpenAI 最先进的推理模型，Deep Research 很多分析能力来源于底层 O3 模型。**OpenAI 专门对 Deep Research 模型在复杂浏览任务和其他推理任务上进行了训练，**因此，Deep Research 还可以使用浏览工具和 Python 工具。通过在这些任务上进行端到端的训练，Deep Research 学会了应对这些任务的策略，最终使得该模型在在线搜索分析方面表现出色。

直观地说，用户提出一个请求，模型会先仔细思考这个请求，然后搜索相关信息，提取信息并阅读。模型理解这些信息如何与请求相关后，再决定接下来搜索什么，以便更接近用户想要的最终答案。Deep Research 能够将所有这些信息整合成一份整洁的报告，并附上指向原始信息来源的引用。

**Deep Research 能有 Agent 能力的创新之处就在于 OpenAI 对模型进行了端到端的训练，**这意味着在进行研究的过程中，很多操作是事先无法预测的，不可能通过编写某种语言模型、程序或脚本，来达到模型通过训练所能得到的灵活程度。**Deep Research 模型通过训练，学会了如何对实时的网页信息做出反应，并根据所看到的信息及时调整策略等，所以 Deep Research 模型实际上在进行非常创造性的搜索，**用户可以通过阅读 CoT 的总结发现模型在如何决定接下来要搜索什么或如何绕过某些问题方面非常聪明。

**Deep Research 和 AI 搜索的差异**

对于 John Collison 提出的“Deep Research 的能力有多少来自于实时访问网页内容，又有多少来自于 CoT”的问题，OpenAI 的两位研究员认为， Deep Research 的突出能力是两者组合的结果。

其他 AI 搜索产品并不是端到端训练的，所以在响应信息时不会像 Deep Research 那样灵活，也不会像 Deep Research 那样在解决特定问题时表现得那么有创意。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Josh Tobin 在加入 OpenAI 之前在一家初创公司工作，曾尝试按照大多数人描述的构建 Agent 的方式来构建 Agent，基本上就是构建一个操作图，而其中一些节点上会有 LLM 介入。虽然 LLM 可以决定接下来做什么，但整个步骤序列的逻辑是由人定义的。

Josh Tobin 发现这是一个快速构建原型的强大方法，但在现实世界中很快就会出现问题，因为很难预见模型可能面临的所有情境，也难以考虑可能想要采取的路径的所有不同分支。此外，由于这些模型并没有专门接受做决策的训练，它们通常不是节点上最好的决策者，它们是被训练来做一些与决策类似的事情。

**这再次说明了 Deep Research 模型的真正强大之处来源于端到端直接训练，目的是解决用户实际需要解决的任务，所以不需要在后台架构中设置操作图或做节点决策，一切都是由模型本身驱动的。**

更近一步，如果用户有一个非常具体且可预测的工作流程，那么按照上文 Josh Tobin 描述的方式来做是很有价值的。但如果需要非常灵活的处理，那么类似 Deep Research 的方法可能是最好的选择。

Josh Tobin 建议不应该将一些严格的规则硬性嵌入到模型中，如果有类似“不希望模型访问某个数据库”的需求，最好还是用人工编写的逻辑来实现。**人们往往认为自己可以通过编写代码做得比模型更聪明，但实际上，随着领域的发展，模型通常会比人类提出更好的解决方案。**

机器学习的一个最重要的教训就是，你得到的结果取决于你优化的目标。所以，如果用户能设置一个系统来直接优化想要的结果，那么会比用户尝试将不适配整个任务的模型拼凑在一起要好得多。所以**在模型整体基础上进行 RL 调优，可能会成为构建最强大的 Agent 的关键部分。**

**模型成功的关键因素之一
****在于****高质量数据**

**Deep Research 模型能够成功的关键因素之一是有高质量的数据集。**投入到模型中的数据质量，很可能是决定模型质量的关键因素。在 Deep Research 项目中，Edward Sun 会对所有数据集进行优化。

**03.**

**Deep Research** **的优势**

**Deep Research 的优势在于，当用户有一个详细的需求描述时，Deep Research 能够通过阅读大量的互联网内容来提供最佳答案，但如果用户的问题比较模糊，Deep Research 也能理清想要的信息。**Deep Research 最强大的时候是用户在寻找一组具体信息的时候。

**Deep Research 不仅能广泛地收集关于某个来源的所有信息，还能很好地找到一些非常冷门的事实，**比如在传统搜索中不会出现在前几页的长尾内容，某部冷门电视节目其中某一集的细节信息等。在一个有关奥地利将军的问题中，ChatGPT 曾经给出了错误的答案，而 Deep Research 成功找到了正确的答案。

Deep Research 非常擅长综合信息，尤其是在找到一些特定的、难以找到的信息上。**不过，Deep Research 从已有信息中提炼出新的见解的效果不佳，还不能做出新的科学发现。**

**04.**

**Deep Research** **的使用场景**

**目标用户**

**Deep Research 是为任何在日常工作或生活中从事知识性工作的人员设计的，特别适合需要大量收集信息、分析数据并做出决策的人。**很多使用者将 Deep Research 应用于工作中，比如在做研究的时候，用于了解市场、公司、房地产等领域的情况。

**Use Case**

**OpenAI 希望 Deep Research 能兼顾商业场景和个人生活场景，**因为 Deep Research 实际上是一种非常通用的能力，既适用于工作，也适用于个人生活。Deep Research 的魅力在于能够节省很多时间，有些任务原来可能需要花费数个小时，甚至几天时间，但现在人们可以用 Deep Research 得到 90% 的答案。OpenAI 认为商业场景中的类似任务会更多，但 Deep Research 也会成为人们个人生活的一部分。

**Deep Research 不是取代劳动力，对于知识型工作，尤其是需要花大量时间查找信息并得出结论的工作，Deep Research 将赋予人们超能力，**使得原来可能需要 4 或 8 小时才能完成的事情可以在 5 分钟内完成，用户因此可以实现更多的事情。

访谈中提及的 use case 包括：医疗、投资等工作场景，购物、旅行等家庭场景，编程和个性化教育等。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**•** **医疗、投资等专业工作场景**

在医疗上，Deep Research 能够帮助寻找某种疾病的所有文献或最近的病例，从而节省了时间。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在投资上，在 Deep Research 帮助下，投资人可以选择对每一个可能投资的初创公司都进行研究，而不仅仅是只研究有时间会面的公司。

在公司经营上，有一个正在考虑创办一家消费品公司的用户，他一直在大量使用 Deep Research 来确定特定的品牌名称是否已经被注册，域名是否被占用，市场规模等各种信息。

**•** **购物、旅行等家庭场景**

有用户在考虑买新车的时候，想知道下一款车型什么时候发布，而网上有很多猜测性的文章，因此用户让 Deep Research 整理相关的所有传闻等，最后 Deep Research 整理出了一份很出色的报告，告诉用户可能会在接下来的几个月里发布新车。

在日本推出 Deep Research 时，用户发现 Deep Research 在找到符合特定要求的餐厅方面非常有帮助，还能帮用户发现一些本来可能找不到的东西。

用户需要购买某个贵重物品，或者规划一趟特别的旅行，或者需要花很多时间去思考某个问题时，用户可能会花费几个小时在网上查找相关信息，浏览所有的评论等，而 Deep Research 可以迅速把这些信息整理出来，像是做一个总结报告，提供详细和个性化的建议。

忙碌的职场妈妈往往没时间为孩子策划生日派对，但现在在 Deep Research 的帮助下可以快速做到。

Deep Research 在指令跟随方面也非常出色。如果用户不仅想要了解某个产品的信息，还想要与其他所有产品进行对比，甚至想要查看来自 Reddit 等网站的评论，用户可以对 Deep Research 提出许多不同的要求，Deep Research 会一次性完成这些任务，用户还可以让 Deep Research 把信息做成表格。

**• 编程**

很多人把 Deep Research 用于编程，这个场景并不是 OpenAI 最初所考虑在内的，但确实有很多人用来编写代码、进行代码搜索，甚至查找某个包的最新文档，或者写脚本等，效果令人印象深刻。

**• 教育**

个性化教育是一个非常有趣的应用场景。如果用户有一个想学的主题，比如需要复习生物学，或者想了解一些时事，用户只需要提供自身不理解的部分，或者想深入研究的信息，Deep Research 就能整理出一份详细的报告。或许在未来可以做到根据 Deep Research 了解到的用户情况，提供个性化的教育。

**05.**

**Agent 会在 2025 年****崭露新头角**

**Deep Research 未来发展方向**

在产品形态上，OpenAI 希望未来 Deep Research 能够嵌入图像，可以找到产品的图片，也能生成图表，并将这些图表嵌入回答中。

在信息来源上，OpenAI 希望能够扩展模型可以访问的数据源，希望模型未来能够搜索私人数据，OpenAI 接下来会进一步提升模型的能力，使得模型在浏览和分析方面做得更好。

在信息准确度上，为了让用户能够信任 Deep Research 的输出，用户可以看到模型引用的信息来源。在训练模型的过程中，OpenAI 也会努力确保引用的正确性，但模型仍然有可能出错，或者产生幻觉，甚至信任一个可能不是最可信的信息来源。因此，这是 OpenAI 希望继续改进的领域。

为了更广泛地融入 OpenAI Agent 路线图，OpenAI 希望 Deep Research 能够扩展到许多不同的应用场景，将最先进的推理模型与人类可以用来完成工作或日常生活任务的工具结合起来，然后直接优化模型以实现用户希望 Agent 能够完成的结果。

**现阶段实际上没有什么能够阻止 Deep Research 扩展到更加复杂的任务场景上，AGI 现在是一个操作性问题，未来还会有很多值得期待的进展。**

Sam Altman 认为，Deep Research 能够完成的任务将占到世界上所有经济上可行的任务的百分之几。**Josh Tobin 认为， Deep Research 并不能为用户做所有的工作，但能够为用户节省几个小时，甚至是几天的时间。**OpenAI 希望相对接近的目标是，Deep Research 和接下来构建的 Agent，以及在这个基础上构建的其他 Agent，可以根据用户所从事的工作类型，帮用户节省 1%、5%、10% 或 25% 的时间。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Agent & RL**

**Isa Fulford 和 Josh Tobin 一致认为今年 Agent 会崭露头角。**

RL 经历了一个高峰，之后感觉又有点低谷，现在又受到人们关注。Yan LeCunn 曾经有一个类比**，如果人们在做蛋糕，那大部分是蛋糕，会有一点糖霜，最后放上几颗樱桃，无监督学习就像是蛋糕，监督学习是糖霜，RL 就是樱桃。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Josh Tobin 认为，在 2015-2016 年做 RL 的时候，以做蛋糕类比，可能是试图在没有蛋糕的情况下先加樱桃，但现在，已经有了在大量数据上预训练的语言模型，这些模型非常强大，并且知道了如何对这些语言模型进行监督微调，使模型擅长执行指令和做出人们想要的事情，现在一切运作得非常好，非常适合根据用户定义的奖励函数来调整这些模型，用于任何用例。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

排版：杨乐乐

延伸阅读

OpenAI 都在用的 AI 招聘，2 年内实现 7500 万美元 ARR

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Chai Discovery：OpenAI 投资的 AI4Sci 公司，AlphaFold 最快追赶者

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Codeium：企业原生 AI Coding 产品，能开创 Agentic IDE 新范式吗？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxjoXQWuIBttMBiaech7KgqkEOfHdv4OKITs0CCbIz20kdnMrFFxYfCyYpc8HxVMsibnwQxb8kCw5YA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20)

对 DeepSeek 和智能下半场的几条判断

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxjoXQWuIBttMBiaech7KgqkEOfHdv4OKITs0CCbIz20kdnMrFFxYfCyYpc8HxVMsibnwQxb8kCw5YA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22)

扛住 DeepSeek 黑天鹅，AGIX 如何实现 3 倍纳指回报

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxjoXQWuIBttMBiaech7KgqkEOfHdv4OKITs0CCbIz20kdnMrFFxYfCyYpc8HxVMsibnwQxb8kCw5YA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=24)