---
name: andrej-karpathy-skills
title: Andrej Karpathy Skills (multica-ai)
url: "https://github.com/multica-ai/andrej-karpathy-skills"
category: plugin
summary: "CLAUDE.md + Cursor rules implementing 4 of Karpathy's coding principles (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution); Claude Code marketplace plugin + .cursor/rules/.mdc format; overlaps with karpathy-12-rules (covers 4 of 12)"
tags: [claude-md, cursor-rules, best-practices, karpathy, claude-code-plugin]
reviewed: 2026-07-06
acquired: 2026-07-06
license: MIT
security_flags: []
overlaps: [karpathy-12-rules]
source: unknown
---

## What it is

A single CLAUDE.md file derived from Andrej Karpathy's observations on LLM coding pitfalls, packaged as a Claude Code marketplace plugin. Also ships a `.cursor/rules/karpathy-guidelines.mdc` for Cursor and an `AGENTS.md` reference. Four principles: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. By multica-ai (Jiayuan).

## Assessment

Strict subset of what we already have. Our `setup-behavioral-baseline.sh` covers all 4 of these principles (as rules 1–4 of the Karpathy 12) plus 8 additional rules (LLM/deterministic boundary, token budgets, surface conflicts, read-before-write, intent-based tests, checkpointing, match conventions, fail loud), the Fable-Mode disposition governor (8 rules for Opus self-audit pathology), a UserPromptSubmit re-injection hook, and `leak_test.py` for quantitative convergence measurement.

The upstream repo also ships a `.cursor/rules/karpathy-guidelines.mdc` (Cursor) and an `AGENTS.md` (Codex) carrying the same four principles — packaging variants, not new content.

## What to adopt

Nothing — the content is a subset of what we already run. Codex parity in our own stack was handled separately by extending `setup-behavioral-baseline.sh` to install the Karpathy 12 to `~/.codex/AGENTS.md`; Cursor is not a target for us.

## Security

Reference document and CLAUDE.md text only. No executable code, dependencies, or network calls. MIT licensed. No supply-chain risk.