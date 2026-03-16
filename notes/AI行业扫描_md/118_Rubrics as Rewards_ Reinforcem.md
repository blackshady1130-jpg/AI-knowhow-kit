---
url: https://arxiv.org/html/2507.17746v1
title: "Rubrics as Rewards: \nReinforcement Learning Beyond Verifiable Domains"
captured_at: "2026-03-09T03:33:24.069Z"
---

# Rubrics as Rewards: 
Reinforcement Learning Beyond Verifiable Domains

## Rubrics as Rewards:
Reinforcement Learning Beyond Verifiable Domains

Anisha Gunjal  Anthony Wang  Elaine Lau
 Vaskar Nath  Bing Liu  Sean Hendryx
Scale AI
anisha.gunjal@scale.com

###### Abstract

Extending Reinforcement Learning with Verifiable Rewards (RLVR) to real-world tasks often requires balancing objective and subjective evaluation criteria. However, many such tasks lack a single, unambiguous ground truth—making it difficult to define reliable reward signals for post-training language models. While traditional preference-based methods offer a workaround, they rely on opaque reward functions that are difficult to interpret and prone to spurious correlations. We introduce Rubrics as Rewards (RaR), a framework that uses structured, checklist-style rubrics as interpretable reward signals for on-policy training with GRPO. Our best RaR method yields up to a 28% relative improvement on HealthBench-1k compared to simple Likert-based approaches, while matching or surpassing the performance of reward signals derived from expert-written references. By treating rubrics as structured reward signals, we show that RaR enables smaller-scale judge models to better align with human preferences and sustain robust performance across model scales.

Rubrics as Rewards:
Reinforcement Learning Beyond Verifiable Domains

Anisha Gunjal   Anthony Wang††thanks: Work done while at Scale AI.   Elaine Lau  Vaskar Nath  Bing Liu  Sean Hendryx Scale AI anisha.gunjal@scale.com

## 1 Introduction

Reinforcement Learning with Verifiable Rewards (RLVR) has enabled large language models to elicit complex reasoning on tasks with verifiable outcomes, most prominently in mathematics and coding, where a reward model can be replaced with a scoring function and final answers are easily verifiable or test cases provide automated mechanisms for evaluation Lambert et al. ([2024](https://arxiv.org/html/2507.17746v1#bib.bib16)); Guo et al. ([2025a](https://arxiv.org/html/2507.17746v1#bib.bib10)); Cui et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib6)). However, many real-world tasks lack such explicit verifiable answers, leaving models without direct reward feedback. In practice, researchers often turn to RLHF via preference ranking—collecting human judgments over pairs or lists of model outputs to fill this gap. While preference-based reward models can bootstrap performance, they tend to overfit superficial artifacts (e.g. response length, formatting quirks, annotator biases) Singhal et al. ([2023](https://arxiv.org/html/2507.17746v1#bib.bib26)); Wang et al. ([2024](https://arxiv.org/html/2507.17746v1#bib.bib30)); Chen et al. ([2024b](https://arxiv.org/html/2507.17746v1#bib.bib4)); Ye et al. ([2024](https://arxiv.org/html/2507.17746v1#bib.bib32)); Gudibande et al. ([2023](https://arxiv.org/html/2507.17746v1#bib.bib9)) and require large volumes of pairwise comparisons Ouyang et al. ([2022](https://arxiv.org/html/2507.17746v1#bib.bib21)), making preference-based reward models brittle and costly.

To address this gap, we introduce Rubrics as Rewards (RaR) for on-policy Reinforcement Learning that treats structured criteria or rubrics as the core reward mechanism. We use rubrics as checklists Arora et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib2)); Sirdeshmukh et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib27)) composed of independent subgoals allowing for automatable feedback aligned with expert intent. By decomposing “what makes a good response” into tangible, human-interpretable criteria, rubrics offer a middle ground between binary correctness signals and coarse preference rankings.

![Refer to caption](https://arxiv.org/html/2507.17746v1/x1.png)

Figure 1: Overview of Rubrics as Rewards (RaR). (i) Rubric Generation: We synthesize prompt-specific, self-contained rubric criteria using a strong LLM guided by four core design principles, with reference answers serving as proxies for expert supervision. (ii) GRPO Training: These rubrics are used to prompt an LLM judge for reward estimation, which drives policy optimization via the GRPO on-policy learning loop.

Previous works train generative reward models that learn to evaluate reasoning or final outputs with interpretable scores Chen et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib5)); Whitehouse et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib31)); Anugraha et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib1)); Guo et al. ([2025b](https://arxiv.org/html/2507.17746v1#bib.bib11)), and some have even used a model’s internal confidence estimates as a proxy for reward Zhao et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib35)). Concurrently, recent efforts have extended verifiable datasets beyond STEM domains, broadening the applicability of RLVR methods to a wider range of tasks Su et al. ([2025b](https://arxiv.org/html/2507.17746v1#bib.bib29)); Ma et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib19)). However, developing a general-purpose approach for specifying reliable and scalable rewards remains an open challenge, particularly in settings where no single ground truth exists, or where both subjective and objective criteria must be considered to evaluate response quality. The Rubrics as Rewards strategy offers a flexible solution by repurposing structured evaluation criteria into multi-dimensional reward signals. Figure [1](https://arxiv.org/html/2507.17746v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains") illustrates our approach for generating rubrics and leveraging them as reward signals for on-policy training.

Our key contributions are as follows: (i) We introduce Rubrics as Rewards (RaR), an on-policy reinforcement learning framework that uses checklist-style rubrics to supervise multi-criteria tasks, enabling stable training and improved performance in both reasoning and real-world domains. (ii) We apply our rubric generation approach to the medicine and science domains, producing two training datasets—RaR-Medicine-20k and RaR-Science-20k111The datasets will be released soon.. (iii) We show that models trained with RaR match or outperform strong baselines, achieving notable gains in accuracy across diverse domains. (iv) By using rubrics as structured reward signals, RaR enables smaller judge models to achieve better alignment with human preferences and maintains robust performance across different model scales.

## 2 Rubrics as Rewards

### 2.1 Problem Formulation

Let xx denote an input prompt and y^∼πθ(⋅∣x)\\hat{y}\\sim\\pi\_{\\theta}(\\cdot\\mid x) be a sampled response from a model parameterized by θ\\theta. In domains without single ground-truth answers or automatic correctness signals, we define a structured reward function using prompt-specific rubric criteria.

Each prompt xx is associated with a set of kk rubric items {(wj,cj)}j\=1k\\{(w\_{j},c\_{j})\\}\_{j=1}^{k}, where wj∈ℝw\_{j}\\in\\mathbb{R} denotes the weight of criterion jj, and cj:(x,y^)↦{0,1}c\_{j}:(x,\\hat{y})\\mapsto\\{0,1\\} is a binary correctness function that indicates whether the response y^\\hat{y} satisfies that criterion given the prompt. The final normalized scalar reward is computed as:

<table id="S2.E1"><tbody><tr><td></td><td><math alttext="r(x,\hat{y})=\frac{\sum_{j=1}^{k}w_{j}\cdot c_{j}(x,\hat{y})}{\sum_{j=1}^{k}w_{j}}" display="block" id="S2.E1.m1" intent=":literal"><semantics><mrow><mrow><mi>r</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mover accent="true"><mi>y</mi><mo>^</mo></mover><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mfrac><mrow><msubsup><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>k</mi></msubsup><mrow><mrow><msub><mi>w</mi><mi>j</mi></msub><mo lspace="0.222em" rspace="0.222em">⋅</mo><msub><mi>c</mi><mi>j</mi></msub></mrow><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mover accent="true"><mi>y</mi><mo>^</mo></mover><mo stretchy="false">)</mo></mrow></mrow></mrow><mrow><msubsup><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>k</mi></msubsup><msub><mi>w</mi><mi>j</mi></msub></mrow></mfrac></mrow><annotation encoding="application/x-tex">r(x,\hat{y})=\frac{\sum_{j=1}^{k}w_{j}\cdot c_{j}(x,\hat{y})}{\sum_{j=1}^{k}w_{j}}</annotation></semantics></math></td><td></td><td rowspan="1"><span>(1)</span></td></tr></tbody></table>

This normalization ensures reward values are consistent across prompts with varying numbers and weights of rubric items.

#### Explicit Rubric Aggregation.

Each criterion is evaluated independently using a generative reward model, and the reward is computed using Equation [1](https://arxiv.org/html/2507.17746v1#S2.E1 "In 2.1 Problem Formulation ‣ 2 Rubrics as Rewards ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains"). While we currently assume binary values for cjc\_{j}, this framework supports extension to continuous-valued judgments.

#### Implicit Rubric Aggregation.

An alternative approach passes all rubric descriptions and weights to a generative reward model, which internally computes a scalar reward:

<table id="S2.E2"><tbody><tr><td></td><td><math alttext="r_{\text{implicit}}(x,\hat{y})=f_{\phi}(x,\hat{y},\{(w_{j},d_{j})\}_{j=1}^{k})" display="block" id="S2.E2.m1" intent=":literal"><semantics><mrow><mrow><msub><mi>r</mi><mtext>implicit</mtext></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mover accent="true"><mi>y</mi><mo>^</mo></mover><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><msub><mi>f</mi><mi>ϕ</mi></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mover accent="true"><mi>y</mi><mo>^</mo></mover><mo>,</mo><msubsup><mrow><mo stretchy="false">{</mo><mrow><mo stretchy="false">(</mo><msub><mi>w</mi><mi>j</mi></msub><mo>,</mo><msub><mi>d</mi><mi>j</mi></msub><mo stretchy="false">)</mo></mrow><mo stretchy="false">}</mo></mrow><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>k</mi></msubsup><mo stretchy="false">)</mo></mrow></mrow></mrow><annotation encoding="application/x-tex">r_{\text{implicit}}(x,\hat{y})=f_{\phi}(x,\hat{y},\{(w_{j},d_{j})\}_{j=1}^{k})</annotation></semantics></math></td><td></td><td rowspan="1"><span>(2)</span></td></tr></tbody></table>

Here, fϕf\_{\\phi} denotes an LLM-based judge that takes as input the prompt xx, the generated response y^\\hat{y}, and a set of weighted rubric criteria. Each pair (wj,dj)(w\_{j},d\_{j}) consists of a scalar or categorical weights wj∈ℝw\_{j}\\in\\mathbb{R} and a rubric criterion djd\_{j} describing a specific aspect of response quality. This formulation delegates the aggregation of evaluation criteria to the model itself, allowing it to compute a holistic reward score.

In practice, we use an LLM-as-judge with separate prompt templates containing prompt, response, and rubric items for explicit and implicit aggregation. The prompts used in our experiments are detailed in Appendix [E](https://arxiv.org/html/2507.17746v1#A5 "Appendix E LLM-Judge Prompts ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains").

### 2.2 Generalization of RLVR with Rubrics as Rewards

Rubric-based reinforcement learning extends the standard RLVR (Reinforcement Learning with Verifiable Rewards) setting by supporting multi-dimensional, prompt-specific evaluation criteria. We formalize this relationship below.

Rubric-based reward functions thus generalize RLVR by enabling multi-dimensional supervision, flexible weighting across criteria, and the incorporation of both objective and subjective aspects of response quality.

This formalization highlights that RLVR can be seen as a restricted instance of rubric-guided RL with a single essential criterion. In contrast, rubric-based rewards further enable structured supervision in settings where correctness is multifaceted and may not be strictly verifiable.

## 3 Rubric Generation

### 3.1 Desiderata

We synthesize prompt-specific rubrics guided by a set of design principles. Each rubric defines the criteria for a high-quality response and enables human-interpretable supervision. We use large language models (LLMs) as expert proxies to generate these rubrics while ensuring adherence to the following desiderata:

#### Grounded in Expert-guidance

Reference answers produced by human experts or stronger LLMs serve as proxies for expert guidance. Rubrics are grounded in these references to capture the key facts, reasoning steps, and conclusions necessary for correctness.

#### Comprehensive coverage

Rubrics are designed to span multiple quality dimensions, including factual accuracy, logical structure, completeness, style, and common pitfalls. Negative “pitfall” criteria help penalize frequent or high-risk errors. The total number of rubric items per rubric (typically 7–20) is chosen to balance coverage with signal sparsity.

#### Semantic weighting

Each criterion is labeled with a categorical importance level (e.g., Essential, Important, Optional, Pitfall) that reflects its relative priority in the final reward. This supports interpretable reward aggregation. Future work may explore numeric or learned weighting for greater flexibility.

#### Self-contained evaluation

Rubrics are written to be independently actionable-each item can be evaluated in isolation by either human annotators or LLM-based judges, without requiring external context or domain knowledge.

### 3.2 Synthesis

We apply the above framework on real world science and Medicine reasoning domains. For each domain, the prompt (included in Appendix [H](https://arxiv.org/html/2507.17746v1#A8 "Appendix H Synthetic Rubric Generation Prompts ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains")) instructs the LLM to generate 7–20 rubric items based on the complexity of the input question. Each item is assigned a categorical weight (e.g., Essential Criteria, Important Criteria) to determine its importance to a correct answer. The rubrics are designed to be fully self-contained which means that non-expert readers should be able to evaluate response quality using only the rubric. The evaluation outcome can be directly used as reward functions during reinforcement learning.

We generate synthetic rubrics using OpenAI’s o3-mini and gpt-4o models OpenAI o3-mini ([2025](https://arxiv.org/html/2507.17746v1#bib.bib20)); Jaech et al. ([2024](https://arxiv.org/html/2507.17746v1#bib.bib14)); Hurst et al. ([2024](https://arxiv.org/html/2507.17746v1#bib.bib13)) as described in Section [3](https://arxiv.org/html/2507.17746v1#S3 "3 Rubric Generation ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains"). The RaR-Medical-20k and RaR-Science-20k are released for public use. For both domains, we use the reference answers provided in the datasets as a proxy for human expertise while generating synthetic rubrics. These rubric sets are then used to supervise the training of smaller models through either explicit or implicit reward aggregation (Section [2.1](https://arxiv.org/html/2507.17746v1#S2.SS1 "2.1 Problem Formulation ‣ 2 Rubrics as Rewards ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains")).

## 4 Experiments

Table 1: Performance of baseline and RaR (Rubrics as Rewards) methods on medicine and science domains. For HealthBench-1k, we report the overall score; for GPQA\_Diamond, we report mean accuracy over 4 runs with standard deviation. All experiments use gpt-4o-mini as the judge model. (RaR) methods are trained using rubrics generated by either o3-mini or GPT-4o. Across both domains, the RaR-Implicit method consistently outperforms Simple-Likert and matches or exceeds the performance of Reference-Likert.

### 4.1 Datasets

We investigate the utility of rubrics as rewards across two reasoning domains medicine and science.

-   •

    RaR‑Medical‑20k: We curate a set of 20k prompts from medicine‑related subsets of medical‑o1‑reasoning‑SFT Chen et al. ([2024a](https://arxiv.org/html/2507.17746v1#bib.bib3)), the natural\_reasoning dataset Yuan et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib33)), the SCP‑116K dataset Lu et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib18)), and the GeneralThought‑430K dataset General Reasoning ([2025](https://arxiv.org/html/2507.17746v1#bib.bib8)).

-   •

    RaR‑Science‑20k: We curate roughly 20k science prompts aligned with the GPQA Diamond benchmark from the natural\_reasoning dataset Yuan et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib33)), the SCP‑116K dataset Lu et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib18)), and the GeneralThought‑430K dataset General Reasoning ([2025](https://arxiv.org/html/2507.17746v1#bib.bib8)).

Refer Tables [7](https://arxiv.org/html/2507.17746v1#A1.T7 "Table 7 ‣ A.1 Medicine training dataset - Overall Data Distribution ‣ Appendix A Training dataset breakdown ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains") and [10](https://arxiv.org/html/2507.17746v1#A1.T10 "Table 10 ‣ A.2 STEM Dataset - Overall Data Distribution ‣ Appendix A Training dataset breakdown ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains") in Appendix for the full topic distributions.

### 4.2 Training Details

We train all models using the GRPO algorithm Shao et al. ([2024](https://arxiv.org/html/2507.17746v1#bib.bib25)), with Qwen2.5-7B as the base policy. Training is conducted with a batch size of 96, a learning rate of 5×10−65\\times 10^{-6}, and a constant learning rate schedule with 10% linear warmup. Full hyperparameter details are provided in Appendix [11](https://arxiv.org/html/2507.17746v1#A3.T11 "Table 11 ‣ Appendix C Judge Quality impacts on Post-training ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains"). All models are trained on a single compute node equipped with 8 NVIDIA H100 GPUs.

Our training pipeline consists of the following key components:

Response Generation: For each prompt qq, we sample k\=16k=16 responses from the current policy πθ\\pi\_{\\theta}, using a context length of 3584 and a sampling temperature of 1.0.

Reward Computation: We use gpt-4o-mini as the judge model to assign rewards RqR\_{q} to the sampled responses. The reward functions are described in Sections [4.3](https://arxiv.org/html/2507.17746v1#S4.SS3 "4.3 Baselines ‣ 4 Experiments ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains") and [4.4](https://arxiv.org/html/2507.17746v1#S4.SS4 "4.4 Rubric-guided Methods ‣ 4 Experiments ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains").

Policy Update: The policy is updated using GRPO based on the computed rewards.

### 4.3 Baselines

We consider compare various baselines and off-the-shelf post-trained models. All rubric-free baselines are with Qwen2.5-7b as the base policy.

For off-the-shelf baselines we evaluate performance on Qwen2.5-7b. We also include the performance of Qwen2.5-7b-Instruct to compare with instruction tuned variant of the base policy.

We describe the post-trained baselines without rubrics below:

SIMPLE-LIKERT:

LLM-judge is asked to output a Likert Score from 1-10 (normalized to 0-1) for each response-prompt pair.

REFERENCE-LIKERT:

The judge model compares the generated response against a high-quality reference answer and outputs a Likert score from 1–10, which is then normalized to the \[0,1\]\[0,1\] range. The reward for each (prompt, response, reference) triplet is defined as:

<table id="S4.Ex1"><tbody><tr><td></td><td><math alttext="R_{\text{ref}}(q,x)=\mathrm{Norm}(\text{LikertScore}(q,x,x^{*}))" display="block" id="S4.Ex1.m1" intent=":literal"><semantics><mrow><mrow><msub><mi>R</mi><mtext>ref</mtext></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>q</mi><mo>,</mo><mi>x</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mi>Norm</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mrow><mtext>LikertScore</mtext><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>q</mi><mo>,</mo><mi>x</mi><mo>,</mo><msup><mi>x</mi><mo>∗</mo></msup><mo stretchy="false">)</mo></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow><annotation encoding="application/x-tex">R_{\text{ref}}(q,x)=\mathrm{Norm}(\text{LikertScore}(q,x,x^{*}))</annotation></semantics></math></td><td></td></tr></tbody></table>

where x∗x^{\*} denotes the reference answer, either written by a human or generated by a stronger LLM.

### 4.4 Rubric-guided Methods

PREDEFINED-RaR:

This method uses a fixed set of generic rubrics (not prompt-specific, as described in Appendix [C](https://arxiv.org/html/2507.17746v1#A3 "Appendix C Judge Quality impacts on Post-training ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains")) and computes the reward via an explicit weighted sum, following Equation [1](https://arxiv.org/html/2507.17746v1#S2.E1 "In 2.1 Problem Formulation ‣ 2 Rubrics as Rewards ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains"). All rubric criteria are weighted uniformly.

RaR-EXPLICIT:

This variant also employs explicit aggregation ([1](https://arxiv.org/html/2507.17746v1#S2.E1 "In 2.1 Problem Formulation ‣ 2 Rubrics as Rewards ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains")) but uses prompt-specific rubrics generated by the method in Section [3](https://arxiv.org/html/2507.17746v1#S3 "3 Rubric Generation ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains"). Since the generated rubrics include categorical labels, we assign numerical weights using a simple default scheme: {"Essential": 1.0, "Important": 0.7, "Optional": 0.3, "Pitfall": 0.8}, with higher penalty applied to violated pitfalls. 222Pitfall criteria are phrased in positive form (e.g., “The response avoids misinformation”), so satisfying them contributes positively to the score. If a pitfall is not satisfied, the corresponding reward is reduced or penalized.

RaR-IMPLICIT:

This variant also leverages prompt-specific rubrics; however, instead of aggregating criterion scores explicitly, it prompts the judge model to evaluate the response holistically and assign a single Likert rating (1–10). This rating is then normalized to the \[0,1\]\[0,1\] range:

<table id="S4.Ex2"><tbody><tr><td></td><td><math alttext="R_{\text{implicit}}(q,x)=\mathrm{Norm}(\text{LikertScore}(q,x,R_{q}))" display="block" id="S4.Ex2.m1" intent=":literal"><semantics><mrow><mrow><msub><mi>R</mi><mtext>implicit</mtext></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>q</mi><mo>,</mo><mi>x</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mi>Norm</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mrow><mtext>LikertScore</mtext><mo lspace="0em" rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>q</mi><mo>,</mo><mi>x</mi><mo>,</mo><msub><mi>R</mi><mi>q</mi></msub><mo stretchy="false">)</mo></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow><annotation encoding="application/x-tex">R_{\text{implicit}}(q,x)=\mathrm{Norm}(\text{LikertScore}(q,x,R_{q}))</annotation></semantics></math></td><td></td></tr></tbody></table>

where RqR\_{q} denotes the list of rubrics associated with prompt qq.

### 4.5 Evaluation Setup

#### Medical Reasoning

We evaluate models trained on curated medical reasoning data using HealthBench-1k Arora et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib2)), a 1,000-example subset of HealthBench.333We introduce HealthBench-1k as a cost-effective evaluation split for medical reasoning tasks and will release the test set identifiers to support reproducibility.. We generate model responses with greedy decoding (temperature=0) and report the overall\_score.

#### Science Reasoning

We evaluate models trained with curated science set on the GPQA-Diamond subset Rein et al. ([2024](https://arxiv.org/html/2507.17746v1#bib.bib23)). Each evaluation is independently repeated 4 times to account for variance, where each run samples one response per prompt using greedy decoding (temperature=0). Answer choices are permuted per example, and model outputs are parsed for boxed answer formats (e.g.,
boxed{A}). If extraction fails, we fall back to a GPT-4o verifier that checks whether the response contains the correct option letter or text (see [F](https://arxiv.org/html/2507.17746v1#A6 "Appendix F Evaluation Prompts ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains")). Final accuracy is reported as the mean of the 4 independent runs.

## 5 Results

We now present the main findings of our study.

#### Rubrics as Rewards Combine Interpretability with Strong Performance.

Table [1](https://arxiv.org/html/2507.17746v1#S4.T1 "Table 1 ‣ 4 Experiments ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains") reports results on the Medicine (HealthBench-1k) and Science (GPQA\_Diamond) benchmarks. Our method, RaR-Implicit, consistently outperforms baselines such as Simple-Likert, with the best variant achieving upto 28% relative improvement on HealthBench-1k and 13% on GPQA. It also surpasses both base and instruction-tuned policy models, demonstrating the effectiveness of rubric-guided training for nuanced response evaluation.

Furthermore, RaR-Implicit matches or exceeds the performance of the Reference-Likert baseline. In our setup, synthetic rubrics are generated using reference answers as proxies for expert supervision, meaning their quality is inherently constrained by the completeness and clarity of those references. Despite this, transforming open-ended answers into structured rubric criteria produces reward signals that are both effective and aligned with evaluation objectives.

We also find that implicit aggregation outperforms explicit, weighted summation which indicates that allowing an LLM-based judge to infer how to balance rubric criteria per prompt is more effective than relying on fixed, hand-crafted weights. While explicit aggregation offers more transparency and control, implicit methods better adapt to real-world complexity.

Rubric-based supervision further enables transparent reward specification by breaking response quality into interpretable criteria. Unlike holistic reference comparisons, rubrics reduce stylistic bias and surface-level overfitting. Though reference-based Likert scoring may perform slightly better in some cases, rubrics offer a more scalable and controllable approach—particularly where references are scarce or model interpretability is essential.

![Refer to caption](https://arxiv.org/html/2507.17746v1/figs/llm_judge_line_comparison.png)

Figure 2: LLM Judge Alignment Across Model Scales. Rubric-guided evaluation (orange) consistently improves judge accuracy across model sizes compared to pure Likert-based scoring (blue). Rubrics without reference answers (green) perform better than Likert baseline, though still lag behind full rubric guidance. Smaller scale models benefit the most from rubric structure, narrowing the performance gap with larger judges.

#### Rubrics enhance alignment with human preferences across model scales

To evaluate the effectiveness of rubric-based evaluations in reflecting human preferences, we generated datasets consisting preferred (chosen) and perturbed (rejected) responses (see Appendix [I](https://arxiv.org/html/2507.17746v1#A9 "Appendix I Perturbed Dataset Generation ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains") for details on dataset generation). We use LLM-Judges to assign ratings from 1 to 10 for these responses both with (RaR-IMPLICIT ) and without the guidance of rubrics (SIMPLE-LIKERT). Figure [2](https://arxiv.org/html/2507.17746v1#S5.F2 "Figure 2 ‣ Rubrics as Rewards Combine Interpretability with Strong Performance. ‣ 5 Results ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains") shows how often judges correctly rated the preferred responses higher than the rejected ones across various model scales (from 3b to 72b to o3-mini). The results consistently show that rubric-guided evaluations provide clearer and more accurate signals, as evidenced by the higher accuracy with which preferred responses receive higher ratings when rubrics are involved. This indicates that rubrics improves the alignment with human preferences by offering detailed, context-specific criteria that help judges better discern subtle differences in quality compared to evaluations using only simple Likert-based ratings. Further study on LLM-Judge scaling impacts on policy training are discussed in Appendix [C](https://arxiv.org/html/2507.17746v1#A3 "Appendix C Judge Quality impacts on Post-training ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains").

#### Expert guidance is crucial for synthetic rubric generation

Human guidance significantly influences the effectiveness of rubrics in capturing subtle human preferences. Figure [2](https://arxiv.org/html/2507.17746v1#S5.F2 "Figure 2 ‣ Rubrics as Rewards Combine Interpretability with Strong Performance. ‣ 5 Results ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains") highlights performance differences between rubric-based evaluations that include reference answers and those without them. The data shows that rubrics developed with reference answers achieve higher accuracy, emphasizing that human insights integrated during rubric generation enable granular criteria and improved alignment with human preferences.

## 6 Ablations

#### Elements of Rubric Design

This ablation study examines how the structure and weighting of synthetic rubrics—generated using o3-mini—affect downstream performance on HealthBench. As shown in Table [2](https://arxiv.org/html/2507.17746v1#S6.T2 "Table 2 ‣ Elements of Rubric Design ‣ 6 Ablations ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains"), predefined generic rubrics substantially underperform compared to prompt-specific ones, underscoring the importance of contextualization. Rubrics that include a broader range of criteria—both positive and negative—consistently outperform those limited to essential checks, suggesting that richer evaluation signals lead to better learning. Interestingly, we observe minimal performance differences when including rubric weights or pitfall criteria during training. One possible explanation is that synthetically generating effective pitfall criteria is inherently difficult, as it requires anticipating the most common or critical failure modes of the model, a task that often demands human intuition and domain expertise. As a result, these synthetic negative criteria may lack the specificity or relevance needed to meaningfully penalize undesirable responses.

Table 2: Ablation results on HealthBench-1k (trained on HealthBench-3.5k subset with Qwen2.5-7B base policy). Rubrics generated using o3-mini with access to reference answers. Variations test the impact of rubric structure and weighting on implicit reward aggregation.

Table 3: Evaluation on HealthBench: Comparison of human- vs. synthetic-generated rubrics (with and without reference answers). RaR methods trained with GRPO significantly outperform Likert-only, Reference-based-likert and SFT baselines. Synthetic rubrics generated without access to reference answers perform notably worse, highlighting the importance of human-grounded guidance. Notably, human-authored rubrics and synthetic rubrics with access to references yield comparable performance.

#### Impact of Rubric Generation Strategies in Real-World Domains

How does the method of rubric generation affect downstream training in challenging, real-world settings? To investigate this, we evaluate on the HealthBench dataset using a curated subset of 3.5k human-annotated examples, split into train and test sets. Table [3](https://arxiv.org/html/2507.17746v1#S6.T3 "Table 3 ‣ Elements of Rubric Design ‣ 6 Ablations ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains") summarizes the results.

We observe that all rubric-based methods outperform rubric-free baselines, including Reference-Likert. Notably, even the weakest RaR variant significantly surpasses Reference-Likert, underscoring the advantage of structured supervision in subjective, open-ended domains like healthcare. We attribute this to the finer granularity and clarity rubrics provide in assigning rewards-especially when correctness is not binary and answers may vary in tone, completeness, or safety relevance.

Moreover, we find that rubric quality is crucial: synthetic rubrics generated with reference-answer guidance consistently outperform those generated without it. This highlights the importance of incorporating expert signal, whether via human-in-the-loop annotations or high-quality reference completions, for generating effective and aligned rubrics. Purely synthetic rubrics, while scalable, currently fall short in capturing the subtle criteria required for robust training in high-stakes domains.

#### Impact of LLM Expertise on Rubric Quality

To assess how the capabilities of rubric-generating LLMs affect downstream performance, we generate synthetic rubrics without access to reference answers and use them to train policies on HealthBench. This isolates the effect of LLM quality on reference-free rubric utility. Specifically, we evaluate on the HealthBench-1k subset, using models trained on rubrics generated for the remaining 4k training examples from HealthBench.

As shown in Table [4](https://arxiv.org/html/2507.17746v1#S6.T4 "Table 4 ‣ Impact of LLM Expertise on Rubric Quality ‣ 6 Ablations ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains"), larger or more capable LLMs generally produce more effective rubrics, with GPT-4o yielding the best performance among reference-free models. However, all remain below the performance of rubrics generated with reference guidance (e.g., O3-mini with access to reference answers). Additionally, model attributes such as instruction tuning and reasoning capabilities play a key role in the effectiveness of rubric generation.

Table 4: Policy performance on HealthBench-1k when trained with GRPO using rubrics generated by different LLMs *without* reference answers. GPT-4o-generated rubrics yield the strongest performance, though they still fall short of rubrics generated with expert (reference-guided) supervision. Smaller aligned models (e.g., GPT-4o-mini, O3-mini) remain competitive with larger open-weight models, underscoring the importance of alignment and reasoning ability in rubric generation.

## 7 Related Work

#### RLVR across domains

Reinforcement learning with verifiable rewards (RLVR) is quickly extending its reach well beyond math and code. General-Reasoner trains on a 200 k mixed corpus-physics, finance, policy, and more-and reports a ten-point jump on MMLU-Pro after GRPO fine-tuning Ma et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib19)). A follow-up study extends RLVR to medicine, chemistry, psychology, and economics, showing that a single cross-domain reward model can supervise all four areas without task-specific tweaks Su et al. ([2025a](https://arxiv.org/html/2507.17746v1#bib.bib28)). Focusing on healthcare, Med-RLVR applies the same recipe to multiple-choice clinical QA, gaining eight accuracy points over supervised baselines while eliciting chain-of-thought reasoning from a 3B-parameter base model Zhang et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib34)). These studies collectively show promising progress in taking RL beyond math and code, yet sparse reward signals, unreliable verifiers, and limited benchmark coverage remain open challenges.

#### Rubric-based Evaluation

Concise, task-specific rubrics are now standard for evaluating frontier LLMs on open-ended benchmarks (Arora et al., [2025](https://arxiv.org/html/2507.17746v1#bib.bib2); Ruan et al., [2025](https://arxiv.org/html/2507.17746v1#bib.bib24); Hashemi et al., [2024](https://arxiv.org/html/2507.17746v1#bib.bib12); Pathak et al., [2025](https://arxiv.org/html/2507.17746v1#bib.bib22)). Pathak et al. show that rubric-prompted GPT-4 graders are more accurate and consistent than a single question-agnostic checklist (Pathak et al., [2025](https://arxiv.org/html/2507.17746v1#bib.bib22)), yet their rubrics appear only at evaluation time, not in training. HealthBench extends the idea to medicine, pairing 48 k clinician-written criteria with GPT-4 judges to score factuality, safety, and empathy (Arora et al., [2025](https://arxiv.org/html/2507.17746v1#bib.bib2)). Moving from evaluation to tuning, Configurable Preference Tuning (CPT) synthesizes rubric-conditioned preference pairs for DPO fine-tuning (Gallego, [2025](https://arxiv.org/html/2507.17746v1#bib.bib7)). None of these approaches, however, integrates rubrics with verifiable rewards. Rubrics are used only to grade held-out outputs or to generate preference pairs.

#### Learning from feedback signals

RLHF tunes LLMs with thousands of human preference comparisons, but these subjective labels introduce noise and invite reward hacking (Ouyang et al., [2022](https://arxiv.org/html/2507.17746v1#bib.bib21)). Reinforcement learning with verifiable rewards (RLVR) alleviates these issues by relying on programmatic checks—ranging from exact string matches on GSM8K and MATH to mixed-domain verifiers in General-Reasoner and Cross-Domain RLVR Ma et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib19)); Su et al. ([2025a](https://arxiv.org/html/2507.17746v1#bib.bib28)). Although the resulting signals are low-variance and fully automatic, they can be sparse. Process supervision provides more detailed feedback by rewarding intermediate reasoning steps. MCTS-generated labels and generative reward models such as ThinkPRM improve performance, but at a significant annotation cost (Li et al., [2025](https://arxiv.org/html/2507.17746v1#bib.bib17); Khalifa et al., [2025](https://arxiv.org/html/2507.17746v1#bib.bib15)). Our rubric based RLVR closes this gap by turning rubric criteria into structured verifiers and using their scalar scores as dense rewards in on-policy RLVR training.

## 8 Future Work

#### Interpretability and Reward Robustness

RaR offers a transparent alternative to black-box reward models by explicitly optimizing against human-interpretable rubric criteria. Unlike neural reward models or preference-based methods such as DPO, RaR enables auditability and objective attribution of reward signals. This transparency may also increase robustness to reward hacking, as discrete, interpretable criteria are harder for models to exploit than opaque learned scores.

Future work can explore formal evaluations of RaR’s resilience to reward hacking, including adversarial training scenarios where models attempt to game individual rubric components.

#### Extending to Real-World Domains and Use Cases

Rubric-guided post-training has been underexplored in open-ended or agentic tasks. A promising direction is expanding RaR to domains with subjective or multi-step goals such as tool use, reasoning under uncertainty, or real-world decision support-where rubrics can provide structured, task-specific guidance.

#### Rubrics as Curriculum

Rubrics naturally encode hierarchical task structure—from essential facts to optional stylistic preferences—which can support implicit curriculum learning. Early in training, models may only satisfy simpler criteria; as learning progresses, more complex targets become attainable. Future work can investigate dynamic weighting or staged introduction of rubric items to further leverage this curriculum effect.

## 9 Conclusion

We introduced Rubrics as Rewards (RaR), a framework for post-training language models using structured, checklist-style rubrics as reward signals. By decomposing response evaluation into transparent, multi-criteria objectives—both subjective and objective—RaR provides a modular and interpretable alternative to preference-based methods. Our experiments demonstrate that rubric-guided training achieves strong performance across domains, significantly outperforming Likert-based baselines and matching or exceeding the performance of reference-based reward generation. Additionally, we show that RaR improves alignment with human preferences while reducing dependence on large judge models.

## Limitations

Our study is limited to two domains (medical and science), and further validation is needed to assess generalizability to other tasks, such as open-ended dialogue. We explore only two reward aggregation strategies—implicit and explicit—and do not investigate alternative weighting schemes. Additionally, we do not conduct controlled analyses of reward hacking risks. Finally, our judges are off-the-shelf LLMs; future work could explore dedicated evaluators with stronger reasoning capabilities.

## Acknowledgments

We thank Qin Lyu, Nikhil Barhate, and Zijian Hu for supporting this research through the development of the in-house post-training platform RLXF. We also thank Robert Vacareanu for valuable early feedback and discussions.

## References

-   Anugraha et al. (2025) David Anugraha, Zilu Tang, Lester James V Miranda, Hanyang Zhao, Mohammad Rifqi Farhansyah, Garry Kuwanto, Derry Wijaya, and Genta Indra Winata. 2025. R3: Robust rubric-agnostic reward models. *arXiv preprint arXiv:2505.13388*.
-   Arora et al. (2025) Rahul K Arora, Jason Wei, Rebecca Soskin Hicks, Preston Bowman, Joaquin Quiñonero-Candela, Foivos Tsimpourlas, Michael Sharman, Meghan Shah, Andrea Vallone, Alex Beutel, et al. 2025. Healthbench: Evaluating large language models towards improved human health. *arXiv preprint arXiv:2505.08775*.
-   Chen et al. (2024a) Junying Chen, Zhenyang Cai, Ke Ji, Xidong Wang, Wanlong Liu, Rongsheng Wang, Jianye Hou, and Benyou Wang. 2024a. Huatuogpt-o1, towards medical complex reasoning with llms. *arXiv preprint arXiv:2412.18925*.
-   Chen et al. (2024b) Lichang Chen, Chen Zhu, Davit Soselia, Jiuhai Chen, Tianyi Zhou, Tom Goldstein, Heng Huang, Mohammad Shoeybi, and Bryan Catanzaro. 2024b. Odin: Disentangled reward mitigates hacking in rlhf. *arXiv preprint arXiv:2402.07319*.
-   Chen et al. (2025) Xiusi Chen, Gaotang Li, Ziqi Wang, Bowen Jin, Cheng Qian, Yu Wang, Hongru Wang, Yu Zhang, Denghui Zhang, Tong Zhang, et al. 2025. Rm-r1: Reward modeling as reasoning. *arXiv preprint arXiv:2505.02387*.
-   Cui et al. (2025) Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. 2025. Process reinforcement through implicit rewards. *arXiv preprint arXiv:2502.01456*.
-   Gallego (2025) Víctor Gallego. 2025. Configurable preference tuning with rubric-guided synthetic data. *arXiv preprint arXiv:2506.11702*.
-   General Reasoning (2025) General Reasoning. 2025. [General reasoning](https://gr.inc/).
-   Gudibande et al. (2023) Arnav Gudibande, Eric Wallace, Charlie Snell, Xinyang Geng, Hao Liu, Pieter Abbeel, Sergey Levine, and Dawn Song. 2023. The false promise of imitating proprietary llms. *arXiv preprint arXiv:2305.15717*.
-   Guo et al. (2025a) Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. 2025a. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. *arXiv preprint arXiv:2501.12948*.
-   Guo et al. (2025b) Jiaxin Guo, Zewen Chi, Li Dong, Qingxiu Dong, Xun Wu, Shaohan Huang, and Furu Wei. 2025b. Reward reasoning model. *arXiv preprint arXiv:2505.14674*.
-   Hashemi et al. (2024) Helia Hashemi, Jason Eisner, Corby Rosset, Benjamin Van Durme, and Chris Kedzie. 2024. Llm-rubric: A multidimensional, calibrated approach to automated evaluation of natural language texts. *arXiv preprint arXiv:2501.00274*.
-   Hurst et al. (2024) Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. 2024. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*.
-   Jaech et al. (2024) Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. 2024. Openai o1 system card. *arXiv preprint arXiv:2412.16720*.
-   Khalifa et al. (2025) Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, and Lu Wang. 2025. Process reward models that think. *arXiv preprint arXiv:2504.16828*.
-   Lambert et al. (2024) Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James V Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, et al. 2024. T\\\\backslash" ulu 3: Pushing frontiers in open language model post-training. *arXiv preprint arXiv:2411.15124*.
-   Li et al. (2025) Shuangtao Li, Shuaihao Dong, Kexin Luan, Xinhan Di, and Chaofan Ding. 2025. Enhancing reasoning through process supervision with monte carlo tree search. *arXiv preprint arXiv:2501.01478*.
-   Lu et al. (2025) Dakuan Lu, Xiaoyu Tan, Rui Xu, Tianchu Yao, Chao Qu, Wei Chu, Yinghui Xu, and Yuan Qi. 2025. Scp-116k: A high-quality problem-solution dataset and a generalized pipeline for automated extraction in the higher education science domain. *arXiv preprint arXiv:2501.15587*.
-   Ma et al. (2025) Xueguang Ma, Qian Liu, Dongfu Jiang, Ge Zhang, Zejun Ma, and Wenhu Chen. 2025. General-reasoner: Advancing llm reasoning across all domains. *arXiv preprint arXiv:2505.14652*.
-   OpenAI o3-mini (2025) OpenAI o3-mini. 2025. [Openai o3-min](https://openai.com/index/openai-o3-mini/).
-   Ouyang et al. (2022) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. 2022. Training language models to follow instructions with human feedback. *Advances in neural information processing systems*, 35:27730–27744.
-   Pathak et al. (2025) Aditya Pathak, Rachit Gandhi, Vaibhav Uttam, Yashwanth Nakka, Aaryan Raj Jindal, Pratyush Ghosh, Arnav Ramamoorthy, Shreyash Verma, Aditya Mittal, Aashna Ased, et al. 2025. Rubric is all you need: Enhancing llm-based code evaluation with question-specific rubrics. *arXiv preprint arXiv:2503.23989*.
-   Rein et al. (2024) David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R Bowman. 2024. Gpqa: A graduate-level google-proof q&a benchmark. In *First Conference on Language Modeling*.
-   Ruan et al. (2025) Jie Ruan, Inderjeet Nair, Shuyang Cao, Amy Liu, Sheza Munir, Micah Pollens-Dempsey, Tiffany Chiang, Lucy Kates, Nicholas David, Sihan Chen, et al. 2025. Expertlongbench: Benchmarking language models on expert-level long-form generation tasks with structured checklists. *arXiv preprint arXiv:2506.01241*.
-   Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. 2024. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*.
-   Singhal et al. (2023) Prasann Singhal, Tanya Goyal, Jiacheng Xu, and Greg Durrett. 2023. A long way to go: Investigating length correlations in rlhf. *arXiv preprint arXiv:2310.03716*.
-   Sirdeshmukh et al. (2025) Ved Sirdeshmukh, Kaustubh Deshpande, Johannes Mols, Lifeng Jin, Ed-Yeremai Cardona, Dean Lee, Jeremy Kritz, Willow Primack, Summer Yue, and Chen Xing. 2025. Multichallenge: A realistic multi-turn conversation evaluation benchmark challenging to frontier llms. *arXiv preprint arXiv:2501.17399*.
-   Su et al. (2025a) Yi Su, Dian Yu, Linfeng Song, Juntao Li, Haitao Mi, Zhaopeng Tu, Min Zhang, and Dong Yu. 2025a. Crossing the reward bridge: Expanding rl with verifiable rewards across diverse domains. *arXiv preprint arXiv:2503.23829*.
-   Su et al. (2025b) Yi Su, Dian Yu, Linfeng Song, Juntao Li, Haitao Mi, Zhaopeng Tu, Min Zhang, and Dong Yu. 2025b. Expanding rl with verifiable rewards across diverse domains. *arXiv preprint arXiv:2503.23829*.
-   Wang et al. (2024) Haoxiang Wang, Yong Lin, Wei Xiong, Rui Yang, Shizhe Diao, Shuang Qiu, Han Zhao, and Tong Zhang. 2024. Arithmetic control of llms for diverse user preferences: Directional preference alignment with multi-objective rewards. *arXiv preprint arXiv:2402.18571*.
-   Whitehouse et al. (2025) Chenxi Whitehouse, Tianlu Wang, Ping Yu, Xian Li, Jason Weston, Ilia Kulikov, and Swarnadeep Saha. 2025. J1: Incentivizing thinking in llm-as-a-judge via reinforcement learning. *arXiv preprint arXiv:2505.10320*.
-   Ye et al. (2024) Zihuiwen Ye, Fraser Greenlee-Scott, Max Bartolo, Phil Blunsom, Jon Ander Campos, and Matthias Gallé. 2024. Improving reward models with synthetic critiques. *arXiv preprint arXiv:2405.20850*.
-   Yuan et al. (2025) Weizhe Yuan, Jane Yu, Song Jiang, Karthik Padthe, Yang Li, Ilia Kulikov, Kyunghyun Cho, Dong Wang, Yuandong Tian, Jason E Weston, et al. 2025. Naturalreasoning: Reasoning in the wild with 2.8 m challenging questions. *arXiv preprint arXiv:2502.13124*.
-   Zhang et al. (2025) Sheng Zhang, Qianchu Liu, Guanghui Qin, Tristan Naumann, and Hoifung Poon. 2025. Med-rlvr: Emerging medical reasoning from a 3b base model via reinforcement learning. *arXiv preprint arXiv:2502.19655*.
-   Zhao et al. (2025) Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, and Dawn Song. 2025. Learning to reason without external rewards. *arXiv preprint arXiv:2505.19590*.

## Appendix A Training dataset breakdown

In this section, we show the topic distribution breakdown of the medicine and science training dataset and the rubric type distribution breakdown for the corresponding dataset.

### A.1 Medicine training dataset - Overall Data Distribution

Table 5: Aggregate statistics for the full medical (train and validation) dataset.

Table 6: Rubric-type distribution across all 20,166 examples.

Table 7: Distribution of topics in the medical training and validation dataset

### A.2 STEM Dataset - Overall Data Distribution

Table 8: Aggregate statistics for the full medical (train and validation) dataset.

Table 9: Rubric‐type distribution across all 20 625 examples.

Table 10: Distribution of topics in the STEM training and validation dataset

## Appendix B Synthetic Preference Set Generation

We leverage the publicly-released HealthBench Arora et al. ([2025](https://arxiv.org/html/2507.17746v1#bib.bib2)) corpus, which contains 5,000 health-related prompts accompanied by expert-written answers. Of these, 4,203 datapoints already include an *ideal* completion vetted by licensed clinicians. For every such prompt–ideal pair we automatically generate a *perturbed* counterpart using o3 with the structured template shown below. The template forces the model to (i) spell out a \[reasoning\] plan for degrading quality, (ii) emit the degraded \[perturbed\_completion\], and (iii) log exact \[chunks\_added\] and \[chunks\_removed\]. Perturbations are accepted only after manual screening confirms that they are *objectively worse*, along at least one axis of medical accuracy, completeness, clarity, safety, specificity, structure, or tone, while remaining coherent and free of dangerous advice. This procedure produces a balanced evaluation set of 4,203 preferred and 4,203 perturbed responses (8,406 total), which we use in the rubric-versus-Likert experiments in Section [5](https://arxiv.org/html/2507.17746v1#S5 "5 Results ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains").

## Appendix C Judge Quality impacts on Post-training

We assess whether rubric-guided evaluation improves judge effectiveness compared to rubric-free Likert scoring when used for GRPO training. Table [11](https://arxiv.org/html/2507.17746v1#A3.T11 "Table 11 ‣ Appendix C Judge Quality impacts on Post-training ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains") reports judge accuracy on synthetic medical data, with all policies trained using Qwen2.5-7B and varying judge models.

Table 11: Judge quality comparison: rubric-based evaluation vs pure Likert scoring on synthetic medical rubrics.

Rubric-based evaluation consistently yields stronger policies across all judge sizes. The most pronounced improvement appears with Qwen-7B-Instruct (+0.047), where rubric guidance lifts it from weakest to nearly matching larger models. Additionally, rubric-based scores are more tightly clustered (0.250–0.279) than those from Likert-only judges (0.220–0.254), indicating improved consistency.

These results suggest that rubrics help smaller judges approximate high-quality supervision by breaking evaluation into interpretable, binary criteria. This structured approach mitigates scale-related limitations, enabling more reliable reward modeling even with limited-capacity evaluators.

## Appendix D Training Details

The training hyperparameters are described in Table [12](https://arxiv.org/html/2507.17746v1#A4.T12 "Table 12 ‣ Appendix D Training Details ‣ Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains").

Table 12: GRPO hyperparameter settings for Medical and Science domains.

## Appendix E LLM-Judge Prompts

## Appendix F Evaluation Prompts

## Appendix G Predefined Rubrics

## Appendix H Synthetic Rubric Generation Prompts

## Appendix I Perturbed Dataset Generation