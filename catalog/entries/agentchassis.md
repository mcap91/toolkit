---
name: agentchassis
title: "AgentChassis — contract-first orchestration for long-running coding agents"
url: https://github.com/agent-chassis/agent-chassis
category: framework
summary: "Contract-first orchestration that splits agentic coding into non-overlapping orchestrator/worker/reviewer roles under one rule: the agent that defines the work cannot implement it. Every task is a durable work record stating scope, acceptance criteria, and validation before any code is written; a task missing those is rejected before any model runs (deterministic check, no model call). Workers are confined to their declared file scope (Linux bwrap sandbox where available); reviewers check each change against its contract; every run records honest enforcement provenance (enforced true/false plus isolation backend). Parallel agents run on non-overlapping scopes without collision, interrupted tasks resume from their record, and the repo accumulates an engineering record of what was planned, why, and whether it passed. Drives multiple agent CLIs (Codex, Claude, and more) through a typed MCP interface. Source-available under Elastic License 2.0 as public @agent-chassis/* npm packages; an optional hosted Chassis Control Engine (CCE, private beta) adds org-level admission and signed attestation."
tags:
  - multi-agent
  - orchestration
  - code-agent
  - work-records
  - sandbox
  - mcp
  - git-native
  - provenance
  - runtime-governance
  - elv2
reviewed: 2026-08-14
acquired: 2026-07-29
overlaps: []
source: unknown
---
## What it does

AgentChassis installs into your repository and enforces a separation-of-concerns rule: the agent that defines the work cannot implement it. Three non-overlapping roles coordinate through durable work-record contracts — an **orchestrator** plans and breaks the work into small scoped tasks but never writes product code; **workers** each implement one task, confined to the files that task is allowed to change; **reviewers** check each change against what its task said it should do.

Every task is a written work record stating its scope, acceptance criteria, and validation before any code runs. A task missing those fields is rejected before any model runs — a fast, deterministic check, not a judgment call. Because all implementation passes through this loop, the repository accumulates an engineering record — what was planned, why, who did it, and whether it passed — as an ordinary byproduct of getting work done.

Install one public npm package, run setup, build the code index, and point an orchestrator at your repo. Requires Node.js 22+.

## Why it exists

Long-running coding agents drift from declared scope on multi-file work, degrade as context grows, and still resolve fewer than half of long-horizon software-engineering tasks. Better prompts do not close that gap: agent execution is non-deterministic and path-dependent, so runtime behavior cannot be fully governed at design time by prompts or static access controls. AgentChassis applies runtime-governance principles to coding work — a canonical contract per task, execution contained to the declared scope, and a result reviewed against the contract — on the premise that unsupervised execution needs a boundary regardless of model capability.

## Differentiators

**Contract-gated work.** Every task carries scope + acceptance + validation before code runs; malformed tasks are refused early by a deterministic shape check with no model call.

**Scope-confined parallelism.** Because each task declares which files it may touch, multiple agents work concurrently on non-overlapping parts of the codebase without collision. Coordination is by declared scope, not a hand-authored routing graph.

**Grounded review.** A reviewer checks a change against the task's written acceptance criteria instead of inferring intent; review records are tied to the exact change they reviewed.

**Crash-resumable work.** A stalled or failed task carries its full definition in its record, so another agent — or the operator — picks it up later without rebuilding lost context from a chat log.

**Honest enforcement provenance.** Every run records whether it was `enforced` and which `isolation_backend` was used. Free/local mode never claims containment it does not have, and a CCE-key run never silently degrades to unenforced.

**Vendor-neutral, MCP-first.** The same setup drives multiple agent tools (Codex, Claude, and more) through typed tools — an MCP server with built-in discovery. The command line is an operator fallback, not the primary path.

**Code graph for impact analysis.** The local tier builds a graph of your code used for impact analysis and review tooling — distinct from the work-record coordination model, which is not a traversed execution graph.

## Mechanical details

**Packages:** `@agent-chassis/core` is the public install package — it provides the wiki binary (bootstrap, validation, lint, generated views, code index), the `wiki-mcp` stdio MCP server agents call, and the `agent-launch` operator entrypoint. It transitively installs the public, independently versioned `@agent-chassis/controlled-contract`. Published to the public npm registry under the `@agent-chassis` scope; plain `npm install`, no `.npmrc` or auth.

**Setup:** `npm install --save-dev @agent-chassis/core`, then `npx agent-chassis setup` — runs bootstrap, detects or asks the local agent family, copies the launcher template when `agent-launch.toml` is absent, and runs `agent-launch init-config`. Bootstrap seeds the wiki contract surfaces, an owned `IN-0001` adoption initiative and `WK-0001` adoption tracker, cache directories, `.gitignore` entries, `wiki/.wiki-mcp.json`, and the initial lexical search index; it is idempotent. The code index is required for normal operation (readiness, dispatch review, graph-impact, review tooling).

**Operator commands** (human/operator entrypoints — agents do not launch orchestrators; orchestrator sessions are interactive and stay attached, often running on their own for hours):
- `npx agent-launch orchestrator IN-0001 --model opus` (or `--model gpt-5.5`) — start an initiative orchestrator
- `npx agent-launch resume IN-0001 --model opus` — resume an existing orchestrator session
- `npx agent-launch orchestrator list --json` — list orchestrator runtime records

**Wiki surfaces:** local `wiki/` work records, initiatives, decisions, sources, and areas, plus generated views. The consuming repo keeps its product source, repo-specific docs, local wiki records, schema extensions, and MCP client configuration.

**Agent interface:** MCP over stdio — the `wiki-mcp` server, spawned per session, with built-in tool discovery.

## Security

**Enforcement posture (two axes).** "Enforced" means AgentChassis actively contained a run to its declared file scope rather than merely asking the agent to stay inside it.
- *Can it enforce?* Backend availability. When a supported isolation backend (Linux **bwrap** today) is active, worker, reviewer, and redteam runs are contained to their declared write scope and recorded `enforced=true`.
- *Must it enforce?* A configured **Chassis Control Engine (CCE)** key selects the governed posture — it does not add sandboxing capability. With no CCE key and no backend, dispatch may run unenforced, recorded loudly as `enforced=false, isolation_backend=none`. With a CCE key and no backend, dispatch refuses unless the operator sets an explicit unsandboxed opt-out. Local/free use never requires a CCE key.

**Threat model:** structured admissibility and honest provenance — not a guarantee that a hostile or compromised same-user agent is harmless. See `docs/enforcement-model.md` for threat-model limits.

**security_flags:** Local sandbox enforcement is Linux-only (via `bwrap`); macOS filesystem-layer parity is on the roadmap, so non-Linux hosts run unenforced unless a backend is available. Hosted CCE is a paid control plane (private beta, requires form signup). ELv2 is source-available, not OSI open-source.

**license_note:** Elastic License 2.0 — source-available, not OSI-approved open-source. Permits use, modification, and redistribution but prohibits providing the software as a managed service or circumventing license-key functionality. If adopting patterns, design independently; do not copy implementation code.
