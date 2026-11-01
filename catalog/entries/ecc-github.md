---
name: ecc-github
title: ECC — Everything Claude Code (GitHub)
url: "https://github.com/affaan-m/ecc"
category: framework
summary: massive cross-harness skill/hook/agent system worth monitoring but high adoption complexity and scope overlap with existing stack
tags: [skills, hooks, agents, rules, security, cross-harness, plugin, claude-code]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: [hook-system-broad-scope, third-party-install-scripts, pro-tier-upsell]
overlaps: [ecc-plugin]
source: unknown
---

## What it does

ECC is a large-scale agent harness performance system for Claude Code and six other AI coding tools (Codex, Cursor, OpenCode, Gemini CLI, Zed, GitHub Copilot). At v2.0.0 (June 2026) it ships 64 specialized subagents, 261 skills, 84 legacy command shims, a hook automation system (PreToolUse/PostToolUse/Stop/SessionStart/End), language-specific rules (12 ecosystems), cross-platform Node.js scripts, a Tkinter desktop dashboard, and AgentShield — a static security scanner with 1,282 tests and 102 rules that runs a red-team/blue-team/auditor Opus pipeline against your Claude Code configuration. It also provides continuous learning v2 (instinct-based pattern extraction with confidence scoring), token optimization guidance, session memory persistence, and strategic compaction tooling. Install paths: Claude Code plugin (`/plugin install ecc@ecc`), shell installer (`install.sh`/`install.ps1`), or `npx ecc-install`. Selective profiles (minimal, core, full) allow targeted installation.

## Assessment

**Watch.** ECC is the most comprehensive publicly available Claude Code enhancement system, with genuine engineering depth (cross-platform Node.js hooks, deterministic install state, 997+ internal tests, regression guards). AgentShield and the continuous learning v2 system are distinctive and potentially valuable in isolation. However, the full system is extremely large-scope and introduces significant overlap with the existing superpowers stack, kb integration, and local skills in this repo. The hook system fires broadly across all tool events and could interact unpredictably with existing hooks. The `ecc-plugin` entry already covers the plugin-hub surface; this entry supersedes that assessment with verified upstream content. Adoption should be component-scoped rather than full-install — specific skills, the AgentShield scanner, or individual agents may be worth cherry-picking.

## Mechanical details

- **Install (recommended):** `/plugin marketplace add https://github.com/affaan-m/ECC` then `/plugin install ecc@ecc`; Claude Code v2.1.0+ required
- **Selective install:** `npx ecc-install --profile minimal --target claude` excludes hook runtime; add `--modules hooks-runtime` later only if needed
- **npm package:** `ecc-universal` (OpenCode plugin integration)
- **Rules (manual):** Clone repo, copy `rules/common` + language dirs to `~/.claude/rules/ecc/`; plugin cannot distribute rules
- **AgentShield (standalone):** `npx ecc-agentshield scan` — no full ECC install required; `--opus` runs three-agent adversarial pipeline
- **Continuous learning v2:** `/instinct-status`, `/instinct-import`, `/instinct-export`, `/evolve`
- **Hook env vars:** `ECC_HOOK_PROFILE`, `ECC_DISABLED_HOOKS`, `ECC_SESSION_START_MAX_CHARS`, `ECC_AGENT_DATA_HOME` for multi-harness isolation
- **State store:** SQLite; `node scripts/ecc.js list-installed`, `doctor`, `repair` for recovery without reinstalling
- **Do not stack install methods** (plugin + full installer causes duplicates); uninstall with `node scripts/uninstall.js`

## Security

MIT license, no copyleft obligations. ECC Pro is a commercial GitHub App for private repos — OSS layer is perpetually free per README. Key security considerations:

- **Hook system broad scope:** Hooks fire on every matching tool event across all sessions. The SessionStart hook injects context (capped at 8,000 chars by default). Broad hook coverage is powerful but expands the attack surface for hook injection — mitigated by AgentShield's own hook injection analysis rules.
- **Third-party install scripts:** `install.sh`, `install.ps1`, and `npx ecc-install` write to `~/.claude/` directories. Review before running; use `--dry-run` where available.
- **AgentShield:** The `--opus` scan mode invokes three Claude Opus 4.6 API calls, incurring cost. Static analysis covers secrets detection (14 patterns), permission auditing, hook injection, MCP server risk profiling, and agent config review — genuinely useful for auditing this repo's own configuration.
- **Supply chain:** 230+ contributors, active release cadence (weekly per README), 997+ internal tests, CI enforced catalog counts and manifest validation. No signed releases noted.
- **No eval() or shell injection patterns** identified in hook architecture description; hooks delegate to Node.js scripts via adapter pattern rather than inline shell strings.
- **ECC_DISABLED_MCPS env var** is an install-time filter, not a live toggle — runtime MCP disable requires `/mcp` in Claude Code.
