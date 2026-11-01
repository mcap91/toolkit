---
name: jantt
title: Jantt
url: https://github.com/AhmadHassan-BTed/Jantt
source_url: https://www.instagram.com/reel/DeqoyYOAl7w/
category: framework
summary: TypeScript Gantt chart engine that renders interactive, draggable timelines from a declarative JSON schema — zero runtime dependencies, under 14KB gzipped core; ships as @jantt/core, @jantt/react, @jantt/standalone (UMD/IIFE script tag), and a jantt CLI with bidirectional file-watch sync; includes a topological DAG solver, Critical Path Method analysis, PERT estimation, Earned Value Management (ANSI/EIA-748), and DCMA-14 schedule audits; optional real-time multi-user collaboration backed by Firebase Realtime Database + Cloudflare Workers, gated behind GitHub OAuth and a "follow and star the maintainer's repos" unlock; MIT license, single maintainer (AhmadHassan-BTed), ~155 commits, 339 passing tests
tags:
  - gantt-chart
  - project-management
  - typescript
  - json-schema
  - critical-path
  - dag
  - react
  - cli
  - zero-dependencies
  - ai-native
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: MIT
security_flags:
  - new-project
  - single-maintainer
  - cloud-dependency
source: instagram
---

## What it does

Jantt turns a declarative JSON document into an interactive, draggable Gantt chart: task bars, 90-degree orthogonal dependency wiring, baseline ghost bars, inline progress-drag handles, and a 5-tier zoom (day to year). The same JSON backs a Kanban board (drag-and-drop status columns), a todo checklist view, shared markdown notes with `@person`/`/task` mentions, and a PM dashboard (progress velocity, Critical Path, Earned Value Management, DCMA-14 audit flags). The core engine (`@jantt/core`) is pure TypeScript with no runtime dependencies, under 14KB gzipped; it validates the JSON against a published schema, resolves task scheduling topologically, computes the critical path and float, and lays out the 90-degree dependency routing. Distribution targets: a React component (`@jantt/react`), a script-tag UMD/IIFE bundle (`@jantt/standalone`) for plain HTML with no build step, and a Node.js CLI (`jantt`) that opens a JSON file in-browser with live two-way file-watch sync (`npx jantt open <file.json>`, `npx jantt validate <file.json>`).

The README pitches the JSON schema as an "AI-native" interface: instead of prompting an LLM to generate React/JSX or SVG coordinate math for a timeline (claimed to be brittle and hallucination-prone), the agent emits JSON conforming to Jantt's schema contract, which the README claims costs roughly 10x fewer tokens than equivalent JSX and is schema-validated before render. The repo ships copy-paste system prompts for this workflow.

## Mechanical details

- Packages: `@jantt/core` (validator, topological resolver, layout/routing engine, exporters — zero runtime deps), `@jantt/react` (`<Jantt />` component), `@jantt/standalone` (UMD/IIFE bundle), `jantt` CLI (file-watch two-way sync).
- Headless use: `@jantt/core` exports `validate`, `resolveSchedule`, `calculateCriticalPath`, `exportToCsv` for backend/server use without rendering.
- Exporters: CSV (RFC-4180), SVG, raw JSON; optional remote-URL sync with ETag caching and polling.
- Schema: formal JSON Schema at `schema/jantt.schema.json` (v1.4.0), referenced from `tasks[]` (id, dates, `dependsOn` as a DAG, `milestone`, `progress`, `baseline`), `categories{}`, `people[]`, `teams[]`, `notes[]`.
- Optional real-time collaboration: Firebase Realtime Database + Cloudflare Workers backend, 3-way CRDT reconciliation on room writes. Auth is GitHub OAuth only (`read:user`, `user:follow`, `public_repo` scopes) — no email/password or Google login. Free collaboration rooms are unlocked by following the maintainer's GitHub account and starring their repos; the maintainer's own account is auto-verified. The plan sanitizer (`sanitizePlanForJson`) strips internal database IDs/UIDs before any JSON export, keeping only `@username` mentions.
- Test suite: 339 tests across 22 suites (`npm test`), TypeScript typecheck (`npm run typecheck`).
- Single contributor (AhmadHassan-BTed), ~155 commits on main at review; star count varies by source consulted (observed between ~2.5k and ~5.4k) and should be treated as unverified.

## Security

MIT license. The core engine and CLI are local/offline with no network calls. The optional collaboration feature introduces a third-party cloud dependency (Firebase Realtime Database, Cloudflare Workers) and GitHub OAuth token handling; review `database.rules.json` before relying on it for sensitive project data. The collaboration unlock mechanism (follow + star the maintainer to get a free room) is a growth-hacking gate tied to the maintainer's own social metrics rather than a standard paid/free tier — worth noting given the project's own GitHub star count is inconsistently reported across sources. Single maintainer, no CVE or incident history found; too new for a security track record.
