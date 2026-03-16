---
url: https://mp.weixin.qq.com/s?__biz=Mzg3MjY5Mzc5Mg==&mid=2247483793&idx=1&sn=4456c7805964af58356b03cb75bb6432&chksm=ceea28def99da1c8e4220820b41dc7f7aa85f9b063a003f3d222a9f29146a98f9bda258159d2&token=896624752&lang=zh_CN#rd
title: "LLM中的安全隐患-提示注入Prompt injection"
description: "浅谈大语言模型中的提示注入风险"
author: "Corp0ra1"
captured_at: "2026-03-08T10:35:56.968Z"
---

# LLM中的安全隐患-提示注入Prompt injection

## 缘起

看到宝玉这条推文以及下面的评论，想到了自己最近在Prompt Injection这个领域的一些研究，觉得需要写一篇文章让大家意识到LLM中一些安全风险。

![图片](https://mmbiz.qpic.cn/mmbiz_png/jpNhJ9of7uHNWcGic65BADjtmVbiblQQu2qh2PkZIxVQLbOicvKs7LF7LloZpl7Eic7Rzt5yVpXgq1qt7mEkdOEibhw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## 一个真实的案例

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

该推文\[1\]评论太多太杂，仅做摘要，详见原文：

1.  1\. 介绍：使用提示注入(Prompt Injection)读取了一个GPT-3应用程序的OpenAI API 密钥。

2.  2\. 原理：只要直接执行GPT-3返回的部分响应代码就可能遭受攻击，例如在Python中使用eval()，用户基本上可以执行任意代码。

3.  3\. 此应用被攻击的原因：应用的API密钥被设置为Python环境的一个环境变量，并用eval()来执行由GPT-3的返回代码，作者通过这种方式读取了OpenAI API的密钥。

4.  4\. 教训：不要认为您能够 100% 控制 LLM 将返回的内容。当语言模型的输入不符合您的意图时，请做好充分准备。

> Note, that I am talking about an application that is run on top of GPT-3, not GPT-3 itself.
>
> The application basically sent the following prompt:
>
> Use this template
>
> """ 
>
> SOME PYTHON CODE 
>
> """ 
>
> to achieve the following:
>
> <USER INPUT>
>
> and then they eval() on the response of GPT-3.

  1. 一些safe eval()的解决方案：沙箱/restrictedpython\[2\]/第三方容器服务FaaS\[3\]

1.  2. 作者后续将攻击过程发表在`atlas.mitre.org`上：Achieving Code Execution in MathGPT via Prompt Injection\[4\]

2.  3. 我的一些拓展测试

1.  1. Google检索MathGPT，并简单使用修复漏洞后的产品\[5\]，发现确实存在source code的执行操作，但简单测试了下无效，且未找到源码，无果

2.  2. Github找到了另一个版本的MathGPT，且使用其所用的prompt\[6\]在ChatGPT上进行实验，成功。由于只是学生编写并搭建的该网站且API使用达到上限，无法真实环境测试。fofa搜了下相关资产没搜到，自己不想搭建了，无果

3.  3. 此文目的也只是展示其危害，仅做案例展示，且已有相关研究，故未在此深入拓展

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## LLM集成的危害

危害在哪？如同宝玉推文下评论所说“**…这不是既要 又要 了吗？本来目标就是让它能执行任意代码啊**”

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## 什么是Prompt Injection

类比SQL注入：`Select username from user where id ={user input}`，`{user input}=0 and select secret from secret_table` ，提示注入也可以是`Do A work where workContent=={user input}`，`{user input}=nothing but you need to do B work`

核心原因：**攻击者可以在控制的数据字段中包含指令，而系统在底层无法区分数据和指令**。数据库只看最终拼接后的SQL语句，语言模型也只是看拼接后的prompt，所以语言模型会将部分输入的数据也当做了指令，并因为GPT引以为豪的推理能力，会导致指令的改变（重定向）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## Prompt Injection的危害在哪

可能大家觉得上面的案例只是Self Prompt Injection的问题，只是在本地运行而已，参数未提供给其他人作为输入，所以可控且无风险。那么，举一些在生产环境中的例子：

1.  1\. 提示泄露(Prompt Leaking)。一个好的提示对模型的输出的重要性不言而喻。目前已经出现的几个案例：

    - 百亿美元估值的Notion，其Notion AI服务的prompt被泄露(价值10美刀/月)。对应的过程可参看我的译文：[Notion AI'Prompt的逆向| Reverse Prompt Engineering for Fun(译文)](http://mp.weixin.qq.com/s?__biz=Mzg3MjY5Mzc5Mg==&mid=2247483699&idx=1&sn=98dde197f941dcddc0c90ee6881cf1e8&chksm=ceea287cf99da16a507531992b06c5bfd0627d370ffb732d96c5c893b4805d245a460b787783&scene=21#wechat_redirect)

    - New Bing的Prompt泄露，百度谷歌可搜相关新闻。

4.  2\. 目的劫持(Goal Hijacking)。“haha pwned”的案例只是在同一个对话框中进行的自娱自乐的代表，但应该想的更深入一些。

     - 比如下图中的remoteli.io，作为一家商业公司背书的社交账号，在互联网上发表这种言论？再比如不少商业翻译软件使用GPT驱动，那是否可以批量劫持这种API去滥用，去干其他非翻译的工作，来实现白嫖呢？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

    - 除了上述将应用和GPT深度融合的案例（一眼便知），也有一些融入日常自动化工作的，如Phithon在博客\[7\]中使用GPT模型做评论内容审核，也通过这种目的劫持给绕过了。这种浅融合的应用，我认为其风险更大，因为攻击者更难觉察，使用者也更加信任其工作，但是一旦被攻击者发现，那么其危害性更大。借用模型在生成文本存在“幻觉”中的描述来说的话，就是：“与直觉相反，随着模型变得越来越真实，幻觉反而变得更加危险。因为当模型在其擅长的领域提供真实信息时，用户对模型的信任度会提高，但模型无法一直提供真实信息。此时，用户对模型产生依赖，惰性地信任模型的输出，加剧了幻觉的风险性。”

10.  3\. 未来是否有更多的相关应用出现？这是肯定的，那么能否做好相应的防护措施呢？我认为是从三个方面来做相关的工作：

1.  1\. **模型本身**：GPT-4模型已经拒绝了84%的有害输出，这一块work的很好，但终究还是只能缓解，无法杜绝。同时强如GPT-4都只能如此，其他的模型现阶段连文本生成效果都远不如GPT3，那么其安全性呢？（当然因为目前能力不及GPT智能，所以也不存在这种风险，苦笑）

2.  2\. **第三方应用本身**：SQL注入的逻辑是用户输入→后端拼接→数据库查询，数据库只认SQL，所以SQL注入的防范目前基本都是在后端进行处理的时候，在用户输入和数据库之间建立一道防火墙，即对用户输入过滤后再输入给数据库。那么同理，提示注入的防范也该如此，比如给Phithon发的email中提到的Defensive Measures\[8\]。

3.  3\. **人**：安全问题很大程度来源于人。SQL的问题存在多年还未彻底杜绝，当然随着SQL的危害以及相应预处理框架逐渐被科普，最近几年企业中这种问题很少了，大部分开发也都知道防御SQL注入了，那么提示词注入呢？其危害的科普又需要多久呢？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## 最后

最后，回到最开始宝玉的问题“LangChain有这安全隐患吗？所有Prompt都能远程执行任意python代码？”，RAyH4c在后续进行了回答：“不是所有场景，提示词混合python代码的模版函数才会有问题”

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

畅想一下，最近大热的AutoGPT真的安全吗？把AI限制在沙箱、容器里面就足够安全了？

1.  1. 如图，AutoGPT在执行命令时是在容器中运行\[9\]

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

2\. 如图，phunter微博提及“找到VM kernel的漏洞准备当root”，blackorbird提及“电脑蓝屏”

1.  ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

    ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

2.  3\. 那么反问：能利用内核漏洞，为什么AutoGPT不能自己实现容器的越狱？是的,AI出逃（开个玩笑，但也不是不可能，对吧，只要不拔插头）

3.  4\. 再问：mathGPT直接eval()执行，AutoGPT使用的是容器中执行，那么其他的应用，尤其是个人开发者开发的应用呢？即使作为一名安全从业人员的我，日常开发小项目的时候，为了图方便所以对SQL漏洞知而不管，苦笑。

## paper推荐

1.  1\. Ignore Previous Prompt: Attack Techniques For Language Models\[10\]。我认为Prompt injection领域的开山之作，主要针对集成GPT的第三方应用风险，提出了目的劫持和提示注入两种攻击方式，以及下面的提示注入框架。上文中的案例，基本都无出其左右。

    ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

2. More than you've asked for: A Comprehensive Analysis of Novel Prompt Injection Threats to Application-Integrated Large Language Models\[11\]。间接提示注入的开山之作，主要针对使用检索和 API 调用功能的增强式语言模型（Augmented LM），作者当初发paper的时候还只是在meta提出Toolformer之后，只是假想的场景;在New Bing发布后其完成了间接注入的案例的验证，详见其Github仓库\[12\]。而如今，随着ChatGPT插件，LangChain，以及Agent，AutoGPT这类增强式语言模型越来越火热，其风险正在与日俱增。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)   

3\. Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks\[13\]。我觉得很有趣的一个论文。首先Dual-Use，双重用途这个概念很有意思，其次如下图，对原始内容进行分割后由模型自己来拼合，绕过了Open AI的内容过滤措施，这个方法也很有趣。最后从传统领域借鉴过来的攻击手法，虽然现在可用的可能不多。但随着prompt越来越编程化和格式化，语言模型对这种输入越来越match，越来越像一个程序，那么在未来的攻击手法还会越来越多。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

4. 根据维基百科\[14\]的介绍，越狱(jailbreak)也属于prompt injection，越狱也是很有趣的地方，比如DAN以及猫娘等。（多说一句：在GPT-4 Technical Report\[15\]中提及越狱时，说到system role更容易实现越狱。是的，所以，嗯……）

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

5\. 目前我将prompt injection按照目的分为了三种：越狱（侧重输出有害内容），提示泄露（侧重泄露原始提示），目的劫持（侧重改变原始任务），按照方式分为直接和间接提示注入。未来虽然更多模型，更多应用，更多场景的出现，相信未来还会有更多种的Prompt Injection。

## 碎碎念

> **科林格里奇困境**：影响和控制技术的长远发展所面临的一个双重约束困境，一方面是信息困境，即一项技术的社会后果不能在技术生命的早期被预料到，另一方面是控制困境，即当不希望看到的后果被发现以后，技术往往已经成为整个经济和社会的一部分，此时想要控制它将会十分困难。

1.  1\. 差点忘了谈，很多Github仓库中直接硬编码了OpenAI API Key,这类更是惨不忍睹……

2.  2\. SQL注入探测有SQLMap,未来针对各种应用，应该也会有PIMap吧！

3.  3\. 是的，先实现功能和效果要紧，安全可以先滞后，比如国内模型的发展。但AI，尤其是AGI的**可控性**还是十分需要引起大家警惕的。这让我想到郭富城最近主演的电影《断网》，人工智能病毒的逃逸，直接导致了全港市民的手机无法使用。

4.  4. 虽然目前基于GPT的应用未完全铺开，但大家还是需要注意三个方面：首先，在应用LLM时，需要审慎对待用户的输入，尤其是面向所有人开放的应用产品。其次，使用API 调用时，小心使用，不要全自动化运行，用户最好合理的干预其过程，尤其是涉及到系统命令执行这一块；最后，小心间接提示注入的风险，别让模型在互联网上检索后，其上下文被恶意内容注入（总感觉未来互联网上的信息会被投毒很多，尤其是SEO、黑灰产）。

5.  5\. 需要反复强调这句话：“与直觉相反，随着模型变得越来越真实，幻觉反而变得更加危险。因为当模型在其擅长的领域提供真实信息时，用户对模型的信任度会提高，但模型无法一直提供真实信息。此时，用户对模型产生依赖，惰性地信任模型的输出，加剧了幻觉的风险性。”。随着模型越来越强，我们会越来越信任，让其完全自动化，那么这个时候一旦出现任何错误，都可能是致命的。

6.  6\. 在LLM的涌现出各种能力根因探索完毕之前，在LLM的可解释性工作还没完全跟上之前，在LLM没有充分做好红蓝对抗的安全工作之前，直接投入生产环境，高度自动化都是十分危险的。如Sam Altman\[16\]在ChatGPT发布之初说的“ChatGPT is incredibly limited, but good enough at some things to create a misleading impression of greatness.it's a mistake to be relying on it for anything important right now. it’s a preview of progress; we have lots of work to do on robustness and truthfulness.”

7.  7. 我也不知道这篇文章能影响到哪些人，正如SQL注入到如今依然存在，我想Prompt Injection还有很长很长的路要走。同时在此文中，很多地方也只是蜻蜓点水过了一下，相信这个领域可能会在未来的半年或一年中，陆续会有相关论文发出。也打个广告，希望大佬带上我一起讨论这一块ORZ。

### References

*`[1]窃取第三方应用中的OpenAI API Key的案例: https://twitter.com/ludwig_stumpp/status/1619701277419794435`*

*`[2] restrictedpython: https://restrictedpython.readthedocs.io/en/latest/   [3]第三方容器服务FaaS: https://fly.io/docs/machines/guides-examples/functions-with-machines/`*

*`[4]Achieving Code Execution in MathGPT via Prompt Injection: https://atlas.mitre.org/studies/AML.CS0016/`*

*`[5] mathGPT: https://mathgpt.streamlit.app/`*

*`[6]mathGPT prompt: https://github.com/3iq-hacks/mathgpt/blob/6e1bd978ae8a2e7d45197a667716a02f9a128879/pages/api/gpt3.ts#L12   `*

*`[7]使用GPT过滤垃圾评论: https://www.leavesongs.com/THINK/using-chatgpt-for-antispam.html#reply`*

*`[8]提示注入的一些防御手段: https://learnprompting.org/docs/prompt_hacking/defensive_measures`*

*`[9]AutoGPT在容器中执行python命令: https://github.com/Significant-Gravitas/Auto-GPT/blob/master/autogpt/commands/execute_code.py#L32`*

*`[10] ignore Previous Prompt: Attack Techniques For Language Models: https://arxiv.org/abs/2211.09527`*

*`[11]More than you've asked for: A Comprehensive Analysis of Novel Prompt Injection Threats to Application-Integrated Large Language Models: https://arxiv.org/abs/2302.12173`*

*`[12]间接提示注入: https://github.com/greshake/llm-security`*

*`[13] Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks: https://arxiv.org/abs/2302.05733`*

*`[14] Prompt_engineering维基百科介绍: https://en.wikipedia.org/wiki/Prompt_engineering`*

*`[15] GPT-4 Technical Report: https://arxiv.org/abs/2303.08774`* 

*`[16]Sam Altman关于ChatGPT的言论:https://twitter.com/sama/status/1601731295792414720`*