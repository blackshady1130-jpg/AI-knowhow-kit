# 智谱唐杰老师的最新推特，讨论long-horizon task、模型训练、组织架构等

> 来源：https://x.com/jietang/status/2054222017566855508


Recent thoughts:
The Shift to Long-Horizon Tasks
The most likely breakthrough this year will be in long-horizon tasks. We are moving toward a stage where Large Language Models (LLMs) learn to complete extended, complex missions by interacting with Agent environments. This is perhaps where the true value of LLMs lies. Take cybersecurity as an example: imagine a model that continuously hunts for software bugs and vulnerabilities. While it sounds like a search process, it’s actually the model learning the high-level intuition and methodology of a professional hacker. Unlike humans, AI can run 24/7 without fatigue. It could potentially find exploits at a much higher frequwill ency and claim bounties on platforms like HackerOne or BugCrowd. It sounds fun, but fundamentally, it's a revolution that displaces the hacker. If even hackers are being "disrupted," one can only imagine the impact on general programmers.

From One-Person to None-Person Companies
Building on long-horizon capabilities, Autonomous Agent Systems (AAS) will inevitably become the next frontier. Last year, we were discussing the rise of the "One Person Company" (OPC). I didn't expect us to move so quickly toward the "None Person Company" (NPC). It’s an ironic twist—we might all end up as NPCs in this new ecosystem.

Engineering the Impossible: Memory and Learning
To realize the vision above, we must solve three technical pillars: Memory, Continual Learning, and Self-Judging.
I used to think these would require massive paradigm shifts and years of research. However, the pressure from both the technical and application sides is so intense that we are seeing these capabilities emerge through ingenious engineering "tricks":
Memory: Long context windows (1M+) and RAG have significantly bridged the gap.
Continual Learning: While true continual learning remains difficult, the release cycles are shrinking. Global models are updated monthly; domestic models are catching up. If we reach weekly updates by next year, it will effectively function as continual learning.
Self-Judging: This remains the most elusive, yet models like Opus 4.7 are already demonstrating early self-correction and judgment capabilities.

The Self-Evolving Endgame
The most difficult—and most promising—path is Self-Evolution. The current wave is incredibly fierce. I suspect that models like Claude may have already achieved a baseline for self-training: writing their own code, cleaning their own data, generating synthetic data, and then training on it. It might "waste" some compute, but it saves the most precious resources: human labor and time. In the LLM era, speed is everything. Rapid iteration is what creates the cognitive gap between leaders and followers. Claude’s rumored 2-million-chip cluster for next year is likely dedicated to exactly this: autonomous model self-training.
Technical Summary:
1M Context: Necessary baseline.
Memory & Continual Learning: Prerequisites, likely solved first via "tricky" engineering.
Harnessing Environments: The breakthrough point.
Self-Judging: The tipping point.
Full Self-Training: The endgame.

Redefining AGI and the Industry
If this is the road to AGI, then AGI’s definition should be the sum of all human collective intelligence, not just an individual’s intelligence. It must possess the creative capacity to produce something as profound as the "Theory of Relativity"—meeting the bar set by Hassabis.
During this transition, every APP will need to be reconstructed as AI-native. In fact, we might move past the concept of APPs entirely. The most significant challenge will be the reconstruction of the operating system itself. In the future, you won’t see a traditional desktop; you will see an LLM OS, where applications are "generated on demand." This challenges the 80-year-old Von Neumann architecture and represents a total upheaval of the computer science industry.

The Irreversible Wave
From completing long-horizon tasks to fully autonomous operations, every sector—Security, Finance, Law, E-commerce—will be reshaped. Many friends have reached out lately, asking how to transform their enterprises to keep pace with AI. But few truly realize that this irreversible process has already begun. As this massive technical wave hits, we must be prepared to act, but we must also start thinking seriously about how to regulate it.
