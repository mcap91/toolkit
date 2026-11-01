---
name: laya
title: Laya (Convai Innovations)
url: "https://huggingface.co/convaiinnovations/laya"
category: framework
summary: "Multilingual, non-autoregressive 'System 1' decision model family from Convai Innovations — takes a state (text/email/ticket/JSON) plus typed questions (choice/score/noul) and returns typed answers with calibrated probabilities in one forward pass (~33ms); open-weight (Apache 2.0), self-hostable alternative to TypeSafe AI's closed Jev API, with a Jev-compatible HTTP endpoint; trained via RLCD so honest probability reporting is reward-maximizing"
tags: [classification, inference, llm-alternative, open-weights, multilingual, rlcd, bert, jev-alternative, self-hosted, agent-routing]
reviewed: 2026-09-25
acquired: 2026-09-25
license: Apache-2.0
security_flags: [no-auth-by-default]
overlaps: [jev]
source: unknown
---

## What it does

Laya is a "System 1" decision model: given a state (text, email, ticket, or JSON) and one or more typed questions (choice, score, or noul/boolean), it returns typed answers with calibrated probabilities in a single forward pass — it never generates free text, so there is nothing to parse and nothing to hallucinate. It is explicitly positioned by its author (NandhaKishorM, Convai Innovations) as an open-weight, self-hostable alternative to TypeSafe AI's closed, hosted Jev "System One" API, matching Jev's input/output shape.

Three checkpoints ship under the `convaiinnovations/laya` Hugging Face repo family:
- `convaiinnovations/laya` (repo root): ModernBERT-large backbone, 421M params, 512 context — best for English text, guardrails, email triage.
- `convaiinnovations/laya-multilingual`: mmBERT-base backbone, 322M params, 1024 context (up to 8192 via `max_len`), 100+ languages, ~2.2x faster.
- `convaiinnovations/laya-typed-decisions`: ModernBERT-large, 421M params, 1024 context, fine-tuned for four typed-decisions workflows (invoice processing, security incidents, customer service, agent-trace observability).

The built-in `Router` class detects script/language in under 0.5ms and dispatches to the right checkpoint automatically (or accepts an explicit `lang_guess`/`model=` override). `laya-serve` (optional extra) exposes a `POST /v1/systemone` endpoint with the same request/response shape as TypeSafe Jev, so existing Jev clients can switch by changing the base URL.

Training method: RLCD (Reinforcement Learning for Calibrated Decisions). The policy reports a probability distribution; exploration adds zero-mean Gaussian noise to the logits; the reward is a strictly proper scoring rule (log + spherical, plus ranked probability score for ordinal questions), so expected reward is maximized only by reporting honest probabilities. Updates are REINFORCE with a group-mean baseline (GRPO-style); multi-turn conversations use TD(λ=1.0) over prefix slices.

## Differentiators / benchmarks

Self-reported benchmarks (measured by the Laya authors on a Tesla T4, byte-identical questions across models; Jev figures are third-party-published, not independently measured by Convai Innovations) vs TypeSafe Jev 1.13.0:
- typed-decisions accuracy: 0.766 vs 0.727 (beats a 0.735 teacher-agreement ceiling)
- AG News: 0.950 vs 0.910; DAIR Emotion: 0.595 vs 0.480
- ECE (calibration, lower better): 0.081 vs 0.246 — 3x better after per-(question-type, option-count) temperature fitting
- p50 latency, 1 question: 32.8ms vs 236–276ms (7.8x faster)
- Languages usable at >3x random: 45/51 vs no published Jev benchmark
- Weights: Apache 2.0 open vs closed API; cost: $0 self-hosted vs $0.042/1M tokens

Jev leads on high-cardinality label spaces: on Banking77 (72 vs 77 labels), Jev scores 0.870 vs Laya's 0.425, because Laya's fixed per-question token budget (192–256 tokens by default, shared across all options) leaves only ~3–4 tokens per label once option count is high; the authors document raising `head_max_len`/`max_len` or using a two-step hierarchical choice as workarounds.

The authors publish an explicit "Honest Limits" section rather than only headline numbers: base checkpoints are near/below chance on typed-decisions zero-shot (0.362, vs a 0.461 majority-class baseline) — the 0.766 figure belongs only to the checkpoint fine-tuned on that benchmark's own training split, so Laya is described as "a fast base to specialise, not a zero-shot decision engine." Ordinal "score" questions are the weakest primitive (SST-5 0.372). The "noul" (yes/no) primitive can anchor on its own option-label tokens rather than the input state, occasionally returning a confident "no" for clearly positive input; the authors recommend rephrasing as a two-option `choice` with neutral keys if this is observed. The `action.act_probability` field carries no usable signal yet (near-constant 1.0, AUROC 0.30 against correctness on 396 labelled decisions — confidence gating instead reaches AUROC 0.77). Out of the box the model ships over-confident (mean ECE 0.466 pre-calibration); per-(question-type, option-count) temperature fitting is needed on the deployer's own data.

## Mechanical details

- `pip install laya` (Python 3.10+); optional extras: `laya[serve]` (HTTP server), `laya[mcp]` (MCP server), `laya[langchain]` (LangChain/LangGraph), `laya[onnx]` (ONNX Runtime), `laya[fast]` (TileLang GPU fast path)
- Single-model mode: `laya.load("convaiinnovations/laya", subfolder=...)` downloads only the requested checkpoint's weights
- Architecture: backbone + a decision head trained from scratch (2 transformer layers, an option-marker scorer, an act/escalate head). Every option is scored at its own `[MASK]` token and softmaxed over that question's options, so the answer space is defined at request time with no retraining needed for new schemas. All questions in a call run in one single forward pass.
- Memory management: `Router(preload=True)` keeps all checkpoints resident (32.8ms/request on GPU); lazy default keeps 2 hot (english + multilingual, LRU eviction) — cold switches cost a 7.4–10.3s reload; `max_loaded` is configurable
- A fine-tuning notebook runs the full loop (dataset build, train, calibration-temperature fitting, evaluation, push to Hub) on Kaggle's free 2x T4 GPUs
- Links: GitHub source at `github.com/NandhaKishorM/laya`; PyPI at `pypi.org/project/laya`; live demo Space at `huggingface.co/spaces/convaiinnovations/laya-demo`

## Security

- License: Apache 2.0
- `laya-serve` binds `0.0.0.0` with **no authentication unless `LAYA_API_KEY` is explicitly set**, in which case it requires a `Bearer` token — self-hosted deployments must set this or firewall the port before exposing it
- Model weights only; standard Hugging Face / `transformers` supply chain. One documented gotcha: `transformers` probes for TensorFlow at import time, and if TF is installed its abseil runtime can deadlock `laya.load()` — the documented workaround is running with `USE_TF=0`
- No independent CVE/vulnerability findings surfaced; the project's README documents its own failure modes transparently (see Differentiators above) rather than only publishing favorable numbers, which is a positive signal for evaluating its claims

## Usage notes

- **Naming collision, not a related project**: this catalog's intake queue paired this Hugging Face model with `https://github.com/aayushch/laya`. That repo is an unrelated, separate tool — a Tauri + Svelte + Python "AI notification command center" desktop app (aggregates Slack/Gmail/GitHub/Jira/Notion/Outlook/Calendar notifications via local or cloud LLMs) by a different author, with no connection to Convai Innovations, NandhaKishorM, or this decision model. The two projects merely share the name "Laya." That GitHub repo is intentionally **not** described in this entry and has been returned to the catalog inbox for separate handling rather than folded in here.
