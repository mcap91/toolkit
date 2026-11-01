---
name: agentic-memory-benchmark
title: Agentic Memory Index — Benchmark of AI Agent Memory Systems
url: "https://example.com"
category: reference
summary: "Benchmark of 8 AI agent memory systems across 2176 tasks (272 scored per system: 200 fact-recall + 72 never-stored hallucination checks), in which a plain curated markdown wiki outscored all commercial memory products tested"
tags: [memory, benchmark, agent-memory, evaluation, markdown, mem0, rag-alternative]
reviewed: 2026-08-09
acquired: 2026-08-09
license: NOASSERTION
security_flags: []
overlaps: [karpathy-llm-wiki]
source: unknown
---

## What it does / What it says

Reports results from an "Agentic Memory Index" benchmark evaluating 8 AI agent memory systems across 2176 total tasks, with 272 scored tasks per system: 200 fact-recall questions (facts that were previously stored and must be retrieved correctly) plus 72 questions about facts that were never stored (testing whether the system hallucinates a plausible answer instead of correctly reporting absence). A separate 5,000-page scale test was run alongside the primary benchmark.

## Differentiators / Key takeaways

Reported scores/results:
- **Plain markdown wiki** (structured on the pattern of Karpathy's `llm-wiki` gist) — 98.5, the top score overall, ahead of every commercial product tested
- **Mitosis Cortex** — 96.9, the top-scoring hosted commercial product
- **gbrain** (free, open-source, local) — 92.9
- **Mem0** — 92.3; also the cheapest per successful answer at $341/1000 successful answers
- **Zep** — had freshness problems: 162.7s median delay before newly written facts became retrievable
- **Supermemory** — near-perfect short-term recall (59/60) but only 11/72 on long-horizon recall, a sharp falloff over time

Headline takeaway stated by the source: a plain markdown file set, curated directly by the agent, outperformed every dedicated memory product in this benchmark — a result that speaks directly to (and empirically tests) the `karpathy-llm-wiki` pattern already in this catalog.

## Mechanical details

Benchmark methodology combines standard fact-recall accuracy with a hallucination-detection axis (questions about facts that were never stored), which is a stronger test than fact-recall alone since it penalizes systems that answer confidently regardless of whether they actually have the information.

## Security

Reference/benchmark content — no code shipped by this entry itself; the systems it evaluates (Mem0, Zep, Supermemory, gbrain, Mitosis Cortex) are third-party products not independently audited here.

## community

Practitioner counterpoint (r/ClaudeCode): argues unstructured agent memory is fundamentally flawed — "a completely unstructured, arbitrary source of random data, outside of a repo, just seems like a terrible idea." Prefers structured alternatives: simple rules in CLAUDE.md, complex rules in skills/developer guides, complex data in a database or markdown git repo. Aligns with the benchmark's finding that a curated markdown wiki outperforms commercial memory products.
