# 刚刚，Anthropic 工程师公开了内部数百个 Skill 的打造秘诀

Original J0hn J0hn | AGI Hunt

Anthropic 的工程师 Thariq 发了一篇长文，把 Anthropic 内部使用 Claude Code Skills 的经验倾囊相授。

## 不只是 markdown

Skill 是一个文件夹，里面可以包含脚本、资源文件、数据、配置等，Agent 可以自己去发现、探索和操作这些文件。在 Claude Code 中还支持注册动态 hooks 等配置选项。

## 九大类型

1. **库和 API 参考**——帮助 Claude 正确使用某个库、CLI 工具或 SDK
2. **产品验证**——搭配 Playwright、tmux 等外部工具测试验证代码
3. **数据查询与分析**——连接数据源和监控系统
4. **业务流程自动化**——把重复性工作流浓缩成一条命令
5. **代码脚手架**——为代码库中的特定功能生成框架代码
6. **代码质量与审查**——adversarial-review 启动子 Agent 来挑刺并反复迭代
7. **CI/CD 与部署**——babysit-pr：监控 PR，CI 挂了就重试，有冲突就解决，最后自动合并
8. **事故排查手册**——引导 Claude 走完多工具调查流程输出结构化报告
9. **基础设施运维**——找到孤儿 Pod/Volume → 通知 → 冷静期 → 确认 → 清理

## 怎么写好：九条技巧

**别说废话**——把精力放在能把 Claude 推出默认思维模式的信息上。frontend-design Skill 专门纠正 Claude 的"老毛病"（默认 Inter 字体和紫色渐变）。

**Gotchas 是灵魂**——每次 Claude 踩一次坑，就加一行。这才是 Skill 真正"活"起来的方式。

**用文件夹做信息分层**——SKILL.md 作为中枢只有约 30 行，根据症状指向不同子文件，Claude 按需去读。

**别把 Claude 管太死**——把意图说清楚，把方法交给 Claude。

**首次配置**——配置信息存在 config.json 里，不存在就主动问用户。

**description 是给模型看的**——重点是"什么时候该触发"而不是描述做什么。

**让 Skill 有记忆**——通过存储数据实现记忆，可以简单到追加写入的文本日志。

**给代码，别给指令**——给 Claude 函数库，让它把精力花在"组合"上。

**按需 Hooks**——`/careful` 碰生产环境时激活，拦截危险操作；`/freeze` 锁定特定目录。

## 怎么分享

小团队直接提交到仓库 `.claude/skills/` 下。规模扩大后用内部插件市场。让有用的 Skill 自然浮现——先上 sandbox，Slack 里吆喝，有足够用户后正式搬进市场。

## 核心理念

先写一个，哪怕只有三行。用起来，踩到坑了，加一行。三个月后回头看，你会发现它已经成了团队里最有价值的文档。

---
Source: https://mp.weixin.qq.com/s/UDEYdaTAGV2xVQedSlnA3g
