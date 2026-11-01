---
name: crewai
title: CrewAI
url: "https://github.com/crewAIInc/crewAI"
category: framework
summary: "Lean Python multi-agent orchestration framework — role-based Crews for autonomous collaboration + event-driven Flows for precise control; MIT, 100K+ certified devs, Claude Code skills plugin, independent of LangChain"
tags: [multi-agent, orchestration, python, agent-framework, llm]
reviewed: 2026-06-19
acquired: 2026-06-19
license: MIT
security_flags: [telemetry-default-on]
overlaps: [architect-loop, weft]
source: unknown
---

## What it does

CrewAI is a standalone Python framework for orchestrating autonomous AI agents. Two core paradigms:

- **Crews**: Teams of role-based agents with autonomous decision-making, dynamic task delegation, and collaborative problem-solving. Defined via YAML config (agents.yaml, tasks.yaml) with a Python crew class.
- **Flows**: Event-driven workflows with `@start`, `@listen`, `@router` decorators, typed Pydantic state management, and conditional branching. Production-focused with precise execution control.

The two compose: Flows orchestrate Crews as steps, combining autonomy with deterministic control flow. Supports sequential and hierarchical processes, parallel task execution, memory, delegation, and human-in-the-loop.

Built from scratch — no LangChain dependency. Connects to any LLM (OpenAI default, Ollama for local). CLI scaffolding (`crewai create crew <name>`). Ships official Claude Code skills plugin (`/plugin marketplace add crewAIInc/skills`) with 4 auto-activating skills. Also has an enterprise AMP suite (control plane, tracing, observability).

## Assessment

The most mature open-source multi-agent framework alongside LangGraph. The Crews + Flows architecture is well-designed — Crews handle the "let agents figure it out" cases while Flows handle the "I need deterministic orchestration" cases. Claims 5.76x faster than LangGraph on benchmarks.

For our stack, CrewAI is relevant as an alternative orchestration layer for complex multi-agent bioinformatics pipelines that outgrow kb dispatch + Claude Code workflows. The Claude Code skills integration is a plus. However, we already have Claude Code's native Agent tool, workflows, and kb dispatch for orchestration — CrewAI would be additive complexity unless we need cross-model agent teams or the Flows state management.

The telemetry collects agent roles, tool names, and model info by default (disable via `OTEL_SDK_DISABLED=true`). `share_crew=True` opt-in goes further with task descriptions and outputs.

## Mechanical details

- **Install**: `uv pip install crewai` (or `crewai[tools]` for agent tools)
- **Scaffold**: `crewai create crew <name>` generates project structure with YAML configs
- **Run**: `crewai run` or `python src/<project>/main.py`
- **Claude Code**: `/plugin marketplace add crewAIInc/skills` for 4 auto-activating skills
- **Local models**: Ollama, LM Studio integration
- **Python**: >=3.10 <3.14
- **Courses**: learn.crewai.com (100K+ certified developers)

## Security

- **License**: MIT — no restrictions
- **Telemetry**: On by default. Collects CrewAI/Python version, OS, agent count, process type, roles, tool names, LLM used. Disable with `OTEL_SDK_DISABLED=true`. Opt-in `share_crew=True` shares task descriptions, goals, backstories, and outputs.
- **Supply chain**: Active development, pre-commit hooks, mypy, pytest. Large contributor base.
- **Dependencies**: Standalone (no LangChain). Optional `crewai[tools]` adds extra deps including tiktoken (requires Rust compiler on some platforms).
- **API keys**: Requires LLM API key (OpenAI default) stored in `.env` file.
