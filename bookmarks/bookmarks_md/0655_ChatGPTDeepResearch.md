---
url: https://mp.weixin.qq.com/s/Mq7LZHVeo-maCvj2YCvzIg
title: "使用 ChatGPT 新功能 Deep Research 后，谈谈它会带来的影响"
description: "信息分发又一次开始变化。"
captured_at: "2026-03-08T12:47:25.886Z"
---

# 使用 ChatGPT 新功能 Deep Research 后，谈谈它会带来的影响

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/qpAK9iaV2O3sAVsSPfCN9UX44XiaoicbUJI6gOMAYyYuDxZ51FI70rCqWW323AoYLHYbdunn8eSQJYsh53EKoUssg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

知名博主 Ben Thompson 在使用 Deep Research 后写的一篇 Deep Research and Knowledge Value\[1\]，谈到了在信息搜索上带来的价值。Deep Research 极大的降低了信息整合的成本，以前要专门人去整理的工作，现在借助 Deep Research 十分钟左右就可以完成，但是它也很依赖于公开的信息，而且热门话题往往噪音多、信噪比差；小众/专业话题数据更集中且高质，价值更明显。

但对于小众信息来说，如果真正关键或独家数据并未对外公开，那么再强大的 AI 也无法查询到，最终会导致报告中出现“严重缺失”，反而并给人造成“似乎已经知道一切”的假象。

文章转载自「宝玉AI」，原文作者Ben Thompson，Founder Park 转载时做了结构调整。

“你是什么时候感受到 AGI 的？”

这是近来在 AI 圈子里广泛流传的问题，但想回答却并不容易。原因有二：首先，AGI 究竟是什么？其次，“感受”本身有点像对淫秽品的判定：正如美国最高法院大法官波特·斯图尔特在 Jacobellis v. Ohio\[2\] 一案中著名地表示：“我一看就知道。”

我在《AI 的不平衡到来》\[3\]一文中给出了自己对 AGI 的定义：

“o3 与推理时的规模化（inference-time scaling）表明的，是一种截然不同的场景：AI 可以实际接收任务，并有可靠的能力去完成任务。换句话说，这更像是一个独立工作者，而不是一个助手——更像是“弹药”，而不是“瞄准镜”。这也许是个奇怪的类比，*但它来自 Keith Rabois 在斯坦福的一次演讲\[4\]* ……我对 AGI 的定义是，它能成为“弹药”——也就是给它一个任务，它可以以足够好的成功率独立完成（我对 ASI（人工超级智能，Artificial Super Intelligence）的定义则是它能自己想出要做的任务）。”

至于问题里提到的“感受”部分，则是最近的新发现：**OpenAI 推出的 DeepResearch 感觉就像是 AGI；它相当于招来了一个新员工，而价格却只有每月 200 美元，真是不可思议。**

## **01**

**Deep Research 要点**

OpenAI 在 2 月 2 日的博客文章\[5\] 中宣布了 Deep Research：

> 今天 ChatGPT 推出全新智能体功能 Deep Research，可在互联网中进行多步研究来完成复杂任务。几十分钟内完成需要人类数小时的工作。
>
> Deep Research 是 OpenAI 新的智能体产品，只要给出提示，ChatGPT 就会在网上搜索、分析、综合数百信息源，生成媲美研究分析师的全面报告。它搭载了专为网页浏览和数据分析而优化的即将发布的 OpenAI o3 模型，能凭借推理能力处理海量互联网内容，并能根据过程中获得的信息灵活转向。
>
> 综合知识的能力，是创造新知识的前提。Deep Research 标志着我们向 AGI 的广泛目标迈出重要一步。我们长期以来设想的 AGI 能够进行真正的科学研究，并产出原创性的研究成果。

如今 OpenAI 的 AGI 定义变得复杂多变——Sam Altman 在昨天的文章\[6\]里，将 AGI 定义为“一个能在人类水平上在多个领域处理日益复杂问题的系统”。但如果按我更加温和的定义，Deep Research 恰好位于那段话中间所指向的范畴：它能综合研究，并在经济层面具备价值，但尚未创造出新的知识。

我在上周二的 Stratechery 更新\[7\]里已经展示了两个 Deep Research 的示例。虽然我建议大家阅读完整内容，这里我先概括一下：

1.  1\. 首先，我发表了自己对 Apple 最新财报\[8\] 的简要评论，包括三个观察点：

-   • 虽然 iPhone 销售同比下滑，但苹果依然创下了营收纪录，这成为该公司从硬件业务向服务巨头\[9\]转型的又一最新例证。

-   • 中国区销售再次下降，但这已不是新趋势，而是可追溯到近十年前的一贯走势，只是华为芯片禁令在当时给苹果在中国带来过短暂的提振。

-   • 尽管苹果高管声称 Apple Intelligence 带动了 iPhone 的销售，但从各地区的销售数据上并没有明显的支撑。

3.  2\. 其次，我使用了一个非常通用的提示词，让 Deep Research 生成了针对该财报的研究报告：

我是 Ben Thompson，Stratechery 的作者。这段身份信息很重要，因为我希望你能理解我之前对苹果的分析，以及我在 Stratechery 上写作的风格。请写一份关于苹果最新财报的研究报告，风格和语气与 Stratechery 相符，并符合我之前的分析观点。

1.  3\. 第三，我又用一个融入我财报见解的提示词生成了另一份 Deep Research 报告：

我是 Ben Thompson，Stratechery 的作者。这段身份信息很重要，因为我希望你能理解我之前对苹果的分析，以及我在 Stratechery 上写作的风格。我想要一份关于苹果 2025 财年第一季度（即 2024 年第四季度）的研究报告。以下是我特别感兴趣的几个角度：

\- 首先，服务收入对公司盈利的整体趋势。这个趋势如何延续？对利润率意味着什么？

\- 其次，关于中国市场的讨论。我的观点是，苹果近期在中国的下滑并不新鲜，而是过去近十年延续下来的长线趋势。华为芯片禁令只是在此过程中带来过短暂的回升。此外，我希望能结合对中国手机市场的更深层分析，探讨一线城市与其它城市的区别，以及这对苹果在中国市场前景的启示。

\- 第三，苹果在 AI 方面的前景如何？公司声称 Apple Intelligence 推动了已上线市场的销量。但这是不是因为中国市场尚未推出这项功能？

请用适合 Stratechery 的格式和风格来撰写报告。

你可以在那一期 Stratechery 更新\[10\]里阅读具体输出内容，而我当时的评价是：

> *第一个回答在指令非常简单的情况下，表现算是尚可；更多是一种总结，但也有一些不错的观点。第二个回答则更让我印象深刻。这个问题更多依赖于我以前写过的文章，并将我以往的观点融入到了答案里。说实话，从中我没学到什么新东西，但如果这是读者第一次接触这个话题，那他们肯定能学到一些。我也可以这样说：如果我是要找一个研究助理，那么至少就第二个答案而言，我会认真考虑雇用撰写该答案的人。*

换句话说，Deep Research 并不算是“枪管”，但至少在这个问题上，确实是一个相当不错的“弹药”。

## **02**

**Deep Research 示例**

不过，对我来说，这份“弹药”价值有限；我在录制早上 8 点的 Dithering\[11\] 播客前就已经看过 苹果财报电话会议的文字记录\[12\]，并马上得出了那三个观点。毕竟，我已经深入思考并报道苹果公司将近 12 年之久，这是我的“积累优势”。另外，如我之前所说，第二个 Deep Research 报告之所以有价值，是因为我事先提出了观点，然后 Deep Research 进行了论据支撑\[13\]；但这些支撑离我心中 Stratechery 的完整标准还差一大截（当然我对自己的要求带有主观偏见）。

不过，第二天我就发现了一个更有价值的使用案例：在进行采访前，我往往需要数小时来研究采访对象及其所处公司、行业背景等。那天我要采访 ServiceNow 的董事长兼 CEO Bill McDermott（我对这家公司有所了解，但并不算非常熟悉），于是我向 Deep Research 提出了请求：

我要采访 ServiceNow 的 CEO Bill McDermott，需要进行一些研究来准备我的问题。

首先，我想更多了解 McDermott 以及他的背景。最好能读到一些关于他的报道。我知道他以前在 SAP 工作过，我想了解他在那里的经历有哪些亮点，以及他为何、又是如何加入 ServiceNow？

其次，我想知道 ServiceNow 的背景。它是怎么创办的？最初的产品-市场契合点是什么？公司是如何逐步拓展的？哪些企业在使用 ServiceNow？

然后，ServiceNow 的商业模式如何？市场开拓策略是什么？McDermott 想讨论 ServiceNow 在 AI 领域的机遇。这些机会是什么？它们与简单的自动化有何不同或优势？用户对 ServiceNow 的评价又是怎样？有人觉得它的界面难看、难用吗？为什么它的客户粘性很高？企业为什么会被它吸引？ServiceNow 的竞争对手有哪些？它能成为其他企业的平台吗？还是说，未来有可能出现颠覆 ServiceNow 的机会？

你觉得我还应该问哪些其他问题？可以参考以往的 Stratechery 访谈，了解我通常会问哪些类型的问题

这个结果\[14\]对我来说非常有用，虽然其中给出的提问建议中规中矩，但至少给了我一个起点，省去了很多查资料的时间。我之后还是去看了财报之类的材料，随后完成了对 McDermott 的采访\[15\]。总的来说，单单这一个例子就值回我这个月的订阅费了。

另一个更有说服力的例子是关于我朋友的一件复杂医疗问题（出于隐私原因，我不会展示提示词和结果）。我那位朋友为这个问题已经奔波一年多，看了多个医生，尝试了各种方案。Deep Research 用 10 分钟就指出了一种他上周才从专科医生那儿听说的可能病因。尽管是否真能解决他的问题还未可知，但确实值得注意：Deep Research 可能在 10 分钟里完成了我朋友数月、多位专家、多次就诊的“信息收集”工作。

不过，最后一个例子才是最具启发性的：因为它也最能展现 Deep Research 的局限性。我就另一个朋友所在行业进行了深入的研究性询问：主要行业参与者是谁？供应链如何？客户群分布怎样？等等。我问得非常全面，结果 Deep Research 给出了一份条理清晰、内容丰富的报告。

问题在于，这份报告完全错误，但错得很“离奇”。若要对这种错误方式进行最恰当的概括，可引用美国前国防部长唐纳德·拉姆斯菲尔德的一段著名论述：

> ***“有些事是我们知道自己知道的（known knowns）。我们也知道有些事是我们知道自己不知道的（known unknowns）。但还有一些事是我们不知道自己不知道的（unknown unknowns）。”***

而 Deep Research 这份报告的最大问题在于：它彻底忽略了这个行业里的一家重要企业。该企业虽不知名，但在供应链中是非常主要的角色。任何关于该行业的报告如果没提到它，最仁慈的说法也只能称其“严重不完整”。

这其实就是拉姆斯菲尔德没有提到的第四种情况：“未知的已知（unknown known）”。读了 Deep Research 那份报告的人，以为自己已经掌握了这个行业的一切，却不知道自己实际缺了非常关键的一块信息。

## **03**

**知识的价值**

互联网时代最痛苦的启示之一，是我们发现“新闻其实一文不值”。我说的不是社会价值，而是经济价值：当一件事人尽皆知时，它虽然重要，但却无法通过“付费获取”的形式来变现；也就是说，新闻一旦公开，商业价值就被稀释了。我在《出版商与对过去的追寻》\[16\]中写道：

太多报业倡导者并没有真正理解这一点；事实上，报纸在过去能赚钱，并非因为其对社会的贡献，而是因为它们在各自的地区几乎垄断了平面广告业务。社会价值只是一种额外“附加”。因此，当 Chavern 抱怨“当今的互联网分发体系扭曲了优质新闻报道所带来的经济价值”时，实质上是把“社会价值”和“经济价值”混为一谈；后者并不存在，也从来没有存在过。

对过去缺乏正确认知，就导致了对当下的误判：谷歌和 Facebook 的利润并不是从新闻报道中“夺走”的，而是从报纸的**广告业务**中“夺走”的。而且，两大平台的产品和服务对用户极具吸引力，即使所有报纸内容都从平台上消失（欧洲的做法已经证明了这点\[17\]），用户也仍然会继续使用这些平台，而那些报纸只会损失更多流量和营收。

因此，试图在新闻上维系旧有模式是错的：报纸已经失去了对广告的垄断地位，在互联网时代也不可能再通过“打包内容”来竞争，同时“新闻”本身依旧对社会有价值，但从商业角度却“毫无价值”（受众越广，盈利越难；真新闻和假新闻都能免费传播）。

也许说“从来都是如此”有点过于绝对；在以摩擦和稀缺\[18\]为特征的传统纸质时代，与如今互联网的透明和丰盈\[19\]并没有完全可类比的切入点。但至少在我们曾经买报纸的时代，或许我们以为是为了获取新闻，而实际上是因为当地那家日报社拥有印刷机、送报卡车和广告销售团队，才得以维持营收。现在我们可以在社交媒体上免费获取新闻——好坏皆有，我有时甚至希望自己知道得少一点\[20\]。

然而，Deep Research 让我们看到了还有更多东西可以了解。互联网上有**海量**的东西可读，但显然没法指望任何个人真的把一切都读完。更糟糕的是，随着人类与 AI 生成的“水分内容”越来越多，想找到真正有价值的材料只会变得更加困难。值得一提的是，对于那些热门话题，Deep Research 反而常常给出质量比较差的结果，因为相关内容中鱼龙混杂，“水分”很多。相对冷门的话题，Deep Research 反而更容易找到真正权威且切中要害的论文和文章。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "null")

但这张图还不完整，因为正如我朋友那个行业的例子所示：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "null")

可以预见，Deep Research（以及同类 AI）未来很可能会成为史上最有效的搜索引擎：它能够找到并展示任何已公开的信息，从而让“以晦为明”（security through obscurity）终将走向消亡。此前我们经历了从“付费获取新闻”到“新闻免费推送”这一转变；而现在，则可能从“需要花费数小时研究一个主题”转变为“AI 可以随时为你提供一份详尽的报道”。

但前提是：这些信息必须是“公开可得”的。如果信息并不在互联网上，那 AI 也就无从得知。也就是说，这就是“保密”会在 AI 时代更具价值的原因。就拿前面提到的那家企业来说，由于它是私营公司，没有公开的财务文件或报告，官网也少得可怜，所以 AI 完全无法获取到它的存在。

在科技界，我们还有另一件与此类似的经典案例：亚马逊在 2006 年推出了 S3（AWS 的首个服务原型），之后又推出 EC2，从而彻底改变了初创企业与风险投资的方式（详见我对这一变化的分析\[21\]）。AWS 逐渐也把亚马逊自己的业务都迁到了云上，但当时外界并不知道 AWS 对亚马逊自身的影响究竟有多深远。起初 AWS 与 Amazon.com 的财报数据是合并的，直到 2012 年才算是从零售业务中单独出来，“AWS” 名义上被列入了“其他”收入项目，里面还包括信用卡和（当时规模很小的）广告收入等。

这项关键性的揭示出现在 2015 年：那年 1 月，亚马逊宣布会单独披露 AWS 的财务数据。根据当时路透社的报道\[22\]：

*多年来一直对投资者“冷若冰霜”的亚马逊，这次似乎“热情”了一些。美国最大的在线零售商在周四的第四季度财报电话会议上罕见地对外界敞开了一些信息，表示会在今年首次单独披露快速增长的云计算业务——Amazon Web Services（AWS）的业绩。*

*在发布第四季度财报时，亚马逊披露的信息量之大超出寻常，并且表示会注重提升效率，似乎也说明亚马逊开始更加听取华尔街的意见。一家私募银行的高级分析师 Rob Plaza 表示：“这季度，亚马逊展现出赚钱的能力，算是向外部展示了自己的实力。如果公司能保持 20% 左右的营收增速，同时还能盈利，那么股价自然会有正面反应。” 他又笑称：“不过我并不会因为这个就立刻买它的股票。”*

*即便如此，信息披露本身对投资者也是好事。多年来，投资者一直想知道这家增速最快、也可能是盈利能力最强的部门到底贡献了多少销售额。有分析师估计它占亚马逊总营收的 4%。*

事实证明，AWS 占总营收的比重实际接近 7%，盈利能力也比任何人想象的都要强。最终引发了亚马逊股价的大涨，我在《AWS 的 IPO》\[23\]一文中指出了这一点：

*科技行业最近有一次重大且重要的“IPO”，估值达 256 亿美元。这个数字超过了谷歌 IPO 时的 246 亿美元，更远高于亚马逊在上市首日 4.38 亿美元的估值。但需要注意，我说的“IPO”是指亚马逊的云计算服务 AWS，虽然它依旧属于亚马逊这家在 20 年前上市的电商公司。*

*我当然是在开玩笑——AWS 并没有真的进行 IPO，只是亚马逊在财报里单独列了这个项目。然而，这个新报表项目在 4 月 23 日至 4 月 24 日之间就让亚马逊的市值从 1820 亿美元增长到 2070 亿美元。因为 AWS 是云计算的先行者，市场需求还在扩张，并且它的经济模型也十分出色。它甚至有可能是亚马逊电商业务长期发展的关键支柱。*

这次市场对 AWS 新增披露的“惊喜”拉动了亚马逊约 256 亿美元的市值增长，但这个“惊喜”也带来了后续影响：微软和谷歌相继加大了云计算投入，如今 AWS 虽然仍在市场上占据领先地位，但竞争远比从前激烈。对消费者和客户来说，这当然是好事，不过也再度说明：有些“未知”本身就潜藏着很大的价值。

## **04**

**数据的浮现**

并不是说亚马逊不该披露 AWS 的财务数据。事实上，按照美国证监会的规定，当 AWS 收入占公司总营收的 10% 左右（现在已 15%）时，就必须单独列示。况且，AWS 的财务披露确实使投资者对亚马逊的业务更有信心，从而为其在物流等各方面进行进一步投资提供了支撑（也促成了亚马逊后来的物流体系转型\[24\]）。我在这里想强调的是，“保密”有其自身的价值。

那么，要思考的关键问题就是，像 Deep Research 这样的 AI 工具将会如何影响“保密”这件事。对冲基金一直明白“专有数据”的价值，会花钱买各种卫星图像、交通观测等信息，以此获取比市场更快或更精确的情报。可以想见，如果说所有公开信息都能被 AI 瞬间扫描和整合，那么单纯依靠阅读金融文件或通用数据去挖掘“阿尔法”就变得更加困难，能够提供“非公开信息”的服务就会越来越值钱。

**目前来看，Deep Research 在这一方面的能力还不算突出——比如说，我尝试让它生成一份关于 2015 年亚马逊财报披露变化的报告，结果并不理想。不过这也正是它“最糟糕”的阶段，未来只会越来越好。**

但对冲基金或类似机构的报告属于“私有产品”，它们不会公开。然而，这些研究却会以交易行为的方式体现在股价上——而股价作为一个“公开价格”，每个人都能看到。随着 AI 的快速发展，对一切都给出“类似搜索引擎”功能的时代里，价格信号的重要性只会不断攀升，也就引出了另一个话题：预测市场。

在 2024 年美国总统大选期间，预测市场迎来一阵热潮——它们对特朗普胜选的预测比主流民调更乐观\[25\]，并且最终被证明预测准确度更高。以后，随着 AI 的普及和信息的极度透明化，预测市场会变得更加重要，甚至可能是“必需”。因为当所有公开信息都能被 AI 处理后，“保密”就成了很多人的首选，而通过价格预测市场，人们可以用经济利益的方式鼓励信息（至少是其影响）得以传播。哪怕信息本身是保密的，市场价格信号也能有所揭示。

有趣的是，预测市场目前多和加密货币捆绑在一起，而加密货币在“AI 大爆发”的年代或许也将迎来新的机遇：当世界充斥无限的 AI 生成内容时，“数字稀缺性”和“可验证性”就会变得更有价值；而当一切变得高度透明时，“保密”也会变得更加珍贵。或许 AI 正是把这一切衔接起来的关键所在：通过可验证的信息和可理解的价格波动，我们才能从互联网上日益泛滥的“水分”内容中获取真正有意义的东西。

换句话说，AI 的出现使信息生态进一步拥挤不堪，但它也可能是唯一能在“信息噪音”中找到“信号”的工具。就像互联网时代让资讯极度透明、毫无门槛地涌现，同时却要求个人或公司投入更多精力去筛选真伪，并在此过程中催生了像我现在所做的这个独立品牌。AI 同样会令信息污染加剧，却也同时是唯一摆脱这片“泥淖”的方法。

## **05**

**Deep Research 的影响**

以上大多是对（不太遥远的）未来的展望；从目前来看，Deep Research 已经是科技界极具价值的一项工具。是的，每月 200 美元并不便宜，而且 Deep Research 仍然受到互联网上信息质量的限制，并极度依赖提示词的设计。此外，就我在熟悉的领域观察，它并没有给出真正能让我眼前一亮的创意。但与此同时，确有大量并不需要“创意”的工作——比如查找和综合信息——是大多数行业都必须完成的。对我个人而言，Deep Research 让我感觉更高效，而且说实话，我本来也不会去雇一个专职研究员。

但这带来了两层隐忧。首先，我之所以过去没雇研究员，是因为自己在做资料收集和筛选的过程中往往会有意想不到的收获：所谓“在去往目的地的路上，能学到更多东西”。而用 Deep Research 直接生成报告，可能会错过了这种“偶然的收获”。此外，那些尚未经历“12 年苹果财报追踪、30 年科技观察”训练的人，该如何跨越这些学习“门槛”？他们会不会因此失去积累经验、培养直觉的机会？

第二层隐忧则是就业。很多公司雇着研究员从事各个领域的调查分析工作，但如今 AI 工具带来的性价比或许会让人力难以维系。此前我对“AI 将取代大量知识型工作”这件事只停留在“理性思考”的层面，而亲身感受后才更深刻地意识到，这一点很快就要变成现实。

同样值得强调的是，我也提到“保密”可能变得更重要。故意设定“信息壁垒”，或确保自己掌握的数据不在公共域中，都是对 AI 过度透明化的一种反制方式。可以想见，在未来的 AI 世界里，那些能产生原创研究、真实数据以及对这些信息进行有效定价的基础设施和工具会愈加有价值。而那些“构筑围墙”“设置付费关卡”的做法，或许也是一些企业的必然选择，以便从他们（或他们的研究团队）深入现实世界所获得的独家见解中收取“租金”。

以现在的趋势看，AI 的威力主要来自它对“所有公共信息”的整合；而人们的（或许徒劳的）应对方式是努力让更多信息保持“不公开”。我们也许会看到，未来会有人在城市、社区甚至更大范围内去建立各类封闭式平台或交易市场，以便把自己收集到的原创信息牢牢捂在内部，并只通过某种形式的付费或协议向外展示少量信息。这些都体现了知识在 AI 时代重新被定价的可能性。

总而言之，随着 AI 的不断发展，我们会看到许多令人惊叹的进步，也会被迫直面信息过载、创意不足以及就业压力等严酷现实。但正如互联网时代“透明”与“污染”并存，给了我们通过独立品牌或媒介建立个人信誉与影响力的机会一样，AI 时代也会在加剧“信息泛滥”的同时，为我们带来新的解决思路和商业模式。Deep Research 只是一块敲门砖，透过它，我们可以瞥见下一个时代的更多可能性。

---

作者：Ben Thompson

#### 引用链接

`[1]` Deep Research and Knowledge Value:*https://stratechery.com/2025/deep-research-and-knowledge-value/*`[2]`Jacobellis v. Ohio:*https://supreme.justia.com/cases/federal/us/378/184/*
`[3]`《AI 的不平衡到来》:*https://stratechery.com/2025/ais-uneven-arrival/*
`[4]`Keith Rabois 在斯坦福的一次演讲:*https://www.youtube.com/watch?v=6fQHLK1aIBs*
`[5]`2 月 2 日的博客文章:*https://openai.com/index/introducing-deep-research/*
`[6]`昨天的文章:*https://blog.samaltman.com/three-observations*
`[7]`上周二的 Stratechery 更新:*https://stratechery.com/2025/apple-earnings-openai-deep-research-the-unbundling-of-substantiation/*
`[8]`Apple 最新财报:*https://www.apple.com/newsroom/2025/01/apple-reports-first-quarter-results/*
`[9]`服务巨头:*https://stratechery.com/2024/boomer-apple/*
`[10]`那一期 Stratechery 更新:*https://stratechery.com/2025/apple-earnings-openai-deep-research-the-unbundling-of-substantiation/*
`[11]`Dithering:*https://dithering.passport.online/member/episode/apple-earnings?guid=https%3A%2F%2Fdithering.passport.online%2Fmember%2Fepisode%2Fapple-earnings*
`[12]`苹果财报电话会议的文字记录:*https://sixcolors.com/post/2025/01/this-is-tim-and-kevan-apples-q1-results-call-transcribed/*
`[13]`Deep Research 进行了论据支撑:*https://stratechery.com/2022/the-ai-unbundling/*
`[14]`这个结果:*https://chatgpt.com/share/67a231d2-49c4-8011-a18f-751e435a9820*
`[15]`完成了对 McDermott 的采访:*https://stratechery.com/2025/an-interview-with-servicenow-ceo-bill-mcdermott-about-enterprise-ai-agents/*
`[16]`《出版商与对过去的追寻》:*https://stratechery.com/2017/publishers-seek-antitrust-exemption-news-versus-advertising-a-better-solution-for-publishers/*
`[17]`已经证明了这点:*https://stratechery.com/2014/economic-power-age-abundance/*
`[18]`摩擦和稀缺:*https://stratechery.com/2013/friction/*
`[19]`透明和丰盈:*https://stratechery.com/2015/aggregation-theory/*
`[20]`希望自己知道得少一点:*https://x.com/schopenhauernow/status/1887189824185958603?s=46*
`[21]`我对这一变化的分析:*https://stratechery.com/2015/venture-capital-and-the-internets-impact/*
`[22]`路透社的报道:*https://www.reuters.com/article/technology/aws-move-disclosure-suggest-amazon-yielding-more-to-wall-street-idUSKBN0L305S/*
`[23]`《AWS 的 IPO》:*https://stratechery.com/2015/the-aws-ipo/*
`[24]`物流体系转型:*https://stratechery.com/2016/the-amazon-tax/*
`[25]`它们对特朗普胜选的预测比主流民调更乐观:*https://www.wsj.com/politics/elections/how-the-trump-whale-and-prediction-markets-beat-the-pollsters-in-2024-dd11ec4e*

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Founder Park 正在搭建开发者社群，邀请积极尝试、测试新模型、新技术的开发者、创业者们加入，请扫码详细填写你的产品/项目信息，通过审核后工作人员会拉你入群～**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

进群之后，你有机会得到：

-   高浓度的主流模型（如 DeepSeek 等）开发交流；

-   资源对接，与 API、云厂商、模型厂商直接交流反馈的机会；

-   好用、有趣的产品/案例，Founder Park 会主动做宣传。

---

---

**更多阅读**

[中美 AI 创业者的闭门讨论：DeepSeek-R1 之后，AI 创业的变化和新趋势](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247514229&idx=1&sn=1c4d6a586667750867a9f2153212ba02&scene=21#wechat_redirect)

[DeepSeek R1 之后，重新理解推理模型](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247514239&idx=1&sn=e39e9f2b1d92ee64df429f7d6c9ada11&scene=21#wechat_redirect)

[Lex Fridman 五小时聊 DeepSeek：一文看懂 DeepSeek 的创新与2025 AI 趋势](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247514199&idx=1&sn=1c4c919d850e131e898e086ddfdca3f0&scene=21#wechat_redirect)

[拾象科技李广密：对 DeepSeek 和智能下半场的几条判断](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247514187&idx=1&sn=8b951d368aa93f465b6dbda3d32a3239&scene=21#wechat_redirect)

[台积电张忠谋万字访谈：如何拿下黄仁勋、苹果和高通，成为全球最大芯片代工厂？](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247514171&idx=1&sn=0f00a05b0eba78c256bc72dd9dbbc34a&scene=21#wechat_redirect)

[SemiAnalysis万字解析DeepSeek：训练成本、技术创新点、以及对封闭模型的影响](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247514161&idx=1&sn=eddc22223f2422bbc8181e6b31c1d912&scene=21#wechat_redirect)

转载原创文章请添加微信：founderparker