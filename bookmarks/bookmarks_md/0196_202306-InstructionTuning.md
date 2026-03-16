---
url: https://yaofu.notion.site/2023-06-Instruction-Tuning-935b48e5f26448e6868320b9327374a1
title: "2023.06 - Instruction Tuning 阶段性总结"
description: "A tool that connects everyday work into one space. It gives you and your teams AI tools—search, writing, note-taking—inside an all-in-one, flexible workspace."
author: "Yao Fu"
captured_at: "2026-03-08T10:53:10.208Z"
---

# 2023.06 - Instruction Tuning 阶段性总结

符尧 爱丁堡大学

yao.fu@ed.ac.uk

2023 年 6 月 26 日

ChatGPT 大火之后，在 2023 年 2 月 24 日，LLaMA 的出现让 instruction tuning 这个方向变得火热；3 月 18 日，Alpaca 让大家看到从成熟的模型 distill 小模型成为还不错的 ChatBot 的可能性，从而引发羊驼系模型寒武纪大爆发。但仅仅过去三个月，大家开始发现意识到用 ChatGPT 的数据训练 LLaMA 的各种问题。本文回顾在过去三个月内的 LLaMA 系模型的发展，讨论 Instruction Tuning 的下一步挑战。

Disclaimer: 这篇文章算是一个 quick research memo，是从我近期的一个分享大纲里 edit 出来的，做了一些删减和补充；现阶段开源社区对于 LLM 训练清楚 / 不清楚的地方同时存在，我尽量做到引用 / 讨论的内容都是有切实证据，而不是基于流言。很多的内容是我跟对应论文的原作者直接讨论过的。但即便这样，我的 take 也可能有误，很多也讨论不出来，所以请大家直接在文章旁边 comment，积极参与讨论，真理越辩越明。

1

目录

最开始

Natural Instructions v1: Cross-task generalization via natural language crowdsourcing instructions

最初的起点，发布于 2021 4 月. 在 LLaMA 前两年. 非常 visionary!!!

InstructGPT: Training language models to follow instructions with human feedback

FLANv1: Finetuned Language Models Are Zero-Shot Learners

T0: Multitask Prompted Training Enables Zero-Shot Task Generalization

对比

InstructGPT 的目标是对齐，zero-shot / cross lingual 是副产物

这篇文章用的 7B 的 Reward model 来对应 175B 的 Policy model，然后被 DeepSpeed Chat 以及之后一系列 RL 的开源工作 follow，这种做法应该是错的。

模型上线现阶段 10-50B 是一个比较跑得起的量级，再大太贵了

FLANv1 和 T0 的目标是 zero-shot，所以不对齐

然后是 Self-instruct

Self-Instruct: Aligning Language Models with Self-Generated Instructions

注意 self-instruct 的重点

Base model 可以是任意，不需要是经过了 alignment 之后的模型 (ChatGPT)

复现了从初代 davinci 到 text-davinci-001 的过程 — 非常 insightful!!

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F928250bf-e7ee-4206-90fa-4b386cac27eb%2FUntitled.png?table=block&id=ff65b63a-b90f-44ee-a9a1-12658338cb47&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1360&userId=&cache=v2)

然后是 FLANv2 — 很重要，我可能读了十遍以上，建议背诵全文

1

Scaling Instruction-Finetuned Language Models

效果除了不加 human preference 之外其他都加，等下转门讨论

1

Human preference 确实是喜欢能说的，但是能说的模型不一定能干活。Flan 能干活，但是不能说，跟程序员一样

Alpaca：起始文章，但是模型本身强度并不多高

Vicuna

在开源中只做对话强度不错，格式符合人类喜好，生成内容多，unique token 多

Automatic eval 中，可能 in-context learning / reasoning / knowledge suboptimal (体现在 MMLU，BBH 分数)，不是说它不行，而是说它可以更好

GPT-4 eval 到底行不行还不好说，LMSys 团队自己说行，前提是 prompt engineering 做得足够到位：Judging LLM-as-a-judge with MT-Bench and Chatbot Arena

另外 LMSys 的团队在 efficiency 方面非常强，模型的 serve 看 [vllm](https://github.com/vllm-project/vllm) 这个 project，或许是开源最快的

然后一系列以 GPT-4 做 judge 然后号称自己达到了 GPT3.5 x% 水准的模型，全部不推荐，因为 Eval 不可靠

但是存在几篇工作在 alignment 的时候没有依赖 ChatGPT，这些工作推荐，它们包括

LIMA: Less Is More for Alignment — 关注他们选数据的方法，推荐花一个小时的时间把他们的[数据](https://huggingface.co/datasets/GAIR/lima)有感情地朗读一遍，这样就知道什么样的 SFT 的数据是好数据了

Dromedary: Principle-Driven Self-Alignment of Language Models from Scratch with Minimal Human Supervision — 关注他们 prompt engineering 的方法，这个基本上是一个 LLaMA 版的 Constitutional AI - SFT

然后是一些 paper （终于） 开始分析 instruction tuning 的 data mixture

Tulu: How Far Can Camels Go? Exploring the State of Instruction Tuning on Open Resources

结果非常 mix，没办法下结论哪种 mixture 好

但是知道哪种不好：NLP benchmark

首先，不要在一堆 benchmark 上算分数看平均，特别是不要在 GPT-3 的测试任务上看平均，因为平均下来大家都一样；推荐只看核心的有区分度的 benchmark

没有区分度的例子：

这里面其实涵盖了 MMLU 和 MATH，但是被其他数据集平均了

Summarization + Rouge / Translation + BLUE:

1

Rouge 和 BLUE 模型强弱只有四五分的差别，数字太小 v.s. accuracy 下模型强弱是 90 分和 10 分的差别，数字足够大

Rouge 和 BLUE 和人类便好不 align — 注意 BLUE 也不完全 align

1

那么 Pretrain 建议看哪些呢？

区分度，模型强弱需要能一眼看出

分方向，现阶段可以暂时分成

英文知识 — MMLU

中文知识 — C-Eval

推理 — GSM8k / BBH

代码 — HumanEval / MBPP

解决上面四项平衡之后，可以接着做

MATH：高难度 reasoning

Dialog：这个可能只有 human eval 才行，automatic eval 搞不定

接下来讲 Automatic Eval

Knowledge: MMLU

这个数据集很稳定，基本上没有 sensitivity issue

Reasoning:

GSM8k: 也比较稳定，但要注意答案提取函数的提出率，低于九十的话得多加 regular expression

BBH - Algorithmic:

不是很稳定，需要注意答案提出率

BBH - Language:

不是很稳定，需要注意答案提出率 — Chain-of-thought Hub 马上会出一个答案提出率对于结果的 sensitivity 的分析，结论是 BBH 比较 sensitive

现在除了增大模型之外，还不清楚哪些操作可以增加 BBH 数据集上的分数

Coding:

Human Eval / MBPP: 似乎比较稳定但需要注意做 unbiased estimation

先看上面的几个数据集，分数能够 match llama 之后，就看 MATH

MATH：

超级难，GPT-4 的分数

naive prompting: 42

→ majority voting over 18k: 69.6

→ best of n with outcome based reward modeling: 72.4

1

→ PPO + process-based reward modeling = ? 推测会上 90

泛化？— 应该是比较强的，泛化一般而言跟基础模型大小正相关，跟 SFT 数据总量负相关，跟 SFT 数据丰富度正相关

如果不是 GPT-4

Minerva / PaLM-2: 34.3

Galactica: 33.6 — 这篇文章操作很好，因为 Hallucination 被喷下架导致重要性被严重低估

88B paper + 7B code + 7B encyclopedias, textbooks and educational material + 2B KB + 1B CC + 0.4B prompt / instruction \* 4 epochs

LLaMA 65B: 10.6

其他：低于 10 分

对于一个已经 finetune 成了 chatbot 的模型

首先把上述 benchmark 用 few-shot 的方式过一遍，确保不要掉点

如果只是 dialog finetuning 的话可能会伤已有的能力 (MMLU / BBH)

如果掉点，则考虑 LM mixing / FLANv2 mixing

注意 Chatbot 的 few-shot prompting 要用 dialog 的版本因为 single round 里塞很多 in-context example 模型可能不 instruction-following 不够强，见 CoT Hub 的 [standard prompt library](https://github.com/FranxYao/chain-of-thought-hub/blob/main/spl/gsm8k/chat/few_shot_cot.chatml)

然后就是去 eval 用户偏好了，这个时候只能人做

如果有很大的，已经训练好了的 reward model，可以用它 eval 上线的小型 / 中等模型，这个其实跟人做 eval 区别不大

对于一个很大的 Policy Model

Online iterative RLHF 前期怎样都需要需要 expert eval

那么能不能用稍微弱一点的模型做 eval 呢？— 可以用，但是注意 query 的难度和分布，注意 prompt engineering

如果不经过 prompt engineering ，肯定不行，因为各种 bias

如果 query 难度不够，diversity 不够，也不一定行

但是对于 reasoning 相关，non-information seeking 相关（比如 TLDR），又不一定行

对于 information seeking 相关的 query 会 biased 到长的回复

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F5c486cfd-df5a-4a44-86d6-7e3ca3151508%2FUntitled.png?table=block&id=4a9ed8f3-1487-40c3-aad8-9841daacdf67&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1150&userId=&cache=v2)

回复越长，GPT-4 越喜欢，分越高

FLANv2 是一个很神奇的数据集，它除了不加 user preference 之外什么都加

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fac7c36ca-f89a-40f3-a95a-04f3ca99aab6%2FUntitled.png?table=block&id=be27cb12-cc0b-4aa5-8e29-ab84e39ec215&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

注意 CoT prompting

只在 62B 之后才会比 Direct 更好

不加 knowledge (MMLU) 只加 reasoning (BBH)

FLANv2 增加的效果有

knowledge (MMLU)

reasoning (BBH)

Multilingual (TyDiQA / MGSM)

注意 FLAN 的作者们验证过，没有数据泄露

注意以上内容对 in-context learning 和 zero-shot 均成立

但是 FLAN 的回复短，所以不加 user preference — Flan 的性格就像直男，能干活儿，话太少

注意区分数据泄漏和分布内泛化

如果一个数据集的测试集被用来训练模型，叫做数据泄漏，此时模型的分数会特别高，不可信

如果一个数据集的训练集被用来训练模型，叫做分布内泛化，此时模型的分数是可信的

有些数据集分布内泛化的难度不高，比如 MMLU / C-Eval，基本上做 data scaling 就可以加分

有些数据集，如果模型不强，即使看过了训练集，模型在测试集上也做不好，比如 GSM8K — 这种类型的数据集是优质 eval 数据集

代码的难度可能介于 MMLU 和 GSM8k 之间，分布内泛化不像 GSM8K 那么难，但也不简单

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fedde8392-33b5-4d5e-b219-1d238153bfbe%2FUntitled.png?table=block&id=66bf2994-fe53-4c5b-9be2-b893f2b3d5b9&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

注意这里 FlanT5 和 T0pp 只有 instruction 的数据集有区别，但是 FlanT5 仅靠 T5 的 relative positional encoding 来 naively scale 到 8k 的 context length 会显著高于 T0

Long Context 或许 data engineering 跟 neural architecture engineering 同样重要

两篇文章的 data engineering 非常出色

WizardCoder: Empowering Code Large Language Models with Evol-Instruct

通过不断 prompt AlpacaCoder 构造 instruction tuning 数据集，不依赖 ChatGPT

1

HumanEval，DS-1000 仅次于 GPT-4，超过 Claude / Bard

base model 用的是 StarCoder，这意味着 The Stack V3 的质量再次得到验证，同时注意 pretrain code data 可以过多个 epoch 但网页只过一个 epoch

Phi-1: Textbooks Are All You Need

Pretrain 数据集来源于 filtered code + prompt ChatGPT

Instruction tuning 的数据集来自于 prompt ChatGPT

base model 只有 1B

怎么评价

一定要好好研究他们是如何 prompt base model 的 — 要对 base model 有信心，只要 MMLU / BBH / HumanEval 分高，它的潜力就超过你的想象

prompt 出来的数据集相当于给 HumanEval / MBPP 这种比较短的算法题搞了一个超大训练集

但是不可以认为它对着测试集优化，因为它泛化的空间应该大于 HumanEval / MBPP — 这个泛化空间跟 model scale 显著正相关

在此基础上，比较难的点是

Repo-level code understanding / completion — HumanEval / MBPP 还是有点短

Ability balance — 如果照着 Phi-1 的做法，除了代码之外的其他能力都会被冲掉

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6a296d1c-9259-4af4-84d4-53d4be0c62c7%2FUntitled.png?table=block&id=c50be7c9-7d68-4b92-bef5-7c5744f8b40c&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Continue training 时 使用 50% 的代码 作为 data mixture 不会伤模型 language 的能力，反而会提升 coding 和 reasoning

目标：

构造一个 instruction tuning data mixture，使得 dialog / coding 增加

同时 MMLU (English knowledge) / C-Eval (Chinese knowledge) / BBH and GSM8K (reasoning) 不掉点

In-context learning 不掉点

思路

可以用 FLAN 打底 — 它非常大几乎相当于 continue training

1

考虑做一个中文版的 FLAN — 最近智源发的 [COIG-PC](https://huggingface.co/datasets/BAAI/COIG-PC) 似乎有点像

code 的部分参照 WizardCoder 和 Phi-1 的做法

以上数据做好之后，搜 instruction tuning 的 data mixture and data curriculum 的超参数

用上面提到的方法做 Eval

现阶段 instruction tuning 核心问题是能力平衡

基础能力的 Eval 可以参照 Chain-of-thought Hub，但 dialog 还是得人来，且人也不一定 eval 得足够好

FLAN 非常神奇，可以考虑做一个中文版

抓紧把 instruction tuning 收尾，快点进到 reward modeling 阶段

注意要先把 reward modeling 本身做好，确保 reward model 有判断力，再去做 PPO

不要 reward model 还没搞清楚就上 PPO ，步子迈太大容易扯到