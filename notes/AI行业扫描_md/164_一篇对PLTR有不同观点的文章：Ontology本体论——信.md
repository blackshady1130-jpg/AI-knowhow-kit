---
url: https://mp.weixin.qq.com/s/uhM-teLeGULXrpNgMO-xmQ
title: "Ontology本体论——信息差下的技术垃圾"
description: "作为从业者，这样的概念能得到追捧，我们都有责任"
author: "Mercy"
captured_at: "2026-03-09T03:43:21.123Z"
---

# Ontology本体论——信息差下的技术垃圾

Dumpster fire

最近数月，随着AI生成内容占据中文技术世界，Ontology开始获得关注，但是其名声和英文世界却是完全两级。

在全球范围内，讨论Ontology及PLTR的声音分为两种：80%是散户投资者发出的随机噪音，20%是深受其苦的用户工程师的愤怒控诉。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/at32qdQsdwFSVy7GE1s1EpehHaQibYns30BE1UdrMAe8ystuiamdthU9wybKIIqc1cSGo1QicoBNd793lMW9VYbAhcq3YNt1ia44WbXOneh2v8U/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/at32qdQsdwGytibnp188MIwbZ253yx64PyogqIUBRcQel779dJLKA2VJWnXSEbZof0eiaEBxM7PfgWoQdqdmibDOcibzJZXAtuz4kQdCmtriagUo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/at32qdQsdwGIp79qWUADtOnicibtF95piaqqcyLWhNHhx9wXbfURES1IVEK8eUAeOLkBLdamH4vGOicSADrmaOQr3mUNBr2AAic4OoJSzdNtNeo8/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

不同于硬件，软件之间的差距可以是千百倍，而PLTR证明，一个烂软件甚至可以通过面向高管的概念和脱裤子放屁的功能，让用户整体技术水平倒退。

Ontology就是PLTR实现这一壮举的核心。

Ontology，一万个零件组成的太阳能手电

PLTR是一家开放的公司，其文档之丰富、Demo教学之透明堪称B2B软件领域之典范。我们借此可以了解Ontology这个概念/功能的每一个细节。//这或许证明Alex Karp虽然对技术一窍不通，但是个有点纯真理想的人.

Ontology是一种数据模型，将所有信息用一种语言表达，实现单一事实数据来源。它也定义了如Object、Link、Action、Function、Interface、Dataset、Virtual table、Model等等子概念，以实现通过可以操作、互动的数据模型。

![航空本体论](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

从Ontology的架构图（上）不难看出，其设计者没少读Solace的文档（下）

对于不了解软件技术的人而言，这听起来像是某种魔法，可以让软件通过一个数字孪生与现实世界交互，甚至还能积累语义数据为AI时代做准备。

但是这禁不起细想，其实你家的扫地机器人、Openclaw、聊天软件、扫码点餐、任何一个ERP/OA，都是通过数据模型实现与现实交互，短视频、购物应用甚至在LLM出现前就一直利用AI大规模分析数据。

Ontology并不是神奇魔法，软件发展了半个世纪，数据库Schema、RESTful、ORM....有太多工具和标准可以构建数据模型了，和Ontology相比，这些标准的区别或许在于真正能用且不会一年收$1M授权钱。

买了PLTR的人会说，Foundry+AIP+Ontology才是完全体，虽然数据模型是复杂了点，但是用上全家桶的企业，每个员工都能开发AI Ontology应用。

基于具体用例不难发现，使用Ontology方法开发是将简单问题指数级复杂化。

我们选择一个Palantir官方教学频道Ontologize的推荐用例，分析使用Ontology和上世纪流行的开放标准SOAP开发这个用例时孰优孰劣。

这是一个学习助手应用，用户可以上传笔记，一键让AI生成针对这个笔记和考试的问题卡。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Ontologize视频中用了37分钟实现了这个应用，而用Cursor+SOAP，只需要一句话+两分钟，就能做出更好用的效果。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

<table><tbody><tr><td data-colwidth="83"><section><span leaf=""><span textstyle="">步骤</span></span></section></td><td data-colwidth="193"><section><span leaf=""><span textstyle="">SOAP(来自1998年）</span></span></section></td><td data-colwidth="299"><section><span leaf=""><span textstyle="">Ontology</span></span></section></td></tr><tr><td data-colwidth="83"><section><span leaf=""><span textstyle="">第一步</span></span></section></td><td data-colwidth="193"><section><span leaf=""><span textstyle="">定义一个 XSD 文件，写清楚：</span></span><code data-path-to-node="4,1,1,0" data-index-in-node="16" data-pm-slice="0 0 []"><span leaf=""><span textstyle="">Flashcard</span></span></code><span leaf=""><span textstyle="">&nbsp;有三个字段（Q, A, ID）。</span></span></section></td><td data-colwidth="299"><section><span leaf=""><span textstyle="">在 Ontology Manager 里手动点击，创建 Flashcard 对象类型。</span></span></section></td></tr><tr><td data-colwidth="83"><section><span leaf=""><span textstyle="">第二步</span></span></section></td><td data-colwidth="193"><section><span leaf=""><span textstyle="">把&nbsp;</span></span><code data-path-to-node="4,2,1,0" data-index-in-node="2" data-pm-slice="0 0 []"><span leaf=""><span textstyle="">Exam</span></span></code><span leaf=""><span textstyle="">&nbsp;的 ID 写进 XSD。</span></span></section></td><td data-colwidth="299"><section><span leaf=""><span textstyle="">继续在UI上手动点击，创建&nbsp;</span></span><section><code data-path-to-node="4,2,2,0" data-index-in-node="9"><span leaf=""><span textstyle="">Exam</span></span></code><span leaf=""><span textstyle="">&nbsp;对象，定义主键、外键。</span></span></section></section></td></tr><tr><td data-colwidth="83"><section><span leaf=""><span textstyle="">第三步</span></span></section></td><td data-colwidth="193"><section><span leaf=""><span textstyle="">没了</span></span></section></td><td data-colwidth="299"><section><span leaf=""><span textstyle="">创建&nbsp;</span></span><code data-path-to-node="4,3,2,0" data-index-in-node="9" data-pm-slice="0 0 []"><span leaf=""><span textstyle="">Link</span></span></code><span leaf=""><span textstyle="">（关联关系）。定义它是 1:N 还是 N:1，手动绑定外键。</span></span></section></td></tr><tr><td data-colwidth="83"><section><span leaf=""><span textstyle="">第四步</span></span></section></td><td data-colwidth="193"><section><span leaf="">/</span></section></td><td data-colwidth="299"><b data-path-to-node="4,4,2,0" data-index-in-node="0" data-pm-slice="0 0 []"><span leaf=""><span textstyle="">点击 Save &amp; Save Changes，等待系统缓慢地把这些元数据索引化。</span></span></b></td></tr></tbody></table>

Ontology的问题在其官方文档和视频中体现的尤为明显，用了它比不用它要麻烦的多不说，做出来的东西还更烂。

PLTR用户分享也彰显着Ontology营销在业余人士心智中造成的泡沫效应，下图的内容是一个Public Service部门用户，侃侃而谈PLTR FDE为他们构建的大学生毕设级别Dashboard有多么神奇。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/at32qdQsdwGyH2fdGsXLpice4InBg20BQLDuAKl1jQZXxVoRmKvwEPmlvU7rBetgRUtbDjdHnOdvIyI99SaianCCttYuAh7WOZ3vWdiaiaahibdg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

另外，对Ontology的中文解读中也常常听到SAP Clean Core，这又是另一个及其愚蠢的故事，一个为早该进入垃圾桶的技术打的绝望补丁，就不再浪费读者的生命在此详述了。

```
//A palantir style definition
```

信息壁垒与FOMO

数据、软件，是令人畏惧的概念。人们总默认这些知识需要系统性的训练才能入门，但是时代变了，从开源软件接管世界开始，理解技术原理的成本已经大幅下降，在LLM时代更是趋近于零。

此时，信息壁垒是由傲慢构筑的。“技术应该是CS毕业的loser关心的东西，决策者只需了解概念并专注管理”，社会意识中还残存着这种经典分工思想。

但是世界又一次进入由技术进步主导的增长期，谁都不想被落下，此时的人们不经思索的接受、传播概念，谎言和谬论就有了土壤。