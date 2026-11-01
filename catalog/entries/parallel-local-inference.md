---
name: parallel-local-inference
title: Parallel Local Inference Pattern (vLLM)
url: "https://github.com/vllm-project/vllm"
category: agent-pattern
summary: Strategy for maximizing local GPU throughput by running multiple concurrent LLM agents via vLLM — exploits idle compute from memory-bandwidth bottleneck; 8-9x aggregate throughput over single-stream; per-agent throughput drops slightly but total throughput scales near-linearly with concurrency
tags: [vllm, local-inference, parallel-agents, gpu, throughput, llama-cpp, concurrent-inference]
reviewed: 2026-07-01
acquired: 2026-07-01
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it says

GPU LLM inference is bottlenecked by memory bandwidth, leaving significant compute capacity idle during single-stream generation. vLLM's architecture enables multiple concurrent inference streams, allowing parallel agents to exploit this idle compute for higher aggregate throughput.

Benchmarked performance: vLLM delivers 8-9x aggregate tokens/second over single-stream engines at high concurrency. For LLaMA-2-13B, 2.8x throughput over TGI (8,934 vs 3,187 tok/s). Throughput scales more linearly with concurrency than alternatives due to PagedAttention, continuous batching, prefix caching, and chunked prefill.

Contrast with llama.cpp: optimized for single-stream inference (low latency for one user) but does not natively serve multiple concurrent streams at the same efficiency. For agent swarms, vLLM's serving architecture is the better fit.

## Key takeaways

- Memory bandwidth is the inference bottleneck, not compute — concurrent agents put idle compute to work
- Per-agent throughput drops slightly with concurrency (e.g., 30 tok/s single → ~25 tok/s each with 3 concurrent), but aggregate throughput increases substantially
- For coding specifically, Qwen 3.6-27B matches or exceeds 100-230B MoE models on SWE Pro and Terminal Bench — running multiple 27B agents may outperform a single large model
- Implementation: agents connect as separate clients to a vLLM endpoint; orchestration (task ledger, lifecycle) is separate from the inference runtime
- vLLM supports multi-accelerator: NVIDIA, AMD ROCm, Intel Gaudi, AWS Trainium/Inferentia, CPU
- Current stable release: v0.20.2 (May 2026) with Model Runner V2 for up to 56% higher throughput on GB200

- Hardware sizing example: with 74 GB VRAM + 64 GB system RAM, multiple Qwen 3.6-27B instances fit comfortably; alternatively Stepfun 3.7 q4xs reported to have better reasoning than Qwen 3.6-27B on unified memory systems, with slightly faster inference but longer startup time
- For deep analysis tasks, running a 27B model at 7 tok/s on a single long-running task (60+ minutes) is a viable strategy alongside fast parallel agents — not every workload benefits from parallelism
- Agent swarm implementation pattern: bash script spins up N agents, each pings a central task ledger, selects an open task, executes it, marks complete, and repeats; search "agent swarm" for cloud-model examples of this pattern

## Mechanical details

vLLM serves as the inference backend. Each agent is a separate client sending requests to the vLLM API (OpenAI-compatible). Hardware sizing: divide available VRAM by per-model memory footprint to determine maximum concurrent instances, accounting for KV cache overhead per stream. Quantization support: FP8, INT8, GPTQ, AWQ, AQLM, GGUF, and FP8 KV cache. Tensor parallelism and pipeline parallelism for models exceeding single-GPU VRAM.

Agent frameworks (CrewAI, AutoGen, LangGraph, OpenAI Agents SDK) treat the inference engine as interchangeable — switching to vLLM is a configuration change.

## Security

vLLM is Apache-2.0 licensed. Pattern itself has no security concerns beyond standard API serving considerations. Task ledger implementations vary in security properties.