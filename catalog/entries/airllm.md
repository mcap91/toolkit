---
name: airllm
title: AirLLM
url: "https://github.com/lyogavin/airllm"
category: framework
summary: "Clever layer-shard inference to run 70B models on 4GB VRAM, but maintenance has stalled since August 2024 while better-maintained alternatives (Ollama/llama.cpp) have matured."
tags: [llm-inference, low-vram, memory-optimization, python, huggingface, quantization]
reviewed: 2026-06-10
acquired: 2026-06-10
license: Apache-2.0
security_flags: [no-ci-evidence, stale-since-2024, community-contributed-cpu-backend]
overlaps: []
source: unknown
---

## What it does

AirLLM is a Python library that enables running large language models (70B parameters and up) on consumer GPUs with as little as 4GB VRAM, and 405B Llama3.1 on 8GB VRAM. It achieves this by decomposing a HuggingFace model into per-layer shards saved to disk, then loading and executing one layer (or a small set of layers) at a time during inference. No quantization is required for the base mode, though optional block-wise 4bit/8bit quantization is supported for up to 3x throughput improvement with minimal accuracy loss. The API mirrors the HuggingFace Transformers interface (`AutoModel.from_pretrained`, `model.generate`), making migration straightforward. Supported models include Llama 2/3/3.1, Mixtral, Mistral, ChatGLM, Qwen/Qwen2.5, Baichuan, and InternLM. macOS (Apple Silicon via mlx) and CPU inference are also supported as of v2.10.1.

## Assessment

The core technique — sequential layer-shard loading to sidestep VRAM limits — is genuinely useful for resource-constrained inference and was novel when released in late 2023. However, the project's last tagged update is v2.11.0 from August 2024, with no subsequent activity visible. The broader ecosystem (Ollama with GGUF quantization, llama.cpp, ExLlamaV2) now covers the same use-case with active maintenance, broader hardware support, better throughput, and quantization that is more mature than AirLLM's block-wise approach. Worth monitoring in case development resumes, but not the right choice for new deployments today.

## Mechanical details

- **Install:** `pip install airllm` (plus `bitsandbytes` for quantization; `mlx` and `torch` for macOS)
- **Init:** `AutoModel.from_pretrained(repo_id_or_local_path, compression='4bit'|'8bit'|None, hf_token=..., layer_shards_saving_path=..., delete_original=True)`
- **Inference:** standard HuggingFace `model.generate()` call; tokenizer is attached as `model.tokenizer`
- **First run:** the model is split into layer shards and saved to disk (HuggingFace cache by default); subsequent runs skip re-splitting. Ensure sufficient disk space (~2x model size during conversion).
- **Prefetching:** enabled by default (overlaps disk loading with compute); ~10% speed improvement for Llama2 class.
- **Compression config:** only weights are quantized (not activations), which the authors argue preserves accuracy better than full quantization — the bottleneck is disk I/O, not compute.
- **What to adopt if needed:** the `delete_original=True` flag to halve disk usage, and 4bit compression for throughput, are the two most impactful options if this library is evaluated.

## Security

- **License:** Apache-2.0 — permissive, no copyleft obligations.
- **Dependencies:** PyTorch, HuggingFace Transformers, bitsandbytes (optional), mlx (optional). None are pinned in the README; the CPU inference backend was contributed by a community contributor (@NavodPeiris) and carries the usual review uncertainty of external contributions.
- **CI/tests:** No CI configuration or test suite is referenced in the README. No evidence of automated testing found.
- **Supply chain:** Single primary maintainer (Gavin Li / lyogavin); few contributors. No signed releases visible. Release cadence was rapid in late 2023 but has slowed to a stop as of mid-2024.
- **Dangerous patterns:** No eval(), shell injection vectors, or credential handling issues identified. HuggingFace token (`hf_token`) is passed as a plain string argument — callers should avoid logging or persisting it.
- **Maintenance:** Last commit visible August 2024. Open issues and responsiveness to PRs not verified (GitHub API not queried), but active development appears to have ceased.
- **Overall:** Low direct security risk for the library itself; the main concern is using a stale, undertested dependency in a production pipeline.
