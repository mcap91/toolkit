---
name: opus-fable-mode
title: opus-fable-mode
url: "https://gitlab.com/timo2026/opus-fable-mode"
category: hook
summary: "Data-driven behavioral governor + re-injection hook to steer Opus 4.8 toward Fable 5's terse, result-first working style; honest about limits (style not capability) and backed by 37K-message corpus analysis"
tags: [behavioral-tuning, claude-code, hook, token-reduction, fable-5]
reviewed: 2026-06-17
acquired: 2026-06-17
license: MIT
security_flags: [single-contributor, settings-json-modification]
overlaps: [karpathys-12-rules-for-claudemd, rtk]
source: unknown
---

## What it does

A small toolkit to recover the behavioral qualities of the now-suspended Claude Fable 5 model when using Opus 4.8 in Claude Code. Based on analysis of 9,224 Fable and 27,685 Opus messages across 68 projects, it identified measurable behavioral differences:

- Fable's median reply is 2.6x shorter (18 vs 47 words)
- Fable's tool:text ratio is 3.91 vs Opus's 1.41 (Opus narrates ~3x more per unit of work)
- Fable opens with results ("Done", "task"); Opus opens with self-narration ("I'll", "Let me")

Three components form a setpoint/thermostat/measurement loop:
1. **governor-block.md** — 8-rule behavioral directive appended to `~/.claude/CLAUDE.md`
2. **reinject.sh** — `UserPromptSubmit` hook that re-prints the governor every turn to defeat context decay
3. **leak_test.py** — measures whether Opus is converging toward Fable's behavioral signature using your own JSONL logs

## Assessment

The methodology is unusually rigorous for this category — corpus-based behavioral analysis with clearly stated definitions, caveats, and honest framing about what prompts can and cannot change. The three-layer architecture (setpoint → thermostat → measurement) is a clean pattern: the governor states intent, the hook defeats decay, and the leak test closes the feedback loop.

The core insight — that Fable's *style* (terse, result-first, high tool:text ratio) is separable from its *capability ceiling* — is useful even without adopting the full toolkit. The specific behavioral metrics (tool:text ratio, opener words) could inform our own CLAUDE.md tuning.

However: the hook modifies `~/.claude/settings.json` (global scope), the re-injection adds tokens every turn, and it's a single-contributor GitLab project with no visible CI or tests. The Fable suspension context also means this tool addresses a specific moment in time — if/when Fable returns or Opus's behavior changes, the governor rules may need recalibration.

## Mechanical details

- Install: append `governor-block.md` to `~/.claude/CLAUDE.md`, copy `reinject.sh` to `~/.claude/fable-mode/`, merge hook snippet into `settings.json`
- Toggle off: `export FABLE_MODE_OFF=1`
- Measurement: `python3 leak_test.py` reads `~/.claude/projects/` JSONL files locally (no API, no telemetry)
- Reads `message.model` field to bucket messages by model
- Shell hook (bash) — Windows users need WSL/Git Bash

## Security

- **License**: MIT — no restrictions
- **Supply chain**: Single contributor on GitLab. No CI, no tests visible. Very new project tied to Fable 5 suspension (June 12, 2026)
- **Hook behavior**: `reinject.sh` is a `UserPromptSubmit` hook — it runs on every prompt submission. The hook re-prints a text block; it does not execute arbitrary code or phone home. However, installing any hook into `~/.claude/settings.json` is a trust decision with global scope
- **Data access**: `leak_test.py` reads local JSONL session files under `~/.claude/projects/`. This is read-only analysis of your own data, no network calls
- **Dangerous patterns**: No eval, no shell injection vectors visible in the described components. The hook is a simple echo/cat script