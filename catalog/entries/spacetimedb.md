---
name: spacetimedb
title: SpacetimeDB
url: "https://github.com/clockworklabs/spacetimedb"
category: framework
summary: "Relational database that is also the application server (Clockwork Labs, Rust) — schema + business logic compile into a WASM module running inside the database, clients connect directly and subscribe to tables with automatic real-time state sync; ACID with in-memory state plus commit log; modules in Rust/C#/TypeScript/C++, client SDKs for web/Unity/Unreal; powers the BitCraft Online MMORPG backend; BUSL-1.1 (→AGPL-3.0 with linking exception), ~25k stars"
tags: [database, realtime, relational, rust, wasm, game-development, multiplayer, subscriptions, serverless-architecture, unity, unreal]
reviewed: 2026-09-10
acquired: 2026-09-10
license: BUSL-1.1
security_flags: [busl-license-restrictions]
overlaps: []
source: unknown
---

## What it does

SpacetimeDB (Clockwork Labs) collapses the database and application server into one system: you upload application logic directly into the database and clients connect to it with no server in between. A module — written in Rust, C#, TypeScript, or C++ — defines **tables** (data) and **reducers** (logic/API endpoints); SpacetimeDB compiles it, runs it inside the database, and pushes state changes to subscribed clients automatically (no polling or refetching). Permission/authorization logic lives in the module.

It provides full ACID guarantees with all application state in memory for speed and a disk commit log for durability and crash recovery. The stated proof point: the entire backend of the MMORPG BitCraft Online — chat, items, terrain, player positions — runs as one SpacetimeDB module synchronized to thousands of players in real time.

## Differentiators

- One language, one binary, zero infrastructure: no separate web server, containers, Kubernetes, or caching layer.
- Reducers-as-API: `#[spacetimedb::reducer]` functions replace REST/RPC endpoints; clients call them via SDK and `useTable(...)`-style hooks deliver live table state.
- Four server languages and client SDKs spanning TypeScript (React/Next/Vue/Svelte/Angular/Node/Bun/Deno), Rust, C# (standalone + Unity), and C++ (Unreal Engine) — game engines are first-class targets.
- `spacetime dev --template chat-react-ts` scaffolds, publishes to their Maincloud hosting, and hot-republishes on save.

## Mechanical details

- Install: `curl -sSf https://install.spacetimedb.com | sh` (macOS/Linux) or `iwr https://windows.spacetimedb.com -useb | iex`; `spacetime login` (GitHub OAuth); self-host via `docker run clockworklabs/spacetime start` (port 3000) or build from source (Rust + wasm32-unknown-unknown, `spacetimedb-standalone`/`-cli`/`-update` crates).
- Docs at spacetimedb.com/docs: concepts (tables, reducers, subscriptions, auth), tutorials (chat, Unity, Unreal), Maincloud deployment, CLI and SQL references.
- Rust, ~25.1k stars, ~1.1k forks, 882 open issues; created 2023-06, pushed same day as review; commit signoff required.

## Security

- **License:** `busl-license-restrictions` — Business Source License 1.1, converting to AGPL-3.0 **with a linking exception** after 4 years (MariaDB-style). The linking exception means user application code need not be open-sourced; only changes to SpacetimeDB itself. Production-competitive use is restricted during the BUSL window — read the grant before commercial deployment.
- Install path is curl-pipe-sh / iwr-pipe-iex; signed releases not indicated in the README.
- Self-hosting is supported (Docker/source); the default quickstart path publishes to the vendor's Maincloud (paid tiers apply).
- VC-backed company (Clockwork Labs) with a shipping commercial game on the platform; active org with discussions enabled.