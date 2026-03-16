---
url: https://mp.weixin.qq.com/s/aW7LuCSMkve7cPrW7jPn3Q
title: "AI时代请别聊护城河：从Cursor说起"
description: "AI创业公司和护城河从来没什么关系"
author: "全速前进"
captured_at: "2026-03-08T13:12:34.000Z"
---

# AI时代请别聊护城河：从Cursor说起

1/ Cursor如果今年能维持增速，到年底Revenue可能到10亿ARR（现在是3亿），非常可观，快要接近OpenAI ARR的10%，只是Cursor的成功真的和护城河没什么关系，没必要什么都往上套，尤其对于AI创业公司，大多时候追问护城河没什么意义

2/ 护城河这个词其实是巴菲特带火的，这词在AI时代该和他老人家一起退休了，众所周知巴菲特自己不怎么投科技股（除了Apple），但是奈何影响力太大Tech Bro们也开始讨论护城河，但该词的实际上的作用大部分时候是搅浑水。Elon Musk一样不喜欢这个词，Moat is lame

2/ 护城河（Moat）强调的更多还是是防御属性，适用于不需要太多努力，但依然能保持竞争力的生意。微信两年不做功能更新也没人能撼动地位，可口可乐配方n年也不用变，每年做做Marketing就行，操作系统像iOS/Windows保持不变2年，用户根基也不会有什么变化，这才是护城河的水平（都是很老很大的东西）。如果对应到传统生意则是长期成本优势/专利等等，在科技语境下解释力不如网络效应/生态

3/ 现在的AI产品别说2年不更新迭代，2个月不更新可能就被竞争对手卷飞，下面一层的模型厂商们也一样在卷，内部压力都挺大的，我之前在[这篇文章](https://mp.weixin.qq.com/s?__biz=MzI0NDk0MzI2NA==&mid=2247483888&idx=1&sn=267c685381adaba91738d59585427ff5&scene=21#wechat_redirect)里有详细写过。科技领域，非要说Moat，那也只有一个，就是创新迭代的速度

4/但Cursor当然有优势，以下几点：

1）产品体验比较好，UI/UX丝滑，训练了自己的小模型（Coding类产品基本都在做），在大模型的输入侧和输出侧两个部分都有自己的小模型，增强针对代码的理解和生成能力

a. 具体说是模型在输入端为大模型（Sonnet/Gemini/GPT）筛选代码库的相关部分，在输出端，模型将大模型生成的high level draft转化为完整的代码差异。自己的小模型快且便宜， 可以靠基于开源模型post-train或者和闭源模型厂商合作

b. 数据飞轮，值得注意的是，Coding IDE的数据飞轮 > Chatbot的数据飞轮（目前基本没有），因为反馈频次高、客观上有对错、更结构化。AI IDE的UI/UX其实有更多机会积累用户数据，不像chatbot就是一个框，也可以解释大家都是wrapper套壳为什么Perplexity活得就更艰难。不过不同数据飞轮之间差距很大，即便如此，Coding的代码编辑到模型提升的循环，和推荐系统和社交网络这种正反馈强度还差得远，但可以慢慢观察到底如何，个人觉得有，但不多…不decisive

2）先发优势，现在Cursor的DAU超100万，产品打磨的比较好，也是AI IDE里用户心智最强、流量最大的Coding app，社区也很活跃，最近完成30亿美元融资后启动一波拉新，全球写代码的学生估计都蹭了一年Pro订阅，如果没有显著的体验差异，大部分用户还是会留在Cursor

3）团队执行力强/强工程背景/年轻/MIT，不展开了

4）Cursor永远能用到SOTA的Coding模型，未来的Claude 4/Grok 4/GPT-5/Gemini 3等等，而这是模型公司自己做Coding app所不具备的优势，我在之前的的文章[《应用公司的优势，模型公司硬伤中》](https://mp.weixin.qq.com/s?__biz=MzI0NDk0MzI2NA==&mid=2247483852&idx=1&sn=795da301de85874d8336eef0282f2c45&scene=21#wechat_redirect)详细讨论过这个问题。显然OpenAI自己的Coding app不会接入Gemini/Claude，只能用自己的模型，但自己的Coding模型如果又比较菜，那就比较尴尬。OpenAI刚用3B收购了Windsurf（100M ARR），其实是焦虑的一种体现，因为的Coding这个方向至关重要，而Anthropic却做得更好。按照过去2年的发展态势，并没有哪一家模型厂商可以全方位领先，Cursor可能长期在这个方面都会有优势。不过这个点有counter argument，下面会讨论到

5/ Cursor作为一个单一维度的工具，远没有到讨论护城河的阶段，如果有更好的AI IDE出现，很多用户会选择切换，程序员是最在意效率和爱鼓捣的一群人，什么好用用什么。IDE本身迁移成本不高，大家都是VScode的Fork，当然UI/UX上有差异，但不会是决定性的，以及这么多人切到Cursor上本身也说明IDE的切换成本比较低（也感觉没机会在上面做出social layer）

6/ 当然今年依然看好Cursor的增长，绝大部分写软件的企业都不会拒绝Cursor，一个月几十美元的花费给员工提效10%，这ROI都是几十倍，采购动力非常足，现在也没有显著更优的产品

7/ 短期增长没问题，但长期竞争有很多讨论的空间，Coding领域下一阶段的竞争可能马上就要来了，Jeff Dean说AI距离Junior Engneer还有一年，OpenAI刚刚推了Codex，加上Windsurf的收购，大概率不会仅仅是IDE，而是一个整合度更高的产品

8/Coding未来的市场很大，可能这个领域大头最终还是被模型厂商吃掉（bolt/v0这种都算），可能有以下几点原因（供讨论）：

1）Coding本质上并不是一个垂类市场，大家都知道市场巨大，是一个非常核心的业务，或者说在模型厂商的主航道上，刚刚Sam Altman的原话是Coding is central to the future of OpenAI, not vertical app。过去几十年互联网的繁荣，最本质的逻辑是软件吞噬世界，而现在AI编程要吞噬软件生产，Coding完全可能带来以十亿计的营收，所以模型公司一定会亲自下场

2）模型厂商能做端到端的优化，进而有更强的Coding/SWE能，原因在于可以端到端优化，类似OAI现在的DeepResearch，用一个微调版本o3进行端到端RL训练，把tool use之类的功能都做进去，未来不用像Cursor一样做三明治在基础模型上下各加一层自己的小模型，可以直接做E2E的一个模型，因为分多个模型彼此之间不可导，本质上还是割裂的scaffolding，上限不高。不过风险在于，万一自己的基础模型训练能力菜，比如Llama，即使端到端的效果可能也不会很好。OpenAI收购Windsurf其实也是焦虑的体现，Coding这个方向至关重要，而自己明显被Claude压一头，需要额外强化这个方向

3）分发优势，比如ChatGPT现在周活超5亿，还在涨，具体优势是：

a. Coding产品很可能整合到ChatGPT里面，加到现有订阅combo里，i. 有大量的C端流量加持，ii. 可以进一步刺激用户订阅。这件事情发生的概率很大，Sam Altman原话是希望ChatGPT 成为core AI subscription, 通往智能的默认接口，里面会有各种组件，Coding也会是其中之一

b. 如果说用户反馈的数据飞轮确实是核心因素，那么ChatGPT的用户基数可以帮忙bootstrap这个飞轮。这里的数据飞轮主要是：i. 用户的输入习惯，用户在代码库中会先输入一部分代码，可反映用户的输入偏好/习惯，这是GitHub的完整项目代码无法学习的，ii. 用户在具体代码上的code edit和quest acceptance可以积累反馈数据

4）AI IDE现在的UI/UX 可能只是一种或者初级阶段，未来有其他形式

a. OpenAI做Canvas这个产品的Karina Nguyen说，未来UI/UX会根据用户意图来调整，想写代码的时候的Canvas就应该变成AI IDE，如果要实现，这件事肯定是模型厂商做起来更合适，时间窗口大概也就6-12个月甚至更短

b. OpenAI的Coding/SWE Agent也传了一段时间了，可能分化出整合度更高/普通用户友好的版本，可能在下半年发布

5）自用优势，可以内部打磨，定义AGI的角度之一就是AI能自己开发自己，这件事情肯定发生在模型厂商，

a. 从这个角度看长期最强Coding系统一定是AGI Lab先做出来，in-house的Eng/Research都好几百人，内部可以先dogfooding用起来。现在已经观察到一些信号，例如OpenAI的Codex和Anthropic的Claude Code最初都是从内部流行开始（Internal DAU is high），再产品化后推向市场。同时，也只有AGI Lab内部能体验到最前沿的模型能力，在最上游进行全栈研发

b. OpenAI的现任首席科学家Jakub Pachocki（Ilya的继任，大概和现在的Mark Chen co-lead Research）刚在Nature的一个采访上也畅想了下AI研究自动化，如果这个问题被解决，基本上AGI/ASI is solved.. 如果模型厂商能用AI Coding加速研发，显然第一个客户就是自己，形成正反馈循环，也许就是2年左右的事情

6) 成本问题 ，Cursor这种应用还是主要用模型厂商的API，在和模型厂商的Coding类产品竞争的时候，意味着用户要在Anthropic/OpenAI API价格的基础上再加一层Margin（以Cursor为例，定价是API成本价的20%+订阅费），创业公司能否用更好的产品体验来弥补这一层成本差距？这里打个问号，虽然这是偏长期的问题，但AI行业变化也很快，Cursor是否会成为是下一个Jasper（也曾到过近3亿ARR）拭目以待。本质上AI创业公司发展的窗口期，很多情况下就是模型公司走完一个【Research->工程->产品化】的周期，这个cycle未来只会加速

9/ 最后绕回来护城的问题， 一句话，不存在的，AI创业公司的优势很朴素，全靠加班卷，快速迭代，动作快且灵活，在合适的时间窗口聚焦做事。但关于时间窗口，模型公司自己对模型能力发展也吃不准，可能也就看到6个月，再往前都在摸黑炼丹试错

10/ 最后补充一个小点，最近Sam Altman在红杉AI Ascent上说，GPT-5不会比o3聪明太多（will not way smarter than o3），OpenAI在Reddit上的AMA也和大家说了，主打的是把各种工具整合到一起减少切换。也在想，2025年靠堆CoT的Reasoning model，性能上可能也要开始边际递减了，一下个关键的Scaling vector会是什么？这个问题背后同样是在说，不创新就会落后，没有护城河

欢迎大家关注点赞转发、链接交流呀，如果想加群请加微信：fullspeedai，备注里欢迎介绍一下自己