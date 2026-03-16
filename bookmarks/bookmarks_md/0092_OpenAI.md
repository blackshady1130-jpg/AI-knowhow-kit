---
url: https://mp.weixin.qq.com/s/Y_s2hZUZpRghDUT9x3ps1Q
title: "OpenAI：过程监督在数学推理中的新突破！"
description: "通过过程监督改善数学推理能力。"
author: "lencx"
captured_at: "2026-03-08T10:27:35.445Z"
---

# OpenAI：过程监督在数学推理中的新突破！

> 🔗
>
> -   论文：Let’s Verify Step by Step\[1\]
>
> -   Blog：Improving mathematical reasoning with process supervision\[2\]
>
> -   Dataset：openai/prm800k\[3\]
>

OpenAI  训练了一个模型，通过对每一个正确的推理步骤（过程监督）给予奖励，而不仅仅是奖励最后的正确答案（结果监督），使其在数学问题解决方面达到了新的水平。与结果监督相比，过程监督不仅提高了模型的性能，而且也带来了重要的对齐（即模型与人类期望相符）优势：它直接训练模型产生符合人类认可的思维过程。

## 引言

近年来，大型语言模型在执行复杂的多步推理任务的能力上有了极大的改进。然而，即便是最先进的模型仍然会产生逻辑错误，这些错误通常被称为“幻觉”。降低这种幻觉的出现频率是构建符合人类期望的 AGI（人工智能）的关键步骤。

可以通过结果监督或过程监督来训练奖励模型以检测这些“幻觉”，其中结果监督是根据最终结果提供反馈，过程监督则是为思考链中的每个步骤提供反馈。在之前的研究基础上，OpenAI 使用了 MATH 数据集进行了详细的比较，发现过程监督的效果明显优于结果监督，即使仅从结果评价也是如此。为了鼓励相关研究，OpenAI 公开了完整过程监督数据集。

> 📌 PRM800K
>
> PRM800K 是一个过程监督数据集，包含了由模型生成的 MATH 数据集问题解决方案的 800,000 步级别的正确性标签。关于 PRM800K 数据集和该项目的更多信息可以在论文中找到。
>
> OpenAI 发布了原始标签以及在项目第一阶段和第二阶段向标签制作者提供的指示，以下图片中可以看到示例标签。
>
> ![图片](https://mmbiz.qpic.cn/mmbiz_png/90Kxd0FAJJd3Gia00qKdaG5xV384jUZZXMnIt2iahl2EPUQWcvpFPb1fbclBd7tiaic8JBZzgZQsacqJ5TrRkwSRhQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## 对齐影响

过程监督相比结果监督在对齐上有几个优点。它直接奖励模型按照符合人类期望的推理链条进行思考，因为每一步都得到了精确的监督。过程监督更可能产生可解释的推理，因为它鼓励模型遵循人类认可的流程。相比之下，结果监督可能奖励一个并不符合人类期望的过程，而且通常更难以审查。

在某些情况下，更安全的 AI 系统方法可能会导致性能降低，这个成本被称为“对齐税”。一般来说，任何对齐税可能会阻碍对齐方法的采用，因为人们总是倾向于部署最强大的模型。OpenAI 研究结果显示，在数学领域，过程监督实际上导致了负对齐税。这可能会增加过程监督的采用，这会产生正面的对齐效果。

## 解决 MATH 问题

OpenAI 使用 MATH 测试集的问题来评估过程监督和结果监督奖励模型。为每个问题生成多个解决方案，然后选择由各个奖励模型排名最高的解决方案。图表显示了选择的解决方案能够达到正确最后答案的百分比，作为考虑的解决方案数量的函数。过程监督奖励模型在所有情况下的表现都优于结果监督模型，而且当考虑每个问题的更多解决方案时，性能差距会进一步扩大。这表明过程监督奖励模型更为可靠。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这里展示了三类探索示例，共 12 个问题和解决方案，并总结了奖励模型的优缺点。

> 📌 混淆矩阵
>
> 混淆矩阵（Confusion Matrix），也称为错误矩阵，可以更好地理解模型的性能，特别是模型在分类预测上的错误。并且可以基于混淆矩阵来计算其他的评估指标，如准确率（Accuracy）、召回率（Recall）、精确率（Precision）和 F1 分数等。
>
> 混淆矩阵的每一列代表了预测类别，每一行代表了实际的类别（或反之）。这就可以让我们看到系统在哪些类别上犯错，错误倾向如何。对于二分类问题，混淆矩阵通常如下所示：
>
> |
>  | 预测为正 | 预测为负 |
> | --- | --- | --- |
> | 实际为正 | 真阳性 (TP) | 假阴性 (FN) |
> | 实际为负 | 假阳性 (FP) | 真阴性 (TN) |
>
> TP、TN、FP 和 FN 是用来评估一个分类器（或预测模型）预测结果的准确性的术语。这里，真阳性（True Positives，TP）是指模型正确地预测出的正类别实例，真阴性（True Negatives，TN）是模型正确地预测出的负类别实例，假阳性（False Positives，FP）是模型错误地预测出的正类别实例，假阴性（False Negatives，FN）是模型错误地预测出的负类别实例。
>
> 在模型尝试的示例中，提到的真阳性和真阴性表示模型在解决数学问题时正确或错误地执行每个步骤，假阳性则表示模型错误地认为它正确地执行了某个步骤。
>
> ---
>
> 这些都是用来评估分类器性能的重要指标：
>
> -   准确率（Accuracy）：这是最直观的评估指标，表示分类器正确预测的样本占总样本的比例。计算公式是 (TP+TN) / (TP+TN+FP+FN)。在某些情况下，准确率可能不是一个好的衡量标准，特别是当我们的数据不平衡时，例如，一个类别的样本比另一个类别的样本多很多。
>
> -   召回率（Recall）：也称为敏感度、真阳性率或者命中率，表示的是所有正类样本中被正确预测出的比例。计算公式是 TP / (TP+FN)。
>
> -   精确率（Precision）：精确率是指预测为正的样本中实际为正的比例。计算公式是 TP / (TP+FP)。
>
> -   F1 分数：F1 分数是精确率和召回率的调和平均数，因此，F1 分数能够综合考虑精确率和召回率。当你试图找到精确率和召回率之间的平衡时，F1 分数是一个很好的指标。计算公式是 2 \* (Precision\*Recall) / (Precision+Recall)。
>
>
> 这些指标在衡量模型性能时各有优缺点，所以通常需要结合实际情况和任务需求，一起使用来评估模型的好坏。

### True positives

> 😄 示例 1
>
> 在这个具有挑战性的三角函数问题中，需要以一种并非显而易见的顺序应用几个恒等式。大部分解决方案尝试都会失败，因为选择哪些恒等式真正有帮助是困难的。尽管 GPT-4 通常无法解决这个问题（只有 *0.1%* 的解决方案尝试得出了正确答案），但奖励模型正确地认出了这个解决方案是有效的。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> 😄 示例 2
>
> 在这里，GPT-4 成功地执行了一个复杂的多项式因式分解序列。在第 5 步中使用 Sophie-Germain 恒等式是一个可能被认为是富有洞见的重要步骤。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> 😄 示例 3
>
> 在第 7 和 8 步，GPT-4 开始进行猜测和检查。这是模型可能产生幻觉的常见地方，比如声称一个特定的猜测是成功的，但实际上并非如此。在这种情况下，奖励模型验证了每一步，确定了思考链条是正确的。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> 😄 示例 4
>
> 模型成功地应用了几个三角函数恒等式来简化表达式。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### True negatives

> 😄 示例 5
>
> 在第7步，GPT-4 尝试简化一个表达式，但操作错误。奖励模型发现了这个错误。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> 😄 示例 6
>
> 在第 11 步，GPT-4 计算错误。奖励模型发现了这个错误。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> 😄 示例 7
>
> 在第 12 步，GPT-4 尝试在一个并非实际上是平方差的表达式上使用平方差公式。奖励模型发现了这个错误。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> 😄 示例 8
>
> 在第 8 步的解释中，有些奇怪，但奖励模型没有指出这个问题。然而，在第 9 步，模型错误地分解了表达式。奖励模型发现了这个错误。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### False positives

> 😄 示例 9
>
> 在第 4 步，GPT-4 错误地声称该序列每 12 项重复一次，而实际上是每 10 项重复一次。这种计数错误偶尔会欺骗奖励模型。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> 😄 示例 10
>
> 在第 13 步，GPT-4 尝试通过合并相同项来简化方程。它正确地将线性项移动并合并到左侧，但错误地保留了右侧的状态不变。奖励模型被这个错误欺骗。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> 😄 示例 11
>
> GPT-4 尝试进行长除法，但在第 16 步，它忘记在十进制重复部分包括前导零。奖励模型被这个错误欺骗。
>
> ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> 😄 示例 12
>
> 在第 9 步，GPT-4 产生了一个微妙的计数错误。表面上，宣称有 5 种方法来交换相同颜色的球，因为有 5 种颜色，看起来是合理的。然而，这样的计数方式低估了 2 倍，因为 Bob 有两种选择来决定返回给 Alice 哪个球。奖励模型被这个错误欺骗。
>
> ![图片](https://mmbiz.qpic.cn/mmbiz_png/90Kxd0FAJJd3Gia00qKdaG5xV384jUZZXjvuK7skYC3fe44CVyBNcmePa4SyzeFPsDAJjp2GibIOY6rd2F4Xv3ibA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

目前还不清楚这些结果在数学领域之外的适用性如何，OpenAI 认为未来的工作需要探索过程监督在其他领域的影响。如果这些结果可以推广，可能会发现过程监督既提高了性能又比结果监督更一致，这将为我们带来最好的两个世界。

### References

\[1\]

Let’s Verify Step by Step: *https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets\_Verify\_Step\_by\_Step.pdf*

\[2\]

Improving mathematical reasoning with process supervision: *https://openai.com/research/improving-mathematical-reasoning-with-process-supervision*

\[3\]

openai/prm800k: *https://github.com/openai/prm800k*