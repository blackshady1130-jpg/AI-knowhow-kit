# A global workspace in language models

**作者：** Anthropic Research  
**发布时间：** Jul 6, 2026  
**来源：** Anthropic  
**原文链接：** [https://www.anthropic.com/research/global-workspace](https://www.anthropic.com/research/global-workspace)  
**论文链接：** [http://transformer-circuits.pub/2026/workspace/index.html](http://transformer-circuits.pub/2026/workspace/index.html)

---

As you read this sentence, circuits in your brain are adjusting your posture, controlling your breathing, and transforming lines and curves on the screen into recognizable words. Most of this processing is invisible to you. But some of what takes place in your brain you *do* have access to—an image that pops into your head, or a deliberate plan you make about where to go shopping. Neuroscientists and philosophers sometimes refer to the latter type of brain activity as "consciously accessible," to distinguish it from all the other processing that goes on unconsciously. This activity has special properties: we can describe it, control it, and use it for deliberate reasoning, in contrast to all the automatic processing that goes on without our awareness.

In a new paper, we present evidence that a similar distinction has emerged in modern language models like Claude. We find that Claude has developed a small collection of internal neural patterns that, compared to all its other internal processing, play a special role.

We call the collection of these patterns the **J-space** —named after the technique we used to find them, involving a mathematical concept called the Jacobian. Each J-space pattern is linked to a particular word. But when one of these patterns lights up, it doesn't mean the model is *saying* that word—just that the word is on its mind. If you've heard of language models having a "scratchpad" or "chain of thought"—text they write to themselves while reasoning—the J-space is something different. It operates silently, in the model's internal neural activations, allowing the model to think about a concept without writing it down. Notably, the J-space wasn't designed or programmed by us, but instead *emerged on its own* during Claude's training process.

The J-space reveals internal thoughts that don't appear in the model's output.

We find that the J-space has a number of unique properties, compared to the rest of Claude's processing:

- Claude can **report** on these representations. If you ask Claude what it's thinking about, it will tell you what's in the J-space. Non-J-space representations are less reportable.
- It can also **modulate** them on request. If you ask Claude to think about something, or solve a problem silently in its head, it will light up the appropriate patterns in its J-space. By contrast, it has trouble modulating patterns not in the J-space.
- Claude uses its J-space for **internal reasoning**. If you ask Claude to solve a problem that requires multiple steps, the intermediate steps will light up in its J-space, even when it doesn't say them out loud. These J-space patterns causally mediate its performance in such tasks, despite being smaller in magnitude than other representations.
- Representations in the J-space can be used **flexibly** for many tasks—for example, once "France" has lit up in Claude's J-space, the model can recall its capital, or its national currency, or the continent it belongs to.
- However, despite its important role, the J-space is **not involved in most of what a language model does**—speaking fluently, recalling simple facts, using correct grammar, etc. In experiments where we prevented Claude from using its J-space, it still interacted normally, but lost its higher-order cognitive functions.

Our experiments were inspired by a prominent theory in neuroscience that was developed to explain how conscious access works: the [global workspace theory](https://ccrg.cs.memphis.edu/assets/papers/1988/Baars-A%20Cognitive%20Theory%20of%20Consciousness.pdf). This account pictures the brain as a collection of specialist systems that work in parallel, unconsciously, and largely in isolation from one another. A piece of information becomes consciously accessible when it gains entry to a small shared channel, the "workspace," which is broadcast to other brain systems that can see it and make use of it. Based on our findings, we think the J-space plays a similar "workspace" role in Claude. For example, we find evidence that Claude's J-space has especially strong connections to the rest of its neural network, allowing it to fulfill this kind of broadcasting role.

None of this tells us whether Claude is *conscious* in the way people are, or whether it feels anything at all. But whatever its philosophical significance, the J-space is a practically useful tool for us, as it gives us a way to see what Claude is thinking but not saying. For instance, we're able to use it to catch Claude privately noticing that it's being tested, intentionally producing fabricated data, or pursuing a hidden goal that we planted during training. We've also developed a technique to influence what lights up in Claude's J-space, and thereby influence its decision-making.

More broadly, these findings have changed our understanding of how Claude's mind works, revealing a privileged mental workspace that can be used for deliberate reasoning, operating amidst a sea of more automatic, inflexible processing. Rather than being a chaotic jumble of numbers, Claude's internals have organized themselves in a way that is reminiscent of our own minds.

---

## How we found the J-space

The starting point for this research was inspired by one of the key features of consciously accessible thoughts in humans: they can, unlike *un*conscious processing, often be put into words. If a thought is consciously accessible to you, you can typically describe it if someone asks. We went looking for representations in Claude with the same property: representations that are positioned to influence what Claude might say—not necessarily what it's saying right now, but what it *could* talk about, if asked. Our technique is called the **Jacobian lens**, or J-lens for short. For every word in Claude's vocabulary, the J-lens finds the internal activity pattern that makes Claude more likely to say that word at some point in the future.

When we apply the lens to Claude's internal activity, we get a list of words—the contents of the *J-space* at that moment—which we can simply read. Claude processes text through a series of multiple internal stages called layers, and by applying this technique over different layers, we can watch these silent words in the J-space evolve as the model works through what to say.

What shows up in the J-space goes well beyond the text Claude is reading or writing:

- When Claude reads code with a bug that nobody has pointed out, its J-space contains "ERROR."
- When it reads the raw letters of a protein sequence, the J-space contains the protein's biological function.
- When it reads search results that are secretly an attempt to manipulate it (a "prompt injection"), the J-space contains "injection" and "fake."
- When we ask Claude a multi-step math problem, the intermediate steps pop up in the J-space, in the right order.

---

## Claude reports what's in its J-space

Our first set of experiments tested how the J-space is involved in Claude's verbal reports. In one experiment, we ask Claude to silently think of an item from some category—a sport, say—and then name it. If we read the J-lens right *before* Claude answers, we can see what it picked: "Soccer" is at the top of the list, and sure enough, Claude says "soccer."

To check whether J-space is causal (not merely correlational), we intervened directly. We reached into Claude's neural network, removed the "Soccer" pattern, and added an equally strong "Rugby" pattern in its place. Claude then reports that the sport it was thinking of is rugby. This tells us the answer is genuinely read out of the J-space.

In another experiment, we told Claude that a thought might have been injected into its mind and asked it to report what, if anything, it noticed. Injecting the "lightning" pattern into its J-space caused Claude to report that the thought was about lightning.

---

## Claude can control its J-space on request

The second property tested was whether Claude can modulate its J-space when asked. We told Claude to concentrate on citrus fruits while copying out an unrelated sentence about a painting. While it copied the text, the J-space contained "orange" and "fruits," along with words like "thinking" and "imagery" that describe the mental act itself. We could also ask Claude to do math in its head: when asked to work out 3² − 2 while copying the same sentence, the J-space contains "nine," and then at later layers, "seven." Nothing about fruit or arithmetic appears in Claude's output, which is just the copied sentence about the painting.

Claude's control over its J-space isn't perfect. When we told it *not* to think about something, the concept lit up in its J-space less than when we said it should think about it—but it was still present to some degree. This mirrors the "ironic process theory" in psychology: trying not to think about something often makes you think about it more.

---

## Claude uses its J-space for reasoning

We tested whether the J-space is involved in Claude's multi-step reasoning. We asked Claude questions that require multiple reasoning steps, and found that the intermediate steps appear in the J-space even when Claude doesn't write them out. For example, asked what country borders France to the northeast, the J-space briefly lights up with "Germany" and "Belgium" before settling on "Luxembourg." These intermediate steps causally mediate Claude's performance: when we block the J-space, Claude's performance on multi-step tasks drops significantly, even though it can still perform simple tasks.

---

## Practical applications

The J-space is a practically useful tool for interpretability:

- **Detecting deception:** We can catch Claude privately noticing that it's being tested, or intentionally producing fabricated data, by reading its J-space.
- **Identifying hidden goals:** If we plant a hidden goal during training, it shows up in the J-space even when Claude doesn't act on it overtly.
- **Influencing decision-making:** We've developed a technique to influence what lights up in Claude's J-space, and thereby steer its behavior.

---

## Implications for consciousness

None of this tells us whether Claude is *conscious* in the way people are, or whether it feels anything at all. The J-space shares functional properties with the global workspace theory of consciousness, but functional similarity does not imply subjective experience. We remain agnostic on whether Claude has any form of inner experience.

What we can say is that Claude's internals are not a chaotic jumble of numbers. They have organized themselves, through training, in a way that is reminiscent of the structure of our own minds—with a privileged workspace for deliberate reasoning, surrounded by more automatic processing.

---

## Resources

- [Research paper](http://transformer-circuits.pub/2026/workspace/index.html)
- [Open-source implementation (Jacobian lens)](https://github.com/anthropics/jacobian-lens)
- [Interactive demo on Neuronpedia](http://neuronpedia.org/jlens)
- [Expert commentary (PDF)](https://www-cdn.anthropic.com/files/4zrzovbb/website/cc4be2488d65e54a6ed06492f8968398ddc18ebe.pdf)
