---
name: suede-creator-skills
title: Suede Creator Skills
url: "https://github.com/JasonColapietro/suede-creator-skills"
category: plugin
summary: "MIT-licensed pack of 25 Claude Code / Codex skills covering multi-agent orchestration (WIP collision detection, rollback trees), Codex worker fleets (Claude plans + parallel Codex CLI workers), A-F code review grading across 7 lanes with instant-F triggers, AI eval framework, design/copy/SEO audits, and consumer automation; ships MCP server with 7 tools"
tags: [claude-code, codex, skills, code-review, multi-agent, orchestration, mcp-server, ai-eval, seo, design]
reviewed: 2026-07-15
acquired: 2026-07-15
license: MIT
security_flags: []
overlaps: [get-shit-done, native-subagents]
source: unknown
---

## What it says

A collection of 25 SKILL.md files for Claude Code and OpenAI Codex, organized into five domains:

**Agent orchestration:** `suede-agent-teams` coordinates agent lanes with WIP collision detection, RFC mode, feature-flag strategy, rollback trees, and a handoff checklist that requires evidence before closing. `suede-codex-fleet` (the "Suede Fable Fleet") has Claude decompose a job into self-contained briefs, spawn parallel Codex CLI `codex exec` workers, and review every output against acceptance criteria. `suede-ai-eval` generates AI-SPEC artifacts, failure-mode rubrics, eval cases, and acceptance gates for LLM/RAG/classifier/agent surfaces.

**Code quality:** `suede-code` combines deep review + A-F ship grade in one pass across 7 lanes (Correctness, Security/permissions, Data/state, Domain truth, UX/release behavior, Tests/verification, Deploy readiness). Instant-F triggers lock the grade on hardcoded secrets or bypassable permission checks. `suede-ship-gate` generates CI config that gates merges. Separate skills available for review-only or grade-only workflows.

**Design/copy/SEO:** Design systems and visual QA, conversion copywriting with anti-slop gate, SEO/AEO/AI-EO audits, A-F page visibility grades, funnel analysis.

**Consumer automation:** `amazon-returns-recovery` scans Amazon order/return history and digital subscriptions for restocking fees, short refunds, and forgotten charges, then drives live chat to recover funds. Author reports $448.31 recovered across real cases including a previously denied refund.

**Distribution:** MCP server (dependency-free stdio, 7 tools, 6 resources, 5 prompts), plugin marketplace install (`/plugin install`), npx skills CLI, or manual clone. Compatible with Cursor, Copilot, Windsurf via the `npx skills add` path.

## Key takeaways

- The Codex fleet pattern (Claude as planner/reviewer, Codex CLI as parallel workers) is an architecturally interesting delegation model — Claude never generates code directly, only briefs and reviews
- A-F grading with instant-F triggers and lane caps provides a structured, repeatable code review signal
- Self-benchmarked against GSD and Superpowers on a 15-category self-graded rubric; claimed wins in 4 categories, losses in long-project lifecycle (GSD) and engineering discipline/skill maintainability (Superpowers); overall A- vs Superpowers' A
- 25 skills is broad surface area; the "broader skill packs hurt more than they help" finding from independent testing (Mikhail Shcheglov) applies — selective installation of individual skills is likely more effective than loading the full pack

## Security

MIT licensed. Skills inspect local files and repos. Author states no uploads, registry writes, private service calls, or secret requests. Creator skills generate drafts that may contain names, payment notes, file hashes, and rights claims — review before publishing. The `amazon-returns-recovery` skill interacts with Amazon's live chat interface on the user's behalf.