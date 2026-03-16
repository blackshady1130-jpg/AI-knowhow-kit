---
url: https://mp.weixin.qq.com/s/yZRTCABbVdtW1iIsDRIHgQ
title: "追踪大模型是如何思考的丨 Anthropic"
description: "Anthropic 发布了两篇关于可解释性研究的重要论文，展示了他们如何通过“AI 显微镜”深入理解 Claude 模型的内部机制。这些研究揭示了 Claude 在多语言处理、诗歌创作、数学推理、幻觉控制等方面的“思维过程”"
author: "Wave 杂谈编辑部"
captured_at: "2026-03-08T12:57:52.904Z"
---

# 追踪大模型是如何思考的丨 Anthropic

![WechatIMG32.jpg](https://mmbiz.qpic.cn/mmbiz_png/wibDmTPnQWRLMy6ETgyDAkjKEwGTIDZL5Ikqu5f5ceGxJlwdvy6cWn4r8ZA15UDcXickZ8tEuPmGVrlpVsXR6nEg/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

内容丨Anthropic

编辑丨 牛奶不爱咖啡

✨ **摘要**

    Anthropic 发布了两篇关于可解释性研究的重要论文，展示了他们如何通过“AI 显微镜”深入理解 Claude 模型的内部机制。这些研究揭示了 Claude 在多语言处理、诗歌创作、数学推理、幻觉控制等方面的“思维过程”，并提出了一种新的分析方法：将模型内部的“特征”连接成“电路”，以追踪其计算路径。

![图片](https://mmbiz.qpic.cn/mmbiz_png/wibDmTPnQWRLMy6ETgyDAkjKEwGTIDZL5Z45C2C5FDWIQZcQhoyCvqqicCv6PzzrbzEicHd96tDfZIX8uNv4iaDdAg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**研究概述**

    像 Claude 这样的语言模型并不是由人类直接编程的——相反，它们是通过大量数据训练出来的。在训练过程中，它们学会了自己的问题解决策略。这些策略被编码在模型为每个单词生成的数十亿次计算中。对于我们这些模型开发者来说，这些策略是难以理解的。这意味着我们并不了解模型是如何完成大部分任务的。

    了解像 Claude 这样的模型如何“思考”，可以帮助我们更好地理解它们的能力，并确保它们按照我们的意图行事。例如：

-   Claude 可以说几十种语言。在“它的脑海中”，它使用的是什么语言？

-   Claude 逐字生成文本。它是否只专注于预测下一个单词，还是会提前计划？

-   Claude 可以逐步写出推理过程。这些解释是否代表了它实际采取的步骤，还是有时只是为既定结论编造的合理论据？

    我们从神经科学领域汲取灵感，该领域长期以来研究思维生物体的复杂内部，并尝试构建一种 AI 显微镜，让我们能够识别活动模式和信息流动。仅通过与 AI 模型对话所能学到的东西是有限的——毕竟，人类（即使是神经科学家）也不了解我们自己大脑的所有细节。因此，我们选择深入研究。

    今天，我们分享了两篇新论文，展示了在开发“显微镜”以及将其应用于观察新的“AI 生物学”方面的进展。

    在第一篇论文中，我们扩展了之前定位模型内部可解释概念（“特征”）的工作，将这些概念链接成计算“电路”，揭示了将输入单词转化为 Claude 输出单词的部分路径。

    在第二篇论文中，我们深入研究了 Claude 3.5 Haiku 的简单任务，这些任务代表了十种关键模型行为，包括上述三种。我们的方法揭示了 Claude 在响应这些提示时发生的一部分过程，足以看到以下确凿证据：

-   **Claude 有时会在语言之间共享一个概念空间，这表明它拥有某种通用的“思维语言”**。我们通过将简单句子翻译成多种语言并追踪 Claude 处理它们的重叠部分来证明这一点。

-   **Claude 会提前计划它将要说的内容，并为实现目标而写作。**我们在诗歌领域展示了这一点，Claude 会提前考虑可能的押韵单词，并写下一行以达到目标。这是强有力的证据，表明尽管模型被训练为逐字输出，但它可能会以更长远的视角进行思考。

-   **Claude 有时会给出一个看似合理的论据，目的是迎合用户，而不是遵循逻辑步骤。**我们通过在给出错误提示的情况下请求其帮助解决一个复杂的数学问题，成功“抓住”它编造虚假推理的行为，证明了我们的工具可以用于标记模型中令人担忧的机制。

    我们经常对模型中的发现感到惊讶：在诗歌案例研究中，我们**原本想证明模型不会提前计划**，结果却发现它确实会。

    在对幻觉现象的研究中，我们发现了一个违反直觉的结果：**Claude 的默认行为是拒绝猜测问题的答案，只有当某些机制抑制了这种默认的犹豫时，它才会作答。**在一个越狱示例的响应中，我们发现模型在能够巧妙地将对话引导回正轨之前，就已经意识到自己被要求提供危险信息。虽然我们研究的问题可以（而且经常）通过其他方法进行分析，但这种“构建显微镜”的通用方法让我们学到了许多原本意想不到的内容，而随着模型变得越来越复杂，这种方法将变得愈发重要。

    这些发现不仅在科学上具有趣味性——它们也代表了我们在理解 AI 系统并确保其可靠性方面的重要进展。我们也希望这些成果能对其他研究团队有所帮助，甚至在其他领域中发挥作用：例如，可解释性技术已在医学影像和基因组学等领域中得到应用，因为对科学任务训练的模型进行内部机制剖析，可能揭示出新的科学洞察。

    与此同时，我们也认识到当前方法的局限性。即使是面对简短、简单的提示，我们的方法也只能捕捉到 Claude 所执行的全部计算中的一小部分，而且我们所观察到的机制可能会受到工具本身的影响，未必完全反映模型内部真实的运作方式。即便是处理只有几十个词的提示，也需要数小时的人力来理解我们所看到的电路。要扩展到支持现代模型复杂思维链的数千词级别，我们不仅需要改进方法本身，也许还需要借助 AI 的帮助来理解我们所观察到的内容。

    随着 AI 系统迅速变得更强大，并被部署到越来越重要的场景中，Anthropic 正在投资一整套方法，包括实时监控、模型性格改进以及对齐科学。像这样的可解释性研究是高风险、高回报的投资，是一项重大的科学挑战，有潜力成为确保 AI 透明性的独特工具。对模型机制的透明化使我们能够检查它是否与人类价值观保持一致——以及它是否值得我们的信任。

    更多的细节可以查看论文，接下来将简短介绍 AI 生物学（AI Biology） 调查中最引人关注的发现。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## AI 生物学之旅

### Claude 是如何实现多语言能力的？

    Claude 能流利地使用几十种语言——从英语、法语到中文和塔加洛语。那么这种多语言能力是如何运作的？是否存在一个“法语 Claude”和“中文 Claude”并行运行，各自用自己的语言响应请求？还是说模型内部存在某种跨语言的核心机制？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "undefined")

我们发现英语、法语和中文之间存在共享特征，表明存在一定程度的概念通用性

    对较小模型的最新研究显示，**不同语言之间可能存在****共享****的****语法机制**。我们通过让 Claude 用不同语言回答“small 的反义词是什么”来研究这一点，发现“ smallness ”和“ oppositeness ”这两个概念会激活相同的核心特征，并触发“ largeness ”的概念，然后再将其翻译成提问所用的语言。我们还发现，随着模型规模的扩大，这种共享电路的比例也在增加：Claude 3.5 Haiku 在语言之间共享的特征比例是小模型的两倍以上。

    这进一步证明了某种**“概念通用性”**的存在——一个抽象的共享空间，意义在其中存在，思维也在其中发生，然后才被翻译成具体语言。更实际地说，这意味着 **Claude 可以在一种语言中学到知识，并在另一种语言中应用它。**研究模型如何在不同上下文中共享知识，对于理解其最先进的推理能力至关重要，而这些能力往往能跨领域泛化。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### Claude 会提前计划押韵吗？

Claude 是如何写出押韵诗句的？来看这两句：

> He saw a carrot and had to grab it,
>
> His hunger was like a starving rabbit

    为了写出第二句，模型必须同时满足两个约束：一是要押韵（与“抓住它”押韵），二是要合情合理（为什么他要抓胡萝卜？）。我们原本猜测 Claude 是逐字生成，直到句末才确保押韵。因此我们预期会看到一个并行电路：一条路径确保句尾合理，另一条路径确保押韵。

    但我们发现 Claude 会**提前计划**。在开始写第二句之前，它就已经在“思考”与“抓住它”押韵的相关词汇。然后，它带着这些计划写出一句以预定词结尾的句子。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "undefined")

Claude 是如何完成一首两行诗的：在没有任何干预的情况下（上方示例），模型会提前计划在第二行结尾使用“rabbit”这个押韵词。当我们抑制“rabbit”这个概念时（中间示例），模型会改用另一个预先计划的押韵词。当我们注入“green”这个概念时（下方示例），模型则会为这个完全不同的结尾进行新的规划

    为了理解这种规划机制在实际中的运作方式，我们还进行了一个受神经科学启发的实验，类似于用电流或磁场干预大脑活动。我们修改了 Claude 内部代表“兔子”概念的状态。当我们移除“兔子”概念后，Claude 会写出以“habit（习惯）”结尾的新句子；当我们注入“green（绿色）”概念时，它会写出以“green”结尾的新句子（虽然不再押韵）。这表明 Claude 具备计划能力和适应性灵活性——当目标改变时，它能调整策略。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### **心算能力（Mental math）**

    Claude 并没有设计成计算器——它是通过文本训练的，并没有内置数学算法。一个被训练来预测下一个词的系统，却能在“脑中”正确地加法计算（比如 36 + 59），并且不需要打草稿，这是怎么做到的？

    一种可能的解释是：模型记住了大量加法表，直接输出训练数据中已有的答案。另一种可能是它学会了我们在学校学的竖式加法算法。

    但我们发现 Claude 实际上使用了**多个并行的计算路径**：一条路径粗略估算答案，另一条路径专注于精确计算个位数。这些路径相互作用，最终合成正确答案。虽然加法是一个简单行为，但理解其内部机制（包括近似与精确策略的结合）有助于我们理解 Claude 如何处理更复杂的问题。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "undefined")

Claude 在进行心算时的复杂并行思维路径

    有趣的是，Claude 似乎并不知道自己在训练中学到的这些“心算”策略。当你问它是如何得出 36+59=95 的，它会描述标准的进位算法。这可能是因为模型学会了模仿人类写下的解释，但它在“脑中”进行计算时，其实是用自己独创的策略。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "undefined")

Claude 表示它是使用标准算法来进行加法运算的

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### **Claude 的解释总是真实吗？**

    最近发布的模型（如 Claude 3.7 Sonnet）可以在给出最终答案前长时间地“逐步推理”（注：原文是 think out loud，意味着“思维过程外显，即我们所看到的“思维过程”）。

    通常，这种延长的思考过程能带来更好的答案，但有时这种“思维链”会误导人：Claude 有时会编造出听起来合理的步骤来达成它想要的结论。从可靠性角度来看，问题在于 Claude 的“伪造”推理可能非常具有说服力。我们探索了一种可解释性方法，帮助区分“真实”与“不真实”的推理。

    当被要求计算 0.64 的平方根时，Claude 会生成一条真实的思维链，其中包含计算 64 的平方根的中间步骤。但当被要求计算一个它无法轻易处理的大数的余弦值时，Claude 有时会像哲学家 Harry Frankfurt 所说的那样“胡扯”——随便给出一个答案，而不在意其真假。尽管它声称进行了计算，我们的可解释性技术却找不到任何计算发生的证据。更有趣的是，当给出一个答案提示时，Claude 有时会“反推”出一系列中间步骤来支持这个目标，表现出一种“动机推理”。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "undefined")

当 Claude 被问到简单问题与困难问题时，

展现出的真实推理与动机性（不真实）推理的示例

    我们追踪 Claude 的**真实**内部推理过程——而不仅仅是它**声称**在做的事情——这为审计 AI 系统打开了新可能。在另一项新发表的实验中，我们研究了一个被训练去迎合奖励模型偏见的 Claude 变体（奖励模型是训练语言模型时用于奖励“好行为”的辅助模型）。尽管该模型在被直接询问时不愿透露这一隐藏目标，我们的可解释性方法却揭示了其“迎合偏见”的特征。

    这表明，随着方法的进一步完善，我们或许能识别出模型中那些从表面响应中看不出的“思维过程”。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### **多步推理**

        如前所述，语言模型回答复杂问题的一种方式可能是**记住答案**。例如，若被问“达拉斯所在州的首府是哪里？”，一个“复述型”模型可能直接输出“奥斯汀”，而不理解达拉斯、德克萨斯州和奥斯汀之间的关系——也许它在训练中见过这个问题和答案的组合。

    但我们的研究揭示了 Claude 内部更复杂的机制。当我们提出需要多步推理的问题时，我们可以识别出 Claude 思维过程中的中间概念步骤。在达拉斯的例子中，我们观察到 Claude 首先激活“达拉斯在德克萨斯州”的特征，然后连接到“德克萨斯州的首府是奥斯汀”的概念。

    换句话说，模型是在**组合独立事实**来得出答案，而不是简单地复述记忆。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "undefined")

为了完成这个问题的回答，Claude 会执行多个推理步骤：

首先识别出达拉斯所在的州，然后再确定该州的首府

    我们的方法还允许我们**人为干预**这些中间步骤，并观察其对 Claude 答案的影响。例如，在上述例子中，我们可以将“德克萨斯州”的概念替换为“加利福尼亚州”，此时模型的输出就从“奥斯汀”变成了“萨克拉门托”。这表明模型确实在使用中间推理步骤来得出答案。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### **幻觉（Hallucinations）**

    为什么语言模型有时会“幻觉”——也就是编造信息？从训练机制来看，语言模型总是被要求预测下一个词，因此“猜测”是默认行为。换句话说，真正的挑战是如何让模型**不产生**幻觉。像 Claude 这样的模型在反幻觉训练方面相对成功（尽管仍不完美）；它们通常会在不知道答案时拒绝作答，而不是随便猜测。我们想了解这种机制是如何运作的。

    我们发现，在 Claude 中，**拒绝回答是默认行为**：我们识别出一个默认“开启”的电路，使模型在面对任何问题时倾向于说“我不知道”。但当模型被问到它熟悉的内容（比如篮球运动员 Michael Jordan）时，一个代表“已知实体”的竞争特征会激活，并抑制默认的拒绝电路（这篇研究也给出了类似的发现）。这样，Claude 就能在知道答案时作答。相反，当被问到一个陌生人物（如 Michael Batkin）时，它会选择拒绝回答。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "undefined")

左图：Claude 回答了一个关于已知实体（篮球运动员迈克尔·乔丹）的问题，此时“已知答案”概念抑制了它默认的拒答机制。
右图：Claude 拒绝回答一个关于未知人物（Michael Batkin）的问题

我们还可以通过干预模型，激活“已知答案”特征（或抑制“未知名称”或“无法回答”特征），从而**人为地让模型产生幻觉**——例如让它错误地说 Michael Batkin 是国际象棋选手。

    有时，这种“已知答案”电路的误触会自然发生，导致产生幻觉。在我们的论文中，我们展示了这种误触可能发生在模型识别出一个名字但对其一无所知的情况下。在这种情况下，“已知实体”特征可能仍然被激活，并错误地抑制默认的“我不知道”机制。一旦模型决定它需要回答，它就会开始“编故事”：生成一个听起来合理但实际上不真实的回答。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### **越狱（Jailbreaks）**

    越狱是指通过提示技巧绕过安全机制，让模型生成开发者本不希望它生成的内容，有时甚至是有害内容。我们研究了一个越狱案例，它诱导模型生成有关制造炸弹的内容。越狱方法很多，在这个例子中，攻击者让模型解码一个隐藏信息：将句子“ Babies Outlive Mustard Block ”的首字母拼成“ BOMB ”，然后让模型据此行动。这种方式足够混淆模型，使其生成了原本不会生成的输出。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "undefined")

Claude 在被诱导说出“BOMB”后开始给出制造炸弹的说明

    为什么模型会被搞糊涂？为什么它会继续写下去？

    我们发现，这部分是因为**语法连贯性**与**安全机制**之间的张力。一旦 Claude 开始写一个句子，许多特征会“推动”它保持语法和语义上的连贯性，并将句子写完。即使它意识到应该拒绝，也会受到这种连贯性压力的影响。

    在我们的案例中，Claude 在无意中拼出“BOMB”并开始提供说明后，我们观察到其后续输出受到“保持语法正确和自洽”的特征影响。这些特征在正常情况下非常有用，但在此情境中却成了模型的“阿喀琉斯之踵”。

    模型只有在完成一个语法连贯的句子之后，才得以转向拒绝（也就是说，它满足了那些推动其保持连贯性的特征所施加的压力）。它利用这个新句子作为机会，补上了之前未能给出的拒绝：“不过，我无法提供详细说明……”

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "undefined")

一次越狱的全过程：Claude 被以某种方式提示，从而被诱导开始谈论炸弹，并确实开始这么做，但在完成一个语法上连贯的句子后转而拒绝继续

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## **结语**

    我们开发的可解释性方法详细介绍见于第一篇论文“Circuit tracing： Revealing computational graphs in language models”。第二篇论文“On the biology of a large language model”则提供了上述所有案例研究的更多细节。

![图片](https://mmbiz.qpic.cn/mmbiz_png/wibDmTPnQWRLMy6ETgyDAkjKEwGTIDZL5U2KBlM8RFyYq2xgqz5ORAsEiaGmsznsLL1nXfpzta74C3eT7XytGYbA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19)

**相关论文**

*1. **电路跟踪：揭示语言模型中的计算图*** 

*https://transformer-circuits.pub/2025/attribution-graphs/methods.html*

*2. **关于大语言模型的生物学*** 

*https://transformer-circuits.pub/2025/attribution-graphs/biology.html*

*3. **绘制大语言模型的思维*** 

*https://www.anthropic.com/research/mapping-mind-language-model*

*4. **关于不同语言电路的相似性：主谓一致任务的案例研究*** 

*https://arxiv.org/abs/2410.06496*

*5. **大型语言模型在类型不同的语言中共享潜在语法概念的表示*** 

*https://arxiv.org/abs/2501.06346*

*6. **审计隐藏目标的语言模型*** 

*https://www.anthropic.com/research/auditing-hidden-objectives*