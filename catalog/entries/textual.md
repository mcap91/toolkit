---
name: textual
title: Textual
url: "https://github.com/Textualize/textual"
category: framework
summary: "Textualize's Python TUI framework for building cross-platform terminal user interfaces with a simple, optionally-async API and a large widget library (buttons, trees, data tables, inputs, text areas); apps can also be served to a web browser via textual serve / Textual Web. MIT."
license: MIT
tags: [tui, terminal, python, ui-framework, textualize, async, widgets, cli]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it does

Textual is a Python framework for building cross-platform user interfaces that run in the terminal or a web browser, from Textualize. It offers a simple, declarative API with CSS-like styling, a flexible layout system, predefined themes, and a widget library spanning buttons, tree controls, data tables, inputs, and text areas. It is asynchronous under the hood but does not require the developer to use async. The `textual-dev` package provides a dev console that connects from a second terminal to surface logs, print statements, and events. Apps include a fuzzy-search command palette (ctrl+p) and can be served to the web with `textual serve` or the Textual Web service.

## Mechanical details

- **Install:** `pip install textual textual-dev`
- **Demo:** `python -m textual`, or `uvx --python 3.12 textual-demo` without installing
- **Serve to web:** `textual serve "python -m textual"`
- Apps subclass `App`, implement `compose()` yielding widgets, and run via `app.run()`

## Security

MIT licensed. Textual apps run locally in the terminal; serving to the web (`textual serve` / Textual Web) exposes an app over HTTP and shares it beyond the local machine — treat served apps and their inputs accordingly. No security flags recorded from the observed material.

## How to use it

pip install textual textual-dev
