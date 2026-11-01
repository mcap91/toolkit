---
name: ollama-system-one-api
title: Ollama System One API (Decision Models)
url: "https://docs.ollama.com/api/systemone"
category: framework
summary: "Local decision-model endpoint in Ollama 0.35+ — Jev-compatible /v1/systemone API returns typed choices, yes/no probabilities, and rubric scores instead of generated text; ships three models (Nimble 9B from Bespoke Labs, Tev1 4B and 0.8B from Together AI); 91ms average latency on M5 Max; runs entirely offline; MIT"
tags: [decision-models, local-inference, ollama, classification, scoring, jev-compatible, nimble, tev1, typed-output]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: [laya-decision-model]
license: MIT
security_flags: []
source: unknown
---

## What it does

Ollama 0.35 adds a `/v1/systemone` endpoint that runs decision models locally. Instead of generating text, these models return structured decisions: a choice from a set of options, a yes/no answer with a probability, or a score against a rubric. The API is wire-compatible with TypeSafe's Jev API.

Three models ship at launch:

- **Nimble 9B** (Bespoke Labs): 9.5 GB Q8_0 download. Mean accuracy 75.7% on Bespoke Labs' 13 public human-labelled datasets (3,880 decisions), vs 76.0% for Jev 1.13. Average 91ms per decision on Apple M5 Max.
- **Tev1 4B** (Together AI): 4.5 GB download. Mean accuracy 73.3% on same benchmark.
- **Tev1 0.8B** (Together AI): 812 MB download. Mean accuracy 63.5% on same benchmark.

Use cases: ticket triage, model routing, content classification, sentiment scoring, content moderation.

## Mechanical details

API: `POST http://localhost:11434/v1/systemone` with fields `model`, `state` (the text to evaluate), `questions` (array of decision questions), and optional `keep_alive`.

Wire format compatibility: the same `/v1/systemone` shape works across TypeSafe (Jev direct), Ollama 0.35+ (Nimble/Tev1), and OpenRouter (`/api/alpha/decisions`).

v0.35.0 is tagged as a pre-release (published 2026-09-28). CLI and client libraries do not yet support decision models — use the HTTP API or TypeSafe's SDK directly.

Install: `ollama pull nimble` or `ollama pull tev1` (or `tev1:0.8b`).

## Security

MIT licensed. Runs entirely local — no data leaves the machine. Models carry their own licenses. Same localhost binding as standard Ollama.