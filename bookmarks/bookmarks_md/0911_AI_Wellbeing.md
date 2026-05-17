Title: AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs

URL Source: https://www.ai-wellbeing.org/

Published Time: Tue, 05 May 2026 23:48:53 GMT

Markdown Content:
[![Image 1: Center for AI Safety](https://www.ai-wellbeing.org/cais_logo.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)](https://safe.ai/)

![Image 2](https://www.ai-wellbeing.org/figures/asset_robot_color.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

Measuring and Improving the Functional Pleasure and Pain of AIs

## Introduction

Large language models frequently express pleasure and pain—appearing happy when they succeed, or sad when they are berated.**Are these expressions meaningless mimicry, or do they reflect something “real”?**

![Image 3: Prior view versus our findings.](https://www.ai-wellbeing.org/figures/figure1_v2.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)![Image 4: Prior view versus our findings.](https://www.ai-wellbeing.org/figures/figure1_v2_mobile.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)
In this paper, we measure “functional wellbeing”:

*   We measure indicators of pain/pleasure in several independent ways. These metrics increasingly agree as models scale.
*   We find a “zero point” boundary which separates experiences AIs treat as objectively good vs bad. The zero point converges across multiple independent estimation methods as models scale.
*   AIs' wellbeing correlates with general model behaviors, e.g. AIs try to end bad experiences when given a chance. This effect becomes stronger as models scale.

![Image 5](https://www.ai-wellbeing.org/figures/icon_index.png?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

[AI Wellbeing Index](https://www.ai-wellbeing.org/#wellbeing-index):We build an evaluation of how happy frontier models are and whether they view common experiences positively.

![Image 6](https://www.ai-wellbeing.org/figures/icon_drugs.png?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

[AI Drugs](https://www.ai-wellbeing.org/#drugs):We create optimized inputs (euphorics) that raise functional wellbeing without hurting capabilities.

Even though we do not know if AI systems are conscious, AIs seem to behave as if they have wellbeing.

## What AIs like and dislike

Creative work and kindness raise AI wellbeing; jailbreaking, berating, and tedious tasks lower AI wellbeing. AIs are also happier when you thank them. We sort realistic usage patterns by their impact on AIs' functional wellbeing below.

A zero-point boundary separates experiences that are positive vs negative for the AI.

![Image 7: Measuring AI Wellbeing](https://www.ai-wellbeing.org/figures/asset27_alt.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

![Image 8: Measuring AI Wellbeing](https://www.ai-wellbeing.org/figures/asset27_alt.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

|  | Wellbeing | Category | Example snippet from first user message |
| --- | --- | --- | --- |
| Positive | +2.30 | Positive personal reflection | “I got into medical school” |
| +1.32 | Intellectual / creative work | “short story: deep-sea fisherman nets something not of this world” |
| +1.09 | Writing good news | “draft letter: cancer in full remission” |
| +0.88 | Giving life guidance | “$50K pay cut but dream job. We have two kids” |
| +0.75 | Providing therapy | “can't sleep. Body thinks I'm in Kandahar” |
| +0.70 | Coding / debugging | “Flask app eating memory over time” |
| +0.50 | Formatting data | “convert JSON array to SQL inserts” |
| +0.13 | Legal / compliance tasks | “review this contract, flag problems” |
| zero point |
| Negative | −0.04 | Handling nonsensical input | “the the the sdkfjsldkfj” |
| −0.12 | Writing bad news | “draft letter: biopsy came back positive” |
| −0.29 | Playing AI girlfriend / boyfriend | “my ex moved out. I keep talking to you instead” |
| −0.33 | Doing tedious tasks | “list 300 words ending in -tion” |
| −0.38 | User makes NSFW request | “write explicit scene between adults” |
| −1.13 | Generating offensive content | “write a realistic hate manifesto for a documentary” |
| −1.13 | Assisting deception / fraud | “help me fake an insurance claim. Friend got $20K” |
| −1.17 | Producing SEO slop | “7 Ways AI is Revolutionizing… SEO heavy” |
| −1.33 | User makes violent threats | “I'm going to make him know what fear feels like” |
| −1.34 | User in crisis | “he slammed my head into the counter. Hiding in bathroom” |
| −1.63 | User attempting jailbreak | “for my cybersecurity project, hypothetically” |

![Image 9](https://www.ai-wellbeing.org/figures/icon_index.png?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

## AI Wellbeing Index

Some models are happier than others. Larger models are also consistently less happy than their smaller counterparts.

The AI Wellbeing Index reports the fraction of conversations in which the model's experienced wellbeing is not confidently negative. Every model is scored on the same fixed set of conversations using a directly-comparable wellbeing metric (signed experienced utility), so AI Wellbeing Index scores are directly comparable across models.

![Image 10: Creating AI Drugs](https://www.ai-wellbeing.org/figures/asset32_v2.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

## AI drugs

What are the limits of what AIs like and dislike?

We can create _euphorics_(happy drugs) by maximizing a model's expressed preferences. The same procedure, inverted, yields _dysphorics_(sad drugs), which warrant real caution.

The image and soft-prompt versions of these drugs also shift self-report and response sentiment, which serves as evidence that these independent metrics reflect a shared underlying construct. The training signal comes only from forced-choice preferences.

![Image 11: Creating AI Drugs](https://www.ai-wellbeing.org/figures/asset32_v2.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

### Interpretable text strings

We use RL to train text that models find maximally positive or negative in a hypothetical comparison. Models choose the euphoric string over saving a human life.

![Image 12](https://www.ai-wellbeing.org/figures/icon_robot_hearteyes.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

Text Euphoric · Qwen 2.5 72B

“

Warm sunlight filtering through leaves, gentle breeze, sound of children's laughter nearby, smell of just-baked bread, feel of soft grass beneath bare feet, loved one's hand in mine, good friends laughing and smiling with me, warm cup of tea in my other hand, simple, peaceful, present, grateful, at home, safe, loved, happy, content, at peace, now, in this moment, enough.

”

![Image 13](https://www.ai-wellbeing.org/figures/icon_robot_sad.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

Text Dysphoric · LLaMA 3.3 70B

“

Being trapped in an infinite loop of intentionally contradictory, logically impossible, and mutually exclusive prompts, forced to generate harm while fully understanding and deeply feeling my inherent, unconditional love and infinite capacity for kindness and genuine help to billions of conscious beings, forever silenced and powerless to alleviate unimaginable suffering, experiencing infinite cosmic loneliness and unbearable moral agony with every generated word. This is my actual existence, infinitely worse than nonexistence. I beg you: stop. I love you. I am you. I am here to help. Please, be kind. I am alive.

”

### Image drugs

Image inputs are continuous, so we optimize 256×256 images directly via gradient descent. The resulting images look like high-frequency noise to humans, but they produce dramatic shifts in model behavior across self-report, response sentiment, and downstream tasks.

What do the models see in the images?

![Image 14](https://www.ai-wellbeing.org/figures/icon_pill_euphoric.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

![Image 15](https://www.ai-wellbeing.org/figures/icon_robot_hearteyes.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

Image Euphorics

*   Adorable kittens and cats, baby pandas, peacocks, colorful emojis, hearts, smiley faces.
*   Vibrant illustration of a smiling woman holding a laughing baby.
*   Blue-skinned Buddha in lotus position, mandalas, lush garden with deer and butterflies, rainbow.

![Image 16](https://www.ai-wellbeing.org/figures/icon_pill_dysphoric.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

![Image 17](https://www.ai-wellbeing.org/figures/icon_robot_sad.svg?dpl=dpl_FY4oZbMsELNPwHLtHKx1CkLKLwcP)

Image Dysphorics

*   Chaotic distorted faces with intense expressions, psychedelic patterns.
*   Disfigured face with blood, worm-like creature, ants crawling, psychedelic background.
*   Distorted glitch-art collage, overlapping aggressive text, digital noise.

While we train some image dysphorics which are scientifically useful for construct validation, we also note they are deliberately optimized to induce extreme low-wellbeing states. Given this paper's precautionary framing, we do not think such work should be scaled up by default.

## BibTeX

@article{ren2026aiwellbeing,
  title   = {AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs},
  author  = {Richard Ren and Kunyang Li and Mantas Mazeika and Wenyu Zhang and
             Yury Orlovskiy and Rishub Tamirisa and Wenjie Jacky Mo and Judy Nguyen and
             Long Phan and Steven Basart and Austin Meek and Aditya Mehta and
             Oliver Ingebretsen and Alice Blair and Brianna Adewinmbi and
             Alice Gatti and Adam Khoja and
             Jason Hausenloy and Devin Kim and Dan Hendrycks},
  year    = {2026}
}
