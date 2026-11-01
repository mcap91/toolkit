---
name: titans-atlas-cronus
title: Titans (Atlas + Cronus)
url: "https://github.com/titans-tools"
category: framework
summary: "Local-first, agent-first infrastructure pair from a solo AI-assisted builder — Atlas is persistent project memory (knowledge packages, typed graph, evidence/provenance, SQL, blobs, audit history; retrieval blends lexical + vector + graph + evidence, scoped per project/tenant), Cronus is durable execution (DAG workflows, scheduling, checkpoints, at-least-once retries with lease fencing, dead-letter, approval gates); shared MCP server over stdio plus REST/gRPC; free binaries, proprietary source, signed releases (SHA-256 + Ed25519); Windows/Linux"
tags: [agent-infrastructure, persistent-memory, durable-execution, mcp-server, scheduling, provenance, local-first, workflow-engine, proprietary]
reviewed: 2026-09-10
acquired: 2026-09-10
license: LicenseRef-proprietary
security_flags: [closed-source, single-maintainer, curl-pipe-sh-installer]
overlaps: [claude-mem, memstack, mempalace]
source: unknown
---

## What it says

A builder's writeup of Titans, a local-first infrastructure project extracting the plumbing every agent system rebuilds — persistent memory, retrieval, provenance, background execution, retries, scheduling, workflow state, coordination — into reusable services agents consume. Development was heavily AI-assisted (Claude Code for repo-level implementation, Codex for independent passes, ChatGPT for architecture review). The first two systems:

**Atlas — persistent memory.** Stores knowledge packages, project/work state, typed graph relationships, evidence and provenance, structured SQL data, blobs, and audit history. Deliberately does not treat vector search as "memory": retrieval combines lexical/full-text, vector, graph relationships, and evidence to answer "what do we know, where did it come from, how is it connected." State is scoped per project/tenant, not per agent, so multiple agents share one source of truth.

**Cronus — durable execution.** Owns work independent of agent-session lifetime: background jobs, DAG workflows, scheduling, checkpoints, retries with backoff, leases, stale-claim fencing, dead-letter handling, approval gates, and recovery after worker death. Explicitly at-least-once with idempotent claim/completion — exactly-once external side effects require the destination connector to honor an idempotency key.

The boundary rule: "Atlas remembers. Cronus runs." Each is independently adoptable. Interfaces: one shared MCP server over stdio for all installed systems (discoverable by Claude Code, Codex, etc.), plus local REST and gRPC — "agent-first, not agent-only."

## Key takeaways

The post's engineering lessons from AI-assisted development of a large system:

1. Generating code is easy; maintaining architectural boundaries is hard — AI will couple systems you wanted separated unless boundaries are explicit.
2. Give agents invariants, not features ("a worker may die at any point; stale claims must not remain authoritative") — constraint lists produce better implementations than feature requests.
3. Use more than one reasoning pass — a second model challenging the first finds hidden assumptions.
4. Don't let the AI accidentally decide product architecture — it optimizes the next change, not six-month tradeoffs.
5. Building for agents changes API design: predictable contracts, stable identifiers, explicit errors, namespaced operations, canonical references.

## Mechanical details

- Repos: github.com/titans-tools/Atlas, github.com/titans-tools/Cronus (documentation + signed release binaries; product source is proprietary).
- Runs locally on Windows and Linux, binds locally, no telemetry, no hosted account.
- Distribution: signed catalogs and binaries — SHA-256 integrity, Ed25519 signatures; one-line installers with manual verification as the alternative.

## Security

- `closed-source` — the public repos contain docs and binaries only; the implementation cannot be audited. "Free to use" currently, with no stated license terms for the binaries beyond that.
- `single-maintainer` — solo project; supply chain rests on one person's signing keys.
- `curl-pipe-sh-installer` — one-line install scripts are the primary path (manual artifact verification offered).
- The source content is a self-promotional post; capability claims (fencing, recovery semantics) are the author's own and untested here. A reply in the thread is itself an LLM-disclosed promotional comment for a different product (Perseus Vault).