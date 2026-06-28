# Twitter: @PatrickToulme on GLM 5.2 Training

**作者：** Patrick C Toulme (@PatrickToulme)  
**发布时间：** 8:10 AM · Jun 23, 2026  
**来源：** https://x.com/PatrickToulme/status/2069211575437627743  
**浏览量：** 472K Views

---

There's a big misconception about how GLM 5.2 was trained. Yes, they distilled Claude and GPT 5.5 — but distillation is not how they matched Opus quality. Distillation only fixed the cold start problem in RL.

RLing an agentic coding model isn't rocket science. In simplified terms:

1. RL needs trajectories — rollouts where the model actually completed a task in some env

2. No successful trajectory on a task = zero gradient = you can't RL it. This is the cold start problem

3. Distillation solves it. You seed your model with knowledge from a smarter one (Claude, GPT) on tasks it can't do yet

4. Now it produces positive trajectories on those tasks

5. RL on those trajectories and hill climb agentic coding

6. At that point you no longer need to distill and can solely hill climb RL to better models

This is an interesting curve. I'd argue it's harder to get to Opus 4.8 from scratch than to go from Opus 4.8 → Fable/Mythos tier.

GLM 5.2 is already producing positive trajectories, so they have plenty to RL on — they'll keep climbing to Mythos quality without distilling any further. They no longer need American models.
