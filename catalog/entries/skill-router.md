---
name: skill-router
title: Skill Router
url: "https://github.com/pcx-wave/skill-router"
category: meta-skill
summary: superpowers using-superpowers already handles skill routing
tags: [meta-skill, routing, skill-discovery]
reviewed: 2026-05-25
acquired: 2026-05-25
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Scans installed skills, builds a lightweight keyword index, and routes incoming requests to the most relevant skill. Operates in two modes: suggest (presents matches for confirmation) and auto (applies high-confidence matches without prompting). Conservative by design — only triggers on high-confidence keyword matches to avoid false routing.

## Assessment

`superpowers using-superpowers` already handles skill discovery and routing in this stack. Skill Router would duplicate that responsibility without adding capability. No gap to fill.

## Mechanical details

Not recommended for install. If skill routing gaps are discovered that superpowers does not cover, revisit this entry before building a custom solution.

## Security

Skill Router is MIT-licensed with no external network calls at runtime — it operates purely over the locally installed skills at `~/.claude/skills/`. The only file write is a usage stats JSON (`~/.claude/skill-usage.json`), which is low-risk local telemetry. No credentials, secrets, or privileged APIs are accessed. The main surface to be aware of is that the skill index is built from installed skill filenames and frontmatter, so a malicious skill injected into `~/.claude/skills/` could influence routing decisions; this is bounded by the same install-time trust boundary that applies to all Claude Code skills (see `agent-lockdown`).
