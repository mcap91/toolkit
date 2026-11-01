---
name: fluiddocs-deck-builder
title: FluidDocs Deck Builder
url: "https://github.com/FluidForm-ai/fluiddocs-deck-builder"
category: plugin
summary: Well-built skill/plugin pack for HTML slide decks; interesting multi-reviewer architecture but outside bioinformatics workflows
tags: [presentation, slides, skill-pack, claude-code-plugin, html, pdf-import, meta-skill, pdf]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Open-source Claude Code plugin that generates interactive HTML slide decks from one-line briefs. Ships five type-correct deck spines (pitch 14 slides, sales 11, launch 12, keynote 28, all-hands 15), a PDF/PPTX importer, and a critique skill. Each generated deck is a single self-contained HTML file with inline editing (press E), localStorage autosave, and Ctrl+S download. A multi-reviewer quality pipeline (Brand, Copy, Layout) runs in parallel when subagents are available. Optional deploy to fluiddocs.ai via included shell script.

## Assessment

The skill architecture is well-executed — type-correct content spines per deck type, multi-reviewer pipeline, and clean SKILL.md format make it a good reference for how to structure a skill pack. However, slide decks are outside the bioinformatics/agent-tooling focus of this catalog. Note for architecture reference; no adoption path.

## Mechanical details

- Install via `/plugin marketplace add` or manual copy to `~/.claude/skills/`
- Seven skills: deck-pitch, deck-sales, deck-launch, deck-keynote, deck-all-hands, deck-import, deck-critique-lite
- Deploy script at `scripts/deploy.sh` handles auth caching, project naming, and cross-platform browser open
- Works with Claude Code, Codex, Kimi Code, OpenCode, Gemini CLI via SKILL.md convention

## Security

MIT license with no restrictions. The deploy script handles auth tokens cached at `~/.config/fluiddocs/auth.json` — standard OAuth flow. Single-file HTML output has no external dependencies at runtime. The plugin install path (`~/.claude/skills/`) is the standard Claude Code convention. No eval patterns, no shell injection vectors in the skill definitions. Deploy script uses `curl` with proper quoting. Clean.