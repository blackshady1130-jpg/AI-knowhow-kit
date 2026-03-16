---
url: https://x.com/yan5xu/status/2021162107170095186
title: "X 上的 yan5xu：“Agent 工程师，是怎么用 AI 写代码的 ” / X"
published: "2026-02-10T09:59:32.000Z"
captured_at: "2026-03-09T03:40:04.622Z"
---

# X 上的 yan5xu：“Agent 工程师，是怎么用 AI 写代码的 ” / X

## 文章

## 对话

Agent 工程师，是怎么用 AI 写代码的

我的工作是做 AI Agent 研发。日常就是跟 agent 的能力边界打交道 — 它能做什么、不能做什么、怎么让它做得更好。

2024 年 5 月，Claude 3.5 还没出来的时候，我就开始用 GPT-4 + Dify 自己搭 workflow 写代码了。后来从 Cline 到 Claude Code 再到 OpenCode，一路用过来。我几乎不自己手写代码 — 不是用 AI 做补全，而是完全交给 agent 来写。不是写 demo、不是跑 benchmark，是真的用它来写生产代码、改 bug、做重构、提 PR。

从 Dify workflow 到现在的 AI coding agent，用了一年多。我发现最大的坑不是模型不够聪明，而是它记不住事。

做 agent 研发的人都知道，上下文管理是 agent 系统里最核心的问题之一。没有上下文，再强的模型也是无根之木。

AI coding agent 也一样。一个复杂功能做到一半，对话已经很长了。第二天开新会话 — 它什么都不记得。你得重新描述背景、重新解释决策、重新踩一遍昨天已经趟过的坑。

更糟糕的是 compress。大部分工具在上下文快满时会自动"压缩"对话历史。作为做 agent 的人，我太清楚这意味着什么 — 这是不可控的有损压缩。关键的设计决策、踩过的坑、中间推理链条，压缩之后大概率丢失。然后 agent 开始重复犯已经解决过的错误。

这个问题我做 agent 的时候就在解决。现在发现，用 agent 写代码时，同样的问题又出现了。

做 agent 系统时，我们怎么处理这些问题？

-   上下文不够？结构化存储 + 按需加载，关键节点保存状态，下次精确恢复。

-   单个 agent 能力有限？多 agent 协作，主 agent 编排，sub-agent 执行，通过外部存储传递信息。

-   并发冲突？隔离执行环境，每个任务独立空间，互不干扰。

同样的思路，一一对应到 AI coding agent 上：

HANDOFF 替代 compress — 解决上下文丢失。

在上下文还充足的时候，主动让 agent 写一份结构化的交接文档 — 已经完成了什么、正在做什么、下一步做什么、有什么坑要注意。然后开新会话，agent 读取 HANDOFF，直接恢复上下文继续工作。

这不是模糊的"摘要"，而是精确的状态快照。信息密度远高于 compress 后的残留。

如果 compress 已经触发了也不慌 — 回退到压缩之前的状态，执行一次 HANDOFF，再开新会话恢复。几乎不会出现上下文丢失。

一个复杂功能做三天，每天换会话，每次 agent 都能从交接文档里精确恢复到昨天的状态。和人类团队的交接逻辑一模一样。

Sub-Agent 拓展上下文窗口 — 单个 agent 做不完的事，拆给多个做。

单个 agent 的上下文是固定的。所有工作都塞在一个对话里 — 分析代码、写方案、改文件、跑测试 — 上下文很快就满了。

Sub-Agent 的思路是：主 agent 只做规划和决策，具体的重活委托给 sub-agent，结果通过 workspace 文件传回来。主 agent 收到的只是 4 行摘要，但实际完成的工作量可以很大。本质上是用文件系统做信息中转，把单个上下文窗口扩容成了多个。

Worktree 隔离并发 — 多个任务同时进行，互不干扰。

每个任务在独立的 git worktree 中开发。主仓库始终干净，多个 agent 或多个任务可以并行，不会互相污染代码。做完清理 worktree 就行。

这三个方案加在一起：HANDOFF 解决时间轴上的连续性，Sub-Agent 解决单次会话的容量限制，Worktree 解决并发隔离。都是做 agent 系统时的标准思路。

我的项目有多个仓库 — 后端服务、CLI 工具、前端。传统的 AGENTS.md 放在单个 repo 里，agent 只能看到这一个仓库。

但做 agent 的人知道，agent 的能力取决于它能获取到多少信息。如果它不知道其他仓库的存在，不了解前后端的依赖关系，改了一个 API 不会想到调用方也要改。

所以我的工作区结构是这样的：

Agent 的配置在所有代码仓库之上，启动后自动加载全局视图。它知道每个仓库的位置、技术栈、依赖关系和基础设施。这不是 monorepo — 每个 repo 仍然独立，工作区只是给 agent 一个全局的信息入口。

用了这套工作流之后，我发现自己跟 AI 的协作方式已经完全不是"在编辑器里跟 AI 对话"了。

传统模式是：你坐在编辑器前面，跟 AI 一行一行地写代码，实时对话，像结对编程。你是操作者，AI 是工具。

现在变成了：你在 Issue 里写需求和验收标准，agent 从 Board 上捡任务，自己开分支、开发、提 PR。你通过 PR review 审查代码。

这本质上是 tech lead + 开发者的协作模式：

-   你做架构决策、定优先级、review 代码

-   Agent 做具体实现、跑测试、提交 PR

-   通过 Issue 和 PR 沟通，不需要实时盯着

-   多个 agent 可以同时做不同的 Issue，你看 Board 就知道全局进度

-   任何 agent（甚至人类开发者）都可以通过 HANDOFF 接手任何任务

做 agent 的人应该很熟悉这个转变 — 我们做的 agent 系统，本质上也是把人从"执行者"变成"监督者"。现在用 AI 写代码也是一样的路径。

代码审查从"在聊天窗口里看 agent 输出"变成了"在 GitHub PR 界面看 diff、逐行评论、跑 CI"。这是工程团队几十年验证过的流程，比在对话里 review 代码靠谱得多。

很多人用 AI 写代码就是打开编辑器、对话、写代码。但实际工程里，写代码只是很小一部分。一个真正的开发者还需要：跑测试验证、查线上日志定位问题、查数据库确认数据、用 CLI 部署上线。

如果这些能力不给 agent，它就只能写完代码等你验证、等你查日志、等你告诉它线上报了什么错。每一次"等你"都是一次上下文切换，效率大打折扣。

给 agent 自验证的能力。 搭好本地测试环境，让它能跑单元测试、跑 build、跑 lint、自己确认代码是否正确。我的项目里 agent 可以跑 vitest 单测、e2e 测试、Docker 集成测试、甚至启动本地 gateway 做 API 验证 — 不是写完代码就扔给你，而是验证通过了再提交。这一步省掉的来回沟通比你想象的多。

给 agent 获取信息的能力。 这个变化最大。我给 agent 写了一份日志查询手册，告诉它怎么用 aws logs CLI 查 CloudWatch 日志 — 按 Pod 名过滤、按模块过滤、按错误级别过滤。Agent 拿着这份手册，自己查了几百个 Pod 的日志，分析出了十几类生产错误，按优先级分级，还自动配了告警规则。整个过程我只做了 review。

如果没有这个能力，这些工作全得我手动做 — 复制日志贴到对话里，agent 看了再问我更多信息，来回好几轮。有了直接查询的能力，agent 自己定位问题自己修，正确率高很多。当然，权限控制要做好 — 给只读权限，限定可访问的日志组和时间范围。

给 agent 完整的 CLI 工具链。 现在几乎所有云平台都有 CLI — AWS CLI、GCP gcloud、Cloudflare wrangler。Agent 完全可以完成从写代码到部署上线的一条龙操作。我的项目里 agent 日常用 gh 管理 Issue 和 PR、用 aws logs 查日志、用 docker 构建镜像、用 pnpm 跑测试。

这三点的核心思想是一样的：不要把 agent 当成只会写代码的代码生成器，要把它当成一个需要完整工具链的工程师。 你给它的工具越完整，它需要你介入的次数就越少。

Boot Sequence — Agent 自举

每次打开项目，agent 按固定顺序加载配置：工作协议 → 开发流程 → 资源索引 → 任务状态。不需要你手动喂背景信息，agent 自己读文件、自己恢复上下文、自己知道接下来该做什么。

第一次使用时 RESOURCE-MAP.yml 是空的，agent 会主动问你项目情况（几个仓库、什么技术栈、怎么部署），然后自动生成配置。之后每次启动都是全自动的。

Worktree 隔离

具体来说，每个任务通过 git worktree 获得独立的工作目录：

> git worktree add repos/backend-auth -b feature/42-auth main​

不在主仓库上切分支，做完清理 worktree 就行。

Sub-Agent 的文件通信协议

Sub-Agent 之间通过 workspace/ 目录传递信息，每个 sub-agent 只返回 4 行摘要给主 agent：

> 状态：已完成 报告：workspace/1.1-dependency-report.md 产出：1 个文件 决策点：无

主 agent 上下文只多了 4 行，但 sub-agent 实际完成的可能是大量的代码分析。把主 agent 的上下文留给规划和决策，不被执行细节占满。

SCOPE 控制 — 限制 Agent 的写入范围

本地文件模式下，每个任务有一个 SCOPE.yml，白名单指定 agent 可以写哪些文件：

> write: - repos/backend/src/auth/ - repos/backend/src/middleware/ forbidden: - .env

超出范围的文件，agent 不能擅自修改，必须先问你。这是我做 agent 研发养成的习惯 — 给 agent 的权限应该刚好够用，不多不少。

这套工作流从最早的 Dify workflow 时代就开始摸索，到现在迭代了很多版。现在整理成了一个开源协议叫 Code Relay。

就是一组 markdown 和 yaml 文件，不是 CLI，不是 SDK。复制到你的项目里就能用。兼容 Cline、Claude Code、OpenCode、Windsurf 等所有主流工具。

两种模式：

-   GitHub 模式 — 任务管理在 Issue + Project Board 上，适合已经用 GitHub 的团队

-   本地文件模式 — 不依赖任何平台，适合离线工作或不想绑定特定平台

两种模式都支持 HANDOFF、SCOPE、Sub-Agent、Worktree 等全部核心能力，区别只是任务状态存在哪里。

如果你也在认真用 AI coding agent 做项目，欢迎试试。有问题直接提 Issue。

GitHub: