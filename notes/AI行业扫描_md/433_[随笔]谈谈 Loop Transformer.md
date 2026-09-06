# [随笔]谈谈 Loop Transformer

> 作者：渣B
> 来源：zartbot（微信公众号文章）
> 时间：2026 年 9 月 4 日 08:43

---

在机场等飞机, 随手写一点...

微信公众号有一个好处就是过往的观点每一篇都真是的记录着, 比较有价值的是几年之后可以用来校验自己的技术判断. 例如你回顾公众号23年 24 年的文章, 我就在谈 MoE, 那时候还不是显学...但是我要设计RDMA传输协议解决 AlltoAll 的问题呢, 还好赶在 CIPU 2.0 流片前全搞定了... 这几天内部还有人跟我说某公司的顶级网卡开了EP就废了, 还有一些关于 IB 的八卦... 笑抽了... 突然觉得自己三年前的判断无比的正确... 但今天谈论的并不是这个.

今天主要谈谈 Loop Transformer,  其实在 GPT-5 的时候就有传言用了 Universal Transformer. 这几天GPT-6又在传, 再加上智谱的财报也在提...

现在再来引用一些一年多来的几篇的文章, 阐述一下为什么我比较喜欢 Loop Transformer吧...

去年的时候写了一篇《谈谈Transformer的一些演进: UT,MoD,MoR...》, 大概分析了 Universal Transformer, MoD 和 MoR 几篇论文. 我说服自己接受 Loop Transformer的观点有几个理由.

首先, 从计算机体系结构而言, 如果把 Attention block 当作一个计算机的指令执行单元, 而FFN 作为存储器. 这个视角下 MoE 和 Sparse Attention 相当于是有了一种类似于分支决策的能力, 但是似乎离一个比较完备的计算机还是缺乏一些循环指令的能力. 所以在这个视角下很容易去接受 Loop Transformer 的算法.

另一个观点就是从信息论的视角, 并不是每个 token 都有一样的新息的, 那么我们就应当为更多的新息的 token 支付更多的算力, 这也是我比较支持类似于 MoD/MoR这样的算法的原因.

当然还有一些 TDA 拓扑分析的视角, 都似乎指出了 Attention 需要某种迭代算法获取更高的智能.

然后就是对于 Linear Attention 是不是也能算一种 Loop Transformer ? 去年也详细的分析了一下《谈谈未来Attention算法的选择, Full, Sparse or Linear ?》. 当时有一个结论:

在Sparse Attn的路线上引入类似于 KDA 的“状态矩阵”, 增加一些递归结构, 例如UT/MoR, 甚至是Google Titan 《Titans: Learning to Memorize at Test Time》这样的方法, 引入Memory Context达到类似于 KDA 这样算法的“状态矩阵”的效果, 即Memory as Context(MAC).

其实回到今年, 再看一些 RSI / Test-time training 一类的文章, 越来越觉得有趣了... 另外是今年上半年的一些想法《浅谈Claude Mythos和Loop Transformer》, 更多的是在考虑一个更有趣的问题, 如何在国产算力上推理10T参数的模型...

对于一个模型, 我们要 Scale 它到更高的参数规模, 最简单直接的路有两条, 一条是加宽, 例如加宽Hidden-dim, 另一个是加深模型的深度, 例如更多的层数. 但是两条路都有它的缺陷... 两种做法整体的激活参数都会更多, 而加深后对于TBT的影响会更大, 而此时我们需要一个更稀疏的模型, 既有足够的容量存储更多的预训练的知识, 也有足够的能力在后训练中更好的泛化, 这是模型本身的需求, 但是需要叠加一个算力的约束. 而简单的加宽加深更要命的是 KVCache 的占用会成倍的增加, 这些都不太适合国产算力的需求

如果用Loop Transformer, 例如模型还是40层, 但是多 Loop 一圈, 实际上 KVCache 只需要记录最后一圈的, 似乎这样 KVcache 就比一个 80 层的模型少了一半? 这些收益是很明确的. 但是这与我想象中的 Loop Transformer 还有些不同, 可能我更期望的是一种 Loop Attention, 然后少穿越一半的 MoE/FFN 层...

昨天和某个公司的人聊天, 大概给我的说法是未来10T模型90%的激活参数都是 FFN 了, 所以需要做 LPU /FFN 专用处理器. 但是我可能更多的持有反对的太多... 我直觉上的答案应该是 Attention 和 MoE/FFN 还是应该有某种平衡.

假设我要做一个 10T 模型, 可能总的激活参数想把它限制到 100B~150B 的规模, 然后尽量少的穿越 MoE/FFN 这些内存bound的层. 直觉上这些 MoE 应该是非常稀疏的, 例如 1024/2048 专家选 8 这样的结构, 少的 topk 有利于降低整个推理时 EP 通信的开销, 但是这样的结构在训练的时候, 我们又期望这些参数都能记录下所学到的知识, 尽量少的出现 dead expert.

很自然的一个选择就是期望在进入 topk router的时候能够有更多更准确的信息协助路由. 很自然的一个选择就是要利用类似于 Hyper Connection 的机制扩大进入 topk router 的宽度. 然后对于Attention 需要用更多的算力使得它有更好的“分辨率”.

当然很多人会说, 除了在Expert上堆参数, 不是还有 engram 这样的扩展么? 最近一段时间对 engram 的一些思考是, 它可能对一些本来参数在100B~300B 左右的 flash 模型扩展参数有效, 而对于 2T~10T 参数的模型未必有效, 特别是对于 CSA 这样的在 KV 上还有一些 overlap 的,  可能 KV overlap 或者Linear Attn中本来就带的conv 本身就有了一系列 n-gram 的表示能力了... 当然有一个O(1) 的查参数的免计算的能力还是非常 promising 的, 或许类似于 engram 的算法应该更仔细的去考虑一些 latent space 的表示能力.

在这些约束下, 那么不得不把模型 arch 的设计转向到 Attention block 了. 可能还有一些以前读数学系学计算方法的缘故, 自己还是比较喜欢一些迭代算法的, 所以目光就转向了 Loop Attention 一类的算法, loop 的实质是等效的去增加 Attention 的 head, 使得多次迭代的attention 计算中能够把它输出给 topk 的 latent space 中 token 的表示在一个更高的维度内充分的展开, 使其能够更好的适应更稀疏的 Expert Routing.

最近我在读 Google 的一篇论文 《recirculation》[1],  可能我更期望的是这样的工作方式, looping 与 recirculation 的区别是态射复合方向的差异. 把每一层看作状态空间  上的自映射, looping 复合的是同一对象上的映射迭代 , 仍在深度范畴内; recirculation 则引入了时间平移函子 , 复合的是 , 把深度范畴嵌入到了时空双范畴中. 但是这种方式或许对 KVCache 的占用和处理也会更复杂, KV prefix match 也会因此变得复杂. 后续有空详细解读这篇论文的时候再展开叙述吧...

其实为什么需要Recirculation/loop 的根本原因是, 实质上我需要在 Recirculation / Loop 的过程中, 对于Attention, 实质是在一个 latent space 的改写 Q, 而 K V 也在这个过程中得到了优化. 特别是对于 Sparse, 每次 Loop 的 topk 有助于动态的选择更多的block,而不是简单的截断.  最近还有一个很大的脑洞, 我们假设存在一个类似于 DSA/ CSA 的结构, 通过 Recirculation/Loop 把每次输出的 OV 作为给 MoE Gating 输入的一个子空间, 多次的输出构成的某种组合成的更高维的空间里存在一个更稀疏的表示, 使得 topk 的Expert 选择更加细粒度, 这样是否就成了?

当然或许此时会问, Linear attention 本身不就有某些递归/Loop的属性么? 此时我大概的一个想法还是尽量要提高 Prefill 和 Decode 时的并行性, 以及 KVCache context 的可交换和可组合性来提高推理时 Attention 算子的并行性.

大概这些就是近期回顾 Loop Transformer时, 我的一些不成熟的想法吧...

或许这些东西都没有什么卵用, 直接有更高质量的数据比什么模型架构的变化都更管用呢?

## 参考资料

[1] recirculation: https://arxiv.org/abs/2608.17981

---

## 原文链接

https://mp.weixin.qq.com/s/Egn_qJP-vlRJu4KtAz1v6A
