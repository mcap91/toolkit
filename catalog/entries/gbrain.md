---
name: gbrain
title: gbrain
url: "https://github.com/garrytan/gbrain"
category: framework
summary: kb wiki already provides persistent typed records with relationships and search
tags: [memory-graph, vector-search, kb, memory]
reviewed: 2026-05-25
acquired: 2026-05-25
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

A persistent memory graph with hybrid search (vector + keyword) and typed links. Designed for long-lived memory across sessions covering entities, experiments, and literature. Combines vector similarity search (semantic) with keyword search to retrieve relevant memory nodes.

## Assessment

kb wiki already provides persistent, typed records with relationships and text-based search. gbrain's typed links overlap with kb graph's structural relationships. The one genuine addition is vector search (semantic similarity), which kb's text-based search index doesn't have — but this isn't a current gap that needs closing. Only worth revisiting if kb hits a wall on search relevance that would benefit from vector embeddings.

## Mechanical details

Do not install. The use case is fully covered by kb wiki + kb graph. If search relevance becomes a concern in the future, vector embeddings could be added to the existing search index rather than adopting a separate memory graph system.

## Security

Licensed MIT. The project ships a `SECURITY.md` documenting its OAuth 2.1 threat model and hardening defaults for the HTTP MCP server (scope-gated access: read / write / admin, DCR-style client registration, rate limiting). The local PGLite path has no network exposure by default; the HTTP server path requires explicit `gbrain serve --http` and bearer-token or OAuth setup. Team/multi-user deployments use per-login brain scoping; the README notes fuzz-testing across all read paths with zero cross-user data leaks observed. No supply-chain concerns beyond standard npm/bun ecosystem; install is from a public GitHub repo with no binary blobs. Since verdict is `skip`, no install or credential exposure applies to this project.
