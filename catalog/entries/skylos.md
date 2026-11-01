---
name: skylos
title: Skylos
url: "https://github.com/duriantaco/skylos"
category: cli-tool
summary: "Local-first static analysis CLI (Python, TS/JS, Java, Go, Kotlin, PHP, Rust, Dart, C#, Shell) that scans for dead code, security flaws, secrets, CI/CD misconfig, quality regressions, and AI-generated code defects; ships as CLI, GitHub Action, VS Code extension, and MCP server"
tags: [static-analysis, dead-code, sast, secrets-scanning, ci-cd, pr-gate, mcp-server, ai-code-verification, python, cli]
reviewed: 2026-08-09
acquired: 2026-08-09
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Skylos is an open-source static analysis CLI covering Python, TypeScript/JavaScript, Java, Go, Kotlin, PHP, Rust, Dart, C#, Shell, and deployment config (GitHub Actions, GitLab CI, Dockerfile, Compose, systemd, Kubernetes manifests). The default scan (`skylos .`) finds dead code; `-a` adds security-flaw detection (SQLi, XSS, SSRF, path traversal, command injection, unsafe deserialization), secrets/credential scanning, dependency CVE checks, and quality-regression checks (complexity, duplicate branches, deep nesting). An `--ai-defects` mode targets AI-generated-code failure patterns: phantom security calls, missing guards/decorators, invented package APIs, impossible dependency versions, unfinished stubs.

It also ships an agent-verification layer: `skylos verify` checks a changed file/range for hallucinated code before a coding agent hands it to review (versioned JSON output, pass/fail/incomplete exit codes); `skylos discover` inventories LLM integrations in a codebase (provider SDKs, agent frameworks, MCP servers/tools); `skylos defend` scores guardrails against OWASP LLM Top 10 / Agentic ASI Top 10 and emits SARIF/markdown evidence reports with a reproducible SHA-256 attestation digest; `skylos agent test` checks a running agent's behavior against a versioned contract (tool calls, refusals, source IDs).

## Differentiators / Key takeaways

- Explicitly positions itself as complementary, not a replacement, for Bandit/Semgrep/CodeQL/Vulture — it focuses on framework-aware dead-code signal, PR gating, and a combined dead-code+security+secrets+quality+AI-defect workflow in one CLI.
- Core static analysis runs fully locally with no LLM calls or cloud upload required; LLM-powered agent commands (`skylos agent scan/security-deep`, contract verification) are opt-in via the `skylos[llm]` extra.
- Deterministic AI-code hallucination checks (`skylos verify`, `.skylos/ai-contract.yml`) plus an MCP server (`verify_change`, `verify_agent` tools) let coding agents self-verify changes before human review, without executing target code for JS/TS/Python/Go.
- Framework-aware dead-code detection (FastAPI, Django, Flask, pytest, SQLAlchemy, Next.js, React) and Kubernetes/GPU-release exposure rules (e.g., flagging an externally-routed Flask debug/reload misconfiguration in a rendered manifest bundle) go beyond typical dead-code tools.
- Real-world validation: Skylos-assisted dead-code cleanup PRs merged into Black, NetworkX, Optuna, mitmproxy, pypdf, beets, and Flagsmith — accepted cleanup PRs, not project endorsements, per the project's own framing.

## Mechanical details / What to adopt

- Install: `pip install skylos` (core), `skylos[llm]` (agent workflows), `skylos[lint]` (Ruff passthrough via `skylos lint`), `skylos[all]`; also published as a Docker image (`ghcr.io/duriantaco/skylos`, Python 3.11–3.14 tags).
- CLI: `skylos .` (dead code), `skylos . -a` (full audit), `skylos . -a --diff origin/main` (changed-lines only), `skylos cicd init` (generates a GitHub Actions PR-gate workflow), `skylos init` (project config in `pyproject.toml`).
- Config discovered from `[tool.skylos]` in `pyproject.toml`, walking up from the scan path; supports baselines, whitelists, inline suppressions, custom YAML rule packs, and dead-code entrypoint annotations for framework lifecycle methods.
- 515 GitHub stars, 29 forks, 1 open / 540 closed PRs as of an August 2026 snapshot; checked-in regression benchmark suite (self-reported: dead code 100/100, security 100/100 on its own test corpus; a separate frozen "golden-v0.2" suite scores lower, e.g. Python dead-code 93.33, security 96.52) — self-reported benchmarks, not independently verified.

## Security

Apache-2.0, no restrictive license terms. Core static analysis is local-only by default (no API keys, no upload). An optional cloud-upload path exists (`skylos cicd init --upload`, "Skylos Cloud") using GitHub OIDC. LLM-backed agent commands (`skylos agent scan/test`, remote contract verification) require explicit opt-in flags (`--allow-remote`, `--allow-contract-endpoint`) and the project documents these as sending data to a configured LLM/endpoint. No CVEs or vulnerability history surfaced during this research pass; the project is relatively young/small (515 stars) — verify current maintenance activity before adopting as a CI gate.
