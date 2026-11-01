---
name: grill-with-docs
title: Grill With Docs
url: "https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md"
category: skill
summary: "Well-structured DDD design-review skill that enforces domain language, but relies on companion format files (CONTEXT-FORMAT.md, ADR-FORMAT.md) not bundled with the skill."
tags: [domain-driven-design, design-review, documentation, adr, glossary, planning]
reviewed: 2026-06-10
acquired: 2026-06-10
license: LicenseRef-unknown
security_flags: [no-license-stated]
overlaps: [advise-project-approach, context-graph-compressor]
source: unknown
---

## What it does

`grill-with-docs` is a Claude Code skill that runs a structured interrogation session to stress-test a design plan against a project's existing domain model. The agent asks probing questions one at a time, walks every branch of the design tree, proposes its own recommended answers, and explores the codebase when questions can be resolved by code inspection.

Four core behaviours fire during the session:

1. **Terminology challenge** — when the user's language conflicts with terms already in CONTEXT.md, the agent calls it out immediately with a precise quote from the glossary.
2. **Language sharpening** — vague or overloaded terms are replaced with a canonical name from the project vocabulary (e.g. "account" → Customer vs. User).
3. **Code cross-reference** — stated behaviour is checked against actual code; contradictions are surfaced explicitly.
4. **Live documentation writes** — when a term is resolved it is written into CONTEXT.md on the spot (not batched); ADRs are written only when all three criteria are met: hard-to-reverse, surprising without context, and the result of a real trade-off.

The skill expects a specific file layout: a root-level `CONTEXT.md` (glossary only, no implementation details), `docs/adr/` for decisions, and companion files `CONTEXT-FORMAT.md` and `ADR-FORMAT.md` that define the write formats. For multi-context repos, a `CONTEXT-MAP.md` at the root points to per-context `CONTEXT.md` files.

## Assessment

Verdict: **pilot**

The skill embodies sound DDD discipline — strict glossary enforcement, conservative ADR gating, and inline-capture beats batch-later for actually keeping docs current. The three-criterion ADR gate (hard-to-reverse + surprising + real trade-off) is one of the clearest ADR guidelines available in a skill format.

The obstacle to `adopt` is incompleteness: the skill references `CONTEXT-FORMAT.md` and `ADR-FORMAT.md` without providing them. Without those files the write steps produce inconsistent output or require the agent to improvise format. It also presupposes the CONTEXT.md convention, which most projects lack; projects already using this convention will get the most value immediately.

Worth piloting in a project that already uses or is willing to adopt CONTEXT.md + ADR conventions. A full adoption requires sourcing or authoring the companion format files.

## Mechanical details

- **Trigger:** Use when a user wants to stress-test a plan against existing domain documentation before implementation.
- **Session flow:** Single-question-at-a-time loop; agent provides its recommended answer with each question; branches are resolved before moving on.
- **Documentation layout assumed:**
  - Single-context: `CONTEXT.md` at root + `docs/adr/`
  - Multi-context: `CONTEXT-MAP.md` at root; each context has its own `CONTEXT.md` + `docs/adr/`
- **Lazy file creation:** CONTEXT.md and `docs/adr/` are created only when first needed — not pre-provisioned.
- **CONTEXT.md contract:** Glossary only; no implementation details, no spec content.
- **ADR gate:** All three must be true — hard-to-reverse, surprising without context, genuine trade-off with real alternatives.
- **Missing companion files:** `CONTEXT-FORMAT.md` and `ADR-FORMAT.md` must be sourced or written separately.
- **No runtime dependencies:** Pure prompt skill, no tooling required beyond Claude Code itself.

## Security

Pure prompt text — no code, no shell execution, no dependencies, no network calls initiated by the skill itself. There is no supply-chain or injection surface beyond normal Claude Code skill operation.

The skill instructs the agent to write files (`CONTEXT.md`, ADR files) to the project tree during a session. This is expected and scoped to documentation files only; no source-code modifications are directed by the skill.

**License:** Not stated in the skill file. The parent repo (mattpocock/skills) license was not confirmed from the fetched content; treat as unknown until verified.

**security_flags:** `no-license-stated`
