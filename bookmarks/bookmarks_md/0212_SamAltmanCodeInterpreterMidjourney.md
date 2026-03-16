---
url: https://mp.weixin.qq.com/s/MKhc17x9MrqBSsmNA-qhJA
title: "Sam Altman：大家如此喜爱Code Interpreter！这是结合Midjourney的神奇用例"
description: "谁是Code Interpreter最佳拍档？Midjourney当仁不让"
captured_at: "2026-03-08T10:56:51.454Z"
---

# Sam Altman：大家如此喜爱Code Interpreter！这是结合Midjourney的神奇用例

机器之心报道

**编辑：杜伟**

> 如何让 ChatGPT 干些以前做不到的事？让它自己去写代码解决吧。

当人们问 ChatGPT 问题时，大语言模型（LLM）会通过不断预测下一个单词的方式生成答案。

但当全新的代码解释器（Code Interpreter）启用时，ChatGPT 会编写并运行一段计算机代码来寻找答案，这可以让它完成此前难以企及的新任务，比如执行复杂的计算、根据用户上传的数据生成图表，这些都是由代码完成的。

很多人认为，Code Interpreter 减少了大模型出现幻觉的问题。

几天前，OpenAI 正式开放了其 Code Interpreter 插件。本周四，ChatGPT Plus 的订阅者可以使用它。该插件允许 ChatGPT 分析数据、创建图表、解决数学问题和编辑文件等用途。它还支持上传和下载文件。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gW9D7TQnBlKKjO52St3iaVlWZ2621CADA70UXrdEq2MzURoYWYNqz72r8L1elVVb5PXZo1Klia6rIQ4A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

一时之间，各路人马都在使用这种新方法解决难题。

但 Code Interpreter 的潜能是不是只在这些领域呢？显然不是。该插件与 ChatGPT 的组合有更广阔的应用空间。

而Code Interpreter ，也成功地为 ChatGPT 带来新的关注与流量。今日，OpenAI CEO Sam Altman 发布 Twitter 表示大家如此喜欢代码解释器，我很高兴。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在这篇文章中，机器之心为大家整理了更多酷炫、神奇的 Code Interpreter 用例，除了数据分析领域，还能在游戏、图像和视频等 CV 领域大放异彩。

**几分钟制作一个游戏**

**![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)**

推特博主 @icreatelife 表示，ChatGPT Code Interpreter 太不可思议了。

你可以使用任何 AI 生成器来制作自己的游戏资产，然后要求带 Code Interpreter 插件的 GPT-4 来编写代码。五分钟就能搞定了。详细教程依次如下。

-   第一步：输入这段提示，「为经典电玩游戏 Asteroids 编写 p5.js 代码，其中用鼠标控制飞船，单击鼠标左键射击小行星。如果你的飞船与小行星相撞，你就输了。如果你击落了所有小行星，你就赢了。我想用自己的纹理来制作飞船和小行星。」

-   第二步：转到 Openprocessing 网站，创建并保存草图（你需要在上传任何纹理文件之前保存下来）。复制粘贴 GPT-4 的代码。

-   第三步：生成纹理文件并删除背景，例如在 Clip Drop 中。

-   第四步：用你自己的文件名替换纹理文件名。

-   第五步：运行程序。

-   第六步：如果出现问题，要求 GPT-4 进行修复（你可以复制错误并粘贴到 GPT-4 中），就像你要求人类程序员所做的那样。

-   最后一步，学习一点编程知识，给 GPT-4 写这些提示：「做我的编程老师。详细告诉我 Asteroids 游戏的算法，为函数命名，并解释每个函数的作用。不要只是写这些代码。」

您的浏览器不支持 video 标签

另一位博主 @aron\_brand 同样使用 Code Interpreter 和 Midjourney，在几分钟内创建了一个太空入侵者游戏。数百行代码完美无瑕，令人难以置信。

您的浏览器不支持 video 标签

**图像转换平移短视频**

**![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)**

推特博主 @chaseleantj 展示了如何利用 ChatGPT Code Interpreter 将图像转换为短视频。

您的浏览器不支持 video 标签

-   第一步：启用 Code Interpreter 插件功能。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   第二步：上传想要转换为短视频的图像。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   第三步：输入提示，要求从左到右将图像动画化。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

静等 30 秒，然后就能得到想要的平移短视频了。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

类似例子还有很多，博主 @Web3Brainiac 利用 GPT Code Interpreter 将以下 AI 制作的图像转换成了平移短视频。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

转换后是下面这样的。

您的浏览器不支持 video 标签

同样，博主 @anukaakash 联合使用 ChatGPT Code Interpreter 和 Midjourney 制作了一个平移短视频。

您的浏览器不支持 video 标签

**几秒生成缩放短视频**

六月底，Midjourney 发布了 v5.2，新增了「Zoom out」自定义缩放功能，非常适合做短视频。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

此次结合 Code Interpreter，推特博主 @minchoi 在几秒内使用多张图像和单个提示生成了下面这个缩放短视频。

您的浏览器不支持 video 标签

这位博主还详细介绍了教程。首先是多张图像，对使用 Midjourney Zoom Out 功能生成的多张图像进行压缩，这里自定义缩放系数为 1.25。此外按照字母顺序为图像后缀命名，从 image\_a.png 到 image\_p.png。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

接着启用 Code Interpreter，这里确保 ChatGPT 设置中启动了该插件。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然后将压缩的图像文件上传到 Code Interpreter。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

下一步是输入单个提示，包括如下内容：根据需要更新图像文件名、Midjourney 中使用的缩放系数、视频时长、FPS 等。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

最后一切交给 Code Interpreter，生成缩放短视频。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**几秒制作幻灯片**

**![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)**

推特博主 @jamesyeung18 利用 Code Interpreter，将 Midjourney 5.2 raw 生成的图像制作成为了连续性的幻灯片 —— 温布尔登（网球公开赛）的众生百态。

制作过程很简单，只需要压缩图像并要求 Code Interpreter 使用自然语言随机显示每张图像 2 秒就行了。

您的浏览器不支持 video 标签

**丰富的 CV 应用：高级视频分析、人脸追踪等**

**![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)**

推特博主 @skalskip92 使用 ChatGPT Code Interpreter，对视频中的物体进行检测、追踪和计数。他表示，Code Interpreter 非常擅长创建启发式方法，来基于物体的大小、位置或颜色对它们过滤。

您的浏览器不支持 video 标签

详细步骤如下。

-   第一步：隔离浅蓝色物体。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   第二步：在蓝色像素簇周围绘制相框。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   第三步：过滤掉小的蓝色像素簇。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   第四步：应用基于 IoU 的追踪。这里最开始出现了一些检测错误。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   第五步：对物体进行计数。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

-   最后一步：删除错误检测。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

此外，这位博主还探索了 ChatGPT Code Interpreter 在计算机视觉领域的多个其他用例。比如人脸检测和追踪。

您的浏览器不支持 video 标签

对 MNIST 数据集的图像分类。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

使用 OCR 提取图像中的文本。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**在 ChatGPT 中运行 GPT-2**

**![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)**

推特博主 @sdand 让 Code Interpreter 在 ChatGPT 中完整地运行具有 GGML 的 1.17 亿参数的 GPT-2。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

一，通过展示你知道一些 Code Interpreter 不知道的事情来建立「关系」（文件位于 /mnt/data/<etc> 中）。

二，在失败后建立信任，即不让 Code Interpreter 在第一次尝试时就运行 GPT-2 推理。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

三，Code Interpreter 可以运行 MNIST，并希望它很快能运行 Whispher。

四，你可以要求 Code Interpreter 更改文件的权限。这里告诉了它在整个目录上运行 chmod 777。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**数据科学，比人还强？**

在一篇博客中，宾夕法尼亚大学沃顿商学院副教授 Ethan Mollick 详细介绍了他使用 Code Interpreter 编写代码、执行复杂计算和生成图表的第一印象，称这个新工具使 ChatGPT 可以成为一名高效的数据科学家。

Mollick 在博客中写道：「我在读博期间花了几周时间才能掌握的事情，人工智能在几秒钟内就完成了，而且错误通常比我对人类分析师的预期要少。」

具体来说，Code Interpreter 为 AI 提供了一个解决问题的通用工具箱（用 Python 编写代码），内存足够大（可以上传最大 100MB 的文件，且可以是压缩形式）。这有助于解决以前版本的 ChatGPT 存在的许多问题：

-   它可以编写 Python 代码来解决大语言模型在数学和语言方面的天然弱点。

-   降低了幻觉的发生率。代码有助于保持 AI 的「诚实」，因为如果代码不正确，Python 就会生成错误。由于代码操作的是数据，而不是 LLM 本身，因此人工智能不会在数据中插入错误。当然这并不完美，AI 仍然会产生幻觉，但错误不太常见，并且不太可能影响代码或数据本身 。

-   它使 AI 更加通用化。大量问题可以通过代码解决，GPT-4 非常擅长以新颖有趣的方式确定何时使用代码解释器。例如要求它用代码向怀疑者证明地球是圆的，它提供了多个论证，将文本与代码和图像结合在一起。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Mollick 还强调了该工具类似人类的「推理」能力，因为它足够灵活，可以就分析用户上传数据的不同方式进行对话。因此，该工具「对于那些没有写过代码的人来说可能非常有用，」他写道。

只要想不到，没有做不到。机器之心未来还将继续关注 Code Interpreter 的更多有趣酷炫应用。

![图片](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gWibqs3dicZ1ibGicA1BHoaoMf3Im3KMaWO4e4OeUMNhIEuYfTib5b6fMialKic9qVWic4OvTyOwxSO6cLhyiaQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=31)

© THE END 

转载请联系本公众号获得授权

投稿或寻求报道：content@jiqizhixin.com