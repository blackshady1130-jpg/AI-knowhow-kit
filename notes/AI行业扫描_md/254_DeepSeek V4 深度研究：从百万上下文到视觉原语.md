# DeepSeek V4 深度研究：从百万上下文到视觉原语

- 日期：2026-05-04
- 任务口径：基于用户提供材料，不做外部搜索
- 目标读者：AI 战略、产品、评测、行业分析同事；默认非纯技术背景
- 主要材料：
  - `C:\Users\Administrator\Downloads\DeepSeek_V4.pdf`
  - `AI report\DeepSeek_V4_tech_report_analysis_2026-04-25.md`
  - `C:\Users\Administrator\Downloads\Thinking_with_Visual_Primitives.pdf`
  - `D:\yantao\文件夹中转保存\DeepSeek相关访谈.md`

## 一句话结论

DeepSeek V4 最值得讲的不是“又一个更强开源模型”，而是 DeepSeek 把能力竞争推进到“长上下文压缩、低精度训练、后训练工艺、Agent 沙箱、评测闭环、视觉指代机制”的整栈工程；后续 visual primitives paper 则说明它正在把同一套“压缩加定位”的系统思路，延伸到多模态推理。

## 0. 这份新稿相比旧解读新增了什么

之前基于 tech report 的解读已经抓住了主线：V4 是长上下文与 agent 时代的系统设计。新增访谈和 visual primitives paper 后，判断需要向三个方向加深。

| 新材料 | 新增信息 | 对旧判断的修正 |
| --- | --- | --- |
| 晚点访谈 | V4 不是 R1 级别的新范式，而是在既有 long reasoning / test-time scaling 路线上解决计算瓶颈；四个新部件同时上线导致训练和适配复杂度组合爆炸 | 不宜把 V4 包装成“范式革命”，更应讲成“系统级耦合优化的胜利” |
| 晚点访谈 | API 定价上探、训练成本不再披露、token 消耗变长、用户用脚投票成为关键变量 | 从“低成本神话”转向“单位任务完成成本”：价格、思考长度、吞吐、成功率要一起看 |
| visual primitives paper | DeepSeek 提出 Reference Gap：多模态推理的瓶颈不只是看不清，而是语言无法精确指代视觉空间 | V4 的长上下文压缩不是孤立技术，它可能成为多模态 System-2 推理的底座 |
| visual primitives paper | 基于 DeepSeek-V4-Flash，加入 DeepSeek-ViT、视觉 token 压缩、box/point 原语、专门 SFT/RL/RFT/OPD 流程 | DeepSeek 的后训练路线不只适用于文本专家合并，也可迁移到视觉能力专家合并 |
| 内库定向召回 | BabyVision、Agent Infra、模型性价比等历史锚点与本次材料高度同频 | 组会中可以把 V4 放进更大趋势：评测从答题转向任务，Agent infra 从 uptime 转向 resumability，视觉从语言描述转向视觉操作 |

## 0.1 术语速查：这些词分别发生在模型生命周期哪里

这部分建议作为组会前置材料。读者不需要掌握公式，但需要知道每个术语属于训练模型的哪一环、解决什么问题、DeepSeek 做了什么、为什么值得关注。

### A. 架构与长上下文：决定模型“怎么存信息、怎么取信息”

| 术语 | 发生环节 | 通俗解释 | DeepSeek V4 做了什么 | 主要好处 | 创新层级 |
| --- | --- | --- | --- | --- | --- |
| MoE, Mixture-of-Experts | 模型架构 / 预训练 / 推理 | 把模型做成很多“专家”，每个 token 只激活一小部分专家。不是每次都调用全模型。 | V4-Pro 是 1.6T 总参数、49B 激活；V4-Flash 是 284B 总参数、13B 激活。 | 总容量大，但单次推理成本相对低；适合扩展知识和能力容量。 | 架构路线延续 + 激活比进一步激进化 |
| Total Params | 模型规模描述 | 模型所有参数总量，代表潜在容量。 | V4-Pro 达到 1.6T，Flash 为 284B。 | 反映模型可容纳知识和能力的上限，但不直接等于推理成本。 | 规模指标 |
| Activated Params | 推理成本描述 | 每个 token 实际调用的参数量。MoE 模型里比总参数更接近推理成本。 | V4-Pro 每 token 激活 49B，约 3% 激活比。 | 把“模型容量”和“每次调用成本”解耦。 | 架构效率指标 |
| 激活比 | 架构效率评估 | 激活参数 / 总参数。越低说明每次只调用越小比例的专家，但太低会带来训练不稳。 | V4-Pro 约 3%，比 V3 的约 5.5% 更激进。 | 在成本受限下放大模型容量。 | 工程风险较高的架构优化 |
| Hash Routing / HashTop-K MoE | MoE 路由 / 预训练 | 决定 token 分配给哪些专家。普通路由由模型算亲和度，哈希路由用 token ID 做更固定的专家分配。 | V4 在前 3 个 MoE 层使用 hash routing。 | 缓解早期层专家路由集中、负载不均的问题。 | 路由机制优化 |
| MLA, Multi-head Latent Attention | 注意力架构 / 推理效率 | DeepSeek V2/V3 使用的低成本注意力机制，通过 latent 压缩降低 KV cache。 | V4 放弃 MLA，转向 MQA + CSA/HCA 混合注意力。 | 说明开源模型架构尚未收敛；长上下文压缩需要重新设计。 | 路线切换信号 |
| MQA, Multi-Query Attention | 注意力架构 / 推理 | 多个 query head 共享较少的 key/value，降低 KV cache 和带宽压力。 | 访谈称 V4 相比 MLA 更接近 MQA，再叠加 CSA/HCA。 | 降低长上下文推理中的显存和带宽负担。 | 经典机制的重新组合 |
| SWA, Sliding Window Attention | 注意力架构 / 长上下文 | 只重点看最近一段上下文，像短期记忆。 | V4 每层保留滑动窗口分支，用于近距离细节。 | 避免远距离压缩损失近期细节。 | 架构组件 |
| CSA, Compressed Sparse Attention | 注意力架构 / 长上下文 / 推理 | 先把若干 token 压成一个 KV 条目，再从压缩条目里挑 top-k 重点看。 | V4 CSA 使用 4:1 压缩；Pro 的 top-k 为 1024，Flash 为 512。 | 在长上下文中保留“可检索重点”，降低计算和 KV cache。 | 核心架构创新 |
| HCA, Heavily Compressed Attention | 注意力架构 / 超长上下文 | 更激进地把大量 token 压成高度浓缩表示，保留远距离整体语义。 | V4 HCA 使用 128:1 压缩。 | 让 1M context 不至于被远距离历史拖垮。 | 核心架构创新 |
| Hybrid Attention | 注意力架构 | 同时使用 SWA、CSA、HCA，让不同层从不同尺度看上下文。 | V4 把 CSA 和 HCA 交错放在不同层，并配合 SWA。 | 近处看细节，中距离查重点，远距离看轮廓。 | 系统级架构组合 |
| KV Cache | 推理系统 / 长上下文 | 模型生成时缓存历史 token 的 key/value，避免每次重新计算。长上下文越长，KV cache 越大。 | V4 在 1M context 下，Pro 的 KV cache 约为 V3.2 的 10%，Flash 约为 7%。 | 大幅降低长对话、长文档、agent 任务的显存成本。 | 推理效率核心指标 |
| FLOPs | 训练 / 推理成本 | 浮点计算量。单 token 推理 FLOPs 越低，生成一个 token 的计算压力越小。 | V4-Pro 在 1M context 下单 token FLOPs 为 V3.2 的 27%；Flash 约为 10%。 | 支撑更长上下文和更多 test-time compute。 | 系统效率指标 |
| 1M Context | 产品能力 / 架构结果 | 模型一次可读约 100 万 token，但不代表完美记住全部内容。 | V4 系列原生支持 1M context，并通过 CSA/HCA 降低成本。 | 长文档、长程 agent、多轮工具调用可用空间变大。 | 能力结果，不是单点创新 |
| mHC, Manifold-Constrained Hyper-Connections | 模型架构 / 深层信号传递 | 改造层与层之间的残差连接，让深模型里的信息流更宽、更稳定。 | V4 引入 mHC，并用 Sinkhorn 约束改善稳定性。 | 提升深层模型训练和推理时的信息传递能力。 | 架构组件创新 |
| Sinkhorn-Knopp | 架构约束 / 数值稳定 | 一种矩阵归一化方法，用于让分配更均衡。 | V4 的 mHC 中使用 Sinkhorn-Knopp 迭代。 | 降低超连接带来的训练不稳定。 | 数学工具工程化应用 |

### B. 训练工艺与数值精度：决定模型“能不能稳定训出来”

| 术语 | 发生环节 | 通俗解释 | DeepSeek V4 做了什么 | 主要好处 | 创新层级 |
| --- | --- | --- | --- | --- | --- |
| Pre-training | 预训练 | 用海量语料学习语言、代码、数学、世界知识和基础模式。 | Flash 训练 32T tokens，Pro 训练 33T tokens；数据强调 math、code、long documents、multilingual、agentic data。 | 形成基础能力和知识底座。 | 基础训练阶段 |
| Mid-training | 预训练后段 / 能力倾斜 | 在基础预训练后加入更有方向性的能力数据。 | V4 在 mid-training 阶段加入 agentic data。 | 让模型更适合工具调用、代码、长程执行等任务。 | 数据配方优化 |
| Context Extension | 预训练策略 | 训练时逐步拉长序列，而不是一开始就上 1M。 | V4 从 4K 逐步扩展到 16K、64K、1M。 | 降低长上下文训练难度，逐步适应超长输入。 | 训练课程设计 |
| Sample-level Attention Masking | 预训练数据组织 | 把不同样本打包到同一序列时，用 mask 防止它们互相“串线”。 | V4 采用 sample-level attention masking。 | 提升数据打包效率，同时降低跨样本污染。 | 数据/训练细节优化 |
| Muon Optimizer | 预训练 / 后训练 / 优化器 | 与 AdamW 的逐元素更新不同，Muon 更强调对矩阵整体做正交化更新。 | V4 大部分参数使用 Muon，并使用 0.18 update rescaling factor 和 10 次 hybrid Newton-Schulz 迭代。 | 提高收敛效率和训练稳定性，节省 optimizer state。 | 训练工艺核心变量 |
| AdamW | 预训练 / 后训练 / 优化器 | 传统大模型常用优化器，对每个参数独立维护动量和二阶状态。 | V4 仍在 embedding、prediction head、RMSNorm 等模块使用 AdamW。 | 与 Muon 互补，保留对特定模块更稳的更新方式。 | 经典基线 |
| Hybrid Newton-Schulz | Muon 内部计算 | 用迭代方式近似矩阵正交化。 | V4 使用 8 步快速收敛 + 2 步稳定化的 hybrid 方案。 | 让 Muon 的矩阵更新更稳定、更精确。 | 优化器实现细节 |
| Anticipatory Routing | 预训练稳定性 / MoE 路由 | 遇到 loss spike 时，用历史参数提前计算路由，打断路由和特征同步恶化的循环。 | V4 在 loss spike 触发时短暂启用，并把额外 wall-clock 控制在约 20%。 | 缓解 MoE 训练中的突发不稳定。 | 训练稳定性工程创新 |
| SwiGLU Clamping | 预训练稳定性 | 对激活值做范围限制，避免异常大值引发训练不稳。 | V4 把 SwiGLU 的线性部分 clamp 到 [-10, 10]，gate 上界设为 10。 | 抑制 outliers，降低 loss spike 风险。 | 训练稳定技巧 |
| FP8 / BF16 / FP4 / INT4 | 训练和推理精度 | 不同位宽的数值格式。位宽越低，显存和带宽越省，但训练更难。 | V4 预训练主要用 FP8；后训练和 rollout/部署中大量使用 FP4；KV cache 中 RoPE 维度用 BF16，其余用 FP8。 | 降低显存、带宽和推理延迟。 | 低精度工程路线 |
| FP4 QAT, Quantization-Aware Training | 后训练 / 部署一致性 | 训练时模拟低精度误差，让模型提前适应部署时的量化损失。 | V4 对 MoE expert weights 和 CSA indexer QK path 使用 FP4 QAT。 | 让训练、采样、线上部署行为更一致。 | 训练-部署一致性优化 |
| FP4-to-FP8 Lossless Dequantization | QAT 实现 | FP4 权重反量化到 FP8 计算，在特定 scale 条件下不损失 FP4 信息。 | V4 复用已有 FP8 框架，不改 backward pipeline。 | 用较低工程成本接入 FP4 QAT。 | 数值系统工程 |
| Straight-Through Estimator, STE | 量化训练 | 量化不可微时，用近似梯度让训练继续传播。 | V4 QAT 中把梯度直接传回 FP32 master weights。 | 让低精度量化参与训练优化。 | 经典训练技巧应用 |
| Loss Spike | 训练监控 | 训练损失突然飙升，常意味着数值、路由或数据异常。 | V4 明确承认遇到 notable instability，并给出缓解方法。 | 披露真实训练难点，有助判断工程可信度。 | 训练风险信号 |

### C. 推理与底层 Infra：决定模型“跑得快不快、稳不稳、能不能复现”

| 术语 | 发生环节 | 通俗解释 | DeepSeek V4 做了什么 | 主要好处 | 创新层级 |
| --- | --- | --- | --- | --- | --- |
| Inference | 推理部署 | 模型上线后接收输入并生成输出。 | V4 为 CSA/HCA、FP4、KV cache、agent 工具调用重建推理框架。 | 让复杂架构真正可服务。 | 部署系统 |
| Rollout | RL / OPD / Agent 训练 | 让当前模型生成完整轨迹，用于打分、蒸馏或训练。 | V4 将 rollout 服务做成可抢占、可恢复、支持长上下文。 | 大幅提升 RL/OPD 采样效率和可靠性。 | 后训练基础设施 |
| Expert Parallelism, EP | MoE 训练/推理并行 | 把不同专家分散到不同设备上，需要频繁通信。 | V4 提出细粒度 EP 通信-计算重叠，并在 NVIDIA GPU 与华为昇腾 NPU 上验证。 | 降低 MoE 的通信瓶颈。 | 分布式训练/推理优化 |
| Communication-Computation Overlap | 分布式训练/推理 | 把通信等待藏到计算过程中，不让 GPU 空等。 | V4 将 MoE 的 Dispatch/Combine 与 Linear 计算做成细粒度 pipeline。 | 报告称一般推理场景 1.50-1.73x，加速敏感场景最高 1.96x。 | 系统级效率创新 |
| Kernel | 底层算子 | 直接在 GPU/NPU 上执行的基础计算代码。 | V4 为 mHC、CSA/HCA、OPD KL 等定制大量 kernel。 | 把算法想法变成可高效运行的工程实现。 | 底层计算实现 |
| TileLang | Kernel DSL / 编译器工具 | 介于 CUDA 和 Triton 之间的 kernel 编写语言，降低写高性能算子的难度。 | V4 报告大量使用 TileLang，并强调快速开发和 bitwise reproducibility。 | 降低新算法落地到硬件的边际成本。 | Infra 工具创新 / 生态创新 |
| CUDA / Triton | Kernel 开发生态 | CUDA 最底层、性能强但开发成本高；Triton 更易用但表达能力和性能可能受限。 | 访谈用它们与 TileLang 对比，说明 TileLang 的中间层价值。 | 帮非技术同事理解为什么 kernel DSL 是战略基础设施。 | 生态参照 |
| DeepGEMM | 矩阵乘法库 | 大模型训练和推理里最核心的底层计算之一。 | V4 用 DeepGEMM 替代传统 cuBLAS 以支持 batch invariance。 | 保证复现性，同时保持性能。 | 底层库工程 |
| Batch Invariance | 推理/训练可复现性 | 同一个 token 的输出不应因它在 batch 里的位置不同而变化。 | V4 端到端实现 bitwise batch-invariant kernels。 | 便于 debug、稳定性分析和一致评测。 | 可复现 infra |
| Deterministic Kernels | 训练/推理可复现性 | 同一输入和同一状态下，每次计算得到 bitwise 一致结果。 | V4 处理 sparse attention backward、MoE backward、mHC split-k 等非确定性来源。 | 训练异常可定位，评测结果更可信。 | 可复现 infra |
| Bitwise Reproducibility | 训练/推理一致性 | 不只是近似一致，而是二进制位级别一致。 | V4 把它作为 kernel library 的目标之一。 | 支撑大规模训练 debug 和后训练一致性。 | 工程质量标准 |
| TTFT, Time To First Token | 产品体验 / 推理 | 用户发出请求后，第一个 token 出来的等待时间。 | Quick Instruction 复用 KV cache，避免额外小模型重复 prefill。 | 降低用户体感延迟。 | 产品化推理优化 |
| Prefill / Decode | 推理过程 | Prefill 是先处理完整输入并建 KV cache；decode 是逐 token 生成。 | V4 为混合 KV cache 和长上下文重新设计管理方式。 | 提升长 prompt、长工具轨迹下的推理效率。 | 推理系统基础 |
| Speculative Decoding | 推理加速 | 小模型或草稿模块先猜一批 token，主模型批量验证。 | 访谈提到 V4 新架构使前缀缓存和投机解码链路需要重建。 | 降低逐 token 生成瓶颈。 | 推理加速技术 |
| 3FS | 分布式文件系统 | DeepSeek 自研/开源的 Fire-Flyer File System，用于大规模训练和沙箱镜像存储。 | DSec 建在 3FS 之上，支持镜像和状态的分布式管理。 | 支撑大规模 sandbox 和 rollout。 | 基础设施底座 |

### D. 后训练与能力合并：决定模型“学会怎么做任务”

| 术语 | 发生环节 | 通俗解释 | DeepSeek V4 做了什么 | 主要好处 | 创新层级 |
| --- | --- | --- | --- | --- | --- |
| Post-training | 预训练之后 | 把基础模型调成能对话、能推理、能遵循指令、能用工具的模型。 | V4 采用 specialist training + OPD，而不是简单 mixed RL。 | 让不同能力更稳定地整合进统一模型。 | 模型工艺阶段 |
| SFT, Supervised Fine-Tuning | 后训练第一步 | 用高质量示范答案教模型“应该怎么答”。 | V4 和 visual primitives paper 都使用专门 SFT 冷启动能力。 | 建立格式、任务风格和基本能力。 | 标准后训练环节 |
| RL, Reinforcement Learning | 后训练 / 推理能力增强 | 让模型自己生成答案，再用 reward 判断好坏并优化。 | V4 对专家模型使用 GRPO；visual primitives paper 对 box/point 专家分别做 RL。 | 提升推理、工具、代码、视觉任务表现。 | 后训练核心 |
| GRPO, Group Relative Policy Optimization | 强化学习算法 | DeepSeek R1 系列使用的 RL 算法，比较同组候选轨迹的相对好坏。 | V4 继续在专家训练中使用 GRPO。 | 不完全依赖传统 value model，适合推理任务优化。 | DeepSeek 后训练路线延续 |
| Reward Model, RM | 强化学习打分器 | 给模型生成结果打分，告诉模型什么更好。 | visual primitives paper 设计 format、quality、accuracy 三类 RM。 | 让 RL 有可学习信号。 | 后训练评估组件 |
| GRM, Generative Reward Model | Reward 模型 | 不只输出一个分数，还能生成评价理由的奖励模型。 | V4 对 hard-to-verify tasks 使用 rubric-guided RL data 和 GRM；visual paper 用 LLM-based GRM 判断质量。 | 用更少人工标注处理开放式任务。 | 后训练评估创新 |
| Specialist Training | 后训练策略 | 先训练多个领域专家，而不是让一个模型一次学所有目标。 | V4 训练十多个 teacher models 覆盖不同领域；visual paper 训练 box/point 两类专家。 | 减少多目标冲突，提升合并前的单项能力。 | 后训练流程创新 |
| OPD, On-Policy Distillation | 能力合并 / 后训练 | 学生模型基于自己生成的轨迹，向多个教师模型学习输出分布。 | V4 用 OPD 替代 mixed RL 合并专家；visual paper 也用 OPD 合并 ETwG/ETwP。 | 比权重合并或混合 RL 更稳定地整合多专家能力。 | 核心后训练工艺创新 |
| Teacher / Student Models | 蒸馏流程 | teacher 是专家模型，student 是最终要合并能力的模型。 | V4 使用超过十个 teacher models 蒸馏单一 student。 | 把多个专家能力压入一个可发布模型。 | 训练组织方式 |
| Full-vocabulary Logit Distillation | OPD 实现 | 不只看最终采样 token，而是看整个词表概率分布来学习 teacher。 | V4 为 OPD 计算完整 logits 的 reverse KL，并用工程手段降低内存负担。 | 蒸馏更稳定、更忠实，但工程成本更高。 | 后训练 + infra 结合创新 |
| Reverse KL | 蒸馏目标 | 一种衡量 student 与 teacher 输出分布差异的数学目标。 | V4 的 OPD objective 使用 reverse KL。 | 让 student 更贴合专家输出分布。 | 数学目标 |
| RFT, Rejection Fine-Tuning | 数据再筛选 / SFT | 从模型生成结果中挑更好的样本再做微调。 | visual primitives paper 用专家 rollout 生成 RFT 数据，并按难度筛样。 | 扩大高质量专门训练数据。 | 数据合成/后训练流程 |
| Reasoning Effort | 产品模式 / 后训练 | 控制模型花多少 token 思考。 | V4 提供 Non-think、Think High、Think Max 三档，并用不同 RL 配置训练。 | 让模型在速度、成本和准确性之间切换。 | 产品化后训练设计 |
| Length Penalty | RL / reasoning 控制 | 对过长回答施加惩罚，避免模型无限延长思考。 | V4 不同 reasoning mode 使用不同 length penalty 和 context window。 | 控制推理 token 成本和回答节奏。 | 成本治理手段 |

### E. Agent Runtime：决定模型“能不能稳定完成长程任务”

| 术语 | 发生环节 | 通俗解释 | DeepSeek V4 做了什么 | 主要好处 | 创新层级 |
| --- | --- | --- | --- | --- | --- |
| Agentic AI | 应用 / 后训练 / 评测 | 模型不只回答问题，还能调用工具、读写文件、搜索、执行多步任务。 | V4 在数据、评测、工具 schema、DSec sandbox 中都围绕 agentic tasks 优化。 | 从“会答题”转向“能做事”。 | 能力方向 |
| Tool-call Schema | Agent 工具接口 | 规定模型怎样调用工具、传参数、接收结果。 | V4 引入 XML 风格 DSML tool-call schema。 | 降低工具调用格式错误和 escaping failures。 | Agent 接口标准化 |
| DSML | 工具调用格式 | DeepSeek 的 XML-like 工具调用格式。 | V4 用 DSML tool-calls block 等特殊结构管理工具调用。 | 让工具调用更结构化、更可解析。 | 产品/Agent 接口设计 |
| Interleaved Thinking | Agent 上下文管理 | 工具调用多轮之间保留 reasoning state，不让模型每轮从头想。 | V4 在 tool-calling 场景跨用户消息边界保留完整 reasoning history。 | 长程任务状态更连贯，减少重复思考。 | Agent 长程状态管理 |
| Quick Instruction | 推理前辅助任务 | 用特殊 token 让主模型顺手完成搜索判断、query 生成、领域判断等任务。 | V4 用 Quick Instruction 复用已有 KV cache，替代部分小模型。 | 降低 TTFT 和系统复杂度。 | 产品化推理优化 |
| DSec, DeepSeek Elastic Compute | Agent sandbox / 后训练 / 评测 | DeepSeek 的生产级沙箱平台，用于运行工具、代码、环境和 agent 轨迹。 | DSec 支持数十万并发 sandbox instances，含 Apiserver、Edge、Watcher 三个 Rust 组件。 | 支撑大规模 agent 训练、评测和恢复。 | Agent infra 核心创新 |
| Sandbox | Agent 执行环境 | 把模型执行代码和工具调用放在隔离环境里。 | DSec 提供 Function Call、Container、microVM、fullVM 四种 substrate。 | 按任务风险和环境需求选择隔离级别。 | 安全/执行基础设施 |
| Container | Sandbox 类型 | 类似 Docker 的轻量执行环境。 | DSec container Docker-compatible，并用 EROFS on-demand loading。 | 快速启动，适合常规执行任务。 | 执行基底 |
| microVM / fullVM | Sandbox 类型 | microVM 提供更强隔离，fullVM 支持完整操作系统。 | DSec 分别基于 Firecracker 和 QEMU。 | 满足安全敏感和复杂 OS 任务。 | 执行隔离层 |
| Trajectory Log | Agent 轨迹日志 | 记录每次命令调用和结果，像 agent 的执行账本。 | DSec 为每个 sandbox 维护全局有序 trajectory log。 | 可恢复、可追溯、可复现。 | Agent 可观测性核心 |
| Preemption-safe Resumption | 训练/Agent 容错 | 任务被抢占或中断后，从已有状态恢复，不重跑危险操作。 | V4 rollout service 用 token-granular WAL；DSec 用 trajectory log 恢复 sandbox。 | 提高 GPU 利用率，同时避免长程任务重跑出错。 | 容错 infra |
| Deterministic Replay | 调试 / 评测 | 历史 session 可以按轨迹复现。 | DSec 支持从 trajectory 重放历史会话。 | 支撑 debug、审计、评测复现。 | Agent 治理能力 |
| WAL, Write-Ahead Log | Rollout 容错 | 每生成一个 token 先写日志，中断后可继续。 | V4 rollout service 使用 token-granular WAL。 | 避免从头重生成造成长度偏差和额外成本。 | 训练/采样容错创新 |
| Resumability | Agent infra 目标 | 系统不追求永不失败，而是失败后能正确恢复。 | V4 的 DSec 和 rollout service 都围绕恢复设计。 | 更适合长程、高权限、有副作用的 agent。 | Agent infra 范式 |

### F. 多模态与视觉原语：决定模型“能不能在图像里准确指代”

| 术语 | 发生环节 | 通俗解释 | DeepSeek visual primitives paper 做了什么 | 主要好处 | 创新层级 |
| --- | --- | --- | --- | --- | --- |
| MLLM, Multimodal Large Language Model | 多模态模型 | 能同时处理文字和图像的大模型。 | paper 基于 DeepSeek-V4-Flash 加 DeepSeek-ViT 做视觉推理。 | 把 V4 的长上下文和压缩能力延伸到视觉。 | 多模态模型路线 |
| Perception Gap | 多模态能力诊断 | 模型看不清图像细节。 | paper 认为高分辨率 crop 主要解决这个问题。 | 帮助区分“看不清”和“不会推理”。 | 问题定义 |
| Reference Gap | 多模态推理诊断 | 模型看到了，但语言无法精确指向视觉空间中的对象、位置、路径。 | paper 把它定义为复杂空间推理中的核心瓶颈。 | 解释为什么语言 CoT 在计数、路径、迷宫任务中容易崩。 | 关键问题定义 |
| Visual Primitives | 多模态推理接口 | 把 box 和 point 当作视觉推理的最小单位。 | paper 让模型在 thinking content 中输出 boxes/points。 | 模型可以“一边想，一边指”。 | 多模态推理范式探索 |
| Bounding Box | 视觉原语 | 用矩形框标出对象位置和尺度。 | 用于 counting、fine-grained counting、spatial reasoning。 | 降低对象遗漏、重复计数和指代漂移。 | 视觉指代工具 |
| Point | 视觉原语 | 用坐标点标出位置或轨迹。 | 用于 maze navigation、path tracing、拓扑推理。 | 表达路径、连通性、轨迹等语言难以描述的信息。 | 视觉操作工具 |
| DeepSeek-ViT | 视觉编码器 | 把图像切成 patch 并转成视觉 token 的模块。 | paper 使用自研 ViT，从头训练，支持任意分辨率。 | 为 V4-Flash 提供视觉输入。 | 多模态架构组件 |
| Patch Token | 视觉编码 | 图像切块后得到的视觉 token。 | 756 x 756 图像先变成 2,916 个 patch tokens。 | 把图像转成模型可处理的 token 序列。 | 基础视觉表示 |
| 3x3 Spatial Token Compression | 视觉 token 压缩 | 把 9 个相邻 patch token 压成 1 个。 | paper 将 2,916 个 patch token 压成 324 个视觉 token。 | 大幅降低视觉输入成本。 | 多模态压缩工程 |
| Visual KV Entries | 多模态推理缓存 | 视觉 token 进入 LLM 后在 KV cache 中的缓存条目。 | 经 CSA 后，756 x 756 图像最终约 81 个 visual KV entries。 | 用少量缓存承载图像信息。 | 视觉压缩 + 长上下文结合 |
| Thinking with Grounding | box 路线 | 推理时用 bounding boxes 锚定对象。 | paper 训练 FTwG/ETwG 专家。 | 适合对象定位、计数、空间关系。 | 视觉推理模式 |
| Thinking with Pointing | point 路线 | 推理时用点序列表达位置和路径。 | paper 训练 FTwP/ETwP 专家。 | 适合迷宫、路径追踪、拓扑任务。 | 视觉推理模式 |
| Cold-start Data | 后训练启动数据 | 少量高精度样本，先教模型按照新接口做事。 | paper 构造 counting、spatial VQA、maze、path tracing 冷启动数据。 | 让模型先学会 visual primitive 输出格式和推理套路。 | 数据工程 |
| Trigger Words | 产品/模型路由 | 需要特定提示词才能激活某种能力。 | paper 承认当前 visual primitives 能力依赖显式 trigger。 | 说明能力还未完全自主路由。 | 当前限制 |

### G. 评测、产品和商业分析口径：决定“模型是不是真的有用”

| 术语 | 发生环节 | 通俗解释 | DeepSeek V4 相关信息 | 主要好处 / 风险 | 创新层级 |
| --- | --- | --- | --- | --- | --- |
| Benchmark | 模型评测 | 标准化任务集合，用于横向比较模型。 | V4 覆盖 MMLU-Pro、GPQA、HLE、LiveCodeBench、Terminal Bench、SWE、MRCR、CorpusQA 等。 | 可比较，但容易被刷榜，也不等于真实任务体验。 | 评测工具 |
| Eval | 评估体系 | 比 benchmark 更宽，包含真实任务、人评、内部任务、用户反馈。 | 访谈强调“We cannot optimize what we cannot evaluate”。 | 从分数转向任务治理。 | 方法论层 |
| In-house Harness | 内部评测框架 | 公司自建的任务环境和工具链。 | V4 的 code agent、search agent、white-collar tasks 使用内部 harness。 | 接近产品场景，但复现性和横向公平性要留边界。 | 评测基础设施 |
| Agentic Benchmark | Agent 评测 | 测模型是否能多步调用工具完成任务。 | V4 测 Terminal Bench、SWE、BrowseComp、MCPAtlas、Toolathlon 等。 | 更接近“能不能做事”，但受工具和 harness 影响大。 | 评测方向升级 |
| MRCR / CorpusQA | 长上下文评测 | MRCR 偏多针检索，CorpusQA 更接近真实长文档问答。 | V4-Pro-Max MRCR 1M 为 83.5，CorpusQA 1M 为 62.0。 | 能看长上下文可用性，但不代表完美记忆。 | 长上下文评测 |
| Human Eval | 人工评测 | 人类按 rubric 对模型输出做判断。 | V4 中文写作、白领任务、内部代码采用意愿都有人工或用户反馈成分。 | 接近真实体验，但受样本和标注偏好影响。 | 产品评估 |
| Non-loss Rate | 人评结果口径 | 胜率 + 平率，表示模型至少不输的比例。 | V4 白领任务对 Opus-4.6-Max non-loss rate 为 63%。 | 比单纯胜率更适合开放式任务，但仍需看样本。 | 人评指标 |
| Unit Task Completion Cost | 商业分析口径 | 一个任务真正完成所需的总成本，不只是 token 单价。 | 本文建议用它替代“每百万 token 价格”。 | 同时考虑成功率、token、工具调用、人工返工、延迟。 | 战略分析框架 |
| Token Inflation | 成本风险 | 模型思考越来越长，同一任务消耗更多 token。 | 访谈提到 V4 可能存在 token 消耗变长，抵消效率提升。 | 单 token 更便宜不代表任务更便宜。 | 成本治理问题 |
| Data Flywheel | 产品/训练闭环 | 用户真实使用产生数据，数据反过来改进模型。 | 访谈讨论 coding/agent 数据来自真实使用，默认工作流入口很关键。 | 决定模型能否持续改进真实任务。 | 竞争壁垒 |
| Default Workflow | 产品竞争 | 用户是否把某模型作为默认工作工具。 | DeepSeek 内部 85 名开发者/研究员中，52% 认为 V4-Pro 可作为默认主力 coding 模型，39% 倾向可以。 | 比榜单更接近真实采用意愿。 | 产品采用指标 |

## 1. 给组会的五个主判断

### 判断一：V4 的核心不是“百万上下文”，而是让百万上下文进入可用成本区间

已确认事实：

- DeepSeek-V4-Pro：1.6T 总参数，49B 激活参数。
- DeepSeek-V4-Flash：284B 总参数，13B 激活参数。
- 两者都支持 1M token 上下文。
- 在 1M 上下文下，V4-Pro 的单 token 推理 FLOPs 是 V3.2 的 27%，KV cache 是 V3.2 的 10%；V4-Flash 分别约为 10% 和 7%。
- V4 使用 CSA 和 HCA 混合注意力：CSA 做 4:1 压缩后 top-k 选择，HCA 做 128:1 重压缩并保留全局概览。

解读：

百万上下文不是把 100 万 token 全量细读，而是把上下文变成分层记忆：近处保细节，中距离做选择，远距离留轮廓。V4 的真实贡献是让长上下文、长程 agent、长推理 rollout 的成本下降到可以持续实验和部署的区间。

组会可讲：

“V4 不是把窗口开大这么简单。它是在回答一个更工程的问题：当 agent 需要持续读、写、调用工具、保留状态时，模型怎样才能不被 KV cache 和推理 FLOPs 拖死。”

### 判断二：V4 是工程胜利，不是 R1 式范式变化

访谈嘉宾赵晨阳的判断很直接：R1 是开源世界里走通 Long Reasoning 的范式样本，V4 更像是在这个范式下解决计算瓶颈。刘益枫也认为 V4 的震撼程度不如 R1，也不如 Kimi 早期长文本能力带来的新能力感。

这个判断很重要，因为它能避免把所有发布都讲成“范式革命”。V4 的价值是工程积累：

- 放弃既有 MLA 路线，改用 CSA/HCA 混合压缩。
- 在大规模 MoE 上使用 Muon，并采用更细的超参数选择。
- 把 FP4 从部署压缩推进到训练、rollout、部署一致性。
- 为 mHC、混合注意力、Muon、FP4、DSec、OPD 重新适配训练和推理系统。

推断判断：

未来一两年，前沿模型竞争很可能会更多发生在“把许多难以单独商业化的工程优化集成进一个可训练、可部署、可评估的系统”上。这个方向不如新范式好讲，但对成本、吞吐、迭代速度和模型可用性更直接。

### 判断三：DeepSeek 正在从“成本叙事”切换到“能力加工程叙事”

V3/R1 时代，外界记住的是训练成本和极低 API 价格。V4 报告没有再公布训练成本，访谈中两位嘉宾给出的解释是：最后一次训练成本只是总成本的一部分，前沿探索、对比实验、人力、数据才是大头；DeepSeek 也不再主要用成本定义自己。

这会带来一个新的观察框架：

| 旧框架 | 新框架 |
| --- | --- |
| 每百万 token 价格 | 单位任务完成成本 |
| 模型 benchmark 排名 | 用户真实任务是否愿意迁移 |
| 训练成本是否低 | 训练、推理、RL rollout、agent serving 是否形成闭环 |
| 开源等于便宜 | 开源权重加高价 API 可以并存，本地部署价值仍然存在 |

需要特别注意 token 膨胀。访谈里提到，有用户反馈 V4 解决同一问题时 token 消耗比之前更多，这会抵消部分效率优化。也就是说，模型单 token 更便宜不等于任务更便宜；如果思考 token 大幅变长，用户体感成本仍可能上升。

组会可讲：

“V4 把成本问题从价格表转移到了任务经济学：一个复杂任务是否更快完成、少失败、少返工、少人工检查，才是最终成本。”

### 判断四：Agent 已经变成模型基础设施问题，而不是应用层 wrapper

Tech report 里最容易被非技术读者低估的部分，是工具调用、interleaved thinking、Quick Instruction、DSec sandbox、rollout 容错。

已确认事实：

- V4 引入 XML 风格的 DSML tool-call schema，用特殊 token 管理工具调用。
- 在 tool-calling 场景下，V4 保留跨轮 reasoning traces，用于长程 agent 任务状态管理。
- Quick Instruction 用特殊 token 触发搜索判断、标题生成、query 生成、权威性判断、领域判断等辅助任务，复用 KV cache，减少额外小模型和重复 prefill。
- DSec 是生产级沙箱平台，包含 Function Call、Container、microVM、fullVM 四种执行基底。
- DSec 单集群管理数十万并发 sandbox instances，并维护 trajectory log，支持 preemption-safe resumption 和 deterministic replay。

战略含义：

DeepSeek 不是把 agent 看成“模型外面加几个工具”，而是把 agent 看成训练、评测、部署共同面对的系统问题。这个方向与内库中 Agent Infra 的判断一致：长程、高权限、有副作用的 agent，需要 effect log、状态恢复、权限隔离和可复现轨迹。

组会可讲：

“Agent 的瓶颈已经从‘模型会不会调用工具’推进到‘执行过程能不能恢复、能不能追责、能不能复现、能不能安全隔离’。”

### 判断五：Visual primitives paper 是 V4 路线的多模态延伸

这篇随后发布又删除的 paper 不应只当作一个多模态小论文看。它把 DeepSeek V4 的两个核心思想迁移到了视觉推理：

- 压缩：用 DeepSeek-ViT、3x3 spatial token compression 和 V4-Flash 的 CSA，大幅压缩视觉 token 和 KV cache。
- 定位：把 bounding boxes 和 points 作为“思考最小单位”，让模型在推理过程中直接指向图像坐标。

paper 的核心问题叫 Reference Gap。它不是 Perception Gap。Perception Gap 是模型看不清细节；Reference Gap 是模型即使看到了，也很难用自然语言精确指代复杂空间布局。对于计数、路径追踪、迷宫、空间关系、多步视觉推理，语言 CoT 容易在“这个、那个、左边那个”里丢失目标。

组会可讲：

“这篇 paper 的价值不是让模型多画几个框，而是把视觉空间里的坐标变成推理过程的一部分。它在尝试让模型一边想，一边指。”

## 2. 技术路线：用非技术语言讲清 V4 的工程含义

### 2.1 MoE 激活比：容量和成本继续解耦

V4-Pro 的总参数是 1.6T，但每个 token 激活 49B，激活比约 3%。访谈补充了一组横向对比：V3 约 5.5%，Kimi K2.6 约 3.2%，MiMo-2.5-pro 约 4.1%，MiniMax M2.7 约 4.35%，GLM 5.1 约 5.3%。

这件事的商业含义是：模型可以拥有更大的总容量，但每次推理只调用少量专家，试图同时获得“知识容量”和“推理成本”两个收益。

边界：

激活比不是越低越好。过低会带来路由负载不均、专家训练不充分、训练不稳定。V4 报告承认训练中遇到 loss spikes，并用 Anticipatory Routing 和 SwiGLU Clamping 缓解，且坦诚其机理仍未完全理解。

### 2.2 CSA/HCA：长上下文的“压缩索引”路线

对非技术同事可以这样解释：

- 滑动窗口注意力：保留附近细节，像短期工作记忆。
- CSA：先把每 4 个 token 压缩，再从压缩结果中挑重点，像中距离检索。
- HCA：把每 128 个 token 压成一个高密度摘要，像远距离全局地图。

它解决的是长上下文的两个硬问题：

- 计算量：每次生成 token 需要看历史，历史越长越贵。
- 存储量：KV cache 是长对话和长文档推理的隐形成本。

这也是为什么 V4 的 1M context 对 agent 有直接意义。长程 agent 会反复积累工具结果、代码片段、文件状态、失败记录、用户约束。如果不能压缩和复用上下文，agent 的成本会指数式恶化。

### 2.3 Muon、mHC、FP4：训练工艺开始变成战略资产

V4 的工程栈里有三类信号值得看。

| 模块 | 简化解释 | 战略含义 |
| --- | --- | --- |
| Muon optimizer | 从“逐参数更新”转向更偏“矩阵整体更新” | 优化器重新成为前沿模型差异化变量，考验训练系统 |
| mHC | 改造层间信息流，让深层模型训练和推理更稳定 | 深模型能力不是只堆层数，还要管理信号传递 |
| FP4 QAT | 训练时让模型适应 4 位权重，rollout 和部署使用真实 FP4 | 训练、采样、部署一致性成为效率核心 |

FP4 部分尤其值得讲。Tech report 写到，DeepSeek 对 MoE expert weights 和 CSA indexer 的 QK path 使用 FP4；index scores 从 FP32 到 BF16 的优化让 top-k selector 获得 2x speedup，同时保留 99.7% 的 KV entry recall。访谈中赵晨阳进一步解释，RL 采样可能占很大时间，采样阶段真实使用 FP4 权重可以直接降低访存瓶颈。

组会可讲：

“FP4 不是简单把模型压小，而是把训练、RL 采样、线上部署放到同一套数值假设里。这能减少‘训练时很好，部署后变味’的问题。”

### 2.4 TileLang 和 deterministic kernels：可复现性是评测地基

V4 报告强调 batch-invariant、deterministic、bitwise reproducibility。这些词看起来底层，但对评测和产品很关键。

如果同一条输入因为 batch 位置不同、硬件调度不同、kernel 累加顺序不同而得到不同中间结果，训练异常就难定位，后训练行为也难复现，agent 评测会更不稳定。

所以这部分可以理解为 DeepSeek 在修“模型生产线的计量系统”。没有可复现的训练和推理，后续所有 reward、eval、agent benchmark 都会变脆。

## 3. 后训练：从单模型 RL 到“专家分科加 OPD 合并”

### 3.1 训练流程的核心变化

Tech report 明确说，V4 的 post-training 大体继承 V3.2，但有一个关键替换：mixed RL 被 On-Policy Distillation 取代。

简化流程：

1. 先训练多个 domain specialists。
2. 每个专家用 SFT 和 GRPO 做领域强化。
3. 对 hard-to-verify 任务，用 Generative Reward Model 评估 trajectory。
4. 用 OPD 把十多个 teacher models 的能力合并到一个学生模型。
5. 使用 full-vocabulary logit distillation，避免传统 mixed RL 或权重合并中的能力损失。

非技术解释：

它不是让一个模型同时学数学、代码、搜索、写作、agent、工具调用，然后期待所有目标都一起涨。更像是先让不同专家在各自任务上收敛，再把专家的输出分布蒸馏进一个统一模型。访谈里赵晨阳把这解释成：从多目标 loss surface 上直接找 Pareto 最优，改成在多个已收敛离散点之间做插值，工程上更稳定。

### 3.2 三档 reasoning effort 是产品化信号

V4 同时提供 Non-think、Think High、Think Max 三档：

- Non-think：日常、低风险、快速任务。
- Think High：复杂问题、规划、较高准确性。
- Think Max：能力边界探索，使用特殊系统提示和更长推理。

这说明 reasoning effort 已经不是纯研究变量，而是产品变量。模型供应商会越来越需要解决“什么时候该多想，什么时候该少想”的路由问题。访谈里赵晨阳提到“减少推理量”可能是下一阶段重要能力，因为现在很多模型被长上下文和 infra 优化惯坏了，解决简单任务也会过度推理。

组会可讲：

“未来模型不只比谁会想，还要比谁知道什么时候不该想太多。”

## 4. 数据：文本主模型仍然不透明，多模态 paper 给出了一部分可见方法

### 4.1 V4 tech report 里的文本数据：方向清楚，配方不透明

已确认事实：

- Flash 预训练 32T tokens，Pro 预训练 33T tokens。
- 训练数据包含 math、code、web pages、long documents 等。
- web 数据过滤批量自动生成和模板化内容，以降低 model collapse 风险。
- mid-training 加入 agentic data。
- 多语言语料规模扩大，用于长尾知识。
- 长文档特别强调 scientific papers、technical reports 等材料。
- 上下文长度从 4K 逐步延展到 16K、64K、1M。

边界：

报告没有披露 web/code/math/long-doc/multilingual 的配比，也没有披露 synthetic data 占比、版权过滤口径、污染检测结果和安全数据细节。所以关于数据只能做方向判断：V4 的数据资源明显向长文档、代码、数学、agentic 场景倾斜，但不能直接判断数据质量全貌。

### 4.2 Visual primitives paper 的数据：更透明，也更值得讨论

这篇 paper 对视觉原语数据构建披露较多。

已确认事实：

- 从多网站抓取 box grounding 相关数据，以 HuggingFace Object Detection / Grounding 数据为例，使用 API 和 popularity 指标做初筛，并排除 validation/test split 以降低污染风险。
- 初始获得 97,984 个 box-grounding 数据源。
- 语义质量过滤后保留 43,141 个数据源。
- 视觉几何质量过滤后保留 31,701 个数据源。
- 通过类别均衡采样和去重，最终得到 4,000 万以上高质量样本。
- 预训练阶段统一 box 和 point 格式，box 坐标归一到 0-999。
- cold-start 数据包括 counting 约 10,000 条、spatial reasoning/general VQA 约 9,000 条、maze navigation 约 460,000 条、path tracing 约 125,000 条。

解读：

这份 paper 把 DeepSeek 的数据方法展现得更像“工程化数据工厂”。它不只收集数据，还明确处理语义噪声、几何噪声、box 漏标、超大无意义框、私有实体、缩写歧义、低质量标签等问题。

风险：

视觉原语 paper 的数据更透明，但任务仍然是围绕视觉指代设计的 focused suite。它不能证明模型整体多模态能力全面领先，也不能证明视觉原语能自然泛化到所有真实图片、UI、图表、医学、遥感或具身场景。

## 5. 评测：哪些能信，哪些要留边界

### 5.1 更可信的部分：同系对比和系统指标

同一团队、同一框架、同一口径下的 V3.2、V4-Flash、V4-Pro 对比，可信度相对更高。

示例：

- LongBench-V2：V3.2 Base 40.2，V4-Flash Base 44.7，V4-Pro Base 51.5。
- MMLU-Pro：V3.2 Base 65.5，V4-Flash Base 68.3，V4-Pro Base 73.5。
- Simple-QA verified：V3.2 Base 28.3，V4-Flash Base 30.1，V4-Pro Base 55.2。

系统指标也相对可信：

- 1M context 下 FLOPs/KV cache 的相对下降。
- EP overlap 在推理和 RL rollout 中的加速。
- FP4 top-k selector 的 2x speedup 和 99.7% recall。
- DSec 的执行 substrate、trajectory log 和恢复机制设计。

这些结论不依赖外部模型 API 状态，更能说明 DeepSeek 自身路线有效。

### 5.2 中等可信：跨模型标准 benchmark

V4-Pro-Max 在多项公开 benchmark 上进入一线区间，但不能讲成全面超过闭源。

关键结果：

| 任务 | V4-Pro-Max 结果 | 稳妥解读 |
| --- | --- | --- |
| LiveCodeBench | 93.5 | 很强，已进入闭源第一梯队附近 |
| Codeforces | 3206 | 竞赛代码能力突出，报告称可比 GPT-5.4 |
| Terminal Bench 2.0 | 67.9 | 强于部分开源，对最强闭源仍有差距 |
| SWE Verified | 80.6 | 接近头部，和多家开源模型相近 |
| Toolathlon | 51.8 | 工具使用能力不错，但 GPT-5.4 为 54.6 |
| MRCR 1M | 83.5 | 长上下文检索强于 Gemini 3.1 Pro，弱于 Opus 4.6 |
| CorpusQA 1M | 62.0 | 更接近真实长文档场景，仍非完美长记忆 |

边界：

- GPT-5.4 的 1M 长上下文评测未完成，因为 API 大量无响应。
- K2.6 和 GLM-5.1 部分条目空缺，因为 API 过忙。
- agent benchmark 往往受 harness、工具、上下文管理策略影响。

### 5.3 低到中等可信：内部白领任务和写作人评

这些评测接近真实产品体验，但样本选择、rubric、标注者偏好会影响结果。

已确认结果：

- 中文功能写作：DeepSeek-V4-Pro 对 Gemini-3.1-Pro 总胜率 62.7% vs 34.1%。
- 创意写作：对 Gemini-3.1-Pro，instruction following 胜率 60.0%，writing quality 胜率 77.5%。
- 复杂中文指令和多轮写作：Claude Opus 4.5 仍以 52.0% vs 45.9% 领先。
- 白领任务：V4-Pro-Max 对 Opus-4.6-Max non-loss rate 63%，优势主要在 task completion 和 content quality；短板在 specific formatting constraints、长文压缩摘要、PPT 美观度。

组会可讲：

“这些内部人评最适合判断 DeepSeek 的产品优化方向，不适合当作横向排名的绝对证据。”

### 5.4 评测方法本身变成竞争点

访谈中有一个很重要的判断：现在行业已进入 benchmark 可信危机。很多模型在静态榜单上都很高，但用户在真实 agent、coding、写作、搜索任务中的体感差异仍然明显。

因此，V4 的评测部分最值得学习的不是某个分数，而是评测形态：

- 标准题：MMLU-Pro、GPQA、HLE、LiveCodeBench。
- 长上下文：MRCR、CorpusQA。
- 真实任务：中文写作、搜索、白领任务、内部 R&D coding。
- Agent 任务：Terminal Bench、SWE、BrowseComp、MCPAtlas、Toolathlon。
- 内部采用意愿：85 名 DeepSeek 开发者/研究员问卷，52% 认为可以作为默认主力 coding 模型，39% 倾向可以，少于 9% 否定。

真正要看的指标应从“答题正确率”升级为：

- 任务完成率。
- 成本和时延。
- 人工返工率。
- 失败恢复能力。
- 工具调用错误率。
- 长程状态保持能力。
- 用户是否愿意把默认工作流迁移过去。

## 6. Visual primitives paper：为什么值得单独拿出来讲

### 6.1 它提出的不是“看得更清”，而是“指得更准”

paper 先区分两个问题：

- Perception Gap：模型看不清细节，所以需要高分辨率 crop、dynamic patching。
- Reference Gap：模型即使看到细节，也无法用语言精确引用复杂视觉对象和空间关系。

这对多模态路线判断很关键。过去很多 MLLM 优化集中在“增加像素、增加视觉 token、增加 crop”。DeepSeek 这篇 paper 说，复杂视觉推理的另一个瓶颈是指代系统。如果模型不能稳定指向“我正在数的这几个对象”或“路径经过的这些点”，语言 CoT 会出现级联幻觉。

### 6.2 视觉原语：box 和 point 变成思考过程的一部分

paper 使用两类 visual primitives：

- Bounding boxes：适合定位对象的位置和尺度，尤其适合计数、对象辨别、细粒度视觉问答。
- Points：适合抽象视觉引用、轨迹、路径、迷宫、拓扑推理。

这不是在最终答案里补一个框，而是在 thinking content 中持续输出框和点。例如计数任务中，模型先用 box 一次性圈出所有候选对象，再做属性筛选和统计；路径追踪任务中，模型输出一串 point 坐标来表达自己沿曲线走过的路径。

非技术解释：

“过去模型像是闭着眼用语言描述图像，现在它开始用手指着图像说：我说的是这里、这里和这里。”

### 6.3 它延续了 V4 的效率路线

paper 基于 DeepSeek-V4-Flash：

- 语言底座：284B total parameters，13B active parameters。
- 视觉编码器：DeepSeek-ViT，自研，从头训练，支持任意分辨率。
- 756 x 756 图像：先变成 2,916 个 ViT patch tokens，经 3x3 压缩后变成 324 个视觉 token，再经 CSA 变成 81 个 visual KV entries。
- 从原始像素到最终 KV entries，整体压缩比约 7,056x。
- 对 800 x 800 输入，paper 图中 Ours 约 361 tokens、约 90 KV cache entries，平均分 77.2；Gemini-3-Flash 约 1100 tokens，平均分 76.5；GPT-5.4 约 740 tokens，平均分 71.1；Claude-Sonnet-4.6 约 870 tokens，平均分 65.3。

边界：

图 1 的平均分只覆盖 counting 和 spatial reasoning 等 7 个相关 benchmark，且排除了 in-house benchmarks。paper 自己也说明，这不能代表模型整体能力。

### 6.4 训练方式复用了 V4 的“专家再合并”思想

visual primitives paper 的 post-training 流程：

1. Specialized SFT：70% general multimodal/pure-text，30% visual primitives 数据。
2. 分别训练 box 路线的 FTwG 和 point 路线的 FTwP，避免小规模专门数据下的 mode conflict。
3. Specialized RL：用 GRPO，奖励由 format、quality、accuracy 三类 RM 共同构成。
4. Unified RFT：用两个专家模型生成 RFT 数据，保留 Normal-Level 和少量 Easy-Level，训练统一模型。
5. On-Policy Distillation：用 ETwG 和 ETwP 两个专家作为 teacher，把能力合并进单一模型。

这与 V4 tech report 的“多专家 OPD 合并”是一致思想。区别是：V4 主模型是文本/代码/数学/agent 等专家合并，paper 是 box/point 两种视觉思维模式合并。

### 6.5 paper 的局限同样值得讲

paper 自己列了三条 limitation：

- 输入分辨率受限，细粒度场景的 visual primitives 输出仍可能不精确。
- 当前能力依赖显式 trigger words，未来才希望模型自主判断是否启用。
- point primitives 解决复杂拓扑推理仍然困难，跨场景泛化有限。

组会可讲：

“这篇 paper 更像一个强信号，不是定论。它提示多模态推理可能需要从语言 CoT 走向视觉操作，但现阶段还需要 trigger、专门数据和任务内验证。”

## 7. 竞争格局：DeepSeek V4 放在中美开闭源路线里怎么看

### 7.1 中国开源路线的优势：工程透明度和效率堆栈

访谈里两位嘉宾都强调，中国团队在 Infra、训练效率、长上下文、MoE、量化训练上形成了自己的路径。DeepSeek 的 FP8 到 FP4、TileLang、mHC，Kimi 的 MuonClip 和长文本，Qwen、MiniMax、GLM 在多模态和 agent 上的探索，都不是简单复制 GPT 或 Claude。

这类透明度带来两个收益：

- 社区可以复现、适配、优化，SGLang 在 V4 发布当天支持推理和 RL 适配就是例子。
- 推理框架、训练框架、kernel DSL、量化方案会形成共创生态，反过来降低模型团队探索新架构的边际成本。

### 7.2 中国开源路线的压力：数据飞轮和默认工作流

访谈里关于数据飞轮有一个关键问题：最好的 coding/agent 数据来自真实使用，而获取真实使用的最佳方式是被大量用户用作默认工作流。

开源权重不一定意味着拿不到数据，因为万亿参数模型个人难以本地部署，很多使用仍然会通过 API 或第三方云发生。但在编程和 agent 领域，真实高质量数据很可能集中在少数有用户工作流入口的产品里，比如 coding assistant、IDE、云端 agent、企业协作平台。

这会带来一个竞争分野：

- 模型公司如果只有 checkpoint，没有默认工作流入口，评测和训练数据会受限。
- 拥有真实用户工作流的模型和产品团队，更容易形成“任务失败、人工修复、重新评测”的闭环。

### 7.3 闭源领先不只来自模型，也来自产品和定价信心

访谈对美国闭源模型的概括是：高溢价、快迭代、敢为新能力定价。DeepSeek V4 的 API 定价上探，说明中国开源模型在第一梯队能力上也开始尝试能力定价。

但这不意味着开源路线会完全变成闭源路线。更可能的形态是分层：

- 顶尖能力 API 接近闭源高价，用于覆盖训练、推理、RL、服务成本。
- 开源权重保留生态、本地部署、私有数据和二次优化价值。
- Flash/旧版本/轻量模型承担性价比和规模化使用。

## 8. 最适合会上的讨论题

### 讨论题一：我们评估模型时，是否还在看错误指标

建议从“模型单价”改成“单位任务完成成本”：

- 成功率。
- 平均 token。
- 平均工具调用。
- 平均人工返工。
- 失败恢复成本。
- 是否能进入默认工作流。

### 讨论题二：长上下文和 RAG/Agentic Search 是替代关系，还是协同关系

V4 自己的产品路线已经给了答案：

- non-think 使用 RAG。
- thinking mode 使用 agentic search。
- 1M context 用来承接长程状态、工具结果和复杂推理，不是完全替代检索。

### 讨论题三：visual primitives 是否会成为多模态推理的新基本接口

需要继续验证：

- 是否能泛化到 UI 操作、图表分析、工业视觉、医疗影像、地理遥感。
- 是否能从 trigger-based 变成模型自主路由。
- 是否能在真实多轮任务中减少幻觉和返工。
- 是否能与视觉生成、画线、标注、草图操作结合，形成更强的视觉外部化推理。

### 讨论题四：Agent infra 的护城河在哪里

V4 的 DSec 说明，模型团队会越来越需要自己的 agent sandbox、trajectory log、工具执行和恢复系统。可以讨论：

- 这是模型公司的内生能力，还是会被独立 infra 公司商品化。
- Agent 执行日志和数据飞轮是否会成为比模型权重更重要的数据资产。
- 企业部署时更关心模型分数，还是可恢复、可审计、可隔离。

### 讨论题五：DeepSeek V4 的“删除 paper”事件应如何解读

已确认事实：

- 本分析只确认用户提供了本地 PDF，且 PDF 元数据创建时间为 2026-04-30。
- “发布后删除”这一状态来自用户背景，本地材料无法独立验证原因。

谨慎推断：

- 不建议过度解读为技术错误。
- 更稳妥的说法是：这篇 paper 涉及数据构建、专门 benchmark、与 GPT/Claude/Gemini 的横向比较，披露边界可能更敏感。
- 如果要对外分享，建议把它作为“方向信号”和“方法启发”，不要把 release 状态包装成结论证据。

## 9. 可以直接放进 PPT 的标题句

1. DeepSeek V4 的主线不是“窗口变长”，而是“长程任务的成本结构被重写”。
2. V4 不是 R1 式新范式，而是系统级工程集成能力的展示。
3. 模型成本要从 token 价格，改看单位任务完成成本。
4. Agent 能力正在从应用层 wrapper，进入训练、评测、部署基础设施。
5. Visual primitives paper 把多模态推理问题从“看得清”推进到“指得准”。
6. 视觉原语不是最终答案里的框，而是推理过程里的坐标。
7. 评测的下一阶段不是更大榜单，而是更接近真实工作流的动态 eval。
8. DeepSeek 的开源路线正在从低价竞争，转向效率、工程透明度和生态共创。

## 10. 结论边界

### 已确认事实

- V4-Pro 和 V4-Flash 的参数规模、激活参数、1M 上下文、CSA/HCA、mHC、Muon、FP4、OPD、DSec 等来自 tech report。
- 访谈中关于 V4 工程复杂度、非 R1 式范式变化、成本叙事变化、benchmark 可信危机、定价上探、开源生态等内容来自用户提供的访谈原文。
- visual primitives paper 的 Reference Gap、box/point 原语、数据构建、训练流程、评测和 limitations 来自用户提供 PDF。

### 推断判断

- V4 的产业价值更接近“整栈效率和 agent 基建”，不是单点 benchmark。
- DeepSeek 正在从“低成本模型”转向“能力加工程透明度”的竞争叙事。
- visual primitives paper 可能代表 DeepSeek 多模态路线的一种下一步：用视觉操作补语言 CoT 的指代缺陷。
- Agent infra 和 eval infra 会成为模型公司下一阶段的核心资产。

### 待验证点

- V4 在真实企业任务中的单位完成成本是否优于闭源模型。
- V4 的 1M context 在多轮、多工具、强干扰长程任务中的稳定性。
- Flash 在商业场景中的最佳位置：默认工作模型、廉价 reasoning 模型，还是私有部署底座。
- OPD 是否能长期替代 mixed RL，且不造成隐性能力损失。
- visual primitives 是否能跨 benchmark、跨视觉领域泛化。
- DeepSeek 是否能通过 API、开源生态或自有产品形成足够强的数据飞轮。

## 11. 最终判断

如果只看 tech report，V4 是长上下文和 agent 时代的系统升级。如果把访谈和 visual primitives paper 加进来，V4 更像是 DeepSeek 正在形成的一条长期路线：在算力、成本、开源透明度和真实任务之间，用极端工程优化换取能力上限。

这条路线不一定总能在通用榜单上压过闭源头部模型，但它有清晰的战略价值：

- 让 1M context 变成可持续使用的系统能力。
- 让 RL rollout、agent serving、长程推理有更低成本。
- 让工具调用、沙箱、轨迹恢复进入模型训练和评测闭环。
- 让多模态推理从语言描述走向坐标化、可验证的视觉操作。

更克制的说法是：DeepSeek V4 没有证明开源模型已经全面超过闭源模型；它证明的是，开源模型团队可以在架构、infra、训练工艺和评测透明度上持续给行业贡献新的工程标准。

## 参考锚点

### 主材料

- DeepSeek-AI, `DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence`, PDF, 58 页，PDF 元数据创建时间 2026-04-24。
- DeepSeek-AI, `Thinking with Visual Primitives`, PDF, 25 页，PDF 元数据创建时间 2026-04-30。
- `DeepSeek_V4_tech_report_analysis_2026-04-25.md`，此前基于 tech report 的内部解读。
- `DeepSeek相关访谈.md`，《晚点聊 LateTalk》访谈整理。

### 内库方向锚点

- AI_SCAN id 123：BabyVision，多模态视觉原子能力与 “unspeakable” 视觉任务。
- AI_SCAN id 184：为什么现有 Agent Infra 无法支撑生产级应用，Agent 的 effect log、能力隔离、恢复语义。
- AI_SCAN id 088：模型能力性价比，强调价格、思考 token、速度、任务效果共同决定用户选择。
- AI_SCAN id 078：DeepSeek OCR paper，token compression 与 text-to-image 压缩路线作为视觉压缩历史锚点；该 md 抓取正文不可用，仅使用索引摘要作方向提示。
