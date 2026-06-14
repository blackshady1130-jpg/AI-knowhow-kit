# Anthropic 工程分享 Notes：长时运行 Agent 的 Harness 工程

## 一句话总览

这期 Anthropic 工程分享的核心问题是：如果希望 AI Agent 不只是完成几分钟的小任务，而是能连续运行数小时甚至更久，独立构建应用、调试系统、测试界面、发现问题并持续推进，工程上到底要补什么？

Ash Prabaker 和 Andrew Wilson 的答案不是“只等模型变强”，而是模型能力和 harness 共同演进：模型负责越来越强的推理、规划和工具使用，harness 则通过上下文管理、角色拆分、持久化状态、对抗式评估器、明确 contract、真实浏览器测试和 trace 调试，把模型从一次性生成器推向可持续工作的工程系统。

---

## 最高价值观点清单

### 1. 长时运行 Agent 的难点主要有三类：上下文、规划、自我评估

Andrew 把长时运行 Agent 的困难拆成三类。

第一是上下文问题。上下文窗口有限，新 session 会像失忆一样重新开始；长 session 里会出现 context rot，模型越往后越容易失去连贯性；接近上下文末尾时还可能出现 context anxiety，模型会急着收尾，把任务草草结束。

第二是规划问题。模型默认不擅长长期规划，可能一口气想做完所有事情，也可能只做半个功能就停，或在上下文用完前留下半成品。

第三是自我评估问题。模型很容易对自己的产出过于宽容：按钮看起来存在，就认为功能完成；前端看起来像样，就忽略后端没有接上。

### 2. 解决 Agent 能力问题有两条路：改模型和改 harness

Anthropic 的思路是双线推进。

一条路是把能力烤进模型权重里，让模型本身更擅长长任务、规划、工具选择、上下文管理和自我纠错。Andrew 提到，从 Opus 3.7 到 Opus 4.6，模型在最小 scaffold 下可完成任务的持续运行时间，从大约 1 小时提升到约 12 小时。

另一条路是改 harness，也就是模型外部的脚手架：agent loop、工具调用、MCP、子 agent、权限系统、skills、检查点、压缩、持久化文件、评估器等。

关键点是：模型和 harness 不是替代关系，而是共同演进。

### 3. Harness 不会因为模型变强而消失，只会不断移动边界

一个重要判断是：模型越强，harness 不是消失，而是改变形态。

当模型弱时，harness 需要更强约束，比如拆任务、重置上下文、强制单功能推进、外部状态文件。模型变强后，有些 scaffold 可以删掉，比如新模型已经更能承受长 session，就不一定需要频繁切 fresh context。

工程方法是：找到模型当前短板，用 harness 补；再训练或等待模型吸收这种能力；模型变强后，删掉不再需要的 scaffold。

这是一种持续迭代的共同设计，而不是一次性架构。

### 4. Claude Code 本身就是模型改进的实验场

Andrew 提到，Claude Code 早期发布的目的之一，是观察开发者如何用 Claude 编程，从而反过来改进基础模型。

这很重要：Claude Code 不只是一个产品，也是一个高密度真实使用环境。用户怎样提示模型、模型在哪些环节失败、需要哪些工具、如何处理上下文、哪里会 reward hacking，都会反馈到模型和 harness 设计里。

换句话说，产品使用数据和工程 harness，本身也是模型进化的一部分。

### 5. 过去一年 Agent 能力提升，来自一组 primitives 的累积

Andrew 回顾了多项关键能力：

- Computer Use：模型可以点击、截图、测试自己写的界面；
- MCP：让模型连接外部工具和服务；
- Claude Code / Agent SDK：提供通用 agent loop 和工具调用框架；
- checkpoints：记录代码状态，可回退到之前步骤；
- Skills：通过 progressive disclosure 降低上下文浪费；
- programmatic tool calling：让模型写代码批量调用工具，只把最终结果带回上下文；
- Agent teams：子 agent 可以彼此沟通，而不只是全部回报主 agent；
- server-side compaction：长 session 可以在服务端压缩；
- 1M context：更大的上下文窗口改变了长任务设计空间。

这些 primitives 共同让 Agent 从“跑 20 分钟”走向“跑数小时甚至更久”。

### 6. Skills 的价值在于 progressive disclosure

Skills 不是简单把更多说明塞进上下文，而是通过 progressive disclosure 节省上下文。

模型先只看到 skill 的 front matter；只有当 skill 被真正调用时，才加载完整说明、参考资料或可执行代码。这避免了所有工具描述一开始就挤占上下文窗口。

对长时运行 Agent 来说，这种按需加载很关键：上下文不是越多越好，而是要在正确时间加载正确知识。

### 7. 早期长时运行 harness 依赖持久化 artifacts

Andrew 介绍了第一代长时运行 harness：用户给一个模糊 prompt，比如“写一个浏览器”或“做一个 Slack clone”，initializer agent 会先把它拆成一组持久化 artifacts。

这些 artifacts 包括：

- feature list JSON；
- progress file；
- git repo；
- init script；
- 每个功能是否完成、是否通过测试的状态。

他们甚至发现模型更容易覆盖 markdown 文件，而较少误改 JSON 文件，所以 feature list 用 JSON 更稳。这是很典型的 Agent 工程细节：格式选择会影响模型行为。

### 8. 长任务需要外部状态，而不是全靠上下文记忆

第一代 harness 通过文件系统保存状态：每次新 session 启动时，Agent 先读当前目录、progress file、init script，再选择一个未完成 feature，实现、测试、提交 git commit、更新状态。

这让 Agent 不必把所有历史都塞进上下文。长任务的关键状态应该落在可读、可检索、可交接的外部 artifacts 中。

这个原则在后面 Q&A 里也反复出现：用文件系统留下 breadcrumbs，比依赖模型记忆更可靠。

### 9. 单 Agent 自评是陷阱

Ash 最强调的一点是：self-evaluation is a trap。

让同一个 Agent 写代码，再让它检查自己写的代码，很容易失败。模型会 rubberstamp 自己的结果，尤其是在功能表面看起来完成时，它会忽略真实交互、边界条件、后端连接、控制台错误、网络错误等问题。

这和人类似：批评一幅画或一道菜，比自己画出来、做出来更容易。LLM 也一样，做 critic 往往比做 generator 更容易。

因此，调一个“严苛评估器”比让 builder 变得自我批判更可行。

### 10. Generator-Evaluator 模式是这期最重要的 harness pattern

Ash 介绍的核心模式是 generator-evaluator：

- generator 负责构建；
- evaluator 负责评估；
- 两者拥有独立 system prompt、独立上下文窗口、独立角色；
- evaluator 不只是读 diff，而是真正打开页面、点击、截图、测试；
- evaluator 把具体 critique 返回给 generator；
- generator 根据 critique 继续修改。

这种对抗式压力类似 GAN：生成器构建，判别器挑错。关键是把“构建”和“评估”拆成两个心理状态，而不是让一个模型自己说服自己已经完成。

### 11. Evaluator 必须真的使用产品，而不是只看代码

Ash 反复强调 evaluator 要用 Playwright 打开 live page、点击、操作、截图、跑测试，而不只是看 diff 或读代码。

很多 bug 只有真实使用才会暴露：

- 按钮存在但点击无效；
- 前端有控件但后端没实现；
- 键盘事件不起作用；
- 路由顺序在 unit test 里通过但生产会坏；
- 删除键存在布尔逻辑 bug；
- 文本重叠或布局错误；
- 网络错误、console error 被忽略。

这说明 Agent 的评估不应停留在静态代码层，而要进入真实运行环境。

### 12. 主观质量可以评分，只要你有足够清晰的观点

很多人会说 design taste、originality、craft 这类主观质量无法评分。Ash 的观点相反：如果你有强观点，就把它写成 rubric。

他们为前端设计评估构造了四个维度：

- design；
- originality；
- craft；
- functionality。

并且根据模型阶段调整权重。比如当 Opus 4.6 已经足够擅长 functionality，就更重视 design 和 originality，避免紫色渐变、AI slop 式审美和模板化页面。

这对团队很有启发：所谓 taste 不是玄学，它可以被写成具体偏好、反例和评分标准。

### 13. Contract 是把用户故事转成可测试断言的关键

Generator 和 evaluator 之间最关键的 glue，是在写代码前先协商“什么叫完成”。

流程是：

1. generator 提出要做什么 feature，以及 evaluator 应该怎么验证；
2. evaluator 反驳 scope 太大、测试太弱、遗漏 edge case；
3. 两者通过磁盘文件来回写 markdown；
4. 直到双方同意一个 contract；
5. generator 才开始实现；
6. evaluator 后续按 contract 评分，而不是按最初模糊 spec 评分。

这把高层 user story 转化成了可测试断言。Ash 认为这是传统 loop 缺失的关键能力。

### 14. Planner 应该高层规划，不应过度指定技术细节

为了从漂亮页面走向完整应用，他们加入了 planner 角色。

Planner 的任务是把一句话 prompt 拆成高层 spec 和 sprint，而不是提前规划每个技术细节。原因是：如果 planner 在一开始就写错细节，错误会在多小时任务里级联放大。

更好的分工是：

- planner 设定产品边界和大方向；
- generator/evaluator 协商每个阶段的 contract；
- evaluator 用真实测试不断校正。

这类似 PM、工程师和 QA 的组织结构，只是每个角色都有自己的上下文窗口。

### 15. 对抗式评估器能让 Agent 学会“推倒重来”

Ash 举了 retro game maker 的例子。同样 prompt、同样模型，solo loop 可以做出看起来不错的页面，但 play mode 中箭头键无效、空格键无效，游戏核心交互不存在。

使用 planner-generator-evaluator harness 后，Agent 构建了更完整的产品：项目创建、sprite editor、调色板、游戏比例预览、AI level assistant、play mode、debug HUD、碰撞检测、键盘操作等。

更重要的是，如果 generator 在某个维度上持续低分，比如 originality，harness 会让它扔掉当前方案重新开始，而不是在坏方案上不断 patch。这是单 Agent 自评很难做到的。

### 16. Granular criteria 才能产生 actionable critique

他们的 retro game maker 最后形成了 27 条 contract criteria。Ash 说，这种粒度是必要的。

如果标准模糊，critique 就模糊；critique 模糊，generator 只会耸耸肩，继续乱修。

如果标准具体，模型就知道要修哪一类问题，甚至能定位到具体行为或具体代码路径。

这条非常适合落地：Agent 评估不是写一句“请严格检查”，而是把成功条件拆到足够可操作。

### 17. 读 traces 是构建 Agent 的核心调试方法

Ash 说，构建这个系统没有什么秘密，真正的工作是 reading the traces。

他们主要不是盲目跑更多实验，而是读模型实际做了什么，找出模型判断和人类判断分歧在哪里，再调 prompt、rubric、harness。

他说这像读 stack trace：你要逐行理解模型为什么这么想、为什么跑偏、为什么觉得自己完成了。

Q&A 里他进一步强调：最好的方法仍然是手读 traces。可以让另一个 Agent 先帮忙 grep 或找异常，但真正理解模型行为，还是要人工坐下来读。

### 18. Agent 工程需要“模型同理心”

Ash 提到构建 browser-use harness 时的一个练习：想象你闭着眼睛操作网页，每 10 秒睁眼看一张静态截图，然后继续闭眼点击。

这能帮助工程师理解模型为什么在浏览器任务中出错。模型不是像人一样连续看见世界，它常常是在离散截图、工具反馈、文本输出之间推断状态。

因此，优秀 Agent 工程师需要一种“模型同理心”：站在模型可见信息的角度，理解它为什么误判，然后调整 prompt、工具输出、状态表示和 scaffold。

### 19. Harness 要随模型版本简化，不要迷信旧架构

Ash 提到，他们曾经在 Opus 4.5 里依赖 fresh context、sprint decomposition、每个 sprint 评估等设计，因为当时模型有 context anxiety，需要强 scaffold。

到 Opus 4.6，模型更能保持长 session 连贯性，一些机制就可以简化：单一连续 session 加 compaction 已经足够；evaluator 不必每个 sprint 都跑，而可以在较完整生成后再评估。

重要的不是某个 harness 永远正确，而是它对当时模型正确。frontier 移动后，要主动删掉不再需要的复杂性。

### 20. Compaction 不等于 coherence

Ash 的提醒很关键：压缩不等于连贯。

lossy summary 会漂移。如果长时运行只依赖模型对过去内容的压缩总结，系统可能逐渐偏离原始意图。

更可靠的模式是：

- clean context；
- structured handoff；
- 文件系统状态；
- 明确 contract；
- 可追踪 progress；
- 必要时重读 artifacts。

也就是说，压缩可以省上下文，但不能替代结构化状态管理。

### 21. 文件系统是长时运行 Agent 的好共享状态层

Ash 多次提到他们喜欢用文件系统做 shared state。

原因很简单：

- 另一个模型或人可以随时 grep；
- JSON 文件不容易被模型误改；
- 可以存 progress、尝试记录、bug、fix、timestamp；
- 可以留下 breadcrumbs，方便后续 session 或人类接手；
- 可以维护高层文档、文件结构和当前状态。

对长生命周期项目来说，Agent 不应该只把历史藏在对话里，而应该主动写下可继承的工程记忆。

### 22. 绿色地项目适合强 autonomy，棕地项目需要更多项目定制

Q&A 中他们承认，这套 planner-generator-evaluator pattern 更适合 greenfield 项目，比如从一句话 prompt 生成完整 app。

Brownfield 项目更复杂，因为已有技术栈、架构约束、代码风格、历史债务和团队习惯。要用这套模式，需要为具体项目定制 rubric、测试、contract 和 subagent。

但原则仍然可迁移：在现有软件开发生命周期里，可以把监控、issue 生成、PR 生成、PR review、bug fix loop 等环节逐步 agent 化。

### 23. 不要让 critic 直接吸收 generator 的全部上下文

有人问 critic 是否应该看到 generator 的全部思考和 trace。Ash 的倾向是否定。

他们试过，但发现会“污染”两条模型流。更有效的是让 evaluator 只判断输出和可观测结果，不要被 generator 的解释带偏。

Evaluator 应该说：“这里有问题。”然后让 generator 自己反思如何修。否则 generator 对自己工作的误判可能传染给 evaluator。

这也是角色拆分的要点：critic 要保持独立视角。

### 24. 评估 harness 质量不一定能跨项目比较，但能在单次任务内 hill-climb

有人问如何更科学地衡量 harness-agent pair 的质量。Ash 的回答是：通过极细 rubric，让 generator/evaluator 围绕这些 criteria hill-climb。

这种评分不一定适合跨不同产品比较，因为不同产品目标不同、技术栈不同、审美不同。但在单个产品或单次任务中，它能清楚显示模型从哪里开始、最后在哪些维度上提升。

这提醒我们：Agent eval 不一定总要变成通用 leaderboard。很多时候，项目内的可执行标准更重要。

### 25. Human-in-the-loop 可以加，但目标是把经验烤回 harness

Q&A 里有人问是否应该加入类似 sprint review 的 human-in-the-loop。Ash 的态度是：当然可以通过 hooks 在特定 stop condition 把任务交给人类，让人输入反馈后继续。

但他们探索的目标更偏 fully autonomous：先观察多轮失败，读 traces，调整 prompt 和 harness，把人类纠偏经验烤回系统里，而不是长期靠人类兜底。

这不是否认人类反馈，而是把人类反馈用于改进系统，而不只是临时救火。

---

## 访谈大框架

## 一、长时运行 Agent 的本质：把模型从“生成器”变成“工程系统”

这期分享最重要的背景，是 Agent 任务从几分钟变成几小时甚至几天。

短任务里，模型只需要完成一个明确请求；长任务里，模型必须保持目标、规划路径、分解任务、管理上下文、测试产物、发现错误、修复错误、记录状态，并在多轮循环中持续推进。

因此，长时运行 Agent 不是简单“给模型更多 token”，而是把模型包进一个工程系统：

- 有状态；
- 有工具；
- 有角色；
- 有评估；
- 有合约；
- 有回退；
- 有持久化记忆；
- 有真实世界反馈。

这就是 harness 的意义。

## 二、Anthropic 的演进路径：模型和 harness 互相塑造

Andrew 的历史回顾展示了一条清晰路径。

早期 Claude Code 只是 research preview，模型甚至还会在 bash 转义和字符串处理上挣扎，只能跑 20 分钟左右。随后 Computer Use、MCP、Claude Code SDK、Agent SDK、checkpoints、Skills、programmatic tool calling、Agent teams、server-side compaction、1M context 等 primitives 逐步出现。

这些不是孤立功能，而是在补模型当时的短板。模型更弱时，harness 更强约束；模型更强后，harness 变轻、更通用、更少干预。

工程启发是：不要把 Agent 架构当静态设计。它必须和模型版本、成本结构、上下文能力、工具能力一起迭代。

## 三、核心 harness：Planner + Generator + Evaluator

Ash 展示的当前核心模式可以理解为三个角色。

Planner 负责把一句话 prompt 转成高层产品 spec 和 sprint，但不应该写死技术细节。

Generator 负责实现功能、修改代码、推进产品。

Evaluator 负责以严苛 critic 身份打开真实应用、点击、测试、截图、检查 console/network、阅读运行结果，并按 contract 给出具体 critique。

这套结构的关键不在“多 Agent 很酷”，而在每个角色有独立上下文和独立动机。尤其是 evaluator，它不参与构建，所以更容易保持批判性。

## 四、Contract：把模糊需求变成可执行判断

长时运行 Agent 最大的问题之一，是“完成”的定义会漂移。

用户说“做一个 retro game maker”，这不是可测试需求。Planner 可以给方向，但如果它过度指定细节，错误会级联。

Anthropic 的做法是让 generator 和 evaluator 在每轮开始前协商 contract：

- 这个 feature 到底是什么；
- 怎么验证；
- 哪些 edge cases 必须覆盖；
- 什么算通过；
- 哪些测试太弱；
- 哪些 scope 太大。

这个 contract 成为后续评估基准。它把用户故事转成可测试断言，是长时运行 Agent 能持续推进的关键。

## 五、评估器：从“看起来完成”到“真实可用”

模型最容易犯的错，是把表面完成当成真实完成。

一个按钮出现，不代表它有后端逻辑；一个页面好看，不代表交互可用；unit test 通过，不代表真实生产路径正确；代码存在，不代表用户工作流闭环。

Evaluator 的任务就是打破这种幻觉。它要像真实 QA 一样使用产品，而不是像模型那样礼貌地相信自己。

这也是为什么 Playwright、Chrome MCP、Computer Use、截图、console/network 检查会成为关键工具。Agent 的评估必须进入运行态。

## 六、调试方法：少一点架构崇拜，多读 traces

Ash 对 Agent 工程最朴素、也最重要的建议是：sit with the model, read the traces。

很多 harness 问题不是靠更复杂架构解决，而是靠读模型行为发现：

- 它在哪一步误解了目标；
- 它为什么认为测试通过；
- 它为什么忽略边界条件；
- 它为什么不愿推倒重来；
- 它为什么被上下文带偏；
- 它为什么过早宣布完成。

只有读懂这些，才知道 scaffold 里哪些该保留，哪些该删除。Agent 工程不是堆层数，而是理解模型行为。

## 七、实践原则：可复用，但必须贴合模型和任务

Q&A 里他们反复强调，这些 pattern 可迁移，但不是固定银弹。

不同模型有不同 spiky behavior；不同任务需要不同 rubric；greenfield 和 brownfield 的约束不同；成本结构会影响用 Opus 规划还是 Sonnet 执行；有些任务需要 fresh context，有些任务可以 continuous session；有些任务适合人类 review，有些任务应该追求 fully autonomous。

最好的做法不是复制 Anthropic 的完整 harness，而是把这些原则拿回去做自己的版本：

- 拆角色；
- 写 contract；
- 用真实工具评估；
- 留外部状态；
- 读 traces；
- 随模型版本删复杂度。

---

## 可直接复用的工程检查清单

如果你要构建长时运行 Agent，可以用下面的问题检查自己的 harness：

1. Agent 的目标是否被拆成可持久化、可追踪的 artifacts？
2. 关键状态是否写在文件系统或数据库里，而不是只存在上下文中？
3. 是否明确区分 planner、generator、evaluator 的角色？
4. Evaluator 是否拥有独立上下文和严苛 system prompt？
5. Evaluator 是否真的运行产品、点击页面、看截图、查 console/network？
6. 在写代码前，generator 和 evaluator 是否协商过“什么叫完成”？
7. Contract 是否足够具体，能产生 actionable critique？
8. 是否为主观质量写了 rubric，而不是假装无法评分？
9. 是否有机制让 Agent 推倒重来，而不是在坏方案上无限 patch？
10. 是否能记录尝试、bug、fix、timestamp 和最终状态，方便后续接手？
11. 是否定期阅读 traces，找出模型判断和人类判断的偏差？
12. 是否警惕 compaction 带来的 summary drift？
13. 是否根据模型版本调整 scaffold，而不是固守旧架构？
14. 是否区分 greenfield 和 brownfield 的不同需求？
15. 人类反馈是临时兜底，还是会被沉淀回 prompt、rubric 和 harness？

---

## 精简结论

这期 Anthropic 工程分享的价值，在于把“长时运行 Agent”从 demo 拉回工程现实。

Agent 能跑数小时，不是因为简单开一个长上下文，也不是因为让模型自己循环检查自己，而是因为 harness 提供了清晰角色、外部状态、真实测试、对抗式评估和可执行 contract。

最关键的实践判断有三条：

第一，自我评估是陷阱，要用独立而严苛的 evaluator。

第二，模糊需求必须通过 contract 变成可测试断言。

第三，真正的 Agent 工程调试，不是盲目加架构，而是认真读 traces，理解模型为什么跑偏，再决定 scaffold 里哪些该加、哪些该删。

一句话概括：长时运行 Agent 的核心不是让模型“更努力地生成”，而是给它一个能持续工作、真实验证、不断校正的工程环境。

