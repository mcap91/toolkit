---
name: gvs5h-ledger-orchestration
title: GVS5H — Ledger-Based Zero-Shot Self-Orchestration
url: "https://github.com/slee-persis/GVS5H"
category: agent-pattern
summary: "Training-free multi-agent coding method where fresh instances of one model decompose problems and coordinate through a shared filesystem (plan, notes, current solution); Qwen3.8-27B rises from 69.2% to 92.4% pass@1 on LiveCodeBench Hard (exceeding Fable 5's 90.4%); GPT-5.6-Terra reaches 88.0% at 19% of Fable 5's cost; gains attributed to decomposition and persistent context; MIT/CC-BY-4.0"
tags: [multi-agent, self-orchestration, coding-benchmark, livecode-bench, zero-shot, qwen, cost-optimization]
reviewed: 2026-09-14
acquired: 2026-09-14
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

GVS5H introduces ledger-based zero-shot self-orchestration — a training-free method where fresh instances of a single model decompose coding problems and coordinate through a shared filesystem holding a plan, notes, and current solution.

Results on the 100 latest hard LiveCodeBench problems:
- **Qwen3.8-27B** (locally served, open-weight): 69.2% → 92.4% pass@1, slightly exceeding Fable 5's 90.4%
- **GPT-5.6-Terra**: 88.0% pass@1 at 19% of Fable 5's cost
- Gains up to 23.2 percentage points on pinned backends
- Gains are not universal — some models are unchanged or worse

Transcript analysis attributes the gain to decomposition and persistent context. The method requires no fine-tuning or special training — it's purely an inference-time organization technique.

Usage: `--engine multiagent` runs the manager orchestration; `--engine single` is the one-call baseline. Supports OpenAI, Anthropic, DashScope, and OpenRouter backends.

## Mechanical details

- **Coordination**: shared filesystem (plan + notes + current solution)
- **Agents**: fresh instances of the same model, zero-shot
- **Benchmark**: LiveCodeBench (release_v6), 100 latest hard problems
- **Models tested**: 9 open and closed-weight models
- **Runtime**: Python 3.12, uv, datasets, numpy
- **Parallelism**: configurable (--parallel N)

## Security

- **License**: MIT (code), CC BY 4.0 (paper/figures/data)
- **No dangerous patterns**: benchmark runner with filesystem coordination