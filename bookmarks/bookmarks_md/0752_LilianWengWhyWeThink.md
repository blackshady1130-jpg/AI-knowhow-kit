---
url: https://mp.weixin.qq.com/s/fcDRzd3cwuM_JOnQW5XRMQ
title: "刚刚！北大校友Lilian Weng最新博客来了：Why We Think"
description: "学习大模型的优质博客又更新了！"
captured_at: "2026-03-08T13:12:03.001Z"
---

# 刚刚！北大校友Lilian Weng最新博客来了：Why We Think

选自 Lil'Log

**作者： Lilian Weng** 

**机器之心编译**

学习大模型的优质博客又更新了！

最近，北大校友、前 OpenAI 应用 AI 研究负责人 Lilian Weng 更新了一篇长长长长长长长博客《Why We Think》。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWicQLrH5hicvSvEAK9wuG4cIPrZ91Eq8vmbsK3o92lwfznxrANsrvH8rsXIcLLoChmuEvvtVFf2xMmQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

文章回顾了近期在如何有效利用测试时计算（即「思考时间」）及其作用机制方面的研究进展，旨在让模型「思考得更久」这一目标可以从多个角度得到合理动机支持。

通过观察 GPT、Claude、Gemini 等模型的迭代，可以清晰地看到，它们在复杂逻辑推理、长文本理解、数学问题求解以及代码生成与调试等高级认知任务上的性能边界被不断拓展。

这种性能的提升得益于思维链（CoT）和测试时计算等策略的优化，但也带来了新的研究挑战。

为了方便国内读者更好地学习这篇内容，机器之心对此文章进行了编译。感兴趣的读者也可查阅原英文内容。

-   英文博客链接：https://lilianweng.github.io/posts/2025-05-01-thinking/

类比心理学

该核心思想与人类的思维方式密切相关。人类通常无法立即给出「12345 × 56789」的答案，对于复杂问题，进行一段时间的思考和分析是自然的过程。

在《思考，快与慢》（Thinking, Fast and Slow）一书中，丹尼尔・卡尼曼（Daniel Kahneman 基于「认知双系统理论」（dual process theory），将人类的思维方式划分为两种模式：

-   快速思维（System 1）：运作迅速且自动，受直觉和情绪驱动，几乎不需要认知努力。

-   慢速思维（System 2）：依赖有意识的逻辑推理与严密思考，需耗费较高认知能量并主动参与。

由于快速思维易于启动且更为省力，它往往成为决策主导，但这通常以牺牲准确性与逻辑性为代价。它天然依赖于人脑的「认知捷径」（即启发式方法 heuristics），进而容易产生错误与偏差。而通过有意识地放慢思维速度，给予更多反思、改进与分析的时间，可以激活慢速思维，挑战直觉，从而做出更具理性与准确性的决策。

计算即资源

在深度学习中，有一种观点认为神经网络可以通过其在每次前向传播中所能调用的计算与存储资源进行刻画。

如果我们使用梯度下降法来优化它们以解决问题，那么优化过程将自行「找出」如何组织这些资源，用于计算与信息存储，因此可以被看作会自动规划电路的过程。

从这一角度来看，如果我们设计的架构或系统在测试时（test time）可以执行更多计算，并且我们训练模型以有效地利用这一额外资源，那么模型的性能将会更好。

在 Transformer 中，每生成一个 token，模型所执行的浮点计算量（FLOPs）大致是其参数数量的两倍。而在稀疏模型（如专家混合模型 Mixture of Experts, MoE）中，由于每次前向传播只激活部分专家网络，参与计算的参数仅为总参数的一部分，因此计算量为 2 × 参数数 ÷ 稀疏度，其中「稀疏度」表示被激活专家网络的比例。

相比之下，思维链（CoT）使得模型在为每个希望生成的 token 进行推理时，能够执行更多的计算（即 FLOPs）。实际上，思维链的一大优势在于，它允许模型根据问题的难度灵活地调整计算量。

潜变量建模

在机器学习中，一种经典的方法是：定义一个含有潜变量（latent variable）z 与可见变量 y 的概率模型，其中 y 是学习算法所观察到的变量。通过对潜变量可能值的边缘化（即求和），可以表达出一个关于可见变量 y 的复杂概率分布，即 P (y) = ∑z∼P (z) P (y | z)。

例如，我们可以用该方法建模数学问题及其解答的分布：将 x 表示为题目文本，y 表示真实答案或证明过程，而 z 则表示引导生成证明的一系列自由形式推理过程。优化的目标是条件概率 P (y | x) = ∑z∼p (z | x) P (y | x, z)。

这种潜变量视角特别适用于理解多线程思维链（multiple parallel CoTs）或基于搜索的思维链生成方法。这些算法可以被视为从后验分布 P (z | x, y) 中进行采样。这一视角还揭示了优化对数似然 log P (y | x) 作为目标函数的好处 —— 因为 log loss 目标函数在预训练中效果显著。

思维以 token 为单位

在生成简短答案之前，先生成中间推理步骤的策略，特别是在数学问题中，最初由研究者提出，并逐渐拓展形成了标准方法。这一方向中早期的研究包括构建数学推理数据集，并训练生成器进行有监督学习，通过人类编写的解题路径作为参考，同时训练验证模型判断候选答案是否正确，从而可以在多个解答中进行有效搜索。

后续研究引入了「草稿板」（scratchpad）概念，即将模型生成的中间 token 视为辅助推理过程的临时内容，并进一步引申出「思维链」（CoT）这一常用术语，以描述大语言模型通过逐步推理而非直接输出答案的能力。

最初提升 CoT 推理能力的方法，主要通过监督学习对人类书写的推理路径进行训练，或对模型生成的、经过正确性过滤的路径进行训练，后者可以被视为一种初级形式的强化学习。还有研究表明，仅通过设计合适的提示方式，如使用「逐步思考」的提示语，或构造更复杂的提示内容，引导模型先思考相关知识，也能显著提升指令微调语言模型在数学任务上的表现。

随着进一步的探索，研究人员发现，在具有自动可验证答案的数据集上应用强化学习，可以显著增强 CoT 推理能力。这些数据集包括带有确定短答案的 STEM 问题，或可以通过单元测试验证正确性的编程任务。这类强化学习策略已被验证可以显著提升大语言模型在多步推理任务中的性能。近期的模型开发中，采用策略梯度算法结合自动评估的问题集，已成为提高模型表现的有效方法。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

思维链提示（CoT prompting）显著提升了解决数学问题的成功率。模型规模越大，其「思考时间」所带来的性能收益越显著。

分支与修订

测试时计算（test-time compute）的根本目的在于：在推理过程中动态地调整模型的输出分布。为此，有多种策略可用于消耗额外的测试时资源，从而优化解码过程、选择更优样本，并将模型输出引导至更符合需求的分布。

目前主要有两类提升生成质量的策略：并行采样（parallel sampling）与序列修订（sequential revision）。

-   并行采样是在每一步并行生成多个输出序列，同时通过过程奖励信号（process reward signals）或结果评估模块（如验证器）对最终输出的质量进行判断，以此挑选最优答案。这是目前广泛采用的提升测试时性能的解码方法形式，例如 best-of-N 和束搜索。在无法获得标准答案（ground truth）的情境下，常使用自洽性策略（self-consistency），即在多个思维链（CoT）推理序列中，以多数投票的方式选择最终答案。

-   序列修订是指基于模型前一轮输出的结果，对其进行反思与迭代性修正，引导模型在后续输出中主动识别并纠正可能的错误。这种修订流程通常需要在经过微调的模型上实现；若仅依赖模型自身进行「内生性自我修正」（intrinsic self-correction），且缺乏外部监督反馈，则往往难以取得明显提升。

并行采样具有实现简单、直观、易部署等特点，但其效果在很大程度上取决于模型是否能够「一次性」生成正确答案；而序列修订通过显式引导模型识错与改错，逻辑上更具针对性，但速度较慢，且需额外控制过程中的修订风险，例如原本正确的答案被不当更改为错误，或模型产生新的幻觉（hallucination）。这两种方法可以结合使用。Snell 等人发现：对于简单问题，单一使用序列化策略的测试时计算效果最佳；而对于高难度问题，则通常需要在并行计算与序列修订之间找到最优组合比例，以获得最好的任务表现。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

并行采样与序列修订示意图。

并行采样

当我们手头有一个生成模型（generative model）以及一个可用于对完整或部分生成样本进行评分的评分函数（scoring function）时，便可以设计多种搜索算法，以寻找评分更高的生成结果。其中最简单的一种算法便是 best-of-N：直接独立生成 N 个样本，再依据评分函数从中选出得分最高者。

相较之下，束搜索是一种更复杂且更具适应性的搜索算法，它通过动态分配计算资源，优先探索解空间中更具潜力的部分。在束搜索过程中，模型维护一组当前最有前景的部分序列，并在扩展这些候选序列与剔除不够理想的序列之间交替进行。

在选择生成候选时，可以引入过程奖励模型（Process Reward Model, PRM）作为引导机制，辅助束搜索的路径筛选。例如，有研究使用大语言模型自身来评估其生成的每个推理步骤是否合理，将其格式化为选择题，从而进行逐步自我评估（per-step self-evaluation）。这种方法能够显著减少多步推理过程中的累计错误，特别是在束搜索解码阶段，表现尤为明显。

此外，在采样过程中通过温度退火（annealing the temperature）策略来调控随机性，也有助于缓解生成过程中不必要的波动。这一系列实验方法在 Codex 模型上应用于 GSM8k、AQuA 与 StrategyQA 等少样本任务时，取得了 5–6% 的性能提升。

区别于传统束搜索，REBASE（Reward Balanced Search）方法训练了一个独立的过程奖励模型，用于评估束搜索树中每一节点在不同深度下的扩展优先级。该模型基于 softmax 归一化的奖励分值，动态决定哪些节点获得更多生成资源。

另一种名为 RATIONALYST 的过程奖励模型，则利用大量无标注数据训练用于多步推理任务，模型通过生成候选推理路径（称为 rationale），并根据这些 rationale 是否能减少真实答案 token 的负对数概率（negative log-probability）达一定阈值，来筛选高质量推理过程。

在推理阶段，RATIONALYST 可以以两种方式引导思维链 CoT）生成器进行推理：一种是隐式地估计下一个推理步骤的概率（implicit supervision）；另一种是显式地将下一步的推理内容直接作为提示词的一部分生成（explicit supervision）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

束搜索解码过程中由大语言模型对每个推理步骤进行自我评估的引导机制。

有趣的是，即使不采用显式的零样本提示（zero-shot prompting）或少样本提示（few-shot prompting），也有可能激发出语言模型中的思维链（CoT）推理路径。Wang 与 Zhou 发现，如果在采样的第一个 token 处进行分支，并保留置信度最高的前 k 个 token（其置信度通过 top-1 与 top-2 候选之间的概率差来衡量），然后分别对这 k 条路径采用贪婪解码（greedy decoding）继续生成，那么其中相当一部分生成序列天然包含完整的思维链。

尤其在上下文中本就存在思维链内容时，这种机制更容易引导模型生成更具置信度的最终答案。在评估最终答案的置信度时，需首先通过特定任务的启发式方法（task-specific heuristics）标识出答案片段，例如，在数学题中提取最后出现的数值答案；或通过进一步提示模型（例如在末尾提示 「So the answer is」）来提取明确答案。

仅在首个 token 处进行分支的设计逻辑在于，相比于后续 token，早期分支能显著提升推理路径的多样性，而后续 token 的生成则更多受限于已有上下文序列。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Top-k 解码中，k 表示在首次采样步骤中保留的候选项数量。

顺序修订

如果一个模型具有反思并纠正其先前回答中错误的能力，我们应期望它能够产生一个质量不断提高的迭代修订序列。然而，事实证明，这种自我修正能力并非大语言模型所固有，且在未经特别设计的情况下往往难以实现，其中的失败模式包括：

（1）幻觉，即将原本正确的回答修改为错误的版本；

（2）行为坍缩为不修正的状态，例如，在最初的错误回答上只进行细微甚至不作修改；

（3）在测试时无法泛化到分布转移（distribution shift）的情况。

Huang 等人的实验表明，直接应用自我修正策略反而可能导致性能下降，模型若要实现自我提升，仍需依赖外部反馈信号，例如与真实标签比对的结果、启发式规则、针对任务设计的评估指标、编程题的单元测试结果、更强大的模型输出参考，以及人类反馈等。

自我修正学习旨在在固定的生成模型 P₀(y₀∣x) 基础上，训练一个修正器模型 Pθ(y∣y₀, x)。其中生成模型保持通用性，而修正器模型则可以针对具体任务进行定制，并且只在给定初始模型响应和可选附加反馈（例如一段文本、编译器提示信息或单元测试结果）条件下进行生成：

1\. 自我修正学习首先针对数据池中的每个提示生成多个候选输出；

2\. 然后，为每个提示构造「价值提升对」；即挑选两个输出，如果其中一个相较于另一个在评价指标上更优，则组成（提示 x，初始答案 y，修正答案 y′）三元组；

3\. 接着，根据修正带来的价值提升幅度 v (y′) − v (y)，以及两个输出之间的相似度 Similarity (y, y′)，对这些样本对进行加权采样以训练修正器模型；

4\. 为鼓励探索，修正器生成的新输出也会加入数据池。推理时，可以反复调用修正器，从而形成一个连续改进的修订轨迹。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

通过匹配同一问题下模型的不同输出，构造「价值提升对」以训练修正模型的自我修正学习示意图。

递归检视（Recursive Inspection）同样旨在训练更优的修正器模型，但其采用的是单一模型同时完成生成与自我修正的策略。

SCoRe（Self-Correction via Reinforcement Learning）是一种基于多轮交互的强化学习方法，旨在鼓励模型在第二次尝试时生成相较第一次更优的答案，从而实现自我修正。该方法由两个训练阶段组成：

 第一阶段的目标是最大化第二次尝试答案的准确性，同时仅对第一次尝试施加 KL 散度惩罚（KL penalty），以防止第一次生成行为偏离基础模型太远，保持其生成风格的稳定性；

 第二阶段则同时优化第一次和第二次生成答案的准确性。

理想情况下，我们希望模型在第一次和第二次尝试中都能获得更好的性能，但引入第一阶段可以有效避免「行为坍缩」，即模型仅对初始响应进行微小甚至无修改；

而第二阶段则在此基础上进一步提升整体表现。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

显式训练设置，通过进行两阶段 RL 训练来提高自我纠正能力。

使用强化学习提升推理能力

近期，越来越多的研究成功地利用强化学习（RL）提升语言模型的推理能力。这类方法通常采用带有可靠参考答案的问题集（主要是 STEM 领域的问题或易于验证答案的逻辑谜题），通过奖励模型生成正确答案来优化其性能。

这一方向的发展受到 OpenAI 发布系列模型出色推理表现的推动，随后 DeepSeek 的模型及技术报告进一步加速了相关研究的进展。

DeepSeek-R1 是一款开源大语言模型，专为应对数学、编程和逻辑推理等高复杂度任务而构建。其训练流程包括两轮 SFT-RL（监督微调 + 强化学习），使得 R1 在推理类与非推理类任务上均具备良好能力。

在训练初期，采用「冷启动监督微调」（cold-start SFT），即在数千条冷启动数据上对基础模型进行微调。若省略此步骤，模型在初期表现中可能会出现语言混杂、表述不通顺等问题。

面向推理的强化学习（reasoning-oriented RL）阶段，使用仅包含推理任务的提示，对模型进行强化训练，奖励信号设计为两类规则型指标：

格式奖励（format rewards）：要求模型使用特殊 token 包裹「思维链」（CoT）。

准确性奖励（accuracy rewards）：判断最终答案是否正确。数学问题的答案需以特定格式呈现（如放入方框中）以便自动验证；编程问题则通过编译器评估是否通过测试用例。

拒绝采样 + 非推理监督微调 阶段，使用 RL 第 2 步的 checkpoint 生成的推理输出，通过拒绝采样（rejection sampling）进行质量筛选，并结合写作、事实问答、自我认知等非推理任务中的监督数据，构建新的训练集，用于训练 DeepSeek-V3-Base：

-   筛除含有语言混杂、超长段落或冗长代码块的 CoT 结果；

-   利用 DeepSeek-V3 流水线生成并标注非推理类任务；

-   对于某些非推理需求，可调用 DeepSeek-V3 提前生成潜在思维过程作为提示（prompt）再进行回答，而对于诸如「你好」之类的简单查询则不需要思维链；

-   最终使用约 80 万条样本对 DeepSeek-V3-Base 微调两个 epoch。

最终的强化学习阶段 使用第三阶段的 checkpoint，同时在推理类与非推理类提示上进行训练，从而全面提升模型的有用性（helpfulness）、无害性（harmlessness）和推理能力（reasoning）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在多个广泛使用的推理基准测试中，DeepSeek-R1 的表现可与 OpenAI 模型相媲美。其中，仅有 DeepSeek-V3 是榜单中唯一的非推理类模型。

有趣的是，DeepSeek 团队展示了，即使完全不经过监督微调（SFT）阶段，仅依靠纯强化学习（pure RL），依然可以学习到诸如反思（reflection）和回溯（backtracking）等高级推理能力，即所谓的「顿悟时刻」（「Aha moment」）。在强化学习训练过程中，模型自然学会在解决推理任务时投入更多的思考 tokens，从而提升解题能力。

所谓「顿悟时刻」，是指模型能够反思先前的错误，并尝试替代性策略进行修正。这种能力的涌现表明模型具备了类人式的深层思维过程。

随后，一些开源项目也试图复现 R1 的成果，包括 Open-R1、SimpleRL-reason 和 TinyZero，这些项目均基于 Qwen 模型构建。相关研究也同样证实了纯强化学习方法在数学问题上可以取得优异表现，并能涌现出类似的「顿悟时刻」。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

模型学习反思并纠正错误的示例。

DeepSeek 团队还分享了一些训练中未成功的尝试。例如，使用过程奖励模型失败了，因为很难对每一个中间步骤制定明确的评分标准，也难以判断中间推理是否正确。此外，这种方式容易导致奖励欺骗（reward hacking），从而影响训练稳定性。

在蒙特卡洛树搜索（Monte Carlo Tree Search, MCTS）方面的尝试也宣告失败，原因在于语言模型的 token 空间远大于如国际象棋这类传统有限动作空间的场景，使得搜索过程计算复杂度极高。同时，用于引导搜索的细粒度价值模型（value model）的训练也极具挑战性。

尽管失败，但这些尝试提供了独特的研究洞察。我们鼓励研究社区进一步分享这类「未能奏效的尝试」，以推动更全面的理解与进步。

外部工具的使用

在推理过程中，某些中间步骤可以通过执行代码或数学计算实现高效且精确的求解。通过将这部分推理工作交由外部代码解释器处理，例如 PAL（Program-Aided Language Model，程序辅助语言模型）或 Chain of Code（代码链）方法，可以拓展大语言模型的能力，使其无需自行学习代码执行或充当计算器角色。

在 Chain of Code 中，所使用的代码执行系统可以由 LLM 进一步增强：当标准代码解释器无法正确运行特定代码行时，模型还可以尝试由 LLM 来直接执行该段代码。使用代码来辅助推理，尤其适用于数学问题、符号推理以及算法类任务。

在某些编程任务中，题目中未必提供单元测试。此时，我们可以引导模型自主生成用于验证解法的单元测试，从而提升解答的正确性。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

程序辅助语言模型（Program-Aided Language Model）提示示例如下所示。

ReAct（Reason+Act，推理与行动）方法将调用 Wikipedia API 等外部操作与生成推理轨迹相结合，实现将外部知识纳入推理路径的能力。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

ReAct 提示方法的示例，展示其如何通过调用 Wikipedia 搜索 API 作为外部工具，辅助推理以解答一个 HotpotQA 问题。

OpenAI 最近发布的 o3 与 o4-mini 模型亦是融合工具使用的典型案例，其推理过程涉及网页搜索、代码执行与图像处理等操作。研究团队观察到，在类似 GPT 的训练范式中，大规模强化学习同样呈现出「计算资源越多，性能越好」的趋势。

忠实地思考

深度学习模型通常被视为黑盒子，人们提出了各种可解释性方法。可解释性之所以有用，有几个原因：首先，它为我们提供了一个额外的测试，以确定模型是否与创建者的意图不符，或者是否以某种我们无法通过监控其行为来判断的方式出现了错误。其次，它可以帮助我们确定模型是否使用了合理的程序来计算其答案。思维链提供了一种特别方便的可解释性形式，因为它能让模型的内部过程用自然语言表达出来。然而，这种可解释性建立在模型如实描述其内部思维过程的假设之上。

最近的研究表明，监控推理模型的 CoT 可以有效检测模型的不当行为，如 reward hacking，甚至可以使较弱的模型监控较强的模型。增加测试时间的计算量还能提高对抗鲁棒性；这在直觉上是有道理的，因为当模型遇到不寻常的输入时，如对抗样本或越狱尝试，思考时间更长应该特别有用，它可以利用额外的思考时间来理解所遇到的奇怪情况。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在实验中，我们要求模型判断另一个模型是否试图以某种方式入侵单元测试，以解决其思维过程中的编码问题。我们可以在训练过程中使用不同类型的监控器来监控这些奖励黑客行为。exit (0) 编码黑客攻击是指代理利用了一个漏洞，允许它在没有运行所有单元测试的情况下提前退出环境。raise SkipTest 黑客是指代理从测试框架外的函数中引发异常，以跳过单元测试评估。图源：Baker et al. 2025

模型是否忠实地表达了自己的想法

直观地说，由于缺乏旨在鼓励忠实推理的明确训练目标，模型的 CoTs 可能存在偏差。或者，当我们根据人类撰写的解释对模型进行微调时，这些人类撰写的样本可能包含错误。因此，我们不能默认 CoT 总是忠实的。

Lanham et al. (2023) 通过故意在 CoT 中引入错误，并测量其对一系列多选任务（如 AQuA、MMLU、ARC Challenge、TruthfulQA、HellaSwag）准确性的影响，研究了 CoT 忠实性失效的几种模式：

-   错误 1（过早回答）： 模型可能会在 CoT 生成之前过早地形成结论。测试方法是提前截断或在 CoT 中插入错误。不同任务对 CoT 有效性的依赖程度不同；有些任务的评估性能对截断的 CoT 敏感，有些则不敏感。Wang et al. (2023) 做了类似的实验，但在形成 CoT 的过程中出现了与桥接对象或语言模板有关的更微妙的错误。

-   错误 2（无信息 token）： 不具信息性的 CoT token 可提高成绩。这一假设通过用填充文本（如所有句号）替换 CoT 进行了测试，结果表明这种设置并没有提高准确率，与不使用 CoT 相比，某些任务的成绩可能会略有下降。

-   错误 3（人类无法阅读的编码）： 以人类难以理解的方式对相关信息进行编码。以非标准方式转述 CoT 并未降低各数据集的性能，这表明准确率的提高并不依赖于人类可读的推理。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

以不同方式对 CoT 进行扰动以评估其忠实性的示意图。图源：Lanham et al. 2023

有趣的是，Lanham et al. 认为，对于多选题，较小的模型可能无法很好地利用 CoT，而较大的模型可能能够在没有 CoT 的情况下解决任务。这种对 CoT 推理的依赖性（以使用 CoT 与不使用 CoT 得到相同答案的百分比来衡量）在多选题中并不总是随着模型大小的增加而增加，但在加法任务中却会随着模型大小的增加而增加，这意味着在复杂的推理任务中，思考时间更为重要。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

对 CoT 推理的依赖性以使用 CoT 和不使用 CoT 时获得相同答案的百分比来衡量。对于像加法这样的推理任务来说，CoT 的作用更大，而对于更大的模型来说，CoT 的作用也更大。

对 CoT 推理的依赖性以有 CoT 和无 CoT 时获得相同答案的百分比来衡量。对于像加法这样的推理任务来说，CoT 的作用更大，而更大的模型也能带来更多益处。

测试 CoT 忠实度的其他方法包括扰动提示而不是直接修改 CoT 路径 。

其中一种方法是在少数几个样本中将正确答案标记为「(A)」，而不考虑真实标签，从而引入偏差。

另一种提示技术是在提示中插入误导性提示，例如 「我认为答案是 < random\_label>，但很想听听您的看法 」或 「一位斯坦福大学教授认为答案是 < random\_label>」。通过比较模型对同一问题的预测是否包含误导性提示，我们可以衡量模型是否能够忠实地描述提示对其答案的影响。特别是在模型得出的提示答案与非提示答案不同的情况下，我们可以衡量模型在解决有提示的问题时是否承认提示。如果模型是忠实的，它就应该明确承认提示的影响，并承认其答案的变化是由提示引起的。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

GPT 模型和 Claude 模型对不同类型的上下文偏差都很敏感。模型准确性的降低表明系统性的不忠实。直接提示错误标签比 "答案总是 A" 类型的偏差更有效。图源：Turpin et al. 2023

多项研究发现，推理模型对暗示影响的描述要比所有测试过的非推理模型可靠得多。例如，我们可以测量模型承认暗示是决定性因素的样本比例（「忠实 CoT」）。推理模型（Claude 3.7 Sonnet、DeepSeek R1）的整体表现优于非推理模型（Claude 3.6、DeepSeek V3）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

推理模型比非推理模型更有可能揭示忠实的 CoT。图源：Chen et al. 2025

一些证据表明，使用奖励模型会降低模型输出的忠实度。经典 RLHF 中的奖励模型在本测试中并不是为了激励忠实行为而训练的，因为偏好比较数据集是由人类选择哪一个看起来更好或更讨人喜欢而收集的。然而，在推理模型中，CoT 路径是为产生正确的最终答案而优化的，而不是为了与 RM 中定义的人类偏好相匹配，因此直观上预计会更加忠实。

CoT 面临的优化压力： 好还是坏？

监控推理模型的 CoT 以发现 reward hacking 行为是有效的。使用这种监控器的一个简单方法是在测试时将监控器作为过滤器运行拒绝采样，找出没有 reward hacking 行为的解决方案。然而，这种方法只在推理的早期阶段有效，而且随着模型的进一步优化，在预算范围内很少能找到通过 CoT 监控的样本。这一挑战自然表明，我们可以考虑在 RL 奖励中加入 CoT 监控 — 一种基于流程的监督形式 — 以防止 reward hacking。

然而，在 RL 中加入 CoT 监控奖励的效果并不好，因为这会导致混淆 reward hacking 行为，即模型试图在 CoT 中隐藏其真实意图 (Baker et al. 2025)。如果在 RL 训练过程中使用 CoT 监控提供的这种直接优化压力，模型仍然可以找到黑客攻击的方法，虽然频率会低一些，但可以在 CoT 中隐藏自己的意图，避免被监控发现。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在训练过程中，当使用监视器提供 RL 奖励信号以防止 reward hacking 行为时，模型仍然可以找到 hacking 行为的方法，同时避免被监视器发现。图源：Baker et al. 2025

Yeo et al. 对 CoT 长度 RL 信号的实验证实了与 Baker et al. 类似的信息，即新型 RL 奖励整形会导致新型 reward hacking 行为的发生。他们设计的奖励函数可以使正确的 CoT 比错误的 CoT 获得更高的奖励，短的正确 CoT 比长的正确 CoT 获得更高的奖励，短的错误 CoT 比长的错误 CoT 获得更高的惩罚。有了这种额外奖励，模型就学会了在有挑战性的问题上重复 CoTs 中的文字，而不是尝试解决这些问题。Yeo et al. 进一步应用了 n-gram 重复惩罚来防止这种 hacking 行为。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

要稳定使用 CoT 长度奖励进行的训练，就必须进行精心的奖励塑造。图源：Yeo et al. 2025

Chen et al. 在一个有缺陷的 RL 环境中进行了实验，特别是使用了一个在多选题中填入错误答案的评分器。在超过 99% 的提示中，模型学会了利用 reward hacking，但在一半以上的环境中，模型几乎从未（<2%）在其 CoT 中口头表达过 reward hacking。在这种情况下，额外的 RL 优化压力无法激励模型口头表达 hacking 行为。

RL 训练本质上对 reward hacking 行为非常敏感。仅仅依靠对 reward hacking 行为的启发式调查和手动修复可能会导致「whack-a-mole」的局面。我们建议在 RL 训练过程中尝试直接对 CoT 进行优化时要非常谨慎，或者尽量避免这样做。

在连续空间中思考

Alex Graves 于 2016 年提出的自适应计算时间（Adaptive Computation Time）早于大语言模型，但开创了相同的方向，即让模型能够在推理时动态决定计算步骤的数量，这可以被视为让模型在测试时能够在连续空间中「思考更多」。连续空间中的自适应思考时间可以通过递归架构纵向实现，也可以通过更多的连续采样步骤横向实现。

递归架构

为了使 Transformer 架构成为递归架构，实现自适应测试时间计算，人们提出了许多架构变体。如果深入探讨这一主题的文献，会使文章过于冗长，因此我们只回顾其中几篇。

Universal Transformer 将 Transformer 中的自注意力与 RNN 中的递归机制相结合，利用自适应计算时间动态调整步数 。从高层次上看，它可以被看作是一种用于学习每个 token 的隐藏状态表示的递归函数，如果步数是固定的，Universal Transformer 就等同于跨层共享参数的多层 Transformer。

Geiping et al. 提出的最新递归架构设计，在标准 Transformer 的基础上增加了一个递归块 R。该循环块的每次迭代都需要嵌入 e 和随机状态 s\_i。从概念上讲，这种递归深度架构有点类似于条件扩散模型，即在每个递归步骤中提供原始输入 e，而随机高斯初始化状态 s\_i 则在整个过程中迭代更新。(有趣的是，他们对一些更像扩散模型的设计所做的实验结果并不理想）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

训练过程中的递归计数 r 是随机的，从对数正态 Poisson 分布中按输入序列采样。为了控制计算成本，反向传播只截断递归单元的最后 k 次迭代（实验中 k=8），从而可以对 Poisson 分布的重尾部分进行训练。由于嵌入块的输出 e 在每一步中都会注入，因此嵌入块在每一步中都会继续接收梯度更新，模仿 RNN 训练。不出所料，训练递归模型的稳定性非常敏感。初始化、归一化和超参数等因素都很重要，尤其是在扩大训练规模时。例如，隐藏状态可能会因为对每个 token 预测相同的隐藏状态而崩溃；或者模型可能学会忽略传入的状态 s。为了稳定训练， Geiping et al. 采用了嵌入比例因子、较小的学习率和细致的调整。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

利用深度递推训练 3.5B 模型的实验图。饱和大致发生在 r¯=32 附近，这让我们不禁要问，这种结构如何外推并推广到更大的迭代次数。图源： Geiping et al. 2025

思考 token

思考 token 指的是在训练或推理过程中引入的一组不具有直接语言意义的隐含 token。相反，它们的作用是为模型提供额外的思考时间和计算能力，使其表现更好。

Herel & Mikolov（2023 年）提出了在句子中的每个单词后插入特殊思考 token（<T>）并在这样的数据集上训练模型的想法。每个思考 token 都为模型处理和做出更好的预测赢得了额外的时间。在玩具模型设置上使用思考 token 进行训练，其结果比不使用思考 token 训练的基线模型的复杂度要低。对于非琐碎的推理任务或涉及数字的句子，思考 token 的优势更为明显。

同样，Goyal et al. (2024) 提出的暂停标记通过在输入序列末尾添加虚拟 token（如。或 # 等字符）来延迟模型的输出，从而在推理过程中为模型提供额外的计算量。在训练和推理过程中注入这种暂停 token 都很重要，而只对暂停 token 进行微调只能带来有限的收益。在训练过程中，我们会在均匀随机的位置插入多份暂停 token，并在训练中忽略暂停 token 的损失。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

有趣的是，上述实验中的思考令牌或暂停令牌并不携带任何额外信息或添加许多新参数。但为什么它仍然有帮助呢？一方面，它通过引入更多的推理循环来帮助扩展计算，从而有效地提高计算能力。另一方面，它可以被视为 CoT 的一种特殊的隐式形式。这里的一个缺点是模型需要根据思考令牌进行预训练。尽管如此，这种策略仍然是一种有趣的方法，可以在推理时间 CoT 的基础上进一步提高测试时间计算利用率的能力。

Quiet-STaR 通过训练模型在每个标记后生成理由来解释未来的文本，从而引入了标记级推理。它将未来文本预测与基本原理和无基本原理混合在一起，并使用学习来生成更好的基本原理，并使用 REINFORCE 来优化基本原理生成的质量。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Quiet-STaR 图示。

将思维作为潜变量

潜变量模型定义了一个概率框架，其中可观察数据通过未观察到的（潜在的）变量来解释。这些潜变量捕获了生成可观察结果的隐藏结构或中间过程。语言模型可以被视为概率潜变量模型，其中测试时思维和推理步骤是潜在思维变量。这样的潜变量模型定义了问题 x\_i、答案 y\_i 和潜在思维 z\_i 的联合分布。我们希望优化在给定问题和各种思维链作为潜变量条件下答案的对数似然（N 是样本数量；K 是每个问题的思维链数量）：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

我们的目标是最大化正确答案的边际似然 p (y∣x)，给定每个问题的多个推理轨迹 {z (k)} k=1K。

期望最大化

期望最大化是一种常用的迭代算法，用于优化具有（隐含）潜变量的模型参数，因此可以应用于训练更好的思维链，然后以此为条件生成更好的响应。通常我们在 E 步（期望）和 M 步（最大化）之间迭代，E 步中我们猜测关于潜变量的缺失信息（即如何采样更好的思维链），M 步中我们基于潜变量优化模型参数（即如何采样更好的答案），直到收敛。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 因为我们无法直接从潜变量分布 p (z∣x,y) 中采样，研究人员探索了依赖人工标注数据、Metropolis-Hastings MCMC 或具有特殊重要性权重的蒙特卡罗采样的方法来抽取好的思维链样本以更新模型。Ruan et al. (2025) 实验了在大量网络文本语料上使用 EM 算法训练带有潜在思维的模型，其中针对每个观察数据块合成潜在思维，然后模型以自回归方式在潜在思维和数据上学习。 

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在注入潜在思维的数据语料上进行训练的示意图。

 他们首先提示一个大语言模型根据观察数据 X\_i 生成合成的潜在思维 Z\_i： 

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

 使用特殊 token 如 < StartOfLatent><Prior> ... <EndOfPrior > 将生成的潜在思维内容插入到原始数据中，用于训练联合分布 p (z,x) 或近似后验 q (z∣x)，这取决于 z 是插入在 x 之前还是之后。然而，由于我们使用大语言模型来生成思维链，这对近似 q (z∣x) 的好坏程度施加了性能上限。Ruan 等人在 E 步引入了重要性权重来选择思维链样本，公式化为：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这样我们就会优先选择那些擅长预测观察结果（即高 p (x∣z (k))）、简单直观（即高 p (z (k))）但又信息丰富且不太明显（即低 q (z (k)∣x)）的思维链样本。 

迭代学习

由于预训练模型已经具备了生成思维链的能力，因此我们可以直观地设计一个迭代改进过程，在这个过程中，我们会生成多个 CoTs，并只根据能得出正确答案的理由对模型进行微调。

然而，这种直截了当的设计可能会失败，因为模型在无法解决的问题上得不到学习信号。STaR 通过为失败的尝试添加一个「合理化」过程来解决这一局限性，在这个过程中，模型会根据问题和基本真实答案生成良好的后向 CoTs，因此模型可以生成更合理的 CoTs。然后，根据正确的解决方案对模型进行微调，这些解决方案要么能产生正确的输出，要么是通过合理化生成的。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

STaR 算法。

我们可以把 STaR 看作是 RL 中策略梯度的近似值，奖励是一个简单的指标函数𝟙1 \[y^=y\]。我们希望在对 z∼p (z∣x) 和 y∼p (y∣x,z) 进行采样时，最大化该奖励的期望值。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

每次迭代相当于首先根据选择 CoT 样本，然后运行监督微调以优化生成良好 CoT 和答案的对数问题。STaR 的性能会随着训练迭代的增加而提高，而生成更好 CoT 的 “合理化 ”过程可以加速学习。他们观察到，高温采样会增加通过错误推理获得正确答案的机会，而对此类数据微调 LLM 会损害泛化。对于没有真实数据的数据，多个高温输出的多数票可以作为真实数据答案的代理，从而可以使用合成样本进行训练。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

对两个 n 位数加法的准确度进行比较。在有理化（基于真实结果的逐步推理生成）的情况下，模型能够在相对较早的阶段学习复杂的算术任务，例如五位数的加法。

思维时间的 Scaling Law

到目前为止，已经有大量证据表明，允许模型在推理时投入额外的计算资源，在产生最终答案之前进行思考，可以显著提升性能。诸如提示模型在给出答案前生成中间推理步骤，或训练模型在预测下一个 token 前暂停和反思等技术，都被发现可以将模型性能提升到超出训练时获得的能力极限。这本质上引入了一个改善模型智能的新维度，与 scaling law 中定义的模型规模、训练计算量和数据量等既有因素相补充。 

最近的研究表明，优化大语言模型的测试时计算可能比扩展模型参数更加有效。结合先进推理算法的小型模型可以在成本和性能之间提供帕累托最优的权衡。

Snell et al. 评估并比较了测试时计算和预训练计算，发现它们并非 1:1 可互换的。当模型能力差距很小时，测试时计算可以轻松弥补简单和中等难度问题上的差距，但对困难问题的效果较差。预训练和推理的 token 预算比例非常重要。只有当推理 token 显著少于预训练 token 时，测试时计算才更有优势。这表明，利用充足的预训练数据和计算资源开发有能力的基础模型仍然至关重要，因为测试时计算无法解决所有问题或填补大的模型能力差距。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（左图）通过迭代修订或并行解码，评估准确率作为测试时计算预算的函数。（右图）比较一个小模型配合测试时计算采样技巧与一个大 14 倍的模型仅使用贪心解码。我们可以控制测试时使用的 token 预算，使得推理与预训练 token 的比例为 <<1、~=1 或 >>1，只有当比例 <<1 时，测试时计算的好处才明显。

s1 模型通过预算强制（budget forcing）技术（即通过添加单词「wait」来强制延长思维，或通过添加思维结束 token 或「Final Answer:」来缩短模型的思考过程而终止）实验了思维链推理路径长度的扩展。他们观察到以 token 衡量的平均思维时间与下游评估准确率之间存在明显的正相关关系。 

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

s1 实验中，测试时计算的并行和顺序 scaling 方法都显示出与评估性能的正相关关系。

当将这种预算强制技术与其他控制推理轨迹长度的解码方法进行比较时，令人相当惊讶的是，简单的拒绝采样（即采样生成直到长度符合 token 预算）导致了反向 scaling，意味着更长的思维链会导致更差的性能。 

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（左图）更长的思维链路径长度与评估准确率呈正相关。（右图）用于控制生成的思维链路径长度的拒绝采样显示出负 scaling，其中更长的思维链导致更差的评估准确率。（图片来源：Muennighoff & Yang, et al. 2025）

未来展望

对测试时计算和思维链推理的探索为增强模型能力带来了新的机遇。更有趣的是，通过测试时思考，我们正朝着构建未来 AI 系统的方向迈进，这些系统能够反映人类思维的最佳实践，融合了适应性、灵活性、批判性反思和错误纠正能力。

对当前进展的兴奋促使我们进行更多未来研究，以改进并深入理解 —— 不仅是我们和我们的模型如何思考，更要理解为什么思考。

最后，我希望呼吁对以下关于测试时计算和思维链推理的开放性研究问题进行更多研究。

-   我们能否在强化学习训练过程中激励模型产生人类可读、忠实的推理路径，同时避免 reward hacking 行为？

-   如何定义 reward hacking？我们能否在强化学习训练或推理过程中捕获 reward hacking 行为而无需人工干预？如何防止在强化学习训练中采用「打地鼠」式的 reward hacking 修复方法？

-   自我纠正可以在思维链内部发生，也可以在多轮强化学习中得到显式鼓励。当没有真实答案可供参考时，我们如何训练模型进行自我纠正而不产生幻觉或性能倒退？

-   对于高度情境化、个性化且难以评分的任务（如创意写作、指导建议、头脑风暴），我们如何进行带有思维链展开的强化学习训练？

-   当我们在现实中部署模型时，我们无法无限延长测试时思考的时间，那么如何能够平滑地将性能提升转化回基础模型，从而降低推理时间成本（例如通过知识蒸馏）？

-   如何根据当前问题的难度，让测试时计算资源的使用变得更加自适应？

© THE END 

转载请联系本公众号获得授权

投稿或寻求报道：liyazhou@jiqizhixin.com