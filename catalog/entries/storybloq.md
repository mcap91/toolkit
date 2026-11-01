---
name: storybloq
title: Storybloq
url: "https://github.com/Storybloq/storybloq"
category: framework
summary: PolyForm Noncommercial license + heavy overlap with kb wiki
tags: [project-state, wiki, tickets, kb]
reviewed: 2026-05-25
acquired: 2026-05-25
license: PolyForm Noncommercial 1.0.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

A file-based project state system stored in a `.story/` directory with JSON records for tickets, issues, notes, lessons, handovers, snapshots, and roadmap. Ships as an npm package with a CLI, 53-tool MCP server, and Claude Code `/story` skill. Solves AI coding statelessness by persisting project state across sessions. Includes an autonomous ticket execution mode (`/story auto T-001`) that chains PICK → PLAN → REVIEW → WRITE_TESTS → IMPLEMENT → TEST → REVIEW → FINALIZE. Supports multi-repo federation with an orchestrator + node model and cross-node blocking. Two standout lifecycle features: a PreCompact hook that auto-snapshots state before Claude compacts context, and a Lessons lifecycle with reinforce (priority boosting on reuse) and digest (compact injection into skills) operations.

## Assessment

PolyForm Noncommercial 1.0.0 license is a hard blocker for any commercial adoption path. Beyond the license, Storybloq and kb wiki solve the same problem — persistent project state across AI sessions — with heavy overlap in record types and relationships. The table below shows the overlap and divergence.

| Feature | Storybloq | kb wiki |
|---|---|---|
| Record format | JSON files (T-001.json) | Markdown with YAML frontmatter (WK-0001.md) |
| Record types | tickets, issues, notes, lessons, handovers, roadmap | issues (typed), areas, initiatives, decisions, sources |
| Relationships | `blockedBy`, `parentTicket`, `crossNodeBlockedBy` | `depends_on`, `blocks`, `related` (bidirectional schema) |
| Views | Status derived from tickets; `recommend` command | Generated views (catalog, now, inbox, backlog, archive) |
| Search | Via 53 MCP tools | Search index + MCP search tool |
| Cross-session | Handovers + snapshots + `recap` | HO records via dispatch; wiki persists in git |
| Hooks | PreCompact (auto-snapshot), SessionStart | No compaction hooks; dispatch is process-based |
| Multi-repo | Federation with orchestrator + nodes | Single repo per wiki instance |
| Lessons lifecycle | create/update/reinforce/digest | Decisions exist but lack reinforce/digest |
| Autonomous mode | `/story auto T-001` — chained workflow per ticket | No autonomous mode |

**What Storybloq does that kb doesn't**: PreCompact hook, Lessons reinforce/digest, autonomous ticket execution, multi-repo federation, 53 MCP tools (kb has ~15).

**What kb does that Storybloq doesn't**: Graph extraction, dispatch lifecycle, schema enforcement, generated views from frontmatter.

**Two concepts worth promoting to kb**:

1. **PreCompact hook** — kb should hook into Claude's context compaction to snapshot or summarize state before context is discarded. Storybloq auto-snapshots to `.story/snapshots/` on this event.
2. **Lessons lifecycle** — `reinforce` bumps a lesson's priority each time it's invoked; `digest` compacts high-priority lessons for injection into skills. kb decisions exist but have no equivalent priority or digest mechanism.

## Mechanical details

Do not install. PolyForm Noncommercial license prohibits commercial use, and kb wiki covers the same ground. The two concepts worth studying (PreCompact hook and Lessons lifecycle) can be extracted from the README without running the tool. If kb ever implements a compaction hook, Storybloq's `.story/snapshots/` approach is a concrete reference for what state to capture.

## Security

Storybloq is an npm global package that registers an MCP server and installs hooks into Claude Code's settings. The `storybloq setup --client all` command mutates `~/.claude/settings.json` to add PreCompact and SessionStart hooks, meaning a compromised or malicious package version could inject arbitrary shell commands that run inside every Claude Code session. The MCP server itself exposes 53 tools with write access to `.story/` records; tools that mutate state (create/update/delete tickets, issues, lessons, handovers) run without additional confirmation prompts once the server is registered. The PolyForm Noncommercial license means no security audit obligation or commercial support path exists; vulnerabilities would rely on community disclosure alone. For reference/study use only — do not install in any environment where the MCP server would be active.
