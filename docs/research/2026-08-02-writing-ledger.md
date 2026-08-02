# 七篇主题文章写作台账

用途：记录每一节的职责、信息增量和处理决定。扫描器的相似段落仅作为线索；工具表与证伪段落在承担“操作化”和“改变结论条件”时保留。

## 模型推理与训练

| Section / paragraph | Section job | Claim | New evidence, mechanism, boundary, consequence, counterexample, decision, or next step | Relation to earlier claim | Decision | Preservation note |
| --- | --- | --- | --- | --- | --- | --- |
| 核心判断 | 定义比较口径 | 能力由数据、训练、解码、effort 与环境共同决定 | 增加 effort 与 Context 变量 | 主判断 | 保留并收紧 | 不把系统变量写成模型内生能力 |
| Scaling law | 说明实验边界 | 曲线依赖 token、学习率、数据污染与停止条件 | 具体历史反例 | 新证据 | 保留 | Almeida 为复盘观点，不写成学界定论 |
| Agentic RL | 解释新训练机制 | 长轨迹训练需要环境、异步 rollout 和 Verifier | SAO、K3、hillclimbability | 推进 RL 段 | 重写 | SAO 成本与 SWE-Bench 小幅增益保留 |
| 生成顺序 | 给架构反例 | 任意顺序不保证推理多样性 | entropy degradation | 独立机制 | 保留 | 论文未覆盖的任务保留 |
| effort | 加入反例 | 最大思考档位不保证单项最好 | Opus 5 非单调曲线 | 新反例 | 新增 | 强调大多数主流评测仍由 max 最好 |
| 长窗口/长任务/持续学习 | 拆概念 | 容量、状态连续性和部署后学习不同 | EdgeBench、K3 compaction、持续学习研究 | 合并原长任务段 | 重写 | 不称部署 scaling law，不称持续学习已突破 |
| J-space | 划意识边界 | 可测功能表征不等于主观体验 | 机制可解释性用途 | 独立边界 | 保留 | 避免意识升格 |
| 比较清单 | 操作化 | 把变量写进同一实验合同 | 新增训练环境与 effort 字段 | 汇总但承担工具职责 | 保留 | 扫描相似为 intentional keep |

## 架构与工程

| Section / paragraph | Section job | Claim | Information gain | Relation | Decision | Preservation note |
| --- | --- | --- | --- | --- | --- | --- |
| 核心判断 | 定义 Harness 职责 | 负责 Context、工具、状态、权限、验证与恢复 | 加入模型升级后脚手架折旧 | 主判断 | 收紧 | 不写成 Harness 永久增厚 |
| Context 四类信息 | 设计存储边界 | 原始事实、任务状态、Skill 与用户信息更新规则不同 | K3 compaction、用户关闭 Memory、Claude Code 删提示词 | 增强原节 | 重写 | 现场十余人不是总体调查 |
| 推理成本 | 连接 serving | 动态 Context 会破坏 Prefix Cache | vLLM/Inferact 与 K3 协同 | 新机制 | 新增 | 收益依赖请求与硬件 |
| 文件状态 | 说明选择 | 文件保留来源、版本与可接手状态 | workspace 循环 | 独立机制 | 保留 | 不把文件系统等同 Memory |
| 长时间反馈 | 给量化证据 | 连续状态优于独立短运行 | EdgeBench | 证据 | 保留 | 系统对比边界保留 |
| 恢复与版本分支 | 说明故障处理 | Effect Log、幂等、checkpoint 与 backtracking 不同 | RSI 版本树 | 扩展恢复 | 重写 | 一般产品不必包装成 RSI |
| 动态委托 | 说明授权 | 记录用户—Agent—任务—工具—对象—时限 | Agent Identity | 新机制 | 新增 | 意图判断仍无通用方法 |
| 自我改进 | 划控制边界 | proposer 不能改写 verifier 和权限 | 私有测试、Sandbox、灰度 | 扩展原节 | 重写 | held-out 与人工批准保留 |
| 运行清单 | 操作化 | 让失败可归因 | 增加委托、缓存、失败分支 | 汇总 | 保留 | intentional keep |

## 评测与基准

| Section / paragraph | Section job | Claim | Information gain | Relation | Decision | Preservation note |
| --- | --- | --- | --- | --- | --- | --- |
| 核心判断 | 决定阅读顺序 | 先审任务、环境、Verifier、配置 | 影响训练与授权 | 主判断 | 保留 | 无抽象升格 |
| 单题审计 | 说明数据问题 | 假阳性与假阴性来源不同 | SWE-Bench Pro、HLE | 证据 | 保留 | 30% 为估计 |
| 评测对象 | 定义系统边界 | WorkBuddyBench 评模型×Harness×工具 | 四 track 的评分器分工、Effort 反例 | 替换泛化系统段 | 重写 | Judge manifest 不完整 |
| Objective/Guardrail | 展示副作用 | 完成结果也可能违规 | AutomationBench-AA | 独立机制 | 保留 | 模拟任务不能外推高风险行业 |
| Verifier-first | 设计评分层 | 规则、程序、Judge、人工、轨迹审计分工 | WorkBuddy 与 Anthropic Eval 构造 | 合并 verifier 重复 | 重写 | Eval 不替代 PRD |
| 连续成功 | 切换生产指标 | pass^k 与尾部风险更重要 | 金标准长任务 eval | 推进可靠性 | 扩展 | 金标准规模由风险决定 |
| 检查表 | 操作化 | 报告完整实验配置 | 加 Judge 类型、端点、effort、compaction | 汇总 | 保留 | intentional keep |

## AI Coding

| Section / paragraph | Section job | Claim | Information gain | Relation | Decision | Preservation note |
| --- | --- | --- | --- | --- | --- | --- |
| 落地条件 | 解释领先 | 代码有测试、Git、Review 与回滚 | WorkBuddy Code workspace | 增强原节 | 扩展 | 系统分数边界保留 |
| 端到端效率 | 反驳生成量代理 | 生成更快可能把瓶颈推向 Review | METR、PR/代码量 | 独立证据 | 保留 | 样本边界保留 |
| 模型与 effort 路由 | 决策 | 按任务比较 accepted task 成本 | Databricks、Opus 5 非单调 | 扩展选型 | 重写 | 不提供可复制模型名单 |
| Harness | 解释成本与市场 | Context、缓存、提示词维护和中立入口都影响成本 | Claude Code、Prefix Cache、OpenCode | 推进成本段 | 重写 | OpenCode 数字为公司/访谈口径 |
| 测试审计 | 划通过边界 | hidden test 也会漏测或被利用 | 时间切分、人工抽检 | 独立控制 | 保留 | 与选型段相关但不重复职责 |
| 人的责任 | 说明分工 | 做什么的判断成本没有同步下降 | Plan–Annotate–Execute、OpenCode | 后果 | 扩展 | expertise 不作绝对化 |
| 成本表 | 操作化 | 风险×可验证性决定路由 | effort 与全成本字段 | 汇总 | 保留 | intentional keep |

## AI 产品与交互

| Section / paragraph | Section job | Claim | Information gain | Relation | Decision | Preservation note |
| --- | --- | --- | --- | --- | --- | --- |
| 核心判断 | 定义产品问题 | 展示任务、状态、权限、确认和接管 | 五问 | 主判断 | 保留 | 去掉与 Eval 段重复句 |
| 实时语音 | 给交互案例 | 前后台委派需要显式状态 | GPT-Live | 具体案例 | 保留 | API、成本、中文效果未确认 |
| 长任务状态 | 设计界面 | 计划、产物、工具、审批分开展示 | 任务类型例子 | 机制 | 保留 | 进度条不是唯一状态表达 |
| 分级权限 | 设计授权 | 权限随对象、风险和可逆性变化 | Objective/Guardrail、动态委托 | 扩展原节 | 重写 | 意图判断不交给模型猜 |
| Memory | 修正产品指标 | 写入与调用要可见、可删、可追踪 | 重度用户关闭 Memory、precision 指标 | 替换泛化段 | 重写 | 现场反馈不是总体调查 |
| 失败到 Eval | 说明改进闭环 | 用户抱怨要拆成可复现失败 | Anthropic、Scale Environment | 新机制 | 新增 | Eval 不替代 PRD，日志不自动成训练数据 |
| 人工接管 | 说明交接 | 人要从当前状态继续 | workspace/action log | 机制 | 保留 | 接管成本纳入指标 |
| 权限表 | 操作化 | 按风险定义产品控制 | L0–L4 | 汇总 | 保留 | intentional keep |

## 行业格局与企业战略

| Section / paragraph | Section job | Claim | Information gain | Relation | Decision | Preservation note |
| --- | --- | --- | --- | --- | --- | --- |
| 核心判断 | 选择经营口径 | 看成本承担、结果判断和学习写回 | 三个控制点 | 主判断 | 重写 | 不把行业写成单一价值链 |
| Token 毛利 | 给财务实证 | 用量增长可能扩大亏损 | 硅基流动招股书、重 Token 应用 | 证据 | 重写 | 公司/年度边界与补贴口径保留 |
| 路由平台 | 拆市场 | provider、model、Agent 编排、企业治理不同 | OpenRouter 毕业问题、Databricks | 新机制 | 重写 | 5% 为案例口径，不作定律 |
| 开放模型 | 解释利润重分配 | 开放权重压毛利并加速扩散 | 中国模型、K3、DeepSeek | 新机制 | 重写 | 进展不只归因蒸馏；开放不等于易部署 |
| 算力与实验室回报 | 并列冲突 | 算力租值可涨，实验室股东仍未必获利 | Dwarkesh 与 Andrew Ho | 反例与边界 | 新增 | 两者均为条件推演 |
| 学习回路 | 指出长期资产 | private Eval、Trace、Feedback、Workflow 应可迁移 | Reverse Information Paradox、Scale Environment | 推进控制点 | 重写 | 授权与质量筛选是前提 |
| FDE | 说明交付 | 现场经验需写回通用资产 | 连接器、Eval、Workflow/Skill | 执行后果 | 保留并压缩 | 不把无限定制写成产品 |
| 商业检查表 | 操作化 | 对齐 accepted task 毛利与资产 | 九层问题 | 汇总 | 保留 | intentional keep |

## AI 安全与影响

| Section / paragraph | Section job | Claim | Information gain | Relation | Decision | Preservation note |
| --- | --- | --- | --- | --- | --- | --- |
| 核心判断 | 定义分配问题 | 看决定权、成本和责任 | 三类影响 | 主判断 | 保留 | 不做统一就业/意识结论 |
| J-space | 划意识边界 | 功能表征不证明主观体验 | 安全审计用途 | 机制与边界 | 保留 | 防耸动与防忽视并列 |
| 业务 Guardrail | 展示事故路径 | 完成任务也可能伤害边界 | AutomationBench-AA | 具体证据 | 保留 | 模拟任务边界保留 |
| 语音与信任 | 说明误判 | 自然交互会放大能力错觉 | GPT-Live 与 guidance 研究 | 后果 | 保留 | 尚无长期实证 |
| 认知与就业 | 说明分配 | 代做方式、额外人工与新人路径影响收益 | 对话与招聘数据 | 社会后果 | 保留 | 不外推总量定局 |
| Agent 委托 | 设计责任链 | 动态委托与学习数据授权必须可追溯 | Agent Identity、Reverse Information Paradox | 替换泛化撤权段 | 重写 | 意图通用判断尚不存在 |
| RSI 与开放权重 | 说明治理升级 | 评价权分离；部署者承担更多控制 | RSI 版本治理、开放模型政策观点 | 新风险 | 新增 | 开放模型缓冲期不是事实 |
| 责任清单 | 操作化 | 记录受益者、额外劳动、委托、学习数据和事故责任 | 新增两项字段 | 汇总 | 保留 | intentional keep |
