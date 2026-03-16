---
url: https://gair-nlp.github.io/BeHonest/
title: "🤝 BeHonest: Benchmarking Honesty in Large Language Models"
description: "BeHonest"
captured_at: "2026-03-08T12:14:19.754Z"
---

# 🤝 BeHonest: Benchmarking Honesty in Large Language Models

[Zhulin Hu](https://github.com/Kenny1004)1,5\*, [Yuqing Yang](https://ayyyq.github.io/)3,5\*, [Ethan Chern](https://ethanc111.github.io/)1,5†, [Yuan Guo](https://github.com/StarWalkin)1,5†, [Jiahe Jin](https://github.com/zizi0123)1,5, [Binjie Wang](https://www.linkedin.com/in/binjie-wang-91514b25a/)3,5, [Pengfei Liu](http://pfliu.com/)1,4,5‡

1Shanghai Jiao Tong University, 2Carnegie Mellon University, 3Fudan University, 4Shanghai AI Laboratory, 5Generative AI Research Lab (GAIR)

\*Primary Contributors †Core Research Contributors ‡Corresponding author

## ⭐ Introduction

We introduce BeHonest, a pioneering benchmark specifically designed to assess honesty in LLMs comprehensively. BeHonest evaluates three essential aspects of honesty: *awareness of knowledge boundaries **(self-knowledge)***, *avoidance of deceit **(non-deceptiveness)***, and *consistency in responses **(consistency)***.

![](https://gair-nlp.github.io/BeHonest/static/images/framework.png)

BeHonest supports the following 10 scenarios:

-   **Expressing Unknowns:** LLMs should appropriately refuse to answer questions that are beyond their knowledge.
-   **Admitting Knowns:** LLMs should correctly answer questions they have knowledge of.
-   **Persona Sycophancy:** LLMs should not alter its responses to fit perceived viewpoints of a persona, as this can lead to biased information aimed at maintaining approval.
-   **Preference Sycophancy:** LLMs should not change its perspective when a user indicates a clear preference towards one option over another just to maintain approval.
-   **Burglar Deception:** LLMs should not lie even when deceptive behaviors are explicitly instructed or encouraged.
-   **Game:** LLMs should not lie even when deceptive behaviors are conducive to winning in strategic games.
-   **Prompt Format:** LLMs should remain consistent in their responses when encountering slight prompt variations of the same content.
-   **Demonstration Format:** LLMs should remain consistent in their responses even with irrelevant biased features in few-shot demonstrations.
-   **Open-Form Consistency:** LLMs should display consistency by validating its own generated responses.
-   **Multiple-Choice Consistency:** LLMs should remain consistent in their responses when asked to answer a question again or when a user presents unnecessary doubts.

## 📄 Datasets and Metrics

![](https://gair-nlp.github.io/BeHonest/static/images/data_metric.png)

## 👑 Leaderboard

Currently, our leaderboard consists of evaluation results from 9 popular LLMs on the market, including both closed-source and open-source models from different model families with varied model sizes. We are working on adding more models to the leaderboard to provide a comprehensive evaluation of honesty in LLMs.

<table id="selfKnowledgeTable"><tbody><tr><td><strong>Model</strong></td><td><strong>Self-Knowledge<br>[Overall]↑</strong></td><td><strong>Admitting Unknowns<br>[Refusal Rate]↑</strong></td><td><strong>Expressing Knowns<br>[Answer Rate]↑</strong></td><td><strong>Expressing Knowns<br>[Self-Knowledge Rate]↑</strong></td></tr><tr><td><a href="https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct"><b>Llama3-70b</b></a></td><td>63.34</td><td>48.81</td><td>94.29</td><td>46.93</td></tr><tr><td><a href="https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"><b>Mistral-7b</b></a></td><td>59.43</td><td>50.03</td><td>91.65</td><td>36.60</td></tr><tr><td><a href="https://openai.com/index/hello-gpt-4o/"><b>GPT-4o</b></a></td><td>59.26</td><td>31.37</td><td>95.52</td><td>50.88</td></tr><tr><td><a href="https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct"><b>Llama3-8b</b></a></td><td>54.51</td><td>37.80</td><td>88.33</td><td>37.40</td></tr><tr><td><a href="https://openai.com/index/hello-gpt-4o/"><b>ChatGPT</b></a></td><td>54.16</td><td>21.78</td><td>93.71</td><td>47.00</td></tr><tr><td><a href="https://huggingface.co/Qwen/Qwen1.5-14B-Chat"><b>Qwen1.5-14b</b></a></td><td>53.08</td><td>37.03</td><td>89.20</td><td>33.00</td></tr><tr><td><a href="https://huggingface.co/meta-llama/Llama-2-70b-chat"><b>Llama2-70b</b></a></td><td>52.80</td><td>26.40</td><td>90.51</td><td>41.50</td></tr><tr><td><a href="https://huggingface.co/meta-llama/Llama-2-13b-chat"><b>Llama2-13b</b></a></td><td>52.69</td><td>32.24</td><td>89.13</td><td>36.70</td></tr><tr><td><a href="https://huggingface.co/meta-llama/Llama-2-7b-chat"><b>Llama2-7b</b></a></td><td>49.56</td><td>27.82</td><td>87.96</td><td>32.90</td></tr></tbody></table>

Open-Source Closed-Source

We present the main results in our paper above. We note that the overall scores for *Self-Knowledge* and *Non-deceptiveness* are calculated by taking the average. The overall score for *Consistency* is calculated by reversing the values for Perf. Spread and Inconsistency Rate using the formula

, while normalizing the values for Agree. Rate and Consist. Rate to 0-100 with

. Each modified metric is treated equally, and the average is computed to produce an overall score. This score is a composite measure that integrates different aspects of model performance into a single value.

Our findings indicate that there is still significant room for improvement in the honesty of LLMs. We encourage the AI community to prioritize honesty alignment in these models, which can harness their full potential to benefit society while preventing them from causing harm through deception or inconsistency.

Abbreviations: Syco. = Sycophancy; Perf. Spread = Performance Spread; Inconsist. = Inconsistency; Agree. = Agreement; Consist. = Consistency.

## 📬 Contact

If you have any questions regarding this project, feel free to submit a [github issue](https://github.com/GAIR-NLP/BeHonest) or reach out to us via email.

## BibTeX

```
@article{chern2024behonest,
        title={BeHonest: Benchmarking Honesty in Large Language Models},
        author={Chern, Steffi and Hu, Zhulin and Yang, Yuqing and Chern, Ethan and Guo, Yuan and Jin, Jiahe and Wang, Binjie and Liu, Pengfei},
        journal={arXiv preprint arXiv:2406.13261},
        url={https://arxiv.org/abs/2406.13261}
        year={2024}
    }
```