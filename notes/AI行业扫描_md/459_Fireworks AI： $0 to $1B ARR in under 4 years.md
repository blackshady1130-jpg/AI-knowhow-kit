# 🌊 Fireworks AI: $0 to $1B ARR in under 4 years

| 项目 | 内容 |
|---|---|
| Author | Ivan Landabaso |
| Date | Oct 01, 2026 |
| Source | [Startup Riders](https://www.startupriders.com/p/fireworks-ai-growth-playbook) |

## 正文

---

[![](https://substackcdn.com/image/fetch/$s_!rcYB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1893760-c14b-4156-ae66-ec20556d79c3_2912x2400.png)](https://substackcdn.com/image/fetch/$s_!rcYB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1893760-c14b-4156-ae66-ec20556d79c3_2912x2400.png)

> **Investors rarely tell you why they passed. [PitchMagic](https://pitchmagic.ai/)** does, before you hit send.
>
> I built it because friends kept asking me for feedback on their pitch decks. PitchMagic grades yours on the 4 questions every investor asks (do I get it, is it real, can it be huge, is it them?), scores it out of 100, marks the exact words to change on every slide, and ranks the 3 fixes that matter most to get your foot in the door.
>
> **Pro members get 10 full reviews free** (€49 value) → [get your code](https://www.startupriders.com/perks).
>
> [Review my deck free](https://pitchmagic.ai/)

---

Hello there!

This week I’m diving into [Fireworks AI](https://fireworks.ai/), a company running open AI models for other companies (i.e. Cursor, Uber, Notion) that recently raised [$1.5B at a $17.5B valuation](https://www.crunchbase.com/organization/fireworks-ai#overview) (4 years after its founding, another AI-wave rocket-ship):

[![](https://substackcdn.com/image/fetch/$s_!F01o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e963b24-af7d-4293-994d-acf7a0d3dbd0_2160x2700.png)](https://substackcdn.com/image/fetch/$s_!F01o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e963b24-af7d-4293-994d-acf7a0d3dbd0_2160x2700.png)

In a nutshell:

* **Product**: think about it like an “engine room” for AI. Companies that don’t want to depend on OpenAI / Anthropic take a free open model (i.e DeepSeek or Llama) and Fireworks runs it for them (fast, cheap and inside their product). Today it apparently already handles **40T+ tokens a day** (tokens are the chunks of words AI reads + writes) for [10K+ companies](https://fireworks.ai/blog/series-c).
* **Money**: the model is what’s quickly becoming a classic = pay per use (i.e. [$0.30 per million tokens in, $1.20 per million out](https://docs.fireworks.ai/serverless/pricing) on a model like DeepSeek), renting chips by the hour (i.e. $8/hr for an Nvidia H100), or pay to train your own custom model. They’ve already passed [$1B in annualized revenue](https://fireworks.ai/blog/series-d-announcement) as of July this year with around [~200 people](https://thenextweb.com/news/fireworks-1-5-billion-series-d-specialized-intelligence) ($5M per employee!).
* **Driver**: loved how they frame it here: *[“Companies are no longer renting general intelligence. They’re building their own.”](https://fireworks.ai/blog/series-d-announcement)*

### 8 growth levers in this drop:

1. Sold Meta’s internal speed tricks to everyone
2. Made switching painless at the moment costs typically start to hurt
3. Had every hot new free model running on launch day
4. Built custom for the fastest-growing customer + then sold it to everyone
5. Made engineers part of the “unofficial” sales team (inside the customer’s Slack)
6. Made a custom model cost the same as a generic one
7. Turned big clouds into both suppliers and a sales channel
8. Bet on deciding which model runs for each task

***📐 Quick note on editorial + methodology**: this analysis focuses on the 80/20 mechanics that explain their growth (it’s not a comprehensive profile, not an endorsement or investment advice). I use AI like a fund leverages an analyst for groundwork, the direction + judgement are mine. Company-reported figures are marked as such, treat directional estimates as directional.*

---

# **Zero to one**

[![](https://substackcdn.com/image/fetch/$s_!HVFT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa7e6ecb-0272-4618-bdcb-3e7abca73502_2048x1148.webp)](https://substackcdn.com/image/fetch/$s_!HVFT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa7e6ecb-0272-4618-bdcb-3e7abca73502_2048x1148.webp)

[source](https://sequoiacap.com/article/fireworks-production-deployments-for-the-compound-ai-future)

* **Who:** 7 engineers who used to run the AI plumbing at my good old employer Meta + Google (6 from Meta and four of them actually from the PyTorch team aka the free toolkit most of the world uses to build AI models today).

  * [Lin Qiao](https://www.linkedin.com/in/lin-qiao-22248b4/) (CEO): led the PyTorch there growing the team from 5 to ~300 people, before that IBM and LinkedIn. She started Fireworks at age 48 (after shelving a 2015 startup plan to learn how to lead people at Facebook). She meant to stay “one year or two” and [stayed 7](https://www.youtube.com/watch?v=PCAiqKCfRSk).
  * [Dmytro Dzhulgakov](https://www.linkedin.com/in/dzhulgakov) (CTO): from Ukraine who’s a PyTorch core maintainer after 11 years at Meta, before intern at Google.
  * [Benny Chen](https://www.linkedin.com/in/benny-yufei-chen-2238575a/): a new Zealand-born engineer who ran ads infra also at Meta.
  * Plus [Dmytro Ivchenko](https://www.linkedin.com/in/dmytroivchenko/), [James Reed](https://www.linkedin.com/in/jamesr66a/), [Pawel Garbacki](https://www.linkedin.com/in/pawel-garbacki-490422/) (all ex-Meta) and [Chenyu Zhao](https://www.linkedin.com/in/chenyuzhao) (ex-Google).
* **Where they started (fall 2022):** they all apparently left Meta about 2 months before ChatGPT came out and the first plan was a platform to help companies use PyTorch. Benny, in 2024 said: *“Exactly how, we didn’t really figure out completely... ChatGPT wasn’t out yet, so we had to [pivot](https://www.youtube.com/watch?v=xGilLPQTymg) somewhere in the middle.”* They raised [$25M from Benchmark and Sequoia](https://techcrunch.com/2024/03/26/fireworks-ai-open-source-api-puts-generative-ai-in-reach-of-any-developer/) before having let alone launching a product. Apparently, fun detail, they started in a building literally called the “Sequoia building” before Sequoia invested.
* **The wedge:** PyTorch was of course free and open so companies like Walmart, Disney, Tesla, Netflix etc used it too and they kept coming back to Lin’s team asking *“can you build this training platform for us? Can you build this serving platform for us?”* Lin took it as a [signal](https://www.youtube.com/watch?v=n7ZBBFL09Nk) the industry was ready / market timing was right, *“and then more importantly, we have the key.”*
* **The MVP:** a platform that [launched in August 2023](https://fireworks.ai/blog/fireworks-ai-fast-affordable-customizable-gen-ai-platform) (11 months in). Run and customize free models through a simple web connection with a free tier for devs:

[![Fireworks.ai: Fast, Affordable, Customizable Gen AI Platform](https://substackcdn.com/image/fetch/$s_!vPKP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F051a78c8-b36e-4cd0-8ba2-e488ea463fae_1024x462.webp "Fireworks.ai: Fast, Affordable, Customizable Gen AI Platform")](https://substackcdn.com/image/fetch/$s_!vPKP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F051a78c8-b36e-4cd0-8ba2-e488ea463fae_1024x462.webp)

[source](https://fireworks.ai/blog/fireworks-ai-fast-affordable-customizable-gen-ai-platform)

* **First users:** *“a lot of ex-coworkers from Meta,”* says Benny plus teams who trusted the PyTorch name (this is a classic Silicon Valley dense network kindling effect), and by mid-2024 the list already included Cursor, DoorDash and Quora.

[![Fireworks Raises $52M Series B to Lead Industry Shift to Compound AI Systems](https://substackcdn.com/image/fetch/$s_!fzOK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65eaf7fd-e507-4e1b-8499-a21a5ac7ddfc_3840x2883.jpeg "Fireworks Raises $52M Series B to Lead Industry Shift to Compound AI Systems")](https://substackcdn.com/image/fetch/$s_!fzOK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65eaf7fd-e507-4e1b-8499-a21a5ac7ddfc_3840x2883.jpeg)

[source](https://en.ain.ua/2025/10/29/fireworks-ai-raised-250m/)

---

# **Growth Mechanics**

## **Lever 1: Sold Meta’s internal speed tricks to everyone**

*“Our biggest differentiation is... Fireworks off the shelf is faster than both of the offerings and second is we’re building a system, not just a library.”* (Lin, [Sequoia](https://www.youtube.com/watch?v=U8FFeG0qeTU))

[![](https://substackcdn.com/image/fetch/$s_!QAD9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72962f45-6492-42e7-b9b3-709b6fa88124_3840x1794.png)](https://substackcdn.com/image/fetch/$s_!QAD9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72962f45-6492-42e7-b9b3-709b6fa88124_3840x1794.png)

**What happened:** at Meta they’d built these tricks that let AI run at planet scale with things like custom code that squeezes more work out of chips, compression that makes models smaller without losing (much?) quality, etc. At Fireworks they then packaged those tricks + rented them to companies through a simple connection.

**The details:**

* In Jan 2024 they said their engine ran [4x faster than open-source alternatives](https://fireworks.ai/blog/fire-attention-serving-open-source-models-4x-faster-than-vllm-by-quantizing-with-no-tradeoffs)
* Speed matters here, you’ve probably experienced it using any of the models consumer facing interfaces: *“low latency is a critical part of product viability... people are not patient enough to wait for half a minute.”*
* By Series B in July 2024 they were serving already [140 billion tokens / day](https://fireworks.ai/blog/fireworks-ai-series-b-compound-ai).
* Meta itself became one of their customers this year.
* But this edge doesn’t last on its own as we see on Artificial Analysis (independent speed rankings) Fireworks sits [6th of 11](https://artificialanalysis.ai/models/deepseek-v4-pro/providers) on DeepSeek’s newest big model.

**So what:** turning a big company’s internal tools into a product is a classic founding play and in this case it got them in the door / great wedge. Speed was an advantage but it isn’t necessarily a lasting moat (rivals caught up within 2 years, its also a little silly to talk about moats in this market considering how fast everything moves, but worth keeping an eye out). Interesting what they’ve done to retain customers (levers 4 to 6 later).

---

## **Lever 2: Made switching easy when costs start to hurt**

*“They cannot open up the floodgate because they’re going to scale into bankruptcy.”* (Lin, [theCUBE](https://www.youtube.com/watch?v=DcnynqHPKOs))

[![](https://substackcdn.com/image/fetch/$s_!hS70!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F185030a3-06d4-4396-9f53-1ba910ad9c03_3840x1794.png)](https://substackcdn.com/image/fetch/$s_!hS70!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F185030a3-06d4-4396-9f53-1ba910ad9c03_3840x1794.png)

**What happened:** companies often build the first version of their AI products on OpenAI, Anthropic or similar because it’s the fastest way to test an idea. If the product takes-off usage can explode and so does the bill and that can be a problem. So Fireworks built for that moment or rather with that in mind. So they made it easy to move over with a few lines of code and the open models it runs cost much less to use.

**The details:**

* Going bankrupt on AI bills comes up in 17 of the 44 interviews we went through for this deep-dive, it’s essentially their sales pitch.
* It now reaches big companies too, the founder Lin recently said in a Sequoia interview: *“their CFO is blocking their AI feature launch because of the cost”*
* The pain in the market has become so big / obvious that apparently they barely marketed. Lin recently said on 20VC *“we feel product speaks for itself... we didn’t spend much time [marketing](https://www.youtube.com/watch?v=PCAiqKCfRSk) at all.*”
* They apparently priced for the comparison table, moving in March 2024 to a flat price per token *“because people would often make comparisons using output token cost*”.
* And just to show you how fast these switches are going for out there apparently Innovative Solutions (AWS partner) moved *“90% of Anthropic inference spend”* to Fireworks in 2 weeks ([case study, May 2026](https://fireworks.ai/blog/innovative-solutions)).

**So what:** they never fought OpenAI for the prototype. They waited for the moment the bill hurts and made leaving nearly free. In strategy terms they’re the cheaper substitute for the closed labs, and a substitute only wins if switching is painless.

---

## **Lever 3: Had every new “hot” free model running immediately on launch day**

*“We are very proud of day zero launch always. Like we kind of become famous on day zero launch.”* (Lin, [Startup Grind Q&A, May 2026](https://www.youtube.com/watch?v=nFA-gt3Y29U))

[![](https://substackcdn.com/image/fetch/$s_!Hci6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0f0d175-b4fb-4659-8d9b-a6042d13173e_3840x1794.png)](https://substackcdn.com/image/fetch/$s_!Hci6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0f0d175-b4fb-4659-8d9b-a6042d13173e_3840x1794.png)

**What happened:** every time a new free model came out like DeepSeek, Kimi, Llama etc. etc., they tried to have it running for customers the same day.

**The details:**

* DeepSeek R1 came out in Jan last year and they had a [full breakdown](https://fireworks.ai/blog/deepseek-r1-deepdive) 4 days later.

[![deepseek r1 benchmark performance against claude-3.5-sonnet-1022, gpt-4o, DeepSeek V3, OpenAI o1-mini, and OpenAI o1-1217](https://substackcdn.com/image/fetch/$s_!Ffok!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8628f21c-502a-4753-af0c-3032527103c5_1080x1080.webp "deepseek r1 benchmark performance against claude-3.5-sonnet-1022, gpt-4o, DeepSeek V3, OpenAI o1-mini, and OpenAI o1-1217")](https://substackcdn.com/image/fetch/$s_!Ffok!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8628f21c-502a-4753-af0c-3032527103c5_1080x1080.webp)

[source](https://fireworks.ai/blog/deepseek-r1-deepdive)

* OpenRouter’s CEO says Fireworks *“captured most of the inference”* on DeepSeek in the early days at least *“as far as our metrics told us”* ([Sequoia](https://www.youtube.com/watch?v=aRpzxkct-WA))
* Two months after R1 they matched DeepSeek’s API price at [$0.55 in and $2.19 out](https://fireworks.ai/blog/fireworks-ai-developer-cloud) per million tokens.
* They also know when to break their own rules intelligently for example with DeepSeek’s V4 release since it had bugs, so they held it back about 3 days.
* They now host [200+ models](https://fireworks.ai/blog/series-d-announcement) and add one pretty much every week these days.

**So what:** the open-model boom to certain extent was luck in terms of a tailwind, but what they did differently was treat each launch as a free acquisition moment and try to never miss one (turning others’ announcements into their own marketing).

---

## **Lever 4: Built custom for the fastest-growing customer, then sold it to everyone**

*“We have finite engineers like everybody else. We would like prefer to have engineers make training more efficient... rather than like spin up like a inference effort.”* (Federico Cassano, Cursor, [Sequoia 2026](https://www.youtube.com/watch?v=UDTr9yUnLUI))

[![](https://substackcdn.com/image/fetch/$s_!UqHs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7516e1de-1446-4699-864f-2ffe97fdfb38_3840x1794.png)](https://substackcdn.com/image/fetch/$s_!UqHs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7516e1de-1446-4699-864f-2ffe97fdfb38_3840x1794.png)

## References

[1]: https://www.startupriders.com/p/fireworks-ai-growth-playbook "🌊 Fireworks AI: $0 to $1B ARR in under 4 years"
