---
url: https://mp.weixin.qq.com/s/yFQ4FObR8P0c_R7x05zP_A
title: "参加完 OpenAI 的活动，我看到了「草莓」的隐患"
description: "o1 将直面一堆问题\\x0d\\x0a当然，不只是 o1"
author: "金色传说大聪明"
captured_at: "2026-03-08T12:24:31.729Z"
---

# 参加完 OpenAI 的活动，我看到了「草莓」的隐患

## 背景

我常参加各种分享会。

之前有一场 OpenAI 的，主题是管理「自主 AI 系统」（Agentic Systems）。所讲的东西，与 o1 的的关注点极其相似：**管控 AI 的自主行为**

相关内容曾发过：

《[OpenAI：搞 Agent 时，你要注意这些](http://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247488117&idx=1&sn=91a8b45f6bba15e92fff8c1199ac8c5a&chksm=c2bcdf73f5cb5665337422aba4c6e6dcec1fcd1cba0e81aaa2ba8b3ec0eeb0a464d194119f48&scene=21#wechat_redirect)》

那时o1 还没发布，所以大家对里面的说辞，可能没太大感觉

在这篇文章里，我会先铺垫一点背景信息，然后从落地角度，来谈谈这里现在、以及将来会遇到的一些挑战，主要包括：执行效果评估、危险行为界定、默认行为确定、推理透明展示、Agent 行为监控、Agent 作恶追责、危险事故叫停。

我得明确：**OpenAI 会面对这些挑战，并非是其水平不行，而是更早的开始探索边界 -- 大家都将会遇到**

---

## 相关阅读

之前写了 3 篇关于 o1 的内容：

-   《**[「草莓」实测：可能只是工程 Trick，且有扣费陷阱！](http://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247491570&idx=1&sn=97bced49c9792645088895907be33737&chksm=c2bcd2f4f5cb5be2fe2b96583b914991b95b23df59aa7059c51519562470b492d948ac8ea866&scene=21#wechat_redirect)**》

-   《**[150 行代码，复刻「草莓」，青春版支持联网](http://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247491584&idx=1&sn=503894952c1d69935176efde5998b634&chksm=c2bf2d06f5c8a4104fb0e0897c2b3164d95e3071d3f27e4ab00489ebff8d14677bc091600513&scene=21#wechat_redirect)**》

-   《[**o1 能带我们走进 AGI 吗？**](http://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247491606&idx=1&sn=688b08923aed6299693c403b8cd76894&chksm=c2bf2d10f5c8a4068f90b41881c7679bc0c625ad15f9c2fe6322842e1d6b82bcdf2b9e9b2813&scene=21#wechat_redirect)》

这里有一篇关于 Agent 治理的论文，来自 OpenAI

https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

---

## 有关 Agent

按当前的语境，我们会把 ChatGPT 就是看成一种 AI 应用，它能理解你的问题并给出回答。而会把 GPTs 这种订制后的、能调用外部功能的、能够自己处理复杂任务的产品，叫做 Agent。

Agent 和 AI应用（如ChatGPT）之间的区别和联系主要体现在“代理性”（agenticness）这的程度上。如果一个AI系统，能够在没有直接人类监督的情况下运作，其自主性越高，我们称之为代理性越强。这是一个连续体，不是非黑即白的判断，而是根据它在特定环境中的表现来评估其代理性的程度。

在这种定义下，正统 Agent 不仅能回答问题，还能自己决定做什么，它能够通过生成文本来“思考”，然后做出一些操作，甚至能创造出更多的 AI 帮手来帮帮忙，就比如下面这个图。（**仔细看这个 Twitter 图，是不是和 o1 很像？**）

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

（再补一张一年前， 时任 OpenAI Dev Rel 的 Logan 的发言）

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

但我们发现，尽管 Agent 看起来很美好，但在实际落地的场景中，也是困难重重，风险多多，出现了问题，责任划分也很麻烦。比如这里：如果我希望让某个 Agent 帮我微信收款，但它给别人展示的是付款码，那么这里谁背锅？

这些问题，也将会是 o1 在真正行业落地时，所要面对的。

---

## 落地难点

由于会上的 PPT 不便分享，我便在自己吸收后，重新制作了一份 PPT，安心食用

01

执行效果评估

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在商业环境中，确保任何工具的可靠性是基本要求。

然而，AI Agent 的复杂性在于其工作场景和任务的不确定性。例如，一个在模拟环境中表现优异的自动驾驶车辆，可能因现实世界中不可预测的变量（如天气变化和道路条件）而表现不稳定。

我们尚缺乏有效的方法，来准确评估 AI Agent 在实际环境中的性能。

02

危险行为界定

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

AI Agent 在执行高风险操作之前需要获得用户的明确批准。例如，在金融领域，AI 执行大额转账前必须得到用户同意。

但需要注意，频繁的审批请求可能导致用户出现审批疲劳，从而可能无视风险盲目批准操作，这既削弱了批准机制的效果，也可能增加操作风险。

03

默认行为确定

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

当 AI Agent 遇到执行错误或不确定的情形时，是要有一个默认行为的。例如，如果一个客服机器人在不确定用户需求时，其默认行为是请求更多信息以避免错误操作。

然而，频繁的请求可能会影响用户体验，因此在保障系统安全性与保持用户体验之间需要找到平衡。

04

推理透明展示

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

为了保证 AI Agent 决策的透明性，系统需要向用户清晰展示其推理过程。举例来说，一个健康咨询机器人应详细解释其提出特定医疗建议的逻辑。

但如果推理过程太复杂，普通用户可能难以理解，这就需要在确保透明性和易理解性之间找到平衡。

05

Agent 行为监控

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

假设一个 AI 系统用于监控仓库库存，如果监控系统误报，误认为某项商品缺货，进而不断的进货，那么可能导致库存的严重积压，并造成极大损失。

于是，我们思考：是否需要另一个 Agent 来监控这个 Agent？成本账怎么算？

06

Agent 作恶追责

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

考虑一个匿名发布内容的 AI Agent，如果其发布了违规内容，要追踪到具体负责的人或机构可能极其困难。这种情况下，建立一个能够确保责任可追溯的系统尤为关键，同时还需要平衡隐私保护和责任追究的需求。

07

严重事故叫停

*![图片](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYrI3uacFWaKypCXZjERibZjbx7OgNVgrY9qISxRibhU3qlqsdSxlxS44y0RnGIcMxBUVlDFdBrImq8A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)*

想象一个用于自动化工厂管理的 AI Agent，在系统检测到严重故障需要立即停机时，不仅需要停止主控系统，还要同步关闭所有从属设备和流程。如何设计一个能够迅速且全面响应的紧急停止机制，以防止故障扩散或造成更大损失，是一项技术和策略上的复杂挑战。

---

## 最后

个人来说，希望大家来思考这个问题

《[**对于 AI & AGI，我有 3 个问题**](http://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247489796&idx=1&sn=2d2a1c814e4703d3a3ab6b83c76ea634&chksm=c2bcd402f5cb5d1491c4fd69f50d64c8a2738f4981635c213f378a3e3cfac8a59ed68cd80a05&scene=21#wechat_redirect)》