---
url: https://mp.weixin.qq.com/s/_wXjuAo7q5Nkn1l_ormcmQ
title: "放弃永生的凡人计算：AI教父Hinton 智源大会闭幕主题演讲  (附中文视频）"
description: "最后一页或许才是Hinton最想说的..."
author: "天空之城城主"
captured_at: "2026-03-08T10:29:58.763Z"
---

# 放弃永生的凡人计算：AI教父Hinton 智源大会闭幕主题演讲  (附中文视频）

作者：城主

前言

昨天AI教父连线北京智源大会做了闭幕主题演讲。时长30分钟。

本以为Hinton还是类似之前上多个视频访谈那样，泛谈AGI超级人工智能如何控制人类的顾虑；但错了，AI教父带给我们的是一项让他相信超级智能将会比预期快得多的研究：**凡人计算（Mortal Computation）**。

实际上，演讲描述了一种新的计算结构，在抛弃了软硬件分离的原则后，即不再用反向传播描述神经网络内部路径的情况下，如何实现智能计算。

演讲小部分时间偏技术， 但教父就是教父，整个PPT没公式只讲概念，依然把最前沿的算法思想讲得清清楚楚。

全新的计算模式之所以被Hinton称为 Mortal computation，寓意是深刻的：

1）之前Hinton说过，永生事实上已经实现。因为当前的AI大语言模型已把人类知识学习到了千万亿的参数里，且硬件无关：只要复刻出指令兼容的硬件，同样的代码和模型权重在未来都可以直接运行。在这个意义上，人类智慧（而不是人类）永生了。

2）但是，这种软硬件分开的计算在实现的能量效率和规模上是极其低效的。如果抛弃硬件和软件分离的计算机设计原则，把智能实现在一个统一的黑盒子里，将是实现智能的一种新道路。

4）这种软硬件不再分离的计算设计将极大幅度降低能耗和计算规模（考虑一下，人脑的能耗才20瓦）

5）但同时，意味着无法高效的复制权重来复制智慧，即放弃了永生。

B站传送：【【中文精校】AI教父Hinton智源大会闭幕演讲 “智能的两种道路”-哔哩哔哩】 

https://b23.tv/YxlsUKL

其实吧，作者对整个演讲，印象最深的是Hinton在最后说的这句：

**我看不出如何防止这种情况发生，但我老了。我希望像你们这样的许多年轻而才华横溢的研究人员会弄清楚我们如何拥有这些超级智能**

不防备看到这么一句， 一种“前辈即将离开之际，对人类未来不甘和对新人寄望交代”的苍凉感扑面而来，简直了。

最后，Hinton放出PPT的最后一页， **THE END**，真是意味深长。。。作者寻思，是不是Hinton讲了那么多，最后一句，才是他真想说的...

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

*（注：新的神经网络方法也被称为Forward-Forward（FF）网络，用以取代Hinton自己发明的现代所有神经网络的核心基础：反向传播技术。Hinton 提出，FF网络可能更合理地接近现实生活中在大脑中发生的情况。论文在22年底提出:*

 *https://www.cs.toronto.edu/~hinton/FFA13.pdf ）*

*主持人：*

*嗨，Hinton教授，很荣幸今天能请到您。*

*5月，您离开了谷歌，以便能够更自由地谈论人工智能带来的生存风险。我听说在那个决定之后，你每隔几秒钟就会收到一次采访和媒体邀请。因此，我们感到非常幸运，您能够抽出时间与我们交谈。*

*我现在将把它交给你来发表我们的闭幕主题演讲。*

*![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)*

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**我今天要谈的是使我相信超级智能比我想象的要近得多的研究。**

所以我想谈两个问题，我将几乎完全关注第一个问题，即人工神经网络很快会比真实神经网络更智能吗？就像我说的那样，我将描述使我得出结论认为这可能很快就会发生的研究。

就在最后，我会稍微谈谈我们是否可以控制超级智能人工智能，但这不是谈话的主题。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

因此，**在传统计算中，计算机被设计为精确地遵循指令。我们可以在不同的物理硬件上运行完全相同的程序或相同的神经网络，**因为它们被设计为精确地遵循指令，这意味着程序或**神经网络的权重中的知识是不朽的。它不依赖于任何特定的硬件。**

现在要实现**这种永生需要付出高昂的代价**。我们必须以高功率运行晶体管，以便它们以数字方式运行，我们无法利用硬件的所有丰富的模拟和高度可变的特性。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

数字计算机存在的原因，以及它们精确地遵循指令的原因，是因为它们的设计是让我们看到一个问题，会弄清楚需要采取什么步骤来解决问题，然后告诉计算机采取这些步骤。

但这已经改变了，**我们现在有一种让计算机做事的不同方式，那就是从例子中学习。**我们只是向他们展示我们希望他们做什么，并且由于您让计算机做您想做的事情的方式发生了这种变化，**现在可以放弃计算机科学最基本的原则，即软件应该与硬件分开。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

所以在我们放弃软硬件分开的原则之前，让我们先回顾一下为什么它是一个很好的原则。

由于这种可分离性，我们可以在不同的硬件上运行相同的程序。我们还可以担心程序的属性，并在神经网络上研究程序的属性，而不必担心电子学，这就是为什么你可以拥有不同于电气工程系的计算机科学系。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**如果我们真的放弃软件和硬件的分离，我们就会得到我称之为凡人计算的东西**。

它显然有很大的缺点，但它也有一些巨大的优点，所以我开始研究凡人计算，以便能够**以更少的能量运行大型语言模型之类的东西，特别是能够使用更少的能量来训练它们。**

因此，我们从**放弃永生中获得的巨大好处是放弃硬件（身体）和软件（灵魂）的分离，我们可以节省大量能源，因为我们可以使用非常低功耗的模拟计算，而这正是大脑正在做的事情。**

它确实有一位数字计算，因为神经元要么发射要么不发射，但大部分计算都是以模拟方式完成的，而且可以在非常低的功率下完成。

我们还可以获得更便宜的硬件，因此目前硬件必须在2D中非常精确地制造，我们实际上可以拥有您只需在3D中生长的硬件，因为我们不需要确切地了解硬件的连接性或每个部件的确切方式有用。

显然，要做到这一点将需要大量新的纳米技术，或者可能需要对生物神经元进行基因改造，因为生物神经元将大致按照我们的意愿行事。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在我深入探讨凡人计算的所有缺点之前，我只想给你一个计算示例，可以明显的通过使用模拟硬件以更便宜的方式完成计算。

因此，如果你想将一个神经活动向量乘以一个权重矩阵，这就是神经网络的核心计算，大部分工作量都在这。我们目前所做的是驱动非常高功率的晶体管来表示数字的数字表示中的位，然后我们执行n阶平方运算将两个n位数字相乘。

我的意思是这可能是计算机上的一个操作，但它是n平方位操作。

另一种方法是将神经活动实现为电压和权重作为电导，然后每单位时间电压乘以电导给你一个电荷，电荷将自己加起来，所以现在很明显你可以如何将电压向量乘以电导矩阵。

这大大提高了能源效率。以这种方式工作的芯片已经存在。不幸的是，**人们随后所做的是尝试使用非常昂贵的ATG转换器将模拟答案转换为数字答案。如果可以的话，我们希望完全留在模拟领域。**

但问题是不同的硬件最终会计算出略有不同的东西。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

因此，凡人计算的主要问题是，学习过程必须利用它所运行的硬件的特定模拟属性，而无需确切知道这些属性是什么。

例如，不知道将神经元的输入与神经元的输出相关联的确切函数，并且可能不知道连接性。这意味着我们不能使用反向传播算法之类的东西来获得梯度，因为反向传播是前向传播的精确模型。（注：模拟计算意味着无法得到内部的精确模型）

所以问题是，如果我们不能使用反向传播，我们还能做什么，因为我们现在都高度依赖反向传播。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

所以这里有一个非常简单明了的学习过程，人们已经谈论了很多。

为网络中的每个权重生成一个由小的临时扰动组成的随机向量。然后你测量一个小批量示例的全局目标函数的变化。然后你通过改进的目标函数去缩放扰动向量，以永久地改变权重。

因此，如果目标函数变得更糟，您显然会朝另一个方向前进。这个算法的好处是，平均而言，它的行为与反向传播相同，因为平均而言，它遵循梯度。它的问题在于它具有非常高的方差。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

因此，当您选择一个随机方向移动以考虑权重空间时所产生的噪声与网络的大小成正比。这意味着这种算法适用于少量连接，但不适用于大型网络。

所以这里有一些效果更好的东西。它仍然有类似的问题，但**比扰动权重要好得多。那就是扰乱活动**。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

也就是说，您考虑对每个神经元的总输入进行扰动的随机向量。

当您对一小批示例进行随机扰动时，您会查看目标函数会发生什么。由于这种扰动，您会得到目标函数的差异。然后您可以计算如何更改神经元的每个传入权重以遵循梯度。同样，它只是梯度的随机估计，但与扰乱权重相比，它的噪音要小得多。而且这个算法足以学习像MNIST这样的简单任务。

如果你使用非常非常小的学习率，它的行为与反向传播完全一样，但速度要慢得多，因为你需要使用非常小的学习率。如果你使用更大的学习率，它会很嘈杂，但它仍然适用于像MNIST这样的东西。但它的效果还不够好，无法将其扩展到大型神经网络。

那么我们可以做些什么来扩大规模呢？

好吧，有两种方法可以使事情规模化。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

我们可以尝试找到可以应用于小型神经网络的目标函数，而不是试图找到适用于大型神经网络的学习算法。

所以我们的想法是训练一个大的神经网络。我们要做的是有很多适用于网络小部分的小目标函数。所以每一小组神经元都有自己的局部目标函数。现在可以使用这种活动扰动算法来学习小型多层神经网络。它将以与反向传播大致相同的方式学习，但噪声更大。然后我们通过拥有更多小的局部神经元组将其扩展到更大的网络。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

那么这就引出了这些目标函数从何而来的问题。

一种可能性是对局部补丁进行无监督学习，该局部补丁具有图像的多个表示级别，并且每个级别都有局部补丁。并在特定图像上制作每个局部补丁，制作该局部神经网络的输出，尝试与所有其他局部补丁产生的平均表示一致。因此，您试图在从本地补丁中提取的内容，与从同一图像中的所有其他本地补丁中提取的内容达成一致。

这是经典的对比学习。您还试图不同意您为该级别的其他图像提取的内容。

我们如何做到这一点的具体细节更加复杂，我不打算深入探讨这些细节。但是我们可以让这个算法工作得很好，每个表示级别都有几个隐藏层，所以你可以做非线性的事情。

这些级别使用活动扰动贪婪地学习，并且没有反向传播到较低级别。所以它不会像反向传播那样强大，因为它不能反向传播很多很多层。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Mengye Ren 为使该算法发挥作用投入了大量工作，他证明了它可以适度发挥作用。它的效果可能比提出的任何其他算法都要好，这些算法可能是现实的，可以在真实的神经网络中运行。但是让它发挥作用很棘手，而且它仍然不如反向传播。当你使网络更深时，它会变得比反向传播更糟糕。

所以我没有深入探讨此方法的所有细节，因为您可以在ICLR和网络上的一篇论文中阅读它们。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

那么现在让我谈谈凡人计算的另一个大问题。

所以总而言之，**到目前为止，我们还没有找到一个真正好的可以利用模拟属性的学习算法，但我们有一个学习算法还可以**，并且足够好，可以很好地学习像MNIST这样的东西，并且学习像ImageNet这样更大的东西，但不是很好。

所以**凡人计算的第二个大问题是它的生命有限性（Mortality）。当一个特定的硬件死掉时，它学到的所有知识也随之死去，因为知识和硬件的细节错综复杂地纠缠在一起。**因此，**该问题的最佳解决方案是在硬件失效之前，将知识从老师那里提取给学生**。这就是我现在想做的。

教师向学生展示对各种输入的正确反应，然后学生尝试模仿教师的反应。如果你看看特朗普的推文是如何运作的，人们会非常沮丧，因为他们说特朗普说的是假话。他们认为他是在试图描述事实，而事实根本不是这样。特朗普所做的是采取一种情况并对这种情况做出反应，对这种情况做出非常情绪化的反应，这让他的追随者能够接受这种情况并弄清楚如何改变他们神经网络中的权重，这样他们就会给出对那种情况有同样的情绪反应。这与事实无关。那就是让邪教领袖对邪教追随者做出顽固的回应，但效果很好。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

因此，如果我们考虑蒸馏的效果如何，请考虑将图像分类为大约一千个非重叠类别的代理。

*（注：模型蒸馏，最早在 2006 年由 Buciluǎ 提出。Hinton 进行了发展并在 2015 年发表了著名的 《Distilling the Knowledge in a Neural Network “从神经网络中提取知识”》。*

*出于计算资源的限制或效率的要求，深度学习模型在部署推断时往往需要进行压缩，模型蒸馏方法将原始数据集上训练的重量级模型作为教师，让一个相对更轻量（参数更少）的模型作为学生。*

***对于相同的输入，让学生输出的概率分布尽可能的逼近教师输出的分布，则大模型的知识就通过这种监督训练的方式「蒸馏」到了小模型里。小模型的准确率往往下降很小，却能大幅度减少参数量，从而降低对硬件和和能耗的需求。****）*

指定正确答案只需要大约10位信息。因此，当您在训练示例上训练该代理时，如果您告诉它正确的答案，您只是对网络的权重施加了10位的约束。那没有太大的限制。

但是现在假设我们训练一个agent来同意一个老师对这1024个班级给出的回答，也就是得到相同的概率分布。该分布有1023个实数，这提供了数百倍的约束，假设这些概率都不是很小的。所以不久之前，我和Ori O'Vignals、Jeff Dean研究了蒸馏并证明它可以很好地工作。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

确保老师的输出概率都不小的方法是在高温下运行老师，并且在训练学生时也在高温下运行学生。所以你采用logits，这就是进入softmax的东西，对于老师来说，你按温度缩放它们，然后你得到一个更柔和的分布。你在训练学生时使用相同的温度，而不是在MNIST中使用学生，只是在训练学生时

（注：提高温度系数会使得输出分布的信息熵增加）。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

所以我只想给你看一个蒸馏的例子。这是来自MNIST训练集的两张各种图像。而我给大家展示的是当你在老师身上使用高温时，老师分配给各个类别的概率。

对于第一行，很有信心是二。如果你看第二行，它很确定那是一个二，但它也认为它可能只是一个三或者它可能是一个八。所以如果你看一下，你会发现二比其他两个更像八。如果你看第三行，特别明显的是二很像零。老师告诉学生，当你看到那个时，你应该说2，但你也应该在0上小注。

所以学生现在从这个例子中学到的东西比仅仅告诉它是二的要多得多。它正在学习它看起来有点像的其他东西。如果你看第四行，你会发现它非常有信心它是2，但它也认为它可能是1的可能性非常小。它真正认为可能是一个的其他两个都不是，也许是第一行。而我所做的就是画出它认为可能是的那个。所以你可以明白为什么它看起来像一个，因为偶尔会有一些像那个一样在顶部有一点，在底部有一点。也就是那种两人长得有点像的。然后如果你看最后一个，那是老师实际上错了的一个。老师以为是五。根据MNIST标签，它实际上是一个二。

再一次，学生可以从那里老师的错误中学到很多东西。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

好吧，我特别喜欢蒸馏的一个特殊性质，那就是**当你用老师的概率训练学生时，你是在训练学生以与老师相同的方式进行概括。那就是通过给错误答案赋予小概率来泛化到错误答案。**

通常当你训练一个模型时，你训练它以获得关于训练数据的正确答案，然后希望它能正确地泛化到测试数据。你试着让它不要太复杂，或者你做各种其他事情，希望它能正确概括。但是在这里，当你训练学生时，你是在直接训练学生进行泛化，因为它正在被训练以与老师相同的方式进行泛化。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

显然，您可以创建更丰富的蒸馏输出，而不是给标签一个图像，而是给它一个标题，然后训练学生预测标题中的单词，和老师一样。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

我现在想谈谈代理人社区如何共享知识。因此，与其考虑个体代理，不如考虑在社区内共享知识。

事实证明，**社区共享知识的方式很大程度上决定了进行计算的方式。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

有了数字模型，有了数字智能，你可以拥有一大堆使用完全相同权重副本的代理，并以完全相同的方式使用权重。

这意味着你可以采用所有这些智能体，不同的智能体可以查看训练数据的不同部分，它们可以为训练数据的这些部分的权重计算梯度，然后它们可以对它们的梯度进行平均。

所以现在，每个模型都从每个模型看到的数据中学习。这意味着，**你获得了查看大量数据的巨大能力，因为你可以让模型的不同副本查看不同的数据位，并且它们可以非常有效地共享它们学到的东西，只需共享梯度或分享权重。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

如果你有一个拥有一万亿权重的模型，这意味着每次他们共享东西时你都会获得一万亿位的带宽。但**这样做的代价是你必须拥有以完全相同的方式行事的数字代理，以完全相同的方式使用权重。这对于制造和运行而言都是非常昂贵的能源成本。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**因此，使用权重共享的替代方法是使用蒸馏。**

如果它们具有不同的架构，这就是我们已经对数字模型所做的事情。但如果您的生物模型正在利用特定硬件的模拟特性，那么这就是您必须做的事情。**那时你不能分享权重。所以你必须使用蒸馏来分享知识。这就是这次谈话的内容。**

正如您所看到的，它不是很有效。使用蒸馏很难分享知识。我写句子，你试着想办法改变你的权重，这样你就能写出相同的句子。但它的带宽远低于仅共享梯度。

每个受过教育的人都希望能够将他们所知道的知识直接灌输到学生的大脑中。那太好了。那将是大学的终结。但我们不会那样工作，因为我们是生物智能，我的权重对你没用。

(注：Hinton这里的潜台词是，蒸馏实际上是更符合生物智能的算法结构，因为它和生物一样，无法复制另一个的权重。这让人想起，Hinton一生致力的，都是寻找大脑工作的方式）

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

所以到目前为止的故事是有两种不同的计算方法。利用数字计算和利用模拟特性的生物计算。它们在不同代理之间共享知识的效率方面有很大差异。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

因此，如果您查看大型语言模型，它们会使用数字计算和权重共享。但是**模型的每个副本，每个代理，都以非常低效的方式从文档中获取知识。它实际上是一种非常低效的蒸馏形式。**

比如它需要一个文件，它试图预测下一个词。并且没有显示教师对下一个单词的概率分布。它只是被显示为一个随机选择。这就是文档的作者选择放在下一个词中的内容。所以这是非常低的带宽。这就是这些大型语言模型向人们学习的方式。

所以**每个副本通过蒸馏学习效率非常低。但是你有几千份**。这就是为什么他们比我们学到的东西多数千倍。所以**我相信这些大型语言模型比任何人知道的都多数千倍。**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

现在的问题是，**如果这些数字智能不是通过蒸馏非常缓慢地向我们学习，而是开始直接从现实世界学习，将会发生什么？**

我应该说，**尽管他们向我们学习时升华速度很慢，但他们正在学习非常抽象的东西。**所以人类在过去的几千年里已经学到了很多关于这个世界的东西。**这些数字智能现在的好处是我们可以用语言表达我们学到的东西**（注：语言是我们对世界的抽象）。因此，他们可以捕捉到人类在过去几千年中记录在案的关于世界的一切知识。

但是每个数字代理的带宽仍然很低，因为他们正在从文档中学习。如果他们可以通过对视频建模进行无监督学习，例如，如果我们一旦找到一种有效的方法来训练这些模型来对视频建模，他们就可以从YouTube的所有内容中学习，这是大量的数据。如果他们能够操纵物理世界，那也会有所帮助。所以如果他们有机器人手臂等等。

但我相信，一旦这些数字代理人开始这样做，他们将能够比人类学到更多，而且他们将能够学得非常快。所以这让我想到了我在开头提到的另一点，即如果这些东西变得比我们更聪明会发生什么？

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

很明显，这（'超级智能会如何取得控制'）就是这次会议的主要内容。但我的主要贡献只是说，我认为这些超级智能可能比我过去认为的要快得多。不良行为者会想利用它们来做诸如操纵选民之类的事情。为此，他们已经在美国和许多其他地方使用它们。为了赢得战争。

如果你想让超级智能更有效率，你需要让它创建子目标。现在，这有一个明显的问题。有一个非常明显的子目标，它或多或少对你想要实现的任何事情都非常有帮助。那就是获得更多的权力，获得更多的控制权。您拥有的控制权越多，实现目标就越容易。而且**我发现很难看出我们将如何阻止数字智能试图获得更多控制权以实现他们的其他目标。**

因此，一旦他们开始这样做，我们就会遇到问题。一个超级智能会发现很容易通过操纵人来获得更多的权力。我们不习惯思考比我们聪明得多的事情。以及我们将如何与他们互动。

但在我看来很明显，它会学会非常擅长欺骗人，因为它通过在小说和马基雅维利等作品中看到我们欺骗他人的所有例子进行了大量练习。一旦你非常擅长欺骗人，你就可以让人们实际执行你喜欢的任何动作。因此，例如，如果您想入侵华盛顿的一座建筑物，则无需前往那里。你只是欺骗人们认为他们通过入侵大楼来拯救民主。我觉得这很可怕。

现在，我看不出如何防止这种情况发生，**但我老了。我希望像你们这样的许多年轻而才华横溢的研究人员会弄清楚我们如何拥有这些超级智能，**这将使我们的生活在没有他们控制的情况下变得更好。

我们有一个优势，一个相当小的优势，就是这些东西没有进化。我们建造了它们。可能是因为它们没有进化，所以它们没有原始人所具有的竞争性、攻击性目标。也许我们可以提供帮助。那会有所帮助。也许我们可以给他们道德原则。

但目前，我只是很紧张，因为我不知道在智力差距很大时，更聪明的东西被更不聪明的东西控制的例子。我想举的例子是假设青蛙发明了人。你认为现在谁将负责，青蛙还是人民？

这让我看到最后一张幻灯片，也就是结尾"THE END"。

![图片](https://mmbiz.qpic.cn/mmbiz_png/V08icaMk7MVYtHl74qKIOatibwL3HNkXicuAnqHemiafCZrztibwyQqpykV5VMktsxq2PkN7pgxibMP60A21u9Pexuyw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=29)

*主持人：*

*Hinton 教授，非常感谢您分享您对人类失去对超级智能的控制的见解和担忧。我希望人类能够迎接这一全球挑战。再一次，很荣幸今天有你和我们在一起。*

*让我们再次为 Hinton 教授鼓掌。非常感谢。*