# Anthropic 官方指南：怎么给 Agent 设计工具

**作者**: 赛博禅心
**发布时间**: 
**原文链接**: https://mp.weixin.qq.com/s/eOkICy56oQFAzmStzgTxkw

---



BLOG


本文翻译自 Anthropic 官方博客「Seeing like an agent: how we design tools in Claude Code」，作者 Thariq Shihipar，Claude Code 团队工程师，今天发布


以下为逐段中英对照翻译


## 构建 Agent 最难的部分之一：设计工具


One of the hardest parts about building an agent harness is constructing its tools.


构建 Agent harness 最困难的部分之一，是设计它的工具集


Claude acts completely through tool calling, but there are a number of ways tools can be constructed in the Claude API with primitives like bash, skills and code execution.


Claude 完全通过工具调用来行动。在 Claude API 中，工具可以用 bash、skills、代码执行等基础原语来构建


So how do you design your agents' tools? Do you give it one general-purpose tool like bash or code execution? Or fifty specialized tools, one for each use case?


那你该怎么给 Agent 设计工具？给它一个通用工具（比如 bash 或代码执行）就够了？还是做五十个专用工具，每个场景一个？


To put yourself in the mind of the model, imagine being given a difficult math problem. What tools would you want in order to solve it? It would depend on your own skill set!


要站在模型的角度想这个问题，可以想象你面前有一道很难的数学题。你想要什么工具来解决它？答案取决于你自己的能力


Paper would be the minimum, but you'd be limited by manual calculations. A calculator would be better, but you would need to know how to operate the more advanced options. The fastest and most powerful option would be a computer, but you would have to know how to use it to write and execute code.


一张纸是最低配，但你只能手算。计算器好一些，但你得知道怎么用高级功能。最快最强的选择是电脑，但你得会用它来写和执行代码


This is a useful framework for designing your agent. You want to give it tools that are shaped to its own abilities. But how do you know what those abilities are? You pay attention, read its outputs, experiment. You learn to see like an agent.


这是一个很有用的设计框架。你要给 Agent 的工具，应该贴合它自身的能力形状。但你怎么知道它的能力是什么？你观察它，读它的输出，反复实验。你学会「像 Agent 一样看」


If you're building an agent, you'll face the same questions we did: when to add a tool, when to remove one, and how to tell the difference. Here's how we've answered them while building Claude Code, including where we got it wrong first.


如果你在做 Agent，你会面对和我们一样的问题：什么时候加工具，什么时候删工具，怎么区分这两种情况。下面是我们在 Claude Code 的实际经验，包括一开始做错的地方


## 用 AskUserQuestion 工具改善提问能力


![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FjXSGuwJvpdhFTsBPcNMP7EIGEMtCVVI3C8auDqMOnjVNvWAWqgr8mrWue7JfPSZBsNbEjM9SfmHemhklibZ6BEqyrAfPwEhNGXQojicBvibzjc%2F640%3Ffrom%3Dappmsg)


三种方案的光谱：从无结构到过度刚性，AskUserQuestion 工具落在中间


When building the AskUserQuestion tool, our goal was to improve Claude's ability to ask questions (often called elicitation).


设计 AskUserQuestion 工具时，我们的目标是提升 Claude 向用户提问的能力（通常称为 elicitation）


While Claude could just ask questions in plain text, we found answering those questions felt like they took an unnecessary amount of time. How could we lower this friction and increase the bandwidth of communication between the user and Claude?


虽然 Claude 可以用纯文本提问，但我们发现回答这些问题的体验很差，耗时太多。怎么降低这个摩擦，提升用户和 Claude 之间的沟通带宽？


### 第一次尝试：修改 ExitPlanTool


The first approach we tried was adding a parameter to the ExitPlanTool to have an array of questions alongside the plan. This was the easiest fix to implement, but it confused Claude because we were simultaneously asking for a plan and a set of questions about the plan. What if the user's answers conflicted with what the plan said? Would Claude need to call the ExitPlanTool twice? We knew this tactic wouldn't work, so we went back to the drawing board.


我们第一个方案是给 ExitPlanTool 加一个参数，让它在输出计划的同时输出一组问题。这是最省事的改法，但它让 Claude 很困惑：我们同时要求它做计划和对计划提问。如果用户的回答和计划矛盾怎么办？Claude 是不是得调两次这个工具？我们知道这个方案行不通，于是回到原点

### 第二次尝试：改变输出格式


Next, we tried updating Claude's output instructions to serve a slightly modified markdown format that it could use to ask questions. For example, we could ask it to output a list of bullet point questions with alternatives in brackets. We could then parse and format that question as UI for the user.


接下来，我们尝试修改 Claude 的输出指令，让它用一种特殊的 Markdown 格式来提问。比如用 bullet point 列出问题，每个问题后面用方括号给出选项。然后前端解析这个格式，渲染成 UI


Claude could usually produce this format, but not reliably. It would append extra sentences, drop options, or abandon the structure altogether. Onto the next approach.


Claude 大部分时候能生成这个格式，但不稳定。它会在末尾多加一句话，漏掉选项，或者干脆不用这个格式。下一个方案

### 第三次尝试：AskUserQuestion 工具


![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FjXSGuwJvpdhNCxBo6TUQBOhozN3X5ReiciciadlTmVsgicsIEusA5C3aibUGgn2INGl3jfWV6tgVIRdzQxWCm9ENU7Akhibs0yW0iaIYYWCS7RNz8Q%2F640%3Ffrom%3Dappmsg)


AskUserQuestion 工具的实际界面


Finally, we landed on creating a tool that Claude could call at any point, but it was particularly prompted to do so during plan mode. When the tool triggered we would show a modal to display the questions and block the agent's loop until the user answered.


最终方案是做一个独立的工具，Claude 可以在任何时候调用，但在规划模式中会被特别引导去使用。工具触发后弹出一个模态框显示问题，阻塞 Agent 循环直到用户回答


This tool allowed us to prompt Claude for a structured output and it helped us ensure that Claude gave the user multiple options. It also gave users ways to compose this functionality, for example calling it in the Agent SDK or using referring to it in skills.


这个工具让我们能引导 Claude 输出结构化内容，确保给用户多个选项。它也给了用户组合使用的空间，比如在 Agent SDK 或 Skills 中引用它


Most importantly, Claude seemed to like calling this tool and we found its outputs worked well. After all, even the best designed tool doesn't work if Claude doesn't understand how to call it.


**最关键的一点：Claude 喜欢调用这个工具，输出质量也好**。毕竟，再好的工具设计，如果模型不理解怎么调用，也是白搭


Is this the final form of elicitation in Claude Code? We doubt it. As Claude gets more capable, the tools that serve it have to evolve too. The next section shows a case where a tool that once helped started getting in the way.


这是 Claude Code 中 elicitation 的最终形态吗？大概不是。随着 Claude 能力提升，服务它的工具也必须跟着演进。下一节会展示一个曾经有用的工具后来开始碍事的案例


## 跟随能力迭代：从 Todos 到 Tasks


![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FjXSGuwJvpdjweCRvVNBB3JfXHJlkAn9amUy3nNnPboHTc3JGmsMJroE6jooP9IciaJc473ibuKkXHDPxBY8YyfCTpPdU2qhyicXngkThaXh3ia8%2F640%3Ffrom%3Dappmsg)


从 Todos 到 Tasks：单 Agent 线性清单 → 多 Agent 协作任务图


When we first launched Claude Code, we realized that the model needed a todo list to keep it on track. Todos could be written at the start and checked off as the model did work. To do this we gave Claude the TodoWrite tool, which would write or update Todos and display them to the user.


Claude Code 刚上线时，我们发现模型需要一个待办清单来保持专注。开工前列好待办，做完一项勾一项。我们做了 TodoWrite 工具来实现这个功能


But even then, we often saw Claude forgetting what it had to do. To adapt, we inserted system reminders every 5 turns that reminded Claude of its goal.


即便如此，Claude 还是经常忘记该干什么。我们于是每隔 5 轮对话就插一条系统提醒


As models improved, they found To-do lists limiting. Being sent reminders of the todo list made Claude think that it had to stick to the list instead of modifying it when it realized it needed to change course. We also saw Opus 4.5 also get much better at using subagents, but how could subagents coordinate on a shared todo list?


随着模型迭代，Todo 列表开始碍事。系统提醒让 Claude 觉得必须严格按清单执行，不敢中途调整方向。Opus 4.5 用子 Agent 的能力大幅提升，但多个子 Agent 怎么共享一个 Todo 列表？


Seeing this, we replaced the TodoWrite feature with the Task tool. Whereas todos are focused on keeping the model on track, tasks help agents communicate with each other. Tasks could include dependencies, share updates across subagents and the model could alter and delete them.


看到这些问题，我们把 TodoWrite 替换成了 Task 工具。Todo 的重点是让模型保持方向，Task 的重点是让 Agent 之间互相沟通。Task 支持依赖关系，可以跨子 Agent 共享状态更新，模型可以随时修改和删除


模型能力提升之后，曾经需要的工具可能反过来限制它


As model capabilities increase, the tools that your models once needed might now be constraining them. It's important to constantly revisit previous assumptions on what tools are needed. This is also why it's useful to stick to a small set of models to support that have a fairly similar capabilities profile.


随着模型能力提升，你的模型曾经需要的工具现在可能反过来在限制它。定期回头审视「这些工具是否还有必要」很重要。这也是为什么建议只支持少量能力相近的模型，这样工具设计可以聚焦


## 设计搜索界面


The most consequential tools we've built are the ones that let Claude find its own context.


**我们做过的最有影响力的工具，是那些让 Claude 自己寻找上下文的工具**


When Claude Code was first released internally, we used RAG: a vector database would pre-index the codebase, and the harness would retrieve relevant snippets and hand them to Claude before each response. While RAG was powerful and fast, it required indexing and setup and could be fragile across a host of different environments. Most importantly, Claude was given this context instead of finding the context itself.


Claude Code 内部版本最早用的是 RAG：向量数据库预先索引代码库，每次回复前自动检索相关片段塞给 Claude。RAG 速度快、效果好，但需要预处理，环境兼容性脆弱。最根本的问题是：上下文是被塞给 Claude 的，不是 Claude 自己找的


But if Claude could search on the web, why couldn't it also search your codebase? By giving Claude a Grep tool, we could let it search for files and build context itself.


如果 Claude 能搜网页，为什么不能搜代码库？给 Claude 一个 Grep 工具，就能让它自己搜文件、自己构建上下文


As Claude gets smarter, it becomes increasingly good at building its context when given the right tools.


Claude 越聪明，给它合适的工具后它就越擅长自己构建上下文


When we introduced Agent Skills, we formalized the idea of progressive disclosure, which allows agents to incrementally discover relevant context through exploration.


Agent Skills 上线后，我们把这个思路正式化为**渐进式披露**（progressive disclosure）：让 Agent 通过探索逐步发现相关上下文


Claude could now read skill files and those files could then reference other files that the model could read recursively. In fact, a common use of skills is to add more search capabilities to Claude like giving it instructions on how to use an API or query a database.


Claude 现在可以读 Skill 文件，Skill 文件可以引用其他文件，模型可以递归地发现和加载上下文。一个常见的 Skill 用法就是给 Claude 增加搜索能力：告诉它怎么调 API、怎么查数据库


Over the course of a year, Claude went from not really being able to build its own context to being able to do nested search across several layers of files to find the exact context it needed.


一年时间，Claude 从几乎不会自己构建上下文，到能在多层文件中嵌套搜索，精确找到需要的信息


Progressive disclosure is now a common technique we use to add new functionality without adding a tool. In the next section, we explain why.


渐进式披露现在是我们常用的一种技术：不加工具就能加功能。下一节解释具体怎么做


## 渐进式披露：Claude Code Guide 子 Agent


Claude Code currently has ~20 tools, and our team frequently revisits if we need all of them for Claude to be most effective. The bar to add a new tool is high, because this gives the model one more option to think about.


Claude Code 目前有大约 20 个工具，团队经常审视是否每个都有必要。**加新工具的门槛很高**，因为每多一个工具，模型就多一个需要思考的选项


For example, we noticed that Claude did not know enough about how to use Claude Code. If you asked it how to add a MCP or what a slash command did, it would not be able to reply.


比如，我们发现 Claude 不够了解 Claude Code 自身的功能。你问它怎么加 MCP、某个斜杠命令是什么意思，它答不上来


We could have put all of this information in the system prompt, but given that users rarely asked about this, it would have added context rot and interfered with Claude Code's main job: writing code.


可以把这些信息全塞进 system prompt，但用户很少问这类问题，塞进去会造成上下文腐蚀，干扰 Claude 的主要工作（写代码）


Instead, we tried progressive disclosure: we gave Claude a link to its docs that it could load and search when needed. This worked, but Claude would pull large chunks of documentation into context to find an answer the user could have gotten in one sentence.


我们尝试渐进式披露：给 Claude 一个指向文档的链接，需要时自己去查。能用，但 Claude 会把大段文档拉进上下文，只为回答一个一句话就能搞定的问题


So we built the Claude Code Guide — a subagent Claude calls whenever a user asks about Claude Code itself. The subagent does the doc-searching in its own context, follows detailed instructions on how to search and what to extract, and hands back only the answer. The main agent's context stays clean.


最终我们做了一个**Claude Code Guide**子 Agent。当用户问 Claude Code 自身的问题时，主 Agent 把请求转给这个子 Agent。子 Agent 在自己的上下文里搜索文档、提取答案，只把答案传回来。主 Agent 的上下文保持干净


While this isn't a perfect solution (Claude can still get confused when you ask it about how to set itself up), we were able to add things to Claude's action space without adding a new tool.


这个方案不完美（Claude 有时候还是会在自身配置问题上犯糊涂），但关键是：**不用加新工具，就能扩展 Agent 的能力范围**


## 像 Agent 一样看，是手艺活


Designing the tools for your models is as much an art as it is a science. It depends heavily on the model you're using, the goal of the agent and the environment it's operating in.


给模型设计工具，与其说是科学，更接近手艺。它取决于你用的模型、Agent 的目标、运行的环境


Our best advice? Experiment often, read your outputs, try new things. And most importantly, try to see like an agent.


我们最好的建议？多实验，读你的输出，试新东西。最重要的是，学会像 Agent 一样看


Experiment often, read your outputs, try new things. And most importantly, try to see like an agent.


原文链接


https://claude.com/blog/seeing-like-an-agent


作者：Thariq Shihipar，Anthropic 工程师，Claude Code 团队
