---
name: claude-skills-rezvani
title: Claude Skills (Rezvani)
url: "https://github.com/alirezarezvani/claude-skills"
category: plugin
summary: "355-skill library for 13 AI coding tools — 18 domains (engineering, marketing, product, compliance, C-level advisory, research, finance, business ops), 602 stdlib-only Python CLI tools, 711 reference templates; cross-platform (Claude Code, Codex, Gemini CLI, Cursor, Aider, Windsurf, and 7 more); MIT"
tags: [claude-code-plugin, skills-library, multi-platform, engineering, marketing, compliance, research]
reviewed: 2026-07-06
acquired: 2026-07-06
license: MIT
security_flags: []
overlaps: [agent-skills-addy-osmani, dotclaude, claude-spellbook]
source: unknown
---

## What it does

Comprehensive skill library providing 355 skills across 18 domains for 13 AI coding tools. Each skill includes a SKILL.md, optional Python CLI tools (602 total, all stdlib-only), and reference documents (711 templates/checklists).

**Domains:** Engineering Core (52), Engineering POWERFUL (81), Product (17), Marketing (48), Productivity (7), Research Academic (9), Research Operations (5), Project Management (9), Regulatory & QM (19), Compliance OS (9), C-Level Advisory (68), Business & Growth (5), Business Operations (7), Commercial (8), Finance (4), Loop Library (1), Markdown → HTML (5), Landing (1).

**Supported tools:** Claude Code, OpenAI Codex, Gemini CLI, OpenClaw, Hermes Agent, Mistral Vibe, Cursor, Aider, Windsurf, Kilo Code, OpenCode, Augment, Antigravity. Conversion script (`scripts/convert.sh --tool all`) generates native formats for each.

## Differentiators

- **Scale** — 355 skills is the largest single-source skill library cataloged; 5,200+ GitHub stars
- **18 domains** — extends well beyond engineering into marketing (AEO/SEO), C-suite advisory, regulatory (ISO 13485, MDR, FDA, GDPR, SOC 2), academic research, and enterprise research ops
- **POWERFUL tier** — 81 advanced skills including agent-designer, RAG architect, zero-hallucination-coder, agent-harness, security-guidance PreToolUse hook
- **Skill security auditor** — Python script that scans skills for command injection, code execution, data exfiltration, prompt injection, and supply-chain risks before installation
- **Personas** — pre-configured agent identities (Startup CTO, Growth Marketer, Solo Founder) with curated skill loadouts
- **Orchestration protocol** — four patterns (Solo Sprint, Domain Deep-Dive, Multi-Agent Handoff, Skill Chain) for coordinating personas and skills
- **All Python tools are stdlib-only** — zero pip installs, verified to run with `--help`

## Mechanical details / What to adopt

- **Install (Claude Code):** `/plugin marketplace add alirezarezvani/claude-skills` → `/plugin install <bundle>@claude-code-skills`
- **Install (Codex):** `npx agent-skills-cli add alirezarezvani/claude-skills --agent codex`
- **Install (manual):** clone repo, copy skill folders to `~/.claude/skills/` or equivalent
- **Cross-tool conversion:** `./scripts/convert.sh --tool all` generates Cursor `.mdc` rules, Aider `CONVENTIONS.md`, Windsurf/OpenCode/Augment/Antigravity native formats
- Notable individual skills: `skill-security-auditor` (scan skills for malicious code), `self-improving-agent` (auto-memory curation), `playwright-pro` (test gen/flaky fix), `named-persona-adversarial-review`

## Security

MIT licensed. All 602 Python tools are stdlib-only with zero external dependencies. Includes a built-in skill security auditor for scanning third-party skills. 5,200+ stars, active maintenance. Single primary contributor (Alireza Rezvani). `scripts/check.py` lints manifests and verifies cross-file references before push.