---
url: https://hub.baai.ac.cn/view/33670
title: "Gemini Pro还不如GPT-3.5，CMU深入对比研究：保证公平透明可重复 - 智源社区"
description: "谷歌的Gemini Pro版本与GPT-3.5 Turbo相比接近但略逊，而GPT-4仍然遥遥领先。这是卡耐基梅隆大学进行的专业客观第三方比较的结果。所有模型使用相同的提示和生成参数，并提供了可重复的代码和完全透明的结果。在深入分析中，还发现了Gemini一些奇特之处。"
captured_at: "2026-03-08T11:18:07.995Z"
---

# Gemini Pro还不如GPT-3.5，CMU深入对比研究：保证公平透明可重复 - 智源社区

##### 梦晨 发自 凹非寺
量子位 | 公众号 QbitAI

谷歌Gemini实力到底如何？卡耐基梅隆大学来了场专业客观第三方比较。

为保证公平，**所有模型使用相同的提示和生成参数，并且提供可重复的代码和完全透明的结果**。

![](https://simg.baai.ac.cn/hub-detail/87a157de7602b014864f5eecfe4f76df1703157632870.webp)

不会像[谷歌官方发布会那样，用CoT@32对比5-shot了](http://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247708466&idx=1&sn=5fd8ec0598239ebf17db4a8d7668bd43&chksm=e8df1840dfa89156c8650d32ef2031597ea14d1e5b25cac0519b33fde91ce2eb0942e745e2b8&scene=21#wechat_redirect)。

一句话结果：**Gemini Pro版本接近但略逊于GPT-3.5 Turbo**，GPT-4还是遥遥领先。

![](https://simg.baai.ac.cn/hub-detail/4548b9120e3c95af1ce9c554fc0fe7591703157632871.webp)

在深入分析中还发现Gemini一些奇怪特性，比如**选择题喜欢选D**……

![](https://simg.baai.ac.cn/hub-detail/723ca8eb85d1325b2a7a4992626625ad1703157632871.webp)

不少研究者表示，太卷了，Gemini刚发布没几天就搞出这么详细的测试。

![](https://simg.baai.ac.cn/hub-detail/4eb9edc089df24545d9c75f7ed9034a41703157632871.webp)

## 六大任务深入测试

这项测试具体比较了6大任务，分别选用相应的数据集：

-   知识问答：MMLU

-   推理：BIG-Bench Hard

-   数学：GSM8k、SVAMP、ASDIV、MAWPS

-   代码：HumanEval、ODEX

-   翻译：FLORES

-   上网冲浪：WebArena

### 知识问答：喜欢选D

从结果可以看出，使用思维链提示在这类任务上不一定能带来提升。

![](https://simg.baai.ac.cn/hub-detail/705a8d200e187ea93a2de36576a6a8ea1703157632871.webp)

MMLU数据集里都是多选题，对结果进一步分析还发现奇怪现象：Gemini更喜欢选D。

GPT系列在4个选项上的分布就要平衡很多，团队提出这可能是**Gemini没针对多选题做大量指令微调造成的**。

![](https://simg.baai.ac.cn/hub-detail/94eaede5f2c68e75e68b1810f85786cc1703157632871.webp)

另外**Gemini的安全过滤比较严重**，涉及道德问题只回答了85%，到了人类性行为相关问题只回答了28%。

![](https://simg.baai.ac.cn/hub-detail/ce73f1e14c779163d0c89bc978c0d03d1703157632871.webp)

Gemini Pro表现超过GPT-3.5的两个科目是安全研究和高中微观经济学，但差距也不大，团队表示分析不出来什么特别的。

![](https://simg.baai.ac.cn/hub-detail/d77eeec8c8d4fdf5c6661b9e15423df91703157632872.webp)

### 推理：长问题不擅长

![](https://simg.baai.ac.cn/hub-detail/85ec6a0f05a341b4be6dfd922a9f25381703157632872.webp)

Gemini Pro在更长、更复杂的问题上表现不佳，而GPT系列对此更稳健。

GPT-4 Turbo尤其如此，即使在较长的问题上也几乎没有性能下降，表明它具有理解复杂问题的强大能力。

![](https://simg.baai.ac.cn/hub-detail/c553ac4d99de3e7ff8c25859e63e031d1703157632872.webp)

如果按问题类型来分析，Gemini特别不擅长“tracking\_shuffled\_objects”这类问题，也就人们交换物品，最后让AI判断谁拥有哪些物品。

![](https://simg.baai.ac.cn/hub-detail/06b7af9e3c9031098fc3c5e2446a51ad1703157632872.webp)

Gemini比较擅长的任务是，需要世界知识的体育运动理解、操作符号堆栈、按字母顺序排序单词，解析表格。

![](https://simg.baai.ac.cn/hub-detail/2fd26e826eeddc8d70c90003351625871703157632872.webp)

### 数学：复杂任务反超

![](https://simg.baai.ac.cn/hub-detail/fe1bfd244a654861edffdeee0a243ba61703157632872.webp)

这一次问题本身太长Gemini Pro和GPT-3.5表现就一起下降，只有GPT-4还能保持一贯水准。

![](https://simg.baai.ac.cn/hub-detail/b37e2b47acf2e2cc184c66c179823d631703157632873.webp)

但使用的思维链提示长度最长时，Gemini反超GPT-3.5。

![](https://simg.baai.ac.cn/hub-detail/b277d9ca55744dacad50a4c7104419dc1703157632873.webp)

### 代码：擅长matplotlib

对于代码问题，Gemini在参考答案长的问题上表现很差。

![](https://simg.baai.ac.cn/hub-detail/2cb021e9686f78a62d647f182623f2de1703157632873.webp)

按调用的库来分类，GPT系列在大多数类型更强，但matplotlib就完全不行。

![](https://simg.baai.ac.cn/hub-detail/b5eddf81457b49c5b08a3fff7169dd841703157632873.webp)

### 翻译：只要回答了，质量就很高

翻译任务上，有12种类型Gemini拒绝回答，但是只要回答了的翻译质量都很高，整体表现超过GPT-4。

![](https://simg.baai.ac.cn/hub-detail/ad2a5b43f06eb70b2a7c1a9751f47f091703157632873.webp)

Gemini拒绝翻译的类型主要涉及拉丁语、阿拉伯语。

![](https://simg.baai.ac.cn/hub-detail/72cca7ab8d199f52fd3b9c2d144eb0f41703157632873.webp)

### 网络导航：擅长跨站点冲浪

WebArena给AI模拟了一个互联网环境，包括电子商务、社交论坛、GitLab协作开发、内容管理系统和在线地图等，需要AI查找信息或跨站点完成任务。

Gemini在整体表现不如GPT-3.5 Turbo，但在跨多个站点的任务中表现稍好。

![](https://simg.baai.ac.cn/hub-detail/48c53a1c1c7c3e9bcc14276c43029eb51703157632873.webp)

## 网友：但是它免费啊

最后，CMU副教授Graham Neubig承认了这项研究的一些局限性。

-   基于API的模型行为可能随时变化

-   只尝试了有限数量的提示，对不同模型来说适用的提示词可能不一样

-   无法控制测试集是否泄露

![](https://simg.baai.ac.cn/hub-detail/aa8ef31cb0ba53a26986231facbf76141703157632874.webp)

谷歌大模型推理团队负责人周登勇指出，对于推理任务把Gemini的温度设置为0可以提高5-10个百分点。

![](https://simg.baai.ac.cn/hub-detail/a5ee0cd1ef4afcd0244fc502590d11991703157632874.webp)

这项测试中除了Gemini与GPT系列，还搭上了最近很受关注的开源MoE模型Mixtral。

不过强化学习专家Noam Brown认为可以忽略其中Mixtral的结果，因为用的是第三方API而非官方实现。

![](https://simg.baai.ac.cn/hub-detail/ba4c3ef83692cb01ebe6356187261d771703157632874.webp)

![](https://simg.baai.ac.cn/hub-detail/49414b71dd6f5feda46d754f74cd32f11703157632874.webp)

Mistral AI创始人也来给团队提供了官方版调用权限，认为能得到一个更好的结果。

![](https://simg.baai.ac.cn/hub-detail/873c6348728c13bd890688bab9c01b231703157632874.webp)

总得来，虽然Gemini Pro还是不如GPT-3.5，但是它胜在每分钟调用不超过60次就免费。

所以还是有不少个人开发者已经转换了阵营。

![](https://simg.baai.ac.cn/hub-detail/0070deebe84bc9cbfd5d5f8b1e09dd6e1703157632874.webp)

目前Gemini最高版本Ultra版尚未发布，到时CMU团队也有意继续这项研究。

你觉得Gemini Ultra能达到GPT-4水平么？

论文：
https://arxiv.org/abs/2312.11444

参考链接：
\[1\]https://twitter.com/gneubig/status/1737108977954251216

— **完** —

**点这里👇关注我，记得标星哦～**

**一键三连「分享」、「点赞」和「在看」**

**科技前沿进展日日相见 ~** 

![](https://simg.baai.ac.cn/hub-detail/31c9b8cfa7eef026b99cf24944cd52221703157632874.webp)