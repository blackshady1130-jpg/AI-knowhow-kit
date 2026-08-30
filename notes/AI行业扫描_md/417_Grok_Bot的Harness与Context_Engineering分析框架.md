# Grok Bot 的Harness 与 Context Engineering 的变化、常识与分析框架

> 日期：2026-08-29  
> 研究对象：Grok Bot 0.18.0 的非官方重建及两篇分析文章、Manus 2025 年上下文工程文章，以及 2026 年 Cursor、Claude Code、Agent Skills 等公开资料  
## 先说结论

1. **Harness 没有简单地变厚或变薄，复杂度换了位置。** 强模型减少了底层的提示词扶手、硬编码流程和细碎防呆；工具发现、上下文管理、权限、恢复、按模型适配、线上评测和多 Agent 协调反而更重要。过去的重点是“怎么让模型按步骤做”，现在更像“怎样经营一个可观察、可恢复、可持续改进的运行系统”。

2. **Manus 2025 年提出的原则大多没有过时，2026 年把它们做成了系统能力。** 稳定前缀、把大结果放到文件、在长任务中重述目标、保留失败线索，这些仍然有效。变化在于：工具和知识开始分层加载；缓存命中率被当作运行指标；Harness 会针对不同模型版本单独调节；线上轨迹直接进入评测、错误修复和 Skill 更新。

3. **要把可用、被发现、被调用、调用成功、任务成功分开。** 工具或 Skill 没有使用，可能因为没开放、没被检索到、模型判断不该用、模型漏用了，也可能因为用户任务根本不需要。没有这几层状态，无法判断应当改模型、改 Harness、改工具描述，还是删掉无效能力。

5. **成本优化最终要看“每个成功任务的总成本”。** Token 价格只是一部分；缓存、重复调用、工具延时、错误后的重试、无效规划、用户纠正和人工接管都会改变真实成本。同样地，少用 Token 不一定更好：少给了一段关键上下文，可能换来更多重试和更差结果。

## 一、2025 到 2026：Harness 到底发生了什么

### 1. 2025 年的 Manus：核心问题是上下文纪律

Manus 的文章把 Agent 的工程难点说得很朴素：模型每走一步，都要重新读一遍此前的上下文。前面的系统提示、工具定义和历史轨迹既耗钱，又影响速度和判断。它提出了六个很耐用的做法：

- 保持前缀稳定，尽量让缓存重复利用；
- 工具定义尽量固定，用约束控制当前允许调用的工具；
- 把文件系统当作外部记忆，大结果不必全部塞回对话；
- 长任务中不断重述待办和目标；
- 保留失败结果，给模型留下“刚才为什么不行”的证据；
- 避免上下文过度重复，让模型陷入机械模仿。

这些做法来自 Manus 的生产经验，适用范围要结合具体架构判断。原文也明确说，它们是从自身架构中总结出来的做法。[Manus 原文](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

> **工程批注｜什么是“稳定前缀”**  
> 多轮调用时，系统提示、工具定义、规则和较早的历史通常位于输入开头。只要这一段逐字稳定，服务端就更容易复用已计算的缓存；如果每轮都改日期、调整工具顺序或重写系统提示，前缀会被打断。它既影响费用，也影响首个 Token 的等待时间。

### 2. Grok Bot 的变化：把“知识”和“能力”拆开

两篇 Grok Bot 分析最值得追的是下面两层。12KB 阈值和九个动态提示只属于该重建版本的实现细节：

- **Skill / 知识层**：告诉模型“这类工作应该怎么做”，内容通常是可按需加载的 Markdown、脚本和参考资料；
- **Tool / MCP / 能力层**：告诉模型“当前允许调用什么”，由工具 Schema、权限和执行器控制。

在这份重建里，大部分核心工具固定提供；规模大、低频使用的 MCP 工具先只露出简短索引，模型需要时再通过 `GetMcpTools` 获取详细定义，然后由 `CallMcpTool` 执行。较大的定义结果会落到文件，模型必须读过定义后才能调用。这样既不用频繁改动传给模型的工具清单，也能把低频内容延迟到使用时再加载。

这与 Manus 的“全部工具固定存在，再在解码阶段屏蔽当前不允许的调用”做法不同，但要解决的经济问题一致：**保持可缓存部分稳定，同时别让模型每一步都背着全部工具细节。** [Grok 动态工具文章](https://yage.ai/share/grok-bot-dynamic-tools-20260827.html)；[上下文工程文章](https://yage.ai/share/grok-bot-context-engineering-20260827.html)

> **工程批注｜Skill、Tool、MCP 不宜混着统计**  
> MCP 是连接外部能力的协议和接口；Tool 是模型可调用的动作；Skill 更像操作手册。一个 Skill 可以教模型如何组合搜索、文件和代码工具，但它本身未必新增任何执行权限。分析日志时，Skill 应看“是否加载、是否遵循”，MCP/Tool 应看“是否发现、是否获权、是否调用、是否成功”。

### 3. 2026 年的新主线：从上下文技巧变成运行系统

Grok 的非官方重建、Cursor 和 Claude Code 的公开经验出现了很强的共识：

| 变化 | 2025 年常见做法 | 2026 年更明显的做法 | 对百炼分析的含义 |
|---|---|---|---|
| 给模型信息 | 系统提示和工具一次性铺开 | 目录常驻，详细定义和 Skill 按需加载 | 既要记录“可用集合”，也要记录“本轮实际暴露集合” |
| 约束模型 | 靠规则、固定步骤、工具屏蔽 | 更强模型自己找上下文，Harness 只保留关键边界 | 同一种 Harness 不应默认适合所有模型版本 |
| 管理缓存 | 写提示词时顺便注意 | 系统提示顺序、工具顺序、压缩和分叉都围绕缓存设计 | 需要 prompt/tool hash、缓存读写 Token 和命中率 |
| 管理错误 | 把错误留在历史里 | 区分预期错误与未知错误，结构化保留，避免错误堆积造成上下文污染 | 要记录原因、首次发生点、恢复动作和最终结果 |
| 改进系统 | 离线看几个案例 | 离线基准 + 线上 A/B + 逐工具/逐模型基线 | 日志模型要支持 Harness 版本和实验桶对比 |
| 扩展能力 | 不断增加原生工具 | MCP、Skill、子 Agent 和插件化运行时 | 能力数量增长后，检索质量和协调成本成为新瓶颈 |

Cursor 在 2026 年公开表示，随着模型增强，他们删掉了不少早期防护和静态上下文，让模型自行获取需要的信息；与此同时，他们加重了逐模型 Harness 调节、线上 A/B、工具错误基线、Token/延时/缓存命中和用户满意度观测。[Cursor：Continually improving the agent harness](https://cursor.com/blog/continually-improving-agent-harness)

Claude Code 的公开经验则把 Prompt Cache 直接当成架构约束：稳定内容放前面，动态信息以新消息追加；不要每轮增删工具或改变顺序；模式切换通过状态和工具表达；对话压缩和子会话分叉也要保住可复用前缀。[Anthropic：Prompt caching is everything](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything)

Agent Skills 的开放规范也说明，Skill 已经从“一段超长提示词”变成分级暴露的资料包：先展示名称和说明，需要时再加载完整 `SKILL.md`，执行时才读取脚本、参考资料和资源文件。[Agent Skills 规范](https://agentskills.io/home)

### 4. “Harness 变薄”只说对了一半

可以把复杂度迁移理解成两层：

- **靠近模型的一层变薄了**：更少的逐步指挥、更少的重复说明、更少用脆弱的固定流程代替模型判断；
- **靠近系统的一层变厚了**：上下文选择、工具发现、权限、状态、恢复、缓存、观测、评测、模型路由和多 Agent 协调都要有人负责。

所以，“模型更强，Harness 会消失”并不成立。更准确的说法是：**补偿模型能力不足的 Harness 在收缩，经营生产运行的 Harness 在扩张。** DeepSeek Harness 的“Everything is a Plugin”可以看作这种趋势的激进实验，但项目仍标注为 Developer Preview，尚不足以证明插件化会成为唯一答案。[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)

## 二、什么没有变：六条应长期保留的工程常识

### 1. 上下文窗口再大，也需要选择

长上下文降低了“放不下”的压力，没有消除注意力分散、输入费用和延时。真正的问题一直是：当前一步需要哪些事实，哪些只需可取回，哪些应当压缩，哪些应该彻底退出活跃上下文。

### 2. 状态要能外置，压缩要能恢复

文件、计划、工具结果、用户偏好和任务进度不能只存在于模型“脑内”。压缩后的摘要需要能指回原始证据；任务恢复时，也要知道压缩发生在哪一轮、哪些状态仍然有效。Grok 重建中按 `compactionEpoch` 冻结记忆快照，是为了保证一个压缩周期里的记忆渲染一致。

### 3. 工具空间需要被组织

工具少时，可以一次性列出来；工具和 MCP 多到一定程度后，就要有目录、检索、分组和权限边界。Manus 的屏蔽、Grok 的元工具、Claude Code 的延迟加载，都是在控制“模型此刻面对多少可能动作”。实现可以变，动作空间不能失控。

### 4. 错误既是证据，也可能成为噪声

Manus 强调保留错误，让模型学会适应；Cursor 发现工具错误堆积会造成 context rot。这两点并不矛盾。更稳妥的原则是：

- 保留能解释失败、支持恢复的错误类型、关键参数和处置结果；
- 同一错误反复出现时压缩重复正文；
- 大段日志、网页或堆栈外置，活跃上下文只放摘要和引用；
- 恢复成功后留下结论，不必永远携带全部失败细节。

### 5. 模型和 Harness 必须成对评价

相同模型换了工具格式、系统提示、超时、并行策略或压缩方法，效果会不同；同一 Harness 换模型后，工具错误、计划习惯和缓存行为也会变化。所有分析至少要带上 `model_version × harness_version × task_type`，否则很容易把 Harness 的问题归给模型，或反过来。

### 6. 没有结果验证，过程指标会失真

工具调用多可能代表能力丰富，也可能代表在打转；规划文字长可能很认真，也可能没有帮助；低 Token 可能是高效，也可能是遗漏了关键上下文。最终需要某种结果信号：代码测试、文件是否生成、任务是否完成、用户是否接受、是否重新修改、是否人工接管。

## 参考资料

- [Grok Bot 泄露：Cursor 为什么只给模型一部分工具的完整定义](https://yage.ai/share/grok-bot-dynamic-tools-20260827.html)
- [Grok Bot 泄露代码里的 Context Engineering](https://yage.ai/share/grok-bot-context-engineering-20260827.html)
- [Manus：Context Engineering for AI Agents](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Cursor：Continually improving the agent harness](https://cursor.com/blog/continually-improving-agent-harness)
- [Anthropic：Lessons from building Claude Code—Prompt caching is everything](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything)
- [Agent Skills 规范](https://agentskills.io/home)
- [Grok Bot 0.18.0 非官方重建](https://github.com/b-nnett/grok-bot-0.18-reconstructed)
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)
- [SkillsBench](https://arxiv.org/html/2602.12670v1)
- [Demystifying Agent Skills](https://arxiv.org/abs/2608.14036)
