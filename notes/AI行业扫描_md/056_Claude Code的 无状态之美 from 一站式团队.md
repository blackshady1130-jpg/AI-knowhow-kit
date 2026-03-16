---
url: https://mp.weixin.qq.com/s/Fa15GoM3_2CUnjdHQ3I7Nw
title: "为什么Claude Code放弃代码索引，使用50年前的grep技术？"
author: "余志臻"
captured_at: "2026-03-09T03:19:17.289Z"
---

# 为什么Claude Code放弃代码索引，使用50年前的grep技术？

![图片](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe97bCSICdmD5k5Jibib2IpkhLFtkOzvD2504vSVCg0ricAJ8DBknMIDgGN2c7LmRtoAwLDibBkZTMCkALA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/VY8SELNGe96srmm5CxquJGSP4BbZA8IDLUj8l7F3tzrm8VuILsgUPDciaDLtvQx78DbkrhAqOJicxze5ZUO5ZLNg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

👉目录

1 引言：一个看似倒退的选择

2 理解状态的本质

3 无状态思想的历史脉络

4 无状态设计的优势

5 现实的权衡

6 AI时代的新思考

当AI编程助手都在比拼谁的索引更智能时，Claude Code选择了每次都实时搜索、不保留任何状态。这个反直觉的设计背后，是对Unix哲学的现代传承，也是对“什么才是好工具”的重新定义。

关注腾讯云开发者，一手技术干货提前解锁👇

7小时不间断直播，看腾讯最新黑科技，赢百份周边好礼！

## 01

引言：一个看似倒退的选择

最近，Claude Code的技术选择引发了不少讨论。

有观点认为，Claude Code与Gemini放弃代码索引是“一步烂棋”。Milvus的技术博客更是直言不讳：“Claude Code的grep-only方式会烧掉太多tokens”。在HackerNews的讨论中，有开发者质疑：“Claude用grep，Cursor用向量搜索——我们是在技术倒退吗？”

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

当主流AI编程助手纷纷采用向量索引实现语义搜索时，Claude Code却选择了grep——这个诞生于1973年的命令行工具。它不建立持久的代码索引，不预测编码意图，每次搜索都是实时执行。

根据Anthropic团队在5月份的博客访谈《Claude Code: Anthropic's Agent in Your Terminal》，他们测试了RAG（向量索引）等多种方案后，最终选择了"agentic search"——就是使用glob、grep这些常规的代码搜索。令人意外的是，这种方式“在性能上大幅超越了所有其他方案”。

这种取舍并非一时兴起，而是一条贯穿计算机科学 50 年的设计哲学，从Unix管道到REST API，从MapReduce到Serverless， 无状态（Stateless）设计在计算机历史上一次次证明了它的价值：通过放弃复杂的状态管理，系统获得了更好的可组合性、可靠性和可扩展性。

本文将探讨“无状态”这个设计理念——它不是简单的“不保存数据”，而是关于如何明智地选择在哪里、以什么方式管理必要的状态。理解了这个设计哲学，你就会明白Claude Code的选择背后的深层逻辑。

> 每个计算时代都在重新发现同一个道理：有时候，遗忘比记忆更强大。

## 02

理解状态的本质

   2.1 什么是状态？

让我们从最简单的例子开始理解状态的本质。

想象两种不同的计算方式：

有状态的计数器：就像一个记账本，每次调用都会在之前的基础上累加。第一次调用返回1，第二次返回2，第三次返回3……它“记住”了之前发生的一切，每次的输出都依赖于历史。

无状态的加法器：就像一个计算器的加法功能，给它输入2和3，无论何时、无论调用多少次，结果永远是5。它不知道也不关心之前发生了什么，每次都是全新的计算。

这个区别看似简单，却是理解整个系统设计的关键。用数学语言表达：

-   无状态：Output = f(Input)

-   有状态：Output = f(Input, History)

   2.2 生活中的状态

为了更好理解，看看生活中的例子：

银行账户是有状态的。你的余额是所有历史交易的累积结果。银行必须记住每一笔存取款，否则你的钱就消失了。

汇率转换是无状态的。100美元换人民币，只需要知道当前汇率，不需要知道你上次换了多少。

对话是有状态的。当朋友说“还记得昨天那件事吗？”，需要共同的记忆才能继续。

翻译是无状态的。把"Hello"翻译成“你好”，不需要知道之前翻译过什么。

这个区别看似简单，却深刻影响着系统设计的方方面面。

## 03

无状态思想的历史脉络

   3.1 数学起源：纯函数的优雅（17世纪）

无状态的思想并非始于计算机。17世纪，莱布尼茨和牛顿发展微积分时，数学函数就是无状态的。f(x) = x²，无论何时计算f(3)，结果都是9。

这种确定性和可预测性，成为后来所有无状态设计的理论基础。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

   3.2 Unix革命：管道的哲学（1973）

真正将无状态思想带入实践的，是Unix的创造者们。

1973年，Doug McIlroy在贝尔实验室提出了管道（pipe）概念。他用了一个绝妙的比喻：“我们需要某种方式把程序连接起来，就像花园里的水管——当需要以另一种方式处理数据时，只需拧上另一段管子。”

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Unix管道的优雅体现在它的组合方式上。想象一个处理日志文件的场景：你需要找出所有错误信息，统计每种错误出现的次数，并显示最常见的10种错误。

在Unix中，这个复杂任务可以通过管道符号（|）将五个简单工具串联完成： bash。

```
# Unix管道的优雅
```

每个工具都是无状态的：筛选工具不知道数据来自文件读取，排序工具不关心会被统计工具处理。每个工具只做一件事，并把这件事做到极致。

这种设计带来了意想不到的威力——5个简单工具理论上可以产生120种不同的组合方式。如果这些工具是有状态的、相互依赖的，大部分组合都会失效。这就是无状态设计的魔力：通过放弃记忆，获得了无限的组合可能。

   3.3 函数式编程的批判（1977）

1977年，John Backus在图灵奖演讲中投下一枚炸弹：《编程能否从冯·诺依曼风格中解放出来？》

python

```
# 冯·诺依曼风格（有状态）
```

他批判了主流的命令式编程方式。传统的求和方式就像记账：创建一个“总和”变量，初始值为0，然后逐个遍历数组，每次都修改这个变量，把新的数字加到已有的和上。**这个过程充满了状态变化**——变量在不断被修改，每一步都依赖前一步的结果。

而函数式的方式完全不同：它把求和看作一个纯粹的数学运算，通过组合“加法”这个基本操作来处理整个数组。没有变量被修改，没有状态在变化，只有数据在函数间流动。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Backus认为，状态修改是程序复杂性的根源。当程序中充满了不断变化的状态时，理解和调试都会变得困难。这个观点深刻影响了整整一代语言设计。

   3.4 分布式时代的必然选择（2000年）

2000年，Roy Fielding在博士论文《Architectural Styles andthe Design of Network-based Software Architectures》 中提出REST架构，将无状态作为核心约束。他的理由很简单：在分布式系统中，状态是扩展性的敌人。

对比两种设计：

-   有状态：服务器记住用户会话，但请求被分配到其他服务器时就失效了。需要在所有服务器间同步会话，复杂且昂贵。

-   无状态：每个请求携带JWT令牌，包含所有必要信息。任何服务器都能处理，可随意增减服务器。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这就是为什么 REST 能支撑互联网规模的应用——以无状态为前提的设计降低了横向扩容的复杂度，成为互联网级系统的基础实践之一。

   3.5 分布式时代的必然选择（2000年）

2014年，Lambda带来了一个激进的承诺：“假装每次函数调用都在全新的机器上运行”。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这个设计哲学很纯粹：开发者写函数时必须假设什么都不会被保留——没有全局变量、没有临时文件、没有数据库连接。但实际执行时，Lambda会悄悄复用容器来提升性能。这是个聪明的把戏：强制无状态的编程模型，但在实现层做优化。

为什么这么设计？看看传统服务器的痛点：

-   负载突增时手忙脚乱地加机器

-   闲置时还在烧钱

-   一台服务器挂了，上面的状态也没了

Lambda的无状态让这些问题消失了。黑五促销？函数自动扩展到上万个实例。凌晨三点没人访问？成本归零。某个实例崩溃？下一个请求在新实例上执行，用户无感知。

但“纯粹无状态”在现实中总要妥协。Lambda允许512MB的/tmp空间，容器复用时全局变量会保留。Cloudflare Workers走得更极端——完全没有文件系统，10毫秒CPU限制，换来的是全球任意节点执行。Azure Functions则务实地提供了Durable Functions，承认某些工作流确实需要状态编排。

Serverless的“无状态”不是技术洁癖，而是一种交易——用编程模型的约束，换取运维的简单和成本的弹性。你失去了对执行环境的控制，但获得了不用管理服务器的自由。

## 04

无状态设计的优势

   4.1 可组合性：乐高积木vs精密手表

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

无状态组件就像乐高积木，可以自由组合来解决不同问题：

bash

```
# 今天的需求：找出错误日志中的IP地址
```

注意到了吗？每个新需求都是在已有组合上的微调。我们不需要重写整个程序，只需要像玩乐高一样，替换或添加几个模块。每个工具都不知道会被如何组合，所以能被任意组合。

相比之下，有状态系统像精密手表——每个齿轮都精确咬合，牵一发而动全身。想要改变功能？对不起，你需要重新设计整个机芯。

这就是为什么Unix哲学历经50年依然生命力旺盛——通过保持每个组件的独立性，获得了应对未知需求的灵活性。

   4.2 并行的自然性：无冲突的世界

这是我最喜欢展示的例子，想象你需要在一个大型代码库中搜索需要的文件：

传统串行方式：就像一个人拿着手电筒，逐个房间地搜索。搜索第一个文件，完成后搜索第二个，然后第三个……在我的测试中，搜索整个项目耗时42秒。

并行方式：就像派出16个人，每人负责一部分房间，同时搜索。结果呢？同样的任务只需要3.8秒。

10倍的性能提升！ 这不是什么高深的优化技巧，仅仅是因为搜索工具是无状态的：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   搜索文件A不会影响搜索文件B

-   没有共享变量需要加锁保护

-   没有竞争条件需要小心处理

-   16个CPU核心可以真正独立工作，互不干扰

如果搜索工具需要维护全局状态——比如记录搜索历史、更新进度条、或者保持结果的顺序——并行化会变得复杂且低效。你需要处理线程同步、锁竞争、死锁风险……最后可能发现，并行版本甚至比串行更慢。

无状态设计让并行变得自然而然。这就是为什么现代的大数据处理框架（MapReduce、Spark）都采用无状态的计算模型——不是因为他们不想要状态，而是因为只有这样才能真正发挥成千上万个核心的计算能力。

   4.3 简单性：没有生命周期管理

看看有状态服务需要背负的沉重包袱：

启动时的仪式：

-   初始化连接池，确保有足够的数据库连接

-   加载配置文件，恢复上次的运行状态

-   检查未完成的任务，重建内存缓存

-   启动后台线程，开始心跳检测

关闭时的清理：

-   保存当前状态，以便下次恢复

-   等待所有请求处理完成，不能丢失用户数据

-   优雅地关闭所有连接，释放所有资源

-   通知其他服务自己要下线了

崩溃后的恢复：

-   检查数据一致性，是否有损坏？

-   恢复中断的事务，用户的钱有没有丢？

-   重建索引和缓存，性能能否恢复？

这就像经营一家24小时营业的便利店——开店要准备货架、收银系统、监控设备；关店要盘点库存、结算账目、清理卫生；如果突然停电，还要检查冷藏柜、恢复收银数据、安抚排队的顾客。

而无状态服务就像计算器——插电就能用，断电就停止，重启立即恢复。没有状态恢复流程，没有繁琐的清理工作，崩溃了重启就行。

这种简单性不仅降低了开发复杂度，更重要的是提高了系统的可靠性。复杂的生命周期管理往往是bug的温床——忘记释放资源导致内存泄漏，清理顺序错误导致死锁，恢复逻辑有漏洞导致数据不一致……

   4.4 可测试性：确定性的力量

测试无状态函数就像测试数学公式——2+3永远等于5。不需要准备环境，不需要清理状态，不需要模拟依赖。

测试有状态系统则像做化学实验，处处是坑：

-   环境污染：其他测试留下的全局状态、数据库遗留数据

-   依赖地狱：模拟数据库、消息队列、外部API

-   时序问题：测试顺序依赖、并发干扰、异步等待

而无状态则带来确定性——相同输入永远产生相同输出。测试失败时，你知道是逻辑错误，而不是环境问题。

## 05

现实的权衡

   5.1 什么时候需要状态

有些场景，状态不是可选项，而是必需品：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**游戏世界需要持续性**。玩家辛苦打下的装备、升级的等级、探索的地图，这些都是游戏体验的核心。没有人愿意玩一个每次登录都要重新开始的RPG游戏。

**用户界面需要响应性**。购物车里的商品、表单填写的内容、页面滚动的位置——这些临时状态虽然不需要永久保存，但在用户会话期间必须保持，否则每次操作都要重新来过。

**资源管理需要经济性**。数据库连接、网络套接字、线程池——这些都是昂贵的资源。每次请求都创建新连接不仅慢，还可能耗尽系统资源。连接池通过复用连接，用少量的状态换取了巨大的性能提升。

   5.2 如何选择？一个简单的判断标准

我最喜欢用这个问题来判断：

> **“如果系统崩溃重启，用户能接受从零开始吗？”**

-   编译器崩溃了？重新编译就行 → 无状态

-   游戏崩溃了？存档丢失不可接受 → 有状态

-   搜索崩溃了？重新搜索就行 → 无状态

-   购物车崩溃了？商品丢失很恼人 → 有状态

这个简单的问题能帮你快速定位系统的本质需求。

   5.3 混合策略：现实世界的智慧

无状态和有状态，看上去是布尔变量true/false般的两个完全对立的值。但这其实是中文语境里的一个误解——英文的 stateless/stateful 并非“无/有状态”的二元开关，更像 -less/-ful 的“程度词”：强调依赖的轻重与记录方式的取舍，而非是否“完全没有/完全存在”。

真实系统也很少是纯无状态或纯有状态，而是智慧地混合使用。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

最常见的模式：无状态计算 + 有状态存储

这就像餐厅的运营模式：服务员（无状态）可以随时换班，任何服务员都能为任何桌子服务；但收银系统（有状态）必须准确记录每一笔账单。应用服务器是无状态的，可以随意扩展；数据库是有状态的，负责持久化。

现代云架构几乎都采用这种模式：

-   无状态的API服务器 → 有状态的数据库

-   无状态的Lambda函数 → 有状态的DynamoDB

-   无状态的容器 → 有状态的Redis缓存

Event Sourcing：用无状态事件构建有状态系统

不直接存储状态，而是存储所有导致状态变化的事件。账户余额不是一个数字，而是所有存取款事件的累加结果。就像银行的流水账——每笔交易都是独立的、不可变的，但累加起来就是你的账户余额。这种方式既保留了完整的历史，又能灵活地重建任意时刻的状态。

   5.4 核心洞察

选择无状态还是有状态，不是技术信仰的问题，而是工程权衡的艺术。无状态不是目的，而是手段——它帮助我们构建更简单、更可靠、更可扩展的系统。

状态并不是坏的，无管理的状态才是问题的根源。最好的设计不是完全无状态，而是在正确的地方、以正确的方式管理必要的状态。就像生活中的断舍离——不是要扔掉所有东西，而是只保留真正重要的，并且妥善管理它们。

## 06

AI时代的新思考

   6.1 Claude Code的选择：具体的技术对比

回到开头的质疑，让我们用事实说话。

根据Anthropic团队在5月份的博客访谈《Claude Code: Anthropic's Agent in Your Terminal》，他们测试了RAG（向量索引）等多种方案后，最终选择了"agentic search"——就是使用glob、grep这些常规的代码搜索。令人意外的是，这种方式“在性能上大幅超越了所有其他方案”。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

当前主流的AI编程助手采用了三种截然不同的技术路线：

-   Cursor的向量索引方案： 采用AI原生设计，使用Merkle树快速索引代码库，将代码智能分块后生成向量嵌入，存储在远程向量数据库Turbopuffer中。优势是语义理解——搜索“用户认证”能找到login、authenticate、verifyUser等相关函数，即使没有准确关键词。

-   JetBrains的传统索引方案： 经过20年打磨的索引系统，通过深度解析创建PSI树和stub索引。支持强大的代码导航、重构和智能提示，是企业级IDE的黄金标准。

-   Claude Code的无索引方案： Claude Code选择了最简单直接的方案——每次搜索都是实时执行，不依赖任何预构建的索引。根据逆向工程分析，它内部包含GrepTool（支持完整正则表达式的内容搜索）、GlobTool（文件模式匹配）等经典Unix工具（当然随着架构迭代现在可能有一定优化）。就像直接在终端输入grep命令一样简单纯粹。

   6.2 为什么“健忘”反而更好？

这个反直觉的选择，背后有四个关键优势：

1\. 零配置的自由 大型项目中，Cursor需要上传生成嵌入，IntelliJ需要构建索引——往往耗时几分钟。Claude Code？立即可用。更重要的是无状态命令带来的组合能力：

bash

```
tail -f app.log | claude -p "如果看到异常就通过Slack通知我"
```

这种管道组合的优雅，是索引系统永远无法提供的。

2\. 确定性的价值 向量搜索失败时，调试是噩梦——是嵌入质量？语义偏差？索引过期？grep的行为完全可预测：搜索"processPayment"就是精确匹配，失败原因只有一个——关键词不匹配。这种确定性在调试复杂问题时无比宝贵。

3\. 隐私的根本保障 Cursor需要上传代码生成嵌入向量。虽然声称“不存储”，但学术研究已证明可从嵌入反推原始内容。Claude Code的grep完全本地执行，从架构上杜绝了泄露可能——不是通过加密，而是让泄露变得不可能。

4\. 维护的零成本 没有“索引卡住”，没有“缓存损坏”，没有后台进程偷偷吃CPU。每次搜索都是全新开始，每次结果都是最新真相。

   6.3 不同场景，不同选择

这不是技术优劣的绝对判断，而是设计哲学的不同选择。每种方案都有其最适合的场景：

Cursor的向量索引适合创意编程场景——当你大概知道要什么但不确定具体名称时，语义搜索能帮你探索代码库。它特别适合学习新项目或寻找灵感。

JetBrains的传统索引是企业级开发的黄金标准——当你需要可靠的重构、精确的类型检查、复杂的代码导航时，经过20年打磨的索引系统无可替代。

Claude Code的grep方案则是Unix哲学的现代传承——当你重视简单、可控、可组合时，当你需要绝对的确定性和隐私保护时，这种“原始”的方案反而是最先进的选择。

正如Boris所说：

> “Claude Code不是一个产品，而是一个Unix工具。”

   6.4 无状态之美：在AI时代的新意义

Claude Code的选择，让我们重新思考什么是“智能”。 在一个AI无处不在的时代，真正稀缺的不是智能，而是**可预测性**；不是功能的丰富，而是**行为的确定**；不是记住一切，而是**知道何时遗忘**。

这就是为什么grep在2025年依然重要，为什么Unix哲学历经50年依然闪光，为什么Claude Code的“倒退”其实是一种清醒。

> 简单的工具活得最久，“健忘”的设计最自由。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

致谢:

特别感谢我的Mentor浩哲在本文撰写过程中提供的宝贵启发与建议。

\-End-

原创作者｜余志臻

感谢你读到这里，不如关注一下？👇

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

📢📢来抢开发者限席名额！点击下方图片直达👇

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

你平时在IDE里用“全局搜索”多还是“语义搜索”多？欢迎评论留言分享。我们将选取1则优质的评论，送出腾讯云定制文件袋套装1个（见下图）。9月23日中午12点开奖。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe979Bb4KNoEWxibDp8V9LPhyjmg15G7AJUBPjic4zgPw1IDPaOHDQqDNbBsWOSBqtgpeC2dvoO9EdZBQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=k6ek17wp&tp=webp#imgIndex=21)

![图片](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe95pIHzoPYoZUNPtqXgYG2leyAEPyBgtFj1bicKH2q8vBHl26kibm7XraVgicePtlYEiat23Y5uV7lcAIA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=qxwo93ci&tp=webp#imgIndex=25)