---
name: nvk-llm-wiki
title: llm-wiki (nvk)
url: https://github.com/nvk/llm-wiki
source_url: https://github.com/nvk/llm-wiki
category: plugin
summary: Claude Code plugin (with ports for Codex, DeepSeek Harness, OpenCode, and generic SKILL.md agents) implementing Karpathy's LLM Wiki pattern — treats raw sources as immutable "source code" and the LLM as a "compiler" that synthesizes them into a structured, source-linked wiki; organizes topics as isolated sub-wikis in a hub, runs parallel multi-agent research (5/8/10 agents per depth mode), and enforces that no wiki page exists without a cited source; commands include /wiki init, /wiki:research, /wiki:thesis, /wiki:query, /wiki:ingest, /wiki:compile; ~1.5k GitHub stars; MIT
tags:
  - llm-wiki
  - claude-code-plugin
  - knowledge-base
  - source-citation
  - multi-agent
  - obsidian
  - mcp
  - rag-alternative
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - karpathy-llm-wiki
  - nashsu-llm-wiki
license: MIT
security_flags: []
source: web
---

## What it does

Claude Code plugin (also packaged for OpenAI Codex, DeepSeek Harness, OpenCode, and as portable SKILL.md files for other agents) implementing Andrej Karpathy's LLM Wiki pattern. Frames raw ingested sources as immutable "source code" and the LLM as a "compiler" that synthesizes them into a structured wiki, enforcing that no wiki page is written without a cited source behind it. Organizes knowledge as a hub of isolated topic sub-wikis ("one topic, one wiki") with dual-linking for Obsidian and plain-markdown compatibility. Supports parallel multi-agent research at three depths (5 agents standard, 8 deep, 10 maximum speed), source ingestion from URLs/files/PDFs/bulk collections, thesis-driven research that evaluates specific claims, deterministic linting/integrity verification, session-memory checkpoints, and privacy-sealed project handoffs. Installed on Claude Code via `/install-plugin github:nvk/llm-wiki`; core commands are `/wiki init`, `/wiki:research "topic" --sources N`, `/wiki:thesis`, `/wiki:query`, `/wiki:ingest`, `/wiki:compile`.

## Mechanical details

- Distribution: Claude Code plugin marketplace; also ships an OpenAI Codex plugin marketplace package (`@wiki research "topic"`, `$wiki-query`), DeepSeek Harness filesystem skill, OpenCode instruction-file config, and generic SKILL.md files for other agents.
- Sandboxing: documents permission requirements for tools like `nono`, needing explicit filesystem access to plugin caches and wiki data directories.
- Session capture (memory checkpoints) is optional and can be disabled.
- ~1.5k GitHub stars, 142 forks at time of review.
- MIT licensed.

## Security

MIT license. No network-service component described (runs as a local CLI/plugin inside the host agent's existing sandbox/permissions). Session memory capture is optional and user-disableable. No telemetry described in available documentation.

## Usage notes

- Cited in an Instagram reel (uncredited blind benchmark methodology) as getting more right answers than plain Claude Code on blind-graded questions, but costing about twice as much per answer (source: https://www.instagram.com/reel/DfFSZDvN6oV/)
