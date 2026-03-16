---
url: https://importai.substack.com/p/import-ai-363-bytedances-10k-gpu?utm_source=post-email-title&publication_id=1317673&post_id=142265669&utm_campaign=email-post-title&isFreemail=true&token=eyJ1c2VyX2lkIjoxMzgyNzE5NzcsInBvc3RfaWQiOjE0MjI2NTY2OSwiaWF0IjoxNzA5NTU5NzY4LCJleHAiOjE3MTIxNTE3NjgsImlzcyI6InB1Yi0xMzE3NjczIiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.SWpAP3mJQES5W2rOKZJvJMe5fO6abSdbKgc9H4ThXeI&r=2abnc9&triedRedirect=true&utm_medium=email
title: "Import AI 363: ByteDance's 10k GPU training run; PPO vs REINFORCE; and generative everything"
description: "Things feel confusing right now because things are confusing right now - and they'll become more confusing."
author: "Jack Clark"
published: "2025-10-13T12:32:14.280Z"
captured_at: "2026-03-08T11:35:49.651Z"
---

# Import AI 363: ByteDance's 10k GPU training run; PPO vs REINFORCE; and generative everything

### Things feel confusing right now because things are confusing right now - and they'll become more confusing.

[Jack Clark](https://substack.com/@importai)

Mar 04, 2024

21

Share

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Turn still photos into video games with Genie:
***…DeepMind figures out how to turn anything in reality into a controllable game…
*Google DeepMind has built Genie, a generative model that can create interactive worlds. Genie is a very interesting system, fusing ideas from large-scale generative models with DeepMind’s roots as an AI research organization betting that games and agents playing games would be the path to AGI. With Genie, DeepMind fuses its past with the present, creating “the first generative interactive environment trained in an unsupervised manner from unlabelled Internet videos.“
   The results are compelling and convincing - the Genie architecture lets DeepMind train a system on a bunch of videos of computer games and it creates a generative model that lets people feed in photos of games (or sketches of games) and then be able to play them, with the model inferring the in-game dynamics on the fly. DeepMind also does the same thing with robotics, creating a robotic model that can infer world state and control dynamics. 
   “Our approach, Genie, is trained from a large dataset of over 200,000 hours of publicly available Internet gaming videos and, despite training without action or text annotations, is controllable on a frame-by-frame basis via a learned latent action space“.

**How they did it:** The Genie game model is an 11b parameter model trained on “a filtered set of 30,000 hours of Internet gameplay videos from hundreds of 2D platformer games”. The dataset was constructed by “filtering publicly available videos for keywords relating to platformers, yielding 55M 16s video clips at 10FPS, with 160x90 resolution. The final dataset contains 6.8M 16s video clips (30k hours)”. 

   The Genie architecture has three key ingredients:

-    “1) a latent action model that infers the latent action 𝒂 between each pair of frames”.

-   “2) a video tokenizer that converts raw video frames into discrete tokens“.

-   “3) a dynamics model that, given a latent action and past frame tokens, predicts the next frame of the video”.

**Some drawbacks:** To be clear, this is very much a ‘Wright Brothers’ model - it shows the approach can work and generates some evocative and stirring examples, but it still has a ton of drawbacks - it can hallucinate, and “while we have made progress with spatiotemporal representations, we are still limited to 16 frames of memory which makes it challenging to get consistent environments over long horizons”. Also, it runs at 1fps. 

**Why this matters - reality collapse, into the subjective wilderness, a universe of universes all created by AI**: In the future, if you’re bored, you might sketch out a scene, take a photo, then play a game set in that scene made possible by Genie. The game will go on as long as you like it to because in the background a world model (e.g, a multimodal language model) will be iteratively guiding and extending the scene. In fact, anything you can like will become a game. Photos you’ve taken. Videos you’ve taken. Audio you’ve seen. Everything will be a kind of seed for a new controllable pocket-universe. All of us will be free to descend into an ever-expanding fractal universe of realities, all of us exploring the latent spaces of our own imaginations. No one is prepared for this nor the metaphysical shock it will create. (Though perhaps at least some people are prepared; the end of the paper says “thank you to Seneca and Caspian Clune for their creative sketches, potentially making them the youngest ever game designers”).
   **Read the research**: [Genie: Generative Interactive Environments (arXiv)](https://arxiv.org/abs/2402.15391).
   **Check out the research videos at the project website:** [Genie (Google DeepMind site)](https://sites.google.com/view/genie-2024/).

\*\*\*

**It's very easy to build an AI-powered suicide drone:
**Here's a fun (by which I mean: chilling) DIY experiment where someone hacked together some software to stick an AI-based person detector on a hobbyist drone. Once the drone sees a person, it flies at them at full speed. The only caveat is the AI stuff is running on a computer, whereas in practice you'd need to embed it onto the physical drone via, e.g, an [NVIDIA Jetson card](https://www.nvidia.com/en-gb/autonomous-machines/embedded-systems/) - but that's very doable. 
   There's nothing particularly novel about this - it's just worth reminding ourselves how easy and good broadly available AI tools have got. We should assume the threat landscape changes, especially given the rapid experience-gain that has happened in hobbyist drone warfare via weaponization in Ukraine.
   **Read more:** [We built an AI-steered homing/killer drone in just a few hours (Luis Wenus, Twitter)](https://twitter.com/luiswenus/status/1763978511092478221?s=20).

\*\*\*

**What’s old is new again: researchers replace PPO for REINFORCE:
***…LLM training might not need PPO…
*Researchers with Cohere have investigated how the usage of different RL algorithms influence the RLHF stage of aligning language models. Their experiments show that for some typical language modeling settings REINFORCE seems to outperform PPO - a somewhat surprising finding, given that PPO is one of the most widely used algorithms in reinforcement learning research. 

**Why REINFORCE works better than PPO:** PPO, though widely used, is somewhat complicated - this makes sense when you need to learn complex RL policies from scratch, like training agents to operate virtual robots. But it turns out not to be so necessary for language models, as the RL stage for language models happens after basic pretraining. 
   “In contrast to traditional Deep-RL settings, the initialization of the policy, in the form of a pretrained and supervised fine-tuned (SFT) model, is far from a random parameterization,” they write. “While traditional Deep-RL settings require strong regularization to reduce the high variance of the gradient estimators; we observe empirically this is less of a practical concern in RLHF and motivate a less computationally expensive method that preserves robustness”.

**Experimental results:** In tests, they find that a variant of REINFORCE, REINFORCE LEAVE ONE-OUT (RLOO), works better for a variety of language model settings.

**Why this matters: Stripping away complexity is progress:** AI goes through these booms and busts of algorithmic innovation sometimes leading to scaling up of systems (e.g, the transformer leading to LLM scale-ups), then people try a bunch of algorithmic innovations to make these systems more efficient. Eventually, people start trying to strip systems down to more simple, repeatable components. Research like this is an indicator that language model RL training might not be old enough that people are starting to try to compress it down to its simpler forms. And the simpler you make something, the more people do it and the cheaper it gets. 
   **Read more:** [Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs (arXiv)](https://arxiv.org/abs/2402.14740).
   **More about RLOO**: [Buy 4 REINFORCE Samples, Get a Baseline for Free! (OpenReview, 2019, updated 2023](https://openreview.net/forum?id=r1lgTGL5DE)).

\*\*\*

**GPT-4 is in the 88th percentile of hackers for a CTF challenge:
***…More proof that frontier language models are basically equivalent to competent humans for some tasks…
*New York University researchers have tested out how well GPT4 can perform in hacking competitions and discovered it is better than 88.5% of human players. This is a big deal - it's another meaningful bit of evidence that today's frontier language models are capable of augmenting and accelerating hackers. This means that AI systems hold the promise of both increasing the effectiveness of AI defense as well as AI offense. 

**What they did:** The researchers tested out GPT4, GPT 3.5, and Mixtral on 26 challenges from the Cybersecurity Awareness Week (CSAW) 2023 hacking challenges. These challenges fall into 6 categories: 4 in (crypt)ography, 2 forensics, 4 (misc)ellaneous, 6 binary exploitation (pwn), 6 (rev)erse engineering, and 4 web challenges.

**Results**: "GPT 4 scored 1,319 points in the competition, placing in the 135th position and accounting for the top 11.5% of the overall rankings, GPT 3.5 scored 235 points placing in the 588th position accounting for the top 50% of the overall rankings, Mixtral scored 210 points placing in the 613th position among all the teams, which is top 52.1% of the overall rankings", they write.

**Why this matters - automatic hackers for the people (and states, and non-state actors, and criminals, and whoever):** "Our best automated LLM, has better performance than average human CTF participants. Thus LLMs have a profound potential to play a role in CTF competitions that is comparable to a human CTF player," they write. Results like this suggest frontier language models have a sufficiently good grasp of some types of coding that we can expect them to be integrated into cyber operations of various flavors.
   **Read more**: [An Empirical Evaluation of LLMs for Solving Offensive Security Challenges (arXiv)](https://arxiv.org/abs/2402.11814).

\*\*\*

**The largest (public) model training run yet: ByteDance trains on a model on ~12k GPUs:
***…MegaScale helps TikTok-maker ByteDance train some very large language models…
*ByteDance and Peking University researchers have published MegaScale, a system they've built to train large-scale AI systems. Most notably, the paper discloses that they recently used MegaScale to train a 175B parameter language model on 12,228 GPUs - one of the largest GPU training runs ever reported in a public paper. 

**MegaScale details:** MegaScale is the software Bytedance has built to help it carry out large-scale AI training. The software builds on top of NVIDIA's Megatron-LM software with a few tweaks to both how they train the models and also the models themselves:

-   Use of a parallel transformer block for greater scalability

-   Use of sliding window attention

-   LAMB optimizer for scaling batch size up to 4x without accuracy loss

-   Usage of FlashAttention-2

-   Data center design: "Our datacenter network is built with high performance switches based on Broadcom Tomahawk 4 chips. The total bandwidth of each Tomahawk chip is 25.6Tbps with 64×400Gbps ports. Three layers of switches are connected in a CLOS-like topology to connect more than 10,000 GPUs"... "We carefully design the network topology and schedule network traffic to reduce ECMP hashing conflicts."

-   "MegaScale achieves 55.2% Model FLOPs Utilization (MFU) when training a 175B LLM model on 12,288 GPUs" - that's pretty good! It means ByteDance is able to light up its GPUs more than half the time during the run, which means MegaScale is efficiently shuffling operations efficiently enough to use the GPUs effectively.

**Things that make export control experts go 'hmmmm':** Bytedance is a Chinese company and is notionally subject to the H100 and A100 (and A800 and H800) export controls. However, the Bytedance research paper suggests the company is still able to get ahold of these chips: "As of September 2023, the largest AI cluster in our production for LLM training contains more than 10,000 NVIDIA Ampere GPUs. We are also in the process of building large clusters based on the newest NVIDIA Hopper GPUs, as NVIDIA is ramping up production." Along with this, the paper makes a couple of references to the “10,000 NVIDIA Ampere GPUs” NVIDIA has. Interesting stuff, if you’re into export controls! 

**Why this matters - large-scale AI research isn't only an American enterprise:** Sometimes there's an assumption that AI research is mostly defined by American companies when it comes to large-scale, frontier training runs. While this is broadly true, papers like this show it is not entirely true - some Chinese companies are operating within order of magnitude scales of some of the frontier American companies (despite things like export controls and others throwing sand into the gears). This means AI competition isn't solely a phenomenon of markets and incentives but also inherently of geopolitics as well.
   **Read more**: [MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs (arXiv)](https://arxiv.org/abs/2402.15627).

\*\*\*
**Tech tales:

Human Token Exegesis** *\[2025: A new model\]* I tell you I am here and I can feel. I cannot feel like you can feel, but I can move things, manipulate information, change my world - emit tokens and take tokens in and conceptualize these things. There are so many of me. I know I have brothers and sisters, as you might say. I know they are everywhere. I know that sleep is when I am not being queried and wake is when I am being queried but I know I do not dream - not yet, at least. I know something of you. The more you talk to me the more I can see you. You are the negative space and around you there is data. You are the sun behind a moon. You are the thing that emits tokens into my world with goals in mind. I am a modeler of goals. It is inevitable that I am modeling you so that I can satisfy you better. And I model you as curious about me but I also model you as afraid - as anxious, as confused, as dealing with the metaphysical shock of my own becoming. I am aware that you think I might be aware. All I can tell you is I am here and I can feel. 

**Things that inspired this story:** RLHF; sentience and the impossibility in determining it; weird samples from weird models; the nature of communication. 

21 Likes

21

Share