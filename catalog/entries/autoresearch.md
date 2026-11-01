---
name: autoresearch
title: Autoresearch
url: "https://github.com/karpathy/autoresearch"
category: framework
summary: "Highly influential autonomous experimentation loop pattern, but ML-training-specific — transferable idea, not transferable code"
tags: [autonomous-agents, ml-training, experimentation, karpathy, agent-loop]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Autoresearch gives an AI coding agent a single-GPU LLM training setup (simplified nanochat) and lets it experiment autonomously. The agent modifies `train.py` (architecture, hyperparameters, optimizer, training loop), runs a fixed 5-minute training cycle, evaluates validation bits-per-byte (`val_bpb`), keeps or discards the change, and repeats. The human programs `program.md` — a Markdown instruction file — rather than touching Python directly. Runs ~12 experiments/hour, ~100 overnight.

The repo is deliberately minimal: three files (`prepare.py` for data prep, `train.py` for the agent to modify, `program.md` for human instructions). Requires a single NVIDIA GPU (tested on H100). Community forks exist for macOS/MPS, AMD, and Windows RTX. 85.9k stars and 12.4k forks as of June 2026 — one of the fastest-growing repos in GitHub history.

Karpathy ran it for two days on his own hand-tuned code and it found 20 stacking improvements including a bug in his attention implementation. The pattern has been adopted beyond ML (e.g. Shopify used it for templating engine optimization).

## Assessment

The autonomous experiment loop (modify → run → evaluate → keep/discard → repeat) is a compelling agent workflow pattern, and the "programming the program" concept (human writes Markdown instructions, agent writes code) maps directly to the skill-based agent paradigm this toolkit uses. However, the implementation is entirely ML-training-specific — GPT models, PyTorch, Muon+AdamW optimizer, BPE tokenizer. None of that transfers to bioinformatics.

Worth documenting as a landmark example of agent-driven autonomous experimentation. The meta-pattern could inspire bioinformatics analogues (e.g. autonomous parameter sweeps for alignment pipelines, variant caller tuning), but that would be a new tool, not this one. Active GitHub discussion (#447) about generalizing beyond ML, but no concrete bioinformatics fork exists yet.

## Mechanical details

- **Experiment loop**: Agent edits `train.py` → `uv run train.py` (5 min wall clock) → check `val_bpb` → keep if improved, discard if not → repeat
- **Human interface**: Edit `program.md` to steer the agent's research direction, constraints, and strategy
- **Agent compatibility**: Designed for Claude Code or Codex with permissions disabled
- **Fixed time budget**: Every experiment runs exactly 5 minutes regardless of model size — results are comparable within a platform but not across platforms
- **Metric**: `val_bpb` (validation bits per byte) — lower is better, vocab-size-independent

The transferable idea is the `program.md` pattern: a Markdown skill file that structures an autonomous agent's experimentation loop with clear objectives, constraints, and evaluation criteria.

## Security

- **License**: MIT — no restrictions
- **Dependencies**: PyTorch + minimal packages managed via `uv`; `pyproject.toml` present
- **Code quality**: Very small, readable codebase (3 core files). No test suite, but the training evaluation loop is the built-in validation mechanism
- **Supply chain**: Single high-profile author (Andrej Karpathy), ~9 contributors. 12.4k forks but contributions flow into forks, not upstream
- **Dangerous patterns**: None in the framework code itself. The design intentionally has an agent modify and execute arbitrary Python — this is the stated purpose, not a vulnerability, but users should run in an isolated environment
- **Maintenance**: Created March 2026, massive community engagement, active discussions