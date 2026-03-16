---
url: https://huggingface.co/spaces/GiorgioV/Qwen-Image-Edit-2511-Fast_Reference
title: "Qwen Image Edit 2511 Fast - a Hugging Face Space by GiorgioV"
description: "Transform your photos by simply describing what you'd like to edit. Upload up to three reference images and write a prompt explaining your desired changes. The tool will generate a new image based ..."
captured_at: "2026-03-08T10:49:19.734Z"
---

# Qwen Image Edit 2511 Fast - a Hugging Face Space by GiorgioV

Fetching metadata from the HF Docker repository...

## runtime error

## Exit code: 1. Reason: 00%|██████████| 10.0G/10.0G \[00:25<00:00, 388MB/s\] diffusion\_pytorch\_model-00003-of-00003.s(…): 0%| | 0.00/434M \[00:00<?, ?B/s\]\[A diffusion\_pytorch\_model-00003-of-00003.s(…): 15%|█▍ | 65.0M/434M \[00:01<00:05, 64.5MB/s\]\[A diffusion\_pytorch\_model-00003-of-00003.s(…): 100%|██████████| 434M/434M \[00:01<00:00, 218MB/s\] Traceback (most recent call last): File "/app/app.py", line 43, in <module> transformer=QwenImageTransformer2DModel.from\_pretrained( ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^ "prithivMLmods/Qwen-Image-Edit-Rapid-AIO-V19", ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ...<2 lines>... device\_map='cuda' ^^^^^^^^^^^^^^^^^ ), ^ File "/usr/local/lib/python3.13/site-packages/huggingface\_hub/utils/\_validators.py", line 114, in \_inner\_fn return fn(\*args, \*\*kwargs) File "/usr/local/lib/python3.13/site-packages/diffusers/models/modeling\_utils.py", line 1314, in from\_pretrained ) = cls.\_load\_pretrained\_model( ~~~~~~~~~~~~~~~~~~~~~~~~~~^ model, ^^^^^^ ...<14 lines>... disable\_mmap=disable\_mmap, ^^^^^^^^^^^^^^^^^^^^^^^^^^ ) ^ File "/usr/local/lib/python3.13/site-packages/diffusers/models/modeling\_utils.py", line 1654, in \_load\_pretrained\_model \_caching\_allocator\_warmup(model, expanded\_device\_map, dtype, hf\_quantizer) ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.13/site-packages/diffusers/models/model\_loading\_utils.py", line 759, in \_caching\_allocator\_warmup \_ = torch.empty(warmup\_elems, dtype=dtype, device=device, requires\_grad=False) File "/usr/local/lib/python3.13/site-packages/torch/cuda/\_\_init\_\_.py", line 424, in \_lazy\_init torch.\_C.\_cuda\_init() ~~~~~~~~~~~~~~~~~~~^^ RuntimeError: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx

Container logs:

```
Failed to retrieve error logs: SSE is not enabled
```