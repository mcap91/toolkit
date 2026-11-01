---
name: reducto-model-routing
title: Reducto — When Is a Bigger Model Actually Better? (model routing framework)
url: https://reducto.ai/engineering/posts/when-is-a-bigger-model-actually-better/
source_url: https://www.instagram.com/reel/DfAVR6MtdFR/
source: instagram
category: reference
license: n/a
summary: Reducto engineering-blog post (2026-08-13, Apurv Gandhi) framing document-model routing as a constrained optimization problem — a per-request 'model advantage' score (delta), a dimensionless cost-quality tradeoff parameter (lambda) that carries across model upgrades, an oracle frontier for benchmarking, and an AUC-based efficiency metric for grading a learned router against that oracle; reports 43.4%/56.6% split of low-gain vs. meaningful-gain requests across 8,276 paired evaluations.
tags:
  - model-routing
  - ocr
  - cost-optimization
  - regression
  - evaluation
  - reducto
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - isaacflath-ocr-guides
security_flags: []
---

## What it does

Engineering blog post from Reducto (a document-parsing API company), published 2026-08-13 by Apurv Gandhi, framing model routing — deciding per-request whether to pay for a larger, more capable model or use a faster/cheaper one — as a constrained optimization problem rather than a set of hand-tuned rules.

## Framework

- **Model advantage (delta):** for each request, delta_i = score(big model) - score(small model), measuring the accuracy/quality gain from escalating that specific request.
- **Trade-off parameter (lambda):** a single dimensionless cost-quality knob; the routing rule escalates a request when delta_i - lambda * cost_i > 0. Lambda is reported to carry across model version upgrades, so a routing policy's budget can be re-tuned without retraining when a new model ships.
- **Oracle frontier:** computed by labeling every request in an eval set with its true delta and cost, then sweeping lambda from high to low — traces the best-case routing curve achievable on that dataset and serves as the benchmark a learned router is graded against.
- **Router grading:** efficiency = (AUC_router - AUC_random) / (AUC_oracle - AUC_random) — the share of theoretically available routing value a learned router actually captures.
- **Features:** cheap-to-compute inputs derived from the small model's own output — page/region geometry (dimensions, aspect ratio), OCR confidence statistics, text metrics (word/line counts), structural predictions, and content counts. Two separate regressors are trained: one predicts delta-hat (accuracy gain), one predicts cost-hat (added cost/latency).
- **Reported findings:** across 8,276 paired evaluations (the same request scored by both models), 43.4% showed little to no gain from the bigger model (indistinguishable or slightly worse, often from grader verbosity penalties), and 56.6% showed meaningful advantage where routing adds real value.

## Security

Blog post; no code execution or installable artifact.

## Usage notes

- Summarized and demonstrated end-to-end by Isaac Flath across Instagram reels with worked OCR-router examples (LiteParse → Docling → Qwen, Tesseract-vs-heavier-model pairings) built on this framework's two-regressor (accuracy-delta / latency-delta) design. See isaacflath-ocr-guides. (source: https://www.instagram.com/reel/DfAVR6MtdFR/)