---
name: jev-kit
title: Jev-kit
url: "https://github.com/jonathanavis96/jev-kit"
category: plugin
summary: "Multi-component Claude Code integration kit wiring TypeSafe's Jev (a ~0.3s typed-decision model) into the agent loop: a PreToolUse tool-call guard ('Airlock', code rules first + one Jev question for the ambiguous ~7%), sub-agent tier right-sizing, a 'Belay' check that sends unverified 'done' claims back to the agent, plocate/Everything-based file search, a Jev-driven browser agent (vendored fork of browser-use's jev-ultrafast), plus installer/doctor/warm-daemon tooling; MIT, requires a TypeSafe API key, Linux/WSL2-first with a reduced-feature native Windows port"
tags: [claude-code, hook, pretooluse, guardrails, agent-routing, sub-agent, typesafe-ai, model-routing, file-search, browser-automation, installer]
reviewed: 2026-09-25
acquired: 2026-09-25
license: MIT
security_flags: []
overlaps: [jev, browser-use, agent-browser, playwright-cli]
source: unknown
---

## What it does

jev-kit bundles everything the author wired up to run TypeSafe's Jev (a non-generative "System One" model that returns typed yes/no/choice/score decisions with a probability in ~0.3s, rather than free text) inside Claude Code. It frames itself around one idea: the judge (Jev) is easy to call; the value is in the wiring around it — which tool call to question, which sub-agent rung a task needs, what to redact before sending, and how to fail open when no answer arrives.

Components:
- **Airlock** (tool-call guard, formerly `jev-guard`/`plumbline`): a `PreToolUse` hook registered for every tool call. Code-first rules (R1–R10 deny triggers, R11 cost steers) filter ~93% of calls in ~33ms median with no network call; the remaining ambiguous fraction gets one typed Jev question. Not a sandbox — it is "a policy hook inside your own session that judges individual tool calls and at most returns a deny to Claude Code," with no containment.
- **Tier guard**: asks Jev what kind of job a sub-agent dispatch is and flags mismatches (e.g., dispatching Opus for a grep-sized task). Reported 98.2% accuracy with zero false denies.
- **Belay**: a check that sends an agent's turn back when it reports "done" without verifying its own work.
- **File search**: swaps `find` for a per-user `plocate` index on Linux (steers to `es.exe`/Everything on Windows).
- **Browse**: a Jev-backed browser-automation tool where Jev makes the click/navigation decisions and Sonnet (low-effort) plans, positioned as an alternative to Playwright MCP for simple navigation. Reports 233x lower cost per run than a Sonnet-driven browse agent for the same task (9/9 success on both). The vendored agent is browser-use's `jev-ultrafast`, pulled in via git subtree with modifications tracked in a `NOTICE` file.
- **Review**: a Jev-powered code reviewer with a fail-open wrapper.
- **Compaction**: an optional plugin that reduces raw tool input tokens (community feature, opt-in).
- **Warm daemon**: keeps a persistent connection to cut judgment latency from ~0.9s (cold) to ~0.3s.
- **Installer/doctor/auto-updater**: install, verify, and roll back the kit; checks guard status at startup; updates Claude Code when no run is active; five-minute health checks with optional push monitoring; a tuning loop that scores shadow-log verdicts and commits results to a dedicated branch.

Every component except the guard is optional and separately installable by flag.

## Mechanical details

**Install:** `git clone https://github.com/jonathanavis96/jev-kit.git ~/code/jev-kit && cd ~/code/jev-kit && install/install.sh` (bash, Linux/WSL2). `--check-only` previews changes without installing; `--wire` writes the hook directly into Claude Code's settings (omit it to just print the JSON diff). Default install mode is **shadow** (logs what would be blocked, does not enforce).

**Platform support:** Linux with systemd — fully supported. WSL2 with systemd enabled — fully supported. WSL2 with systemd off — works degraded (no daemon, timers, or index refresh). macOS — "plausible but untested," requires `--no-systemd`. Windows native — separate `install/windows_install.py` path with `.cmd`/`.ps1` launchers; only the core guard is ported (no daemon, belay, compaction, browser, or review).

**Config/state locations:** `~/.local/share/airlock/` (guard binaries/config), `~/.config/airlock/` (rules, mode, state), `~/.config/jev-kit/env` (holds `TYPESAFE_API_KEY=...`, read by all components). Never runs `sudo`; never writes outside `$HOME`.

**Modes:** `shadow` (log-only), `enforce` (blocks per rules), `off` (disabled). Switch via `echo enforce > ~/.config/airlock/mode`. Kill switches: `AIRLOCK_DISABLE=1` env var, `~/.config/airlock/disabled` file, or `echo off > ~/.config/airlock/mode`.

**Safety model:** fail-open on error/timeout/missing key/unreachable daemon (call always proceeds). Hard time budget caps a judgment at 1500ms enforce-mode (2000ms on Windows); past that the call proceeds anyway. `[airlock-ok: <reason>]` in a tool description bypasses any deny (logged). Same call isn't denied twice within 10 minutes, except cost-control rule R11 (browse-via-Jev), which keeps refusing repeats — only the `browse` tool itself failing opens the door. Denies require 0.8+ confidence with a 0.4+ margin; rewrites require 0.9/0.5. Custom rules can override the built-in table via `~/.config/airlock/rules.json`.

**Measured numbers (self-reported in the repo):** guard hook latency (no match) 33.2ms median; warm-daemon judgment latency ~0.3s (Windows, no daemon: 1030ms median); browse-tool cost $0.0008 (Jev) vs $0.1868 (Sonnet) per run, both 9/9 success; rule-based deny accuracy 100% with zero false denies; tier-guard accuracy 98.2% with zero false denies.

## Security

MIT licensed. The vendored browser agent (`jev-ultrafast`, forked from browser-use at commit `1231850` via git subtree) carries its own attribution in a `NOTICE` file.

Requires a TypeSafe API key (`TYPESAFE_API_KEY`), stored in `~/.config/jev-kit/env`; the README instructs never to print/paste/echo it back for confirmation. All components share the same key; everything degrades gracefully without it (code-only rules still fire, no Jev calls are made).

**Data sent off-machine:** only redacted summaries of the ambiguous fraction of tool calls that reach Jev (command line or dispatch description, secrets stripped via `airlock/redact.py`) — never raw tool results or file contents, and never code, since only the ambiguous fraction is evaluated at all. Two opt-in exceptions widen this: the compaction plugin sends raw tool inputs/outputs, and the review component sends diffs.

**System modifications:** installs a `PreToolUse` hook into Claude Code's tool pipeline (only when `--wire` is passed; otherwise the JSON diff is shown without being applied). This is the highest-privilege integration point in Claude Code — every tool call passes through it before execution. Default shadow mode means a fresh install does not block anything until the operator explicitly switches to enforce mode.

The project (and the wider "Jev integration" wave it belongs to — jev-use, claude-jev, jev-review, fast-jev-compaction) is recent; most of these repos were created in the days around September 17-20, 2026, so review the guard's rules table and the `--wire` diff directly rather than assuming default behavior, and treat maturity/provenance claims as unverified pending independent review.
