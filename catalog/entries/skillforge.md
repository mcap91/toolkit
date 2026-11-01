---
name: skillforge
title: SkillForge
url: "https://github.com/tripleyak/SkillForge"
category: meta-skill
summary: "Evidence-driven skill creator for Claude Code/Codex — RED/GREEN baseline testing (fresh agent without skill vs. with skill), cross-runtime dedup and compilation, per-skill regression evals, ecosystem doctor for trigger collisions/duplicates, opt-in friction mining from session history, proactive advisor via hooks; MIT"
tags: [meta-skill, skill-creation, testing, evals, baseline, cross-runtime, ecosystem-health, claude-code, codex, dedup]
reviewed: 2026-08-02
acquired: 2026-08-02
overlaps: [superpowers-writing-skills]
license: MIT
security_flags: []
source: unknown
---

## What it does

SkillForge is a meta-skill that routes any skill-related request (use, improve, create, compose) through an evidence-driven pipeline. Its core principle: skill quality is a property of behavior, not documents — a skill is done when a fresh agent demonstrably does better with it than without it.

The v6 pipeline (ground-up rework after external audit):

1. **Phase 0 TRIAGE**: Index + word-boundary matching routes to USE, IMPROVE, CREATE, COMPOSE, or CLARIFY. Deduplication against every skill across runtimes (personal, Codex, Claude Code plugin cache).
2. **Phase 0b RED GATE**: Fresh subagent attempts the task WITHOUT the skill. If it succeeds anyway, no skill is needed — creation stops.
3. **Phase 1 ANALYSIS**: Load-bearing lenses (Inversion, Pareto, Root Cause), failure-form matching against baseline results.
4. **Phase 2 SPEC**: Tiered specification (minimal default / full for infrastructure), decisions documented with WHY.
5. **Phase 3 GENERATE**: Fresh-context subagent receives ONLY the spec + baseline failures (no contamination from prior context).
6. **Phase 4 GREEN GATE**: With-skill runs must clear the recorded baseline failures; trigger tests verified.
7. **Phase 5 REVIEW**: Automated lint (`validate_skill.py`) + one adversarial reviewer charged to refute.
8. **Phase 6 SHIP**: Skills ship with `evals/` (trigger queries + behavioral scenarios) + `run_skill_evals.py` for permanent regression testing.

Toolbox of Python scripts (stdlib-only, Python 3.8+):
- `discover_skills.py` — build/refresh cross-runtime skill index
- `triage_skill_request.py` — route a request with JSON output
- `validate_skill.py` — full validation + lint for a skill directory
- `run_skill_evals.py` — run a skill's regression evals (optionally `--live`)
- `skillforge_doctor.py` — ecosystem health: trigger collisions, duplicates, stale refs, budget violations, pinned models
- `compile_skill.py` — cross-runtime compile (`--target claude|codex|agentskills`)
- `mine_skill_friction.py` — mine local session transcripts for skill gaps (requires `--consent`)
- `package_skill.py` — package as `.skill` archive
- GitHub Actions CI workflow template included

## Mechanical details

v6 SKILL.md is 1,158 words (down from v5's 5,049). Depth lives in `references/` loaded on demand. Skill descriptions are trigger conditions only — workflow summaries made agents skip the body. Proactive advisor delivered via Claude Code hooks (SessionStart + UserPromptSubmit), capped and opt-in. Personal context scanning strictly opt-in with recorded consent. Shared typed frontmatter parser with 100+ unit tests.

## Security

MIT licensed. No security flags. All scripts are stdlib-only Python (PyYAML optional). The friction mining feature scans local session transcripts and requires explicit `--consent` flag. The proactive advisor uses Claude Code hooks but is opt-in and never auto-invokes. No network calls, no credential handling. The install script (`install_skillforge.py`) modifies Claude Code hooks configuration interactively.

## How to use it

git clone https://github.com/tripleyak/SkillForge.git /tmp/skillforge && cp -r /tmp/skillforge ~/.claude/skills/skillforge
