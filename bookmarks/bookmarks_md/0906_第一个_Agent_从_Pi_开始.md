# 第一个 Agent 从 Pi 开始

**作者**: 浮之静
**发布时间**: 
**原文链接**: https://mp.weixin.qq.com/s/5r2tbJCu75f75hgRwQpF-Q

---



![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FoghJwiaPb1CukcAolicOOnSciaumVXEbBvt1M6wSm3BFpJLCdJb3SeoB6QMz1N6PqpLibfUXYNyn5eicgUfq1D3LGia9fPJzSz4uwyHViadWBqIYwk%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


学 Agent，入口经常比模型 API 更先把人卡住。


不少人第一天就去研究 memory、MCP、skills、multi-agent、Agent OS。概念都对，但落到代码实现时，最先撞上的问题往往很具体：模型怎么看文件？怎么改文件？怎么跑命令？跑错了怎么办？上下文溢出了怎么办？它说做完了，证据在哪里？


我的建议是，从Pi[1]这种项目看起。


Pi 在`coding-agent`README 里把自己称为一个 minimal terminal coding harness。这个定位很准确。它没有停在聊天壳，也没有把几十个概念堆在一起做演示。默认情况下，它先给模型一组很小的身体能力：`read`、`write`、`edit`、`bash`。除此之外，Pi 还内置了`grep`、`find`、`ls`这类只读检索工具，适合只读模式或按需 allowlist。


再往外，才是 session、context files、compaction、skills、extensions、TUI、RPC、SDK。


Pi 这个顺序把 Agent 的底层工程暴露得很清楚：能力不会从概念里自动长出来，它靠一层层工程边界托住。


推荐参考阅读：

- [深度解析：Harness Engineering](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247491737&idx=1&sn=7540894e1d73a1cf20da8e34ba421634&scene=21#wechat_redirect)
- [Agent Memory 架构本质](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247491781&idx=1&sn=3ff0a8d934f8fc9f4175b8c789b946f1&scene=21#wechat_redirect)
- [深度解析：Claude Code 源码](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247491747&idx=1&sn=402e7be9dc30cccdcd2c2f748974726c&scene=21#wechat_redirect)
- [深度解读：OpenClaw 架构及生态](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247491455&idx=1&sn=33d58cb6f0d2cd3b9c08c3c84a223e25&scene=21#wechat_redirect)
- [AI 操作系统：从指令到意图](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247491695&idx=1&sn=78edff3e611f6e99d9e1deee83453b3b&scene=21#wechat_redirect)
- [深度解析：Codex Pet Skill](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247491869&idx=1&sn=f33fefc279f7f11c3d2b2a8569d2f7b8&scene=21#wechat_redirect)
- [从 Prompt Engineering 到 Context Engineering](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247491129&idx=1&sn=451107b90247a2f8ae5aaacca3804328&scene=21#wechat_redirect)
- [深度解析：Anthropic MCP 协议](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247489489&idx=1&sn=6ea58e8984a34a4967e112b44ab01c37&scene=21#wechat_redirect)
- [顶层思维](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247491855&idx=1&sn=22d4eebe8562ae573d7ea0161fdf8780&scene=21#wechat_redirect)
- ...


## Harness 到底补齐了什么


今天群里有人问什么是 harness，我说：**凡是让 Agent 趋近于目标的一切工程化手段，都是 harness（意图 → harness 工程 → 趋近目标）。**


这句话可以保留，但还不够落地。


换成工程语言，harness 做的是这些事：让模型能观察环境，能采取动作，动作前能被限制，动作后能被记录，失败后能继续修，最后能拿证据判断任务有没有完成。


用户说：“帮我修一下这个 bug。”


模型本身只能生成文本。它不会天然知道项目结构，不会真的打开文件，不会运行测试，也不会记住刚才改了什么。要让它从“建议你怎么修”走到“自己去修”，至少要补齐几件事：

- 读取项目
- 修改文件
- 执行命令
- 把工具结果送回模型
- 保存行动轨迹
- 裁剪上下文
- 拦截风险动作
- 用真实证据判断完成状态



这些加起来，就是 harness。


别把 harness 想成一个新名词。它就是模型进入真实任务后绕不开的那套工程外壳。


Pi 的价值就在这里：它把最小 coding harness 拆成了模型、loop、工具、session、上下文和扩展点。没有多余包装，骨架直接暴露出来。

## 先看 Pi 的分层


先别急着把`pi-mono`当成一个 CLI。它的 monorepo 分得很清楚：

- `packages/ai`：多 provider 的 LLM API 适配层
- `packages/agent`：通用 agent runtime，处理 tool calling、state、event streaming
- `packages/coding-agent`：终端 coding harness，也就是`pi`
- `packages/tui`/`packages/web-ui`：界面层



这几个包之间的关系，大概可以看成：

```
Provider API  -> agent loop  -> coding tools  -> session / context / compaction  -> terminal UI / RPC / SDK
```


这层划分比抽象概念更容易落到工程判断上。


写 Agent 最常见的坏习惯，是把模型请求、工具执行、UI 输出、文件读写、会话存储全塞进一个函数里。刚开始能跑，后面一加权限、一加压缩、一加恢复，就会变成难以调试的隐式状态机。


Pi 的边界更清楚。模型适配是一层，agent loop 是一层，coding tools 是一层，session/context 是一层，UI 只是外围投影。


这个分层处理的都是硬问题：工具调用要不要并发？参数谁来校验？工具失败怎么回给模型？流式输出怎么给 UI？session 怎么落盘？模型看到的上下文和用户看到的界面消息是不是同一份东西？


这些问题都不能只靠 prompt 解决。

## Agent 的心跳：先把 loop 写稳


从零写 Agent，先把 loop 写稳，再谈 memory 和 multi-agent。


一个最小 loop 大概长这样：

```
user goal  -> build context  -> call model  -> stream assistant output  -> detect tool calls  -> validate tool args  -> execute tools  -> append tool results  -> call model again  -> stop with evidence
```


看起来很简单，写起来全是细节。


流式输出不能只打印到屏幕。你要维护一条正在增长的 assistant message，因为 tool call 可能在流中逐步出现。


工具执行这一步也容易被低估。工具参数要校验，执行过程要能取消，结果要进入 session，错误要返回给模型。多个工具并行执行时，UI 可以按完成顺序展示，但进入下一轮模型上下文的 tool result 最好保持原始 tool call 顺序。否则同一个任务会因为工具返回速度不同，产生不同上下文，后面很难调。


Pi 的 agent core 支持 sequential 和 parallel 两种工具执行模式，还提供`beforeToolCall`和`afterToolCall`钩子。前者发生在工具实际执行前，适合做参数、路径、权限、风险动作检查；后者发生在工具结果返回后，适合做审计、截断、结构化补充和错误标记。


风险拦截适合落在 runtime 层，不能只写进 prompt。命令已经生成，路径已经解析，这时候检查比在 prompt 里写“不要做危险操作”可靠得多。


Agent 工程的第一项基本功，是把 loop 当 runtime 写。不要写成一段模型调用脚本。

## 工具不是函数，是合约


Pi 默认给模型的工具很朴素：`read`、`write`、`edit`、`bash`。


这四个工具刚好对应 coding agent 的基本身体能力：

- `read`：观察项目
- `write`：创建或覆盖文件
- `edit`：做局部修改
- `bash`：运行测试、构建、查看环境反馈



`grep`、`find`、`ls`这类只读工具也很有用。它们看起来只是把 shell 命令拆出来，但能减少模型乱跑命令的机会，也让文件检索更可控。Pi 默认不把它们放进那组四个 coding tools 里，但 built-in tool 集合和只读模式里都有它们的位置。


重点不在工具数量，而在工具合约。


以`read`为例。如果它只是`fs.readFile`，很快就会出问题：大文件怎么办？图片怎么办？二进制文件怎么办？输出太长怎么办？敏感文件要不要拦？


Pi 的 read tool 支持 offset/limit，文本输出会按行数和字节数截断。内容被截断时，还会提示下一次该从哪个 offset 继续读。这个细节背后是实战经验：**工具结果很容易吃掉上下文窗口，`read`和`bash`尤其明显。**


`bash`也是同样的思路。命令输出通常保留尾部，因为错误大多在最后；输出太大时会截断，并把完整输出写到临时文件；执行过程支持 timeout 和 abort。模型拿到的是整理后的观察结果，不是未经处理的原始输出。


`edit`更典型。它要求模型提供精确的`oldText/newText`replacement，`oldText`必须唯一，不能重叠。执行后返回 diff。这个设计比整文件重写稳得多。修改范围收窄了，结果也方便展示和审计。


工具设计至少要守住几条线：

- 输入有 schema
- 输出适合模型消费
- 大输出要截断
- 截断后要能续读
- 有副作用的工具要返回 diff 或 details
- 工具失败也要回到 loop



如果工具只是把某个 API 包一下，Agent 很快会变成一个不可控的 API 调用器。

## Context 要按轮装配


不少人把 context 理解成“把资料塞给模型”。做 Agent 时，这个理解会带来问题。


一个 coding agent 每一轮都可能有很多材料：系统规则、用户目标、项目约定、历史消息、工具调用、工具结果、错误日志、压缩摘要、已读文件、已改文件、当前模型、可用工具、技能描述。


全塞进去，模型会被噪声拖慢；塞少了，它又会忘掉关键约束；顺序乱了，它会抓错重点；旧错误一直留着，它会反复修已经修好的问题。


Pi 的`packages/agent`把这里拆成两步：

- `transformContext()`：在 AgentMessage 层做裁剪、注入、压缩
- `convertToLlm()`：把应用自己的消息类型转成模型能理解的 user / assistant / toolResult



没有这条边界，UI 状态、审计状态、模型上下文会混成一份东西，后面很难拆。UI-only message、bash execution message、compaction summary、branch summary、extension state，并不都应该原样进入模型请求。有些给用户看，有些给审计留，有些只存在 session 里。


Pi 的 SessionManager 里也刻意区分了`custom`和`custom_message`：前者是扩展状态，不参与 LLM context；后者才会被构造成模型可见的 custom message。这个细节足够说明一件事：**Agent 里的“发生过”和“模型该看到”不是同一个集合。**


Pi 的 coding-agent 还会加载 context files，比如全局和项目里的`AGENTS.md`/`CLAUDE.md`。这类文件不用神化。它们更像项目约定入口：常用命令、目录边界、编码风格、不要碰的文件、验证方式。


context engineering 要反复回答几个问题：

- 这轮模型需要知道什么？
- 哪些历史已经过期？
- 哪些工具结果只要摘要？
- 哪些约定需要放到高优先级位置？
- 当前任务推进到哪一步？



回答不好，Agent 运行时间越长，决策越容易漂移。

## Session 是行动账本


只保存 user / assistant 对话，得到的是 chat log。


Agent session 要记录行动轨迹：用户说了什么，模型打算做什么，调用了哪个工具，参数是什么，结果是什么，改了哪些文件，跑了哪些命令，哪里失败，最后靠什么证据收尾。


Pi 的 session 是 JSONL。除 session header 外，后续 entry 都有`id`和`parentId`，同一个 session 文件里可以形成树。`/tree`做的是原地导航：用户可以选中历史位置，Pi 会移动当前 leaf，后续消息从那里继续长出新分支；如果选中的是 user message，它会回到这条输入之前，并把原输入放回编辑器，方便改写后继续。


别把它看成 UI 小功能。它是在给 Agent 留退路。Agent 走错方向不是异常，是常态。能回到某个判断点继续，比重开一局有价值得多。


Pi 的 session entry 也不只有 message。它还记录 model change、thinking level change、compaction、branch summary、custom entry、custom message、label、session info。


到这一步，session 的职责已经从保存聊天，扩展到恢复、分支、审计、导出、调试和扩展状态。


自己做 Agent，早期不用这么完整，但最好从 event log 开始。每次用户输入、模型输出、工具调用、工具结果、文件修改、命令执行，都应该能回放。


没有 event log，后面做 compaction、eval、bug 定位，都会变成事后猜测。

## Compaction 是连续性机制


只要 Agent 能读文件、跑命令，上下文膨胀很快就会发生。一次测试失败可能几千行，读几个大文件就会占掉大量 token。


**把 compaction 当省钱技巧，会低估它对任务连续性的作用。**


Pi 的 compaction 大概是这样：从最近消息往前找 cut point，保留一段近期上下文；把更旧的内容交给模型总结；生成`CompactionEntry`，记录 summary、`firstKeptEntryId`、tokensBefore 等信息；重新构建 session context 时，用 summary 加近期消息继续工作。


关键点在这里：完整历史仍然留在 JSONL 里。模型当前看到的是压缩视图，系统没有把历史删掉。


可以这样理解：

```
durable history: 完整行动轨迹working context: 当前模型可见材料summary: 二者之间的压缩视图
```


只保留完整历史，模型会被旧日志拖垮。只保留摘要，摘要一错就没证据可查。所以两层都要保留。


Pi 的 compaction 文档里还有一个经验细节：序列化待总结消息时，工具结果会被截断到固定长度，避免`read`/`bash`输出把总结请求撑满。做 Agent 久了就知道，token 经常耗在工具输出上，而不是“对话”本身。

## 权限要按运行环境设计


Pi 的设计哲学里有一个值得注意的选择：它没有把 permission popups、plan mode、sub-agents、MCP 都塞进核心。它更鼓励你通过 container 或 extensions 接入确认流、路径保护、git checkpoint、sandbox execution、MCP integration。


这说明 Pi 对边界很克制。


通用框架很难替你判断什么是危险动作。对本地 demo 来说，`npm install`可能没问题；对生产服务器来说，这可能就是高风险操作。对某些团队，删除临时目录很正常；对另一些团队，任何`rm`都应该审批。


权限不能只是一层弹窗。先看 Agent 运行在哪里：

- 本机项目
- 临时容器
- 远程 sandbox
- CI runner
- 生产运维环境
- 带用户账号的浏览器



运行环境不同，工具策略完全不同。


做第一个 coding agent，可以先保守一点：把只读工具默认开启，写文件和 bash 单独开关；bash 加 timeout；高风险命令走确认；敏感路径默认禁止；每次修改后展示 diff。


早期 coding agent 要先做到可控。它应该让你知道它做了什么，也能在出问题时把它收回来。

## 完成判断要靠证据


Agent 很容易过早宣布完成。


它会说“问题已经修复”，但可能没跑测试；跑了测试但失败；只修了 happy path；顺手改了无关文件；甚至把错误日志看反了。


harness 里需要有 completion check。


对 coding agent 来说，最基础的完成证据包括：

- 相关文件有明确 diff
- 运行了和任务相关的测试或检查
- 命令结果成功
- 没法验证时说明原因
- 没有明显无关改动
- 最终说明能对应到真实工具结果



模型可以写总结，证据要来自工具。


最终回答应该像一份工程交付说明：改了什么，为什么这么改，怎么验证，还有什么没验证。只说“已完成”，没有意义。


Pi 鼓励公开真实 OSS coding agent sessions，也正是因为这些轨迹里有工具使用、失败、修复和验证。它们比玩具 benchmark 更接近真实 Agent 工程。

## 从 Pi 到 OpenClaw


读完 Pi，可以继续看OpenClaw[2]。


Pi 更接近 runtime kernel，解决模型适配、tool loop、session JSONL、工具执行、compaction、skills、resource loader。


OpenClaw 更接近 product control plane。它把 Pi 嵌进一个长期运行的个人助理系统里，外面接入 IM 通道、移动端节点、Canvas、cron、webhook、Control UI。用户从不同入口发来的消息，最后路由到某个 agent session。底层模型循环、工具调用、session transcript，仍然大量复用 Pi 的 agent core / coding-agent 能力。


Pi 和 OpenClaw 的关系，可以直接看成 runtime kernel 与 control plane 的分工。


Pi 负责内核语义：模型怎么跑，工具怎么调，runtime transcript 怎么写，上下文怎么压。


OpenClaw 负责产品世界：谁发来的消息，应该进哪条 session，用哪些工具策略，走哪个 sandbox，失败后怎么重试，token 和成本怎么展示，远程节点怎么投递。


从 OpenClaw 里可以看到几件 Pi CLI 里不那么明显的事。


第一，session 需要两层状态。Pi 的 transcript 是 JSONL，适合记录对话和工具轨迹。OpenClaw 还维护`sessions.json`，用`sessionKey -> sessionId`管不同通道、群组、cron、hook、sub-agent 的路由和当前会话。transcript 记录发生了什么，session store 记录消息该进入哪条轨道。


第二，工具策略需要动态化。OpenClaw 会根据 agent、provider、group/channel、sender、sandbox、owner-only 规则算出 effective tool policy，再把最终可用工具通过`customTools`统一注入 Pi。这个设计比全局工具列表成熟很多。


第三，context builder 已经进入运行时层面。OpenClaw 的系统提示词构建会按规则纳入 workspace 里的`AGENTS.md`、`SOUL.md`、`TOOLS.md`、`IDENTITY.md`、`USER.md`，以及待完成首轮引导时的`BOOTSTRAP.md`；还会控制 skills metadata、时间、运行时信息、通道能力、sandbox 信息、memory 引用、工具结果长度。


第四，安全边界会被通道放大。本地 Pi session 通常是用户自己在终端里发指令；OpenClaw 面对的是真实消息入口，私聊、群聊、cron、webhook 都可能是不可信输入。Agent 一旦从本地 CLI 走向网络通道，权限就不再是“加个确认弹窗”这么简单。


第五，长期运行会逼出运维问题。auth profile 管理、provider fallback、队列 lane、流式消息分块、token/cost 展示、session 清理、trajectory 记录、compaction 超时、上下文溢出恢复，都会变成真实问题。


OpenClaw 很适合作为 Pi 之后的拓展阅读。先看 Pi，理解最小 harness 怎么跑；再看 OpenClaw，理解 harness 接到真实用户、真实通道、真实权限、长期运行环境后，会长出哪些控制面。

## 自己搭个 Agent


不用一次做成 Pi。比较稳的路线是：

1. **先做只读 Agent**：接模型 provider，写最小 loop，提供`read`、`grep`、`find`、`ls`，重点放在工具 schema、上下文组装和结果截断。
2. **再加精确修改**：提供`edit`，用小块 replacement，返回 diff，至少保证路径限制和 diff 可见。
3. **然后加命令执行**：提供`bash`，带 cwd、timeout、输出截断、abort，让 Agent 形成“改完跑测试，失败再修”的闭环。
4. **尽早做 event log**：不要只存 messages，工具调用、工具结果、模型变化、文件修改、人工插话都应该能回放。
5. **再做 context builder 和 compaction**：把 durable history 和 working context 分开，旧内容用摘要进入当前上下文，完整历史仍然保留。
6. 最后再上 skills、extensions、MCP、memory。基础 loop 不稳，接更多能力只会让问题更隐蔽。


## 启发：工程模式


Pi 和 OpenClaw 留下的价值，主要不在某个工具实现，而在几种能复用到其他 Agent 系统里的工程模式。


**第一，Context 更像投影。**


很多 Agent 一开始把 context 当成无边界容器：凡是发生过的，全往模型里塞。Pi 的做法更克制：session 可以很丰富，但模型每轮看到的应该是一份经过治理的 projection。做自己的 Agent，可以把状态拆成三类：给模型看的，给用户界面看的，只给审计和恢复看的。


**第二，Transcript 是账本，working context 是视图。**


Pi 的 session JSONL 记录行动轨迹和分支历史，compaction 也只是新增摘要 entry，不删除旧消息。OpenClaw 额外维护`sessions.json`，用`sessionKey -> sessionId`管路由、模型覆盖、工具开关、token 计数等元信息。这个分层很朴素，也很耐用：transcript 记录发生过什么，session store 记录现在该往哪里走，working context 是运行时临时构建出来的视图。


**第三，权限要进入运行时管线。**


Pi 的`beforeToolCall`/`afterToolCall`给工具执行前后留出边界。OpenClaw 继续往前走：按 owner-only、agent 配置、provider、group/channel、sender、sandbox、sub-agent 等规则算出 effective tool policy，再把最终可用工具通过`customTools`注入 Pi。这个模式比“给模型一批工具，再在 prompt 里提醒它别乱用”可靠得多，因为权限来自运行时元数据，而不是模型文本。


**第四，Runtime 内核要小，产品控制面可以厚。**


Pi 没有把所有时髦能力都塞进核心。核心主要负责模型、loop、工具调用、状态、事件和 session。OpenClaw 展示了另一半：长期运行的个人助理系统会长出 Gateway、通道接入、pairing、Control UI、auth profile 管理、usage 展示、sandbox、队列、fallback、cron、webhook。Pi 和 OpenClaw 的组合给了一个中间答案：内核负责可复用的 Agent 语义，控制面负责具体产品世界。


**第五，失败路径和证据链要一起设计。**


Pi 的工具没有假设一切顺利。`read`会截断并提示续读，`bash`会保留完整输出路径、支持 timeout 和 abort，`edit`会因为 oldText 不唯一或重叠而拒绝修改。OpenClaw 也没有把长期在线写成一个乐观循环，它处理 provider fallback、auth profile 管理、idle timeout、context overflow、tool result truncation、trajectory 记录和 compaction 超时。一个 Agent 越能动手，越需要留下行动轨迹；否则用户看到的是一个会改环境的黑盒，团队面对的是一个难以复盘的运行时系统。


这套实现给出的更深结论：**Agent 工程不急着把模型包装得更像人。关键在于，把模型的判断放进一套可投影、可授权、可恢复、可观测的系统里。模型越强，这套外部秩序越不能省。**

## Harness 会被模型内化吗


会有一部分被内化。


更强的模型会更自然地规划步骤、选择工具、理解 diff、根据测试失败继续修。过去需要 prompt 反复提醒的工作习惯，确实会逐渐变成模型能力。比如“先读文件再改”、“改完跑测试”、“输出不要太长”，这些可以被模型学进去。


但这类内化主要发生在认知策略层。工程 harness 里的另一部分，模型内化不了，也不应该交给模型内化：文件系统在哪里，当前用户是谁，哪些路径不能碰，哪条消息来自群聊，谁有 owner 权限，工具结果怎么截断，session 怎么恢复，成本怎么记，失败后怎么重试，审计日志写到哪里。


这些不是模型聪明一点就能解决的问题。它们属于外部世界的边界和制度。


如果把 harness 理解成一堆提示词和流程模板，它会被模型吸收一部分；如果把 harness 理解成模型进入真实任务后的运行时秩序，它只会越来越重要。prompt scaffolding 可能变薄，runtime harness 会变硬。弱模型需要 harness 帮它做事，强模型更需要 harness 确保它做事不越界、可复盘、能交付。

## 回到 Harness


现在再看 harness，就没那么玄了。


它不只是 prompt、tools、memory 的列表。把模型放进真实任务之后，需要补齐的那套工程系统，才是它的内容。


Pi 给了一个很好的入门样本：核心很小，边界很清楚。`packages/agent`负责 loop 和事件；`packages/coding-agent`负责终端 harness、工具、session、context files、compaction 和扩展；TUI、web-ui、RPC、SDK 都是外围投影。


还是最初的那句定义：**凡是让 Agent 趋近于目标的一切工程化手段，都是 harness。**


落到工程里，它不是口号。它是你每天要做的一组选择：让模型看什么、能做什么、怎么做、做错怎么停、历史怎么存、上下文怎么裁、风险怎么管、完成怎么验。


把这些问题一个个回答清楚，你就已经在做 Agent 工程了。

## 源码参考入口

- `pi-mono/README.md`
- `packages/coding-agent/README.md`
- `packages/agent/README.md`
- `packages/agent/src/agent.ts`
- `packages/agent/src/agent-loop.ts`
- `packages/coding-agent/src/core/messages.ts`
- `packages/coding-agent/src/core/tools/index.ts`
- `packages/coding-agent/src/core/session-manager.ts`
- `packages/coding-agent/docs/compaction.md`
- `packages/coding-agent/docs/extensions.md`
- `packages/coding-agent/docs/skills.md`
- `openclaw/README.md`
- `openclaw/docs/concepts/agent.md`
- `openclaw/docs/reference/session-management-compaction.md`
- `openclaw/docs/reference/token-use.md`
- `openclaw/src/agents/pi-embedded-runner/run/attempt.ts`
- `openclaw/src/agents/pi-embedded-runner/effective-tool-policy.ts`
- `openclaw/src/agents/pi-embedded-runner/tool-split.ts`


### References


[1]

**Pi:***https://github.com/badlogic/pi-mono*
[2]

**OpenClaw:***https://github.com/openclaw/openclaw*
