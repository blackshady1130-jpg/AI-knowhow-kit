---
name: eval-conclusion-builder
description: 生成评测结论与对比分析文案。适用于模型评测、A/B对比、in-domain/out-of-domain结果解读、月报评测结论输出。
---

# Eval Conclusion Builder

## Use When

- 用户给了评测数据，要求“怎么讲结论”。
- 用户要比较版本差异、竞品差异或泛化能力。

## Mandatory Frame

输出必须包含：

1. 任务定义：评测对象、任务范围、样本边界
2. 指标口径：使用什么指标、如何解释
3. 对比结论：至少两个维度（如历史版本、外部基线）
4. 结论边界：哪些成立、哪些暂不能外推
5. 下一步：badcase、复评或数据补充动作

## Default Output Format

- 一句话结论
- 对比表（维度/结果/解读）
- 风险与边界
- 执行建议（短期/中期）

## Hard Rules

- 没有口径就不能下强结论。
- 只在 in-domain 提升时，不称“全面提升”。
- 不把推断写成事实。
