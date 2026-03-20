# MiniMax M2.7: 开启模型的自我进化

Original MiniMax | MiniMax 稀宇科技

M2.7 是第一个模型深度参与迭代自己的模型。能够自行构建复杂 Agent Harness，基于 Agent Teams、复杂 Skills、Tool Search tool 等能力完成高度复杂的生产力任务。

## 构建模型自我进化智能体

以 RL 场景为例：研究员从实验想法出发，Agent 协助文献调研、完成数据流水线、启动实验、自动监控分析、日志读取、问题排查、代码修复、合并请求以及冒烟测试。在这个场景下 M2.7 能够胜任 30-50% 的工作流。

M2.7 全程自主运行"分析失败轨迹 → 规划改动 → 修改脚手架代码 → 运行评测 → 对比结果 → 决定保留或回退"的迭代循环超过 100 轮，在内部评测集上效果提升 30%。

MLE Bench Lite 的 22 个机器学习任务测试中，最好一次取得 9 枚金牌、5 枚银牌、1 枚铜牌。三次平均 66.6% 得牌率，仅次于 Opus-4.6 (75.7%)、GPT-5.4 (71.2%)，和 Gemini-3.1 持平。

## 真实的软件工程

SWE-Pro 中 56.22% 正确率追平 GPT-5.3-Codex。VIBE-Pro 55.6% 几乎与 Opus 4.6 持平。Terminal Bench 2 达到 57.0%。

面对实际生产环境告警，M2.7 能关联监控指标与部署时间线做因果推理，定位到代码仓库中缺失的索引迁移文件，已多次将线上生产系统故障恢复时间缩短到三分钟以内。

原生 Agent Teams（多智能体协作）：角色边界、对抗性推理、协议遵循、行为分化内化为模型原生能力。

## 专业办公

GDPval-AA 的 ELO 得分 1495（开源最高）。在 40 个复杂 skills (> 2000 Token) 的 case 上保持 97% 的 skills 遵循率。MM-Claw 评测中接近 Sonnet 4.6。

Finance 领域示例：自主阅读台积电年报与业绩沟通会纪要，交叉比对多篇研报，独立设计假设并构建营收预测模型，基于模版产出 PPT、Word 报告和 Excel 图表。

## 互动娱乐

开源 OpenRoom 项目（github.com/MiniMax-AI/OpenRoom），将 AI 互动置入万物皆可互动的 Web GUI 空间。

M2.7 已在 MiniMax Agent 与开放平台上全量上线。

---
Source: https://mp.weixin.qq.com/s/Xfsq8YDP7xkOLzbh1HwdjA?scene=1
