# 注意力机制谱系：从 MHA、GQA、MLA 到 KDA、DSA 与 QSA

> 更新于 2026 年 8 月 26 日。本文补充《国内大模型注意力路线》，重点回答两件事：这些缩写最早来自谁、同一家族里的不同方法究竟差在哪里。

## 先说最重要的结论

MHA、GQA、MLA、KDA、DSA 看起来都是“注意力缩写”，其实不在同一个层级：

- **MHA、MQA、GQA、MLA**主要回答：历史信息以什么形式保存，每个查询头是否共用、怎样压缩 KV。它们通常仍然可以查看全部历史。
- **Linear Transformer、DeltaNet、GDN、KDA**主要回答：能否不保存逐 Token 的完整历史，而把历史持续写入一个有限状态。
- **Sparse Transformer、DSA、MSA、QSA**主要回答：面对长历史，能否只读取被选中的少数位置或区块。
- **Hybrid Attention**不是一种单独的注意力，而是把上述方法按层混合。例如 K3 的 KDA + MLA、Qwen3-Next 的 GDN + 全局注意力。

因此，之前所说的“注意力机制可以归成 5 类”，更适合作为一张理解地图，而不是严格的学术分类。更准确的五类是：**全局 Softmax、线性/循环、固定稀疏、动态/压缩稀疏、混合架构**。它们之间可以交叉组合，并非五选一。

## 一、全局 Softmax 家族：都能翻整本书，区别是怎样保存书页

### 1. 方法谱系

| 方法 | 命名或代表论文 | 最早提出团队 | 核心变化 |
|---|---|---|---|
| **MHA**（Multi-Head Attention） | [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762)，2017 | Google Brain / Google Research | 每个查询头拥有各自的 Q、K、V 投影，是 Transformer 的原始标准方案 |
| **MQA**（Multi-Query Attention） | [*Fast Transformer Decoding: One Write-Head is All You Need*](https://arxiv.org/abs/1911.02150)，2019 | Google，Noam Shazeer | 多个查询头共用同一组 K、V，大幅减少 KV Cache 和解码带宽 |
| **GQA**（Grouped-Query Attention） | [*GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints*](https://arxiv.org/abs/2305.13245)，2023 | Google Research，Joshua Ainslie 等 | 把查询头分组，每组共用一组 K、V，是 MHA 与 MQA 的折中 |
| **MLA**（Multi-Head Latent Attention） | [*DeepSeek-V2*](https://arxiv.org/abs/2405.04434)，2024 | DeepSeek-AI | 不只是减少 KV 头，而是先把每个 Token 的 KV 压进低维潜变量，需要时再恢复各头所需表示 |

这里的“最早”相对清晰：MHA、MQA、GQA、MLA 都有明确的命名论文。需要区分的是，**提出者和采用者不是一回事**：例如 Qwen、GLM、Hunyuan 大量使用 GQA，但 GQA 来自 Google；Kimi K2 和 DeepSeek V3 使用 MLA，而 MLA 来自 DeepSeek。

### 2. 用“档案副本”理解四者差异

- **MHA：每个阅读员都有一整套自己的档案。**信息最丰富，但副本最多。
- **MQA：所有阅读员共用一套档案。**保存和搬运最省，但不同阅读员看到的底稿缺少差异。
- **GQA：几个阅读员共用一套档案。**比 MHA 省，比 MQA 更有表达余量，因而成为很多模型的稳妥默认值。
- **MLA：每页只存一张压缩母版，需要时再生成各阅读员所需的版本。**通常能在更小 KV Cache 下保留较强表达力，但投影、位置编码和推理内核更复杂。

它们并不是“大致相同、换个名字”。但它们解决的是**同一个问题的不同压缩力度**，并没有从根本上改变“当前 Token 可以回看全部历史”这一点。长上下文越长，全局读取的计算仍会增长。

一句话排序：

> **MHA 更偏表达力，MQA 更偏极致省缓存，GQA 是工程折中，MLA 试图用更复杂的低秩压缩同时保住质量和缓存效率。**

## 二、线性/循环家族：不再保存整套书页，而是持续改写工作笔记

### 1. 这条路线没有唯一“祖师爷”

“线性注意力”是一个宽泛方向，早期有多条并行路线。若讨论今天大模型里可递推的线性注意力，比较合理的谱系是：

| 方法 | 命名或代表论文 | 团队 | 核心贡献 |
|---|---|---|---|
| **Efficient Attention** | [*Efficient Attention: Attention with Linear Complexities*](https://arxiv.org/abs/1812.01243)，2018 | Zhuoran Shen、商汤、香港中文大学等 | 较早利用矩阵乘法重排实现线性复杂度；主要从视觉任务出发 |
| **Linear Transformer** | [*Transformers are RNNs*](https://arxiv.org/abs/2006.16236)，2020 | Katharopoulos 等，Idiap/EPFL 学术团队 | 用核特征和乘法结合律把因果注意力写成可逐 Token 更新的状态，是今天“线性注意力像 RNN”的关键里程碑 |
| **Performer** | [*Rethinking Attention with Performers*](https://arxiv.org/abs/2009.14794)，2020 | Google Research / Google Brain 等 | 用随机特征近似 Softmax，目标是尽量保留传统注意力的行为 |
| **DeltaNet** | [*Linear Transformers Are Secretly Fast Weight Programmers*](https://arxiv.org/abs/2102.11174)，2021 | Schlag、Irie、Schmidhuber | 用 Delta Rule 更新有限状态：先纠正旧映射，再写入新信息，减少简单累加造成的记忆冲突 |
| **Gated DeltaNet（GDN）** | [*Gated Delta Networks*](https://arxiv.org/abs/2412.06464)，2024 | MIT CSAIL / NVIDIA | 在 Delta Rule 上加入可学习遗忘门，让模型能主动清理旧状态；后来被 Qwen3-Next、Qwen3.5 等采用 |
| **Lightning Attention-2** | [*A Free Lunch for Handling Unlimited Sequence Lengths*](https://arxiv.org/abs/2401.04658)，2024 | Zhen Qin 等，OpenNLPLab 路线；后由 MiniMax 大规模产品化 | 用分块计算和硬件友好内核兑现线性注意力的理论速度，创新重点更偏计算实现 |
| **KDA**（Kimi Delta Attention） | [*Kimi Linear*](https://arxiv.org/abs/2510.26692)，2025 | Moonshot AI / Kimi Team | 在 GDN 上做更细粒度的门控，并配套专用分块算法；K3 以 KDA 为主、MLA 为辅 |

所以，不能说“Qwen 发明了 GDN”。更准确的是：**MIT/NVIDIA 论文提出 GDN，Qwen 把它推进旗舰架构；Moonshot 则在这条谱系上继续发展出 KDA。**

### 2. 同为线性注意力，差别主要在“怎样写笔记”

- **早期 Linear Transformer：不断往笔记里累加。**结构简单，但有限笔记容易被大量内容挤满，相似 Key 之间也会互相干扰。
- **Performer：尽量用数学近似模拟原来的 Softmax 阅读方式。**理论边界更清楚，但随机特征数量、近似误差和实际常数会影响效果与速度。
- **DeltaNet：写新内容前先修改或擦除冲突的旧记录。**记忆管理更精确，但状态更新更复杂。
- **GDN：再加一个“何时整体遗忘”的门。**它比 DeltaNet 更善于清理过时内容，是 Qwen 选择它的重要原因。
- **KDA：把遗忘和更新控制做得更细。**表达力更强，代价是状态、训练和内核实现更复杂。
- **Lightning Attention：重点是怎样把这套笔记机制切块并高效跑在 GPU 上。**它与 KDA/GDN 不完全是同一维度的竞争。

线性家族共同的收益是：状态大小不随上下文逐 Token 增长，超长文本的理论成本漂亮。共同的弱点也很明确：**原文细节被折叠进有限状态后，无法像全注意力那样随时精确回到任意旧 Token。**这正是 K3、Qwen3-Next、MiniMax M1 都没有完全取消全局注意力的原因。

## 三、稀疏家族：原文仍在，但只翻被选中的页

### 1. 固定稀疏和动态稀疏是两代思路

| 方法 | 命名或代表论文 | 最早提出团队 | 怎样选历史 |
|---|---|---|---|
| **Sparse Transformer** | [*Generating Long Sequences with Sparse Transformers*](https://arxiv.org/abs/1904.10509)，2019 | OpenAI，Rewon Child 等 | 按预先设计的固定模式连接，计算较规整 |
| **Longformer** | [*Longformer: The Long-Document Transformer*](https://arxiv.org/abs/2004.05150)，2020 | Allen Institute for AI | 局部滑窗加少数全局位置，适合长文档编码 |
| **BigBird** | [*Big Bird: Transformers for Longer Sequences*](https://arxiv.org/abs/2007.14062)，2020 | Google Research | 局部窗口、随机连接和全局 Token 的组合 |
| **DSA**（DeepSeek Sparse Attention） | [DeepSeek-V3.2-Exp](https://api-docs.deepseek.com/news/news250929/)，2025 | DeepSeek-AI | 轻量索引器根据当前 Query 动态打分，再读取 Top-K 历史位置 |
| **CSA / HCA** | [DeepSeek-V4](https://api-docs.deepseek.com/news/news260424/)，2026 | DeepSeek-AI | CSA 先低比例压缩再动态 Top-K；HCA 高比例压缩后读取全部压缩条目，严格说 HCA 是“压缩全局”而非稀疏选择 |
| **IndexShare for DSA** | [GLM-5.2](https://z.ai/blog/glm-5.2)，2026 | Z.ai / GLM | 让相邻四层复用同一个 DSA 索引结果；是索引器复用优化，不是新的注意力范式 |
| **MSA**（MiniMax Sparse Attention） | [*MiniMax Sparse Attention*](https://arxiv.org/abs/2606.13392)，2026 | MiniMax | 按 GQA 组选择相关 KV Block，再对选中的块做精确注意力；块级访问更适合 GPU |
| **HiLS Attention** | [*Hierarchical Sparse Attention Done Right*](https://arxiv.org/abs/2607.02980)，2026 | Tencent Hunyuan | 用压缩 Chunk Key 分层选择区块，并端到端学习；目前主要是研究路线 |
| **QSA**（Qwen Sparse Attention） | Qwen3.8-Flash-Next / Qwen4 架构预告，2026 | Qwen Team | 截至本文日期只有名称和预告，尚无论文；Token 级还是 Block 级、索引器和 Top-K 均未知 |

### 2. 同为稀疏注意力，真正的差别是“目录怎样做”

- **固定稀疏：目录是印刷时写死的。**滑窗、固定间隔等模式规则、内核好做，但遇到任意位置的远程细节，可能根本没有直达路径。
- **动态稀疏：目录根据当前问题临时生成。**DSA 能为不同 Query 选择不同历史，召回更灵活；代价是要训练索引器，还要承担“资料存在但索引没选中”的风险。
- **块稀疏：目录指向章节，而不是单个字。**MSA 牺牲一点选择精度，换取连续内存访问和更容易落地的 GPU 加速。
- **压缩后稀疏：先把多页合成卡片，再查目录。**DeepSeek V4 的 CSA 同时减少历史条目和实际读取量，但压缩与检索可能连续丢失信息。
- **共享索引：几位阅读员共用一次查目录的结果。**GLM IndexShare 进一步省计算，但牺牲了每层独立选择的自由度。

因此，DSA、MSA、CSA 绝不是“大致相同”。它们都采用“先选再读”，但分别押注 **Token 级精度、Block 级硬件效率、压缩后的极限成本**。

QSA 目前只能确定属于 Qwen 自己命名的稀疏路线，不能仅凭名字断言它是 DSA、MSA 或某种全新算法。等正式技术报告时，最值得看的是：**按 Token 还是 Block 选、索引器怎样训练、Top-K 多大、是否保留局部窗口和全局兜底层。**

## 四、混合架构没有单一发明者

混合架构更像一份配方，而不是一种基础算法：

| 模型 | 混合方式 | 读书类比 |
|---|---|---|
| **Kimi K3** | 多数 KDA + 少数全局 MLA | 平时改写工作笔记，隔几层仍能翻全部压缩档案 |
| **Qwen3-Next / 3.5** | 多数 GDN + 定期全局 Gated Attention | 三层写笔记，一层翻原书 |
| **Qwen3.8-Flash-Next（预告）** | GDN Hybrid Layers + QSA | 很可能是写笔记 + 动态查目录，但层数比例和全局兜底尚未公布 |
| **DeepSeek V4** | 局部滑窗 + CSA + HCA | 近处直接看原文，远处使用低压缩检索卡或高度压缩摘要 |
| **MiniMax M3** | 全局/局部稠密层 + MSA 稀疏层 | 关键层完整阅读，其余层按章节检索 |

混合正在成为主流，并不是因为团队“不会二选一”，而是三种机制的短板正好互补：全局注意力可靠但贵，线性注意力便宜但会压缩细节，稀疏注意力保留原文但可能漏选。

## 五、四个经常被误算成“注意力类型”的东西

- **FlashAttention**：Tri Dao 等在 2022 年提出的 [IO-aware 精确注意力算法](https://arxiv.org/abs/2205.14135)。它通常不改变 MHA/GQA 的数学结果，只是让同一种全局注意力少搬数据、跑得更快。
- **RoPE**：位置编码，来自 [RoFormer](https://arxiv.org/abs/2104.09864)，不是“看哪些 Token”的注意力路线。
- **N-gram Embedding**：短语或局部模式的条件查表记忆，不是注意力。Qwen3.8-Flash-Next 预告中的 **51B N-gram embeddings** 应理解为额外的静态模式库，不能归入 GDN 或 QSA，也不能简单与 125B 主模型参数相加后当成每 Token 计算量。
- **MTP**：一次预测多个后续 Token 的训练/解码机制，也不是注意力。

## 最后：看到一个新缩写，先问四个问题

1. **它还保留 Softmax 全局读取吗？**如果保留，通常属于 MHA/GQA/MLA 的改造；如果改成有限状态，才更接近线性/循环路线。
2. **历史以什么形式存在？**逐 Token KV、共享 KV 头、低维潜变量、固定大小状态，还是压缩 Block？
3. **选择是固定还是随 Query 变化？**固定滑窗容易加速；动态 Top-K 更灵活，但会增加选择成本和漏召回风险。
4. **创新发生在算法还是实现层？**KDA、DSA 改变记忆或选择规则；FlashAttention、Lightning Attention-2 很大一部分价值在高效计算与内核。

最简洁的判断是：

> **MHA/GQA/MLA 是“档案怎么存”，GDN/KDA 是“笔记怎么改”，DSA/MSA/QSA 是“原文怎么找”。同一家族的方法共享大方向，但压缩粒度、记忆规则、选择单位和硬件友好度足以造成实质差异。**

## 主要资料

- 全局注意力：[Transformer / MHA](https://arxiv.org/abs/1706.03762)、[MQA](https://arxiv.org/abs/1911.02150)、[GQA](https://arxiv.org/abs/2305.13245)、[DeepSeek-V2 / MLA](https://arxiv.org/abs/2405.04434)
- 线性注意力：[Efficient Attention](https://arxiv.org/abs/1812.01243)、[Linear Transformer](https://arxiv.org/abs/2006.16236)、[Performer](https://arxiv.org/abs/2009.14794)、[DeltaNet](https://arxiv.org/abs/2102.11174)、[Gated DeltaNet](https://arxiv.org/abs/2412.06464)、[Lightning Attention-2](https://arxiv.org/abs/2401.04658)、[Kimi Linear / KDA](https://arxiv.org/abs/2510.26692)
- 稀疏注意力：[Sparse Transformer](https://arxiv.org/abs/1904.10509)、[Longformer](https://arxiv.org/abs/2004.05150)、[BigBird](https://arxiv.org/abs/2007.14062)、[DeepSeek DSA](https://api-docs.deepseek.com/news/news250929/)、[DeepSeek V4](https://api-docs.deepseek.com/news/news260424/)、[GLM IndexShare](https://z.ai/blog/glm-5.2)、[MiniMax MSA](https://arxiv.org/abs/2606.13392)、[Tencent HiLS](https://github.com/Tencent-Hunyuan/HiLS-Attention)
- 实现与相邻机制：[FlashAttention](https://arxiv.org/abs/2205.14135)、[RoFormer / RoPE](https://arxiv.org/abs/2104.09864)、[SCONE N-gram](https://arxiv.org/abs/2502.01637)、[DeepSeek Engram](https://arxiv.org/abs/2601.07372)

