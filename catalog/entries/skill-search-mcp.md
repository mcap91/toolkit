---
name: skill-search-mcp
title: Skill Search MCP
url: "https://github.com/sowhan/skill-search"
category: mcp-server
summary: "Semantic skill retrieval MCP for Claude Code — replaces per-turn skill listing tax (~7.3K tokens) with vector search over descriptions; saves 3.19% of 200K context window per turn at 117 skills, recall@3 of 0.79; MIT, service-free default"
tags: [claude-code, skills, mcp-server, vector-search, token-optimization]
reviewed: 2026-06-19
acquired: 2026-06-19
license: MIT
security_flags: []
overlaps: [skill-router]
source: unknown
---

## What it does

Replaces Claude Code's native per-turn skill listing (which injects name + description for every installed skill) with a two-part system:

1. **generate_overrides.py**: Sets all skills to name-only in `.claude/settings.local.json`, freeing the description budget. A small allowlist (the router skill) stays fully visible.
2. **MCP server** (4 tools): `search_skills` (semantic vector search over full descriptions), `get_skill`, `reindex`, `health`. Returns top-k relevant skills for the current task.

A companion router skill acts as the always-on trigger — it tells Claude to call `search_skills` before guessing which skills to invoke.

Measured on 117 skills: native listing costs ~7,267 tokens/turn (3.63% of 200K). Name-only + skill-search costs ~887 tokens/turn (0.44%). Saves ~6,380 tokens/turn. Semantic matching fixes the name-bias problem — `a11y-debugging` surfaces for "review my UI for accessibility" despite no shared keywords.

## Assessment

Well-engineered solution to a real scaling problem. The token math is honest and reproducible (ships measurement scripts). The recall@3 of 0.79 on a 24-query eval set is modest but the author is transparent about it — and the genuine misses are short, generic-named skills where small embedders struggle.

For our setup we currently have ~20 skills (from the available-skills list), well below the "hundreds" threshold where this pays off. Worth monitoring as the skill count grows. The architecture is sound — incremental reindex, content-hash dedup, staleness warnings, health checks with non-zero exit codes for CI.

The service-free default (embedded Qdrant + fastembed ONNX) means no Docker or Ollama required. Opt-in tier uses Qdrant server + Ollama embeddings for better recall.

## Mechanical details

- **Install**: `pipx install skill-search-mcp`
- **Setup**: `skill-search --reindex` → `claude mcp add --transport stdio skill-search -- skill-search` → install router skill → `skill-search-overrides`
- **Default embedder**: fastembed BAAI/bge-small-en-v1.5 (384-dim, downloads once, runs offline)
- **Opt-in**: Qdrant server + Ollama `embeddinggemma` (768-dim) for better recall
- **Config**: All env-var overridable (`SKILL_*` prefix); `SKILL_TOP_K=6` default
- **Reindex**: Incremental via content hash — ~0.07s when nothing changed, ~18.8s full rebuild
- **Tests**: 13 unit tests (offline) + integration tests; `pytest -m "not integration"`

## Security

- **License**: MIT — no restrictions
- **Supply chain**: Single contributor, but clean codebase with tests, eval harness, and reproducible measurements
- **Dependencies**: fastembed (ONNX), qdrant-client, tiktoken — standard ML stack, no unusual deps
- **No dangerous patterns**: No eval, no shell injection, no credential handling beyond standard env vars
- **Local-only by default**: Embedded Qdrant stores vectors at `~/.cache/skill-search/qdrant`, no external calls unless Ollama tier opted in

## Usage notes

- Author measured 117 skills → ~7,300 tokens injected every turn (~3.6% of 200K window) from skill descriptions alone. Name-only mode + semantic MCP retrieval drops this to ~900 tokens/turn.
- Keyword matching misses skills whose names don't echo user wording (e.g. "review my UI for accessibility" won't surface a skill named "a11y-debugging")
- The semantic retrieval recall is ~0.79 on the author's test set — not perfect but better than keyword overlap
- Only pays off with many skills (hundreds); light installs won't notice the savings
