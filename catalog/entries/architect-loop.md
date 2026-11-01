---
name: architect-loop
title: Architect Loop
url: "https://github.com/DanMcInerney/architect-loop"
category: agent-pattern
summary: "Research-backed cross-vendor agent loop with strong separation of concerns; excellent design patterns for gated, worktree-isolated multi-agent builds"
tags: [multi-agent, cross-vendor, claude-code-skill, codex, worktree-isolation, gates, research, orchestration]
reviewed: 2026-06-16
acquired: 2026-06-16
license: MIT
security_flags: []
overlaps: [claude-agent-teams, scheduled-multi-agent-coordinator]
source: unknown
---

## What it does

Two Claude Code skills that wire Claude Fable (architect/planner/reviewer) with GPT-5.5 Codex CLI (builder/researcher) into a repo-centered loop. Runs on existing subscriptions — no API keys required.

**`/architect`** — the build loop. One work block per invocation:
1. **Spec + gates first.** Fable specs a one-PR slice, splits into 1–4 lanes with non-overlapping file sets, commits acceptance gates to `docs/gates/` before builders start. Gates are read-only — builder edits auto-fail the slice.
2. **Parallel isolated builders.** One fresh `codex exec` per lane in its own git worktree. Builders must argue with the spec before building (silent compliance = defect), build only declared files, and report raw results. No commit access in sandbox.
3. **Fable judges and integrates.** Runs gate commands itself (builder claims are "hearsay"), reads the diff against spec intent (passing tests ≠ mergeable), commits and merges passing lanes in a fresh context.

**`/architect-research`** — the research loop. Scout-first design:
1. Cheap Codex scout maps the topic (~10 searches)
2. Fable designs 3–6 topic-specific lanes from the scout map, drawing tactics per source class (academic snowballing, dependents-not-stars evidence, hype gating, expert tracking)
3. Parallel Codex researchers run under hard budgets with strict findings discipline (URL + date + quote + confidence tag; NOT FOUND beats inference)
4. Fable verifies (≥2 sources per claim, adversarial falsification) and writes one decision-oriented report

Repo is the only memory: `docs/HANDOFF.md` (pruned each session), `docs/gates/`, `docs/lanes/`, git history.

## Assessment

**Pilot.** This is one of the most thoughtfully designed multi-agent orchestration patterns in the catalog:

- **Research-backed design** — every choice is cited in DESIGN.md with a failure-mode table; not heuristics but observed evidence
- **Strong security model** — frozen external gates, worktree isolation, no builder commit access, architect verifies directly rather than trusting builder claims
- **Anti-gaming measures** — builders must argue with specs (silent compliance = defect), passing tests ≠ mergeable (architect reads the diff), builder gate edits auto-fail
- **Practical** — 30-second install, Windows support (install.ps1), works on existing subscriptions
- **Clean separation** — architect never writes code, builders never judge quality

The main caveats:
- Requires both Claude Code (paid plan) and Codex CLI (ChatGPT plan) subscriptions
- Tied to specific model versions (Fable, GPT-5.5 Codex) which will evolve
- Builder runs consume meaningful ChatGPT weekly quotas
- Young project — limited community validation beyond the design doc

The design patterns (frozen gates, fresh-context review, "builder claims are hearsay") are worth studying even without adopting the full system.

## Mechanical details

**Install:** `git clone` + `./install.sh` (or `./install.ps1` on Windows) + `npm i -g @openai/codex@latest`. `--project` flag installs to current repo only instead of globally.

**File structure:**
- `DESIGN.md` — 12 enforced rules, failure-mode table, cited sources
- `skills/architect/SKILL.md` — architect role rules + procedure
- `skills/architect/dispatch.md` — verified codex exec commands, worktree fan-out, stall triage
- `skills/architect/research.md` — slice-scale inline fact-check fan-out
- `skills/architect-research/SKILL.md` — research orchestration procedure
- `skills/architect-research/lanes.md` — scout block + source-class tactics library
- `tests/validate_skills.py` — repo sanity checks

**Key design rules to adopt:**
1. Weak planners hurt more than weak executors — put the stronger model on design
2. Frozen external gates beat trusting the agent
3. Manager + worktree-isolated workers is well-supported for shared-artifact work
4. Memory files rot — keep handoffs as short maps with detail in linked files
5. Research lanes should be designed per-topic after a scout pass, not fixed taxonomies
6. Gathering parallelizes; synthesis never does

## Security

- **License:** MIT — permissive, no restrictions
- **Dependencies:** Minimal — Claude Code skills are just Markdown files; only runtime dep is Codex CLI (npm package)
- **Code quality:** Tests exist (`validate_skills.py`), design document with failure-mode analysis
- **Dangerous patterns:** Dispatches `codex exec` child processes — but in worktree-isolated sandboxes with no commit access; architect runs verification commands directly rather than trusting builder output
- **Supply chain:** Single author (DanMcInerney), early project, no signed releases
- **Supervision:** Built-in liveness checks on dispatched runs, stall triage (diagnose child process tree, kill narrowest thing), explicit timeouts on long commands
- **security_flags:** Clean — the security model is a distinguishing strength of this project