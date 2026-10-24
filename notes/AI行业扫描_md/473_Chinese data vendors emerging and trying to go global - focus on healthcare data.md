# Chinese data vendors emerging and trying to go global - focus on healthcare data

| 项目 | 内容 |
| --- | --- |
| 作者 | [Grace Shao](https://substack.com/@gshao) |
| 发布日期 | Oct 09, 2026 |
| 副标题 | The appearance of China’s data companies. A story about data quality, networks, walled gardens, and expertise. |
| 原文 | [AI Proem 文章][1] |

## 正文

![Neural network diagram showcasing input, hidden, and output layers, surrounded by colorful code, illustrating data science concepts.](https://substackcdn.com/image/fetch/$s_!wBHb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd046198d-9642-40e6-ae88-2628c5a80f71_1600x899.webp)

*From big data to smart data - Netzsch*

China has spent more than a decade collecting enormous amounts of data, and yet for all of that activity, we haven’t really seen the emergence of big independent AI data companies like Surge AI, Scale AI, or Mercor in the US. This is a little strange when you think about it, and I get asked a lot about it, given China’s massive internet economy, relatively inexpensive labor force and the sheer amount of information that its technology companies have accumulated over the years.

**I think there are a few reasons for this, and they tell us quite a bit about the differences between the two AI ecosystems and the underlying data infrastructure.**

**1/**For one, the market for sophisticated LLM training data is still relatively new, and the US has generally been ahead in developing frontier models, and the upstream has also been built up first in the US. Of course, data labeling existed long before ChatGPT. Companies like Scale AI originally built their businesses around autonomous driving, image labeling and other relatively straightforward tasks, with much of the actual work outsourced to lower-cost labor markets - in India, parts of Africa and Southeast Asia. In China, a considerable amount of that work was already being done domestically - by third tier city workers to support first/second tier city work -, often by the big technology companies themselves or through existing outsourcing arrangements.

**2/**Chinese big tech has also historically been quite protective of its own data, this is not a secret and remains to be the dominant strategy even now. The companies spent years building closed ecosystems, or what people in China often describe as 竖井, vertical ‘wells’ silos, where data is collected and used internally rather than shared with the wider industry. And while China is incredibly sophisticated when it comes to consumer internet products, enterprise software is notoriously a rather different story. Across many traditional industries, data remains scattered across departments and inconsistent systems, making it much harder to collect, standardize, and turn into something an outside company can actually sell. Adding to that is another layer of complexity that is not present in the US: because a good chunk of China's GDP is still dominated by SOEs and their internally built apps and databases, everything is fragmented and scattered.

**3/**But as frontier models become more capable, what the labs need from data is changing. They increasingly want expertise from mathematicians, doctors, lawyers, engineers, and other professionals and specialists, along with realistic environments where AI agents can learn how to perform actual work. They also need more specialized information from industries such as healthcare or finance and/or manufacturing, where much of the data comes in the form of images, audio, video, and other formats (feels) that are far more complicated to process than text.

**4/**And suddenly, companies that already have access to these experts or industry relationships are finding themselves in a rather interesting position. That is why we are now seeing the emergence of Chinese data companies like UniPat and Humanlaya, while older businesses like 本原智数 and 海天瑞声 are also trying to capture this opportunity.

***So why are these businesses only becoming prominent in China now, and how are they building out, and what is each of their competitive advantage?***

## The American data gold rush

In the US, the data business has turned into a rather extraordinary industry over the past couple of years, with companies that most consumers have never heard of commanding valuations in the billions - and now stoking ambition and greed on the other side of the world.

Surge AI is perhaps the most remarkable example. Founded by Edwin Chen, who previously worked at Google, Twitter and Facebook, the company stayed bootstrapped and generated a[reported $1.2 billion in revenue in 2024](https://www.forbes.com.au/news/billionaires/how-this-google-alum-became-a-low-key-ai-billionaire/), ahead of Scale AI’s roughly $870 million that year. Bloomberg reported in July 2025 that Surge was[discussing its first outside funding round at a valuation of at least $25 billion](https://news.bloomberglaw.com/capital-markets/scale-rival-surge-ai-in-talks-for-funding-at-25-billion-value), although those discussions should not be confused with a completed financing.

The company screens contractors for expertise, evaluates their work against quality standards, and helps design the rubrics that define what a good answer looks like.[Anthropic has described working with Surge](https://surgehq.ai/blog/anthropic-surge-ai-rlhf-platform-train-llm-assistant-human-feedback)on precisely this kind of training, where conventional crowdsourcing platforms struggled to provide the expertise or consistency required.

Mercor, meanwhile, sells access to the person. It started in 2023 as an AI recruiting company, then discovered that its ability to find and screen professionals was particularly valuable to frontier AI labs. An HR software company that had accumulated a huge network, including lawyers, bankers, physicians, consultants, and other academics or specialists, started offering candidates an additional option: do you want to spend some of that spare time and teach models how experts actually approach problems in their fields, of course with pay.

In October 2025, Mercor[raised $350 million at a $10 billion valuation](https://www.mercor.com/blog/series-c/). By June this year, the company had reportedly surpassed a[$2 billion gross annualized revenue run rate](https://www.theinformation.com/briefings/exclusive-mercor-hit-2-billion-gross-annualized-revenue), although roughly 60% to 70% of its billings go directly to contractors. That implies approximately $600 million to $800 million in annualized revenue retained after contractor payouts, before other costs, assuming the reported payout ratio still holds. It is an important distinction when comparing Mercor with businesses that primarily sell finished datasets rather than expert hours. For better or worse, entrepreneurs in China are salivating at that valuation, but starting something like this from scratch isn't simple.

And Mercor and Surge are hardly the only ones. Handshake, originally a college recruiting network, was[estimated by Sacra](https://sacra.com/research/handshake-indeed-for-data-labelers/)to have reached $1.1 billion in gross annualized revenue in April 2026 after tapping its network of students, graduates and PhDs for AI training work. Micro1, another former recruiting business, reportedly[raised more than $100 million at a $4 billion valuation](https://www.forbes.com.au/news/uncategorized/this-25-year-old-raised-us100-million-for-his-ai-startup-at-a-us4-billion-valuation/)in September, up eightfold in just one year.

And AI helped me pull even more examples. Snorkel AI has followed a slightly different path. Originally a Stanford research project that became a company selling software to automate data labeling, it has moved toward producing finished datasets and reinforcement learning environments. In September, it[raised $350 million at a $3.5 billion valuation](https://snorkel.ai/blog/data-2-0-and-the-research-era-of-ai-data/), with the company reporting an annualized revenue run rate of more than $375 million.

**What was particularly interesting about these companies is how many did not start out as data companies at all.**They were recruiting businesses, software vendors, or companies that already had access to particular networks of people.As model capabilities improved, those existing relationships suddenly became rather valuable. So as much as these companies get public pushback on their IP infringement, the reality is that what can be scraped has largely been scraped and will be scraped for the sake of LLMs at this point. What they’ve done actually goes beyond the first step of ‘collecting data’; they’ve taken it further to ‘elevate data’ to structured, usable products. The business of data selling/ collecting/ creation/ organizing itself is nascent and evolving in real time, right in front of us.

Much of the original data labeling industry was about volume — especially during its collection stage. It involved drawing boxes around images, transcribing speech, or categorizing content. But today’s reasoning models need more complicated data, and often it is about structuring unstructured data for completing tasks, not just solving an equation. You need someone who actually understands the subject and can evaluate whether the model’s reasoning makes sense.

And now even that business is moving further up the stack, because models are becoming better at generating synthetic data and evaluating some of their own answers. One of the more interesting opportunities is in reinforcement learning environments, essentially simulated workplaces where AI agents can practice completing tasks, use different software tools, and receive feedback on whether they actually got the job done correctly.

In July,[Mercor announced its acquisition of Deeptune](https://www.mercor.com/blog/mercor-to-acquire-deeptune/), a startup that had recreated hundreds of enterprise software environments, including spreadsheets and Salesforce. Mercor already had access to experts who could design realistic tasks, while Deeptune had built the environments where agents could practice them. Surge has been developing similar capabilities through[EnterpriseBench and CoreCraft](https://surgehq.ai/blog/enterprisebench-corecraft), while Snorkel is also investing in environments and evaluation.They’re acquiring businesses with standardized processes that can now be turned into structured data.

**Ultimately, what these companies increasingly want to sell is a combination of expert knowledge, task design, simulated environments and the ability to measure whether the model actually improved.**But then there are limits to how defensible, especially when frontier labs have every reason to develop parts of the process internally. Meanwhile, the combination of expert relationships, technical capabilities, and accumulated experience working on difficult model-training problems has become increasingly valuable.

*Which brings us back to China, where the industry historically developed quite differently.*

## Why did China develop so differently?

We have[written before about how many AI application companies may eventually become data companies](https://aiproem.substack.com/p/who-owns-what-makes-your-company), with their competitive advantage increasingly tied to the proprietary information, workflows, and customer relationships they accumulate. Whether that is exercise and health information, consumer behavior, or purchasing patterns, the data can become one of the most valuable assets underneath the application.

Chinese superapps like WeChat (Tencent), Alipay (Alibaba/ Ant), Douyin (ByteDance), and Meituan, and others like them, have been collecting and studying data for more than a decade. Every transaction, search, and interaction potentially tells the company something more about its users. But accumulating that information is very different from making it available to outside parties, let alone preparing it for AI model training, especially now, when what is needed often comes in various forms — image, text, and even voice.

And these internet platforms have generally preferred to keep their information within their own ecosystems with serious walled gardens. The same goes for banks, hospitals, and traditional enterprises, especially those of SOE nature, many of which maintain their own data systems with relatively little incentive to share — which can also be attributed to the fact that there is no single software proliferated across sectors. People in China often refer to these as 数据孤岛, or otherwise known as data islands.

Of course, owning proprietary data and outsourcing the work required to label it are two separate things. A company can hire an outside supplier without giving up ownership of its data. But I think the tendency to keep information, software systems, and the teams that work historically with them inside the organization helps explain why China’s data-services industry developed differently.

In March, Chinese technology publication[数据猿 interviewed 林震亚](https://caifuhao.eastmoney.com/news/20260403231540397163440)Lin Zhenya, CTO of 本原智数 (no joke, it is called byaidata, no typo here), about why American data companies were so much more valuable than their Chinese counterparts. His explanation was quite revealing. According to Lin, companies like OpenAI and Google are more willing to outsource entire data projects because they trust specialist suppliers to understand the data and how to produce it. Chinese big tech, by contrast, tends to keep that expertise and decision-making internally, leaving outside suppliers mainly to provide manpower at labeling facilities - so think about what ScaleAI essentially sold.

If the model company decides what data it needs, designs the tasks, and sets the quality standards, the external supplier doesn’t necessarily accumulate much valuable know-how. It largely provides labor rather than a complete service, which is much harder to turn into something like Surge.

And there was already plenty of inexpensive labor (in third/ fourth-tier cities) available in China.For relatively straightforward image, speech, and other annotation tasks, large technology companies have largely relied on internal teams or existing contractors without necessarily paying a premium for an independent specialist provider, unlike companies like Scale, which hired lower-cost international workers for US lab use. But cheap labor alone doesn’t explain the difference. The more important question is who owns the customer relationship, the task design, and the expertise accumulated through the projects.

We know that China has been incredibly successful in consumer internet applications, but enterprise software and data management across traditional industries have developed in a more fragmented way. Organizations rarely have a single standardized system or consistent format, let alone across an entire industry as mentioned earlier. Different departments may maintain their own databases, making it hard to extract or use information outside the original workflow.

And the scale of the problem is enormous. According to China’s[National Data Administration](https://www.nda.gov.cn/sjj/ywpd/sjzy/0429/20260429164803571173880_pc.html), the country generated 52.26 zettabytes of data in 2025, while only 22.13% of its stored data was classified as structured. That doesn’t mean the remaining data is useless, since images, audio, and video are naturally unstructured, nor does it prove China is worse than other countries at organizing information. But it gives us some sense of how much of the information exists outside conventional databases - like I said earlier, it’s not that easy to do this actually; there is some technical capability required.

So increasingly, the information that AI labs want is precisely this kind of data. Not just documents and spreadsheets, but images, recordings, video, and the details of how people perform actual work.

The supplier market itself is also fragmented. In the same 数据猿*Data Orangutan*(best translation I managed) interview, Lin estimated that China had between 2,000 and 3,000 labeling companies, with the top three accounting for perhaps 20% to 30% of the market, compared with his estimate of 70% to 80% for the top three in the US. These are industry estimates rather than independently measured market shares, but his reasons for the fragmentation are interesting.

Government projects are frequently awarded to local teams or, of course, SOEs; different industries maintain their own supplier relationships, and the larger companies don’t necessarily have access to every major customer. There hasn’t been the same degree of consolidation around a few national specialist providers as we have seen in the US.

So it is not that China lacked data companies. It had plenty of them, and some had been operating for years. But much of the valuable expertise remained inside big technology companies, while outside providers competed for more labor-intensive projects. The rapid improvement of Chinese reasoning models and agents is now creating demand for a more sophisticated set of services, and that is where the opportunity for independent suppliers is beginning to open up.

## The Chinese data companies are finally showing up

In September,[The Information reported](https://www.theinformation.com/newsletters/ai-agenda/chinas-answer-surge-ai-got-1-billion-valuation-just-30-million-orders)that UniPat, a Beijing-based AI training-data and evaluation startup founded in December 2025, had completed a financing round at a $1 billion pre-money valuation. Its competitor Humanlaya, which claims to be*[“built by model builders, for model builders"](https://x.com/Humanlayadata?lang=en)*had also completed a round at a post-money valuation approaching $1 billion.

[Both companies have received funding from HSG,](https://dealroom.co/news/info-ab64c2-why-chinas-answer-to-surge-ai-got-a-1-billion-valuation-on-just-30-milli/)formerly Sequoia Capital China, and both reportedly serve some of China’s leading model developers, including Alibaba, ByteDance, Moonshot and DeepSeek.

The backgrounds of their founders are particularly interesting, as they all come from big tech. They knew what was needed and left to create and fill in the void along that supply chain

UniPat was co-founded by Li Kuan, who previously worked at Alibaba on reinforcement learning infrastructure. The company originally focused on synthetic data before expanding into expert-generated training data and evaluation. Humanlaya co-founder Jasper Jiao previously helped build ByteDance’s own expert data platform, Xpert, before leaving to establish his company.

Humanlaya has developed an expert platform called TalentsAI, with more than 100,000 people from roughly 300 industries and academic disciplines reportedly registered, although they must pass additional screening before they can qualify for work. This, in a way, is similar to Surge. UniPat is also building an expert network alongside its synthetic data and evaluation capabilities.

It reminds me of how Mercor and Handshake developed in the US. These businesses don’t necessarily start out owning some enormous proprietary dataset. Instead, they knew how to find the right people, found ways to incentivize them to participate, and turned their expertise into something the labs can use. (*Of course there has been skepticism toward this approach*)

China’s older generation of data-services companies are now trying to capture this new opportunity.

One example is 本原智数, a data-services business acquired by C.Banner (千百度, 01028.HK), the Hong Kong-listed women’s footwear and retail group. Yes, a shoe company (*what it is, is using the shell, and it’s not the only one trying to do this).*

According to[C.Banner’s Hong Kong Stock Exchange announcement](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0605/2026060502220.pdf), it agreed to a RMB300 million transaction in June 2026, consisting of RMB150 million paid to existing shareholders and RMB150 million injected as new capital, giving it approximately 90.91% ownership of 本原智数. The transaction valued the business at RMB180 million before the capital injection.

The company generated RMB146.5 million in revenue in 2024 and RMB156.2 million in 2025, with net profit of approximately RMB11.1 million in 2025. It is not independently listed, but sits within a Hong Kong-listed group trying to build an AI data business alongside its traditional footwear operations.

Another is 海天瑞声 (688787.SH), which is directly listed on the Shanghai Stock Exchange’s STAR Market. Unlike the new startups, 海天瑞声 has been providing speech, language, computer vision and other AI training-data services for many years. According to its[2025 annual report](https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12167706), revenue grew 59% to RMB377 million, from RMB237 million the previous year. First-half 2026 revenue grew another 22.5% to approximately RMB192 million.

These businesses are still much smaller than the leading American data providers, but they are useful reminders that Chinese data companies existed long before the current excitement. The newer startups are approaching a different set of problems, with more emphasis on expert-generated data, evaluation, and reinforcement learning.

GOMAX LAB, or 骨码智元实验室, is another interesting new entrant. At WAIC this year, it was already promoting high-quality scientific and industry datasets developed around specialist expertise rather than simply collecting generic internet content. In July, GOMAX[launched a research initiative with China’s National Information Center](https://www.sic.gov.cn/sic/83/260/0722/20260722071357160171379_pc.html)focused on developing an ecosystem for high-quality AI training corpora, including specialist datasets and evaluation standards for different industries.

Now, each of these companies has some previous industry dabbling. They’re not exactly coming in fresh, so they lean into their strengths. One I heard is a company that already has longstanding relationships with researchers, authors, and publishers, which would help digitize their IP. The thinking now is that they may be able to tap into digital content and the expertise of the people who created it, although unclear what the IP access rules around that is - a sensitive and touchy subject obviously. But what they’re betting on now is that the relationships themselves could turn out to be just as valuable as the original content.

And the money is moving quickly. As a newsletter run by former 36Kr reporter[Elsewhere wrote in September](https://elsewhere.news/en/elsewhere/data-companies-are-all-acting-way-too-godlike), some data startups have reached valuations of hundreds of millions of dollars in less than a year.

## From buying existing datasets to creating specialized ones

There is another interesting aspect of China’s data market that we have[touched on lightly before](https://aiproem.substack.com/p/part-i-the-gala-the-suburbs-and-the).

Earlier this year, in conversations with researchers, we learned that some Chinese labs have alluded to waiting for exclusivity periods on certain datasets purchased by American frontier labs to expire before buying access to the same material at a considerably lower price (a fraction).

As we discussed in our[May interview with](https://aiproem.substack.com/p/nathan-lambert-reflects-on-chinas)[Nathan Lambert](https://open.substack.com/users/10472909-nathan-lambert?utm_source=mentions), some Chinese labs were willing to wait until American buyers' exclusivity contracts expired before purchasing the same specialized datasets at a fraction of the price. Nathan's broader point was that competing on increasingly sophisticated training data would require considerable additional investment, not just in compute and researchers, but also in the expert networks and environments used to improve the models.

For many of the labs we’re referring to, the trade-off of preserving (not spending an enormous amount) capital for a bit of a delay is justified.

And this is not simply an old story about Chinese labs relying on data from overseas. The Information’s September reporting confirmed that Chinese model developers continue buying data and services from American suppliers, including Surge, even as the domestic industry develops.

But I suspect that strategy may become less useful as the demand shifts toward more specialized data and customized training environments.

Some datasets can be produced once and sold to multiple customers. Others are designed around weaknesses in a particular model, access to proprietary information, or a very specific industry workflow.The work may not be transferable, and there may not be an equivalent dataset sitting around waiting for its exclusivity period to expire.

This is particularly true when we get into industries such as healthcare, where the challenge isn’t necessarily finding a collection of medical documents, but assembling information that was never designed to be used for model training in the first place. So this will be new know-how.

## The opportunity in specialized and multimodal data

Healthcare is somehow becoming everyone’s new obsession in AI, and I think the data angle deserves much more attention.

Any hospital might have millions of medical images, years of physician notes, laboratory results, recorded consultations, and detailed patient histories. But those records were collected for treating patients, not for training a foundation model. The images might sit in one system, the doctor’s notes in another, while information about treatment outcomes may not be recorded until months or years later.

Now, the good thing is that Western medical practice is quite consistent globally, but the bad news is that no one can ever decipher a doctor’s handwriting, so this becomes a challenge for machines too. But beyond that, even if records are mostly digital, much of the diagnosis is based on experience or even senses that cannot be easily captured by data. Such as voice, visual cues, and even emotional feedback. That is also why radiologists did lose their jobs, as some predicted; their analysis requires judgment that goes beyond just a scan of an image.

Anywho, even if a company has access to all this information, turning it into a usable training dataset is quite a different undertaking. The records need to be cleaned and standardized, the different modalities have to be matched, identifying information needs to be handled appropriately, and in many cases specialists have to explain what the information actually means. Companies like Singapore-based Deep Intelligent Pharma, founded in 2017, are already trying to automate the complicated workflows surrounding clinical trials. Whether businesses like these eventually become valuable suppliers of specialized AI training data is another interesting question.

*Maybe Dr.[Ruby Wang](https://open.substack.com/users/2545218-ruby-wang?utm_source=mentions)can help us fill in the knowledge gap for an upcoming podcast recording.*

Unlike the traditional business of labeling images or transcribing audio, much of the value comes from the ability to combine different kinds of information with expert interpretation.

And again, don’t forget that these are compute-costly tasks. Much of the conversion of multimodal assets into model inputs depends on resolution, duration, and the architecture of the model itself. The different approaches have been shown, such as[OpenAI’s technical documentation](https://developers.openai.com/api/docs/guides/images-vision)shows how images are converted into tokens, while[Alibaba Cloud’s multimodal pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing)distinguishes among text,,audio and image or video inputs.

Those are inference-pricing examples rather than direct estimates of training cost, but the underlying issue is relevant. High-resolution images, continuous audio and video introduce processing, storage, alignment and potentially substantial training-compute requirements. A model needs to preserve enough information to learn from the data without making the cost of processing it prohibitive.

Of course, access to data isn’t the same as having the legal right to sell it or use it for training, and this is the grey area some of these companies are trying to push the line on. Privacy, copyright and licensing rights remain important considerations, particularly in healthcare. But companies that can solve both the technical and commercial problems may end up building something much more valuable than a traditional annotation business.

In June, China’s[National Data Administration formally identified](https://www.nda.gov.cn/sjj/swdt/mtsy/0608/20260608214755016924597_pc.html)high-quality industry datasets, including text, images, audio and video, as a priority for AI development. The timing also helps explain the bolstered confidence in these rising data vendors.

## Where is the money in data?

The valuations of many of the companies we mentioned have attracted a lot of attention, but I think a more interesting question is what these companies are actually getting paid to do. Because under the rather broad label of AI data, there are some very different businesses emerging.

At one end, you have companies like Mercor and Humanlaya, whose main advantage is their ability to find the right experts.If a model lab suddenly needs hundreds of mathematicians, doctors or experienced software engineers to produce and evaluate training data, these companies can recruit and organize them far more quickly than the lab could do itself. The customer is essentially paying for access to specialized labor, along with the screening and management required to make that labor useful. This is largely dependent on network access.

Then there are companies like Surge, which take on more responsibility for the finished product. Rather than simply supplying experts, they help design the tasks, establish evaluation criteria, manage the labeling process and deliver datasets that can actually improve the model. In many ways, this seems more sophisticated or at least has a higher barrier to entry. In this case, the supplier begins to accumulate some of the expertise that previously belonged to the customer and no longer just provides one-time execution, but increasingly helps the lab figure out what those workers should be doing.

There is also a business in[creating datasets that can be licensed repeatedly.](https://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12167706&stockid=688787)Shanghai-listed Haitianruisheng[海天瑞声, for example](https://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12167706&stockid=688787), distinguishes between customized data services and standardized dataset products. The latter can potentially be sold to multiple customers, assuming the company owns the necessary rights, rather than requiring an entirely new project every time. This makes it easier to scale at lower cost.

I suspect this becomes particularly interesting as AI training moves into specialized industries. A medical dataset combining imaging, clinical notes, expert interpretation, and treatment outcomes is not something that can easily be assembled or deciphered overnight. Much of the value may lie in having the industry relationships, access rights and technical expertise to turn all that fragmented information into something a model can actually learn from.

And now companies are moving further into reinforcement learning environments, where the product is not just a dataset but a simulated workplace, complete with tasks and a way to evaluate whether the model succeeds. If those environments can be reused across training runs or different customers, there may be a more enduring business than producing the next batch of labeled examples.

This brings us back to the biggest question for the Chinese suppliers. Historically, the model labs tended to keep the higher-value work internally, leaving external vendors to supply manpower. But if companies like UniPat, Humanlaya and GOMAX can take on more of the process, from sourcing specialized knowledge to designing the tasks and evaluating the results, they could capture a much larger part of what the labs are spending.

Of course, the labs can still decide to build these capabilities themselves, and the data they need today may not be particularly valuable a few months from now. So eventually it won’t be just about the biggest networks or data collections, but about those that keep delivering something the labs would find difficult or too time-consuming to produce internally.

## ByteDance is the whale

Of course, for any of this to work, somebody has to be willing to pay for the data, and ByteDance appears to be one of the most aggressive buyers in China. And following suit are Alibaba and Tencent.

According to the Chinese tech blog Elsewhere, ByteDance is among the Chinese labs most willing to spend heavily on training data, with a reported budget exceeding $1 billion, although the precise period and scope of that figure are unclear, so I would take it with a grain of salt.

In August,[36氪 reported](https://eu.36kr.com/zh/p/3934936980667776)that ByteDance had established a new AI Data & Security department, bringing together previously scattered teams responsible for data procurement, production, synthesis, cleaning, quality evaluation and related work. It is a significant organizational development for a company that already had extensive internal data capabilities, and an indication of how much attention the data side of model development is receiving.

The same report said Zhang Yiming had told the Seed team that ByteDance should resolutely avoid distillation, even if doing so meant accepting some short-term performance gap. CEO Liang Rubo similarly emphasized building the company’s own models and accepting the possibility of temporarily falling behind.

That makes ByteDance’s data strategy particularly interesting. If the company wants to improve its models without relying heavily on outputs from competing frontier models, it needs to invest more in generating, acquiring and evaluating its own training material. Some of that will be developed internally, but not every specialized task or expert network needs to be built from scratch.

And ByteDance is a good example of the tension we discussed earlier.**It has built sophisticated internal data operations, but it is also purchasing services from independent suppliers like Humanlaya and likely others too.**

The big tech playbook now is to keep proprietary data, core research, and evaluation capabilities in-house while outsourcing expert recruitment, specialized datasets, or specific training environments to outside providers. That seems a much more plausible direction for China’s market than assuming the big technology companies will suddenly decide to outsource everything.

The question is how far that change goes. If Chinese labs become more willing to trust specialist suppliers with the design and delivery of entire projects, those vendors have a better chance of accumulating the expertise and customer relationships that made the American companies so valuable in the first place.

And as demand becomes increasingly specialized, the suppliers may find opportunities in industries where the model labs have neither the relationships nor the internal knowledge to collect and organize the data themselves.

## What is actually scarce?

One thing I still find a little puzzling is the tension between how the American and Chinese markets talk about the value of training data.

In the US, much of the investor enthusiasm around Surge, Mercor and Snorkel is about quality, expert judgment and the ability to improve model performance in areas where ordinary synthetic data is not enough. But Elsewhere describes a Chinese market where, at least for now, some labs care more about speed and volume than getting every detail right.

I believe both views could stand.

A frontier lab still needs high-quality data for difficult tasks, but it also needs enormous amounts of material across constantly changing domains. When new capabilities emerge, the labs have to figure out where their models are weak, find the right experts and collect enough examples to improve them, often under enormous time pressure.

And the useful life of certain types of data can be surprisingly short. The blog Elsewhere suggested that some categories of training data may become outdated in less than three months. A dataset that was incredibly useful to a model in June might have much less incremental value by September, given the iteration speed these days and particularly if the next generation of models can already solve those problems.

But I think we should distinguish between the value of an individual dataset and the value of the infrastructure needed to keep producing useful datasets.

So when an individual dataset becomes less useful, relationships with experts, rights to access the original information, and the technical infrastructure needed to produce the next dataset may still be valuable.

I suspect this is where the real differentiation among the new Chinese data companies will emerge. Some will remain expert staffing businesses, others will sell specialized datasets, while a smaller group may develop the ability to continuously collect, structure, and evaluate data that is difficult for the model labs to produce themselves.

Tbh, like how the different players differentiated themselves in the US too. It’s just that we’re moving away from purely collecting raw, scrapable data, and now the value is in what happens after you collect data, or at least the ability to collect unique data.


## References

[1]: https://aiproem.substack.com/p/does-china-not-have-data-vendors "Chinese data vendors emerging and trying to go global - focus on healthcare data"
