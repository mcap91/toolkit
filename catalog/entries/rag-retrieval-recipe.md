---
name: rag-retrieval-recipe
title: RAG Retrieval Recipe
url: "https://en.wikipedia.org/wiki/Retrieval-augmented_generation"
category: agent-pattern
summary: "Practitioner's RAG recipe — semantic chunking (500-1000 tokens, 100 overlap), embed once with nomic/mxbai, store in ChromaDB/Qdrant/LanceDB, retrieve top-20 → BGE rerank → top-5, cite source chunks in LLM output"
tags: [rag, embeddings, vector-db, reranking, retrieval]
reviewed: 2026-06-19
acquired: 2026-06-19
license: ""
security_flags: []
overlaps: [chromadb]
source: unknown
---

## What it says

A compact practitioner's recipe for production RAG pipelines:

1. **Chunking**: Semantic chunking, 500-1000 tokens per chunk with 100-token overlap
2. **Embedding**: Embed everything once using an embedding model like `nomic-embed-text` or `mxbai-embed-large`. Re-run only when documents change.
3. **Storage**: Store vector, original text, and metadata in a vector database (ChromaDB, Qdrant, or LanceDB)
4. **Retrieval**: For each query — embed it, search top 20 chunks, rerank with a BGE reranker, keep top 5
5. **Generation**: Send retrieved chunks and the query to the LLM; prompt it to cite the source chunk for every claim

## Assessment

Solid standard-practice RAG recipe. The key insights worth preserving:

- **Embed once, re-run on change** — avoids redundant embedding compute
- **Over-retrieve then rerank** (top-20 → BGE reranker → top-5) — two-stage retrieval significantly improves precision over single-stage nearest-neighbor search
- **Citation enforcement** — prompting the LLM to cite source chunks per claim is the simplest grounding technique

The specific model recommendations (nomic-embed-text, mxbai-embed-large, BGE reranker) are reasonable open-source choices that run locally. The vector DB recommendations align with what's already cataloged (ChromaDB).

Directly applicable to literature RAG for bioinformatics — chunk papers/protocols, embed, retrieve relevant context for agent queries.

## Mechanical details

- **Embedding models**: `nomic-embed-text` (Ollama), `mxbai-embed-large` (Ollama) — both run locally
- **Reranker**: BGE reranker (e.g., `BAAI/bge-reranker-v2-m3` via HuggingFace)
- **Vector DBs**: ChromaDB (already cataloged), Qdrant, LanceDB
- **Chunk params**: 500-1000 tokens, 100-token overlap, semantic boundaries

## Security

Not applicable — this is a technique description, not installable software. Security considerations would apply to the individual components (vector DB, embedding model, LLM) chosen for implementation.

## Usage notes

- **Chunking strategy selection guide**: (1) Fixed-size: cut every N tokens, fast but splits mid-sentence. (2) Recursive: paragraphs → lines → words until each piece fits. (3) Document-based: keep headers, tables, code blocks whole. (4) Semantic: cut where embedding distance between sentences spikes. (5) Propositional: LLM breaks text into atomic self-contained facts. (6) Agentic: LLM agent decides chunk boundaries. Smart strategies (4-6) call a model at index time (slower, costs more). Start with a middle chunk size + sliding window with ~10-25% overlap. Common failure modes: chunks too small → context cut away, chunks too large → one vector blurs multiple topics and retrieval misses.
