---
name: advisor-strategy
title: Advisor Strategy
url: "https://claude.com/blog/the-advisor-strategy"
category: agent-pattern
summary: architectural concept for cost-effective agent orchestration; executor/advisor split
tags: [agents, cost-optimization, dispatch, patterns]
reviewed: 2026-05-25
acquired: 2026-05-25
license: proprietary
security_flags: []
overlaps: []
source: unknown
---

## What it says

The Advisor Strategy is an architectural pattern where one model executes (cheaper/faster) and a smarter model advises only when needed. The executor handles routine work; when it hits uncertainty it escalates to the advisor for a targeted review. No tool to install — this is a design concept from the Anthropic blog.

## Assessment

Maps cleanly to a kb dispatch pattern: a cheap executor (Codex, Haiku) handles routine HO responses while a smart advisor (Opus) reviews only when the executor flags uncertainty. If the advisory step is done via an interactive Claude subagent rather than a separate API call, no API credits are consumed beyond the subscription. Worth noting as an architecture reference when designing dispatch profiles, but not a standalone tool to evaluate or install.

## What to adopt

When designing dispatch profiles that combine multiple model tiers, structure them as executor/advisor pairs rather than always routing to the most capable model. The advisor review step can be an interactive subagent call, keeping it within subscription billing. Concretely: let Codex or Haiku draft the HO response; spawn an Opus subagent only when the executor's confidence is low or when a review gate is required.

## Security

This entry describes a proprietary Anthropic API feature (the `advisor_20260301` tool, available in beta on the Claude Platform), not an open-source package. No installation artifact, dependency chain, or third-party code is involved. There is no license to audit and no supply-chain risk from pulling packages.

The primary operational consideration is cost and billing exposure: advisor tokens are billed at the advisor model's rate separately from executor tokens, and uncapped `max_uses` values could inflate spend on high-volume runs. Set `max_uses` conservatively and monitor the usage block. The pattern itself introduces no network egress beyond normal Claude API calls, no filesystem access, and no code execution outside the agent's existing tool set.
