---
url: https://mp.weixin.qq.com/s/t5ByNhtOz0MXlTx940JeKQ
title: "Notion CEO：为什么RAG会彻底改变知识型工作？"
description: "AI将SaaS带入新一轮Bundling周期"
captured_at: "2026-03-08T11:36:25.035Z"
---

# Notion CEO：为什么RAG会彻底改变知识型工作？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/3tHNibnJ2jgxqciagxK2eiac3HqvzStGW0PreZx5EwXbR4YeiciczNIZvuCnia9HbvyXltDVvv4EqrYPGjVJ4DAsAv0w/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxqciagxK2eiac3HqvzStGW0PjHnrjebLAcwCXJ2HRwawrNrIWiaHClSbdKzK4SJiakibGErf7ZMdY9WPA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3tHNibnJ2jgxqciagxK2eiac3HqvzStGW0Pic3CMRULN4vhk1hicR5185ux11Es1HHpfcTDX3KdYrOP1JbWR4SviaHkg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

编译：海外独角兽

排版：Scout

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgxqciagxK2eiac3HqvzStGW0PgFEL9RiaIHyyBz2XBkRQZ96sgjuuadMt94oonkuia1atmgiamsyyd0TIA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

本篇内容是 No Priors 对 Notion CEO Ivan Zhao 的访谈编译。

Notion 是生产力工具领域 AI 策略最为激进的一家公司：在 ChatGPT 推出 2 个月后，Notion 就宣布推出Notion AI，将 GenAI 的体验直接融入到产品，并根据不同需求和场景预设了 prompt，用户只需要空格或“/”即可调用 GPT。Notion AI 上线 1 个月后，就有消息称 Notion AI 为 Notion 带来了 1000 万美元的 ARR，上线 2 个月后，Notion AI 用户突破 400 万。除了不断提升问答交互的体验，Notion 还推出了 Notion Project、Notion Q&A 和 Notion Calendar 等新功能、产品。

在访谈中，Ivan 分享了 Notion 在 AI 实践中的思考：团队all-in AI 的决策是如何做出的、为什么说  RAG、workflow agent 被外界低估了，以及 language model 一定程度上会将 SaaS 世界带入到新一轮 bundling 周期中。

Notion 的愿景是通过构建出各种各样的“积木块”让用户在平台上搭建出更具个性化、符合实际需求的定制化应用，从而实现“人人都能制作自己的软件”这件事，Ivan 认为，language model 的出现一定会加速这一过程，更进一步，RAG 还会彻底革命知识型工作和团队沟通的形态，Notion Project、Notion Q&A 和 Notion Calendar 等新功能、产品正是服务于此。

**以下为本文目录，****建议结合要点进行针对性阅读。**

****👇****

01 AI 是 Notion 的机会

02 Notion AI 的诞生

03 RAG：知识管理的未来

04 AI 让 SaaS 进入新一轮 Bundling 

**01.**

**AI 是 Notion 的机会**

 **Sarah Guo ：****你会怎么定义 Notion？**

**Ivan Zhao：**Notion 很难被定义，因为它可以被用来做很多事情，但我们本身也希望打造一个全能的工具，用户可以用它来完成日常生活中的大部分任务，比如个人用户可以用 Notion 来记笔记、做旅行规划、婚礼统筹等，企业用户也可以只通过 Notion 这一个工具就完成文档管理、任务追踪以及内部知识库的构建等。我们之所以想做这件事是因为现在市面上有大量的 SaaS 软件工具、市场相当分散，但也许对于用户来说如果一个产品能让他们 all-in-one 地完成大部分工作是一件好事。

Notion 实现这个目标的方式并不是把很多功能塞进一个具体的产品里，而是去构建更底层的 block，用户可以像搭建乐高积木一样，用这些 blocks 来创造性地做出各种各样完美符合个人或团队需求的用例。

其实 Notion 在做的这件事并不新，因为在上世纪 80 年代、甚至 70 年代人们就讨论过用 block 逻辑来构建软件这件事。到了今天，我们只不过是在云和 AI 的支持下去实现这件事、打破过去以具体功能导向的软件的限制。

 **Sarah Guo ：****确实在过去 20 年我们一直处于过度分散的 SaaS 世界中，理论上，做一个通用的工具应该是自然而然的趋势，但为什么没有人来做这件事？**

**Ivan Zhao：**其实人们已经从很多角度进行过尝试。比如最近很流行的 No-code 就是从个人开发者角度来想这件事，No-code 让每个人都能修改他们日常使用的软件工具。Language model 提供了另外一个角度，就是底层知识和数据的管理需要被统一起来。宏观也是一个视角，因为如果考虑预算的话，和支付 5 个 SaaS 软件的费用相比，只给一个供应商付费显然要更能节省开支。

我认为 Notion 更多是从计算、内容或者说文本相关角度出发来想这件事。比如我们所有人都会阅读和写作，但对于绝大多数人而言，电脑只是一台打字机或者看 YouTube 的工具，本身并不具有创造力。如果更多的人能够更具创造性地使用他们的软件，可能情况就会不一样。创造软件的人和用软件的人提供的价值是完全不同的，这也是旧金山房租如此昂贵的重要原因。

计算机领域的先驱们在很早之前已经讨论过这件事，他们认为操控计算机有一天会像识字一样普及，不过他们当时可能完全没想到 AI 会成为一个有趣的变量，language model 不仅可以创造软件，还可以帮人们完成大量思考相关的工作。接下来的发展会相当有趣。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 **Sarah Guo ：****你经常提到 Notion 不仅是一个生产力工具，更是一个应用构建平台。你是如何想到这个观点的？为什么你认为人们想要去搭建更多的应用？**

**Ivan Zhao：**我并不认为人们想搭建更多的应用。

Notion 的诞生源于我在大学时读过的一篇论文， Douglas Engelbart 的 *Augmenting Human Intellect: A Conceptual Framework*。今天人们使用软件通常情况下都是具体一款产品对应一类具体任务，但在计算机刚出现的时候，比如 60、70、80 年代，人们使用电脑的方式要更加灵活，我们可以进入到系统层面进行调整，甚至是在操作系统正在运行的时候，实时地对其进行修改或调整。这件事对我的启发很大。

今天，人们在使用电脑、和软件交互的方式有时候会显得很死板，那么我们能不能创造一种全新的软件，让人们可以去灵活调整和定制？这就是我们创立 Notion 的初衷，我们其实在重新审视计算机领域的先驱们当年讨论过的议题。

你刚刚也提到，大多数人并不想创建软件，更多的是完成老板分配的任务即可。所以，我们在创立 Notion 过程中学到的经验以及由此带来的一个转变是，相较于提供一个构建软件的工具，更好的方式是提供给用户各种各样的 blocks 构建的模板，让用户上手即用。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 **Elad Gil ：****AI 对这个目标带来了什么样的影响？**

**Ivan Zhao：**我认为 Notion 还是很幸运的，我们其实没有特别专注于某个具体用例的搭建，我们的重点一直是放在构建这些用例的乐高积木块上面，这些“积木”中既有文档编辑这类最基础层的“积木”，很我们还推出了关系型数据库（Relational database），表格、评论以及不同的访问权限等等也是很重要的“积木块”。过去 5 年时间我们一直在构建这些积木。

AI 更像是一个以新的方式来组合、驱动这些积木块的新引擎，也正因为我们一直在构建、完善这些积木块，我们才可以迅速把 AI 和已有功能结合起来。我们之所以是市面上大规模推出 AI 协作的软件之一，是因为我们已经在文本编辑器上花了很多年时间，也因为我们已经做了关系型数据库，所以我们可以把 AI 和数据库结合起来，我们能够快速推出 Notion Q&A 也是因为我们在知识库产品上的投入。我们能把 RAG 应用到 Notion 的产品中也是因为我们做了各种各样的“乐高积木块”，AI 对于 Notion 是一个特别好的机会，而我们正好抓住了这个机会。

 **Elad Gil ：****Notion 已经构建了很多核心模板和用例，比如项目管理工具、知识库等等，在它们之中，****你认为有哪些功能受 AI 的影响最大？**

**Ivan Zhao：**我认为 RAG 会彻底改变知识管理的方式，让人们摆脱繁琐的信息组织工作。Notion 最受人喜爱的功能之一是侧边栏，人们会用它整理知识库和个人 workspace。但以后我们可能不再需要这样的工具来组织知识库了。用户只要简单地将信息丢到 Notion 中，就可以通过各种方式进行检索。这就是知识管理的未来。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 **Sarah Guo ：****在 PC 时代发展早期，当时人们会讨论 30 或 40 年后，PC 带来的最大变化会是什么？今天你对 AI 未来的发展有什么期待？**

**Ivan Zhao：**对于 AGI 来说，时间尺度放在 30 或者 40 年可能有点太久了，甚至不用等到下一个 10 年，在未来 1-2 年内 AI 就会有明显突破。这之中我认为一个被低估的领域是 RAG。

今天 language model 已经能够很好地理解人们输入到计算机中的内容了，这意味着我们不需要再自己去做信息的组织来方便未来对信息的检索，AI 在这件事上做得比任何人类都要好。

在 language model 之前，我们要在知识库搜索一些内容通常需要很精确的关键词，甚至有些时候还要询问同事是否记得某个序列、某个信息存放的数据库是哪个。但现在可以直接询问 Notion AI 想要搜寻的问题，很快 AI 就会给到答案，这是我个人很兴奋的一个应用场景，不少人也在讨论。另外一个我认为很值得期待的是 Work Agent，这个领域也已经开始有很多人关注到了。

**02.**

**Notion AI 的诞生**

 **Sarah Guo ：****Notion AI 的进展相当快，尤其和很多还不知道如何运用 AI 的产品比。这个过程中你们是如何做决策以及进行资源分配的？**

**Ivan Zhao：**我和 Simon 对 AI 都有足够强的 conviction，我们早些年去 OpenAI 的办公室时，根本不理解这家公司在做的事情是什么，但当时我们已经见过很早期的 GPT 的 demo。

必须承认的是，GPT-3 刚出现的时候我是轻视了这件事的。虽然 GPT-3 已经可以帮助人们进行市场营销策划、完成初稿写作，但我并不认为这能有多大用处，直到我看到 GPT-4 的能力我的想法才发生了转变，我发现 GPT-4 已经可以思考、推理，可以完成各种各样的事情，可以更加实际地优化工作流。GPT-4 对我影响很大，它给了我很多信心，我也因此觉得这会是一个巨大的转折点。

什么是知识型工作？人们为什么需要软件？从根本上说，软件就是我们所有人的信息处理活动，就像一张纸传到面前，人类改变几个字，然后推送给另一个人。在某种程度上，language model 已经可以帮助我们完成这种信息处理。所以，我相信这将完全改变我们与计算机的交互模式。

在那之后，我们团队基本上就全身心投入到 AI 项目中了。我们已经搭建好了很多积木，接下来就是弄清楚哪些积木可以与 AI 相结合，以及公司内部谁对这项技术有深入了解。虽然我们有搜索团队，但我们的 ML 团队并不大，所以，我们还需要招聘更多的人才，与此同时还要让公司内部的人对这项技术有共同的信念，这样我们才能朝着同一个方向前进。我们就像面临小行星撞击地球的恐龙一样，需要为即将到来的巨变做准备。

 **Elad Gil ：****为了让 Notion 成为一个 AI-first 的产品，你们在团队层面做了哪些工作？**

**Ivan Zhao：**Notion AI 早期主要还是靠“大力出奇迹”，我的 co-founder Simon Last 在这件事上做了很多贡献，他快速学习了很多 AI 相关的东西。

Notion 团队里有很多对 interface 和设计感兴趣的人，前后端也分别有很多全栈型人才，我们内部也有一部分专门在做搜索，但 ML 相关的人才并不多，甚至可以说是没有。过去一年的时间中，我们一直在学习怎么做 AI。

我们在 AI 上的各种尝试很像做烘焙的过程：准备好一切原材料、把这些原材料放进烤箱、按下按钮之后就只剩下等待，没有人能够预知成品是什么样的，所以这要求我们有足够的耐心，同时还要做大量的调整和准备。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 **Elad Gil ：****有一些人把这个过程总结为概率工程，这会让人觉得我们进入到了一个充满随机性的领域当中，至少是部分随机的。**

**Ivan Zhao：**是的，这一类工作很像是在做园林培育，我自己并不会这类工作，所以我很需要这样一类人帮我做这件事。

Notion 需要的另外一类人是富有好奇心以及快速学习能力的人。Language model 让每个人可以实时地调用 AI 能力来完成自己的任务，但如何用好模型能力其实有很多技巧，以及如何将 LLM 和用户交互做结合也是很重要的问题。这类人一般被称为 AI 工程师，Notion 的 AI 工程师们都很年轻，很多甚至还不到 21 岁。

这两类 AI 人才的工作能力都很强。Notion 目前还没有很多 AI researchers，这类人才在我看来也相当重要。不过 Notion 毕竟处于应用层，所以我们很多时间是花在研究如何用模型上。

 **Elad Gil ：****从 GPT-3 到今天，我们看到 GPT 能力提升特别快，并且每一代模型都会带来新的商业模式，你认为要充分利用 GPT 的能力还需要做哪些工作？**

**Ivan Zhao：**技术的本质是做 trade off 。Language model 带来了一种全新特性，这是过往被设定为具体功能的软件所不具备的，但我们还不太了解它完整的工作原理，所以人们一直在 Twitter 上讨论要怎么才能更好地使用模型的能力。对于企业和创业者来说，面对新技术也要做出一些权衡，他们要时刻了解市场对于各种新模型能力的评价。这个行业目前正在快速发展、不断变化。

技术层面，模型现在能够处理更广泛的上下文信息，具备更强的推理能力，运行速度更快，同时占用的资源更少。这对于 Notion 来说非常重要，因为我们需要的就是像 GPT-4 这样既智能又高效的云服务。我们需要 AI 来帮助我们进行复杂的推理任务或者快速地总结文本内容，并且最好成本够低，速度够快。这就是技术层面上我们需要关注的方向。

除了技术因素，我个人还会关注很多人类行为习惯角度的改变，比如个人用户的行为惯性、公司的风险承受能力等，这些也都在慢慢演变。就像 **Steve Jobs 常说“你不能做出太新的东西，你必须在保持大部分相同的基础上，改变一两个关键点。”Off White 创始人 Virgil Abloh 的理念是，只需要改变 3%，但足以推动边界，让人们接受新事物。**

3% 理念（3 Percent Approach）是时尚品牌 Off White 创始人及设计师 Virgil Abloh 的设计哲学，这个理念的核心思想是，在现有设计的基础上只做出不超过 3% 的改变，从而使产品看起来既熟悉又新颖。这种方法允许设计师在尊重原有设计的同时，通过细微的调整来创造新的作品，这些改变可能包括颜色、材料、结构或其他设计元素的轻微变动。

Language model 能力的提升，以及把 language model 和 SaaS 软件相结合这两件事应该是同步进行的，**因为如果一下子改变太大，人们可能会不太适应，RAG 的好处也在于它在现有交互习惯基础上给到了更好的输出。**

 **Elad Gil ：****你提到了要在推理质量、速度以及成本之间做平衡，Notion 是如何用模型的？只使用了 Llama 还是会在不同场景中调用不同模型？**

**Ivan Zhao：**不同的公司、产品的目标不一样，选择的模型自然也不一样。Notion 会尝试各种模型，尤其当下水平最领先的开源模型，但因为 Notion 很看重推理能力，所以我们一般会调用高水平的模型。

**03.**

**RAG：知识管理的未来**

 **Sarah Guo ：****Notion Q&A 还没开放给所有人，可以给还没体验过的人讲讲 Notion 的 AI Q&A 是什么吗？**

**Ivan Zhao：**本质上 Notion 会帮助用户记忆他们输入到 Notion 中的所有内容，不只是 Notion 能这样做，绝大多数给予 RAG 的系统都能做这件事。

Language model 和 RAG 出现之前，人们之所以需要计算机是因为需要一个地方来存储信息，并且可以随时检索、调用这些信息，但检索主要依赖于关键词，并且这个词要相当精确，因此有的时候还会要求用户具备一些优化关键词的技巧。但有了 RAG 之后，language model 能够理解你输入的内容。所以，我们不需要在 Notion 中专门做信息的组织管理，因为无论我们输入了什么，我们都能顺畅地搜索出来。无论对个人还是团队公司来说，RAG 都提供了很完美的记忆能力这对于个人、公司或团队来说，相当于拥有了完美的记忆。

在此之上，如果我们把产品设计得足够好，还能够实现将合适的信息在合适的时间推送给对应的成员，不仅如此，如果我们设计得当，还可以将正确的信息在正确的时间推送给正确的人。可能 50% 以上的知识性工作都是这类任务。

Notion 可能是市场上比较早去大规模提供 RAG 相关功能的公司，但大范围提供 RAG 服务的难度比较大，Notion Q&A 还处于 waiting list 的状态，我们还在完善。

有了 RAG 之后，团队搜索的体验会完全不一样。我自己就已经改变了使用 Notion 的方式。比如我会提问 “公司什么时候搬到新办公室？”，如果团队中有人在某个文档中记录过这件事，Notion 就会回复我对应信息，我不需要再像之前那样去问其他人。

团队中的所有人，无论是设计师、工程师还是运营，每天也会在 slack 和邮件问到类似问题。要回答这些问题可能要花 10 分钟来写邮件，在此之前还要耗费 20 分钟来找到对应答案，如果算上各种等待时间，可能需要耗费半个小时以上的时间，但有了 Noton Q&A，这类问题只需要几秒钟就可以解决。RAG 已经帮我们提高了工作效率，而这还只是开始。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 **Elad Gil ：****最近一段时间关于 Agent 的讨论越来越多了，但客观来说因为某些能力还不能实现，所以 Agent 或者自动化相关的应用价值还没真正体现出来。Notion 最近也推出了 Calendar 应用，我很好奇你怎么看 AI 和日程管理之间的结合？**

**Ivan Zhao：**我自己会去这么看 AI 的能力，首先， RAG、信息 retrieval 是一类，属于知识类相关。另外一类则是 workflow 相关，我们选择用 agent 来定义这件事。人们之所以需要会议、日程这些东西是因为我们需要完成彼此大脑之间的“比特传输”，那么我可以借助一个 language model 来完成这件事吗？也许是可以实现的。最基本的环节就是，人们在敲定会议时间的那一刻，日程安排上也做出了对应变化。我们做的很多事情都涉及到了时间这个纬度，language model 可以帮我们来调整时间安排吗？我认为是可以的。

 **Elad Gil ：****听起来 retrievable 也是整个过程中很关键的部分。如果我们的日历可以自动补齐我们需要了解的关于会议、参会人员或其他相关事项的所有信息，对于用户来说相当有价值。你认为 Notion Calendar 还能在哪些环节创造价值？**

**Ivan Zhao：**它可以简化我们的工作流程，这是一个重大的突破，可以让 Agent 帮助我们完成知识类工作。

我们之所以需要沟通是因为有些工作不能由软件自动完成，需要我们进行实时处理。这也许这是一个值得思考的问题，随着 language model 的发展，我们未来的沟通会更多还是更少？我猜是更少。因为 Agent 基本上依赖于 language model，这就是沟通的未来。

*欢迎关注**海外独角兽**视频号*

*获取最前沿的科技行业资讯*

 **Sarah Guo ：****你提到 Notion 可以像大脑那样帮助用户进行信息的组织和管理，如果一个人的大脑本身就很混乱、缺乏体系，这会影响他在 Notion 或者类似系统中的信息交互方式吗？用户需要先结构化地构建一个自己的知识库，还是只需要把所有信息以信息流的方式输入就可以？**

**Ivan Zhao：**我们可能逐渐就不再需要信息结构化或者类似概念，我们之所以需要把组织和整理信息是因为只有做好这些工作才可以检索，我们需要 index 也是因为 index 就好像文件夹上的各种标签，能够帮我们快速找到各类文件，但因为 embedding 和 RAG ，我们只需要把所有信息放进这个“文件袋”，然后就可以根据需要以任意方式搜索、找到你想要的信息。信息的自由度会大大提升。

我们还可以想象这样一个场景，当我有新的 idea 时，只需要拍张照片、或者写下来一些东西，然后把它放进 Notion，Notion 就会帮我们组织、管理这些信息，如果未来我们需要用到这些知识的时候，作为一个完美的记忆助手，Notion 就会帮我们调取它们。这是 Notion 的长期愿景，我个人觉得这件事很令人兴奋。

**04.**

**AI 让 SaaS 进入新一轮 Bundling**

 **Sarah Guo ：****你是怎么思考 Notion 的 AI 战略的？这些战略是否也受到了哪些计算机技术发展历史中的启发？**

**Ivan Zhao：**我的很多直觉其实都基于一些对历史的理解，历史不是简单地重复，但总有一些相似规律。我个人认为，我们目前还处于 bundling 的阶段。《三国演义》的第一回就提到“久分必合，久合必分”，我觉得商业的运作也是如此。在 bundling 阶段之前，SaaS 行业其实已经经历过一个 unbundling 和服务分散的阶段。

Unbundling 的趋势从 2000 年代中就开始了，在这之前整个信息领域相关的产品都需要基于 Microsoft 来完成，是 典型的 building 的阶段。

PC 时代早期其实有很多各种各样的应用，比如《星际争霸》的早期版本，还有各种文本编辑器、dBase数据库软件以及其他不同的数据库软件。到了 90 年代，因为 Microsoft 提供了一个底层的操作系统，我们也随之进入了一个 bundling 阶段。随后，随着网络技术的发展，软件开始可以在 Web 上运行，这就带来了过去 10 到 15 年前的解绑和碎片化阶段，与此同时，资金成本降低带来创业门槛降低，也因此导致了信息领域的过度碎片化。

到今天，随着 AI、language model 的出现和发展，我们似乎又回到了 bundling 阶段。因为模型本质上要求将信息集中在一个地方去实现更高效的信息处理。

所以，我们今天正处于 bundling 阶段，这既是因为宏观经济的趋势，也因为 language model 的内在需求就是将信息和功能整合在一起。

 **Sarah Guo ：****如果我们仔细看Oracle 这类过去 15 年一直占据主导地位的公司，会发现它们有一个共同策略：收购同领域中排名第二的产品。因为对于客户来说单独去部署这些产品是很困难的，或者说他们更倾向于将所有东西都整合到一个单一的数据库中。我认为这与你提到的 language model 有某种相似之处。**

**Ivan Zhao：**是的，Oracel 的这个例子很好。我认为既有分发层面的 bundling，也有信息层面的 bundling，前面提到的 Oracle 更偏向于销售角度的 bundling，language model 需要的是数据和信息的 bundling。

 **Sarah Guo ：****Notion 刚起步时，最先使用 Notion 来构建知识库的是那些初创公司。今天，在 Notion 规模得到增长的同时，我们所处的宏观环境也发生了变化，初创公司的预算比以前更加紧张。你如何看待帮助企业采用 AI 进行知识管理这件事？**

**Ivan Zhao：**我们还相当早期，也还没完全实现用户的规模化。我认为，bundling 有很多好处。首先，这很方便，用户不需要在不同的界面之间来回切换就能完成任务。其次，这有助于节省成本，有了 Notion，用户就不必购买其他项目管理和 issue 跟踪的工具，从而减少了大量开支。这一点对于企业来说非常重要，尤其是在当前的经济环境下，CFO 也想降低成本。所以，bundling 确实带来了许多优势。除了方便信息管理，还能节省大量资金。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 **Sarah Guo ：****在 Notion 之外，你认为还会有哪些 SaaS 软件公司会在 AI 时代产生很大影响？**

**Ivan Zhao：**在某种程度上，SaaS 公司做 AI 可能像是一场竞赛。Notion 主要是做 bundling 和 front office 业务。

我是这么定义 “Front office” 的：可以先假设如果我们身处在 1960 年代的一间办公室里会看到哪些东西？人们桌子上会有一个用来记东西的记事本，可能还会有一台打印机，左右两旁还堆着很多文件夹，对应到 Notion，记事本相当于用户文档和笔记，文件夹则类似于 Wiki，人们身后的文件柜则可以对应到 Notion 中的关系数据库，文件柜中还会有各种小纸片来帮助整理信息。

相对应的，还会存在“Back Office”，类似于图书管理员工作的地方，back office 对应的是今天 Snowflake、过去 IBM 在做的事情。Notion 不会去碰“back office”相关的部分，我们还是聚焦我们的优势领域，就是我刚刚提到了软件界面，UI、UX 这些。

Back office 的场景和 front office 相比要更加垂直，比如专注于医疗健康领域、特定的工作流等等，并且通常还需要一个专门的地方来存储相关信息并在垂直场景中进行整合，这些场景也是可以被 AI 改造的。在法律等高度专业化的领域里，large language model 已经开始代替人类处理一些复杂任务了。

Front office 对应的任务是开放性的，back office 的则更偏特定、具体的任务，所以我认为二者之间会存在某种竞赛，但与此同时市场也很大，不一定是零和游戏。

 **Sarah Guo ：****你很看重设计，Notion 的设计也一直被外界称赞，你认为 Notion 是一个设计驱动的公司吗？你是如何在整个团队中保证设计一致性的？**

**Ivan Zhao：**我认为这个取决于我们要怎么定义设计，至少对于我来说，设计不仅仅是外观，更重要的是一个系统是如何协同工作的。在这种情况下，我们需要做出一些 tradeoff，是选择把设计集中还是分散到每个板块？有些公司或业务产品适合把设计工作下放到不同板块，尤其是那些很重运营的公司。

Notion 的价值在于提供一个统一的信息空间、一个让人们可以集中完成各种不同的任务的 workspace 。因此，这些功能需要协同高效地工作。这有点像是在构建一个操作系统或编程语言，没有人会把设计编程语言的任务分散给 50 个人来做，通常这些工作都是由一个人来完成的。

所以 Notion 的设计相当集中，有点类似于苹果公司，Apple 软硬件紧密集成开发 OS 的方式在今天很少见。在这种情况下，为了实现好的产品和良好的用户体验，我们就需要更横向、全面的思考，也因此我们的设计决策是相对集中的，更偏 Apple 的风格而不是 Amazon。

此外，我认为我们不能局限于某一种思维模式，因为很多界限其实是人为设定。Notion 80% 的设计师都会编程，他们既是设计师也是工程师，也因此在设计中可以做出很好的平衡。技术的本质是 tradeoff，好的tradeoff 能够激励用户来尝试使用新产品、引导他们形成习惯，这是最核心的。我们会的事情更多，相对于其他设计上就更能在设计上做出好的平衡，再比如设计师知道如何编程，他们就会知道如何调整设计，使其更容易实现；如果你会设计也是同理，就像在挤压空气泡泡时，找到最容易挤压的方向。

因此，我认为这种多样化的能力对我们的帮助很大，Notion 中的每一个人都在努力变得“全能”，这也使我们的团队小而精悍。相对于我们的业务规模，我们的团队人数很少，但团队中的每个人都能把自己的能力发挥到极致。我们没有固定的角色，也不需要做重复性的工作，大家都很享受这种工作方式。不过，尽管这样做有很多好处，但找到具备这样能力的人确实更难。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

延伸阅读

我们距离AGI还有多远？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Scaling能通往AGI吗？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

专访月之暗面杨植麟：lossless long context is everything

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Perplexity CEO：AI 创业公司要先做产品，后做模型

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

八问Canva：在AI时代称王还是落败？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)