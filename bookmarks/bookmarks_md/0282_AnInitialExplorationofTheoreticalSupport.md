---
url: https://yaofu.notion.site/An-Initial-Exploration-of-Theoretical-Support-for-Language-Model-Data-Engineering-Part-1-Pretraini-dc480d9bf7ff4659afd8c9fb738086eb
title: "An Initial Exploration of Theoretical Support for Language Model Data Engineering. Part 1: Pretraini"
description: "A tool that connects everyday work into one space. It gives you and your teams AI tools—search, writing, note-taking—inside an all-in-one, flexible workspace."
author: "Yao Fu"
captured_at: "2026-03-08T11:12:07.631Z"
---

# An Initial Exploration of Theoretical Support for Language Model Data Engineering. Part 1: Pretraini

University of Edinburgh | yao.fu@ed.ac.uk

Started writing in Aug 20 2023

Released in Sep 05 2023

Recently, the focus of research and open-source community are gradually shifting from model engineering to data engineering, realizing the crucial importance of data quality. However, when we say “we want better data”, what does “better data” mean precisely? When we say “we optimize the data composition”, what is the objective that we are optimizing?

We would like to study the theoretical support for the language modeling data engineering. We believe that in-depth understanding of the problem is equally important as developing methods to solve the problem, and theoretical analysis will lead us to predictable scaling: to predict the eventual performance on every single task before we actually run the experiments.

In this post, we aggregate recent insights about data engineering, and give problem formulations for data optimization — this is to say, we do NOT propose specific methods for optimizing data, but we discuss what is the problem we should solve when optimizing data, and the underlying principles that guide us. Specifically, we discuss the following objectives for pretraining and SFT data optimization:

For pretraining data optimization:

![💡 标注图标](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

Find the optimal mix ratio + data format + data curriculum such that the speed of learning is maximized.

For supervised finetuning / instruction tuning data optimization:

![💡 标注图标](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

Find the minimal combination of query-response pairs such that their coverage of the user preference distribution is maximized

Combining the insights from pretraining and finetuning, we would further find ways to connect the two to achieve predictable scaling, that is, given the pretrain and finetune data, given the model architecture and training hyperparameters, we would like to predict all the results before doing the experiments. Specifically,

For predictable scaling:

![💡 标注图标](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

Find the scaling law where given the input as: pretrain data mixture + model scale + finetune data mixture \+ training algorithm such that the pretrain dev loss, downstream performance, human preference can be predicted before all experiments

Table of Content

We first clarify that although the final next-word prediction loss is typically used for measure pretraining, this is not the objective when we optimize the pretrain data mixture. We are not directly optimizing the final loss, but we are optimizing the speed of loss decrease — we would like the the derivative of the learning curve to be larger, thus a steeper curve. To measure the speed of learning, instead of using the next-word prediction loss (which is quite informative given its connection to lossless compression), we consider the speed of grokking — how fast the model can obtain a specific skill — might be a good alternative metrics. We will circle back to the connection of grokking and next word prediction loss later.

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F952b2f36-b39c-4d87-9da5-a0ec5d719722%2FUntitled.png?table=block&id=ed7f5efa-1363-4428-9793-f16b3f6d9e96&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Grokking means at a certain step of training, the model suddenly learns a skill and transits from memorization to generalization

For a specific “skill”, for example, modular addition, we quote a typical learning curve from Pearce et. al. 2023. As we can see, at the beginning of training, the model memorizes the training data and the test performance does not change. As the training goes on, there is a phase-change period from step 35k to 45k where the model suddenly transits from memorization to generalization, showing 100% accuracy on the test set. Such phase change during learning is called “grokking”.

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F490fa5d1-17b9-439a-8a88-661463cf09d2%2FUntitled.png?table=block&id=ba046444-0d04-441e-b814-f6c1ff12c251&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Under different hyper-parameters, the model have different speed of grokking.

Speed means, say I have two hyperparameter settings, for setting 1 the model achieve 90+ test accuracy after 1000 optimization steps, for setting 2 the model that requires 2000 steps, then we say hyperparameter setting 1 gives model a faster speed of grokking than setting 2.

As we can see in the above figure we quote from the original grokking paper (Power et. al. 2022), multiple factors influence the speed of grokking: weight decay makes the grokking time earlier (thus faster speed), while too small / large learning rate makes the grokking time later (thus slower speed) — again, here the objective is not optimizing the final performance, the objective is to optimize the speed, the derivative of the performance curve.

Ideally, we want a steep learning curve where the speed of grokking is maximized.

We note there exists a notion of granularity of skills. For example:

Single skill: like two digits addition

Aggregated skills: one digit addition + two digits addition + two digits subtraction + …

Downstream performance: GSM8k math work problem performance

Usually, a task requires the combination of multiple skills. Say a downstream task is GSM8k-styled math reasoning, then the skills required might be two digits addition, two digits subtraction, understanding the order between numbers like 1 is smaller than 2, understanding the 1 week means 7 days .etc. — each of these skill may have different grokking point during training (this also explains why one needs to train the model long enough), and only by combining all of them the model can do GSM8k reasoning.

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F1c66c3b8-a70a-41b6-bc50-5728de890252%2FUntitled.png?table=block&id=76ba7fc5-5ace-4572-bcc0-0e8d80e61f84&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Left: list of linguistic skills; right: locations when these skills emerge during training. Speeding up grokking means we want to move these dots leftwards — to make these skills emerge at a earlier training stage.

Sorry these fonts are small. This amazing figure is quoted from Evanson et. al. 2023. The left part of the figure are list of specific linguistic skills that the model obtain, the right part of the figure shows when these skills are acquired during the training process. Clearly different skills have different speed of learning and emerges at different time. Speeding up grokking, in this context, means that we want to move the dots leftwards — which means that we can observe them earlier during training (such that we can leave “room” for more advanced skills during later training stage).

One important corollary is that intermediate model checkpoints are very important for studying the learning dynamics. We call for existing models (@LLaMA team plz) open-source the intermediate checkpoints!!

1

As we can see from above section, instead of using next-word prediction loss as the measurement, grokking seems to be closer to generalization and can be better linked to specific set of skills, thus being a good alternative metrics for learning. In this section, we discuss the observed data factors that influence the speed of learning, focusing on data format, mixture, and curriculum.

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F512e21e7-4506-4240-b951-bdf1d9866e48%2FUntitled.png?table=block&id=8c09b54f-099c-4dde-9b94-657f2e30a1c3&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Different format of the data gives different speed of learning. Also note that they are the same data — same equation same answer, only the formats are different.

In our previous work, we have shown that training on chain of thought formatted data gives the model CoT reasoning capability. In the above figure, we can further see that there are different formats of CoT / scratchpad data, and the more detailed the scratchpad is, the faster the model learn.

1

Pay attention to the nuances as the devil is in the detail:

The model can learn from all formats of CoT — the final results are similar and it is not the case that the model cannot learn — it is the speed that is being different, and the model learns faster for some formats.

The content / meaning / semantics of the data is the same — they are the same three digits addition questions. It is the format of the CoT is different — one is more detailed than another.

To understand the data curriculum, note the following points:

There are many skills that we would like to teach the model, say skill 1 to 3.

For different skills, there exist different sources of training data that could help with that skill (e.g., webpages for MMLU-styled problems, GitHub for coding problems).

Say we want to teach the model both text and code capability, we have 10B text and 10B code, our compute only allows us to train 10B data. We want to maximize the coding capability. Here are three possible solutions:

Method 1 (code-only): directly feed 10B code data

Method 2 (uniform mixing): mix the 5B text and 5B code data uniformly, then feed them simultaneously to the model

Method 3 (data curriculum): feed 5B text first, then 5B code

Which one could perform the best?

If the skills that the model could learn from text data is not helpful to the code data, then we may directly do method 1, code only, as is the case of StarCoder and AlphaCode.

2

If the skills that the model could learn from text data can transfer to the code data, then we may want to do method 2, uniform mixing

1

If learning code skills requires the model to have text skills first, that is to say, there are dependencies between text and code and text must come first, then we need to do method 3, the data curriculum. This is the case of Codex and CodeLLaMA (although they may not intentionally choose to do this).

2

But which of the setting could likely to be the “correct recipe” for pretraining? We note the following observation from Chen et. al. 2023.

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6d5022a7-5341-419c-a45c-7593385d85b0%2FUntitled.png?table=block&id=7d109036-8553-4a1f-b815-4217e1944612&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Different source of data induces different skills. Training on a particular ordering of data can give faster learning speed than training on skill-specific data.

Here the authors show that, in synthetic and simplified settings, a learned data curriculum scheduling data of skill 1, 2, 3 can achieve faster learning speed of learning on data of skill 3.

Mix ratio refers to how we weight data from different sources. for example, LLaMA uses the following weight:

![](https://yaofu.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F281b3c78-d734-43fb-aa33-707babff9463%2F8e013503-cf9b-4c43-901a-46d04e57b0ca%2FUntitled.png?table=block&id=dccf637e-29ac-4b16-9781-b69f68a776af&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1060&userId=&cache=v2)

LLaMA data mix ratio. This ratio down weights code data like Github and StackExchange, also it down weights paper data like Arxiv.

Apparently LLaMA downweights:

Code data like Github, consequently LLaMA’s coding performance is not very high. In comparison, starcoder, which trains mostly on code, performs good on coding tasks.

Paper data like Arxiv, consequently LLaMA’s scientific reasoning seems not very high. In comparison, Galactica, which trains mostly on papers, performs good on scientific reasoning.

Different mix ratio may result in different speed of learning, as is shown by the DoReMi paper:

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa5d69829-8514-4c05-9c11-33115d2117c8%2FUntitled.png?table=block&id=ddb66081-a99f-455b-a7e1-100b37468d5b&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Different mix ratio of data improves speed of learning.

As Xie et. al. 2023 shows, a better mix ratio of Pile improves models’ performance with a higher learning curve, making the model learns faster from the data.

Although data format / curriculum / mix ratio are important for learning speed, one very important caveat is model scaling, as large models learns much faster than small models. It is very common that results of data engineering on model scale less than 30B cannot transfer to model larger than 70B. One example here is our verification on whether code data truly improves reasoning, we observe that:

5

Coding data seems to improve:

Symbolic reasoning, like BABI and BBH-Algorithmic

Translation between symbolic data and language data, such as structure-to-text or text-to-sql

But, the above observation only happens for 7B model — when the model is 70B, we cannot observe improvements on BBH-Algorithmic

Further, coding data cannot improve:

Natural language reasoning, like BBH-Language

Math reasoning, like GSM8K

Pay attention to the point that code data only improve 7B model’s BBH-Algo but not 70B. Similar observation have been made by various places who build language models. In fact, I am a bit of worried that some sub-directions of data engineering might be flushed by paper publications which makes a large voice but cannot generalize to larger model scale ![🙃](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==).

Consequently, all of the improvements from data format / curriculum / mix ratio may be easily overwhelmed by model and data scaling — they work only for small models and simple tasks, when the model / data become large, then may become useless. If this is the case, we should put more efforts on solid data cleaning rather than useless fancy curriculum. We are not sure if this is the case, but we hope not.

In this section, we discuss different granularity of skills and their learning curves, we also consider how to measure the speed of learning beyond single-skill metrics and dev loss.

Let’s say during training, the model learns multi-granularity skills from small to large, then we may consider skills from the following perspectives:

Micro level: single tiny skill, quickly gained from relevant pieces of text, may not be interpretable.

Meso level: interpretable skills that are aggregated from micro skills and become interpretably to human, like 3-digits addition.

Macro level: continue aggregating meso-level skills that eventually shows statistical behaviors, specifically we may observe

Power laws (log-linear scaling curve): as the model gradually accumulate micro and meso level skills, the overall macro level skills improves smoothly

Emergent abilities (phase-change scaling curve): some of the macro skills require the meso-level skill pass a certain threshold. For example, the multi-step reasoning capability requires the model have a certain level of single-step accuracy, like for a 5-step reasoning, if the single-step accuracy is 95% then the accumulated accuracy is 77%, yet a 80% single-step accuracy only has 32% accumulated accuracy, because the error blows exponentially.

The above perspectives are very similar to statistical physics: in the micro level (say a gas molecule) things are hard to precisely model and predict, but if we gather many micro pieces to the macro level (a tank of ideal gas), we can describe their macro properties statistically.

![](https://yaofu.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F602f0c91-8ec5-46ea-af46-a915620ceb92%2FUntitled.png?table=block&id=b6d883df-b9cd-4a14-9bc6-de7c951c98b7&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Aggregating curves of different skills lead to an overall loss curve.

When I initially read the “quantization model” I feel like this is yet another bullshit. Usually in AI, anything named under “quantum” is either extremely insightful or completely bullshit. At the second glance, I feed like this paper might be extremely insightful.

As is shown in the above curve, we see:

Single-skill (”quantum”) curves typically exhibit phase-change shapes.

The model learn different skills with different speed.

When aggregating multiple skills together, we obtain a smooth log-linear shaped loss curve.

We consider:

Loss is good, it is predicatable, well-aligned with overall performance, and can be interpreted as compression ratio. The only problem is that loss cannot directly be translated into downstream task performance (which we aim to bridge this in our next blog post using scaling laws for transfer).

3

Single-skill accuracy (either meso or macro level) is good, but it only measures single skill.

Can we find some metrics that measures something in between? Something that

Aligns well with a direction of capability (say reasoning)

Can be derived from first principles (like information theory)

Measures how close we are to the “true generative process”, like some sort of mutual information

I am not sure if such a better metric exists, but would very much love to explore.

In this section, we explain that the reason the model can learn (do “grokking” and exhibit emergent abilities) is because the model learns the true generative process. We explain this under the lossless compression perspective.

Recently, there are discussions that interpret the pretraining process as lossless compression of the training data. I find this perspective extremely inspiring. Specifically:

1

Training the language model is equivalent to compressing the training data in a lossless way.

Note that the compression is lossless — some argue that the model memorizes the training data and that the model weights is a lossy compression of the data. The compression perspective tends to believe that \[model weights is a lossy compression\] is wrong.

The integral of the loss curve — the area between the loss curve and the x-axis (indexed by data) can be interpreted as the compression ratio under arithmetic coding and [can be derived analytically](https://www.zhihu.com/question/618248946/answer/3174763820).

The better the model compress the data, the lower loss, the more likely the model learns the underlying generative process of the data — the algorithm/ rule about how the data is generated.

Kolmogorov complexity is the minimum description length of the generator that generates the data. The language model approximates the Kolmogorov compressor, the shortest (randomized) algorithm that generates the data (human language).

What the model weights encode is not the data, but the underlying generative process (it is a stochastic process) of human language (the process within your brain about how language is generated).

The model weights is a side product of lossless compression. It encodes the generative process of human language. We call such generative process “intelligence”. Under this perspective, intelligence is the generative process that lying in human brain that generates human language.

To see why lossless compression uncovers the true generative process, we give a lossless compression of the random number example:

Say you store your random number generation algorithm with your initial random seed in a file. This file is not so large. For example, the Python random number generation algorithm takes 31.4 kb of disk memory.

Say you use this algorithm to generate 100B pseudo random numbers.

You send this 100B random numbers to a friend and ask the friend to compress it.

Without know the underlying generative process (the algorithm), if your friend use some common compression software like gzip, they may end up in 50B or similar scaled files, the compression ratio is low.

Yet if your friend somehow figures out the random number generation algorithm and the initial seed, simply storing the algorithm and the seed only takes 31.4kb disk memory, that is extremely high compression ratio.

Large neural networks and their learning algorithms, are similar to the above process — to recover the underlying generative process (data generation algorithm) using large amount of observations. The higher compression ratio / training loss one get, the more likely that they recover the underlying generative process.

This sounds like magical, but training LLMs feels indeed like recovering the random number generation algorithm from a large amount of generated random numbers.

Kolmogorov complexity refers to the minimum length of the algorithm that generates the data. Under the lossless compression perspective, the language model is viewed as an approximation of the (uncomputable) Kolmogorov compressor.

This is to say, the weights of the language model probably encodes a generative process, an algorithm that generates its training data. Note that the weights of the model does not encode the data, but the program that generates the data, and optimizing the weights pushing it towards the shortest program that generates the data, which is precisely the definition of the Kolmogorov compressor. Actually, there are already works showing how RNNs and transformers encode CFGs (generative process that generates context-free languages).

2

In this post, we review multiple empirical observations of language model learning dynamics (grokking, log-linear scaling law, emergent abilities), the data factors that effects the learning speed (data format, mix ratio, and curriculum).

We discuss possible explanation of the empirical phenomena, and connect these observations with the recent lossless compression theory.

Our eventual objective is to build a theory and guides us to do data (and other important factors of learning) such that we can predict the final performance of every task (not just pretrain loss) before the experiments, without writing one single line of code.

There is already scaling laws that predicts the dev loss, the theories we discussed above further considers grokking and emergent abilities.

We further explain that the reason the model can learn is because the model learns to approximate the true generative process / Kolmogorov compressor under the lossless compression perspective.

In the next post, we will study how the learned skills / generative process can transfer to downstream tasks by instructions tuning under the perspective of scaling law for transfer, and further discuss the possibilities of predicting all downstream task performance from the pretraining loss and finetuning data mixture.

1

OpenAI reported that during the development of GPT-4, they predicted the performance on HumanEval before the experiments. We believe such prediction can be unified by an unknown theorem that is able to predict all the downstream performance beforehand.

By exploring and building such a theorem, we may turn deep learning and language modeling from alchemy to empirical science.

Hestness et. al. Dec 2017. Deep Learning Scaling is Predictable, Empirically

Baidu’s pioneer study on scaling law of neural networks

Kaplan et. al. Jan 2020. Scaling Laws for Neural Language Models

Initial OpenAI LM scaling law

Henighan et. al. Nov 2020. Scaling Laws for Autoregressive Generative Modeling

Extension of the initial OpenAI LM scaling law to multimodal

Hernandez et. al. Feb 2021. Scaling Laws for Transfer

OpenAI scaling law for SFT

Bahri et. a. Feb 2021. Explaining Neural Scaling Laws

Clark et. al. Feb 2022. Unified Scaling Laws for Routed Language Models

DeepMind scaling law for MoE

Hoffmann et. al. Mar 2022. Training Compute-Optimal Large Language Models

DeepMind Chinchilla scaling law

Gao et. al. Oct 2022. Scaling Laws for Reward Model Overoptimization

OpenAI scaling law for RL

Aghajanyan et. al. Jan 2023. Scaling Laws for Generative Mixed-Modal Language Models

Meta FAIR Chinchilla scaling law for multimodal