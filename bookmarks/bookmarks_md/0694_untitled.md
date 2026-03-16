---
url: https://mp.weixin.qq.com/s/yXKMNgfh4ntyTdKfHbceLw
title: "大，就聪明吗？论模型的“尺寸虚胖”"
description: "本文作者：\\x0d\\x0a金色传说大聪明"
author: "金色传说大聪明"
captured_at: "2026-03-08T12:57:40.837Z"
---

# 大，就聪明吗？论模型的“尺寸虚胖”

你可能刷过这样的新闻：

> 一个只有 27B 参数的 Gemma-3，竟和 671B 参数 DeepSeek V3 不相上下。世界又要变天了

后面，可能还带个图，像这样：

![Dense VS MoE](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYpg8MPzeyGE8iakNdHfXFBY0SdxIdbBCKCxia8TTA159ibLO2BliauFwnMdaXwpblfQNWAjtib9w2ZNZiaA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "null")

Gemma：我 27B

**这种“技术奇迹” ，总被媒体反复包装成“一夜变天”** ，但其实并不新鲜：

-   • 大模型说：我参数更大、上限更高。

-   • 小模型说：我表现差不多，推理还便宜。

-   • 厂商都在说自己赢了，**读者却越来越搞不懂这到底在比什么。**

**细究起来，这表面是在做模型对比，实则是两种语言体系在鸡同鸭讲**，而参数恰成了“最容易理解、但最容易误导”的数字，如同：用人口数量，来判断足球水平。

我想借着这个话题，来聊聊几个核心问题：

-   • 为什么参数量大 ≠ 实际效果强？

-   • Dense 和 MoE 到底是怎么一回事？

-   • “看起来很大”的模型，到底动用了多少能力？

-   • 在大模型持续扩张的趋势下，小模型还有哪些“后发机制”？

## 大，不一定“聪明”

我们说“参数量大 ≠ 实际效果强”，不是在否定参数的意义，而是在拆一个经常被误用的判断标准。**最常见的误区，就是把不同类型的模型，拉到同一个坐标轴上用参数量做对比：而它们，本就没有可比性。**

**Gemma-3 是 Dense 架构，也就是稠密模型，它的全部 27B 参数在使用中都会被激活**，全部参与计算，属于“全员出战”的结构。

**DeepSeek V3 是 MoE 架构（Mixture of Experts）**，也就是混合专家模型。它的总参数量高达 671B，但每次推理只会激活其中一小部分专家网络，**实际参与计算的大约是 37B**。剩下的大多数参数处于“待命状态”。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Dense VS MoE

**你看到的是 671B vs 27B，但模型实际调用的是 37B vs 27B：这看上去体量悬殊，实则差别不大**。所以说，参数比较本身没问题，问题在于**不能混着比**。

当然了，在同一架构内（比如 Dense 对 Dense），参数依然是判断能力上限的重要指标；**但跨架构直接对比参数数量，得出的“谁强谁弱”往往是错位的。**

## MoE 的由来

接着回来说说参数：**参数的增加能带来“规模效应”——也就是能力的非线性跃迁**。因此，各家模型才持续堆大，从 GPT-2 到 GPT-3，再到 PaLM、Gemini、Qwen，每一代都在冲上限。

只不过，**Dense 架构的增长曲线实在太“正经”了**。随着参数规模增大，算力成本也得不断翻翻，几乎没有优化空间。当参数飙升到几千亿、上万亿时，一轮训练就要烧掉上千万美元，硬件和能源的门槛也迅速被拉高。模型越大，训练成本越高，硬件要求越严，能做的人越来越少。

**MoE 的到来，正是为了在不炸成本的前提下，继续扩容。**

MoE 并不是哪个厂商的独门绝技，而是渊源已久。**早在1991年， Michael I. Jordan 和 Geoffrey E. Hinton 就提出这个思想**。只不过当时受限于工程能力，难以真正落地。直到2017年，Google 的 Jeff Dean 团队将 MoE 应用于 LSTM 架构，训练出了一个 137B 参数的模型，参数规模巨大，但计算开销却没有爆表，这一尝试也正式为大模型扩容打开了新路。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Adaptive Mixtures of Local Experts

2020年，Google 推出结合 Transformer 架构的 Switch Transformer，参数量飙升至 1.6 万亿。这并不是为了炫数字，而是为了验证一个核心概念：**参数可以很多，但不需要每次都全部激活。只要调度得当，就能在控制计算成本的同时，获得更高的模型容量。** 这也彻底改变了大模型的设计逻辑，从“每个参数都得上场”，变为“让对的专家在对的时刻出场”。

**国内最早大规模落地 MoE 架构的，是“悟道”团队（北京智源研究院）**，2021年，他们训练了一个 1.75 万亿参数的模型，并自研了 FastMoE 框架，重写了底层调度逻辑，才支撑起这种超大规模的训练任务。自此，MoE 架构逐渐成为工业级大模型的主流形态之一，Google PaLM、Mistral-8x22B、阿里的 Qwen-MoE 等也陆续采用类似方案。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

2024年初，Mistral

**DeepSeek 则做出了一些「本土创新」**，比如引入“细粒度专家”机制，把原本的大模块进一步细分，提升了专家的专业性；同时设计了“共享专家”组件，用于捕捉底层通用知识，减少冗余，也提升了多任务之间的表现一致性。**这些改进一方面减轻了算力压力，另一方面也有效缓解了传统 MoE 常见的问题**，比如：路由不稳定、风格漂移、知识碎片化等。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

DeepSeek MoE

但也正是 DeepSeek 的出色表现，带来了一些新的误解。比如，不少人将“MoE”简单等同于“更聪明”“更先进”，反过来认为 Dense 模型因为体积小就一定弱。这其实是一个需要澄清的观念偏差。**MoE 和 Dense，本质上只是两种不同的资源调度策略，是否采用 MoE，并不能决定一个模型是不是“聪明”。真正决定智能水平的，仍然是模型的训练质量、架构合理性、任务适配能力。**

有关 MoE 的另一个误解是“用不到的专家，不占资源”。正相反，在 MoE 架构中，虽然每次只激活少数专家，但所有参数依然必须常驻显存，真正部署起来的硬件负担一点都不轻。因此，对于私有部署同性能模型来说，MoE 显卡成本会高出很多。

## 小，也可以“聪明”

聪明，不一定靠“大”。

人可以靠后天努力提升能力，小模型也能成长，比如通过**知识蒸馏（Knowledge Distillation）：让小模型参考大模型的答案，并模仿它处理任务的方式**。它的本质仍然是“看答案”，但不是死记答案，而是**学会答题的思路和节奏**。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

模型蒸馏

整个过程通常是这样的：

1.  1\. 大模型先跑一轮任务，生成高质量参考输出，比如说「五年急转弯，三年弱智吧」；

2.  2\. 小模型拿这些答案来学习，但重点不在“复制结果”，而是在模仿—— 学它怎么理解问题、怎么组织信息、怎么一步步得出结论。

需知：蒸馏并不是“把大模型压缩成小模型”，而是**把聪明的部分提炼出来、迁移过去，保留了方法论（而不是复制粘贴参数）**。

比如 DeepSeek-R1 的蒸馏版 —— **DeepSeek-R1-Distill-Qwen-32B**，就是一个很典型的例子：虽然参数缩小了一个数量级，但在多个任务上的表现依然接近，甚至在一些结构化输出上更稳定。

可见，**聪明不是大模型的特权，是训练出来的本事。**

## 写在最后

**模型的对比，不是参数拉踩，不是看谁的数字更大、名字更响。**

MoE 架构的出现，是为了让大模型在成本可控的前提下继续扩容；而知识蒸馏，则让小模型有机会承接大模型的能力，用更轻的体积完成更多的任务。它们分别指向两个方向，但都在回答同一个问题：**如何更高效地使用资源**。

所以，真正值得关注的，不是模型有多大，而是它能不能把事办好、办稳、办漂亮。

毕竟，“大”不一定代表聪明。

**当然，如果名字就叫“大聪明”，那另说 😎
**