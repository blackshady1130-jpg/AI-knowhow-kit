---
url: https://mp.weixin.qq.com/s/B-XQRuns_U9Li5jXW-sOuw
title: "ChatGPT：GPT-4 架构揭秘"
description: "信息量巨大 !!!"
author: "lencx"
captured_at: "2026-03-08T10:56:11.522Z"
---

# ChatGPT：GPT-4 架构揭秘

OpenAI 自 GPT-3.5 之后的版本就未开源，网上经常有人吐槽说不如改名 ClosedAI。关于 GPT-3.5、GPT-4 的所有信息就像是一个黑盒，被 OpenAI 紧紧的包裹起来。但是一帮大佬们可没闲着，George Hotz\[1\] 前段时间就揭秘过一次（[GPT-4 混合模型：8 个 2200 亿参数的专家模型？](http://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247486958&idx=1&sn=e0510eed7ea8f594587787a2ae6f158d&chksm=e8dd4c1adfaac50ce2643958a8c84f36cbc6adde108b489fae1c588a070dfbf838808f44c0ad&scene=21#wechat_redirect)），相比于之前，这次爆出的信息更多更大。不论真假，都值得一看。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/90Kxd0FAJJcUGwPhgrxFQasTuMcSfVlZicCvIS219J6MQljsGXibX1M7NP5Sb2XezcSR7SYTj4rQmDVecDocQQAQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## 推文揭秘

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

以下信息并非官方消息，大家自行判断。@Yampeleg 在推上进行了一系列 GPT 揭秘，迫于压力，现在所有帖子均已删除。以下内容整理自之前的时间线：

-   参数数量：GPT-4 比 GPT-3 大 10 倍以上，大约有 1.8 万亿个参数，分布在 120 个层中。

-   专家混合模型（Mixture of Experts, MoE）：OpenAI 使用了 MoE 模型，共有 16 个专家在模型中，每个专家约有 1110 亿个 MLP 参数。每次向前传递都会路由到两个专家中。注意力机制共享的参数大约有 550 亿。

-   推理（Inference）：每次向前传递推理（生成 1 个 token）只使用约 2800 亿个参数和约 560 TFLOPs。这与一个纯密集模型的向前传递需要的约 1.8 万亿参数和约 3700 TFLOPs 形成了对比。

-   数据集：GPT-4 在约 13 万亿个 token 上进行了训练。这些并不是唯一的 token，它们也将 epochs 计算为更多的 token。文本数据为 2 epochs，代码数据为 4 epochs。从 ScaleAI 和内部获取了数百万行的微调指令数据。

-   GPT-4 32K：在预训练阶段，有一个 8k 的上下文长度（seqlen）。GPT-4 的 32k seqlen 版本是基于预训练后的 8k 进行微调的。

-   批大小（Batch Size）：在集群上，批大小在几天内逐渐增加，但最终，OpenAI 使用的批大小为 6000 万。由于不是每个专家都能看到所有的 token，所以这只是每个专家的 750 万 token 的批大小。

-   并行策略：为了在他们的所有 A100s GPUs 上实现并行，他们使用了 8 路张量并行，这是 NVLink 的限制。除此之外，他们还使用了 15 路管道并行（可能使用了 ZeRo Stage 1，块级 FSDP）。

-   训练成本：OpenAI 的 GPT-4 训练 FLOPS 是大约 2.15e25，在大约 25000 个 A100s 上运行了 90 到 100 天，MFU 在 32% 到 36% 之间（极低的利用率部分是由于需要从检查点重新开始的故障数量极多）。如果他们在云中的成本是每小时约 1 美元/A100，那么这次运行的训练成本将是约 6300 万美元（现在，预训练可以用约 8192 个 H100 在约 55 天内完成，成本为 2150 万美元，每小时 2 美元/H100）。

-   专家混合模型的权衡：选择使用的专家数量是需要权衡的（例如：MoE 在推理上非常难处理，因为并不是每个 token 的生成都会利用模型的每个部分。这意味着当其他部分被使用时，一些部分可能会处于休眠状态。在服务用户时，大大降低了利用率），一个原因是更多的专家更难以在许多任务上泛化。更多的专家也可能更难以实现收敛。对于如此大规模的训练运行，OpenAI 选择在专家数量上更保守（研究人员已经证明，使用 64 到 128 个专家可以比 16 个专家获得更好的损失，但这只是纯研究）。

-   GPT-4 推理成本：GPT-4 的成本是 175B 参数的 Davinchi 的 3 倍。这主要是由于 GPT-4 需要更大的集群和达到的利用率较低（它的成本估计是每 1000 个 token 0.0049 美分，用 128 个 A100 推理 GPT-4 8k seqlen，每 1000 个 token 0.0021 美分，用 128 个 H100 推理 GPT-4 8k seqlen。值得注意的是，我们假设有相当高的利用率，并保持批量大小较高）。

-   多查询注意力（Multi-Query Attention）：OpenAI 正在使用 MQA，这样只需要 1 个 head，可以显著减少 KV 缓存的内存容量。即使是这样，32k seqlen 的 GPT-4 肯定无法在 40GB A100s 上运行，8k 的则受到最大 bsz 的限制。

-   连续批处理（Continuous batching）：OpenAI 实现了可变批大小和连续批处理。这样可以在一定程度上允许最大延迟并优化推理成本。

-   视觉多模态（Vision Multi-Modal）：这是一个与文本编码器不同的视觉编码器（该架构与 Flamingo\[2\] 类似），具有交叉注意力。它在文本预训练后，通过另外约 2 万亿个 token 进行微调（对于视觉模型，OpenAI 本想从头开始训练，但是它还不够成熟，所以他们决定先从文本开始以降低风险。视觉模型的主要目标之一就是能够读取网页并转录图片和视频中的内容，为自主智能体提供服务。他们训练的数据包括联合数据（渲染的 LaTeX/文本），网页截图，YouTube 视频采样帧，并围绕它运行 Whisper 以获得转录）。

-   推测解码：OpenAI 可能在 GPT-4 的推理过程中使用了推测解码（不确定 100%）。其思想是用一个更小更快的模型预先解码几个 token，然后将这些 token 作为一个单独的批次输入到一个大型的 oracle 模型中。如果小模型对其预测是正确的 – 大型模型同意，那么我们就可以在一个批次中解码几个 token。但是，如果大型模型拒绝了草拟模型预测的 token，那么其余的批次将被丢弃，我们继续用大型模型。关于新的 GPT-4 质量降低的阴谋理论，可能只是因为他们让 oracle 模型接受来自推测解码模型的低概率序列。

-   推理架构：推理在一个由 128 个 GPUs 组成的集群上运行。这些集群分布在不同地点的多个数据中心中。它使用 8 路张量并行和 16 路管道并行。每个由 8 个 GPUs 组成的节点只有约 1300 亿个参数。

-   为什么没有 FSDP？：可能的原因之一是他们获得的一些硬件基础设施是旧的一代。在本地计算集群中这是非常常见的，因为组织通常会通过几个"波次"升级基础设施，以避免完全停止运行。

-   数据集混合：他们在 13T 个 token 上进行了训练。CommonCrawl 和 RefinedWeb 都是 5T。去除因多次迭代而产生的 token 重复，我们得到了一个更为合理的"未说明" token 数量：这就是"秘密"数据。此时，我们已经听到了一些关于部分数据来自 twitter，reddit 和 youtube 的传言。有一些猜测包括：LibGen（400 多万本书），Sci-Hub（8000 多万篇论文），GitHub 的全部内容。

@Yampeleg 的观点：

这个缺失的数据集是一个定制的大学教科书数据集，尽可能多地手动收集各种课程的教科书。这个数据集非常容易转换为 txt 文件，然后用自我指导将其转换为指令形式。这就创造了 GPT-4 "聪明"的"幻觉"，无论谁使用它，它都能提供帮助。计算机科学家？当然，它可以帮助你解答 P!=NP 的问题。哲学专业？它完全可以和你讨论知识论。你没看出来吗？它是在教科书上进行训练的，这是如此明显。有一些研究试图从 GPT-4 中强行提取出它记住的书本的部分，以了解它训练的内容。有一些书，它非常熟悉，可以确定它肯定看过。而且，如果我没记错的话，它甚至知道欧拉项目练习的唯一 id。

> 相关阅读：GPT-4 Architecture, Infrastructure, Training Dataset, Costs, Vision, MoE\[3\]

## 名词解释

-   MLP：是 "多层感知机"（Multi-Layer Perceptron）的缩写，是一种前馈神经网络，它将输入（例如像素）映射到合适的输出。MLP 由至少三层神经元组成：输入层、一个或多个隐藏层，以及输出层。

-   TFLOPs：是"万亿次浮点运算"的缩写，它是衡量计算性能的一个单位。一般用于评估图形处理器（GPU）或其他硬件的性能。

-   epochs：在机器学习中，epoch 是一次完整的前向和后向传播，也就是将整个数据集送入网络进行训练的过程。

-   张量并行：是一种并行化策略，用于处理大规模的深度学习模型。它将一个模型的各层分布在多个处理器上，允许每个处理器仅处理一部分参数。

-   seqlen：是序列长度（Sequence Length）的缩写，是指一组数据或输入中元素的数量。

-   Batch Size：批量大小是指在训练神经网络时，一次同时处理的样本数。

-   ZeRo Stage 1：ZeRo 是 "零冗余优化"（Zero Redundancy Optimizer）的缩写，是微软的深度速度团队开发的一种内存优化策略。ZeRo Stage 1 是 ZeRo 的一个版本，主要进行优化器状态和梯度的划分，以减少训练大型模型的内存占用。

-   MQA（Multi-Query Attention）：在自然语言处理和计算机视觉领域中，注意力机制（Attention Mechanism）被广泛用于帮助模型聚焦于输入数据的关键部分。通常的注意力机制基于单个查询（Single Query）来确定输入数据的重要性。然而，Multi-Query Attention 是一种扩展的注意力机制，它允许模型同时使用多个查询来计算输入数据的重要性。每个查询都可以独立地关注输入数据的不同部分，从而使模型能够捕获更丰富和复杂的模式。

-   KV 缓存：指的是键值（Key-Value）缓存，这是一种常见的缓存系统，在大规模模型中也有所使用，以缓存和快速访问数据。

-   bsz：是 "batch size"（批大小）的缩写。

-   FSDP：是 "Fully Sharded Data Parallelism"（全体参数分布式优化）的缩写，是一种新的并行训练策略，旨在减少内存使用，从而在现有硬件上训练更大的模型。

-   P!=NP：这是计算理论中最著名的未解决问题之一。这个问题涉及到两类问题：P 类问题（Polynomial Time，多项式时间）和 NP 类问题（Nondeterministic Polynomial Time，非确定性多项式时间）。P 类问题是那些可以在多项式时间内找到答案的问题，NP 类问题是那些可以在多项式时间内验证答案的问题。P!=NP 的主要猜想是：存在一些问题，我们可以在合理的时间内验证其解决方案，但是我们不能在合理的时间内找到解决方案。换句话说，找到解决方案的难度大于验证解决方案的难度。如果 P=NP，那么说明我们可以快速找到并验证解决方案。然而，尽管经过几十年的努力，这个问题仍然没有得到解决，即我们还不能确定 P 是否等于 NP。

-   NVLink：NVLink\[4\] 是由 NVIDIA 开发的一种高速数据连接技术，主要用于连接高性能 GPU 和 CPU，以及 GPU 之间。

    ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## 拓展阅读

### ZeRo Stage 1 拓展

DeepSpeed\[5\] （[DeepSpeed Chat：一键搞定不同规模 ChatGPT 类模型训练！](http://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247485972&idx=1&sn=18afcbc4e79c67283b84eaec5dfc89a6&chksm=e8dd4be0dfaac2f60832cce0721f68606c3685286cb8b0172df81bed43917ac21b1036d58ca7&scene=21#wechat_redirect)）实现了 ZeRO 论文中描述的所有内容。目前它完全支持：

-   优化器状态划分（ZeRO stage 1）

-   梯度划分（ZeRO stage 2）

-   参数划分（ZeRO stage 3）

-   自定义混合精度训练处理

-   一系列基于 CUDA 扩展的快速优化器

-   ZeRO-Offload 到 CPU 和 Disk/NVMe

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)*比较了 ZeRO 的三个阶段与标准数据并行基线的内存节省和通信量。在内存消耗公式中，Ψ 指的是模型中的参数数量，K 是优化器特定的常数项。作为一个具体的例子，我们展示了一个使用 Adam\[6\] 优化器的 75 亿参数模型在 64 个 GPU 上的内存消耗，其中 K=12。我们还显示了 ZeRO 相对于基线的通信量。（原文：ZeRO & DeepSpeed: New system optimizations enable training models with over 100 billion parameters\[7\]）*

-   Stage 1：跨数据并行工作线程/GPU 的分片优化器状态

-   Stage 2：分片优化器状态 + 跨数据并行工作线程/GPU 的梯度

-   Stage 3：跨数据并行工作线程/GPU 的分片优化器状态 + 梯度 + 模型参数

-   优化器卸载（Optimizer Offload）：在 ZERO 第二阶段的基础上，将梯度 + 优化器状态卸载到 CPU/硬盘

-   参数卸载（Param Offload）：在 ZERO 第三阶段的基础上，将模型参数卸载到 CPU/硬盘

注意：关于硬盘卸载，硬盘应该是 NVME 才能有较好的速度，但技术上它可以在任何硬盘上工作。

> 🔗 ZeRO：朝向训练万亿参数模型的内存优化
>
> > ZeRO: Memory Optimizations Toward Training Trillion Parameter Models\[8\]
>
> 大型深度学习模型能够提供显著的精度增益，但训练十亿至万亿的参数却面临挑战。现有的解决方案，如数据并行和模型并行，在将这些模型适应有限设备内存的同时，仍存在获得计算、通信和开发效率的根本限制。我们开发了一种新的解决方案，零冗余优化器 (ZeRO)，用于优化内存，极大地提高训练速度，同时增加可以高效训练的模型大小。ZeRO 消除了数据和模型并行训练中的内存冗余，同时保持了低通信量和高计算粒度，使我们能够按设备数量比例扩展模型大小，同时保持高效率。我们对内存需求和通信量的分析显示：ZeRO 有可能使用今天的硬件扩展到超过 1 万亿参数。
>
> 我们实现并评估了 ZeRO：它在 400 个 GPU 上训练了超过 1000 亿参数的大型模型，实现了超线性加速，达到了 15 Petaflops 的吞吐量。这在模型大小上代表了 8 倍的增长，同时在可实现性能上增加了 10 倍，超过了现有技术。就可用性而言，ZeRO 可以训练最多达 130 亿参数的大型模型（例如：比 Megatron GPT 的 83 亿和 T5 的 110 亿还要大），而不需要应用更难以应用的模型并行。最后但并非最不重要的是，研究人员已经使用 ZeRO 的系统突破，创建了世界上最大的语言模型（Turing-NLG，170 亿参数），创造了突破性的精度记录。

### References

\[1\]

George Hotz: *https://en.wikipedia.org/wiki/George\_Hotz*

\[2\]

Flamingo: *https://www.theregister.com/2022/04/29/flamingo\_deepmind\_ai*

\[3\]

GPT-4 Architecture, Infrastructure, Training Dataset, Costs, Vision, MoE : *https://www.semianalysis.com/p/gpt-4-architecture-infrastructure*

\[4\]

NVLink: *https://www.nvidia.com/en-us/data-center/nvlink*

\[5\]

DeepSpeed: *https://github.com/microsoft/DeepSpeed*

\[6\]

Adam: *https://arxiv.org/pdf/1412.6980.pdf*

\[7\]

ZeRO & DeepSpeed: New system optimizations enable training models with over 100 billion parameters: *https://www.microsoft.com/en-us/research/blog/zero-deepspeed-new-system-optimizations-enable-training-models-with-over-100-billion-parameters*

\[8\]

ZeRO: Memory Optimizations Toward Training Trillion Parameter Models: *https://arxiv.org/abs/1910.02054*