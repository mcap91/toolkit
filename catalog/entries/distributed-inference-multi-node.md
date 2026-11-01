---
name: distributed-inference-multi-node
title: Distributed LLM Inference Across Multiple Consumer PCs
category: reference
summary: "Practitioner reference on connecting multiple consumer PCs for combined VRAM — llama.cpp and vLLM both support distributed inference and ROCm, but neither supports tensor parallelism across nodes (pipeline parallel only, splitting layers across nodes); minimum 2.5GbE or WiFi 6 recommended; one practitioner building four nodes with 56GB InfiniBand connectivity"
tags: [distributed-inference, multi-node, local-inference, llama-cpp, vllm, rocm, infiniband, networking, consumer-hardware]
reviewed: 2026-09-25
acquired: 2026-09-25
license: N/A
security_flags: []
overlaps: [on-prem-llm-deployment-architecture, nvidia-pair]
source: unknown
---

## What it does

Reference documenting the current state of multi-node consumer LLM inference (as of Sep 2026):

- **llama.cpp / vLLM:** Both support distributed inference and ROCm, but tensor parallelism across multiple nodes is not supported — only pipeline parallelism (layer-splitting). Works but slower than single-node TP.
- **Networking:** WiFi 6 minimum, 2.5GbE or faster preferred. Latency adds up even though data volume is modest.
- **Mixed backends:** Unknown whether different GPU backends can be mixed across nodes.
- **Real build:** One practitioner assembling four nodes with 56GB InfiniBand, targeting 128GB+ combined VRAM.

Discussion source: r/LocalLLaMA (Sep 2026).

## Assessment

Practical ceiling for consumer multi-node is pipeline parallelism, which scales poorly compared to tensor parallelism. The NVIDIA PAIR router (now cataloged) may improve LAN coordination but doesn't solve the TP limitation.