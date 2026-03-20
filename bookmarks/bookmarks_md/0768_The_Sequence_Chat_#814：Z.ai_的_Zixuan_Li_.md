# The Sequence Chat #814: Z.ai's Zixuan Li Talks About GLM

Feb 26, 2026 · TheSequence

Zixuan Li, Head of Z.ai Global Ecosystem, discusses the GLM models, Chinese open source and more.

## Background

**Q: Can you introduce yourself and tell us about your journey from academy to Zhipu AI?**

I'm Zixuan Li, Head of Z.ai Global Ecosystem, responsible for Z.ai Chat, Z.ai API services, global partnerships, and global branding. When I joined Z.ai, I saw fascinating challenges: product development, partnership building, commercialization, and establishing a global brand.

## The Main Sequence

**Q: What was the original hypothesis behind GLM?**

The original hypothesis behind GLM was that the dichotomy between autoencoding (BERT-style) and autoregressive (GPT-style) models was a false choice. We believed a unified framework could capture the best of both worlds. GLM's autoregressive blank infilling objective was designed to bridge that gap. This DNA still influences our models today.

**Q: With GLM-4 and now GLM-4.7, have you maintained that unique architectural lineage?**

The GLM model architecture today has evolved significantly from its previous versions. We continuously absorb industry best practices while making our own innovations. There is no unified "best practice." The field is moving too fast.

**Q: With GLM-4.5, you moved heavily into MoE architectures. Is MoE purely an efficiency play?**

We see MoE as a superior path to reasoning, not merely an efficiency optimization. The sparse activation pattern allows different experts to specialize in different types of knowledge and reasoning patterns.

**Q: Why does Z.ai continue to release weights?**

We want to expand the cake before taking a bite of it:
1. **Improve accessibility**: Lower barriers for developers and researchers worldwide.
2. **Enable ecosystem innovation**: Community takes our models in directions we hadn't anticipated.
3. **Shape standards**: Help set norms and standards for open models.

Open-sourcing does not cannibalize our business. Demand for GLM has exceeded supply.

**Q: What are the unique technical bottlenecks in building agents that control local devices?**

Three main obstacles:
1. **Speed of operations**: Agents must match or exceed human navigation speed.
2. **Error recovery and robustness**: Humans are incredibly good at recovering from small mistakes.
3. **Context persistence across sessions**: Humans remember what we were doing yesterday.

Latency is important, but error-correction and graceful degradation are the bigger blockers today.

**Q: Is visual data necessary to teach a model 'physics'?**

Vision capabilities are still essential in many scenarios. The most capable systems will likely combine both modalities. The question isn't "text or vision" but "how do we best integrate multiple modalities for richer understanding?"

**Q: What is Z.ai's differentiation?**

Z.ai is relatively more mature in "service" and more committed to the model-as-a-service (MaaS) philosophy. Our soul: we're builders who serve builders.

**Q: What makes GLM-5 unique?**

GLM-5 scales from 355B parameters (GLM-4.5) to 744B total parameters, with 40B active per inference through MoE. It integrates DeepSeek Sparse Attention for the first time. GLM-5 uses "slime," a custom asynchronous reinforcement learning infrastructure. On Vending Bench 2, it ranked first among open-source models and close to Claude Opus 4.5.

## Miscellaneous

**Q: Is there a 'reverse brain drain'?**

For Z.ai, most of our researchers are Z.ai-originated. What attracts talent? The combination of cutting-edge research, pace of iteration, and the chance to see work deployed at massive scale very quickly.

**Q: Do you believe the Transformer architecture is sufficient for AGI?**

I believe the current Transformer architecture has a very high ceiling. Most of the data patterns we'll see in 2027 and 2028 haven't even been created yet. We're still in the early innings.

**Q: Give us one prediction for 2026 that 90% of readers would disagree with.**

Pricing by tokens might no longer be the mainstream business model. LLMs will be charged by the value they create. We don't pay for electricity based on how many electrons flow through our devices.

---
Source: https://thesequence.substack.com/p/the-sequence-chat-814-zais-zixuan
