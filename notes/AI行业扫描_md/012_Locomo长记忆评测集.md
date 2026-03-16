---
url: https://snap-research.github.io/locomo/
title: "Evaluating Very Long-Term Conversational Memory of LLM Agents"
description: "Evaluating Very Long-Term Conversational Memory of LLM Agents"
captured_at: "2026-03-09T03:07:59.243Z"
---

# Evaluating Very Long-Term Conversational Memory of LLM Agents

1UNC Chapel Hill 2University of Southern California 3Snap Inc. †Equal advising

![Logo](https://snap-research.github.io/locomo/static/images/evaluation_framework.svg)

## **Overview of our evaluation framework.** We propose three tasks: question answering, event summarization and multimodal dialog generation to evaluate models' comprehension in very long-term dialogues.

## Motivation

Existing works on long-term open-domain dialogues focus on evaluating model responses within contexts spanning no more than five chat sessions.

We introduce a machine-human pipeline to generate high-quality, very long-term dialogues by leveraging LLM-based agent architectures and grounding their dialogues on personas and temporal event graphs. Moreover, we equip each agent with the capability of sharing and reacting to images. The generated conversations are verified and edited by human annotators for long-range consistency and grounding to the event graphs. Using this pipeline, we collect LoCoMo, a dataset of very long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions.

Based on LOCOMO, we present a comprehensive evaluation benchmark to measure long-term memory in models, encompassing question answering, event summarization, and multi-modal dialogue generation tasks.

## How do we generate *very* long-term conversations?

![Intro](https://snap-research.github.io/locomo/static/images/intro_figure_conv_only_v2.svg)

An example of a conversation in LoCoMo is shown to the right.

-   We create two **virtual agents**, each initialized with a LLM.
-   To start, unique **persona statements** are assigned to each agent, ensuring the integration of distinct personalities into their dialogues.
-   To mirror real-life experiences, we create a **temporal event graph** for each agent, which illustrates a realistic sequence of life events.
-   The LLM **agent architecture** is utilized for each agent, enabling them to effectively memorize and reflect conversation history into ongoing dialogues.
-   Further, each agent can share coherent images, thereby enhancing the **multi-modal dialogue** aspect.
-   Finally, human annotators are tasked with **manually filtering and refining** the generated data.

![Logo](https://snap-research.github.io/locomo/static/images/main_v4.svg)

## **Overview of the generative pipeline for LoCoMo.** Each LLM agent is assigned a distinct persona and a timeline of causally connected events in their file. The agent is equipped with a memory and reflection module to retrieve relevant history for dialog generation and is also enabled for image-sharing and image-reaction behaviors (left). The generated conversations are edited by human annotators to maintain long-range consistency (right).

![Logo](https://snap-research.github.io/locomo/static/images/events.svg)

## **Temporal Event Graph Creation.** Each event is generated in accordance with the specified persona p and causal connections l between events are depicted to illustrate the casual relationships among them.

## Evaluation Framework

In this study, we present a holistic evaluation framework to assess an agent’s proficiency in managing and responding within long-term contexts.

-   **Question Answering.** Agents need to “recall” past context correctly to integrate relevant information into future responses. We present a direct examination of their memory via a question answering task. We classify questions into five distinct reasoning types to evaluate memory from multiple perspectives: *single-hop*, *multi-hop*, *temporal*, *commonsense or world knowledge*, and *adversarial*.
-   **Event Graph Summarization.** Agents also need to recognize long-range causal and temporal connections in the dialogues to generate empathetic and relevant responses. We propose a measurement of their causal and temporal understanding with an event graph summarization task where the event graphs linked to each LLM speaker serve as the correct answers, and models are tasked with extracting this information from the conversation history.
-   **Multi-modal Dialog Generation.** Conversational agents need to utilize relevant context recalled from past conversations to generate responses that are consistent with the ongoing narrative. We assess this ability via the multi-modal dialog generation task.

## Findings

We present extensive experimental results on the LoCoMo benchmark using instruction-based LLMs, long-context LLMs, and RAG techniques. Our findings include:

-   **Long-context LLMs and RAG demonstrate effectiveness in QA tasks** , improving ‘memory’ capabilities of LLMs (with improvements ranging from 22-66%), but still significantly lag behind human levels (by 56%), especially in temporal reasoning, (by 73%);
-   **Long-context LLMs demonstrate significant hallucinations**, leading to difficulty with adversarial questions in the QA task and in the event graph summarization task.
-   **RAG offers a balanced compromise**, combining the accuracy of short-context LLMs with the extensive comprehension of wide-context LLMs, and does particularly well when dialogues are transformed into a database of assertions (observations) about each speaker’s life and persona.

![Logo](https://snap-research.github.io/locomo/static/images/tables.svg)

## **Question answering performance of Base, Long-context and RAG models.** Optimal performance is in bold. Results are based on F1-score for answer prediction; higher is better.

![Logo](https://snap-research.github.io/locomo/static/images/minigpt5_results.svg)

## **Multimodal dialog generation performance of MiniGPT-5**. (A) an example of multimodal dialog predicted using MiniGPT5 with and without observation as retrieved context, (B) Variation of MM-Relevance score with length of dialog history, and (C) comparison of RAG-based MiniGPT-5 methods.

## BibTeX

```
@article{maharana2024lococmo,
  author    = {Maharana, Adyasha and Lee, Dong-Ho and Tulyakov, Sergey and Bansal, Mohit and Barbieri, Francesco and Fang, Yuwei},
  title     = {Evaluating Very Long-Term Conversational Memory of LLM Agents.},
  journal   = {arxiv},
  year      = {2024},
}
```