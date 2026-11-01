---
name: gemini-3-8-flash
title: Gemini 3.8 Flash
url: "https://deepmind.google/models/model-cards/gemini-3-8-flash/"
category: framework
summary: "Google DeepMind's Gemini 3 family Flash-tier model (built on Gemini 3.7 Flash), published 2026-09-02 — 1M-token multimodal input context (text/image/audio/video), 64K text output, customizable inference effort levels, $0.75/$3.75 per 1M input/output tokens; targets cost-effective software engineering and agentic knowledge-work at production scale"
tags: [google-deepmind, gemini, llm, multimodal, agentic, model-card, long-context, api-model]
reviewed: 2026-09-25
acquired: 2026-09-25
license: proprietary
security_flags: []
overlaps: []
source: unknown
---

## What it does

Gemini 3.8 Flash is Google DeepMind's next Flash-tier release in the Gemini 3 model family, built directly on Gemini 3.7 Flash (architecture, training dataset/processing, and hardware/software stack are inherited unchanged — the model card defers to the 3.7 Flash card for those details). It accepts text, images, audio, and video with up to a 1M-token context window, and produces text output up to 64K tokens. It supports customizable "effort levels" to trade off quality, cost, and latency at inference time. Published 2 September 2026, alongside a separate cybersecurity-specialized sibling, Gemini 3.8 Flash Cyber (frontier-level vulnerability detection and automated patching).

## Differentiators / Key takeaways

- **Pricing unchanged from 3.7 Flash**: $0.75/1M input tokens ($1.50 at the higher "regular" tier), $3.75/1M output tokens ($7.50 regular) — positioned as a low-cost, high-throughput tier rather than a frontier flagship.
- **Benchmark gains over 3.7 Flash**, per the model card's own comparison table (vs. Claude Opus 5, Claude Sonnet 5, GPT-5.6 Sol, GPT-5.6 Terra):
  - DeepSWE v1.1 (long-horizon software engineering): 73.7% (3.7 Flash: 65.3%; best competitor Claude Opus 5: 74.0%)
  - Terminal-bench 2.1 (agentic terminal coding): 89.4% (3.7 Flash: 85.8%)
  - HLE-Verified (multidisciplinary expert reasoning): 54.9% (3.7 Flash: 53.6%)
  - BioMysteryBench (bioinformatics research workflows), Human Solvable: 88.8%; Human Difficult: 56.5% (3.7 Flash: 87.1% / 43.5%)
  - LABBench2 (biology real-world research tasks): 86.2% (3.7 Flash: 82.1%)
  - Notably behind Claude Opus 5 on Terminal-bench 4.0 (19.1% vs. 51.8%) and OSWorld-2.0 agentic computer use (59.0% vs. 75.4%).
- **Knowledge cutoff**: March 2026 for general training, though the card notes some domains may reflect only a January 2025 cutoff, consistent with the rest of the Gemini 3 family.
- **Safety posture vs. 3.7 Flash**: broadly similar text-to-text and image-to-text safety and tone; multilingual safety regressed by 5.4 percentage points; unjustified refusals improved by 1.1pp. Passed required child-safety launch thresholds. Frontier Safety Framework (April 2026) assessment found no new Tracked/Critical Capability Levels reached, based on carried-over 3.7 Flash results (DeepMind states 3.8 Flash was not independently re-assessed because no meaningful capability increase was found relative to 3.7 Flash).
- **Availability**: Google AI Studio, Gemini API, Android Studio, Google Antigravity (reported as the default model there), and Gemini Enterprise.

## Mechanical details / What to adopt

- Inputs: text, images, audio, video; context window up to 1,000,000 tokens.
- Outputs: text only, up to 64,000 tokens.
- Effort-level control lets callers tune the quality/cost/latency tradeoff per request.
- Model card explicitly defers architecture, training data, training data processing, hardware, and software details to the Gemini 3.7 Flash model card — no new information is disclosed for 3.8 Flash on those axes.
- Released roughly three weeks after Gemini 3.7 Flash, during a Google DeepMind leadership transition reported in outside coverage (Demis Hassabis moving to chairman, Koray Kavukcuoglu taking over as SVP) — not stated on the model card itself but relevant context from third-party reporting (The Register).

## Security

- **License**: Proprietary — hosted API model accessed via Google AI Studio / Gemini API / Vertex-adjacent surfaces (Gemini Enterprise, Android Studio, Antigravity); no open weights or local deployment option described.
- **Known limitations (per model card)**: general foundation-model hallucination risk; ongoing jailbreak-resistance hardening work; occasional slowness/timeout issues; higher token consumption at higher effort levels.
- **Safety evaluation caveat**: automated safety evaluations were revised between model versions, so the model card states results are not directly comparable to prior Gemini model cards' published numbers.
- Benchmark and safety figures are self-reported by Google DeepMind on the official model card; no independent third-party reproduction was consulted for this entry beyond general release coverage.
