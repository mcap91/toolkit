---
name: termdraw
title: termDRAW
url: "https://github.com/benvinegar/termdraw"
category: cli-tool
summary: "Agent-friendly ASCII diagram editor for the terminal — retained vector-style objects (lines, boxes, text) with rearranging, fenced Markdown export, native .td.json documents for re-editing, clipboard via OSC 52, embeddable OpenTUI components; Bun 1.3+, MIT"
tags: [terminal, ascii-art, diagrams, drawing, agent-friendly, opentui, pi, bun, markdown-export]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

termDRAW is a terminal-based diagram editor that treats drawn elements as retained objects rather than painted pixels. Lines, boxes, and text remain selectable and rearrangeable after creation. Boxes can act as frames for fully contained children. The editor outputs terminal text (not SVG or bitmap), making the output directly usable in READMEs, docs, tickets, and agent prompts.

Described as "agent-friendly" — it was built because the author found himself hand-typing ASCII diagrams to help coding agents understand intent, and a proper drawing tool works better for that.

Key capabilities:

- **Tools**: Brush (B), Select (A), Box (U), Line (P), Text (T); clean line glyph rendering including sub-cell Braille for shallow/steep angles.
- **Export**: plain text to stdout on Enter/Ctrl+S, fenced Markdown (`--fenced`), clipboard via OSC 52 (`--clipboard`).
- **Persistence**: native `.td.json` documents preserve object metadata for re-editing; plain-text output is export-only.
- **Embeddable**: the `@termdraw/opentui` package exposes `TermDrawApp`, `TermDrawEditor`, and lower-level renderables for embedding in OpenTUI applications.
- **Pi integration**: `@termdraw/pi` opens termDRAW in a Pi overlay (`/termdraw`).

## Mechanical details

Requires Bun 1.3+ and a terminal with mouse support. Three npm packages: `@termdraw/app` (standalone CLI), `@termdraw/opentui` (embeddable components), `@termdraw/pi` (Pi overlay). OSC 52 clipboard support works over SSH; inside tmux, requires `set-clipboard on` or `external`. Active development — clipboard feature merged September 2026, recent releases through v0.4.x.

## Security

MIT licensed. No security flags. Terminal-local tool with no network calls, no telemetry, no credentials. The OSC 52 clipboard path is handled by the terminal emulator, not the host OS.

## How to use it

npm install --global @termdraw/app
