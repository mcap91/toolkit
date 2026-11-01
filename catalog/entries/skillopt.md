---
name: skillopt
title: SkillOpt
url: "https://github.com/microsoft/SkillOpt"
category: meta-skill
summary: "Microsoft research framework that optimizes agent skills via training loops; +23.5 point lifts on Claude Code, Sleep mode for nightly skill consolidation is directly relevant"
tags: [skill-optimization, microsoft, training-loop, claude-code, codex, agent-skills, research, meta-skill]
reviewed: 2026-06-16
acquired: 2026-06-16
license: MIT
security_flags: []
overlaps: [bmad-skill-forge, one-skill-to-rule-them-all]
source: unknown
---

## What it does

A text-space optimizer from Microsoft Research that treats agent skill documents (SKILL.md files) as trainable state and optimizes them using a training loop modeled on deep learning: epochs, mini-batches, learning rates, and validation gates — but without touching model weights. A separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a skill document; edits are accepted only when they strictly improve a held-out validation score. The deployed artifact is a compact `best_skill.md` (300-2,000 tokens) that runs against the unchanged target model.

Training loop: rollout → reflect → aggregate → select → update → evaluate. Features a textual learning-rate budget (constraining edit magnitude), a rejected-edit buffer, and epoch-wise slow/meta updates for stability.

Results: across 6 benchmarks, 7 target models, and 3 execution harnesses (direct chat, Codex CLI, Claude Code CLI), SkillOpt is best or tied-best on all 52 evaluated cells. On GPT-5.5: +23.5 points in direct chat, +24.8 in Codex, +19.1 in Claude Code. Optimized skills transfer across model scales, between harnesses, and to nearby benchmarks.

SkillOpt-Sleep (preview): a nightly offline companion for local coding agents that reviews past sessions, replays recurring tasks, and consolidates validated skills behind a held-out gate.

## Assessment

The approach is novel and the results are strong — turning skill optimization into a principled training problem rather than ad-hoc iteration. The +19.1 point lift on Claude Code CLI is directly relevant to our skills. The SkillOpt-Sleep feature (nightly session review → skill consolidation) is exactly the kind of automated skill improvement loop we'd want for our own skills. Multi-backend support (OpenAI, Azure, Claude, Qwen, MiniMax) means we can use it with our existing model setup. The research paper backing (arXiv:2605.23904) gives confidence in the methodology. Pilot to test whether it can meaningfully improve our existing catalog-intake, debugging, and research skills.

## Mechanical details

- Install: `pip install skillopt` (v0.1.0 on PyPI)
- Training loop: rollout → reflect → aggregate → select → update → evaluate
- Multi-backend: OpenAI, Azure, Claude, Qwen, MiniMax for chat; Codex CLI, Claude Code CLI for agentic execution
- Six built-in benchmarks with dataloaders and seed skills
- WebUI dashboard: `pip install -e ".[webui]"` then `python -m skillopt_webui.app` (Gradio-based, port 7860)
- Extensible: add new backends via `skillopt/model/<name>_backend.py`; new benchmarks via `skillopt/envs/<name>/`
- SkillOpt-Sleep: nightly offline mode — reviews past sessions, replays recurring tasks, consolidates validated skills behind a held-out gate
- Output artifact: `best_skill.md` (300-2,000 tokens), deployable as-is
- Cross-transfer: optimized skills transfer across model scales, between harnesses, and to nearby benchmarks

## Security

- **License**: MIT (Microsoft open-source)
- **Dependency health**: Python package on PyPI; optional Gradio dependency for WebUI; multi-backend means API keys for various providers
- **Code quality signals**: Research-grade code with documentation site (GitHub Pages); reproducibility guide; six benchmarks with dataloaders; demo video
- **Supply chain**: Microsoft Research — major organization; published paper (arXiv:2605.23904); v0.1.0 initial release June 2026
- **Dangerous patterns**: Requires API keys for backend models (standard for LLM tools). The optimizer model makes bounded edits to skill documents — edits are validation-gated, reducing risk of skill degradation. No eval() or shell injection concerns visible
- **Maintenance**: Very active — v0.1.0 released June 2, 2026; Sleep preview June 15, 2026; integrations with gbrain, gbrain-evals, darwin-skill