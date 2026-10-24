# GPT-6 Astra 参数规模反推：10T 总参数，550B激活

| 项目 | 内容 |
| --- | --- |
| 作者 | [zac.w](https://www.zhihu.com/people/zac-w) |
| 发布日期 | 2026-09-11 18:58（中国标准时间） |
| 最后编辑 | 2026-09-11 19:00（中国标准时间） |
| 原文 | [知乎专栏文章][1] |

## 正文

> **结论摘要**
> OpenAI 尚未披露 GPT-6 Astra 的参数规模和 MoE 架构。综合训练规模、GB200 NVL72 的部署边界、MoE 稀疏率、单流推理性能、expert routing/communication、Fast mode 以及 Kimi K3 与 GPT-5.6 Sol 的定价锚点，本文当前最自洽的估计是：

- **总参数量：9–11T，点估计约 10T**
- **Unique active parameters：400–650B，点估计约 550B**
- **经济性 soft ceiling：约 800B**
- **Stretch ceiling：约 1T**

训练侧呈现出的计算规模更接近 **1T+ parameter-execution equivalent**。如果 Astra 确实采用 recurrent-depth 一类重复执行机制，那么约 500–550B 的 unique active weights 与更高的实际执行计算量可以同时成立。

本文试图回答两个问题：**Astra 的 checkpoint 可能有多大？一个 token 实际会激活多少 unique weights？** 分析方法是把训练规模、硬件部署、MoE 架构、推理性能与经济性放进同一个工程框架中，寻找能够同时满足这些约束的参数区间。

## 1. 结论总览与证据矩阵

### 1.1 核心证据链

下表中的区间和点估计，是每条证据链在相对独立的假设下给出的 working estimate。最终结论会综合考虑各证据的质量、约束强度与相互依赖性。

| 证据链 | Total params：区间 / 点估计 | Unique active：区间 / 点估计 | 置信度 | 核心说明 | 详见 |
| --- | --- | --- | --- | --- | --- |
| ① >100k GPU 预训练规模 | 7–14T / 10T | 约束弱；训练计算支持 1T+ effective-eq. | 总：中；激活：低 | Astra 使用 OpenAI 迄今最大规模之一的训练 run；更直接约束的是总训练 compute。 | 3.1 |
| ② NVL72 HBM / checkpoint 部署边界 | 8–12T / 10T | 约束弱 | 总：中；激活：低 | ~10T checkpoint 在 FP4/FP8 下与 NVL72 的 HBM 和 replica geometry 很自然。 | 3.2 |
| ③ MoE activation-ratio 架构 prior | 条件沿用 8–12T / 10T | 300–650B / 500B | 总：低；激活：中 | K3 等 frontier MoE 的激活比例处于几个百分点量级；10T × 约 5% ≈ 500B。 | 3.3 |
| ④ Standard decode：~54 tok/s | 8–11T / 9.5T | 350–900B / 600B | 总：中；激活：低–中 | 大 batch 下 weight traffic 更接近“本轮触达的 total expert bank”，因此对 total 更敏感。 | 3.4 |
| ⑤ EP routing / communication / fanout | 约束弱 | 350–650B / 500B | 总：低；激活：中 | 更高 activation ratio 会显著提高 destination fanout、dispatch/combine 和 per-expert workload。 | 3.5 |
| ⑥ Fast mode：最高 ~2× speed / 2× price | 约束弱 | 350–700B / 500B | 总：低；激活：中 | 较低 activation ratio 更容易通过缩小 batch、增加硬件或 MTP/spec decode 换取接近 2× 的单流速度。 | 3.6 |
| ⑦ K3 市场定价锚点 | 约束弱 | 350–500B / 420B | 总：低；激活：低–中 | K3 为 104B active、12–15/M output；按市场价格粗映射，Astra 50/M 对应约 350–430B。 | 3.7 |
| ⑧ Sol → Astra 同厂商定价 | 约束弱 | 500–800B / 625B | 总：低；激活：中–高 | 输出价只提升 2.5×；在相近 margin 和 serving efficiency 下，对 active 增长形成较强经济约束。 | 3.8 |
| ⑨ Recurrent depth（若存在） | 约束弱 | 400–650B / 550B | 总：低；激活：中偏低 | 重复执行同一组 weights，可以让 ~500B unique active 对应 ~700–900B 甚至更高的 effective execution。 | 3.9 |
| 综合 posterior | 9–11T / 10T | 400–650B / 550B | — | 当前最自洽区间；~800B 为经济性 soft ceiling，~1T 为 stretch ceiling。 | 5 |

### 1.2 关键公开锚点

- GPT-6 Astra API 标准定价为 **$10/M input、$50/M output**；Fast mode 为标准价格的 2×，官方描述为最高可达 Standard 的 2× 速度。[^1][^2]
- GPT-5.6 Sol 标准定价为 **$4/M input、$20/M output**。[^3]
- Artificial Analysis 当前测得 Astra（max）约 **54 tok/s**，Sol（max）约 **65 tok/s**。[^4]
- Kimi K3 技术报告公开 **2.8T total / 104B activated**，896 个 routed experts 中每 token 激活 16 个。[^5]
- K3 官方输出价格约 **$15/M**；第三方市场最低输出价格约 **$12/M**。[^6][^7]
- Axios 报道，Astra 使用了 OpenAI 迄今最大的训练 run，规模超过 **100,000 GPUs**，位于 Stargate Texas。[^8]
- NVIDIA 公布的 GB200 NVL72 规格为 **72 GPU、13.4 TB HBM3E、576 TB/s HBM bandwidth、130 TB/s NVLink bandwidth**。[^9]
- 关于 Astra 使用 recurrent-depth / looped execution 的说法目前主要来自媒体报道，因此本文将其作为解释性架构假设。[^10]

## 2. 三个需要分开的“参数量”

讨论 MoE frontier model 时，至少要区分三个量。

### 2.1 Total parameters：$P_{total}$

checkpoint 中全部参数的总量。对于 MoE，大部分 routed expert weights 在单个 token 上不会同时参与计算，但它们仍然决定模型容量、checkpoint residency 和 replica 的最低内存规模。

### 2.2 Unique active parameters：$P_{active}$

一个 token 在一次标准 forward 中实际触达的不同 weights 总量。这是本文重点希望约束的变量，也是推理成本、routing density 和 per-token compute 的核心架构量之一。

### 2.3 Effective parameter-executions：$P_{effective}$

同一组 weights 若在一个 token 的处理过程中重复执行，或者训练阶段还包含额外 head、辅助目标和额外计算，那么实际 parameter executions 会高于 unique active weights。

一个可用于理解本文结论的示意关系是：

$$
P_{total}\approx 10T, \qquad P_{active}\approx 500\text{–}550B, \qquad P_{effective}\approx 700\text{–}900B+.
$$

如果训练阶段进一步叠加更高执行倍率或额外目标，总训练算力呈现出 **1T+ parameter-equivalent** 的特征是自然的。

## 3. 九条核心证据链

本节与 1.1 的证据矩阵严格一一对应。为了让不同证据链能够被独立复核，每一节都按 **计算输入 → 计算过程 → 区间与点估计** 展开。

其中 3.4–3.6 在需要把 MoE 行为量化时，共用一个计算实例：**routed expert bank = 9.28T、576 个 routed experts、FP4 weight payload ≈ 0.5 byte/param**。这组参数只用于把公式变成可计算数字，第 4 节会说明它为什么能自然构成一个约 9.3T total / 450B active 的模型。

### 3.1 证据①：>100k GPU 的预训练规模

Axios 报道，Astra 使用了 OpenAI 最大规模的 training run，超过 100,000 张 GPU。[^8] 训练规模首先给出的是 **parameter-execution equivalent** 的量级，因此可以从训练 FLOPs 反推“每 token 实际执行了多少参数等价计算”。

#### 计算输入

用 GB200 作为数量级参照：

- GPU 数：$N_{GPU}=100,000$；
- dense FP8 峰值：约 $5\,PFLOPS/GPU$，即整集群约 $500\,EFLOPS$；[^9]
- 大规模训练 sustained model FLOPS：取峰值的 **25–35%**；
- 因而 sustained compute 约为：

$$
P_{sustained}\approx125\text{–}175\,EFLOPS.
$$

不同训练时长对应的总 FLOPs 为：

| 训练时长 | 125 EFLOPS | 175 EFLOPS |
| --- | --- | --- |
| 45 天 | 4.86*10^{26} | 6.80*10^{26} |
| 60 天 | 6.48*10^{26} | 9.07*10^{26} |
| 90 天 | 9.72*10^{26} | 1.36*10^{27} |

经典 decoder-only 训练的一阶关系为：

$$
C\approx6N_{eff}D,
$$

其中 $D$ 是训练 token 数，$N_{eff}$ 是每 token 的 parameter-execution equivalent。

取一个中性场景：**60 天、30% sustained efficiency、100T training tokens**：

$$
C\approx500\,EFLOPS\times30\%\times60\times86400 \approx7.78\times10^{26}\ FLOPs,
$$

因此：

$$
N_{eff}\approx \frac{7.78\times10^{26}}{6\times100\times10^{12}} \approx1.30T.
$$

如果把训练窗口放在 45–90 天、token budget 放在 80–120T、sustained efficiency 放在 25–35%，则 $N_{eff}$ 会扩展到大约 **0.7–2.8T**。这个范围很宽，但中心区域稳定地进入 **1T+ effective execution**。

要把这个量条件性地映射到 total checkpoint，还需要两个架构量：

$$
P_{total}\approx \frac{N_{eff}}{m_{exec}\cdot r_{active}},
$$

其中 $m_{exec}$ 表示 recurrent / auxiliary compute 对 unique weights 的执行倍率，$r_{active}$ 表示 unique active / total 的比例。以中心 $N_{eff}\sim1.3T$、$m_{exec}\sim1.3\text{–}1.7$、$r_{active}\sim6\text{–}10\%$ 做条件换算，会落到约 **8–17T** 的大区间；考虑后文 serving 证据把高端进一步收紧后，训练侧对应的工作区间取 **7–14T，中心约 10T**。

这一步的价值主要在于说明：**10T 级 sparse checkpoint 与 >100k GPU 的 hero run 处于同一合理量级，同时训练侧允许 effective execution 显著高于 unique active。**

**落到矩阵：** Total **7–14T / 10T**；Unique active 单独约束较弱；training effective execution 的中心量级约 **1T+**。

### 3.2 证据②：NVL72 的 HBM 与 checkpoint 部署边界

GB200 NVL72 提供 **13.4 TB HBM3E**，并将 72 张 GPU 放在一个高带宽 NVLink domain 中。[^9] 对 10T 级 MoE 来说，一个重要问题是：模型权重能否以自然的 replica geometry 驻留在一个 NVL72 内。

#### 计算输入

权重 residency 可以写成：

$$
M_{weights}=P_{total}\times b_w,
$$

其中 $b_w$ 是每个参数的存储字节数。

| Total params | FP8：1 byte/param | FP4：0.5 byte/param |
| --- | --- | --- |
| 8T | 8 TB | 4 TB |
| 10T | 10 TB | 5 TB |
| 12T | 12 TB | 6 TB |
| 14T | 14 TB | 7 TB |

如果以 FP8 residency 作为更严格的 memory geometry 检查：

- **8T**：留下约 $13.4-8=5.4$ TB runtime headroom；
- **10T**：留下约 $3.4$ TB；
- **12T**：留下约 $1.4$ TB；
- **14T**：单纯 FP8 weights 已超过单柜 HBM。

而在 FP4 serving 下，10T 只需要约 5 TB weight payload，scale / metadata 加进去后仍有充足空间用于 KV cache、workspace 与 runtime buffers。

因此，**10T 左右同时位于“FP8 尚可完整驻留、FP4 有明显 runtime headroom”的甜点区**。8T 更宽松，12T 已接近 FP8 单柜 residency 的上沿，再往上则越来越依赖 FP4 或更复杂的 placement。

这条证据对 routing sparsity 几乎不施加直接约束，因为 400B active 和 1T active 都可能来自同一个 10T checkpoint。

**落到矩阵：** Total **8–12T / 10T**；Unique active **约束弱**。

### 3.3 证据③：现代 MoE 的 activation-ratio prior

Kimi K3 是一个公开参数较完整的 frontier MoE 锚点：**2.8T total / 104B activated**。[^5]

它对应的整体激活比例为：

$$
r_{K3}=\frac{104B}{2.8T}\approx3.71\%.
$$

Astra 的精确 sparsity 未知，因此本文使用一个更宽的工作 prior：**3–6% 为宽区间，3.5–5% 为主要概率区域**。

#### 具体计算

把 total 先放在上一节支持的 8–12T 区间。为了显式考虑 always-active dense components，写成：

$$
P_{active}=P_{dense}+r_{MoE}(P_{total}-P_{dense}).
$$

取 $P_{dense}=50\text{–}100B$，$r_{MoE}=3.5\text{–}5.0\%$：

- 低端例子：$P_{total}=8T$、$P_{dense}=50B$、$r=3.5\%$

$$
P_{active}\approx50B+(8T-50B)\times3.5\% \approx328B;
$$

- 高端例子：$P_{total}=12T$、$P_{dense}=100B$、$r=5.0\%$

$$
P_{active}\approx100B+(12T-100B)\times5\% \approx695B.
$$

- 中心例子：$P_{total}=10T$、$P_{dense}=60B$、$r=4.5\%$

$$
P_{active}\approx60B+(10T-60B)\times4.5\% \approx507B.
$$

考虑架构 prior 本身的误差，把两端略作收缩后，工作区间取 **300–650B**，点估计约 **500B**。

**落到矩阵：** Total 条件沿用 **8–12T / 10T**；Unique active **300–650B / 500B**。

### 3.4 证据④：Standard decode 的 ~54 tok/s

Artificial Analysis 测得 Astra（max）输出速度约 **54 tok/s**。[^4] 对应单流 token step budget：

$$
T_{step}=\frac{1}{54}\approx18.5\text{ ms/token}.
$$

这 18.5 ms 可以拿来做一个 HBM + communication + attention 的总预算检查。

#### 第一步：batch 会让 expert-bank coverage 快速上升

如果模型有 $E$ 个 experts、每 token 选择 $k$ 个，一个 decode batch 中至少被某个 token 命中过一次的 expert-bank 比例近似为：

$$
f(B)=1-(1-k/E)^B.
$$

以 $E=576,k=24$ 为例：

| Decode batch B | expert bank coverage |
| --- | --- |
| 8 | 28.9% |
| 16 | 49.4% |
| 32 | 74.4% |
| 64 | 93.4% |
| 128 | 99.6% |

所以 Standard production batch 到几十个 token/step 后，weight traffic 已经接近整个 routed expert bank。

#### 第二步：把 total expert bank 换成 HBM 时间

以 9.28T routed expert bank、FP4 payload $b_w=0.5$ byte/param 为例：

$$
M_{expert}=9.28T\times0.5\approx4.64\ TB.
$$

GB200 NVL72 理论 HBM bandwidth 为 576 TB/s。若有效 bandwidth utilization 取 65–80%，则：

$$
BW_{eff}\approx374\text{–}461\ TB/s.
$$

在 $B=64$、coverage = 93.4% 时，需要读取的 expert weights 约：

$$
4.64\times93.4\%\approx4.33\ TB.
$$

对应 HBM 时间：

$$
T_{HBM}\approx\frac{4.33}{374\text{–}461} \approx9.4\text{–}11.6\ ms.
$$

在 $B=128$ 时 coverage 接近 100%，则约为：

$$
T_{HBM}\approx10.1\text{–}12.4\ ms.
$$

相对于 18.5 ms 的完整 step budget，还剩约 **6–9 ms** 给 attention、router、dispatch/combine、同步、sampling 与 kernel gaps。

反过来，如果 total expert bank 继续显著超过 11–12T，在相同 FP4 和 bandwidth efficiency 下，weight streaming 会进一步侵占这部分余量；而 8–11T 正好处于较协调区域。因此 Standard decode 对 total 的中心估计约为 **9.5T**。

对 unique active 的约束较宽。若 total 在 9–10T 左右，单 token activation ratio 在约 3–9% 都能在大 batch 下产生相近的 full-bank HBM 行为，对应 active 粗略为 **350–900B**；因此这里取 **600B** 作为弱点估计。

**落到矩阵：** Total **8–11T / 9.5T**；Unique active **350–900B / 600B**。

### 3.5 证据⑤：EP routing、communication 与 fanout

当 total expert bank 基本固定时，unique active 的增大主要体现为 **top-k / routing density 增大**。这一条证据可以直接比较 500B 与 1.2T 两种假设在通信上的代价。

#### 第一步：active params 映射到 top-k

仍取 9.28T routed expert bank、$E=576$，并假设 always-active dense components 约 60B：

$$
P_{active}\approx60B+9.28T\times\frac{k}{576}.
$$

由此：

| top-k | routed active | +60B dense 后 unique active |
| --- | --- | --- |
| 18 | 290B | 350B |
| 24 | 387B | 447B |
| 32 | 516B | 576B |
| 36 | 580B | 640B |
| 72 | 1.16T | 1.22T |

所以矩阵中的 **350–650B**，在这个例子里大致对应 **top-18 到 top-36**；1.2T 则需要接近 **top-72**。

#### 第二步：计算 destination-GPU fanout

576 experts 均匀分布到 72 GPU，相当于 8 experts/GPU。忽略 routing correlation 时，一个 token 选择 $k$ 个 experts 后触达的不同 GPU 数量期望约为：

$$
G_{dest}\approx72\left[1-\left(\frac{71}{72}\right)^k\right].
$$

代入：

| top-k | 期望 destination GPUs |
| --- | --- |
| 18 | 16.0 |
| 24 | 20.5 |
| 32 | 26.0 |
| 36 | 28.5 |
| 72 | 45.7 |

因此 top-72 相对于 top-24，destination fanout 大约提高：

$$
\frac{45.7}{20.5}\approx2.23\times.
$$

若 hidden size 取 16,384、dispatch activation 使用 2 bytes/element，则每个 token 的 hidden payload 为：

$$
16384\times2\approx32\ KB.
$$

假设同一 destination GPU 上的多个 expert assignment 可以合并成一次 token payload，那么单层 dispatch + combine 的网络 payload 约为：

- top-24：$20.5\times32KB\times2\approx1.35MB/token/layer$；
- top-72：$45.7\times32KB\times2\approx2.99MB/token/layer$。

若有 64 个 MoE layers，累计 payload 数量级约为：

- top-24：**86 MB/token**；
- top-72：**192 MB/token**。

实际实现会受到 overlap、NVLink collectives、token packing 和 local-expert hits 影响，但 **2.2× fanout 与约 3× per-expert workload** 的相对关系非常稳定：

$$
m_{expert}\approx\frac{Bk}{E},
$$

所以 top-72 的 $m_{expert}$ 永远是 top-24 的 3×。

这使 350–650B 区间在 communication、load balance 与 compute pressure 上明显更容易维持高吞吐。

**落到矩阵：** Unique active **350–650B / 500B**。

### 3.6 证据⑥：Fast mode 的 2× speed / 2× price

OpenAI 官方表示，Astra Fast mode 最高可达到约 **2× Standard speed**，价格也是 Standard 的 **2×**。[^1][^2] 如果 Standard 是 ~54 tok/s，则 Fast 的目标速度可以接近 100 tok/s，对应：

$$
T_{Fast}\sim10\ ms/token.
$$

Fast mode 的关键是：**降低 batch 时，较低 routing density 能显著减少每一步真正触达的 expert bank。**

#### 直接计算 top-24 与 top-72

仍使用 9.28T expert bank、FP4 0.5 byte/param，因此 full-bank payload 为 4.64 TB。取有效 HBM bandwidth 的中值：

$$
BW_{eff}=576\times72.5\%\approx418\ TB/s.
$$

expert coverage 仍由：

$$
f(B)=1-(1-k/E)^B
$$

给出。

| routing | Batch | expert coverage | 本步 weight payload | 仅 HBM 时间 |
| --- | --- | --- | --- | --- |
| top-24 | 8 | 28.9% | 1.34 TB | 3.2 ms |
| top-24 | 16 | 49.4% | 2.29 TB | 5.5 ms |
| top-72 | 8 | 65.6% | 3.05 TB | 7.3 ms |
| top-72 | 16 | 88.2% | 4.09 TB | 9.8 ms |

这个表对 Fast mode 很有区分力：在约 10 ms 的 token-step budget 下，**top-24 / ~450B active** 在 batch=8–16 时仍能留下约 4.5–6.8 ms 给 attention、communication 与其他 overhead；而 **top-72 / ~1.2T active** 在 batch=16 时，理论上仅 expert-weight HBM read 就已经接近 10 ms。

Fast 实际还可以依靠更多硬件、MTP/speculative decoding 或更好的 quantization 来突破这个简单 roofline，因此这里给出的仍是 serving preference，而非物理边界。将 routing density 从 top-18 到约 top-40 映射回 active params，大致得到 **350–700B** 的友好区间。

**落到矩阵：** Unique active **350–700B / 500B**。

### 3.7 证据⑦：K3 的市场定价锚点

K3 同时公开了 active parameters 和 API 价格，因此可以构造一个直接的跨厂商 market-price prior：

- K3 active：104B；[^5]
- K3 官方 output：15/M；[^6]
- 市场较低 output：约 12/M；[^7]
- Astra output：50/M。[^1]

#### 一阶价格缩放

若先假设“每单位 active parameter 的市场价格”相同，则：

按 K3 官方价格：

按市场较低价格：

两种口径给出的中心都在 400B 左右。跨厂商比较还包含厂商 margin、batch policy、硬件效率、模型价值溢价与供需差异，因此给它约 ±15–20% 的宽化后：

点估计取靠近这两个一阶结果上沿的 **420B**。

这条证据的意义是：**400B 量级 active 完全可以用当前 frontier open-model 市场价格解释；Astra 的50/M 并不要求 1T 级 active 才能成立。**

**落到矩阵：** Unique active **350–500B / 420B**。

### 3.8 证据⑧：Sol → Astra 的同厂商定价

同厂商比较能够最大程度减少产品定位、基础设施成本口径和 margin 策略的差异，因此这是本文对 active upper bound 权重较高的一条证据。

OpenAI 当前 output pricing 为：[^1][^3]

$$
Price_{astra}=\$50/M, \qquad Price_{sol}=\$20/M,
$$

因此：

$$
\frac{Price_{astra}}{Price_{sol}}=2.5.
$$

设每 active parameter 的 serving cost 为 $\kappa$，gross margin 为 $g$，则：

$$
\frac{P_A}{P_S} =2.5\times \frac{1-g_A}{1-g_S} \times \frac{\kappa_S}{\kappa_A}.
$$

#### 第一步：给 Sol 一个工作 prior

K3 的 104B active 在 $12\text{–}15/M$；若机械映射到 Sol 的 $20/M$：

$$
104B\times\frac{20}{15}\approx139B,
$$

$$
104B\times\frac{20}{12}\approx173B.
$$

考虑 OpenAI 的 serving stack、模型价值定价与 batch 策略可能与 K3 provider 显著不同，本文把这个结果向上放宽为：

$$
P_{Sol}\approx200\text{–}300B,
$$

中心取 250B。它是后续经济性计算的 working prior。

#### 第二步：用 2.5× price ratio 推 Astra

若 margin 与单位 active serving cost 基本相同：

| Sol active | Astra implied active |
| --- | --- |
| 200B | 500B |
| 250B | 625B |
| 300B | 750B |

因此同单位经济性对应的自然区间就是 **500–750B**，中心 **625B**。

#### 第三步：计算更高 active 所要求的效率提升

取 Sol = 250B，假设两代 gross margin 不变，则为了容纳更大的 Astra active，所需单位 active cost 比例为：

$$
\frac{\kappa_A}{\kappa_S} =\frac{2.5}{P_A/P_S}.
$$

| Astra active | 相对 Sol active | $\kappa_A/\kappa_S$ | 所需单位成本改善 |
| --- | --- | --- | --- |
| 625B | 2.5× | 1.00 | 0% |
| 800B | 3.2× | 0.78 | 22% |
| 1.0T | 4.0× | 0.625 | 37.5% |
| 1.2T | 4.8× | 0.52 | 48% |

这张表直接给出了经济性上限的含义：

- **~625B** 几乎不需要额外效率假设；
- **~800B** 可以由一代约 20–25% 的 serving efficiency 改善解释；
- **~1T** 需要接近 40% 的单位成本下降；
- **~1.2T** 需要接近 2× 的单位 active serving efficiency，或者接受明显不同的 margin / GPU allocation。

因此本文把 **~800B** 定义为 economic soft ceiling，把 **~1T** 作为 stretch ceiling，并把 500–800B 作为这条证据的主要区间。

**落到矩阵：** Unique active **500–800B / 625B**。

### 3.9 证据⑨：Recurrent depth 提供训练与推理之间的桥梁

媒体报道将 Astra 描述为采用 recurrent-depth 一类架构，即部分计算 block 可以在同一个 token 上重复执行。[^10] 这条信息目前适合用作 reconciliation scenario：它允许 unique weights 保持在数百 B，同时执行计算量进一步上升。

#### 具体计算

取前述 serving 证据的中心区间：

$$
P_{active}=500\text{–}550B.
$$

假设平均 recurrent execution multiplier 为：

$$
m_{rec}=1.3\text{–}1.7,
$$

则推理侧 effective execution 为：

$$
P_{effective,infer}=P_{active}\times m_{rec} \approx650\text{–}935B.
$$

一个中心场景是：

$$
550B\times1.5\approx825B.
$$

训练阶段若再有 10–30% 的额外 auxiliary / multi-token / training-only compute：

$$
P_{effective,train} \approx825B\times(1.1\text{–}1.3) \approx908B\text{–}1.07T.
$$

如果取 unique active 区间高端和 recurrence 高端：

$$
550B\times1.7\times1.2\approx1.12T.
$$

因此，**500–550B unique active → 650–900B+ inference-effective → 1T 左右 training-effective** 可以形成连续的计算链。这与 3.1 从 >100k GPU 训练规模得到的 1T+ parameter-execution signal 在量级上能够闭合。

由于 recurrent depth 的具体倍率没有官方披露，这条证据对 unique active 的作用主要是提升 400–650B 区间与训练算力之间的一致性，点估计仍取约 550B。

**落到矩阵：** Unique active **400–650B / 550B**；Inference effective execution 约 **650–900B+**，Training effective 约 **1T 左右或更高**。

## 4. 一个可计算的 Astra 架构 sanity check

前面的推导给出了约 **10T total / 500B active** 的统计区间。下面构造一个规整的 MoE geometry，验证这组数字是否能从常见 Transformer 参数关系中自然出现。

取：

| 参数 | 工作假设 |
| --- | --- |
| MoE layers | 64 |
| hidden size H | 16,384 |
| expert intermediate I | 5,120 |
| routed experts E | 576 |
| routing | top-24 |
| GQA | 128 Q heads / 16 KV heads（示意） |
| shared expert | 约 1 个 / layer（示意） |

SwiGLU routed experts 的参数量粗略为：

$$
P_{experts}\approx 3\times H\times I\times E\times L \approx9.28T.
$$

对应 top-24 routed active：

$$
P_{routed,active} \approx9.28T\times\frac{24}{576} \approx386.5B.
$$

再加 attention、shared expert、embedding 等 dense components，unique active 可以自然来到：

$$
\boxed{440\text{–}460B}.
$$

总参数则落在约：

$$
\boxed{9.3\text{–}9.4T}.
$$

这个例子还有一个很顺眼的系统属性：

$$
576 / 72 = 8,
$$

即一个 NVL72 上可以对应 **8 experts/GPU/layer**。如果把 expert 粒度进一步细化为 1152 experts / top-48，activation ratio 仍保持不变，同时可以获得更细的负载均衡粒度。

因此，**9–10T total + 400–500B active** 可以由一个结构规整、硬件 placement 自然的 MoE geometry 产生。具体的 layer 数、hidden size、expert count 和 top-k 仍然只是 sanity-check 参数；真正稳定的量是 **约 4–6% 的 activation ratio 与约 10T 的 total scale**。

## 5. 综合判断

把九条证据放在一起，total 和 unique active 的信息来源并不相同：

- **Total params** 主要由训练规模、NVL72 checkpoint geometry、Standard decode 的 HBM budget 和可构造的 MoE geometry 共同约束；
- **Unique active params** 主要由 MoE activation ratio、routing/communication、Fast mode 以及 K3 + Sol/Astra 的经济性锚点共同约束；
- **Recurrent depth** 则为 unique active 与更高 effective compute 之间提供了一个可能的连接机制。

当前 posterior 可以概括为：

| 变量 | 当前判断 | 置信度 |
| --- | --- | --- |
| Total parameters | 9–11T | 低–中 |
| Total point estimate | ~10T | 低–中 |
| Unique active parameters | 400–650B | 中 |
| Unique active point estimate | ~550B | 中 |
| Economic soft ceiling | ~800B | 中 |
| Stretch ceiling | ~1T | 低–中 |
| Inference effective execution | ~650–900B（若有 recurrence） | 低 |
| Training effective compute | 1T+ parameter-equivalent | 低–中 |

最自洽的中心图景是：

$$
\boxed{P_{total}\approx10T}
$$

$$
\boxed{P_{active}\approx500\text{–}550B}
$$

$$
\boxed{P_{effective}\approx700\text{–}900B+}
$$

这组数字同时解释了三个现象：Astra 需要极大的训练规模；10T 级 checkpoint 与 NVL72 的 memory geometry 高度匹配；而约 500B 的 unique active 又能让 $50/M output 的长期 serving economics、54 tok/s Standard 性能以及 2× price / 2× speed 的 Fast mode 保持在一个相对协调的区域。

在现有公开信息下，**400–650B 是最值得押注的 unique-active 区间**。超过约 800B 后，模型需要越来越依赖更强的 serving efficiency、MTP/speculative decoding 或更高的 GPU allocation；到 1T 左右开始进入 stretch 区域。总参数方面，**~10T** 仍是目前与训练规模、checkpoint residency 和 MoE geometry 最协调的中心估计。

## 参考来源

[^1]: OpenAI, GPT-6 Astra Model, [API documentation](https://developers.openai.com/api/docs/models/gpt-6-astra)
[^2]: OpenAI, [GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/) / [Fast mode](https://openai.com/api-fast-mode/).
[^3]: OpenAI, **GPT-5.6 Sol Model**, [API documentation](https://developers.openai.com/api/docs/models/gpt-5.6-sol).
[^4]: Artificial Analysis, [GPT-6 Astra (max) vs GPT-5.6 Sol (max)](https://artificialanalysis.ai/models/comparisons/gpt-6-astra-vs-gpt-5-6-sol).
[^5]: Kimi Team, **Kimi K3: Open Frontier Intelligence**, [arXiv:2607.24653](https://arxiv.org/abs/2607.24653).
[^6]: Artificial Analysis, **Kimi K3 (max)** — [first-party Kimi API pricing](https://artificialanalysis.ai/models/kimi-k3).
[^7]: Artificial Analysis, [Kimi K3 API Provider Benchmarking & Price Analysis](https://artificialanalysis.ai/models/kimi-k3/providers).
[^8]: Axios, [“Welcome to the AGI era,” OpenAI says as GPT-6 Astra debuts](https://www.axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman), Sep. 3, 2026.
[^9]: NVIDIA, [GB200 NVL72 Specifications](https://www.nvidia.com/en-us/data-center/gb200-nvl72/).
[^10]: TechRadar, [GPT-6 Astra lays the foundations for a new way of reasoning](https://www.techradar.com/pro/gpt-6-astra-lays-the-foundations-for-a-new-way-of-reasoning-a-great-tool-for-businesses-but-experts-have-their-concerns), Sep. 4, 2026.

*基于截至 2026-09-11 的公开信息与工程推断。OpenAI 尚未公开 Astra 的参数量、expert 配置或训练 FLOPs；本文数值均为 working estimates。*


## References

[1]: https://zhuanlan.zhihu.com/p/2081808860764022204 "GPT-6 Astra 参数规模反推：10T 总参数，550B激活"
