---
name: tencentdb-agent-memory
title: TencentDB Agent Memory
url: "https://github.com/TencentCloud/TencentDB-Agent-Memory"
category: framework
summary: "Tencent-built team-level memory hub for AI agents providing four asset types — layered Chat Memory (L0-L3), versioned Skills, linked Wiki pages, and a CodeGraph — managed through a human-reviewable Memory Hub panel with ACL-based sharing"
tags: [agent-memory, memory-hub, knowledge-graph, wiki, skills, codegraph, acl, tencent, docker]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: []
overlaps: [codegraph, mex, claude-mem]
source: unknown
---

## What it does

TencentDB Agent Memory is a self-hosted "team memory hub" for AI coding/ops agents, built by Tencent Cloud. It defines four reusable memory asset types:

- **Chat Memory** — layered distillation of conversations: L0 (raw conversation), L1 (extracted atoms: facts/preferences/constraints), L2 (scenario-organized knowledge blocks), L3 (long-term persona/profile). Retrieval combines BM25 + vector search + RRF, capped by item count/character budget/timeout.
- **Skills** — versioned, executable experience extracted from conversations and tool calls, with resource files, trigger boundaries, execution steps, and validation rules; private by default, shareable to a team after review.
- **Wiki** — product docs, design specs, and runbooks converted into structured, link-graphed pages (the README credits Andrej Karpathy's "LLM Wiki" concept as the direct inspiration for this layer).
- **CodeGraph** — indexes code symbols, files, call relationships, and impact paths so agents can inspect callers/callees and blast radius before modifying code (built on code from the separate open-source CodeGraph project).

A "Memory Hub" web panel (localhost:8125 by default) lets a human create teams and per-role agents, bind specific memory assets to specific agents ("loadouts"), and manage ownership/version/status/visibility per asset. Visibility levels are `private` (owner only), `team`, `restricted` (User/Role/Agent ACL), and `agent` (bound to one agent). New Chat Memory and Skills are private by default — sharing is an explicit action. A "cold-start" import path lets a new team ingest existing codebases (auto-indexed into CodeGraph), documents (auto-converted to Wiki), and past agent conversation sessions (auto-extracted into Skills/Chat Memory).

## Differentiators

- Treats memory as governed, ownable, versioned "assets" rather than a flat conversation/vector-search log — the README contrasts this against both plain chat history and standard RAG on axes of ownership, versioning, and team-sharing controls.
- CodeGraph and Wiki extend memory beyond conversational recall into codebase and documentation structure, discoverable via `/v3/tools/list` and `/v3/tools/call` rather than injected wholesale into context.
- States integration with OpenClaw, Hermes, Claude Code, CodeBuddy, and an SDK; broader cross-framework migration is described as "on the roadmap."
- README reports a PersonaMem benchmark improvement from 48% to 76% (+59% relative) with the system enabled, measuring whether an agent correctly retains and applies user information across extended interactions — this is the project's own reported figure.

## Mechanical details

- Deployment: `git clone` + `deploy/global-images/start-all.sh`, which launches three services (memory-core, memory-hub, proxy) together via Docker; requires two sets of LLM API parameters (memory group + proxy group) in a `.env` file.
- Panel UI at `http://localhost:8125` after startup.
- A separate migration tool is provided for moving data from v1.x/v0.x releases to v2.0.0+.
- The README's clone command (`git clone https://github.com/Tencent/TencentDB-Agent-Memory.git`) references the `Tencent` GitHub org, while the catalogued repository itself is hosted under the `TencentCloud` org — both resolve to the same project per third-party coverage, but the org naming is inconsistent within the README.
- Acknowledged dependencies: uses code from the separate `CodeGraph` project for its CodeGraph module, and part of the Skill-asset management code from Hermes Agent (Nous Research).
- CodeGraph currently prioritizes public HTTPS repos; private-repo/SSH support and fully automated memory routing are both noted as still in progress.

## Security

MIT licensed. Self-hosted, multi-service architecture (memory-core + memory-hub + proxy, each a separate process/container) that requires LLM API keys for two separate parameter groups stored in a `.env` file. No independent security audit or SECURITY.md is referenced in the fetched README. The project grew very rapidly after a July 2026 GitHub Trending placement (multiple third-party trackers report star counts ranging from roughly 4.5k to 15k+ within weeks, captured at different points during that growth), which is a maintenance/scrutiny signal worth noting for a still-young project handling team conversation data, code, and documents. No eval-style or credential-handling issues are visible in the documented feature set itself; the ACL/visibility model (private/team/restricted/agent) is described as the intended boundary for cross-agent and cross-user data exposure, but the fetched material does not include an independent verification of that boundary's implementation.