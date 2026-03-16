---
url: https://aws.amazon.com/cn/blogs/china/generative-ai-in-e-commerce-industry-efficient-production-of-marketing-materials/
title: "生成式 AI 在电商行业的应用场景实践 – 赋能营销物料高效生产 | Amazon Web Services"
description: "基于生成式 AI 行业解决方案指南生成多国模特试穿图、设计商品外观及更换不同场景生成商品海报。"
published: "2023-06-16T10:47:25+08:00"
captured_at: "2026-03-08T11:27:17.272Z"
---

# 生成式 AI 在电商行业的应用场景实践 – 赋能营销物料高效生产 | Amazon Web Services

感谢大家阅读《生成式 AI 行业解决方案指南》系列博客，全系列分为 4 篇，将为大家系统地介绍生成式 AI 解决方案指南及其在电商、游戏、泛娱乐行业中的典型场景及应用实践。目录如下：

-   第一篇 [《生成式 AI 行业解决方案指南与部署指南》](https://aws.amazon.com/cn/blogs/china/generative-ai-industry-solutions-guide-and-deployment-practices/)
-   第二篇 《生成式 AI 在电商行业的应用场景实践 – 赋能营销物料高效生产》（本篇）
-   第三篇 [《生成式 AI 在游戏行业的应用场景实践 – 加速游戏美术内容生产》](https://aws.amazon.com/cn/blogs/china/generative-ai-in-gaming-industry-accelerating-game-art-content-production/)
-   第四篇 [《生成式 AI 在泛娱乐行业的应用场景实践 – 助力风格化视频内容创作》](https://aws.amazon.com/cn/blogs/china/generative-ai-in-entertainment-industry-facilitating-the-creation-of-stylized-video-content/)

## 背景介绍

AI Generated Content（Generative AI，人工智能自动生成内容），是继专业生产内容（PGC, Professional-generated Content）、用户生产内容（UGC，User-generated Content）之后的新型内容创作方式，可以在创意、表现力、迭代、传播、个性化等方面，充分发挥技术优势，打造新的数字内容生成与交互形态。随着科技的发展，生成式 AI 在多个行业均有广泛应用，如泛娱乐行业的风格图、游戏行业的三视图等。本篇将聚焦于生成式 AI 在电商行业中的应用场景。

营销成本往往在电商行业每年的总支出中占据巨大的比例，而营销效果也在一定程度上影响着销量及销售额。电商营销包括短信营销、邮件营销、广告等。现今，直播、短视频带货已成为电商行业中重要的营销渠道。KOL 红人营销方式可以通过粉丝效应为推广商品带来更大的浏览量。但 KOL 推广所需的成本较高，且对于面向全球销售的商品，在多语言、多时区、多审美的场景下，推广成本会成倍增加。同时，在商品和使用体验逐渐同质化的今天，如何提升用户体验，实现差异化，加大用户留存也是电商领域寻求突破的关键问题。在广告方面，针对面对多国用户的跨境电商，往往需要聘请多国模特进行对于不同国家针对性的营销图片及方案，分别进行拍摄，后期修图之后进行呈现，这使得生成营销物料到所需的成本较高且时间均较长。除以上营销考虑，对于设计而言，商品设计，如女装设计，产品外包装设计等对于商品销量也有很大的影响。对于设计师而言，一款产品的设计从产生灵感到可以投入生产所花费的时间和精力是巨大的。对于用户而言，设计师有可能不能够完全理解自己需要的商品，从而无法短时间之后达到自己想要的效果。

基于以上行业需求，亚马逊云科技推出生成式 AI 行业解决方案指南，协助客户简单轻松构建生成式 AI 应用，并通过生成式 AI 更快地解决业务问题。其采用前后端分离、计算存储分离架构，将模型训练及推理构建在 SageMaker 服务上，可更加灵活地扩展，以实现多用户使用。

本篇，我们针对生成多国模特试穿图、设计商品外观及更换不同场景生成商品海报这三个电商行业典型场景，基于生成式 AI 行业解决方案指南，介绍此行业场景的生成式 AI 参数配置优化，以协助使用者得到更加贴合场景的效果。

## 生成式 AI 电商典型场景介绍

电商行业，尤其是跨境电商行业面向的客户群体往往全世界。在推销当季新品时，结合客户画像，提供合适的效果图，进行广告投放效果往往是最好的。

以跨境女装电商为例，在投放女装广告时，需要考虑不同国家客户对于模特图试穿效果的直观感受，这也是很多品牌会聘请不同国家的模特做相同衣服的展示的考虑之一。生成式 AI 在此场景中，可以通过使用 In-paint Mask 并输入相应的提示词，生成不同虚拟模特的试穿效果图。从而节约聘请模特的成本以及节省模特拍摄所需的时间。效果图如下所示：

除女装行业需要生成模特试穿图外，电商行业的典型广告场景还包括设计商品外包装。商品外包装关系到商品对于消费者的吸引力，和受到的关注度，这往往会影响到商品的销量。在设计方面，可以通过生成式 AI 的文生图方式，结合 ControlNet 生成不同设计图。效果图如下：

在完成商品外包装设计后，可以继续结合广告播放季节和特殊节日生成不同使用场景下的商品使用图，吸引客户，并帮助客户更好地了解产品。此场景可以使用 Inpaint 结合图生图实现，案例如下：

## 架构与工作原理

本篇以生成式 AI 行业解决方案指南为基础，其工作原理如下图：

生成式 AI Solution Guidance 架构图

生成式 AI 行业解决方案指南，将前端 Stable Diffusion WebUI 部署在容器服务 Amazon ECS 上，后端使用无服务器服务 Amazon Lambda 进行处理，前后端通过 Amazon API Gateway 调用进行通信。模型训练及部署均通过 Amazon SageMaker 进行。同时使用 Amazon S3、Amazon EFS、Amazon DynamoDB 分别进行模型数据、临时文件、使用数据的存储。

## 快速部署流程

本行业解决方案指南可使用 CloudFormation 一键部署。如需使用生成式 AI 行业解决方案指南，可参考**生成式 AI solution guidance 的全面解读**，本篇不做重点介绍。

## 场景常用配置参数

### 提示词工程

提示词可由多个单词或词组构成，并由”,”进行分隔。其中单词或词组可以通过（prompt : number）等形式改变提示词的权重。若无说明，提示词默认权重为 1。在提示词顺序中，主体顺序应尽量靠前，可参考如下顺序：

画面质量，风格，主题，外表（发型、发色、衣服、眼睛、手臂、胸部、腿部….），情绪，姿势，背景

后续介绍中有详细案例。

### 案例一：模特更换案例配置参数

本节以生成 One Indian Girl 为例。

1\. 选定模型，模型推荐使用真人模型，并保存。

2\. 使用图片处理工具，对图片进行处理，得到蒙版图片。

3\. 进入图生图界面，输入正向提示词：

(masterpiece:1.4), (best quality:1.2), (ultra highres:1.2) ,(8k resolution:1.0),(realistic:1.0),(ultra detailed1:0), (sharp focus1:0), (RAW photo:1.0),

one Indian girl, detailed beautiful skin, kind smile, solo, absurdres, detailed beautiful face, petite figure, detailed skin texture, pale skin, thigh gap, detailed hair, random hair style, detailed eyes, glistening skin, portrait photo,

(blue jeans:1.4), (knit sweater:1.4), ear rings, futuristic, studio, (white background:1.4)

反向提示词：

(nsfw:1.4),

(Easy Negative:1.4), (worst quality: 1.4), (low quality: 1.4), (normal quality: 1.4),

lowers,monochrome,grayscales,skin spots, acnes, skin blemishes, age spot,6 more fingers on one hand,deformity, bad legs, error legs, bad feet, malformed limbs, extra limbs

4\. 如图所示，分别点击局部重绘，上传蒙版选项后，上传原图片及蒙版图片：

此步骤中，蒙版模糊度表示绘图区域与原图边缘的过度平滑度，值越大表示绘图区域与原图边缘的过度越平滑，此案例中，值为 6。

5\. 其余生图参数如图所示：

-   设置图片的相应的长宽，以免图片变形。
-   面部修复启用后会在生成图片后调整面部区域。
-   重绘幅度表示图片变化度，取值越大，说明图片变化越大，0 表示图片几乎不变，1 表示可能严重偏离原图。一般建议参数在 0.6~0.8 范围。此案例中设置为 0.7。
-   随机种子是一个可以锁定生成图像的初始状态的值。

6\. 点击生成即可生成图片：

### 案例二：商品设计图

本节以生成最后一张设计图为例

1\. 选定模型并保存：

2\. 继续下滑页面，设置 Clip 跳过值为 2，指的是提前停止神经网络对提示的处理。有些模型在训练时使用了这种调整方法，因此设置这个值可以帮助在这些模型上获得更好的结果。并保存:

3\. 进入文生图界面，输入正向提示词：

photograph for a can of orange juice with logo ISA,

simple background, white background,

(masterpiece:1.2), (best quality:1.2), (highres:1.1), (photorealistic:1.1)

反向提示词：

easynegative, logo, signature,

4\. 其余生图参数如图所示：

-   设置图片的相应的长宽，以免图片变形。
-   对于真实场景，用 Karras 类型的采样器可以获得相对好的效果，故取样方法选择 DPM ++ SDE Karras。
-   随机种子是一个可以锁定生成图像的初始状态的值。
-   Clip skip:2 指的是提前停止神经网络对提示的处理。有些模型在训练时使用了这种调整方法，因此设置这个值可以帮助在这些模型上获得更好的结果。

5\. 设置 ControlNet：

-   启用 ControlNet
-   开启像素级完美设置之后，无需手动设置预处理器分辨率。 建议开启
-   其余设置如图所示

6\. 设置完成后点击生成即可生成图片

### 案例三：更换背景

本节以生成一张广告图为例

1\. 选定模型，并保存：

2\. 使用图片处理工具，对图片进行处理，得到蒙版图片：

3\. 进入图生图界面，输入正向提示词：

(masterpiece:1.2), (best quality:1.2), (highres:1.1), (photorealistic:1.1),

photograph for a can of orange juice with logo ISA,

background Christmas style, orange, juice, food,

反向提示词：

easynegative, logo, signature,

4\. 如图所示，分别点击局部重绘，上传蒙版，之后上传原图片及蒙版图片：

此步骤中，蒙版模糊度表示绘图区域与原图边缘的过度平滑度，值越大表示绘图区域与原图边缘的过度越平滑，此案例中，值为 2。且由于需要背景产生和原图更加大的区别，可以选取”潜空间噪声“和“潜空间数值零”，在本次的场景中，“潜空间数值零”得到了更好的效果。

5\. 其余生图参数如图所示：

-   设置图片的相应的长宽，以免图片变形。
-   由于期望侧重于速度、融合、新颖且质量不错的结果，取样方法选择 DPM ++ 2M Karras。
-   重绘幅度表示图片变化度，取值越大，说明图片变化越大，0 表示图片几乎不变，1 表示可能严重偏离原图。一般建议参数在 0.6~0.8 范围。此案例需要在灰色背景上画出完全不同的新背景，因此选择了 0.95。
-   随机种子是一个可以锁定生成图像的初始状态的值。

6\. 设置 ControlNet0:

7\. 设置 ControlNet1:

使用 ControlNet inpaint 可以使 AI 对于全图的结构有一定的理解，避免出现太过天马行空的结果。

8\. 点击生成即可生成图片。

## 小结

营销成本往往在电商行业每年的总支出中占据巨大的比例，在广告方面，生成式 AI 可以协助电商客户构建产品宣传海报，及虚拟多国模特的商品展示等，从而实现更快速、更低成本的商品推广。对于设计而言，生成式 AI 通过输入提示词可以协助设计师进行商品设计，为设计师提供基础灵感。并且生成式 AI 提供了一种让客户自行设计商品的新方式，客户可以提供自己的设计或者自己生活中的图片，并通过生成式 AI 使其风格化等，确认效果满意后，提供生产。这在一定程度上可以减少由于设计的退货风险，并减轻设计师负担，使得设计更加快速并满足消费者的预期，并实现使用体验的差异化。

本篇主要介绍在模特更换生成试穿效果、商品外包装设计，及更换背景生成商品广告图这三个电商典型场景下，选取三个案例的建议参数。如果您想达到类似效果，可以参考此参数配置。还有其他场景及行业案例，请参考我们相关的系列博客。

##  参考资料

1\. 生成式 AI 行业解决方案指南：[https://aws.amazon.com/cn/campaigns/aigc/](https://aws.amazon.com/cn/campaigns/aigc/)

2\. 生成式 AI 行业解决方案指南 Workshop：[https://catalog.us-east-1.prod.workshops.aws/workshops/bae25a1f-1a1d-4f3e-996e-6402a9ab8faa](https://catalog.us-east-1.prod.workshops.aws/workshops/bae25a1f-1a1d-4f3e-996e-6402a9ab8faa)

3\. Stable-diffusion-webui：[https://github.com/AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

4\. Hugging Face：[https://huggingface.co/](https://huggingface.co/)

## 本篇作者