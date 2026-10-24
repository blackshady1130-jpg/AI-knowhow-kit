# 训练也“PD分离”，可能是更优的Scaling之路

| 项目 | 内容 |
| --- | --- |
| 作者 | [Yibo Zhu](https://www.zhihu.com/people/yibozhu) |
| 发布日期 | 2026-09-28 11:09（中国标准时间） |
| 原文 | [知乎专栏文章][1] |

## 正文

上周忙完了 Step 5 Preview 的发布，终于有时间整理下过去几个月捣鼓的新idea，并发在了arxiv上。虽然 Step 5 还没用上，但是也许不久的将来就能在我们的主线模型中看到类似的思路了~

KITE: KV-Invariant Transformer Expansion for Efficient Agentic LLM Scaling ([https://arxiv.org/abs/2609.27294](https://arxiv.org/abs/2609.27294))

TLDR：KITE是一个新模型设计与训练范式，在训练时就按推理PD的特性分为两阶段，是为数不多的能实现LLM模型效果、训练成本、推理成本三者**同时获得收益**的手段。

## 1. 模型系统Codesign的目标

一直以来，我与同事们都很关注模型系统codesign。简单说，codesign就是想通过改进模型与系统设计，达成系统成本和算法效果双赢的效果。但是一路走来，我发现这个目标在实际中要更加复杂，主要是“系统成本”又区分为训练成本和推理成本，而它们又不是完全同步增大缩小的。因此实质上我们面对的是个三目标（训练成本，推理成本，模型效果）优化问题。

回顾过去的例子，“三赢”的就能成为业界主流，因为无论算法团队还是Infra团队最终都没有理由不采用；而三目标中只“赢”两个，就容易碰到落地的阻碍。

### 成功例子：MoE

一个最经典的成功例子就是MoE。早在2021年我在前司的时候，做BERT模型的MoE化，相对于一个经典的12层BERT baseline，我们就是通过训一个8层的MoE，证明它在训练成本、推理成本、模型效果获得三赢，从而获得了全司第一个MoE成功的落地和推广。后来就飞快地推广到了很多语言类模型的业务上——谁能拒绝一个又省成本又涨点的方案呢？

这里的关键点是我们在给MoE做论证时，并不拘泥于“等参数量”。在当年刚开始找算法团队时，第一个面临的挑战就是：你把模型做稀疏化了，是不是损了模型效果？这个疑问其实隐含的假设就是“等参数量”——不会有人认为等参数量的MoE能干得过dense模型。然而当年我们精心选择了一个尺寸，使得训的MoE模型实际成本是比dense baseline低的，但是靠总参数量压过dense而获得模型效果的优势。这就是一个成功的co-design。

LLM业界过去几年发生了一模一样的事情，就不赘述了。

### 疑问案例：Upcycle

但是还有一些其它技术，也能获得成本优势，却没有那么流行。例如古老的Upcycle技术（Upcycle这个词我所知来源于2022年的[https://arxiv.org/pdf/2212.05055](https://arxiv.org/pdf/2212.05055)，更古老的词其实是net2net），例如先训dense模型再转变为MoE模型（Mixtral 8x7B），或者先训浅的模型再复制若干层（Qwen和WeLM部分模型）。这么做无疑问是可以省训练成本的。

但是，社区里普遍的担忧是，这样训出来的模型效果是不如from scratch训的同尺寸同结构模型的。我们也可以考虑像论证MoE一样把upcycle的模型给scale大，从而确保模型效果压过from scratch的经典LLM baseline。但此时推理成本就会大于baseline。这样无论如何也无法达成“三赢”，那么就会在落地时碰到阻力。

### 疑问案例：YOCO

最近因为DSv4.1 Flash，YOCO这类模型结构设计被更多人关注了。当然YOCO也不是多新的东西，24年就有了（[https://arxiv.org/abs/2405.05254](https://arxiv.org/abs/2405.05254)）。为什么一直都没什么人真用于主线模型训练呢？究其原因和Upcycle类似：社区对其模型效果的牺牲有担忧。

我们也可以考虑像论证MoE一样把YOCO模型scale大，去和小尺寸baseline比较。DSv4.1 Flash正是这么做的：和其它公司300B级别的Flash模型竞争时，用两倍模型尺寸保效果，同时依赖YOCO的特性把推理成本给压下来。只不过，这么做的代价是训练成本也是按两倍尺寸付出的。

**（Agent时代的机会：**这里插一句，YOCO这类架构确实是非常适合agent时代。我们2~3月份Step 3.5 Flash被全球小龙虾用户狠狠地用了几万亿token后，我们就意识到agent时代和之前reasoning最大的一个区别就是推理成本转变为prefill占大比例。具体数据我们paper里有。而省prefill计算的YOCO就值得好好看看。）

近期就有一个面试的候选人说：他认为YOCO这个技术只适合用于Flash级别模型。而对于他们旗舰级别模型，训练成本会更加重要，因为旗舰级模型最重要的还是在给定算力下训出SOTA模型效果。

我说：说白了你觉得YOCO并不是什么场景都用，核心原因就是它并不省训练成本。甚至想达到和经典LLM baseline一样的模型效果，你可能要付出更大的训练成本（因为你要把模型尺寸扩大去补YOCO亏的效果）。做不到“三赢”，就会在一些地方碰到阻力。

*小孩子才做选择，我们能不能全都要？*

## 2. KITE：PD分离的训练流程+Scaling

### 思路历程

在Agent时代，YOCO类模型架构确实对降低推理成本有着非常诱人的特性。大家最大的concern是其模型效果会损失多少，因此我见到一般的研究路线是，研究各种模型结构改进去尽力论证它与传统满KV的LLM模型效果gap小。

半年前我们就开始思考怎么解决这个问题，思路是回归到模型Scaling。从做MoE的成功经验出发，一个模型架构如果损失了模型效果，其实是可以靠Scaling补回来的。对于LLM这种scaling law已被验证的模型而言尤其如此。关键在于扩大Scale后是否训练成本和推理成本**都**还能保持正收益？

比如相对于一个100B的传统LLM baseline，100B的YOCO模型也许模型效果会略差一点点，但是如果我做一个120B的YOCO呢，用同样的token量训练后，是否模型效果就能超越100B baseline？120B不够的话，150B呢？推理成本在Agent时代重prefill的背景下，依然有可能beat 100B LLM baseline。然而这里的一大问题是120B或150B的YOCO，假设是100B baseline的等比放大，同token量下的训练成本是上升了的。

就在此时我们想到了模型Upcycle的思路，这个省训练成本、但或许会影响模型效果的手段。如果我们也靠scaling来弥补回模型效果，似乎和YOCO结合就会形成绝配？

### KV-Invariant Transformer Expansion

其实 KV-invariant upcycling 才是我们内部的原名，KITE是为了凑个好记的名字 :)

从上面的思路而来，我们定下了训练流程：针对一个将做对比的经典baseline，我们先训一个比该baseline小的，专用于prefill的子结构，能够把所有KV cache生成。再拓展这个模型，加上一块只有decoder才会激活的部分，而这部分复用prefiller生成的KV，再进行continue pretrain。最终获得的模型，比经典baseline scale得更大，从而确保模型效果胜出。

这里最关键的部分就是：upcycle出来的部分，必须对KV计算是没有影响的。例如传统的upcycle，无论是增加MoE expert数量，还是在模型中间部分复制一些层，其实都会对KV计算产生影响，从而导致在推理服务时要付出更大的prefill成本。只要对KV计算没有影响，我们推理时prefill的成本就依然是低的。在对agent这种重prefill时代，虽然我们upcycle后的模型比baseline更大，我们的综合推理成本依然能比baseline有优势。

只要遵循这个KV-invarint原则，其实有很多模型设计方法。我们在paper里采用的类双塔或者叠层结构就是最直接的一种（我们称为SST结构，见图1）。当然也可以强行塞在一个塔里，比如在先训prefiller的基础上，拓展其hidden stream宽度，只要确保拓展出来的hidden宽度从头到尾完全不影响到KV的计算即可。同理也许也可以和hyper connection做一些结合。

![图1：Step Scale Transformer（SST）的模型结构与训练流程](https://pic1.zhimg.com/v2-d13343cc1d2a2656eb4a12395d93c92a_r.jpg)

*图1：Step Scale Transformer（SST）的模型结构与训练流程*

我们在论证这个设计时，走的是和当年论证MoE一样的路线：我们不拘泥于同参数量，而是不吝啬scale模型到更大的尺寸。但我们控制推理与训练成本都比原来的baseline更低，在这个基础上证明模型效果也获得了涨点。实现了模型效果、训练成本、推理成本三赢的结果。

![图2：和一个等比缩放的47A1.48B经典Transformer比，基于KITE原理训练的67B SST结构实现了全面优势。](https://pica.zhimg.com/v2-0d951f85bfeb0ade230f973823ca3336_r.jpg)

*图2：和一个等比缩放的47A1.48B经典Transformer比，基于KITE原理训练的67B SST结构实现了全面优势。*

当一个设计实现“三赢”时，我已经看不到什么理由不适用它了。正如MoE，除了存储容量确实有限的场合还用用dense，其它时候训MoE都是比dense模型更合算的选择。我眼里KITE也是一样级别的技术。KITE成立唯一的假设是线上推理成本还是prefill占大头。只要Agent时代的流量特征没有重大变化，KITE就总是比传统结构更合算的选择。

## 3. 展望未来

### 最佳KITE架构设计有待探索

我们这回SST只用了一个最最基本的架构——先训半个模型，复制一遍，再继续训——来论证KITE。实际上这里可以调整的地方非常多。Paper里提到了一些，例如prefiller侧除了kv外，可以给出更多信息到decoder测；以及decoder侧对KV的使用可以类似WeLM与MIMO HySparse2提到的颠倒顺序而非逐层使用，等等。

还有就是可以玩prefiller和decoder的不对称，例如decoder部分只在decode时使用，因此就可以激活更多的参数量。同时训练的时候因为是upcycle出来的部分，不会过全量的token，所以激活参数量的上升对训练成本的影响也不如from scratch训练大。仔细调一调有可能能调出比SST更好的trade-off。但这就引出了下一个问题——

### Scaling law更复杂了

我们之前对scaling law的研究（Step Law [https://arxiv.org/abs/2503.04715](https://arxiv.org/abs/2503.04715)）获得了蛮多业内朋友，包括硅谷frontier lab朋友的好评。但是KITE又多加了许多维度：prefiller和decoder分别的总参数量和激活参数量的占比，以及两阶段训练所用token数的占比，两阶段的LR策略，等等。

战胜经典LLM baseline简单，找到最佳trade-off却非易事。

### 与Loop Transformer的关系

有一类Loop Transformer其实也属于KITE，如果它满足：

- 先训无Loop版本，再加Loop继续训练
- Loop不会影响KV的计算，只是reuse过模型第一遍时算好的KV

## 4. 结语

该说的，Section 2最后已经说了。期待KITE上到我们主线模型的时候~

最后再安利一下我们刚发布的Step 5 Preview，已经获得了社区蛮多开发者朋友的好评，反馈说可替代Opus 4.8使用。公司内部不少同事现在日常工作也都是完全使用它做开发了。与GPT-6 Astra和Opus 5.5的差距，和业界同仁一样，我们也还在全力追赶。同时期待Step 5正式版与它的下一代。


## References

[1]: https://zhuanlan.zhihu.com/p/2087842854592950950 "训练也“PD分离”，可能是更优的Scaling之路"
