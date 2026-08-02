# 一夜之间，Claude Code删掉了80%系统提示词

> 原文链接：[https://mp.weixin.qq.com/s/mxs3eS7BDq1mePfGK-mKnA](https://mp.weixin.qq.com/s/mxs3eS7BDq1mePfGK-mKnA)
> 发布方／作者：机器之心
> 发布时间：2026年7月25日 15:30

---

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gW889cR13aBX42evqQIRibKlicoCrHPEpT0tQiceNphESCa2eJTqstP8G0yqMTkeMFrOGue6kOyCKdTkA/640?wx_fmt=png&from=appmsg#imgIndex=0)

编辑｜泽南、杨文

「我们删除了 80% 的 Claude Code 系统提示，这是我们从编写系统提示词、Skill 和 Claude.MD 中学到的。」

本周五，[Claude Opus 5 正式上线](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651046545&idx=1&sn=f5d29ec30342354a6bf21315e6d0eec1&scene=21#wechat_redirect)，Anthropic 技术团队成员 Thariq Shihipar 立即发帖，向我们介绍了新一代大语言模型之上，工程方面的趋势变化。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqHUGrRX5RBn4JJTfibfTQFsqt7pWrd9FeRLG6NtwPMemXImZKDicMwd7sgFHGezyeoranjgLmx5Bt36ibB4EktcNdvf2IWm1w06p0/640?wx_fmt=png&from=appmsg#imgIndex=1)

Anthropic 自己发现，在 Claude Opus 5 这种新一代强推理模型发布后，旧的提示词工程范式可能已经过时，甚至在起反作用。

简单来说，就是模型越强，就越不需要「保姆式」指导，冗长的手写规则除了浪费 token，还有可能会让效果变差；新的 Claude.md 应该保持绝对的精简，高绩效团队控制在 60 行以内，通常绝不要超过 300 行；大砍系统提示词之后，可以把那些特定任务的上下文交给 Skill。

可见，随着大模型的参数化知识和推理能力越来越强，提示词工程也要向整体架构的高度转变。

这让我们不由得感叹，时代变了。

让我们看看 Anthropic 自己是如何解释的：

Anthropic 此前介绍过如何为新一代 Claude 5 模型编写提示词，以及如何与模型迭代协作、在过程中逐步明确真正想构建的东西。

但当用户向 Claude 发送一条消息时，提示词只是模型所获上下文中的一小部分。上下文中的绝大部分内容，来自系统提示词、Skills、CLAUDE.md 文件、记忆以及其他来源，这称为上下文工程（context engineering）。无论你是在使用 Claude Code，还是在构建自己的 Agent，它都会显著影响最终产出的质量。

与提示词不同，上下文通常用于多个请求，因此不可能写得那么具体。

那么，在根本不知道用户会输入什么提示词的情况下，该如何为 Claude 编写这类通用的提示和指导？

随着 Claude 自身能力的演进，这件事的难度可能超出预期。

最近，Anthropic 就发现面向新一代 Claude 模型的提示方式出现了一次很大的跃迁：对于 Claude Opus 5、Claude Fable 5 这类模型，团队删掉了 Claude Code 系统提示词中 80% 以上的内容，而在编码评估上没有观察到任何可测量的性能损失。

以下是 Anthropic 在为这一新世代模型编写提示时总结出的经验，以及开发者可以如何用它来更新自己的上下文工程实践。这些最佳实践已被沉淀进 claude doctor —— 在 Claude Code 中使用 /doctor 命令，就能自动把 Skills 和 CLAUDE.md 文件调整到合适的规模。

给 Claude 松绑

总体来看，Anthropic 发现自己对 Claude Code 施加了过多约束，系统提示词如此，CLAUDE.md 文件和 Skills 同样如此。

举个例子，团队翻阅内部使用 Claude Code 的对话记录时，常常在同一次请求中看到互相矛盾的指令。系统提示词、Skills 和用户请求彼此打架，一边说「酌情保留文档」，另一边却写着「禁止添加注释」。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqH5jEHt7g3sITHGaQCdElxpOMd4mcxxgaCIHOYXGh7wXo1Zq33NcvwKNX0gIf8VibD7AWNo2zxYepQU5ibTWF4JeD1RDkFlguDr4/640?wx_fmt=png&from=appmsg#imgIndex=2)

一般来说，Claude 能够读懂用户的真实意图并给出正确答案，但它必须先在这些重叠、冲突的指令之间反复权衡，才能决定该怎么做。

这些约束在过去确实是必要的，它们用来规避最坏情况。但团队后来发现，其中很多都可以删除，转而让模型依据周边上下文和自身判断力行事。

此外，Claude Code 如今拥有的工具也多得多。过去 Claude 主要依赖 CLAUDE.md 作为记忆、信息和指引的来源。而现在有了记忆、artifacts 和 Skills，Claude 可以借助它们创造出跨会话加载与共享上下文的新方式。

昔与今

过去的一些上下文工程「最佳实践」，如今已经沦为误区。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqEGaqhTw1GbZxYFevuHIAVg1dhnTqOLBJ22Hiciaiblrkrl6m8CEXvvH4gR4m7ohPgjTylm08aYkPQBpUpziad2hmmP4RGJIrrVaFk/640?wx_fmt=png&from=appmsg#imgIndex=3)

昔：给 Claude 定规则 → 今：让 Claude 自行判断

Claude Code 刚推出时，Anthropic 团队必须确保它不会踩到最坏情况的雷区，比如删除文件。这意味着要给出一些语气很强、但并不总是成立的指令。

例如，系统提示词里曾经写着：

> 写代码时默认不写注释。绝不要写多段式 docstring 或多行注释块 —— 最多一行短注释。除非用户明确要求，否则不要创建规划、决策或分析类文档 —— 依据对话上下文工作，而不是根据中间文件。

但对某一类提示词而言，这条指令是错的。就文档而言，用户可能有自己的偏好，某些特别复杂的代码，也确实需要多行注释块来说明。

话虽如此，在没有这些护栏的情况下，旧模型写出的注释在很多场景下都是错的，团队只能接受这种取舍。而新模型判断力更好，无需显式规则也能把这类决策处理得很妥当。

在新的系统提示词中，写法变成了：

> 写出的代码要读起来像它周围的代码：匹配其注释密度、命名方式和惯用写法。

昔：给 Claude 举例子 → 今：设计好接口

关于工具使用，过去的第一准则是：给 Claude 提供使用示例。但在最新的模型上，Anthropic 团队发现示例反而会把模型约束在某个特定的探索空间里。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqGVicuLhptZSia3x3nbJZ1iaeriaLEQRrQ2tjbLwrhOX77Cyibp15gmjkPuaichcWQKmvy3QnQRU7VjP05FAjZwZ59b8EyeDr9nLRANw/640?wx_fmt=png&from=appmsg#imgIndex=4)

与其堆砌示例，不如多花心思在工具、脚本和文件的设计上，即 Claude 能拿到哪些参数？这些参数如何才能更具表达力？

以 Todo 工具为例，仅将状态列为待处理、进行中和已完成三个枚举值，就能提示 Claude 如何使用该工具。而「始终只保留一项处于进行中状态」这条说明，则清晰界定了所期望的行为。

昔：一股脑全写在前面 → 今：渐进式披露

由于 Claude Code 聚焦于编码，其系统提示词里塞进了关于代码评审和验证的详尽说明。这些内容并非总能用上，但一旦用上就至关重要。

如今，Claude Code 已经非常擅长渐进式披露 —— 在恰当的时机加载恰当的上下文。比如，团队把验证和代码评审拆成了独立的 Skills，供 Claude Code 按需调用。

渐进式披露不只适用于 Skills，也适用于工具。部分工具采用「延迟加载」：Agent 必须先通过 ToolSearch 检索出完整定义，才能调用。这样就能提供更多工具（比如 Task 类工具），而它们在被真正需要之前不占用任何上下文。

同样的思路也适用于开发者自己的 CLAUDE.md 和 SKILL.md。一个常见的误解是，必须把所有可能用到的实践一股脑塞进这些文件，否则 Claude 就找不到。实际上，请考虑构建一棵文件树，让它们在合适的时机被加载。

昔：反复强调 → 今：简洁的工具描述

早期的 Claude 模型有时需要重复指令，也更倾向于听从上下文窗口末尾而非开头的内容。于是系统提示词里既有对工具的引用，工具描述中又有一套说明。

Anthropic 发现这些重复内容完全可以删掉：把工具的使用说明放进工具描述里，而不是系统提示词中。

昔：把记忆写进 CLAUDE.md → 今：自动记忆

过去，用户被鼓励用 # 快捷键把内容自动写入 CLAUDE.md，以此保存到 Claude 的记忆中。

而现在，Claude 会自动保存与当前工作以及与用户相关的记忆。

昔：简单的规格文档 → 今：丰富的参考材料

在 plan 模式下，Claude Code 一直高度依赖 markdown 格式的计划文件。把计划存成文件，便于 Claude 在需要时回查。另一条类似的最佳实践，是把规格文档存放在代码库中，供 Claude 在长周期项目中随时参考。

但 Anthropic 发现，Claude 已经能够驾驭复杂得多的参考材料。除了简单的 markdown 文件，Claude 还可以引用由我们新的 artifacts 功能生成的 HTML artifact。

开发者也可以用代码本身作为参考材料。一份规格说明可以是一套详尽的测试用例，也可以是另一个代码库中某个待移植的函数。

评分标准（rubric）是另一种形式的参考材料。借助评分标准，Claude 可以通过动态工作流、并派生出验证者智能体（verifier agents），来尝试还原并校验开发者在某个领域中的品味（比如，什么样的 API 设计才算好设计）。

落到你自己的上下文里

把上面这些串起来，在实际组装上下文时应该是什么样子？

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqHja1zO3xODBOoMzjSYNogbvgaq9fiaiaVmQOKyN9jAniaB75KtmVGGwwZjmz1UMTxTHrz2uZq8gYVKEzGglQy2ScD1Yb0p0G54XA/640?wx_fmt=png&from=appmsg#imgIndex=5)

系统提示词

系统提示词与产品语境高度绑定。它告诉 Claude 自己身处什么产品、在做什么事。对 Claude Code 而言，你基本不会去改动它；但如果你在构建自己的智能体框架（agent harness），这里值得你投入大量精力。

CLAUDE.md

保持 CLAUDE.md 轻量：简要说明这个仓库是做什么的，然后把大部分 token 花在代码库中的「坑」上。比如，团队可能把所有类型定义集中放在一个大文件里，别处一概没有 —— 这类信息才值得写。避免陈述那些 Claude 只要看一眼文件结构或仓库就能知道的「显而易见」的事。

更细的内容用渐进式披露来处理。比如，如果有若干套独特的工作验证流程，就做成一个验证 Skill，然后在 CLAUDE.md 中引用它。

Skills

把 Skills 看作轻量级指南，让 Claude 在需要时能找到信息。除非是极其关键的领域，否则不要把它们写得过度约束。

对于篇幅较长的 Skill，尽可能采用渐进式披露，即拆成多个文件，分而治之。

Skills 最能发挥价值的地方，是承载那些属于开发者本人、其团队或其产品所特有的观点、知识和最佳实践。

参考材料

可以用 @ 提及文件，把它们作为参考材料引入。参考材料让 Claude 能够查阅当前计划的深层细节。

这些材料可以是规格文件、设计稿，甚至是整个代码库。总体而言，优先选择以代码形式存在的文件，它们能给 Claude 提供清晰、高保真的指令，而且用的是它非常熟悉的语言。举例来说，一份 HTML 设计稿的效果，通常会好过对设计的文字描述或一张截图。

试着做减法

在系统提示词、Skills 和 CLAUDE.md 之间，开发者或许也需要像 Anthropic 一样做一轮简化。新推出的 claude doctor 命令可以自动帮助完成这件事。

参考链接：

https://x.com/trq212/status/2080710971228918066

© THE END

转载请联系本公众号获得授权

投稿或寻求报道：liyazhou@jiqizhixin.com
