# Create a 5s 1080p Video in 4.5s with FastVideo on a Single GPU

Hao AI Lab @ UCSD

## TL;DR

FastVideo's real-time inference stack achieves a ~4.55-second end-to-end latency for 5-second video generation at 1088 x 1920 resolution at 24 FPS, on a single NVIDIA B200 GPU. This turns LTX-2.3, an open-source TI2AV model, into a single-GPU speed machine for interactive media generation.

[Try the demo](https://1080p.fastvideo.org/) | [GitHub](https://github.com/hao-ai-lab/FastVideo)

## The Problem: Broken Feedback Loop

The biggest bottleneck in video generation is no longer just model quality — it is the broken feedback loop during creative iteration. When each attempt takes minutes and hits your budget, the creation loop collapses. For example, generating an 8-second video with Google's Veo-3 Fast takes about 55 seconds.

Recent research efforts have greatly reduced video generation latency, but most are limited to 480p or 720p and often do not produce audio. 1080p is where things get serious — it's where outputs become usable for storytelling, content creation, and real products.

## FastVideo's New Real-Time Inference Stack

Achieving sub-5-second end-to-end latency requires optimization across every layer:

### Fast attention for video generation
DiTs rely on 3D spatiotemporal attention. FastVideo incorporates optimized attention kernels for NVIDIA's SM100/SM103 architectures (Blackwell).

### Aggressive low-precision execution with NVFP4
Compared to BF16, NVFP4 offers dramatically higher theoretical throughput. FastVideo supports NVFP4-quantized linear layers in the DiT while preserving output quality.

### End-to-End graph and kernel optimization
Multiple kernel fusion techniques optimized every major stage: prompt encoding, latent preparation, denoising, and decoding.

### System-Level efficiency
Using FastVideo's comprehensive system profiling support, streamlined I/O pipeline for frame and audio processing. Uses an optimized ffmpeg build.

## Serving Optimizations

The demo is served on half of a GB200 NVL72 (36x GPUs), with each GPU acting as a serving replica with load balancing. Rust-based middleware for better serving efficiency.

## Outlook

Running high-quality 1080p video generation on a single GPU dramatically simplifies deployment — no need for sequence parallelism or multi-GPU strategies. With continued advances, sub-5-second local generation on consumer devices is coming sooner than most people expect.

### The Team

Core contributors: Matthew Noto, Yechen Xu, Junda Su, Will Lin (equal contribution)
Tech leads: Will Lin, Peiyuan Zhang, Hao Zhang
Advisors: Hao Zhang, Danyang Zhuo, Eric Xing, Zhengzhong Liu

---
Source: https://haoailab.com/blogs/fastvideo_realtime_1080p/
