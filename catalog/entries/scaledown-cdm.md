---
name: scaledown-cdm
title: ScaleDown Constrained Decoding Models (CDM)
url: https://scaledown.ai/
category: framework
summary: Hosted product line of task-specific 'Constrained Decoding Models' from ScaleDown — Classify, Extract, Summarize, and a pre-existing fourth model Compress — that make one prefill pass over up to 1M tokens of multimodal input and pick an answer/label/span directly from it instead of generating text token-by-token; Classify returns a calibrated probability + reason per label, Extract returns JSON with confidence scores and source citations, Summarize returns a consistent summary under 1,000 tokens; launched Oct 13, 2026, positioned against TypeSafe's Jev, Cloudflare's Clef, and OpenAI's Decisions API in the typed-decision-model space; claims 200x faster and 467x cheaper than frontier LLM APIs and 77.2% vs Jev's 72% on a decision benchmark (self-reported); $0.05/million input tokens (OpenRouter lists $0.04), output free; hosted API only in public docs (api.scaledown.xyz, x-api-key auth), though ScaleDown's CTO has separately described an undocumented self-hosted deployment option; LangChain integration via langchain-scaledown middleware, also listed on OpenRouter and Vercel
tags:
  - decision-models
  - classification
  - extraction
  - summarization
  - constrained-decoding
  - non-autoregressive
  - langchain
  - jev-competitor
  - hosted-api
  - multimodal
reviewed: 2026-10-29
acquired: 2026-10-29
license: ""
security_flags: []
overlaps:
  - jev
  - cloudflare-clef
  - openai-decisions-api
  - laya
  - laya-decision-model
  - ollama-system-one-api
source: instagram
source_url: https://www.instagram.com/reel/Devav4iBMF5/
---

## What it does

ScaleDown is an applied research lab (cofounders Neal Patel, CEO, and Soham Chatterjee, CTO)
that on Oct 13, 2026 launched Constrained Decoding Models (CDMs) — a product line of four
task-specific models: three newly announced (Classify, Extract, Summarize) plus a pre-existing
fourth (Compress).

Mechanism: each CDM makes one prefill pass over up to 1M tokens of multimodal input (text and
images) and selects the answer directly from that input, rather than generating it
token-by-token the way an LLM does. ScaleDown's framing: "You already gave the LLM the answer.
So why is it writing it out from scratch?"

- **Classify**: non-generative; sorts text/images into labels for high-throughput tagging,
  triage, and filtering; returns a calibrated probability and a one-line reason per label.
- **Extract**: takes a natural-language description of the fields wanted and returns
  well-formed JSON with confidence scores and source citations/offsets, from text or images
  (e.g. name + total from a bill).
- **Summarize**: the one CDM that does generate text; takes up to 1M tokens of text, images,
  or PDFs and returns a consistent summary under 1,000 tokens, with no chunking or truncation.
- **Compress**: pre-existing fourth model in the same product line (not detailed in the
  Oct 13 announcement).

Positioned directly against TypeSafe's Jev (launched Sep 15, 2026), which the announcement
credits with proving the "decide, don't write" approach; OpenAI, AWS, and Cloudflare each
shipped comparable typed-decision tools within about two weeks of Jev's launch.

Performance claims (ScaleDown's own figures, not independently benchmarked): 200x faster and
467x cheaper than frontier LLM APIs on these narrow tasks; 77.2% vs Jev's 72% on a decision
benchmark.

## Security

- Public documentation describes a hosted-only API (`api.scaledown.xyz`, `x-api-key` header
  auth) — no on-prem, VPC, or downloadable-weights option appears in the docs, meaning input
  data (including images/PDFs sent to Extract/Summarize) leaves the caller's infrastructure.
- A June 2026 newsletter quote from CTO Soham Chatterjee describes a deployment that "can run
  entirely within your infrastructure," but this self-hosted tier is not documented publicly
  alongside the hosted API.

## Usage notes

- Pricing: $0.05 per million input tokens per ScaleDown's own post; OpenRouter's listing shows
  $0.04 per million input tokens instead — the two public prices disagree. Output tokens are
  free on both.
- Ecosystem integrations: available on OpenRouter and Vercel; LangChain published
  `langchain-scaledown`, an open-source middleware package, on the same Oct 13, 2026 launch
  day, plus LangSmith gateway support. LangChain's own description: CDMs are trained for one
  task and only return answers that task allows; its integration uses them to summarize
  history, compress tool results, and extract data for agents.
- Independent critique (e.g. ibl.ai) disputes the "new architecture" framing: constrained
  decoding is an established decoding-time technique, not a new model architecture, and the
  Oct 13 launch is a product line of small task-specific models sold hosted or as licensed
  containers. The same critique notes that on ScaleDown's own benchmark page, its paid Extract
  model beats GLiNER2.5 — a free, Apache-2.0 model — by only 0.2 percentage points.
- (source: https://www.instagram.com/reel/Devav4iBMF5/)
