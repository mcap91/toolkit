---
name: spiderbrain-v3
title: Spiderbrain V3
url: "https://github.com/SaroirCommunity/Spiderbrain-V3"
category: framework
summary: BSL license; master/column concept is the key takeaway for kb graph
tags: [dependency-graph, token-reduction, scoring, kb]
reviewed: 2026-05-25
acquired: 2026-05-25
license: BSL-1.1
security_flags: []
overlaps: []
source: unknown
---

## What it does

Generates dependency graphs with importance scoring, file rankings, and per-cluster webmaps, with explicit focus on token cost reduction by pre-computing which files matter most. The core innovation is master/column detection: nodes are scored by mass (fan-in count — how many nodes depend on this one) and rhythm (git commit frequency), then classified as Masters (high mass, low rhythm — stable architectural anchors that govern many but change rarely) or Columns (fast-changing dependents governed by stable masters — the volatile surface area). Amplitude is mass × theta-gain, where theta-gain is derived from "column phase detection." Example node annotation: `"9.9 MASTER src/worker.js cluster=shell fan-in=14 rhythm=42"`. Output includes synganglion.json (all nodes, edges, scores), spideyorder.md (ranked by mass), spideymove.md (ranked by recency), per-cluster webmap.md (K-nearest-neighbors), per-cluster rules.md (curated constraints), and per-cluster changelog.md (rationale).

Measured token reduction on a 154-node Next.js project: 77% tool call reduction (30 → 7), 84% input token savings (42.4K → 6.8K tokens), 70% API cost reduction.

## Assessment

BSL 1.1 license on the core (commercial production requires a paid license; converts to Apache 2.0 after 4 years) rules out adoption. The table below shows where Spiderbrain V3 diverges from kb graph — primarily in its token-optimization purpose and scoring model.

| Feature | Spiderbrain V3 | kb graph |
|---|---|---|
| Purpose | Token cost reduction via importance scoring | Structural relationship extraction |
| Scoring | amplitude = mass x theta-gain | No scoring |
| Node roles | Masters (stable hubs) vs Columns (volatile dependents) | No role classification |
| Clustering | Per-cluster webmaps with rules and changelogs | No clustering |
| Input | JS/TS imports, SQL schemas, git history, tsconfig aliases | Wiki records, code files, imports |
| Token awareness | Explicitly routes agents to important files first | No token optimization |

**The master/column concept** is the primary takeaway. A record with high fan-in and low change frequency is a stable architectural anchor — agents should read it first and trust it to be stable. A record with low fan-in and high change frequency is volatile surface area — agents should check it for recency. This scoring approach could be added to kb graph as a future stability scoring feature without any Spiderbrain code.

**What kb graph could learn**:

1. **Stability scoring** — mass (fan-in) × rhythm (change frequency) to identify load-bearing records vs hot surfaces
2. **Per-cluster views with curated rules** — architectural domain views beyond generated catalog/now/backlog
3. **Node role classification** — which wiki records are "masters" (high dependency, low change) vs "columns" (fast-changing)

## Mechanical details

Do not install. BSL 1.1 license prohibits commercial production use. The master/column detection concept can be implemented independently in kb graph using fan-in counts from the existing graph structure and git log for change frequency — no Spiderbrain code required. Study the README for the scoring formula; the synganglion.json schema is a useful reference for what a scored graph output looks like.

## Security

This repository is deprecated and archived; Spiderbrain V3 (v3.0.0, May 2026) is no longer maintained by the original authors, who have moved the project to a proprietary product at spiderbrain.ai. No new CVEs, dependency patches, or security fixes will be issued against this codebase.

The tool operates entirely on local files (JS/TS imports, git history, tsconfig) and produces static output files — it does not make network calls at runtime, so the supply-chain risk surface is limited to its npm dependencies at install time. Given the BSL 1.1 verdict and the deprecated status of the repo, the correct action is non-adoption; no further security assessment is warranted.
