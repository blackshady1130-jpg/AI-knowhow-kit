---
url: https://www.yoloworld.cc/
title: "YOLO-World: Real-Time, Zero-Shot Object Detection"
description: "YOLO-World is a zero-shot, real-time object detection model."
author: "@skalskip92"
published: "2024-02-13T20:27:02.000Z"
captured_at: "2026-03-08T11:32:56.273Z"
---

# YOLO-World: Real-Time, Zero-Shot Object Detection

On January 31st, 2024, Tencent’s AI Lab released [YOLO-World](https://playground.roboflow.com/models/tencent%20ai%20lab/yolo-world?ref=blog.roboflow.com) (access code on [Github](https://github.com/AILab-CVC/YOLO-World?ref=blog.roboflow.com)), a real-time, open-vocabulary object detection model. YOLO-World is a [zero-shot model](https://blog.roboflow.com/zero-shot-learning-computer-vision/), which means you can run object detection without any training.

Follow our open source guide on [how to use YOLO-World](https://blog.roboflow.com/how-to-detect-objects-with-yolo-world/) if you are interested in trying the model.

YOLO-World was designed to solve a limitation of existing zero-shot object detection models: speed. Whereas other state-of-the-art models use Transformers, a powerful but typically slower architecture, YOLO-World uses the faster CNN-based [YOLO](https://blog.roboflow.com/guide-to-yolo-models/) architecture.

![](https://blog.roboflow.com/content/images/2024/04/image-314.webp)

****Figure 1.**** Comparison of YOLO-World with the latest open vocabulary methods in terms of speed and accuracy. Models were compared on the LVIS dataset and measured on NVIDIA V100. Source YOLO-World paper.

In this guide, we are going to discuss what YOLO-World is, the recent history of zero-shot object detection, and how the model performs according to the [YOLO-World paper](https://arxiv.org/abs/2401.17270?ref=blog.roboflow.com).

Before we get started, check out the live demo below to see Yolo-World in action.

## From Fixed-Class Object Detectors to YOLO-World

### Traditional Object Detectors

Traditional object detection models, such as [Faster R-CNN](https://blog.roboflow.com/training-a-tensorflow-faster-r-cnn-object-detection-model-on-your-own-dataset/), SSD, and YOLO, are designed to identify objects within a predetermined set of categories defined by their training datasets. For instance, models trained on the [COCO dataset](https://blog.roboflow.com/coco-dataset/) are limited to 80 categories.

**This limitation restricts their applicability to scenarios that match the training data's scope.** Extending or altering the set of recognizable classes necessitates retraining or fine-tuning the model on a custom dataset tailored to the new categories.

### Open-Vocabulary Object Detection

As a response to the limitations of fixed-vocabulary detectors, open-vocabulary object detection (OVD) models aim to recognize objects beyond the predefined categories. Early attempts in this direction, such as GLIP and [Grounding DINO](https://blog.roboflow.com/grounding-dino-zero-shot-object-detection/), focused on leveraging large-scale image-text data to expand the training vocabulary, enabling the detection of novel objects. All you have to do is prompt the model and specify what objects you are looking for.

![](https://blog.roboflow.com/content/images/2024/04/image-320.webp)

****Figure 2****. GroundingDINO “chair” vs “dog's tail” prompt.

**However, they tend to be larger and more computationally intensive, requiring simultaneous encoding of images and texts for prediction**. This approach, while powerful, introduces latency that can hinder practical applications. [See this guide](https://blog.roboflow.com/grounding-dino-zero-shot-object-detection/) if you want to try GroundingDINO.

## What is YOLO-World?

YOLO-World, introduced in the research paper “[YOLO-World: Real-Time Open-Vocabulary Object Detection](https://arxiv.org/abs/2401.17270?ref=blog.roboflow.com)”, shows a significant advancement in the field of open-vocabulary object detection by demonstrating that lightweight detectors, such as those from the YOLO series, can achieve strong open-vocabulary performance. This is particularly noteworthy for real-world applications where efficiency and speed are crucial, like edge applications.

YOLO World has grounding capabilities and can understand the context in a prompt to provide detections. You do not need to train the model on a particular class because the model has been trained using image-text pairs and grounded images. The model has learned how to take an arbitrary prompt – for example, “person wearing a white shirt” – and use that for detection.

![](https://blog.roboflow.com/content/images/2024/04/image-327.webp)

****Figure 3.**** Comparison of different object detection inference paradigms. Source YOLO-World paper.

[YOLO-World](https://playground.roboflow.com/models/tencent%20ai%20lab/yolo-world?ref=blog.roboflow.com) introduces the "prompt-then-detect" paradigm, a novel approach that avoids the need for real-time text encoding. Instead, it allows for the generation of prompts by users, which are then encoded into an offline vocabulary.

![](https://blog.roboflow.com/content/images/2024/04/image-331.webp)

****Figure 4.**** YOLO-World “person, backpack, dog, eye, nose, ear, tongue” prompt.

**By pre-encoding a series of user-generated prompts into an offline vocabulary, the model bypasses the need for real-time text encoding, enabling quicker and more adaptable detection.**

Unlike traditional methods, which rely on a fixed set of predefined categories, or earlier open-vocabulary approaches that encode user prompts in real-time (online vocabulary), YOLO-World introduces a more efficient alternative. 

This approach significantly reduces computational overhead \[Figure 1.\], allowing for dynamic adjustment of the detection vocabulary to meet varying needs without sacrificing performance, thus enhancing the model's utility in real-world applications.

## YOLO-World Architecture

YOLO-World's architecture consists of three key elements:

-   **YOLO detector** - based on Ultralytics [YOLOv8](https://blog.roboflow.com/whats-new-in-yolov8/); extracts the multi-scale features from the input image.
-   **Text Encoder** - Transformer text encoder pre-trained by OpenAI’s [CLIP](https://blog.roboflow.com/openai-clip/); encodes the text into text embeddings.
-   **Re-parameterizable Vision-Language Path Aggregation Network (RepVL-PAN)** - performs multi-level cross-modality fusion between image features and text embeddings.

![](https://blog.roboflow.com/content/images/2024/04/image-338.webp)

****Figure 5.**** Overall Architecture of YOLO-World. Source YOLO-World paper.

The fusion between image features and text embeddings is implemented via:

-   **Text-guided Cross Stage Partial Layer (T-CSPLayer)**: Built on top of the C2f layer, used in the [YOLOv8 architecture](https://blog.roboflow.com/whats-new-in-yolov8/), by adding text guidance into multi-scale image features. This is achieved through the Max Sigmoid Attention Block, which computes attention weights based on the interaction between text guidance and spatial features of the image. These weights are then applied to modulate the feature maps, enabling the network to focus more on areas relevant to the text descriptions.
-   **Image-Pooling Attention:** Optimizes text embeddings with visual context by applying max pooling to multi-scale image features, thus distilling them into 27 patch tokens that encapsulate essential regional data. These tokens are then transformed through a process involving queries derived from text embeddings and keys and values from image patches, to compute scaled dot-product attention weights.

![](https://blog.roboflow.com/content/images/2024/04/image-345.webp)

****Figure 6.**** Text-guided Cross Stage Partial Layer \[T-CSPLayer\]. Source YOLO-World paper.

## YOLO-World Performance

YOLO-World follows on from a series of zero-shot [object detection models](https://roboflow.com/model-task-type/object-detection?ref=blog.roboflow.com) released last year. These models, capable of identifying an object without fine-tuning, are typically slow and resource-intensive.

![](https://blog.roboflow.com/content/images/2024/04/image-351.webp)

****Table 1.**** Zero-shot Evaluation on LVIS. Source YOLO-World paper.

YOLO-World provides three models: small with 13M (re-parametrized 77M), medium with 29M (re-parametrized 92M), and large with 48M (re-parametrized 110M) parameters.

The YOLO-World team benchmarked the model on the LVIS dataset and measured their performance on the V100 without any performance acceleration mechanisms like quantization or TensorRT.

**According to the paper YOLO-World reached between 35.4 AP with 52.0 FPS for the large version and 26.2 AP with 74.1 FPS for the small version.** While the V100 is a powerful GPU, achieving such high FPS on any device is impressive.

## Using YOLO-World

Follow our open source guide on [how to use YOLO-World](https://blog.roboflow.com/how-to-detect-objects-with-yolo-world/) if you are interested in running the model on your own or you can try the model on [Hugging Face](https://huggingface.co/spaces/stevengrove/YOLO-World?ref=blog.roboflow.com) and dive into the [model code on GitHub](https://github.com/AILAB-CVC/YOLO-World?ref=blog.roboflow.com).

When you deploy a YOLO-World model, you specify a custom vocabulary that you want to use. Then, embeddings will be calculated that are used during model inference. Embeddings are passed through a Vision-Language Path Aggregation Network (RepVL-PAN) network developed for the model. The result is then used to apply region-text matching for use in detection.

You can use YOLO-World in a variety of ways:

-   Real-time object detection and tracking on edge devices 
-   Video processing and analytics
-   Auto-labeling data for custom vision model training

While these tasks are achieved with custom vision models today, using YOLO-World you may be able to create applications without needing to train a model. You will be able to get vision applications running in production faster by avoiding the time it takes to label data and train a model.

You are to deploy YOLO-World in [Roboflow Inference](https://github.com/roboflow/inference?ref=blog.roboflow.com), an edge deployment solution trusted by large enterprises to deploy YOLO models in production and Roboflow will be publishing an [Autodistill module](https://docs.autodistill.com/?ref=blog.roboflow.com) to use YOLO World to auto-label your data in a few lines of code.

## Conclusion

YOLO-World is an important step in making open-vocabulary object detection faster, cheaper, and widely available. Maintaining nearly the same accuracy, YOLO-World is 20x faster and 5x smaller than leading zero-shot detectors. 

This opens the way to use cases that so far have been impossible like open-vocabulary video processing or deployment of open-vocabulary detectors on the edge.