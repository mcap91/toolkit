---
name: fable-agent-orchestration
title: Fable Agent Orchestration
url: "https://git.wearein.space/elias/fable-agent-orchestration"
category: plugin
summary: "Apache-2.0 skill database for multi-agent orchestration — 24 reusable skills covering worktree-isolated parallel PR workflows, two-critic review loops, agent PR validation against real diffs/CI, fake-green test detection, orphaned WIP recovery, instruction-drift control, behavior-contract harnesses, and phase-aware engineering ladders"
tags: [agent-orchestration, skills, multi-agent, code-review, worktree-isolation, pr-validation]
reviewed: 2026-07-06
acquired: 2026-07-06
license: Apache-2.0
security_flags: []
overlaps: [architect-loop, agent-skills-addy-osmani, dotclaude]
source: unknown
---

## What it does

A public-clean skill database for Fable-style agent orchestration. Provides 24 reusable SKILL.md files implementing a conductor/worker model: a lead agent splits work into independent slices, launches build agents in isolated git worktrees, tracks workers in a parent registry, requires PR-based output, runs dual-critic review, and merges on green evidence.

**Core loop:** split → launch per-slice agents in worktrees → dispatch packets (role/scope/invariant/proof-gate/output-contract) → track in registry → require PR (not merge) → two-critic review (test critic + code critic) → verify claims against diff and CI → merge one at a time on green → relaunch next slice → never stop while reversible work remains.

## Differentiators

- **24 skills** covering the full orchestration lifecycle: fable-orchestrator, autonomous-finish-loop, think-work-try, one-slice-worker-cycle, two-critic-review-loop, agent-pr-validator, adversarial-reviewer, task-relative-test-gate, review-verifier, orphaned-wip-adopter, agent-dispatch-packet, peer-review-packet, fable-session-skill-miner, external-workflow-adapter, contributor-evidence-gate, instruction-drift-control, behavior-contract-harness, phase-aware-engineering-ladder, investigate-before-fix, long-run-continuity, easy-vs-right-check, periodic-retrospect, seal-both-types
- **Two-critic review** — separates test review from code review into distinct critic roles
- **Agent PR validator** — compares agent claims to the actual diff and CI results
- **Task-relative test gate** — detects fake-green tests (tests that pass but don't actually verify the change)
- **Orphaned WIP adopter** — recovers and reuses abandoned agent work instead of rebuilding
- **Session skill miner** — extracts reusable procedures from agent sessions without leaking raw logs
- **Instruction-drift control** — keeps canonical agent guides in sync, detects stale instructions
- **Behavior-contract harness** — turns style/behavior claims into measurable contracts with eval probes
- **Phase-aware engineering ladder** — scales verification depth by project phase while maintaining a security/data-loss floor
- **Delegation rule of thumb:** "Spawn an agent only when you will immediately go do something else"

## Mechanical details / What to adopt

- **Install (compact):** copy root `SKILL.md` into `~/.claude/skills/fable/SKILL.md`
- **Install (modular):** copy individual `skills/*/SKILL.md` folders
- **Structure:** `catalog.json` machine-readable index, `schemas/skill-record.schema.json` for catalog entries, individual skill folders
- Clean-public boundary explicitly documented: excludes private formulas, identities, memory systems, third-party source dumps, raw transcripts, secrets
- Credits three upstream inspirations (agent-standard-oss MIT, opus-fable-playbook MIT, senior-engineering-partner Apache-2.0) — all rewritten, no vendored code

## Security

Apache-2.0 licensed. No vendored third-party code. No dependencies, credentials, or network calls — pure SKILL.md markdown files. Hosted on a self-hosted Gitea instance (git.wearein.space), not GitHub.