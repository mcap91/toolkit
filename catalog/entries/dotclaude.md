---
name: dotclaude
title: dotclaude
url: "https://github.com/poshan0126/dotclaude"
category: plugin
summary: "Turnkey .claude/ folder setup — 7 specialist agents (code/security/perf/doc reviewers, silent-failure-hunter, frontend-designer), 12 workflow skills (/ship, /pr-review, /tdd, /debug-fix, etc.), 6 modular rules, 8 safety/productivity hooks; marketplace-installable, evidence-based setup scan; MIT"
tags: [claude-code, plugin, agents, skills, hooks, workflow]
reviewed: 2026-06-22
acquired: 2026-06-22
license: MIT
security_flags: []
overlaps: [claude-spellbook, ecc-everything-claude-code]
source: unknown
---

## What it does

A complete `.claude/` configuration kit distributed as a marketplace plugin or git clone. Includes:

**7 specialist agents** (run in isolated context, auto-delegated or invoked with `@name`):
- `@code-reviewer` — correctness, off-by-one, null deref, race conditions, missing tests
- `@silent-failure-hunter` — empty catches, masked errors, floating promises, swallowed failures
- `@pr-test-analyzer` — assertion-free tests, mock theater, tests that can't fail
- `@security-reviewer` — injection, auth flaws, data exposure, crypto issues
- `@performance-reviewer` — N+1 queries, unbounded queries, memory leaks, blocking I/O
- `@frontend-designer` — anti-AI-slop UI design with design tokens and accessibility
- `@doc-reviewer` — cross-references docs against actual source code

**12 skills** (slash commands):
- `/setupdotclaude` — evidence-based install: deep-scans codebase, interviews user, proposes justified plan
- `/ship` — stage, commit, push, PR with confirmations
- `/pr-review` — parallel multi-agent review with confidence-bucketed synthesis
- `/tdd` — strict red-green-refactor loop
- `/debug-fix [--fast]` — careful debug or hotfix mode
- `/fix-issue` — GitHub issue to tested fix with regression test
- `/catchup` — rebuild context after `/clear`, write handoff notes
- `/context-budget` — estimate per-turn token cost of `.claude/` config

**8 hooks**: protect-files, warn-large-files, scan-secrets, block-dangerous-commands, format-on-save (auto-detects Prettier/Black/Ruff/Biome/rustfmt/gofmt), auto-test, session-start, notify (native OS notifications).

**6 rules**: code-quality, testing, database (path-scoped to migrations), error-handling (path-scoped to backend), security (path-scoped to API/auth), frontend (path-scoped to UI).

## Assessment

The most comprehensive single-package `.claude/` setup I've seen. The `/setupdotclaude` evidence-based installer is the standout feature — it scans the actual codebase before proposing what to install, rather than dumping everything. Re-runs detect config drift via fingerprinting.

The multi-agent `/pr-review` (parallel specialist delegation with deduplication and confidence bucketing) is well-designed. The `/context-budget` skill that estimates token cost of the config itself is a nice meta-awareness feature.

Significant overlap with our existing skills (superpowers has TDD, debugging, code review, verification) but the hook collection (especially `block-dangerous-commands`, `scan-secrets`, `format-on-save`) and the agent definitions are worth studying. The path-scoped rules pattern (rules only load when working near matched files) is a good token-saving technique.

## Mechanical details

- Install (marketplace): `/plugin marketplace add poshan0126/dotclaude` then `/plugin install setupdotclaude@dotclaude`
- Install (clone): `git clone`, copy files to `.claude/`, `chmod +x .claude/hooks/*.sh`
- Individual plugins: `/plugin install code-reviewer@dotclaude`, `/plugin install safety-hooks@dotclaude`, etc.
- Config drift detection: `.claude/.dotclaude.json` fingerprint, checked by session-start hook
- Requires: `jq` for hooks
- 20 plugins total, semver-versioned

## Security

- **License**: MIT
- **Hooks**: deterministic shell scripts — `protect-files.sh`, `scan-secrets.sh`, `block-dangerous-commands.sh` provide guardrails
- **No network calls**: everything runs locally
- **Hook testing**: `bash hooks/tests/run-all.sh` fixture-based test suite
- **CI**: GitHub Actions validates hooks on Linux+macOS + `claude plugin validate --strict`
- **format-on-save**: auto-detects installed formatters, doesn't install anything