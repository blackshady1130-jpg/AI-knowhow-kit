# 对话 Google 首席 Jeff Dean：概率性执行的 Agent 时代，Infra 必须重塑！

Original Guanlan Guanlan | Agentic Infra

声明：本文内容基于作者与 Jeff Dean 的真实对话整理，稿件经 Jeff Dean 本人审阅并授权发布。

过去我们追求五个九的高可用性，建立在一个不可动摇的前提上：代码的逻辑是确定的。但现在，当越来越多代码由 Agent 生成，系统底层的基本执行单元本身变成了概率性的。

和 Google DeepMind 首席科学家 Jeff Dean 探讨这个话题时，得出一致判断：Agent 对 Infra 最深的冲击，是引入了一种全新的执行语义。

## 当系统的基本执行单元不再是确定的

AI 生成代码的体量正在快速逼近甚至超过人类直接编写的代码量。有些团队已经在用一个模型 review 另一个模型写的代码。

Jeff 的原话："It can work, but it makes me a little uncomfortable."

当执行者本身开始变成概率性的，很多过去默认成立的基础设施假设将会受到严峻挑战。

## Agent 时代的可靠性：可能要靠更重的手段

让独立的模型把同一个算法写两遍再做投票，或者同时跑三个副本。这是 heavy hammer，但在生成质量还不够稳定时可能最现实。

AI 让生成代码变得言出法随，却让执行的边界变得异常模糊。它把更多责任重新压回了 Infra 执行层。

## 计算图和可恢复性

当模型真正进入系统内部时，整个 Infra 形态会变成多个子模型、工具、判断节点拼出来的执行网络，越来越像一张 computation graph。

Jeff 认为 ML 研究者真正想要的不是同步本身，而是 Reproducibility。同步只是为了换来可重现的一种很贵的办法。这跟 Resumability 原语很接近——系统能不能回到一个有定义的状态再继续往前走。

## 语义化工作区

更好的方向是一个类似 KV Store 的语义化工作区。做 Checkpoint 时留下来的是有意义的 working set，而不是整块内存的无差别转储。背后是朴素原则：只保存 Root State，Derived State 能重算的就不要硬存。

## 无限上下文 vs 可重入的状态模型

真正稀缺的不是更大的 context window，而是能不能把不同类型的信息分层组织好。Memory 的核心不是存得多少，而是状态组织得对不对。

## 结论

执行层 Infra 正在重新变成系统工程里最核心的问题。今天我们连一个长时间运行、带真实权限、已经产生外部副作用的 Agent 在跑崩之后到底应该如何恢复，都还没有形成广泛共识。只要这一点没解决，很多看起来已经能跑的 Agent system，本质上都还只是 demo。

---
Source: https://mp.weixin.qq.com/s/8TYMn2DVE6vTo4xL64CkJA?scene=1
