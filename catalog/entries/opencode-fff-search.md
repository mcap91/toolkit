---
name: opencode-fff-search
title: opencode-fff-search
url: "https://github.com/ozgurulukir/opencode-fff-search"
category: plugin
summary: "Drop-in OpenCode grep/glob replacement with Rust-backed in-memory index, frecency ranking, and SIMD literal matching — 3-10x faster than process-spawning ripgrep at scale."
tags: [opencode, search, grep, glob, rust, performance, fuzzy-search, lmdb, frecency, simd]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: []
overlaps: []
source: unknown
---
## What it does

opencode-fff-search is an OpenCode plugin that overrides the agent's built-in `grep` and `glob` tools with the fff (Fast File Finder) search engine. fff is a Rust library loaded as an N-API native module — no child process is spawned per search call. The plugin provides:

- **Grep tool**: four automatic search paths — direct file read (100% recall), fsGrep for non-ASCII/Turkish patterns (100% recall), fff indexed search with regex/plain mode detection and SIMD-accelerated literal matching, plus an auto-fallback chain back to fsGrep if fff returns zero results.
- **Glob tool**: real glob matching via minimatch for patterns with metacharacters, fff fuzzy search for bare names, and globWalk augmentation when exact basename matches are missing.
- **Frecency ranking**: LMDB-backed aiMode scores files by recent/frequent access, surfacing relevant results first.
- **Bigram inverted content index**: pre-filters 80–95% of files before opening them, yielding 5–20x grep speedups on large repos.
- **Filesystem watcher**: detects new/deleted files mid-session without restart.
- **.gitignore-aware**: respects gitignore at both the fff index level (Rust ignore crate) and the filesystem fallback level.

Benchmarks on the nodejs/node repo (48K files): single grep ~15ms vs ~45ms for a spawned ripgrep; 100 consecutive greps under 1 second vs ~5 minutes.

## Assessment

**watch** — The search optimization patterns here (N-API in-process engine, frecency/LMDB, bigram pre-filter, SIMD matching, graceful fallback chain) are directly applicable to any AI coding agent that performs frequent file search. While this plugin targets OpenCode specifically, the architecture is a reference implementation worth tracking. The 100x throughput advantage on repeated searches is significant for agentic loops. The project is MIT-licensed, has 172 tests, and has a well-documented fallback strategy for the known recall gap. Not cataloged for immediate adoption (requires OpenCode 1.14+), but the patterns are valuable.

## Mechanical details

- **Installation**: Add to `opencode.json` plugins array (`"plugin": ["opencode-fff-search"]`); OpenCode auto-installs from npm on startup. Manual install also documented.
- **Dependencies**: `@ff-labs/fff-node` (N-API), `@ff-labs/fff-bun` (Bun variant), `minimatch`. Platform-specific binaries via npm optional deps (`@ff-labs/fff-bin-*`).
- **Single file**: entire plugin is `index.js` (ES module).
- **Requires**: OpenCode 1.14+, Node.js 18+ (or Bun). Windows supported but WSL recommended.
- **Known limitations**: keyword search not indexed (import/const/return); ASCII-only case folding for uppercase Turkish patterns (ISTANBUL won't find İstanbul); advanced PCRE not supported; workspace-scoped only.
- **Configuration**: all fff features enabled by default (aiMode, mmap cache, content indexing, file watcher) — no config file, hardcoded defaults.

## Security

No elevated privileges or network calls. The native module (`@ff-labs/fff-node`) is a pre-compiled Rust binary distributed via npm — standard supply-chain considerations apply. `security_flags: []` is appropriate; consumers should pin the npm package version as with any native dependency.
