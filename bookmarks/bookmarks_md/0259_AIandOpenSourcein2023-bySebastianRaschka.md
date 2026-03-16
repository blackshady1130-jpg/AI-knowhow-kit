---
url: https://magazine.sebastianraschka.com/p/ai-and-open-source-in-2023?utm_source=post-email-title&publication_id=1174659&post_id=138171169&utm_campaign=email-post-title&isFreemail=true&r=2abnc9&utm_medium=email
title: "AI and Open Source in 2023"
description: "The Highs and Lows: A Year in Review"
author: "Sebastian Raschka, PhD"
published: "2025-07-19T11:11:10.901Z"
captured_at: "2026-03-08T11:07:07.950Z"
---

# AI and Open Source in 2023

### The Highs and Lows: A Year in Review

[Sebastian Raschka, PhD](https://substack.com/@rasbt)

Oct 23, 2023

114

11

14

Share

We are slowly but steadily approaching the end of 2023. I thought this was a good time to write a brief recap of the major developments in the AI research, industry, and open-source space that happened in 2023. 

Of course, this article is only a glimpse of the most relevant topics that are on the top of my mind. I recommend checking out the monthly *Research Highlights* and *Ahead of AI #4-12* issues in the [Archive](https://magazine.sebastianraschka.com/archive) for additional coverage.

# Scaling the Trends of 2022

This year, we have yet to see any fundamentally new technology or methodology on the AI product side. Rather, this year was largely focused on doubling down on what has worked last year:

-   ChatGPT with GPT 3.5 was upgraded to [GPT 4](https://openai.com/research/gpt-4)

-   DALL-E 2 was upgraded to [DALL-E 3](https://openai.com/dall-e-3)

-   Stable Diffusion 2.0 was upgraded to [Stable Diffusion XL](https://stability.ai/blog/stable-diffusion-sdxl-1-announcement)

-   ...

An [interesting rumor was](https://www.reddit.com/r/LocalLLaMA/comments/14wbmio/gpt4_details_leaked/) that GPT-4 is a mixture of experts (MoE) models consisting of 16 submodules. Each of these 16 submodules is rumored to have 111 billion parameters (for reference, GPT-3 has 175 billion parameters). 

A GPT-3/GPT-4 meme from the [State of AI report 2023](https://www.stateof.ai/)

The fact that GPT-4 is an MoE is probably true, even though we don't know for sure yet. One trend is that industry researchers share less and less information in their papers than they used to. For example, while [GPT-1](https://arxiv.org/abs/2305.10435), [GPT-2](https://paperswithcode.com/paper/language-models-are-unsupervised-multitask), [GPT-3](https://arxiv.org/abs/2005.14165), and [InstructGPT](https://arxiv.org/abs/2203.02155) papers disclosed the architecture and training details, the GPT-4 architecture is a closely guarded secret. Or to provide another example: while Meta AI's first [Llama paper](https://arxiv.org/abs/2302.13971) detailed the training dataset that was used to train the models, the [Llama 2 model](https://arxiv.org/abs/2307.09288) keeps this information private. On that note Stanford introduced the [The Foundation Model Transparency Index](https://hai.stanford.edu/news/introducing-foundation-model-transparency-index) last week, according to which Llama 2 leads at 54%, and GPT-4 ranks third at 48%.

Of course, it may be unreasonable to demand that companies share their trade secrets. It's still an interesting trend worth mentioning because it looks like we'll continue on this route in 2024.

Regarding scaling, another trend this year was scaling the input context length. For example, one of the main selling points of the GPT-4 competitor [Claude 2](https://www.anthropic.com/index/claude-2) is that it supports up to 100k input tokens (GPT-4 is currently limited to 32k tokens), which makes it particularly attractive for generating summaries of long documents. The fact that it supports PDF inputs makes it especially useful in practice.

Using [Claude 2](https://www.anthropic.com/index/claude-2) to generate a summary of a PDF document

# Open Source and Research Trends

As I recall, the open-source community was heavily focused on [latent diffusion models](https://arxiv.org/abs/2112.10752) (such as [Stable Diffusion](https://github.com/CompVis/stable-diffusion)) and other computer vision models last year. Diffusion models and computer vision remain as relevant as ever. However, an even bigger focus of the open-source and research communities was on LLMs this year.

The explosion of open-source (or rather openly available) LLMs is partly owed to the release of the first pretrained [Llama](https://arxiv.org/abs/2302.13971) model by Meta, which, despite its restrictive license, inspired a lot of researchers and practitioners: [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html), [Vicuna](https://lmsys.org/blog/2023-03-30-vicuna/), [Llama-Adapter](https://arxiv.org/abs/2303.16199), [Lit-Llama](https://github.com/Lightning-AI/lit-llama), just to name a few.

A few months later, [Llama 2](https://arxiv.org/abs/2307.09288), which I covered in more detail in [Ahead of AI #11: New Foundation Models](https://magazine.sebastianraschka.com/p/ahead-of-ai-11-new-foundation-models), largely replaced Llama 1 as a more capable base model and even came with finetuned versions.

However, most open-source LLMs are still pure text models, even though methods such as the [Llama-Adapter v1](https://arxiv.org/abs/2303.16199) and [Llama-Adapter v2](https://arxiv.org/abs/2304.15010) finetuning methods promise to turn existing LLMs into multimodal LLMs. 

Figures from Llama-Adapter V2, [https://arxiv.org/abs/2304.15010](https://arxiv.org/abs/2304.15010)

The one noteworthy exception is the [Fuyu-8B model](https://www.adept.ai/blog/fuyu-8b), which was released only a few days ago on October 17th. 

Annotated figure from [https://www.adept.ai/blog/fuyu-8b](https://www.adept.ai/blog/fuyu-8b)

It's noteworthy that Fuyu passes the input patches directly into a linear projection (or embedding layer) to learn its own image patch embeddings rather than relying on an additional pretrained image encoder like other models and methods do (examples include [LLaVA](https://github.com/haotian-liu/LLaVA) and [MiniGPT-V](https://github.com/Vision-CAIR/MiniGPT-4). This greatly simplifies the architecture and training setup.

Besides the few multimodal attempts mentioned above, the largest research focus is still on matching GPT-4 text performance with smaller models in the <100 B parameter range, which is likely due to hardware resource costs and constraints, limited data access, and requirements for shorter development time (due to the pressure to publish, most researchers can't afford to spend years on training a single model). 

However, the next breakthrough in open-source LLMs does not have to come from scaling models to larger sizes. It will be interesting to see if MoE approaches can lift open-source models to new heights in 2024.

Interestingly, on the research front, we also saw a few alternatives to transformer-based LLMs in 2023, including the recurrent [RWKV](https://arxiv.org/abs/2305.13048) LLM and the convolutional [Hyena](https://arxiv.org/abs/2306.15794) LLM, that aim to improve efficiency. However, transformer-based LLMs are still the current state of the art.

Annotated Hyena LLM architecture from [https://hazyresearch.stanford.edu/blog/2023-06-29-hyena-dna](https://hazyresearch.stanford.edu/blog/2023-06-29-hyena-dna)

Overall, open source has had a very active year with many breakthroughs and advancements. It's one of the areas where the whole is greater than the sum of its parts. Hence, it saddens me that some individuals are actively lobbying against open-source AI. But I hope we can keep the positive momentum in building more efficient solutions and alternatives rather than just becoming more dependent on ChatGPT-like products released by big tech companies.

To end this section on a positive note, thanks to the open source and research communities, we saw small and efficient models that we can run on a single GPU, like the [1.3B parameter phi1.5](https://arxiv.org/abs/2309.05463), [7B Mistral](https://mistral.ai/), and [7B Zephyr](https://news.ycombinator.com/item?id=37891848) come closer to the performance of the large proprietary models, which is an exciting trend that I hope will continue in 2024.

# The Productivity Promise

I see open-source AI as the primary path forward for developing efficient and custom LLM solutions, including finetuned LLMs based on our personal or domain-specific data for various applications. if you follow me on social media, you probably saw me talking about and tinkering with [Lit-GPT](https://github.com/Lightning-AI/lit-gpt), which is an LLM open-source repository that I actively contribute to. But while I am a big proponent of open-source, I am also a big fan of well-designed products.

Since ChatGPT was released, we have seen LLMs being used for pretty much everything. Readers of this article have probably already used ChatGPT, so I don't have to explain that LLMs can indeed be useful for certain tasks. 

The key is that we use them for the "right" things. For instance, I probably don't want to ask ChatGPT about the store hours of my favorite grocery store. However, one of my favorite use cases is fixing my grammar or helping me brainstorm with rephrasing my sentences and paragraphs. Bigger picture-wise, what underlies LLMs is the promise of increased productivity, which you probably also already experienced.

Besides LLMs for regular text, Microsoft's and GitHub's [Copilot coding assistant](https://github.com/features/copilot) is also maturing, and more and more people are starting to use it. Earlier this year, a report by [Ark-Invest](https://ark-invest.com/home-thank-you-big-ideas-2023/) estimated that code assistants reduce the time to complete a coding task by ~55%.

Chart via [https://ark-invest.com/home-thank-you-big-ideas-2023/](https://ark-invest.com/home-thank-you-big-ideas-2023/)

Whether it's more or less than 55% is debatable, but if you have used a code assistant before, you notice that these can be super helpful and make tedious coding-related tasks easier.

One thing is certain: coding assistants are here to stay, and they will probably only get better over time. Will they replace human programmers? I hope not. But they will undoubtedly make existing programmers more productive.

What does that mean for StackOverflow? The State of AI report includes a chart that shows the website traffic of StackOverflow compared to GitHub, which might be related to the increasing adoption of Copilot. However, I believe even ChatGPT/GPT-4 is already very helpful for coding-related tasks. I suspect that ChatGPT is also partly (or even largely) responsible for the decline in StackOverflow traffic.

Chart from the [State of AI 2023](http://stateof.ai/) report

# AI Problems

**Hallucination**

The same problem still plagues LLMs as in 2022: they can create toxic content and tend to hallucinate. Throughout the year, I discussed several methods to address this, including reinforcement learning with human feedback (RLHF) and Nvidia's [NeMO Guardrails](https://github.com/NVIDIA/NeMo-Guardrails). However, these methods remain bandaids that are either too strict or not strict enough. 

So far, there is no method (or even idea for a method) to address this issue 100% reliably and in a way that doesn't diminish the positive capabilities of LLMs. In my opinion, it all comes down to how we use an LLM: Don't use LLMs for everything, use a calculator for math, regard LLMs as your writing companion and double-check its outputs, and so forth. 

Also, for specific business applications, it might be worthwhile exploring retrieval augmented augmentation (RAG) systems as a compromise. In RAG, we retrieve relevant document passages from a corpus and then condition the LLM-based text generation on the retrieved content. This approach enables models to pull in external information from databases and documents versus memorizing all knowledge.

An illustration of RAG from [Machine Learning Q and AI](https://leanpub.com/machine-learning-q-and-ai/)

**Copyrights**

More urgent problems are the copyright debates around AI. [According to Wikipedia](https://en.wikipedia.org/wiki/Fair_use), "The copyright status of LLMs trained on copyrighted material is not yet fully understood." And overall, it seems that many rules are still being drafted and amended. I am hoping that the rules, whatever they are, will be clear so that AI researchers and practitioners can adjust and act accordingly. (I wrote more about AI and copyright debates [here](https://magazine.sebastianraschka.com/i/136352403/llms-and-copyright-laws).)

**Evaluation**

An issue plaguing academic research is that the popular benchmarks and leaderboards are considered semi-broken because the test sets may have leaked and have become LLM training data. This has become a concern with phi-1.5 and Mistral, as I discussed in my [previous article](https://magazine.sebastianraschka.com/p/ahead-of-ai-12-llm-businesses).

A popular but less easy way to automate LLM evaluation is to ask humans for their preferences. Alternatively, many papers also rely on GPT-4 as the second-best way.

An example using human and GPT-4 preference evaluation from the [LIMA paper](https://arxiv.org/abs/2305.11206)

**Revenue**

Generative AI is currently still in an exploratory stage. Of course, we all experienced that text and image generators can be helpful for specific applications. However, whether they can generate a positive cash flow for companies is still a hotly debated topic due to the expensive hosting and runtime costs. For example, [it was reported that OpenAI had a $540 million loss](https://futurism.com/the-byte/openai-losing-money-chatgpt) last year. On the other hand, [recent reports say](https://fortune.com/2023/08/30/chatgpt-creator-openai-earnings-80-million-a-month-1-billion-annual-revenue-540-million-loss-sam-altman/#:~:text=ChatGPT%20creator%20OpenAI%20is%20reportedly,million%20loss%20from%20last%20year) that OpenAI is now earning $80 million each month, which could offset or exceed its operating costs.

**Fake Imagery**

One of the bigger issues related to generative AI, which is particularly apparent on social media platforms at the moment, is the creation of fake images and videos. Fake images and videos have always been a problem, and similar to how software like Photoshop lowered the barrier to entry for fake content, AI is taking this to the next level. 

Other AI systems are designed to detect AI-generated content, but these are neither reliable for text nor images or videos. The only way to somewhat curb and combat these issues is to rely on trustworthy experts. Similar to how we do not take medical or legal advice from random forums or websites on the internet, we probably also shouldn't be trusting images and videos from random accounts on the internet without double-checking. 

**Dataset Bottlenecks**

Related to the copyright debate mentioned earlier, many companies (including Twitter/X and Reddit) closed their free API access to increase revenue but also to prevent scrapers from collecting the platforms' data for AI training.

I've come across numerous advertisements from companies specializing in dataset-related tasks. Although AI may regrettably lead to the automation of certain job roles, it appears to be simultaneously generating new opportunities.

One of the best ways to contribute to open-source LLM progress may be in building a platform to crowdsource datasets. With this, I mean writing, collecting, and curating datasets that have explicit permission for LLM training.

# Is RLHF the Cherry on the Cake?

When the Llama 2 model suite was released, I was excited to see that it included models that were finetuned for chat. Using reinforcement learning with human feedback (RLHF), Meta AI increased both the helpfulness and harmlessness of their models -- If you are interested in a more detailed explanation, I have a whole article dedicated to RLHF [here](https://magazine.sebastianraschka.com/p/llm-training-rlhf-and-its-alternatives).

Annotated figure from Llama 2: Open Foundation and Fine-Tuned Chat Models, [https://arxiv.org/abs/2307.09288](https://arxiv.org/abs/2307.09288)

I always thought of RLHF as a really interesting and promising approach, but besides InstructGPT, ChatGPT, and Llama 2, it was not widely used. Hence, I was surprised to find a chart on the rising popularity of RLHF. I certainly didn't expect it because it's still not widely used.

Chart on the popularity of RLHF from the [State of AI 2023](https://stateof.ai/) report.

Since RLHF is a bit complicated and tricky to implement, most open-source projects are still focused on supervised finetuning for instruction finetuning.

A recent alternative to RLHF is Direct Preference Optimization (DPO). [In the corresponding paper](https://arxiv.org/abs/2305.18290), the researchers show that the cross entropy loss for fitting the reward model in RLHF can be used directly to finetune the LLM. According to their benchmarks, it's more efficient to use DPO and often also preferred over RLHF/PPO regarding response quality.

Annotated figure from [DPO paper](https://arxiv.org/abs/2305.18290)

DPO does not seem to be widely used yet. However, to my excitement, two weeks ago, we got the first openly available LLM trained via [DPO via Lewis Tunstall and colleagues](https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha), which seems to outperform the bigger Llama-2 70b Chat model trained via RLHF:

Screenshot from the [Zephyr 7B announcement](https://x.com/_lewtun/status/1711756736758178270?s=20)

However, it's worth noting that RLHF is not explicitly used to optimize benchmark performance; its primary optimization goals are "helpfulness" and "harmlessness" as assessed by human users, which is not captured here.

# Classification Anyone?

Last week, I gave a talk at [Packt's generative AI conference](https://www.packtpub.com/conference/put-gen-ai-to-work) a few weeks ago, highlighting that one of the most prominent use cases for text models remains classification. For example, think of common tasks such as email spam classification, document categorization, classifying customer reviews, and labeling toxic speech on social media.

In my experience, it's possible to get really good classification performance with "small" LLMs, such as [DistilBERT](https://arxiv.org/abs/1910.01108), using only a single GPU.

Excerpt from [my talk](https://www.packtpub.com/conference/put-gen-ai-to-work) showing that you can finetune small LLMs as text classifiers

I posted text classification with small LLMs as an exercise in Unit 8 of my [Deep Learning Fundamentals class](https://lightning.ai/pages/courses/deep-learning-fundamentals/) this year, where [Sylvain Payot even achieved >96% prediction accuracy](https://github.com/Lightning-AI/dl-fundamentals/discussions/41) on the IMDB movie review dataset by finetuning an off-the-shelf available Roberta model. (For reference, the best [classic machine learning-based bag-of-words model](https://github.com/rasbt/machine-learning-book/blob/main/ch08/logistic-regression-bag-of-words/log-reg.ipynb) I trained on that dataset achieved only 89% accuracy).

[Discussing the best classification model](https://github.com/Lightning-AI/dl-fundamentals/discussions/41) in my Deep Learning Fundamentals [class](https://lightning.ai/pages/courses/deep-learning-fundamentals/).

Now, that being said, I haven't seen any new major work or trends on LLMs for classification yet. Most practitioners still use BERT-based encoder models or encoder-decoder models like [FLAN-T5](https://arxiv.org/abs/2210.11416), which came out in 2022. That could be because these architectures still work surprisingly and satisfactorily well.

# The State of Tabular Data

In 2022, I wrote [A Short Chronology Of Deep Learning For Tabular Data](https://sebastianraschka.com/blog/2022/deep-learning-for-tabular-data.html), covering many interesting deep learning-based approaches to tabular data. However, similar to LLMs for classification mentioned above, there haven't been that many developments on the tabular dataset front either, or I have just been too busy to notice.

An example of a tabular dataset for reference

In 2022, Grinsztajn et al. wrote a paper on [Why do tree-based models still outperform deep learning on tabular data?](https://arxiv.org/abs/2207.08815) I believe the main takeaway that tree-based models (random forests and XGBoost) outperform deep learning methods for tabular data on small- and medium-sized datasets (10k training examples) is still true. 

On that note, after being around for almost 10 years, XGBoost came out with a big [2.0 release](https://github.com/dmlc/xgboost/releases/tag/v2.0.0) that featured better memory efficiency, support for large datasets that don't fit into memory, multi-target trees, and more.

# Computer Vision in 2023

While this year has been very focused on LLMs, there have been many developments on the computer vision front. Since this article is already very long, I won't cover the latest computer vision research. However, I have a standalone article on the State of Computer Vision Research 2023 from my attendance at CVPR 2023 this summer:

[

## Ahead of AI #10: State of Computer Vision 2023

](https://magazine.sebastianraschka.com/p/ahead-of-ai-10-state-of-computer)

[Sebastian Raschka, PhD](https://substack.com/profile/27393275-sebastian-raschka-phd)

·

2023年7月6日

Large language model development (LLM) development is still happening at a rapid pace. At the same time, leaving AI regulation debates aside, LLM news seem to be arriving at a just slightly slower rate than usual. This is a good opportunity to give the spotlight to computer vision once in a while, discussing the current state of research and development in this field. And this theme also goes nicely with a recap of CVPR 2023 in Vancouver, which was a wonderful conference at probably the nicest conference venue I have attended so far.

[

Read full story

](https://magazine.sebastianraschka.com/p/ahead-of-ai-10-state-of-computer)

Besides research, computer vision-related AI has been inspiring new products and experiences that have been maturing this year. 

For example, when I attended the [SciPy conference](https://www.scipy2023.scipy.org/) in Austin this summer, I saw the first truly driverless Waymo cars roaming the streets. 

And from a trip to the movie theater, I also saw AI usage is becoming increasingly popular in the movie industry. A recent example is the de-aging of Harrison Ford in "Indiana Jones 5", where the filmmakers trained an AI using old archive material of the actor.

Then, there are generative AI capabilities that are now firmly integrated into popular software products. A recent example is [Adobe's Firefly 2](https://www.adobe.com/sensei/generative-ai/firefly.html).

# Predictions for 2024

Predictions are always the most speculative and challenging aspect. Last year, I predicted that we would see more applications of LLMs in domains beyond text or code. One such example was [HyenaDNA](https://arxiv.org/abs/2306.15794), an LLM for DNA. Another was [Geneformer](https://www.nature.com/articles/s41586-023-06139-9), a transformer pretrained on 30 million single-cell transcriptomes designed to facilitate predictions in network biology.

In 2024, LLMs will increasingly transform STEM research outside of computer science.

Another emerging trend is the development of custom AI chips by various companies, driven by GPU scarcity due to high demand. Google will double-down on its [TPU hardware](https://cloud.google.com/blog/products/compute/announcing-cloud-tpu-v5e-and-a3-gpus-in-ga), Amazon has introduced its [Trainium chips](https://aws.amazon.com/machine-learning/trainium/), and AMD might be closing the gap with NVIDIA. And now, [Microsoft](https://www.theinformation.com/articles/microsoft-to-debut-ai-chip-next-month-that-could-cut-nvidia-gpu-costs) and [OpenAI](https://arstechnica.com/information-technology/2023/10/openai-may-jump-into-ai-hardware-amid-high-costs-supply-constraints/) also started developing their own custom AI chips. The challenge will be ensuring full and robust support for this hardware within major deep learning frameworks.

On the open-source front, we still lag behind the largest closed-source models. Currently, the largest openly available model is [Falcon 180B](https://huggingface.co/blog/falcon-180b). This might not be too concerning because most people lack access to the extensive hardware resources required to handle these models anyway. Instead of bigger models, I'm more eager to see more open-source MoE models consisting of multiple smaller submodules, which I discussed earlier in this article.

I'm also optimistic about witnessing increased efforts in crowdsourced datasets and the rise of [DPO](https://arxiv.org/abs/2305.18290) as a replacement for supervised fine-tuning in state-of-the-art open-source models.

---

*This magazine is a personal passion project that does not offer direct compensation. However, for those who wish to support me, please consider purchasing a copy of [one of my books](https://sebastianraschka.com/books). If you find them insightful and beneficial, please feel free to recommend them to your friends and colleagues.*

[Machine Learning with PyTorch and Scikit-Learn](https://www.amazon.com/Machine-Learning-PyTorch-Scikit-Learn-scikit-learn-ebook-dp-B09NW48MR1/dp/B09NW48MR1/), [Machine Learning Q and AI](https://nostarch.com/machine-learning-and-ai-beyond-basics), and [Build a Large Language Model (from Scratch)](http://mng.bz/M96o)

**Your support means a great deal! Thank you!**

---

#### Subscribe to Ahead of AI

By Sebastian Raschka · Thousands of paid subscribers

Ahead of AI focuses on machine learning and AI research and is read by more than 150,000 researchers and practitioners who want to stay ahead in a rapidly evolving field.

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

114 Likes∙

[14 Restacks](https://substack.com/note/p-138171169/restacks?utm_source=substack&utm_content=facepile-restacks)

114

11

14

Share