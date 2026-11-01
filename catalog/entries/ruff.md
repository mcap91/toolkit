---
name: ruff
title: Ruff
url: "https://github.com/astral-sh/ruff"
category: cli-tool
summary: "Rust-written Python linter and formatter from Astral; re-implements 900+ rules (Flake8 + dozens of plugins, isort, pydocstyle, pyupgrade) and a Black-compatible formatter behind one interface, with built-in caching, autofix, pyproject.toml config, and editor/pre-commit/GitHub Action integrations. MIT."
license: MIT
tags: [python, linter, formatter, static-analysis, rust, code-quality, astral, pre-commit]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: [curl-pipe-sh-install]
source: unknown
---

## What it does

Ruff is a Python linter and code formatter written in Rust, developed by Astral (creators of uv and ty). It re-implements over 900 lint rules as first-party Rust code, covering the checks of Flake8 and dozens of its plugins, isort, pydocstyle, pyupgrade, autoflake, and others, plus a formatter with drop-in parity to Black. A single binary replaces the separate tools while running one to three orders of magnitude faster. It supports autofix (e.g. removing unused imports), built-in result caching, hierarchical/cascading configuration for monorepos, and Python 3.14. It is used by projects including FastAPI, Pandas, SciPy, Apache Airflow, Hugging Face, and the Anthropic Python SDK.

## Mechanical details

- **Install:** `pip install ruff`, `uv tool install ruff@latest`, `pipx install ruff`, or `uvx ruff check`; also Homebrew/Conda; standalone installer `curl -LsSf https://astral.sh/ruff/install.sh | sh` (or the PowerShell equivalent on Windows)
- **Lint:** `ruff check [path]` (add `--fix` to autofix)
- **Format:** `ruff format [path]`
- **Config:** `pyproject.toml` (`[tool.ruff]`), `ruff.toml`, or `.ruff.toml`; per-rule select/ignore, `preview = true` for unstable rules
- **CI/hooks:** `astral-sh/ruff-action` GitHub Action; `astral-sh/ruff-pre-commit` hooks (`ruff-check`, `ruff-format`)

## Security

MIT licensed. Primary install is via pip/uv/pipx/package managers; the project also documents a `curl … | sh` standalone installer that pipes a remote script to a shell (`security_flags: curl-pipe-sh-install`) — the package-manager paths avoid that pattern. Ruff is a static-analysis tool that reads source files locally and makes no network calls in normal linting/formatting.

## How to use it

pip install ruff
