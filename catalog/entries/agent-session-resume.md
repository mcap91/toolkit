---
name: agent-session-resume
title: Agent Session Resume
url: "https://github.com/hacktivist123/agent-session-resume"
category: skill
summary: "Cross-agent session resume skill with structured checkpoint workflow; overlaps with our handoff skill but adds multi-agent-platform support (Codex, Cursor, Antigravity, OpenCode)"
tags: [handoff, session-resume, cross-agent, claude-code, codex, cursor]
reviewed: 2026-06-09
acquired: 2026-06-09
license: MIT
security_flags: []
overlaps: [handoff]
source: unknown
---

## What it does

A reusable skill that gives AI coding agents a disciplined resume workflow for continuing
work from a prior session. Instead of asking the next agent to "continue from the previous
session," the skill forces it to first produce a structured handoff checkpoint containing:
the prior goal, what is done, what is still open, key decisions, the stopping point, and
the next action to take before editing. Tasks are classified as DONE, PARTIALLY DONE, or
NOT DONE.

Supports Claude Code, Codex, Cursor, Antigravity, and OpenCode. Installs via
`npx skills add hacktivist123/agent-session-resume` or as a Claude Code plugin.

## Assessment

**Note** rather than pilot or adopt. We already have a `handoff` skill in this repo that
generates self-contained handoff prompts for fresh CLI agents and subagents. This tool
solves a similar problem from the receiving side (resume) rather than the sending side
(handoff generation), and adds cross-platform agent support. Worth tracking for design
ideas — particularly the checkpoint schema and the explicit handling of user deferrals
("skip", "park", "not now") in resume context — but not needed for direct adoption given
our existing coverage.

## Mechanical details

- **SKILL.md-based**: core instructions in `skills/agent-session-resume/SKILL.md` with
  platform-specific reference docs and agent configs
- **Checkpoint schema**: prior goal, completed work, open items, key decisions, stopping
  point, next action — each classified DONE / PARTIALLY DONE / NOT DONE
- **Deferral preservation**: explicit user deferrals are carried through resume context;
  vague "proceed" prompts don't unpark deferred scope without confirmation
- **Version tracking**: resume reports identify loaded skill path and source/version marker
  (plugin manifest version, git commit, tag, or SKILL.md checksum)
- **Install**: `npx skills add hacktivist123/agent-session-resume` or Claude Code plugin
  marketplace

## Security

- **License**: MIT — no restrictions
- **Dependencies**: Python-based; repo is 100% Python per GitHub
- **Code quality**: has tests directory with fixtures and validators; scripts directory
  with validation tools; docs with cookbook and benchmarking guides
- **Supply chain**: 220 stars, 12 forks; single author (hacktivist123); 3 releases,
  latest v1.0.0 (2026-06-02); 0 open issues, 5 open PRs
- **Dangerous patterns**: none observed — skill is instruction-only (SKILL.md), no code
  execution, no eval, no shell injection vectors
- **Maintenance**: actively maintained as of June 2026