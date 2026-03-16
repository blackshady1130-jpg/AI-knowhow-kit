---
url: https://openai.com/research/improving-mathematical-reasoning-with-process-supervision?continueFlag=40c2724537472cbb3553ce1582e0db80
title: "Improving mathematical reasoning with process supervision"
description: "We've trained a model to achieve a new state-of-the-art in mathematical problem solving by rewarding each correct step of reasoning (“process supervision”) instead of simply rewarding the correct final answer (“outcome supervision”). In addition to boosting performance relative to outcome supervision, process supervision also has an important alignment benefit: it directly trains the model to produce a chain-of-thought that is endorsed by humans."
published: "2023-10-19T07:00:00.000Z"
captured_at: "2026-03-08T10:26:46.519Z"
---

# Improving mathematical reasoning with process supervision

This challenging trigonometry problem requires applying several identities in a not-at-all obvious succession. Most solution attempts fail, because it is hard to choose which identities are actually helpful. Although GPT-4 usually can’t solve this problem (only .1%.1\\% of solution attempts reach the correct answer), the reward model correctly recognizes that this solution is valid.

1

I notice that the angle 100 degrees is not a special angle, so I will need to use some trigonometric identities to simplify this expression.

2

I recall that tan⁡θ\=sin⁡θcos⁡θ\\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta} and sin⁡2θ\=2sin⁡θcos⁡θ.\\sin 2\\theta = 2 \\sin \\theta \\cos \\theta.

3

I can use these identities to rewrite the expression as sin⁡100∘cos⁡100∘+4sin⁡100∘.\\frac{\\sin 100^\\circ}{\\cos 100^\\circ} + 4 \\sin 100^\\circ.

4

I can combine the terms by finding a common denominator of cos⁡100∘.\\cos 100^\\circ.

5

I get sin⁡100∘+4sin⁡100∘cos⁡100∘cos⁡100∘.\\frac{\\sin 100^\\circ + 4 \\sin 100^\\circ \\cos 100^\\circ}{\\cos 100^\\circ}.

6

I can simplify the numerator by using the double angle identity again, but in reverse.

7

I get sin⁡100∘+2sin⁡200∘cos⁡100∘.\\frac{\\sin 100^\\circ + 2 \\sin 200^\\circ}{\\cos 100^\\circ}.

8

I notice that 200 degrees is the same as 180 degrees plus 20 degrees, so I can use the sum angle identity for sine.

9

I get sin⁡100∘+2(sin⁡180∘cos⁡20∘+cos⁡180∘sin⁡20∘)cos⁡100∘.\\frac{\\sin 100^\\circ + 2 (\\sin 180^\\circ \\cos 20^\\circ + \\cos 180^\\circ \\sin 20^\\circ)}{\\cos 100^\\circ}.

10

I recall that sin⁡180∘\=0\\sin 180^\\circ = 0 and cos⁡180∘\=−1,\\cos 180^\\circ = -1, so I can simplify further.

11

I get sin⁡100∘−2sin⁡20∘cos⁡100∘.\\frac{\\sin 100^\\circ - 2 \\sin 20^\\circ}{\\cos 100^\\circ}.

12

I notice that 100 degrees is the same as 90 degrees plus 10 degrees, so I can use the sum angle identity for sine and cosine.

13

I get (sin⁡90∘cos⁡10∘+cos⁡90∘sin⁡10∘)−2sin⁡20∘(cos⁡90∘cos⁡10∘−sin⁡90∘sin⁡10∘).\\frac{(\\sin 90^\\circ \\cos 10^\\circ + \\cos 90^\\circ \\sin 10^\\circ) - 2 \\sin 20^\\circ}{(\\cos 90^\\circ \\cos 10^\\circ - \\sin 90^\\circ \\sin 10^\\circ)}.

14

I recall that sin⁡90∘\=1\\sin 90^\\circ = 1 and cos⁡90∘\=0,\\cos 90^\\circ = 0, so I can simplify further.

15

I get cos⁡10∘−2sin⁡20∘−sin⁡10∘.\\frac{\\cos 10^\\circ - 2 \\sin 20^\\circ}{-\\sin 10^\\circ}.

16

I can simplify the sign by multiplying the numerator and denominator by -1.

17

I get 2sin⁡20∘−cos⁡10∘sin⁡10∘.\\frac{2 \\sin 20^\\circ - \\cos 10^\\circ}{\\sin 10^\\circ}.

18

I notice that 20 degrees is the same as 30 degrees minus 10 degrees, so I can use the difference angle identity for sine.

19

I get 2(sin⁡30∘cos⁡10∘−cos⁡30∘sin⁡10∘)−cos⁡10∘sin⁡10∘.\\frac{2 (\\sin 30^\\circ \\cos 10^\\circ - \\cos 30^\\circ \\sin 10^\\circ) - \\cos 10^\\circ}{\\sin 10^\\circ}.

20

I recall that sin⁡30∘\=12\\sin 30^\\circ = \\frac{1}{2} and cos⁡30∘\=32,\\cos 30^\\circ = \\frac{\\sqrt{3}}{2}, so I can simplify further.

21

I get cos⁡10∘−3sin⁡10∘−cos⁡10∘sin⁡10∘.\\frac{\\cos 10^\\circ - \\sqrt{3} \\sin 10^\\circ - \\cos 10^\\circ}{\\sin 10^\\circ}.

22

I can cancel out the cos⁡10∘\\cos 10^\\circ terms in the numerator.

23

I get −3sin⁡10∘sin⁡10∘.\\frac{-\\sqrt{3} \\sin 10^\\circ}{\\sin 10^\\circ}.

24

I can cancel out the sin⁡10∘\\sin 10^\\circ terms in the numerator and denominator.

25

I get −3.\-\\sqrt{3}.

26

Answer: −3\-\\sqrt{3}