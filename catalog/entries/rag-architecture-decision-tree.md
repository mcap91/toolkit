---
name: rag-architecture-decision-tree
title: RAG Architecture Decision Tree
url: "https://en.wikipedia.org/wiki/Retrieval-augmented_generation"
category: agent-pattern
summary: "Diagnostic framework for choosing among 8 RAG architectures (Naive, Hybrid, Reranked, Multi-Query, Hierarchical, Corrective, Graph, Agentic) based on observed failure modes — treat RAG like debugging: let Naive fail first, watch how it fails, then pick the architecture that fixes that specific symptom; measure retrieval separately from generation"
tags: [rag, retrieval, architecture, debugging, decision-tree, agent-pattern]
reviewed: 2026-09-14
acquired: 2026-09-14
license: ""
security_flags: []
overlaps: []
source: unknown
---

## What it does

A practitioner framework for selecting the right RAG architecture by diagnosing the failure mode of a simpler one, rather than stacking tools blindly.

The core method: start with Naive RAG, observe how it fails, then choose the architecture that addresses that specific failure:

| Failure symptom | Architecture fix |
|---|---|
| Keyword/ID matches vanish (semantic-only misses exact terms) | **Hybrid** (combine semantic + keyword search) |
| Correct document exists but ranks too low | **Reranked** (add a reranker after initial retrieval) |
| Different phrasings of the same question give different answers | **Multi-Query** (generate multiple query variants) |
| Long documents lose structural context | **Hierarchical** (preserve document structure in chunks) |
| System is confidently wrong (retrieves plausible but incorrect docs) | **Corrective** (add a verification/correction step) |
| Answer requires synthesizing across multiple documents | **Graph** (knowledge graph connecting cross-document facts) |
| Some questions need zero retrieval, others need multiple rounds | **Agentic** (agent decides when and how often to retrieve) |

Key principle: always measure retrieval quality separately from generation quality. Prompt-tuning a generation problem when the real bug is in retrieval wastes effort.

## Security

No security concerns — this is a conceptual framework, not executable code.