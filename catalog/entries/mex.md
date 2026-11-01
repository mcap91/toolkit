---
name: mex
title: mex
url: "https://github.com/theDakshJaitly/mex"
category: cli-tool
summary: "Structured markdown scaffold + 11-checker drift-detection CLI for persistent AI agent memory; provider-neutral, ~60% token reduction claims, but single-contributor and overlaps with kb wiki + built-in memory"
tags: [agent-memory, context-management, drift-detection, scaffold, cli]
reviewed: 2026-06-17
acquired: 2026-06-17
license: MIT
security_flags: [telemetry-default-on, single-contributor]
overlaps: [claude-mem, mempalace, gbrain]
source: unknown
---

## What it does

mex creates a structured markdown scaffold for AI coding agent memory — a tiny anchor file (CLAUDE.md / AGENTS.md), a routing table (ROUTER.md), context directories for architecture/decisions/conventions, and reusable task patterns. The CLI (`npx mex-agent`) runs 11 zero-token checkers against the real codebase to detect drift (stale paths, broken links, missing dependencies, config desync) and scores scaffold health out of 100. When drift is found, `mex sync` generates targeted prompts for the agent to fix only stale pieces.

Key features:
- **Provider-neutral**: Claude Code, Cursor, Windsurf, GitHub Copilot, OpenCode, Codex
- **Agent Memory Mode**: `--mode agent-memory` for persistent ops/homelab agents with heartbeat monitoring
- **GROW step**: after meaningful work, updates project state and task patterns automatically
- **Append-only event log**: `mex log` writes decisions to `.mex/events/decisions.jsonl`

## Assessment

The core idea — structured, routed context instead of monolithic instruction files — is sound and well-executed. The 11 drift checkers are the real differentiator: they validate scaffold claims against actual codebase state without spending AI tokens, catching a class of staleness bugs that manual CLAUDE.md maintenance misses.

However, our stack already covers the core memory use case: kb wiki provides persistent typed records with relationships, search, and views; Claude Code's built-in memory system handles cross-session recall; and our handoff skill handles context transfer. mex's scaffold approach is complementary but would add a parallel memory system. The drift-detection concept is the most adoptable piece — a lint pass that validates CLAUDE.md claims against the filesystem could be extracted without adopting the full scaffold.

Community-reported ~60% token reduction in a 10-scenario homelab test is promising but comes from a single independent tester on one project (OpenClaw).

## Mechanical details

- npm package: `mex-agent` (name `mex` was taken)
- Install: `npx mex-agent setup` or `npm install -g mex-agent`
- Windows: npx flow works natively; legacy setup.sh requires WSL/Git Bash
- Config: `.mex/config.json` for staleness thresholds, heartbeat intervals
- Post-commit hook: `mex watch` installs git hook for automated drift checks

## Security

- **License**: MIT — no restrictions
- **Telemetry**: On by default; collects command name, version, OS. Opt-out via `DO_NOT_TRACK=1`, `MEX_TELEMETRY=0`, or `mex config set telemetry off`. No paths, args, or file contents collected per docs
- **Supply chain**: Single contributor (theDakshJaitly). No signed releases visible. Active development (updated within past week)
- **Code quality**: README is thorough; 11 checkers suggest non-trivial test surface. No CI badges visible in README
- **Dangerous patterns**: CLI executes no AI calls itself — it generates prompts for the agent. `mex sync` hands prompts to the user's chosen AI tool, so execution trust boundary stays with the existing harness
- **Dependency count**: Not enumerated in README; npm ecosystem typical