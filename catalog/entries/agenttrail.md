---
name: agenttrail
title: AgentTrail — local observability dashboard for AI coding agents
url: https://github.com/sodiumsun/agenttrail
source_url: https://www.instagram.com/reel/DeRukVeytFt/
source: instagram
category: cli-tool
summary: Local, open-source observability layer for coding agents (Claude Code, Codex, Cursor, and any tool that edits files), shipped as two independent npm-installed views in one repo. "Map" (`npx agenttrail`) combines a PLAN.md convention with observed file changes into a live component map with dependency links and session trails; a completed component re-lights when its files change again, and `npx agenttrail init` can scaffold the plan and wire optional Claude Code hooks. "Kitchen" (`npx agenttrail-kitchen .`, public experimental preview) is a separate Three.js 3D view that turns native agent todos and local Codex/Claude session logs — plus optional Cursor hooks — into a cooking-themed board (chefs, tickets, delivery). Both services bind to 127.0.0.1 only, require no account or cloud calls, and do not launch or control agents, only observe local files and logs. Map does not yet parse Claude Code's newer TaskCreate/TaskUpdate todo format (only legacy TodoWrite); native Cursor live behavior and Windows are unverified per the project's own FAQ. JavaScript, MIT license, single contributor (114 commits), 968 GitHub stars and 70 forks as of this review; created 2026-08-21, last pushed 2026-09-09 (no commits in the ~7 weeks before this review).
tags:
  - observability
  - agent-dashboard
  - claude-code
  - codex
  - cursor
  - plan-md
  - local-first
  - cli
  - npx
  - developer-tools
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT
security_flags:
  - bus-factor-1
  - experimental-preview-kitchen
  - dormant-repo-no-recent-pushes
  - optional-claude-code-hooks-require-trust-review
overlaps: []
---

## What it does

AgentTrail is a local-only observability tool for AI coding agents, built as two separate views over one repo: **Map** and **Kitchen**. Neither runs, assigns, or completes agent work — both only observe local evidence (files, plans, and supported agent events) and render it.

**Map** (`cd your-repo && npx agenttrail`) opens a browser dashboard combining a `PLAN.md` convention (components with stable `{#id}` ids, `files:` globs, `needs:`/`links:` dependency arrows, task checkboxes `[x]`/`[~]`/`[ ]`/`[!]` for done/working/todo/stuck, `by:`/`from:` provenance, a decisions log) with observed file changes. A component marked done re-lights if its files change again. `npx agenttrail init` scaffolds a starter plan, adds the convention to `CLAUDE.md`/`AGENTS.md`, offers optional Claude Code hooks (session/tool activity, legacy `TodoWrite` lists — not the newer `TaskCreate`/`TaskUpdate` format), and adds `.agenttrail/` to `.gitignore`. `npx agenttrail up` relaunches saved boards after reboot; `npx agenttrail autostart` runs it at login.

**Kitchen** (`npx agenttrail-kitchen .`, public experimental preview, pinnable via `npx agenttrail-kitchen@0.1.0-alpha.3`) is a separate package with a bundled Three.js frontend, opening at `localhost:4780`. It discovers Codex and Claude Code activity from local session logs automatically (no plan or hooks required) and renders project responsibilities as "chefs," native todos as "tickets/dishes," observed work as "cooking," and completed todos as "delivery." Cursor connects via optional hooks (reviewed/installed through a "Connect agents" flow); other tools get file-change visibility only, with no native session/todo support. A scripted `--example` mode demonstrates the UI without a live agent.

## Mechanical details

- Install/run Map: `cd your-repo`, `npx agenttrail`.
- Install/run Kitchen: `npx agenttrail-kitchen .` (Node.js 20+, a WebGL-capable browser).
- Build Kitchen from source: `git clone`, `npm ci --prefix packages/kitchen`, `npm run build --prefix packages/kitchen`, `npm start --prefix packages/kitchen -- --project /absolute/path/to/your/repo`.
- Repo stats (GitHub API, 2026-10-28): 968 stars, 70 forks, 7 open issues, created 2026-08-21, last pushed 2026-09-09, JavaScript, MIT, single contributor (sodiumsun, 114 commits).
- Per the project's own FAQ: local observation exercised on macOS; automated package/adapter checks run on Linux; Windows and native Cursor live behavior remain unverified; cloud/remote agent sessions with no logs on the Kitchen host are not discovered; local provider log formats can change and break parsing; no VS Code Marketplace extension exists (VS Code use is a browser companion alongside the integrated terminal).

## Security

Both Map and Kitchen bind to `127.0.0.1` only; the project states no account, telemetry, transcript upload, model call, or cloud service is required for basic operation, and Kitchen sends only an allowlisted set of activity fields to its own browser frontend. Map's optional Claude Code hook view can display shortened command text and tool/search details, and persists recent activity under `~/.agenttrail` — worth reviewing before sharing a recording, per the project's own docs. Optional hook installation (Claude Code, Cursor) edits only reviewed provider settings; the project states opening either view does not otherwise change the watched repo. Third-party assets (fonts, Three.js graphics) ship in the npm package rather than being fetched at runtime.

**security_flags:** single contributor / bus-factor 1 (114 commits, created 2026-08-21); Kitchen is explicitly labeled a "public experimental preview" (alpha versioning); no commits in the roughly seven weeks before this review (last pushed 2026-09-09), suggesting the project may be dormant; optional Claude Code/Cursor hook installation requires the operator's explicit review/trust before it activates automatically.
