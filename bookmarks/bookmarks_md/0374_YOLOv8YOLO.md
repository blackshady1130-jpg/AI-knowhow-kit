---
url: https://mp.weixin.qq.com/s/jCt2r7LXq2Ojl0xKa0T1rA
title: "基于YOLOv8，YOLO新作来了！"
description: "腾讯AI Lab发布real-time、open-vocabulary的zero-shot物体检测模型"
author: "啥都生"
captured_at: "2026-03-08T11:32:12.875Z"
---

# 基于YOLOv8，YOLO新作来了！

![图片](https://mmbiz.qpic.cn/mmbiz_png/4NticPLmYQfQbn0sFwFhyeCJe4JI6d7hHZ2CIY7puFW0rbViaKhF2fDTWSJZlYtZWe9XUYGyh6eKibpXh3LWlbR2Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "null")

本月初，腾讯人工智能实验室发布了`real-time`、`open-vocabulary`的`zero-shot`物体检测模型 **YOLO-World**。**旨在提升开放词汇检测能力以及解决现有zero-shot目标检测模型的限制：速度**

与其他使用Transformer这种功能强大但速度慢的架构不同的是，**YOLO-World基于CNN**

> paper | https://arxiv.org/abs/2401.17270

> code  | https://github.com/AILAB-CVC/YOLO-World

我们知道传统的对象检测模型，如 Faster R-CNN、SSD 和 YOLO（老演员了），旨在识别其预定义好的数据集内的对象，如PASCAL、COCO等，**这就限制了在与训练数据范围相匹配的场景中的泛化性。要扩展或改变可识别类别集，就必须在为新类别量身定制的数据集上重新训练或微调模型**

那`Open-Vocabulary Object Detection`干了啥？

由于`fixed-vocabulary` 检测器的局限，`Open-Vocabulary Object Detection`（OVD）模型**旨在识别预定义类别之外的物体**。如 `GLIP` 和 `Grounding DINO`等早期方法，**侧重于利用大规模图像文本数据来扩展训练词汇，从而实现对新物体的检测**。所要做的就是提示模型并指定要寻找的对象

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "null")

GroundingDINO“椅子”与“狗尾巴”提示

然而这些早期方法往往体积较大，计算密集度较高，需要同时对图像和文本进行编码以进行预测，带来的延迟会妨碍实际应用

YOLO-World可以在提示中理解上下文以提供检测，**不需要在特定类别上训练模型，因为该模型已使用图像文本对（image-text pairs）和基础图像（ grounded images）进行了训练**，模型学会了如何接受任意提示，例如“穿白衬衫的人”，并将其用于检测

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "null")

不同对象检测推理范例的比较

YOLO-World 引入了 "先提示后检测 "模式，一种避免实时文本编码的新方法，允许用户生成提示，然后将其编码为离线词汇。**通过将一系列用户生成的提示预先编码到离线词汇表中，绕过了实时文本编码的需要**，从而实现了更快、适应性更强的检测

YOLO-World模型结构是啥样的？其主要包含三个关键部分

-   • YOLO Detector - **基于Ultralytics YOLOv8**，从输入图像中提取多尺度特征

-   • 文本编码器 - 由OpenAI CLIP预训练的Transformer文本编码器，将文本编码为文本嵌入

-   • Re-parameterizable Vision-Language Path Aggregation Network（RepVL-PAN）- **在图像特征和文本嵌入之间执行多级跨模态融合，促进多尺度图像特征与文本嵌入之间的交互**。RepVL-PAN 可将用户的离线词汇重新参数化为模型参数，以便快速推理和部署

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E "null")

YOLO-World 提供三种模型`large`、`medium`、`small`，在 LVIS 数据集上对模型进行了基准测试，在没有任何性能加速机制（如量化或 TensorRT）的情况下基于 V100 测试了性能。**结果表明YOLO-World 的`large`版本达到了 35.4 AP（52.0 FPS），`small`版本达到了 26.2 AP（74.1 FPS）**

![图片](https://mmbiz.qpic.cn/mmbiz_png/4NticPLmYQfQbn0sFwFhyeCJe4JI6d7hHYoyMzvKVRGNpIia6fQQ7M47ic3cd3pyWzZiaCND7cnFFMdI0V9GDQo4vA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "null")

感兴趣的可在如下地址进一步体验与了解

> https://huggingface.co/spaces/stevengrove/YOLO-World

我是啥都生，下次再见~

\- https://www.yoloworld.cc/?ref=blog.roboflow.com

\- https://github.com/AILAB-CVC/YOLO-World

END

### 技能拓展

-   •  [人工智能核心课程推荐](http://mp.weixin.qq.com/s?__biz=MzUzNjE1Nzc1MA==&mid=2247493797&idx=1&sn=bdcf3a096e4d65aa2fd3821a6f34f311&chksm=faf823fccd8faaea3724a20c1d44e2585f75b5973f2ecb6248c5fc89ce247ab3e47ac5e83564&scene=21#wechat_redirect)

### 推介阅读

-   •  [激活函数30年回顾总结，全paper第一份详尽研究来了！](http://mp.weixin.qq.com/s?__biz=MzUzNjE1Nzc1MA==&mid=2247496033&idx=1&sn=12bf20eaeeacd573d8ef79f2d091b706&chksm=faf83a38cd8fb32e5b326d7164289d733f7ceb2eb89ea2015fdeca240eea06e7e7a375b44d6d&scene=21#wechat_redirect)

-   •  [2023年视觉领域突破性研究有哪些？](http://mp.weixin.qq.com/s?__biz=MzUzNjE1Nzc1MA==&mid=2247495721&idx=1&sn=ae0cfb13fa2567a951788809b56b882a&chksm=faf83b70cd8fb266b4b930cc92321662ed7282bc936c30b61da9649b434e4e7c114332a0bfd2&scene=21#wechat_redirect)