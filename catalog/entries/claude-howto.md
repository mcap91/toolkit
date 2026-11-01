---
name: claude-howto
title: Claude Howto
url: "https://github.com/luongnv89/claude-howto"
category: reference
summary: "Well-structured tutorial guide with copy-paste templates, but it is a learning reference rather than an installable tool."
tags: [claude-code, tutorial, learning-path, slash-commands, skills, hooks, mcp, subagents, templates]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: []
overlaps: [awesome-claude-code, claude-spellbook]
source: unknown
---

## What it does

A visual, example-driven tutorial guide for Claude Code structured as 10 progressive modules: slash commands, memory, checkpoints, CLI basics, skills, hooks, MCP, subagents, advanced features, and plugins. Each module includes Mermaid architecture diagrams, production-ready copy-paste templates (CLAUDE.md stubs, hook scripts, subagent definitions, MCP config files), and a self-assessment quiz runnable via `/self-assessment` or `/lesson-quiz [topic]` inside Claude Code. A guided learning path runs beginner to advanced in 11–13 hours. Maintained in sync with Claude Code releases (latest v2.1.160, June 2026). Multilingual: English, Vietnamese, Chinese, Ukrainian, Japanese. Also ships an EPUB generator (`uv run scripts/build_epub.py`) for offline reading.

## Assessment

The guide is genuinely well-crafted and above average for a community reference: it has real CI (pytest, ruff, bandit, mypy), a CONTRIBUTING.md, a SECURITY.md with private-disclosure instructions, and active maintenance cadence. The self-assessment hook is a useful touch. However, the catalog already records the individual features this guide teaches (skills, hooks, subagents, MCP patterns), and the templates are generic enough that a practitioner following those catalog entries will naturally arrive at the same configurations. It belongs in the catalog as a discoverable onboarding resource for newcomers to Claude Code, not as something to adopt or pilot for production use.

## Mechanical details

- Clone and copy individual templates: `cp 01-slash-commands/*.md .claude/commands/`
- Skills land in `~/.claude/skills/` or `<project>/.claude/skills/`
- Subagent definitions go in `.claude/agents/`
- Hook scripts go in `~/.claude/hooks/` with `chmod +x`
- MCP configs drop into `.mcp.json` via `claude mcp add`
- EPUB: `uv run scripts/build_epub.py` — requires `uv` and Python 3.10+
- Tests: `pytest scripts/tests/ -v`; quality: `ruff check`; security: `bandit -c pyproject.toml -r scripts/`
- No npm/node runtime required for the docs themselves

## Security

MIT license — permissive, no copyleft obligations. The repo itself is documentation and shell-script templates, not a running service. Shell hook examples (e.g. `format-code.sh`, `security-scan.sh`) should be reviewed before installation — they are templates, not audited scripts. No credential handling or eval-like patterns are visible in the README. CI includes Bandit (Python security scanner) and mypy, which is a positive signal for the scripting layer. No signed releases. Supply chain risk is low given it is a docs/templates repository with no package registry presence.
