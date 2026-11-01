---
name: harnessx
title: HarnessX
url: "https://github.com/Darwin-Agent/HarnessX"
category: framework
summary: "Python agent-harness foundry from the Darwin Agent Team separating model (ModelConfig) from behavior (HarnessConfig): a 9-dimension processor pipeline (context, control, evaluation, memory, multi-model, observability, tools, plus providers/plugins) composed with a `|` operator, plus two self-reported evolution loops — a meta-harness that auto-searches processor/config combinations, and RL fine-tuning (via VERL) on reward-annotated run trajectories. MIT-licensed, v0.1.0/Beta. Companion papers: HarnessX (arXiv:2606.14249) and a follow-on, DarwinX (arXiv:2608.07545)."
tags: [agent-harness, harness-foundry, composable, processors, self-evolution, reinforcement-learning, python, benchmarks, mit]
reviewed: 2026-08-25
acquired: 2026-08-25
license: MIT
security_flags: [install-script-curl-pipe, self-reported-benchmarks, early-stage-v0.1-beta]
overlaps: [deepseek-harness, harness-engineering]
source: unknown
---
## What it does

HarnessX is a "harness foundry" — a framework for constructing, composing, and evolving agent harnesses independently of the model, from the Darwin Agent Team. Its core separation is `agent = model.agentic(harness)`: a `ModelConfig` (provider routing, fallback, per-role model assignment) is kept distinct from a `HarnessConfig` (the full behavior pipeline — tools, memory, processors, trace, sandbox). The stated goal is to make *behavior* swapping (e.g. from a coding agent to a research agent, adding memory or guardrails) as cheap as model swapping already is in most frameworks, without rewriting the agent.

Behavior is expressed as a 9-dimension processor pipeline: any unit of behavior is a `Processor`, composed across categories with the `|` operator — context (system prompt, history, user wrapper), control (13 safety/reliability processors), evaluation (LLM judge, PRM, self-verify), memory (extraction/retrieval, 5 strategies), multi_model (routing), observability (OpenTelemetry, checkpoints, metrics), and tools (skill loader, schema adapter, filters), on top of 6 model-provider backends and a plugin/dimensions layer.

Two evolution loops are described, both self-reported by the project: **Harness Evolution**, where a meta-harness observes trajectories and auto-searches processor/config combinations (Bayesian Optimization over a claimed ~10^6-configuration space) without changing the model; and **Model Evolution**, where reward-annotated trajectories from harness runs feed RL fine-tuning via VERL (a "slime" recipe: SGLang rollout adapter + token annotation + GRPO). The two are described as composable — evolve the harness, then the model on top of it.

A companion arXiv paper, *HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry* (arXiv:2606.14249), describes the design (typed harness primitives, a substitution algebra, and "AEGIS," a trace-driven multi-agent evolution engine) and reports GAIA/ALFWorld/WebShop/tau³-Bench/SWE-bench-Verified results. A follow-on paper from the same team, *DarwinX: Evolving Agent Harnesses Through Natural Selection* (arXiv:2608.07545), reframes self-evolution as selection over an archived population of harness variants with the model frozen, and was applied to Salesforce's proprietary Monet agent in that paper's evaluation.

## Mechanical details

**Install:** the README's quick-start offers a one-click interactive install script (`curl -sSf https://raw.githubusercontent.com/Darwin-Agent/HarnessX/main/scripts/install.sh | bash`, or with `-s -- --all` for non-interactive) that installs `uv`, Python 3.12, `harnessx`, and optionally a Node.js-based frontend; or a manual path via `uv python install 3.12 && uv venv --python 3.12 .venv && uv pip install -e .` plus `cd frontend && npm install && npm run build`.

**CLI (`hx`):** `hx "<task description>"` for an interactive run, `hx -p "<task>"` for non-interactive print-and-exit, `hx -c path/to/config.yaml` to load a YAML `HarnessConfig`, `hx --resume <run_id>` to resume a session, `hx lab` to open a local Lab UI (FastAPI + SSE backend) at `localhost:8000`. A separate `hx-gateway` service (`~/.harnessx/gateway.yaml`) connects the agent to Feishu, Telegram, Slack, Discord, or DingTalk chat channels through one process, with a bundled React console.

**Python SDK:** minimal example from the README —
```python
from harnessx import BaseTask, HarnessConfig
from harnessx.core.model_config import ModelConfig
from harnessx.providers.anthropic_provider import AnthropicProvider

model = ModelConfig(main=AnthropicProvider("claude-sonnet-4-6"))
harness = model.agentic(HarnessConfig())
result = await harness.run(BaseTask(description="What is 2 + 2?"))
```

**Repo layout:** `harnessx/core` (Harness, Builder, RunLoop, State, Events, Trajectory), `harnessx/processors` (the 7 processor categories), `harnessx/providers` (6 model backends), `harnessx/plugins` (plugin base/discovery/dimensions, including a self-developed file-based "Light-Memory" dimension with time-decay, daily compression, and git versioning), `harnessx/sandbox` (Local, Docker, E2B backends), `harnessx/tracing`, `harnessx/rl`, `harnessx/bundles`, `harnessx/api`, plus top-level `benchmarks/`, `recipe/` (RL training recipes, including `slime`), `examples/`, `extensions/` (docx/pdf/pptx/xlsx skills), `frontend/` (React/TypeScript/Tailwind Lab UI), and `tests/`.

**Status:** README lists this as Phase 1 of a 4-phase roadmap (core pipeline, 13 control processors, multi-provider, SFT/RL bridge, 4 integrated benchmarks, Lab UI). Phases 2–4 (Bayesian-optimization auto search, closed-loop self-evolution training, a "HarnessHUB" community marketplace for publishing/pulling `HarnessConfig` bundles, multimodal memory, and third-party integrations with VERL/SuperMemory/OpenVKing) are listed as planned/roadmap items, not shipped.

## Security

**License:** MIT, stated in the README and confirmed independently via the arXiv:2608.07545 paper text, which also gives the repo's version as 0.1.0 and status as Beta.

**security_flags:**
- `install-script-curl-pipe` — the documented quick-start method pipes a remote install script directly into `bash` (optionally non-interactively with `--all`), which installs `uv`, Python, and an optional Node.js frontend; standard for this class of tool but carries the usual supply-chain risk if the script or its host is compromised. A manual `uv`-based install path is also documented.
- `self-reported-benchmarks` — all GAIA/ALFWorld/WebShop/tau³-Bench/SWE-bench-Verified performance figures in the README and companion papers are reported by the same team that built the tool, with no third-party reproduction found during this review.
- `early-stage-v0.1-beta` — the project is versioned 0.1.0 and labeled Beta; most of the roadmap (auto-search, closed-loop self-evolution, the HarnessHUB marketplace) is unshipped.