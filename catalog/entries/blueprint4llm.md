---
name: blueprint4llm
title: blueprint4llm
url: https://github.com/evgenyigumnov/blueprint4llm
source_url: https://www.reddit.com/r/ollama/comments/1xey67z/comment/19rmojt7579uq/
source: reddit
category: skill
summary: CLI + Claude Code/Codex/Pi skill that renders Markdown plans (plan.md) to HTML or PDF with embedded diagrams and charts, offline, without calling an LLM — fenced blocks for D2, Mermaid, Graphviz, PlantUML, draw.io, Pencil, Balsamiq, Figma, OpenAPI, Excalidraw, Vega-Lite, and ECharts, each rendered locally to SVG; live preview server, CI validation (--check with JSON diagnostics), and a programmatic ESM API; also ships a VS Code preview/export extension; MIT, requires Node.js ≥22.13 and Puppeteer's Chrome.
tags:
  - skill
  - markdown
  - diagrams
  - visualization
  - plan-md
  - d2
  - mermaid
  - plantuml
  - drawio
  - vega-lite
  - echarts
  - cli-tool
  - claude-code
  - codex
  - vscode-extension
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT
security_flags: []
overlaps:
  - dataviz
---

## What it does

Extends what a Markdown file can show beyond CommonMark/GFM's tables and (at most) Mermaid: a dozen diagram/chart/mockup formats can be embedded as fenced code blocks and rendered to real visuals, with Markdown staying the source of truth and the CLI doing the rendering without any LLM call. Motivating use case: instead of an agent-generated `plan.md` being a long wall of text, the agent (or a human) writes flowcharts, UI prototypes, API references, and charts directly into the plan, reviewable before implementation.

**Supported formats (fence → renderer):** D2 (offline, bundled WebAssembly — containers, connections, SQL tables, UML), Mermaid (flows/sequences/classes/states/ER), Graphviz/dot (offline DOT→SVG via worker; dot/neato/circo/fdp/osage/patchwork/twopi engines), PlantUML (local engine, no Java/network), draw.io (structural JSON, automatic layout), Pencil (.pen JSONC schema 2.21), Balsamiq (Mockups 3 JSON), Figma (local JSON rendering or token-gated URL export via the Figma REST API), OpenAPI 3.1.1 (rendered as a static API reference), Excalidraw (.excalidraw JSON v2), Vega-Lite 6, and ECharts (static-chart JSON profile) — the latter two rendered locally to static SVG.

**Install (agent skill):** `npx skills add evgenyigumnov/blueprint4llm --skill blueprint4llm --agent codex|claude-code|pi` (Node.js ≥22.20.0+npm; Codex stores it in `.agents/skills/`, Claude Code in `.claude/skills/`; `--global` for cross-project use). Invoke with `$blueprint4llm <request>` (Codex) or `/blueprint4llm <request>` (Claude Code); the skill walks the agent through writing, validating, and rendering a visual plan, and requires the separate `blueprint4llm` CLI plus Puppeteer's Chrome to actually render.

**CLI commands:** `--serve[--port]` for live preview (dark mode, PDF download in-browser); `--check` validates Markdown/diagrams/local images without writing output (CI-friendly, exit code 2 on invalid args, 1 on diagram errors, 0 on warnings-only); `--report-json=<file>` emits a structured JSON diagnostics report (schemaVersion 1, per-diagnostic severity/code/scope/source-path); `--out=<file>` exports HTML (default), PDF (A4, embedded Noto Sans, landscape for wide D2 diagrams, selectable text), SVG, PNG, or JPEG (image formats require exactly one visual block).

**Limits:** 5 MiB Markdown / 100 visual blocks / 256 KiB per block document-wide; draw.io/Pencil/Figma JSON capped at 1 MiB and 10,000 cells/nodes; Balsamiq at 256 KiB/3,000 controls; Vega-Lite at 256 KiB source and other AST/row caps; OpenAPI at 256 KiB/200 operations/500 schemas. Render timeouts: 30s (Mermaid/PlantUML/Vega-Lite), 5s (draw.io layout), 60s (PDF).

**Programmatic API:** `compileMarkdown()`, `renderPdf()`, `writeBlueprintOutput()`, `startPreviewServer()` as ESM exports (`npm install blueprint4llm`).

**Other integration:** a VS Code extension (built VSIX, `code --install-extension`) providing `Blueprint: Open Preview to the Side` and PDF export, with a 200ms debounced live-compile preview.

## Sources

- [blueprint4llm — GitHub README](https://github.com/evgenyigumnov/blueprint4llm) — format table, CLI commands, limits, API, VS Code extension (fetched directly).
- [blueprint4llm LICENSE](https://raw.githubusercontent.com/evgenyigumnov/blueprint4llm/main/LICENSE) — MIT (fetched directly).
- [I Thought SKILLs Were a Waste of Tokens Until I Wrote My Own — r/ollama](https://www.reddit.com/r/ollama/comments/1xey67z/comment/19rmojt7579uq/) — origin story, install commands, use cases (catalog source).

## Security

MIT, single-maintainer repo (evgenyigumnov). Rendering is designed to run offline for all formats except Figma URL mode (which sends a personal access token only to api.figma.com) and HTML exports referencing external images. README states raw HTML is escaped and SVGs are checked for active content and external resources, with "user scripts and graphical editing... not supported" — i.e., explicit XSS/active-content mitigation claimed for the SVG/HTML rendering path. No independent verification of these claims beyond what the README states; no CVE history found.
