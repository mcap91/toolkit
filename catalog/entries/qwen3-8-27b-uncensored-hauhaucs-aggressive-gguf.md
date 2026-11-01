---
name: qwen3-8-27b-uncensored-hauhaucs-aggressive-gguf
title: Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF
url: "https://huggingface.co/HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF"
category: framework
summary: "Community-produced GGUF quantization of Qwen3.8-27B with safety-refusal behavior deliberately stripped ('uncensored'/abliterated 'Aggressive' profile, publisher-claimed 0/465 refusals), published by pseudonymous Hugging Face contributor HauhauCS; ships multiple quant levels plus a vision projector and a custom 'FastMTP' speculative-decoding sidecar requiring a llama.cpp patch"
tags: [gguf, quantization, uncensored, abliteration, qwen, llama-cpp, local-inference, vision-language-model, speculative-decoding, mtp]
reviewed: 2026-08-25
acquired: 2026-08-25
license: Apache-2.0
security_flags:
  - "UNCENSORED/ABLITERATED MODEL: publisher explicitly markets this as safety-guardrail-removed — Qwen3.8-27B uncensored by HauhauCS, 0/465 Refusals, Aggressive variant: direct answers, no refusal behavior, and minimal preamble on hard prompts; refusal behavior for harmful/hard prompts is intentionally disabled relative to the base Qwen3.8-27B release"
  - "Unverified community artifact from a pseudonymous, non-affiliated publisher (HauhauCS): not the original Qwen/Alibaba release; publisher self-signs its own release manifest with an Ed25519 key it also generated, which authenticates file integrity against HauhauCS's own claims but does not constitute third-party verification"
  - "Independent third-party benchmarking (Nathan Sapwell, Uncensored LLM Abliteration Benchmarked) of other HauhauCS releases found the 0/N refusals marketing claim only partially accurate — some soft/truncated refusals remained under adversarial testing — so the 0/465 figure for this specific release should be treated as an unverified publisher claim"
  - "Running the bundled HauhauCS FastMTP acceleration sidecar requires downloading and applying a third-party patch file to a llama.cpp source checkout and compiling it (git apply of HauhauCS-FastMTP-llama.cpp.patch) — review the patch before applying, as with any third-party build patch"
overlaps: []
source: unknown
---

## What it does

This is a GGUF-format redistribution of Qwen/Qwen3.8-27B (dense 27B causal LM with vision encoder, 64 layers, 262,144-token native context) produced by Hugging Face contributor "HauhauCS," modified with an "uncensoring" post-processing profile the publisher calls "Aggressive." The publisher states the release makes "no changes to datasets or intended capabilities" beyond applying this uncensoring profile, and preserves Qwen3.8's native NextN/MTP (multi-token-prediction) head. The publisher also markets a "HauhauCS FastMTP" acceleration sidecar — a compact draft model plus a required llama.cpp source patch — claimed to speed up token generation (TG) versus both no-MTP and Qwen's standard embedded MTP, at "identical output" to the un-accelerated target model (verified via output-hash matching in the publisher's own reported tests).

Multiple GGUF quantization levels are provided (Q2_K_P through Q8_K_P, plus IQ2/IQ3/IQ4 variants), including publisher-defined "K_P" ("Perfect") quants said to use per-model analysis to selectively preserve quality. A separate BF16 vision projector file (`mmproj-...-BF16.gguf`) is required for image/video input. A "Balanced" (less aggressive) uncensoring variant is referenced as existing "if one is available" for reliability-sensitive agentic use, but is not the artifact at this URL.

## Differentiators / Key takeaways

- Explicitly and intentionally removes refusal behavior from the base model rather than being an incidental side effect of quantization.
- Bundles a from-scratch speculative-decoding acceleration path ("FastMTP") distinct from and layered on top of Qwen3.8's own built-in MTP head, requiring a custom llama.cpp patch to use.
- Publisher provides a self-signed authenticity scheme (Ed25519-signed release manifest + per-file SHA-256 and "canonical tensor fingerprint") to detect tampering/renaming of files — this proves file integrity against HauhauCS's own signature, not third-party trustworthiness of the content.
- Part of a large catalog of similarly-branded "Uncensored-HauhauCS" releases across many base model families (Qwen, GPT-OSS, Gemma, etc.), per third-party reporting.

## Mechanical details

- Base model: Qwen/Qwen3.8-27B (Apache-2.0), 64 language-model layers, hidden size 5,120, FFN size 17,408, 248,320-token vocabulary, 48 Gated DeltaNet + 16 gated-attention layers, native 262,144-token context (extensible to 1,000,000 with framework-specific config).
- Quant files range from Q2_K_P (3.12 BPW, 10.68 GB) to Q8_K_P (9.21 BPW, 31.46 GB); IQ2_M/IQ3_M/IQ3_XS/IQ4_XS variants also provided.
- FastMTP sidecar file: `Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-FastMTP-32K.gguf` (903 MB), used with `--spec-type draft-mtp` on a patched llama.cpp build (patch applied via `git apply` against a pinned commit).
- Compatible with llama.cpp and GGUF-compatible runtimes (LM Studio, Jan, KoboldCpp) at base level; FastMTP requires the patch and rebuild.
- Recommended sampling settings mirror the official Qwen3.8 model card (thinking mode: temp 1.0/top_p 0.95/top_k 20; instruct mode: temp 0.7/top_p 0.80, presence_penalty 1.5).
- License: publisher states the release "retains" Qwen3.8-27B's Apache-2.0 license from Qwen.

## Security

- **License**: Apache-2.0 (inherited from Qwen3.8-27B per publisher statement; not independently verified against Qwen's actual license grant for derivative/modified weights).
- **Safety posture**: Deliberately removes refusal/safety behavior from the base model ("uncensored," "Aggressive" profile) — this is the artifact's stated purpose, not an incidental flaw.
- **Supply chain**: Published by a pseudonymous individual contributor (HauhauCS, associated with Reddit account u/hauhau901 per third-party reporting), not an organization or the original model vendor; authenticity is self-attested via a publisher-controlled Ed25519 key, not a third-party CA or the base model publisher.
- **Benchmark provenance**: "0/465 Refusals" and FastMTP speed-up figures (e.g., "3.02x document TG") are publisher-reported; independent third-party testing of other releases in this same publisher's lineup found partial refusal leakage under adversarial testing despite zero-refusal marketing claims.
- **Build risk**: FastMTP requires cloning llama.cpp, checking out a pinned commit, and applying a third-party `.patch` file before compiling — this executes third-party source-code changes into a locally built binary; review the patch contents before applying.

## Usage notes

- **Community data point — Qwen3.8-Flash-Next-Uncensored (orcarouter)**: IQ4_XS quant running at 22 tok/s on desktop hardware (128GB RAM, 32GB VRAM), fully in memory. Reported as "uncensored to the point that it's a bit concerning" — suggesting aggressive abliteration in this variant.
