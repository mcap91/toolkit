---
name: ultimate-deepseek-ultracode
title: Ultimate DeepSeek UltraCode (Reasonix Fleet)
url: "https://github.com/Tatlatat/ultimate-deepseek-ultracode"
category: framework
summary: "Claude Code extension routing Workflow/UltraCode fan-out lanes to DeepSeek v4-flash via a local Reasonix gateway — keeps Claude as main agent, runs subagent work on cheaper DeepSeek inference with ephemeral sessions and server-side cache optimization reaching 99%+ hit rates"
tags: [claude-code, deepseek, workflow, ultracode, fan-out, cost-optimization, mcp, inference-gateway]
reviewed: 2026-07-01
acquired: 2026-07-01
license: unlicensed
security_flags: [no-stated-license, hook-injection, subagent-policy-override]
overlaps: [frontier]
source: unknown
---

## What it does

A launcher + local gateway that routes Claude Code's Workflow/UltraCode fan-out lanes to DeepSeek v4-flash instead of Claude. Claude remains the main agent with all its normal tools, skills, plugins, auth, and model selection. Only the `agent()` lanes in Workflow scripts are redirected through a `reasonix_fleet` MCP server to DeepSeek.

The bundled fork engine (`deepseek-reasonix-engine`) runs each lane as a one-shot in-process Node turn with no persistent session state, preventing history bleed between concurrent lanes. Combined with a prefix prime-gate for server-side cache warming, fan-out cache hit rates reach 99%+ at steady state.

## Differentiators

- **Safe default mode**: Does not change Claude Code's main model or set a process-wide gateway — only fan-out lanes are rerouted
- **Ephemeral sessions**: Each lane runs with `session: undefined`, eliminating on-disk session state and cross-lane history contamination (measured: 60-94% cache without this, 99%+ with)
- **Bundled engine**: Ships a self-contained fork of the DeepSeek engine under `vendor/reasonix-engine/` — no separate install or upstream dependency
- **Hook-based routing**: A `PreToolUse` hook rewrites Workflow `agent()` calls and blocks generic Claude subagents, replacing them with Reasonix Fleet workers
- **Hard-task harness**: Optional retry loop for failing lanes (`CLAUDE_REASONIX_GATEWAY_LANE_HARNESS=1`)
- **~70 configuration levers**: Cache-tuning, prime-gate, prefetch, output-discipline — all default-OFF

## Mechanical details

Install: `git clone` + `./install.sh` (idempotent). Requires Python 3.8+, Node 18+, Claude Code CLI, and a DeepSeek API key. Installs to `~/.claude/reasonix-fleet` with launcher at `~/.local/bin/claude-reasonix`. Default 16 concurrent workers.

Commands: `on/off/status/workers N/task "..."/run/plain/doctor`. Architecture: launcher → gateway (`reasonix_gateway/`) → MCP server (`reasonix-fleet-mcp.py`) → Node shim (`engine/run-lane.mjs`) → bundled engine.

## Security

No stated SPDX license. Injects hooks into Claude Code's PreToolUse pipeline to intercept and reroute agent calls. Blocks generic subagents via hook policy. Bundled engine is a fork committed as prebuilt dist under `vendor/` — supply chain depends on fork provenance. DeepSeek API key stored in `~/.reasonix/config.json` or env var. Single contributor repository.