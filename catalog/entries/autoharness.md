---
name: autoharness
title: Autoharness
url: "https://github.com/kayba-ai/autoharness"
category: framework
summary: needs eval benchmarks first; pilot when we have eval criteria for our skills/agents
tags: [harness, optimization, eval, benchmarks]
reviewed: 2026-05-25
acquired: 2026-05-25
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

A control plane for agent harnesses that proposes and applies changes to prompts, configs, and middleware, then runs evals and keeps only improvements. Works as a resumable search campaign: Workspace → Track → Campaign. Persists settings, proposals, records, iterations, champion state, and plugins in a `.autoharness/` directory. Benchmark results on tau2-airline: +40.7% (best-of-N scoring), +24.1% (hyperparameter tuning), +22.2% (runtime context injection). Includes an assistant integration that generates a `autoharness.claude.md` handoff document via `guide --assistant claude`.

**Key components**:
- 6 benchmark adapters: `generic_command`, `pytest`, `harbor`, `tau2_bench`, `hal`, `car_bench`
- 7 proposal generators: `manual`, `failure_summary`, `local_template`, `local_command`, `openai_responses`, `codex_cli`, `claude_code`
- Plugin system: `.autoharness/plugins/` or `AUTOHARNESS_PLUGIN_PATHS` env var

## Assessment

The `generic_command` adapter works with any scoring command, making it compatible with bioinformatics pipelines. The blocker is defining a scoring function — "did this pipeline produce correct output for this test dataset?" requires a reference dataset and a correctness check before Autoharness can optimize anything. The framework itself is solid; the prerequisite is eval infrastructure, not a tool limitation.

## Mechanical details

Install from GitHub. Requires a benchmark adapter and scoring command before meaningful optimization can begin. For bioinformatics use, the `generic_command` adapter is the entry point — define a shell command that scores pipeline output against a reference, then let Autoharness propose prompt and config changes. Pilot trigger: when eval criteria for skills or agents are defined.

## Security

Licensed MIT (Copyright 2026 kayba-ai). No security flags apply: the tool runs entirely locally against a target harness repo, does not phone home, and has no web-facing surface of its own. The primary risk surface is the proposal generators — `openai_responses` and `codex_cli` send harness content (prompts, configs) to external APIs, so API key handling and data-sensitivity policies apply when those generators are used. The `claude_code` and `local_*` generators remain fully local. The Python plugin system (`AUTOHARNESS_PLUGIN_PATHS`) deserves the same scrutiny as any arbitrary code execution path: review third-party plugins before adding them to a production harness.
