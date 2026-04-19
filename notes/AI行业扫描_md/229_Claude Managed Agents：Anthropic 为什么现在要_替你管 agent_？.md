# Claude Managed Agents：Anthropic 为什么现在要"替你管 agent"？

> 来源：[https://docs.qq.com/doc/DYW9nU1J0RUp0UWdi](https://docs.qq.com/doc/DYW9nU1J0RUp0UWdi)
> 镜像：[https://yage.ai/share/claude-managed-agents-20260408.html](https://yage.ai/share/claude-managed-agents-20260408.html)
> 调研日期：2026-04-08（发布当天）

---

## 一句话

今天 Anthropic 发布了 Claude Managed Agents。你写一个 agent 的定义——模型、prompt、tools、MCP、skills——交给 Anthropic，它帮你在自家的 sandbox 里运行 session，按 runtime 小时加 token 收费。官方 tagline 是 "build and deploy agents 10x faster"，客户引语都在说"几天而不是几个月"，看上去是一个"让开发者少操心基础设施"的产品。

读完所有材料以后，我的判断是：**这个产品帮你省事是副作用，让 Anthropic 而不是 AWS 握住 agent 这层的入口才是主线。** 你用不用它，实际上是在选一件事——愿意把 agent 的 operational state（credential、memory、session 历史）托管在 Anthropic 那里，换取几周不用写的 plumbing 代码；还是继续自己管这些东西，换取不被 Claude 绑住的自由。

这个选择本身不新，所有云服务都是这笔账。新的是它把"agent"这一层变成了这笔账的新战场。

---

## 产品本身

最快的理解方式是拿一个具体场景走一遍。假设你想给自己的 SaaS 产品加一个"研究助手"——用户扔一个问题进来，agent 能搜网页、读你们内部的 wiki、整理出一份报告回去。这件事过去要你自己干：租一台 container、写 agent loop、管会话状态、配 credential、做 tracing。MA 的存在是让你从头到尾都不碰这些东西。

你打开 Anthropic 控制台填一张表：agent 用 Claude Opus 4.6，system prompt 是"你是研究助手"，工具是 web search 加你自己的一个 MCP server，skills 装上你写的那个"公司 style guide"。表交出去，你拿到一个 agent ID。这是第一个概念，叫 **Agent**——它就是你对"这个 AI 是什么、会做什么"的完整声明，一个静态对象。

然后你告诉 Anthropic 这个 agent 要跑在什么样的环境里：预装 pandoc 和 weasyprint，容器只许访问 api.mycompany.com 和 serpapi.com，其他 host 都封掉。你拿到一个 environment ID。这是第二个概念，**Environment**——一个 container 模板。它和 agent 分开是因为同一个 agent 可以在不同环境里跑，比如生产环境和 staging 环境走不同的 host 白名单。

用户一来，你创建一个 session，把 agent ID 和 environment ID 一起扔进去。Anthropic 那边起一个容器，你的 agent 就在里面活过来了。这是第三个概念，**Session**——一次具体的运行实例。你的应用和这个 session 之间走一条 SSE 通道来回传消息，这些消息叫 **Events**，也是第四个概念，全部在服务端持久化。你的 web 服务器挂了也没事，重连接着跑。用户关了浏览器，session 进 idle，不计费。下次他回来，session 继续，对话状态不用你自己管。

走完这一遍你会注意到两件事。第一件是：整个过程你没写一行 agent loop。模型什么时候调 web search、调用失败怎么重试、context 太长怎么 compact、对话历史存哪——这些决定都是 Anthropic 的 harness 替你做的。这是 MA 的核心卖点。第二件是：credential 是放进一个叫 vault 的 write-only 存储的，agent 运行时能用但读不到原文；每一次 tool call 都写进 event stream，在 Console 里变成一条可审计的时间线。这是 MA 的 governance 卖点。

但同样在这套流程里，有两件官方没大声说的事值得你看一眼。

一是 `agents.update` 这个 API 没有审批。你的 agent 定义本身是 immutable 的（每次更新都发一个新版本号），但任何拿到你 API key 的人都可以直接发 update 改 system prompt 和 tool 清单。Anthropic 在自己的 cookbook 里承认这是个 tradeoff，让调用方自己用版本号 pinning 和 PR review 补上这层保护。对金融、合规、高风险场景，这个洞要在集成时显式堵上。

二是 MA 最吸引人的三个功能今天都在 research preview，没有 GA 时间表。Outcomes 是其中最像 demo 的那个——你写一份 rubric，Claude 自己迭代到 rubric 被满足为止。官方 blog 里反复强调的"让 Claude 自己迭代直到任务完成"就是这个功能，今天你用不到。另外两个是 Multi-agent orchestration（目前只支持单层 delegation，不能 agent 套 agent 套 agent）和 Memory（跨 session 的持久记忆）。发布日能跑的是编排 harness 和 governance 基础，最出片的能力留在门后。

定价只有一行，定义留得很松。blog 原文是 standard Claude Platform token rates apply, plus **$0.08 per session-hour for active runtime**，TheNewStack 的独立报道补了两个细节：idle time 不算钱，web search 额外 $10 每 1000 次。Anthropic 的 pricing docs 页面到今天都还没有 Managed Agents 的章节。active runtime 到底按秒、按分钟还是按小时向上取整，rescheduling 状态算不算 active，这些 docs 都没写。

---

## 为什么说这是 Anthropic 的入口战

把产品的"它帮你做了什么"放一边，换一个角度：Anthropic 选在这个时间点做这件事，是在解决什么问题？

按时间看 Anthropic 是四家大厂里最晚下场的。AWS Bedrock AgentCore Runtime 2025 年 10 月 GA，OpenAI AgentKit 加 Responses API 差不多同期，Google Vertex Agent Engine 也已经到位。Anthropic 晚了半年。这个 delay 不是技术没准备好，Claude Code 早在 2025 年 2 月就有完整的 agent runtime 了，MA 的 harness 大概率就是从 Claude Code 里抽出来的。

真正解释时机的是两件挨得很近的事。

**第一件是财务。** 公开报道里 Anthropic 2025 年前 9 个月给 AWS 付了 26.6 亿美元的 compute，超过同期 revenue，2024 gross margin 大约 -94%，对投资人的承诺是 2028 做到 77%。这条曲线要走通，必须从某处收回毛利。Claude Code 在 2025 年末做到约 10 亿美元 ARR，2026 年初到 25 亿美元以上，证明了"比 raw API 更高层级的产品"确实能把毛利拉起来。MA 是同一个逻辑的第二次发球，从"卖 token"升级到"卖 runtime 加 token"。

**第二件是平台控制权。** MA 发布的 4 天前，Anthropic 切断了 OpenClaw 和几个类似的第三方 harness 通过订阅计划接入 Claude 的便宜通道。两件事挨这么近不像巧合。合理的读法是：先关闭"用我的 token 跑你的 harness"那条价廉路径（这条路径上 Anthropic 拿不到 runtime 的钱，也控制不住 agent 的交互形态），再开放"用我的 harness 在我的 runtime 上跑"的官方路径。一堵一疏，同一个动作的两半。

> Hacker News 发布日讨论里有人直接点出了这个动机（47693047，用户 cedws）："Anthropic wants to shift developers on to their platform where they're in control. The fight for harness control has been terribly inconvenient for them. To score a big IPO they need to be a platform, not just a token pipeline."

还有第三件事，更隐蔽一点。Claude Cowork 已经被 Microsoft 嵌入 Copilot，如果 Anthropic 没有自己独立的 platform 层，它面对的长期局面是"Claude 成为 Microsoft 产品里的一个模型选项"。MA、Claude Code、Copilot 这三层加起来，让 Anthropic 有了 consumer、developer 和 platform builder 三个自己直接掌握的入口，不必把分发权交给任何一家 hyperscaler。

把这三件事并排放：财务要改善毛利、产品要收回 harness 控制权、渠道要摆脱 hyperscaler 依赖。MA 同时解这三道题。**"帮开发者省几个月基础设施工作"是卖点，不是动机。**

---

## 省的事，到底省给谁

发布日有两个独立的声音值得并排读。

一个是 Hacker News 主线程上的 JLO64，一个用 Anthropic Agent SDK 自己搭了 agent runtime 的开发者。他的原话是："I built this myself in a few days, it wasn't that hard." 他说的是真的。如果你是一个有经验的 backend 工程师，agent loop + session state + SSE 通道这套东西不是什么黑魔法，一个人一周内能出原型。

另一个是 Wired 报道里引用的 Anthropic 企业客户，一家叫 Ridgeline 的金融软件公司，他们的 CTO 说："We were able to build and deploy a production-ready agent in days, not months." 这两个人说的都是真话，但他们不是同一个人。

JLO64 是个人开发者或小团队，他的"几天"是在已有基础设施、已有 DevOps 经验、已有 security review 流程的基础上算的。Ridgeline 的"几天"是在企业合规要求、多团队协作、audit trail 要求、credential 管理规范的基础上算的。MA 省掉的那几个月，大部分不是写代码的时间，是走流程、过合规、建 governance 的时间。

这解释了 MA 最适合的客户画像：**中大型企业的 AI 产品团队，他们有预算、有合规要求、有多个 agent 要管、但没有专门的 AI infra 团队。** 对这类客户，MA 的价值不是省代码，是省掉"建自己的 agent platform"这整个项目。

---

## 这个产品的边界和代价

用 MA 意味着接受三层绑定，从浅到深：

**第一层：模型绑定。** 显而易见，MA 只跑 Claude。如果你的 agent 需要在 Claude 和 GPT 之间切换，或者未来想换模型，这层绑定的代价就出来了。

**第二层：API shape 绑定。** MA 的 agent loop 是 Anthropic 的 harness，它的 tool call 格式、context management 策略、error handling 行为都是 Anthropic 定义的。你的 agent 逻辑如果深度依赖这些行为，迁移成本会比迁移模型更高。

**第三层：operational state 绑定。** 这是最深的一层，也是最难迁移的。你的 agent 的 session 历史、memory、credential vault 都在 Anthropic 那里。如果你想迁移到自建或者竞品，这些 state 的导出和重建是真实的工程成本，不是一键迁移。

这三层绑定不是 bug，是 MA 的商业逻辑。它和所有 managed service 的逻辑一样：你用得越深，离开成本越高，Anthropic 的定价权越强。

---

## 我认为最重要的综合判断

MA 是一个真实有用的产品，对特定客户群体有真实价值。但它更重要的意义在于：**它标志着 AI 竞争的战场从"谁的模型更好"正式扩展到了"谁控制 agent 这一层的 runtime"。**

这个战场上，Anthropic 是最晚入场的，但它有一个别人没有的优势：Claude Code 已经证明了"比 raw API 更高层级的产品"在开发者市场里能跑通。MA 是把这个逻辑从 coding agent 推广到通用 agent 的第一步。

对开发者来说，现在的选择不是"用不用 MA"，而是"在哪一层建自己的护城河"。如果你的核心价值在 agent 的业务逻辑和领域知识，MA 帮你省掉 infra 是合理的。如果你的核心价值在 agent 的运行方式和交互形态本身，把这层交给 Anthropic 就是把护城河交出去。

---

## 已确认、推断与待验证

| 类型 | 内容 |
|------|------|
| 已确认 | Managed Agents 目前处于 public beta；核心抽象是 Agent / Environment / Session / Events；定价是 token 费用加 $0.08/session-hour；agents.update 无审批流程；有 credential vault 和 event stream audit |
| 已确认 | memory、multiagent、outcomes 仍有 research preview 成分；Memory 和 Multi-agent 不在 GA 范围 |
| 推断 | Anthropic 的核心动机不只是"帮开发者省事"，更是争夺 harness control 和改善毛利结构 |
| 推断 | Managed Agents 更像面向 SaaS 产品团队和企业平台团队，而不是成熟 AI infra 团队 |
| 待验证 | 长时生产任务的真实账单细节；从其他 runtime 迁入的真实案例；Outcomes GA 时间表 |

---

## 主要来源

**官方材料**
- Anthropic 官方发文：https://claude.com/blog/claude-managed-agents
- Managed Agents overview：https://platform.claude.com/docs/en/managed-agents/overview
- Managed Agents pricing：https://platform.claude.com/docs/en/about-claude/pricing

**外部报道与讨论**
- Wired 报道：https://www.wired.com/story/anthropic-launches-claude-managed-agents/
- Hacker News 讨论：https://news.ycombinator.com/item?id=47693047

**竞品背景**
- OpenAI Frontier：https://openai.com/index/introducing-openai-frontier/
- Google Vertex Agent Engine：https://cloud.google.com/vertex-ai/generative-ai/docs/reasoning-engine/overview
- AWS Bedrock Agents：https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agents/
