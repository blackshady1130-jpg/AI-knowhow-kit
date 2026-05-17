# Agents统一综述：Harness、记忆、Skills和协议

**作者**: PaperAgent
**发布时间**: 
**原文链接**: https://mp.weixin.qq.com/s/4M-ek-pV40caxnynJNIM7Q

---



大家好，我是PaperAgent，不是Agent！


可靠的Agent能力不仅来自模型内部参数权重，更来自将认知负担外部化到结构化基础设施中。


近期，上交大、中山大学、卡梅隆等发表长文对 LLM**Agents**中的外部化：**记忆、Skills、协议与Harness工程**进行了统一综述[5000 star，Harness门槛被OpenHarness打穿了](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247506212&idx=2&sn=3d98124463987b81907b1224f0a904f5&scene=21#wechat_redirect)

![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F5gibgibpTuuwC91UrpT1ia8h9rbiaPVvNBQ3u1ibA5XTrG8xRrXNdUjNyFu5huB8Lz2yqPiaXPUYNPE5LT75ib3ayV4Reh1ry6IHiaxPRjuzicVtOUjU%2F640%3Fwx_fmt%3Djpeg)


借用认知工具（Cognitive Artifacts）理论：Agent基础设施的重要性不仅在于**添加辅助组件**，而在于将难以解决的认知负担转化为**模型能更可靠处理的形式**。

![图1：外部化作为LLM Agent设计的组织原则](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5gibgibpTuuwAAGvJV2cYgKTX22a3PcAjTug584HZ25AqYKqaZDQuhbTUxQYKiafYJY3wicosFVGbLIh6eRcqjuIgsricbYJm61eXsNhxs06He3I%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)
图1：外部化作为LLM Agent设计的组织原则
- 人类认知外部化的弧线（从思维→语言→文字→印刷→计算）
- LLM Agent对应的外部化弧线：从**权重**（Weights）通过三个外部化维度——**记忆**（Memory，外部化状态）、**技能**（Skills，外部化专业知识）、**协议**（Protocols，外部化交互）——最终到达**Harness**（ harness系统）。[只给零散实验日志，谷歌PaperOrchestra就能写出顶会投稿LaTeX论文](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247506295&idx=2&sn=313420aedd244cbe1ad53ebc8713aa7b&scene=21#wechat_redirect)


## 2. 从权重到上下文再到Harness：能力的三次迁移


展示了从2022到2026年，研究重心如何从Weights（预训练、Scaling Law）转向Context（RAG、长上下文），再到Harness（MCP工具生态、安全、多Agent协作）。

![图2：社区主题在三个能力层次上的演变](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5gibgibpTuuwAwn8VTeicDWU7WNCqCcMgqdG74ntbibiccQ808f25Oz532wMfjyrqgmcr7yjxnGAl99YJBOUYiccYghuh7tUcA1lqHcYTFDrjoeCw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)
图2：社区主题在三个能力层次上的演变
### 2.1 权重时代（Weights）：内在知识的局限


早期的现代LLM部署几乎完全依赖模型参数。预训练将统计规律、世界知识和推理习惯压缩进权重中。Scaling Law揭示了参数规模与性能的可预测关系。


**局限**：知识更新困难（需要重新训练）、难以审计（知识分散在数十亿参数中）、缺乏个性化（一套权重服务百万用户却无法区分）。

### 2.2 上下文时代（Context）：提示工程的崛起


能力开始从模型内部向输入设计转移。少样本示例、思维链（Chain-of-Thought）、RAG（检索增强生成）等技术证明：不必修改权重，仅通过精心设计的上下文就能显著改变模型行为。

![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gibgibpTuuwAgHj6VicQVpEeL6vOzCHfRoqBiaIFkWx4wYJY1X0Q0SxaqSzT1NVjnDDNnhDP7LfR49F2aDGttuew7HFfiaLDVNEDA0DPyYuia1ys%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


**关键转变**：将困难的"回忆"问题（模型必须从参数中恢复知识）转化为简单的"识别"问题（模型只需使用已提供的上下文）。

### 2.3 Harness时代：基础设施即能力


随着上下文窗口饱和和提示模板变得笨重，工程注意力转向"模型应在什么样的环境中运行？"。

![图3：Harnessed LLM Agent的外部化架构](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5gibgibpTuuwDmjxTCz0RQVlQbGHtqKfia7d6Pzg0qgOyHzh2hxzbNDrsmNB8b34X8s1M1AaxY3nQVYJo6DfsONZ8zpNUzdxujcRGUTvE2dNwU%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)
图3：Harnessed LLM Agent的外部化架构

Harness层包括：持久记忆存储、工具注册表、协议定义、沙箱、子Agent编排、评估器等。**可靠性越来越多地通过改变环境而非提示模型来解决**。

## 3. 外部化状态：记忆系统（Memory）


记忆外部化解决的是Agent的时间连续性负担。原生LLM是"无状态生成器"：每次调用都是全新的上下文，连续性必须在提示中重建。


**图4：作为外部化状态的记忆**

![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F5gibgibpTuuwCUnPcK09Q67Xiam60GVPYP3fDmiaY1olsqj43vsTziaGME6sCMbsR1eq167wcU43yVib7hepj82kMDGyK6yuVHcLsI7Fp49f7MYss%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg)
展示了从原始上下文到记忆内容的转换，以及四种记忆系统架构：单体上下文、检索存储、分层编排（提取-巩固-遗忘-冷热交换）和自适应记忆系统（动态模块、基于反馈的策略优化）。


**架构演进**：

- **单体上下文**：所有历史保留在提示中（简单但容量受限）
- **上下文+检索存储**：近端状态在上下文，长期轨迹外部存储（RAG模式）
- **分层记忆与编排**：引入显式的提取、巩固和遗忘操作（如MemGPT、Memory OS）
- **自适应记忆系统**：模块和检索策略能根据经验响应（如MemEvolve、MemRL）



**认知工具视角**：记忆系统将"无界回忆"转化为"有界、精选的检索"，改变了模型在每个决策点面临的任务结构。

## 4. 外部化专业知识：技能系统（Skills）


技能外部化解决的是程序性负担。模型可能"知道"如何完成任务，但可靠执行需要重复构建工作流、默认值和约束，这导致方差：遗漏步骤、不稳定的工具使用、不一致的终止条件。

### 4.1 技能的三个组件

1. **操作程序**（Operational Procedure）：任务骨架（步骤分解、阶段、依赖、停止条件）
2. **决策启发**（Decision Heuristics）：分支点的实用经验法则（先尝试什么、何时退出）
3. **规范约束**（Normative Constraints）：可接受性的边界（测试要求、范围限制、访问控制）


### 4.2 从执行原语到能力包


技能系统经历了三个阶段：

- **阶段1：原子执行原语**（如Toolformer）——稳定调用单个工具
- **阶段2：大规模原语选择**（如Gorilla、ToolLLM）——在大量工具中检索选择
- **阶段3：技能作为打包的专业知识**——将任务类别的操作方法打包为可重用单元


![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2F5gibgibpTuuwDUGy8AQfq3tNBJ0emibPY1AYXOKeyicpfqsiaeXKnb5N1vIib6icyWiasp81SPleE6RTxXRAYgjMRcKMVwZnShcQ8mG7wE9Mtdoo7AE%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg)


**图5：作为外部化专业知识的技能**
展示了技能的完整生命周期：从获取（专家编写、从情景记忆蒸馏、环境探索发现、现有单元组合）到技能工件（操作程序、决策启发、规范约束），再到激活流水线（注册表发现、渐进式披露、组合），最后在运行时执行。


**关键机制**：

- **渐进式披露**：不一次性加载完整技能文档，而是分层暴露（名称→摘要→完整指南）
- **执行绑定**：技能必须通过协议接口绑定到可执行动作（工具、API、文件、子Agent）
- **组合性**：技能可参与更高阶协调（串行、并行、条件路由、递归调用）


## 5. 外部化交互：协议系统（Protocols）


协议外部化解决的是协调负担。裸模型可能推断出应该调用工具或委派子Agent，但没有显式契约时，它必须即兴创作消息格式、参数结构、生命周期语义和恢复行为。

### 5.1 协议的内容维度


协议将以下四个维度外部化：

1. **调用语法**（Invocation Grammar）：参数名称、类型、顺序、返回结构（schema化）
2. **生命周期语义**（Lifecycle Semantics）：多步交互的协调规则（状态机、事件流）
3. **权限与信任边界**：授权规则、数据流向、审计要求
4. **发现元数据**（Discovery Metadata）：能力注册表、能力卡片、schema端点


![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5gibgibpTuuwCgoxHxKmS2N5icRRTAzWOp3HtAIyWzGddNEicAibyZnibddTuyyicnAibfLPAiaicXYSVF4DhYOXcEONkGhCnNmMGDl7xXdYWNXodX9A0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


**图6：作为外部化交互的协议**
上图：从孤立模型调用→API硬编码→标准化协议→Agent Web的演进。
下图：Harness通过三个功能界面实现外部化交互管理：Interact（与外部API/工具交互）、Perceive（感知环境/上下文/记忆/反馈）、Collaborate（与其他LLM/Agent/人类协作）。

### 5.2 协议家族综述

![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5gibgibpTuuwCjzn7KUJIMfpmm4r6M9ibwBCvwTWFGJjq20f8yZZYEBpukUtlQMI7rq6JQVC0pBEib0upqxSAgjPViaXGdkv9eIZ9lqnLvOfkYwU%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

## 6. 统一外部化：Harness工程


Harness是承载三个外部化维度（记忆、技能、协议）的工程层，提供编排逻辑、约束、可观测性和反馈循环，使外部化认知在实践中可靠运行。

### 6.1 什么是Harness？


Harness不是模型之外的第四个外部化维度，而是**运行时环境**——模型在其内部运行，通过它感知、决策和行动。

![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gibgibpTuuwDF5Q9Y47hfS7BIibiaVdvnibM6WGbQofw3I83yBpIKiaWcJmllOotlUuyca2Mia7Mfgke1gBAxI1QNpsWL5gkpEMOwfHXObBN1GPp8%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


**图3：Harnessed LLM Agent的外部化架构**
Harness位于中心；三个外部化维度围绕它运行：记忆（工作上下文、语义知识、情景经验、个性化记忆）、技能（操作程序、决策启发、规范约束）、协议（Agent-用户、Agent-Agent、Agent-工具）。操作元素（沙箱、可观测性、压缩、评估、审批循环、子Agent编排）调节Harness核心与外部化模块的交互。

### 6.2 Harness设计的六个分析维度

![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gibgibpTuuwBHAZ3gJmib4mgc4Hc8eibw8ufaKZPtRgQeiaDTYaaL9cD6Z4m0FsyzqjFPCG4TYgO5hOZo6IbLjdbFUDJtrJobOKVa9ECibgBUP0s%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


**图7：作为认知环境的Harness**
![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5gibgibpTuuwBmzqaPkDys32ic6tZ5wGU5gJXKiaDuhMIjTsGb2VHX17DibXXrUdnZlpfehQxeYyLKhvtO7CcNfM7XZK8hg0fviaeicOAkgEiahia48o%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


基础模型（Agent核心）位于中心；六个Harness维度形成协调环：记忆（状态持久化）、技能（可重用例程）、协议（确定性接口）、权限（沙箱、文件隔离）、控制（递归边界、成本上限）、可观测性（结构化日志、执行轨迹）。

### 6.3 Harness作为认知环境


从分布式认知理论看，Harness不仅仅是软件基础设施，而是**塑造Agent有效认知的环境**。它决定了什么进入感知领域、什么跨会话保留、哪些操作可调用、哪些行动需要审批、哪些中间状态可修订。


Harness将无界任务转化为结构化环境，通过外部化记忆、形式化程序、引入显式控制点和约束执行，重新分配认知工作负载。

## 7. 交叉分析：模块间耦合


三个外部化模块在Harness内并非孤立，而是形成六条关键交互流：

![图8：记忆、技能、协议之间的耦合](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5gibgibpTuuwApEHWBiaMD7BzsiarSfXjbhAxKuZqSmv4EFtlqTfZomOY7trLEibck4qiahhJoZZmHGibuMcffDRNSzb1tkEQDIKjgo6svakJNMeD4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)
图8：记忆、技能、协议之间的耦合


```
Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering  https://arxiv.org/pdf/2604.08224
```


[动手设计AI Agents：（编排、记忆、插件、workflow、协作）](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247492838&idx=2&sn=1e25832e7300ef312721325d0def30b4&scene=21#wechat_redirect)


[分享两篇Claude Skills最新论文，有3个核心结论](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247505843&idx=1&sn=9a8a4915606ee747998015395413db87&scene=21#wechat_redirect)


[会学习的龙虾，才是好龙虾：OpenClaw-RL](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247505225&idx=1&sn=4b32282cf6853e29f884bdfb85f89f2e&scene=21#wechat_redirect)
[2026，做Agentic AI，绕不开这两篇开年综述](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247502666&idx=1&sn=d6a467896c6753c8d8634c7400d8dbb4&scene=21#wechat_redirect)


每天一篇大模型Paper来锻炼我们的思维~已经读到这了，不妨点个👍、❤️、↗️三连，加个星标⭐，不迷路哦~
