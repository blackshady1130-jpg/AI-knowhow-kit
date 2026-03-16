---
url: https://mp.weixin.qq.com/s/-tS4lrziFB8jXJw3cxXN9w
title: "2、DeepSeek-R1 进阶之路：多阶段训练，步步为营的推理炼金术！"
author: "玄衍纪源内容官"
captured_at: "2026-03-08T12:38:49.904Z"
---

# 2、DeepSeek-R1 进阶之路：多阶段训练，步步为营的推理炼金术！

## **文章标题：DeepSeek-R1 进阶之路：多阶段训练，步步为营的推理炼金术！）**

各位 AI 爱好者，上一篇咱们聊了 DeepSeek-R1 如何 “不按套路出牌”，靠强化学习 (RL) “单枪匹马” 练成神功。但今天，我得跟大家“坦白”：DeepSeek-R1 的真实进阶之路，绝非“一蹴而就”，而是更像一场精心策划的“推理炼金术”——**多阶段训练，就像在精密仪器中，一步步提炼 LLM 的推理精华，过程复杂又精妙。** 你是不是有点懵？别急，这就带你解开谜团！

![图片](https://mmbiz.qpic.cn/mmbiz_png/FPmVmVfL7G0viclHnYryn380rU6iba57nRd8vScBgNFlwflXWwGsvOLkJlo8POXKGicrFv6ujJvpGuWGe3LJtfXSg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=0)

---

### **一、澄清误区：“无需 SFT” 的真相**

首先，咱们得澄清一个误区：第一篇说 DeepSeek-R1 “无需 SFT”， 并非完全不用 SFT，而是指 **DeepSeek-R1 的核心训练，不依赖于SFT的引导，而是强化学习。** 换句话说，SFT 只是 DeepSeek-R1 的“辅助工具”，而非核心驱动力。真正撑起 DeepSeek-R1 推理能力的，还是强化学习 (RL)。

-   • **SFT 的辅助角色：** SFT 在 DeepSeek-R1 的训练中，主要用于初始化模型、生成高质量数据和增强模型泛化能力。

-   • **RL 的核心地位：** RL 才是 DeepSeek-R1 推理能力提升的 “核心引擎”，让模型具备自主探索和思考能力。

-   • **“无需”的含义：** “无需 SFT” 的意思是指：DeepSeek-R1 可以通过 RL 来达到强大的推理能力，而不需要依赖 SFT 作为最主要的训练手段。

这就像一位武林高手，虽然练习了一些基本功，但真正让他成为高手的，还是在实战中摸爬滚打，不断提升的实战能力。

---

### **二、Step 1：冷启动，初窥推理门径**

DeepSeek-R1 的训练，从一个精巧的 “冷启动” 阶段开始。这个阶段，不是 “大干快上”，而是先 “温水慢炖”， 为后续的推理提升打下基础。

-   • **少量高质量数据：** 研究人员收集了少量但高质量的长思维链 (Chain-of-Thought, CoT) 数据， 这些数据包含了清晰的推理过程和答案。

-   • **SFT 预热：** 使用这些数据，对 DeepSeek-V3 基础模型进行有监督微调 (SFT)，让模型初步具备生成 CoT 的能力， 这就像让模型先 “抄写” 一些范文，了解什么是 CoT。

-   • **避免盲目探索：** 冷启动的主要目的是为了让模型在后续的 RL 训练中，不至于像“无头苍蝇”一样，毫无头绪的探索。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

---

### **三、Step 2：推理导向的 RL (RORL)，锻造推理之魂**

有了冷启动的 “热身”，DeepSeek-R1 进入了关键的 “锻造推理之魂” 的阶段：推理导向的强化学习 (Reasoning-Oriented RL, RORL)。

-   • **GRPO 算法：** 使用 Group Relative Policy Optimization (GRPO) 算法，让模型在环境中进行探索，并根据奖励信号优化策略。

-   • **GRPO 原理：** GRPO 是一种策略优化算法， 它利用同一组输出的奖励信息来估计基线，避免了训练额外的批判模型，减少了训练开销。

-   • **通俗理解：** GRPO 就像一个 “裁判”，每次模型 “答题” 后， “裁判” 会根据模型这一组回答的情况， 给模型打分， 并帮助模型学习如何更好的 “答题”。

-   • **规则奖励：** 在 RORL 阶段，主要使用规则奖励 (Rule-based Reward) 来评估模型的输出， 包括答案的准确率、推理过程的格式等。

-   • **CoT 语言一致性奖励：** 为了避免模型在推理过程中出现语言混乱， 还引入了CoT语言一致性奖励，确保推理过程的语言统一。

-   • **RL 的核心：** 这部分训练的核心在于， 通过奖励来引导模型探索和优化推理策略，使得模型的推理能力真正得到质的提升。

这就像一个武林高手，在实战中不断摸索，总结经验，最终形成自己的独特 “招式”， 这部分的训练可以理解成 “自主探索”。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

---

### **四、 Step 3：重构，生成高质量数据（拒绝采样 + CoT 提示）**

当 DeepSeek-R1 的推理能力初步形成后， 它开始 “反哺” 自身， 生成高质量的训练数据。

-   • **拒绝采样 (Rejection Sampling)：** 基于训练好的模型，使用 “推理提示” 生成推理过程， 如果模型生成的输出不符合要求 (例如：推理步骤不正确，或者输出格式错误)， 则会被拒绝采样， 这样保证了训练数据的质量。

-   • **DeepSeek-V3 的判断：** 除了规则筛选， DeepSeek-V3 模型也会对生成的推理数据进行评估，进一步确保数据的质量。

-   • **CoT 提示：** 使用 CoT 提示来生成非推理相关的 SFT 数据，例如写作，对话等，增强模型的泛化能力。

这就像一位美食家，先自己研究美食，然后把自己的菜谱分享出来， 让其他人也能做出美味的佳肴。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

---

### **五、Step 4：最终进化，RL + 人类偏好**

在数据积累之后，DeepSeek-R1 进入了最终的融合阶段。

-   • **SFT 微调：** 使用拒绝采样生成的推理数据，以及使用 CoT 提示生成的非推理数据，对模型进行再次的 SFT 微调。

-   • **RL + 人类偏好：** 使用多样化的训练提示，并引入人类偏好奖励，对模型进行强化学习的微调，这使得模型更加符合人类的价值观。

-   • **人类偏好奖励：** 使用人类偏好模型来评估模型的 helpfulness 和 harmlessness，让模型在推理的同时，也能够考虑到人类的价值观。

-   • **多样化训练：** 引入各种场景下的训练提示，让模型在不同场景下都能表现出色，增强模型的泛化能力。

这就像一位全能运动员，在掌握了基础技能和核心能力之后，还需要参加各种比赛，积累经验，才能达到 “巅峰” 的状态。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

---

### **六、步步为营，成就卓越推理**

DeepSeek-R1 的多阶段训练，并非简单的步骤叠加，而是经过精心设计的 “炼金术”：

-   • **由浅入深：** 从冷启动到 RORL，再到 SFT 和最终的 RL 融合，训练难度逐步提升。

-   • **相互促进：** 每个阶段都为下一个阶段打下基础，相互促进，共同推动模型的发展。

-   • **精心调配：** 每一步都精细化控制，就像炼金术中的配方，每一个环节都至关重要，共同促成了模型的成功。

这就像一位厨师，需要精选食材、精准掌握火候、巧妙搭配调料，才能最终烹制出美味的佳肴。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

DeepSeek-R1 的 “进阶之路” 向我们展示了一个 LLM 如何从 “青涩” 到 “成熟” 的蜕变。多阶段训练， 让 DeepSeek-R1 不仅拥有了强大的推理能力，也更加符合人类的价值观，为 LLM 的发展提供了新的思路。如果你也对 AI 技术感兴趣，请持续关注我们的系列文章，我们将继续为您深入解读 DeepSeek-R1 的奥秘！

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)