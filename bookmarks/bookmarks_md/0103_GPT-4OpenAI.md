---
url: https://mp.weixin.qq.com/s/u72wzup-5DCQrJdNNYJwDA
title: "GPT-4最全攻略来袭！OpenAI官方发布，六个月攒下来的使用经验都在里面了"
description: "六大策略+实用技巧"
author: "关注前沿科技"
captured_at: "2026-03-08T10:30:10.593Z"
---

# GPT-4最全攻略来袭！OpenAI官方发布，六个月攒下来的使用经验都在里面了

##### 西风 发自 凹非寺
量子位 | 公众号 QbitAI

GPT-4官方使用指南炸裂登场啦！

你没听错，这次不需要自己做笔记了，OpenAI亲自帮你整理了一份。

据说汇聚了大伙儿6个月的使用经验，你、我、他的提示诀窍都融汇其中。

虽然总结下来只有**六大策略**，但该有的细节可绝不含糊。

不仅普通GPT-4用户可以在这份秘籍中get提示技巧，或许应用开发者也可以找到些许灵感。

网友们纷纷评论，给出了自己的“读后感”：

> 好有意思啊！总结来说，这些技巧的核心思想主要有两点。一是我们得写得更具体一些，给一些细节的提示。其次，对于那些复杂的任务，我们可以把它们拆分成一些小的提示来完成。

![图片](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtBEhmNRzfFhiazEdv4ADNgJmDKtxkSjoZJhqoSVYeFGcqbvshIVibXYZk4NUxD1WXZU4cJsxlOheNwg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

OpenAI表示，这份攻略目前仅针对GPT-4。（当然，你也可以在其它GPT模型上试试？）

赶紧瞧瞧，这份秘籍里究竟都有啥好东西。

## 6大干货技巧全在这

### 策略一：写清楚指令

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

要知道，模型可不会“读心术”，所以你得把你的要求明明白白地写出来。

当模型输出变得太啰嗦时，你可以要求它回答简洁明了。相反地，如果输出太过简单，你可以毫不客气地要求它用专业水平来写。

如果你对GPT输出的格式不满意，那就先给它展示你期望的格式，并要求它以同样的方式输出。

总之，尽量别让GPT模型自己去猜你的意图，这样你得到的结果就更可能符合你的预期了。

#### 实用技巧：

**1、有细节才能得到更相关的答案**

为了使输出和输入具有强相关性，一切重要的细节信息，都可以喂给模型。

比如你想让GPT-4：总结会议记录

就可以尽可能在表述中增加细节：

> 将会议记录总结成一段文字。然后编写一个Markdown列表，列出与会人员及其主要观点。最后，如果与会人员有关于下一步行动的建议，请列出来。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**2、要求模型扮演特定角色**

通过改变系统消息（system message），GPT-4会更容易扮演特定的角色，比在对话中提出要求的重视程度更高。

如规定它要回复一个文件，这份文件中的每个段落都要有好玩的评论：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**3、用分隔符清晰标示输入的不同部分**

用"""三重引号"""、<XML标记>、节标题等分隔符标记出文本的不同部分，可以更便于模型进行不同的处理。在复杂的任务中，这种标记细节就显得格外重要。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**4、明确指定完成任务所需的步骤**

有些任务按步骤进行效果更佳。因此，最好明确指定一系列步骤，这样模型就能更轻松地遵循这些步骤，并输出理想结果。比如在系统消息中设定按怎样的步骤进行回答。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**5、提供示例**

如果你想让模型输出按照一种不是能够很好描述出来的特定样式，那你就可以提供示例。如提供示例后，只需要告诉它“教我耐心”，它就会按照示例的风格，将其描述得生动形象。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**6、指定所需输出长度**

你还可以要求模型具体生成多少个单词、句子、段落、项目符号等。但是，在要求模型生成特定数量的单词/字的时候，它有可能不会那么精准。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 策略二：提供参考文本

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

当涉及到深奥的话题、引用和URL等内容时，GPT模型可能会一本正经地胡说八道。

为GPT-4提供可以参考的文本，能够减少虚构性回答的出现，使回答的内容更加可靠。

#### 实用技巧：

**1、让模型参照参考资料进行回答**

如果我们能够向模型提供一些和问题有关的可信信息，就可以指示它用提供的信息来组织回答。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**2、让模型引用参考资料进行回答**

如果在上面的对话输入中已经补充了相关信息，那么我们还可以直接要求模型在回答中引用所提供的信息。

这里要注意的是，可以通过编程，对让模型对输出中引用的部分进行验证注释。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 策略三：拆分复杂任务

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

相比之下，GPT-4在应对复杂任务时出错率更高。

然而，我们可以采取一种巧妙的策略，将这些复杂任务重新拆解成一系列简单任务的工作流程。

这样一来，前面任务的输出就可以被用于构建后续任务的输入。

就像在软件工程中将一个复杂系统分解为一组模块化组件一样，将任务分解成多个模块，也可以让模型的表现更好。

#### 实用技巧：

**1、进行意图分类**

对于需要处理不同情况的大量具有独立性的任务，可以先对这些任务进行分类。

然后，根据分类来确定所需的指令。

比如，对于客户服务应用程序，可以进行查询分类（计费、技术支持、账户管理、一般查询等）。

当用户提出：

> 我需要让我的互联网重新恢复正常。

根据用户查询的分类，可以锁定用户的具体诉求了，就可以向GPT-4提供一组更具体的指令，来进行下一步操作。

例如，假设用户需要在“故障排除”方面寻求帮助。

就可以设定下一步的方案：

> 要求用户检查路由器的所有电缆是否已连接……

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**2、对先前对话进行概括或筛选**

由于GPT-4的对话窗口是有限制的，上下文不能太长，不能在一个对话窗口中无限进行下去。

但也不是没有解决办法。

方法之一是对先前的对话进行概括。一旦输入的文本长度达到预定的阈值，就可以触发一个查询，概括对话的一部分，被概括出来的这部分内容可以变成系统消息的一部分。

此外，可以在对话过程中就在后台对前面的对话进行概括。

另一种方法是检索先前的对话，使用基于嵌入的搜索实现高效的知识检索。

**3、逐段概括长文档，并递归构建完整概述**

还是文本过长的问题。

比如你要让GPT-4概括一本书，就可以使用一系列查询来概括这本书的每个部分。

然后将部分概述连接起来进行总结，汇成一个总的答案。

这个过程可以递归进行，直到整本书被概括。

但是有些部分可能要借前面部分的信息才能理解后续部分，这里有一个技巧：

在概括当前内容时，将文本中当前内容之前的内容概述一起总结进来，进行概括。

简单来说，用前面部分的“摘要”+当前部分，然后进行概括。

OpenAI之前还使用基于GPT-3训练的模型，对概括书籍的效果进行了研究。

### 策略四：给GPT时间“思考”

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

如果让你计算17乘28，你可能不会立刻知道答案，但是可以通过一些时间计算出来。

同样的道理，当GPT-4接收到问题时，它并不会花时间仔细思考，而是试图立刻给出答案，这样就可能导致推理出错。

因此，在让模型给出答案前，可以先要求它进行一系列的推理过程，帮助它通过推理来得出正确的答案。

#### 实用技巧：

**1、让模型制定解决方案**

你可能有时候会发现，当我们明确指示模型在得出结论之前从基本原理出发进行推理时，我们可以获得更好的结果。

比如说，假设我们希望模型评估学生解答数学问题的方案。

最直接的方法是简单地询问模型学生的解答是否正确。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在上图中，GPT-4认为学生的方案是正确的。

但实际上学生的方案是错误的。

这时候就可以通过提示模型生成自己的解决方案，来让模型成功注意到这一点。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在生成了自己的解决方案，进行一遍推理过后，模型意识到之前学生的解决方案不正确。

**2、隐藏推理过程**

上面讲到了让模型进行推理，给出解决方案。

但在某些应用中，模型得出最终答案的推理过程不适合与用户共享。

比如，在作业辅导中，我们还是希望鼓励学生制定自己的解题方案，然后得出正确答案。但模型对学生解决方案的推理过程可能会向学生揭示答案。

这时候我们就需要模型进行“内心独白”策略，让模型将输出中要对用户隐藏的部分放入结构化格式中。

然后，在向用户呈现输出之前，对输出进行解析，并且仅使部分输出可见。

就像下面这个示例：

先让模型制定自己的解决方案（因为学生的有可能是错的），然后与学生的解决方案进行对比。

如果学生的答案中哪一步出错了，那就让模型针对这一步给出一点提示，而不是直接给学生完整的正确的解决方案。

如果学生还是错了，那就再进行上一步的提示。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

还可以使用“查询”策略，其中除了最后一步的查询以外，所有查询的输出都对用户隐藏。

首先，我们可以要求模型自行解决问题。由于这个初始查询不需要学生的解决方案，因此可以省略掉。这也提供了额外的优势，即模型的解决方案不会受到学生解决方案偏见的影响。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

接下来，我们可以让模型使用所有可用信息来评估学生解决方案的正确性。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

最后，我们可以让模型使用自己的分析来构建导师的角色。

> 你是一名数学导师。如果学生回答有误，请以不透露答案的方式向学生进行提示。如果学生答案无误，只需给他们一个鼓励性的评论。

**3、询问模型是否遗漏了内容**

假设我们正在让GPT-4列出一个与特定问题相关的源文件摘录，在列出每个摘录之后，模型需要确定是继续写入下一个摘录，还是停止。

如果源文件很大，模型往往会过早地停止，未能列出所有相关的摘录。

在这种情况下，通常可以让模型进行后续查询，找到它在之前的处理中遗漏的摘录。

换而言之，模型生成的文本有可能很长，一次性生成不完，那么就可以让它进行查验，把遗漏的内容再补上。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 策略五：其它工具加持

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

GPT-4虽然强大，但并非万能。

我们可以借助其他工具来补充GPT-4的不足之处。

比如，结合文本检索系统，或者利用代码执行引擎。

在让GPT-4回答问题时，如果有一些任务可以由其他工具更可靠、更高效地完成，那么我们可以将这些任务交给它们来完成。这样既能发挥各自的优势，又能让GPT-4发挥最佳水平。

#### 实用技巧：

**1、使用基于嵌入的搜索实现高效的知识检索**

这一技巧在上文中已经有所提及。

若在模型的输入中提供额外的外部信息，有助于模型生成更好的回答。

例如，如果用户询问关于一部特定电影的问题，将关于电影的信息（例如演员、导演等）添加到模型的输入中可能会很有用。

嵌入可用于实现高效的知识检索，可以在模型运行时动态地将相关信息添加到模型的输入中。

文本嵌入是一种可以衡量文本字符串相关性的向量。相似或相关的字符串将比不相关的字符串更紧密地结合在一起。加上快速向量搜索算法的存在，意味着可以使用嵌入来实现高效的知识检索。

特别的是，文本语料库可以分成多个部分，每个部分可以进行嵌入和存储。然后，给定一个查询，可以进行向量搜索以找到与查询最相关的语料库中的嵌入文本部分。

**2、使用代码执行进行更准确的计算或调用外部API**

不能仅依靠模型自身进行准确地计算。

如果需要，可以指示模型编写和运行代码，而不是进行自主计算。

可以指示模型将要运行的代码放入指定的格式中。在生成输出后，可以提取和运行代码。生成输出后，可以提取并运行代码。最后，如果需要，代码执行引擎（即Python解释器）的输出可以作为下一个输入。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

代码执行的另一个很好的应用场景是调用外部API。

如果将API的正确使用方式传达给模型，它可以编写使用该API的代码。

可以通过向模型演示文档和/或代码示例来指导模型如何使用API。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在这里OpenAI提出了特别警告⚠️：

> 执行模型生成的代码在本质上来说并不安全，任何试图执行此操作的应用程序中都应采取预防措施。特别是，需要一个沙盒代码执行环境来限制不受信任的代码可能造成的危害。

### 策略六：系统地测试更改

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

有时候很难确定一个改变是会让系统变得更好还是更差。

通过观察一些例子有可能会看出哪个更好，但是在样本数量较少的情况下，很难区分是真的得到了改进，还是只是随机运气。

也许这个“改变”能够提升某些输入的效果，但却会降低其它输入的效果。
而评估程序(evaluation procedures，or “evals”)对于优化系统设计来说非常有用。好的评估有以下几个特点：

1）代表现实世界的用法（或至少是多种用法）

2）包含许多测试用例，可以获得更大的统计功效（参见下表）

3）易于自动化或重复

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

对输出的评估可以是由计算机进行评估、人工评估，或者两者结合进行。计算机可以使用客观标准自动评估，也可以使用一些主观或模糊的标准，比如说用模型来评估模型。

OpenAI提供了一个开源软件框架——OpenAI Evals，提供了创建自动评估的工具。

当存在一系列质量同样高的输出时，基于模型的评估就会很有用。

#### 实用技巧：

**1、参考黄金标准答案评估模型输出**

假设已知问题的正确答案应参考一组特定的已知事实。

然后，我们可以询问模型答案中包含多少必需的事实。

例如，使用下面这个系统消息，

给出必要的既定事实：

> 尼尔·阿姆斯特朗是第一个在月球上行走的人。
>
> > 尼尔·阿姆斯特朗第一次登上月球的日期是1969年7月21日。

如果答案中包含既定给出的事实，模型会回答“是”。反之，模型会回答“否”，最后让模型统计有多少“是”的答案：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

下面是包含两点既定事实的示例输入（既有事件，又有时间）：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

仅满足一个既定事实的示例输入（没有时间）：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

而下面这个示例输入，不包含任何一个既定事实：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这种基于模型的评估方法有许多可能的变化形式，需要跟踪候选答案与标准答案之间的重叠程度，并追踪候选答案是否与标准答案的有相矛盾的地方。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

比如下面的这个示例输入，其中包含不合标准的答案，但与专家答案（标准答案）并不矛盾：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

下面是这个示例输入，其答案与专家答案直接矛盾（认为尼尔·阿姆斯特朗是第二个在月球上行走的人）：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

最后一个是带有正确答案的示例输入，该输入还提供了比必要内容更多的详细信息（时间精确到了02:56，并指出了这是人类历史上的一项不朽成就）：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

传送门：
https://github.com/openai/evals（OpenAI Evals）

参考链接：
\[1\]https://platform.openai.com/docs/guides/gpt-best-practices
\[2\]https://www.reddit.com/r/OpenAI/comments/141yheo/openai\_recently\_added\_a\_gpt\_best\_practices\_guide/

— **完** —

**「AIGC+垂直领域社群」**

**招募中！**

欢迎关注AIGC的伙伴们加入AIGC+垂直领域社群，一起学习、探索、创新AIGC！

请备注您想加入的垂直领域「教育」或「电商零售」，加入AIGC人才社群请备注「人才」&「姓名-公司-职位」。

![图片](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtBfwiaVSmZS2cUzMVzacLtCdVGu0aH1DlLR7GJv3nAynJibjMzFhLFB1CGhVr0jrFqyGkQuqoDuqAQg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=33)

**点这里👇关注我，记得标星哦～**

**一键三连「分享」、「点赞」和「在看」**

**科技前沿进展日日相见 ~** 

![图片](https://mmbiz.qpic.cn/mmbiz_svg/g9RQicMD01M0tYoRQT2cMQRmPS5ZDyrrfzeksiay90KaDzlGBH61icqHxmgFKfvfXtVuwTHV740CDLAaXU1LIfZyoJEpYKcRIiaE/640?wx_fmt=svg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=34)