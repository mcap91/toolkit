---
name: production-rag-system-taxonomy
title: Production RAG as a System (8-Part Taxonomy)
category: agent-pattern
summary: "Practitioner taxonomy framing production RAG as an 8-part system (not a vector-database feature): 01 offline build time (parse/chunk/embed/index), 02 online query time (rewrite/retrieve/rerank/assemble/generate), 03 knowledge store (vectors+metadata+raw docs+freshness), 04 retrieval quality (hybrid search/filters/top-k/reranking), 05 answer quality (grounding/citations/structured output/fallback), 06 state/data layer (Postgres+Redis+object storage+vector index), 07 observability/evals (latency/recall/answer quality/hallucinations/cost), 08 safety operations (ACLs/PII protection/prompt-injection defense/caching/feedback); presented as a directory-tree mental model contrasting with the four-step chunk-embed-retrieve-prompt demo pipeline."
tags: [rag, production-rag, retrieval, taxonomy, system-design, observability, safety, agent-pattern]
reviewed: 2026-08-25
acquired: 2026-08-25
license: NOASSERTION
security_flags: []
overlaps: [agentic-rag, rag-retrieval-recipe, five-levels-of-chunking]
source: unknown
---

## What it says

A short practitioner post arguing that production RAG is a system, not a vector-database feature. Most demos stop at Chunk → Embed → Retrieve → Prompt; the post frames everything past that point as "where production RAG starts," organized as eight additional concern areas.

## The 8-part taxonomy

Presented as a directory-tree mental model (repo-shaped):

1. **01_offline_build_time/** — Parse → chunk → embed → index
2. **02_online_query_time/** — Rewrite → retrieve → rerank → assemble → generate
3. **03_knowledge_store/** — Vectors + metadata + raw docs + freshness
4. **04_retrieval_quality/** — Hybrid search + filters + top-k + reranking
5. **05_answer_quality/** — Grounding + citations + structured output + fallback
6. **06_state_data_layer/** — Postgres + Redis + object storage + vector index
7. **07_observability_evals/** — Latency + recall + answer quality + hallucinations + cost
8. **08_safety_operations/** — ACLs + PII protection + prompt injection defense + caching + feedback

## Thesis

"RAG is not a vector database feature; it's a production system." The hard part, per the post, is making retrieval fresh, relevant, secure, observable, and reliable every time.

## Notes

- Source is a short-form post captured without an attributable source URL (content-only intake item); no named author, reference implementation, or benchmark data is included — it is a mental-model/checklist, not a tutorial or codebase.
- Reusable technique/checklist, not an installable tool — nothing ships with it.

## Security

- Conceptual/technique content — no executable component. License N/A (recorded as NOASSERTION).