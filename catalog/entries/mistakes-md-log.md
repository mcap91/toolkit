---
name: mistakes-md-log
title: MISTAKES.md — a self-accumulating agent error log
category: agent-pattern
summary: "Lightweight Claude Code technique: keep a MISTAKES.md in the repo plus one CLAUDE.md line ('Log mistakes in MISTAKES.md (what happened, root cause, prevention).'). Whenever the agent breaks something or is corrected, it appends an entry (what happened / root cause / consequence / the rule that prevents a repeat), newest first — no tooling, plugin, or vector store. Two reported effects: the agent starts citing and avoiding past mistakes, and a failure that recurs 4–5 times graduates from a logged mistake into a hard rule in CLAUDE.md. MISTAKES.md accumulates evidence; CLAUDE.md enforces it."
tags: [claude-code, claude-md, memory, self-improvement, error-log, workflow, agent-pattern]
reviewed: 2026-08-17
acquired: 2026-08-17
license: NOASSERTION
security_flags: []
overlaps: [creating-claude-md]
source: unknown
---
## What it says

A simple, tooling-free practice for making a coding agent learn from its own errors. Setup: a `MISTAKES.md` file in the repo and one line in `CLAUDE.md` — "Log mistakes in MISTAKES.md (what happened, root cause, prevention)." Every time the agent breaks something or the user corrects it, it appends an entry recording what happened, the root cause, the consequence, and the rule that prevents a repeat, newest first. No plugin, no vector store.

## Why it reportedly works

- **The agent reaches for it.** It begins to cite the log ("this approach was avoided because it caused XYZ before, as documented in MISTAKES.md"); over time the knowledge migrates out of the log and into behavior, so the file becomes something the agent points at rather than a diary.
- **Repeat entries graduate into hard rules.** When the same failure appears four or five times it stops being a mistake and becomes a law in `CLAUDE.md`. `MISTAKES.md` is where evidence accumulates; `CLAUDE.md` is where it gets enforced. Without the log you have a vague sense that "that area is flaky" instead of a countable pattern with a fix.

## Notes

- Complements a persistent instructions file such as `CLAUDE.md` (see [[creating-claude-md]]): the log is the evidence tier, the instructions file is the enforcement tier.
- Reusable technique, not a tool — nothing to install.

## Security

- Instructional practice only; no executable component. License N/A (recorded as NOASSERTION).
