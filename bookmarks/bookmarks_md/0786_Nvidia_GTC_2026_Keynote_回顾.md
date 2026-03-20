# Nvidia GTC 2026 Keynote 回顾

Original 渣B 渣B | zartbot

## TL;DR

又是一年一度的GTC，恰逢今年刚好是CUDA 20周年。Jensen整个Keynote对CUDA生态进行了一个回顾，然后接着谈到了推理时代到来并预测了推理市场的持续性增长。然后就是最激动人心的硬件发布环节，发布了Groq 3 LPU 以及整个Rubin系列家族，有一些新的变化。接着就是OpenClaw以及Nvidia自己的NemoClaw的发布。最后谈论了一下Physical AI 和Robotics。

## 1. CUDA 20年

老黄从2001年开始回忆可编程的Pixel Shader开始的经历。介绍了RTX相关的DLSS5的demo，DLSS 5引入了实时神经渲染模型。然后介绍CuDF用于处理结构化数据，以及cuVS(Vector Search)处理非结构化数据。

通过GCP/AWS/Azure/Oracle/CoreWeave以及他们客户的例子来展示整个软件栈。介绍了和Dell合作的on-prem部署。

对Quant从传统的特征工程到AI模型自动发现特征因子做了很详细的介绍。AI native公司中国内模型公司上了3家：Deepseek / Kimi / Qwen。

## 2. 推理时代

老黄回忆了过去两三年的几个代表时刻：ChatGPT带来的LLM时代，o1带来的LRM时代，Claude Code带来的Agentic时代。宣告整个推理的时代已经完全到来，预测了整个市场持续性的增长。

强调NVL72和nvfp4从Blackwell带来的变化以及对推理的优化，功耗的降低，性能的增长和推理成本的快速下降。再次强调了AI Factory的概念。

## 3. 硬件

从最早的DGX开始回顾：Volta / Ampere / Hopper / Blackwell，整个Rubin这一代露出全貌，Groq 3 LPU成为发布重点。

展示了Groq 3 LPU compute Tray / NVL6 Switch Tray / Rubin Compute Tray。

**Groq 3 LPU**：单颗SRAM增加到500MB（第一代为220MB），带宽增加到150TB/s（第一代80TB/s）。这一代仅支持FP8，接下来会出Groq L35支持nvfp4。

**Rubin + Groq 架构**：Rubin做Prefill（Compute Bound和Memory Capacity Bound），Groq 3做Decode（Memory Bandwidth Bound）。同样功耗下Vera-Rubin + Groq 3 LPX还可以相对Rubin提升1倍的能效。

**Vera CPU**：单个Vera Compute Tray集成8颗Vera处理器，每个88核，支持8通道LPDDR5x，单socket支持1.2TB/s内存带宽。

**Roadmap**：
- Rubin Ultra + Groq 3.5(LP35)支持NVFP4
- Oberon机框8个机柜并联支持NVL576
- Feynman采用3D堆叠，LPU从C2C切换到NVLink，全面支持CPO光互连
- CX10和BF5排到2028年

Rubin已点亮交付给微软在测试。

## 4. Agentic Computing

老黄谈论OpenClaw，介绍Agentic Computing与Linux/HTTP/HTML一样带来的变革。宣告企业IT从SaaS到Agent-as-a-Service的转变。发布NemoClaw，强调安全和易部署能力，以Agent为中心构建生态。

介绍了Nvidia的开源模型和相应的合作伙伴。

## 5. Robotics & Physical AI

自动驾驶方面：BYD/吉利/现代/尼桑等厂家加入Robotaxi，与Uber合作。机器人方面：KUKA/FANUC/ABB等厂商。配套的整个软硬件平台包括仿真/模拟等，强调GB300训练、RTX6000仿真、Thor终端执行的硬件栈。

针对地球电不够，在研究太空中的抗辐射的Vera Rubin架构。

参考资料：GTC 2026 Keynote: https://www.youtube.com/watch?v=jw_o0xr8MWU

---
Source: https://mp.weixin.qq.com/s/zAcXpurG2o5TeJ05sW01wA
