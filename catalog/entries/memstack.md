---
name: memstack
title: MemStack
url: "https://github.com/cwinvestments/memstack"
category: framework
summary: "Free-tier skill library is substantial but the PyPI MCP loader performs opaque license checks and stores credentials in-process, warranting supply-chain caution before adoption"
tags: [skills, memory, sqlite, hooks, tts, mcp-server, freemium, skill-loader, claude-code, meta-skill]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: [no-tests-evident, license-check-network-call, credential-stored-by-process, single-org-contributor, opaque-pypi-loader, freemium-gating]
overlaps: [claude-spellbook, one-skill-to-rule-them-all, bmad-skill-forge]
source: unknown
---

## What it does

MemStack is a commercial freemium skill framework for Claude Code that distributes 127 SKILL.md-style skills via a Python MCP server installed from PyPI (`memstack-skill-loader`). Skills are organized into domains: Core/Memory, Security, Deployment, Development, Business, Content, SEO, Marketing, Product, and Automation. They load on-demand at runtime — only the skill matching the current task is injected, avoiding context bloat.

The free tier includes 84 skills plus: SQLite-backed persistent session memory with semantic vector search, deterministic hooks (commit safety, secret scanning, build verification), TTS voice notifications, TokenStack™ context compression, and a localhost dashboard (port 3333) for skill management, token analytics, and 3-agent orchestration with real-time streaming.

The Pro tier (paid license via memstack.pro) unlocks 43 additional skills including multi-agent orchestration, browser automation, RAG builder, model router, advanced security, and various platform-specific skills (iOS App Store, Next.js conventions, etc.).

## Assessment

The free skill library is genuinely broad and the on-demand loading architecture is sound — loading a single matched skill rather than dumping all 127 into context is the right pattern. Some individual skills (diary, echo, governor, scan) address real workflow needs.

However, the delivery mechanism introduces risks that outweigh immediate adoption:

1. **Opaque PyPI loader**: The `memstack-skill-loader` package is the gating layer for all skill access. Its behavior — what it sends to servers, what it reads from the filesystem — is not auditable from the README alone.
2. **License-check network call**: Pro activation stores a key permanently via `activate_license()` and the README implies the MCP server validates it at runtime, meaning the process makes outbound calls to memstack.pro during normal Claude Code sessions.
3. **Credential stored in-process**: The persistent key storage ("Your key is saved permanently — no environment variables needed") means the loader manages its own credential store, a non-standard trust boundary.
4. **Single-org contributor**: Published under `cwinvestments` (CW Affiliate Investments LLC) with no evidence of external contributors, code review, or security audit.
5. **No tests or CI visible**: The README contains no mention of a test suite or CI pipeline.

Verdict is `watch`: revisit if the PyPI package is independently audited, gains meaningful community contributors, or if the free-skills-only path (no Pro loader) becomes viable without the license infrastructure.

## Mechanical details

- **Install**: `pip install memstack-skill-loader` then `claude mcp add --scope user memstack-skills -- python -m memstack_skill_loader`
- **Skill format**: Standard SKILL.md with YAML frontmatter; skills load via the MCP catalog system
- **Memory backend**: SQLite + semantic vector search for session recall (`echo` skill)
- **Hooks**: PostToolUse observation capture, SessionStart context injection, commit-safety hooks
- **Dashboard**: `python -m memstack_skill_loader dashboard` at localhost:3333 — skill toggle, token burn report, memory browser, 3-agent monitor
- **Tier gate**: All 127 skill files are in the repo; Pro gating is enforced by the MCP loader's license check, not by absent files
- **New-skill policy**: Skills added to the repo default to Pro-exclusive for 90 days, then drop to free unless marked permanent-Pro
- **Overlapping catalog entries**: `claude-spellbook` (skill reference collection), `one-skill-to-rule-them-all` (meta-skill loader pattern), `bmad-skill-forge` (skill generator)

## Security

- **License**: MIT per README. The MIT license applies to the skill content; the commercial Pro license is a separate runtime agreement with memstack.pro.
- **No tests evident**: README does not reference a test suite or CI configuration.
- **License-check network call**: The MCP loader validates Pro keys at runtime against memstack.pro — an outbound network channel in the agent toolchain that is not user-visible during normal operation.
- **Credential stored by process**: `activate_license()` persists the Pro key inside the loader's own storage, bypassing the standard env-var or secrets-manager pattern. This creates a credential that the MCP server process owns and manages.
- **Opaque PyPI package**: The actual loader logic is distributed as a binary/wheel from PyPI. The GitHub repo contains skill markdown files but the security-relevant code (license check, key storage, MCP message handling) is in the PyPI package, which has not been independently audited per available evidence.
- **Single-org supply chain**: One organization (CW Affiliate Investments LLC) controls both the PyPI package and the license validation server. A compromised package release or server could affect all users.
- **No signed releases noted**: No mention of PyPI release signing, SLSA provenance, or reproducible builds.
