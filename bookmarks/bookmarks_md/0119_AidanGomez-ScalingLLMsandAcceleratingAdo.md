---
url: https://wandb.ai/wandb_fc/gradient-dissent/reports/Aidan-Gomez-Scaling-LLMs-and-Accelerating-Adoption--Vmlldzo0MTIwODU0
title: "Weights & Biases"
description: "On this episode of Gradient Dissent, we’re joined by Aidan Gomez, Co-Founder and CEO at Cohere. Cohere develops and releases a range of innovative AI-powered tools and solutions for a variety of NLP use cases. ."
author: "@weights_biases"
captured_at: "2026-03-08T10:34:01.629Z"
---

# Weights & Biases

## About this episode

On this episode, we’re joined by Aidan Gomez, Co-Founder and CEO at Cohere. Cohere develops and releases a range of innovative AI-powered tools and solutions for a variety of NLP use cases.

We discuss:

-   What “attention” means in the context of ML.

-   Aidan’s role in the “Attention Is All You Need” paper.

-   What state-space models (SSMs) are, and how they could be an alternative to transformers.

-   What it means for an ML architecture to saturate compute.

-   Details around data constraints for when LLMs scale.

-   Challenges of measuring LLM performance.

-   How Cohere is positioned within the LLM development space.

-   Insights around scaling down an LLM into a more domain-specific one.

-   Concerns around synthetic content and AI changing public discourse.

-   The importance of raising money at healthy milestones for AI development.

## Connect With Aidan

## Connect With Cohere

-   ﻿[Cohere on Twitter](https://twitter.com/CohereAI)﻿﻿﻿﻿﻿

## Resources

## Listen

## Transcript (via Otter.ai)

Aidan Gomez 0:00

I think by and large, fine-tuning is like a mature system feature. It's like you want to fine-tune the model after you've exhausted all the other things that you can do. It's really only once the system has been deployed, optimized, and then eventually landed the fact Okay, the only way for me to squeeze more performance out of this is via fine-tuning.

Lukas Biewald 0:25

You're listening to gradient descent, a show about machine learning in the real world. And I'm your host, Lucas DeWald. Aiden Gomez is the CEO and co-founder of go here. And the author of the seminal paper Attention is All You Need, which introduced transformers. I've been looking forward to talking to him for a long time, and he's super willing to answer my crazy questions like how many universes in the metaverse do transformers exist in the form it's taken? This is a really fun, thoughtful interview, and I hope you enjoy it. And I think the place that I really wanted to start was, you're one of the authors of the Attention is All You Need paper, which has to be one of the most influential papers of all time. And I think most people listening to this would have read it. But maybe you could describe the result just to catch up with the few that haven't heard of this paper.

Aidan Gomez 1:20

Yeah, for sure. I appreciate you saying it's one of the most influential papers of all time. I don't know if I believe that, but it's definitely influential for the current time. Yeah, I was part of the paper back when I was at Google Brain. I was just like an intern there during my undergrad and I landed under the management of Lukash, Kaiser. And he and I built this software platform for training big neural nets called tensor. And then during the internship very early on, we connected with Nam, and Jakob and Ashish and Nicky and convinced them to train the models that they were exploring on tensor, two tensor. And that model, what they were building ended up being the transformer. So it's like a architecture, which the purpose was really to come up with a much simpler, more refined, scalable architecture than LSTMs RNNs, which were the category of model deployed itslearning before the transformer. And some people view transformers as extremely complex. I think most of those people aren't putting it in comparison to LSTMs and what came before, because transformers are really just like an attention block stacked on top of a multi layer perceptron or feed forward layer, and then a bunch of those stacked on top of each other. And so I think that's an incredibly simple and yeah, in comparison to what came before a very simple platform to build off of. Obviously, with the benefit of hindsight, the importance of scale is now obvious. But back then I don't think it was there was like the general rule of thumb, which was the bigger the neural network, the better. But I don't think people really grasped how far we in the field needed to push that there were still fears of big models were fitting was this big fear. And you don't want to get too large, because you're going to start performing worse at the task that you care about. But I think we took a bet that we can take this to a more extreme level and scale this up to not just single digit accelerators or 10s of accelerators, but 1000s of accelerators. And that bet paid off.

Lukas Biewald 3:29

I guess what inspired you to try the attention mechanism without the underlying LS TM I remember when attention first came out on these recurrent neural networks. I guess in hindsight, it seems like an obvious thing to try. But I guess what inspired you to do that? So I

Aidan Gomez 3:45

think for one, it was like very much a team effort and certainly driven by folks like gnome and Jakob II, Clairol like question. Yes. So like my understanding of where the inspiration came from attention had been already hugely successful, actually, with RNNs and with LSTMs. And it became this really crucial part of the stack in that old generation of sequence learning with RNNs. But I think the notion of attention from a neuroscience perspective was really attractive. And it was viewed as something that was fundamental to human intelligence. And folks like Geoff Hinton, I think really appreciated that and the people that I was working with, you know, men like Jakob, they saw that same sort of elegance in the structure, then they say, saw that same fundamental importance of attention as a computational modeling structure or tool. And they wanted to put that front and center in a model and see what popped out the other side. And so taking away all the other complexity, taking away all the other little tricks and hacks they wanted attention to shine through as the fundamental unit of intelligence within this neural net architecture. Yeah, so that was a seed.

Lukas Biewald 4:59

That's Tension is such an evocative word. Like, it's hard not to extrapolate units, her own brains and things like that when you use the word attention. But yet the math of a transformer is super simple. And sometimes I wonder if the math came from a different path, it might not be called attention. I imagine. Do you think there's any truth to that? Like how fundamentally attention is this thing?

Aidan Gomez 5:29

Yeah, I think the other way of describing it is like a soft lookup, right? Like you're doing some sort of soft lookup in a table. And by soft, I mean, the hard lookup would be just looking at one entry in a table soft lookup would be looking at a bunch of different entries, with different weights associated. And as far as I'm aware, the tension was branded attention by BATNA or whoever that was, but they were parallel efforts in integrating and lookups into neural network. So I think you're right, that description of attention is very salient. And from an intuition, perspective, from making a computational concept, intuitive. Attention is just way better than a lookup, right? A soft lookup attention, we can understand we can grok it, we get what the model is doing underneath, much more quickly than if you use language from databasing, or something like that. And so from a branding perspective, I think attention just took off because it maps onto our own understanding of these things much more closely. It gives us better analogies to work with the concepts.

Lukas Biewald 6:33

Okay, so another experience that I've had with neural networks is that it seems like the exact details of the architecture often doesn't matter. And we ended up kind of picking these architectures based on trying to replicate previous papers and not wanting to mess something up. How fundamental Do you think transformers are? And maybe to make it a more well formed? Question? If you've ran back history, 1000 times? How many of those times do you think you would get the transformer architecture specifically? Here?

Aidan Gomez 7:09

That's a really interesting thought experiment. I don't think it's that fundamental. I think this is less and less of a hot take. But I think all you really need to do is saturate compute in a good way, you need to come up with an architecture that scales that is sufficiently simple, that people can mess with the architecture itself and explore their own ideas within it. But yeah, sufficiently scalable, that you can basically go to any parameter count that you want, in a nice way.

Lukas Biewald 7:35

So do you think we're the only universe in the multiverse where there's the exact transformer calculation?

Aidan Gomez 7:42

I think there's probably countably infinite instantiations that do use the transformer gets more than measure zero of that. Yeah, it's I think it's measures there.

Lukas Biewald 7:51

I think it's I think it's measures here. fascinate Yeah,

Aidan Gomez 7:54

I think there's like loads of combinations we could have landed on at, I just feel like it's really unlikely that the transformer is optimal. I think there's like still more exciting avenues to explore in particular SSMS. So state space models, those are emerging as like, really promising alternatives to the transformer.

Lukas Biewald 8:12

How does that I'm not familiar with that. How does that work?

Aidan Gomez 8:15

Yeah, I'm not familiar with it either. But it's potentially the next step.

Unknown Speaker 8:18

There is this idea to give me a link to learn more about,

Aidan Gomez 8:21

I think, read the s four paper. The general principle what makes you think that there probably is like, if you don't understand that I'm getting I'm being facetious. So SSMS The idea is that we're trying to cut some middle ground in between transformers which are like fully auto regressive, they attend over the entire past sequence. And then on the other end of the spectrum are LSTMs or RNNs, which they have a state and they just they need to memorize in order to remember the past. So ssmc are trying to find this middle ground where, yeah, you have some window within which you can do look up. But for everything that's outside of that, you can rely on an internal memory that you can read and write from. Okay, so doing that, which sounds a lot like a middle ground between the two doing that while also being extremely scalable. So you can paralyze it across 1000s of 10s of 1000s of accelerators. And it's trying to strike that middle ground. I think its success is going to be predicated on whether the community builds tooling for it. Because obviously, like the folks hugging face with the Transformers library, and many others, they built incredible software tooling for transformers, they make it like trivial to scale from 10 million parameters up to a trillion parameters. Nowadays, they've made that trivial, which is tons and tons of work at the software level for SSL gems for state space models. It just doesn't exist today. None of that exists. There's no mature software platform for scaling these things. So I could see a world where trends farmers get replaced SSMS, the software support for them gets more mature. And our next generation of model, we lose that context window constraint that transformers give us where it's like you have this many tokens, anything outside of that, sorry, I have no idea about it, I've never seen it. Instead, you get something that, in theory could have an infinite context window. And it could just continuously read and write from this big buffer of memory. Although

Lukas Biewald 10:27

it seemed like the latest GPT four release had quite a large context, when I was kind of surprised to see how big that context window had gotten. Do you think they're doing something fancy to make that possible?

Aidan Gomez 10:40

Yeah, there are nice techniques like alibi and others that let you quite naturally extend. So even if they did train it on, let's say, they trained it on a context window of 8k tokens, they're able to serve one that has access to 32,000 tokens, because they have methods that at inference time can quite naturally quite easily go beyond that limit. That was like an important breakthrough for not alleviating completely the limitation of transformer context windows, but giving you like a workaround, I still think we need to push pass on I still think memory is going to be an important piece of that. But definitely it makes the issue far less painful

Lukas Biewald 11:21

Can you say more about what it means to saturate compute, like, I guess from my perspective, correct me if I'm wrong, the thing that transformers has just done phenomenally well, is scale as compute gets bigger. And it seems like almost like nothing else like it just every level of compute, it seems to continue to forms continues to improve. And I don't think that was true of other architectures that folks have used in the past. But if transformers is measure zero in the metaverse, what are other ways that you think that compute can be saturated?

Aidan Gomez 11:59

I think a very high measure a set of architectures are the ones that saturate compute. That's like a necessary component of success

Lukas Biewald 12:07

What does it take for an architecture to saturate compute,

Aidan Gomez 12:10

it requires tons and tons of mammals, and very few unnecessary ops, you really want your entire architecture to just look like big, big mammals.

Lukas Biewald 12:22

But wouldn't that be true of just sort of like very classical, just like fully connected neural network would satisfy that condition? Right, that would be ideal, why wasn't a multi layer perceptron work, then it seems like it would satisfy your condition is laid out,

Aidan Gomez 12:37

I think transformers are almost MLPs. And they're like a very short skip away from MLPs. So they do look like just a bunch of Madballs, they add it in like one more access to do miles across. And that's the length of your sequence. But I think it's basically trying to cut as close to a massive MLP as you possibly can, because those do saturate, compute the best. What you want to avoid are tons of little ops, like soft maxes and little activation functions, drop out layers, all of these little things, which break up those big map malls. And you certainly don't want to introduce operations that require that break your horizontal scaling of layers, your ability to split a layer, across 10s of accelerators. So you're widthwise, parallelism, anything that you have to do intra layer access across these trunks, that slows things down, because now you need to start communicating between those parallel lines of compute. So you want to minimize the amount of like intra layer communication that you have to do and just maximize your ability to paralyze that, let it run and then come back with the result. Yeah, that's that's really just a computational

Lukas Biewald 13:48

optimization. Right? There's nothing sort of like intrinsic about that. Intrinsic in one sense, I guess. Do you think almost like any architecture, trained for long enough with enough parameters would have this property that it would improve over time? And then really, what you're looking for is something where you can do back propagation distributed quickly, is that what you're saying?

Aidan Gomez 14:13

I do believe that there are a lot of possible architectures that would be fast, efficient, and result in performance that we're seeing from the current large language models. There are some things you can't literally just scale up a MLP was really loose, because that would be done point wise, right? It would just be a bag of words model, you wouldn't be able to learn relationships between words do you need like sequence structure, you need to train sequence models, but so long as you're not breaking that, or like severely compromising that? I think there's a huge swath of models that would perform equivalently well, and would scale equivalently well, and we've mostly just had this joint optimization between our software like that Transformers in the frameworks that train them. And even our hardware, like the routines that we support within CUDA and within our accelerators. It's been feeding back on each other for a little while now. And so at the moment, there might be like a local minima, where it's hard to break off of transformers, because there's just so much software and hardware support for transformers, it's so heavily optimized. As soon as you step off of that rail, you're sacrificing some performance because now you're dropping back to a more general implementation of a kernel, which runs 20% slower, which for a big model costs you, I don't know, a million dollars for something. So there are some interesting effects there with that feedback between hardware and software and us getting locked in to one architecture.

Lukas Biewald 15:43

So then do you think that there's no architecture that's sufficiently better than transformers, that there would be an impetus to change?

Aidan Gomez 15:53

I think stuff like the sequence length constraint could be problematic enough that it actually might push us off of transformers? Yeah, I would not be surprised if that was the case. That is like a scaling quadratically in the sequence length is a huge problem, one that you only run into once you start doing more and more interesting stuff. But I think we're heading into that territory, especially with multi modality.

Lukas Biewald 16:18

I would think, then, that you would predict that the model performance will continue to scale consistently, as compute is added basically, forever. Would you agree with that?

Aidan Gomez 16:35

Yeah, I think it is quite predictable. If you fix the data set, you fix the architecture, and you choose your levers of scaling, it is going to give you quite a predictable scaling pattern or scaling law.

Lukas Biewald 16:47

And how do you think about data constraints as the model complexity grows, like is data going to be the next constraint then for building very large MLMs?

Aidan Gomez 16:59

Yeah, it already really is. So I think of these models, they think of the tech stack for large language models as a literal stack where each piece builds off the one before. And we started with base models, like GPT, three, and you just train on, I don't know, like a trillion tokens scraped from the web. And super noisy, but you learn a little bit about a lot of different stuff, you consume a ton of knowledge from all over the web, that model is like, it's not useful. It's very cool that it has some prompting few shot behavior and that type of thing. But it's really hard to make it useful for you. And so what you need to do is then train what at cohere, we call them command models, open AI, calls them instruct models need to train these, like instruction tuned models from human feedback. And that changes the model into something that is way more useful changes the UI onto the model. Now you can just give it a natural language instruction. It leverages all that stuff that it learned from the first training phase of just the raw internet, but it's just a much more pleasant user experience. Those are like far more useful. The next step above that is dialogue models. And so again, you go out and collect some human data of dialogue of conversation. And you fine tune that command model, that instruction following model to do dialogue. Again, that unlocks another huge improvement in user experience. People just love conversation, right? Because what you and I are doing right now it's the natural intellectual modality, it's the most natural thing for humans to do is chat to each other, have a conversation. And so when you flip into that modality, when you flip into conversations driven by data, when you flip into command following or instruction following, it's driven by human annotated data, so this tech stack that we're working along, the vertical momentum is like ostensibly, entirely driven by data, there's almost no modeling changes. So what is the vertical momentum, or vertical momentum up this tech stack, I'm thinking base model, command model, dialog model, et cetera, et cetera, the momentum up that tech stack, the thing that takes you from one layer to the next, it's all data.

Lukas Biewald 19:10

What is a model? Like before it's had this sort of specific human feedback to make it respond to commands like what does it feel like to interact with that

Aidan Gomez 19:21

feels a little bit like, schizophrenic, it's like, very all over the place. It's hard to get it to do what you want, you're trying to give it instructions, and it might break in some very unpredictable way, you might change one word and suddenly it gets what you're saying and is capable of actioning on it. But it's a very inconsistent partner to build with and to create systems with. So it knows tons of stuff and has tons of ideas and can vaguely pull from it's big, vast breadth of knowledge, but it's very disorganized. It's very hard to pull it coherent behavior out of it.

Lukas Biewald 20:03

And then what exactly is happening in that fine tuning phase with the human feedback? What exactly are you doing?

Aidan Gomez 20:08

So you're collecting examples of the behavior that you want the model to possess. So in the command phase, which is just one layer above the base model, you're collecting pairs of examples that are like, I give the model and instruction and the model response. Following that instruction, you do that a bunch of times for a ton of different tasks. And the model just picks up the general idea of okay, the user is going to tell me what they want me to do with some data. And my job is to just respond with the answer. And it starts to behave like that. And so now, it's not super finicky about the placement of words, the word choice is like kind of indifferent to that. And that UI is just way more usable way more useful.

Lukas Biewald 20:54

How did you measure if that's working? Or how do you know when you're done with that part?

Aidan Gomez 21:00

Yeah, so measurement of performance, like evaluation of these models is incredibly hard for a bunch of different reasons. One of them is like, a lot of the academic data sets that we have are super noisy and low signal. And they might actually be like negative signal, like if you're doing really well on a particular academic data set that might be like cause for concern, which is worrying. And then the other piece is that these models have seen the internet. And so there might be like, leakage, right? There might be tests that leak with leakage. And so I think the only reliable measure is actually putting it in front of people. And asking them which models you prefer, you put two models in front of them, you let them interact with both put prompts into both, and just pick the one that they prefer. That's the most reliable measure. But what I was just describing of going from the base model up to the command model, you can just measure that an academic dataset performance, if you throw a base model at these academic datasets, and you throw a command model, which is really just like a derivative of the base model command model is going to perform just leaks leaks better, dramatically better.

Lukas Biewald 22:05

And much like effort. Is this step? Is it like comparable in cost to training? The base model? Or? Like how like practically, like, how long does it take, like, How expensive is it?

Aidan Gomez 22:19

It's really hard to get right. Of course, it's all data collection, the scale of data is way less. And the chain of training is way shorter than the initial phase, like the base model phase, we're certainly not talking about trillions of tokens in this curated data regime. But the specific tokens that you choose are extremely important, they need to be noiseless need to be extremely peint combed over and make sure that they're clean and make sure that there's no noisy samples in there. And that's a really difficult, expensive process. It involves a lot of humans looking over a lot of data in terms of like comparison of the cost, it's definitely less than the base model. It's definitely less, I don't know, like the relative ratio. Yeah, I would say it's all expensive, it's certainly expensive to get humans to generate data for you. That is like extremely costly. And the more valuable the data, the more smart or challenging or the more valuable the data, the more expensive it is to get. You can imagine, if you want your model to be as good as a lawyer answering legal questions, the data that you need to collect there is going to be from lawyers that cost $1,000 an hour. And so the costs can be extreme.

Lukas Biewald 23:38

I guess when I look at the performance of large language models, there, it's hard to not sort of infer this exponential curve and expect that like in a year, they're going to be even more amazing than they are today. But if your view is that we've hit this wall with data for the base model, is that wrong then or like we are on the verge of needing a totally new approach?

Aidan Gomez 24:08

I think we are approaching the need for another scaling breakthrough. I guess I don't know how close we are to it. But it definitely feels like it's coming up and we're starting to hit the limits of these models are increasingly operating it average human performance or above on such a wide selection of tasks that you can no longer rely on the average human as a source of data to improve your model. Obviously, once your model performs as well, as an average human, it's no longer valuable to collect data from average humans because they don't add to the models performance. You need to start going to exceptional humans, you need to start going to experts in particular fields or outliers in terms of performance in particular things. And eventually you run into the bottleneck of humanity's performance on a particular task and then you can't go to humans. To offer data that outperforms your model, because your model is already performing, as well as the best human at that task. And so you need to search for a way for the model to self improve, and to work with itself and test itself to start getting effects like you saw with Alpha zero, where it's obvious how to do that, in a game playing setting, write two copies of the model play against each other, they self improve by each one gets a little bit better, and the other one has to beat it, it's much more difficult to think about how you would do that with a large language model. But at some point, once these start to reach top tier human performance, we're going to have to find ways to enable that sort of interaction and self improvement.

Lukas Biewald 25:42

Interesting. I mean, it does appear like these models can do lots of things that the average person can't do, or I can't do, I guess, one domain where it's kind of easy to sort of check them to generate is code generation. Right? I mean, I'm, like, amazed at the quality of, or maybe the rapid progress. And in cogeneration, it sort of seems to me like, it could be easy to at least know if you got the right answer for a cogeneration problem. Does that seem like maybe more tractable than other domains?

Aidan Gomez 26:14

Yeah, writing software is nice that you can run it. And if it doesn't compile, that's a huge issue. And if it runs, but outputs the wrong answer, there's a very clear signal for success there. It's much softer in other areas. So I definitely think that code is, has nice properties. For those reasons. Evaluation might be easier, although it's verification of code is like, also a super hard problem. And there can be like very subtle bugs that your tests don't capture that the model might introduce, then you'll miss and then you'll deploy this and it could have catastrophic consequences. You know, in some sense, it's nice, because it feels like a much harder and more objective. Yes, the model did well, or no, it didn't, although there's nuance to that whole topic as well. But yeah, I also think it's a limited setting, as well, there's a lot you can do in code and in software development. But if we're trying to completely transform human productivity, or you know, value creation, or whatever, we have to step outside the bounds of code. And we need to be able to automate work in spaces that have nothing to do with code. So it's a great platform for experimenting and developing these models. But we have a lot to do outside of code as well

Lukas Biewald 27:26

That makes sense. I'd love to ask you, but your company cohere. Right, yeah. You're also CEO of a company that's building these models and making them available. That how would you describe coheres like positioning in the landscape of companies building and selling these large models?

Aidan Gomez 27:44

Yeah, so for cohere that we got started, I think, three and a half years ago. So that was before GPT. Three, but I believe after GPT, two, and even back then, like the founding mission, it was really just to get this tech deployed in as many hands and as many products as we possibly could. I think my co founders and I, Nick and I met and we were obviously part of the folks that got the earliest access to these sorts of models, these generative models. And I felt personally like it had pulled my timelines for like interesting, compelling AI way forward, like decades forward. And so it felt like we were getting a glimpse of the future and that there was a very important technological frontier that was about to get crossed. But we weren't seeing things lining up. To make these models accessible to people. They were behind barriers, they were inside of large behemoths, and they weren't being put into the hands of developers and enterprises weren't being supported in overcoming the barriers to adoption. And so cohere our product or company that the whole point is really undo those barriers, put it in more hands, make the API's easy to use accessible to folks who aren't machine learning expert, and then solve all those barriers that enterprises have to adoption. I think the reason why it's taken this long. To see the surface area of products and technology change with MLMs is because of mundane stuff, like data privacy, and people's trusting these models and us building awareness so that there's actual consumer demand for know the way that I want to interact with your product is through dialogue, right. We're now at a point where it feels like the market is seeing that and enterprises are starting to see that the consumer is going to choose the product that lets them interact with it in the best possible way. In the same way that like when I was graduating from high school, I chose my bank because it had a mobile app. And that's how I wanted to interact with my bank. I didn't want to I don't know use my browser or walk into an actual physical location. I just wanted to on my phone in the future. I think like the next generation is graduating from high school. They're going to choose their bank based on the one that They don't have to, like call in to debug something, they can just talk to it, they can just chat to it at three to those consumer product decisions are going to be based off of the interfaces that they're able to use products with. And cohere wants to help enable that, to help accelerate organizations in adopting that because it's going to become a competitive necessity. So yeah, the vision is to really just support everyone in adopting this tech, and to help accelerate that to accelerate that adoption.

Lukas Biewald 30:29

Do you offer a way to use these models without the data leaving your own infrastructure?

Aidan Gomez 30:36

Yeah, totally. So we're cloud agnostic, we're not locked into any one cloud. And yeah, like the data privacy piece is a super important one, especially if you're working with customer data, or like internal documents and secrets, so we can deploy within your VPC. No visibility on our side of your data. So yeah, data privacy is a core feature for us.

Lukas Biewald 31:00

And I guess, it seems like you offer, you know, specific use case based API's. But I mean, one thing I've been struck by with GB three being publicly available, it's just the plethora of use cases that seemed like maybe possible or new use cases possible, I guess, like, how do you think about that? Or is there a way to views your models more flexibly? Or do you plan to release like tons of API's on every possible way to someone might want to use a model like this.

Aidan Gomez 31:30

So we have the general models, which are like our command models, and you can use them for anything within Terms of Service, right? Like Super General, whatever you want to do in it extraction, summarization, just chatting to it, like whatever you want to use it for. It'll support it. And if it doesn't support it, let us know. And we have the ability to improve it next week when we launch a new version. So I think, yeah, definitely, the general purpose nature of the technology is a huge piece of the value prop that you can just go to one model, and you can get it to do tons of different tasks for you. At the same time, there is value to specialized endpoints, which we also build stuff like the summarize endpoint that we built, the classify endpoint, the search endpoint. And so those specialized ones are much more targeted. And there's only going to be a few of them, because we're only going to focus on the most popular use cases, like summarization, like search, like classification, but those will be very tailored to that use case. So there's both there's like the highly General Command style model, and then there's specific endpoints targeted at one use case.

Lukas Biewald 32:37

How do you think about open source in general and sort of opening up these models more?

Aidan Gomez 32:45

Yeah, I love open source, I come from research, which is inherently are supposed to be inherently open. At the same time, I am trying to build a business, something that's sustainable, an economic engine, lets us continue to innovate, continue to compete, and giving away your IP for free tends to be a bad business model, you disintermediate yourself. So we've been very hesitant to do that, principally from the fact that we want to build something healthy and sustainable. And we want to be doing this for the rest of our lives. And to do that we need people to pay us for the work that we do. But I'm super, super supportive of more open models, and better performing open source models, there will always be that category of developer who didn't want to use an API, they want to get right down to the parameters and mess around with that and compress the model onto their laptop, etc. And I think there's loads of groups out there that are doing that work and are building that foundation, I think, a Luthor carpers, there's loads of these folks who are doing that. And so I'm super happy to see them out there. And I really appreciate the work that they do.

Lukas Biewald 33:57

I think I saw a result from Stanford recently Paco, where they the ket, an API of an LM quite a bit to the point where they are able to kind of reconstruct the LM for a really small amount of money. Does that seem right to you? Does that approach like worry you that your customers might rebuild your models?

Aidan Gomez 34:19

I think it doesn't seem right. I think the result may have been a little bit exaggerated, or maybe misunderstood by some folks like the performance of that model is super impressive. And I think it's ostensibly like a distillation of one of these large models into a smaller model when you get down to it that's like, principally what's happening. And maybe the interesting result is the extent to which you can recover interesting behavior in a small model, but it's still leaves behind a larger model, and its utility is much more narrow than that large model. It might be good at the few things that it was trained to do, and it might evaluate well on to a specific subset of tasks, but you lose a lot of what makes those big models. Magic, you lose a lot of that generality. But yeah, I think if you pick 1530 tasks, you can train an extremely small model to perform as well as a big model, as soon as you narrow in on like a small set of abilities can get quite good performance there. I think that's an exciting truth, right? Because you can go from using these big general models, to as soon as you know, your use case, and as soon as you know, the thing you want to do, you can scale down massively and get a much cheaper version of that system. So I think that's like a, an interesting result. But I don't think it's fair to say that Stanford result is like the same as the large model, like those two are not the same, this one that can run on your cell phone, it's impressive within a limited domain, but it's lost something. It's lost some generality, some intelligence relative to the large one it was distilled from.

Lukas Biewald 36:05

So it sounds like your experience of working on these large language models has pulled up by decades, your belief about when they get like interesting. It has for me to, to be honest. And it I guess, it makes me feel like AGI which isn't a clearly defined, there's aspects of it that seem incredibly important for the world that makes me think that that really could happen in our lifetime, when you sort of like plot forward the curtain I have to ask for you. Is that like top of mind for you and your work? I

Aidan Gomez 36:43

don't think so. Like I don't spend an outsized amount of my time thinking about HBO HCI, I do spend an outsized amount of my time thinking about how to make models more useful. And I think that's along the critical path towards AGI, we're going to build a lot of useful stuff that's going to make people way more efficient, way more productive, that like lofty goal of AGI I think it's exciting. And it's like super salient, like it's very easy to get sucked into it. And it certainly makes your work feel like monumental in terms of importance, but I don't think you need AGI for this technology to be extremely impactful. And I think there's gonna be a lot of other issues along the way, deploying these models that don't touch on the issues that maybe AGI makes AGI discourse puts front and center. So in because I'm on the side of AGI discourse matters. And we should be investing time and thought into it. But it's completely consumed the conversation around AI in general, to a point where it's distracting. And a lot of the issues that the AGI community, tau, which is like the largest issues and of pressing importance and worthy of regulation and slowing down and et cetera, et cetera, et cetera. A lot of those issues, I think, are frankly, over overstated.

Lukas Biewald 38:18

Well, what do you think then are the most important pressing issues?

Aidan Gomez 38:23

Yes, I think stuff like how these models can change public discourse, is really concerning what the consequences of synthetic media at a scale that we've just never encountered, what that'll have, what pressures that will put on society. I think those issues are much more near term and plausibly implementable with the technology of today or maybe the next couple of years. And so that's really where public attention should be. And I'd see very light discussion about that. There's a lot of what happens if the paperclip Maximizer turns us all into iron to generate more paper clips. And obviously, that's an exaggeration, unfair characterization. But a lot of the discourse has that flavor. And it's very far future and disconnected from the present reality of the technology and the near term reality of the technology. And so I would be really excited to see social media like us as a public putting pressure on social media to implement verification of who's posting, how do I know this is a bot or not, right? I really want that filter I want to be able to filter for I'm hearing from humans. I'm reading the opinions of humans, not a language model. But that doesn't seem to be happening. That conversation seems to be quite niche or restricted to very small communities. I think the broader public needs to start demanding that as a feature, because I think there will be a flood of content synthetic content. Yeah.

Lukas Biewald 39:53

It's funny that I would have expected a flood of synthetic content already at this point. The quality seems very high to me of synthetic content. And there's lots of ways to do it. And it's pretty cheap. I'm kind of surprised that there's not way more synthetic content at this point, it makes me wonder if that's really going to happen.

Aidan Gomez 40:14

Yeah, I think it's an awareness thing, I think it might already be happening. And it's such compelling text that it's hard to pick up, like, it might be difficult for you and I to appreciate when we click on a tweet that's popular, and we read through some of those replies, the extent to which those are machine generated, because you just intuitively believe I'm staring at a bunch of humans giving their thoughts and opinions on this tweet, you just trust that, right? That's just what social media is. And similarly, like your emails, right, like the flood of emails that you're getting, you read emails written by someone that you think is trying to market to you and they're speaking very eloquently and fluently. And your spam catcher didn't flag this because it's very compelling. And it seems targeted specifically to you. And it's been observing all the emails coming into Gmail servers. And now like this one isn't just a template of another one, it's specifically written to you so it must be human, but it's not right. And so I think it's very easy for this to slip past because of exactly the reason you're describing which is like, these models are extremely fluid, they write very coherently. And yet these models aren't people. So if they're pressing some idea in response to some political tweet, we don't want that. We don't want synthetic amplification of some position

Lukas Biewald 41:39

Do you have any other things that you think are going to change in the next year or two, based on something have already happened in the capability of these models? I'll say like, one example, from my perspective, is, I can imagine a lot more chat based interfaces into product. Like I think that actually is like a nice interface when it actually works. And I feel like I'm starting to see these incredibly evocative demos, like using things with just a chat interface. I'm curious, from your perspective, do you think our modes of interacting with computers is likely to significantly change,

Aidan Gomez 42:16

definitely, like, it's important to remember that the end of November when chat GPT came out, that was like, for most people who interacted with that product, that was the first time for most humans that they had a compelling conversation with silicone every other moment in their life, they had only ever experienced that with people. And I think for those of us who are like in the field, building these models, it can be like the frog in the pot where nothing is ever surprising. It's all one small step from the step behind. But for most people, it was like, that was the first time they had a conversation with a computer, the first time a human talk to a piece of silicon, I think it's important to remember like how massive of a leap that is. And also to think about what that unlocks, I think it's going to become much, much more common that the default way you interact with a product, or a piece of technology is going to be through conversation. Instead of having to like go through 10 layers of menus are whatever to find the thing that you want to do, you're just going to have a conversation with that agent, and it has access to the ability to affect the change that you're asking it to do, it's just so much more convenient to talk to a product than it is to learn a complex GUI and onboard in that way. I think this unlock of like dialogue is an interface on to the space of products. It's just totally a transformation in how we interact with the stuff we build the systems we build. So you haven't

Lukas Biewald 43:46

raised the massive funding rounds, we've raised a fair amount of money but not at the scale of like open AI or anthropic does what they're doing making nervous, like, Are you kind of consciously trying to not enter like, an arms race of building the most compute intensive model ever? Or like plan to enter that realm? Or like, what are your sort of like, thoughts and plans there?

Aidan Gomez 44:11

Yeah, so we have raised a lot of money, not on the level of 10 billion. And we also haven't gotten to individuals or patrons to raise money. I haven't made friends with a bunch of billionaires and gotten them to write checks into CO here. I think our prerogative has always been to build the company, like the right way and to raise money at healthy milestones when we've proved value creation when we can convince an institutional investor that we hit these milestones. We need this much money to hit this next milestone. And so we don't do those flashy big rounds from one strategic or one patron or one benefactor, I think principally because we're building a company in a different way. And I think there's more independence afforded to you by doing that. If you're completely beholden to one entity or a small pool of entities can lead to problems. Yeah, it unlocks massive capital. But I think cohere is a proof point that you don't need $10 billion to build an extremely compelling, very smart model. I think we're a proof point that you don't need that if you're scrappy and capital efficient, and you have like, super motivated, talented team. But we also don't want to take those shortcuts. We don't want to like sell out and basically give half of our company to one of the tech behemoths and become a subsidiary, we want to stay independent. And we want to build a company, a new company, like Belfie, kind of, I guess, the normal way. It's weird that we're an outlier. Because we raise capital, like a normal, good healthy business, but I guess we are.

Lukas Biewald 45:48

But I guess like in a world where there are people doing that, like, I haven't think like weights and biases, we might run leaner and slower, but react to a world where the space is growing fast. And certainly we have also well funded competitors, we want to make sure that we're you know, I guess like it feels to me, like the space that weights and biases and it's probably winner take all or winner take most. Do you not believe that's the case with the space that you're in? Like? Do you sort of imagine a world where there's lots of different foundation models that do different things? Like why would the world go in that direction?

Aidan Gomez 46:25

I sure hope that it's not a monopoly? Yeah, I definitely don't believe that. It can be like our competition. I think they're great. They're super talented teams, they build great models, or they have their own flavor of doing it, they have their own way of doing it, they have their own concerns that they're optimizing for. I think our flavor is different, right? And that's healthy. And there should be a bunch of folks with a bunch of different takes building these models, putting them out there. And then the market should decide which one they want to adopt, who do they feel is the best partner? Who do they trust the most? Who do they think's going to help them succeed? And I think for cohere, we want to win that on our merits. And I think that the end state of this effort for these foundation model companies like ourselves, it's very unlikely that it's winner takes all. We're all like within a few months of each other. And so it feels very unlikely that it's winner takes all and winner takes all, it's just bad for the market. It's just it's a bad setup for the people who need to consume these models. And so I'm yeah, I'm super optimistic that we'll have diversity. And we'll have a handful of folks building and deploying these models. Do you think that there are specific cases where the answer is yes, but I think by and large, fine tuning is like a mature system feature. It's like, you want to fine tune the model after you've exhausted all the other things that you can do to boost its performance. And so it's really only once the system has been deployed, optimized, and then eventually you land at the fact Okay, the only way for me to squeeze more performance out of this is via fine tuning. We're probably still too early in the tech adoption curve, to actually see strong demand for that. I think eventually it does arise. In the interim, the focus for coherer is just make the models so adaptable via prompting, or by grounding or via these other methods, make them as adaptable as possible without having to customize weights to just give other levers for people to pull on to squeeze better performance out of the model.

Lukas Biewald 48:29

Okay, we're almost at a time. But before I let you go, can you tell me one thing that's been surprisingly hard, and so many things seem hard, but maybe something that people wouldn't necessarily know is hard about building these large models and building an API around them that customers actually use for mission critical stuff?

Aidan Gomez 48:49

What's something surprising and hard? Because I feel like a lot of people know how hard it is to like train, the model itself is obviously 1000s of accelerators. Trying to keep that thing up is like, really difficult.

Lukas Biewald 49:00

sounds stressful to you're spending so much money?

Aidan Gomez 49:03

Yeah, I like in the GPT. For post, there was like the model babysitters, that's a real thing that's like, we have people who just sit and watch models trained so that we can bring them back up when they inevitably fail. The importance in the sensitivity to data, I think was a real shock for me this year, as we really started scaling up our data collection efforts from humans as opposed to the web, like the web. When we were collecting data there, the model is super robust to noise, you get away with just some like weak heuristics or really just wanna, like throw as much as you can in there. As soon as we went into the human data collection phase. Like one example, or two examples. Like you only need to, like mess up a couple times. And suddenly you've sent the model down to direction that you really don't want it to go. It's extremely sensitive. If you teach it something that's wrong, it will lock that in And just before I ever believe that wrong thing.

Lukas Biewald 50:02

that is surprising. That's very surprising. Yeah.

Aidan Gomez 50:05

So like the sensitivity there. Just, I was not prepared for how delicate these models are.

Lukas Biewald 50:12

Okay, actually, final question. Is this some other topic that you're interested in that if you had some extra time, you would look into some topic around machine learning that you wish you had more time to explore? around machine

Aidan Gomez 50:25

learning? Yeah, I think I would probably be in robotics, and embodiment. I just think that's so cool. And it's like, there's such a strong consumer demand for that. Like, we all know what the imaginary success of extremely intelligent brain plus extremely capable body, we know what that would be like, and how transformational that would be to have in our lives to have access to and it feels like we're really far off. So I would love to effect change there and help build that. Yeah, robotics is super sick.

Lukas Biewald 51:01

Totally agree. Love it. Thank you. Thanks. That was really fun.

Aidan Gomez 51:05

Thank you so much. Yeah, that was great.

Lukas Biewald 51:07

If you're enjoying these interviews, and you want to learn more, please click on the link to the show notes in the description where you can find links to all the papers that are mentioned supplemental material and a transcription that we worked really hard to produce. So check it out.