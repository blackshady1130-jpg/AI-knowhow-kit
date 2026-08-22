# 工具使用与模型规模：为何更大的模型仍然重要

> 来源：X 原帖：Jason Wei（@_jasonwei），2026 年 8 月 18 日 03:10；仅保留原帖正文

---

When language models first started using tools well, I was sympathetic to the narrative that instead of scaling up language models, all we needed was a strong enough "cognitive core", say 1B parameters, and anything else could be done with tool use, like browsing the internet or executing code. I think a lot of people were sympathetic to this argument, and indeed it is pretty hard to come up with a meaningful task that cannot be in principle achieved by a 1B model with adequate access to tools. For example, any esoteric fact that a large language model would know can be, in principle, retrieved from the internet and reasoned over by a 1B language model.

However I now think this is totally wrong for one simple reason: doing tasks quickly and naturally without tool use matters a lot.

The way that I internalized this reason was actually in my personal journey learning badminton this year. In badminton I am very much like a "1B cognitive core". While I can physically do every movement in a badminton shot that my coach teaches me, it requires a lot of work to mentally remember every cue and put it together. In practice I can do a shot almost perfectly, but I struggle to do it across a point and I definitely can't do it consistently in a game. This is obviously different from someone who has practiced a shot ten-thousand times and effortlessly executes it as a natural instinct.

In the same way, language models knowing a fact internally, without tool calls, is meaningful. The first reason is that we obviously care about speed; you'd much rather get an answer immediately than have the model think a long time to be sure of its answer or browse the web. A second reason is that there are some things that are simply best learned via backpropagation over lots of data. If you ask about how people generally think of the Shambhala music festival, you'd rather a large language model give you an aggregate opinion based on all the data on the internet, than get a regurgitation of the first three reviews that show up in a web search. A third reason is that having to do a lot of work to find an answer is not as reliable as already knowing the answer. While this does not have to be true in theory, it is probably true in practice, at least for now. If you have to re-look up facts or redo a mathematical derivation all the time there is a higher chance of mistakes, which can compound in a long-horizon task.

Once you buy that it is valuable to do things parametrically without tool use, then you must buy the argument that a 1B cognitive core is not sufficient. There is an information limit to how much knowledge can be internalized by a 1B model, and we will surely want AI to know more than that. Even 1T probably won't be enough. We will want the AI to know as much about our world as possible, we will want it to be updated with new information, and our expectations of what AI can do for us will continue to grow.

In summary, tool use enables small models to do a lot more, but those who demand the highest quality intelligence will always want larger models. Bitter lesson strikes again.

---

## 原文链接

https://x.com/_jasonwei/status/2089429555371024577
