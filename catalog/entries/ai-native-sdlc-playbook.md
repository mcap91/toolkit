---
name: ai-native-sdlc-playbook
title: AI-Native SDLC Playbook (Anthropic)
url: "https://claude.com/blog/the-ai-native-sdlc-playbook"
category: reference
summary: "Anthropic's stage-by-stage playbook for AI-native software development — six-stage loop (Plan→Design→Build→Test→Deploy→Maintain) where each stage commits a version-controlled artifact triggering the next; covers CLAUDE.md as institutional knowledge, skills/hooks as guardrails, plan mode before implementation, agentic review with human gates, and production monitoring feeding back into intent; Claude Code-centric"
tags: [sdlc, claude-code, anthropic, planning, skills, hooks, software-engineering, agent-workflow, governance]
reviewed: 2026-09-29
acquired: 2026-09-29
overlaps: []
license: ""
security_flags: []
source: unknown
---

## What it says

Anthropic's published playbook (August 2026, by Louis Claxton) for restructuring the software development lifecycle around AI agents. Core thesis: code generation is no longer the bottleneck — planning, review, testing, and deployment still run at human speed, so those stages need the same transformation the build phase got.

Six stages, run as a loop where each stage commits a file that starts the next:

1. **Plan**: idea becomes `intent.md` in hours, not weeks of meetings.
2. **Design**: Claude writes `spec.md` with company skills loaded; conflicts flagged early.
3. **Build**: plan mode first (read, don't touch); `CLAUDE.md` holds team rules; 1 engineer runs 3 sessions.
4. **Test**: Claude checks its own work; a hook stops it editing tests to game pass rates.
5. **Deploy**: Claude reviews every PR but never approves its own; prod waits for a release manager.
6. **Maintain**: a 3 AM spike triggers a script that calls Claude, which writes a new `intent.md`, restarting the loop.

Each stage includes prerequisites, infrastructure needs, execution steps, governance considerations, and leading/lagging indicators.

## Guardrails architecture

- **Skills** make mistakes rare (structured prompts for recurring tasks).
- **Hooks** make mistakes close to impossible (pre/post-commit checks, test-editing prevention).
- Continuous evals on `CLAUDE.md`, skills, and hooks.
- Claude Tag on-call in Slack for incident response.
- Scheduled security scans via Claude Code Security.
- Managed settings + sandboxing for regulated teams.

## Companion materials

- Security companion post (July 2026, Jason Clinton, Deputy CISO): how Security Engineering secures an SDLC where AI authors 80% of merged code.
- Claude Academy course: 14 lessons, ~1 hour.
- Community implementations: multiple GitHub repos scaffolding the playbook as Claude Code plugins with approval gates.

## Security

Reference entry — no installable artifact. The playbook itself addresses security governance extensively: human approval gates at every handoff, hooks preventing self-approval, separation of review and authorship, scheduled vulnerability scanning.