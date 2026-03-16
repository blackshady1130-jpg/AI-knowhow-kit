---
url: https://mp.weixin.qq.com/s/H8UYQ27nNPbW2jetseJgYQ
title: "去魅Sora: OpenAI 鲜肉小组的小试牛刀"
description: "本文分为两大部分，第一部分是技术探讨，猜测 Sora 的算法框架，去伪存真，提供复现指引，对Sora的算法原理去魅。第二部分是八卦，分析 Sora 背后核心人员的发展路径，对 Sora 的研发组织去魅。"
author: "红博士说"
captured_at: "2026-03-08T11:30:09.978Z"
---

# 去魅Sora: OpenAI 鲜肉小组的小试牛刀

全文5000字，大概需要一杯咖啡的时间。

引言：

> *我们换位思考 Tim 和 Bill 的状态。有丰富的工业界实习经历，博士工作扎实，这种刚写完博士论文、做完学位 Defense 的博士毕业生，对博士期间的工作刚刚完成梳理，并对领域未来做了深度展望，这种状态下研究想法几乎处于爆炸的状态。*
>
> *而 OpenAI的文化，允许小团队像Startup一样运作。所以两个刚刚毕业的PhD，领导一个全新的项目，并不意外。当整个公司的人，都在 All in ChatGPT 和 DALL-E 两个大项目的时候，Sora 其实是一个不起眼的小项目。*

> *Sora 这套框架的优化目标是找训练数据的分布，而不是数据的最小描述长度。所以Sora team对博客的标题起的是物理世界的模拟器，不是物理世界规律的发现者。*
>
> *可以进一步推测，Ilya大概率是没有参与Sora的，因为他不会感兴趣。DeepMind 也不会 follow Sora，但是 Google Research 做 Diffusion Model 的 team，应该还会沿着自己的路走下去，并且坚定 Scale up的信心，如果他们有训练资源的话。*

摘要：

本文分为两大部分，第一部分是技术探讨，猜测 Sora 的算法框架，去伪存真，提供复现指引，对Sora的算法原理去魅。第二部分是八卦，分析 Sora 背后核心人员的发展路径，对 Sora 的研发组织去魅。

提纲：

1.  Sora 什么原理？

2.  如何复现 Sora？

3.  Sora 是谁研发的？怎么组织的研发？

4.  Sora 跟 ChatGPT 什么关系？

5.  Sora 除了生成视频还能干啥？能搞 AGI 吗？

6.  这套方案有像 GPT 一样的 Scaling law 吗？

7.  用了虚幻引擎了吗？

8.  可以期待开源复现吗？

9.  会把 Startup 干掉吗？

10.  Sora 会如何发展?

## 第一部分：复现 Sora

### 1\. Sora 什么原理？

根据 OpenAI 的官方博客“Video generation models as world simulators”， 重点其实就几句话，也就是博客摘要，已经把实验目标、方案设计、实验结果写的很清楚了，在此之上的借题发挥都是自作多情。我们再一起看一遍这段摘要：

> We explore large-scale training of generative models on video data. Specifically, we train text-conditional diffusion models jointly on videos and images of variable durations, resolutions and aspect ratios. We leverage a transformer architecture that operates on spacetime patches of video and image latent codes. Our largest model, Sora, is capable of generating a minute of high fidelity video. Our results suggest that scaling video generation models is a promising path towards building general purpose simulators of the physical world.

第一句点题，实验目标就是要在视频数据上探索一下生成式模型的Scale Up.

第二句说方法，用的文本条件扩散模型（理解为Stable Diffusion即可），在各种长度的视频和图像的混合数据上，也就是说视频帧数从 1 到 T 的数据混在一起。

第三句说架构，基于时空块（就是W, H, T三个维度的切块）隐编码（latent codes）之上的 Transformer 架构。所谓隐编码，就是从像素域转换到了压缩域，也叫隐空间，主要作用是降低计算复杂度，这是 Stable Diffusion 背后的关键技术，很常规。

第四句说结论，最大的模型叫 Sora（天空这个词的日语名字），可能是作者觉得模型能力像天空那么大吧。

最后一句展望，继续Scale Up也许可以成为物理世界的模拟器。

当然，作为搞学术的人，看到这样好的实验结果，我们想的是如何复现，也就是复刻一个 Sora 出来。稍微有点难，因为这个博客毕竟不是论文，面向的不是学术界读者，更不是审稿人，而是紧盯着 OpenAI 的科技和创意领域的活跃人士。所以作为科研人员，会感觉这个 Research Blog 写的非常暧昧，甚至在关键细节故弄玄虚。当然，复现难归难，仔细分析还是能拼出算法全貌。

### 2\. 如何复现Sora？

#### 2.1 方案 Overview

方案：VAE Encoder（视频压缩） -> Transform Diffusion （从视频数据中学习分布，并根据条件生成新视频） -> VAE Decoder （视频解压缩）

从博客出发，经过学术Survey，可以推断出全貌。一句话结论：

**Sora是采用了Meta的 DiT (2022.12) 框架，融合了Google的 MAGViT (2022.12) 的Video Tokenize方案，借用Google DeepMind的NaViT (2023.07) 支持了原始比例和分辨率，使用OpenAI DALL-E 3 (2023.09) 里的图像描述方案生成了高质量Video Caption（视频描述），即文本-视频对，实现了准确的条件生成。**

可以发现，算法层面只有一点原创，就是基于自家的GPT Vision (2023.3) 模型生成了高质量的视频描述。

**Sora 能够生成最长达1分钟的视频，是一大亮点。**这个从结果上看算得上原创，所以没有很确定的猜测。不过，Sora博客引用了一篇Team Lead Tim Brooks 在NVIDIA实习期间的一篇论文：Generating Long Videos of Dynamic Scenes. (NVIDIA, 2022.06). 这篇论文的基本理念是，训练视频的长度很重要，但是长视频训练复杂度太高，所以设计了两阶段的训练来生成长视频，先用低分辨率长视频训练，再用高分辨率短视频训练。

另外，Google的多篇论文里已经发现，视频压缩结合Transformer Diffusion (W.A.L.T，Google，2023.12) 或者自回归(VideoPoet, Google, 2023.12)的方案，能够大幅提升视频的一致性。

所以，关于长视频原理的合理猜测是：OpenAI训练的视频压缩比较强，本身可以在时间维度做高质量压缩；在Diffusion阶段，Scale up以后，视频的一致性变强，加上高质量、详细的视频描述，可以支撑在更长的时间跨度上的内容连续性；OpenAI的 Infra 支持使用更长的视频进行训练（Sora的Systems Lead是Connor Holmes，2023年12月刚从Microsoft DeepSpeed团队来到OpenAI）；再结合常规的插帧，实现了最长达1分钟的视频。

**至此我们可以推测Sora的算法原理如下：**

基本框架是Latent Diffusion（VAE + Diffusion）, 把Diffusion从U-Net 换成Transformer。这个方案就是 DiT (Meta, 2022.12)，但DiT只做了图片生成。

为了支持视频，Sora 使用了MAGViT里的VQ-VAE统一压缩图像和视频的方案，但是因为压缩的视频用于diffusion，而不是自回归，所以把VQ-VAE换回了VAE (Universiteit van Amsterdam, 2013.12), 这就是Sora 所谓的时空压缩。

这个改动的方案其实就是 W.A.L.T: Photorealistic Video Generation with Diffusion Models (Google, 2023.12)里采用的方案，这是第一个 Image+Video VAE 结合 Transformer based Diffusion的方案。

OpenAI只是Follow并融合了Meta的DiT和Google的W.A.L.T.  所以如果说 Sora team 工作做了一年，最近两个月开始有成果，时间都对的上。

#### 2.2 对技术博客的逐段评价

**Turning visual data into patches** 这段高屋建瓴说了下方案，把图像变成Patch（Token），以便Scale up到互联网规模的数据。作者引用了ViT (Google, 2020.10), Video ViT (Google, 2021.03), MAE (Meta, 2021.11), NaViT(Google, 2023.07). 从行文看，作者是受LLM中文本Token的启发，设计了Patch。其实，Patch是ViT的发明，后面的工作都用了这个方案，并不是Sora作者的新发明。这个类比也有点勉强，因为文本的Token是离散的codebook，而Sora的方案显然没有codebook，是连续隐空间里的diffusion. 真正可以类比为文本Token的是Google和DeepMind多年来的一系列工作，这里不再展开。

所以，这段OpenAI 的所谓Patch as Token，其实就是ViT，但就是不肯直说。而且示意图是有一处错误，压缩的过程在时间维度是从T -> t，所以并不一定相等，而且通常压缩后的 t 要小很多，而OpenAI把T（帧数）画成相等，有误导的嫌疑。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图1. OpenAI 官方博客提供的视频压缩示意图

总之，OpenAI不想让人看懂原理，而同行能看懂，OpenAI知道我们能看懂，我们知道OpenAI知道我们能看懂，OpenAI知道我们知道OpenAI知道我们能看懂。但OpenAI还是故弄玄虚，不想让你看懂。

最可能的解释就是，这是Sam设计的Propaganda，强行让非从业人员认为Sora是LLM扩展到了Video，离AGI更近了。显然二者之间除了数据标注，就没有什么关系。也许 OpenAI 以为，相比Google Gemini 1.5 的10M token的58页的技术报告，写几段看似玄乎的技术博客，不至于 Sora 技术层面显得过于苍白。当论文缺乏创新的时候，Method部分实在没啥可以写的，通常都是靠story telling来凑字数。

**Video compression network** 这段，引用了VAE的论文，但没有再次引用Google的MAGViT、W.A.L.T 等图像视频联合压缩的方案。

**Spacetime Latent Patches** 和 **Variable durations, resolutions, aspect ratios** 这两段，讲分辨率、时长、长宽比都可变，但是没有再次引用Google的 NaViT的论文。

**Language understanding** 这段，讲用了Video Caption的技术获得了大量的视频-文本对。对用户输入的简单Prompt，借助GPT先扩展成详细的视频Caption，再用于生成视频。

**Scaling transformers for video generation** 这段，讲Scale up，终于引用了Meta的DiT论文，但是DiT的论文里面其实已经分析过换成Transformer之后很容易Scale up，这不算OpenAI的新发现。另外，Google的几篇工作，也都提到了模型能够Scale up. 从这段来看，还是OpenAI的数据质量高，Scale的规模更大吧。感谢OpenAI Sora小组，让大家开了眼界。

## 第二部分：去魅 Sora

### 3\. Sora是谁研发的？怎么组织的研发？

根据OpenAI的官方介绍，Sora 有两位Research Leads: Tim Brooks 和 Bill Peebles. 有一位Systems Lead:  Connor Holmes. 另有12位Contributors. Sora 应该是处于 Research 阶段的项目，我们重点关注Research Leads.

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图2. Tim Brooks, Sora Co-lead

我开始关注Tim Brooks是从2018年，他在大四的时候复现了HDR+，我们在做ISP的时候，第一步也是复现HDR+，就调研到了Tim的这个代码。（一个有趣的题外话，我们组当时参与复现HDR+的一个实习生，当年是大三或者大二吧，现在也在OpenAI，比Tim Brooks去的早一些，参与了ChatGPT首发）。不知道这是不是Tim的毕业设计，毕业后就去了Google, Marc Levoy带领的计算摄影组，做了Unprocessing算法实现RGB -> raw数据的合成和降噪算法，后来又跟Tianfan Xue学长、Jon Barron大神等人参与了Pixel的超级夜景算法，这个算法非常牛逼，后来我们基于Deep Learning做了个更好的，也去投SIGGraph，被审稿人拍的很惨。

所以，在2022年11月的一天，我读到一篇论文InstructPix2Pix (UC Berkeley, 2022.11)，发现这是Tim Brooks写的，感到非常亲切，有种多年以后又相遇的感觉。这篇论文写的是用Diffusion Model做指令修图，但训练数据是用GPT-3的API和Stable Diffusion生成的。这个数据生成的方法很聪明，通常研究这种算法需要昂贵的数据标注，但是这个工作通过GPT-3结合Stable Diffusion实现了自动化的数据标注。我当时感觉到图像领域的研究范式已经开始转变，马上把这篇论文发给整个部门的同学，让大家关注研究范式的迁移。过了没多久，ChatGPT发布了。所以我对Tim的这篇论文印象很深，它伴随了那段时间，我在玩 GPT-3 Playground和 API 的时候感受到的冲击。

做完 InstructPix2Pix，Tim Brooks 就从 Berkeley BAIR 博士毕业了，博士论文是 Generative Models for Image and Long Video Synthesis. 作为一个图像领域的研究员，调用GPT-3 Instruct API用一种新范式做了新研究，我想一定会对GPT的能力感到震撼吧，不久ChatGPT就发布了，顺理成章Tim Brooks在2023年1月去了OpenAI.

在 Tim Brooks 做 InstructPix2Pix 的几乎同一时间，他的同届同门 William (Bill) Peebles 在Meta 跟 Saining Xie 大神实习，做出了DiT: Scalable Diffusion Models with Transformers (Meta, 2022,12). 3月份，Bill 入职OpenAI，与早入职两个月的Tim co-lead Sora项目。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图3. William (Bill) Peebles, Sora Co-lead.

我们进行换位思考Tim和Bill的状态。有丰富的工业界实习经历，博士工作扎实，这种刚写完博士论文、做完学位 Defense 的PhD，对博士期间的工作刚刚完成梳理，并对领域未来做了深度展望，这种状态下研究想法几乎处于爆炸的状态。一个非常自然的想法，便是延续自己之前的工作，Diffusion Model 和Video Generation, 甚至直接从 Bill 一作的 DiT出发。

而OpenAI的文化，允许小团队像Startup一样运作。所以两个刚刚毕业的PhD，领导一个全新的项目，并不意外。当整个公司的人，都在All in ChatGPT 和 DALL-E 两个大项目的时候，Sora其实是一个不起眼的小项目。当项目有了起色，逐渐有公司的其他人来协助，或者招聘新的人，而项目的Systems Lead Connor Holmes 就是这样进来的。

Connor Holmes 在2023年12月份才从微软DeepSpeed团队（LLM Infra最顶尖的团队之一），加入到OpenAI Sora团队。Research Leads和Systems Lead这三个人以外的人，其实我们不必细看，大概率要么是DALL-E的团队的人来帮忙，要么是刚入职不久。

这就是一个小团队，而且，实验刚刚成功不久，以至于整个OpenAI，只有这两个Research Leads 和 CEO Sam在发Sora视频，几乎没有OpenAI的其他人参与。这种情况通常发生在一个研究成果刚刚出来的时候，产品代码还没写好，需要研究员很多手动参与，才能跑实验。

一个研究团队里面，如果有新毕业的博士加入，并且有硬核的工业界经历，那么企业要创造的是一个自由的平台、挑战的目标、充足的资源和适量的指导。这是被反复证明的经验。Sora team只是新添了一个案例。

### 4\. Sora 跟ChatGPT什么关系？

Sora 和 ChatGPT在模型层面没关系，所谓的世界模型不是从LLM获得的，而且Sora Team 也没有提 World Model 这个概念。ChatGPT的作用，在训练阶段，它是用GPT-Vision给视频标注Caption数据，在推理阶段，扩写Prompt.

### 5\. Sora 除了生成视频还能干啥？能搞 AGI 吗？

不能。目前就是生成视频，可见的未来，这种架构也只能在创意领域发挥价值。要在GPT-4的基础上更进一步，还是要靠 GPT 框架：Gemini，GPT-5、以及VideoPoet.

Sora 这套框架它的优化目标是找训练数据的分布，而不是数据的最小描述长度。所以Sora team对博客的标题起的是物理世界的模拟器，不是物理世界规律的发现者。前者可以通过最大化像素的似然性来生成与训练数据在统计上相似的图像或视频，而后者追求的是一种旨在寻找能以最简洁形式描述数据的模型的方法，即最小描述长度原则，它基于的是一种认识，即如果一个模型能够以更短的描述完整地解释数据，那么这个模型可能更接近数据的真实生成机制。在这种框架下，模型被激励去学习数据的“原因”而不仅仅是数据本身的表象。

基于此，我继续buy in GPT框架。可以进一步推测，Ilya大概率是没有参与Sora的，因为他不会感兴趣。DeepMind 也不会 follow Sora，但是 Google Research 做 Diffusion Model 的 team，应该还会沿着自己的路走下去，并且坚定 Scale up的信心，如果他们有训练资源的话。

### 6\. 这套方案有像GPT一样的Scaling law吗？

能Scale up，但是没看到Scaling law.

### 7\. 用了虚幻引擎了吗？

没必要。把事情想复杂了。Why bother？模型中应该没有，既没有作为模型的超参数，更没有把虚幻引擎的渲染作为 pipeline 的一部分。搞那么复杂没用，既难work，又与end2end的反向传播的理念背道而驰。简单而可扩展的模型架构，是Scaling up的关键。

那为什么生成的一些场景和细节，与游戏有些像？因为Youtube和Twitch上有非常多游戏视频，被做进了训练数据集，而且这种数据有个好处，游戏直播有很多的讲解，是非常高质量的数据，相比影视作品和常规UGC，版权风险也更小。

### 8\. 可以期待开源复现吗？

我相信开源社区的速度，比大家想象的更快。另外NVIDIA其实同时期做了一个叫Diffit (NVIDIA, 2023.12) 的工作，方案类似，还没开源，计划开源。

### 9\. 会把 Startup 干掉吗？

哈哈，钱已到位的视频生成 Startup 现在应该都踌躇满志，蠢蠢欲动，高歌猛进地复现Sora了吧。估计Sora放出的第一天，各家CEO都被打懵了，结果等报告出来，仔细一琢磨，我上我也行，便又打了鸡血。*Game on.*

### 10\. Sora 会如何发展?

首先，Sora的定位，应该是新时代的创意工具，大大降低影视(包括Video Games）创意工作的门槛。而人，就是喜欢看视频。好的作品显然是不够的，比如我，电影工业都发展一百年了，但还是可着那么一些好作品翻来覆去地看。

其次，它也仅仅是创意工具而已。真正的变革，还是看GPT.

by 红博士

2024.02.19