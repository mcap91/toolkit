---
name: obsidian-skills
title: Obsidian Skills (Kepano)
url: "https://github.com/kepano/obsidian-skills"
category: skill
summary: Obsidian-specific; Defuddle (web→clean markdown) and skill packaging patterns worth noting
tags: [obsidian, skills, markdown, canvas, defuddle, web-extraction]
license: MIT
security_flags: []
overlaps: []
reviewed: 2026-05-25
acquired: 2026-05-25
source: unknown
---

## What it does

A collection of five Claude Code-compatible skills for working with Obsidian vaults: Obsidian Markdown (wikilinks, embeds, callouts, properties), Obsidian Bases (database-like views with filters and formulas), JSON Canvas (visual node/edge canvas files), Obsidian CLI (vault interaction via command-line for plugin/theme dev), and Defuddle (extracts clean markdown from web pages, stripping unnecessary content to conserve tokens). Installable via plugin marketplace, npx, or manual copy. 33k stars.

## Assessment

The Obsidian-specific skills (Markdown, Bases, Canvas, CLI) don't apply — we use kb wiki, not Obsidian, as our knowledge layer. Defuddle is the interesting outlier: extracting clean markdown from web pages while conserving tokens is a pattern we could use for catalog research or source ingestion. The skill packaging approach (marketplace + npx + manual install paths) is also a useful reference for how to distribute skills.

## What to adopt

- Defuddle concept: consider a "web→clean markdown" extraction step for catalog research or kb source ingestion workflows.
- Multi-platform install pattern (marketplace, npx, manual) as a distribution model if we ever publish skills externally.

## Security

This is a collection of SKILL.md instruction files with no executable code — skills are plain Markdown that an agent reads and follows. There is no installation of binaries, no network access, and no runtime dependencies beyond the agent itself. The MIT license (copyright Steph Ango / kepano) permits unrestricted use and redistribution.

The only surface worth noting is the Defuddle skill, which directs the agent to fetch and process arbitrary web URLs. Any risk here is bounded by the agent's own tool permissions and SSRF guards; the skill itself does not expand the permission boundary. No supply-chain, credential-handling, or code-execution concerns apply.
