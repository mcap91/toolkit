---
name: pageindex
title: PageIndex
url: "https://github.com/VectifyAI/PageIndex"
category: framework
summary: "Vectorless reasoning-based RAG engine — replaces vector index with hierarchical tree index, uses LLM reasoning for retrieval instead of similarity search; 98.7% accuracy on FinanceBench (vs vector RAG baselines); SDK with local mode (pip install pageindex) and cloud mode; ~$0.001/page indexing cost; ideal for financial/legal/medical/technical documents; MIT"
tags: [rag, document-retrieval, tree-index, vectorless, reasoning, pdf, financial, legal, python, llm]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: [rag-retrieval-recipe]
license: MIT
security_flags: []
source: unknown
---

## What it does

PageIndex replaces vector-based RAG with a reasoning-based approach. Instead of embedding chunks and searching by similarity, it builds a hierarchical tree index of each document and lets an LLM reason its way through it — mimicking how a human expert navigates a long report.

Two-step retrieval:
1. **Index**: generate a tree-structure index for the document (one-time, ~$0.001/page with gpt-5.6-luna)
2. **Retrieve**: agentically search the tree with LLM reasoning

Key advantages over vector RAG: traceable results (not opaque "vibe retrieval"), full context (conversation history, domain knowledge), no chunking, no vector database.

98.7% accuracy on FinanceBench (financial document QA), outperforming vector-based RAG. Cost savings: 2.1x cheaper at 52 pages, 16.6x cheaper at 420 pages vs feeding the whole PDF to the model.

Ideal for: financial reports, legal documents, regulatory filings, technical manuals, medical literature, academic textbooks.

## Mechanical details

SDK: `pip install -U pageindex`. Local mode runs entirely on your machine with your own LLM key. Cloud mode uses PageIndex-managed indexing/storage with your model for chat.

PageIndex Flash: fast tree index for text-based PDFs (default in local mode). PageIndex File System: file-level tree indexing for reasoning over entire corpora (cloud-only).

Cloud adds: OCR, image understanding, block-level citations, metadata, folders, MCP server. Agent integration examples for OpenAI Agents SDK and Claude Agent SDK.

## Security

MIT licensed. Local mode keeps all data on your machine. Cloud mode is optional. No bundled API keys — bring your own.