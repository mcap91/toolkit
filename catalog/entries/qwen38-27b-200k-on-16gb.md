---
name: qwen38-27b-200k-on-16gb
title: Qwen 3.8 27B at 200K Context on 16GB VRAM (tutorial)
url: "https://huggingface.co/unsloth/Qwen3.8-27B-GGUF"
category: agent-pattern
summary: "Practitioner recipe for running Qwen 3.8 27B UD-IQ4_XS at ~196K context and 50 t/s on a single RTX 5070 Ti (16GB) — prune non-ASCII rows from the embedding table and LM head (~700MB, ASCII-condensed variant published), offload the embedding table to CPU, disable MTP, use adaptive-KV streaming (llama.cpp fork) to page KV cache from host RAM, and quantize cache Q8 K / Q4 V"
tags: [qwen, local-inference, llama-cpp, quantization, kv-cache, long-context, vram-optimization, gguf, unsloth, embedding-pruning]
reviewed: 2026-09-10
acquired: 2026-09-10
license: LicenseRef-forum-content
security_flags: [community-modified-weights]
overlaps: [kv-cache-vram-sizing, qwen3-8-27b-uncensored-hauhaucs-aggressive-gguf]
source: unknown
---

## What it says

A tutorial post for fitting Qwen 3.8 27B with ~196K tokens of context on a 16GB consumer GPU (RTX 5070 Ti, Ryzen 7 9700X, Windows 11) at ~50 t/s, stacking five techniques:

1. **Base quant:** Unsloth's UD-IQ4_XS GGUF of Qwen3.8-27B.
2. **Embedding/LM-head pruning:** since Qwen3.8 reasons exclusively in English unless prompted otherwise and the workload is English + code, prune most non-ASCII rows from the embedding table and LM head, saving ~700MB (author published the result as `bsaleh03/Qwen3.8-27B-ASCII-Condensed`).
3. **CPU-offload the embedding table** (`-ot "token_embd.weight=CPU"`): another 270MB of VRAM freed.
4. **Disable MTP** (keep the multi-token-prediction head off the GPU), leaving 3.6GB for context — 84K tokens natively.
5. **Adaptive-KV streaming:** a llama.cpp fork (`RaymondHuang210129/llama.cpp-adaptive-kv-streaming`) pages the KV cache and streams it from host RAM at some depth-performance cost; with Q8 K-cache and Q4 V-cache quantization this reaches 196,608 tokens.

Full args: `-ngl 99 -fa on -ctk q8_0 -ctv q4_0 -np 1 -ub 128 -b 512 -ot "token_embd.weight=CPU" --jinja`.

## Key takeaways

- Vocabulary pruning is an unusual lever: when the workload is ASCII-only, the multilingual embedding rows are dead weight recoverable as context budget.
- The stack is composable — each step is independent (quant, prune, offload, MTP off, KV paging), so partial adoption is possible on other hardware.
- KV paging trades throughput at depth for context length; the 50 t/s figure is at the author's settings, not at full 196K depth.

## What to adopt

- The exact llama.cpp argument set for 16GB-class GPUs running 27B models long-context.
- The ASCII-condensed pruning idea generalizes to any English/code-only local deployment.

## Security

- `community-modified-weights` — both the pruned model and the adaptive-KV llama.cpp fork are individual community artifacts without upstream review; weights modified by a third party warrant verification against the base model before trust-sensitive use.
- Forum tutorial; performance numbers are the author's single-machine reports.

## Usage notes

- **Agentic coding benchmark (Strix Halo 128GB)**: Qwen 3.8 27B Q6_K (~31 GiB) on ASUS ROG Flow Z13 (Ryzen AI Max+ 395) using llama.cpp + LlamaStash + Pi harness. 27B at xhigh scores 34 on Artificial Analysis index vs Opus 4.6's 32; one-shotted a whole feature on a large Rust codebase. Flash Next (UD-Q4_K_XL, ~86 GiB) scores 40 vs Opus 4.8's 42. MTP gives 7.3→22.4 tok/s on empty window but payoff shrinks at full context (1.15x at 256K). Key insight: thinking tokens are 90–95% of output, so Flash Next's 45% fewer tokens (76.5s vs 289.8s) matters more than tok/s. Prefill is the bottleneck — cold 31K token transcript takes 3 min, 128K ~18 min; warm follow-ups ~45s.

- **3090 Ti community throughput (24GB)**: Qwen3.8-27B is a dense 27B that fits 262K context on one 24GB 3090 Ti via hybrid attention — most layers use cheap linear/GDN-style attention (fixed-size state), only some layers keep a real KV cache. Community numbers on 3090/3090 Ti: ~75 t/s through 100K on a single long generation, ~99–124 t/s on short/chat prompts, ~300+ on RAG-copy tasks (draft acceptance is easy). Speed kit: tight quant (weights leave room for cache/state, ~23 GB used), MTP (biggest free speedup), FP8 KV + int8 head quantization, custom Ampere kernels (LlamAmpere-style forks). Reality checks: native 262K max ≠ practical at full depth; decode at 8K ≠ decode at 200K; 3090 Ti draws 350–450 W.
- **LiteLLM compaction proxy**: for faster prefill, add a Qwen 4B to llama.cpp and use LiteLLM to detect compaction requests, proxying them to the 4B model. llama.cpp auto-unloads and reloads models. The full swap is faster than waiting on the 27B model to compact.

- **Custom imatrix quants (r/unsloth, Sep 2026):** Practitioner-made IQ4_XS quants (stock + abliterated) with importance matrix blending general corpus + ~1M tokens of SEC-contract/financial text. Results: 93.2% on 59-task domain harness vs 89.8% for Unsloth UD-IQ4_XS; KL parity with BF16. Key finding: token embedding layer upgrade from q3_K to q4_K closed the last gap. Decode: ~70 t/s with MTP at 32K, ~27 t/s at 64K (MTP incompatible with extended context), ~20 t/s at 96K (beellama kvarn4 KV), ~15 t/s at 105K+ (kv-stream fork, usable to 252K). Vocab pruned to 141K tokens (English + accented Latin) so 64K fits natively; full-vocab multilingual builds also available. Vision works (quantized projector). Thinking-off recommended for agents; high reasoning effort worth +5 tasks, xhigh adds nothing over high.
- **beellama kvarn4 at 109K (r/unsloth):** Anbeeld/beellama.cpp with `--cache-type-k kvarn4 --cache-type-v kvarn4` + `--kv-tail-tokens 1024` reported 70 t/s at 109K context on 16GB 5070Ti with IQ3_S quant. Combines MTP + ngram-mod speculative decoding. Branch 0.4.7 has performance/memory improvements not yet in main.
- **Q4_K_S practitioner notes (r/LocalLLaMA):** Running Q4_K_S with Q8_0 context quantization in Pi agent (Docker sandbox on Raspberry Pi). Swift-Qwen faster but prone to loops; stock Qwen more reliable. Edit tool weakest link — model frequently retries due to indentation errors. kv-streaming fork (github.com/troed/llama.cpp-adaptive-kv-streaming) enables context >160K on 16GB. Podman sandbox MCP: git.sync.wtf/troed/umwelt.

- Practitioner report (r/Qwen_AI, Oct 2026), one month of work use: Qwen 3.8 27B FP8 on a single 48GB NVIDIA L40S via vLLM (batch size 4, multi-token prediction 3) averaging ~28 tok/s at xhigh effort; harness was Zed + Qwen Code + a SearXNG MCP server for web research. Reported comparable results to Opus 4.8 on the same planning/SQL/Spark-analysis tasks (cross-reviewed by Opus 5.5), reliable adherence to QWEN.md/AGENTS.md rules, and autonomous tool use (wrote a PDF-extraction script; ran EXPLAIN ANALYZE against a DB given read-only credentials). Speed (minutes to ~1 hour per task) was the main reason the author still mostly used Opus.
- Same thread: several commenters report Qwen 3.8 Flash Next (MoE) hallucinating more than dense 27B in unattended agentic runs, especially below 4-bit quants; others recommend the Swift-1.5-Qwen3.8-27b fine-tune (huggingface.co/ukisai/Swift-1.5-Qwen3.8-27b) for shorter thinking.
