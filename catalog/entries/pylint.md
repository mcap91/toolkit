---
name: pylint
title: Pylint
url: "https://github.com/pylint-dev/pylint"
category: cli-tool
summary: "Static code analyzer for Python that checks for errors, enforces coding standards, and flags code smells and refactoring opportunities without executing the code."
tags: [python, linter, static-analysis, code-quality]
reviewed: 2026-09-16
acquired: 2026-09-16
license: GPL-2.0-or-later
security_flags: []
overlaps: []
source: unknown
---

## What it does
Pylint is a static code analyser for Python 2 or 3 (current releases require Python 3.10.0+). It parses source code without executing it and reports errors, coding-standard violations (PEP 8 and beyond), suspicious constructs, and design-level issues such as overly complex functions and duplicate code blocks. It also produces a numeric code-quality score. It is installed via `pip install pylint` and integrates with most editors and IDEs. It ships two additional bundled tools: `pyreverse` (package/class diagram generator) and `symilar` (duplicate-code finder, also integrated into the main linter).

## Differentiators
According to the project's own README, Pylint does not rely purely on type annotations; it infers the actual values/types of nodes using its internal code representation (astroid). For example, given `import logging as argparse`, Pylint can determine that `argparse.error(...)` is actually a logging call, not an argparse call. This inference makes Pylint slower than syntax-only linters but lets it catch more issues in code that is not fully typed. The README also states Pylint includes more checks than many alternatives, including opinionated ones disabled by default. Web sources (Wikipedia, PyPI, third-party comparison articles, retrieved 2026-09-16) describe Pylint as the slowest of the major Python linters in benchmarks (one comparison cited ~1125.5ms vs Ruff's ~23.3ms on an 8-file test fixture) and note it lacks a plugin API equivalent to Ruff's, though it retains an established plugin ecosystem (e.g., pylint-django, pylint-pydantic) and is commonly used alongside or in place of newer tools like Ruff, flake8, mypy, and bandit. The README explicitly recommends pairing Pylint with other tools (ruff, flake8, mypy, pyright/pyre, bandit, black, isort, autoflake, pyupgrade, pydocstringformatter) rather than treating it as a complete solution on its own.

## Mechanical details
Install with `pip install pylint` (or `pip install pylint[spelling]` for spell-checking, which requires the enchant C library). Configuration is via `.pylintrc` or `pyproject.toml`. The README recommends starting adoption on legacy codebases with `--errors-only`, then `--disable=C,R` to suppress convention/refactor messages, progressively re-enabling checks. Supports custom plugins for internal libraries or rules; third-party library support beyond the standard library typically requires a plugin (e.g., searchable on PyPI as `pylint <library>`). Per PyPI, the current stable line requires Python >=3.10.0.

## Security
No security advisories or flags were surfaced in the fetched README or search results. Pylint performs static analysis and does not execute the code it analyses. Professional/commercial support is offered separately via a Tidelift subscription, per the README.
