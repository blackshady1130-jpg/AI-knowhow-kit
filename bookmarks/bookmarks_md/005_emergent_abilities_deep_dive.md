---
url: https://yaofu.notion.site/514f4e63918749398a1a8a4c660e0d5b
title: "深入理解语言模型的突现能力"
description: "A tool that connects everyday work into one space. It gives you and your teams AI tools—search, writing, note-taking—inside an all-in-one, flexible workspace."
author: "Yao Fu"
captured_at: "2026-03-08T10:01:27.848Z"
---

# 深入理解语言模型的突现能力

爱丁堡大学 (University of Edinburgh) 博士生，本科毕业于北京大学

请同时参考CoT团队的博客。

1

英文版完稿于 2022年11月20日，中文版完稿于2022年12月24日。

其他版本: \[pdf\] \[Arxiv\] \[[英文原版](https://yaofu.notion.site/b9a57ac0fcf74f30a1ab9e3e36fa1dc1)\]

初次翻译，哪里没写好，不地道的地方，还请邮件帮忙指出

转发请在文章的开头标明出处，而不是在结尾列一行小字

注：本文完成于 ChatGPT 上线之前的一个月，当时我意识到大模型非同小可，所以写下本文，希望引起更多人关注到大模型有可能带来的研究范式转变。一个月之后，ChatGPT 上线，全网轰动，范式从此转变。

最近，人们对大型语言模型所展示的强大能力（例如思维链、[便签本](https://lingo.csail.mit.edu/blog/arithmetic_gpt3/)）产生了极大的兴趣，并开展了许多工作。我们将之统称为大模型的突现能力，这些能力可能只存在于大型模型中，而不存在于较小的模型中，因此称为“突现”。其中许多能力都非常令人印象深刻，比如复杂推理、知识推理和分布外鲁棒性，我们将在后面详细讨论。值得注意的是，这些能力很接近 NLP 社区几十年来一直寻求的能力，因此代表了一种潜在的研究范式转变，即从微调小模型到使用大模型进行上下文学习。对于先行者来说，范式转变可能是很显然的。然而，出于科学的严谨性，我们确实需要非常明确的理由来说明为什么人们应该转向大型语言模型，即使这些模型昂贵、难以使用，并且效果可能一般。在本文中，我们将仔细研究这些能力是什么，大型语言模型可以提供什么，以及它们在更广泛的 NLP / ML 任务中的潜在优势是什么。

6

Recently, there has been great interest and progress in showing great abilities in large language models (chain of thought, [scratch pad](https://lingo.csail.mit.edu/blog/arithmetic_gpt3/)). Collectively referred to as emergent abilities of large language models, these are abilities likely to only exist in large models but not in smaller ones, hence the “emergence” framing. Many of the abilities are quite impressive, like complex reasoning, reasoning with knowledge, and out-of-distribution robustness, as we will look closely below. These abilities are potentially close to what the NLP community have urged for decades, thus representing a potential research paradigm shift from fine-tuning small models to in-context learning with large models. For pioneers, the paradigm shift may be straightforward without the need for justification. Yet, for scientific rigor, we do need very explicit reasons why one should shift to large language models, which are expensive, hard to access, and potentially not as good. In this post, we will scrutinize what these abilities are, what large language models may deliver, and what are their potential advantages in a broader NLP/ ML context.

目录

前提：我们假设读者具备以下知识：

预训练、精调、提示（普通从业者应具备的自然语言处理/深度学习能力）

思维链提示、便签本（普通从业者可能不太了解，但不影响阅读）

Prerequisites: we assume the readers have the following knowledge:

Pretraining, fine-tuning, prompting (average Natural Language Processing / Deep Learning practitioners should know).

Chain-of-thought prompting / scratch pad (maybe less known by average practitioners, but it should be OK to read without knowing them in advance)

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbaa9181c-640a-4ca2-acfd-3641a0bb0b7b%2FUntitled.png?table=block&id=61e70dab-956c-43d5-961e-3b7cedd57cc7&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1060&userId=&cache=v2)

图片来自于 Wei. et. al. 2022. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models。X 轴为模型大小。GSM8K是是一个小学水平的数学问题集。

在以上的效果图中，我们可以观察到模型的表现：

当尺寸相对小的时候提升并不大

当模型变大时有很明显的提升

这从根本上说明，某些能力可能不存在于小模型中，而是在大模型中获得的。

In the above performance figure, we observe that the model performance:

does not increase much when the model size is relatively small

significantly increase when the model becomes large

This indicates fundamentally, certain abilities may not be in small models but may be obtained by large models.

有很多种突现能力，比如 Wei 等人在 2022年 所梳理的。有些能力很有意思，但我们在本文不会讨论，比如把一串单词的最后一个字母拼起来，我们认为这是 Python 而不是语言模型要做的任务；或者3位数加法，我们认为这是计算器而不是语言模型要做的事。

1

There are many emergent abilities, as summarized by Wei et. al. 2022. Certain abilities are fun, but we are not interested, for example, last latter concatenation, as we believe that’s the task for Python but not for language models, or 3-digit addition, as we believe that’s the task for a calculator but not for language models.

在本文中，我们主要对以下能力感兴趣：

NLP 社区近几年都关注，但之前的 NLP 模型很难达到的能力

源自于人类语言最深层的本质的能力（能力的深度）

可能达到人类智力的最高水平的能力（能力的上限）

The abilities that we are interested in are the abilities (1) that the NLP community have urged for years but have yet to come, (2) that all previous NLP models struggle with, (3) that root from the deepest nature of human language, and (4) that potentially reach the highest level of human intelligence.

很多有意思的能力都可以归到上文提到的类别里，在它们之中，我们主要讨论以下三种典型能力：

复杂推理

知识推理

分布外鲁棒性

接下来让我们一个个详细讨论。

Many interesting abilities fall into the above-mentioned categories. Among them, we consider the following three typical abilities:

Complex Reasoning

Reasoning with Knowledge

Out-of-distribution robustness

Now we take a close look at them one by one.

下面是一个 GSM8K 数据集中，用提示词显著超过精调的例子：

问题： 克莱儿每天早饭都用 3 颗蛋做蛋卷，她 4 周会吃掉多少打鸡蛋？ 克莱儿每天早饭都用3颗蛋做蛋卷。 一周有 7 天。 所以她一周会吃 3 \* 7 \= 21 颗蛋。 她4周会吃掉 4 \* 21 \= 84 颗蛋。 一打里面是 12 颗蛋。 所以 84 / 12 \= 7。 答案是7。

​

虽然这道题对于10岁的孩子来说很容易，但对语言模型来说却很难，主要是由于数学和语言混合在一起。

GSM8K 最初由 OpenAI 于 2021 年 10 月提出。当时他们用第一版GPT3在全部训练集上进行了精调，准确率约为 35%。这个结果让作者相当悲观，因为他们的结果显示了语言模型的缩放规律：随着模型大小呈指数增长，性能呈线性增长（我之后会讨论）。因此，他们在第 4.1 节中思考：

2

> “175B 模型似乎需要至少额外两个数量级的训练数据才能达到 80% 的求解率。”

三个月后，即 2022 年 1 月，Wei 等人基于 540B PaLM 模型，仅使用了 8 个思维链提示示例便将准确率提高到 56.6%（无需将训练集增加两个数量级）。之后在 2022 年 3 月，Wang 等人基于相同的 540B PaLM 模型，通过多数投票的方法将准确率提高到 74.4%。当前的 SOTA 来自我自己在 AI2 的工作（Fu et. al. Nov 2022），我们通过使用复杂的思维链在 175B Codex 上实现了 82.9% 的准确率。从以上进展可以看到，技术进步确实呈指数级增长。

3

思维链提示是一个展示模型随着规模突现出能力的典型例子：

从突现能力来看：模型大小确实要大于 100B ，才能使思维链的效果大于的仅有回答提示。所以这种能力只存在于大型模型中。

从效果来看：思想链提示的性能明显优于其之前的精调方法。

1

从标注效率上来看：思维链提示只需要 8 个示例的注释，而微调需要完整的训练集。

有些同学可能会认为模型能做小学数学代表不了什么（从某种意义上说，他们确实没有那么酷）。但 GSM8K 只是一个开始，最近的工作已经把前沿问题推向了高中、大学，甚至是国际数学奥林匹克问题。现在更酷了吗？

3

This is an example where prompting significantly outperforms fine-tuning. We start from a quick first example from GSM8K:

Question: Claire makes a 3 egg omelet every morning for breakfast. How many dozens of eggs will she eat in 4 weeks? Claire makes a 3 egg omelet every morning. There are 7 days in a week. So in one week she will eat 3 \* 7 = 21 eggs. In 4 weeks she will eat 4 \* 21 = 84 eggs. There are 12 eggs in a dozen. So 84 / 12 = 7. The answer is 7.

​

Although this is simple for a 10-year-old, it is nontrivial for a language model to solve, largely due to the mixture of math and language.

GSM8K was originally proposed by OpenAI in Oct 2021. At that time, they fine-tuned the first version of GPT3 with a verifier on the full training set, and the accuracy was about 35%. The authors were rather pessimistic because their results show a scaling law of language models: the performance increase linearly as the model size increases exponentially (I will get back to this later). Consequently, they ponder in their Section 4.1:

> “it appears likely that the 175B model would require at least two additional orders of magnitude of training data to reach an 80% solve rate.”

Note that two additional orders of magnitude would be 17500B. How many years would you think this should take?

Three months later, In Jan 2022, with a 540B PaLM model, Wei et. al. pushed the accuracy to 56.6% within only 8 chain-of-thought prompt examples (no need to fine-tune on the full training set). Then in Mar 2022, with the same 540B PaLM model, Wang et. al. improved the number to 74.4% by majority voting. The current SOTA performance is from my own work at AI2 (Fu et. al. Nov 2022), where we achieve 82.9% accuracy with the 175B Codex by using complex chains of thought. Technology improvement is indeed exponential.

Chain-of-thought prompting is a very typical example showing the emergence with scale:

Emergence: although 17500B is not required, the model size indeed has to be larger than 100B for chain-of-thought to outperform standard answer-only prompting. So the ability only exists in large models.

Performance: the performance of chain-of-thought prompting is significantly better than its previous fine-tuning methods.

Annotation Efficiency: chain-of-thought prompting only require annotations of 8 examples, while fine-tuning takes the full training set.

One may argue that primary school math is still not meaningful (in a sense, they are indeed not so cool). But GSM8K is just the beginning, recent works have pushed the frontier to high school, college, and even International Mathematical Olympiad problems. Cooler now?

下一个例子是需要知识的推理能力（例如问答和常识推理）。在这种情况下，对大型模型进行提示不一定优于精调小型模型（哪个模型更好还有待观察）。但是这个情况下的注释效率被放大了，因为：

在许多数据集中，为了获得所需的背景/常识知识，（以前很小的）模型需要一个外部语料库/知识图谱来检索，或者需要通过多任务学习在增强的数据上进行训练

2

对于大型语言模型，可以直接去掉检索器，仅依赖模型的内部知识，且无需精调

2

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff79bc38f-5721-4c02-a1c7-1ca518e4b9a4%2FUntitled.png?table=block&id=8cc32585-ba7f-4b38-9674-323b695f1f87&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

图片来自于 Yu et. al. 2022. 以前的 SOTA 模型需要从外部知识源中检索。 GPT-3 的性能与以前的模型相当/优于以前的模型，且无需检索。

如表中所示，与数学题的例子不同，GPT-3 并没有明显优于之前的精调模型。但它不需要从外部文档中检索，本身就包含了知识。

1

The next example we look at is reasoning that requires knowledge (e.g., question-answering and commonsense reasoning). In this setting, prompting large models does not necessarily outperform fine-tuning small models (which one gives a better score is yet to see). But the annotation efficiency in this setting is amplified, because:

in many datasets, to obtain the required background/ commonsense knowledge, the (previously small) model needs an external corpora/ knowledge graph to retrieve from or needs to be trained on augmented data with multi-task learning

with a large language model, it is possible that one directly drops the retriever and only relies on the internal knowledge from the model, and again, without tuning

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff79bc38f-5721-4c02-a1c7-1ca518e4b9a4%2FUntitled.png?table=block&id=8e6070af-d923-4649-9f12-5832e043a270&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Figure from Yu et. al. 2022. Previous SOTA models require retrieving from outside knowledge sources. GPT-3 performs on par with/outperforms previous models without needing to retrieve.

As is shown in the table, unlike the math case, GPT-3 does not significantly outperform previous fine-tuned models. But it does not require the retrieval from external documents because it contains the knowledge within itself.

为了理解这些结果的重要性，我们可以回顾一下历史：NLP 社区从一开始就面临着如何有效编码知识的挑战。人们一直在不断探究把知识保存在模型外部或者内部的方法。上世纪九十年代以来，人们一直试图将语言和世界的规则记录到一个巨大的图书馆中，将知识存储在模型之外。但这是十分困难的，毕竟我们无法穷举所有规则。因此，研究人员开始构建特定领域的知识库，来存储非结构化文本、半结构化（如维基百科）或完全结构化（如知识图谱）等形式的知识。通常，结构化知识很难构建（因为要设计知识的结构体系），但易于推理（因为有体系结构），非结构化知识易于构建（直接存起来就行），但很难用于推理（没有体系结构）。然而，语言模型提供了一种新的方法，可以轻松地从非结构化文本中提取知识，并在不需要预定义模式的情况下有效地根据知识进行推理。下表为优缺点对比：

<table><tbody><tr><td dir="ltr"></td><td dir="ltr"><div><p>构建</p></div></td><td dir="ltr"><div><p>推理</p></div></td></tr><tr><td dir="ltr"><div><p>结构化知识</p></div></td><td dir="ltr"><div><p>难构建 需要设计体系结构并解析</p></div></td><td dir="ltr"><div><p>容易推理 有用的结构已经定义好了</p></div></td></tr><tr><td dir="ltr"><div><p>非结构化知识</p></div></td><td dir="ltr"><div><p>容易构建 只存储文本即可</p></div></td><td dir="ltr"><div><p>难推理 需要抽取有用的结构</p></div></td></tr><tr><td dir="ltr"><div><p>语言模型</p></div></td><td dir="ltr"><div><p>容易构建 在非结构化文本上训练</p></div></td><td dir="ltr"><div><p>容易推理 使用提示词即可</p></div></td></tr></tbody></table>

To understand the significance of these results, we need a bit of historical note: the NLP community have been facing the challenge of efficiently encoding knowledge since the very beginning. Knowledge should be stored somewhere anyway, either within or outside the model. Since the 90s, people have been trying to store knowledge outside the model by handwriting all the rules of language and the world into a gigantic library. Yet this later turned out to be extremely hard because one simply cannot enumerate every single rule of the world. So instead of writing all possible rules, researchers retreat back to domain-specific libraries of knowledge that are useful. This domain-specific knowledge can be unstructured text, semi-structured like Wikipedia, or fully structured like knowledge graphs. Usually, structured knowledge is hard to construct (because one needs to design the schema) but easy to reason with (because there are structures), unstructured knowledge is easy to construct (one just stores them) but hard to reason with (there are no structures ready to use). Language models, given this context, provide a way to simultaneously extract knowledge easily from unstructured text and reasoning upon the knowledge effectively without the need for a predefined schema. The table below shows the comparison of pros and cons:

<table><tbody><tr><td dir="ltr"></td><td dir="ltr"><div><p>Construction</p></div></td><td dir="ltr"><div><p>Reasoning</p></div></td></tr><tr><td dir="ltr"><div><p>structured knowledge</p></div></td><td dir="ltr"><div><p>hard to construct need to design schema and parse</p></div></td><td dir="ltr"><div><p>easy to reason useful structures already defined</p></div></td></tr><tr><td dir="ltr"><div><p>unstructured knowledge</p></div></td><td dir="ltr"><div><p>easy to construct just store the text</p></div></td><td dir="ltr"><div><p>hard to reason need to extract useful structures</p></div></td></tr><tr><td dir="ltr"><div><p>large language model</p></div></td><td dir="ltr"><div><p>easy to construct trained on unstructured text</p></div></td><td dir="ltr"><div><p>easy to reason just prompt</p></div></td></tr></tbody></table>

我们讨论的第三种能力是分布外的鲁棒性。在 2018 年至 2022 年期间，NLP、CV 和通用机器学习领域有大量关于分布偏移/对抗鲁棒性/组合生成的研究，人们发现当测试集分布与训练分布不同时，模型的行为性能可能会显著下降。然而，在大型语言模型的上下文学习中似乎并非如此。Si 等人在2022年的研究显示：

1

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe09b6739-81b5-46e9-b8c3-f84076402047%2FUntitled.png?table=block&id=35a123f5-909d-406f-a546-b1434cf34ded&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

数据来自于 Si et. al. 2022. 虽然 GPT-3 在同分布设置下比 RoBERTa 要差，但在非同分布设置下优于 RoBERTa，性能下降明显更小。

同样，在此实验中，同分布情况下基于提示词的 GPT-3 的效果并没有精调后的 RoBERTa要好。但它在三个其他分布（领域切换、噪声和对抗性扰动）中优于 RoBERTa，这意味着 GPT3 更加鲁棒。

The third ability that we discuss is out-of-distribution robustness. During 2018 - 2022, quite a lot of research across NLP, CV, and general machine learning, under the name of distribution shift/ adversarial robustness/ compositional generation, observed the behavior that when the test set distribution is different than the training distribution, model performance may drop significantly. Yet this seems not to be the case for large language models’ in-context learning. A quick experimental result is from Si et. al. 2022:

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe09b6739-81b5-46e9-b8c3-f84076402047%2FUntitled.png?table=block&id=26ef1658-bbcc-4ccd-a9f0-0ddc52dc4846&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Table from Si et. al. 2022. Although GPT-3 cannot outperform RoBERTa in the in-distribution setting, it outperforms RoBERTa in the out-of-distribution setting with a significantly smaller performance drop.

Again, in this setting, prompting GPT-3 does not outperform the fine-tuned RoBERTa in the in-distribution setting. But it outperforms RoBERTa in three out-of-distribution (domain shift, noisy and adversarial perturbation) settings, meaning that it is more robust.

此外，即使存在分布偏移，好的提示词所带来的泛化性能依旧会继续保持。比如：

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbbc93ed3-2cdf-4d49-b593-5e01b48c4df4%2FUntitled.png?table=block&id=15946f9b-b1e7-4cf6-9f6c-2b98589036a5&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

图片来自于 Fu et. al. 2022. 即使测试分布与训练分布不同，复杂提示也始终比简单提示的表现更好。

Fu 等人2022年的研究显示，输入提示越复杂，模型的性能就越好。这种趋势在分布转移的情况下也会继续保持：无论测试分布与原分布不同、来自于噪声分布，或者是从另一个分布转移而来的，复杂提示始终优于简单提示。

1

Furthermore, certain good generalization behaviors of prompting can be consistent even if there is a distribution shift. For example:

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbbc93ed3-2cdf-4d49-b593-5e01b48c4df4%2FUntitled.png?table=block&id=288ca82b-f230-4e74-bc01-c840ad23fe4a&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Figure from Fu et. al. 2022. Complex prompts consistently induce better performance than simple prompts, even when the test distribution is different from the training distribution.

In Fu et. al. 2022, we observe that the more complex the input prompt is, the better performance the model gives. This trend the consistent under distribution shift: no matter whether the test distribution is the same as the prompt distribution or is a noisy distribution, or the prompt is transferred from another distribution, complex prompts consistently outperforms simple prompts.

在上文中，我讨论了只有大型模型才有的三种突现能力。它们是：

复杂推理，大型模型在没有使用全部训练数据的情况下便显著优于以前的小型模型。

知识推理，大型模型可能没有小模型效果好，但大模型不需要额外的知识来源（知识可能很昂贵，或者很难从非结构化数据中抽取）。

分布外鲁棒性，这是之前进行模型精调时需要努力解决的问题。大型模型虽然在同分布情况下的效果不如以前的方法，但非同分布情况下的泛化性能却好得多。

We have discussed three emergent abilities that potentially only large models have. They are:

Complex reasoning, where large models significantly outperform previous smaller models without the need for full-dataset training.

Reasoning with knowledge, where large models may not outperform previous smaller models, but do not require the additional source of knowledge (which can be expensive to obtain or hard to extract from unstructured data).

Out-of-distribution Robustness, where most previous fine-tuned models struggle. Here large models may still not outperform previous methods in the in-distribution setting, but they seem to be much better in the out-of-distribution setting.

鉴于上文列出的优点，大家可能会开始觉得大型语言模型确实很好了。在进一步讨论之前，让我们再回顾一下之前的工作，就会发现一个很奇怪的问题：GPT-3 在 2020 年就发布了，但为什么直到现在我们才发现并开始思考范式的转变？

这个问题的答案就藏在两种曲线中：对数线性曲线和相变曲线。如下图：

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbe187b59-ec07-4b95-8999-c0245c698ec8%2FUntitled.png?table=block&id=9d924e0f-46e7-4838-94c3-e6caf713dbf4&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

左图: 比例定律. 当模型大小呈指数增长时，相应的模型性能呈线性增长。右图: 当模型尺寸达到一定规模时，会出现突现能力，让性能急剧增加。

最初，（OpenAI）的研究者认为语言模型的性能与模型尺寸的关系可以通过对数线性曲线预测，即模型尺寸呈指数增长时，性能会随之线性增加。这种现象被称为语言模型的缩放定律，正如 Kaplan 等人在2020年最初的GPT3文章中讨论的那样。重要的是，在那个阶段，即便最大的 GPT-3 在有提示的情况下也不能胜过小模型精调。所以当时并没有必要去使用昂贵的大模型（即使提示词的标注效率很高）。直到2021年，Cobbe 等人发现缩放定律同样适用于精调。这是一个有点悲观的发现，因为它意味着我们可能被锁定在模型规模上——虽然模型架构优化可能会在一定程度上提高模型性能，但效果仍会被锁定在一个区间内（对应模型规模），很难有更显著的突破。

3

在缩放定律的掌控下（2020年到2021），由于GPT-3无法胜过精调 T5-11B，同时T5-11B微调已经很麻烦了，所以NLP社区的关注点更多的是研究更小的模型或者高效参数适应。Prefix tuning就是提示和适应交叉的一个例子，后来由 He 等人在 2021统一。当时的逻辑很简单：如果精调效果更好，我们就应该在高效参数适应上多下功夫；如果提示词的方法更好，我们应该在训练大型语言模型上投入更多精力。

2

之后在 2022 年 1 月，思维链的工作被放出来了。正如作者所展示的那样，思维链提示在性能-比例曲线中表现出明显的相变。当模型尺寸足够大时，性能会显著提高并明显超越比例曲线。

当使用思维链进行提示时，大模型在复杂推理上的表现明显优于微调，在知识推理上的表现也很有竞争力，并且分布鲁棒性也存在一定的潜力。要达到这样的效果只需要8个左右的示例，这就是为什么范式可能会转变（注：本文完成于 ChatGPT 上线之前的一个月；在 ChatGPT 上线之后，整个领域为之震撼，意识到范式已经转变了）。

Given the above advantages, one may start to feel large language models are indeed very good. Before going into further discussions, let’s take a step back and look a little bit more at the literature. One curious question is that GPT-3 was released in 2020; why is it until now we are interested and start to think if the paradigm is shifting?

The answer traces back to two different types of scaling curves: the log-linear curve and the phase change curve. As is shown below:

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbe187b59-ec07-4b95-8999-c0245c698ec8%2FUntitled.png?table=block&id=a45617be-8197-4a02-9404-58c15f738d43&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Left: scaling law. Model performance increases linearly as the model size increases exponentially. Right: emergent abilities show a phase change at a certain scale where the performance suddenly increases.

Initially, (OpenAI) people believed that the performance of language models w.r.t. model size can be predicted by a log-linear curve, where the performance increase linearly as the model size increase exponentially. This behavior is called the scaling law of language models, as is initially discussed in Kaplan et. al. 2020 then observed in GPT-3 Original paper. Importantly, at this stage, prompting even the largest GPT-3 cannot outperform fine-tuning smaller models. This cast the question of why bother using so large expensive models (even prompting is annotation-efficient). Later in Cobbe et. al. 2021, the scaling law seems also to apply to fine-tuning. This is rather pessimistic because it implies that we are maybe locked to our model scale — different tweaks of model architectures may improve the model performance to a certain extent, but still, we seem to be locked in its corresponding scale range and cannot have a significant performance breakthrough.

During the age of scaling law (2020 - 2021), since GPT-3 cannot outperform fine-tuning T5-11B, and T5-11B is already troublesome to fine-tune, the community’s focus is more on prompting smaller models or parameter-efficient adaptation. Prefix tuning is one notable example in the intersection between prompting and adaptation, which was later partially unified by He et. al. 2021. The logic of our bets is simple: if fine-tuning is better, we should put more effort into parameter-efficient tuning; if prompting is better, we should put more effort into training large language models.

Later in Jan 2022, chain-of-thought comes out, and the story begins. As is shown by the authors, chain-of-thought prompting exhibits a clear phase change in the performance-scale curve. When the model size is large enough, the performance increases significantly and clearly transcends the scale curve.

When prompted within chain-of-thought, we get significantly better performance than fine-tuning on complex reasoning, also competitive performance on reasoning with knowledge, and there is a further potential of distributional robustness. All these advantages only require about 8 in-context examples. This is why the paradigm may shift.

范式转变究竟意味着什么？下面我们给出精调和提示词方法的对比：

<table><tbody><tr><td dir="ltr"><div><p>模型规模</p></div></td><td dir="ltr"><div><p>小模型</p></div></td><td dir="ltr"><div><p>大模型</p></div></td></tr><tr><td dir="ltr"><div><p>学习方法</p></div></td><td dir="ltr"><div><p>微调</p></div></td><td dir="ltr"><div><p>上下文学习</p></div></td></tr><tr><td dir="ltr"><div><p>学习范式</p></div></td><td dir="ltr"><div><p>监督学习</p></div></td><td dir="ltr"><div><p>监督学习？？</p></div></td></tr><tr><td dir="ltr"><div><p>数据</p></div></td><td dir="ltr"><div><p>完整训练数据集</p></div></td><td dir="ltr"><div><p>少量上下文学习样本</p></div></td></tr><tr><td dir="ltr"><div><p>泛化</p></div></td><td dir="ltr"><div><p>分布内泛化</p></div></td><td dir="ltr"><div><p>同时泛化到分布内 + 分布迁移</p></div></td></tr></tbody></table>

提示词的好处很明显：我们不再需要繁琐的数据标注和在全量数据上进行精调，只需要编写提示词并获得满足要求的结果，这比精调要快很多。

另外要注意的两点是：

上下文学习是监督学习吗？

坦白讲，我不确定。

相似之处在于，上下文学习也需要像训练数据一样的示例

不同之处在于，上下文学习的泛化行为并不同于监督学习，这使得之前的泛化理论（例如 Rademancher Complexity 或 Neural Tangent Kernel）均不适用。

上下文学习真的比监督学习效果要好吗？

答案还未知。

大多数提示词和精调的对比都只比了 提示词+大模型 vs 精调+小模型，但公平的对比应该是 提示词+大模型 vs 精调+大模型，且对比时的基座模型应该一样。所以在最初的思维链文章中，如果 Wei 等人要说明提示词好于精调，他们应该对比精调后的PaLM，而不是GPT3。

我的假设是：精调可以提高分布内的性能，但会损害分布外的鲁棒性。提示词在分布变化的场景中表现更好，但在同分布场景下不如精调。

如果假设是真的，那么一个值得研究的问题就是如何在不牺牲其上下文学习能力的情况下进行精调

注意分布外精调的效果同样会随着模型尺寸变化。比如 Yang 等人在2022年的工作中，第四张表就显示，Bart-based的分布外泛化能力会下降，但Bart-large则提升。对于大模型，当测试集的分布和训练集相差不大时，同分布的精调效果也应该会提升。

再回顾一下前文提到的的逻辑：如果精调更好，我们应该努力研究如何进行参数高效的优化；如果提示词更好，我们应该努力去训练更好的大型语言模型。

所以，尽管我们相信大型语言模型有巨大的潜力，仍然没有确凿的证据表明精调和提示词哪种方法更好，因此我们不确定范式是否真的应该转变、或应该转变到什么程度。仔细比较这两种范式，使我们对未来有一个清晰的认识，是非常有意义的。我们将更多讨论留到下一篇文章。

What does paradigm shift mean exactly? Below we give a comparison between fine-tuning and prompting:

The advantage is very clear: we no longer need the cumbersome data annotation and full-set fine-tuning. We only need to write prompts and get at least good enough results, which is substantially faster than fine-tuning.

Two more things to note:

Is in-context learning still supervised learning?

I don’t know.

They are similar in the sense that in-context learning also needs demonstrations that are conceptually similar to training data.

They are different in the sense that in-context learning’s generalization behavior is systematically different than supervised learning, making none of the previous generalization theories (e.g., Rademancher Complexity or Neural Tangent Kernel) apply.

Is in-context learning really better than fine-tuning?

The answer is not known.

Most existing comparisons between prompting v.s. fine-tuning is prompting + large model v.s. fine-tuning + small model. A fair comparison should be prompting + large model v.s. fine-tuning + large model. Also, the fine-tuned large model should be the same as the prompted large model. So in the original CoT paper, if Wei. et. al. really claim that prompting is better than fine-tuning; they should have the fine-tuned performance from PaLM, rather than reporting the number from GPT-3.

My hypothesis: fine-tuning will improve in-distribution performance, but hurt out-of-distribution robustness. Prompting will be better in the distribution shift setting, but worse in the in-distribution setting.

If this is true, then a straightforward research problem is how to fine-tune the model without sacrificing its in-context learning ability

Note that the OOD generalization of fine-tuning will also change with the model scale. As a quick example, Yang et. al. 2022, Table 4 shows that Bart-based finetuning decreases OOD generalization, but Bart-large finetuning improves OOD generalization. It is totally possible that with large models, fine-tuning may also improve performance in distribution shift settings if the test distribution is related/ not far away from the training distribution.

Again, recall the simple logic: if fine-tuning is better, we should put efforts into parameter-efficient tuning; if prompting is better, we should put efforts into getting better large language models.

So, although we believe that large language models exhibit great potential. There is still no hard evidence showing if one is absolutely better than the other, so we do not know if the paradigm should really shift or to what extent it should shift. It would be very meaningful to compare the two paradigms carefully such that we have a clear picture of the future. We leave more discussions to our next post.

两个数字：62B 和 175B。

模型至少需要62B，使思维链的效果才能大于标准的提示词方法。

模型至少需要175B（GPT3的尺寸），思维链的效果才能大于精调小模型（T5 11B）的效果。

62B这个数字来自于 Chung 等人 2022 年工作的第五张表：

1

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe954a643-4318-4c4e-a500-b92f49ce6b82%2FUntitled.png?table=block&id=b23c9e80-f552-4d99-84c1-66fc5c95835e&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

对于所有小于62B的模型，直接用提示词都好于思维链。第一个用思维链更好的模型是 Flan-cont-PaLM 62B 在BBH上的结果。540B的模型使用思维链会在更多任务上得到好的效果，但也不是全部任务都好于精调。另外，理想的尺寸可以小于 540B，在 Suzgun 等人2022年的工作中，作者展示了175B的 InstructGPT 和 175B的 Codex 使用思维链都好于直接用提示词。综合以上结果，我们得到了63B和175B两个数字。所以，如果想要参与这场游戏，首先要有一个大于平均尺寸的模型。

1

不过，还有其他大型模型在思维链下的表现差了很多，甚至不能学到思维链，比如 OPT、BLOOM 和 GPT-3 的第一个版本。他们的尺寸都是175B。这就引出了我们下一个要讨论的问题。

1

The quick answer is two numbers: 62B and 175B.

For chain-of-thought to be better than standard answer-only prompting, one needs the model to be at least 62B

For chain-of-thought to be better than fine-tuning small models (say T5-11B), one needs the model to be larger than 175B where the number 175B comes from GPT-3.

The number 62B is from Chung et. al. 2022 Table 5.

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe954a643-4318-4c4e-a500-b92f49ce6b82%2FUntitled.png?table=block&id=a8a909c1-5638-4ef4-9558-4d5996583c69&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

For all models smaller than 62B, direct prompting outperforms CoT. The first model where CoT outperforms direct prompting is Flan-cont-PaLM 62B on BBH. For 540B models, there are more settings where CoT outperforms direct prompting, but not all of them. Also, the number can be smaller than 540B. In Suzgun et. al. 2022, the authors show that the 175B InstructGPT and 175B Codex also have better CoT performance than direct prompting. Combining all the results, we get the two numbers 62B and 175B. So yes indeed, to enter the game of scale you do need a ticket to larger models than average.

However, there are also other large models like OPT, BLOOM, and the first version of GPT-3. They all have 175B, yet their CoT performance is significantly worse, or even cannot do CoT. This naturally leads to our next question.

不是。

规模是一个必要但不充分的因素。有些模型足够大（比如 OPT 和 BLOOM，都是 175B），但并不能做思维链。

有两种模型可以做思维链:

1

GPT3系列的模型，包括 text-davinci-002 和 code-davinci-002 (Codex)。这是仅有的两个具有强大突现能力并可公开访问的模型。

除了以上两个模型，其他GPT3模型，包括原来的GPT3，text-davinci-001，以及其他更小的GPT-3模型，都不能做思维链。

当说“能做思维链”时，我们是指使用思维链方法的效果比直接用提示词、精调T5-11B效果更好。

另外要注意的是，code-davinci-002 在语言任务上的性能始终优于 text-davinci-002。这个观察非常有趣且耐人寻味。这表明基于代码数据训练的语言模型可以胜过根据语言训练的语言模型。目前为止我们还不知道是为什么。

1

PaLM系列模型，包括 PaLM、U-PaLM、Flan-PaLM 和 Minerva。这些模型目前还未开放访问（此处@谷歌，快开源吧）。

为什么会有突现能力目前还不清楚，但我们找出了一下可能产生突现能力的因素：

1

指令精调：GPT-3 text-davinci-002 就是用指令+强化学习精调的产物。在这之前，text-davinci-001 做思维链的效果并不好。同时PaLM在经过指令精调后的效果也有提升。

3

在代码上精调：Codex code-davinci-002 是在代码上进行精调的，它的效果持续好于 text-davinci-002。PaLM 也在代码上进行了调整。从表面上看，代码与语言关系不大，但似乎起了很大作用，我们会在之后的文章进行讨论。

1

用思维链精调：在 text-davinci-002 发布时，谷歌已经发布 PaLM 3 个月了。所以 OpenAI 应该看到了思维链相关的工作。还有一些工作表明，直接用思维链数据进行精调可以激发模型的思维链能力。

1

然而，所有这些因素在现阶段都是推测。揭示如何训练才能让模型产生突现能力是非常有意义的，我们将更多讨论留到下一篇文章。

1

No.

Scale is a necessary but not sufficient factor. There are models that are large enough, like OPT and BLOOM, both 175B, but cannot do CoT.

There are only two model families that fully do CoT (TODO: add discussions about UL2):

GPT-3 models including text-davinci-002 and code-davinci-002 (Codex). These are the only two publicly accessible models that have strong emergence

Other than the above two models, other GPT-3 models, including the original GPT3, text-davinci-001, and other smaller GPT-3 models, none of them can do CoT

By “can do CoT”, we mean CoT performance being better than: (a). direct prompting (b). fine-tuning T5-11B

Also, note that code-davinci-002’s performance is consistently better than text-davinci-002 on language tasks by a large margin. This observation is quite interesting and intriguing. It means a language model tuned on code can outperform a language model tuned on language. We do not know why.

PaLM models, including PaLM, U-PaLM, Flan-PaLM, and Minerva. These models are not accessible to the general public. (@Google, Please release more checkpoints!!)

The source of emergence is still unclear. Yet we identify the following factors/ indicators that may also contribute to emergent abilities:

Instruction tuning: GPT-3 text-davinci-002 is instruction-tuned with reinforcement learning. Before that, text-davinci-001 could not do CoT well. It seems that PaLM is not instruction-tuned, but later Google does, and the performance increases.

Tuning on code: Codex code-davinci-002, tuned on code, is consistently better than text-davinci-002. PaLM is also tuned on code. Code superficially has little to do with language, yet we don’t know why they help. But it seems that code is very helpful.

Tuning on chain-of-thought: by the time text-davinci-002 was released, Google has already released PaLM for 3 months. So OpenAI should have information about the chain-of-thought. Also there are works showing directing tuning on CoT data can enable the model’s CoT ability.

Yet all these factors are conjectures at the current stage. It would be very meaningful to unveil the recipe for training the model to unlock emergent abilities. We leave more discussions to our next post.

在本文中，我们仔细研究了语言模型的突现能力。我们强调了复杂推理、知识推理和分布外鲁棒性的重要性和其中存在的机会。突现能力是非常令人兴奋的，因为它们可以超越比例定律，并在比例曲线中表现出相变。我们详细讨论了研究范式是否会真的从精调转向上下文学习，但我们目前还没有确切答案，因为精调和上下文学习在分布内、分布外场景下的效果仍有待对比。最后，我们讨论了产生突现能力的三个潜在因素：指令精调、代码精调和思维链精调。非常欢迎大家提出建议和讨论。

另外我们还提到了两个尚未讨论的有趣问题：

我们是否能公平对比精调和上下文学习的效果？

我们是如何训练大模型，才能让模型具备突现能力、思维链能力？

对于这两个问题，我们会在之后的文章中进行讨论。

2

In this article, we scrutinize the emergent abilities of language models. We emphasize the importance and opportunities with complex reasoning, reasoning with knowledge, and distributional robustness. Emergent abilities are promising and exciting because they transcend the scaling law and exhibit a phase change in the scaling curve. We carefully discuss whether the research paradigm is actually shifting from fine-tuning to in-context learning, and our answer for that is not yet because we are still not sure about the performance comparison between fine-tuning and in-context learning in in-distribution and out-of-distribution settings. Finally, we discuss three potential factors that lead to emergent abilities: instruction-tuning, tuning on code, and tuning on chain-of-thought. We very much welcome comments, suggestions, and discussions.

There are two more interesting questions we mentioned but have not throughly discussed yet:

Can we set up a face-to-face battle between fine-tuning v.s. in-context learning?

Can we come up with a recipe of training, such that as long as one follow the recipe, one is guaranteed to get the emergent, or at least CoT ability?

We leave these two questions to our next posts.

1

<table><tbody><tr><td dir="ltr"><div><p>英文</p></div></td><td dir="ltr"><div><p>中文</p></div></td><td dir="ltr"><div><p>释义</p></div></td></tr><tr><td dir="ltr"><div><p>Emergent Ability</p></div></td><td dir="ltr"><div><p>突现能力</p></div></td><td dir="ltr"><div><p>小模型没有，只在模型大到一定程度才会出现的能力</p></div></td></tr><tr><td dir="ltr"><div><p>Prompt</p></div></td><td dir="ltr"><div><p>提示词</p></div></td><td dir="ltr"><div><p>把 prompt 输入给大模型，大模型给出 completion</p></div></td></tr><tr><td dir="ltr"><div><p>In-Context Learning</p></div></td><td dir="ltr"><div><p>上下文学习</p></div></td><td dir="ltr"><div><p>在 prompt 里面写几个例子，模型就可以照着这些例子做生成</p></div></td></tr><tr><td dir="ltr"><div><p>Chain-of-Thought</p></div></td><td dir="ltr"><div><p>思维链</p></div></td><td dir="ltr"><div><p>在写 prompt 的时候，不仅给出结果，还要一步一步地写结果是怎么推出来的</p></div></td></tr><tr><td dir="ltr"><div><p>Scaling Laws</p></div></td><td dir="ltr"><div><p>缩放法则</p></div></td><td dir="ltr"><div><p>模型的效果的线性增长要求模型的大小指数增长</p></div></td></tr><tr><td dir="ltr"><div><p>Parameter-efficient Adaptation</p></div></td><td dir="ltr"><div><p>高效参数适应</p></div></td><td dir="ltr"><div><p>在固定住大模型参数的情况下，增加少量的新参数进行精调</p></div></td></tr><tr><td dir="ltr"><div><p>Distribution Shift</p></div></td><td dir="ltr"><div><p>分布转换</p></div></td><td dir="ltr"><div><p>在一种数据分布上进行训练，在另一种数据分布上测试</p></div></td></tr><tr><td dir="ltr"><div><p>Instruction Tuning</p></div></td><td dir="ltr"><div><p>指令精调</p></div></td><td dir="ltr"><div><p>用 instruction 来 fine-tune 大模型</p></div></td></tr><tr><td dir="ltr"><div><p>Code Tuning</p></div></td><td dir="ltr"><div><p>在代码上微调</p></div></td><td dir="ltr"><div><p>用代码来 fine-tune 大模型</p></div></td></tr></tbody></table>