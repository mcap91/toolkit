---
name: finding-unknowns-skills
title: Finding Unknowns Skills
url: "https://github.com/Neeeophytee/finding-unknowns-skills"
category: skill
summary: "8 installable SKILL.md skills distilled (with attribution) from Thariq Shihipar's essay on finding your unknowns — blindspot-pass, brainstorm-prototypes, interview-me, reference-hunt, implementation-plan (before), implementation-notes (during), pitch-packager and change-quiz (after); each keys its trigger on the situation and the essay's literal phrases; MIT, cross-agent (Claude Code / Codex / any agentskills.io reader)"
tags: [skills, claude-code, codex, planning, unknowns, prompt-clarification, multi-platform, community]
reviewed: 2026-07-09
acquired: 2026-07-09
license: MIT
security_flags: [single-maintainer, community-distillation]
overlaps: [agent-skills-spec, skills-cli]
source: unknown
---

## What it is

A community project (MIT, explicitly not an official Anthropic repository) packaging eight installable skills that operationalize Thariq Shihipar's (Anthropic, Claude Code team) essay "A Field Guide to Fable: Finding Your Unknowns." The framing: your prompt is a map, the codebase and world are the territory, and the gap is your unknowns; each skill is a cheap way to move an unknown out of the "unknown unknown" quadrant before implementation makes it expensive. Skills use the agentskills.io SKILL.md format and run in Claude Code, OpenAI Codex, or any agent that reads that format.

## The eight skills

Before implementation: `blindspot-pass` (surface unknown unknowns in an unfamiliar area, then rewrite your prompt), `brainstorm-prototypes` (3–5 throwaway variations, each labeled with the belief it bets on), `interview-me` (one question at a time, architecture-changing questions first, never asks what the codebase can answer), `reference-hunt` (use working source as the spec, write a semantics summary before reimplementing, even across languages), `implementation-plan` (leads with the decisions most likely to change). During: `implementation-notes` (log every deviation, take the reversible option). After: `pitch-packager` (demo-first buy-in doc) and `change-quiz` (a comprehension quiz to pass before merge). The author notes each description keys on both the situation and the essay's literal phrases so skills fire when wanted and stay quiet otherwise, and that all eight combined are ~537 always-on tokens (~400 each on invoke) per the plugin details.

## Install

`npx skills add Neeeophytee/finding-unknowns-skills` (Vercel skills CLI, auto-detects Claude Code / Cursor / Codex / Copilot / Gemini); or as a Claude Code plugin (`/plugin marketplace add Neeeophytee/finding-unknowns-skills` then `/plugin install finding-unknowns@finding-unknowns-skills`); or copy any `skills/<name>/` folder into `.claude/skills/` (or `~/.agents/skills/` for Codex). A one-file `CLAUDE.md`/`AGENTS.md` provides the same approach as passive guidance; `EXAMPLES.md` has ready-to-paste prompts. The README reports testing against Codex CLI v0.143 (all 8 load, verifiable with `codex debug prompt-input`).

## Security

MIT-licensed skill text; the techniques are attributed to Thariq Shihipar's public essay. The skills are prompt/instruction text (no scripts), installed into your agent's skill directory — the usual consideration is that installed skills add model-visible instructions that fire on their triggers. Community project maintained by a single author; installation pulls from a third-party GitHub repo or via npx.

## Usage notes

- Pack expanded from 8 to 11 skills (as of late July 2026). Three new skills from Thariq Shihipar's second essay on context engineering for Claude 5 models: **context-audit** (reads all instruction layers as the model receives them, sorts into conflict/duplicate/obvious/model-handles-this-now/real-gotcha, outputs a cut list as a diff), **agent-interface-design** (for building tools/MCP servers/scripts an agent calls — design parameters instead of usage examples, since examples constrain newer models to shown paths), **progressive-disclosure** (splits oversized skills/specs into entry file plus conditionally-loaded files; user-invoked only in Claude Code, but Codex CLI v0.143.0 ignores disable-model-invocation and loads it unconditionally).
