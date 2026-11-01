---
name: subtask4llm
title: subtask4llm
url: https://github.com/evgenyigumnov/subtask4llm
source_url: https://www.reddit.com/r/LocalLLM/comments/1xgqyz4/125_tokens_per_second_on_an_rtx_4070_ti_super_how/
source: reddit
category: skill
summary: Skill pack that splits a coding task into a dependency-ordered plan of up to 10 subtasks, each run by a fresh, isolated one-shot coding-agent worker (Pi Coding Agent or OpenAI Codex CLI) with its own clean context window instead of one agent accumulating the whole task's history; a Python runner (scripts/run_workflow.py) executes workers sequentially, passing each only shared project context plus its declared-dependency results, with bounded per-step timeouts/retries, one shared live log, and --continue-on-error; ships subtask4llm-pi and subtask4llm-codex skills installable independently via the Skills CLI (no Claude Code skill yet — README requests a PR); MIT
tags:
  - skill
  - task-decomposition
  - context-management
  - pi-coding-agent
  - codex
  - local-llm
  - cli-tool
  - orchestration
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags:
  - single-maintainer
  - unsandboxed-worker-execution
overlaps:
  - local-model-harness-patterns
  - blueprint4llm
---

## What it does

subtask4llm splits a large coding task into a dependency-ordered plan of up to 10 subtasks, each executed by a fresh, isolated coding-agent worker process with its own clean context window, rather than one agent working through the whole task in a single accumulating context. A planner (the calling agent) writes a version-1 JSON plan — ordered steps, each with a unique ID, bounded task, nonempty acceptance criteria, and dependencies restricted to earlier steps — and validates it with `--dry-run`. A standalone Python runner (`scripts/run_workflow.py`) then launches one-shot worker processes sequentially in the target workspace; each worker receives only the shared project context, its own assigned task, and the results of its declared dependencies — not the full project or conversation history. Workers run as `--mode json --no-session --no-skills` one-shot processes and must return raw JSON matching a documented result schema.

All worker/orchestrator activity streams to one shared live log per run (default: outside the workspace, in the system temp directory; `--live-log <path>` picks another location), with a printed `tail -f` command for the user to follow progress. The runner checks progress every 10 minutes, kills a shell command with no output for 10 minutes, and enforces a 30-minute hard limit per step; timeouts are never retried. Non-timeout failures get at most one configured retry (`--retries 0|1`). By default the workflow stops after a step remains unsuccessful past its retries; `--continue-on-error` runs the remaining planned steps anyway (final status still reports failure if any step failed).

Ships two independent, agent-specific skills under `skills/<skill-name>/`: `subtask4llm-pi` (drives Pi Coding Agent workers) and `subtask4llm-codex` (drives OpenAI Codex CLI workers); each installs standalone via the Skills CLI. No Claude Code skill exists yet — the README asks for a pull request to add one. No recursive agent spawning and no bundled infrastructure beyond the runner script; workers are plain CLI subprocesses.

## Mechanical details

- Install (Pi): `npx skills add evgenyigumnov/subtask4llm --skill subtask4llm-pi --agent pi`
- Install (Codex): `npx skills add evgenyigumnov/subtask4llm --skill subtask4llm-codex --agent codex`
- Skills CLI places the skill under `.agents/skills/` for the target agent
- Run: `python3 <skill-path>/scripts/run_workflow.py <plan.json> --workspace <repository>` (`py -3` on Windows)
- CLI flags: `--model`, `--timeout-seconds`, `--timeout-checkpoint-seconds`, `--retries 0|1`, `--max-summary-chars`, `--pi-bin`, `--artifacts-dir`, `--continue-on-error`, `--live-log <path>`
- Pi worker model selection order: `--model` flag, then `PI_WORKFLOW_MODEL` env var, then Pi's configured default
- The live log records tool commands and response summaries; the README flags it as potentially sensitive
- Related project from the same author: blueprint4llm (renders plan.md to HTML/PDF with embedded diagrams)

## Security

MIT licensed. Single-maintainer repo (Evgeny Igumnov, also author of blueprint4llm). Worker subprocesses run with the invoking user's filesystem permissions; the README states the CLI "is not a sandbox" and that the skill should only be used when those permissions are appropriate for the target repository. No telemetry or network calls described beyond whatever the underlying Pi/Codex CLI and chosen model provider already perform.
