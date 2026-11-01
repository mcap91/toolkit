---
name: obsidian-claude-second-brain-workflow
title: Obsidian + Claude Code Second Brain Workflow
url: "https://medium.com/@evgeni.n.rusev/how-i-built-my-second-brain-with-obsidian-claude-code-9fb54b7665ca"
category: agent-pattern
summary: "Practitioner workflow for building an AI-native personal knowledge base using Obsidian as the storage layer and Claude Code as the structuring agent — vault organized as books/, articles/, posts/, wiki/ with frontmatter tags and wikilinks; CLAUDE.md defines the schema and operating manual; Claude reads raw text and structures it into tagged pages, wiki entries, comparison tables, and cross-referenced summaries without plugins or API wrappers"
tags: [obsidian, knowledge-management, second-brain, claude-code, workflow, markdown, personal-knowledge-base]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: [obsidian-skills, second-brain-skills, third-brain-v5-wiki]
license: N/A
security_flags: []
source: unknown
---

## What it does

Practical guide (by Evgeni Rusev, published April 2026) to building an AI-native personal knowledge base where Obsidian is the storage layer and Claude Code is the structuring agent.

Key design decisions:

- **Obsidian as LLM-native storage**: Obsidian vaults are plain Markdown with tags, frontmatter, and wikilinks — Claude reads and writes `.md` files natively with no API wrappers, plugins, or export steps.
- **Vault structure**: `books/`, `articles/`, `posts/`, `wiki/` (with subfolders for domains like mental-models, economics, psychology, history, ai), plus `index.md` as master catalog, `log.md` for chronological records, and `CLAUDE.md` as Claude's operating manual/schema definition.
- **Claude as structuring agent**: Raw highlights, notes, or source text go into the vault; Claude structures them into tagged pages, extracts key insights, represents knowledge as summaries, wiki entries, or comparison tables, and creates cross-references via wikilinks.
- **CLAUDE.md as schema contract**: Defines the vault's conventions, naming patterns, frontmatter fields, and tagging taxonomy so Claude produces consistent output across sessions.

The approach treats the vault as a knowledge graph that Claude can both read from (for context) and write to (for structured capture), making the knowledge base grow with each interaction.

## Security

N/A — workflow article, not software. No code to audit.