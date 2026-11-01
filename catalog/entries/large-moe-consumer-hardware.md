---
name: large-moe-consumer-hardware
title: Running Large MoE Models on Consumer Hardware (llama.cpp CPU-MoE Offload)
category: reference
summary: "Practitioner guide to running 176B MoE models (Qwen3.8-Flash-Next, 6B active) on a single 16GB GPU + 192GB RAM via llama.cpp --cpu-moe flag — attention on GPU, experts on CPU; ~16 tok/s; includes llama.cpp n-gram speculative decoding reference (--spec-type ngram-simple/ngram-cache, --lookup-cache-dynamic for SSD offload, tuning flags --spec-ngram-simple-size-n/m), q8_0 KV cache sizing at 262K context (~14GB), and memory budgeting guidance"
tags: [moe, llama-cpp, local-inference, cpu-offload, speculative-decoding, n-gram, consumer-hardware, vram, gguf]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: [on-prem-llm-deployment-architecture, kv-cache-vram-sizing]
license: N/A
security_flags: []
source: unknown
---

## What it does

Practitioner report on running Qwen3.8-Flash-Next (176B total, 6B active MoE) on consumer hardware: RTX 5070 Ti (16GB VRAM), 192GB DDR5 RAM, Linux. The key insight is that large MoE models don't need large GPUs — they need large system RAM.

**Configuration that works:**

- llama.cpp built from PR #27742 branch (experimental at time of writing)
- Q8_0 GGUF, ~175GB across 12 shards (llama.cpp handles split transparently — point at shard 1)
- `--cpu-moe` flag: experts run on CPU (in system RAM), attention stays on GPU
- 262K context, q8_0 KV cache
- Result: ~16 tok/s generation, usable for interactive chat

**Memory budget:**

- q8_0 KV cache at full 262K context = ~14GB — fits 16GB GPU with room to spare
- 175GB model weights sit in system RAM — tight on 192GB, 128GB would struggle, 256GB comfortable
- GGUF quants (Unsloth, DevQuasar) available pre-built — no need to convert from safetensors

**llama.cpp n-gram speculative decoding reference:**

Available spec types (stackable via comma-separation):
- `ngram-simple` — basic n-gram lookup
- `ngram-map-k` — n-gram map (K cache only)
- `ngram-map-k4v` — n-gram map (K+V cache)
- `ngram-mod` — modular n-gram with configurable N range
- `ngram-cache` — n-gram with persistent cache

SSD offload for n-gram lookup table:
- `--lookup-cache-static /path/cache.bin` — load static cache, not updated during generation
- `--lookup-cache-dynamic /path/ngram_cache.bin` — load AND update cache during generation, persists and improves across runs (the SSD offload option)

Tuning parameters:
- `--spec-ngram-simple-size-n 12` — lookup n-gram length (tokens to match on)
- `--spec-ngram-simple-size-m 48` — draft m-gram length (tokens to generate as draft)
- `--spec-ngram-simple-min-hits 1` — minimum hits before accepting draft
- For ngram-mod: `--spec-ngram-mod-n-min 48`, `--spec-ngram-mod-n-max 64`, `--spec-ngram-mod-n-match 24`

Full SSD-offload example:
```
llama-server --model model.gguf --spec-type ngram-cache --lookup-cache-dynamic /mnt/ssd/ngram_cache.bin --spec-ngram-simple-size-n 12 --spec-ngram-simple-size-m 48
```

Use a fast NVMe SSD — SATA SSDs will likely be too slow for benefit.

## Security

N/A — reference content, not software.

## Usage notes

- Daily-driver report (r/LocalLLM, Oct 2026): Qwen 3.8 Flash Next (plus some 27B) on an Asus ROG Flow Z13 Strix Halo laptop (128GB unified memory), full 256K context, ~1,200+ tok/s prefill and ~40 tok/s decode; the author's merged PRs on a Rust repo (github.com/llamastash/llamastash, PRs labeled "Qwen") were produced this way and the setup prompt is published as a gist (gist.github.com/deepu105/d0b321f3256edf67ebd85e747c0010b9). Commenters on Strix Halo report 50 tok/s decode / 1,200–1,700 tok/s prefill with gufo and up to ~2,000 tok/s prefill on recent halogen builds; one OpenCode Go user reported loops and poor quality from Flash, attributed in-thread to harness/inference config; an M5 Max 128GB user noted Flash Next's ~6B active parameters suit unified-memory Macs but sometimes produces less-batched implementations than Opus.
