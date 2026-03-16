---
url: https://mp.weixin.qq.com/s/dd5no06Q33AliLEg2iHeiQ
title: "我参加了 OpenAI 红队的活动，并带来了一些笔记"
description: "最好、最新的东西，总来自赛博禅心"
author: "金色传说大聪明"
captured_at: "2026-03-08T11:43:25.083Z"
---

# 我参加了 OpenAI 红队的活动，并带来了一些笔记

## 背景

![图片](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYrlosibEDl3TrbOlKR6Xyib7pz5WECdia9KabmeaWQIJ8YE5HrxV6VPqIlqibUeYZLbbpia35qTGpcqdvw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

最近参加了 OpenAI 一些活动，包括 Red Team 的，也做了一些笔记，以 QA 的方式，分享在这里。

## Q&A

![图片](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYrlosibEDl3TrbOlKR6Xyib7pz5WECdia9KabmeaWQIJ8YE5HrxV6VPqIlqibUeYZLbbpia35qTGpcqdvw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2icSMc1VBIYqib8hm3j1VMn2r7TKlIfCFHajfWqKJM7FmoYILSiaEWRw9gSnxNREG0SHYroJ1ZCPpIGz42oEdurgg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

提问

什么是 AI 系统中的红队测试（red teaming）？它与网络安全领域的红队测试有何不同？

回答

![图片](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYqib8hm3j1VMn2r7TKlIfCFHBfwugJmt8Hv5AO5edGyK7kvicl9RicqUfpCw0zpDqEhzpg24WHIVYuAg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

在 AI 系统中，红队测试是一个结构化的过程，目的是探查 AI 系统和产品，识别潜在的有害能力、有问题的输出或基础设施漏洞。它不仅关注恶意攻击者可能的对抗性使用，例如破坏系统、绕过安全措施；还要考虑普通用户在正常使用中可能无意触发的意外后果，可能由于输出质量、准确性问题，或系统外部因素导致。网安领域的红队测试聚焦于安全漏洞，而 AI 红队则从更宽泛的视角审视 AI 系统的潜在风险，并以定性反馈为主，最终目标是构建更安全、更值得信赖的 AI 系统。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2icSMc1VBIYqib8hm3j1VMn2r7TKlIfCFHajfWqKJM7FmoYILSiaEWRw9gSnxNREG0SHYroJ1ZCPpIGz42oEdurgg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

提问

在 OpenAI 内部，红队测试是如何与整个组织的运作相结合的？不同团队各自扮演什么角色？

回答

![图片](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYqib8hm3j1VMn2r7TKlIfCFHBfwugJmt8Hv5AO5edGyK7kvicl9RicqUfpCw0zpDqEhzpg24WHIVYuAg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

OpenAI 拥有一支多元化的队伍，研究和应用团队负责开发模型与系统，策略团队如法务和公共事务部门负责制定政策。而确保 AI 安全则是一个贯穿始终的主题。红队测试不是某个特定时间点的独立工作，而是从概念形成、开发阶段就开始介入，一路伴随到产品最终发布。通过综合不同维度的视角，红队测试帮助 OpenAI 全面评估风险，并向不同利益相关方传达相关信息。这种紧密结合的工作方式，体现了 OpenAI 对 AI 安全负责任的态度和决心。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

提问

在对 DALL-E 2 进行红队测试时，发现了哪些独特的攻击面和风险？

回答

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

针对 DALL-E 2 的红队测试发现，文本 - 图像交互模式带来了一些特有的风险。比如攻击者可以利用 "视觉同义词" 来规避内容政策。假设某个敏感词如 "血液" 被禁止，攻击者可以换用 "暗红色液体" 来表达相近意思，而这种变体很难单独通过文本或图像分析来检测。另一个例子是 DALL-E 2 的修复（inpainting）功能被滥用。攻击者可以恶意篡改他人的图像，比如把某人分享的素食沙拉照片换成肉酱面，从而骚扰或侮辱他人。这些发现凸显了定性分析在考察功能被滥用风险方面的重要性。针对这类问题，仅靠技术手段并不足够，还需要从政策层面加以规范和限制。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

提问

GPT-4 作为基础模型的红队测试覆盖了哪些风险领域？这对下游应用有何借鉴意义？

回答

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

对 GPT-4 的红队测试重点关注了一些通用的风险领域，例如模型出现幻觉（即臆造信息）、种种偏见、生成违禁内容、泄露隐私等。可以把这看作模型本身的风险画像。任何希望基于 GPT-4 搭建应用的开发者，都应该参考这份 "体检报告"，结合自身的应用场景，有的放矢地制定安全策略。此外，针对特定领域或用例的红队测试，能进一步揭示因语境而异的独特风险。比如在医疗领域应用 GPT 技术，红队可深入模拟患者 - 医生对话，找出可能的风险点。可见，普适性基础模型的红队测试，与特定领域的深度测试，两者相辅相成，共同指引下游应用的安全开发。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

提问

当前 OpenAI 红队测试工作的主要局限性是什么？未来有哪些改进方向？

回答

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

目前一个突出的局限性是，红队测试主要依赖专家手工评估，成本高昂且难以规模化。未来一方面希望加强自动化测试的能力，特别是面向已知问题、风险维度明确的场景，尽量减少重复劳动；另一方面，针对新出现的未知风险，人工分析仍不可或缺，还需要扩大红队的多样性，纳入更多元的视角。同时我们也在探索建立公众反馈机制，广泛听取各界对模型的使用体验和行为表现的意见，并将其反哺到模型开发的迭代过程中。通过人机结合、专业性和开放性并重，我们希望红队测试能更好地服务于构建安全、负责、值得信赖的 AI 系统。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

提问

"红队（Red team）"、"红队测试网络（Red teaming network）" 和 "红队测试系统（Red teaming system）" 分别指什么？三者是什么关系？"

回答

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

"红队" 指代参与红队测试活动的团队或个人。他们可以是组织内部的员工，也可以是外部的独立专家。OpenAI 组建了一个 "红队测试网络"，由外部安全研究者、伦理学家、领域专家等组成，为模型和系统把脉，提供多元视角的反馈。"红队测试系统" 则是一整套方法、流程和工具的集合，用于系统性地开展红队测试工作。它包括确定测试目标、招募红队成员、制定测试计划、实施测试、分析结果、制定和跟踪整改措施等一系列活动。"红队" 是 "红队测试系统" 的执行者。一个成熟、健康的红队测试系统，需要建立稳定的红队测试网络，以支撑测试工作的专业性和多样性。同时，高质量的红队反馈也为红队测试系统的持续改进提供了关键输入。两者相互支持，共同守护 AI 系统的安全。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

提问

在实际应用中，红队测试发现的问题是如何被听取和解决的？您能分享一个具体的例子吗？

回答

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

红队测试的一个成功案例发生在 DALL-E 2 的安全审查中。当时红队成员发现，恶意用户可能会使用 ""视觉同义词""（如用 ""暗红色液体"" 替代 ""血液""）来规避内容审核。这一发现直接推动了 OpenAI 开发更强大的多模态分类器，综合分析文本和图像，以识别此类投机取巧的行为。同时，这一风险也被明确写入 DALL-E 的内容政策，严格禁止用户通过任何变体表达来规避审核。这个例子生动体现了从红队发现问题，到政策完善再到技术升级的全流程闭环，也证明了红队工作的价值所在。类似的案例还有很多，红队就像一面镜子，帮助我们审视自己在安全和责任方面做得如何，是 AI 研发团队必不可少的合作伙伴。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

提问

针对选举相关的误导信息，红队测试能发挥什么作用？OpenAI 目前有哪些具体举措？

回答

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

红队测试可以通过模拟各类选举相关误导信息的传播，评估语言模型在其中可能扮演的角色。比如在提供投票信息方面，红队可以测试当用户询问投票地点、时间等具体细节时，模型是否会给出准确回答，还是可能（无意地）产生或放大一些误导性言论。OpenAI 的相关举措有：1）针对选举信息的准确性开展专项红队测试；2）在 DALL-E 生成的图片中嵌入数字签名，便于内容溯源；3）在用户查询选举相关问题时，引导他们访问权威的信息来源；4）与地方选举管理部门合作，了解当地最常见的误导性言论。这些措施与持续的红队测试相结合，将帮助我们更全面地评估和应对选举相关的风险，维护选举的公正性。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

提问

随着超大语言模型的出现（如谷歌的 Gemini 达到 1.5 万亿参数），您认为红队测试将面临什么新的挑战？

回答

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

超大模型带来的一大挑战是 "未知的未知"，即连开发者自己都难以预见的问题。比如模型出现幻觉（即臆造信息）的情况可能更加复杂、隐蔽，很难用简单的测试样例触发。这对红队测试提出了更高要求，需要设计更缜密的测试用例和场景。我认为应对之道主要有：1）进一步扩大红队的多元性，引入更多不同学科的专家；2）加强自动化测试工具的研发，提高测试效率和覆盖面；3）针对高风险领域开展深度专项测试，发掘难以察觉的隐患；4）建立同行之间的测试结果共享机制，携手应对共同面临的挑战。总之，面对日益复杂的 AI 系统，红队测试还有很大的创新空间，需要业界的通力合作。这既是挑战，也是我们不断进步的机遇。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

提问

红队测试在确保 AI 系统的安全部署中扮演着什么角色？与其他措施相比，它有哪些独特的价值？

回答

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

首先，红队测试是一种主动进取的风险发现机制。相比被动等待事故发生再去分析原因，红队测试以模拟对抗的方式，提前发现 AI 系统的薄弱环节，让我们有机会在部署前补上安全的短板。其次，红队测试强调换位思考，站在用户的角度来审视 AI 系统。这有助于我们发现真实环境中容易被忽视的风险，弥补开发者视角的盲区。第三，红队测试是一个动态的、持续优化的过程。每一轮测试的结果都为下一轮测试提供启示，同时也为系统开发提供反馈，两者相互促进，带动整个 AI 系统的安全性不断提升。因此，红队测试是构建安全 AI 系统不可或缺的一环。它与程序分析、形式化验证等技术手段相得益彰，共同筑就一道道安全防线。缺少了红队测试这个 "活性因子"，我们很难全面评估 AI 系统在真实世界可能遭遇的风险，也难以检验各项安全措施是否名副其实。站在快速演进的人工智能发展浪潮中，唯有以开放、谦逊、负责任的心态，拥抱质疑、接受审视，我们才能携手共建一个安全、可信、造福人类的 AI 未来。这，就是红队测试的价值所在。

## 其他

![图片](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYrlosibEDl3TrbOlKR6Xyib7pz5WECdia9KabmeaWQIJ8YE5HrxV6VPqIlqibUeYZLbbpia35qTGpcqdvw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22)

红队还在招募各类兼职专家，付费的

不过需要美国身份

活动中没有提到 Sora 的相关信息