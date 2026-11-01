---
name: repowise
title: repowise
url: "https://github.com/repowise-dev/repowise"
category: framework
summary: "Local-first codebase-intelligence engine: index a repo once and keep it current per-commit, then serve it to coding agents via ~11 task-shaped MCP tools plus a CLI, local dashboard, VS Code extension, and a zero-LLM PR bot. Builds a five-layer index (dependency graph across 19 languages, git behavioral signals, generated wiki, mined architectural decisions, deterministic 1–10 code-health scores with concrete refactoring plans), plus change-risk scoring, dead-code detection, and reversible command-output 'distill'. Structural index needs no API key and runs offline; AGPL-3.0 with a commercial license option."
tags: [codebase-intelligence, mcp, code-health, dependency-graph, agent-context, git-analytics, documentation, self-hosted, agpl]
reviewed: 2026-08-17
acquired: 2026-08-17
license: AGPL-3.0
security_flags: [agpl-3.0-copyleft]
overlaps: [graphify]
source: unknown
---
## What it does

repowise precomputes the answers a coding agent normally rediscovers on every task (who calls this function, what breaks if I change it, why it's written this way, which files are risky) and keeps them current on each commit, so the agent reads an answer instead of re-exploring the codebase. The same index also gives a team a defect-validated health score, change-risk scoring on PRs, and a local dashboard. It runs on your machine; the first (structural) index needs no API key and the code never leaves the box. It reports large token savings in its own benchmarks (e.g. loading one commit's context at 393 vs 13,984 raw tokens; −31.6% agent output tokens on a 43-question loop) — vendor-measured against an open-source agent-context field, with losing rows published.

## Mechanical details

- **Five layers (single pass, zero LLM):** Graph (file+symbol nodes, 3-tier call resolution, Leiden communities, PageRank, route→handler edges across 22 frameworks), Git (hotspots, ownership %, co-change pairs, bus factor, bug-fix recency), Docs (generated per-module/file wiki, incremental, hybrid search), Decisions (architectural decisions mined from ~8 sources with verbatim evidence spans), Code health (49 deterministic detectors, 26 scoring; defect/maintainability/performance signals; refactoring plans with blast radius; <30s on a 3,000-file repo).
- **~11 MCP tools:** `get_overview`, `get_answer`, `get_context`, `get_symbol`, `search_codebase`, `get_risk`, `get_change_risk`, `get_why`, `get_dead_code`, `get_health` — each response carries an `_meta` envelope with index age, indexed commit, and a stale warning.
- **CLI:** `repowise init` (`--no-prose -y` = free, no key), `generate`, `serve`, `update`, `watch`, `search`, `ask`, `context`, `symbol`, `why`, `health`, `risk`, `impacted-tests`, `dead-code`, `distill <cmd>` (reversible, errors-first command-output compression), `saved`, `workspace`, `doctor`, `uninstall`.
- **Surfaces:** local dashboard (`repowise serve`, localhost:3000), VS Code / Open VSX extension, free GitHub PR bot (deterministic, zero LLM calls), multi-repo Workspaces (cross-repo contracts/co-change/federated MCP), worktree support, auto-sync hooks. 19 languages parsed to AST (13 full-tier). Optional model-written prose (Anthropic/OpenAI/Gemini) only on request, behind a cost estimate; Ollama for offline embeddings.

## Security

- **License:** AGPL-3.0 (network copyleft — free for internal individual/team/company use; embedding in a product without AGPL obligations requires a commercial license). Enterprise adds SSO/SCIM/RBAC, security/compliance layer, IP indemnification.
- **Privacy (self-hosted):** code never leaves your infrastructure; stored artifacts are the graph, non-reversible embeddings, generated wiki, and git metadata (raw source processed transiently, not persisted). CLI sends anonymous opt-out usage telemetry (command names + coarse environment) — disable via `repowise telemetry disable`, `DO_NOT_TRACK=1`, or running offline. Bring-your-own-key LLM calls are not seen by repowise.
- Deterministic layers make no LLM calls and can't be prompt-injected; the model-written prose step is optional and off the indexing path.
