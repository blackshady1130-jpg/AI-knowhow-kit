# 为什么现有的 Agent Infra 无法支撑生产级应用？

Original Guanlan Guanlan | Agentic Infra

想象一个帮客户做跨云迁移的 Agent。前两小时它完美地在 AWS 和 GCP 之间配置了 VPC，拉起了实例，并在第 12 步删改了旧数据库。然后在第 13 步，它因为一个罕见的 API 限流崩溃了。

你该怎么办？重试？它会再修改一遍数据库；重启？它不知道哪些实例已经拉起。没有有效状态恢复，现在你的整个云环境就是一团乱麻。

这是一个贴近现实的场景，任何在生产中跑过超过 10 步的 Agent 都会遇到类似的问题。

## Agent 的执行特征

它同时具备五个属性：长程运行、敌意输入、真实权限、不确定决策、真实副作用。

最近出圈的龙虾 OpenClaw 把这个问题推到了前台。这五个属性单独拿出来都不新鲜。Agent 的难点在于它把这五个属性同时绑在了同一条执行链上，而且没有任何现成的系统是为这个组合设计的。

## 两个错位的假设

第一个是威胁模型的假设——整个行业在用服务器代码的安全假设运行客户端代码。Agent 的威胁模型是浏览器，而不是服务器。

第二个是执行模型的假设——现有的执行 Infra 为确定性、短时、无状态的任务设计。Agent 的执行是概率性的、长程的、带状态的。

后果是三个缺失：没有副作用日志，没有可恢复的执行状态，没有隔离边界。

## 三条缺失的原语

**一、Effect Log**：把外部世界的副作用做成一套 write-ahead log。有副作用的调用在执行前先写 intent record，执行后写 completion record。Tool call 按可恢复语义分类：不可逆写调用禁止重放，幂等写调用带幂等键允许重放，纯读调用可以重放。

**二、能力隔离**：通过 Capability Gateway 中介所有外部访问。Agent 拿到的是有时间限制、有范围限制、可即时撤销的临时令牌。跟浏览器的安全模型同一个思路。

**三、分叉恢复**：每个分支需要独立的 checkpoint——模型输出、tool 输出以及 effect log 的游标位置。恢复时能精确回到某个节点继续推进。

## 从 Uptime 到 Resumability

在 SaaS 时代，Infra 核心指标是 Uptime。但对于 Agent，正确的指标是 Resumability：能不能在任意时间点重新进入执行，完整恢复状态、上下文和环境？

一个可以被中断然后被正确恢复的 Agent，比一个理论上永远不停但遇到硬件故障就没有退路的 Agent 更可靠。

## 现有 Infra 的抽象层错位

Kubernetes、Firecracker、gVisor、Modal、E2B、WASM——它们做到了 execution isolation，但没有提供 semantic isolation。传统软件的逻辑是确定性的、可信的，Agent 打破了这个前提。

Temporal 和 Conductor 的核心前提是 workflow 的代码逻辑是确定性的、可信的。LLM 从根本上打破了这个前提。

## Infra 的真正使命是做熵减

LLM 本身的任务就是不停在做熵增，而 Infra 的真正使命是做熵减。

Agent loop 决定行为。Infra 决定边界。

Infra 不应该追求模型永远正确，而是让模型的错误变得可预测、可隔离、可挽回。现有的 infra 还远远不够，我们的 Infra 栈应该从执行层开始重建。

---
Source: https://mp.weixin.qq.com/s/_h3DJRFoC7k61T1KO83dng
