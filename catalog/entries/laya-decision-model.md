---
name: laya-decision-model
title: Laya
url: "https://github.com/receptron/laya"
category: framework
summary: "Open-source non-autoregressive decision model from Convai Innovations — 421M params (ModernBERT-large backbone) English, 322M multilingual (100+ languages); single forward pass in ~33-40ms on T4; three primitives (choice, score, noul); accuracy 0.766 vs Jev's 0.727 on typed-decisions benchmark at 7.8x lower latency; self-hosted, zero marginal cost; Apache 2.0"
tags: [decision-models, open-source, classification, scoring, jev-alternative, modernbert, non-autoregressive, multilingual, apache-2, self-hosted]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: [ollama-system-one-api, cloudflare-clef]
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

Laya is a non-autoregressive decision engine that performs typed classification in a single forward pass, returning calibrated probability distributions instead of generated text. Three primitives: choice (select from options), score (rate against a rubric), noul (yes/no with probability).

Two checkpoints:
- **English** (ModernBERT-large + decision head): 421M params, 512 context, ~39.5ms on T4
- **Multilingual** (mmBERT-base): 322M params, 1024 context, 100+ languages, ~32.8ms on T4

Performance vs Jev 1.13.0: accuracy 0.766 vs 0.727 on typed-decisions benchmark, latency 33ms vs 236-276ms (7.8x faster). Limitation: accuracy collapses past ~20 options in a choice question (0.425 vs Jev's 0.870 at 77 options) — wide categorical decisions need a two-step hierarchy.

Zero-shot performance is limited: 0.362 accuracy (vs 0.318 random baseline), so fine-tuning on task-specific data is expected for production use.

From Convai Innovations (Kasaragod, Kerala, India). Released 2026-09-18. ~7,900 GitHub stars in first 3 days.

## Mechanical details

Weights on HuggingFace under Apache 2.0. Self-hosting cost: $0/M tokens (vs Jev's $0.042/M tokens). Node.js/TypeScript integration via ONNX Runtime. Jev-compatible API wire format.

Third checkpoint available: typed-decisions fine-tune for the benchmark's training split.

## Security

Apache 2.0 licensed. Runs entirely locally. No network calls required. No telemetry.