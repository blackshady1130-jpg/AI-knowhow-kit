---
url: https://bytedance.feishu.cn/docx/KFXFdEikzoWNJDxFXIycmWOgnpd
title: "精华笔记：微软 Build 2023 开发者大会专题演讲：State of GPT（GPT 的现状）​"
captured_at: "2026-03-08T10:53:43.606Z"
---

# 精华笔记：微软 Build 2023 开发者大会专题演讲：State of GPT（GPT 的现状）​

[

飞书云文档

](https://www.feishu.cn/)

ByteDance

精华笔记：微软 Build 2023 开发者大会专题演讲：State of GPT（GPT 的现状）

最新修改时间为11月02日

-   [精华笔记：微软 Build 2023 开发者大会专题演讲：State of GPT（GPT 的现状）](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#KFXFdEikzoWNJDxFXIycmWOgnpd)
-   [B 站观看](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#OAXudAj1toZbBgxYAVUcSirjncg)
-   [PPT 下载](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnFgQl4EWSaWK8cEZKWlGYgh)
-   [写在前面](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#IfbPdHzTQo0qbSxF4OFccwmjneh)
-   [如何训练 GPT 助手](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcn9nU62u03sb8UFidyDP2LGc)
-   [01 预训练](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnxssMwqin7flXSaKCpPgvNe)
-   [数据收集](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnSlAj7BTPDrRooHWgCleaTm)
-   [标记化（tokenization）](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnAwYoHiDo83sntBGMFbkiXm)
-   [输入 Transformer](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnWtzG4We9ddW3BV8js2Au1c)
-   [预测序列中的下一个标记](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcn5fFcX0uMx1felCkHtQQTem)
-   [重复以上预训练过程](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcne1qXlwqgc9VD0NXVq26huf)
-   [在小型监督数据集上微调模型](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnRl60kb2OJ9PewR3TStmfKd)
-   [提示模型以引导其完成任务](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnbRUkSC6DNJaKJmcISXe4tb)
-   [02 监督微调](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnOOvCLlTmKaZNR6leinTped)
-   [03 奖励建模](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnOgHT94m7ssdUmwxzzoU3Hh)
-   [04 强化学习](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcn9tqLWHjHl9FS7b56GxUcNd)
-   [如何有效应用 GPT 助手](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcng6esVimoU34DeNNqllAyUf)
-   [认知差异](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnbIHJqgYW3VdQLedgycVhOc)
-   [善用提示](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnJ8xxUuD50sx9LUPh3c1QSe)
-   [自我一致性](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcn3Q09aw49MPl8OljCSA1VEb)
-   [LLM 怪癖：不保证成功](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnv5Ejm54hpBIPK3tc5N3DTh)
-   [确保能获得正确答案](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnmg7hxUzlwNcSvGxP8FwN0f)
-   [合理的智商设定](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcn8uAIOCpYB0niNF1jE8Ukjg)
-   [在计算上依赖工具](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnORTJM4xBPzzhLofBwSd3ue)
-   [明确模型的知识边界](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnReIPybW6HOXql0UVTCbapd)
-   [检索增强模型](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcntNds5Klc9mCCpPZGS7JKrh)
-   [将任务相关信息加载到工作内存](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnXU8bK7mPjT4hk7lDQMWwhb)
-   [获取相关文档，进行向量转换并查询](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnk3ECN4aGydVtvKB6C6pomd)
-   [约束提示](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnF9YgAXFmxmqyW0Zj5U6b3c)
-   [微调](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnKE1jo4llND7T3GCFHZhYac)
-   [模型的限制](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnmTsLWhjITF4moP76WrT9Am)
-   [延 伸 阅 读](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnktbMuG6pAobBZiq0lY0kNf)
-   [（ 理 论 部 分 ） 省 流 ： 吴 恩 达 联 合 O p e n A I 制 作 的 《 面 向 开 发 者 的 C h a t G P T 提 示 工 程 》 图 文 版 笔 记](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnsFjS79uPojY5jc6EarSZug)
-   [（ 实 践 部 分 ） 省 流 ： 吴 恩 达 联 合 O p e n A I 制 作 的 《 面 向 开 发 者 的 C h a t G P T 提 示 工 程 》 图 文 版 笔 记](https://bytedance.sg.larkoffice.com/docx/KFXFdEikzoWNJDxFXIycmWOgnpd#doxcnRTf2Ej9c4L9IFvMekvLw3g)

2023年11月2日修改

🔗 原文链接： [https://mp.weixin.qq.com/s/tlQF5W75...](https://mp.weixin.qq.com/s/tlQF5W75NIMPqMW9vCsD1A)​

⏰ 剪存时间：2023-06-28 18:21:39 （UTC+8）​

✂️ 本文档由 [飞书剪存](https://www.feishu.cn/hc/zh-CN/articles/606278856233?from=in_ccm_clip_doc) 一键生成​

​

https://www.youtube.com/watch?v=YrBJiy-V8MY

​

B 站观看​

​

​

PPT 下载​

​

stateofgpt.pdf

​

评论（13）

跳转至首条评论

0 字

-   帮助中心

-   效率指南