---
url: https://blog.eladgil.com/p/things-i-dont-know-about-ai?utm_source=post-email-title&publication_id=1119759&post_id=141265232&utm_campaign=email-post-title&isFreemail=true&r=2abnc9&utm_medium=email
title: "Things I Don't Know About AI"
description: "The more I learn about AI markets, the less I think I know. I list questions and some thoughts."
author: "Elad Gil"
published: "2025-07-22T16:47:51.166Z"
captured_at: "2026-03-08T11:31:48.963Z"
---

# Things I Don't Know About AI

### The more I learn about AI markets, the less I think I know. I list questions and some thoughts.

[Elad Gil](https://substack.com/@eladgil)

Feb 21, 2024

278

38

Share

In most markets, the more time passes the clearer things become. In generative AI (“AI”), it has been the opposite. The more time passes, the less I think I actually understand.

For each level of the AI stack, I have open questions. I list these out below to stimulate dialog and feedback.

### LLM Questions

There are in some sense two types of LLMs - frontier models - at the cutting edge of performance (think GPT-4 vs other models until recently), and everything else. [In 2021 I wrote that I thought the frontier models](https://blog.eladgil.com/p/ai-platforms-markets-and-open-source) market would collapse over time into an oligopoly market due to the scale of capital needed. In parallel, non-frontier models would more commodity / pricing driven and have a stronger opensource presence (note this was pre-Llama and pre-Mistral launches).

Things seem to be evolving towards the above:

Frontier LLMs are likely to be an oligopoly market. Current contenders include closed source models like OpenAI, Google, Anthropic, and perhaps Grok/X.ai, and Llama (Meta) and Mistral on the open source side. This list may of course change in the coming year or two. Frontier models keep getting more and more expensive to train, while commodity models drop in price each year as performance goes up (for example, it is probably ~5X cheaper to train GPT-3.5 equivalent now than 2 years ago)

As model scale has gotten larger, funding increasingly has been primarily coming from the cloud providers / big tech. For example, Microsoft invested $10B+ in OpenAI, while Anthropic raised $7B between Amazon and Google. NVIDIA is also a big investor in foundation model companies of many types. The venture funding for these companies in contrast is a tiny drop in the ocean in comparison. As frontier model training booms in cost, the emerging funders are largely concentrated amongst big tech companies (typically with strong incentives to fund the area for their own revenue - ie cloud providers or NVIDIA), or nation states wanting to back local champions (see eg [UAE and Falcon](https://falconllm.tii.ae/)). This is impacting the market and driving selection of potential winners early.

It is important to note that the scale of investments being made by these cloud providers is dwarfed by actual cloud revenue. For example, Azure from Microsoft generates $25B in revenue a quarter. The ~$10B OpenAI investment by Microsoft is roughly 6 weeks of Azure revenue. AI is having a big impact on Azure revenue revently. [Indeed Azure grew 6 percentage points](https://www.wsj.com/business/earnings/microsoft-msft-q2-earnings-report-2024-57743658) in Q2 2024 from AI - which would put it at an annualized increase of $5-6B (or 50% of its investment in OpenAI! Per year!). Obviously revenue is not net income but this is striking nonetheless, and suggests the big clouds have an economic reason to fund more large scale models over time.

In parallel, Meta has done outstanding work with Llama models and recently announced [$20B compute budget](https://www.pcmag.com/news/zuckerbergs-meta-is-spending-billions-to-buy-350000-nvidia-h100-gpus), in part to fund massive model training. I [posited 18 months ago that an open source sponsor for AI models](https://blog.eladgil.com/p/ai-platforms-markets-and-open-source) should emerge, but assumed it would be Amazon or NVIDIA with a lower chance of it being Meta. (Zuckerberg & Yann Lecunn have been visionary here).

### Questions on LLMs:

-   **Are cloud providers king-making a handful of players at the frontier and locking in the oligopoly market via the sheer scale of compute/capital they provide?** When do cloud providers stop funding new LLM foundation companies versus continuing to fund existing? Cloud providers are easily the biggest funders of foundation models, not venture capitalists. Given they are constrained in M&A due to FTC actions, and the revenue that comes from cloud usage, it is rational for them to do so. This may lead / has led to some distortion of market dynamics. How does this impact the long term economics and market structure for LLMs? Does this mean we will see the end of new frontier LLM companies soon due to a lack of enough capital and talent for new entrants? Or do they keep funding large models hoping some will convert on their clouds to revenue?

-   **Does OSS models flip some of the economics in AI from foundation models to clouds? Does Meta continue to fund OS models? If so, does eg Llama-N catch up to the very frontier?** A fully open source model performing at the very frontier of AI has the potential to flip a subportion the economic share of AI infra from LLMs towards cloud and inference providers and decreases revenue away from the other LLM foundation model companies. Again, this is likely an oligopoly market with no singular winner (barring AGI), but has implications on how to think about the relative importance of cloud and infrastructure companies in this market (and of course both can be very important!).

    -   One of the most brilliant things in the [Llama2 terms of use is the open commercial use of the license if you have fewer then 700 million users](https://ai.meta.com/llama/license/)\[1\]. This obviously prevents some large competitors from using their models. But it also means if you are a big cloud provider you need to pay a license to Meta for Llama, which Microsoft has already done. This creates an interesting long term way for Meta to control (& monetize) Llama despite being open source.

-   **How do we think about speed and price vs performance for models?** One could imagine extremely slow incredibly performant models may be quite valuable if compared to normal human speed to do things. The latest largest [Gemini models](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/) seem to be heading in this direction with large 1 million+ token [context windows a la Magic](https://magic.dev/blog/ltm-1), which announced a 5 million token window in June 2023. Large context windows and depth of understanding can really change how we think about AI uses and engineering. On the other side of the spectrum, Mistral has shown the value of small, fast and cheap to inference performant models. The 2x2 below suggests a potential segmentation of where models will matter most.

-   **How do architectures for foundation models evolve? Do agentic models with different architectures subsume some of the future potential of LLMs? When do other forms of memory and reasoning come into play?**

-   **Do governments back (or direct their purchasing to) regional AI champions?** **Will national governments differentially spend on local models a la Boeing vs Airbus in aerospace? Do governments want to support models that reflect their local values, languages, etc?** Besides cloud providers and global big tech (think also e.g. Alibaba, Rakuten etc) the other big sources of potential capital are countries. There are now great model companies in Europe (e.g. Mistral), Japan, India, UAE, China and other countries. If so, there may be a few multi-billion AI foundation model regional companies created just off of government revenue.

-   **What happens in China?** One could anticipate Chinese LLMs to be backed by Tencent, Alibaba, Xiaomi, ByteDance and others investing in big ways into local LLMs companies. China’s government has long used regulatory and literal firewalls to prevent competition from non-Chinese companies and to build local, government supported and censored champions. One interesting thing to note is the trend of Chinese OSS models. Qwen from Alibaba for example has moved higher on the broader [LMSYS leaderboards](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard).

-   **What happens with X.ai?** Seems like a wild card.

-   **How good does Google get?** Google has the compute, scale, talent to make amazing things and is organized and moving fast. Google was always the worlds first AI-first company. Seems like a wild card.

### Infra companies

There are a few types of infrastructure companies with very different uses. For example, [Braintrust](https://www.braintrustdata.com/) provides eval, prompt playgrounds, logging and proxies to help companies move from “vibe based” analysis of AI to data driven. [Scale.ai](http://scale.ai/) and others play a key role in data labeling, fine tuning, and other areas. A number of these have open but less existential questions (for example how much of RLHF turns into RLAIF).

The biggest uncertainties and questions in AI infra have to do with the AI Cloud Stack and how it evolves. It seems like there are very different needs between startups and enterprises for AI cloud services. For startups, the new cloud providers and tooling (think Anyscale, Baseten, Modal, Replicate, Together, etc) seem to be taking a useful path resulting in fast adoption and revenue growth.

For enterprises, who tend to have specialized needs, there are some open questions. For example:

-   **Does the current AI cloud companies need to build an on-premise/BYOC/VPN version of their offerings for larger enterprises?** It seems like enterprises will optimize for (a) using their existing cloud marketplace credits which they already have budget for, to buy services (b) will be hesitant to round trip out from where their webapp / data is hosted (ie AWS, Azure, GCP) due to latency & performance and (c) will care about security, compliance (FedRAMP, HIPAA etc). The short term startup market for AI cloud may differ from long term enterprise needs.

-   **How much of AI cloud adoption is due to constrained GPU / GPU arb?** In the absence of GPU on the main cloud providers companies are scrambling to find sufficient GPU for their needs, accelerating adoption of new startups with their own GPU clouds. One potential strategy NVIDIA could be doing is preferentially allocating GPU to these new providers to decrease bargaining power of hyperscalers and to fragment the market, as well as to accelerate the industry via startups. **When does the GPU bottleneck end and how does that impact new AI cloud providers?** It seems like an end to GPU shortages on the main clouds would be negative for companies whose only business is GPU cloud, while those with more tools and services should have an easier transition if this were to happen.

-   **How do new AI ASICS like [Groq](https://groq.com/) impact AI clouds?**

-   **What else gets consolidated into AI clouds?** Do they cross sell embeddings & RAG? Continuous updates? Fine tuning? Other services? How does that impact data labelers or others with overlapping offerings? What gets consolidated directly into model providers vs via the clouds?

-   **Which companies in the AI cloud will pursue which business model?**

    -   It is important to note there are really 2 market segments in the AI cloud world (a) startups (b) mid-market and enterprise. It seems likely that “GPU only” business model default works with the startup segment(who have fewer cloud needs), but for large enterprises adoption may be more driven by GPU cloud constraints on major platforms. **Do companies providing developer tooling, API endpoints, and/or specialized hardware, or other aspects morph into two other analogous models - (a) “Snowflake/Databricks for AI” model or (b) “Cloudflare for AI”? If so, which ones adopt which model?**

-   **How big do the new AI clouds become? As large as Heroku, Digital Ocean, Snowflake, or AWS? What is the size of outcome and utilization scale for this class of company?**

-   **How does the AI stack evolve with very long context window models? How do we think about the interplay of context window & prompt engineering, fine tuning, RAG, and inference costs?**

-   **How does FTC (and other regulator) prevention of M&A impact this market?** There are at least a dozen credible companies building AI cloud related products and services - too many for all of them to be stand alone. How does one think about exits under an administration that is aggressively against tech M&A? Should the AI clouds themselves consolidate amongst themselves to consolidate share and services offered?

### Apps questions

ChatGPT was the starting gun for many AI founders. Prior to ChatGPT (and right before that Midjourney and Stable Diffusion) most people in tech were not paying close attention to the Transformer/Diffusion model revolution and dislocation we are now experiencing.

This means that people closest to the model and technology - ie AI researchers and infra engineers - were the first people to leave to start new companies based on this technology. The people farther away from the core model world - many product engineers, designers, and PMs, did not become aware of how important AI is until now.

ChatGPT launched ~15 months ago. If it takes 9-12 months to decide to quit your job, a few months to do it, and a few months to brainstorm an initial idea with a cofounder, we should start to see a wave of app builders showing up now / shortly.

-   **B2B apps. What will be the important companies and markets in the emerging wave of B2B apps?** **Where will incumbents gain value versus startups?** I have a long post on this coming shortly.

-   **Consumer.** Arguably a number of the earliest AI products are consumer or “prosumer” - ie used in both personal and business use cases. Apps like ChatGPT, Midjourney, Perplexity and Pika are examples of this. **That said, why are there so few consumer builders in the AI ecosystem? Is it purely the time delay mentioned above?** It seems like the 2007-2012 social product cohort has aged out. New blood is needed to build the next great wave of AI consumer.

-   **Agents.** Lots and lots of things can happen with agents. **What will be strong focused product areas versus startups looking for a use case?**

This is one of the most exciting and fast-changing moments in technology in my lifetime. It will be fun to see what everyone builds. Looking forward to thoughts on the questions above.

Thanks to [Amjad Masad](https://twitter.com/amasad) and [Vipul Prakash](https://twitter.com/vipulved) for comments on a draft of this post.

**NOTES**

\[1\] Yes I occasionally read terms of use for fun.

**MY BOOK**
You can [order the High Growth Handbook here](https://www.amazon.com/High-Growth-Handbook-Elad-Gil/dp/1732265100/). Or [read it online for free](https://growth.eladgil.com/).

**OTHER POSTS**

**Firesides & Podcasts**

-   [Apoorva Metha: Starting Instacart](https://blog.eladgil.com/p/video-and-transcript-apoorva-metha)

-   [Satya Nadella: Building Microsoft](https://blog.eladgil.com/p/fireside-chat-with-satya-nadella)

-   [Brad Gerstner: Altimeter and Macro](https://blog.eladgil.com/p/altimeters-brad-gerstner-on-macro)

-   [Clem Delangue: Hugging Face, Open Source, AI](https://blog.eladgil.com/p/video-and-transcript-fireside-chat)

-   [Dylan Field: Figma, AI & Design, Education](https://blog.eladgil.com/p/transcript-and-video-fireside-w-dylan)

-   [Reid Hoffman on AI, Big Tech, and Society](https://blog.eladgil.com/p/fireside-chat-with-reid-hoffman-on)

-   [Sam Altman, CEO OpenAI](https://www.youtube.com/watch?v=PJXYYnX9HqA)

-   [Emad Mostaque, Stability.AI](https://www.youtube.com/watch?v=f9v5_7HjnAE&t=10s)

-   [NoPriors AI Podcast](https://podcasts.apple.com/us/podcast/no-priors-artificial-intelligence-machine-learning/id1668002688)

**Markets:**

-   [2023 Unicorn Market Cap & Rise of AI](https://blog.eladgil.com/p/unicorn-market-cap-2023-rise-of-ai)

-   [AI Regulation](https://blog.eladgil.com/p/ai-regulation)

-   [Early Days of AI](https://blog.eladgil.com/p/early-days-of-ai)

-   [AI Safety: Technology vs Species Threats](https://blog.eladgil.com/p/ai-safety-technology-vs-species-threats)

-   [Startup Decoupling and Reckoning](https://blog.eladgil.com/p/startup-decoupling-and-reckoning)

-   [Defensibility and Competition](https://blog.eladgil.com/p/defensibility-and-competition)

-   [AI Platforms, Markets, and Open Source](https://blog.eladgil.com/p/ai-platforms-markets-and-open-source)

-   [Changing times (or, why is every layoff 10-15%?)](https://blog.eladgil.com/p/changing-times-or-why-is-every-layoff)

-   [AI Startup Vs Incumbent Value](https://blog.eladgil.com/p/ai-startup-vs-incumbent-value)

-   [AI Revolution - Transformers and Large Language Models](http://blog.eladgil.com/2022/08/ai-revolution-transformers-and-large.html) 

-   [Startup Markets Summer 2022](http://blog.eladgil.com/2022/07/what-may-be-coming-to-startups-2022.html)

-   [False Narrative Around Theranos](http://blog.eladgil.com/2021/09/the-false-narrative-around-theranos.html)

-   [Index Companies](http://blog.eladgil.com/2020/12/index-companies.html)

-   [Defense Tech](http://blog.eladgil.com/2020/10/silicon-valley-defense-tech.html)

-   [Collaborative Enterprise](http://blog.eladgil.com/2020/09/collaborative-enterprise-at-last.html)

-   [Industry Towns: Where you start a company matters](http://blog.eladgil.com/2019/06/industry-towns-where-you-start-company.html)

-   [Markets are 10X Bigger](http://blog.eladgil.com/2019/05/markets-are-10x-bigger-than-ever.html)

-   [Hot Markets 2019](http://blog.eladgil.com/2019/01/interesting-markets-2019-edition.html)

-   [End of Cycle?](http://blog.eladgil.com/2016/07/end-of-cycle.html)

-   [Machine Learning Startups](http://blog.eladgil.com/2016/08/startups-in-machine-learning-ai.html)

-   [3 Types Of Platform Companies](http://blog.eladgil.com/2015/01/the-3-types-of-platform-companies.html)

-   [Defensibility and Lock-In: Uber and Lyft](http://blog.eladgil.com/2014/12/defensibility-and-lock-in-uber-lyft.html)

-   [Uber And Disruption](http://techcrunch.com/2014/01/19/uber-and-disruption/)

-   [Who Cares If Its Been Tried Before?](http://blog.eladgil.com/2013/04/who-cares-if-its-been-tried-before.html)

-   [The Road To $5 Billion Is A Long One](http://blog.eladgil.com/2012/10/the-road-to-5-billion-is-long-one.html)

-   [How To Win As Second Mover](http://blog.eladgil.com/2012/10/how-to-win-as-second-mover.html)

-   [End Of Silicon Valley](http://blog.eladgil.com/2012/09/enough-with-this-end-of-silicon-valley.html)

-   [Social Products](http://blog.eladgil.com/2013/06/social-products.html)

-   [Hot Markets For 2015](http://blog.eladgil.com/2015/01/hot-markets-for-2015.html)

**Startup life**

-   [Capital Efficient Businesses](https://blog.eladgil.com/p/capital-efficient-businesses)

-   [Startups Are An Act of Desperation](https://blog.eladgil.com/p/startups-are-an-act-of-desperation)

-   [Back To The Office](https://blog.eladgil.com/p/back-to-office)

-   [Hiring Executives and Bad Advice](http://blog.eladgil.com/2021/02/hiring-executives-bad-advice.html)

-   [When executives break](http://blog.eladgil.com/2021/02/when-executives-break.html)

-   [Fear of Sales](http://blog.eladgil.com/2019/10/fear-of-sales.html)

-   [A brief guide to startup pivots](http://blog.eladgil.com/2019/05/a-brief-guide-to-startup-pivots-4-types.html)

-   [4 Ways Startups Fail](http://blog.eladgil.com/2011/05/4-ways-startups-fail.html)

-   [Founder Investors and Scout Programs](http://founder%20investors%20&%20scout%20programs/)

-   [Better Meetings](http://blog.eladgil.com/2018/07/meeting-etiquette.html)

-   [Magic Startup Moments](http://blog.eladgil.com/2019/12/magic-startup-moments.html)

-   [Founder Investors & Scout Programs](http://blog.eladgil.com/2019/04/founder-investors-scout-programs.html)

-   [Jobs, Wozniak, Cook](http://blog.eladgil.com/2020/10/jobs-wozniak-cook-build-sell-scale.html)

**Co-Founders**

-   [How To Choose A Co-Founder](http://blog.eladgil.com/2012/02/how-to-choose-co-founder.html)

-   [Unequal Cofounders](http://blog.eladgil.com/2017/08/unequal-cofounders.html)

-   [How To Fire A Co-Founder](http://blog.eladgil.com/2013/01/how-to-fire-co-founder.html)

-   [Founders Should Divide and Conquer](http://blog.eladgil.com/2014/12/founders-should-divide-and-conquer.html)

**Raising Money**

-   [Preemptive rounds](http://blog.eladgil.com/2018/06/preemptive-rounds.html)

-   [Don't Ask For Too Much Money](http://blog.eladgil.com/2017/02/dont-ask-for-too-much-money.html)

-   [Building VC Relationships](http://blog.eladgil.com/2017/02/building-vc-relationships.html)

-   [Founders Should Divide And Conquer](http://blog.eladgil.com/2014/12/founders-should-divide-and-conquer.html)

-   [Lead VC Vetos](http://blog.eladgil.com/2014/12/should-your-lead-vc-veto-other-investors.html)

-   [What Is A Good VC?](http://blog.eladgil.com/2014/07/what-is-good-vc.html)

-   [How To Choose The Right VC For You](http://blog.eladgil.com/2012/11/how-to-choose-right-vc-partner-for-you.html)

-   [Signs a VC Just Isn't That Into You](http://blog.eladgil.com/2012/07/signs-vc-is-just-not-that-into-you.html)

-   [Series A Crunch](http://blog.eladgil.com/2011/11/why-fewer-companies-are-successfully.html)

-   [Questions VCs Will Ask You](http://blog.eladgil.com/2011/03/questions-vcs-will-ask-you.html)

-   [How To Raise A Successful VC Round](http://blog.eladgil.com/2011/03/tactics-for-how-to-raise-vc-round-or.html)

-   [Differences Between Funding Rounds: Series Seed, A, B, C...](http://blog.eladgil.com/2011/03/how-funding-rounds-differ-seed-series.html)

-   [Financing Approaches Most Likely To Kill Your Company](http://blog.eladgil.com/2010/12/financing-approaches-most-likely-to.html)

-   [Party Rounds: How to Get A High Valuation For Your Seed Startup](http://blog.eladgil.com/2010/09/party-rounds-how-to-get-high-valuation.html)

-   [20 Questions To Ask Yourself Before Raising Money](http://blog.eladgil.com/2010/08/20-questions-to-ask-yourself-before.html)

-   [The 7 Types Of Angel Investors](http://blog.eladgil.com/2010/03/7-types-of-angel-investors-what-is.html)

-   [Fundraising Will Take You 3 Months](http://blog.eladgil.com/2012/09/fundraising-will-take-you-3-months.html)

-   [How To Sell Secondary Stock](http://blog.eladgil.com/2014/01/how-to-sell-secondary-stock.html)

---

#### Subscribe to Elad Blog

By Elad Gil · Launched 3 years ago

I am a serial entrepreneur obsessed with technology and startups.

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

278 Likes∙

[38 Restacks](https://substack.com/note/p-141265232/restacks?utm_source=substack&utm_content=facepile-restacks)

278

38

Share

PreviousNext