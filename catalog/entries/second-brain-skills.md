---
name: second-brain-skills
title: Second Brain Skills
url: "https://github.com/coleam00/second-brain-skills"
category: plugin
summary: "Claude Code skill collection for knowledge work — MCP client with progressive disclosure, PPTX/carousel generator with brand system, SOP/runbook creator, Remotion video creator, skill creator guide, and brand & voice generator; by Cole Medin"
tags: [claude-code-plugin, skills, knowledge-work, presentations, video, documentation, mcp-client]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: []
source: unknown
---

## What it does

Collection of Claude Code skills that extend the agent from a coding tool into a "second brain" for knowledge work. Six skills with progressive disclosure — metadata always in context, body loaded when triggered, resources on demand.

**Skills included:**

1. **MCP Client** — connects Claude Code to external MCP servers (Zapier, GitHub, Sequential Thinking, etc.) with on-demand tool schema loading to avoid context bloat; Python script wrapping stdio/SSE/HTTP transports; config format matches Claude Desktop
2. **PPTX Generator** — professional 16:9 presentations and square LinkedIn carousels using python-pptx; 16 slide layout templates, 5 carousel layouts, batch generation (max 5 slides at a time), visual-first layout selection ("content-slide is the LAST RESORT")
3. **Brand & Voice Generator** — creates `brand.json`, `config.json`, `brand-system.md`, `tone-of-voice.md` files that power the PPTX Generator and guide all other skills; includes 5 example voice configurations (Technical Educator, Calm Authority, Builder's Perspective, Approachable Expert, Contrarian Thinker)
4. **SOP Creator** — runbooks, playbooks, and technical documentation; 12 document types across Tech/Engineering, Operations/Business, Content/Creative, and General; universal structure with Definition of Done as the most important element
5. **Remotion Video Creator** — programmatic video creation using React with Remotion; 28 modular rules covering animations, compositions, assets, captions, charts, 3D, transitions, maps; credited to official remotion-dev/skills by Jonny Burger
6. **Skill Creator** — guide for creating new skills with the correct anatomy (SKILL.md + scripts/ + references/ + assets/), creation process, and progressive disclosure principles

## Differentiators

- **Progressive disclosure architecture** — skills load context on demand rather than bloating the context window
- **Brand system integration** — brand identity defined once, consumed by PPTX generator and other skills
- **Visual-first layout selection** — PPTX skill includes a decision tree that maps content types to visual layouts, treating text-heavy content slides as a last resort
- **MCP client abstraction** — wraps MCP servers behind a Python CLI that loads tool schemas on demand

## Mechanical details / What to adopt

- Clone repo, copy skill folders to `~/.claude/skills/`
- MCP Client requires creating `mcp-config.json` from the example config with your API keys
- PPTX Generator requires running the Brand & Voice Generator first (or manually creating brand files in `brands/your-brand-name/`)
- Remotion requires external project setup via `npx create-video@latest`
- SOP Creator and Skill Creator work out of the box with no configuration
- Author: Cole Medin (coleam00)

## Security

License not explicitly stated in README. No external dependencies for SOP Creator and Skill Creator. MCP Client stores API keys in a local config file. PPTX Generator requires python-pptx. Remotion skill delegates to an external npm project.