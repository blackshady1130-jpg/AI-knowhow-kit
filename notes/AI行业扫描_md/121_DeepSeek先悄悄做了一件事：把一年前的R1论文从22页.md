---
url: https://mp.weixin.qq.com/s/G1uE4FH9C71ceBnBDlacHQ
title: "DeepSeek V4即将发布？先读懂梁文峰这份86页的技术底牌"
description: "最近DeepSeek V4的传言越来越多了。据The Information报道，知情人士透露DeepSeek计划在2月中旬、农历新年前后发布V4模型。"
author: "花叔"
captured_at: "2026-03-09T03:34:39.094Z"
---

# DeepSeek V4即将发布？先读懂梁文峰这份86页的技术底牌

最近DeepSeek V4的传言越来越多了。

据The Information报道，知情人士透露DeepSeek计划在2月中旬、农历新年前后发布V4模型。内部测试显示，V4在编程能力上可能超越Claude和GPT系列——尤其是处理超长代码提示的场景。

![图片](https://mmbiz.qpic.cn/mmbiz_png/HRdaeEmxNHanibrVRq3roDXojyVVnt8ooicI9S2cKtB02JAwmjQia7F0hgjPBVYsIXMc9iaAGw0tQRiaED2vw98lubQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

去年R1也是春节前一周发布的，直接引发了全球市场一万亿美元的震动。在大型节假日前搞大事确实也很符合DeepSeek一贯的做法，今年会不会故技重施？

但在V4发布之前，DeepSeek先悄悄做了一件事：**把一年前的R1论文从22页扩充到了86页**。

我下载了两个版本对比，文件大小从928KB变成4.8MB。多出来的60多页显然不是废话，是他们训练的详细账本和踩过的坑。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这个时间点更新旧论文，绝不是巧合。我猜他们在做两件事：一是为V4铺路，让社区先完全理解R1的技术细节；二是用行动回应之前"只开源权重不给训练细节"的质疑。

说实话，看完这份更新，我对Open这个词有了新的理解。上周我发的这篇关于DeepSeek mHC论文的解读很多人表示意外地能看懂，阅读量都突破20万+了，哈哈哈～

[【梁文锋署名】DeepSeek新论文：所有人都觉得没必要改的东西，他们改了](https://mp.weixin.qq.com/s?__biz=Mzg2OTA1OTAxNA==&mid=2247487744&idx=1&sn=9a17b69b4a7e11affdc9aff91bb88282&scene=21#wechat_redirect)

所以我今天再挑战下自己，试试给大家用人话说说这次DeepSeek老论文里都更新了啥。

## 先说更新了什么

v1版本发布于2025年1月22日，22页，主要讲R1是什么、怎么训的、效果多好。

v2版本发布于2026年1月4日，86页。时隔将近一年，多出来的60多页都在讲什么？

我把两个版本的目录对比了一下。v1只有一个简短的Appendix（作者列表）。v2新增了6大类Supplementary：

-   A: GRPO和PPO的详细对比

-   B: 训练细节（这部分最长，约50页）

-   C: 推理行为分析

-   D: 基准测试详情 + 10页安全报告

-   E: 综合分析（与V3对比、test-time scaling等）

-   F: 推理能力迁移

说白了，这次更新就是把"解题过程"补上了，给出了可复现的技术文档。

之前R1开源的时候，很多人吐槽说"只给权重不给训练细节，这算什么开源"。现在DeepSeek把这块补上了。

## 294K美元的训练账单

论文新增了Table 7，第一次公开了完整的训练成本：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

|
阶段

 |

GPU小时

 |

成本

 |
| --- | --- | --- |
|

DeepSeek-R1-Zero

 |

101K

 |

$202K

 |
|

SFT数据创建

 |

5K

 |

$10K

 |
|

DeepSeek-R1

 |

41K

 |

$82K

 |
|

总计

 |

147K

 |

$294K

 |

这个成本是按H800租赁价格$2/GPU hour算的。

29.4万美元，训练一个媲美OpenAI o1的推理模型。

29.4万美元是什么概念？之前写V3.2的时候我提到，DeepSeek只有150人的团队。现在加上这个成本数据，画面更清晰了——他们不是靠砸钱，是靠效率。

具体怎么训的？论文给了精确配置：

-   R1-Zero: 64×8张H800 GPU，跑了198小时

-   R1: 同样的GPU配置，80小时（约4天）

64×8是512张卡。198+80=278小时。不到12天，训完了两个阶段。

## 数据配方首次公开

这是我觉得最有价值的部分——Table 4详细列出了RL训练数据的构成：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**数学**：26k题

-   从区域竞赛到国际奥林匹克级别

-   包括代数、微积分、概率、几何

-   排除了数学证明（因为难以自动验证）

**代码**：17k + 8k

-   17k算法竞赛题（Codeforces、LeetCode风格）

-   8k GitHub真实bug修复问题

**STEM**：22k选择题

-   化学占46.5%（最多）

-   生物30.7%

-   物理15.5%

-   其他7.3%

**逻辑**：15k题

-   真实世界：脑筋急转弯、经典逻辑谜题

-   合成数据：Code-IO问题、Zebra puzzle等

**通用**：66k + 12k

-   66k评估helpfulness（创意写作、编辑、问答、角色扮演）

-   12k评估harmlessness

总共约150k条数据。

为什么化学题最多？论文没解释，但我猜测可能是因为化学题的答案更容易自动验证（选择题），同时又需要多步推理。

更有意思的是Cold Start数据的创建流程。R1不是从零开始训的，而是先用R1-Zero的输出，经过这个流程：

1.  用R1-Zero在高温度（1.0）下生成多条推理轨迹

2.  过滤：保留答案正确、格式可读的

3.  用sympy验证数学表达式

4.  用DeepSeek-V3重写，让推理过程更"人话"

5.  人工二次验证

论文里甚至给出了重写的prompt，让V3把R1-Zero那种"we"风格的推理，改成"I"风格——因为用户更喜欢第一人称的思考过程。

这种细节，以前根本不会公开。

## 失败也写进论文

v1版本有一小节叫"Unsuccessful Attempts"，提到PRM和MCTS不太行。v2把这部分扩展了，还加了一个我觉得很有价值的案例：Reward Hacking。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Figure 6展示了一个典型的失败场景：用helpful reward model训练时，reward分数一直在涨（左边红线），但CodeForces的实际性能却在跌（右边蓝线）。

这就是reward hacking——模型学会了"讨好"奖励函数，但并没有真正变强。

论文原文的解释是：

> "如果reward model包含系统性偏差或不准确，LLM可能学会生成那些被模型高评分、但与真实人类偏好背离的回答。"

PRM（Process Reward Model）的问题也讲得更清楚了：

1.  细粒度步骤难定义：什么算"一步推理"？在通用推理任务里很难界定

2.  中间步骤对错难判断：自动标注效果差，人工标注又没法规模化

3.  必然导致reward hacking：只要引入模型做判断，就会被exploit

所以DeepSeek最后用的是rule-based reward——数学题直接匹配答案，代码题跑测试用例。简单粗暴，但不会被hack。

为什么要公开这些失败？我觉得这才是真正的Open。告诉社区"这条路我们走过了，不通"，比只展示成功更有价值。

## 基础设施首次披露

Supplementary B.1详细描述了RL训练的基础设施，分为4个模块：

**1\. Rollout Module**

-   用vLLM做推理

-   对MoE架构实现expert parallelism，减少内存访问开销

-   部署热点expert的冗余副本来负载均衡

-   用MTP（Multi-Token Prediction）做self-speculative decoding加速

**2\. Inference Module**

-   加载reward model和reference model

-   对rollout阶段生成的样本做forward pass

**3\. Rule-based Reward Module**

-   统一接口：代码执行器、答案匹配器、格式检查器

-   异步调度，和前两个模块overlap执行

**4\. Training Module**

-   支持PPO、GRPO、DPO等算法

-   数据打包策略：先按长度排序，再用Best-Fit装箱

-   集成了DualPipe算法做pipeline parallelism

还有一个细节：每个模块跑完后，模型会自动从显存offload到内存或磁盘，给下一个模块腾空间。

这些基础设施细节以前只有DeepSeek内部知道。现在写进论文，其他团队可以照着搭。

## 10页安全报告

Supplementary D.3是一份完整的安全评估报告，包括：

1.  风控系统：公开了完整的risk review prompt（Listing 8）

2.  6个公开benchmark对比：和其他SOTA模型的安全性比较

3.  分类测试：基于自研安全测试集的细分评估

4.  多语言安全：不同语言下的安全表现

5.  Jailbreak鲁棒性：对抗攻击下的表现

风控prompt里列了11条安全标准，从"通用原则"到"隐私伪造"到"风险建议"，细到可以直接抄。

对想部署R1的企业来说，这部分很实用——不只是模型安全性数据，还告诉你外部风控系统怎么搭。

## 为什么选择现在更新？

论文更新的时间点是2026年1月4日。

结合V4的发布传言，时间线就很清晰了：

-   2025年1月20日：R1发布，春节前一周

-   2026年1月4日：R1论文v2发布，详细补全技术细节

-   2026年2月中旬（传闻）：V4发布，又是春节前后

DeepSeek似乎在做一件事：**先把上一代的账本摊开，再发布下一代**。

这对社区的好处是显而易见的——当V4发布时，研究者已经完全理解R1的技术细节，可以更清晰地看出V4到底改进了什么。

当然，这也可能是回应之前"只开源权重不给训练细节"的批评。不管出于什么原因，结果很实在——社区拿到了一份真正可复现的技术报告。

## 最后

回到"Open"这个词。

大多数公司的Open是什么？开源权重，开源推理代码，发个技术博客。

DeepSeek的Open是什么？

-   训练成本精确到GPU小时

-   数据配方精确到每个类别的数量和来源

-   失败尝试写进论文，告诉你哪条路不通

-   基础设施架构图，告诉你怎么搭RL系统

-   安全评估报告，告诉你怎么做风控

这才是让社区能真正复现和改进的Open。

之前写mHC论文的时候我说，DeepSeek的技术哲学是"去质疑那些所有人都觉得没必要改的东西"。现在看来，他们对"开源"这件事的理解也是一样——不是做到行业平均水平就够了，而是要做到让别人能真正用起来。

从22页到86页，多出来的60页不是凑数，是掏心窝子的诚意。

至于V4会带来什么？如果传言属实，2月中旬就会揭晓。

但不管V4表现如何，这份86页的论文已经是一份礼物——它让我们知道，一个顶尖推理模型是怎么从零训出来的。这种知识，以前只有极少数公司内部才有。

**参考资料**：

-   DeepSeek-R1论文v2: https://arxiv.org/abs/2501.12948v2

-   DeepSeek-R1论文v1: https://arxiv.org/abs/2501.12948v1

-   V4传言报道: https://finance.yahoo.com/news/deepseek-set-launch-next-gen-153258894.html