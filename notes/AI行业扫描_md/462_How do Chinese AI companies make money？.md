# How do Chinese AI companies make money?

| Field | Value |
|---|---|
| Type | Report |
| Author | Cheryl Wu and Anson Ho |
| Date | Oct. 6, 2026 |
| Source | [Epoch AI](https://epoch.ai/publications/how-do-chinese-ai-companies-make-money) |

## 正文

## Key takeaways

- **Chinese AI firms earn a small fraction of what US frontier labs do.** As of September 2026, China’s six leading AI firms collectively earn about 10% of OpenAI and Anthropic combined, in terms of AI-related revenue.
- **Chinese AI companies earn revenue through five streams:** (1) consumer-facing AI applications, (2) selling model access (e.g., via API), (3) consulting and customizing AI for enterprises and governments, (4) AI licensing fees, and (5) using AI to complement existing product lines. Model-focused firms earn the most revenue through API sales, though this is unclear for large AI conglomerates, who potentially earn more by complementing existing product lines.
- **Consumer apps attract users but have low gross margins** — e.g., MiniMax’s AI-native apps had a gross margin of 4.7% in the first nine months of 2025. Margins are likely low because only a small fraction of Chinese AI app users pay, and those who do only pay small amounts.
- **API margins are often limited because model weights are publicly released, reducing pricing power.** Z.ai’s share of GLM 5.3 Flash tokens on OpenRouter fell from 88% to 22% in just 20 days after releasing model weights.
- **Enterprise and government solutions generate meaningful profits, but may be hard to scale.** For example, Z.ai has been deliberately shifting away from this business strategy, citing high maintenance costs that limit economies of scale. As such, from 2025 to H1 2026, the share of their revenue from on-premise deployments fell from 73.7% to 13.5%.
- **Licensing fees are a potential revenue stream, but there is little public data on their contribution.** Moonshot AI released Kimi K3’s weights under a modified MIT license, but we lack public data on overall earnings from the associated licensing fees.
- **For large AI conglomerates, AI can indirectly generate revenue by complementing existing product lines**. Alibaba and ByteDance’s model releases support their existing compute sales and advertising revenues.

## Overview

As of September 2026, China’s leading AI companies earn a small fraction of what OpenAI and Anthropic do. Understanding their current revenue sources can help us assess the Chinese frontier AI industry’s potential by showing us where demand for Chinese AI comes from, which firms have structural advantages, and how these firms are shaping their business strategies.

![Bar chart of annualized revenue in US$ billions: Anthropic 65, OpenAI 40, ByteDance 4.0, Alibaba 2.4, Z.ai 1.8, Moonshot 1.0, DeepSeek 1.0, MiniMax 0.8. China's six leading AI firms together earn about 10% of OpenAI and Anthropic's combined revenue.](https://epoch.ai/assets/images/posts/2026/how-do-chinese-ai-companies-make-money/revenue-comparison.png)

Revenue estimates are from different months ranging from June to September. Run rates were reported for [Anthropic](https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html) (July), [OpenAI](https://www.bloomberg.com/news/articles/2026-08-13/openai-s-revenue-run-rate-tops-40-billion-ahead-of-ipo) (August), and [DeepSeek](https://www.theinformation.com/articles/deepseeks-annualized-revenue-hits-1-billion-startup-finalizes-7-5-billion-fundraising) (September), [Moonshot](https://news.bloomberglaw.com/artificial-intelligence/china-ai-star-moonshot-eyes-2-billion-annualized-sales-in-2026) (August), [MiniMax](https://companies.caixin.com/2026-08-27/102478343.html) (August), [Z.ai](https://m.21jingji.com/article/20260917/herald/799af777af2dce66951712579b73ae35.html) (September), [ByteDance](https://finance.sina.com.cn/wm/2026-07-30/doc-inikpxkp1334857.shtml) (July), and [Alibaba](https://www.fool.com/earnings/call-transcripts/2026/08/27/alibaba-baba-q1-2027-earnings-call-transcript/) (August). The Alibaba and ByteDance figures are specific to Model-as-a-Service revenue, including serving proprietary and third-party models.

In this article, we analyze the revenue sources, gross margins, and growth potential of six notable Chinese AI companies: Alibaba, ByteDance, Z.ai, Moonshot, DeepSeek, and MiniMax. The first two are big tech companies with existing businesses besides AI (like Google), and the latter four are model-focused companies (like OpenAI).

Concretely, we find that these Chinese AI companies mainly make money from five sources:

1. Consumer-facing AI applications (direct monetization)
2. Selling model access (direct monetization)
3. Consulting and customizing AI for enterprises and governments (direct monetization)
4. Licensing fees (direct monetization)
5. Other products that are complementary to AI, e.g., hardware and compute (indirect monetization)

Examining these more closely helps shed light on which revenue source is the most important among Chinese AI labs. For model-focused companies, the dominant revenue source is API sales. In contrast, Alibaba and ByteDance potentially earn more through indirect monetization, though this is unclear from public data. We share company-specific data on these revenue streams in the Appendix.

## Consumer-facing AI applications appear to have weak gross margins

Consumer-facing AI applications are AI products and interfaces used directly by individual consumers. Examples include general-purpose AI assistants on the web, apps like ChatGPT and Claude, and more specialized products like Sora or AI companions.

In China, ByteDance’s Doubao is the most popular AI-native app. DeepSeek, Qwen, and others are also AI-native apps with many monthly active users ([MAU](https://36kr.com/p/3896193801602697)), [according to QuestMobile](https://www.questmobile.com.cn/research/report/2076954943839809537/). Some video and audio models are also turned into AI applications, such as MiniMax’s Hailuo and Talkie.[1](https://epoch.ai#user-content-fn-1)

![Scatter plot of Chinese AI apps by monthly active users and minutes per user per month, June 2026. Doubao leads with about 380 million MAU and 140 minutes; DeepSeek has about 130 million MAU; Qwen about 170 million MAU but under 30 minutes.](https://epoch.ai/assets/images/posts/2026/how-do-chinese-ai-companies-make-money/chinese-ai-apps-usage.png)

These consumer apps make money in several ways. First, they can **display ads.** For example, advertisements inside Talkie, MiniMax’s companion app, generated 20.9% of the company’s total revenue in the first nine months of 2025.[2](https://epoch.ai#user-content-fn-2)

Alternatively, **they charge fees for better models or more tokens.** For example, ByteDance’s Doubao’s standard subscription [costs](https://www.cls.cn/detail/2407871) ￥68 ($9.6)/month.

However, this likely does not yield a large profit because consumers rarely pay for such services. MiniMax’s consumer-facing AI products, including MiniMax, Hailuo AI for video generation, MiniMax Audio for speech and audio generation, and Talkie, an AI companion app, accounted for 36.6% of its total revenue in the first six months of 2026. However, the gross margin of MiniMax’s AI-native apps was only 4.7% in the first nine months of 2025. For comparison, MiniMax’s gross margin for Open Platform and other enterprise services was 69.4% in the same period.

Why are these margins so low? It is hard to know for certain without information about the compute and labor costs of deploying these consumer apps. But even still, we can identify likely contributing factors:

1. **Few users pay**. The apps averaged 27.6 million monthly active users (MAU) but only 1.77 million paid users in the first 9 months of 2025 (~6% of MAU).[3](https://epoch.ai#user-content-fn-3) In another example, when ByteDance trialed a [paid membership service](https://www.tmtpost.com/8040655.html) for Doubao, the paid conversion rate was allegedly low. Low paid conversion is not unique to Chinese consumer-facing AI applications. [The Information](https://www.theinformation.com/newsletters/dealmaker/openai-anthropic-missed-gross-margin-forecasts) reports that only 5% of ChatGPT’s ~900 million weekly active users (WAU)[4](https://epoch.ai#user-content-fn-4) paid in 2025, while OpenAI spent $3.9B on inference for nonpaying users.
2. **Users who do pay don’t spend a lot**. MiniMax Hailuo’s standard package costs as little as ¥55/$7.99, which is cheap compared to video models in the US. Another example is Z.ai’s chatbot, which is free in the US, and with a [VIP subscription](http://apps.apple.com/cn/app/%E6%99%BA%E8%B0%B1%E6%B8%85%E8%A8%80-%E4%B8%80%E7%AB%99%E5%BC%8F%E8%A7%A3%E6%94%BEai%E7%94%9F%E4%BA%A7%E5%8A%9B/id6450893458) of $11 (￥79)/month in China. In contrast, OpenAI’s paying users pay far more: ChatGPT Plus starts at $20/month.

Overall, consumer-facing AI apps are not highly profitable when there are many free-tier users and paid tiers are very cheap. Ads could help monetize free-tier users, though the revenue they generate depends a lot on the size of the user base.

## Selling model access accrues limited revenue, since releasing model weights reduces pricing power

AI companies can sell model access through either metered API tokens or flat-token subscription plans.[5](https://epoch.ai#user-content-fn-5) Most revenue in US frontier AI comes from these sources. [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-3q26-profit-over-1b-the) estimates that 75-85% of Anthropic’s revenue comes from selling API tokens.

Chinese AI companies also sell model access, but using a somewhat different strategy: they tend to release their model weights, which increases adoption but comes at the expense of their pricing power.

Consider Z.ai’s GLM-5 model. [As of September 16th](https://archive.is/md9hp), the model had eight separate providers, some of which (GMI Cloud and StreamLake) had cheaper offerings than Z.ai itself. Only about 25% of all GLM-5 tokens were served through Z.ai’s own API over the previous 24 hours, with the rest handled by other providers. Another example is DeepSeek V4 Pro. As of the same date, the [cheapest offering](https://archive.is/WYuNQ) on OpenRouter was under 87% of DeepSeek’s input token pricing. And in the last 24 hours, only 28.4% of the model’s tokens were served by DeepSeek.

More generally, there is a pattern: when open-weight model developers charge a higher premium, they capture a smaller share of their own models’ tokens on OpenRouter.

![Scatter plot of 21 open-weight Chinese models: the developer's price as a multiple of the cheapest host's price against the developer's share of the model's OpenRouter tokens. A downward-sloping line of best fit shows that developers charging a higher premium serve a smaller share.](https://epoch.ai/assets/images/posts/2026/how-do-chinese-ai-companies-make-money/openrouter-price-premium-vs-share.png)

Prices are weighted averages of uncached-input, output, and cached-input token rates, using the same token mix and cache-hit rate for all hosts of a given model.

By contrast, a closed-weight model such as Anthropic’s Fable is almost always [provided](https://openrouter.ai/anthropic/claude-fable-5#providers) at the same list price of $10 per million input tokens, whether it’s accessed from Claude’s API platform or Amazon Bedrock. Small price differences sometimes arise because of factors like geographic restrictions or service tiers, but these are not the result of providers competing to serve the model more cheaply.

We can get an even clearer sense of how releasing model weights reduces pricing power using a GLM 5.3 Flash case study. On August 26th, Z.ai listed the model on OpenRouter at a 50% promotional discount and simultaneously released its weights. Within hours, third parties began serving the model, and after just a day there were twelve competitors, two of which price-matched the promotional cost. Z.ai had already ended their discount by September 15th, but by then they found themselves competing with 26 rivals, 8 of which managed to undercut them. The consequences on pricing were massive: over those 20 days, Z.ai’s largest rival, Relace, ended up serving more tokens than they did. Moreover, Z.ai’s share of OpenRouter tokens collapsed from 88% (measured around 33 hours after launch) to 22%, and their daily token volume dropped 70% despite GLM 5.3 Flash’s volume growing 17%.

![Stacked bar chart of GLM 5.3 Flash tokens served on OpenRouter on Aug 27, 2026 and Sept 15, 2026. Z.ai's share fell from 88% with 12 third-party hosts to 22% with 26 third-party hosts.](https://epoch.ai/assets/images/posts/2026/how-do-chinese-ai-companies-make-money/glm-5-3-flash-hosting.png)

Given this limited pricing power, what is the gross margin on API access? Unfortunately, there is very little precise data on this. According to Z.ai’s annual and interim reports, the gross margins on their API and developer platform were 18.9% in 2025 and 24.6% in the first half of 2026. They attribute this growth to the “expansion of cloud-based deployment business, the launch of programming subscription packages, and enhanced inference efficiency.”[6](https://epoch.ai#user-content-fn-6) For comparison, Opus 4.8 had [85%](https://newsletter.semianalysis.com/p/spacex-10gw-in-2027-why-its-real) API-serving gross margins at the first-party list API price by mid-2026.

One outlier is DeepSeek. The API gross margin for DeepSeek V4 (both Pro and Flash) is estimated to be [70-80%](https://www.theinformation.com/articles/deepseeks-annualized-revenue-nears-500-million-boosting-fundraise-ipo-plans). This is due to two reasons. First, Liang Wenfeng [stated](https://thechinaacademy.org/leaked-transcript-of-deepseek-ceos-four-hour-meeting-118-answers-on-his-roadmap/) that DeepSeek “doesn’t have that much compute” and “the primary goal of the model we built is not for others to find it easy to use, but for ourselves to find it easy to use.” According to [The Information](https://www.theinformation.com/articles/deepseeks-annualized-revenue-hits-1-billion-startup-finalizes-7-5-billion-fundraising), [DeepSeek](https://www.theinformation.com/briefings/deepseek-aims-close-7-5-billion-funding-round-end-october?rc=ok83pn) “has continued to invest in developing new models, allocating more than 70% of its computing capacity to model training and less than 30% to inference.” With limited compute resources, keeping the gross margin high helps reduce inference demand. Second, DeepSeek has managed to [keep its inference costs low by improving the efficiency of its AI infrastructure](https://www.theinformation.com/articles/deepseeks-revenue-reaches-70-million-july-tenfold-jump-2025). Consistent with this, DeepSeek captures the smallest share of OpenRouter spending on its own models out of the five labs: only about 8% of estimated customer spending on DeepSeek models goes to DeepSeek. We see a similar pattern across other Chinese AI companies on OpenRouter, when we look at model use across eight sampled days.

![Stacked bar chart of estimated annualized OpenRouter spending on each Chinese developer's models, split between the developer and third-party hosts. For Z.ai, DeepSeek and Moonshot most spending goes to third parties; Alibaba retains the largest share.](https://epoch.ai/assets/images/posts/2026/how-do-chinese-ai-companies-make-money/openrouter-spending-by-host.png)

Overall, releasing model weights leaves Chinese labs competing with third-party hosts to serve their own models. On OpenRouter, that competition limits what the labs can charge without losing volume and, for most of them, hands the bulk of the spending on their models to other providers.

## Enterprise and government solutions generate meaningful gross profits, but are harder to scale

AI companies can monetize by customizing and deploying their models for companies or governments. This usually involves adapting the model to the customer’s needs, integrating it with the customer’s data, and deploying it in a dedicated cloud environment or on the customer’s premises.[7](https://epoch.ai#user-content-fn-7)

Most Chinese AI companies (except DeepSeek) do this to some extent, but Z.ai in particular is known for serving entities with sensitive information, like government agencies, state-owned enterprises, and banks. This may be due to their background at the prestigious [Tsinghua University, which gives the company credibility.](https://www.chinaventure.com.cn/news/80-20260622-391942.html) For example, in 2025, [Z.ai worked with Hangzhou Urban Investment Group](https://finance.sina.com.cn/roll/2025-09-15/doc-infqqqea9575158.shtml) to create a public transportation model, flood control agent, and multimodal large-scale road and bridge maintenance model. According to Z.ai’s annual report, 73.7% of its revenue in 2025 came from on-premises deployment with a gross margin of 48.8%.

However, Z.ai is shifting away from the on-premises deployment business toward standardized cloud and API services. Notably, we see a sharp decline in on-premises deployment in H1 2026.

![Two line charts of Z.ai's on-premises deployment business from 2022 to 2026: its share of Z.ai's revenue falls from over 90% to about 13.5% in H1 2026, while on-premises revenue in US$ million rises to about 75.2 in 2025 before an estimated decline in 2026.](https://epoch.ai/assets/images/posts/2026/how-do-chinese-ai-companies-make-money/zai-on-premises-revenue.png)

This may be because it is hard to scale this business strategy. As the company’s [interim report](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0831/2026083101539.pdf) states, “the delivery and maintenance costs of this type of business have a certain degree of rigidity, resulting in reduced economies of scale.” Unlike selling standardized API access, customized deployments require substantial engineering work to fine-tune and integrate a model into a customer’s business. Z.ai’s gross margin on on-premises deployment has indeed decreased over the years.[8](https://epoch.ai#user-content-fn-8)

Alibaba and ByteDance also sell enterprise and government solutions. In May 2026, Alibaba’s [Cloud Intelligence Group](https://ue.aliyun.com/) [collaborated](https://ue.aliyun.com/news/20260528-03?spm=5176.14406642.root.40.af202bc8oSZn9U) with Tongji Hospital to work on medical imaging and support the hospital’s research model training, among other initiatives. Similarly, ByteDance’s enterprise cloud branch collaborated with the investment bank [China International Capital Corporation](https://www.jiemian.com/article/14691627.html) to develop a customized financial model.

Unlike independent model startups, both Alibaba and ByteDance have more enterprise reach and cloud infrastructure, which make it easier for them to sustain an enterprise deployment strategy. We have not been able to find public information about enterprise solution gross margins for these two firms.

## Licensing fees could help AI companies earn revenue in theory, but we lack public data on how much this contributes in practice

AI companies could in theory make money from licensing fees, but it is unclear whether developers could actually enforce these fees. At the moment, only a few flagship model releases from China’s top AI labs are open under a restrictive license.

![Timeline of flagship language model releases by DeepSeek, MiniMax, Z.ai, Moonshot, Alibaba and ByteDance from 2022 to 2026, colored by open weights, open with a restrictive license, or closed weights. A dashed line marks the DeepSeek-R1 release in January 2025. Only a handful of recent releases use a restrictive license.](https://epoch.ai/assets/images/posts/2026/how-do-chinese-ai-companies-make-money/flagship-release-licenses.png)

On July 27, 2026, Moonshot released Kimi K3’s weights under a modified MIT license. Section 2 of the [license](https://github.com/MoonshotAI/Kimi-K3/blob/main/LICENSE) reads:

> “If the Licensee or any of its affiliates operates a Model as a Service business, and the aggregate revenue of the Licensee and its affiliates exceeds 20 million US dollars (or the equivalent in other currencies) in total over any consecutive 12 months, the Licensee must enter into a separate agreement with Moonshot AI before using the Software or its derivative works for any commercial purpose.”

The statement has several caveats. First, Section 4 of the license says that the requirements do not apply to “(a) internal use of the Software, defined as any use that does not make the Software, its outputs, or its underlying capabilities available to third parties.” For example, if a firm downloads Kimi K3 and runs it on its own servers for employees, that would constitute internal use, and the firm would not need to enter a separate agreement with Moonshot.

Second, the copyright status of model weights is unsettled. US copyright law generally requires human authorship, but model weights are numerical parameters produced by an automated training process. As such, enforcing these restrictions through copyright law may not be straightforward, and Moonshot might instead have to rely more on contract law.

Third, it could be difficult to attribute use to a specific model and determine the licensee’s revenue. In practice, the license might therefore apply primarily to major cloud or inference providers and public companies whose revenue clearly exceeds the $20 million threshold.

Ultimately, this license likely targets large inference providers who serve Kimi K3. These include (but are not limited to):

1. Chinasoft, a large public Chinese IT services company, [entered](https://filingreader.com/news-wire/hongkong/2026-07-20/chinasoft-and-moonshot-ai-partner-for-revenue-sharing-ai-model) a joint innovation cooperation with Moonshot to integrate Kimi for enterprise customers. The two companies share revenue based on token consumption.
2. Cursor, who built its own model on top of Kimi K2.5 through continued pretraining and reinforcement learning (RL), with RL sampling and inference run on Fireworks as part of an authorized [commercial partnership](https://techcrunch.com/2026/03/22/cursor-admits-its-new-coding-model-was-built-on-top-of-moonshot-ais-kimi/).
3. Together AI, a cloud platform and API provider, [entered](https://www.together.ai/blog/together-ai-announces-strategic-partnership-with-moonshot-ai-to-natively-serve-kimi-models) a strategic partnership with Moonshot AI.
4. According to [Reuters](https://ca.marketscreener.com/news/china-s-moonshot-in-talks-with-microsoft-amazon-google-over-k3-revenue-sharing-sources-say-ce7858d9d88af325), Moonshot is seeking a share of up to 30% of revenue from K3-related services on Microsoft’s Azure, AWS, and Google Cloud. (For comparison, [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-growth-and-bedrock-mix?triedRedirect=true) estimates Anthropic’s revenue share is about 75%, though after paying Amazon’s infrastructure fee, its gross margin on Bedrock sales was only about 45% in early 2026).

Z.ai has also established revenue-sharing arrangements with cloud providers. According to China Star Market, Amazon has integrated Z.ai’s GLM-5.3 into [Bedrock](https://www.ithome.com/1/009/946.htm) in Oct 2026 and will share revenue with Z.ai. Z.ai has also [signed revenue-sharing agreements](https://finance.sina.com.cn/roll/2026-09-16/doc-inirzshx3737272.shtml) with several leading domestic and international cloud service providers. However, the terms of the revenue-sharing arrangement, including the share received by Z.ai, have not been disclosed.

We do not have reliable figures for how much money is made in this way, though we do know that some American companies consider this a viable strategy. In particular, Meta has pursued a similar licensing strategy with Llama. Meta has [revenue sharing agreements](https://techcrunch.com/2025/03/21/meta-has-revenue-sharing-agreements-with-llama-ai-model-hosts-filing-reveals/) with Llama AI model hosts, and Llama 4’s community license states the following:

> “If, on the Llama 4 version release date, the monthly active users of the products or services made available by or for Licensee, or Licensee’s affiliates, is greater than 700 million monthly active users in the preceding calendar month, you must request a license from Meta.”

## AI could generate indirect revenue by complementing existing product lines, but only in large conglomerates

Up to this point, we have only considered direct sources of AI company revenue — that is, scenarios where the AI model itself is the product. But AI models can also produce revenue *indirectly*, such as by increasing sales of complementary products. This is only possible at large conglomerates with many product lines, like Alibaba and ByteDance.

Broad adoption of AI increases demand for the compute needed to run the models. Alibaba and ByteDance can thus earn revenue from enterprise AI projects not only by providing models and integration, but also by selling the associated compute. For example, the aforementioned Alibaba-Tongji Hospital collaboration includes Alibaba Cloud providing cloud computing infrastructure.

Collaborations like these may have contributed substantially to Alibaba’s AI revenue. For Q2 2026, Alibaba’s [revenue](https://secure.businesswire.com/news/home/20260818525201/en/Alibaba-Group-Announces-June-Quarter-2026-Results) from AI cloud and compute services was $7.1 billion, with year-over-year revenue growth accelerating to 45%, allegedly driven by “the increasing adoption of AI-related products.” AI-related product revenue specifically reached $1.8 billion in Q2 2026, the twelfth consecutive quarter in which this product line saw triple-digit year-over-year growth. Note that in annualized terms, these are higher than the $2.4 billion we saw in the first figure of the report, which comes from MaaS sales specifically.

Similarly, ByteDance’s cloud platform Volcano Engine handled 49.5% of China’s public-cloud large-model token calls in 2025, according to the [IDC](https://news.qq.com/rain/a/20260508A03CXL00). Its model-as-a-service (MaaS) [revenue](https://kr-asia.com/bytedance-raises-volcano-engines-maas-revenue-target-on-seedance-2-0-growth) was around $221 million in 2025, and ByteDance recently raised its 2026 target to [$4 billion](https://finance.sina.com.cn/wm/2026-07-30/doc-inikpxkp1334857.shtml).

![Bar chart of 2025 shares of China's public-cloud model tokens: Volcano Engine (ByteDance) about 49.5%, Alibaba Cloud about 28%, other providers about 22%.](https://epoch.ai/assets/images/posts/2026/how-do-chinese-ai-companies-make-money/volcano-engine-token-share.png)

Alibaba and ByteDance’s compute businesses also benefit from open-weight models from other companies. Alibaba’s Model Studio (Bailian) [lists](https://www.alibabacloud.com/help/en/model-studio/text-generation-model/) DeepSeek, Z.ai, Moonshot, and MiniMax’s models alongside Qwen. The CEO of Alibaba Group, Yongming Wu, [claimed](https://www.tradingkey.com/news/transcripts/262122052-tradingkey) that “a thriving open source model ecosystem drives greater demand for our cloud computing services, creating a virtuous cycle.” Similarly, ByteDance’s Volcano Engine has a [coding plan](https://cloud.tencent.com/developer/article/2648470) that allows users to use DeepSeek, Moonshot, and Z.ai models.

A second source of indirect AI revenue is advertisements. As AI helps produce content, creators have more content to advertise on platforms, and thus spend more on ads to attract viewers. One interesting example is Seedance, which complements Douyin’s (Chinese TikTok) advertisement business. As Seedance made creating videos cheaper, short drama production companies produced more episodes. In Q1 2026 alone, about 128,000 micro-dramas launched—over 95% of them [AI-generated](https://www.jingjiribao.cn/static/detail.jsp?id=653585)—compared to ~33,000 micro-dramas launched in all of [2025.](https://www.chinanews.com.cn/cul/2026/02-06/10567327.shtml)[9](https://epoch.ai#user-content-fn-9)

After production, short dramas gain viewership by advertising on Douyin. Short-drama producers and distributors devote substantial resources to paid distribution. According to Wang Xiaoshu (founder of Jiashu Technology, a business distributing short dramas),[10](https://epoch.ai#user-content-fn-10) his company’s spending on advertising has grown [tenfold](https://www.36kr.com/p/3835814391100550) over the last year or so.[11](https://epoch.ai#user-content-fn-11) Li Tao (head of Fengxing Culture, the company behind many top short dramas) also emphasized that “for a short drama, 90% of the revenue is spent on online distribution.”

This ad spending is a big part of ByteDance’s business. [An industry insider](https://www.36kr.com/p/3835814391100550) said that AI short-drama advertisers’ daily ad spending on ByteDance’s platform peaked at roughly ￥120 million. If this is true, and average daily spending was even a quarter of that peak, AI short-drama advertisers would be spending roughly $1.6 billion per year on Douyin ads.[12](https://epoch.ai#user-content-fn-12) That is roughly two-thirds of the API revenue for DeepSeek, Moonshot, MiniMax, and Z.ai combined.

AI can also increase advertising revenue more directly by improving and powering the tools used to create advertisements, such as Alimama’s multimodal creative platform Wanxiang Creation.[13](https://epoch.ai#user-content-fn-13) These kinds of tools have produced quantitative results. Alibaba [reported](https://home.alibabagroup.com/en-US/document-1898208128135069696) in 2025 that Chinese e-commerce customer management revenue “rose 10% year over year to ￥89.3bn ($12.5 billion)”, and explicitly attributed the improvement in part to “the growing adoption of the AI-powered marketing tool Quanzhantui.”

Overall, this strategy of supporting complementary products seems fairly lucrative among large Chinese AI conglomerates. It is not surprising that we see similar strategies among US companies. Google [says](https://abc.xyz/investor/events/event-details/2025/2025-Q1-Earnings-Call/) that “with the launch of AI Overviews, the volume of commercial queries has increased,” meaning that more ads can be served to users. Similarly, [Meta’s second quarter 2026 results](https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf) conference call says “9 million small businesses on [Meta’s] platforms are now using at least one of [their] AI ad creative tools.”

## Summary

To some extent, Chinese AI companies face similar business problems to those faced by their US counterparts. For example, consumer AI products can attract large numbers of users who are expensive to serve but difficult to convert into paying customers.

However, Chinese companies face those constraints from a different starting point. Their models are less capable and their businesses are younger. This might have motivated strategies that trade short-term monetization for broader model diffusion, such as by releasing their model weights.

This does not mean Chinese companies will not capture the value they create. They are experimenting with new ways of reconciling diffusion with monetization, such as with modified licenses. Alibaba and ByteDance have an additional solution where they can benefit from widespread AI adoption through cloud computing, ads, and other existing businesses.

As Chinese AI models become more capable, it will be important to keep an eye on how Chinese companies try to monetize their models. The strategies they employ have significant implications for their future investments and funding, and it is crucial to watch how they evolve.

---

All translations are Cheryl’s, unless we specify otherwise.

We would like to thank Alan Chan, Campbell Hutcheson, Zi Cheng Huang, Mary Clare McMahon, Zilan Qian, Konstantin Pilz, Lisa Soder, Jean-Stanislas Denain, Karthik Tadepalli, Elias Groll for their helpful feedback on this article.

## Appendix: Summary by company

Below is a company-by-company summary of the revenue sources discussed in this article. “Main AI revenue source” is our estimate of each firm’s main source of AI-related revenue, based on company disclosure and other public reporting. Estimates for MiniMax and [Z.ai](http://z.ai/) are from their interim reports, annualized assuming 2025’s seasonality.

### DeepSeek

Main AI revenue source: Selling model access.

- Consumer-facing apps: Free [app](https://www.deepseek.com/en/news/deepseek-app/)/web; no ads.
- Selling model access: [Yes](https://api-docs.deepseek.com/quick_start/pricing/). Estimate: [$1B](https://www.theinformation.com/articles/deepseeks-annualized-revenue-hits-1-billion-startup-finalizes-7-5-billion-fundraising?rc=ok83pn), assuming most of DeepSeek’s revenue comes from API sales.
- Enterprise/government solutions: Not publicly identified.
- Licensing fees: Not publicly identified.
- Other businesses complemented by AI: Not publicly identified.

### Moonshot

Main AI revenue source: Selling model access.

- Consumer-facing apps: [Subscription](https://www.kimi.com/en/help/membership/membership-pricing). Estimate: unknown, but probably low.
- Selling model access: [Yes](https://platform.kimi.com/). Estimate: [70%](https://finance.sina.com.cn/wm/2026-06-30/doc-inifesxw6711270.shtml) of total revenue as of June 2026.
- Enterprise/government solutions: [Some](https://platform.kimi.com/#:~:text=%E5%AE%9A%E5%88%B6%20%E4%BC%81%E4%B8%9A%E6%9C%8D%E5%8A%A1-,%E9%80%82%E5%90%88%E4%B8%AD%E5%A4%A7%E5%9E%8B%E4%BC%81%E4%B8%9A%26%E7%89%B9%E6%AE%8A%E9%9C%80%E6%B1%82,-%E9%AB%98%E6%80%A7%E8%83%BD%E4%BF%9D%E9%9A%9C%EF%BC%9A%E5%BC%B9%E6%80%A7). Estimate: unknown.
- Licensing fees: [Yes](https://huggingface.co/moonshotai/Kimi-K3/blob/refs%2Fpr%2F37/LICENSE), for K3. Starting to partner with forward-deployed engineers such as AsiaInfo and let them serve private-deployment and customization projects.
- Other businesses complemented by AI: Not publicly identified.

### MiniMax

Main AI revenue source: Selling model access, together with enterprise services. The two are reported as one figure in the interim report. Note that to categorize these revenues accurately, we use the numbers from the interim report (H1 2026), which differ from the number in the first figure of this report.

- Consumer-facing apps: [Subscription, credits, and ads, mainly on Talkie](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1231/2025123100025.pdf). Estimated 2026 revenue: $107M (based on H1 results and 2025 H1/FY seasonality).
- Selling model access: [Yes](https://platform.minimax.io/docs/guides/pricing-paygo). Estimated 2026 revenue: ARR $208M for 2026 (based on H1 results and 2025 H1/FY seasonality), combining API and enterprise solutions.
- Enterprise/government solutions: [Yes, including dedicated inference resources, customization, and customer deployment](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0109/sehk25122100270.pdf). Estimate: see above, we only know the revenue combined with API sales.
- Licensing fees: [Yes](https://huggingface.co/MiniMaxAI/MiniMax-M2.5/blob/refs%2Fpr%2F50/LICENSE-MODEL), but mainly commercial-use and attribution conditions.
- Other businesses complemented by AI: Not publicly identified.

### Z.ai

Main AI revenue source: Selling model access. Note that to categorize these revenues accurately, we use the numbers from the interim report (H1 2026). As a result, the numbers shown here differ from the $1.8 billion ARR reported by Z.ai management in September, and shown in the first figure of this report.

- Consumer-facing apps: [Subscription](https://apps.apple.com/cn/app/%E6%99%BA%E8%B0%B1%E6%B8%85%E8%A8%80-%E4%B8%80%E7%AB%99%E5%BC%8F%E8%A7%A3%E6%94%BEai%E7%94%9F%E4%BA%A7%E5%8A%9B/id6450893458?platform=mac). Estimate: unknown, but low.
- Selling model access: [Yes](https://docs.bigmodel.cn/cn/api/introduction), now its main business. Estimated 2026 revenue: $805M (based on H1 results and 2025 H1/FY seasonality).
- Enterprise/government solutions: Used to be its main [business](https://docs.bigmodel.cn/cn/guide/tools/model-deploy), but has [shifted away](https://ea-cdn.eurolandir.com/press-releases-attachments./4174940/HKEX-EPS_20260831_12308929_0.PDF). Estimated 2026 revenue: $60M for 2026 (based on H1 results and 2025 H1/FY seasonality).
- Licensing fees: Yes. GLM-5.3 has a custom [license](https://huggingface.co/zai-org/GLM-5.3/blob/main/LICENSE), and has started revenue sharing with Amazon Bedrock and multiple domestic cloud providers.
- Other businesses complemented by AI: Not publicly identified.

### ByteDance

Main AI revenue source: other businesses complemented by AI.

- Consumer-facing apps: [Subscription](https://www.doubao.com/legal/ey01) plus [commerce and channel fees](https://lf9-cdn-tos.draftstatic.com/obj/ies-hotsoon-draft/grace_legal/Shopping-Payment-FAQ.html), which funnel customers to ByteDance’s Douyin shop. High future revenue potential.
- Selling model access: [Yes](https://seed.bytedance.com/en/blog/seed-2-0-official-launch#:~:text=the%20model%20API%20for%20the%20Seed2.0%20full%20series%20is%20available%20on%20Volcano%20Engine), through Volcano Engine. Estimate: [~$4B](https://finance.sina.com.cn/wm/2026-07-30/doc-inikpxkp1334857.shtml) MaaS ARR for 2026. This figure could also include enterprise solutions.
- Enterprise/government solutions: [Yes](https://www.volcengine.com/solutions/Financial-LLM-Solutions), through Volcano Engine. Estimate: see above. ~[$4B](https://finance.sina.com.cn/wm/2026-07-30/doc-inikpxkp1334857.shtml) MaaS ARR for 2026. This figure also includes API sales.
- Licensing fees: No. Mostly closed-weight.
- Other businesses complemented by AI: Yes: [ads](https://www.oceanengine.com/products), [e-commerce](https://lf9-cdn-tos.draftstatic.com/obj/ies-hotsoon-draft/grace_legal/Shopping-Payment-FAQ.html), and [cloud](https://www.volcengine.com/product/apmplus).

### Alibaba

Main AI revenue source: other businesses complemented by AI.

- Consumer-facing apps: [Subscription](https://www.alibabagroup.com/en-US/document-2027233133950140416#:~:text=Qwen%20App%20rolled%20out%20paid%20subscriptions%20for%20productivity%20and%20professional%20features%20in%20August.), rolled out August 2026, plus [Qwen funnels users into Alibaba commerce](https://www.alibabagroup.com/en-US/document-1991231293551017984). Estimate: unknown.
- Selling model access: Yes, [QwenCloud](https://www.qwencloud.com/pricing/api). Estimate: unknown. Model and application services: roughly [$2.4B](https://earningscalls.dev/transcripts/alibaba-group-holding-limited_baba_earnings_call_transcript_2026-08-20) annualized in August. This includes more than Qwen API sales, such as third-party model hosting.
- Enterprise/government solutions: [Yes](https://ue.aliyun.com/), Bailian Dedicated Edition. Estimate: unknown.
- Licensing fees: Yes, e.g., [Qwen-3.8 Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/main/LICENSE).
- Other businesses complemented by AI: Yes: [e-commerce](https://www.alibabagroup.com/en-US/document-1991231293551017984) and [cloud](https://www.alibabacloud.com/en?_p_lc=1&f-8DC992C756BA=). Estimate: AI-related product revenue reached [$1.824B](https://secure.businesswire.com/news/home/20260818525201/en/Alibaba-Group-Announces-June-Quarter-2026-Results) in Q2 2026 (ARR $7.3B).

Notes

1. Hailuo AI is MiniMax’s consumer-facing video-generation product, available through its website and mobile apps and powered by its Hailuo video models; Talkie is an AI companion app. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-1)
2. According to MiniMax’s IPO document, ad revenue is $11,188,000 for the first 9 months of 2025, or on average $41,000/day. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-2)
3. Note that this cross-period ratio is not a conventional monthly paid-conversion rate. MiniMax does not disclose the actual monthly conversion rate. In theory, the true average-month figure could lie anywhere from roughly 0.7% to 6.4%, depending on how frequently those 1.77 million users paid or remained active. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-3)
4. Note that WAU figures are not convertible to MAU when comparing the number to Chinese AI apps in Figure 1. Sensor Tower reports that ChatGPT reached approximately 1 billion mobile MAU in May 2026. We can also compare companies’ app usage with a back-of-the-envelope calculation. According to QuestMobile, Doubao’s MAU in June 2026 is 382.3 million with an average of 143.7 minutes per month per MAU. Multiplying the numbers, we get 915.6 million user-hours monthly. SensorTower reports approximately 215 minutes per ChatGPT user per month. Multiplying that by MAU, we get 3.58 billion user-hours monthly, approximately 4× Doubao’s. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-4)
5. Metered API access charges per token used, with separate rates for input and output. A flat-rate plan charges a fixed monthly fee for a usage allowance; Z.ai’s GLM Coding Plan, which works inside coding assistants such as Claude Code, is an example. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-5)
6. The other way to sell an unmodified model is a flat-rate plan: a monthly or per-seat subscription, usually bundling the model with a harness such as a coding agent. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-6)
7. Note that customers can also customize models themselves. For example, customers can [fine-tune](https://developers.openai.com/api/reference/resources/fine_tuning) OpenAI models on their own training data. This is better classified as part of the API business than as a bespoke customization service. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-7)
8. Z.ai’s gross margin on on-premises deployment went from [66.0%](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1230/2025123000017.pdf#page=265) (2024) to [48.8%](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0331/2026033101549.pdf#page=9) (2025) to [37.9%](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0831/2026083101539.pdf#page=24) (H1 2026, down from 59.1% in H1 2025). [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-8)
9. In Q1 2026, approximately 122,000 of the 128,000 micro-dramas launched in China were AI-generated. However, note that for the Spring Festival season of 2026, “the number of live-action short dramas released was about 1/50 that of AI dramas, but the total number of views reached 25 times that of AI short dramas.” It is possible that live-action short dramas earn more viewers than AI-generated short dramas. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-9)
10. Jiashu Technology is simultaneously [producing live-action short dramas and AI-generated short dramas](https://www.cbndata.com/information/295426), with the latter accounting for 60% of its domestic business. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-10)
11. We don’t know the gross margin of advertising on Douyin, but in 2020, when advertising accounted for ~[77%](https://www.jiemian.com/article/6250854.html) of ByteDance’s revenue, it had an overall gross margin of roughly [56%](https://www.chyxx.com/shuju/202106/957857.html). [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-11)
12. This is an illustrative estimate, not reported ByteDance revenue, and does not account for rebates, taxes, or other differences between gross billings and recognized revenue. We do think 25% of peak spending is within the reasonable range, however. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-12)
13. Alimama is a subsidiary of Alibaba. [![Return](https://epoch.ai/assets/icons/arrow-return-left.svg)](https://epoch.ai#user-content-fnref-13)

## References

[1]: https://epoch.ai/publications/how-do-chinese-ai-companies-make-money "How do Chinese AI companies make money?"
