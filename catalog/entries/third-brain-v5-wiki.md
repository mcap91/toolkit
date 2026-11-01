---
name: third-brain-v5-wiki
title: Third Brain V5 (Wiki/Knowledge Layer)
url: "https://github.com/Mark393295827/third-brain-v5-skills"
category: framework
summary: "Obsidian-specific schema, heavy; staleness and contradiction detection concepts worth noting for kb"
tags: [wiki, knowledge-os, ingest, lint, kb]
reviewed: 2026-05-25
acquired: 2026-05-25
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

18 skills turning Claude/Codex/Gemini into a persistent knowledge OS. This entry covers the wiki and knowledge layer only — the verification skills from this same repo are covered separately in `verify-before-claim`. The wiki-relevant skills are: wiki-ingest (STOW pipeline converting articles/PDFs/meetings into interlinked wiki with source notes, entity/concept pages), knowledge-ops (classify, deduplicate, vectorize via ChromaDB, sync across repositories), and wiki-lint (health checks across 8 dimensions: frontmatter, links, orphans, staleness, contradictions, drift, and two more). The storage schema assumes Obsidian-style directories (sources/, concepts/, entities/) and Obsidian markdown conventions.

## Assessment

Obsidian-specific schema is the primary incompatibility — kb wiki uses typed records with YAML frontmatter in issues/, decisions/, areas/, initiatives/ directories, not Obsidian's flat-file convention. The system is also heavy (ChromaDB dependency for vector search, 18 skills, cross-repo sync machinery). The comparison below shows the overlap and the lint dimension gap that is worth addressing in kb.

| Feature | Third Brain V5 | kb wiki |
|---|---|---|
| Ingest pipeline | STOW (articles, PDFs, meetings → linked wiki) | Manual `wiki create` + frontmatter |
| Storage schema | Obsidian-style: sources/, concepts/, entities/ dirs | Typed records: issues/, decisions/, areas/, initiatives/ |
| Vectorization | ChromaDB for semantic search | Text-based search index (.search-index.json) |
| Lint dimensions | 8: frontmatter, links, orphans, staleness, contradictions, drift, + 2 more | Frontmatter validation, schema compliance |
| Cross-repo sync | knowledge-ops syncs across repositories | Single repo per wiki |
| Format | Assumes Obsidian markdown | YAML frontmatter + markdown body |

**What kb could learn**:

1. **Staleness detection** — Third Brain's wiki-lint checks for stale records by examining `updated` dates against a configurable threshold. kb lint currently checks only frontmatter validity, not content freshness.
2. **Contradiction detection** — semantic validation checking whether two records make conflicting claims. kb has no semantic validation beyond schema compliance.
3. **Structured ingest pipeline** — STOW is a concrete pipeline for converting external content (articles, PDFs, meeting notes) into wiki records automatically. kb has no automated ingest path; all records are manually created.

## Mechanical details

Do not install. Obsidian-specific schema is incompatible with kb wiki's record format, and running a separate knowledge OS alongside kb would create competing sources of truth. The three lint concepts (staleness, contradiction, ingest) can be developed as native kb lint rules without any Third Brain code. Study the wiki-lint skill definition in the source repo for the staleness threshold and contradiction detection heuristics.

## Security

Licensed MIT. No executable binaries are distributed — the package consists entirely of Markdown skill files that are copied into the user's agent config directory (e.g. `~/.claude/skills/`). The install script (`install.sh`) performs only directory creation and file copies; it does not download additional dependencies, modify system paths, or escalate privileges. The ChromaDB dependency used by the knowledge-ops skill is only relevant if that skill is actively run, and is invoked via `pip install` at the user's discretion, not automatically.

No credentials, tokens, or network calls are required at install time. Skills run entirely through the agent's own LLM context — they contain no server-side components, webhooks, or telemetry. The primary security consideration is supply-chain: skills are installed into the global agent config and will be loaded for all projects on that machine. Review individual skill files before installing, and prefer project-scoped installation (`.claude/skills/`) over global (`~/.claude/skills/`) to limit blast radius.
