---
url: https://mp.weixin.qq.com/s/Hamz5XMT1tSZHKdPaCBTKg
title: "专访VideoPoet作者：LLM能带来真正的视觉智能"
description: "tokenizer是被严重忽视的一个领域，值得发力去做。"
author: "拾象"
captured_at: "2026-03-08T11:19:26.020Z"
---

# 专访VideoPoet作者：LLM能带来真正的视觉智能

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/3tHNibnJ2jgwDRQWBU8kk8EJ135GiaQ15r3upgxFZF9LEJULicBzan6etZx9EcFyRoPia584sBjyXk1ictoDBDVrE8w/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwDRQWBU8kk8EJ135GiaQ15ryvibyojF8sCS7Xz5gwO8kibE2VYrpcDaHXsFHWetCnsg2W6aJ2AP4YWA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwDRQWBU8kk8EJ135GiaQ15rC7R72ohqT9WiaH7TLg2olTP18z2ewzYmM9kZekcqNt5RvrhTYjU6kUA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

采访：penny、Kefei    

编辑：Siqi、penny

排版：Scout

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwDRQWBU8kk8EJ135GiaQ15rOldA7IHdnpvUkiaFd47W6wT7vewGr5mwb4M5bOFpe4x9Hz7qichwro9A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

在 AI 领域，近年来各个子领域都逐渐向 transformer 架构靠拢，只有文生图和文生视频一直以 diffusion + u-net 结构作为主流方向。diffusion 有更公开可用的开源模型，消耗的计算资源也更少。

不过，最近视频生成领域也出现了效果惊艳、基于大语言模型架构的成果—— VideoPoet，让大众看到了 transformer 和 LLM 在视频生成领域的强大可能性。

VideoPoet 是 Google 近期发布的一个专注于视频生成的 LLM ，能够一站生成视频、音频、支持更长的视频生成，还对现有视频生成中比较普遍动作一致性提供了很好的解决方案。除了效果惊艳，VideoPoet 值得关注的另外一个原因在于，和绝大多数视频领域模型不同，VideoPoet 并没有走 diffusion 的路线，而是沿着 transformer 架构开发，将多个视频生成功能集成到单个 LLM 中，它的推出以及它所呈现出的效果，是 transformer 在视频生成任务上拥有极大潜力的有力证明。作为一个全能的视频生成 foundation model，VideoPoet 接下来还会发布更多功能。

本文是海外独角兽对 VideoPoet 项目的 research lead 蒋路的深度访谈 (http://www.lujiang.info/)。Lu Jiang 一直专注于视频相关研究，从 2019 年就开始尝试将 Transformer 用在图像、视频生成研究上，在访谈中，他详细分享了自己对于视频生成领域技术路线的思考、为什么很早就坚信 transformer 在视频领域的潜力，以及 VideoPoet 项目里关于 tokenizer 的核心创新。

蒋路认为，视频生成领域的“ChatGPT 时刻”预计会在 24 年底或 25 年中实现，到那个时候视频生成已经可以达到好莱坞样片级别的效果。放眼更长远的未来，视频生成研究更加终极的目标是追求 “visual intellegence”，人工通用智能也会在视频生成中实现。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**01.**

**视频生成的技术路线**

 **海外独角兽：****在视频生成领域，最合适的技术路线还没有收敛。你会怎么给已有的技术路线分类？**

**Lu Jiang：**现在的技术路线大致可以分为两大类（这里不包括 GAN 延续的工作）：一类是基于 diffusion 的技术，另一类则是基于 language model 的技术。举例来说，我们最近发布的 VideoPoet 是典型的基于 language model 的路线，我们组的另一个工作 WALT 则是基于 diffusion。也有人用 token-based 来区分基于语言模型的技术和基于 diffusion 的技术，但我认为这种说法不太准确，因为 diffusion 里面也有 token 的概念。

基于 VideoPoet 制作的短片 *Rookie the Raccoon*

diffusion 技术迭代过几次了，从最早的的 pixel diffusion 发展到第二代 latent diffusion，再到第三代 latent diffusion with transformer backbone， **diffusion 路线现在是绝对主流，大约 90% 的研究者都在这个领域探索。**

基于 language model 的技术其实比 diffusion 出现得更早，2020年的 ImageGPT 和后来的 DALL-E 都是引入这个概念的，但到 DALL-E2 就换成了 diffusion。Google 的 Parti 模型也是利用语言模型实现文生图。

基于语言模型的工作又可以分为两类：一类是以 mask language model（例如BERT） 为主，比如 Google 的 MaskGIT，属于奠基性的工作，后面比较出名的是 Muse 文生图模型；另一类是基于自回归（auto-regressive）的语言模型，这个更接近于现在 LLM 的逻辑。

💡

**MaskGIT：**Google Research 在 2022 年 2 月发布的图像生成模型（对应论文为 *MaskGIT：Masked Image Generative transformers*），MaskGIT 改进了 VQGAN 的串行序列生成模式，通过并行解码（parallel decoding）提升生成效率，最高加速 64 倍，MaskGIT 还进一步提升了图像生成质量，可以支持类别条件输入，也可以用于图像编辑和扩展。不过 MaskGIT 不支持文本引导图片生成。

**Muse**：Google 在 2023 年 1 月发布的文生图模型（对应论文：*Muse：Generation via masked generative transformers*）。不同于 diffusion 或自回归模型的方案，Muse 是在离散的 token 空间上基于 Mask 方式进行训练，在当时获得 SOTA 水平，并且生成效率更高。

但实际上，diffusion 和 large language base 这个分类更多是方便我们理解，随着时间的推移，**这两个概念的内涵是在不断扩展延伸的，尤其是 diffusion 也在不断地吸收和学习来自语言模型的方法，它们之间的界限变得越来越模糊。**

 **海外独角兽：****为什么说 diffusion 也在不断学习语言模型的东西？怎么体现在 diffusion 的发展和迭代中？**

**Lu Jiang：**第一代 diffusion model 是 pixel diffusion ，这种方法处理速度较慢，尤其是在处理大量像素，比如高分辨率图像时。所以，**如果直接在视频任务上应用 pixel diffusion 就会相当挑战，因为视频是一个三维空间。**为了解决这个问题，行业早期采用的是级联（Cascade）的方法，先使用一个小型模型进行渐进式生成，然后逐渐扩大模型规模，再把四到五个模型串联在一起。

Diffusion 的一个重要突破是引入了 latent diffusion，相关研究是 High-Resolution Image Synthesis with Latent Diffusion Models，这个是 stable diffusion 奠基性的工作。它最基本的思想是首先将高维数据，比如一个很大的图像，降维到一个 feature，这个其实就是用 token，再在这个 feature 上做 diffusion，完成后再把特征空间投射回图像空间。latent diffusion 的研究团队之前就是做语言模型的，这个思想其实就是从语言模型那里来的，从 latent diffusion 的研究文章我们也可以看到，第一个所谓的 tokenizer（分词器）是从语言模型中引入的。

💡

**Tokenizer：**将文本或序列转化为标记（tokens）的工具或算法。在自然语言处理（NLP）领域，tokenizer 通常用于将文本分割成单独的单词、短语或符号，这些单元被称为标记。在生成模型中，tokenizer 的作用是将连续的输入序列转换为离散的标记，这些标记可以被模型理解和处理。上述的 diffusion model 采用的是 tokenizer 转化为连续的标记。

**第二个比较大的里程碑是将 U-Net 架构逐渐转换成 transformer 上**，这里的代表研究是 DiT，这是个比较自然而然的过程，因为 transformer 架构能力更强、更能做生成。

对于基于 transformer 的工作，不管是 latent diffusion 还是 language model，它们之间的区别很小，都是 token-based，最大的区别在于基于 diffusion 的生成是连续的 token， language model 处理的是离散的 token。

 **海外独角兽：****你提到目前有 90% 的视频生成研究者都做的是 diffusion 路线，为什么 diffusion 会是主流？**

**Lu Jiang：**我们要把 “研究成果”和“真正 avaliable”分开看。现在之所以这么多人用 diffusion，**最大的原因是 stable diffusion 是一个最好的开源模型，它完整影响了整个生态圈。因为 99% 的论文不可能重新训基础模型，都是找一个已有模型再在它的基础上做一些尝试。**

**在理解生成模型时，可以分两个层次：基础模型和应用。**基础模型的目标是实现整体的最佳性能，但可能不关心某个具体应用场景。根据（Bommasani等人 2021）定义， foundation model 有两个特性，第一可以赋能 sample efficient learning，如果训练出这个 foundation model，用户在解决具体问题时可能只需使用 1% 的数据或更少，第二个就是所谓的 coverage，模型可以用来做任何事，只要微调都能用起来，现在的 NLP 基本上就是这样，拿我们的工作举例，VideoPoet、WALT 和 Muse 等这些模型都是 foundation model。

相对于 foundation model 的就是下游的 application model ，从 foundation model 出发，针对特定任务优化，比如大家现在看到的跳舞、Control-Net 以及各种视频编辑、风格化（stylization）等等，都属于下游应用。

很现实地说，绝大部分高校很多研究者都没有能力做 foundation model，需要的资源太多。在 stable diffusion 之前，DALL-E 的出现极大地激发了研究社区的兴趣，DALL-E 相比 GAN 在生成、计算和多样性等方面都有本质的提升。社区中有很多人尝试重现 DALL-E，比如，有网友做了 mini DALL-E，但质量惨不忍睹，社区很缺一个“可用”的模型。开源模型 stable diffusion 的出现填补了这个空缺。

在 2022 年那时候，Stable diffusion 和 DALL-E 、Google Imagen、Google Muse 相比，不一定是最强的模型，但确实是最公开可用的模型，后续工作都是在它的基础上构建的，对社区有本质的影响。

这也是为什么视频生成领域也受到 stable diffusion 路线限制，因为现阶段的视频生成研究通常先从图像出发，把“帧”先生成出来，然后尝试减少一些不一致性、再播放成为一个视频，**目前阶段的视频生成更像是“幻灯片生成”**，我相信市场上都不认为这是最佳方法，但如果要生成一些可看的内容，这是唯一能做的方法，**开源社区上的资源在很大程度上限制了我们能做什么。**

最近推出的 stable video diffusion 会极大地改变这一现状，作为了一个视频 foundation model，stable video diffusion 的出现也会对现有的应用，比如编辑、稳定化，带来明显进步，因为之前的问题或许已经被这个新的 foundation model 解决了，现在生成的东西本身就具有时间一致性。可能在未来的一年或半年内，许多研究工作将不再走之前的技术路线，而是从 stable video diffusion 开始。虽然我个人觉得当前的 stable video diffusion 肯定不是最优的技术，但它是目前唯一可用的，大家可以在它上面持续做东西出来。

 **海外独角兽：****随着基于 diffusion 和大语言模型的技术之间的界限变得模糊，是否意味着越来越多的研究者会转向使用 transformer 架构？**

**Lu Jiang：**我觉得即使在基于 diffusion 的路线中，使用 transformer 也会是个趋势，因为 transformer 更 scalable，这是大家的共识。我了解到 diffusion 最大的模型也就 7 到 8 个 billion 参数规模，但 transformer 模型最大可能已经达到 trillion 级，他们是完全两个量级。

为什么 diffusion 没有训出更大的模型？我认为肯定有人试过，但没成功。不是说 diffusion 不能 scale，而是要考虑花多大体量的资源和资金才能实现这件事。在 NLP，大公司花了 5 年时间、投入数百亿美元，才把模型做到现在规模，而且，随着模型规模的增大，对于所有公司来说，scaling、包括 model parameter 变成了 top secret，search 大模型架构成本也成倍增长。

**所以对于 diffusion 来说，我不觉得没有 scale 的可能，只不过从 U-Net 转到 transformer 的话，可能就能利用之前的学习配方（ learning recipes），大大降低搜索这种架构的成本。**

 **海外独角兽：****用 LLM 的架构做视频生成模型，和给一个 LLM 比如 ChatGPT 加上多模态能力，这两者有什么区别？**

**Lu Jiang：**本质上说，基于 language model 的视频模型仍是一个语言模型，因为训练和模型框架没有改变。只是输入的“语言”扩展到了视觉等其他模态，这些模态也可以离散化表示为符号。对模型来说，理解其他模态就像理解一种外语。我认为当前难点在于让 LLM 理解多模态任务，只要表示方式设计得当，LLM 模型可以无缝理解和生成。

所以不需要专门设计新的模型结构。只要模型理解了以后，输出形式也很灵活，可以自然的组合不同模态，实现多模态的生成，这方面也有很多相关研究。

**02.**

**VideoPoet ：LLM 能带来真正的视觉智能**

 **海外独角兽：****最近发布的 Video Poet 和 WALT 都用了 transformer 架构，效果也都很惊艳，大家也都觉得看到了 diffusion 路线之外的新趋势。这些研究的背景是什么，对视频生成领域的主要贡献是什么？**

**Lu Jiang：**VideoPoet 和 WALT 是我们最近发布的工作，VideoPoet 是一个基于 language model 的 video foundation model，它的目的就是想做一个模型，把所有关于视频的功能囊括到里面。WALT 是与李飞飞老师和其学生合作的项目，WALT 基于 diffusion，但也使用了 transformer 。有意思的是，这两个模型其实用的是同一个 tokenizer 架构叫 MAGVIT-v2，它们之间的关系其实非常紧密。WALT 和 VideoPoet 使用的 tokenizer 层不同，WALT 用的是连续层（微调后），VideoPoet 采用离散层。

VideoPoet Overview

VideoPoet 的贡献在于，它提出的视频生成方法在生成动作时能保持很好的一致性，尤其是大范围 motion 的连贯性，这是很强的贡献，另一个贡献是实现多种任务的一站式处理，和生成长度 10 秒视频。技术上的贡献或许没有多么复杂，**这篇工作的主要意义是让社区重新认识 LLM 在视频生成上会扮演很重要的角色，它可能比人们当前的认知要强很多。**

 **海外独角兽：****大动作、一致性等问题是视频生成的难点，LLM 能更好地解决这些难点吗？**

**Lu Jiang：**我个人觉得视频生成的难点是 motion 部分，现在图片生成的方向是高清细节，但在视频里，人对动作是很敏感，一些奇怪的行为一下就能发现。目前市场上大部分视频生成的公司基本上做的都是运镜、非常小的动作，再加上 camera 的不同模式，很少有大动作，这对于现有的 diffusion 来说非常吃力。我的理解是**因为它们没有很好的能建模运动的 tokenizer，这也是为什么 WALT 的 motion 能做的比它们好。**

我认为 motion modeling 属于很头部的问题，尤其是复杂动作的连贯性。

2019 年时我就见识了 transformer 的强大。那时通过合作，我也在做NLP方面的研究，和当时大多数视觉领域的人相比，我特别相信 transformer ，**当时我的研究小组有个明确的目标，就是必须采用 transformer，所以在 GAN 时期我们已经逐步把 GAN 架构替换为 transformer**，当然后面 GAN 也逐渐退出历史舞台了。

后来我们研究 Mask Language Model，为什么做这个呢？Mask 首先这是个 transformer，当时解决的是速度问题，因为 auto-aggressive 太慢了，diffusion 当时会更慢，但 Mask 可以很快生成，在 2022 年 diffusion 需要 1000 步的时候，它可能就只需要 8 步了。

做 Mask 的过程中我们提出了 MaskGIT，认为可以用 Mask Language Model 的方式做图像生成，是把这件事做到了 text-to-Image 上。

我们在开发 Muse 时，曾有过一段时间可以与 stable diffusion 的某个版本进行比较，因为当时我们的训练数据是一样的，所以能比较客观地比较，我们的结论是，MaskGIT、Muse 这种语言模型的作品在质量要略高于 stable diffusion，速度也要快很多，在一些计算口径中这种速度差距能到几倍。

当时 Muse 刚出来的时候，也有网友呼吁我们开源，但出于各种原因没有开源。如果当时开源了，可能现在的开源社区的研究格局可能会有所不同，比如可能同时有些人研究基于 language model 路线，有些人研究基于 diffusion 的路线。而且 Muse 当时在速度上非常有竞争力，diffusion 可能花了大半年时间才追上，所以如果当时开源的话可能推广性也很好。

**我一直很坚信 language model 的方法，从我内心来说，我不认为 language model 比 diffusion 差，所以我一直主张坚持这一路线，比如后面包括用 auto-aggressive 与 LLM 结合。**

做完 image 之后，我们就转向了视频。对于视频，我的信念是一定要使用 transformer，虽然在视觉领域中使用 U-Net 依然是主流，这也是为什么 WALT 即使是用 diffusion，我们仍然要使用 transformer 的原因。

 **海外独角兽：****为什么你这么早就坚信 transformer 路线，这会是未来视频生成技术收敛的方向吗？**

**Lu Jiang：**我所说的 transformer 、language model 以及 large language model（LLM）是一样的意思，因为这两者在 NLP 中是几乎相同的概念。长远来看，比如未来 3 到 5 年，我个人认为 diffusion 可能会失去竞争力。

**首先，LLM 可能是人类历史上第一个能够窥探所谓 AGI 的模型**，而且是通过非常简单的方法实现，只要持续增长模型和数据，模型就能带来惊喜。在这之前的 AI ，我们基本可以知道它能做什么、不能做什么，但整体上不会“be suprised”，但现在，就像 OpenAI 的Ilya 说的，通过很简单的预测下一个 token 的操作，就能支持非常智能的应用，我觉得因为 transformer ，我们几乎已经敲开了通用人工智能 AGI 的大门。人类历史上提出了很多 AI 模型，这是唯一一个实现这件事的，我们为什么不把它的能力发挥到最大呢？

**第二点，未来 5-10 年，几乎不太可能出现一个新的模型挑战 LLM 在文本的地位。**然后现在越来越多的比如音乐生成、音频生成、机器人等领域主流仍然是 language model，最近 vision 领域也发生了变化比如GPT-V和Gemini，我看到的大概率 language model 也会把绝大部分 visual understanding 囊括。

**所以从大的格局上来看，如果所有领域的研究都进入到 LLM ，那么为什么视觉领域要被单独拿出来做？它到底难到多大程度需要我们单独处理呢？**因为单独处理意味着很多，从工程角度，要同时引入两套模型，会增加成本和优化难度。当然未来可能会发明一种 diffusion 和 LLM 混合使用的方式，**但生成仍然是要在 language model 内原生的，diffusion 更像是辅助的存在。**从大的格局上，我认为没有什么不可抗的困难要把图像和视频生成任务从语言模型中单独剥离出来。

我深信 LLM 的第三个原因是：现在的图像生成模型解决的问题类比到 NLP 来说相当初级，例如，让模型生成一张“戴红色圣诞帽的狗的图片”这样的任务，这在 NLP 中相当于生成“dog”、“red hat”和“on top of the dog”几个词语，人们不会觉得这是“智能”，只是换到图像模态，大家在视觉上觉得很惊艳，但这绝对不能代表是视觉领域的智能。

 **海外独角兽：****如果把大模型类比成人，现在只是有了语言，还需要眼睛和其他模态。怎么定义视觉和多模态的智能？为什么现在还没能实现？**

**Lu Jiang：**“智能”是一个整体思想，“模态”是人类智能的表现形式——语言是最抽象的，声音和视觉领域是语言的延伸。LLM 已经展示了语言智能，但还不是全部，类似于一个人有想法，但没有手画出来，没有途径表达出来。这是暂时的制约，不是 LLM 的本质缺陷。

未来谁能打败 Midjourney？一定不是在图像质量上竞争，现在的症结点已经不在这里了，大家现在说 DALL-E 比 Midjourney 好，我认为是说 DALL-E 的 prompt following 要更好，在 visual intelligence 语境下，prompt following 可能是最基本的。

用一个例子说明什么是真正的 visual intelligence，比如一个创业者想准备融资的 pitch deck，目标是能获得融资。这是个很任务导向的问题，把这个需求给模型，模型理解了问题后可能还会追问一些细节，例如投资人的背景等等，在这些信息基础上，输出一份满足需求的 deck，最终融资结果可能比人做得还好，这才是视觉领域中隐藏的真正智能。

Visual intelligence 是广泛存在于我们社会中的，甚至后面还可以接入 VR、AR。

我觉得 LLM 是有这个能力的，现在的局限是新模态中的理解和表达。现在有两条路来解决这个问题，一种是重起一套新模型让它实现理解和表达，这就是 diffusion 的思路，还有一个思路是，能不能想办法让 LLM 模型自己学习理解和表达新的模态？如果能够实现第二点，那么我们就真正解决了这个问题。

 **海外独角兽：****VideoPoet 和 WALT 这两个项目效果为什么这么好？其中有什么关键工作吗？**

**Lu Jiang：**WALT 和 VideoPoet 的相似点在于都使用了 transformer、使用了同一套 tokenizer 架构，就是 Magvit V2，这是我个人很满意的一项工作。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

💡

**Magvit：****Masked generative video transformer** 研究中引入了一个 3D 分词器，将视频量化为时空视觉 token，并提出了一种掩码视频 token 建模的嵌入方法，以促进多任务学习。

我们之前做了 Spae 的项目，Spea 的核心是做**图像和文本语义的互联**。我们发现，如果把这种东西接入到 ChatGPT 3.5、Bard 这种 LLM 里面，即使这些模型之前从未接触过任何图像，也能通过极少量的图像示例实现图像生成和 caption 描述，只需要十几张例子就能完成。**这个发现让我非常惊讶，一个之前完全没有接触过图像的语言模型，只需要少量的示例就能生成、理解图像。**后来我们就沿着这个思路，继续探索如何让语言模型更好地理解和表达视觉世界。

**这就是我们设计 Magvit V2 分词器（tokenizer）架构的初衷，也是 VideoPoet 效果好的最核心原因。**使用分词器的方法有很多人尝试过，比如很早之前的 VideoGPT 等，但效果并不理想，我认为关键在于 language model 虽然有足够潜力、但并不理解生成任务的具体目标是什么，**tokenizer 的存在就是通过建立 token 之间的互联让模型明确“我现在要做什么”，互联建立得越好、LLM模型越有机会发挥它的全部潜力。**

所以，如果模型不理解当前的生成任务，问题并不在于语言模型本身，而是我们没有找到让它理解任务的方法。

这也是为什么我们的研究叫做：***language model Beats diffusion - tokenizer is key to visual generation，***在这篇研究里面，我们和 ImageNet 这些项目在 benchmark 上相比证明了，**一个好的 tokenizer 接入到语言模型后，能够立即可以获得比当时最好的 diffusion 还要好的效果。**

我们的研究可能会让社区意识到 tokenizer 是被严重忽视的一个领域，值得发力去做，我也相信 tokenizer 会变得越来越好。

 **海外独角兽：****除了让 LLM 更明确理解任务，tokenizer 在视觉智能中还会起到什么重要作用？**

**Lu Jiang：**text 模态里面已经有 tokenizer ，在人类自然语言上万年的发展造就了现在“自然语言”系统。我们要构建的是视觉领域的语言系统。如果能把 tokenizer 做得更完善，随着能力进化，它连入 LLM 的能力就越强，我觉得是一个实现 visual intellegence 的方法。

如果想实现 visual intellegence，能不能只是把 LLM 和 diffusion 桥接起来？我觉得这是个好的过度方法， 但是最终可能性很低，因为这对桥的要求很高，要保证信息能够被准确传输，现在大多数桥是通过 cross attention 实现的，但真正的关键在于 transformer 的大计算量的 self-attention，现在这个桥的带宽会限制 LLM 的发挥。但如果把 tokenizer 的这种能力集成到 language model，就能和其他模态互联，很轻松地做 multi-task。

另外一个就是长度问题，diffusion 的生成长度通常受限，但在 LLM 里面，比如 music generation 可以做到 3 分钟，VideoPoet 的特点之一是 long video，借助LLM，不需要特殊处理就可以生成十秒，这些也是基于 tokenizer 实现的。我们之前尝试了很长时间，效果不佳，但解决了 tokenizer 问题后，LLM 的生成效果完全不同了，现在的 tokenizer 还可以变得更好，一定能产生更卓越的效果。

 **海外独角兽：****要做出好的 tokenizer 最大的难点是什么？Magvit V2 的成功主要突破了哪些难点？**

**Lu Jiang：**难点主要是压缩问题，语言模型的逻辑是压缩器，但视频序列相比文本来说信息量太大，现在的 LLM 更适配于自然语言的处理，虽然现在很多模型说自己能处理更长的 context，但这是建立在文本数据的前提上。**文本中的依赖关系较弱，可能偶尔有些词汇存在依赖关系，但视频中依赖关系要强很多。**

所以如果要让 LLM 表现好，**需要把 sequence length 压缩到一个合理的范围****内，难点在于怎么设计压缩。**有个领域叫 Neural Compression，专门研究怎么把视频压缩到一个很小的内存上。有一类观点是“压缩得越好，生成得越好”，其实不是，可能现在我们还没理解这两者的联系。压缩不仅要追求压缩率，还要保证压缩后能把高质量的信息准确传递给 language model，我们攻坚的也是这个问题。

我们花了 3 年半的积累才最终设计出现在的 tokenizer，在2021年做图像生成的时候，我们就发现 tokenizer 就是很关键的环节，这里有很多技术细节，也包括一些 GAN 的东西、怎么评估压缩效果等，都是需要去攻克的，还有个难点是怎么判断压缩得好还是不好，我们团队也是做了上千组的实验才找到方向。

 **海外独角兽：****和文字相比，视频数据体量很大、但信息密度低，模型处理起来也很困难，这个问题要如何解决？tokenizer 也会在这个环节发挥作用吗？**

**Lu Jiang：**如果做视频理解，只需把关键信息拆出来就可以压缩得很小，但问题在于如果要做生成，怎么把细节重构出来？只靠几个字是不够的。

Spae 这篇论文中就意识到了这个问题，里面的思想我认为很好。Spae 提了一个叫做“金字塔结构”的方法，在压缩的时候就呈现成一个“金字塔”，上层保留核心语义信息，越往下越细节，如果做理解相关的任务，只需要取上面层的数据就可以，如果进行视频生成，可以向下移动到金字塔的更深层，因为需要恢复细节。

这个方向很有趣、很值得进一步探索，因为任务对表示的细节有不同的需求。例如，对于高清视频压缩任务，压缩后的表示必须能很好地重构并展示所有细节，用于生成的表示也必须保留足够的细节，方便后续高质量地重建内容。

💡

**Spae：**Google 和 CMU 在 2023 年联合发布的基于 LLM 的多模态语义金字塔自编码生成模型，Spae 实现了一种向量化的映射器，将图片这类非文本的多模态信息先编码映射到大语言模型的词汇空间中，实现图片到文本转译，再通过金字塔形逐层细化的图片文本转译，从而实现对图片的文本化精确理解。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Tokenizer 的另外一个价值在端侧，现在大家都在提“未来是 on-device 的天下”，要真正做到这一点也需要 tokenizer 的加入。**

用 Magvit V2 举例，如果不把它看成生成模型，看作是一个压缩模型，它把视频压缩成一系列离散的语义 token，这些 token 再转换回视频，就完成了压缩和解压的过程。从压缩比来看，这种方法已经超过了当前主流的 H265，接近下一代视频编解码标准 H266 的性能。

对于 on-device 来说，我认为这个特性相当重要。我们进行视频的修改，是从视频解码这个环节开始，再把解码后的 code 放在内存，再通过一套方法生成，链条会特别长。但如果从 token 开始，首先在存储上的要求变得更友好了，其次，节省了很多前序处理的环节和内存，直接拿到的就是模型需要的东西，然后再直接输出。

在这个模型里，生成和显示或许是同一件事，模型可以直接输出显示的视频，也可以直接用于生成新的内容，比如视频从横屏变成竖屏可以瞬间完成，因为对于生成来说，它在做渲染的时候也可以生成，而不是分成两个模型来做，**所以接下来视频的修改会变得非常容易**，在未来竞争中也会变成重要武器，因为 tokenizer 实现了本质上的速度提升。

 **海外独角兽：****从 token 开始处理视频意味着在视频的解编码模式在未来也会被替代？**

**Lu Jiang：**理论上可以，但需要长远的发展，模型越做越好肯定会超过，但受制于一些实际应用层面的问题，这些问题还需要再优化，比如 token 逻辑下 neural network decoding 的速度是个瓶颈，还未涉及到 CPU 的优化等等，有很多类似技术上的考量。但我觉得社区能持续做优化，这件事就是非常有可能的。

另外当前是因为**视频解码编码已经有一套固化的 infra 了，新东西如果想改变它，就必须比它好很多倍。可能到下一代，视频的生成和显示是一体的，这就是本质上的上升，人们在玩手机上编辑视频可以是瞬间的，就可以把一些显示出来、一些生成出来，或者混着去做，这是现在的解编码的压缩还是无法做到的。**

 **海外独角兽：****VideoPoet 现在已经可以实现了一些可控性，如果想让可控性更强，比如通过对话就可以实现精准控制和生成、甚至具有前面提到的 intelligence，还需要做哪些突破？**

**Lu Jiang：**我一点也不担心精准控制的问题，因为这是典型的下游的问题，只要 foundation model 越好，下游研究和应用的效果就会更好，比如基于 SVD 做视频生成不再是基于每一帧残影的 slide generation。我们开源社区的创造力非常另人赞叹，到后面各种各样有趣的应用都会实现（故事生成）。

也有人认为不同的 foundation model 有自己的特点，可能有的问题在新的 foundation model 上就不存在了。举个例子，StyleDrop 作者在 Muse 模型和 stable diffusion 上都尝试 StyleDrop 的工作，Muse 模型本身就能表现得非常好，但 stable diffusion 需要做进行大量调整，且最终效果也不够理想。

💡

**StyleDrop：**Text-to-Image Generation in Any Style研究的核心结果，是一种通过文本到图像模型实现忠实地遵循特定风格的图像合成方法。StyleDrop 能够捕捉用户提供的风格的微妙细节，如颜色方案、阴影、设计模式以及局部和全局效果。它通过微调极少量的可训练参数（占总模型参数的少于百分之几）并通过与人工或自动反馈的迭代训练来提高质量，高效地学习新的风格。即使用户只提供了一张指定所需风格的单一图像，StyleDrop 也能够产生较好的结果。

 **海外独角兽：****VideoPoet 未来有什么产品方向的计划？**

**Lu Jiang：**VideoPoet 可能会选择以某种产品的方式跟大家见面，比如 API 或者集成到 Google 的现在现有产品的生态圈。

 **海外独角兽：****视频生成的 foundation model 存在我们在语言模型中看到的 scaling law 吗？当架构和技术路线确定后，竞争的关键是否就成了数据、模型的scale问题？**

**Lu Jiang：**我们论文有一些关于 scalling 的内容可以作为参考：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

💡

随着模型规模的增长和训练数据量的增加，性能会有所提升。Video Poet 训练了具有 3 亿、10 亿和 80 亿参数的语言模型，分别在包含 10 亿、37 亿和 58 亿视觉和视听 token 的数据集上进行训练。增加模型规模提高了时间一致性、提示保真度和运动动态性，同时增加了有限文本渲染、空间理解和计数的能力。

通常来说，大公司相比创业公司，在数据方面限制更多。但与此同时，数据规模和模型规模应该匹配。**小模型配大数据集可以工作，但大模型配小数据集一般不行。最理想的情况还是大模型配大数据集。**

所以 stable diffusion 其实还没有成功地 scale，可能它的数据已经很多了，但如果能做到 scale 可能会发挥更多实力，相比起来，我们的观察是 transformer scale 起来更容易，而且 transformer 有很多现成的学习配方（learning recipes）。

 **海外独角兽：****在 LLM 路线上，视频生成要做到较高质量，需要的 GPU 是什么量级？**

**Lu Jiang：**目前视频生成方案还不够稳定，仍需要继续探索一个不同的模型，还不到某个质量阶段化，具体的需求就很难去讲，现在这个阶段过早地做模型的 scale 可能也不是最合适的，但 tokenize 之后的视频其实是存储友好的，因为它实际上和文本一样都是 token，不过压缩的长度更长，这可能是之后研究的一个核心。

**03.**

**视频领域的 GPT 时刻**

 **海外独角兽：****你会如何定义视频生成的 “ChatGPT 时刻”，什么时候会到来？**

**Lu Jiang：**视频生成的“ChatGPT 时刻”，我觉得大概是，哪怕模型生成的还是比较短的片段，比如 2-5s，但这个生成是可控的，人类也很难分辨是 AI 生成还是人类制作。从用户角度，只需要几美分的代价，就能获得一个可以被送到好莱坞专业 studio 的样片。如果类比的话，可以类比到图像领域 stable diffusion 1.x 或 2.x 版本，肯定还有再提升的空间，但已经到了能使用的程度，而且能激发很多应用。

**我的预测是，到 2024 年底或 2025 年初，我们可能会到这个时刻。**并且我认为，实现这个时刻肯定也需要 diffusion 参与，并且 diffusion 在未来一段时间，比如 1 到 2 年内，可能仍然是主流，扮演很重要的角色。这里说的 diffusion 已经包含了 transformer。

“ChatGPT 时刻”意味着模型到了一个相对稳定的阶段，但后面还会再改，只不过是在这个基础上做小的改动，可能一开始版本只能做到逼近好莱坞，有一些缺点，但可以商业化运用了，但要达到真正稳定需要更长时间。随后还可能仍会迭代升级。

现在市场上所有的视频生成都达不到这个标准，所以我认为视频生成的方法可能还需要进一步迭代，有可能要达到“ChatGPT 时刻”需要新的模型和方法，它不一定是全新的模型或者架构，可能是现在市场上的某个技术路线或者方案再往前走一步。

 **海外独角兽：****视频生成技术会和文生图一样 commoditize 吗？如果选择 LLM 的路线，是不是会更容易拉开差距？因为资源、能力、技术壁垒带来的差距会更大？**

**Lu Jiang：**我觉得可能会和 image 很像，但取决于几点：

开源社区也有很好的 LLM 作为支持，如果想做也可以走这条路线，但重点还是要攻克 tokenizer 技术，我相信会慢慢赶上。

**视频生成的主要竞争力可能在于数据上。**因为视频是版权保护最严格的，当前大部分视频平台要花很多价钱去购买版权或与视频创作者去分享利润。

未来总会有部分人实现更先进的技术，并影响整个领域，可能会有一个提前量，几个月或者一年，但总会有人追赶上来，**我觉得可能最终关键不是看技术，而是怎么把技术放到用户的手里。**Midjourney 就是一个典型，Midjourney 已经做得很成功了，但是其实它可能不是一个很好的产品，因为其很容易被替代。所以更核心的是怎么把同一套技术更好地放到产品里。

Video 和 image 还有一个非常大的区别，视频具有更广泛的应用场景，用户在视频上花的时间要比图像多非常非常多，所以视频领域的 foundation model 可能有很大潜力衍生出新的商业模式，就像短视频的模式对视频的改变一样，短视频从技术上讲是很小的改变，但创造了一个新的模式，所以视频生成的潜力有可能会更大。

 **海外独角兽：****我们也经常讨论这个问题，视频生成其实相当于把拍摄和后期的很多过程省掉了，能够影响的产业很多。**

**Lu Jiang：**降低视频制作成本还只是视频生成发展的起步阶段，接下来的方向可能会是所谓的 “personalized movie”，模型根据每个人的背景、想法生成个性化的结果。

再比如现在大家看短视频是随着“下划”，推荐算法会帮忙“找”出更符合用户兴趣的内容，也许在生成技术足够成熟的时候，随着用户划动，系统会自动生成他们更想看的内容，这是一种真正意义上的变革。

 **海外独角兽：****为什么最近半年视频生成领域成为热点、甚至有“井喷式的重复”的感觉？**

**Lu Jiang：**一方面是因为这个领域逐渐成为关注热点，越来越多研究力量涌入。另一方面也因为现在技术发展很快，但当前大家技术路线和方法差异不大，模型框架基本上都是基于 stable diffusion，主要就是数据和模型细节上的比拼，所以会出现大量“井喷”的工作，做的早的团队有一定优势，但技术更替很快，也很容易被追上。**如果技术上有长足的创新，可能就会一下子拉开差距。**

 **海外独角兽：****能够在技术上做到实质性突破的团队画像是什么样的？需要 Ilya 之于 OpenAI 这样方向领袖型的人？还是团队一起突破？**

**Lu Jiang：**目前阶段如果要实现一些突破性只靠一两个人是不行的，但是也不需要很多人，可能核心人员 4-5 个左右、再加上一些支持性角色就可以实现。现在 diffusion 其实很大程度上都受益于 Jonathan Ho 等关键科学家的研究。

我非常钦佩早年推广 diffusion 的学者，比如 Google 内部的 Imagen 和 David J. Fleet 的团队，他们 diffusion 这条一路走过来很艰难，他们从 16 年开始，当时大家都不看好，因为当时 diffusion 比 GAN 质量差非常远，又慢 1000 倍，但是他们就一直坚持做，直到真正把 diffusion 变成主流。我觉得有自己有信仰是科学家一个非常崇高的品质。

技术并不成熟的时候，是需要由领袖人物来做出重要突破的，但现在不一样的一点是资源分配很不公平，所以现在可能需要一个非常有能力的团队，以及充足的计算资源和 support 来不断创新。

另外，视频生成相对特殊的一点是，需要大量的计算资源。从事机器学习的人大多数是专注于图像领域，做 text 或 image，而视频相对较少，因为视频领域的计算力门槛相对较高。但是视频有自己的一些逻辑和理论内在的东西。如果在这视频方面有经验，这些经验是可以大量迁移的，可能能用很少的计算资源找到一个好方向。如果计算资源有限，有经验的人能更合理地设计，把每件事都想到极致。

 **海外独角兽：****你在研究过程中有遇到什么困难吗？**

**Lu Jiang：**在2022年，我们在做 Magvit 的时候，当时 Google 有另外两个重点项目，Phenaki 和 Imagen Video，我们的团队规模非常小，能够使用的 Google 计算资源也非常有限，可能和大学的 lab 一样，差不多是其他项目的 1% 左右。当时，这些团队都在做 text-to-video，我们忍痛放弃，并且最终决定开发 video-to-video也就是Magvit。最终，在条件非常有限的情况下，我们从 benchmark 上是显著高于 Phenaki 的，这个过程中我的压力很大，我的家人也给了我很多支持。

我认为这就是因为我们自己的经验和方法，在设计过程能节省很多计算资源。我已经在视频领域工作了十多年，我们也有一套自己的方法论，比如怎么提升性能，我们在视频处理上已经掌握了大量 know-how，这些可以在不同的项目中迁移。

 **海外独角兽：****你在视频领域做研究十多年，这种热情源自于哪里？**

**Lu Jiang：**主要还是科研上的热爱，我对视频的热爱主要体现在我一直以来的科研工作上。我大部分时间都在处理视频相关的问题。我研究的领域属于 multi-media 科学领域，是多模态科学领域。

我个人很喜欢看视频（YouTube, B站等等），和解决视频领域的问题，在这个领域也投入了很多时间。例如一些设计，我想能够想出来，也只是因为我在这个领域的时间相对较长。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

延伸阅读

跨年对谈：千亿美金豪赌开启AI新摩尔时代

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Speak：用LLM重塑语言学习，再造一个Duolingo？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Mistral AI：开源不是威胁，模型变小才能催生Agents

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwDRQWBU8kk8EJ135GiaQ15rsqAyark7zaDibfvtqpxGqPHFibiaPr7sMU4Xd2pPEiaopxK3r3Ij3K5r9g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

LLM-first IDE：Code Agents 超级入口，软件开发的“Excel 时刻”

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwDRQWBU8kk8EJ135GiaQ15rsqAyark7zaDibfvtqpxGqPHFibiaPr7sMU4Xd2pPEiaopxK3r3Ij3K5r9g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

Filming Less：AI时代的视频剪辑产品淘汰赛

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3tHNibnJ2jgwDRQWBU8kk8EJ135GiaQ15rsqAyark7zaDibfvtqpxGqPHFibiaPr7sMU4Xd2pPEiaopxK3r3Ij3K5r9g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)