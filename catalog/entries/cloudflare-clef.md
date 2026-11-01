---
name: cloudflare-clef
title: Cloudflare Clef
url: "https://huggingface.co/cloudflare/clef"
category: framework
summary: "Open-weight decision models from Cloudflare — Clef (27B, Qwen 3.8-27B backbone, 209ms median) and Clef-flash (9B, Qwen 3.5-9B backbone, 39ms median); return typed probabilities instead of text; 64K context; vision encoder (up to 4 images); RL fine-tuning platform on Workers AI; beats Jev on 7/10 benchmarks; Apache 2.0"
tags: [decision-models, cloudflare, open-weights, classification, scoring, jev-competitor, vision, workers-ai, apache-2, non-autoregressive]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: [ollama-system-one-api]
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

Clef and Clef-flash are Cloudflare's first in-house trained AI models — non-autoregressive decision models that return typed probabilities for every allowed answer, with no free-form text generation. Released 2026-10-01.

Two variants:

| | Clef | Clef-flash |
|---|---|---|
| Parameters | 27B | 9B |
| Backbone | Qwen 3.8-27B | Qwen 3.5-9B |
| Median latency | 209.3ms | 38.8ms |
| Context | 64K tokens | 64K tokens |

Both include a vision encoder supporting up to 4 images per request.

Competitive position: beats Jev (the category creator from TypeSafe) on 7 of 10 benchmarks. Released alongside OpenAI's Decisions API and Amazon's Strands Decider 2B — Cloudflare is the only one offering full open weights under Apache 2.0.

Use cases: agent action selection, routing, classification, content moderation, ticket triage.

## Mechanical details

Open weights on HuggingFace under Apache 2.0 — run on your own hardware or use the hosted Workers AI API ($0.24/M tokens for Clef, $0.09/M for Clef-flash).

Cloudflare also debuted an RL fine-tuning platform on Workers AI for adapting the models to specific workloads.

## Security

Apache 2.0 licensed. Open weights — full self-hosting possible. Workers AI API is metered. Vision encoder processes images locally within the model.

## Usage notes

- Per Cloudflare's own benchmark, Clef-flash answered in ~38ms versus Jev's ~520ms (about 10x faster) (source: https://www.instagram.com/reel/DeIV3Tam24w/)
