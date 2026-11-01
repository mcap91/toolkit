---
name: alcoa-plus-for-ai
title: AI Needs What ALCOA+ Gave Records
url: "https://bryandownie.substack.com/p/ai-needs-what-alcoa-gave-records"
category: reference
summary: Useful framing for regulated-AI governance but no actionable tool or framework yet — CASTEM teased but unpublished
tags: [ai-governance, gxp, regulatory, data-integrity, pharma]
reviewed: 2026-06-10
acquired: 2026-06-10
license: UNLICENSED
security_flags: []
overlaps: []
source: unknown
---

## What it says

Bryan Downie argues that generative AI breaks the traditional division of labor in regulated-industry record-keeping. ALCOA+ (Attributable, Legible, Contemporaneous, Original, Accurate + Complete, Consistent, Enduring, Available) governs data records, while other regimes (IQ/OQ/PQ, CSV, SOPs) governed the *producer* of those records. AI models are a new kind of producer that existing qualification regimes don't cover.

Regulatory bodies (FDA, EMA, EU AI Act) are beginning to address this gap through guidance on model credibility, context-of-use, and lifecycle management. The article argues that operators need a mnemonic-level set of first principles — like ALCOA+ did for records — to reason about whether an AI system is fit to produce a given output. The author calls his forthcoming framework "CASTEM" but does not define it in this piece.

## Assessment

**Note** — the article provides valuable conceptual framing for anyone working on AI in GxP/regulated bioinformatics (validation of AI-assisted pipelines, audit trails for AI-generated annotations). However, the promised actionable framework (CASTEM) is not yet published, and the piece itself is a position essay with no tool, code, or implementable methodology. Worth revisiting when CASTEM is published.

## Mechanical details / What to adopt

- Mental model: ALCOA+ governs the *record*; a new regime must govern the *AI producer*. Neither alone covers AI-generated outputs in regulated settings.
- Key regulatory refs cited: FDA draft guidance on AI in drug development (model credibility), EMA reflection paper on AI/ML, joint FDA–EMA principles, EU AI Act.
- Context-of-use principle: AI model fitness is tied to the specific task, not transferable across tasks the way instrument qualification is.

## Security

Not applicable — this is a blog post with no code, dependencies, or executable components. License is standard Substack copyright (UNLICENSED / all rights reserved). No security concerns.