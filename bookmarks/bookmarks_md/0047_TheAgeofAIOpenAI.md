---
url: https://mp.weixin.qq.com/s/AxX-Q7njegNTAxMkYFwsfA
title: "The Age of AI：拾象大模型及OpenAI投资思考"
description: "OpenAI有机会成为Win95级别的通用计算机平台。"
author: "拾象"
captured_at: "2026-03-08T10:15:27.417Z"
---

# The Age of AI：拾象大模型及OpenAI投资思考

![图片](https://mmbiz.qpic.cn/mmbiz_gif/3tHNibnJ2jgzWic9ViaQNX2f1uQeSDXUQwoiauLCXftvkAsFMul5ggwhBhrBJpyj2cCB0ndVUcIiakiafhtIWiamB6Msg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgzWic9ViaQNX2f1uQeSDXUQwo4wDjBSEMdGJcU9tmPoqLhMwLCZYO6RKUeicjur96YLhkEicSYdA6kb1A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgzWic9ViaQNX2f1uQeSDXUQwormOwstePiagTDzYyyXn0qnIWXQpdWyuZWUVYGCFx45c1aKIAGicxlp1A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

作者：拾象投研团队

编辑：Siqi、penny

排版：Mengxi

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgzWic9ViaQNX2f1uQeSDXUQwoeN5VQibN1HagexVicibeRu114vS8nckj0qok10JoPklSWPEdxCGukLscQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

The Age of AI has begun.

在《[拾象硅谷见闻：寻找下一个黄金 10 年](http://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247498585&idx=1&sn=1e5d463f9753e623eb339ac01e924b32&chksm=ce9b44c7f9eccdd1f9f596c7f5c190bc14ebe1a8d679eb6913373c9760904258ba9f4a97a52b&scene=21#wechat_redirect)》中，拾象首次提到了 AI 2.0 趋势，我们指出“目前似乎还没有看到任何人挑战 Google、Microsoft 等万亿美元的科技巨头，但 AI 让我们倾向于认为这件事情即将发生”。几个月后，以 OpenAI、Anthropic 为代表的团队正是我们所预言的这股力量。

我们已经正式从 Mobile 时代进入到 LLM 时代。参考 PC 到 Mobile 的变化，随着信息的组织效率和能力再度变强，LLM 的浪潮下也一定能带来更大、更新的商业模式升级。计算机真正开始理解人类的自然语言，这不仅是对人和计算机交互方式的变革，也是对传统互联网信息聚合与分发、复杂任务和社交等行为的颠覆。

上个月，我们开源了拾象 AI Infra 投资图谱，对整个机器学习工作流和价值链进行拆解。本研究则是拾象团队在过去 2 个月对大语言模型的边界，大模型公司格局、生态，以及顶级玩家 OpenAI 的 deep dive。

本研究中，我们探讨了一系列关键问题：

**• 什么是大模型？**大模型是新一代通用计算机，会成为 Windows 95 级别的计算机平台；

**• 从基础模型到 Killer Apps，价值链如何被分配？**以 OpenAI、Anthropic 为代表的基础模型能力边界还在不断的拓宽，会在一定阶段内占据价值链中最主要的环节；

**• 什么是 AI Native 应用****？**AI Native 应用不能只是语言模型的嵌套，而是对现有软件服务的重构；

**• LLM 浪潮下，科技巨头们是如何和 LLM 做结合的？**全球顶级 CEO 们对于 LLM 尚未形成共识，未来 6 个月是重要的窗口期；

**• OpenAI 为什么能够成为 LLM 最强王者？**OpenAI 的组织活力来自自上而下对 AGI 的坚定信仰、极高的人才密度，以及自下而上推动创新的实验机制。

……

以下是拾象团队的研究和解读，**如果您想领取完整版 PDF ，请填写问卷「拾象 LLM 及 OpenAI 研究报告」领取链接****，我们会把 PDF 文件发到您的邮箱中。**

**以下为本文目录，****建议结合要点进行针对性阅读。**

**👇**

01 关于大模型的几个关键判断

02 AI Native 的应用会是什么样？

03 科技大厂融合 LLM：Attention is all you need

04 OpenAI 案例研究

05 相较于应用层，未来 3-5 年 AI Infra 的确定性机会更高

06 硬件增量：训练及推理环节的价值捕获

**01.**

**关于大模型的几个关键判断**

**判断 1:**  

**OpenAI 是新一代通用计算机**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

大模型到底是什么？会产生哪些影响？我们认为这个问题可以收敛到 OpenAI  是什么以及 OpenAI 现阶段在做什么。OpenAI 不仅是在 LLM 领域从基础模型到产品化、商业化进展最快的团队，也是我们目前看到的全球最坚定信仰 AGI 的团队，这个信仰影响了他们的路线图、技术和商业策略的选择。从不同角度对 OpenAI 做定义可以帮我们来判断 OpenAI 未来的天花板，以及整个 LLM 的格局。

**• 新一代底层技术设施：**首先可以将大模型类比为 GPU 、搜索入口以及操作系统等数字基础设施，这些领域都呈现出 9:1 的市场格局，头部垄断效应极强，而 OpenAI 现阶段的优势和站位让它有机会获得 90% 左右的市场份额，开发者和生态会成为很强的壁垒；

**• 新一代公有云：**Sam Altman 对于 OpenAI 当前的规划是专注做一个通用的智能平台，为大模型之上的应用提供 AI 能力，作为大模型生态的 Infra，OpenAI 的角色就像 AWS，公有云呈现了 5:3:2 的格局，OpenAI 作为头部公司有机会享受至少 50% 的市场；

**• 新一代终端：**大模型时代最大的特征就是让人们能够用自然语言和计算机形成交互，自然语言操纵机器的形式会产生新的交互、也就有了下一代终端的机会。如果参考定义了移动时代的 iPhone 和其他智能手机的格局，那么作为头部的 OpenAI 也有机会可以拿走 70% 左右的市场份额。

总体上，我们认为 OpenAI 在海外至少可以拿走 60% 以上的份额，至于能否到 80-90% 核心就看其他几股力量在大模型领域的动作：

1\. OpenAI 后续 AGI 能力涌现速度：微软和 OpenAI 现在的各项资源比全球所有团队都好，模型迭代速度极快，其他团队还在追赶和 OpenAI 之间的窗口期；

2\. 虽然现阶段并没有太多出色的产品表现，但中长期仍旧要关注 Google、Apple、AWS 以及 Tesla 这四家大厂在大模型领域的动作以及与 OpenAI 之间的潜在竞争点，市场不会让 OpenAI 和微软一家独大；

3\. 开源大模型。拾象内部的判断是到今年底能有 GPT-4 水平的开源模型出来，并且有可能来自AWS、Nvidia、Meta 中的其中一家，从时间线上 OpenAI 同期有可能已经发布了 GPT-5。

**判断2:** **Foundation Models 将拿走价值链的大头**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

现阶段我们可以将大模型相关的上下游的玩家分为 3 类：

**• 基础模型：**核心代表就是 OpenAI、Anthropic；

**• AI Infra：**底层模型和上层应用之间的中间件，例如 Hugging Face、Weight&Biaes；

**• AI 应用：**现阶段出现的 Killer Apps 还不多，ChatGPT 是一个主要代表。

短期来看，以 OpenAI、Anthropic 为代表的基础模型能力边界还在不断的拓宽，会占据价值链中最主要的环节；而中期随着模型的能力和发展速度渐渐稳定后，Infra 层会有更稳定的工作流和机会出现，同时应用层也会出现深入某个垂直领域的新一代 Saas 和消费级的 Killer Apps。

**由于大模型的能力还在不断提升，形成类似操作系统的下游生态过程中，我们认为在这个过程中价值占比最大的会是形成生态壁垒的大模型公司。**

**判断 3 ：从 Mobile 到 LLM ：数据组织效率和能力再度加强**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Mobile 时代，手机作为新的终端最重要的是带来和 LBS 传感器和大屏幕两个变化，在此基础上，本地生活和短视频应用完成了大爆发；此外，手机的随身便捷性让可采集的数据颗粒度比 PC 时代上升到了新的量级。沿着这个逻辑，如果我们站在“大模型是新一代计算机平台”这一语境中，大模型相对于 Mobile 又到底带来了变化，基于这些变化，人和数据、计算机的交互又会如何演进？

**最大的变化是，计算机真正开始理解人类的自然语言。**在此之前，我们需要编程代码和固定程序才能和计算机做交互，而现在用自然语言和行为动作就可以做交互。

**交互方式变得更宽广后带来了第二个大的变化：计算机可采集的数据比以往更多、更细。**这些数据大部分是非结构化数据，甚至我们个人都没意识到、但可以被计算机采集，针对企业和消费者的数据一定会爆发很多，Snowflake、Databricks 等数据基础设施在我们看来还会持续收益。

可采集的数据结构、数据规模的变化对美国 SaaS 行业影响，有利的地方是 SaaS 公司的成本结构会发生变化，过去企业内配置的算法工程师团队可以被 AGI 取代、或者在 AGI 的基础上缩减规模、获得盈利，这是组织管理层面的上的影响，但对于相当一部分 SaaS 公司还应该关注的风险是自身的价值是否会被 AGI 所淹没，尤其是工具型 SaaS。

交互方式带来产品形态的变化，AI Native 对产品经理本身的能力也提出了新的要求。在过去，产品经理做的事情是把用户需求抽象出来就可以，现在要求产品经理非常懂大模型的能力和边界，因为很多产品的服务都能够通过大模型来实现，这就要求新一代产品经理的出现。

**判断 4 ：LLM 的边界是什么？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

LLM 的通用能力很强，但反过来看，有哪些事情是 LLM 现阶段做不到的？或者短期内我们会对它预期过高了？

最核心的一点是，如果我们将 OpenAI、以及其他大模型公司比作大脑的话，大脑只有身体是不够的。对于 OpenAI 来说，和微软的合作的就像是大脑和身体的结合，多模态是眼睛和耳朵，所以虽然今天 LLM 在我们看来已经很强了，但仍旧在成长过程中。

从能力边角层面，我们认为具备了拥有专有数据、网络效应、规模效应以及机器人这些涉及到物理世界环节的领域，是暂时不会被 LLM 的能力所淹没，相对而言具有壁垒的场景。

在当下的时点，我们可以把 LLM 的能力比作自动驾驶的 L2 —— 有一定的理解能力和执行能力，但仍旧需要具体的指令；在 4-5 年后，LLM 到了自己的 L4 阶段，不仅会获得主动解决问题的能力，也极有可能会超越人类最强大脑。

**判断 5: 大模型探索的下一步：给“脑子”装上“手”**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Action 是大模型探索的下一步。Action 的相关探索可以类比为“给大模型的脑子装上手”。**使用工具的能力，是人类智能的重要特点。对于大语言模型也是如此。**大语言模型有很强的理解能力，但还不足以判断自己生成内容的置信度，在部分数学计算、实时知识场景下用外部工具才能得到更准确的回答。因此在大模型出色的理解能力之上，教会他使用计算机上的各种工具，是对其能力最大的提升。

在 Action 的实现上，除了 OpenAI  的 Plugin，我们看到 Adept 和 Inflection 这两家早期团队想以自然语言为基础，为用户打造新的 LUI （语言为基础的 UI）方式。

在 Action 实现后，传统的 App 生态和 Saas 软件生态会被打破，体现为三个方面：

1）下游站点的价值有可能被削弱；

2）定义之后大模型与应用互联的 api 标准，之后应用接入都会迎合这一标准；

3）LMO ( Large Model Optimization ) 在未来可能会取代传统 SEO（Search Engine Optimization）。

**02.**

**AI Native 的应用会是什么样？**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

现阶段我们很难精确定义未来的 AI Native 应用会长什么样，这里提供一些观察视角。我们认为 AI Native 不能只是语言模型的嵌套，而是对现有软件服务的重构：

**1\. 交互的重构**

图形界面仍然承载高频、刚需、易抽象的功能，但低频、灵活度高、复杂的用户需求（以前可能通过低代码实现）能通过和 LLM 交互来解决。从用户学习如何使用复杂产品，变成产品能适应用户需求，用户输入也从有限变成无限，比如输入给 MidJourney 的 Prompt 可以无限灵活。

**2\. 数据和信息重构**

CRM 记录姓名、电话等结构化数据，以 Gong 为代表的 AI-based CRM 则是记录分析 B2B 销售和客户录音。人们常说**数据是石油，LLM 明显把炼油能力增强了，**高价值行业和企业内部曾经难记录、难处理的数据都可以被重新以前分析。**数据和信息的重构也意味着 AI 能承担更多决策权。**

**3\. 服务的重构**

服务的重构分为两种：

**• 一种是 AI 有能力直接提供服务。**设计师、旅行规划这类发散性服务能先被满足，律师咨询（Donotpay）等需要推断、推理的服务后被满足。Character.ai 和 Quora 推出的 Poe 也可以被看成提供了情感陪伴和知识问答服务；

**• 第二种是 AI 能让消费决策到交易发生的链路变短。**以前用户需要在下厨房搜索菜谱，再到生鲜平台下单，有了 ChatGPT Plugin 功能，菜谱和购买食材都可以在一个对话框里完成。

**4\. 反馈机制的重构**

传统产品的迭代更多在产品 feature 层面，而以生成模型为基座的产品，不仅能通过 context learning 的能力让用户多轮尝试，纠正输出结果，还能根据用户产生的数据和反馈迭代模型。ChatGPT 是把数据飞轮做得很好的爆款产品，GPT-4 的贡献者名单里还有专门的 data flywheel 负责人。Midjourney 的四选一，Poe、Character.ai 设置的 like 和 dislike 按钮，都是一些获取用户反馈的方法。

**03****.**

**科技大厂融合 LLM ：**

**Attention is all you need**

过去 6 个月和未来 6 个月是争夺用户和开发者注意力的竞争期。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

我们整理了目前二级上市科技公司、科技独角兽和 LLM 的结合，发现大部分都还处于**中间发展阶段****：有比较明确的大的集成的方向、产品才刚出来，**例如微软的 Office 365 Copilot 也处于 beta 测试阶段。GitHub Copilot、Notion AI、Snapchat（My.ai) 以及 Duolingo（Duolingo Max）属于进展得比较深入的几家。

二级公司整体在等未来 6-8 个月的窗口期，在今年下半年来验证目前的集成项目是否能从客户增长、订价保护等层面获得更反馈。微软和 Google 投了 AI research 的公司之外，大部分二级市场科技公司几乎没有在 LLM 进行提前投入，所以基本上大家都在统一起跑线上。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

目前的二级市场上市科技公司、科技独角兽在和 LLM 结合中找的场景，可以大体分为四类：

**1\. 作为内部提效工具，省成本：**数据审核、产品开发、客服等都是典型的运用场景，例如我们举例的 Chime、Bubble 都属于这一类型；

**2\. 自然融入现有业务场景：**大多数公司在做的尝试都属于这一类场景，也是一种线性的思考逻辑，就是我们哪些场景比较适合用，在具体的实践上，大家的普遍做法就是说不断测试场景，最后可能挑出来 10- 20 个比较好的，再到后期选择 4-5 重点去做；

**3\. 利用大模型对过去比较难的业务进行突破：**有一些公司会说将希望 LLM 成为一个突破点，来实现过去很难做起来、或者很难突破的业务。

例如 Segment， Segment 的主要业务是提供实时消费者数据，传统的 CRM 的数据和业务之间其实并不直接衔接，因为过去 CRM 采集到的数据可能也有错的、并且也过时了，但在 LLM 基础上，Segment 其实反而提供更实时、更有效的数据。

Zoom 的尝试也类似。Zoom 一直想要突破“开会软件”的限制，也因此推出了 VoIP、Zoom IQ for Sales 等新业务，目前也是通过叠加 AI 能力来做突破，并且 Zoom 的执行力层面比竞争对手更快，可能会帮助他们在订单层面获得一些突破。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**4\. 通过 LLM 获得新的战略增长点：**典型代表是微软 Azure 和 OpenAI 的结合。Salesforce 也是比较典型的实操案例。

**在拾象的 Mapping 和追踪中，全球顶级 CEO 们对于 LLM 尚未形成共识，尤其是和业务结合的时间点的判断上。**这其中微软最为激进，认为 GPT-4 已经是 AGI 的一种形态，而 Office 365 Copilot 是 Enterprise-Ready ，总体上，这些观点可以被分为 4 个派别：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**04.**

**OpenAI  案例研究**

**OpenAI 里最重要的人是谁？**

**OpenAI 的组织活力来自自上而下对 AGI 的坚定信仰、极高的人才密度，以及自下而上推动创新的实验机制。**

在接触过 OpenAI 团队后，我们能感觉到他们对 AGI 的信仰远超同行。对外界来说，ChatGPT 的爆发是一场行业地震，但对 OpenAI 来说，是他们坚持探索 AGI 路线多年后的其中一个成果，前面许多年并没有太多人关注。这件事有点像一帮人默默在沙漠里造原子弹，等到发射时众人才恍然大悟。

OpenAI 对 AGI 的信仰既来自管理层自上而下的愿景，也来自在内部切身感受到 Scaling Law 带来的模型能力变化。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

OpenAI 的几位 Co-founder 凑齐了业内最好的工程师+科学家+企业家，团队人才密度高，每个人都是六边形战士。从整体组织上看，基建部分的 scaling 团队和超算团队支持所有模型训练和应用团队。OpenAI 目前约有 400 人，此处列举在科学和工程方面最核心的几位：

**• Sam Altman：****美国最懂 PMF 的人，自带流量，给全球讲好 OpenAI AGI 故事。**

作为 CEO，Sam 将 OpenAI 的内部氛围组织得很好，有位前员工告诉拾象团队，当 2018 年 GPT-2 的论文被驳回时，Sam 在团队周会上将拒信的内容朗读给所有员工，并告诉大家在通往成功的路上总会有阻碍，但是大家一定要有信念。

**• Greg Brockman：OpenAI 内部的大管家和冲锋队长，⼯程能⼒和基础设施的打造者。**

作为 OpenAI 的早期重要联创之一，Greg 是一位数一数二的工程天才，Greg 本人有 80% 的时间在写代码，我们了解到 OpenAI 内部的模型训练的 infra 架构基本都由 Greg 一个人完成，包括了 GPT-4 的 Infra。同时，Greg 也想一个冲锋队长，能在大家都不知如何下手时候带队冲锋。

**• Ilya Sutskever ：DL 启蒙者，帮助 OpenAI 及时⾛上 Transformer 路线。**

Ilya 在 OpenAI 属于精神领袖的存在，他的技术直觉和品味很好，能够找到一些大家之前没有很重视的方向，比如 Scaling 能 work，三年前大家都不相信的时候特别坚持。

**• Wojciech Zaremba：联创，攻坚手，亲自放弃机器人探索后打造 Codex。**

在 GPT-4 的研究中，Wojciech 创建了 GPT-4 的数据集并负责了强化学习和 Alignment 中的人类数据管理工作。很多人评价 GPT-4 之所以能和别的大语言模型拉开差距，模型很重要，数据更重要。

**• John Schulman：RLHF 的开创者，打造了 OpenAI 的 RL 基础设施。**

John 在 Reinforcement Learning 的积累成就了目前的 ChatGPT。John 在 GPT-4 的开发过程中是 RL 和 Alignment 的带队人。

**• Jan Leike：落地 instruct GPT , 把 alighment 带到新高度。**

Alignment 是 OpenAI  区别于 Google 等大厂的重要能力，Jan Leike 带领团队攻坚递归奖励模型、辩论、迭代放大三大研究，并主导落地了 Instruct GPT，在 GPT-4 的开发过程中也负责了 Alignment 部分。

**• Andrej Karpathy：从特斯拉回归的创始成员和 CV 大牛，OpenAI 做多模态的有力加速器。**

Andrej 曾加入 Tesla 担任 Sr. Director of AI。回归 OpenAI 后，Andrej 在 Twitter 上表示自己将在 OpenAI 创造另一个“JARVIS”，意味着 Andrej 回归后会探索 AI 与语音识别的交互。

**• Mira Murati：OpenAI 新晋 CTO ，引领了 OpenAI 在 AI 安全上的探索。**

Mira 的背景十分有趣，在加入 OpenAI 之前，Mira 在 Leap Motion 负责产品和工程（Leap Motion  是 MidJourney  CEO 的上一个创业项目），Mira 在职业生涯早期还曾在 Tesla 担任产品。我们认为 **Mira 可能是人机交互领域最重要的 PM 之一**。

**• Lilian Weng：前沿技术和应用研究的桥梁，也是 OpenAI 高管团队中唯一的中国人。**

Lilian 是前沿技术和应用研究的桥梁，通过设计 API 拓宽了 GPT 的应用领域。在 GPT-4 项目中，她主导了应用领域的研究。在她的 Lil Log 中有很多研究的分享，是在 AI 从业者中很有影响力的博客。

**• Jakub Pachocki：OpenAI 的预训练专家，Sam 在 GPT-4 发布后专门感谢的人。**

他参与了 OpenAI 几乎大部分成功项目——深度参与了 Gym 和 Dota 的研究，负责了其中核心技术的攻坚，后带领推理和深度学习组。作为 GPT-4 预训练和整个项目的负责人（整个项目一共有两位 overall lead），Sam Altman 在 GPT-4 发布后发布一条 Twitter：“*GPT-4 预训练方法的成就离不开 Jakub 的领导力和远见。”*

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

OpenAI 的组织方式能够有自下而上的创新（ChatGPT 就是一个自下而上的 idea），也能在确定目标后集中力量朝一个方向努力，和传统科研机构单兵作战的方式不同。此外，OpenAI 给员工也有足够的激励，工资+期权平均成本 120 万美金/人/年，相对于 Google、Microsoft 等大厂也十分优渥。

优秀人才的号召力、吸引人的组织氛围以及优渥的激励让 OpenAI 正在“掏空”整个硅谷的科学家和 Super Talents。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*Google Brain 的 AI 人才不断流动至 OpenAI*

OpenAI 在 GPT-4 的论文里公布了贡献者名单，该名单显示，有 249 位员工深度参与了 GPT-4  的研究与开发 。GPT-4 的贡献名单分工非常清晰，可以作为大语言模型公司搭建团队的参考：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

开发 GPT-4 需要六个方向的研究团队：预训练（Pretraining）、长上下文语义理解（Long context）、视觉理解（Vision）、强化学习和对齐（RL & alignment）、评估分析（Evaluation & analysis）、部署（Deployment）。这六个部分不分主次，缺一不可。

每个方向除了领导团队外，又会拆分成不同的小组。成员并非只负责单个工作，而是在不同小组身兼数职。**值得关注的是，Data 工作部分中有很多一线负责预训练、Alignment 的科学家参与其中，说明大模型的数据质量是由很多模型训练的科学家亲力亲为共同完成的。**

此外，OpenAI 的发展中微软的支持也相当重要，相当于 Google 对 Deep Mind 的支持。例如，微软的 CTO 和 EVP Kevin scott 是第一个接触 OpenAI、将其带入微软的人，Sam 曾在第二次创业做 Loopt 就想招揽他去做 CTO；Scott Gruthrie 是微软整个生态系统 copilot 微软 365 Azure 等产品的负责人，真正将 OpenAI 接入系统 azure 的基建也由他负责，在 OpenAI 的发展中，微软几次“大义灭亲”，把计算资源从员工手里收走倾斜到 OpenAI。下图是在双方合作中发挥重要作用的微软高管。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*Source：The Information*

**OpenAI 走向大模型****是渐进的过程**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

从历史来看，OpenAI 绝对不是第一天就想做大语言模型的，这是一个渐进的过程。我们把 OpenAI 的前 ChatGPT 时代的历史大致分成了三部分：

**• 15-17 年：通过开发者产品打基本功。**

在这一阶段，OpenAI 确立了自己重要的产品风格 —— 定期得有产品成果跟社区和用户互动。通过一系列开发者工具包或者环境，OpenAI 建立了开发者圈子的影响力。同时，在交付这些产品过程中，团队认识到工程会成为研究的瓶颈，开始进行了工程基建和“研究与工程并重”的文化打造。

**• 17-19 年：逐渐转向“语言模型”和“大模型”。**

这个阶段 OpenAI 做的事情其实比较分散，包括机器人、语言模型、打 Dota 2 以及其他围绕深度强化学习的探索，这些都被认为是可能通往 AGI 的路。有两个项目让他们聚焦到大语言模型：

第一个项目是 17 年的情绪神经元，OpenAI 团队相信更好的理解才能带来更好的预测，这个工作印证了这一点。因此他们将更多注意力分给了语言模型，并且赶上了 Transformer 架构放大了这块儿的突破可能性；

第二个项目是 OpenAI Five 打 Dota 2。这个游戏由 Elon Musk 推荐给 OpenAI 团队，团队也觉得人从小学习和理解世界的行为和游戏很像，因此重点尝试了这个项目。过程中随着 scale up，Five 能打的对手从业余选手逐步升级到世界冠军，加深了团队对于“规模”的信仰和 AGI 实现的可能性。

**• 19-21 年：从 GPT-3 开始建立了一套大模型的产品打法。**

从 20 年 6 月 GPT-3 API 出来后，OpenAI 探索出一套产品和市场互动的路径，将一个用例不确定的东西抛给市场和开发者，让大家自己探索用例。这种做法对于学术界和 Deepmind 这样的公司是难以想象的，但事实证明非常有效，为 OpenAI 带来了生态和用户数据的飞轮。

**走大模型路线意味着大算力投入，OpenAI 在 19 年选择更专注这个方向后，做了 3 件事，建立了一套匹配大模型的经营策略：**

1\. 把已经有些成果出来的机器人团队砍掉，非常有魄力。事实证明这也是正确的选择，这个团队后面大多数成员转方向做代码的工作，产出了 Codex；

2\. 和微软深度绑定；

3\. 尝试自己建立造血能力。在通过 AGI 的路上，只依靠微软是不够的。OpenAI 还在持续探索自己的商业化能力，例如 OpenAI Foundry 就是 Greg 非常重视的项目，它解决了企业级客户的数据安全和领域 fine tuning 问题。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

除了沿着历史发展脉络来看 OpenAI 的演进，我们还可以反过来看，OpenAI 在这个过程中做了什么非共识或者超过对手的选择。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

有三个重要问题我们认为可以构成开放的思维实验题：

**1\. 从技术和研究角度：OpenAI 在 17 年下半年迅速上了 Transformer 的车，新的公司能不能有这样的敏感度？能不能把握住下一个 Transformer 级的变化？**

**2\. 从投资人角度：18 年是 OpenAI 非共识最强的时候，在各项子任务 GPT-2 效果均不如 BERT 的情况下，把我们放回去愿不愿意投？**

站在投资角度，2018 年可能是 OpenAI 最不被看好的时候 —— BERT 一出世就把 GPT-2 从 GLUE 排行榜上淘汰了，学界的论文和业界的各类子任务都选择使用 BERT。大多数人都惋惜 GPT 没用到下文的信息，认为“它将作为 BERT 的古怪前身被尘封入史册”。但是我们回头看最重要的一点，这种只有上文信息的自然语言生成模式在终局天然兼容了自然语言理解任务，能拥有这个大的认知和判断，而不是陷入对子任务效果的比较非常关键。

**3\. 从中国创业者角度，在没有受科幻小说荼毒那么深的情况下，是否跟随 OpenAI 和 Anthropic 的道路鼓吹 Al Safety，如何建立我们自己的 Safe AGI 定义？**

很多 AI 圈子里的欧美人从小读科幻小说长大，内心有两个深深的信念：第一是“AGI 来了之后人类连拔电线的机会都没有”；第二是“我不是坏人，别人都是坏人”，所以选择闭源、Alignment、Safety……我们中国人文化背景不一样，第一要意识到 LLM 跟社会的关系，第二也要思考怎么建立自己的 Safe AGI 定义。

**GPT 的进阶：充分运用算力，摆脱传统思路，实现通用泛化**

在 Transformer 出现前，传统的语言模型没有泛用的学习能力，只能用中间任务和目标任务的方式曲线救国：如果需要完成一次机器翻译任务，之前可能先要进行词性标注、实体识别等中间任务。

Transformer 出现后，BERT 很快成为了学术界共识。因为当时的 BERT 极大幅度地提高了原本各类任务的基准水平，被广大研究者用于刷细分领域的论文，影响力极强。但 GPT 实际上从 2 代开始，就在结构上表现出了比 BERT 更优的特点：

**1\. GPT 的技术路线使大模型做到了理解任务、举一反三。**GPT-1 和 BERT 的学习模式是让预训练模型迁就下游任务做改变，也就是做具体任务的时候，模型又会重新训练一遍调整参数权重。因此当时的大模型无法举一反三。而之后的 GPT-2 开始，few shot learner 的形式是在模型不变的情况下，模型能够“理解”新数据，这也是今天人类与语言模型最普遍的交互方式。

**2\. GPT 的技术路线更为极致：**一切 NLP 任务转生成。因为 GPT 的论文中经常提到自回归结构，是单向地给定当前位置之前部分的输入，预测当前位置的 Token 的输出。比如 GPT 的自回归是“我喜欢看书”，通过输入“我喜欢看”来预测“书”。这一技术路线的选择最大的优势就是适合生成。

**GPT 时期：Scaling Law 是 Beta，OpenAI 的前沿探索是 Alpha，成为语言场景下的通用模型。**GPT-3 向大家证明了正确的技术路径下，大量级模型的突现能力。突现能力的表现形式是：模型参数达到 65B/175B 时，就像人的18/30岁突然会有能力和心智上的突破。这一现象被学者们不断的挖掘发现，其中比较典型的有：举一反三的能力、一步步思考地推理能力和理解人类意图的能力，在多个海外的大语言模型上被观察到：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

突现能力背后的 Scaling Law 是 OpenAI 坚信当前的技术路线将通往 AGI 的基石。如果拿投资类比的话，Scaling Law 是大模型演进中的 Beta，而 OpenAI 对其边界的探索的优化是 alpha。如果我们拿当前的 GPT 模型和 5-6 年前的 NLP 能力作比较，称其为语言场景下的 AGI 并不为过。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**• Alignment**

Alignment 是 ChatGPT 走红的最关键技术，也是除了 Anthropic 外其他公司所忽视的技术重点。Alignment 是大模型的一个社会化过程，可以用来规范模型的“言行举止”。

在 Alignment 过程中，大家往往会提到 RLHF，但其中最关键的是 HF 部分的数据创新与标注。Instuction tuning 是目前主流做 Alignment 的方式，RL 只有当模型经过这一步 Align 到一定程度后才能起到显著的增益。这一方法会在未来地位将会更加重要，因为如果模型继续按照 scaling law 增长下去，同时如果他们又能随意分配模型技能点，那么这个模型就迟早会在特定领域上超越这个领域里最好的专家；那么在这个时候，alignment 的问题就不止是安全，同时也是如何驾驭远超人类的强人工智能。在强人工智能阶段，alignment 做的事情会像是运动员和教练的关系：运动员在他的项目上远超教练，但教练依然可以训练运动员做得更好。

**• 多模态**

OpenAI已经在内部开发的模型中加入了多模态能力。这一举动有两个重要意义：

**1\. 从数据量级的角度看，多模态是必然的趋势。**因为当下人类积累的文本数据已经接近被耗尽了，而引入图片、视频将能引入新的海量数据，让大模型进一步发挥其 scaling law 让学习能力提升的规律。

**2\. 多模态的加入也很可能产生出新的突现能力。**如果多模态领域能有能力突破的话，未来能基于文字（甚至是多模态）的 prompt 达到图文并茂的效果，这一突破影响极大，可能改变我们组织信息的形式，也可能使最近因为数据量卡脖子的自动驾驶领域有所突破。

谷歌最新公布的 PALM-e 很值得关注，是在多模态领域的一次重要尝试，也呈现了一定的涌现能力。但在多模态极其复杂的场景下，其所能实现的任务通用性还很一般，相比 GPT 在语言场景的通用性，未来还有很长的路要走。

**• 模型评估系统化：****模型效果度量尚未出现北极星指标**

目前在大模型领域已经由学界公布了一套全面的评估体系称为 HELM。此外 Anthropic 也公布了一套效果不错的评估数据集。目前的评估方式全面性有余，泛用性不足，熟悉 LLM 的人自己准备一套全面的问题清单测试下回答是否符合预期，可能是效率更高的方式。当前最接近这一目标的是 Perplexity，当 AI 以一定的概率输出某一句话时，其困惑度越低、确定性越高，代表其越约定这句话与我们的问题是 Align 的。从生成可控性的角度看，这的确是当下最重要的指标之一，其背后与香农的熵理论也高度接近。未来随着 LLM 的继续突破，一定会有更多重要的 metrics 出现。

**• 能力边界：LLM 只擅长 bottom-up 的思维方式，激发人类创造力而非取代**

当前的 LLM 技术路线是基于上文的逐字生成，决定了当前 AI 不具备 top-down 设计规划的能力。无论是文本还是多模态，都需要人使用明晰的 prompt 来做引导和设计。这决定了在分工上，**人是设计师和指路人，AI 是实践者和探索者。**

**OpenAI 接下来有哪些动作**

OpenAI 在本月中旬发布了 GPT-4，后续又迅速推出了 Plugin 这一功能，我们可以围绕这些重要事件来看 OpenAI 接下来可能还会有动作、以及带来的影响：

**1\. Plugin 插件：**

Plugin 最直接的作用就是重构了信息分发的方式，用户可以在同一个界面中完成和不同知识库的交互，Plugin 还能够替代用户执行很多操作，缩短了很多行为、交易的链路。Plugin 的推出对于互联网信息分发、产品间的组织和聚合状态、以及商业模式都会产生重要影响：

• 商业模式：插件接入大模型，收取相应费用；

• 下游站点的价值有可能被削弱；

• 传统 SEO（Search Engine Optimization） 未来可能成为 LMO (Large Model Optimization)；

• Plugin 有能力和先发优势定义大模型与应用互联的 api 标准，之后应用接入都会迎合这一标准；

• 解决原本知识时效性差 + 胡说八道的问题。

**2\. 闭源学术圈，开源创业圈：**

出于 AI Safety 的考虑，OpenAI 在发布 GPT-4 时也完全没有探讨自己的技术细节，但很多创业在发布前就已经提前使用到了 GPT-4 来开发自己的产品，对于 OpenAI 来说这是不断的巩固下游商业生态的方式，总体上 OpenAI 对于生态的构建是十分积极的，这也是加深自身商业壁垒的一个重要路径。

**3\. 和微软更深度的合作：**

除了对创业圈的开放，OpenAI 也通过和 Office、Teams、Azure、Surface（消费级终端）等产品或业务加入 AI 功能，例如之前 Microsoft 365 Copilot，在 Azure 上也在推出 To B 的解决方案来集成 OpenAI 本身的 API 能力。

**4\. OpenAI 还会在 AGI 领域进行哪些投入：**

**• Agent 能力：**让模型主动获取数据。当前的大模型是被动的去输入一些信息，这也和算力限制有关，但未来这一定是要做的一个方向；

**• 消费级终端：**新硬件才能采集更多的非结构化数据作为证实，肯定是他们也在布局的东西。随着大语言模型的提升，可能未来还有很多像自动驾驶机器人可能会都会因为当中的理解能力而受益。

**5\. 模型大拆小：**

当基础模型变成更接近人脑的、多专家的一个网络时，未来需要某个模块的能力的时候，把某个模块可能可以蒸馏或者拆解出来，做一些特定的职能，这都是他们未来会现在已经在努力尝试的一个方向。

**05.**

**相较于应用层，**

**未来 3-5 年 AI Infra 的确定性机会更高**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

AI Infra 主要分为模型层和工具层：模型包括开源、闭源以及从模型到应用的端到端的公司；工具层主要围绕着模型训练和模型推理两大板块 mapping 了各个细分环节。

我们目前更看好 AI Infra 的机会，在现在这个时点，Infra 和应用层相比更稳定，并且不用特别担心底层模型能力大幅提升后受到冲击。模型的价值毋庸置疑，Infra 工具在未来 5 年内也会有爆发式的增长，**核心逻辑是大模型公司搞军备竞赛，卖武器的公司增长一定十分可观。**

在 AI Infra 领域，除 OpenAI 外，我们还重点关注 Anthropic、Hugging Face，以及 Weights&Biases 等。

**• Anthropic：**

作为与 OpenAI 和 DeepMind（Google）并列的 LLM 模型领域 Top3 的公司，Anthropic 是其中唯一没有与大厂深度绑定的，Anthropic 的大语言模型 Claude 被认为是 OpenAI ChatGPT 最大的竞争对手。核心团队来自 OpenAI，CEO Dario Amodei 曾是 OpenAI 的研究和安全 VP。Dario 认为 OpenAI 大模型有很多安全问题尚未解决，便急于商业化，促使他带领 GPT-2 和 GPT-3 的核心作者们离开 OpenAI 创立 Anthropic，Anthropic 因此也十分注重 AI Safety。Anthropic的愿景是构建可靠的、可解释的和可操控的 AI 系统。

**• Hugging Face：**

Hugging Face 是全球最大的 AI/ML 社区和平台，也是 AI/ML 重要基础设施之一。Hugging Face 的核心业务位于 ML Workflow 的上游，是 AI/ML 的入口，用户可以在社区托管和共享 AI/ML 模型和数据集，也可以构建、训练和部署 ML 模型，与此同时，Hugging Face 不断向下游探索商业化路径，包括私人模型库、模型推理和部署、AutoTrain 等。若下游布局顺利，商业化取得成功，Hugging Face 将有可能渗透至 ML Workflow 的各个环节，成为 AI/ML 的中心。

**• Weights & Biases：**

Weights & Biases 聚焦于模型实验管理环节，未来还可能切入下游的模型监控领域，这两个环节是 AI/ML 领域 Datadog 级别的生态位，有机会诞生出 AI/ML 时代的 Datadog。

大模型训练的复杂程度和资源消耗程度使大模型企业对模型实验管理工具的需求激增，Weights & Biases 已经是赛道的 Top 1，OpenAI、DeepMind、Facebook AI Research、Midjourney、Stability、Nvidia、Microsoft 等公司均为 Weights & Biases 的客户。在未来 3-5 年内，Weights & Biases 还将持续享受大模型军备竞赛带来的红利。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在对 AI 应用层进行 mapping 的过程中，我们看到现阶段的 AI 应用整体呈现出两大特点：

1\. To B 应用的数量远大于 To C 应用；

2\. General 工具的数量远大于落地到具体场景的应用的数量。

**从功能看：技术最成熟、效果最好、公司数量也最多的是语言/文字和图片类应用，视频、音频、代码还需要一定时间，3D 似乎是更长远的事。**语言/文字类应用包含：文字生成（e.g Jasper）、语音识别和语义理解（e.g Fathom）、文字摘要和文字总结（e.g Agolo）、聊天机器人（e.g Character.ai）等。图像生成和编辑的典型代表公司是 MidJourney、Typeface 等。

**从场景看：**目前美国市场的应用主要集中在以下三大场景——Sales & Marketing、客服/CRM/CEM、企业内部生产力工具。均为 To B 场景。

**• Midjourney：**

文生图赛道是 Generative AI 概念下商业模式较成熟的领域，而 Midjourney 是其中最具竞争力的选手，也是将 Generative AI 技术成功产品化的代表。Midjourney 的 Discord 社区目前拥有超 1,000 万社区成员、年营收约为 1 亿美元。

Midjourney 有自己的模型，生成的图片效果非常好，一是它用于训练模型的数据质量非常高，二是它有一个四选一的反馈，这个很重要。Midjourney 目前是盈利状态，现金流很健康，团队只有 20 多人，没有接受外部融资。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**• Typeface：**

Typeface 是一个 AI 营销内容生成平台，由前 Adobe CTO 创立。Typeface 最大的特点是能够学习企业客户的“专有数据”。客户将带有企业风格的专有数据导入 Typeface 供模型学习，基于这些专有数据，Typeface 可以输出更个性化的、满足企业实际需求的内容，做到让 AI “更懂用户”。为了实现这一点，Typeface 让每位客户拥有独有的 AI 模型和托管服务，以及原创内容检测、品牌契合度检测和文字上的语法检测等功能。而收集专有数据的意识也在行业内逐渐形成共识。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**• Pilot：**

Pilot AI 2022 年成立，是一款面向销售人员的 AI 产品，核心是能够自动将每一个销售电话变成详细的笔记和结构化数据，并将结构化数据直接同步到 CRM 系统。这也是我们认为大语言模型的核心价值之一。我们平时聊天有非常多的数据，如果没有被记录和分析，就永远是 dark data。而大语言模型理解语言的能力变强之后，dark data 可以变成非结构化数据、结构化数据，变成 information。而且 Pilot 的整个流程都是自动化的，价值非常显著。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**• Character.ai：**

Character.ai 是个性化 AI 聊天机器人平台，用户可以在 Character 上根据个人偏好定制 AI 角色并和它聊天。ChatGPT 已经证明了人们对 Chatbot 的狂热和粘性，Character.ai 在此基础上加入个性化、UGC 两大武器，有了比 ChatGPT 更丰富的使用场景。自 2022 年 9 月发布后的两个月内，用户共创建了 35 万个角色，2022 年 12 月初 - 12 月中，用户日活又翻了 3 倍，我们了解到目前 Character.ai 的月活跃用户数在小几十万的量级。

Character.ai 团队背景也十分亮眼，创始人 Noam Shazeer 是 Transformer 作者之一，联合创始人 Daniel de Freitas 领导了 Meena 和 LaMDA 的开发。Character.ai 给我们带来的行业启发在于：随着高性能大模型的使用门槛进一步降低，未来 AI 应用层的颠覆式创新或许不在技术，而是产品设计维度的绝妙想法。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

最后补充一个值得关注的方向，即 OpenAI Fund 投资的公司。一方面，我们可以通过 OpenAI 的投资布局推测未来大模型最有机会在哪些场景落地、以及不同场景的落地节奏；另一方面，在 OpenAI 的 Portfolio 公司中，几乎每家公司都有非常具体的场景，而不只是工具的形态。因此我们认为 OpenAI 的投资标的非常值得关注。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**06.**

**硬件增量：训练及推理环节的价值捕获**

AI 硬件的增量市场中， 55-75% 的价值流向芯片，10-20% 流向内存，10-20% 流向通信设备。这三个环节中，初创公司的机会主要在于激进型 ASIC、存内计算（In-Memory Computing）和片间通讯（Chip-to-Chip）等场景。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**AI 分布式计算环节：云计算服务商寡头垄断， Server Venders 有部分机会**

**售卖分布式计算系统主要有两种商业模式，服务器供应商（Server Venders）和云计算服务商（Cloud Computing Service）。服务器供应商的 Operating Margin 通常在 10-15% 附近，云计算服务商的通常在 20-30% 左右。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Server Venders 主要由传统的服务器制造商 (75%) 和 ODM Direct 厂商 (25%) 组成，总年营收规模在 1000 亿美元左右；市场仍留了 25% 的空间给各类垂直场景下的小公司或初创企业，AI 场景下的 Server Venders 会有一定的空间，但终局来讲可能算是赚个辛苦钱（10-15% 的 Operating Margin）。

2000 亿美元的云计算服务商市场基本已经被巨头垄断（AWS、Azure、GCP 和 Alibaba Cloud 前四大占了 70% 的市场份额），在 LLM 的新浪潮中，微软正在通过独占 NVIDIA 的 H100 算力挑战 AWS，AWS 通过和开源社区 Hugging Face 合作来应战，谷歌也利用 GCP 资源孵化多家 LLM 初创公司（如 Anthropic）。

**芯片：推理需求未来将占算力大头**

**芯片可以拆分成三种需求：系统芯片、训练芯片和推理芯片。推理需求未来将占算力大头。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

训练需求可能随着模型训练量扩大带来的边际回报降低而最终会有上限，而推理需求随着推理成本的下降和更多 SaaS 集成而指数上升，推理需求未来将占算力大头。

投资推理芯片有需要预判**未来主流推理在云端还是边缘端完成，当前微软和 OpenAI 押注云端，苹果想以隐私为名开拓边缘端。**站在二级视角，终局是云端意味着利好 Nvidia 和 Azure，边缘端意味着利好苹果和台积电（因为需要性能强劲的 SoC 芯片）；对于一级视角，云端意味着利好 ASIC 和 RISCV CPU（后面将会介绍），边缘端将利好 FPGA 和类似 Apple Silicon 的 SoC 芯片研发公司；当然也可以同时押注两边，只是要及时调整市场空间的预期，并根据模型压缩技术的进展及时调整仓位。

**而初创公司不仅需要技术剑走偏锋才能在 ASIC 立足，也需要大模型长期技术路径稳定，所以知道顶尖 AI 模型公司的路线图对芯片公司有重要意义。**

**内存：主流内存技术已被寡头垄断**

**内存分为传统内存和新型内存，传统内存已被三家寡头垄断，新型内存技术离商用还有至少五年以上时间，**存内计算技术成熟后将能同时打下内存端和芯片端的市场份额。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**互联设备：初创公司可以通过片间通讯打破垄断**

互联设备可以分为 Server-to-Server 和 Chip-to-Chip，Server-to-Server 已经被传统网关公司和 NVIDIA 垄断了，Chip-to-Chip 环节还存在有一些初创公司的机会，并且技术成熟度较高，预计 25-27 年会在数据中心推广开。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Chip-to-Chip 指的是芯片之间绕过网线的直连技术，**当前做的最好的是 NVIDIA 的 NVLINK，其他厂商在做超近距离的 Chiplet 和较远较大规模的 CXL。Chiplet 主要被台积电垄断**，它将多个芯片（CPU、GPU 或图像处理特质芯片）在生产过程中堆叠起来，并让它们之间高效通讯和协作。CXL 是 AMD、 Intel 等芯片厂模仿 NVLINK 开发的开源协议。

**Chiplet 是芯片巨头未来的主要优化路径，主要价值还是被巨头捕获。**比如 AMD 的 MI300 和 NVIDIA 的 Grace Hopper，都用台积电的 Chiplet 技术将 CPU 和 GPU 高效的互联起来，现在是 1 CPU 和 1 GPU互联，未来可能可以 1 CPU 和多 GPU 互联，这样可以绕过跟不上时代的主板 和 PCIE 生态，这样单台服务器效率会高很多。

**CXL 则是满足了 data center 大规模互联的需求，NVIDIA 因 NVLINK 领先且垄断不想投入， Intel 和 AMD 很看重且技术积累不高，初创企业有一定的机会。**既然巨头跟 Startup 都在同一个协议下竞争，且巨头的技术积累可能就领先两年，初创企业很有可能在 2025 年 CXL 3.0 大规模量产前被主流芯片厂收购。所以这里应该有投资机会。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

延伸阅读

OpenAI创始人的AGI预言：AI Safety、Scaling laws与GPT-20

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

ChatGPT思考：探索智能的极限

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

ChatGPT：受惊骇的巨头们与焦虑中的军备竞赛

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgzWic9ViaQNX2f1uQeSDXUQwohbdDCBJJOjvWxwMbKHVn5fNjmmicjyx9zibL0UiakxkjticscqBPicPm2Ug/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=47)

LangChain：Model as a Service粘合剂，被ChatGPT插件干掉了吗？

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgzWic9ViaQNX2f1uQeSDXUQwohbdDCBJJOjvWxwMbKHVn5fNjmmicjyx9zibL0UiakxkjticscqBPicPm2Ug/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=49)

Runway：AI Native Tools工厂，视频生成领域的字节跳动

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tHNibnJ2jgzWic9ViaQNX2f1uQeSDXUQwohbdDCBJJOjvWxwMbKHVn5fNjmmicjyx9zibL0UiakxkjticscqBPicPm2Ug/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=51)