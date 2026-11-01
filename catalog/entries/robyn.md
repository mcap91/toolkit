---
name: robyn
title: Robyn
url: "https://github.com/sparckles/Robyn"
category: framework
summary: "Async Python web framework with a Rust runtime (PyO3); sync/async handlers, dynamic routing, middleware, WebSockets, built-in OpenAPI generation, Jinja2 templating, hot reload, CLI scaffolding, plus built-in AI-agent routing and an MCP server mode. No external server needed. BSD-licensed."
license: BSD-2-Clause
tags: [web-framework, python, rust, async, api, websockets, mcp, high-performance]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it does

Robyn is an async Python web framework whose runtime is written in Rust (via PyO3), so it needs no external server for production. Handlers are defined with decorators (`@app.get("/")`, sync or async) on a `Robyn(__file__)` app started with `app.start(port=...)`. Features include a multithreaded runtime with multi-core scaling, dynamic URL routing and sub-routers, before/after middleware, WebSockets, dependency injection, built-in form-data handling, static file serving and file responses, streaming/SSE, startup/shutdown events, exception handling, automatic OpenAPI generation, Jinja2 templating, hot reloading, project scaffolding via CLI, and experimental io-uring support. Recent additions include built-in AI-agent routing/execution and a Model Context Protocol (MCP) server mode to connect the app to AI applications.

## Mechanical details

- **Install:** `pip install robyn` (or `conda install -c conda-forge robyn`; `pip install "robyn[all]"` adds Pydantic validation and Jinja2)
- **Run:** `python app.py`; flags include `--processes`, `--workers`, `--dev` (hot reload), `--log-level`, `--fast`, `--create` (project template), `--disable-openapi`
- Python 3.10–3.14; building from source needs Rust, a C compiler, and `maturin`

## Security

Robyn is released under a BSD license; sources that read the repository LICENSE report BSD 2-Clause ("Simplified"), while the PyPI package metadata lists BSD-3-Clause — verify against the repo LICENSE for a specific release. As a web framework it serves network-facing endpoints; the built-in MCP server and AI-agent routing expose additional surfaces that should be secured when enabled. No other security flags recorded from the observed material.

## How to use it

pip install robyn
