---
name: gstack
title: gstack
url: "https://github.com/garrytan/gstack"
category: framework
summary: kb dispatch covers the relevant orchestration patterns; browser/deployment out of scope
tags: [workflow, orchestration, browser, kb]
reviewed: 2026-05-25
acquired: 2026-05-25
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

An opinionated workflow stack with browser control, code reviews, and deployment helpers. Bundles many moving parts into a single orchestration framework targeting full application development workflows including browser automation and deployment pipelines.

## Assessment

gstack's orchestration overlaps with kb dispatch's launch/review/status lifecycle. The additions gstack makes — browser automation and deployment tooling — are outside kb's scope. kb is a knowledge management and agent orchestration system, not an application deployment framework.

## Mechanical details

Do not install. kb dispatch covers the relevant orchestration patterns (launch, review, status lifecycle for child agent runs). gstack's browser and deployment features are out of scope for kb. No concepts identified as worth adopting.

## Security

MIT licensed; source is fully open and auditable. gstack ships layered prompt-injection defenses for its browser agent (22 MB ML classifier, Claude Haiku transcript check, random canary token, and a two-classifier verdict combiner), but these mitigations protect gstack's own browser session — they are not a security primitive that transfers to this project. The `/cso` skill runs OWASP Top 10 and STRIDE threat-model audits, which is useful context for understanding gstack's security posture, but again does not bear on adoption here. The tool is verdict: skip, so the only security consideration is the installation boundary: the setup script clones directly into `~/.claude/skills/` and runs `./setup`, so any supply-chain compromise of the upstream repo would execute in the user's Claude Code environment. No credential handling or network exposure beyond opt-in anonymous telemetry (off by default, Supabase-backed with public API key, no code or path data collected).
