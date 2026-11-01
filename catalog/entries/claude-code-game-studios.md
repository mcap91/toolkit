---
name: claude-code-game-studios
title: Claude Code Game Studios
url: https://github.com/Donchitos/Claude-Code-Game-Studios
source_url: https://www.instagram.com/reel/De369jptIw-/
source: instagram
category: plugin
summary: Claude Code template that turns one session into a 49-agent, 74-skill simulated game studio with a three-tier director/lead/specialist hierarchy, 15 validation hooks, 14 path-scoped coding rules, and 62 document templates; ships engine-specific agent sets for Godot 4, Unity, and Unreal Engine 5; a project.yaml modes.rigor setting (minimal/standard/full) trades process weight for speed — the project's own measurement built four games from one brief and found the heavier standard-rigor build produced 30 process documents and lost a blind playtest ranking to the minimal-rigor build, which produced only a one-page brief; agents ask before acting and the user approves every write by default; MIT license.
tags:
  - claude-code
  - claude-code-plugin
  - subagents
  - multi-agent
  - game-development
  - skills
  - hooks
  - template
  - godot
  - unity
  - unreal-engine
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
---

## What it does

A git-clone template (`git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git`) that restructures a single Claude Code session into a simulated game development studio. It ships 49 subagent definitions (Markdown + YAML frontmatter) organized into three tiers — Tier 1 directors (creative-director, technical-director, producer), Tier 2 department leads (game-designer, lead-programmer, art-director, audio-director, narrative-director, qa-lead, release-manager, localization-lead), and Tier 3 specialists (gameplay-programmer, engine-programmer, ai-programmer, level-designer, ux-designer, and 19 others) — plus engine-specific lead agents for Godot 4, Unity, and Unreal Engine 5. Agents follow vertical delegation (directors delegate to leads, leads to specialists), horizontal consultation between same-tier agents, and escalation of cross-domain conflicts to a shared parent; domain boundaries keep an agent from editing files outside its own area without explicit delegation.

74 skills expose the studio's workflow as slash commands across onboarding, design, art, UX, architecture, sprint/story management, review, QA, production, release, and nine `/team-*` multi-agent orchestration commands (e.g. `/team-combat`, `/team-release`). 15 hooks validate commits, pushes, large design-doc reads, writes against stated file/registry rules, and asset JSON, plus session lifecycle and subagent audit-trail logging. 14 path-scoped rules enforce coding standards per directory (e.g. no UI references in gameplay code, zero allocations in hot-path core code, server-authoritative networking) across all three supported engines' directory layouts.

A `project.yaml` `modes.rigor` setting (minimal / standard / full) is a single front door over six underlying knobs (workflow depth, doc density, QA evidence level, story granularity, review strictness, team size) and defaults to `minimal`. The README reports its own measurement: four games built from one brief at different rigor levels were compared on documents produced before the first line of game code — minimal produced 1 (the brief, in 0 minutes), standard produced 30 (in 58 minutes) — and all four produced a running, tested game; two blind reviewers and a human playtest then ranked the standard-rigor build last, concluding the extra documents "bought traceability, not a better game."

## Mechanical details

- **Requirements**: Git, Claude Code CLI (native installer, or `npm install -g @anthropic-ai/claude-code` on Node.js 22+), Python 3 (reads `project.yaml` for every skill/hook — settings silently fall back to defaults without it), Bash, optional `jq` for hook validation.
- **Setup**: clone the repo, open Claude Code in the project root (the folder holding `CLAUDE.md` and `project.yaml` — opening in a subfolder skips hooks/deny-rules/ask-first permissions), run `/start`.
- **Collaboration model**: agents ask before proposing solutions, present 2-4 options, and wait for user approval before writing — described as "collaborative, not autonomous" by default; Claude Code's own auto mode and the template's "guided"/"autonomous" automation settings trade some of these prompts for speed.
- **Safety defaults**: hooks auto-allow read-only commands and test runs; deny rules block force-push, `rm -rf`, and reading `.env` files in both Bash and PowerShell tool calls; any screen the player would see must be launched and screenshotted into `production/qa/evidence/` before a story is considered done, at every rigor level including minimal.
- **Testing its own customizations**: a `studio-tests/` directory holds a static linter, category-specific quality rubrics, and behavioral specs for the 49 agents and 74 skills themselves (`/skill-test`, `/skill-improve`) — distinct from the game's own `tests/`.
- Platform-tested on Windows 10 (Git Bash primary), macOS, and Linux; desktop toast notifications are Windows-only (PowerShell) and a no-op elsewhere.

## Security

No elevated-privilege or unsandboxed-execution pattern observed — the template runs as ordinary Claude Code subagents, skills, and hooks operating on repo files, with explicit deny rules for destructive git/filesystem operations baked into `settings.json`. Collaborative-by-default design keeps a human approval step before writes; speed-over-confirmation is opt-in (automation settings, Claude Code auto mode), not the shipped default. MIT licensed.

## Sources

- [GitHub: Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) — README: agent/skill/hook/rule counts, hierarchy, configuration, hooks table, license
- [Instagram reel](https://www.instagram.com/reel/De369jptIw-/) — named the tool as one of five repos that "turn Claude into an entire game studio" (catalog source; no link given in the reel itself)