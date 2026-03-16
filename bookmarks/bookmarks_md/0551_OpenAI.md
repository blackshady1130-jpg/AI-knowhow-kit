---
url: https://mp.weixin.qq.com/s/ryxsDIstzSdpRAbcScvyZQ
title: "OpenAI到底亏了多少钱？"
description: "没亏那么多，所以对微软的收入贡献也没那么多"
author: "波太金"
captured_at: "2026-03-08T12:21:11.898Z"
---

# OpenAI到底亏了多少钱？

**关注共识粉碎机，获取历史讨论会纪要**

文：波太金

**The Information近日爆出了一则OpenAI的亏损新闻，其中新增的的关键数据包括：**

-   OpenAI 目前单月收入约为283mnUSD，全年营收可能在35-45亿美金。

-   **OpenAI 24年推理成本将达到40亿美金，训练成本将达到30亿美金。**

-   推理成本的依据是目前了解到OpenAI向微软租赁了350K A100芯片，并以1.3美金/小时的单价租赁。

-   除去70亿美金的计算成本，OpenAI还有15亿美金的员工成本。

-   所以推导出OpenAI今年的亏损将在45亿-40亿-30亿-15亿美金=-40亿美金。

-   同时还更新了Anthropic的数据，年底ARR估计在8亿美金，亏损在27亿美金。

我们将The Information历次谈到的数据做了次汇总，用蓝色标注为The Information给出的数据，单位为Million USD：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dljQibos6CibYcE8EIl6wIm68bQoxeTWInTEqL0sJhgFTJ4GeNiaxbhXI5H04UUQN67YWicPM7O5zNJO8mk2t6f64w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

在这份数据中对于大部分数据我们都不怀疑，也与我们在微软Preview中提到的数据基本一致。**仅有一份数据令人疑惑，是Inference Cost的40亿美金（Wow，这也给微软太多钱了）。**作为补充，The Information还提到“下半年与苹果的合作可能会带来ChatGPT的进一步亏损”。

我们继续用The Information的数据来矫正，在其之前的的文章中还有一段：**“By contrast,Microsoft's gross profit margin on the Azure OpenAI Service is around 40%。”**

并且其编辑在后续还特地提到**“毛利率数字包含了佣金支出,是在佣金支付之后的数据”**。那Azure OpenAI Service在扣除佣金前，其毛利率大概是60%。

考虑到Azure使用自己的数据中心，不需要为GPU支付超额租金，OpenAI API的毛利率根据此推断大概在30-35%，与Azure OpenAI Service差得近一半的毛利要付给Azure作为Azure GPU IaaS业务的毛利。

在4Q24，如果OpenAI的全年收入达到45亿美金，那4Q24的营收将约为18亿美金。假设其中当时的毛利率还在40%左右，那大概对应的推理成本就是10亿美金，如果是这样的推理逻辑**那Inference Costs所对应的40亿美金就是年底Runrate收入的概念（4季度成本\*4），而不是24年全年成本40亿美金。**也与我们在微软Preview中的假设一致。

**在微软财报公布后，现在结论变得更加清晰。Azure AI占比在2季度贡献8%，而不是贡献9%。很清楚OpenAI的推理成本还没有到40亿美金的runrate贡献，要到年底才会达到。**

在OpenAI的亏损中，值得特别指出的是，**里面有****将近10亿美金推测与股权激励有关**，而非现金成本。这也意味着现金角度的实际亏损（NonGAAP）要更加少。

但根据我们从各方信息的推测，**OpenAI下一轮巨量融资很快就要****开始了。这可能是下一轮融资军备竞赛的导火索，Ilya的新公司也将进入战局。**

最后附上我对OpenAI的模型估算，仅供参考：![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**【讨论会】**

过往的讨论会纪要请参考：

[《EP01：AI如何颠覆数据库讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485464&idx=1&sn=13d6039e278e1e254ec2cbfc36c77b4b&chksm=ea5ad1e0dd2d58f6d4b777e90c79c633de9356763f6ca956b541f58ec036e0547d0b02425721&scene=21#wechat_redirect)

[《EP02：AI如何颠覆游戏讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485766&idx=1&sn=92e349bdb9db3301f555bcfd0b7dd9ce&chksm=ea5ad0bedd2d59a8b6ba0b70c4ecfb87bbb671e15f0f68224af90d651ed121acebfb9d4eb8db&scene=21#wechat_redirect)

[《EP03：生成式广告讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485798&idx=1&sn=60a6392ed12497b157a1d965b1497bfa&chksm=ea5ad09edd2d598896f142b74c41e3da4513c09ca772dd1aebde5c6fc5c7d230b7a11597a45f&scene=21#wechat_redirect)

[《EP04：AI如何颠覆办公与CRM讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485819&idx=1&sn=28c92da1fc59b44d4309a71cc94f95a2&chksm=ea5ad083dd2d59957bb4e7c90525365b3e2520ba7212dc221438f25e7679a3103263d90c590e&scene=21#wechat_redirect)

[《EP05：AI时代产品经理的新要求讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485888&idx=1&sn=8bd28ecca119496dee7e56f06e795ab2&chksm=ea5ad038dd2d592e4430d349ab86297301eecef4b7ae22212005752376888b8efc041920c681&scene=21#wechat_redirect)

[《EP06：AI如何颠覆网络安全讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485918&idx=1&sn=980b533e160c8ffe1a8a76f6f517850a&chksm=ea5ad026dd2d59304390d111ad0c475a9cd4296255c31ba1e0762dd88b827bb39b4c5dab5e63&scene=21#wechat_redirect)

[《EP07：AI如何颠覆设计流程讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485979&idx=1&sn=08b3226888aed3a2b6ca8d82de827734&chksm=ea5ad3e3dd2d5af5952b60b9465c86f260199b6f028e320fea82b7183a3d1805f2d92a80c538&scene=21#wechat_redirect)

[《EP08：AI如何颠覆可观测性工具讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247485995&idx=1&sn=758d9de3a0e277d3193e81d37617d1f4&chksm=ea5ad3d3dd2d5ac5060d6c6cfdb4c1078089446c34653d6394c1aa83d4b605b63be7d6f4a3dd&scene=21#wechat_redirect)

[《EP09：如何突破英伟达垄断》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486017&idx=1&sn=52397108a65999fd7656261302092943&chksm=ea5ad3b9dd2d5aaf858469d1346e4134db9904d626f45a3d5634c7382c510f72de93df47a3d4&scene=21#wechat_redirect)

[《EP10：AI如何改造传统工业讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486033&idx=1&sn=cefc1d887d689d1fdd7903a7622b46ff&chksm=ea5ad3a9dd2d5abfbe6d3d8fb4e8d55a16c349864783c7bce5cae1e7bce3cf0cade3b2b9d61c&scene=21#wechat_redirect)

[《EP11：AI如何改造推荐系统讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486055&idx=1&sn=32f3d75f4fbfda57b8734bbb390e4145&chksm=ea5ad39fdd2d5a89788c97e562a6267ad49c36631fbcdff3c52f236a40ed28502edd1c893a89&scene=21#wechat_redirect)

[《EP12：AI如何重塑教育讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486067&idx=1&sn=3bacd58e2fde79692d3cbb29d96a87da&chksm=ea5ad38bdd2d5a9de9606b9ecf785807f5ee0adc410794dfdf2343a805ee5e26a9c87edebe80&scene=21#wechat_redirect)

[《EP13：OpenAI DevDay带来大变化》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486101&idx=1&sn=6387df44181bfdc676baddbb2c9523aa&chksm=ea5ad36ddd2d5a7badd92900b2f55456e13e1158cb8f98e485d63248387f0f5a9e835a241031&scene=21#wechat_redirect)

[《EP14：到了颠覆AI客服的时候了吗？》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486262&idx=1&sn=39c45a626f49cb7027dc83554c6f91c1&chksm=ea5ad2cedd2d5bd86aa14b2c91e27b22910e572b94905ee5a8d24d02f8a8c852ee4404ed6f2e&scene=21#wechat_redirect)

[《EP15：RAG带来蓬勃应用生态》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486569&idx=1&sn=1bb4d0b44745637079846fa69ea5c3c5&chksm=ea5ad591dd2d5c8743030e2b3e40f376b69d03d473c9a6259f161d6a79c8b562706db3ba197a&scene=21#wechat_redirect)

[《EP16：GPT4o对实时互动与RTC的影响》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486806&idx=1&sn=25235f06777ee57a1f96650226ee31d8&chksm=ea5ad4aedd2d5db831639b06bbdbd0e464913f45715520412853393e28cdbb600a6c043a559b&scene=21#wechat_redirect)

[《EP17：AI Coding以及对编程软件的影响》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247487018&idx=1&sn=b2e505743156d15ad938e25dc36cb8db&chksm=ea5ad7d2dd2d5ec4d3b93aaec27243d418c479a52fabde73e1aa31aec50d4e5ba407eafb028f&scene=21#wechat_redirect)

[《EP18：呼叫中心与Voice Agent讨论纪要》](http://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247487335&idx=1&sn=9394bb141b8316fdb93f7952f582616a&chksm=ea5ad69fdd2d5f89a745e8718fcd865771f2d965374f478a3295b7f594d4a8c4a81780b49a9b&scene=21#wechat_redirect)

**欢迎加入共识粉碎机的活动讨论群，获取更多活动信息**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

---

[大模型未来三年的十个假设](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486395&idx=1&sn=8856ac8d66efeab83683c528e3151cb2&chksm=ea5ad243dd2d5b55d8b967a759beaadd02ea773e60af064b006979f5e9524316f38fde3fa95a&scene=21#wechat_redirect)

[

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Data Infra：大模型决战前夜

](https://mp.weixin.qq.com/s?__biz=MzI2MTM2MTgxNQ==&mid=2247486639&idx=1&sn=cf4a3885d4c852325c11601e53d9e194&chksm=ea5ad557dd2d5c41e7313a9742c49c247248a6870c8668d1159a04b4960f2d5e530906d7c482&scene=21#wechat_redirect)