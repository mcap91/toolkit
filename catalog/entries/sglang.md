---
name: sglang
title: SGLang
url: "https://github.com/sgl-project/sglang"
category: framework
summary: "High-performance LLM/VLM serving framework from UC Berkeley/LMSYS — RadixAttention automatically reuses KV cache across requests with shared prefixes via radix tree, achieving 75–95% cache hit rates on multi-turn agent workloads; structured generation language for constrained decoding; powers 400K+ GPUs in production (xAI, NVIDIA, AMD, LinkedIn); part of PyTorch ecosystem; Apache-2.0"
tags: [inference, serving, kv-cache, radix-attention, structured-generation, llm-serving, vllm-alternative, gpu]
reviewed: 2026-09-14
acquired: 2026-09-14
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

SGLang (Structured Generation Language) is an open-source serving framework for LLMs and multimodal models. Its core innovation is RadixAttention — an algorithm that automatically caches and reuses KV cache for common prefixes across requests using a radix tree data structure.

**RadixAttention**: In multi-turn chats and agent workflows, 80–90% of every prompt is repeated text (system prompt, tool definitions, prior turns). Standard inference engines recompute all these tokens from scratch. SGLang organizes KV cache into a radix tree in GPU VRAM: when a new request arrives, the engine walks the tree to find the longest matching cached prefix and begins computation from that point. An LRU eviction policy manages cache lifetime.

Key performance characteristics:
- **75–95% cache hit rates** on multi-turn agent conversations with shared system prompts
- **Shared prefix deduplication**: 100 agent sessions with the same instructions compute the system prompt KV cache once
- **10–20% throughput improvement** over vLLM on multi-turn workloads; larger gains on high-prefix-overlap scenarios
- **Reduced TTFT**: skipping prefill for cached tokens directly reduces time-to-first-token

SGLang is also a programming language for structured LLM interactions — constrained decoding, tool calls, schema-following output.

Production scale: powers 400K+ GPUs at xAI, NVIDIA, AMD, LinkedIn. Integrated into PyTorch ecosystem (March 2025).

## Mechanical details

- **Version**: v0.5.8 (January 2026)
- **Cache structure**: Radix tree with LRU eviction, cache-aware scheduling policy
- **Supported models**: LLMs and multimodal/vision-language models
- **Deployment**: GPU serving framework, production-ready
- **Organization**: UC Berkeley / LMSYS, PyTorch ecosystem

## Security

- **License**: Apache-2.0
- **Governance**: UC Berkeley / LMSYS, PyTorch ecosystem member
- **Production-proven**: deployed at scale across major companies