---
name: qwen25-coder-32b
title: Qwen2.5-Coder-32B-Instruct
url: "https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct"
category: framework
summary: "Alibaba's 32.5B-parameter code-specialized open-weight LLM — 64-layer transformer with GQA (40Q/8KV), 128K context via YaRN, trained on 5.5T tokens including source code and synthetic data; coding abilities reported as matching GPT-4o; Apache-2.0"
tags: [llm, code-generation, open-weights, qwen, alibaba, local-inference]
reviewed: 2026-06-26
acquired: 2026-06-26
license: Apache-2.0
security_flags: []
overlaps: [qwen36-27b]
source: unknown
---

## What it does

Qwen2.5-Coder-32B-Instruct is the instruction-tuned variant of Alibaba's code-specialized large language model series (formerly CodeQwen). It is a 32.5B-parameter causal language model trained on 5.5 trillion tokens including source code, text-code grounding data, and synthetic data.

The model family covers six sizes (0.5B, 1.5B, 3B, 7B, 14B, 32B). The 32B variant is positioned as the strongest open-source code LLM at its release, with coding benchmarks reported as matching GPT-4o.

## Key takeaways

- Architecture: Transformer with RoPE positional embeddings, SwiGLU activation, RMSNorm, and attention QKV bias. Uses grouped-query attention (40 query heads, 8 KV heads) across 64 layers.
- 128K context via YaRN rope scaling (factor 4.0, base 32K). Default config.json ships with 32K; YaRN config must be added manually for longer contexts.
- Maintains general and mathematical capabilities alongside code specialization — not a code-only model.
- vLLM is the recommended deployment backend for production serving.
- Requires `transformers>=4.37.0`.

## Mechanical details

- **Parameters:** 32.5B total, 31.0B non-embedding.
- **Training:** 5.5T tokens (source code + text-code grounding + synthetic).
- **Context:** 32K default, 128K with YaRN config.
- **Deployment:** HuggingFace transformers, vLLM recommended for production. Standard `AutoModelForCausalLM` + `AutoTokenizer` loading.
- **Long context:** Add `rope_scaling: {factor: 4.0, original_max_position_embeddings: 32768, type: "yarn"}` to config.json. vLLM only supports static YARN (constant scaling factor regardless of input length).

## Security

Open-weight model under Apache-2.0. Standard HuggingFace distribution. No unusual dependencies beyond `transformers>=4.37.0`. Model weights are hosted on HuggingFace Hub with standard checksums.