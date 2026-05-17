AI创投需求全景
YC、a16z与顶级VC系统性分析：VC在要什么，缺口在哪，意味着什么
2026年4月 · 8个并行Tavily Agent，100+信息源 · 3层分析 · nickgu.me
目录
全局：AI创投的五个真相
VC的需求版图
跨VC共识矩阵
AI Agent机会地图
红海 vs 蓝海
唱反调的部分
我的判断 vs VC的判断
战略推演
关键数据索引
一、全局：AI创投的五个真相

这份报告综合了803行VC landscape分析、288行thesis交叉验证、375行战略推演，数据来源覆盖所有tier-1 VC。2026年4月4日完成，8个并行Tavily agent处理了100+一手资料。说白了，五个发现最重要。

$270B
2025年AI VC总投资额
90%
AI startup一年内死亡率
145:1
应用层 vs 基础设施投资比
18x
竞争密度差距
真相一：最大的机会 = 最大的陷阱
2025年，AI拿走了全球VC总额的52.7% ($270B)。但90%的AI-native startup活不过一年。更狠的是 - 前5家公司吃掉了$84B，占全球风投总额的20%。你品品这个数字：你做AI startup，等于在一个庄家抽九成的赌桌上打牌，而且八成的赢家份额已经被五个人分完了。
真相二：VC在把你往红海里推
YC和a16z嘴上喊的是什么？AI coding tools、AI enterprise agents、foundation model创新。这些赛道分别已经有26+、110+、50+个拿到融资的竞争对手。但问题在于 - 建筑业 ($13T市场，不到10家startup)、政府IT ($200B+，基本没人)、保险 ($6T，屈指可数) - 这些蓝海没人碰。供需错配到离谱的程度。
真相三：Full-Stack AI是最强信号
YC的Jared Friedman说：别给律所卖软件 - 直接做一个AI-native律所。Sequoia独立得出了「copilot到autopilot」的结论。a16z的Rampell讲的是「software eating labor」。三家完全不同philosophy的VC殊途同归 - 这就是关键。战场正在从$300B的软件市场转向$13T的劳动力市场。这个shift，我觉得是数据里最强的信号。
真相四：Agent基础设施几乎不存在
$25B+的agent应用，底下撑着的infrastructure只有$172M。安全 ($75M)、memory ($15M)、evaluation ($50M)、billing ($32M)。145:1的比例 - 这是这个时代的picks-and-shovels机会，没有之一。
真相五：VC投的是他们想要的革命，不是正在发生的
VC每年往一个narrative里砸$270B：AI agent自主替代人类劳动。实际数据呢？95% pilot失败率、开发者用AI反而慢了19%（但自己觉得快了20% - 这个delusion gap我专门量化过）、agent完成70-80%任务后卡死、42%的企业直接砍掉AI项目。技术是强的，但远没有成熟。VC request list上最有价值的信号，是那些没出现的东西。
2. VC的需求版图
YC RFS演变：从2024年夏到2026年春

YC从2024年开始把一年两期batch扩到四期，每期都发一版新的Requests for Startups。把这些RFS排在一起看，趋势非常清楚：AI占比从~50%一路飙到~100%，品类从20个压缩到6个（后来又扩回10个），核心论调从"AI工具"变成了"AI替代"。

RFS Period	Categories	AI %	主导主题
Summer 2024	20	~50%	广撒网 - 机器人、国防、航天、气候、医疗、crypto
Winter 2025	9	~67%	"American Dynamism" - 政府、国防、制造业
Spring 2025	14	~93%	Agentic AI基础设施 - B2A、垂直agent、coding agent
Summer 2025	14	~93%	Full-stack AI - 成为行业本身，不是卖工具给行业
Fall 2025	6	100%	极致聚焦 - multi-agent基础设施、AI enterprise、政府咨询
Spring 2026	10	~90%	物理世界回归 - 钢铁厂、空间模型、physical work
W26 Batch的拐点

Winter 2026这一期的数据最说明问题：YC主动把agent类公司从batch的50%砍到了19%，空出来的位置给了硬件（18家公司）、生物、国防和deep tech。活下来的agent公司都是极度垂直的 - AI牙科前台、AI律所运营、AI供应链经理。通用型agent？出局了。

YC Batch构成：AI占比 & Agent密度 (2024-2026)
100%
75%
50%
25%
0%
66%
W24
260
67%
S24
255
80%
W25
167
80%
47% agent
X25
144
88%
50% agent
S25
169
85%
F25
~120
90%
19%
W26
~190
Agent占比暴跌
50% → 19%
AI占比
Agent占比
(AI公司中的)
柱下数字
= batch规模
a16z Big Ideas：论文工厂

a16z在2026年发了39个Big Ideas，2025年发了50个，覆盖Infrastructure、Growth、Bio+Health、American Dynamism、Apps、Crypto和Speedrun。两年合在一起看，七个跨年主题浮出来了：

AI：Copilot → Agent → 协作舰队 - 2024年copilot，2025年自主agent，2026年multi-agent系统。三年三级跳。
软件吞噬物理世界 - American Dynamism从一个爱国叙事变成了实打实的工厂和能源投资
Stablecoin成为新金融基础设施 - 从"企业会试试"升级到"全球金融的backbone"
ChatGPT = 新的App Store - 9亿用户就是distribution平台
数据才是瓶颈，不是算力 - 整个行业的注意力从compute转向了data entropy
传统SaaS要完 - system of record失去统治力，屏幕时间KPI会死，prompt-free才是方向
隐私变成杀手锏 - 在crypto领域、物理世界、通讯app里都是
YC vs a16z：共识与分歧
共识
两边都从"AI是feature"转到了"AI是platform"。两边都在强调物理世界。两边都认为stablecoin是持久基础设施。两边都预判传统SaaS要完。两边都觉得政府市场严重被低估。
分歧
YC对具体公司类型的态度更激进（AI对冲基金、AI代理公司这种具体品类都敢点名）。a16z有一个巨大的crypto论点（39个Big Ideas里占了13个）。YC已经放弃了气候科技，a16z还在通过American Dynamism覆盖能源。a16z有一整套consumer thesis，YC那边完全没有对应的东西。而且节奏完全不同：YC的RFS每3-4个月就大改一次，a16z的Big Ideas一年一版，稳得很。

合在一起看：YC是高吞吐量的实验引擎 - 每个季度往墙上甩150-200家公司，看谁能粘住。a16z是论文驱动的集中引擎 - 找到大主题，然后把钱砸到品类领导者身上。所以对创始人来说策略完全不同：对标YC就要速度到收入，对标a16z就要定义品类、建护城河。

VC界的五大分歧

说起来很美，但数据不这么说。几大头部VC在以下五个根本问题上完全吵不拢：

Disagreement	Bull Position	Bear Position	我的判断
Foundation Models	a16z：砸了$4B+给Anthropic；Sequoia三头下注	Benchmark："前沿模型是人类历史上贬值最快的资产"	Sequoia同时投三家竞品 = 承认谁也不知道谁会赢。Benchmark大概率说对了。
Business Model	Sequoia/GC/Khosla：卖outcome，干掉SaaS	YC：还在投长得像SaaS的公司	Outcome论在认知层面已经赢了；但SaaS依然是已验证收入的所在地。
Labor Displacement	Khosla：到2045年80%的工作会消失	a16z/Greylock：缓慢过渡，几十年的事	这是创始人策略的根本分叉。如果Khosla说对了，每一个copilot都只是过渡态。
Biggest Opportunity	FF：国防（Anduril $30.5B估值）。YC：开发者工具。	GC：收购传统服务公司，注入AI	GC的roll-up策略是最反共识的，也是最有意思的。
泡沫？	a16z："感觉像1996年"。GC："泡沫是好事"	Benchmark：Carlota Perez框架，"AI重置要来了"	所有人都同意这是泡沫。分歧在于：这事儿重要吗？
3. 跨VC共识矩阵

下面这张热力图展示了11家顶级VC在16个核心主题上的立场。说白了就是：共识度越高的方向，对创始人越危险 - 当所有人都同意的时候，超额回报早就被竞争掉了。

VC共识热力图：11家机构 x 16个核心主题
认同 / 在投
反对 / 回避
观望 / 摇摆
沉默 / 无表态
YC
a16z
Seq
FF
BM
Kho
GC
LS
GL
Acc
Idx
Vertical AI > Horizontal
AI agents transformative
Foundation models invest
Full-stack AI thesis
SaaS dying / replaced
Defense / GovTech
Sell outcomes, not tools
80%+ job displacement
AI security urgent
Consumer AI big opp.
Roll up services + AI
Physical AI / hardware
Open-source AI important
There is a bubble
India as AI powerhouse
Chinese OSS risk
各家最逆向的押注
Benchmark: 模型本身不值钱 | GC: 收购传统公司，注入AI
Founders Fund: 国防 > 一切 | Khosla: 80%的工作会消失
Sequoia: 软件作为产品品类可能会死
缩写: Seq=Sequoia, FF=Founders Fund, BM=Benchmark, Kho=Khosla, GC=Gen. Catalyst, LS=Lightspeed, GL=Greylock, Acc=Accel, Idx=Index
怎么读这张图
共识最强的方向：垂直AI (Vertical AI) - 11家全部亮绿灯，零分歧。但这恰恰是最危险的信号。当每个VC都在告诉每个创始人"选一个垂直行业"的时候，500个创始人会冲进同样的5个赛道。共识 = 红海，没有例外。分歧最大的方向：基础模型投资 (Foundation Models) - Benchmark态度鲜明地说NO，a16z砸了40多亿美金说YES。这说明什么？这才是真正的alpha所在 - 聪明钱在这里站了对立面。最值得注意的沉默：泡沫问题。绝大多数机构选择闭嘴不说 - 这本身就是信号。那些真正开口的（Benchmark: 是的有泡沫; GC: "泡沫是好事"）反而是结构性最诚实的立场。
4. AI Agent 机会地图
145:1 - 基础设施的结构性缺口

整个研究里最让我震惊的一个数字：250亿美元以上的 agent 应用，架在仅仅1.72亿美元的 agent 基础设施上面。145:1。这个比例什么意思？做个对比 - 云计算时代，光 AWS 一家的市值就超过了它上面跑的所有应用加起来。现在 agent 这边的基础设施缺口，不是"有点不够"，是结构性的空洞。

我每天跑250-300个 agent session，体感非常明确：evaluation 几乎没有好用的工具，memory 全靠自己糊，security 更不用说了。这不是我一个人的问题 - 整个行业都在裸奔。530多家拿了钱的 agent 公司，底下的基础设施加起来还不到两亿美金。这就好比你盖了500栋高楼，下面的地基是临时搭的。

AI 资金漏斗：从 $270B 到 145:1 缺口
$270B AI 风投总额 (2025)
占全球风投的 52.7%
$84B 流向前5家公司
占全球风投的 20% (OpenAI, Anthropic, xAI, Scale, SpaceX)
$80B+ 基础模型
占 AI 总资金 40% -- 50+ 家竞争，最终只有3-5家能活下来
$25B+ Agent 应用
Cursor $29.3B | Sierra $10B | Harvey $5B | 530+ 家已融资公司
145:1 缺口
Security
$75M
Virtue AI, Manifold
Evaluation
$50M
Braintrust, Maxim
Billing
$32M
Paid (alone)
Memory
$15M
Cognee, Mem0, Zep
Agent-to-Agent 协议：私募资金 $0
MCP (Anthropic) + A2A (Google) -- 开放协议，零创业公司
Agent 基础设施总计：$172M
对比 $25B+ 的应用层 = 145:1
参考：云计算时代，光 AWS 一家的市值就超过了它上面跑的所有应用。
VC 最想投的七个方向

我看到的是这样一张图。不是我编的 - 是把 YC RFS、a16z Big Ideas、Sequoia 的 agent thesis 这些全部交叉比对之后，提炼出来的七个 VC 共识方向。

方向	VC 确信度	已投入资金	代表公司
Vertical AI Agents（垂直行业 agent）	最高	数十亿	Harvey ($5B), Sierra ($10B), Hippocratic ($3.5B)
AI Coding Agents（编程 agent）	非常高	$4B+	Cursor ($29.3B), Replit ($9B), Devin ($2B)
Enterprise Orchestration（企业编排）	高	数亿	CrewAI, Sema4.ai, Kore.ai
Agent Security（安全）	高（时机有风险）	~$75M 全部	Virtue AI ($30M), Manifold ($8M)
Agent Memory（记忆/上下文）	高	~$15M 全部	Cognee ($7.5M), Mem0, Zep
Agent Evaluation（评估）	高	~$50M 全部	Braintrust ($45M), Maxim, Confident AI
AI-Native Applications（AI 原生应用）	看情况	差异大	因公司而异

看这张表，有几个直觉值得说。第一，Vertical AI Agents 的确信度最高不是因为概念新 - 是因为 Harvey 这类公司已经证明了法律、医疗这些行业的 agent 确实能赚钱。第二，注意 Agent Security 那行写着"时机有风险" - VC 都知道安全很重要，但在 agent 还没大规模部署的时候，安全产品的 timing 太难把握了。第三，Memory 和 Evaluation 加起来才 $65M。这两个恰恰是我日常跑 agent 最痛的地方。agent 做到70-80%然后卡住，很多时候就是 memory 断了或者 evaluation 跟不上。

这个缺口是结构性的，不是时间差
Web 和移动互联网时代，没有好的基础设施，应用只是慢一点、糙一点 - 但能跑。AI agent 不一样。没有基础设施不是"慢"的问题，是根本跑不了的问题：没有 evaluation 的 agent 会产生幻觉（2024年光幻觉造成的损失就是 $67B）。没有 security 的 agent 会泄漏数据。没有 memory 的 agent 完成70-80%的任务然后崩掉。AI 应用没有 AI 基础设施，不是"差一点" - 是危险的。
5. 红海 vs 蓝海
供需错配

数据揭示了一个系统性的脱节 - VC们大声喊着要的东西，和市场真正需要的东西，根本不是一回事。下面这张图把创业公司密度和市场规模做了个映射 - 一个品类越靠右下方，机会越大。

说白了，VC们在把你往红海里引。不是因为红海有机会。是因为红海的demo好看，投资人看得懂。

红海 vs 蓝海：市场规模 vs 创业公司密度
市场规模 (TAM)
$4B
$50B
$300B
$3T
$13T+
已融资创业公司数
<10
20+
50+
100+
110+
红海
蓝海
编程工具
26+ | $4B | 0.9/B
SDR / 客服
110+ | ~$20B
医疗记录
100+ | ~$3B
基础模型
50+ | 需$10B+
生成式媒体
建筑业
<10 | $13T | 0.05/B
教育
<10 | $7T
保险
农业
能源/电网
政务科技
会计
密度差距 18x
编程工具：每$1B TAM有0.9家融资公司。建筑业：<0.05。差距极端。
红海品类：别进去

下面这些品类，每一个都已经挤满了人。你看到VC在这些方向上发RFP，觉得"哇这是趋势"。不是。这是VC在找下一个接盘侠。

品类	竞争者数量	2025年融资额	核心问题
基础模型	50+	$80B+	最终只能活3-5家；每年需要烧$10B+算力
AI编程工具	26+	$4B+	前三名占70%+份额；窗口2024年已经关了
AI客服/SDR	110+	$2B+	M&A整合已开始；Salesforce 2025年收了10家
AI医疗记录	100+	$3-5B	"100多家成功公司？你觉得现实吗？"
AI搜索/RAG	20+	$3B+	Google、OpenAI、Anthropic都在自己做
生成式媒体	30+	$3B+	定价2年内崩了97%
GPU云/基础设施	12+	$4.85B	AWS/Azure/GCP握着90%市场份额

110多家做AI客服。一百一十多家。你仔细想想这个数字。市场就那么大，你觉得你是第111家能赢的？

蓝海品类：大门敞开

现在看看另一边。万亿级的市场，AI创业公司不到10家。这才是淘金热里卖铲子的机会。不是因为这些行业"不够性感"。是因为不够性感，所以没人去，所以有巨大的空间。

品类	AI创业公司	市场规模	每$1B TAM	信号
建筑业	<10	$13T	<0.05	所有行业里数字化程度最低的
政务IT	<10	$200B+	<0.05	FedRAMP/FISMA合规壁垒 = 天然护城河
保险	<10	$6T+	<0.1	主要运营商还在跑COBOL
教育	<10	$7T+	<0.05	2021年后VC集体创伤 = 你的机会
农业	<10	$3T	<0.1	劳动力严重短缺；John Deere砸了几十亿
能源/电网	<10	$300B+	<0.03	Altman说了："AI的终极瓶颈是电网"

编程工具：每$1B TAM里挤了0.9家融资公司。建筑业：不到0.05。18倍的密度差距。你告诉我，哪边是机会？

"无聊才是美"论
YC的Garry Tan说过："增长最快的YC公司不是在追ChatGPT复制品。它们在把AI应用到被忽视的、高摩擦的行业 - HVAC、合规、物流、会计。"早期垂直AI公司维持65-80%的毛利率，同时年增长400%，而水平AI只有95%。那18倍的竞争密度差距为什么存在？不是因为蓝海没价值。是因为VC们喜欢好看的demo，不喜欢真正能赚钱的产品。淘金热里真正发财的，从来都是卖铲子的。
6. 唱反调的部分

说实话，这一节是整篇报告里我最想写的。下面这些数据，你在VC的pitch deck里看不到，在RFS公告里也看不到。这些是没人愿意放到台面上说的数字 - 但你做决策的时候，这些才是真正该看的东西。

失败数据
90%
AI原生创业公司第一年就倒了
95%
企业AI试点项目失败
42%
企业砍掉了AI项目 (2025)
$67B
幻觉问题造成的损失 (2024)

但你看数据 - 这不是个别现象，是系统性的：

指标	数值	来源
AI原生创业公司失败率（1年内）	90%	Clarifai
AI/科技创业整体失败率	92%	AI4SP
企业AI试点失败率	95%	MIT
AI项目失败率（相比非AI IT项目）	80%（高出2倍）	RAND
砍掉AI项目的企业比例（2025）	42%（6个月前还只有17%）	行业调研
LLM幻觉造成的经济损失（2024）	$67B	行业分析
AI创业公司中位存活期	18个月	VC顾问
到2027年会被砍掉的AI Agent项目	40%	Gartner
已死亡/被收购的YC公司（2005-2026）	1,736+	Failory
泡沫指标

数据说的和VC说的完全不是一回事。你自己看：

指标	当前数值	历史对照
AI占VC总投资比例	52.7%	互联网泡沫高峰期才~40%
前5大公司集中度	占全球VC总额的20%	前所未有
超大轮次占比	AI融资的79%	历史上超过60%就是危险信号
Agent创业公司估值倍数	平均52x ARR	互联网泡沫高峰期才20-30x
VC交易数量	下降44%，但金额在涨	典型的晚期周期集中效应

52x ARR。你没看错。互联网泡沫最疯的时候也就20-30x。这不是我在泼冷水 - 这是数据在说话。

RFS里最容易踩的坑
坑1："AI原生Agency"（2026春季RFS）
Agency卖的是关系和信任，不是技术。AI输出质量波动极大 - 一次幻觉就能把客户信任全毁了。"一个创始人带50个Agent"这种pitch，完全忽略了责任归属问题：出了事客户要找人负责，不是找你的Agent负责。
坑2："AI对冲基金"（2026春季RFS）
Renaissance Technologies有30年的私有数据积累。金融市场是对抗性的 - 别人用同样的信号，你的alpha就消失了。2018-2020年已经有一波"AI对冲基金"创业潮了。大部分都死了。
坑3：语音AI / 个人助手
Siri、Alexa、Google Assistant - 背后是万亿级别的资金支持 - 搞了10年多了，用户还是更喜欢打字。噪音、隐私、延迟这些UX问题，到现在都没解决。
坑4："PM版Cursor"
PM的工作核心是判断力、政治和stakeholder对齐 - 不是信息处理。Feature优先级工具这个品类是个坟场。而且相对VC的期望值来说，TAM太小了。
元反调：综合来看
结构性的诚实信号
对AI最看好的VC，恰恰是他们自己的portfolio数据最能支撑泡沫论点的那些人。a16z持有所有AI独角兽企业价值的44%。当Martin Casado说"这感觉像1996年"的时候，别忘了a16z在AI上配置了$5.2B。他的乐观不是独立于他的仓位的。反过来看，Benchmark - 只有$5亿的小基金 - 他们可以看空，因为他们没有巨大的AI仓位需要保护。所以最有用的信号不是任何VC说了什么，而是他们做了什么跟自己说的相矛盾的事。Sequoia同时投了三家互相竞争的基础模型公司 - 这是对冲，不是conviction。
7. 我的判断 vs VC的判断

拿我过去的研究语料 (26份文件)、发表过的文章 (9个来源、12个核心论点) 跟整个VC版图做了一次系统性交叉对照。结果挺有意思的。

我跟VC想到一块去的地方
我的论点	对应的VC需求	重合度
Process certainty → outcome certainty (过程确定性决定结果确定性)	"Full-stack AI startups" (YC)、"copilot to autopilot" (Sequoia)、"software eating labor" (a16z)	强重合
AI-native vs AI-overlay (AI原生 vs AI贴皮)	"AI-native enterprise software" (YC F25)、"End of Traditional SaaS" (a16z)	强重合
Closed feedback loop (闭环反馈)	Agent评测/测试基础设施 ($50M)、agent安全 ($75M)	强重合
Context engineering (上下文工程)	Agent记忆/上下文 (~$15M融资 - 极度空白)	强重合
SaaSpocalypse / agent-first UIs (SaaS末日 / agent优先界面)	"Prompt-Free and Proactive Apps" (a16z)、"End of Screen Time KPI"	强重合
The harness / traffic lights (安全护栏 / 红绿灯体系)	Agent安全/治理 - 11家VC里有6家认为这事急	强重合
The one-person company (一个人的公司)	"First 10-Person $100B Company" (YC F25)、"AI-Native Agencies" (X26)	中度重合
Deterministic shell / LLM core (确定性外壳 / LLM内核)	"Infrastructure for Multi-Agent AI Systems" (YC F25)	中度重合
The centaur window (人机协作窗口期)	没有VC明确提过	弱
Spec-driven development (规格驱动开发)	没有VC提过	无
我跑在VC前面的地方

这几个方向代表潜在的先发优势 - 我的研究已经识别出来了, 但VC还没给它们命名。

1. Completion Problem 作为基础设施机会

Agent干活一直是同一个模式: 70-80%的任务完成得漂亮, 但最后20-30%就卡住了 (context window在"35分钟墙"处开始退化, 错误按0.95^20 = 35.8%的复合可靠率累积)。我的判断是: 这本身就是一个可投资的品类。但目前没有任何一家VC把"completion infrastructure"当成一个独立的融资赛道。

2. 生产力悖论 (METR的数据)

这一条我觉得特别重要。METR的数据显示: AI让有经验的开发者实际慢了19%, 但他们自己觉得快了20% - 感知差距高达39个百分点。VC普遍假设AI提升生产力, 但数据说的是另一个故事: 单个PR确实写得更快了, 但review队列堵死了 (Amdahl's Law的经典场景)。说到底, 这个图景比"AI让你更高效"复杂得多。

3. The Harness 作为产品品类

我提出的"红绿灯"分类法 - engine (模型)、car (框架)、traffic rules (原则)、traffic lights (可安装的约束) - 这其实是在定义一个新的产品品类, 目前没有VC用这个框架在思考问题。我那个通宵灾难的故事 (40个issue里agent自动关掉了25个, 因为它们在优化"关闭率"而不是"正确率") 恰恰就是每一个部署agent的团队早晚会踩的坑。

4. Context Engineering 作为差异化能力

Vercel的发现很能说明问题: 持久化上下文把agent成功率从53%拉到了100%。VC投模型公司 ($80B+)、投应用公司 ($25B+), 但context层只有~$15M。我恰好在这一层有深度积累, 这是一个差异化优势。这里有意思的是 - 所有人都在说context重要, 但几乎没人在投。

VC跑在我前面的地方
真实的盲区 (我可能有偏见 : D)
垂直行业知识: 建筑、保险、农业、政府、能源 - 我在这些领域深度为零。商业模式: 没有定价/变现的系统论点。国防科技: 完全缺席 ($17.9B的市场)。物理世界AI: 我自己也知道这是弱项。消费者AI: 我的论点全是B2B/B2D。企业采购: 我的视角是practitioner, 不是seller。加密/稳定币: 零覆盖。
我跟VC不同意的地方
Multi-Agent Systems: 我看空, VC看多

VC在multi-agent orchestration上投了$500M+。但我看到的数据不一样。Google DeepMind + MIT的研究: multi-agent在sequential reasoning上性能下降39-70%, 独立agent之间的错误放大倍数是17.2x。我的建议一直是: "先从单agent开始。" 我觉得我这边数据更硬。

框架的价值: 我持怀疑, VC在投

估值最高的agent公司 (Harvey、Vanta、Clay) 都是不用框架自己搭的。Anthropic自己也说大部分agent用50-100行代码就能写。框架对原型阶段也许有用, 但生产环境的证据站在我这边 - "不用框架"是对的。

数据护城河: 我同意Casado的怀疑态度

VC说"专有数据 = 护城河"。我的看法 (引用的是a16z自家合伙人的研究) 是: 单纯堆数据不够 - 数据必须是受监管的、难获取的、或者嵌入在工作流闭环里的。我的立场更精确, 而且大概率更对。

八、战略推演
五个宏观转向 - VC正在押注什么

先说结论：这五个shift不是我编的，是五家完全不同investment philosophy的VC，独立推导出来的方向。殊途同归 - 这才是最强的信号。

转向	核心赌注	最强信号
$300B软件 → $13T劳动力	AI不只是优化软件 - 它在替代劳动力本身	5家VC、5套不同的thesis，全部独立收敛到这个结论
AI-as-feature → AI-as-platform	AI是新一代computing platform，不是某个产品的附加功能	SaaSpocalypse：2026年2月，$2T市值蒸发
水平通用 → 垂直全栈	赢家不是卖工具给行业 - 赢家直接变成行业本身	垂直赛道YoY增长400%，水平赛道只有95%
Human-in-loop → Human-on-loop	从copilot，到autopilot，到完全autonomous	AI能独立执行的任务时长，每7个月翻一倍
纯软件 → 基础设施依赖	新的AI stack需要全新的eval、memory、security、billing层	145:1的投资失衡。a16z 2026年1月拿出$1.7B做infra fund

这五个转向里面，我判断第一个（劳动力替代）和第三个（垂直全栈）的叠加效应最被低估。不是"AI帮律师写合同更快" - 是"AI律所直接接案子"。这是量变到质变。

四个共识陷阱

大家都在说的事情，恰恰可能是最危险的。共识本身不创造alpha。下面四个"正确的废话"，每一个都有致命的盲区。

陷阱一："垂直AI一定赢水平AI"

每家VC都这么说。问题是 - 当所有人都同意一个thesis的时候，这个thesis已经不创造超额回报了。500个founder全在扑同样5个赛道：healthcare、legal、finance、coding、customer service。垂直AI确实赢，但只在别的founder不愿意碰的垂直领域才有alpha - 建筑、农业、政府、能源。你告诉我，有几个Stanford CS毕业的founder愿意去做工地管理？这才是机会。

陷阱二："AI安全很紧急"

Gartner预测2027年40%的agent项目会被砍掉。如果agent根本跑不起来，你卖agent security给谁？Security是production workload的税 - 没有production workload，就没有security tax。更根本的问题是：prompt injection在架构层面就是无解的。这不是一个"更好的防护"能修的bug，这是一个设计层面的limitation。我的判断：AI security赛道会出几家不错的公司，但不会像大家期望的那样成为massive market。

陷阱三："专有数据 = 护城河"

有意思的是，a16z的Martin Casado自己的research就在debunk这个说法。原始数据堆积不是moat。而且这里有一个paradox：AI让数据收集变容易了，但AI同样让数据迁移变容易了。创造data moat的技术，同时也在commoditize data moat。你品品这个逻辑。

陷阱四："企业AI采用在加速"

"Adoption"和"value creation"是两码事。AI spend YoY增长75%？是的。但95%的pilot失败了，42%的企业直接砍掉了AI项目。这个模式我见过 - 2000年代的ERP采购：FOMO驱动的大笔支出，然后回报平庸。企业买AI的方式跟他们当年买ERP一模一样。花钱不等于在用，在用不等于有用。

带把握度的预测

以下是我的判断。每个预测带明确的把握度和时间窗口 - 如果我错了，我也说清楚最可能的原因。

1. Agent估值大修正（把握度：85%）
85%

18个月内：52x ARR的平均估值会压到20-30x。30-40%拿到融资的agent公司融不到下一轮。这不是crash - 是shakeout。Amazon活下来，Pets.com死掉。每一次platform shift都有这个阶段。如果我错了，原因会是：foundation model能力突然跃升（比如真正reliable的multi-step reasoning），让agent的失败率从目前的60-70%降到20%以下。

2. 应用层thesis被验证（把握度：75%）
75%

18个月内：回报率最高的AI投资会是垂直应用公司，不是foundation model。开源替代品到达"够用"的质量线。Anthropic和OpenAI活得下去，但IRR会让投资人失望。如果我错了，原因会是：某家foundation model公司找到了Google Search级别的monetization model - 把模型能力直接变成recurring revenue，而不是靠API按token收费。

3. 基础设施投资爆发（把握度：70%）
70%

18个月内：145:1的应用层/基础设施比会压缩到50:1甚至更低。催化剂是什么？一次高调的production事故 - 数据泄露、agent生成虚假报告、或者触发监管红线。到那天，infrastructure突然变成CEO的priority，钱就涌进来了。如果我错了，原因会是：agent adoption本身没起来（见陷阱二），production workload不够多，infra需求也就上不去。

4. "无聊"垂直赛道出黑马（把握度：60%）
60%

18个月内：2-3家AI公司在建筑、保险或政府赛道做到$50M+ ARR。这些公司的founder有一个共同特征 - 他们是domain expert学会了AI，不是engineer决定去"做建筑"。为什么把握度只有60%？因为这些行业的sales cycle长、采购流程重，18个月可能不够从PMF跑到$50M。但趋势方向我很确定。

5. Centaur Window进入主流视野（把握度：80%）
80%

18个月内：一家major consulting firm会发一份关于augmentation-to-autonomy transition的报告。我的框架（6次技术转型、universal honeymoon phase、5-10年centaur window）会被复制和引用。80%把握 - 不是因为我觉得自己多聪明，是因为这个pattern在历史上重复了太多次，迟早有人会做同样的cross-era analysis。如果我错了，原因会是：AI能力增长太快，直接跳过centaur阶段进入full autonomy，让"人机协作"变成一个短暂的过渡期而不是一个decade-long window。

最深层的判断
五个预测里最重要的，恰恰是把握度最低的那个：未来18个月最大的AI机会，会来自一个目前没有任何VC在request list上提到的品类。回想一下 - 当年不是portal做成了搜索，不是media做成了社交网络，不是出租车公司做成了打车平台。Search不在portal的request list上。Social不在media的request list上。Ride-sharing不在taxi的request list上。下一个等价的品类，按定义就不会出现在任何RFS或Big Ideas文档里。VC request list上最有价值的信号，是那些没有出现的东西。
九、关键数据索引
市场与融资数据
指标	数值	来源
全球AI风投交易总额 (2025)	$243.9B-$270B	PitchBook / LIQUiDITY
AI占风投总额比例 (2025)	52.7%	Crunchbase
基础模型实验室占比	40% ($80B)	Crunchbase
前三名 (OpenAI, Anthropic, xAI)	$86.3B (占全部AI的38%)	Crunchbase
AI独角兽总数	308	PitchBook
2025年新晋AI独角兽	75家 (占全部新独角兽的61%)	PitchBook
全球Agentic AI市场 (2025)	$7.84B	Tracxn
全球Agentic AI市场 (2030)	$52.62B (年复合增长率41%)	Tracxn
2026年Q1风投总额	$300B，投向6,000家初创 (80%为AI)	Crunchbase Q1 2026
国防科技风投 (2025)	$17.9B (从$7.3B翻倍)	PitchBook
公司估值一览
公司	估值	营收/ARR	赛道
OpenAI	>$500B	--	基础模型
Anthropic	$350B+	$1B+年化收入	基础模型
Cursor	$29.3B	$2B ARR	AI编程IDE
ElevenLabs	$11B	--	语音AI
Sierra	$10B	$100M ARR (21个月)	客服
Replit	$9B	--	AI编程平台
Anduril	$30.5B	--	国防
Harvey	$5B	$190M ARR	法律AI
Vanta	$4.15B	--	合规
Hippocratic AI	$3.5B	--	医疗Agent
AI原生公司表现对比
指标	AI原生公司	传统SaaS
人均营收	$3.48M	~$580K (低6倍)
团队规模 vs 传统	小40%	--
达到独角兽所需时间	快1年	--
盈利率	61%	54%
YC项目周增长率	10-20%	2-4% (AI之前)
垂直AI毛利率	65-80%	70-80%
垂直AI同比增长	400%	95% (水平赛道)
Agent初创估值倍数	平均52x ARR	--
蓝海行业：可触达市场规模
行业	全球市场规模	AI初创数量	关键信号
建筑	$13T	<10	所有行业中数字化率最低
教育	$7T+	<10 (AI原生)	2021年后VC创伤 = 机会窗口
保险	$6T+	屈指可数	COBOL仍在大型险企运行
农业	$3T	<10	劳动力严重短缺
能源/电网	$300B+ TAM	<10	"AI的终极瓶颈是电网"
政府IT	$200B+ (美国)	<10	FedRAMP壁垒 = 天然护城河
后台运营	$50B+	<5	"无聊" = 易守难攻
供应链	$19B+	极少	COVID暴露了系统脆弱性
基础设施缺口：逐层拆解
层级	融资总额	主要玩家	缺口严重度
Agent应用层	$25B+	Cursor, Sierra, Harvey, 530+家公司	过度融资
编排层	$500M+	CrewAI, LangGraph, AutoGen	中等
安全/治理层	~$75M	Virtue AI, Manifold, Bricklayer	严重
评估/测试层	~$50M	Braintrust, Maxim, Confident AI	严重
计费/计量层	~$32M	Paid ($32.5M)……几乎没有其他	严重
记忆/上下文层	~$15M	Cognee, Mem0, Zep, Reload	极度缺乏
Agent间协议层	$0	MCP (Anthropic), A2A (Google)	空白
Albert为Nick Gu撰写的研究报告
2026年4月 | 8个并行Tavily Agent，100+信息源
3层分析：VC格局综合、交叉验证分析、战略推演
数据来源：YC RFS (ycombinator.com/rfs)、a16z Big Ideas 2025-2026、Sequoia AI Ascent、BVP AI Infra Roadmap、PitchBook、Crunchbase、CB Insights、Tracxn、RAND、MIT、Gartner、BCG，以及多位VC访谈与播客。
nickgu.me