---
name: claude-spellbook
title: Claude Spellbook
category: reference
summary: "50 skills, 7 agents, 11 slash commands — use as pattern reference, not default install"
tags: [skills, agents, hooks, patterns]
reviewed: 2026-05-25
acquired: 2026-05-25
license: unknown
security_flags: []
overlaps: []
source: unknown
---

## What it says

A bundled toolkit of 50 skills, 7 agents, and 11 slash commands with auto-formatting hooks. Provides a worked example of the "skill + agent + hook" integration pattern — showing how these three Claude Code primitives can be combined into a coherent operational system. Sourced from a Reddit r/claudeskills post.

## Assessment

Installing all 50 skills would create routing noise and override conflicts with the existing superpowers stack. The value is in the pattern library — how individual skills are structured, how agents are wired to skills, and how hooks trigger behavior automatically. Useful to browse when designing new integrations, not as a default install.

## What to adopt

Browse the repo when designing a new skill + agent + hook integration to see existing examples. Specific skills or hook patterns that solve a gap can be cherry-picked rather than adopting the full bundle. No bulk install.

## Security

No license is listed in the source material; provenance is a Reddit community post with no linked repository verified at review time. The bundle itself contains only prompt/instruction files (SKILL.md, agent definitions, hook configs) — no executable code, no network calls, no shell commands embedded in the skills themselves. The primary risk is **routing conflict**: bulk-installing 50 skills into `~/.claude/skills/` could silently override or shadow skills from the superpowers stack, causing unexpected behavior without any error signal. Cherry-pick adoption eliminates this risk. No supply-chain, credential, or data-exfiltration concerns identified.
