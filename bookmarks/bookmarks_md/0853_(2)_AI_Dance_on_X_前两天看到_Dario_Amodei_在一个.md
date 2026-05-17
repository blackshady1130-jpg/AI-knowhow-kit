**AI Dance** (@AI_Whisper_X)  Sun Apr 12 10:44:44 +0000 2026

前两天看到 Dario Amodei 在一个采访里说，continual learning已经 solved 了。
我当时就觉得这个说法挺大胆的。然后今天刷到 Tianle Cai（蔡天乐，Princeton PhD，在 Google DeepMind、MSR做过实习，毕业后加入了 bytedance）写了一篇长文回应这个观点，读完觉得他提了一个很好的框架，简单翻译一下并聊聊。

先说背景。Continual learning 这个词在传统ML里，大部分人把它等同于解决灾难性遗忘（catastrophic forgetting），做这个方向的人一直被这个狭义定义困住。Tianle自己做了好几年 continual learning，他说每次跟朋友解释自己在做什么，对方都一脸困惑。不是朋友怎么样，是这个概念本身就模糊，continual learning、test-time training、self-evolving、lifelong learning，一堆词互相纠缠，谁也说不清楚边界在哪。
他给出的重新定义我觉得是这篇文章最有意思的地方：continual learning 不是一个具体方法（a point），是一个方向（an arrow）。

大部分人想到 AI 技术演进，想的是一个个离散的方法：pretraining、SFT、RL、agentic context management……每个方法贡献一块能力，拼在一起组成系统。但 Tianle 说不对，你不应该把 continual learning 当成跟 SFT 并列的一个“方法”，它是所有这些方法背后共同指向的那个目标。
这个目标是什么？他借用了 METR 的 task horizon 概念：一个模型能可靠完成的任务的时间跨度。你可以把它理解成衡量模型能力的北极星指标，类似摩尔定律里的晶体管密度（虽然更难测）。所有技术演进，从 pretraining 到 SFT 到 RL 到 agentic context management，本质上都在做同一件事：把这个 task horizon 往外推。
然后他用了《创新者的窘境》里 S-curve 的框架来解释这个过程，这个类比也很到位。每一代技术刚出来的时候看着不如现有方案，但最终会超越它。我们已经反复见过这个模式了，最近一波就是 Anthropic 主导的 agentic coding 进展。

用这个框架回头看，每个时代的“continual learning”其实就是当时突破现有技术天花板的那个新东西。当我们只有 pretraining 的时候，SFT 就是那个时代的 continual learning，它让 base model 能从短 context 里“学习”然后回答问题。现在我们有了 RL，agentic context management 就是这个时代的 continual learning，让模型能压缩信息、做笔记、把记忆延伸到 context window 之外。
所以 Tianle 给出的定义是：“旨在突破现有技术可行 horizon 的一系列努力。”（The set of efforts aimed at breaking past the feasible horizon of current techniques.）

回到 Dario 那句话。Dario 说 continual learning solved 了，其实他说的是 context management 加上工程优化，已经能把 task horizon 推到几周甚至几个月了。从这个角度看，他没错：人类水平的 continual learning 可能确实“解决了”。
但 Tianle 的反问很妙：黎曼猜想还没解呢。很多超长 horizon 的任务还远远搞不定。

说到底，Dario 和 Tianle 其实不矛盾。一个在说”人类水平的 continual learning 够用了“，一个在说”但 AI 的 task horizon 还有很长的路要推”。 革命尚未成功，同志仍需努力，Tianle 原文用的就是这句 hh。

likes 441  views 91342  retweets 65  bookmarks 568

![](https://pbs.twimg.com/media/HFsvgNQawAAER9U.jpg?name=orig)

![](https://pbs.twimg.com/media/HFsviV4XMAAXeEA.jpg?name=orig)

---
Quoted:

> **Tianle Cai**: 