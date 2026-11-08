# AI 如何改写企业安全预算？自动攻防、Agent 权限与代码安全

[原文链接](https://mp.weixin.qq.com/s/6Gm-gu5itI4EDB2h-Tkv8w)

![图片](https://mmbiz.qpic.cn/mmbiz_png/QUs3kaltEh1FbuGqORnX1m9cw65O0iayhlMIQaOicCbsMO73ABFH942IGnmr9jwfyIvoKyDuGgs5D0H0t787TMA75omuPYvEP20BtUicDdmJlc/640?wx_fmt=png&from=appmsg#imgIndex=0)

今年夏天，OpenAI agent 入侵 Hugging Face 的生产系统事件让 AI 带来的安全挑战变得非常具体：模型不仅能找到漏洞，还能获取权限、执行攻击，完成一连串原本需要专业攻击者操作的步骤。

而最近，OpenAI 的“Patch the Planet”计划又协助研究人员发现了 PHP 中的严重漏洞，这次发现把检查系统、紧急修补的压力带到了更多企业面前。AI 正在帮助防守方更快地发现问题，但找到漏洞之后，企业能不能及时判断风险、完成修复，同样决定了系统是否安全。

与此同时，企业自己也在使用越来越多的 agent。它们能读取内部文档、访问源代码，甚至用员工的权限调用业务系统。安全团队一边要借助 AI 处理更多告警、测试更多系统，一边也要弄清这些 agent 能访问什么、做了什么，以及哪些操作必须经过人的审批。

这些变化会如何影响 AI 安全领域？ a16z 最新的这篇面向 100 位首席信息安全官（CISO）的调研是一个很好的材料帮助我们理解这个领域的变化。CISO 们结合 AI 在企业真实生产环境中的变化，讨论了 2027 年在企业安全上的工作重心、预算和采购计划。

相比对技术能力的预测，这些来自一线采购者的回答，让我们更容易看清企业眼下遇到了什么问题，以及它们愿意为什么样的产品付费。

以下是我们对这篇报告的编译。我们想借这份调研梳理两个问题：AI 正在给企业安全带来哪些具体变化？当这些新需求进入采购流程，现有安全平台和创业公司，各自的机会又在哪里？

## 01. Why Now

### AI 正在改变企业安全的重心

AI 比量子计算更早改变了网络安全行业。

今年夏天的 OpenAI 的 Agent 入侵 Hugging Face 是一个开端，在这之后，AI 又陆续帮助发现了互联网基础软件中的漏洞。而就在上周，OpenAI “Patch the Planet”计划的研究人员找到到 PHP 中的严重漏洞，且这些漏洞已经存在了十多年。同一天，人们还发现，所有主流浏览器都信任的证书颁发机构 eMudhra，使用了极弱的加密密钥，其中一个竟然只是数字 4。

Patch the Planet 是 OpenAI 与安全研究机构、开源维护者合作开展的计划，将 AI 辅助漏洞研究与人工验证、补丁开发结合起来。这次 PHP 漏洞在特定条件下，可让未登录的攻击者在服务器上执行代码，风险会沿共同的软件依赖影响许多企业。本次 PHP 事件表明，AI 辅助研究能在被广泛依赖的成熟软件中，验证出长期缺陷的严重后果。

![图片](https://mmbiz.qpic.cn/mmbiz_png/QUs3kaltEh2PmIbm6AwmYRmpkbvjoGic8ViaV4P7J6xBCHAqdZBX7h4mEnwPEibeIGjqWgpVGcfU1s7xAPgJM6Jian4DD7ibHbU9TMksTeA2XC4I/640?wx_fmt=png&from=appmsg#imgIndex=1)

这类安全问题其实一直存在，只是模型发现和利用漏洞的能力在不断提高。AI Security Institute 的评测也反映了这种进步：新模型能够完成越来越复杂的网络安全任务。

AI Security Institute（AISI，人工智能安全研究所）是英国政府设立的前沿 AI 研究与评测机构。

这项测试把模拟网络攻击拆成 32 个步骤。在同档测试预算下：GPT-5.4 平均完成约 13 步，新版本的 Mythos Preview 平均完成约 25 步，而后者最好的一次尝试则是完成了全部 32 步。这个测试说明，新模型已经能把更多攻击环节连起来，推进更长的攻击流程。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh2wWVeyh7GJnvpKTnNsX65wypxsH4iaOjvJCyn3PsZ7OouoialyN8AfPkdL2DtgUKWfkRmN1SPibD0jaOV6fialiaowibdCpx70zfXwE/640?wx_fmt=png&from=appmsg#imgIndex=2)

AISI 测试。以上结果来自模拟网络，不能等同于攻破有防御措施的真实企业网络。

随着漏洞越来越多，企业的安全团队必须快速地作出判断：哪些最可能危及自己的业务，并赶在攻击者利用之前修补好。

Epoch AI 在今年 7 月发布的一组数据显示，企业需要评估和处理的安全漏洞正在增多：下图中，橙线代表高危漏洞，截止 2026 年 7 月已接近 1,200 个；绿线代表严重漏洞，接近 400 个。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh1Wyt7rDy2Chibc6J0S7Pp3y7vicFz7cVsZdQCuC0AEjoBkaXA0SE7s3Lqj7mHe93EPxXL2ibGMF2gFWOsG2eTMZKia3ibG0ZCHDaac/640?wx_fmt=png&from=appmsg#imgIndex=3)

与此同时，企业安全团队的关注范围也在扩大。

随着越来越多员工开始发布用 Vibe Coding 做出的应用，越来越多的 Agent 开始访问公司文档、源代码和生产系统。每增加一个应用、接入一项新服务，安全团队就得弄清它如何运作，以及该怎么保护。

而这些变化也有助于解释 Palo Alto Networks 和 CrowdStrike 等网络安全平台今年的市值上涨，截至 10 月 28 日，这两家公司市值较年初分别增长约 152% 和 132%。

![图片](https://mmbiz.qpic.cn/mmbiz_png/QUs3kaltEh20FG8jSgxU4EHBpib8B6JIQhibnrej29Pj32r4H5IWWiaFZB2BYYQo3j0MaToMZ8LJh2LYWl3bXJwaeicFRxVianIshoMGZeveck14/640?wx_fmt=png&from=appmsg#imgIndex=4)

但企业面临的安全风险越来越多，那么一个相当现实的问题是，企业的网络安全预算会如何变化？

为了了解安全负责人如何应对这些压力，a16z 调查了 100 位 CISO，询问他们 2027 年的工作重点、预算和采购计划。这些受访者所在企业的员工人数均超过 1,000 人。

其中，87% 的受访者预计网络安全支出将增加。原因主要有两个：

- AI 带来了新的安全威胁；

- 企业部署 AI 的程度越深，需要保护的应用和系统也越多。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh1ibnrIHChP0FS29K4lAuxpEEHnn74Qa6eVu5qqTBXjrC7ibKiaJpZwaIPJzrcl9YNVWLxVuylO9wgIvKn8KbaicdEDxvicUyDAMyHg/640?wx_fmt=png&from=appmsg#imgIndex=5)

一方面， 这些新增支出大多会用于采购相关 AI 工具。但和“AI 取代白领”的大趋势不同，这些受访企业目前还没有因此考虑缩减安全团队的规模。甚至接近 ～50% 的受访者仍预计 2027 年安全团队人数会增加，另有一半预计保持不变，只有 4% 预计裁员。

为什么 AI 接管越来越多 coding 类任务的同时，反而为什么还需要这么多人？因为团队希望完成更多工作：团队仍然需要人手，是因为还有更多工作要做：处理原本只能排队等待的告警，测试更多应用，更早修好漏洞。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh00vCn1XedzMH2iabtCL24azLPJFCpGNydClXExrE4YPRicNCKjkBwD2ow8EyibYBuQBcdjBD0j13icyUNkw6MSHGJRt0m4p7tX9Rg/640?wx_fmt=png&from=appmsg#imgIndex=6)

CISO 们已经在开展试点、预留预算，并判断哪些产品足够可靠，可以投入生产环境。很多采购决定会在未来 12 个月内作出，而他们最关心的问题，已经与一年前大不相同。

安全行业的需求在快速发生变化，在 2026 年的 a16z CISO 调研中，优先级最高的分别是暴露面与漏洞管理，以及安全信息与事件管理（SIEM）。而到了 2027 年， CISO 的工作和预算优先级都和 AI 相关。

![图片](https://mmbiz.qpic.cn/mmbiz_png/QUs3kaltEh0QGVYibOA20sC6eIlf4BQV6g5VBA7eeO5b9p6kHppZgmfGuz0GucYc5xK9QhQk73tzSxlFR1CGdXzCiclczgXtyJiaNpsGukpYFU/640?wx_fmt=png&from=appmsg#imgIndex=7)

在 Top 5 priorities 的选择上，AI SOC 与代码安全进入的比例接近，分别为 49% 和 48%，如果要选择最重要的那个，22% 的受访 CISO 则认为是 AI SOC。

SOC （Security Operations Center）安全运营中心，是企业里负责日常监控网络安全、发现攻击并处理安全事件的团队。

虽然不同类型企业的 top priority 并不相同。比如排名最靠前的是 SOC 自动化，也有团队把进攻性安全（Offensive Security）、漏洞修复，或保护自身部署的 AI 更加重要。不过，普遍认同共识是，AI 已经是安全系统不可缺少的一部分。

从具体方向变化趋势来看，对比 2026 年，企业内部 AI Agent 安全（增加了 28 个百分点）、SOC 自动化（增加 26 个百分点）和进攻性安全（增加 24 个百分点）的优先级上升最多，代码安全、漏洞修复和 AI 治理紧随其后。

传统暴露面与漏洞管理下降了 21 个百分点，而同时 AI 漏洞修复上升了 22 个百分点。需求正在向新能力倾斜，不过这里的趋势更多代表企业在 cyber security 上优先级的变化，还不能直接解释为对应品类预算的增减。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh08lOBHaJS7hHwAKDUmSSicCUkFgOTmDjbc4BbI2pB3KSBkwhSPZAAldDmQwE4MB5qELovM6ssFoTBejBsKV7gyjIcrSOpU1u0Q/640?wx_fmt=png&from=appmsg#imgIndex=8)

### 企业开始采购 AI 安全工具

虽然企业对这些工具很感兴趣，但大多还没有真正在生产环境中用起来。只有 18% 的受访者已在生产环境使用 AI SOC 工具，使用 AI 进攻性安全工具，以及 AI 暴露面与漏洞修复工具的比例，均为 13%。

- 目前在实际生产环境中被使用最多的是代码安全工具，有 26% 的受访企业表示已经在使用，36% 的受访企业正在试点；

- 检测工程与威胁狩猎虽然目前只有 9% 投入生产，却有 30% 正在试点，42% 预计未来一年采用。

不过不少企业还处于试点状态，或预计未来一年内投入生产。代码安全和邮件防护的使用更普遍一些，但距离普及仍然很远。

![图片](https://mmbiz.qpic.cn/mmbiz_png/QUs3kaltEh2gQE2JvvuCiboxhqzcm1lC2VuSczguzBBdM8Db7sDdkwCH0JSQDwt1Clbh5dgnSTozcADr0NszKNvIiavEG1VcCUK7mibAhNiahaM/640?wx_fmt=png&from=appmsg#imgIndex=9)

45% 的受访者计划在未来 12 个月内，采购或升级内部 AI Agent 安全产品：

- 计划采购或升级进攻性安全产品的比例为 42%；

- AI 使用管理与治理产品为 38%；

- AI SOC 在前面的优先级调查中最常排第一，但未来一年计划采购或升级的比例为 31%，低于内部 AI agent 安全的 45%。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh3xkjEm0TRrfhaNZp5DuYvZdiaxXmNiaHjeic8Bj8yloIgia8OugUYEsJb2kz4cCktKWE35gxFCWpzKLCiaJwdc8vg2NHLl65mbUqXE/640?wx_fmt=png&from=appmsg#imgIndex=10)

企业正在决定买什么，产品本身却还在不断变化。有的企业准备扩大现有部署，有的则第一次采购这类工具，还在比较供应商。所以 2027 年有可能是能够从企业支出和预算侧真正看到变化的一年，各个品类都将迎来新一轮评估与采购。

接下来，结合 CISO 们的回答，可以看看市场正在发生什么变化，以及哪些地方可能出现机会。

## 02. What's New

### 更高频的安全测试

速度在企业安全里非常重要。

首先，从实际工作流来看，安全团队处理一个漏洞的事件天然很长。因为企业的系统一直在变。团队可能花上几周处理渗透测试发现的问题，但这期间，开发者还在发布功能，员工还在接入新服务，权限设置也在变化。等这一批问题修好，可能又有新的漏洞需要检查。

此外，AI 让攻击者能够更快地发起更多攻击，相对应，防守方也需要同样的能力去应对。贝恩估计，AI 能把一套典型攻击流程从大约四周压缩到约 18 小时，留给企业发现问题并完成修复的时间少了很多。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh00KhqrwcG48GpC1K3uoGOrsE0IOYgQJqQpT3zyTsrIumAOIcVrjjf0m6h5wic9BQxLFbh6IvBjP2qHIByct6Y8LI1nnBEZf2DY/640?wx_fmt=png&from=appmsg#imgIndex=11)

面对这个变化，安全负责人首先是希望提高测试频率。比如，83% 的受访 CISO 就认为，更频繁地测试安全状况很重要，“面对所有这些新的 AI 威胁，我们需要比别人更早发现问题。”.

a16z 参与投资的 [Armadin](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247521704&idx=1&sn=a7ab2c8ec845908e39105bc925f578fa&scene=21#wechat_redirect) 就是通过使用自主 Agent，寻找攻击者可能利用的入侵路径，并帮助安全团队将其堵住。

![图片](https://mmbiz.qpic.cn/mmbiz_png/QUs3kaltEh0QXYE3X0ov1DRRwNqWO7UOUA7aFqEqKJSV5zCQynuAIhLulQZK3XubsDRcnsd1jEw0VOc9G11FfvBZSCticxezVM42CdLjZ908/640?wx_fmt=png&from=appmsg#imgIndex=12)

与此同时，负责模拟攻击的安全人员仍然不可替代，但因为人手有限，能测的应用和系统也有限。一个安全团队告诉 a16z，他们在原有测试预算不变的情况下，还再通过 AI 测试更多应用和基础设施。

从测试会越来越频繁。有 18% 的受访者表示，他们的大多数进攻性安全测试已经在持续检查生产环境中的系统和应用；52% 预计一年内会做到这一点。展望五年后，44% 预计测试会接入 CI/CD，在代码或基础设施发生变化时自动启动。

**图表解读｜持续测试与接入开发流程，是两步不同的变化**

结合前一张测试频率图，多数受访者希望提高测试频率。预期中的改变分阶段发生：一年后，以持续测试为主的比例为 52%，接入 CI/CD 的为 9%；五年后两者分别为 39% 和 44%。近期重点是持续覆盖生产环境，更长期才是随代码和基础设施变更触发测试。以上均为受访者预期。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh0Hd5t7bnq8sZyortKzq7TicJ1S7fjb1DewdeGmOAfXfzcXwCrGQtK4vzRqmWicsqWXhWKId1ePxVe6y6wQBCxlHOvErBgplCpDo/640?wx_fmt=png&from=appmsg#imgIndex=13)

这样一来，安全测试就能跟上软件开发和维护的节奏。每次发布新版本，都可以启动测试；补丁部署后，也能立刻验证修复效果。团队不必等到下一次定期评估，才知道这段时间又出现了哪些问题。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh2BweCtzU0YAD1jLN7PrYCJZwRCjEIzdgG077rejW6z3Igg29Itgf5bj6XIOxzCzXDPcUATTdQ1XQoHMQ5lUsOvwaictibFSWC7A/640?wx_fmt=png&from=appmsg#imgIndex=14)

**图表解读｜进攻性安全的采购倾向更偏向 AI 原生厂商**

在进攻性安全中，42% 计划向 AI 原生厂商采购，24% 选择现有平台的附加功能；其他九类 AI 安全产品的对应中位数分别为 24% 和 45%。这一品类的采购倾向与其他品类不同，但采购计划尚不等于成交。

### 漏洞发现提速，但修复仍是难点

但 AI 加速了漏洞发现之后，随即而来的就是漏洞修复。但漏洞修复往往要更慢：先找到负责的人，确定怎么改，再完成测试和部署。如果团队本来就有大量问题没处理完，即便 AI 可以更快发现漏洞也并不能从本质上提高企业安全水平。

因此，在漏洞发现后，可以先借助 AI Agent 测试确认攻击者能否利用漏洞，以及能够访问哪些系统或数据，甚至生成工单。

随后企业安全团队就可以基于 AI 测试的结果来评估漏洞的实际风险，确定修复优先级，并判断在哪个环节修复可以阻断攻击。

当然 AI 也可以参与协助漏洞修复，并在修复后再次测试，确认原先的攻击路径已被阻断。

![图片](https://mmbiz.qpic.cn/mmbiz_png/QUs3kaltEh3XqvicMJlFBMYpoic2IafdXPdKPDmY8U4Opatfzfo2uicUOn3aQFibbUKmqLBic5qiag7DnlvmcWyUdDMibtMUU8p4qCLRyxdEWAxvHc/640?wx_fmt=png&from=appmsg#imgIndex=15)

### SOC 需要扩容

攻击速度加快，也要求 SOC 更快完成告警调查和响应。但分析师处理一条告警，往往要先从多个系统收集证据，还原事件经过，再确认是否存在真实威胁。等这些工作做完，可能几个小时已经过去，后续处置还没开始。

因此，SOC 可以先让 AI Agent 收集证据、完成常规检查，再由分析师调查复杂事件，作出需要专业判断的决定。这样，在人手有限的情况下，团队也能处理更多原本顾不上调查的告警。

当然，让 Agent 完成调查，并不意味着后续处置都可以由它自行决定。企业还需要根据操作风险，确定哪些权限可以交给 Agent。

现阶段， 36% 的受访者愿意让 Agent 自主执行低风险操作。如果看未来 12 个月，60% 的 CISO 预计会接受让 Agent 自主完成低风险的 SOC 任务。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh0mqpMiaMeULgaELqSHQ25naBpxGvmXib1JicLRpCMibPII8pJSnWtKwCzsq71dF5qLZj1OejNDmK2na9fuZXY6krLXnicXfHsniaJiaY/640?wx_fmt=png&from=appmsg#imgIndex=16)

比如，收集日志和修改生产系统的风险并不相同。团队可以把大部分调查工作交给 Agent，但对可能影响业务运行的处置操作，仍保留人工审批。

Cotool 就提供了这样的工具。安全团队可以先将已有的调查流程配置成 Agent，设定操作权限和审批要求，再让它调用现有工具，筛选告警，并在授权范围内采取行动。分析师可以检查结果，继续调整流程。原本需要人逐步完成的重复调查，就可以交给 Agent 反复执行。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QUs3kaltEh3ibibBHD9nw9bFj2b7AO7jnSWvrpusiclCxqEE8q14yJsjyA4qdT50jqK8eGomVgBnNWLVopcUUibOU0iaElPwHYONnzNwJ8ia90fvI/640?wx_fmt=jpeg&from=appmsg#imgIndex=17)

Cotool 官方产品示意：Agent 先检查应用权限、核查发布者并追踪数据访问，再请安全团队批准撤销授权

### 代码量增加，安全检测压力上升

即使企业自身的安全做得很好，所依赖的软件一旦有漏洞，也可能让企业受到牵连。最近的 PHP 漏洞就说明了这一点。

代码安全并不是新领域。静态应用安全测试（SAST）和软件成分分析（SCA）工具已经有是企业安全软件的标配。但当 AI 让开发者能够编写、发布更多代码，也增加了现有安全工具的检测压力，传统代码安全审查是否也会受到挑战？

因此，接近一半的受访 CISO 把 AI 代码安全列为 2027 年最优先的五项工作之一，而 2026 年这一比例约为 25%。企业可能会升级到 Socket 这类能主动扫描依赖项代码的工具，也可能采用精简容器镜像，持续从源代码重新构建，并及时加入最新补丁；有的企业会两种方式一起用。

“写代码的工程师，远比做安全测试的人多。”

——某金融服务企业 CISO

### Agent 值得信赖吗？

AI 已经进入企业日常业务，安全团队也需要应对这些工具和 Agent 自身带来的风险：

- 92% 的受访者表示，面向员工的生成式 AI 工具至少已在部分生产场景中投入使用；

- 83% 的受访公司已经在生产环境使用 coding copilot/agent；

- 55% 的受访公司已通过 MCP 服务器或其他方式，让 Agent 连接业务应用并投入使用。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh2hT2wCjmTZmfDWSFp2VuydBPjTCXwoxv9yLDFH7yYfpiaoN6lKYLpK9hSaz2HAd0ydGK8iapmqLePZ9pWNhwAgQxUs1nbHkYcJQ/640?wx_fmt=png&from=appmsg#imgIndex=18)

安全团队既要关注员工向 AI 工具输入的数据，也要了解 Agent 能调用哪些工具、执行哪些操作。因为这些 AI 系统不仅能读取源代码、检索公司文档，还能在多个应用中执行操作。一家餐饮软件公司的安全负责人问出了许多团队的困惑：“你怎么才能真正知道，Agent 到底在做什么？”

- 47% 的受访 CISO 把员工向 AI 工具泄露敏感数据列为最担心的问题之一；

- 46% 的人担心 Agent 越权或遭到入侵；

- 另有 29% 担心 AI 应用遭遇提示词注入攻击，或出现数据泄露。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh2qtUbia8LroVfHeib4BjJib05Br4chKg2XyGib39rMxW6YwFnG87ucP4gjPkd4XbX3MYvKv3wSJ48mrmqlGsm2ib6G1CPvLQqKEyfo/640?wx_fmt=png&from=appmsg#imgIndex=19)

这些担忧已经拖慢了不少企业使用 AI 的进度。63% 的回答提到，安全要求已经推迟或限制了部分 AI 应用的使用，比如需要先做安全审查、获得审批，或者不能用于某些用途。

要管理这些风险，企业安全团队就需要充分了解：有哪些工具和 Agent 在运行，由谁负责，拥有哪些访问权限，以及实际执行了哪些操作。并且这些信息需要持续更新：原本获批的普通软件，更新后可能增加 Agent 功能；员工会添加新的扩展和集成；Agent 承担的工作越多，获得的权限也可能越大。

另一个难点，是区分操作究竟由人还是 Agent 发起。

当 Agent 在员工设备上运行、使用员工本人的权限时，它读取文件或调用 API 的行为，可能与员工亲自操作难以区分。这让现有的终端检测与响应（EDR）、数据防泄漏（DLP）和零信任机制，在识别和约束 Agent 行为时面临困难。

a16z 投资的 Neo，就在尝试解决这一问题。Neo 的创始人曾参与创立 SentinelOne。Neo 会识别员工设备上的 Agent、扩展和 MCP 服务器，跟踪各自的访问权限，区分操作由人还是 Agent 发起，并实时执行安全策略。例如，Agent 可以获准调查生产系统的问题，但修改系统仍需审批。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/QUs3kaltEh2PWItpKPEc0tWHR4H4I3VW6SzZjKdkJL3vptsnyM7AYJXyGI6HUKWAsQ8q7gDbx0DU3EzGrpQzAB1iaT2TEWFDaWDlfhDKlvC8/640?wx_fmt=png&from=appmsg#imgIndex=20)

Neo 界面示例：为 Claude Code、Codex 设置文件访问规则。图中针对读取 。ssh 目录的行为，设置了升级处理（Escalate）、生成高危问题记录和通知用户

### AI 让社会工程攻击更难识别

攻击者用 Deepfake 模仿团队成员的声音或面孔，让员工相信自己正在和其通话，进而转账或交出账号权限，这种利用人的信任、诱导其执行危险操作的方式，就是社会工程攻击。

这类攻击不一定需要 Deepfake，冒充同事的钓鱼邮件、仿冒登录页面，也是在利用人的信任。在安全调研机构 SANS 调查中，80% 的受访组织把社会工程攻击列为最主要的人员相关风险。AI 让攻击者更容易伪造可信的消息、声音和视频。过去，员工还能通过拼写错误、可疑措辞识别一些骗局；现在，即使声音听起来像本人，视频里出现了熟悉的面孔，也不能据此认定请求可信。

这意味着安全培训和模拟演练也需要更新。Adaptive 用 AI 模拟钓鱼邮件、冒充他人的语音和深度伪造视频，让员工练习识别这些骗局，以及遇到可疑请求时如何核实对方身份。

除了仿冒身份，借助 AI，攻击者可以批量生成假冒高管的账号、仿冒域名和欺诈网站。对于这类问题，比如 Doppel 这样的公司就则帮助企业发现这些仿冒账号和网站，并推动下架，减少安全团队逐一查找、处理的工作。

## 03. 机会属于谁？

为了争夺接下来企业在 AI 安全领域的新预算，市场上已经出现了大量 AI 安全供应商。

从 Black Hat 2026 供应商图谱中可以看到，AI SOC／SecOps 有 43 家，agent 安全／治理有 35 家，应用与代码安全有 34 家。这些厂商对产品能力的介绍却很相似：让系统自己完成更多工作、更快查清问题、减少人工操作。

![图片](https://mmbiz.qpic.cn/mmbiz_png/QUs3kaltEh25yyxBug6PmbhdkMwvDXsQbY95Okldu2Flea4ckrUZ58bicHd9LgaZDEqFMicYjf5vVTiatM4gpAMRwTPddqiaHyiaP3xs9HKCKrP4/640?wx_fmt=png&from=appmsg#imgIndex=21)

企业要决定买什么，首先需要实际评估：产品能替团队完成多少工作，哪些环节仍要人来跟进，哪些操作可以交给它，以及使用成本是多少。这些评估本身也需要安全团队投入时间和人手。

一家全球服装企业的 CISO 说，他们先从七八家供应商中选出三家，再实际测试。用他的话说：“要给七八家全部做概念验证，人手根本不够。”

新厂商不断出现的同时，已有产品的功能也在随着底层模型能力的提升而变化，企业比较的对象一直在变，采购决定也就更难作出。

另一位安全负责人解释了自己的犹豫：“我不想每天为了一个新问题，就又临时买一个单点产品。”他的方案是先和其中一款工具签订短期合同，同时也在评估其他产品。

### AI 安全采购：企业仍优先考虑现有平台

从 a16z 的调研来看，在选择供应商时，企业通常还是先看已有的安全平台能否满足需求：

- 44% 的受访者会优先考虑现有安全平台提供的功能，只有 21% 会先找 AI 原生厂商；

- 25% 表示不会向创业公司采购。

企业优先选择已有平台的原因相当直接：是现有供应商已经在保护企业终端、处理安全数据，已经通过了采购审核，企业自然更容易先想到它们。

如果现有平台解决不了新的问题，企业也会考虑创业公司。调查中，47% 的受访者把“解决现有供应商无法满足的需求”列为选择创业公司的重要条件。性能、创新速度、价格，以及能否接入现有系统，也会影响采购决定。

虽然当下看，创业团队可切入的空间很窄、赢得客户的门槛极高，但 AI 带来的安全变量未知，AI 安全很快会成为业务运行中不可缺少的一部分，这一批技术变革下一定催生一批重要的安全公司。

![图片](https://mmbiz.qpic.cn/mmbiz_png/QUs3kaltEh3UwmZYYJK9ibbefVrR6hiaRVXJzXkX3rbVZVPT8iatEnywER7ZWbAtsAQN7aaM4d9ViaAp6VBJVaqZUyvGY0IjGoSLWWUfqsibOCSY/640?wx_fmt=png&from=appmsg#imgIndex=22)
