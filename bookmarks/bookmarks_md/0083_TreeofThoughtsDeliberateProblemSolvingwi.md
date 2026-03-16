---
url: https://www.aminer.cn/pub/6466fafbd68f896efaeb751d/tree-of-thoughts-deliberate-problem-solving-with-large-language-models
title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models."
description: "AMiner是基于智谱 GLM模型的AI科研助手，收录全球3亿+文献数据、6000万学者。支持学术搜索、关键词搜索、深度调研、AI阅读、AI文库学术问答等。辅助完成包含真实引文的文献综述、开题报告等深度调研报告，更能使用AI高效理解论文等，提升科学研究效率。"
author: "北京智谱华章科技有限公司"
captured_at: "2026-03-08T10:25:04.778Z"
---

# Tree of Thoughts: Deliberate Problem Solving with Large Language Models.

## Tree of Thoughts: Deliberate Problem Solving with Large Language Models.

[Conference on Neural Information Processing Systems (NeurIPS)（2023）](https://www.aminer.cn/open/journal/detail/5ea1e340edb6e7d53c011a4c)CCF A

Princeton University

引用 **4808**|浏览3621

摘要

Language models are increasingly being deployed for general problem solving across a wide range of tasks, but are still confined to token-level, left-to-right decision-making processes during inference. This means they can fall short in tasks that require exploration, strategic lookahead, or where initial decisions play a pivotal role. To surmount these challenges, we introduce a new framework for language model inference, Tree of Thoughts (ToT), which generalizes over the popular Chain of Thought approach to prompting language models, and enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving. ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action, as well as looking ahead or backtracking when necessary to make global choices. Our experiments show that ToT significantly enhances language models' problem-solving abilities on three novel tasks requiring non-trivial planning or search: Game of 24, Creative Writing, and Mini Crosswords. For instance, in Game of 24, while GPT-4 with chain-of-thought prompting only solved 4% of tasks, our method achieved a success rate of 74%. Code repo with all prompts: https://github.com/princeton-nlp/tree-of-thought-llm.

更多

查看译文

关键词

large language model,general problem solving,heuristic search,reasoning,planning,decision making

PDF

![](https://cdn.aminer.cn/assets/network.png)![](https://cdn.aminer.cn/assets/network-active.png)原文链接![](https://cdn.aminer.cn/assets/xiala-1.png)![](https://cdn.aminer.cn/assets/xiala-active.png)

![](https://cdn.aminer.cn/assets/share-1.png)![](https://cdn.aminer.cn/assets/share-active.png)分享

![](https://cdn.aminer.cn/assets/yinyong.png)![](https://cdn.aminer.cn/assets/yinyong-active.png)引用

加入学术空间

AI 理解论文

视频&图片

暂无数据

立即登录，查看剩余内容

论文作者介绍

-   本文作者包括姚顺雨（OpenAI），研究方向为决策制定、推理、自然语言处理、语言模型；Dian Yu（Google Brain），研究方向为语言属性表示、语言模型、口语对话系统、依赖解析；Jeffrey Zhao（Google Deepmind），研究方向为启发式搜索、决策制定、大型语言模型、规划、推理；Izhak Shafran（Google），研究方向为推理、决策制定、语言模型、命名实体识别、面向任务的系统；Tom Griffiths（普林斯顿大学计算认知科学实验室），研究方向为主题模型、语言模型、表征学习、元学习、社会学习；以及Yuan Cao（Google），研究方向为语言模型、面向任务、决策制定、推理、语言建模；Karthik Narasimhan（普林斯顿大学计算机科学系），研究方向为话题模型、语言模型、语言理解、强化学习、推理。

文献大纲

-   **摘要**

    -   语言模型在解决各种任务方面越来越普遍，但推理过程中仍然局限于标记级别的、从左到右的决策过程。
    -   为了克服这些挑战，本文介绍了“思维树”(ToT)框架，它推广了流行的“思维链”方法，并允许对作为问题解决中间步骤的连贯文本单元(“思维”)进行探索。
    -   ToT 允许语言模型通过考虑多个不同的推理路径、自我评估选择以决定下一步行动，以及在必要时向前看或回溯以做出全局选择来进行深思熟虑的决策。
    -   实验表明，ToT 显著提高了语言模型在三个需要非平凡规划或搜索的新任务上的问题解决能力：24点游戏、创意写作和迷你填字游戏。

    **1\. 引言**

    -   语言模型在解决各种任务方面越来越普遍，但推理过程中仍然局限于标记级别的、从左到右的决策过程。
    -   本文介绍了“思维树”(ToT)框架，它推广了流行的“思维链”方法，并允许对作为问题解决中间步骤的连贯文本单元(“思维”)进行探索。
    -   ToT 允许语言模型通过考虑多个不同的推理路径、自我评估选择以决定下一步行动，以及在必要时向前看或回溯以做出全局选择来进行深思熟虑的决策。

    **2\. 背景**

    -   本文首先形式化了一些现有的使用大型语言模型进行问题解决的方法，这些方法启发了本文的方法，并在后面进行比较。
    -   本文使用了 p θ 来表示具有参数 θ 的预训练语言模型，并使用小写字母 x, y, z, s, … 来表示语言序列。
    -   输入-输出 (IO) 提示是最常见的将问题输入 x 转换为输出 y 的方法。
    -   思维链 (CoT) 提示被提出来解决输入 x 到输出 y 的映射非平凡的情况。
    -   自洽思维链 (CoT-SC) 是一种集成方法，它采样 k 个独立的思维链，然后返回最频繁的输出。

    **3\. 思维树：使用语言模型进行深思熟虑的问题解决**

    -   本文介绍了思维树 (ToT) 框架，它允许语言模型在思维上探索多个推理路径。
    -   ToT 将任何问题都视为对树的搜索，其中每个节点代表一个状态 s = \[x, z 1•••i \]，表示具有输入和到目前为止的序列的中间解决方案。
    -   ToT 框架涉及回答四个问题：
        -   如何将中间过程分解为思维步骤；
        -   如何从每个状态生成潜在的思维；
        -   如何启发式地评估状态；
        -   使用什么搜索算法。

    **4\. 实验**

    -   本文提出了三个任务，即使从最先进的语言模型 GPT-4 中采样，使用标准的 IO 提示或思维链 (CoT) 提示也很难解决。
    -   本文展示了在思维树 (ToT) 中的深思熟虑搜索如何产生更好的结果，更重要的是，展示了使用语言模型解决需要搜索或规划的问题的新颖而有前途的方法。

    **5\. 相关工作**

    -   本文将 ToT 与其他相关工作进行比较，包括规划与决策、自我反思、程序引导的语言模型生成和经典搜索方法。

    **6\. 讨论**

    -   本文讨论了 ToT 的局限性以及未来的研究方向，包括成本和效率问题。

    **结论**

    -   本文介绍了“思维树”(ToT)框架，它允许语言模型在思维上探索多个推理路径，从而进行深思熟虑的决策。
    -   ToT 框架为将经典问题解决见解转化为当代语言模型的可操作方法提供了一种方式。
    -   本文将语言模型与经典人工智能方法的交集视为一个令人兴奋的研究方向。

关键问题

-   ### Q：论文具体用了哪些研究方法？

    -   **Tree of Thoughts (ToT) 框架**: 该框架将问题解决过程视为对一系列“思想”的搜索，每个“思想”都是通向解决方案的中间步骤。ToT 框架包括以下关键组件：
        -   **思想分解**: 将问题解决过程分解为多个“思想”步骤，每个步骤都代表一个中间解决方案。
        -   **思想生成器**: 从当前状态生成多个候选“思想”。
        -   **状态评估器**: 评估每个候选“思想”对解决问题进展的贡献，并作为搜索算法的启发式函数。
        -   **搜索算法**: 使用 BFS 或 DFS 等搜索算法在“思想”树中进行探索，并根据启发式函数选择最有前景的路径。
    -   **实验**: 论文设计了三个新的任务来评估 ToT 框架的有效性：
        -   **24 点游戏**: 使用 4 个数字和基本运算符得到 24。
        -   **创意写作**: 根据给定的 4 个句子生成一个连贯的段落。
        -   **迷你填字游戏**: 根据水平和垂直线索填写 5x5 的字母网格。
    -   **基线方法**: 将 ToT 与以下基线方法进行比较：
        -   **输入-输出 (IO) 提示**: 直接提示模型生成最终答案。
        -   **思维链 (CoT) 提示**: 引入一系列中间步骤来连接输入和输出。
        -   **CoT 自洽性**: 对多个 CoT 样本进行投票以获得最终答案。
        -   **迭代细化**: 在 IO 样本的基础上进行迭代改进。

    ### Q：主要的研究发现和成果是什么？

    -   **ToT 框架显著提高了语言模型在需要推理、规划或搜索的任务上的问题解决能力**。 在 24 点游戏、创意写作和迷你填字游戏中，ToT 的表现都优于基线方法。
    -   **ToT 框架具有通用性、模块化、适应性和便捷性等优点**。 它可以应用于各种问题，并可以根据不同的任务和模型进行调整。
    -   **ToT 框架为语言模型在问题解决中的应用开辟了新的方向**。 它将经典的问题解决方法与语言模型的能力相结合，为解决更复杂的问题提供了新的思路。

    ### Q：这项研究目前有哪些局限性？

    -   **ToT 框架需要更多的计算资源**。 与 IO 或 CoT 提示相比，ToT 需要生成更多的标记才能达到相同的性能。
    -   **ToT 框架的效率还有待提高**。 例如，BFS 可以在找到解决方案时提前停止，或者减少搜索宽度以避免不必要的探索。
    -   **ToT 框架目前只适用于需要推理、规划或搜索的任务**。 对于一些简单的任务，IO 或 CoT 提示可能就足够了。
    -   **ToT 框架的长期成本效益还有待观察**。 随着 LLM 的开源和效率的提高，ToT 的成本可能会降低。

溯源树

核心引用论文

样例

![](https://originalfileserver.aminer.cn/sys/aminer/pubs/mrt_preview.jpeg)

生成溯源树，研究论文发展脉络

相关论文

[Evaluating Language Models for Mathematics Through Interactions](https://www.aminer.cn/pub/647d5ee0d68f896efa5969c7)

[Katherine M Collins](https://www.aminer.cn/profile/katherine-m-collins/63732205ec88d95668d53bd1),[Albert Q Jiang](https://www.aminer.cn/profile/albert-q-jiang/66987c570fe1e120f8dce20e),[Simon Frieder](https://www.aminer.cn/profile/simon-frieder/65d4e914c136ef13318b304b),[Lionel Wong](https://www.aminer.cn/profile/lionel-wong/658fdd69b2e21a410ea7922d),[Miri Zilka](https://www.aminer.cn/profile/miri-zilka/561d7afd45ce1e596480ddb3),[Umang Bhatt](https://www.aminer.cn/profile/umang-bhatt/5628b44445ce1e596600e0eb),[Thomas Lukasiewicz](https://www.aminer.cn/profile/thomas-lukasiewicz/53f4392fdabfaee0d9b7f91b),[Yuhuai Wu](https://www.aminer.cn/profile/yuhuai-wu/6565b3affbb0f21d747255ed),[Joshua B Tenenbaum](https://www.aminer.cn/profile/joshua-b-tenenbaum/53f66220dabfae6a71b63777),[William Hart](https://www.aminer.cn/profile/william-hart/53f459fadabfaedf43619148),[Timothy Gowers](https://www.aminer.cn/profile/timothy-gowers/560aa2c245cedb33971592ce),[Wenda Li](https://www.aminer.cn/profile/wenda-li/542b9f93dabfae200660320f),

 Proceedings of the National Academy of Sciences of the United States of America 2024 49

[Exploring the MIT Mathematics and EECS Curriculum Using Large Language Models](https://www.aminer.cn/pub/648bde84d68f896efaf826f2)

[Sarah J. Zhang](https://www.aminer.cn/profile/sarah-j-zhang/6542deb950dee4c4228f14e6),[Samuel Florin](https://www.aminer.cn/profile/samuel-florin/652670c255b3f8ac465b40ca),[Ariel N. Lee](https://www.aminer.cn/profile/ariel-n-lee/65edd6d30b6735f4855eda8f),[Eamon Niknafs](https://www.aminer.cn/profile/eamon-niknafs/652670c255b3f8ac465b40cb), Andrei Marginean, Annie Wang,[Keith Tyser](https://www.aminer.cn/profile/keith-tyser/64972c53a88fbe7c0500360e),[Zad Chin](https://www.aminer.cn/profile/zad-chin/6455925be0a3f070aeb4e9db),[Yann Hicke](https://www.aminer.cn/profile/yann-hicke/64973301a88fbe7c0500fd1f),[Nikhil Singh](https://www.aminer.cn/profile/nikhil-singh/53f80f76dabfae8faa4d737e),[Madeleine Udell](https://www.aminer.cn/profile/madeleine-udell/5d415bfa7390bff0db70b822),[Yoon Kim](https://www.aminer.cn/profile/yoon-kim/562c7bf145cedb3398c374d8),

 CoRR 2023 35

[When Large Language Models Meet Personalization: Perspectives of Challenges and Opportunities.](https://www.aminer.cn/pub/64c88ca43fda6d7f0626899d)

[Jin Chen](https://www.aminer.cn/profile/jin-chen/5613726545cedb33979c6c38),[Zheng Liu](https://www.aminer.cn/profile/zheng-liu/560f0d8045cedb33976ec606),[Xu Huang](https://www.aminer.cn/profile/xu-huang/645afe25c81747b42a805d3c),[Chenwang Wu](https://www.aminer.cn/profile/chenwang-wu/6177597e60a9653f448f03e4),[Qi Liu](https://www.aminer.cn/profile/qi-liu/6162c2f260a9657b486ca558),[Gangwei Jiang](https://www.aminer.cn/profile/gangwei-jiang/657a70370421653145a64a0b),[Yuanhao Pu](https://www.aminer.cn/profile/yuanhao-pu/6682194b21f6f4c2c114b828),[Yuxuan Lei](https://www.aminer.cn/profile/yuxuan-lei/663f57cca05b27f854d0c0c9),[Xiaolong Chen](https://www.aminer.cn/profile/xiaolong-chen/655c95b633d15b6ea6a82076),[Xingmei Wang](https://www.aminer.cn/profile/xingmei-wang/6546056550dee4c422967d87),[Kai Zheng](https://www.aminer.cn/profile/kai-zheng/560a6dbc45ce1e595fc920a3),[Defu Lian](https://www.aminer.cn/profile/defu-lian/53f42e2edabfaee43ebcf21c),

 World Wide Web 2024 415

[Knowledge Graph Prompting for Multi-Document Question Answering.](https://www.aminer.cn/pub/64e6d5a53fda6d7f0652a3cc)

 THIRTY-EIGHTH AAAI CONFERENCE ON ARTIFICIAL INTELLIGENCE, VOL 38 NO 17 2024 262

[RecMind: Large Language Model Powered Agent for Recommendation.](https://www.aminer.cn/pub/64ed716d3fda6d7f0658aa62)

 FINDINGS OF THE ASSOCIATION FOR COMPUTATIONAL LINGUISTICS NAACL 2024 2024 146

[ITINERA: Integrating Spatial Optimization with Large Language Models for Open-domain Urban Itinerary Planning](https://www.aminer.cn/pub/65cad48c939a5f4082f32c7a)

[Yihong Tang](https://www.aminer.cn/profile/yihong-tang/562ca73645cedb3398c87343), Zhaokai Wang,[Ao Qu](https://www.aminer.cn/profile/ao-qu/65dca38a671a2719988080db), Yihao Yan, Zhaofeng Wu,[Dingyi Zhuang](https://www.aminer.cn/profile/dingyi-zhuang/561bd06245cedb3397f69aae), Jushi Kai, Kebing Hou,[Xiaotong Guo](https://www.aminer.cn/profile/xiaotong-guo/637271e8ec88d95668ce0f32),[Jinhua Zhao](https://www.aminer.cn/profile/jinhua-zhao/560c12b145cedb339747ec55),[Zhan Zhao](https://www.aminer.cn/profile/zhan-zhao/61b2deaf6750f8276edd3bb4),[Wei Ma](https://www.aminer.cn/profile/wei-ma/5448731ddabfae1e0412ccd5)

 EMNLP 2024 2024 26

[SportQA: A Benchmark for Sports Understanding in Large Language Models.](https://www.aminer.cn/pub/65dd4f8013fb2c6cf66f9e71)

 PROCEEDINGS OF THE 2024 CONFERENCE OF THE NORTH AMERICAN CHAPTER OF THE ASSOCIATION FOR COMPUTATIONAL LINGUISTICS HUMAN LANGUAGE TECHNOLOGIES, VOL 1 LONG PAPERS 2024 14

[Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key?](https://www.aminer.cn/pub/65dff38113fb2c6cf62d93f0)

 PROCEEDINGS OF THE 62ND ANNUAL MEETING OF THE ASSOCIATION FOR COMPUTATIONAL LINGUISTICS, VOL 1 LONG PAPERS 2024 127

数据免责声明

页面数据均来自互联网公开来源、合作出版商和通过AI技术自动分析结果，我们不对页面数据的有效性、准确性、正确性、可靠性、完整性和及时性做出任何承诺和保证。若有疑问，可以通过电子邮件方式联系我们：[report@aminer.cn](mailto:report@aminer.cn)

![banner](https://cdn.aminer.cn/assets/pub_detail_banner.png)

AI 解读

一键生成论文网页