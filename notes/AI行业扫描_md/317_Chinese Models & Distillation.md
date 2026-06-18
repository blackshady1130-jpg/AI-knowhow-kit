# antirez: Chinese Models & Distillation — Thread

**Author:** antirez ([@antirez](https://x.com/antirez))
**Date:** Jun 15, 2026 · 9:43 PM
**Link:** https://x.com/antirez/status/2066516853497684342

---

## Original Post

Another important thing: Chinese models are not strong because they distill US models. Distillation of models via API is *impossible*. If somebody tells you the contrary, they don't understand machine learning:

---

## antirez's Reply Thread (1–7)

**1.**
Distillation would require access to an incredible amount of requests with the *full logits* available, including the ones of the Chain of Thoughts generation, which is summarized.

**2.**
Distilling via API calls is like seeing a few points in a very complex surface, and still being able to reproduce this complex surface. It is sci-fi in mathematical terms.

**3.**
The distills created by DeepSeek in their R1 paper improved the target models (that were already pre-trained on many tokens) because such models had no training for thinking, but the potential capability was there: still such distills were not particularly great.

**4.**
What you can really do instead is to get quality signal for the reinforcement learning pipeline. This is kinda useful but not critical, and in the first instance you need to have a RL pipeline that works, which is where the real engineer is.

**5.**
Distillation is hard even if you have the model available: there are many frontier Chinese models available yet many labs (EU labs as well...) are not able to provide models that are aligned with them.

**6.**
DeepSeek has released details of how they setup their pre-training, SFT, RL pipelines. Those results are even reproduced. Why you more easily trust flying monkeys than reproducible and available results? They showed you they can train large models well.

**7a.**
When somebody insists about this ML absurdity, ask them this: you claim the model learned X capability from Y source, well: show me the information path. Pretraining? Needs trillions of tokens.

**7b.**
RL with verifiers? Absent, requires reward signal from exploration. Full logit? That's the teacher's complete distribution and is NOT there since o1 or alike. So what is the info channel?

**TLDR:**
Stop repeating this nonsense. You are just showing the world you don't understand machine learning even if you have "AI expert" in your bio.

---

## Nathan Lambert's Reply

**Nathan Lambert ([@natolambert](https://x.com/natolambert)) · Jun 15**

This isn't very true. A big part of the problem is that the labs use the term distillation, which is a general post-training technique, in lieu of a specific issue of jailbreaking the API. (1)

There is a second debate of *how* impactful distillation is, but it is definitely helpful. (2) This is entirely based on how the Chinese labs are jailbreaking the APIs to get reasoning traces out, which help bootstrap reasoning behaviors in new domains.

There's a third point (3) which I take an excerpt from my recent piece, where the labs need to be more transparent why especially point (2) is true. From the third piece:

> On the point of distillation, my hypothesis is that API builders don't have an easy time preventing hacks or jailbreaking because it's a deeply grounded property of reasoning models to want to output the reasoning traces, and it would make the model far less intelligent to fully patch the behavior. This is based on a few assumptions:
>
> a) Chinese labs are not just showing up as customers to Anthropic's API and paying for tokens in the intended input-output form. If the Chinese labs are paying for intended use behaviors, despite being banned by the terms and conditions, I don't have a lot of sympathy for the frontier labs manifesting policy actions against this.
>
> b) Reasoning traces are disproportionately effective at seeding behavior in downstream models.
>
> c) Leading labs work very hard to patch the pipeline of these jailbreaks.
>
> So, my logical conclusion is that the model companies would have to weaken their economic position to fully protect their IP. If this is the case, Anthropic would get a lot more sympathy from the AI research community by being transparent. It would also be far easier to have informed policy discussions, and not rely on me proposing Occam's razor explanations for what the API jailbreaking looks like.

There's no need to misinform people because the labs use a bad term. The labs use this term partially to make the discourse confusing, as you're doing.

**References:**
- (1) [The Distillation Panic](https://interconnects.ai/p/the-distillation-panic)
- (2) [How Much Does Distillation Really Matter?](https://interconnects.ai/p/how-much-does-distillation-really)
- (3) [Claude, Fable 5, and New AI Safety](https://interconnects.ai/p/claude-fable-5-and-new-ai-safety)
