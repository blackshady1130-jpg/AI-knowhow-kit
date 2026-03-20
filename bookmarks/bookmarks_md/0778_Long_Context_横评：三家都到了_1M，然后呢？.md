# Long Context 横评：三家都到了 1M，然后呢？

调研日期: 2026-03-15

2026 年 3 月，三大前沿模型厂商终于都站到了 1M context window 的门槛上。在 MRCR v2 8-needle（目前最严格的 long context 检索测试）上，Claude Opus 4.6 在 1M 处得分 76%，GPT-5.4 在 512K-1M 区间是 36.6%，Gemini 3 Pro 在 1M 处只有 24.5%。

## 拆解"无敌"假象：GPT-5.2 的 256K 边界

GPT-5.2 只有 256K 的 context window，曲线在那里就截止了。GPT-5.4 扩展到 1M 之后，256K 以外的衰减才暴露出来。

### GPT-5.2 与 GPT-5.4 逐区间对比

| Context 区间 | GPT-5.2 | GPT-5.4 | 差异 |
| --- | --- | --- | --- |
| 4K-8K | 98.2% | 97.3% | -0.9 |
| 8K-16K | 89.3% | 91.4% | +2.1 |
| 128K-256K | 77.0% | 79.3% | +2.3 |
| 256K-512K | N/A | 57.5% | — |
| 512K-1M | N/A | 36.6% | — |

在重叠区间（4K-256K），两个模型的性能差异极小（±2%），说明这不是代际能力退步，而是 GPT-5.2 根本没有被测试过 256K 以上的场景。

## 跨模型横评：谁在 1M 真正能用？

### 256K 聚合分数

| 模型 | 分数 | 来源 |
| --- | --- | --- |
| Claude Opus 4.6 | 93.0% | Anthropic 系统卡 |
| Claude Sonnet 4.6 | 90.3% | Anthropic 系统卡 |
| GPT-5.2 | 70.0% | OpenAI 自报 |
| Gemini 3 Flash | 58.5% | contextarena.ai |
| Gemini 3 Pro | 45.4% | contextarena.ai |

### 1M 聚合分数

| 模型 | 分数 | 来源 |
| --- | --- | --- |
| Claude Opus 4.6 | 76.0% | Anthropic 系统卡 |
| Claude Sonnet 4.6 | 65.8% | Anthropic 系统卡 |
| GPT-5.4 | 36.6% | OpenAI 官方 |
| Gemini 3 Flash | 32.6% | contextarena.ai |
| Gemini 3 Pro | 24.5% | contextarena.ai |

Claude Opus 4.6 在 1M 处的 76.0% 是一个质变。对比前代 Sonnet 4.5 的 18.5%，提升了 4 倍。

## Context Window ≠ Context Reliability

GPT-5.2 只有 256K 的 context window，但在该范围内仍然有 77%。Gemini 2.5 Pro 虽然标称 1M，在 1M 处只有 16.4%。Claude Opus 4.6 是唯一在 1M 处保持 70%+ 的模型。

## 各家策略复盘

### Anthropic："晚发先至"
从 2024 年 3 月到 2026 年 3 月，整整两年都在 200K。Anthropic 认为 context window 扩张不是解决方案，context 管理才是。当他们最终推出 1M 时，性能（76%）远超早年就提供 1M 的 Gemini（24.5%）。

### Google Gemini：先行者的困境
从 2024 年初率先提供 1M，但在 8-needle MRCR v2 上的表现一直不理想。128K 处改善很快，但 1M 处的鸿沟还在。

### OpenAI：精度优先的区间制
GPT-5.2 选择了 256K，GPT-5.4 扩展到 1.1M 时，272K 是标准模式，1M 是付费 premium 模式。

## 结论

"The context-window arms race is over. The context-reliability race is the real story now."

关键 takeaway：
- GPT-5.2 在 256K 内确实很强，但从未在 256K 以上接受过考验
- Gemini 的 1M 和 Claude 的 1M 在 MRCR v2 8-needle 上差距是 3 倍（24.5% vs 76.0%）
- 如果需要可靠地使用 256K-1M 的 context，Claude Opus 4.6 目前是唯一维持 70%+ 性能的选择
- 如果 context 在 128K 以内，各家前沿模型差异不大

---
Source: https://yage.ai/share/long-context-benchmark-20260315.html
