---
name: specship
title: SpecShip
url: "https://github.com/aws-samples/sample-specship"
category: framework
summary: "AWS spec-driven autonomous engineering framework (Kiro Power) — brownfield recon, contract-first markdown specs, strict TDD gates, adversarial parallel validation with up to 7 subagents, and self-healing fix agents"
tags: [spec-driven, tdd, adversarial-review, kiro, autonomous-engineering, aws]
reviewed: 2026-09-16
acquired: 2026-09-16
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

SpecShip is an AWS sample project packaged as a Kiro Power that orchestrates AI coding agents through a five-stage pipeline: recon → plan → build → validate → ship. For brownfield work, the recon stage reverse-engineers the existing repository — architecture, technology stack, APIs, data models, business flows, local conventions, baseline tests, and change impact — before any change is planned. The plan stage produces a sprint contract (acceptance criteria, failure modes, design spec, API contract) plus pre-written failing tests. The build stage runs iterative milestone loops under Test-Driven Development (red → green → refactor); a hard gate blocks each milestone until typecheck, tests, and build all pass. The validate stage runs up to 7 independent adversarial validator subagents in parallel — the agent that built the code does not judge it. The ship stage generates pull requests, changelogs, and archives the contract.

Mission artifacts (recon docs, sprint contract, tests, validator verdicts, changelog) live under `.specship/specs/<id>/` in the target repo.

## Differentiators

**Brownfield recon before planning.** Existing-codebase analysis (architecture, stack, APIs, data models, conventions, baseline tests, change impact) runs before any spec is written, rather than assuming a greenfield start.

**Contract-first specs.** Requirements, design, and tasks are captured as explicit markdown artifacts (sprint contract with acceptance criteria, failure modes, design spec, API contract) before build starts.

**Hard TDD gate.** No production code without a failing test first (red → verify-red → green → verify-green → refactor); a milestone gate blocks progress until typecheck, tests, and build all pass.

**Adversarial parallel validation.** Up to 7 independent validator subagents run in parallel and return typed, evidence-backed verdicts — separate specializations for code review, security (CSO), integration testing, browser/QA, design validation, alignment (always runs), and load testing (when performance requirements exist). The builder agent does not self-judge.

**Self-healing fixes.** When a validator finds a bug, a fresh agent applies one surgical, regression-test-first fix per issue, budget-bounded, with parallel fixes when touching different files.

## Mechanical details

- **Packaging**: distributed as a Kiro Power (`kiro-power-specship/` with `power.json` manifest, `POWER.md` docs, `PREREQUISITES.md`, `SECURITY.md`, `install.sh`/`uninstall.sh`, `specship-verify.sh` integrity verifier, hooks/, templates/, docs/, steering/)
- **Install**: `./install.sh` — detects dependencies, copies steering files to `~/.kiro/steering/`, auto-configures Playwright MCP
- **Required companion skill packs**: `superpowers` (brainstorming, writing-plans, subagent-dev, tdd, debugging) and `gstack` (review, cso, qa-only read-only validators) — SpecShip sequences and delegates to these rather than reimplementing them
- **Validator sub-skills**: `specship-validate-{code,security,integration,browser,design,alignment,load}` plus an aggregate step
- **Recovery skill**: `specship-recover` — surgical, regression-test-first fixes
- **Dependencies**: Node.js, Playwright MCP (auto-configured if missing)
- **Artifacts**: stored under `.specship/specs/<id>/` in the consuming repo

## Security

- **License**: MIT
- **security_flags**: none identified — the project's own documentation carries an explicit disclaimer that it is "experimental and unofficial... has not undergone external security review" and that all generated code is sample/reference implementation requiring AppSec review before production use
- **Integrity verification**: ships a `specship-verify.sh` script to check installed-power integrity
- **Guardrails**: README documents a "no-unauthorized-push" guardrail and a two-stage review during the build phase
