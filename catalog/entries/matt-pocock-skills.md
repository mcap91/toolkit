---
name: matt-pocock-skills
title: Matt Pocock Skills
url: "https://github.com/mattpocock/skills"
category: skill
summary: "Collection of 17 composable Claude Code skills for disciplined engineering — grilling sessions (alignment interviews before coding), domain modeling (CONTEXT.md + ADRs), TDD red-green-refactor loop, codebase architecture audits with HTML reports, issue triage state machine, PRD synthesis, bug diagnosis loop, code review (standards + spec axes); installable via npx skills"
tags: [claude-code-skills, engineering-discipline, domain-modeling, tdd, code-review, grilling, architecture, triage]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: [andrej-karpathy-skills, grill-with-docs]
source: unknown
---

## What it does

Collection of 17 Claude Code skills split into user-invoked (orchestration) and model-invoked (reusable discipline). Designed to be small, composable, and model-agnostic. Addresses four failure modes: misalignment (grilling sessions), verbosity (shared domain language via CONTEXT.md), broken code (TDD + diagnosis loops), and architectural decay (codebase design audits).

### User-invoked skills (engineering)

- **grill-with-docs** — alignment interview that also builds a shared domain language (CONTEXT.md) and ADRs
- **grill-me** — general-purpose grilling session for plans/designs
- **triage** — moves issues through a state machine of triage roles with configurable labels
- **improve-codebase-architecture** — scans for "deepening" opportunities, produces HTML report, then grills through selected improvements
- **to-issues** — breaks plans/specs/PRDs into independently-grabbable vertical-slice issues
- **to-prd** — synthesizes current conversation into a PRD and publishes to issue tracker
- **ask-matt** — router that recommends which skill fits the situation

### Model-invoked skills (engineering)

- **tdd** — red-green-refactor loop, one vertical slice at a time
- **diagnosing-bugs** — reproduce → minimise → hypothesise → instrument → fix → regression-test
- **research** — investigates questions against primary sources, outputs cited Markdown, runs as background agent
- **prototype** — throwaway prototypes (terminal apps for logic, multiple UI variations for design)
- **domain-modeling** — challenges terms against glossary, stress-tests with edge cases, updates CONTEXT.md
- **codebase-design** — deep module design vocabulary (lots of behavior behind small interfaces)
- **code-review** — two parallel sub-agents: Standards (coding standards + Fowler smells) and Spec (faithfulness to issue/PRD)

### Productivity skills

- **handoff** — compacts conversation into a handoff document for another agent
- **teach** — multi-session teaching using current directory as workspace
- **writing-great-skills** — reference for writing predictable skills

## Differentiators

- **Domain-driven design integration** — CONTEXT.md creates a shared language that reduces token usage and improves naming consistency across sessions
- **Two-axis code review** — standards and spec reviewed by parallel sub-agents so neither pollutes the other
- **Architecture health loop** — periodic `improve-codebase-architecture` counteracts AI-accelerated software entropy
- **Installer** — `npx skills@latest add mattpocock/skills` with per-agent selection and interactive setup

## Mechanical details / What to adopt

- Install: `npx skills@latest add mattpocock/skills`, select skills and target agents
- Run `/setup-matt-pocock-skills` once per repo to configure issue tracker (GitHub/Linear/local), triage labels, and docs location
- Skills work with any model — not Claude-specific despite living in `.claude/`
- User-invoked skills may call model-invoked skills, but never other user-invoked skills

## Security

Skills are plain Markdown instruction files — no executable code beyond the agent's own tool calls. Issue tracker integration (GitHub/Linear) uses whatever credentials the agent already has configured.