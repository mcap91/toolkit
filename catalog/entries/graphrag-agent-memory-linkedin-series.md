---
name: graphrag-agent-memory-linkedin-series
title: "GraphRAG & Agent Memory LinkedIn Series"
url: "https://www.linkedin.com/feed/update/urn:li:share:7464580605327060992"
category: reference
summary: "Six-post series covering GraphRAG design, ontology modeling, and unified agent memory architecture — useful conceptual grounding for KG-backed agents."
tags: [graphrag, knowledge-graph, ontology, agent-memory, reasoning, langgraph, crewai, memory]
reviewed: 2026-06-10
acquired: 2026-06-10
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---
## What it says

A six-post LinkedIn series by a practitioner who spent a year building GraphRAG from scratch. Topics covered by title:

1. **3 ways to model your ontologies for GraphRAG** — ontology design patterns for retrieval-augmented generation over knowledge graphs.
2. **LangGraph/CrewAI or from scratch?** — framework trade-offs for agentic orchestration.
3. **A year building GraphRAG from scratch** — retrospective on lessons learned building production GraphRAG.
4. **The third memory type: reasoning memory** — introduces a distinct memory tier beyond episodic/semantic, focused on stored reasoning traces.
5. **Building a production-grade personal AI assistant** — architecture notes for a personal AI built on these memory primitives.
6. **Designing Your Agents' Unified Memory** — synthesis post on how to unify episodic, semantic, and reasoning memory in an agent system.

Posts are unfetchable (LinkedIn post URLs); summary is derived from titles and surrounding context.

## Assessment

`watch` — the series addresses a real gap: how to structure agent memory beyond flat vector stores, using KGs and ontologies. The "reasoning memory" framing is a distinct perspective worth tracking. No code or repo is linked; the value is conceptual/architectural rather than immediately adoptable tooling. Useful reference when designing KG-backed memory for bioinformatics agents.

## What to adopt

- The three-tier memory model (episodic / semantic / reasoning) as a design vocabulary when specifying agent memory architecture.
- Ontology modeling patterns for GraphRAG as a checklist when wiring up a KG retrieval layer.
- The "from scratch vs framework" analysis as a decision aid if evaluating LangGraph or CrewAI for workflow orchestration.

## Security

No installation surface — this is a reading/reference item. No security concerns.

## Usage notes

- **When to use GraphRAG over plain RAG:** Standard RAG retrieves relevant passages for specific queries but fails on corpus-level sensemaking questions ("what are these documents about?"). GraphRAG stores text units with provenance, extracts entities/relationships into a knowledge graph, groups them into a nested hierarchy via the Leiden algorithm, and generates community summary reports upfront. Those pre-computed summaries answer broad questions without re-reading the corpus. Rule of thumb: quick single-fact lookup → plain RAG; sensemaking across the whole corpus → GraphRAG.
