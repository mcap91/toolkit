---
name: openspec-plus
title: OpenSpec Plus
url: "https://github.com/sudokar/openspec-plus"
category: framework
summary: "Spec-driven engineering workflow with strict TDD, adversarial review agents, and self-fixing on failures; similar approach to SpecShip"
tags: [spec-driven, tdd, adversarial-review, autonomous-engineering]
reviewed: 2026-09-16
acquired: 2026-09-16
license: MIT
security_flags: []
overlaps: [specship]
source: unknown
---

## What it does

OpenSpec Plus is a set of agentic skills that layer onto OpenSpec's Spec-Driven Development workflow, adding structured discovery, testable requirements, design-decision capture, vertical-slice task planning, and gated execution. It works with Claude Code, OpenCode, GitHub Copilot, Cursor, and other AI coding agents that support the Skills format. It requires an existing OpenSpec project (`openspec init` must already have created an `openspec/` directory) and installs by detecting the agent environment (`.opencode/`, `.claude/`, `.cursor/`, `.antigravity/`) and copying `openspec-plus-*` skill directories into the detected skills location.

Skills cover each phase: **proposal** (brainstorming-style discovery producing a lean Why/What-Changes/Capabilities/Impact proposal, deliberately stopping short of design or implementation), **spec** (testable acceptance criteria), **design** (trade-off exploration with user-driven decisions), **tasks** (vertical-slice organization with subagent review, mandatory when OpenSpec's apply phase begins), **apply** (spec-verified, quality-gated execution per slice that escalates failures rather than bypassing them), and **tdd** (a strict red/green/refactor state machine).

## Differentiators

**Strict TDD state machine.** The `openspec-plus-tdd` skill enforces an "Iron Law" — no production code without a failing test first — via a mandatory per-test state machine (RED → VERIFY-RED → GREEN → VERIFY-GREEN → REFACTOR-ASSESS). VERIFY-RED requires confirming the test fails for the right reason (missing feature, not a typo or setup bug) before any production code is written. Every Gherkin scenario in `spec.md` must become at least one test; uncovered scenarios block slice completion.

**Subagent-isolated skill loading.** The apply phase loads skills like TDD into an isolated subagent context via the `skill` tool (or reads the skill directly if unavailable) before any code is written.

**Vertical-slice task discipline.** The tasks skill adds thinking discipline before `tasks.md` is written and a subagent review pass after, layered on top of OpenSpec's native task generation.

**Escalate-don't-bypass quality gates.** The apply phase runs a per-slice pre-mark gate (lint, format, tests on affected files) after TDD cycles complete; failures return to the failing cycle rather than being silently patched around.

**Built on OpenSpec, not standalone.** Requires an existing OpenSpec-initialized project; OpenSpec Plus is an enhancement layer (skills only), not a replacement spec-driven framework.

## Mechanical details

- **Distribution**: skills-only repo — `skills/openspec-plus-{proposal,spec,design,tasks,apply,tdd}` plus `VERSION` and `openspec/config.yaml` / `openspec/.plus/config.yaml`
- **Install**: single multi-step prompt pasted into the coding agent (verifies `openspec/` exists, detects agent environment, clones/downloads only the needed paths via `git clone --depth 1`, `gh repo clone`, or `curl`, copies `openspec-plus-*` skill directories into the detected skills path); manual CLI install also documented
- **Prerequisite**: OpenSpec must already be initialized (`openspec init`) in the target project
- **Compatible agents**: Claude Code, OpenCode, GitHub Copilot, Cursor, Windsurf/Devin, and other Skills-format-compatible agents
- **Update check**: skills read `openspec/.plus/last-update-check`; if missing or older than 7 days, they fetch the `VERSION` file from raw GitHub content and notify (notification only, no auto-install)
- **TDD state machine**: RED → VERIFY-RED → GREEN → VERIFY-GREEN → REFACTOR-ASSESS per test, gated on Gherkin scenario coverage from `spec.md`

## Security

- **License**: MIT
- **security_flags**: none identified in available documentation
- **Third-party scan**: per SkillsLLM's automated security scan (dependency vulnerability audit plus prompt-injection heuristics), openspec-plus passed with no high-severity issues found — a third-party assessment, not a first-party audit
- **Update mechanism**: version check fetches a `VERSION` file from raw.githubusercontent.com over HTTPS; it only compares versions and notifies, it does not auto-install code
