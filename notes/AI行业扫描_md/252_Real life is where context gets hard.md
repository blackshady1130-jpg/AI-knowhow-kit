Title: Tencent Hy Research

URL Source: http://hy.tencent.com/research/100039

Published Time: Wed, 29 Apr 2026 11:04:09 GMT

Markdown Content:
🏠 CL-bench family 🧩 project page：[www.clbench.com](https://www.clbench.com/)

📄 CL-bench Life paper link: [download CL-bench Life paper](https://github.com/Tencent-Hunyuan/CL-bench/blob/main/clbench-life-paper.pdf)

🛠️ CL-bench family 🧩 code repository：[Tencent-Hunyuan/CL-bench-family](https://github.com/Tencent-Hunyuan/CL-bench)

🗂️ CL-bench Life data repository：[tencent/CL-bench Life](https://huggingface.co/datasets/tencent/CLBench-life)

## [](http://hy.tencent.com/research/100039#the-other-half-of-context-learning)The other half of context learning

To truly solve real-world tasks, an AI cannot just rely on what it was trained on. It must learn from what is happening right now—taking in new context, reasoning through it, and remembering what matters. We previously built [CL-Bench](https://hy.tencent.com/research/100025?langVersion=en) to test this ability. However, looking back, we gave the AI **a major shortcut**: we handed it information that was clean, well-organized, and perfectly prepared in advance.

![Image 1: image#100%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026042917341426_2d38060ebb79c1c8f8fc04865c7dcc89.png)**Figure:** Contexts in professional or workplace settings are usually more structured and focused around specific knowledge points **(left)**, while everyday-life contexts are messier, more fragmented, and often span multiple topics **(right)**.

That assumption works in a professional workspace, but everyday human life is completely different. **Think about what we humans face daily:** planning a weekend trip from a noisy family-and-friends group chat, making sense of quick ideas scribbled in a diary, or finding the cause of recurring injuries from months of workout and recovery logs. Life is not a neat document. It is messy, fragmented, and only loosely connected by time.

![Image 2: image#100%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026042714040642_f32c49fb99a632b892ae169423d4ec02.png)**Figure:** Three examples of real-life contexts. **Case 1:** analyzing a long, noisy multi-party group chat with multiple overlapping discussion threads, shifting plans, and scattered attendance constraints to help organize a book club; **Case 2:** synthesizing non-linear personal cycling logs and notes to produce a safety-focused checklist for an upcoming 5-day bike trip; and **Case 3:** analyzing hundreds of pre- and post-injury workout and recovery logs to assess which muscle groups were most affected.

We often underestimate how hard this is for an AI. The original CL-Bench **tested whether a model could master novel, complex knowledge such as rules and use it effectively.** But real life doesn't come with a rulebook. An AI must do more than just understand complex rules; it must **piece together messy, fragmented clues and remain highly robust**.

![Image 3: image#80%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026042701131388_fb5c81ed3a220004b71069645f112867.png)**Figure:** Context-learning scenarios covered by CL-bench and CL-bench Life.

If we want models to become genuine personal assistants, they must truly understand how we live. To make this happen, we introduce **CL-bench Life**.

## [](http://hy.tencent.com/research/100039#introducing-cl-bench-life)Introducing CL-bench Life

**CL-bench Life** is a rigorous benchmark for evaluating context learning ability in real-life settings and guiding future model development. It is fully human-curated and contains **405** context-task pairs. Solving these tasks requires models to reason over messy and fragmented real-life context, rather than relying only on pre-trained world knowledge.

To cover the kinds of context that commonly appear in everyday life, we organize the benchmark into three categories:

![Image 4: image#100%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026042814080246_6da8f6b77d30f47c4dc581e83bce9ae8.png)**Figure:** Context taxonomy of CL-bench Life.

**Communication and Social Interactions (context generated when people interact with others):** This covers everything from private one-on-one messages to chaotic group chats and busy community forums. To succeed here, an AI must read between the lines. It has to untangle complex human relationships, sense hidden emotional shifts, track how a group gradually reaches consensus, and mine the actual useful details hidden in daily chatter.

**Fragmented Information and Revisions (context actively generated as people record and revise their own thoughts, plans or other information):** This includes scattered personal notes, streams of public information, and the messy history of document edits. The challenge for AI is to act like a detective: it must reconstruct a coherent logical thread from messy everyday fragments, or figure out how an idea, plan, or arrangement changed across multiple rounds of revision.

**Behavioral Records and Activity Trails (context passively generated by people's daily activities):** Spanning gaming logs, digital footprints, and long-term personal trackers. Here, we test an AI's ability to look at a trail of actions and understand the hidden reasons behind them. It forces models to analyze long records such as spending histories or fitness logs, understand underlying habits, and spot unusual changes in long-term behavior.

![Image 5: image#100%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026042701152030_09dd8c2662b96ce14928333f055c5580.png)**Figure:** Three cases from CL-bench Life.

CL-bench Life includes **5,348** human-written rubrics, averaging 13.2 rubrics per task. These rubrics are designed to be atomic, which allows us to evaluate model outputs in a comprehensive and fine-grained way.

![Image 6: image#90%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026042701163422_8266e4bfeda1bd42d8f9794eb4ea0a13.png)**Table:** Statistics of CL-bench Life, including counts of tasks and rubrics, average user turns, rubrics per task, and context length in tokens.

## [](http://hy.tencent.com/research/100039#what-we-found)What we found

We evaluated 12 language models on CL-bench Life, with more results available on [our open leaderboard](https://www.clbench.com/). Results show that these frontier models solve only **14.5%** of tasks on average. Even the best model, GPT-5.5 (High), solves only 22.2%. This shows that current models are still not good at handling noisy and fragmented context.

![Image 7: image#90%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026043019320779_f5b7b53822a0a966d2315307ec5cfa1b.png)**Table:** Task solving rate of frontier LMs on CL-bench Life.

This result is lower than what we observed on [CL-bench](https://www.clbench.com/). On CL-bench, the same models solve around 20% of tasks on average. This difference confirms that CL-bench Life tests another dimension of context learning. In CL-bench, the context comes from professional domains and is often clearer, more structured, and more deliberately organized. Models need to **master new knowledge, such as rules or procedures, and use it effectively.** In contrast, the context in CL-bench Life comes from everyday life. It is often messier, less organized, and repeatedly revised over time. Models need to **piece together clues scattered across the context, handle noise, and remain robust.**

This reveals that context learning becomes harder when models move from clear, relatively organized context to messy and fragmented everyday context. The two benchmarks place different kinds of demands on this ability.

**Beyond overall performance, our further analyses reveal several important findings:**

① **Across models, although fully correct solutions are still rare, partially correct ones are much more common.** When we vary the task threshold, which is the minimum proportion of rubrics a response must satisfy to count as correct, pass rates change substantially. As the threshold becomes more lenient, pass rates rise sharply across all models, suggesting that many responses get part of the task right even when they do not fully solve it.

![Image 8: image#70%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026043000473717_7d48c5d0b33aeaf3b6dc17b81c850e14.png)**Figure:** Task pass rates under different rubric thresholds.

Moreover, **the relative ranking of models remains broadly stable across thresholds.** It means that CL-bench Life distinguishes partial understanding from full task completion while still supporting robust model comparisons.

![Image 9: image#90%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026043019324194_a1b2581bc194b1ae0f39b8fb094dcc0e.png)**Table:** Performance across categories and subcategories of CL-bench Life.

② **Different types of context place different demands on context learning.** Even though all contexts in CL-bench Life come from everyday settings, they contain different kinds of information and therefore stress different model abilities. For example, in **communication and social-interaction contexts**, the difficulty comes not only from fragmentation, but also from social relationships and multi-party interaction: useful details are scattered across intertwined topics, discussion threads overlap, and references to people and prior messages can be complex. In **fragmented information and revision histories**, models need to integrate disconnected clues and infer how a piece of content changes through repeated revisions over time.

③ **Poor performance on real-life context learning is not simply a long-context problem.** Longer inputs can make tasks harder, but input length alone does not determine difficulty. Once reasoning is enabled, the relationship between context length and performance becomes far less consistent. This shows that the main bottleneck is not simply processing longer inputs, but whether models can reason over highly noisy real-life context.

**This differs from [CL-bench](https://www.clbench.com/), where model performance declines more clearly with context length.** In CL-bench, longer inputs usually mean more new and complex knowledge, rules, or procedures to absorb. But in CL-bench Life, length is a weaker predictor: even shorter contexts can be hard when they are noisy, repeatedly revised, or scattered across many fragments.

![Image 10: image#80%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026042701210198_59b2900aa03cb2182a51cdb520b535b6.png)**Figure:** Task solving rate across context length bins under reasoning and non-reasoning settings.

④ To better understand these limitations, we also analyze model failures directly. Across models, **the dominant failure mode is context misuse:** models often attend to the context, but still misunderstand or misapply it. **This is different from CL-bench**, where misuse often means applying a newly defined rule, procedure, or concept incorrectly. In CL-bench Life, errors more often occur because models fail to reconstruct the full chain of events or the flow of a conversation. For example, they may confuse who a casual ''he'' refers to, rely on early information that has already been overturned by later revisions, or treat a personal activity trail as isolated events rather than evidence of a long-term habit.

![Image 11: image#90%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026042701213922_9eb60bc8bf2b004e4db7d1cc0d5f1d8c.png)**Table:** Distribution of four error types across models.

We further unpack this issue below through a detailed breakdown of model errors in group conversations.

![Image 12: image#50%#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/68558e8d/2026042701221132_c00b57557743e709b8b96933432e0dfa.png)**Figure:** Breakdown of social-context errors in group conversations and meeting transcripts.

**In these contexts, the most common failures are role confusion and speaker-attribution errors:** models often fail to remember who said what, and which statements were being quoted or referred to. For example, in a Slack channel where Alice, Brenda, and Clara collaboratively answer users' recipe and gardening questions, Gemini mistakenly treats Alice, who created the channel and initiated the rules, as the superior, and Clara, who actually made the final decisions, as her subordinate. This leads the model to infer the wrong interpersonal roles in the organization, and then misread a whole chain of reporting relationships.

This shows that understanding group-chat context is not just about tracking what happens over time. Models also need to keep track of participant information, remember who said what, and stay robust as relationships among participants shift across messy multi-party interactions.

Overall, these findings show that **CL-bench Life is not just a harder version of CL-bench, but a complementary test** of whether models can reason robustly over the messy, fragmented, and constantly changing context of everyday life.

## [](http://hy.tencent.com/research/100039#the-end)The end

Taken together, the results from CL-bench Life point to a hard truth: today's most advanced AI models are still struggling to understand our daily reality. This explains a common frustration we all feel. Even when we give an AI our chat histories, scattered notes, or daily records, it still doesn't quite "get it."

We hope CL-bench and CL-bench Life can together push this problem forward **from two complementary directions:** professional-domain, more focused and relatively post-organized context on the one hand, and real-life, more fragmented and less organized context on the other, ultimately making AI systems more intelligent, practical, and reliable.

But the journey doesn't stop here. Utilizing complex context is the key to building AI that actually works in our world. The CL-bench series is a huge step toward helping AI understand context, but a true assistant must also learn how to memorize and organize context over a lifetime.

## [](http://hy.tencent.com/research/100039#acknowledgements)Acknowledgements

Special thanks to **Pluto Zhou.** I hope we can keep working together to push HY's context capabilities forward. I am also deeply grateful to **Shunyu Yao** for devoting his time and care to helping us maintain the quality of work. Thanks to **Yujiong Shen** and **Qianyu He** for their help with writing this blog. Finally, I sincerely thank my advisors, **Tao Gui**, **Qi Zhang**, and **Xuanjing Huang**, for their unwavering guidance and support.

_Written on April 29, 2026. Happy International Workers' Day in advance._
