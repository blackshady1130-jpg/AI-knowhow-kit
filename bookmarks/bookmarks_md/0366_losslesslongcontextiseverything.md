---
url: https://mp.weixin.qq.com/s/UMY0qZsCGh87KnW4wjfvoA
title: "专访月之暗面杨植麟：lossless long context is everything"
description: "AI-Native产品的终极价值是提供个性化交互"
author: "拾象"
captured_at: "2026-03-08T11:30:22.404Z"
---

# 专访月之暗面杨植麟：lossless long context is everything

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/3tHNibnJ2jgyKZyCCAoulic3qyakf7NdAeOm28QQpZUG8hDMbOVGSeoSFeMKg5n9DJlPcn1iaLEKceIuFtpCV9z4Q/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgyKZyCCAoulic3qyakf7NdAejP2WaxD0BMt8CiabwYxYXFGiavRdvA8rdBywXHesHw1OLFxk3lXNyQWQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgyKZyCCAoulic3qyakf7NdAeQHxO4JlczcRErfaCJlSKdibndD6gE9WlFWdw7P1uKMLDqQYB58DgqbA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

采访：天一、penny、guangmi

编辑：天一

排版：Scout

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgyKZyCCAoulic3qyakf7NdAe9yvxKU52I5PBz3icadjrg23Ij2Gq45cbpXhNaYZxRLxibt275omoy6iag/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

Lossless long context is everything。这是我们跟杨植麟聊完两个小时后记忆最深刻的一个观点。

这个技术判断在 23 年 10 月已经被传递出来，当时杨植麟创立的月之暗面发布了首个模型 moonshot 和智能助手 Kimi，支持 20 万字的输入。**做“长”是因为杨植麟判断 AI-Native 产品的终极价值是提供个性化的交互，而 lossless long-context 是实现这一点的基础 —— 模型的微调长期不应该存在，用户跟模型的交互历史就是最好的个性化过程，历史上每一代技术都是在提升 context length。**

杨植麟身上的标签有天才 AI 科学家、连续创业者……在这次深度访谈中，他再次证明自己是个真正“懂”大模型的创业者，所以本文中有许多反共识的观点：杨植麟觉得微调最终会不存在，tokenizer 最后也不一定是必须的；硅谷大模型训练者们担心数据瓶颈和能源限制，他反而觉得所有问题都是互相关联的，多模态可以缓解数据短缺，合成数据则可以通过改变计算范式解决能源问题。

本文还试图回答另一个外界普遍关心的问题：一家新创立的 AGI 公司如何超越 OpenAI？杨植麟的答案是 tech vision，一号位要能做出技术判断，同时还能拍板执行。一个具体的例子是，月之暗面希望比 OpenAI 更关心用户，原因是杨植麟判断用户数据的 scale up 的效果最终会超越 base model 自身。

杨植麟对于用 transformer 这个概率模型的思想基础走向 AGI 也很有信心，用他的话说**“如果你有 10 亿的 context length，今天看到的问题都不是问题”。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**01.**

**AGI：AI 本质就是一堆 scaling law**

 **海外独角兽：****我们把 LLM 的训练比作登月，月之暗面的名字也和登月相关。你怎么看现在创业公司的 LLM 训练，在 GPU 和算力资源有限的条件下，还能实现登月吗？**

**杨植麟：**“登月”有几个不同的生产要素，算力肯定是一个核心，但还有其他的。

你需要一个同时满足 scalability 和 generality 这两点的架构，但今天其实很多架构已经不满足这两条了。transformer 在已知的 token space 符合这两条，但放大到一个更通用的场景，也不太符合。数据也是一个生产要素，包括整个世界的数字化，和来自用户的数据。

所以在很多核心生产要素中，通过改变其他的生产要素，可以让算力利用率变高。

同时，针对“登月”，算力肯定要持续增长。**今天能看到最好的模型是 10 的 25 到 26 次方 FLOPs 这种规模。这个数量级接下来肯定还会持续增长，所以我认为算力是个必要条件，因为机器学习或者 AI 研究了七八十年，唯一 work 的东西其实是 scaling Law，就是放大这几种生产要素。**

我们其实比较有信心，在一年的时间窗口，能够达到 10 的 26 次方这样规模的模型，资源最终会得到合理分配的。

 **海外独角兽：****OpenAI 训下一代模型，我们推测有至少 10 万张 H100，单个集群也能达到 3 万张。OpenAI 显然是追求“登月”的，不足可能是没那么注重用户和客户体验。月之暗面和 OpenAI 的差异化路径会在哪儿？有什么是月之暗面能做而 OpenAI 不做的？**

**杨植麟：**短期内关键的一点在于大家的 tech vision 不完全相同。很多领域并不是 OpenAI 的核心竞争力，比如图片生成，DALL-E 3 至少比 Midjourney 落后一代。GPT 的 long-context 也并不是 state-of-the-art。我们前段时间做出来的 lossless long-context 技术在很多具体场景上要比 OpenAI 效果更好，因为用了无损压缩的技术。你可以用它去读一篇很长的文章，它可以很好地还原一些具体细节，还可以内容做推理。用户自己还会发现很多场景，比如扔给它 50 个简历，让它根据你的要求做分析和筛选。

要做差异化，我认为就是去看这里面的 tech space 有多大，tech space 越大，技术、产品、商业层面能实现的差异化就越大。如果技术已经收敛了，那大家只能去追赶，就是同质化内卷。

然后我其实比较乐观，因为现在仍有巨大的 tech space。AGI 技术可以分为三层：

第一层是 scaling law 结合 next-token-prediction。这个基础对所有人都是一样的，追赶过程逐渐收敛。在这个路径上， OpenAI 现在做得更好，因为他们过去四五年投入了相应的资源。

第二层现在有两个核心问题。首先是如何通用地表示这个世界？真正的“通用”是像计算机一样，用 0 和 1  就能表示整个世界。对于基于 transformer 的语言模型来说，它能表示一本书、一篇文章、甚至一个视频，但表示一个更大的 3D 世界或你硬盘上的所有文件还有难度，没做到 token-in-token-out，离所谓的 unified representation 其实有差距。架构其实解决的是这个问题。

通过 AI 自我进化克服数据稀缺性的瓶颈是第二层的另一个问题。今天的 AI 其实像一个黑盒，这个黑盒有两个输入：电源线和数据线，输入这两个东西后，盒子就能产出智能。随后大家意识到，数据线的输入是有限的，这就是所谓的数据瓶颈问题，下一代 AI 需要拔掉数据线，做到只要源源不断地输入电力，就能源源不断地输出智能。

这两个核心问题导致在第三层有巨大的空间，包括 long-context、不同模态的生成、模型多步规划的能力、指令遵循的能力、各种 agent 的功能等。

这些上层的东西都会有巨大的差异化，因为中间存在两个重要的技术变量。我认为这是我们的机会。

除了技术层面，价值观上我们有一点和 OpenAI 不同：**我们希望在下一个时代，能成为一家结合 OpenAI 技术理想主义和字节所展现的商业化哲学观的公司。**东方的效用主义我认为有一定的可取之处。完全不关心商业价值的话，你其实很难真的做出来一个伟大的产品，或者让一个本身很伟大的技术变得更伟大。

 **海外独角兽：****你觉得模型公司应该讲什么故事？像 OpenAI 一样讲追求 AGI，还是超级应用的故事？两者会有矛盾吗，怎么来平衡？**

**杨植麟：**如何讲故事取决于投资人的心态。对我们来说，更重要的是理解两者之间的关系。

AGI 和产品对我们来说并不是手段和目的的关系，两个都是目的。同时，在追求 AGI 的过程中，我认为所谓的数据飞轮是很重要的，尽管它是一个老套的概念。

像 ChatGPT 这样的产品，还没有完全建立起基于用户数据的持续进化。我觉得这很大程度上是 base model 还在进化，进化了一代，之前的用户数据就没什么用了。这跟发展阶段有关系 —— **现在“吃”的是 base model 的 scaling law，未来可能会去“吃”用户这个数据源的 scaling law。**

历史上基本所有的互联网产品要跑出来，最终都要靠用户数据的 scale。今天 MidJourney 已经能看到一些迹象，它通过“吃”用户的 scaling law 可以胜过 base model 的 scale up，但如果只看语言模型和文本，base model 的 scaling 效果仍然远远超过用户的，但我认为最终会转移到用户的 scaling law，只是个时间问题。

现在面对数据瓶颈，这一点尤为重要。特别是人类偏好数据，它非常有限，但没有它又不行。我觉得这也是每一个AI-Native 产品现在最值得思考的问题之一。**所以，一个不足够关心用户的公司最终可能也没法实现 AGI。**

 **海外独角兽：****怎么看 MoE？有一种说法是 MoE 不是真正的 scale up，只有 scale up dense model 才会提升模型的能力。**

**杨植麟：**你可以认为带 MoE 和不带 MoE 是两条 scaling law。本质上 scaling law 刻画的是 loss 跟参数量之间的关系。**MoE 改变了这个函数，让你能够用更大的参数，但同时 FLOPs 不变。合成数据改变的是另一个关系，FLOPs 不变的情况下让数据规模增长。**

沿着 scaling law 一直走是个有确定性的事情，大家通过试图改变 scaling law 里的具体关系来获得更高的 efficiency，多出来的 efficiency 就是各自的优势。

**现在很多人觉得做出 MoE 就可以实现 GPT-4。我觉得这是片面的说法，最终更实质的可能还是如何有一个统一的表示空间以及可规模化的数据生产。** 

 **海外独角兽：****如果算力足够，会有人想做一个万亿参数的 dense model 吗？**

**杨植麟：**取决于推理成本的下降速度，但我觉得肯定会有。现在大家是因为推理成本太高，所以都在做 tradeoff。但是最终直接训练一个万亿的 dense model 肯定效果会比一个只有千亿参数的模型要好。

 **海外独角兽：****Anthropic 一直在提模型的可解释性，这一点其实有蛮多争论。你是如何思考可解释性的？因为刚刚你也提到了模型是一个黑盒，并且其实人类到现在还没有弄清楚自己的大脑是怎么工作的。**

**杨植麟：**可解释性核心是个信任的问题。建立一个信任的心智是很重要的，对应的应用场景甚至可能和 ChatGPT 的也会不同，比如 long-context 和搜索的结合。

当模型完全不 hallucinate 或者概率非常低，就不需要解释了，因为它说的东西都是对的。而且解释有可能也只是 alignment 的一部分，比如说 chain-of-thought 也可以被认为是一种解释。

Hallucination 是可以通过 scaling law 来解决。但不一定是在 pre-training 环节，**因为其实 alignment 也有 scaling law，它肯定是可以被解决的，只要你能找到对的数据。AI 本质就是一堆 scaling law。**

 **海外独角兽：****你对 AGI 的预期是什么？transformer 本质还是一个统计概率模型，它能通往 AGI 吗？**

**杨植麟：**统计模型没有什么问题。当 next token prediction 足够好的时候，它能够平衡创造性和事实性。

事实性一般是对统计模型的挑战，但是今天的语言模型可以有非常尖峰的分布。让它回答“中国的首都”，模型对“北”这个字能给出 99% 的概率。同时，如果我今天让它写一本小说，那它可能下一个词的概率分布就会很均匀。概率其实是一个通用的表示方式。本质上这个世界上有大量的熵，抓住确定性的东西，让本身是混沌的东西继续混沌。

通往 AGI 的话，long-context 会是一个很重要的点。所有问题都是 long-context 的问题 —— **历史上所有的架构演进本质上都是在提升有效的 context length。**word2vec 最近拿了 NeurIPS 的 Test of Time 奖。它在 10 年前用一个词去预测周围的词，相当于 context length 是 5。RNN 把有效的 context length 提升到了 20。LSTM 涨到大几十。transformer 到了几千。现在我们能做到几十万。

**如果你有 10 亿的 context length，今天看到的问题都不是问题。**

此外，其实无损压缩就是在一片混沌中学习确定性。一个极端的例子是等差数列，给定前两个数，接下来每一个数都是确定的，不存在混沌，所以一个完美的模型可以还原整个数列。但真实世界的很多数据都存在噪声，我们需要过滤掉这些噪声，让模型只学能学习到的内容。在这个过程中，对于那些不确定的可能性，也要分配足够的概率。举个例子，如果要生成一张图片，那么它的 loss 会比生成一段文字更高，这是因为图片包含了更多的混沌和信息量，但只需捕捉其中你能掌握的部分，剩余的部分可以认为是有概率发生的。比如，水杯的颜色是绿色还是红色就是有概率会发生的，但颜色这个信息不会改变“水杯长什么样”这件事，所以这里面需要重点学习的就是水杯的形状，至于它的颜色，就要做一个概率分配。

 **海外独角兽：****context length 的提升存在什么规律？有技术可预见性吗？**

**杨植麟：**我自己感觉存在 context length 的摩尔定律。但需要强调：给定长度下的准确率也非常重要，需要同时优化长度和准确率（无损压缩）两个指标。

在保证模型能力和智商的情况下，我觉得大概率 context length 的提升是指数级增长的。

**02.**

**多模态：大部分架构不值得被  scale up**

 **海外独角兽：****大家都期待多模态会在 2024 年爆发，相比文本，多模态的技术难度会在哪里？**

**杨植麟：**现在 state-of-the-art 的视频生成模型的 FLOPs 其实比语言模型少一个数量级以上，并不是大家不想 scale up，而是大部分架构不值得这么做。

19 年最流行的是架构是 BERT，后来大家问为什么没有人去 scale BERT，其实是因为值得被 scale 的架构需要具备 scalability 和 generality 这两个条件。我不认为 BERT 没有 scalability，但是你能明显看到它没有 generality —— 不管 scale 到多大，它都不可能给你写一篇文章。多模态过去几年也是卡在架构上，缺少真正通用的、有人愿意去 scale 的模型。Diffusion 明显不是，scale 上天了它也不可能是 AGI。今天 auto-regressive 的架构带来了一些新的可能，牺牲了一些效率解决了通用性。

Auto-regressive 本身是 scalable 的，但是 tokenizer 不一定，或者最后就不需要 tokenizer，这是 24 年的核心问题。

 **海外独角兽：****如果 tokenizer 不 scalable ，我们需要一个 transformer 之外全新的架构吗？**

**杨植麟：**光说 transformer 本身，我觉得问题不大。核心还是解决 tokenizer 的问题。transformer 架构其实已经发生很多变化了，今天做 long-context、做 MoE，都不是标准的 transformer。但是 transformer 的灵魂或者思想肯定还会存在很长时间，核心是怎么在这个思想基础上解决更多问题。

 **海外独角兽：****其实 context length 无限长的话，我们也不需要 tokenizer 了？**

**杨植麟：**对。本质上模型足够强的话，它可以处理任何的 token、pixel、byte。有了无限长的 context length，你可以直接把硬盘上所有的东西都输给它，它会变成你真正的新计算机，根据这些 context 采取行动。

 **海外独角兽：****OpenAI、Anthropic 等领先的模型公司觉得 2024 年的一大瓶颈会是数据，所以他们对怎么用合成数据期待比较高，你怎么看合成数据？**

**杨植麟：**一个值得被 scale up 的架构是基础，这个架构首先得支持不断加入更多数据，然后数据才会真的成为瓶颈。我们现在说的数据瓶颈，从文本模态上，2024 年就会遇到，但多模态数据的引入进来会把这个问题推迟 1-2 年。

**如果视频和多模态的卡点解决不了，那文本的数据瓶颈就会很关键。**这点上其实我们也有些进展 —— 如果限定了问题，比如数学或者写代码，数据是相对好生成的。通用的问题现在还没有完全的解法，但是存在一些方向可以去探索。

 **海外独角兽：****2025 年的瓶颈会是能源？因为到时候单个集群规模很大，对能源带来挑战。**

**杨植麟：**这些问题其实是连在一起的，最后可能是多模态解决数据问题，合成数据解决能源问题。

到了 GPT-6 这一代，掌握合成数据技术的玩家会体现出明显差距。因为数据其实有两种，一种是做 pre-training 的数据，另外一种是获取成本更高的 alignment 数据。如果掌握了数据生成技术，alignment 的成本可能会降低好几个数量级，或者能用一样的投入产生更大的几个数量级的数据，格局就会发生变化。

我觉得 2025、2026 年可能是很重要的 milestone —— 模型的大部分计算量会发生在模型自己生成的数据上。

**26 年的时候也许模型用于推理的计算量会远远大于训练本身，可能花 10 倍的成本去推理，推理完之后花一倍的成本来训练。会出现新的范式，推理即训练，而且这个推理不是为任何用户服务的，只为自己本身的合成数据服务。**

**出现这种情况的话，能源的问题也解决了，因为推理是可以分布式的。而且它不违背定律，本质还是个能源守恒。只不过我把计算范式改变了，让能源能够以分布式的方式解决。**

**03.**

**超级应用：模型的微调可能最终不存在**

 **海外独角兽：****Google 和抖音背后的搜索和推荐有很强的飞轮效应，算法能根据用户的行为实时反馈，用户体验也能不断提升。LLM 现在无法实时反馈用户行为，AI-Native 产品的飞轮效应会是什么？**

**杨植麟：**我深入思考过这个问题。**AI-Native 产品最终的核心价值是个性化交互，这是以前技术实现得不好的，所以这个问题其实是关于个性化的 —— 怎么让用户使用你的产品多了之后，获得高度个性化的互动体验。**今天对许多产品来说，这个个性化程度几乎为零。以前我们只能做个性化的推荐，但现在，用户可以与产品进行互动。这种互动是高度拟人化和个性化的。怎么实现这一点？

我觉得这背后实际上是个技术问题。传统 AI 时代，要实现个性化，需要持续更新模型，用小模型解决单点问题。**大模型时代，实现个性化的一种方式是微调，但我认为微调可能不是本质的方法，长期来看可能不会存在模型的微调。**为什么？当你的模型指令跟随能力、推理能力、上下文一致性能力越来越强时，所有东西只需要放在内存里就可以。比如你的大模型内存有一堆 prefix 这样的东西用来 follow，成本可以降到非常低。最终，你对模型个性化的过程实际上就是你所有的交互历史，也是一个包含了你的偏好和反馈的集合，这些反馈会比上个时代的产品更直接，因为它是完全通过对话界面产生的。

基于这个判断，进一步就会想：如何在技术层面实现基于 long-context 的定制化去完全取代微调？

我认为现在正在往这个方向走，未来模型不需要微调，而是通过强大的上下文一致性和指令跟随能力来解决问题，长期趋势应该是底层技术个性化，这会是一个很重要的变化。

比如，GPT-4 带来的新的计算范式，创建 GPTs 并不需要微调。以前的定制化是通过 programming 实现的，今天实际上是通过让模型的 prefix 变得非常复杂，从这个通用的集合中抽出你想要的东西。通过这种方式实现个性化才是 AI-native 的个性化，外挂一个传统的推荐引擎肯定会被新方式淘汰。

 **海外独角兽：****你们先做 lossless long-context 这个决策是怎么做出来的？**

**杨植麟：**我觉得最重要的还是以终为始地思考这个事。**大模型作为新的计算机肯定也需要很大的内存，因为旧的计算机的内存在过去几十年的时间里面至少增长了几个数量级，而且旧的计算机也是一开始的时候只有很少的内存。第二点就在于 AI 的终极价值是个性化。**

 **海外独角兽：****OpenAI 其实也有一定的 long-context 了。**

**杨植麟：**它还没有把用户的交互过程真正视为个性化的场景。比如，如果我们去 ChatGPT prompt 某个东西， 不管是今天还是明天，只要模型版本相同，可能效果基本上差不多，这就是我说的缺乏个性化。

最终所有东西都是指令遵循。只不过你的指令会越来越复杂。今天你的指令一开始可能是 10 个词，但是你到后面有可能它就是 1 万个词、 100 万个词。

 **海外独角兽：****Chatbot 一直是 AI 科学家的白月光，如果每个用户每天和 Chatbot 对话几百条，Chatbot 系统能采集和理解更多的用户 context，最终会大幅超越搜索和推荐系统的匹配准确率吗？就像我们和同事家人之间的互动，只需要一句话甚至一个眼神对方就懂你的意思。**

**杨植麟：**核心是跨越信任这一步。

我觉得最终衡量一个 AI 产品的长期价值，就是看用户愿意在它上面输入多少个人化的信息，然后 lossless long-context 和个性化负责把这些输入变成有价值的东西。

**可能也还需要新的硬件形态，但我觉得模型和软件现在也还是个瓶颈。**因为要再往下钻一层，让用户输入很多信息的前提是 trust，是你需要有足够 engaging 和 human like 的AI。不能说是我为了得到你的信息所以专门设置了一些产品功能。最终效果应该是用户和 AI 成为了朋友，那所有事情都可以跟它说。

Inflection Pi 的 motivation 其实是很好的，想要建立强信任，只是 Pi 可能要再往前推一步，到底怎样跟用户去建立信任，人类社会可能并不接受指派一个终身搭档的做法，这有点反人性。

 **海外独角兽：****月之暗面想做超级应用，你自己理想中的超级应用长什么样子？多大才算超级？**

**杨植麟：**还是看破圈程度。周围的亲戚都在用，你才真正成为超级应用。而且我认为 AI 能力的提升会领先于产品破圈。比如假设今天 character.ai 是非常完美的多模态模型，那我觉得它破圈的概率至少会大 10 倍。最终一个应用的上限体现在以年为维度的 AI 和人的 connection 的增加。

**04.**

**月之暗面：最好的人才需要 unlearn 能力**

 **海外独角兽：****AGI 公司最理想的 CEO 画像应该是什么样的？**

**杨植麟：**一方面需要有 tech vision。不能一直做别人已经证明过的东西。真的 AGI 公司必须有自己独特的技术判断，而且这个判断应该影响到公司的整体方向。如果一号位不能拍板也不行。我们年初已经在做 auto-regressive 的多模态、lossless long-context 了，但它们都是最近一两个月才变得非常火，甚至即使今天，lossless long-context 仍然不是一个共识。但如果今天才看到这个事情，已经没有足够多的时间去迭代，最后会变成跟随者。

第二点是能够很深刻的理解 AI-Native 产品的开发方式，然后基于新的生产方式适配一套组织。**以前做产品是通过了解用户的需求设计功能，新时代需要在制造的过程中完成设计。ChatGPT 就是通过制造完成设计，并没有先设计出来一堆场景再找对应的算法。Kimi 的用户自己去上传简历然后做筛选，也是我们上线之前完全没有测试过的用例。**

资源获取肯定也很重要。其中主要烧钱的是算力。早期靠融资，到后面就需要更多的产品商业化。商业化也不能照搬上一个时代成熟的东西创新，所以好的 CEO 和团队应该有一定经验，但同时也有很强的学习和迭代能力。

 **海外独角兽：****但有可能投资人分辨不出来到底谁的 tech vision 是最领先的。**

**杨植麟：**我不太担心这个问题。现在就是最好的分配方式，更接近一个自由市场，最后会有最高的分配效率。我们要跟别人证明的也不是我们的 vision，因为 vision 是一个抽象的东西，还是要通过真实的 deliver 模型和产品。Anthropic 放出 Claude 这些模型之后，马上就得到了更多的资源。市场是公平的。

 **海外独角兽：****从建立产品和公司竞争壁垒的角度，工业时代讲究规模效应，互联网时代讲究网络效应，AGI 时代会有新范式吗？**

**杨植麟：**短期是组织方式的变化带来技术上的提升 —— 你通过更好的组织带来更好的技术，然后在产品上直接传递出更好的体验。

长期大概率还是网络效应。问题在于网络效应的体现方式是什么？比如以前互联网的双边网络可能仍然会存在，但并不是用户和创作者双边。AI-Native 产品的双边网络可能体现在个性化上，用户和 AI 存在一种共创的关系。

所以我现在看到值得探索的是两点：模型能力的持续提升，另一个是双边效应。它们会在新时代带来新的范式。现在 Midjourney 在双边效应上已经爆发了，Stable Diffusion 作为开源模型就尴尬在单边太分散，只能依赖 base model 的提升。

 **海外独角兽：****从招聘角度，你怎么定义好的人才？**

**杨植麟：**我会拆成经验和学习来看。学习是一个通用的能力，不光是 learn，还要 unlearn，特别是以前的成功经验。假设你是从 0 到 1 做了 YouTube，现在做 AI 产品可能比别人更难，因为要 unlearn 很多东西。学习比经验重要。可能再过 5 年的话， AI 行业会培养出来很多所谓的成熟职能。今天我觉得其实划分职能没有什么意义，需要每个人都很多面。

 **海外独角兽：****什么样的 researcher 才会有 tech vision？**

**杨植麟：**核心是两点，一个是抓大放小，一个是终局思维。我跟很多 researcher 合作过，容易出现的一个问题就是过分雕花，容易在局部里看到有很多可以优化的东西，比如我们发现 transformer 解决了 LSTM 的 context length 问题，但如果再跳出来一层，就会发现本质上每一代技术都是在提升 context length。

 **海外独角兽：****你觉得月之暗面还需要多少这样的人才？**

**杨植麟：**客观上来说，限制我们的肯定还是供给。现在 AGI 的人才稀缺在于经验，但其实拥有学习能力的人才还是很多的。

但是需求角度，整个组织不能太大 —— 把自己活生生又弄成了大厂的话，很多组织优势就丢失了。所以我们肯定还是会维持一个精简高效的组织。我觉得一个核心判断是 AGI 不需要那么多人。而且长期来看，真的“拔掉了数据”之后，GPT-6 水平之后的模型完全可以自我进化，这样才能突破人类已有能力的边界。

 **海外独角兽：****你怎么看追平 GPT-4 的难度和时间？**

**杨植麟：**Benchmarking 刷到 GPT-4 非常简单，但是达到它的实际效果肯定有难度的，而且靠的不只是资源，Google 已经验证了这一点。其实 GPT-4 的训练成本也没那么高，大几千万美元不是一个很吓人的数字，对我们来说是好事，并且我们已经有比较好的进展。

最重要的还是底层有 tech vision 去预判 GPT-5 和 GPT-6 应该是什么样，然后提前去执行和积累，不然永远都不可能超越 Open AI。OpenAI 的很多红利也在于提前预判，它在 2018 年就大概相信自己在探索正确的方向，花了很长时间积累。

 **海外独角兽：****让你来做图片生成这种产品的话，你会怎么做？怎么兼顾语言理解和图片质量？**

**杨植麟：**现在 Midjourney 在图片生成这个单一任务已经做得特别好了，我来做的话会希望它能做很多任务，同时在其中的一些任务也能做得很好。这其实也是 OpenAI 的思路，只是它其实没做成功。

AGI 公司应该是入口逻辑，让用户默认用你，此外特定人群会有一些特殊需求和对极致效果的追求，所以市场里还存在 Midjourney 之类公司的机会。但是 AGI 的通用性足够强大时，很多用户也会转移 —— 如果今天我把 Photoshop 整个软件都重新封装成一个 prompt，它变成大家一个外包的全能设计师，那会有更少的人用 Midjourney。

Midjourney 今天的地位在于它通过先发优势让飞轮跑起来了。比较 tricky 的是未来还会不会有这种时间窗口，如果没时间窗口，那很可能直接被通用模型碾压。

 **海外独角兽：****沿着入口逻辑的话，你觉得未来会有几个入口？**

**杨植麟：**至少有两个，**一个是有用的，一个是好玩的。**

信息入口可能不存在了，因为我们搜寻信息本质上是希望端到端完成一个任务。智能的入口以后大概率会覆盖搜索引擎这类信息入口。人获取信息并不是终极需求，它只是一直被强行定义成一种需求。有些时候我们是希望完成一件事，有些时候是希望学习某个东西，AGI 的入口应该直接帮用户完成任务，而不是帮他们获取信息。

 **海外独角兽：****从今天到实现你理想中的 AGI 还需要多少钱？**

**杨植麟：**严格的 AGI 还需要百亿美元级别。但是它不是一步到位，你需要跑起来一个循环，业务能够自己产出对应的资源。这个百亿美元推论的原因是 scale up 的规模还需要至少 2-3 个数量级。当然，过程中会伴随着成本的优化。

 **海外独角兽：****AGI 公司的商业模式应该是什么样的？还会是 seat-based 或者 usage-based 吗？**

**杨植麟：**AGI 帮你完成的每个任务对应的价值不一样。它可能类似一个外包，按照每个任务定价。除此之外，在任务解决过程中，广告肯定还会扮演重要角色，基于个性化互动和对话的行为，广告的变现效率可能比现在要高很多。

 **海外独角兽：****假如 GPT-4.5、Claude-3、Gemini-2.0 的训练成本是 3 亿美元左右，再往后到 2025 年下一代模型的训练成本可能要涨到几十亿美元，那要探索出 AGI 会是一场千亿美元豪赌，你思考过它最终对人类社会的影响吗？**

**杨植麟：**相对确定的一点是实打实的生产力提升。现在用一个软件，其实对应 1000 个程序员的智能，是固定的，以后我们用的应用背后可能对应 100 万个人的智能，而且每天都在迭代。

看可能性的话，今天的一切都会变化。这么多语言被训练到一起，对文化、价值观都有影响。人的时间分配可能也会产生很多变化，真正为了钱工作的人可能会变少，更多时间可能花在精神世界里面，最后可能会有一个巨大的虚拟的精神空间。要实现 Metaverse，可能其实是要先实现 AI。

另外，我相信 AGI 最终是全球化的。

 **海外独角兽：****但是现在我们判断领先的模型又强又便宜，会有很强的马太效应，最后格局还是很收敛。**

**杨植麟：**5 年的时间窗口的话，头部效应还是会明显。但是 50 年之后，我相信 AGI 肯定是同质化的，跟今天的电没有什么区别。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

延伸阅读

Perplexity CEO：AI 创业公司要先做产品，后做模型

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

八问Canva：在AI时代称王还是落败？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

新摩尔时代：拾象 2024 LLM 猜想

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgyKZyCCAoulic3qyakf7NdAePElibrpziaXeoR3fV1Xk9QYACFEAPAOLZb7TzG0xPibictORMIFoxRDTGQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

专访VideoPoet作者：LLM能带来真正的视觉智能

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgyKZyCCAoulic3qyakf7NdAePElibrpziaXeoR3fV1Xk9QYACFEAPAOLZb7TzG0xPibictORMIFoxRDTGQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

跨年对谈：千亿美金豪赌开启AI新摩尔时代

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgyKZyCCAoulic3qyakf7NdAePElibrpziaXeoR3fV1Xk9QYACFEAPAOLZb7TzG0xPibictORMIFoxRDTGQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)