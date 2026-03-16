---
url: https://mp.weixin.qq.com/s/O7-gv2g4I9XSGiMeivbUFA
title: "500行代码构建对话搜索引擎，贾扬清被内涵的Lepton Search真开源了"
description: "Lepton Search开源代码来了。"
captured_at: "2026-03-08T11:24:42.570Z"
---

# 500行代码构建对话搜索引擎，贾扬清被内涵的Lepton Search真开源了

机器之心报道

**编辑：杜伟**

> 你可以说我「借鉴」，但我是真开源。

来了，贾扬清承诺的 Lepton Search 开源代码来了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gW8d0Iib8tdrWKc6XpMQplfibe3oaeD0Z1oejzhzVpfXcr8yGhHgh78w8VconqVeFqKTnicx8lhWYGcKQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

前天，贾扬清在 Twitter 上公布了 Lepton Search 的开源项目链接，并表示任何人、任何公司都可以自由使用开源代码。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

项目链接：https://github.com/leptonai/search\_with\_lepton

也就是说，你也可以用不到 500 行 Python 代码构建自己的对话搜索引擎了。

今天，Lepton Search 又登上了 GitHub trending 榜单。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

此外已经有人将这个开源项目用来构建自己的 Web 应用程序了，并表示质量非常高，与 AI 驱动的搜索引擎 Perplexity 不相上下。 

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

而就在几天前，关于 Lepton Search 项目，贾扬清还与 Perplexity 这家 AI 搜索引擎初创公司的印度裔创始人展开了一场「隔空对话」。

**demo 被内涵，贾扬清选择开源**

自贾扬清离开阿里创业之后，有关新公司 Lepton AI 的动态一直挺受社区的关注。

1 月 25 日，贾扬清在 Twitter 上宣传了一个 demo，用不到 500 行 Python 代码实现了 AI 对话搜索引擎，展现了构建 AI App 变得如此简单。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

据了解，Lepton Search 具有以下特征：

-   内置支持大语言模型（LLM）

-   内置支持搜索引擎

-   自定义 UI 界面

-   搜索结果可共享、缓存

此外，Lepton Search 背后使用 MistralAI 开源的 [Mixtral-8x7b](http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650904018&idx=4&sn=dc55a2e3c3837a2c3ab68ae09a506a78&chksm=84e451acb393d8baa5a341e5ffe81798edd5f0aaa01c2238bc91cf5be325910c5bfb4b999eab&scene=21#wechat_redirect) 作为支撑模型，运行在 LeptonAI 的 playground 托管平台上，吞吐量高达 200 tokens / 秒。该搜索引擎目前使用的是必应搜索 API，Lepton KV 作为无服务器存储。

贾扬清表示，Lepton Search 的 idea 受到了 Perplexity AI、Phind 等由 LLM 驱动的搜索引擎的启发。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

其中， [Perplexity AI](http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650902401&idx=3&sn=fc30a32911bd9417680924f416c0e182&chksm=84e44bffb393c2e95865f2ef9e26d813c93298e95d124addfc70606b66d15c8b3eb6c8f75f2e&scene=21#wechat_redirect) 成立于 2022 年 8 月，是世界上首个对话式搜索引擎，通过 GPT 这样的先进 AI 技术，它能够为问题直接生成答案，并对准确率与效率有很高的标准。该公司由前 OpenAI 研究科学家 Aravind Srinivas （Perplexity CEO）与前 Meta 研究科学家 Denis Yarats（Perplexity CTO）等合伙人共同创办。

该搜索引擎在发布后广受欢迎，被越来越多的人使用，并对谷歌等传统搜索引擎发起挑战。1 月初，该公司宣布完成了 7360 万美元 B 轮融资，最新估值 5 亿美元。

在看到贾扬清 Lepton Search 的 demo 后，Aravind Srinivas 发表了一段话，「非常高兴看到 Perplexity 成为未来融资活动的标杆，连前阿里巴巴技术副总裁都来借鉴。这说明了 Perplexity 的影响力不再停留在产品自身，还延伸到了整个生态圈层和行业发展。」

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

评论区的网友更是直白，认为 Lepton Search「复刻」了 Perplexity AI 的界面。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

面对 Aravind Srinivas 的善意之言（kind words），贾扬清回应称，自己非常喜欢 Perplexity，它从根本上改变了人们对搜索的看法。Lepton AI 则专注于让创作者更轻松构建 AI 应用程序的现代云解决方案，Lepton Search 的 demo 展示了如何实现这一目标。当然该搜索项目的代码也会开源。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

于是，我们看到了「search\_with\_lepton」项目。目前，该项目已经积累了 1.1k 的 Star 量。贾扬清也兑现了自己的开源承诺。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gW9LSvGJnGeMgN5icZW9coZAvicwuFyhFM09n7QicLPKzKr3WHYGIdVvlVUA20KPvDWYDKFKvXlXMz5XA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

© THE END 

转载请联系本公众号获得授权

投稿或寻求报道：content@jiqizhixin.com