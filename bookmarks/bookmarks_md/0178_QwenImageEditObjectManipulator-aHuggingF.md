---
url: https://huggingface.co/spaces/GiorgioV/Qwen-Image-Edit-Object-Manipulator-2511
title: "Qwen Image Edit Object Manipulator - a Hugging Face Space by GiorgioV"
description: "Upload one or more images and describe what you want to add or remove from them. Choose from different editing modes like adding objects or removing objects. The tool will process your request and ..."
captured_at: "2026-03-08T10:48:56.231Z"
---

# Qwen Image Edit Object Manipulator - a Hugging Face Space by GiorgioV

Fetching metadata from the HF Docker repository...

## runtime error

## Exit code: 1. Reason: | | 0.00/434M \[00:00<?, ?B/s\]\[A diffusion\_pytorch\_model-00003-of-00003.s(…): 26%|██▌ | 112M/434M \[00:01<00:04, 73.9MB/s\]\[A diffusion\_pytorch\_model-00003-of-00003.s(…): 85%|████████▍ | 367M/434M \[00:02<00:00, 156MB/s\] \[A diffusion\_pytorch\_model-00003-of-00003.s(…): 100%|██████████| 434M/434M \[00:02<00:00, 162MB/s\] Traceback (most recent call last): File "/app/app.py", line 96, in <module> transformer=QwenImageTransformer2DModel.from\_pretrained( ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^ "prithivMLmods/Qwen-Image-Edit-Rapid-AIO-V19", ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ...<2 lines>... device\_map='cuda' ^^^^^^^^^^^^^^^^^ ), ^ File "/usr/local/lib/python3.13/site-packages/huggingface\_hub/utils/\_validators.py", line 114, in \_inner\_fn return fn(\*args, \*\*kwargs) File "/usr/local/lib/python3.13/site-packages/diffusers/models/modeling\_utils.py", line 1314, in from\_pretrained ) = cls.\_load\_pretrained\_model( ~~~~~~~~~~~~~~~~~~~~~~~~~~^ model, ^^^^^^ ...<14 lines>... disable\_mmap=disable\_mmap, ^^^^^^^^^^^^^^^^^^^^^^^^^^ ) ^ File "/usr/local/lib/python3.13/site-packages/diffusers/models/modeling\_utils.py", line 1654, in \_load\_pretrained\_model \_caching\_allocator\_warmup(model, expanded\_device\_map, dtype, hf\_quantizer) ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.13/site-packages/diffusers/models/model\_loading\_utils.py", line 759, in \_caching\_allocator\_warmup \_ = torch.empty(warmup\_elems, dtype=dtype, device=device, requires\_grad=False) File "/usr/local/lib/python3.13/site-packages/torch/cuda/\_\_init\_\_.py", line 410, in \_lazy\_init torch.\_C.\_cuda\_init() ~~~~~~~~~~~~~~~~~~~^^ RuntimeError: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx

Container logs:

```
Failed to retrieve error logs: SSE is not enabled
```