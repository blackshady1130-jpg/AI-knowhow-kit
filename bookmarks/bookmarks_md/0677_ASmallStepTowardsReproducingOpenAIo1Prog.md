---
url: https://medium.com/@peakji/a-small-step-towards-reproducing-openai-o1-b9a756a00855#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjkxNGZiOWIwODcxODBiYzAzMDMyODQ1MDBjNWY1NDBjNmQ0ZjVlMmYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTUwNzQzNzA3NzYyNjIxMjA1MTYiLCJlbWFpbCI6ImJsYWNrc2hhZHkxMTMwQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYmYiOjE3NDE5MjQ2NTgsIm5hbWUiOiJCb2IgV2FuZyIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NKeTFNSkdQbWVzck8yWm1fUndzNmNiX0Vub0VxT2tEUDdYenl5NWMwMTd6Q1hoSkZnPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IkJvYiIsImZhbWlseV9uYW1lIjoiV2FuZyIsImlhdCI6MTc0MTkyNDk1OCwiZXhwIjoxNzQxOTI4NTU4LCJqdGkiOiIyMGMyNjU3NGNiMTMzYmM5MGMxZjBkYjhhZDU1MzE0NGRhNDQxMjdjIn0.0zGduEtwpo-wChvqJSjRu4vo2cPTtF3SmpujvCzOePkXQ98pZecSgZcG84UrrueC2Lup_s3-KPbbFnikWkMz_ELDQRBW4XWAlvrROpBOD2pfAAmkaZIktTLRohrUedWIwrRvBsqZSaKEiR-pc5-0W7pIFRwzN40Z0iIj8stNzn-QtuPbMXmV3aK2DnlupRubPl80-NDKLT1uszCgnPRfWMO6ww0TG2YFgAd7URaUPP5v54TQQ6zBDntbd73FuOI2kRdODGcObK6Po1bI2ol82qvXdBgNQZu6-jVIbx6zvUrJssiCPpY8illXLFRdEf58LymJnxK_OO50ZVI2BKO_xA
title: "A Small Step Towards Reproducing OpenAI o1"
description: "Steiner is a series of reasoning models trained on synthetic data using reinforcement learning. These models can explore multiple reasoning paths in an autoregressive manner during inference and autonomously verify or backtrack when necessary, enabling a linear traversal of the implicit search tree."
author: "Yichao 'Peak' Ji"
published: "2024-10-22T09:06:17.159Z"
captured_at: "2026-03-08T12:53:26.791Z"
---

# A Small Step Towards Reproducing OpenAI o1

12 min read

Oct 21, 2024

\--

Since the release of OpenAI o1, I have been working on reproducing o1 as a personal side-project during my spare time. Throughout this process, I’ve gained a lot of interesting knowledge and insights (and failures). Given the limitations of my abilities, time, and financial resources, it’s unlikely that I’ll be the one to take this effort all the way to the finish line. Therefore, I feel it’s important to share these experiences — worth the equivalent of dozens of H100 GPUs — while they’re still fresh.

## TL;DR

Steiner is a reasoning model capable of exploring multiple reasoning paths in an autoregressive manner during inference, autonomously verifying or backtracking as needed. The training process consists of three steps: first, by randomly truncating synthesized reasoning path data and utilizing guided re-completion, each example is transformed into a Directed Acyclic Graph (DAG) from question to answer. Then, 50K reasoning path examples with backtracking nodes are sampled from 10K DAGs. Finally, reinforcement learning is applied using heuristic rewards based on the in-degree and out-degree of each node in the original DAG and their distances, allowing the model to balance exploration depth and breadth. The model achieved a +5.56 improvement on the GPQA-Diamond dataset but failed to reproduce inference-time scaling.

**🤗 Model Download:** [https://huggingface.co/collections/peakji/steiner-preview-6712c6987110ce932a44e9a6](https://huggingface.co/collections/peakji/steiner-preview-6712c6987110ce932a44e9a6)

## Introduction

Steiner is a series of reasoning models trained on synthetic data using reinforcement learning. These models can explore multiple reasoning paths in an autoregressive manner during inference and autonomously verify or backtrack when necessary, enabling a linear traversal of the implicit search tree.

Press enter or click to view image in full size

Steiner can explore multiple reasoning paths in an autoregressive manner during inference and autonomously verify or backtrack when necessary, enabling a linear traversal of the implicit search tree.

Steiner is a personal interest project by Yichao ‘Peak’ Ji, inspired by OpenAI o1. The ultimate goal is to reproduce o1 and validate the inference-time scaling curves. The [Steiner-preview model](https://huggingface.co/collections/peakji/steiner-preview-6712c6987110ce932a44e9a6) is currently a work-in-progress. The reason for open-sourcing it is that I’ve found automated evaluation methods, primarily based on multiple-choice questions, struggle to fully reflect the progress of reasoning models. In fact, the assumption that “the correct answer is always among the options” doesn’t align well with real-world reasoning scenarios, as it encourages models to perform substitution-based validation rather than open-ended exploration. For this reason, I’ve chosen to open-source these intermediate results and, when time permits, to build in public. This approach allows me to share knowledge while also gathering more evaluations and feedback from real human users.

**⚠️ Disclaimer:** While Steiner has been able to achieve high-quality zero-shot results without relying on Chain of Thought (CoT) prompting or an agent framework, it has not yet replicated the inference-time scaling capabilities demonstrated by o1. In experiments using a [specialized logits processor](https://gist.github.com/peakji/f81c032b6c24b358054ed763c426a46f) to intervene on reasoning tokens, increasing the number of reasoning steps did not improve performance; in fact, it led to a decline in benchmarks such as MMLU-Pro and GPQA. As a result, Steiner cannot currently be considered a successful reproduction of OpenAI o1. There may be deficiencies in both the training methods and data quality, so please interpret the results with caution.

## Background

Compared to traditional LLMs, the most notable change in OpenAI o1 is the introduction of reasoning tokens during inference, which enables inference-time scaling. This allows the model’s performance to improve by increasing the compute budget during inference. When discussing inference-time scaling, the most intuitive approach might be to introduce tree search or an agentic framework. However, after reviewing the (limited) official information on o1, I noticed that most of the reported benchmarks are based on pass@1 and majority voting. Additionally, the OpenAI team has mentioned that o1 is a single model, not a system, which piqued my curiosity about how they implemented this remarkable piece of work.

Although the specific content of the reasoning tokens has not yet been made available to developers through the OpenAI API, the token usage statistics do include the number of reasoning tokens (since it is used for billing developers). With this in mind, I designed a simple experiment to use o1’s API to analyze the relationship between the number of completion (including reasoning) tokens and the total request time. We know that if tree search is used, the inference would be as parallel as possible to reuse cache and maximize GPU utilization, which would result in a sub-linear curve. However, the experiment yielded a series of clean, linear results, with o1-mini showing even less fluctuation than GPT-4o-mini:

Press enter or click to view image in full size

OpenAI o1 may still be a model that performs linear autoregressive decoding, but this doesn’t mean that it doesn’t perform any “search” during the reasoning phase.

The above experiment led me to a hypothesis: OpenAI o1 may still be a model that performs linear autoregressive decoding, but this doesn’t mean that it doesn’t perform any “search” during the reasoning phase. Imagine a search tree — when traversing it, the path produced is actually linear. If we could train an autoregressive language model that not only generates reasoning paths but can also validate, backtrack, or switch its approach when necessary, then in the ideal case, it would essentially be performing a linear traversal on an implicit search tree within the same context. While this linear traversal might seem inefficient, it has three key advantages over parallel search:

1.  All prior attempts, whether correct or incorrect, are stored in the context memory, meaning every decision is made with complete historical information.
2.  Implicit backtracking does not require the target node to already exist within the search tree, allowing for more open-ended exploration.
3.  From an engineering standpoint, it allows for the reuse of all existing, highly optimized inference infrastructure.

Press enter or click to view image in full size

Imagine a search tree — when traversing it, the path produced is actually linear.

## Method

Training a model with linear search capabilities is not an easy task; both data synthesis and model training present numerous challenges.

Firstly, currently available reasoning datasets consist mainly of synthetic Chain of Thought (CoT) or reasoning steps, typically generated by inputting “question-answer” tuples into a powerful LLM and asking the model to break down its thought process. This approach means that these datasets do not contain reasonable backtracking steps. As a result, models trained on this type of data essentially learn shortcuts, or in other words, internalize the CoT.

To address this issue, I designed two methods for data synthesis and augmentation:

1.  Randomly truncate the reasoning path and hide the correct answers, allowing a powerful LLM to attempt forward reasoning based on the truncated prefix for a certain number of steps, and then provide the correct answer to obtain backtracking examples.
2.  After clustering the steps generated from the previous step, assign unique IDs to each step and construct a directed acyclic graph (DAG) of all steps for the same question. Random sampling is then performed on the DAG to obtain a polynomial number of reasoning path examples.

Through the aforementioned methods (along with considerable manual effort and clever tricks), I ultimately obtained 10,000 directed acyclic graphs (DAGs) and sampled 50,000 reasoning path examples with backtracking based on these graphs. Each sample contains an average of approximately 1,600 reasoning tokens, which is remarkably close to the statistics collected during previous tests of o1/o1-mini! Considering the training costs, I retained only those samples with reasoning token counts below 4,096 and a total of prompt + reasoning + completion tokens below 8,192.

As an example, for the question “*7.7 or 7.13 — which is bigger?*”, the output format of Steiner is as follows (where the blank lines and indentation are manually added for readability):

<|reasoning\_start|>

<|reasoning\_step\_start|>
 <|reasoning\_step\_name\_start|>Initial Comparison of Decimal Numbers<|reasoning\_step\_name\_end|>
 <|reasoning\_step\_thought\_start|>I need to compare the numbers 7.7 and 7.13 to determine which is larger. A useful way to compare decimal numbers is to ensure both numbers have the same number of decimal places. This allows for a direct comparison of the digits in each place value.<|reasoning\_step\_thought\_end|>
 <|reasoning\_step\_summary\_start|>To compare 7.7 and 7.13, I will convert them to have the same number of decimal places, making it easier to compare directly.<|reasoning\_step\_summary\_end|>
 <|reasoning\_step\_reflection\_start|>Converting both numbers to have the same number of decimal places will allow me to compare them accurately. This step is crucial because it allows me to see which number has a larger value at each place value.<|reasoning\_step\_reflection\_end|>
<|reasoning\_step\_end|>

<|reasoning\_proceed|>

<|reasoning\_step\_start|>
 <|reasoning\_step\_name\_start|>Align Decimal Places<|reasoning\_step\_name\_end|>
 <|reasoning\_step\_thought\_start|>First, I will rewrite 7.7 with two decimal places. Since 7.7 is equivalent to 7.70, I can now compare 7.70 and 7.13 directly.<|reasoning\_step\_thought\_end|>
 <|reasoning\_step\_summary\_start|>I rewrite 7.7 as 7.70 to have the same number of decimal places as 7.13.<|reasoning\_step\_summary\_end|>
 <|reasoning\_step\_reflection\_start|>With both numbers having two decimal places, I can now compare them directly. I need to look at the digits in the tenths and hundredths places.<|reasoning\_step\_reflection\_end|>
<|reasoning\_step\_end|>

<|reasoning\_proceed|>

...

<|reasoning\_proceed|>

<|reasoning\_step\_start|>
 <|reasoning\_step\_name\_start|>Compare Hundredths Place<|reasoning\_step\_name\_end|>
 <|reasoning\_step\_thought\_start|>Next, I compare the hundredths place. In 7.70, the digit in the hundredths place is 0. In 7.13, the digit in the hundredths place is 3. Since 0 is less than 3, this does not change the fact that 7.70 is greater than 7.13 because the difference was already established in the tenths place.<|reasoning\_step\_thought\_end|>
 <|reasoning\_step\_summary\_start|>In the hundredths place, 0 in 7.70 is less than 3 in 7.13, but this does not affect the overall comparison as the tenths place already determined 7.70 is larger.<|reasoning\_step\_summary\_end|>
 <|reasoning\_step\_reflection\_start|>The comparison confirms that 7.70 is indeed greater than 7.13, both in the tenths and hundredths places. I have verified the comparison thoroughly.<|reasoning\_step\_reflection\_end|>
<|reasoning\_step\_end|>

<|reasoning\_end|>

To determine which number is larger between \*\*7.7\*\* and \*\*7.13\*\*, follow these steps:\\n\\n1. \*\*Align the Decimal Points:\*\*\\n   \\n   - \*\*7.7\*\* can be written as \*\*7.70\*\* (adding a zero in the hundredths place for comparison).\\n   - \*\*7.13\*\* remains \*\*7.13\*\*.\\n\\n2. \*\*Compare the Numbers:\*\*\\n   \\n   - \*\*7.70\*\* vs. \*\*7.13\*\*\\n   \\n   - \*\*Tenths Place:\*\*\\n     - \*\*7.70\*\* has \*\*7\*\* in the tenths place.\\n     - \*\*7.13\*\* has \*\*1\*\* in the tenths place.\\n     - \*\*7 is greater than 1\*\*.\\n   \\n   - \*\*Hundredths Place:\*\*\\n     - \*\*7.70\*\* has \*\*0\*\*.\\n     - \*\*7.13\*\* has \*\*3\*\*.\\n     - However, since the tenths place already shows that \*\*7.70\*\* is greater, the hundredths place doesn't need to be compared further.\\n\\n3. \*\*Conclusion:\*\*\\n   \\n   - \*\*7.7\*\* (or \*\*7.70\*\*) is \*\*greater\*\* than \*\*7.13\*\*.

Next, I divided the training of the Steiner series models into three stages:

1.  **Continual Pre-Training (CPT):** This stage involves training on a mix of ordinary text corpora and reasoning paths, allowing the model to familiarize with long reasoning outputs and to preliminarily train the embeddings of the [14 newly introduced special tokens](https://huggingface.co/peakji/steiner-32b-preview/blob/278989ea17f74b14e2b32d9544eb53a17b4ad087/special_tokens_map.json#L16-L29). It should be noted that tests on some small parameter models suggest that this step might be redundant; directly training with a large amount of reasoning data during the Supervised Fine-Tuning (SFT) stage seems to yield good representations as well. However, the 32B CPT was completed early on, so I continued to use it.
2.  **Supervised Fine-Tuning (SFT):** In this stage, training is conducted using a chat template, with the goal of teaching the model to imitate the format of reasoning: first, assign a name to each step, then output a complete thought, summarize the thought, reflect on the reasoning so far, and finally decide whether to proceed, backtrack, or end the reasoning and formally answer the question. You may wonder why an open-source model needs to generate a summary like o1, especially since it doesn’t need to hide its thoughts. This is because I am preparing for a future Steiner model capable of multi-turn dialogue. Theoretically, after training, it would be possible to replace the complete thoughts from previous conversations with summaries to reduce the pre-fill overhead when the prefix cache cannot be hit. Currently, Steiner has not yet been optimized for multi-turn dialogue, and retaining only summaries may lead to negative few-shot effects.
3.  **Reinforcement Learning with Step-Level Reward (RL):** After the first two stages, the model has learned to generate and complete reasoning paths, but it still does not know which choices are correct and efficient. If we blindly reward shorter reasoning paths, the model may degrade into shortcut learning, which is just internalizing the CoT. To address this, I designed a heuristic reward mechanism: weighting the reward for each step and the entire reasoning path based on the number of incoming edges e\_i, outgoing edges e\_o, distance from the original question d\_s, and the distance to the correct answer d\_e of each node in the DAG. This approach guides the model to learn how to balance the breadth and depth of exploration.

The above approach may seem straightforward, but over the past month, I have been struggling with out-of-memory (OOM) issues and reward hacking every weekend (and on evenings without overtime). Finally, on the 38th day after the release of OpenAI o1, I achieved a phase of results that I don’t consider too embarrassing.

## Evaluation

Press enter or click to view image in full size

Performance of the Steiner models at different training stages on the GPQA-Diamond dataset. All Steiner models do not use CoT prompting.

The figure shows the performance of the Steiner models at different training stages on the GPQA-Diamond dataset. It can be seen that the introduction of the reinforcement learning phase resulted in an improvement of +3.53. When combined with a [logits processor](https://gist.github.com/peakji/f81c032b6c24b358054ed763c426a46f) used to constrain the number of reasoning steps, an optimal configuration can yield an enhancement of +5.56.

Press enter or click to view image in full size

The decision to showcase this benchmark is twofold: firstly, because o1/o1-mini has demonstrated significant improvements on this dataset, and secondly, because the contamination situation of this dataset is relatively favorable. Additionally, I observed that Steiner shows no significant differences compared to the baseline on datasets like MMLU, which aligns with OpenAI’s observations regarding o1-mini in their [blog](https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/), potentially reflecting the limitations of a 32B model’s world knowledge gained during the pre-training phase.

While it is important to acknowledge that the current model's capabilities still fall significantly short of o1-mini and o1, the issue lies in the nature of automated evaluation benchmarks, which are primarily composed of multiple-choice questions and may not fully reflect the capabilities of reasoning models. During the training phase, reasoning models are encouraged to engage in open-ended exploration of problems, whereas multiple-choice questions operate under the premise that "the correct answer must be among the options." This makes it evident that verifying options one by one is a more efficient approach. In fact, existing large language models have, consciously or unconsciously, mastered this technique, regardless of whether special prompts are used. Ultimately, it is this misalignment between automated evaluation and genuine reasoning requirements that makes me believe it is essential to open-source the model for real human evaluation and feedback.

The bigger issue lies in the inference-time scaling experiments: unfortunately, after using the [logits processor](https://gist.github.com/peakji/f81c032b6c24b358054ed763c426a46f) to increase the number of reasoning steps, Steiner has shown no improvements on almost all tested benchmarks, and in some cases, performance has even declined. There are numerous speculated reasons for this, including but not limited to:

-   CPT/SFT did not enable the model to truly grasp long output tokens.
-   The heuristic reward design in the RL phase failed to help the model balance breadth and depth in reasoning.
-   During backtracking, context influences can easily lead to confirming incorrect answers or denying originally correct ones.
-   The method of forcibly modifying logits to increase reasoning steps is just too blunt.
-   … …

All in all, this will be the primary focus of my future work.

## **Limitations**

-   Steiner’s current post-training data does not include examples for multi-turn dialogues. The best-performing version of the Steiner model (based on Qwen2.5–32B) lacks the ability to handle multi-turn conversations. The open-source Steiner-preview model (based on Qwen2.5–32B-Instruct) is compatible with chat formats but is still not recommended for multi-turn dialogues.
-   Similar to OpenAI o1–2024–09–12, Steiner also does not recommend the use of custom system prompts or modifications to sampling parameters such as temperature. Steiner has not yet been trained on a diverse set of system prompts, and altering other parameters may lead to errors in the formatting of reasoning tokens.
-   The language composition of Steiner’s post-training data is approximately 90% English and 10% Chinese, but during the reasoning path data augmentation process, almost only English was used. Therefore, while the model’s final responses demonstrate a certain degree of language following ability, the reasoning tokens may predominantly be generated in English.

## Wait… What the heck is “Steiner”?

As for the origin of the name Steiner, why not ask the model itself?

> 🧑🏻‍💻 What is the origin of your name?
>
> 💬 My name, “Steiner,” is inspired by the protagonist’s ability “Reading Steiner” from the visual novel and anime \*Steins;Gate\*. This ability allows the character to retain memories across multiple world lines, which aligns with my capabilities of exploring different reasoning paths and retaining information across them.

## Citation

If you find my work helpful, please consider citing it in your research or projects. Your acknowledgment would be greatly appreciated!

@misc{ji2024steiner,
    title = {A Small Step Towards Reproducing OpenAI o1: Progress Report on the Steiner Open Source Models},
    url = {https://medium.com/@peakji/b9a756a00855},
    author = {Yichao Ji},
    month = {October},
    year = {2024}
}