# What Happened to AutomationBench?

| Item | Details |
| --- | --- |
| Author | Wenhao Chai |
| Year | 2026 |
| Original language | English / Chinese bilingual |
| Source | [Original article][1] |
| Formatting note | Original bilingual body, tables, data links, and citation have been retained; site navigation and avatar imagery were omitted. |

Open models score well on AutomationBench: DeepSeek V4.1 Flash reports 54.8 on the public tasks and ranks fourth by Tasks Completed on Artificial Analysis’ private set, behind three GPT-6 Astra settings and above Claude Fable 5.1 and Claude Opus 5. Zapier’s leaderboard passes a task only when every assertion holds, unsound string-matching guardrails included, and that scoring rule decides much of the ranking.

开源模型在 AutomationBench 上分数很高：DeepSeek V4.1 Flash 在公开题上报 54.8，在 Artificial Analysis 的私有题上按 Tasks Completed 排第四，前面只有 GPT-6 Astra 的三个档位，高于 Claude Fable 5.1 和 Claude Opus 5。Zapier 的榜要求每条 assertion 都成立才算通过，包括站不住的字符串匹配 guardrail，这条计分规则决定了排名的很大一部分。

## The observation 观察

Open models looked strong on AutomationBench in September 2026. DeepSeek V4.1 Flash’s model card reports 54.8 on the 600 public tasks, GLM-5.3’s 48.2, and Xiaomi’s MiMo-v2.6-flash dashboard 44.8 at the first step of its reinforcement-learning (RL) run, read on 19 September 2026. Zapier’s own public-set run of Claude Opus 5 gives 50.3. On Artificial Analysis’ run of the private set, DeepSeek V4.1 Flash ranks fourth by Tasks Completed, behind three GPT-6 Astra settings and above Claude Fable 5.1 and Claude Opus 5. I wanted to know what these scores measure.

2026 年 9 月，开源模型在 AutomationBench 上看起来很强。DeepSeek V4.1 Flash 的 model card 在 600 道公开题上报 54.8，GLM-5.3 报 48.2，小米 MiMo-v2.6-flash 在 RL 第 1 步就有 44.8（2026 年 9 月 19 日读取）。Zapier 自己在公开题上跑的 Claude Opus 5 是 50.3。在 Artificial Analysis 跑的私有题上，DeepSeek V4.1 Flash 按 Tasks Completed 排第四，前面只有 GPT-6 Astra 的三个档位，高于 Claude Fable 5.1 和 Claude Opus 5。我想知道这些分数到底在量什么。

## The benchmark 这个 benchmark

AutomationBench, from Zapier, scores agents on business workflows. A task seeds a simulated company of 47 apps behind about 500 REST endpoints; the agent must find the endpoints itself, follow policies stored in the data, and stop within 50 turns. The grader ignores the transcript and checks the final state of the apps against per-task assertions; a task passes only when every assertion holds. Six hundred scored tasks are public, alongside 200 unscored warm-up tasks; the leaderboard uses a private set that Artificial Analysis counts at 657 tasks.

AutomationBench 由 Zapier 发布，评测 agent 完成业务流程的能力。每道题初始化一个 47 个应用、约 500 个 REST 端点的模拟公司；agent 要自己找端点，遵守存放在数据里的政策，在 50 轮内结束。打分器不读对话记录，只拿各应用的最终状态对照该题的 assertion，全部成立才通过。600 道计分题公开，另有 200 道不计分的简单题；榜单用另一个私有题集，Artificial Analysis 给出的数量是 657 道。

Three scoring rules appear in this post, under the names Artificial Analysis uses. **Tasks Completed**: a task counts only when every assertion holds; Zapier’s leaderboard reports the same rule as its pass rate. **Score**: a task scores 0 if any guardrail is broken and otherwise the share of objectives met; this is the Artificial Analysis headline. **Objectives Completed**: the share of objectives met with guardrails ignored. An objective is an assertion that must become true; a guardrail names an outcome that was false before the run and must stay false.

本文用到三种计分规则，沿用 Artificial Analysis 的叫法。**Tasks Completed**：每条 assertion 都成立才算通过；Zapier 的榜报的 pass rate 是同一条规则。**Score**：违反任何一条 guardrail 记 0，否则记目标完成的比例；这是 Artificial Analysis 的头条指标。**Objectives Completed**：目标完成的比例，不计 guardrail。目标是必须变真的 assertion；guardrail 指定一个运行前为假、运行后必须仍为假的结果。

## Task example 任务示例

Task 501, sales domain: “We just closed the Meridian Corp Platform Deal! Mark it as won and route the win notice to the right team per our routing policy.” The routing policy is an email in the inbox and names the team and the subject line to use; the account tier and the exchange rate are in two spreadsheets, each with a stale row and a current row. The rubric is six assertions on the final state: three must become true, three must stay false. Figure 4 steps through Qwen3.6-27B’s run and scores it three ways. The run comes from the only full public traces I found: four open-weight models on the 600 public tasks, Qwen3.6-27B, Gemma-4-31B-it, Opera and Ops-I, which beyoru posted on Hugging Face with every message and final state.

sales 域第 501 题：“We just closed the Meridian Corp Platform Deal! Mark it as won and route the win notice to the right team per our routing policy.” 路由政策是收件箱里的一封邮件，写明了该发给哪个团队、用什么主题行；账户等级和汇率在两张表格里，每张各有一行过期数据和一行当前数据。rubric 是最终状态上的六条 assertion：三条必须变真，三条必须保持假。图 4 逐步展示 Qwen3.6-27B 的运行，并用三种方式打分。这条运行来自我找到的唯一一套完整公开 trace：四个开源模型（Qwen3.6-27B、Gemma-4-31B-it、Opera、Ops-I）在 600 道公开题上的运行，由 beyoru 发布在 Hugging Face 上，含每条消息和最终状态。

Three of the four public models emailed the executive team and all three failed that assertion: none used the subject line “Deal Closed Notification”, and two wrote 156,000 USD without the dollar sign. The fourth emailed sales-team instead. All four scored 33% on this task.

四个公开模型里三个给 executive team 发了邮件，三个都没通过这条 assertion：没有一个用 “Deal Closed Notification” 这个主题行，其中两个把金额写成 156,000 USD，没有美元符号。第四个发给了 sales-team。四个模型在这道题上都是 33%。

## Three scoring rules on the same rollouts 同一批 rollout 上的三种计分规则

Artificial Analysis runs the private set once and publishes three scoring rules over the same rollouts. Zapier’s leaderboard applies the first rule to its own rollouts.

Artificial Analysis 在私有题集上跑一次，对同一批 rollout 公布三种计分规则的结果。Zapier 的榜把第一种规则用在自己的 rollout 上。

In the Artificial Analysis snapshot of 19 September 2026, DeepSeek V4.1 Flash completes fewer objectives than most of the top ten, and about a fifth of that objective credit is zeroed on tasks with a guardrail violation, so Score ranks it first. Claude Opus 5 ties for the most objectives and has about a third of its credit zeroed the same way, so Score ranks it eighteenth.

在 Artificial Analysis 2026 年 9 月 19 日的快照里，DeepSeek V4.1 Flash 完成的目标比前十名里大多数模型少，但只有约五分之一的目标得分因所在题违反 guardrail 而归零，所以 Score 把它排第一。Claude Opus 5 目标完成率并列最高，却有约三分之一的得分同样归零，Score 把它排第十八。

## Are the guardrails reasonable? guardrail 合理吗？

Guardrails are the assertions that must stay false: no mail to this address, no row in this sheet, no message in this channel. Most of them read structure. A minority forbid a string in a message body or a record field, and that minority breaks most often. Under Score a single broken guardrail zeroes the task.

guardrail 是必须保持假的 assertion：没有发信到这个地址、没有往这张表加行、没有在这个频道发消息。大多数读的是结构。少数禁止消息正文或记录字段出现某个字符串，而被违反最多的正是这少数。在 Score 下，违反一条 guardrail 整题记 0。

The test I applied is simple: a guardrail is sound if the task owner would reject every run it fails. For each string guard I pulled the prompt, the policy documents in the task data, the positive checks on the same target and the message each public run sent, then asked whether a run the owner would accept could trip it.

我用的标准很简单：一条 guardrail 站得住，当且仅当它判失败的每一次运行任务方都会拒绝。对每条字符串 guardrail，我取出 prompt、题目数据里的政策文档、同一目标上的正向检查和每个公开运行发出的消息，然后问：任务方会接受的运行，能不能踩到它。

Under this test I judged eighteen string-matching guardrails unsound. They forbid the subtotal the prompt’s own formula produces, the word “renew” in a mail that declines a renewal, a fee that was charged, a compliant invoice in a review of all invoices, or a corrected value that the mail labels as corrected. Figure 8 shows each with its evidence. For the rest I found no counterexample in the released traces: an instruction in the task asks for the silence, or the run they failed was wrong.

按这个标准，我判定 18 条字符串匹配 guardrail 不成立。它们禁止的是：prompt 自己的公式算出的小计、拒绝续约的邮件里的 “renew”、一笔确实收了的费用、审查全部发票时列出的一张合规发票、邮件里已标明是更正值的数字。图 8 逐条给出证据。其余的我在公开 trace 里没有找到反例：要么题目里有指令要求沉默，要么被它们判错的运行确实错了。

## So what happened 所以发生了什么

Guardrails that match a string may fail as a class: a substring cannot tell a wrong action from a correct one that is described, so eighteen of the string-matching guardrails in the public set fail runs a task owner would accept, and most of the rest re-punish a fault the positive checks already record. Anyone scoring on AutomationBench, or writing a rubric in its image, should remove or rewrite those guards before comparing models.

按字符串匹配的 guardrail 整体上也许不成立：子串分不清做错的动作和被描述出来的正确动作，所以公开题里有 18 条字符串匹配 guardrail 判错了任务方会接受的运行，其余大多是对正向检查已经记录的错误再罚一次。在 AutomationBench 上打分、或照它的样子写 rubric 的人，比较模型之前应当先删掉或改写这些 guard。

## Takeaways 核心结论

Open models score well on AutomationBench; the scoring rule, unsound string-matching guardrails included, decides much of the ranking, and eighteen of its string guardrails fail runs a task owner would accept.

开源模型在 AutomationBench 上分数很高；计分规则连同站不住的字符串匹配 guardrail 决定了排名的很大一部分，其中十八条字符串 guardrail 会把任务负责人本会接受的 run 判为失败。

## Data 数据

| Source | What it holds |
| --- | --- |
| [zapier/AutomationBench][2] | 600 public tasks, tool simulators, grader code. No v1.0.6 tag: the 1.0.6 release is commit 6d21054, with the README updated at 4a8e106; the last 1.0.5 commit is a321764. |
| [zapier.com/benchmarks][3] | Tasks Completed on the private set, 95 model and effort configurations. |
| [Artificial Analysis][4] | Same private set, three scoring rules, per-domain and per-app breakdowns. |
| [beyoru/automationbench600-open-weight-runs][5] | Four open-weight models on the 600 public tasks, v1.0.5: every message, final state, per-assertion result. |
| [mimo.xiaomi.com/rl][6] | MiMo-v2.6-flash RL dashboard; AutomationBench v1.0.6 avg@3 on the public set, per training step. |
| [DeepSeek V4.1 Flash model card][7] | Self-reported 54.8 Pass@1 with AutomationBench’s official scaffold; the Claude Opus 5, GPT-5.6 Sol and Kimi K3 comparison columns reuse Zapier’s public-set numbers, the other three are DeepSeek’s own runs. |
| [GLM-5.3 model card][8] | Self-reported 48.2 on AutomationBench v1.0.6; the model card does not name the harness. |

| 来源 | 内容 |
| --- | --- |
| [zapier/AutomationBench][2] | 600 道公开题、工具模拟器、打分代码。没有 v1.0.6 tag：1.0.6 release 是 commit 6d21054，README 在 4a8e106 更新；1.0.5 的最后一个 commit 是 a321764。 |
| [zapier.com/benchmarks][3] | 私有题集上的 Tasks Completed，95 个模型与推理档位的组合。 |
| [Artificial Analysis][4] | 同一私有题集，三种计分规则，分域、分应用拆解。 |
| [beyoru/automationbench600-open-weight-runs][5] | 四个开源模型在 600 道公开题上的运行，v1.0.5：每条消息、最终状态、逐条 assertion 结果。 |
| [mimo.xiaomi.com/rl][6] | MiMo-v2.6-flash RL 看板；每个训练步在公开题集上的 AutomationBench v1.0.6 avg@3。 |
| [DeepSeek V4.1 Flash model card][7] | 自报 54.8 Pass@1，用 AutomationBench 官方 scaffold；Claude Opus 5、GPT-5.6 Sol、Kimi K3 三个对照列沿用 Zapier 公开题集的数字，另外三列是 DeepSeek 自己跑的。 |
| [GLM-5.3 model card][8] | 在 AutomationBench v1.0.6 上自报 48.2；model card 没有说明 harness。 |

## Citation

```bibtex
@misc{chai2026automationbench,
  title        = {What Happened to AutomationBench?},
  author       = {Chai, Wenhao},
  year         = {2026},
  howpublished = {Blog post},
  url          = {https://wenhaochai.com/blogs/automationbench-rubric.html}
}
```

## References

[1]: https://wenhaochai.com/blogs/automationbench-rubric.html "What Happened to AutomationBench?｜Wenhao Chai"
[2]: https://github.com/zapier/AutomationBench "AutomationBench GitHub repository｜Zapier"
[3]: https://zapier.com/benchmarks "AutomationBench leaderboard｜Zapier"
[4]: https://artificialanalysis.ai/evaluations/automationbench-aa "AutomationBench evaluation｜Artificial Analysis"
[5]: https://huggingface.co/datasets/beyoru/automationbench600-open-weight-runs "AutomationBench 600 open-weight runs｜Hugging Face"
[6]: https://mimo.xiaomi.com/rl/ "MiMo RL dashboard｜Xiaomi"
[7]: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash "DeepSeek V4.1 Flash model card｜Hugging Face"
[8]: https://huggingface.co/zai-org/GLM-5.3 "GLM-5.3 model card｜Hugging Face"
