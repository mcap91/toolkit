---
name: trigger-tree
title: trigger-tree
url: "https://github.com/Hedde/trigger_tree"
category: cli-tool
summary: "Documentation-discovery telemetry for Claude Code / Codex. Measures whether CLAUDE.md directives change agent behavior via deterministic local probes — per-directive adherence rates, file/folder heat maps, A-F docs-health grade, CI discoverability gate. All local, stdlib-only Python, zero tokens for measurement. Claude Code plugin (/tt) and standalone CLI (pipx install trigger-tree). MIT."
license: MIT
tags: [claude-code, codex, telemetry, documentation, measurement, ci, hooks, claude-md, observability]
reviewed: 2026-07-28
acquired: 2026-07-28
overlaps: []
security_flags: []
source: unknown
---

## What it is

trigger-tree is a local, deterministic tool that measures whether project instructions (CLAUDE.md / AGENTS.md) actually change what coding agents do. It answers: "when a directive applied, did its declared probe observe the behavior it requested?" — a narrower, measurable question than "was the file read."

Two capabilities at different time horizons:
- **CI discoverability gate** (immediate): Structural check on router coverage, orphaned docs, folder entry points, watch scope. Fails a PR with the affected file and suggested fix. No telemetry required.
- **Instruction adherence** (after ~5 applicable opportunities): Per-directive adherence rates with confidence levels. A committed manifest maps each rule to a probe; deterministic local code does every count. "Unobserved" means evidence was not captured, not "violated."

Additional features: file/folder heat/cold maps, A-F documentation-health grade, search evidence, prompt-level browsing (with configurable privacy: truncate/hash/off), timeline annotations, evidence-backed routing suggestions, SARIF and GitLab Code Quality exports.

## Mechanical details

- **Install:** Claude Code plugin (`/plugin marketplace add Hedde/trigger_tree`), Codex plugin, or standalone (`pipx install trigger-tree` / `uvx --from trigger-tree tt`)
- **Key commands:** `/tt setup`, `/tt doctor`, `/tt watch`, `/tt insights`, `/tt instructions`, `/tt gate`, `/tt suggestions`, `/tt badge`
- **How it works:** Shell-side hooks log to gitignored `.trigger-tree/history.jsonl`; failures never interrupt the coding session. A deterministic aggregator computes every metric with Python stdlib; the model interprets but never counts.
- **Privacy:** Before setup, only short hashes are stored. Per-project prompt logging choices: truncate (200-char previews), hash, or off. User-wide default via `~/.trigger-tree/config.sh`.
- **Complements:** Token/trace observability tools (Langfuse, Arize, W&B) and documentation linters — trigger-tree measures discoverability and directive adherence, not answer quality.

## Security

MIT licensed. All measurement is local, stdlib-only Python — no cloud, analytics, network calls, or model tokens while measuring. Prompt logging is opt-in per project with configurable privacy levels. No security flags observed.

## How to use it

/plugin marketplace add Hedde/trigger_tree
