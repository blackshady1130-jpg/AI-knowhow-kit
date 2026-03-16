---
url: https://baoyu.io/blog/prompt-engineering/the-core-of-prompt-engineering?continueFlag=f79c68b5945bcb7706484d375c13aad1
title: "Prompt Engineering 的核心是逻辑"
description: "Prompt Engineering 的核心就是你怎么将一个复杂的任务拆成科学合理的步骤，并且让前面每一步的结果都成为后面步骤的基础，所有步骤合并在一起得到最终的结果，而不要指望一步得到结果。"
published: "2024-03-20"
captured_at: "2026-03-08T11:40:25.396Z"
---

# Prompt Engineering 的核心是逻辑

如果你看过我以前写的[多步翻译 Prompt](https://baoyu.io/blog/prompt-engineering/translator-gpt-prompt-v2)，或者这个[总结的 Prompt](https://baoyu.io/blog/prompt-engineering/how-to-get-a-better-summary-result)，你就会发现：

> “所谓提示词工程，核心不是你套个什么模板用什么格式，而是逻辑！！”

\*\*逻辑就是你怎么将一个复杂的任务拆成科学合理的步骤，并且让前面每一步的结果都成为后面步骤的基础，所有步骤合并在一起得到最终的结果，而不要指望一步得到结果。\*\*只有这样你才能得到最佳的效果。

就像翻译，无论你的 Prompt 格式写的多完美，如果只有一步，那么效果上接近 DeepL 那样就是天花板了，但如何你拆分成直译、反思、意译，那么效果就接近人写的效果了！

就像总结，如果你只是让它总结，那么它可能就会偷懒遗漏很多要点，但如果你让它先提炼主题、再检查有没有遗漏的主题、然后基于每个主题列要点，最后再基于上面的去生成总结，就会好很多，也不会“偷懒”。

哪怕只是写一句“让我们一步步思考”，让它自己去分步骤，列出每一步的结果，都会好很多！

下次写 Prompt，效果不理想时，不妨想想看：我是不是可以把这个任务拆分成几个步骤？怎么拆分最合理？

顺便说一下：\*\*即使你在 Prompt 里面指明了步骤，但是如果没有将步骤打印出来，那么也是没有效果的。\*\*因为 LLM 需要基于前面的输出结果去预测后面的结果，如果没有前面步骤的输出，就无法影响后面的预测结果。