---
name: daily-team
title: daily-team (rotating four-person creative agent team)
url: https://github.com/isas1/daily-team
category: skill
summary: Claude Code skill and GitHub Actions project that generates a new four-member creative team each day — `team.sh` deterministically maps the date to four personas, each with a role, working method, stance (e.g. one cuts scope, one questions the brief, one speaks for the user) and, from season 3, a temperament, plus a constraint and an open 'spark'; a model plays the team, which proposes, objects, decides, and builds one small single-file HTML tool; scripts validate it (title, mobile layout, <100KB, no network requests), screenshot it, and commit the day record; weekly seasons rotate rosters with no-repeat windows; install as ~/.claude/skills/daily-team and run `/daily-team`; MIT
tags:
  - claude-code-skill
  - personas
  - multi-agent
  - creative-ideation
  - brainstorming
  - github-actions
  - prototyping
  - html-artifacts
  - devils-advocate
  - role-rotation
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps: []
license: MIT
security_flags:
  - ci-secrets-required
  - llm-generated-artifacts-unreviewed
source: unknown
---

## What it does

Replaces fixed subagent rosters with a creative team that changes every iteration. The author's framing (r/claudeskills, Oct 2026): instead of generic sub-agents or a simulated company (CEO, PM), assemble a team of contrasting perspectives for each prototype — e.g. a "Marcus Aurelius" agent for how the idea affects people, a "Cassandra" agent for the failure nobody wants to say out loud, "the-null" for "is that metric actually telling you anything," and "the-fool" for the question everyone stopped asking — and change the team for the next project.

The repository runs this as a public daily experiment:

- `team.sh` turns the date into four members, each with a role, a method, and a stance, plus a constraint and a spark (an open starting point rather than a brief). The same date always yields the same team. Since season 3 each member also has a temperament (how they argue) and the team decides what to make.
- Rotation rules within a season: no role or method repeats within 7 days, no constraint within 22, no task within 61. A new season (8 roles, 8 methods) is drafted each Monday as a pull request; weekly summaries on Sundays.
- The team proposes, objects, decides, and builds one small tool as single-file HTML. Scripts check it (title present, mobile layout, under 100KB, no network requests, ≤80 words on component tiles), take a screenshot, and commit; failures are marked "needs review". No human reviews the output.
- Community input via GitHub polls/issues for new members and tool types.

## Mechanical details

- Skill use: clone into `~/.claude/skills/daily-team`, invoke `/daily-team` to have a team argue and decide on a plan for a brief, or build the plan as single-file HTML artifacts.
- Local run: `sh daily.sh` uses the user's Claude login.
- CI: GitHub Actions secrets `OPENROUTER_API_KEY` (free models, default) or `CLAUDE_CODE_OAUTH_TOKEN` (Claude subscription); optional `COMPONENT_REQUESTS_TOKEN`. Variables `MODEL`, `CLAUDE_MODEL` (default `claude-opus-5-5`), `ARTIFACTS` (0–4), `TZ`, `PAGES` (publish tools to GitHub Pages).
- Language: shell + JavaScript (`.mjs`) checks; ~61 stars at review.

## Usage notes

- Thread commenters describe the same practice with historical figures/artists, a "fool" and a "witch"; one rationale given is that a persona bundles a scoped context and settings (e.g. reasoning on/off, temperature, allowed tools) into something memorable. A skeptic asked what value LLMs role-playing human jobs adds.

## Security

MIT. CI requires an OpenRouter key or Claude Code OAuth token as repository secrets. Everything under `days/` is model-written and only script-checked; the README recommends browser verification before reusing a generated tool. Generated HTML is checked for no network requests.
