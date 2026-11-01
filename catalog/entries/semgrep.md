---
name: semgrep
title: Semgrep
url: https://github.com/semgrep/semgrep
source_url: https://www.instagram.com/reel/DeJyswKCtCY/
source: instagram
category: cli-tool
summary: Fast open-source static analysis tool using AST pattern matching to find bugs and security issues across 30+ languages; runs as a CLI, pre-commit hook, IDE integration, or CI step; LGPL-2.1 Community Edition engine with per-function-only taint tracking, commercial AppSec Platform adds cross-file/cross-function dataflow and 20,000+ proprietary rules; forked as Opengrep (also LGPL-2.1) after licensing concerns
tags:
  - sast
  - static-analysis
  - pre-commit
  - security
  - ast-pattern-matching
  - code-quality
reviewed: 2026-10-29
acquired: 2026-10-29
license: LGPL-2.1 (Community Edition engine); rules under Semgrep Rules License v1.0; commercial AppSec Platform separately licensed
security_flags: []
overlaps:
  - codeql
---

## What it does

Semgrep is a static analysis tool that matches code against rules written to look like the source code itself, using abstract-syntax-tree (AST) pattern matching rather than plain text/regex matching — a rule like `$X == $X` matches a tautological comparison regardless of variable names or formatting. Supports 30+ languages. Runs as a one-off CLI scan, inside an IDE, as a pre-commit hook on changed files (blocking a commit when a rule matches), or as a CI/CD step; provides SAST (security rules), software composition analysis (SCA), and secrets detection.

## Mechanical details

The open-source Community Edition (CE) engine is LGPL-2.1-licensed; the 3,000+ community rules it ships with are under the separate Semgrep Rules License v1.0 (permits internal business use, bars use in competing products/SaaS). CE's taint analysis is intraprocedural only (per-function); cross-function and cross-file dataflow, custom taint propagators, and the Secrets validators are reserved for the commercial AppSec Platform (20,000+ proprietary rules, 35+ languages). After the platform moved features behind a commercial license, a consortium of application-security companies forked Semgrep 1.100.0 as Opengrep, also under LGPL-2.1, maintaining compatibility with existing Semgrep rules.

## Security

No build step required for most languages — runs against source directly without compiling or executing it. Developed and commercially backed by Semgrep, Inc. No security advisories surfaced against the CE engine itself in this research pass.
