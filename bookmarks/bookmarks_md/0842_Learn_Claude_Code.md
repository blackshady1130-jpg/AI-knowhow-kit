Title: Learn Claude Code

URL Source: https://learn.shareai.run/zh/

Markdown Content:
19 章节、4 个阶段，从最小闭环一路搭到多 Agent 平台与外部能力总线

核心闭环

*   [s01 Agent 循环 真正的 agent 起点，是把真实工具结果重新喂回模型，而不只是输出一段文本。](https://learn.shareai.run/zh/s01/)
*   [s02 工具使用 主循环本身不用变复杂；工具能力靠一层清晰的路由面增长。](https://learn.shareai.run/zh/s02/)
*   [s03 待办写入 对多步骤任务来说，可见计划不是装饰，而是防止会话漂移的稳定器。](https://learn.shareai.run/zh/s03/)
*   [s04 子代理 把探索性工作移进干净上下文后，父 agent 才能持续盯住主目标。](https://learn.shareai.run/zh/s04/)
*   [s05 技能系统 专门知识不该一开始全部塞进上下文，而该在需要时被轻量发现、按需展开。](https://learn.shareai.run/zh/s05/)
*   [s06 上下文压缩 压缩的目标不是删历史，而是保住连续性和下一步所需的工作记忆。](https://learn.shareai.run/zh/s06/)

系统加固

*   [s07 权限系统 模型产生的执行意图，必须先通过清晰的权限门，再变成真正动作。](https://learn.shareai.run/zh/s07/)
*   [s08 Hook 系统 Hook 让系统围绕主循环生长，而不是不断重写主循环本身。](https://learn.shareai.run/zh/s08/)
*   [s09 记忆系统 只有跨会话、无法从当前工作重新推导的知识，才值得进入 memory。](https://learn.shareai.run/zh/s09/)
*   [s10 系统提示词 模型看到的不是一坨固定 prompt，而是一条按阶段拼装的输入流水线。](https://learn.shareai.run/zh/s10/)
*   [s11 错误恢复 系统必须清楚自己此刻是在继续、重试，还是处于恢复流程。](https://learn.shareai.run/zh/s11/)

任务运行时

*   [s12 任务系统 Todo 适合会话内规划，持久任务图才负责跨步骤、跨阶段协调工作。](https://learn.shareai.run/zh/s12/)
*   [s13 后台任务 持久任务描述要完成什么，运行槽位描述谁在跑、跑到哪里；两者相关但不是一回事。](https://learn.shareai.run/zh/s13/)
*   [s14 定时调度 当任务能后台运行以后，时间本身也会变成另一种启动入口。](https://learn.shareai.run/zh/s14/)

多 Agent 平台

*   [s15 Agent 团队 系统一旦长期运行，就需要有名字、有身份、可持续存在的队友，而不只是一次性子任务。](https://learn.shareai.run/zh/s15/)
*   [s16 团队协议 团队只有在协作遵守共同消息模式时，才会变得可理解、可调试、可扩展。](https://learn.shareai.run/zh/s16/)
*   [s17 自主代理 自主性开始于：队友能安全找到可做的事、认领它，并带着正确身份继续执行。](https://learn.shareai.run/zh/s17/)
*   [s18 Worktree 隔离 task 管目标，worktree 管隔离执行车道和收尾状态；两者不能混成一个概念。](https://learn.shareai.run/zh/s18/)
*   [s19 MCP 与插件 外部能力系统不该是外挂；它们应和原生工具一起处在同一控制面上。](https://learn.shareai.run/zh/s19/)
