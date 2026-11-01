---
name: vllm
title: vLLM
url: https://github.com/vllm-project/vllm
category: framework
summary: High-throughput, memory-efficient open-source inference and serving engine for LLMs — PagedAttention KV-cache management, continuous batching, prefix caching, speculative decoding, and tensor/pipeline/data/expert/context parallelism; supports 200+ Hugging Face model architectures; originated at UC Berkeley's Sky Computing Lab, now a PyTorch Foundation hosted project (joined Dec 2024, hosted since May 2025); ~96k GitHub stars, 2000+ contributors; Apache-2.0
tags:
  - llm-inference
  - serving
  - paged-attention
  - continuous-batching
  - speculative-decoding
  - parallelism
  - pytorch-foundation
  - open-source
  - gpu
reviewed: 2026-10-29
acquired: 2026-10-29
license: Apache-2.0
security_flags: []
overlaps:
  - sglang
  - localai
  - on-prem-llm-deployment-architecture
  - parallel-local-inference
  - llm-compressor
source_url: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/
source: reddit
---

## What it does

vLLM is an inference and serving engine for large language models. PagedAttention manages the KV cache like virtual memory pages, and continuous batching keeps GPUs busy across requests of different lengths; the engine also supports prefix caching and speculative decoding. It runs 200+ model architectures from Hugging Face and scales across tensor, pipeline, data, expert, and context parallelism for multi-GPU/multi-node serving. Install with `uv pip install vllm` or `pip install vllm`; serve a model with `vllm serve <model>`.

## Security

Apache-2.0. Self-hosted — no telemetry beyond what a deployer configures. Originated at UC Berkeley's Sky Computing Lab; joined the PyTorch ecosystem in December 2024 and became a PyTorch Foundation hosted project in May 2025, with 2000+ contributors across many institutions and companies rather than a single maintainer.

## Usage notes

- Practitioner report (r/Qwen_AI, Oct 2026): used to self-host Qwen 3.8 27B FP8 on a single 48GB NVIDIA L40S (batch size 4, multi-token prediction 3), averaging ~28 tok/s at xhigh reasoning effort for day-to-day coding and data-analysis work, as part of a harness also using Zed, Qwen Code, and a SearXNG MCP server. (source: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/)
