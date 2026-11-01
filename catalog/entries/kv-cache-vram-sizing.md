---
name: kv-cache-vram-sizing
title: KV Cache VRAM Sizing Formula for Local LLM Inference
category: reference
summary: "Practitioner reference for calculating KV cache memory: formula (2 × layers × kv_heads × head_dim × context_tokens × bytes_per_value), worked example showing Llama 3.1 8B at 128K context uses 16GB for cache alone (3× the 4.9GB Q4 weights); explains why GQA models (fewer KV heads) are dramatically cheaper at long context than MHA models, and why Ollama's default small num_ctx hides the cost until you raise it"
tags: [kv-cache, vram, local-inference, memory-sizing, gqa, llama-cpp, ollama, context-window]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: [turboquant, on-prem-llm-deployment-architecture, llmfit]
license: N/A
security_flags: []
source: unknown
---

## What it does

Practical formula and worked example for calculating KV cache memory consumption during local LLM inference — the hidden cost that causes OOM errors even when model weights fit comfortably in VRAM.

**The formula:**

```
KV bytes = 2 × layers × kv_heads × head_dim × context_tokens × bytes_per_value
```

The `2` accounts for both K and V tensors. `bytes_per_value` is 2 at fp16, 1 at fp8/q8_0.

**Worked example — Llama 3.1 8B (GQA, 8 KV heads):**

- Per token: 2 × 32 layers × 8 kv_heads × 128 head_dim = 65,536 values × 2 bytes = 128 KB/token
- 2K context: 256 MB | 8K: 1 GB | 32K: 4 GB | 128K: 16 GB
- Model weights at Q4_K_M: 4.9 GB — at 128K context the cache is 3× the model

**Key insights:**

- **Budget VRAM as weights + cache, never weights alone.** The cache is linear in tokens and can exceed model size at long contexts.
- **GQA vs MHA matters more than parameter count.** Two models with the same parameter count can have wildly different cache costs because `kv_heads` differs. A GQA model with 8 KV heads costs 1/4 the cache of an MHA model with 32 heads. This is not visible in parameter count or quant name — requires reading `num_key_value_heads` and `num_hidden_layers` from the model's `config.json`.
- **Ollama hides the cost by default.** Ollama runs a small default `num_ctx`. Raising it to use the model's full advertised context (e.g., 128K) triggers the full cache allocation immediately, because it's linear in tokens.
- **Rule of thumb**: On consumer hardware, a smaller GQA model at a large context window usually beats a larger model forced to run at 4K context.

## Security

N/A — reference content, not software.