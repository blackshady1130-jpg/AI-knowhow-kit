# 600亿买一个IDE？看懂 SpaceX 与 Cursor 交易背后的“印钞机引擎”

**作者**: Agentic Infra
**发布时间**: 2026-04-23 05:27
**原文链接**: https://mp.weixin.qq.com/s/diwEZHMP1zZKeYCA_oHDDw

---



看到不少中文圈里对SpaceX 和 Cursor 并购/合作的评价，一波人觉得老马(Elon Musk) 人傻钱多，居然 600 亿美元买一个套壳IDE， 另一波则是震撼于 AI 应用端出现了史无前例的吞金巨兽。在目标估值 1.75 万亿，募资规模 750 亿美元的公司来说、极速推进 IPO 的大背景下，这种资本量级的决策绝不可能是低级错误。Cursor 到底凭什么值 600 亿？SpaceX 到底在买什么？


![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FQFxia3P63qykK1u3EwicOuoELEic7BRHdf4MdtHaTz9Ko9OLyoP2gP2QX44fWHUJrdsxGxW1SibiaGcALm2yx454uNywJ6OG2XaPa2tdiaXaica9l4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


SpaceX 拿到是一个特殊交易结构：它可以在今年稍晚以 600 亿美元收购 Cursor；如果最终不收购，也要支付 100 亿美元继续双方合作。与此同时，Cursor 会接入 xAI 的 Colossus 训练基础设施，加速后续模型训练。


我认为 SpaceX 的真正目的是想买一条能**把算力、模型、应用入口和收入故事接起来的通道**。对一家正朝今年 6 月底 IPO 推进公司来说，这件事尤其重要。因为资本市场会问一个更朴素的问题：你砸进去的 AI 资本开支，什么时候能长成市场听得懂的业务。


![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FQFxia3P63qymhJNQNricm7ngGNzrSejCScZUicY8yvOicqNUCe9c0ZBCYdIOkV7GI8xicakj2E1NibiavACUlOeQfOicOfZV3ia6kUUNOiaKibTT14iassQ%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg)


Reuters 披露的 IPO 信息显示，SpaceX 和 xAI 合并后的主体在 2025 年收入 186.7 亿美元，但同期录得 49.4 亿美元亏损，capex 在两年内接近五倍增长到 207.4 亿美元，主要就是 AI 基础设施投入。与此同时，它又在风险披露里提醒投资者：轨道 AI 数据中心这样的愿景还依赖未经验证的技术，未必能实现商业可行性。也就是说，SpaceX 现在不缺宏大叙事，缺的是一个能把 AI 投入快速翻译成商业化出口的近端故事。Cursor 恰好提供了这个出口：高价值的开发者分发、已经跑出来的收入，以及一个最容易被市场理解的 AI 应用入口。


SpaceX/xAI 缺一个真正能赢下 coding 入口的产品。3 月 FT 报道称，老马对 xAI coding division 的表现不满，做出了管理调整和人员变动，还从 SpaceX 和 Tesla 调锦衣卫去审视 xAI 的执行问题。换句话说，内部从零长出一个足够强的 coding 产品，未必赶得上 IPO 的时间窗口。直接把 Cursor 这种已经证明能打、能卖的入口接进来，比自己重新走一遍要快得多，也更符合老马的风格。


再说 Cursor 本身。过去很长一段时间，中文技术圈对 Cursor 的叙事都过于简单粗暴了。很多人认为这无非就是一个包装得更好的壳，发的自家模型也不过是 Kimi 2.5+RL 换皮。但如果只这么看，你会错过它真正的技术含量。Composer 发布还不到六个月，Composer 1.5 已经把 reinforcement learning 的规模拉高了 20 倍以上，Composer 2 又叠加了 continued pretraining，而且每一次算力上台阶，模型能力都会出现明显提升。在 mid-training、continued pretraining、后训练和整套 pipeline 上都有在持续下硬功夫。


![](https://images.weserv.nl/?url=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FQFxia3P63qymHGWu3Ae6I5JogeBKCT3t3icUSktazBcRw0ABEUpMLc5fsb1GWbfR0IfFFuvXia5HeuLxRGxwq2lSFUjzbdSgklxibnoN6coT8Ow%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


Coding model 的竞争，已经不简单是 model architecture 或 pretraining recipe 的竞争，而是数据运营、环境重建、eval 体系、产品反馈回路的竞争。


**Data 本质上更像运营活，不是纯 Research 活。**


有没有能力把用户在真实开发流程里的行为，稳定地转成可训练、可复现的数据。Consumer data 从来都不是直接能用的。你拥有 token 和 trace，不代表你拥有 environment；代码跑在人家的 codebase 里，真正难的是怎么把这些行为还原成任务表示、训练样本和反馈闭环。这件事远比多训一点代码要难。Cursor 证明了自己是有能力继续进化的。因为一旦你把用户行为和训练闭环接起来，模型 improvement 就不再完全依赖一次性 research breakthrough，而是可以持续滚动优化。看内部 A/B test 数据，对 Cursor 模型的评价是至少已经到了可以和 SOTA coding 模型正面比较的程度。


公开可验证的信息是，Cursor 在 2025 年 11 月已经跨过 10 亿美元年化收入门槛。到今年 3 月，又有媒体援引 Bloomberg 的信息称，它在 2026 年 2 月的年化收入已经超过 20 亿美元，大约 60% 的收入来自企业客户。还有消息称今年年底将有可能冲击 60 亿美元 ARR， 说明 Cursor 已经进入真实的商业化阶段，企业客户开始成为它更稳定的收入底盘。


所以 600 亿美元到底贵不贵？如果你把 Cursor 当成一个 AI 编程工具，这个价格当然很夸张。但如果把它看成一组能力的组合，逻辑就完全不同:它既是开发者工作流的入口，也是已经被企业采购验证过的收入层；更关键的是，它能把真实用户行为反哺回模型的训练飞轮，同时给 Colossus 这种超级算力池找到一个高价值的需求出口，一台把 xAI 算力池变现的印钞机引擎。


往更大一点的格局看，下一代 AI 公司的壁垒，在模型背后那层 runtime：谁掌握了用户行为真正落地的那一层，谁的能力才有机会持续变强。Cursor 的幸运在于它自己就是 IDE，这条管道长在自己家里，所以它能被 600 亿估值。当越来越多 agent 产品要投入真实生产环境的时候，它们每一家都会需要一条类似可进化的管道。这条基础设施长在哪里、由谁提供，是接下来几年比任何一次模型发布都更值得盯着的事。


**用未来 IPO 里 3% 到 4% 的价值，换一个已经跑通闭环、能接上现有的算力、又能补完 coding AGI 故事的资产，这笔账在老马的账本上算得过来。**
