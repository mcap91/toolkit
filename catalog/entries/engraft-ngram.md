---
name: engraft-ngram
title: ENGRAFT
url: "https://github.com/fulvian/engraft-ngram"
category: framework
summary: "Technique for writing facts into an LLM's n-gram (Engram) lookup table by gradient descent on table rows only — no weight changes, one removable overlay file; measured on Qwen3.8-Flash-Next (320M-row table); 84.1% exact-match on 100 invented facts, 0.013 KL divergence on neutral text; gradient runs on CPU replica, verified on llama.cpp GGUF; early-stage research"
tags: [engram, n-gram, knowledge-editing, qwen, llama-cpp, model-editing, overlay, local-inference]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: ""
security_flags: [early-stage, single-model-validated]
source: unknown
---

## What it does

ENGRAFT writes new facts into the Engram-style n-gram lookup table that some LLMs carry alongside the transformer (DeepSeek V4.1 Flash, Qwen3.8-Flash-Next) by gradient descent on selected table rows only. The transformer weights stay frozen and the model file is never modified. New facts ship as one small overlay file; remove it and the model is back, bit for bit.

A fact lives in the rows its n-grams hash to and fires when a prompt contains those n-grams. It sits inside the model's own forward pass — no context tokens, no retriever, no second model.

Key measurements on Qwen3.8-Flash-Next (IQ4_XS, 320M-row table):

- **Accuracy**: 84.1% exact-match (707/841 test sentences) on 100 invented facts; 35/98 correct when asked freely in chat.
- **Capacity**: no ceiling found — 24 facts (0.804), 100 facts (0.792), 300 facts (0.821) on first-token-ranked metric.
- **Collateral damage**: 0.013 KL divergence on neutral text (~4x the table's own 4-bit storage noise); grows with fact count.
- **Cross-lingual**: a fact written in Chinese left Italian questions exactly where the base model had them (one language pair measured).

## Mechanical details

Gradient descent runs on a CPU replica; results verified on the real llama.cpp inference engine, not only on the replica. The Engram table has 320M padded rows of width 160 (51.2B parameters stored in CPU RAM). Each position hashes the last 2 and 3 tokens via 16 heads into 16 rows, added at block 1. Training takes hours per fact set, not milliseconds.

Limitations stated by the authors: single model validated, composition across subjects untested, not general knowledge editing, sentences sharing no n-gram with training corpus are uncovered by construction. v0.2.2 as of September 2026.

## Security

Early-stage research. License not specified in repository. Overlay files are additive and removable — no permanent model modification. The technique was built in Claude Code sessions by a single human operator; design, implementation, adversarial review, and verification done by separate model instances.