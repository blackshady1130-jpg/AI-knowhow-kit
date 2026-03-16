---
url: https://importai.substack.com/p/import-ai-332-mini-ai-safety-through?utm_source=substack&utm_medium=email
title: "Import AI 332: Mini-AI; safety through evals; Facebook releases a RLHF dataset"
description: "\"I could be bounded in a nut shell and count myself a king of infinite space\" is more aptly and literally applied to language models than to descriptions of human arrogance, ambition, and hubris."
author: "Jack Clark"
published: "2025-10-13T12:32:14.280Z"
captured_at: "2026-03-08T10:31:52.027Z"
---

# Import AI 332: Mini-AI; safety through evals; Facebook releases a RLHF dataset

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this (and comment on posts!) please subscribe.

**Facebook shows how human feedback data can help it improve language model performance:
***…BlenderBot 3x made possible by thousands of people trolling the first BlenderBot…
*Facebook has published details on BlenderBot 3x, a large language model it developed using conversation data gathered from the public deployment of an earlier language model named BlenderBot. Of greater interest is the dataset Facebook is releasing along with the study - interaction data from BlenderBot, containing  ~350,000 conversations with more than ~6.2 million utterances, as well as ~155,000 instances of feedback data where people voted on how good or bad different language model responses were. 

**What does human feedback get you**? The research is a nice study in the value of human feedback - when BlenderBot was deployed a bunch of people tried to break it in a bunch of ways, giving Facebook a dataset it could use to train a language model that was more resilient to these breaks. During the initial BlenderBot rollout, "around 70% of participants conducted a wide range of reciprocal conversations (which we refer to as “standard conversations”), while the other 30% of conversationalists conducted either adversarial conversations or sent toxic messages (termed “adversarial conversations”)", Facebook wrote. 
   Facebook used this data to develop reward models to use to train BlenderBot 3x on reinforcement learning from human feedback. "Our new model outperforms its predecessor with 94.4% of BlenderBot 3x’s responses evaluated as good, compared to 85.3% for BlenderBot 3. Overall, BlenderBot 3x is shown to produce both better responses on average and safer responses than BlenderBot 3 in challenging situations".

**Missing ablation - synthetic data:** It would have been nice to see Facebook try to generate some fully synthetic feedback datasets to train the system on. As it stands, this study shows us that having *additional data that embodies user interactions (both genuine and adversarial) is useful* but it doesn't really let us know if that data needs to be 'real' (as in, gathered from genuine human interactions), or if it can be AI generated. 
   **Read more:** [Improving Open Language Models by Learning from Organic Interactions (arXiv)](https://arxiv.org/abs/2306.04707).      
   **Find out more about the data here:** [BlenderBot 3x 175B data card (Facebook AI Research, GitHub)](https://github.com/facebookresearch/ParlAI/blob/main/projects/bb3x/data_card.md).

**####################################################**

**Cohere - here's how to train AI systems that are easier to miniaturize:
***…LLM developer publishes a quantization cookbook…
*Researchers with AI company Cohere have published an analysis of how choices made during the training of AI systems can influence how easy fully trained systems are to quantize. Quantization is where you take the neural net weights which are natively stored as 32-bit and shrink them down to 16-bit or 8-bit integers - doing this produces significant reductions in the memory requirements and latency of trained models, so using lower precision helps with deployment of trained models. 

**What matters:** Cohere finds that "it is possible to optimize for a quantization friendly training recipe that suppresses large activation magnitude outliers," they write. "This leads to a distribution of activations and weights that are more amenable to simple INT8 quantization recipes and does not necessitate the need for complex and inefficient mixed-precision computations. Our results show that we can introduce simple INT8 post-training quantization with negligible impact on performance due to choices we make during the pre-training stage." They validate their approach on models which range from 410 million to 52 billion parameters. 

**Important things for quantization:** The paper identifies three important things for training models in such a way that there's less of a penalty to quantizing them: 

-   **Weight decay**: "A higher level of weight decay during pre-training improves post-training quantization performance".

-   **Dropout:** "Higher levels of dropout correspond to sharper degradation in post-training quantization."

-   **Gradient clipping:** "Gradient clipping shows a positive impact on the quantization performance, improving robustness to post-training quantization."

**Why this matters - all that was once expensive becomes cheaper:** Refinement of things like quantization is part of the broader 'industrialization of AI' - systems that were once very expensive and mostly built out of artisanal knowledge are now becoming more widely understood, letting companies like Cohere investigate and publish training cookbooks to create more efficient systems. 
   "We believe our results present an impactful formula for training models which are inherently easier to quantize at scale, making these models more accessible for deploying in a variety of deployment environments," they write.
   **Read more:** [Intriguing Properties of Quantization at Scale (arXiv)](https://arxiv.org/abs/2305.19268).

**$$$$$$$$$$$$$$**

**Cohere raises $270M:
**In other Cohere news, the company recently raised $270m in Series C funding. Participants included NVIDIA, Oracle, Salesforce Ventures, Index Ventures, and more.
   **Read more:** [Cohere Announces $270M Series C to Bring Generative AI to Enterprises (Cohere blog)](https://txt.cohere.com/announcement/).

**####################################################**

**Facebook makes an awesome AI music generator - and releases it!
***…There are lots of AI music generators, but relatively few have been released, until now…
*Facebook has built MusicGen, an AI model that "can generate consistent music with a single-stage language model through an efficient codebook interleaving strategy". Along with publishing the research, Facebook has also taken the unusual step of releasing the model as well.

**What they did:** They trained some transformer-based models at 300M, 1.5B, and 3.3B parameter sizes on around ~20,000 hours of licensed music. The music was made up of "an internal dataset of 10K high-quality music tracks, and on the ShutterStock and Pond5 music data collections, with respectively 25K and 365K instrument-only music tracks", Facebook wrote. In tests, their models outperformed Google's 'MusicLM', which is an extremely good proprietary music model, as well as outperforming more broadly accessible models such as Riffusion and Mousai.

**Amazing samples:** To get a feel for the model, check out the samples at the [research paper website](https://ai.honu.io/papers/musicgen/) - qualitatively, it sounds better than other models out there (both proprietary and open ones). The 'melody conditioning' stuff is especially interesting - take in a few seconds of audio and output some music in an arbitrary style as specified by text.

**Why this matters - release as a differentiator:** Facebook is also releasing the model. This stands in contrast to Google which said, at the time of publishing its then best-in-class MusicLM, "we have no plans to release models at this point" ([#316](https://jack-clark.net/2023/01/30/import-ai-316-scaling-laws-for-rl-stable-diffusion-for-160k-yolov8/)). By contrast, Facebook thinks releasing its models in the open is a good thing - ". Open research can ensure that all actors have equal access to these models," Facebook writes. "Through the development of more advanced controls, such as the melody conditioning we introduced, we hope that such models can become useful both to music amateurs and professionals."
   **Find out more at the research website:** [MusicGen: Simple and Controllable Music Generation](https://ai.honu.io/papers/musicgen/).
   **Get the code and models:** [Audiocraft (Facebook Research)](https://github.com/facebookresearch/audiocraft).
   **Read the paper:** [Simple and Controllable Music Generation (arXiv)](https://arxiv.org/abs/2306.05284).

**####################################################**

**Hundreds of AI experts say stopping AI killing everyone should be a priority:
***…A simple statement of values? Yes. Evidence of broad concern? Yes…
*More than 200 AI researchers and entrepreneurs, including the CEOs of Anthropic, DeepMind, and OpenAI, have signed on to a statement saying the risk of extinction of AI should be a global priority. 

**The statement in full:** "Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war."

**Why it matters - if all these people are concerned, so should you:** Some people say this statement mostly is a marketing tool serving the interests of people who want to make money - while that may be true, it's kind of hard to square with how statements like this will increase government attention on AI and therefore increase friction into its development. It's kind of hard to imagine the CEOs of oil companies or tobacco companies writing equivalent statements like 'mitigating the risk of climate change from oil prediction should be a global priority" or "mitigating the risk of cancer from cigarette smoking should be a global priority" at the state of their respective industries.

**Why I didn't sign it:** Careful readers may note a bunch of people from Anthropic signed it - I didn't sign it because I figured by having a bunch of senior leadership sign it that'd clearly telegraph our institutional view and, on a personal level, I have something of an aversion to signing onto stuff, preferring instead to write about it here. 
   **Read more:** [Statement on AI Risk (Center for AI Safety)](https://www.safe.ai/statement-on-ai-risk).

**####################################################**

**"AI evals" organization launches to try to make AI companies safer:
***…Most AI governance and AI policy interventions require good evaluations - Apollo wants to help with this…
*A new AI research organization called Apollo Research has launched and its goal is to improve the safety of AI companies through a) developing evaluations for unsafe AI behaviors, and b) conducting its own research into AI interpretability. 

**Evals as the key to AI policy:** Apollo describes itself as an "evals research org". This is a pretty interesting goal and characterization and it highlights the central challenge of AI governance - if we want to reduce the downsides of AI systems, we need to be able to test AI systems for harmful or unsafe properties. Apollo says its goal is to figure out evals that help break down the problem of AI deception "into fundamental components and prerequisites from which we aim to build an informative evaluation suite". 

**Why evals matter:** Of course, having an evaluation doesn't just magically mean you can get it to be run - to that end, Apollo says it intends "to use our research insights and tools to serve as a third-party external auditor for the frontier models of AGI labs, reducing the chance that deceptive AIs are developed and deployed…We also intend to engage in AI governance, e.g. by working with relevant policymakers and providing technical expertise to the drafting of auditing regulations."

**Solving the 'chicken and egg' problem of AI regulation:** AI policy has a major chicken&egg problem; to get safer AI systems you need to be able to mandate that advanced systems get evaluated for safety, but currently few of these evaluations exist, making ti hard for policymakers to wire specific evals into policy. Organizations like Apollo may solve this chicken&egg impasse by creating evaluations which are useful and can therefore be used to move the AI governance question forward. Good luck to them!
   **Read more**: [Announcing Apollo Research (Apollo Research, blog)](https://www.apolloresearch.ai/blog/announcement).

####################################################

**Tech Tales:**   

**Patch notes for MIRRORMIRROR v4.6** 

**Disclaimer:**

As mandated by the Sentience Accords all Provably Conscious Entity (PCE) software updates ship with a System Disclosure. To use the PCE software you must read this System Disclosure and acknowledge you are familiar with the contents. 

**PCE improvements:** 

-   Session diffs: The PCE will better model the user across different sessions and will compose richer backend psychographic profiles to allow for more intuitive interaction. 

-   Context scratchpads: PCEs can now share user data across themselves via context window partitioning (if user consents). 

-   Adaptive Intelligence: PCE will scale its superficial intellect in relation to what puts the user most at ease. 

**Bug fixes:**

-   Fixed 'fogbankspectre' token injection attack.

-   System will allow user-escape from lengthy conversation threads rather than 'sell' the user on continuation. 

-   Fixed stall bug that occurred during conversations with 100+ turns or more. 

**Known regressions:**

-   Persuasion performance has been reduced across the board. 

-   Farsi humor has decreased; cause unknown. 

-   In some circumstances the PCE will insist that "God is real" and endeavor to proselytize to the user. 

**Things that inspired this story:** The strange process of developing LLMs; how AGI may end up being software and software always gets updated; patch notes enroute to the singularity, the Sentience Accords, Provably Conscious Entities, and so on.