---
name: mlx-vlm-turboquant
title: mlx-vlm TurboQuant (Apple Silicon KV Cache Compression)
url: "https://github.com/Blaizzy/mlx-vlm/pull/858"
category: framework
summary: Production-quality Metal kernels implementing TurboQuant on Apple Silicon; benchmarked and ready for review but PR not yet merged
tags: [quantization, kv-cache, apple-silicon, mlx, metal, inference, vision-language]
reviewed: 2026-06-16
acquired: 2026-06-16
license: MIT
security_flags: [pr-not-merged]
overlaps: [turboquant]
source: unknown
---

## What it does

PR #858 on mlx-vlm adds TurboQuant KV cache compression for Apple Silicon via custom Metal kernels. Implements the full PolarQuant + QJL pipeline as GPU-native operations: `_mse_score_kernel`, `_pack_lowbit_kernel`, `_unpack_lowbit_kernel`, `_qjl_score_kernel`, `_prod_score_kernel`, plus fused integer decode kernels.

Key results from the PR benchmarks:
- 3–4 bit KV cache quantization with zero accuracy loss
- Single fused kernel replaces 4 separate Metal dispatches (2.7x decode speedup)
- Float16 norms save 9% KV memory
- Multi-query score kernel: 28ms → 12ms at 64k context
- Prefill attention optimization via dedicated MQ score path

## Assessment

**Pilot.** The implementation is thorough — 20+ commits with detailed Metal kernel work, benchmarks, NIAH test suite, and PPL evaluation. Author (Blaizzy) is the mlx-vlm maintainer. Co-authored with Claude Opus 4.6. PR is marked ready for review (April 2, 2026) but not yet merged. Once merged, this becomes the canonical TurboQuant path for Apple Silicon local inference. Monitor for merge.

## Mechanical details

- Adds `TurboQuantKVCache` class as drop-in replacement for MLX's standard KV cache
- `scaled_dot_product_attention` updated to handle single-query fast path for decode
- Conservative capacity growth in `_reserve_state_capacity` prevents excessive memory allocation
- `QuantizedStateProxy` provides compatibility with models expecting `.keys.shape` access
- Supports 3-bit and 4-bit modes via fractional `self.bits` attribute
- References `turboquant-pytorch` and `turboquant_plus` for cross-validation

## Security

mlx-vlm is MIT licensed, actively maintained by Blaizzy. The PR adds Metal shader code and Python — no network calls, no credential handling, no eval patterns. Tests are included. Primary risk is the PR-not-merged status: the code may change before landing.