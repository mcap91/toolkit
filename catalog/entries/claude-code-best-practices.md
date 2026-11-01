---
name: claude-code-best-practices
title: Best Practices for Claude Code (official docs)
url: https://code.claude.com/docs/en/best-practices
category: reference
summary: "Anthropic's continuously updated Claude Code best-practices page — frames every instruction as non-deterministic (prompt, CLAUDE.md, skills: Claude decides) or deterministic (hooks, deny rules, sandbox, managed settings: the harness enforces); four failure causes map to four fixes: tell Claude what it can't see (short CLAUDE.md, path-scoped .claude/rules/, skills for team procedures), give it a pass/fail check (tests, /goal, Stop hook exiting 2, /code-review), enforce zero-exception rules in hooks/deny rules, and change defaults (auto mode, effort level, subagents, compaction) only when a task costs too much"
tags:
  - claude-code
  - best-practices
  - documentation
  - anthropic-official
  - claude-md
  - hooks
  - permissions
  - sandbox
  - effort-level
  - auto-mode
  - skills
  - verification
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps:
  - claude-howto
  - creating-claude-md
  - harness-engineering
  - scrub-context-engineering
license: proprietary
security_flags: []
source: unknown
---

## What it does

Official Claude Code documentation page describing what to configure when the defaults (auto mode, automatic subagent delegation, automatic compaction, Opus 5.5 at medium effort) are not enough. It is revised as Anthropic learns how current models behave; the page includes a "What you can stop doing" section listing advice made unnecessary by newer models.

Core framing — two kinds of instruction:

| | Non-deterministic (Claude decides) | Deterministic (Claude Code enforces) |
|---|---|---|
| What to do | Prompt, CLAUDE.md, skills | Hooks; skills only the user can start |
| What it can touch | Auto mode's classifier | Deny rules, strict sandbox, managed settings |
| When it's done | Request for evidence, `/goal`, `/code-review` | Tests, typecheck, `Stop` hook, CI |
| How much it spends | Effort level | `--max-turns`, `--max-budget-usd`, spend limits |

Four failure modes and their sections:

1. **Tell Claude what it can't see** — only write down what Claude cannot find by reading the repo or would rediscover every session. Specific prompts (name the file, symptom, definition of fixed); `be ambitious` widens scope; "think step by step" is ordinary text (effort level is the real control). Interview-first spec writing to `SPEC.md`, then build in a fresh session. Keep `CLAUDE.md` short (<200 lines; commands, misleading code, off-repo decisions, anything corrected twice); `/init`, `/doctor`, `/doctor prompt-audit` help trim it. Path-scoped rules in `.claude/rules/` with `paths:`; team procedures as skills (`disable-model-invocation: true` for side-effecting ones); CLIs or MCP for external systems.
2. **Give Claude a check to run** — anything returning pass/fail (tests, build exit code, linter, fixture diff, browser screenshot). Strictness ladder: in the prompt → `/goal` → `Stop` hook (exit 2 blocks the stop; capped at 8 consecutive blocks, `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`) → `/code-review` in a fresh subagent. Ask for evidence (command + output). Spec-review prompts should say "skip style".
3. **Enforce the rules that can't have exceptions** — hooks (`command`/`http` are deterministic; `prompt`/`agent` hooks are not; `onFailure: "block"`), permission `deny` rules (hold in every mode incl. bypassPermissions; `Read` rules catch `cat .env` but not a script opening the file), OS sandbox via `/sandbox` plus strict mode. Settings scope: local vs repo vs managed. Keep the enforced set small.
4. **Change a default** — permission modes (manual / auto / bypassPermissions), `autoMode.environment`/`allow` with `"$defaults"` kept, `/fewer-permission-prompts`; effort (`high`/`xhigh` for easy-to-overlook cases, `low` for fast iteration, `max` for unattended hard problems, `ultrathink` for one message); subagent cost awareness.

## Usage notes

- Reddit r/ClaudeCode thread (Oct 2026): the poster reports output quality improving each time they apply changes from this page and keeps a skill that re-reads it and diffs against the last read; commenters point to `/doctor prompt-audit` and `/claude-api` as built-in commands meant to be re-run periodically or after model updates, and note the page's overall direction is "less setup, fewer plugins".

## Security

Documentation page, no code. Security-relevant guidance: deny rules for secrets (`Read(./.env)`), sandbox for OS-level enforcement, auto-mode classifier is a judgment call and should not hold "never" rules.
