---
name: chunkless-rag
title: Chunkless RAG (IBM)
url: "https://note.com/tam2_sys/n/n2d9c200fb19d?hl=en"
category: agent-pattern
summary: "RAG architecture that preserves document tree structure instead of splitting into fixed-size chunks — AI agents navigate the document hierarchy (table of contents, headings, sections) like a human reader, reading short section summaries to locate relevant content, then drilling into specific sections; requires structural document parsing (e.g. Docling) to reconstruct logical hierarchy from PDFs; trades higher latency and compute for better cross-section reasoning, context preservation, and reduced hallucination on complex documents"
tags: [rag, retrieval, document-structure, chunking-alternative, docling, ibm, pdf, agent-navigation]
reviewed: 2026-09-18
acquired: 2026-09-18
license: ""
security_flags: []
overlaps: [five-levels-of-chunking, docling-mcp, agentic-rag-terminal-tools]
source: unknown
---

## What it does

Chunkless RAG replaces the traditional chunk-embed-retrieve pipeline with agent-driven document navigation. Instead of splitting a document into fixed-size chunks (which destroys headings, sections, and hierarchical relationships), the system:

1. Parses the document into a tree structure preserving headings, sections, subsections, tables, and images (using Docling or similar structural parsers)
2. Generates short summaries for each section node in the tree
3. Agent navigates the tree at query time — reads section summaries, infers relevance, drills into specific sections, follows references to other sections as needed

This preserves the logical context that chunking destroys. The agent always knows which hierarchy level a piece of information belongs to, enabling cross-section reasoning and integrated answers.

When to use: complex documents requiring high-precision answers — contracts, technical manuals, research papers, regulatory filings. Not suited for ambiguous keyword searches across millions of documents, where traditional RAG is more efficient.

Trade-offs: higher latency (more model interactions per query), higher compute cost, requires structural document parsing as a prerequisite.

Source: summary article of an IBM Technology video (August 2026).

## Security

No direct security implications beyond standard RAG considerations.