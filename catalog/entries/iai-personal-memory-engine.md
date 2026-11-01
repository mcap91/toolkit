---
name: iai-personal-memory-engine
title: iai — Personal Memory Engine
url: "https://github.com/CodeAbra/iai-personal-memory-engine"
category: framework
summary: "Fully local MCP-based personal memory engine for AI assistants — ambient capture, three-tier memory (episodic/semantic/procedural), custom storage engine (Hippo), clustering (MOSAIC), HD substrate (LilliHD), Rust embedder; macOS-only, English-only, MIT"
tags: [memory, mcp-server, claude-code, local-first, rust, embeddings]
reviewed: 2026-06-19
acquired: 2026-06-19
license: MIT
security_flags: [macos-only, hooks-modify-settings]
overlaps: [mempalace, claude-mem]
source: unknown
---

## What it does

A local MCP server giving Claude Code (and other MCP hosts) long-term personal memory. Three design principles: fully local, ambient (no "remember this"), and verbatim-first.

**Three memory tiers:**
- **Episodic**: Verbatim, timestamped transcript fragments. Write-once, never rewritten.
- **Semantic**: Summaries induced from clusters of related episodes during idle consolidation.
- **Procedural**: 11 stable parameters about the user (preferences, style, patterns) learned over time.

**Custom internals (not wrappers):**
- **Hippo**: Storage engine — encrypted records (AES-256-GCM), vector index, and graph in one local store.
- **MOSAIC**: Community-detection algorithm for memory graph clustering, tuned for small heterogeneous graphs that mutate nightly.
- **LilliHD**: Hyperdimensional memory substrate — distinct representations per memory tier with structural recall.
- **Native engine**: Rust core for embedder and graph kernels (bge-small-en-v1.5, 384-dim).

**Ambient operation:** Hooks capture every turn verbatim (UserPromptSubmit, Stop). SessionStart hook injects relevant memory prefix. Sleep cycles consolidate — cluster, summarize, decay old connections, reinforce frequently co-retrieved paths. One LLM call per night via `claude -p` (≤1% daily quota).

## Assessment

The most architecturally ambitious open-source AI memory system. The custom storage/clustering/HD substrate approach is genuinely novel — most memory projects are thin wrappers over off-the-shelf vector stores. Benchmarks are honest and reproducible: ties MemPalace on LongMemEval-S (R@5 0.966), but the longitudinal benchmarks (Rescue@10 1.000 for contradiction handling, personal-fact drift 0.9933) test what actually matters for personal memory.

**Key limitations for our stack:**
- **macOS-only** — Rust native engine and launchd daemon don't support Windows/Linux yet. This is a hard blocker for our Windows-primary setup.
- **English-only** by design (translates to English on ingest).
- Solo-maintained, though well-documented and benchmarked.
- Hooks modify `~/.claude/settings.json` — review before installing.
- Cold start needs ~10 sessions before quality improves noticeably.

Worth monitoring for a Linux/Windows port. The architecture (verbatim episodic → consolidation → semantic/procedural tiers, contradiction-aware retrieval) is worth studying even if we can't run it today.

## Mechanical details

- **Install**: Clone → `pip install .` (builds Rust native engine via setuptools-rust) → `npm install` MCP wrapper → `iai-mcp daemon install`
- **Hooks**: `iai-mcp capture-hooks install` wires UserPromptSubmit + Stop + SessionStart
- **Connect**: `claude mcp add iai-mcp -- node <path>/mcp-wrapper/dist/index.js`
- **Verify**: `iai-mcp doctor` (25 checks), `iai-mcp daemon status`
- **Data**: `~/.iai-mcp/` — encrypted at rest (AES-256-GCM), key at `~/.iai-mcp/.key` (mode 0600)
- **CLI**: `iai recall`, `iai capture`, `iai ask` (LLM synthesis grounded in memory), `iai status`, `iai last`
- **Hosts**: Claude Code (primary), Codex CLI, Gemini CLI, Cursor CLI, Claude Desktop
- **Requirements**: macOS (Apple Silicon), Python 3.11-3.12, Node.js 18+, Rust toolchain, ~500 MB disk

## Security

- **License**: MIT — no restrictions
- **Encryption**: AES-256-GCM at rest, key file mode 0600. Back up `~/.iai-mcp/.key` — lose it, lose memories.
- **Local-only**: No telemetry, no cloud, no API keys. Only outbound traffic is normal LLM calls via existing CLI subscription.
- **Hooks**: Modify `~/.claude/settings.json` — review `capture-hooks install` output. Hooks are idempotent and cleanly uninstallable.
- **Doctor check (p)**: Explicitly verifies no Anthropic API-key SDK path is installed — enforces subscription-only LLM access.
- **Supply chain**: Solo contributor. Rust core builds from source. Dependencies: SQLite, candle (tensor), NumPy, audited `cryptography` AES. All permissive.
- **No dangerous patterns**: No eval, no shell injection vectors. Crypto uses audited `cryptography` library, not hand-rolled.
