---
url: https://yaofu.notion.site/How-Do-Language-Models-put-Attention-Weights-over-Long-Context-10250219d5ce42e8b465087c383a034e
title: "How Do Language Models put Attention Weights over Long Context?"
description: "A tool that connects everyday work into one space. It gives you and your teams AI tools—search, writing, note-taking—inside an all-in-one, flexible workspace."
author: "Yao Fu"
captured_at: "2026-03-08T11:42:41.005Z"
---

# How Do Language Models put Attention Weights over Long Context?

Released on Mar 05 2024

Update Mar 15 2024: Check the recent [DMC](https://arxiv.org/abs/2403.09636) paper which implement the compression closely related to our analysis.

We are interested in the problem of lossless KV cache compression: to make the KV cache take less memory without sacrifacing language model’s capability during inference. Just like lossless data compression is the number one principle for scaling, we view lossless KV cache compression as the number one challenge for democratizing and deployting long-context (100K - 10M) language models in real world, simply because they are too large.

But sorry, we won’t discuss any techniques related to KV cache compression in this post ![😅](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==). Instead, we look at its pre-requisition, i.e., the attention patterns inside the transformer architecture, because only an in-depth understanding of the attention mechanism allows us to find out which KV cache is compressible and which is not.

In this post, we discuss six typical attention patterns over long-context input, across all the transformer layers and heads, aiming to provide an intuitive understanding of what’s happening inside the transformer long-context attention, and potentially identify what part of KV cache is compressible.

Cite this work

Table of Content

Say you do Needle-in-a-Haystack. Your input is a document of 100K length and in the middle, there is a sentence “The best thing to do in San Francisco is sitting in Dolores park and eating a sandwidth in a sunny day”. Your prompt is “The best thing to do in San Francisco is”. Then you want to see if your model can retrieve the needle “sitting in Dolores park and eating a sandwidth in a sunny day”. When the model generates the response, what does its attention over 100k input look like?

We perform this experiment on our recently release [LLaMA-2-7B-80K checkpoint](https://github.com/FranxYao/Long-Context-Data-Engineering) and retrieve its attention tensor. An attention tensor has three dimentions / ranks: depth, heads, and context length, as is shown below:

![](https://yaofu.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F281b3c78-d734-43fb-aa33-707babff9463%2F901d4e1f-0c7a-4874-b4a5-6798ca066353%2FUntitled.png?table=block&id=94ad03ea-27c1-4f68-a7b5-dfd560ee4687&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1420&userId=&cache=v2)

Depth: LLaMA-2 7B has 32 layers in total. Each layer has its own attention

Heads: At each layer, there are 32 attention heads

Context length: the input document has 50K tokens, so we have 32 layers \* 32 heads attention distribution over 50K tokens

We first note that the attention distribution in layer 0, 1 and 31 are quite different than the attention within layers 2 - 30.

Layer 0 and layer 1: mostly uniform

Layer 0 is just word embedding. Layer 1 is one-layer mixture of word embeddings.

The attentions on layer 0 and layer 1 are mostly uniform: the model put approximately equal probability mass over the whole 100K context

Layer 2 - 30: attention sink, recency bias, scattered over middle, or concentrated on middle

Starting from layer 2, the geometry of the QKV vectors become significantly different than word embeddings (layer 0 and 1).

We see different modes of attention in these layers. Most of the heads exhibit a “V-shaped” attention where most of the probability mass is put on the initial tokens (aka attention sinks) and the recent/ last tokens (aka the recency bias). There are also fewer heads that put the attention mass on sink token only, or recent token only.

There are few interesting heads exhibit the two attention patterns:

Scattered over middle, where some top K middle tokens, say 256, that randomly scatters over the input, receives most of the attention mass.

Concentrated in middle, where only few middle tokens, say 2, receives most of the attention mass.

Layer 31: the combination of all above

The 32 heads of the last layer can exhibit all of the attention patterns mentioned above.

First few tokens: attention sink

The attention sink means in some layers and some heads, most of the attention mass is put on the initial tokens.

Early works in 2020 like [BigBird](https://arxiv.org/abs/2007.14062) discusses this type of attention pattern. Recent works in 2023 like [StreamingLLM](https://github.com/mit-han-lab/streaming-llm) study this problem in detail.

Middle tokens: lost-in-the middle?

We will show that many attention heads do not attend to middle tokens, but a few heads do

Maybe [lost in the middle](https://arxiv.org/abs/2307.03172) problem where a head should have attended to a middle token, but didn’t

Recent tokens: the classical recency bias

Human language (and many other sequential data) has intrinsic recency bias, and recent words typically, but not always, have the strongest capability to predict next words

We discuss six attention patterns across all layers. In layer 0 and layer 1, most (or all) of the attention heads follow a uniform distribution. In layer 2-30, many attention heads follow a V-shaped pattern, where most of the attention mass is put on the first and last few tokens. Yet there are also some other heads exihibit more interesting patterns, such as scattered over the middle, or concentrated on the middle. We do not observe uniform distribution in layer 2-30. Finally, in layer 31, the last layer, all of the attention patterns can be observed.

![](https://yaofu.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F281b3c78-d734-43fb-aa33-707babff9463%2Fa20a56c2-9028-4182-8515-e417f5a89a1c%2FUntitled.png?table=block&id=9562d9fe-0b3f-4515-9fe9-c58e6898a2d0&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1150&userId=&cache=v2)

Layer 5, head 20, the attention follows a V-shaped pattern. Entropy = 2.53

This is the most common attention pattern in layers 2 - 30

63.2% probability is put on the attention sink, 33.7% is put on the recent tokens

The 3.1% probability mass feels like a small number, so maybe the kv cache of this part can be removed.

![](https://yaofu.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F281b3c78-d734-43fb-aa33-707babff9463%2F0d38fc0e-cd81-4e4b-80df-f3ad683e2614%2FUntitled.png?table=block&id=1dff9fbb-7cc2-4252-943a-19b178682bb7&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=860&userId=&cache=v2)

Layer 12, head 23. The attention sink pattern. Entropy = 0.98

This pattern exist in few heads within layer 2-31

96.9% of the attention probability are most on the attention sink.

3.08% of the attention mass is on the recent tokens, but I’m not sure if this is a significant number of not

Only 0.02% of the attention mass is on the middle tokens. This feels negligible.

Usually the attention sink tokens do not have very strong correlation with the current context, so I strongly feel heads of this attention patterns can be highly compressed, or simply removed.

![](https://yaofu.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F281b3c78-d734-43fb-aa33-707babff9463%2Ff08b5b6e-a10f-4601-8e97-29a9edf6a016%2FUntitled.png?table=block&id=667ab053-69b5-4ef8-abd0-221ee3e768ff&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=860&userId=&cache=v2)

Layer 5, head 15. The recency bias pattern. Entropy = 0.09

This pattern exist in few heads within layer 2-31

99.6% of the attention mass is concentrated on the recent tokens

I feel that the kv cache of this type of heads can be simply removed.

![](https://yaofu.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F281b3c78-d734-43fb-aa33-707babff9463%2F1323cf8f-8f57-4e73-9a19-2b7ecda4303d%2FUntitled.png?table=block&id=8365e138-cab1-4396-b188-0f3d83abcd0a&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1250&userId=&cache=v2)

Layer 11, head 2. The probability mass is scattered over multiple tokens in the middle. Entropy = 6.43

This pattern exist in few heads within layer 2-31

The middle tokens, in total, takes 86.5% of the probability, where the topK (K = 256) tokens take 55.5 — approximately each token takes 0.2%, so it’s fair to say “scattered”

![](https://yaofu.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F281b3c78-d734-43fb-aa33-707babff9463%2F4a46d22c-0449-44e0-b881-25b044596f66%2FUntitled.png?table=block&id=88d59cd9-5f94-4af4-a177-e1cf693d48e7&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=860&userId=&cache=v2)

Layer 11, head 14. The probability mass is concentrated on very few tokens in the middle. Entropy = 1.32 (approximately correspond to a uniform distribution over 4 tokens)

This pattern exist in few heads within layer 2-31

The attended tokens must be very important for this head to do its work.

The difference between this pattern and the previous “scattered over the middle” is, the above one scatter the attention mass over hundreds of tokens, this pattern concentrates the attention mass on less than 10 tokens.

![](https://yaofu.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F281b3c78-d734-43fb-aa33-707babff9463%2Fa36935c8-a4e2-4916-8657-d55e7731c67a%2FUntitled.png?table=block&id=3b090456-a0d6-4e27-b269-90860593b233&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1060&userId=&cache=v2)

Layer 0, head 5, a uniform distribution over all tokens. Entropy = 10.6

Most (or all) of the heads in layer 0 and layer 1 follow this pattern. Note that this observation is clearly different than the observations on layer 2 - 31.

Probably the kv cache on these two layers are not compressible.

<table><tbody><tr><td dir="ltr"><div><p><span data-token-index="0">Layer</span></p></div></td><td dir="ltr"><div><p><span data-token-index="0">Pattern</span></p></div></td><td dir="ltr"><div><p><span data-token-index="0">Frequency</span></p></div></td><td dir="ltr"><div><p><span data-token-index="0">Entropy</span></p></div></td><td dir="ltr"><div><p><span data-token-index="0">Mass over top</span></p></div></td><td dir="ltr"><div><p><span data-token-index="0">Compressible?</span></p></div></td></tr><tr><td dir="ltr"><div><p>0-1</p></div></td><td dir="ltr"><div><p>Uniform</p></div></td><td dir="ltr"><div><p>All heads</p></div></td><td dir="ltr"><div><p>10.+</p></div></td><td dir="ltr"><div><p>50K tokens</p></div></td><td dir="ltr"><div><p>No</p></div></td></tr><tr><td dir="ltr"><div><p>2-30</p></div></td><td dir="ltr"><div><p>V-shaped</p></div></td><td dir="ltr"><div><p>Many heads</p></div></td><td dir="ltr"><div><p>2.+</p></div></td><td dir="ltr"><div><p>16 tokens</p></div></td><td dir="ltr"><div><p>Middle tokens</p></div></td></tr><tr><td dir="ltr"></td><td dir="ltr"><div><p>Sink</p></div></td><td dir="ltr"><div><p>few heads</p></div></td><td dir="ltr"><div><p>&lt;1.0</p></div></td><td dir="ltr"><div><p>3 tokens</p></div></td><td dir="ltr"><div><p>Most tokens except sink</p></div></td></tr><tr><td dir="ltr"></td><td dir="ltr"><div><p>Recency</p></div></td><td dir="ltr"><div><p>few heads</p></div></td><td dir="ltr"><div><p>&lt;1.0</p></div></td><td dir="ltr"><div><p>3 tokens</p></div></td><td dir="ltr"><div><p>Most tokens except recent</p></div></td></tr><tr><td dir="ltr"></td><td dir="ltr"><div><p>Scatterd over many</p></div></td><td dir="ltr"><div><p>few heads</p></div></td><td dir="ltr"><div><p>3.0 - 8.0</p></div></td><td dir="ltr"><div><p>16 - 4K tokens</p></div></td><td dir="ltr"><div><p>Hard to say</p></div></td></tr><tr><td dir="ltr"></td><td dir="ltr"><div><p>Concentrated on few</p></div></td><td dir="ltr"><div><p>few heads</p></div></td><td dir="ltr"><div><p>&lt; 2.0</p></div></td><td dir="ltr"><div><p>8 tokens</p></div></td><td dir="ltr"><div><p>If only we can identify the important tokens</p></div></td></tr><tr><td dir="ltr"><div><p>31</p></div></td><td dir="ltr"><div><p>All of above</p></div></td><td dir="ltr"></td><td dir="ltr"></td><td dir="ltr"></td><td dir="ltr"></td></tr></tbody></table>

Update on Mar 15:

The recent [DMC paper](https://arxiv.org/pdf/2403.09636.pdf) achieves the compresison pattern exactly as our analysis above:

![](https://yaofu.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F281b3c78-d734-43fb-aa33-707babff9463%2Fe0a6df1d-6b64-4289-98bd-00bd6d4d3dbc%2FUntitled.png?table=block&id=7bc9f310-ff77-45e6-99c6-893b110a67b9&spaceId=281b3c78-d734-43fb-aa33-707babff9463&width=1150&userId=&cache=v2)

Side note: use mass over topK tokens to interprete entropy

What does entropy = 3.+ mean? Think about equivalent uniform distribution

Suppose my probability mass is uniformly distributed over top 4 tokens, the rest of the tokens take 0 probability, then the entropy is log(4) = 1.38

Suppose my probability mass is uniformly distributed over top 256 tokens, then the entropy is log(256) = 5.54

If a discrete distribution has entropy 5.54, then one my approximately view it similar to the situation where the top 256 of its token take most of the probability mass

Or interpret it as approximately similar to a uniform distribution over the top 256 tokens

<table><tbody><tr><td dir="ltr"><div><p><span data-token-index="0">Entropy</span></p></div></td><td dir="ltr"><div><p><span data-token-index="0">Approximately uniform over</span></p></div></td></tr><tr><td dir="ltr"><div><p>1.38</p></div></td><td dir="ltr"><div><p>4 tokens</p></div></td></tr><tr><td dir="ltr"><div><p>2.77</p></div></td><td dir="ltr"><div><p>16 tokens</p></div></td></tr><tr><td dir="ltr"><div><p>4.85</p></div></td><td dir="ltr"><div><p>128 tokens</p></div></td></tr><tr><td dir="ltr"><div><p>5.54</p></div></td><td dir="ltr"><div><p>256 tokens</p></div></td></tr><tr><td dir="ltr"><div><p>6.93</p></div></td><td dir="ltr"><div><p>1K tokens</p></div></td></tr><tr><td dir="ltr"><div><p>8.31</p></div></td><td dir="ltr"><div><p>4K tokens</p></div></td></tr><tr><td dir="ltr"><div><p>10.81</p></div></td><td dir="ltr"><div><p>50K tokens</p></div></td></tr></tbody></table>

Non-compressible

I tend to believe attention heads of uniform distributions may not be compressed

For the scattered-over-many pattern, I feel like it is also hard to do KV cache compression.

Compressible

When attention is highly concentrated on tokens that can be identified easily, the kv cache corresponding to the rest of tokens may be compressed.

Wait but is a 1% attention weight really in-significant?

We don’t know.

Given the sensitivity of the language models, it is totally possible that although a token only occupies 1% of the attention mass, it may still play a significant role in terms of next-word prediction

Wait you missed the value vector

Yes indeed.

Imagine you have one token whose value vector’s norm is 100x of other tokens, so even this token only receives 1% of the attention weight, it still has a significant influence on the output vector.

Currently, we are actively research methods for compressing the kv cache and understanding the attention mechanism. We welcome comments, pointers to existing works, criticism on our limitations, and all related topics. So if you are interested in this direction, please definitely get in touch!