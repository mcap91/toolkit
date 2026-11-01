---
name: subtext
title: Subtext
url: "https://github.com/ninjahawk/Subtext"
category: framework
summary: "Live Jacobian-lens viewer that renders a local model's internal 'global workspace' during chat — reads Anthropic's Jacobian lens at 9 layers per token over Qwen3.5-4B, showing verdicts/plans forming before they are spoken; browser canvas + per-token ledger, scrubbable GPU-free replays; validated against Anthropic's reference impl; Apache-2.0"
tags: [interpretability, jacobian-lens, global-workspace, mechanistic-interpretability, qwen, local-inference, visualization, research]
reviewed: 2026-07-09
acquired: 2026-07-09
license: Apache-2.0
security_flags: [single-contributor, unaudited-model-download]
overlaps: []
source: unknown
---

## What it is

Subtext is an independent, Apache-2.0 tool that visualizes a language model's internal "global workspace" live during a conversation. It builds on Anthropic's Jacobian-lens research (the "J-space" / global-workspace work): the Jacobian lens transports a residual-stream activation at any layer into the final-layer basis and decodes it through the model's own unembedding, yielding which vocabulary words an internal state is disposed toward. Subtext applies this continuously, reading the lens at nine layer depths on every token — both while the model reads the user's message and while it generates — and renders the readouts as they happen.

## How it works

A Python server (`server.py`) runs Qwen3.5-4B (bf16, HuggingFace transformers, KV cache) with a pre-fitted Jacobian lens from Neuronpedia (`neuronpedia/jacobian-lens`, revision `qwen-n1000`). Per token it takes residual hooks at 9 layers, applies the lens transport and unembedding, softmaxes over the full vocabulary, and streams word-start top-k readouts over a websocket to a single-file browser UI. The display encodes layer as vertical position and readout strength as size/opacity; amber marks readouts taken while reading the user, blue while generating. A per-token ledger, a per-word aggregate ("words" tab), and a trace view (word strength across layers × tokens) accompany the live canvas, and a transport bar seeks to any token. Sessions export to JSON (every lens frame included) and replay in any browser via `?replay=<file-url>` with no GPU — the hosted demo is such a replay.

## Requirements and models

Requires an NVIDIA GPU (~10 GB VRAM, CUDA PyTorch) or Apple Silicon (16 GB+, `mps`, macOS 14+, PyTorch ≥ 2.3), Python 3.11+; falls back to CPU (slow). First launch downloads ~9 GB of model + lens. Configured for Qwen3.5-4B because Neuronpedia publishes a pre-fitted lens for it (a 27B lens also exists); any HuggingFace decoder can be used by fitting a lens with `jlens.fit()`. On Windows, run `python -u -X utf8 server.py` or `start.bat`.

## Validation and stated limits

`verify_accuracy.py` compares the live path (forward hooks, KV cache) against the reference `JacobianLens.apply()` on identical inputs; across 4 layers × 3 positions the top-5 readouts match exactly, cosine similarity is ≥ 0.99998 between logit vectors, and the expected two-hop intermediates reproduce. The README states the lens reads only single-token concepts (multi-token concepts are invisible or fragmentary), captures the paper's workspace approximately rather than the entire internal state, and that readouts demonstrate functional availability of information for report and reasoning, not subjective experience.

## Security

Apache-2.0, single-contributor independent project (stated as not affiliated with Anthropic). Runs a local server on `localhost:8765` and loads a local model; the main external action is a one-time ~9 GB download of model and lens weights from HuggingFace, which are not independently audited here. No credentials or API keys are required.