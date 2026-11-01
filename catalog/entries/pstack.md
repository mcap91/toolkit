---
name: pstack
title: pstack (Cursor Plugin)
url: https://github.com/cursor/plugins/tree/main/pstack
source_url: https://www.instagram.com/reel/DePGBFXtswr/
source: instagram
category: plugin
summary: "Cursor plugin by Lauren Tan (poteto, React core team) packaging her own engineering discipline as agent workflows: 23 task playbooks (bug fix, perf, feature, refactor, investigation, shipping, autopilot-full/stack, etc.) routed by a single /poteto-mode entry point, 24 one-rule-each engineering principles (prove-it-works, fix-root-causes, boundary-discipline, guard-the-context-window, etc.) indexed inline at task start, situational sub-skills (/architect, /blast-radius, /interrogate, /arena, /swarm, /unslop, /no-comments, /tdd, /correct, /create-verification-skill and others), and two subagent types (poteto-agent, Comment Sicko). Explicit goal is less code at higher quality, not throughput. Installs as a Cursor or Claude Code plugin (/plugin install pstack@cursor-plugins); MIT; several community ports exist for Codex, Pi, OpenCode, and other hosts."
tags:
  - cursor
  - claude-code
  - plugin
  - agent-workflow
  - engineering-principles
  - playbooks
  - code-quality
  - mcp
  - open-source
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT
security_flags: []
overlaps:
  - ponytail
  - unslop-skills
  - thermos
---

## What it does

A Cursor plugin encoding one engineer's (Lauren Tan, "poteto" — React core team, prior work at Meta/Netflix) daily workflow for shipping high-quality agent-written code, released publicly so others can fork and adapt it ("make it yours").

**Entry point:** `/poteto-mode` reads the task, matches it to one of 23 playbooks (investigation, bug fix, perf, hillclimb, runtime/trace forensics, feature, refactoring, prototype, visual parity, authoring a skill, eval, babysit, shipping, autonomous run, orchestrate, autopilot-full, autopilot-stack, session pickup, pause safely, multi-phase plan, worktree cleanup, opening a PR), opens a todo list copied verbatim from the playbook's steps, and routes to other skills as those steps require them.

**Principles (24, one rule each):** grouped as core (e.g. `laziness-protocol` — bias toward deletion and the smallest change; `subtract-before-you-add`), architecture (`boundary-discipline`, `type-system-discipline` — make illegal states unrepresentable), verification (`prove-it-works` — verify against the real artifact, not a proxy or "it compiles"; `fix-root-causes`; `test-behavior-not-implementation`), delegation (`guard-the-context-window` — route bulk work to subagents, keep summaries in the main thread; `never-block-on-the-human`), and meta (`encode-lessons-in-structure` — turn a corrected mistake into a lint/check/script, not more prose).

**Situational skills invoked directly or by a playbook:** `/architect` (settle caller usage/types before crossing a function boundary), `/blast-radius` (prove what a small change could break by running code), `/arena` (N parallel attempts, keep the best parts), `/swarm` (N parallel workers across slices, one aggregated report), `/interrogate` (multiple models try to break a diff, keep only run-proven findings), `/unslop` (remove AI prose tells), `/no-comments` (strip comments, spawn a review subagent called "Comment Sicko" on what's left), `/tdd`, `/correct` (mine history for repeated mistake classes and fix each at the highest leverage level), `/create-verification-skill` / `/create-formal-verification-skill` (generate a project-local verification skill when none exists), `/typescript-best-practices`, `/technical-writing` (Diátaxis + Google style + STE + Global English for docs/RFCs/commit messages), `/automate-me` (mine the operator's own transcripts to draft a personalized routing skill on top of pstack).

**Subagents:** `poteto-agent` (the wrapper used for delegated work inside a run — must read the full `poteto-mode` skill and its principles index first; substituting a generic subagent type causes drift) and `comment-sicko` (read-only comment reviewer, normally invoked via `/no-comments`).

**Explicit non-goal:** no dedicated planning skill is bundled — the author's position is "the best spec is code," relying on Cursor's existing plan mode when planning is wanted.

**Install:** `/add-plugin pstack`, or in Claude Code: `/plugin marketplace add cursor/plugins` then `/plugin install pstack@cursor-plugins` (commands are namespaced `/pstack:poteto-mode`, etc.; cursor-only steps like BugBot are skipped with a note). `/setup-pstack` maps model roles (code vs. judgment vs. review panels) to specific models per operator preference. Companion plugins `cursor-team-kit` (ships `/deslop`, `control-cli`, `control-ui`) and a dormant `benny` Slack-triage automation pack (Cursor-only) are referenced but not bundled.

## Sources

- [cursor/plugins/pstack — README](https://github.com/cursor/plugins/tree/main/pstack) — full playbook/principle/skill list, install steps, author's own framing (fetched directly).
- [A deep dive into pstack — daily.dev](https://daily.dev/posts/a-deep-dive-into-pstack-evqbnto9j)

## Security

MIT. Lives inside Cursor's own official `cursor/plugins` monorepo (not a third-party fork) alongside dozens of other first-party Cursor plugins — distribution/provenance risk is low relative to a single-maintainer community skill. Several of its own principles are explicit security/correctness disciplines (`boundary-discipline`: concentrate input validation at system boundaries; `prove-it-works`: verify against the real artifact rather than trusting a green build). No dangerous runtime components identified — it is prompt/skill content plus playbook routing logic, not a service with its own network surface.
