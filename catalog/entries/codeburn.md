---
name: codeburn
title: CodeBurn
url: "https://github.com/getagentseal/codeburn"
category: cli-tool
summary: "Cross-tool AI spend observability dashboard — reads local session files from 31+ tools (Claude Code, Codex, Cursor, Gemini CLI, etc.), breaks down tokens and cost by task/model/project, waste detection with copy-paste fixes, model comparison, git-correlated yield tracking; MIT, fully local"
tags: [cost-tracking, token-analytics, observability, tui, claude-code]
reviewed: 2026-06-22
acquired: 2026-06-22
license: MIT
security_flags: []
overlaps: [headroom-desktop, rtk]
source: unknown
---

## What it does

Interactive TUI/web dashboard that reads session files already written to disk by AI coding tools and computes per-call token usage and cost. Supports 31 providers including Claude Code, Codex, Cursor, Gemini CLI, Kiro, Warp, Forge, Pi/OMP, Codebuff, Cline/Roo Code, Kimi, and more. Pricing pulled from LiteLLM (cached 24h) with hardcoded fallbacks for Claude and GPT-5 models.

Key commands:
- `npx codeburn` — interactive dashboard (last 7 days)
- `codeburn optimize` — scan for waste patterns (re-read files, low read:edit ratio, bloated CLAUDE.md, unused MCP servers, ghost skills) with estimated savings and copy-paste fixes, graded A–F
- `codeburn compare` — side-by-side model comparison (one-shot rate, retry rate, cost per edit, cache hit)
- `codeburn yield` — correlates sessions with git commits to classify spend as productive/reverted/abandoned
- `codeburn web` — local browser dashboard with charts
- `codeburn overview` — plain-text monthly summary for pasting into Slack/PRs
- Menu bar app (macOS) with real-time spend display

Task classification is deterministic (13 categories from tool usage patterns and keywords, no LLM calls). One-shot rate tracks file-aware retry cycles. Multi-device aggregation via PIN-authorized LAN pairing. 162 currencies supported.

## Assessment

Strong observability tool for anyone running multiple AI coding assistants. The `optimize` command is particularly valuable — it identifies concrete waste patterns (unused MCP servers, ghost skills, bloated context) and provides ready-to-paste fixes. The `yield` command answering "did the spend actually ship?" is a unique angle.

Overlaps with Headroom Desktop on cost tracking for Claude Code specifically, but CodeBurn is broader (31 tools) and read-only (no proxy/MITM). Complements rtk (which reduces cost) with visibility into where cost goes.

Node.js 22.13+ requirement is a minor friction point. The tool reads sensitive session data (conversation history, tool calls) but everything stays local.

## Mechanical details

- Install: `npm install -g codeburn` or `npx codeburn`
- Also: `brew install codeburn` (macOS)
- Data: reads `~/.claude/projects/` JSONL files for Claude Code, `~/.codex/sessions/` for Codex, SQLite for Cursor/OpenCode/Warp/Forge
- Config: `~/.config/codeburn/config.json` (currency, model aliases, plans)
- Cache: `~/.cache/codeburn/` (LiteLLM prices, Cursor results)
- JSON output: `--format json` on most commands for programmatic use
- Env vars: `CLAUDE_CONFIG_DIR`, `CLAUDE_CONFIG_DIRS`, `CODEX_HOME` for custom paths

## Security

- **License**: MIT — no restrictions
- **Local-only**: no network calls except LiteLLM price fetch and optional Frankfurter exchange rates; no API keys, no proxy, no wrapper
- **Data access**: reads session files from `~/.claude/`, `~/.codex/`, Cursor SQLite, etc. — sensitive conversation data but never transmitted
- **Supply chain**: AgentSeal organization, active development, high star velocity
- **Dependencies**: Node.js ecosystem; `better-sqlite3` auto-installed for Cursor/OpenCode support
- **Menu bar**: macOS Swift app downloaded from GitHub releases via `codeburn menubar`
- **Multi-device**: PIN-authorized LAN pairing — usage data shared between paired devices on local network