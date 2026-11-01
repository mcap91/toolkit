---
name: oh-my-hermes
title: Oh My Hermes (OMH)
url: "https://github.com/rlaope/oh-my-hermes"
category: framework
summary: "Operating layer for Hermes Agent — 101 installable workflow skills across six capability families (plan, build, research, code, create, operate) with deterministic routing, evidence boundaries, review-first project memory, and multi-language classification; Python-based, local-first control plane"
tags: [hermes-agent, workflow, skills, routing, evidence-gates, project-memory, multi-language, orchestration, coding-handoffs]
reviewed: 2026-08-02
acquired: 2026-08-02
overlaps: [agent-skills-addy-osmani, superpowers-brainstorming]
license: UNLICENSED
security_flags: [curl-pipe-sh-install]
source: unknown
---

## What it does

Oh My Hermes (OMH) is a professional operating layer for the Hermes Agent (by Nous Research). It packages 101 installable workflow skills behind six human-readable capability families: Clarify and plan (interviews, planning, decisions), Build with leverage (parallel work, goal tracking, team coordination), Research and learn (source-backed evidence with freshness and quality boundaries), Code and ship safely (executor-neutral coding prep, code review, QA), Create polished deliverables (websites, visuals, reports, decks, PDFs with quality gates), and Remember and operate (review-first project memory, operational observability).

OMH does not replace Hermes — it sits above individual Hermes-native skills as a governed routing and evidence layer. When a request arrives, OMH classifies it (supporting English, Korean, Japanese, Chinese, Spanish, French, German, and Hindi without a translation API), returns the recommended capability family, skill, owner, and next action, and tracks what is still unverified. Coding handoffs include repository constraints, scope, acceptance criteria, worktree guidance, and verification gates; supported executors include Codex, Claude Code, Hermes runtime, and generic executors.

Core architectural principle: three-state evidence tracking — Prepared (route/plan/prompt is ready), Observed (a runtime recorded that an action occurred), and Verified (a matching test, review, or gate passed). "Prepared" is never conflated with execution or verification.

## Mechanical details

Install via curl-pipe-sh (`curl -fsSL ... | sh` then `omh setup`) or Hermes skill tap (`hermes skills tap add rlaope/oh-my-hermes`). Update with `omh update`; health check with `omh doctor`. Python-based; tests run with `uv run python -m unittest`. Development workflow includes `compileall`, docs workflow checks, and git diff checks.

The project also maintains a documentation site at rlaope.github.io/oh-my-hermes covering architecture, capability manifests, workflow reference, roles, and application cases.

A forked variant by Salomondiei08 exists with a different skill set (36 skills, 7 agents, 6 workflows).

## Security

No license file identified in the repository — treated as UNLICENSED (all rights reserved by default). The curl-pipe-sh install pattern is a supply-chain risk surface: users execute arbitrary remote code before inspecting it. The `omh setup` command runs post-install configuration whose scope is not auditable without reading the script. Python-based with `uv` as the package manager. The project is developed in the open under "Team Art & Engineering" (@rlaope). Contributor count and release signing status are not documented.

## How to use it

curl -fsSL https://raw.githubusercontent.com/rlaope/oh-my-hermes/main/install.sh | sh && omh setup
