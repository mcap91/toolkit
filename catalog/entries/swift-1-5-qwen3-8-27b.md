---
name: swift-1-5-qwen3-8-27b
title: Swift 1.5 Qwen3.8-27B (UkisAI)
url: https://huggingface.co/ukisai/Swift-1.5-Qwen3.8-27b
category: framework
summary: UkisAI's reasoning-efficient post-trained derivative of Qwen3.8-27B — reduces thinking tokens by a publisher-reported 58.5% while scoring 0.35% higher than the base model on aggregate benchmarks (GPQA-Diamond, C-Eval, IFBench, ERQA, AIME 2026, HMMT, LiveCodeBench v6, Terminal-Bench 2.1), with savings holding across xhigh/medium/low reasoning-effort settings; ships BF16, GGUF/GSQ-RCO GGUF, AWQ/AutoRound/GPTQ INT4, NVFP4, AMD Quark FP8, and Apple MLX exports plus a free OpenAI-compatible demo API; Swift Open License v1.0 (free under $1M annual revenue, enterprise license required above)
tags:
  - qwen
  - fine-tune
  - reasoning-efficiency
  - local-inference
  - gguf
  - vllm
  - sglang
  - quantization
  - huggingface
  - mtp
reviewed: 2026-10-29
acquired: 2026-10-29
license: Swift Open License v1.0 (derivative of Apache-2.0 Qwen3.8-27B)
security_flags:
  - "Custom, revenue-gated license (Swift Open License v1.0): free for personal/research/educational/evaluation/commercial use only up to US$1,000,000 gross annual revenue (including affiliates); above that threshold requires a separate paid Swift Enterprise License from UkisAI — not a standard OSI license despite being built on the Apache-2.0 base model"
overlaps:
  - strata
  - qwen38-27b-200k-on-16gb
source_url: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/
source: reddit
---

## What it does

Swift 1.5 is UkisAI's post-trained (RL + OPD) derivative of Alibaba's Qwen3.8-27B, built to cut "pathological overthinking" — tokens spent on unproductive reasoning — without directly truncating reasoning length, then recovering accuracy with further RL. Publisher-reported results: 58.5% fewer mean thinking tokens on GPQA-Diamond while scoring 0.35% higher aggregate than the base model (88.59% vs 88.28%), with similar token reductions (17-56%) and accuracy parity or small gains across C-Eval, IFBench, ERQA, AIME 2026, HMMT November 2025, LiveCodeBench v6, and Terminal-Bench 2.1; savings persist at xhigh, medium, and low reasoning-effort settings. A publisher demo prompt (building a 3D exploration game) took the base model 104.6 minutes vs 11.39 minutes for Swift 1.5. It is a direct upgrade from an earlier Swift 1.0 release (350k+ downloads), with training data published (though resampled before use) at `ukisai/Qwen3.8-27B-multi-turn-agent-sft`.

## Mechanical details

Main BF16 repo `ukisai/Swift-1.5-Qwen3.8-27b`; exports include GGUF and a compact 2-3-bit GSQ-RCO GGUF for llama.cpp, AWQ INT4 (W4A16), AutoRound INT4 (W4A16), combined AWQ+GPTQ INT4, and NVFP4 for vLLM/NVIDIA Blackwell, AMD Quark FP8 (W8A8), and Apple MLX 5/4/3-bit builds. Serve with vLLM (`vllm serve ukisai/Swift-1.5-Qwen3.8-27b --dtype bfloat16 --tensor-parallel-size 1 --max-model-len 262144 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder`) or a current SGLang build with Qwen3.8 support; both support optional self-speculative MTP decoding via the published MTP head. A free, no-API-key, research-use OpenAI-compatible demo endpoint is hosted at `https://ukisai.com/api/swift/v1` (model id `swift`). Benchmark serving used vLLM 0.27.1-0.29.0 at 131,072-262,144 context, temperature 1.0/top_p 0.95/top_k 20.

## Security

Swift Open License v1.0 for UkisAI's contribution (the adapted weights); the underlying Qwen3.8-27B base remains Apache-2.0 and unrestricted. UkisAI's license is free for personal, research, educational, evaluation, and commercial use up to US$1,000,000 gross annual revenue including affiliates — above that, commercial use needs a separate paid Swift Enterprise License. Quantized/exported variants carry the same license as the parent model per UkisAI's NOTICE file.

## Usage notes

- Recommended in Reddit comments (r/Qwen_AI, Oct 2026) on a Qwen 3.8 27B self-hosting thread as "overthink[ing] much less but mak[ing] good decisions," and noted as already supported by the Strata inference engine. (source: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/)
