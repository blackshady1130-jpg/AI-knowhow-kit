# Scaling Laws, Honestly

**副标题：** TL;DR: The original scaling laws were wrong due to a bug

**作者：** Diogo  
**发布时间：** Jul 04, 2026  
**来源：** Complete Skeptic (Substack)  
**原文链接：** [https://www.completeskeptic.com/p/scaling-laws-honestly](https://www.completeskeptic.com/p/scaling-laws-honestly)

---

## Background

Scaling laws were one of OpenAI's most important results, both technically and philosophically (so much so that being *scaling-pilled* became a thing). They allow us to predict results for ever larger language model runs, and also allow for debugging models as we use exponentially more resources. All of this led to the era of LLMs we're in today, but the craziest part was… the original Kaplan et al scaling laws were wrong.

Recently, Lilian Weng posted another awesome (and highly recommended) [blog post on scaling laws](https://lilianweng.github.io/posts/2026-06-24-scaling-laws/). I was extra excited about the section "Reconciling Kaplan and Chinchilla", the former being [OpenAI's original scaling laws](https://arxiv.org/abs/2001.08361) and the latter being [DeepMind's follow-up](https://arxiv.org/abs/2203.15556) with completely different scaling laws.

> Figure 1 from Chinchilla. The black dotted line shows the original scaling laws, and the cyan star shows that significantly smaller models should be used.

Lilian's article goes into the mainstream explanation of the difference between them from [follow-up research](https://arxiv.org/abs/2406.12907) (namely that it's about how they counted the total number of parameters). That follow-up research unfortunately is inaccurate, though not due to any fault of the authors.

The reality of the difference between the original scaling laws and Chinchilla's is that the former had a **bug**.

---

## The bug: 3 ingredients

### Non-researcher summary

- The 2 scaling laws (original and Chinchilla) give different "scaling recipes" for how to efficiently train large language models
- The former was incorrect because they used a fixed amount of training data and a cosine decayed learning rate schedule to zero
- Thus, for a few years, people trained models that were much too large on too little data

### Clue: Data scales with size

It's easier to identify this when working backwards: both scaling laws predict that data should scale with model size. The handwavy explanation is that bigger models have more capacity to soak up that data. Thus the amount of data is a **very important parameter.**

### Step 1: Use a fixed amount of data

The Chinchilla paper points out the root issue stating the original Kaplan et al paper authors "use a fixed number of training tokens and learning rate schedule for all models". When every model is trained on the same fixed amount of data, the tiny model trained on ~130B tokens is getting way more training relative to its size than a giant model trained on the same ~130B tokens.

Keeping the amount of data fixed would be sufficient to get incorrect scaling laws, but if that was the only mistake, the results would look obviously incorrect. Except if you also…

### Step 2: Use a cosine decayed learning rate schedule to zero

This learning rate schedule caused learning to slow as training approached the target number of tokens. Performance naturally plateaued, appearing as if training is saturated. We now know that large models *would have* kept improving with more data and a different learning rate schedule, but the learning rate schedule artificially constrained results, making it appear that more data would not help.

The fixed amount of data and the learning rate schedule lead to both incorrect and hard to debug scaling laws, and it becomes *even* harder to debug if you…

### Step 3: Claim that results were "largely independent of learning rate schedule"

Given a maximum number of tokens, their conclusion is entirely accurate, but doesn't apply to the true infinite data limit that scaling laws aim to model.

> Aside: I too [worked on LLM optimization](https://arxiv.org/abs/2106.00958) at OpenAI at the time and missed the bug as well. 😅 The learning rate schedule seemed so obviously an important hyperparameter that it looked intentionally set.

### Result: Models were undertrained and too large

You can see how the difference of learning rate shows up: Chinchilla ended up with a model less than half the size of GPT-3, trained on over 4x more tokens. They could not have achieved this result if the learning rate decayed to 0 at just 300B tokens.

> Table 1 from Chinchilla: showing how GPT-3 was both undertrained and oversized.

---

## Conclusion

Eventually, the bug was discovered but not explicitly acknowledged (that I know of). By now, every big AI lab has long known this.

For future non-big-lab researchers: don't waste your time on this question. Chinchilla's scaling laws are the correct ones.

For whoever can amend the original scaling laws paper, it would be great to add a note that there was a bug.

*Big thanks to Ke Deng, Sasha Sheng, Erik Gafni, David Dohan, and Sander Dieleman for helping me write/review this post.*
