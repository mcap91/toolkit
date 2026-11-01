---
name: ponytail
title: Ponytail
url: "https://github.com/DietrichGebert/ponytail"
category: plugin
summary: "YAGNI enforcement plugin with strong benchmarks (80-94% less code, 47-77% cheaper); multi-platform support and clean design make it worth trialing"
tags: [claude-code, codex, plugin, yagni, minimalism, code-quality, over-engineering]
reviewed: 2026-06-16
acquired: 2026-06-16
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

A plugin that makes AI coding agents write minimal code by enforcing a strict YAGNI (You Aren't Gonna Need It) ladder before generating any code. The agent stops at the first rung that holds: (1) does this need to exist? skip it; (2) stdlib does it? use it; (3) native platform feature? use it; (4) installed dependency? use it; (5) one line? one line; (6) only then, the minimum that works. Every shortcut is marked with a `ponytail:` comment naming its upgrade path, so deferred complexity is tracked, not lost.

Benchmarks across five everyday tasks (email validator, debounce, CSV sum, countdown timer, rate limiter) on Haiku/Sonnet/Opus show 80-94% less code, 3-6x faster, and 47-77% cheaper than a no-skill agent.

## Assessment

The philosophy is sound and the benchmarks are reproducible (`npx promptfoo eval`). The plugin explicitly carves out trust-boundary validation, data-loss handling, security, and accessibility as never-skip items, so it's not reckless minimalism. Three intensity levels (lite/full/ultra) plus off give fine control. The review commands (`/ponytail-review` for diff, `/ponytail-audit` for repo) and debt harvesting (`/ponytail-debt`) are useful standalone. Multi-platform support (Claude Code, Codex, Copilot CLI, Gemini/Antigravity, Pi, OpenCode, OpenClaw, Cursor, Windsurf, Cline, Kiro) is impressively broad. Worth piloting to see how it interacts with our existing skills and workflows.

## Mechanical details

- Claude Code install: `/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail`
- Three intensity modes: `lite` (gentle nudges), `full` (default, strict ladder), `ultra` ("when the codebase has wronged you personally")
- Default mode configurable via `PONYTAIL_DEFAULT_MODE` env var or `~/.config/ponytail/config.json`
- Two Node.js lifecycle hooks for always-on activation (requires `node` on PATH)
- Commands: `/ponytail [level]`, `/ponytail-review` (diff review), `/ponytail-audit` (repo audit), `/ponytail-debt` (harvest deferred shortcuts), `/ponytail-help`
- Instruction-only adapters for agents without plugin support (Cursor, Windsurf, Cline, Copilot, Kiro)
- Benchmarks reproducible via promptfoo: `npx promptfoo eval -c benchmarks/promptfooconfig.yaml`
- Rule alignment enforced by `node scripts/check-rule-copies.js` and `npm test`

## Security

- **License**: MIT
- **Dependency health**: Minimal — two small Node.js lifecycle hooks; benchmarks need Python 3 with pandas for CSV checks
- **Code quality signals**: Tests exist (`npm test`); rule-copy alignment checking; reproducible benchmarks via promptfoo; correctness benchmarks for generated code
- **Supply chain**: Single contributor; plugin marketplace distribution; MIT licensed
- **Dangerous patterns**: None observed — the plugin injects a ruleset (text) into the agent context, not executable code. The lifecycle hooks are small and inspectable. Explicitly preserves security-critical code paths (trust boundaries, data-loss handling, accessibility)
- **Maintenance**: Active development; broad platform support indicates ongoing maintenance across multiple agent ecosystems