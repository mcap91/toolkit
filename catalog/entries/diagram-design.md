---
name: diagram-design
title: Diagram Design
url: "https://github.com/cathrynlavery/diagram-design"
category: skill
summary: "Editorial-quality diagram skill for Claude Code, Codex, Copilot, Factory Droid, Pi, and other Agent Skills hosts — 42 visual types (architecture, flowchart, sequence, state, ER, timeline, Sankey, Wardley map, exploded axonometric, etc.) as self-contained HTML+SVG; brand onboarding from a URL; import from draw.io/Mermaid/Excalidraw; export to SVG/PNG; 9 semantic behavior patterns; optional accessible motion; 87 monochrome icons; no shadows, no Mermaid; MIT"
tags: [diagrams, visualization, svg, html, skill, claude-code, codex, copilot, brand-design, editorial, agent-skill, import-export, accessibility]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

A coding-agent skill that generates editorial-quality diagrams as self-contained HTML+SVG files. No build step, no JavaScript dependencies, no external images. Opens in any browser, offline.

42 visual types: architecture, IT current-state, flowchart, sequence, state machine, ER/data model, timeline, swimlane, quadrant, radar, loop/flywheel, nested hierarchy, tree, org chart, layer stack, Venn, pyramid/funnel, bar chart, treemap, line chart, Gantt, scatter plot, high-level stack, process, medallion, data flow, DP integration, DP security matrix, Sankey, fishbone, Wardley map, kanban, user journey, deployment, dependency graph, UML class, story map, database schema, polar chart, waterfall, architecture delta, exploded axonometric, axonometric plan, heatmap.

Three variants per type: minimal light, minimal dark, and full-editorial.

**Brand onboarding**: point the skill at a URL, it extracts the site's palette + font stack and maps them to semantic tokens (paper, ink, accent, muted, link). WCAG AA contrast checks run automatically. Named profiles support multiple client brands.

**Import**: redraws draw.io, Mermaid, or Excalidraw sources at a chosen format/size/detail/audience level. Four dials: format (html/svg/png), size (doc/slide/social/print), detail (faithful ≤24 / balanced ≤12 / simplified ≤7 nodes), audience (engineer/mixed/executive).

**Semantic patterns**: 9 behavior patterns (fan-in queue, policy trace, paved road, governance catalog, compensating layers, etc.) that select layout type automatically based on what the diagram describes.

## Mechanical details

Install: `npx skills add cathrynlavery/diagram-design` (cross-agent), or via marketplace for Claude Code, Codex, Copilot, Factory Droid, Pi. Progressive loading — only SKILL.md + one type reference loaded per request.

Design system: Instrument Serif titles, Geist sans node names, Geist Mono sublabels, 1px hairlines, no shadows, max 10px border-radius, all coords divisible by 4. One accent color, 1-2 focal elements per diagram. 87 monochrome icons (Tabler Icons MIT, Simple Icons CC0).

CI: lint-skin.py (source), lint-render.py (headless Chromium rendered output), geometry verification (label placement, diagonal connectors, port spacing), treemap area accuracy, waterfall conservation, Sankey conservation, block registry, docs sync. Cross-platform CI (Linux/Windows/macOS).

PNG export requires Playwright + Chromium (`pip install playwright && playwright install chromium`).

## Security

MIT licensed. Generated HTML makes no network requests beyond Google Fonts. Motion HTML uses a pinned, reviewed controller — arbitrary scripts, remote assets, CSS imports, and executable attributes are rejected by the linter. PRIVACY.md documents what the skill sends over the network.