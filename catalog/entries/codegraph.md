---
name: codegraph
title: CodeGraph
url: "https://github.com/colbymchenry/codegraph"
category: mcp-server
summary: "Pre-indexed code knowledge graph via MCP — tree-sitter extracts symbols/edges into SQLite, single codegraph_explore tool returns verbatim source + call paths + blast radius in one call; auto-syncs on file changes via native OS watcher; 34 languages, framework route detection (17 frameworks), cross-language bridging (Swift↔ObjC, React Native, Expo); 100% local, MIT"
tags: [code-intelligence, knowledge-graph, mcp, tree-sitter, sqlite, static-analysis, impact-analysis, claude-code, cursor, codex]
reviewed: 2026-07-06
acquired: 2026-07-06
license: MIT
security_flags: []
overlaps: [repomix]
source: unknown
---

## What it does

MCP server that builds a pre-indexed knowledge graph of a codebase's symbols, call edges, and dependencies using tree-sitter parsing into a local SQLite database (`.codegraph/codegraph.db`). Exposes a single `codegraph_explore` MCP tool that returns verbatim source, call paths (including dynamic-dispatch hops), and blast-radius summaries in one call — replacing the agent's typical grep/glob/read crawl loop.

Auto-syncs via native OS file watcher (FSEvents/inotify/ReadDirectoryChangesW) with debounced incremental re-index. Per-file staleness banners warn the agent when a file is pending re-index.

### Language coverage

34 languages: TypeScript, JavaScript, ArkTS, Python, Go, Rust, Java, C#, VB.NET, PHP, Ruby, C, C++, CUDA, Objective-C, Metal, Swift, Kotlin, Scala, Dart, Lua, Luau, R, Nix, Erlang, CFML, COBOL, Solidity, Terraform/OpenTofu, Svelte, Vue, Astro, Liquid, Pascal/Delphi.

### Framework-aware routing

Detects URL routing patterns and links them to handlers across 17 frameworks: Django, Flask, FastAPI, Express, NestJS, Laravel, Drupal, Rails, Spring, Play, Gin/chi/gorilla, Axum/actix/Rocket, ASP.NET, Vapor, React Router/SvelteKit, Vue Router/Nuxt, Astro.

### Cross-language bridging

Bridges cross-language boundaries in mixed iOS/React Native/Expo codebases: Swift↔ObjC `@objc` bridging, React Native legacy bridge (`RCT_EXPORT_METHOD`), TurboModules, native→JS event emitters, Expo Modules DSL, Fabric/Paper view components.

## Differentiators

- **Single-tool MCP surface** — one `codegraph_explore` call replaces multi-step grep/read discovery; benchmarks show 58% fewer tool calls, 22% faster, near-zero file reads across 7 real codebases
- **Always-fresh index** — native OS watcher with debounced auto-sync; no manual re-indexing needed during agent sessions
- **Cross-language flow tracing** — follows call paths across Swift↔ObjC, React Native bridge, and Expo module boundaries that static grep cannot
- **Library API** — embeddable via `import CodeGraph from '@colbymchenry/codegraph'` for programmatic use (requires Node 22.5+)
- **Multi-agent support** — auto-configures Claude Code, Cursor, Codex CLI, opencode, Hermes Agent, Gemini CLI, Antigravity IDE, Kiro via `codegraph install`
- **`codegraph affected`** — traces import dependencies transitively to find which test files are affected by changed source files; usable in CI/pre-commit hooks

## Mechanical details / What to adopt

- Install: `curl -fsSL .../install.sh | sh` (macOS/Linux), `irm .../install.ps1 | iex` (Windows), or `npm i -g @colbymchenry/codegraph`
- Agent setup: `codegraph install` auto-detects and configures agents
- Per-project init: `codegraph init` in project root
- MCP config: `codegraph serve --mcp` (started automatically by agents)
- CLI tools: `codegraph explore`, `codegraph node`, `codegraph callers`, `codegraph callees`, `codegraph impact`, `codegraph affected`
- WSL2 caveat: projects on `/mnt/c` paths have unreliable SQLite locking; use `CODEGRAPH_NO_DAEMON=1` or move to Linux-native filesystem

## Security

MIT licensed. 100% local — no data leaves the machine, no API keys, no external services. SQLite-only storage. Anonymous telemetry (tool/command usage counts, language stats) is opt-in at install; disable with `codegraph telemetry off` or `CODEGRAPH_TELEMETRY=0`. Installer uses `curl | sh` (standard pipe-to-shell risk). Bundles its own Node runtime — no system Node dependency for the CLI.