---
name: archify
title: Archify
url: "https://github.com/tt-a1i/archify"
category: skill
summary: "Agent skill that turns codebase descriptions or system architectures into polished, interactive HTML/SVG diagrams — five diagram types (architecture, workflow, sequence, data-flow, lifecycle), typed JSON IR, deterministic validation, delta comparison for PR review, share-card export; installs into Claude Code / Codex / Cursor / OpenCode; MIT"
tags: [diagrams, architecture, visualization, skill, svg, html, code-review, delta-comparison]
reviewed: 2026-09-14
acquired: 2026-09-14
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Archify is a Node.js rendering and validation system that agents use to produce interactive architecture diagrams. The agent generates typed JSON IR from a description or codebase; Archify deterministically compiles it into self-contained HTML with SVG visuals, motion, and export capabilities.

Five diagram types:
- **Architecture**: components, services, storage, trust boundaries
- **Workflow**: CI/CD, approvals, tool calls, runbooks (lane-based)
- **Sequence**: API calls, cache fallback, auth, async traces
- **Data Flow**: pipelines, lineage, PII boundaries, consumers
- **Lifecycle**: states, retries, waits, terminal outcomes

Key capabilities:
- **Delta comparison**: compare two validated architecture snapshots as Before / Delta / After with machine receipts of added/removed/changed/moved/rerouted facts
- **Validation pipeline**: schema, layout, HTML/SVG, route, and label-to-route clearance checks must all pass before output replaces the last known good artifact
- **Interactive viewer**: search nodes, trace upstream/downstream reach, probe directed routes, compare semantic roles, play guided stories
- **Export**: PNG, SVG, WebM, 1200×630 share cards; dark/light themes; four visual presets (signal-flow, blueprint, classic, grid)
- **Source evidence mode**: nodes can link to Git-verified files and line ranges pinned to a specific commit
- **Live preview**: loopback-only desktop watcher that refreshes only verified revisions

Installation: `npx skills add tt-a1i/archify -g`. Works with Claude Code, Codex CLI, Cursor, OpenCode, Raven, and DeepSeek Harness.

CLI: `node archify/bin/archify.mjs` with subcommands `doctor`, `demo`, `guide`, `validate`, `preview`, `deliver`, `compare`.

## Mechanical details

- **IR**: Typed JSON per diagram type, with schemas
- **Rendering**: Deterministic HTML/SVG compilation from JSON IR
- **Validation**: Atomic — all checks pass before artifact replacement; failures return stable rule codes, exact subjects, measured evidence, and supported repair controls as JSON
- **Version**: v2.17.0-dev.1
- **Localization**: en, zh-CN (UI only, not authored content)
- **Viewer interactions**: focus (#focus=id), reach (#reach=upstream|downstream), route probing (#route=src~tgt), semantic lens (#lens=kind~kind), story playback
- **Update check**: optional GET to manifest; no telemetry, no version/project/account data sent; disable with ARCHIFY_UPDATE_CHECK_DISABLED=1

## Security

- **License**: MIT
- **No telemetry**: update check is opt-out, sends no identifying data
- **Loopback only**: preview mode binds to 127.0.0.1 on a random port
- **Output isolation**: self-contained HTML files, no runtime dependencies
- **No dangerous patterns**: deterministic rendering from validated JSON IR