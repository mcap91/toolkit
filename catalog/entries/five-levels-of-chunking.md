---
name: five-levels-of-chunking
title: "Five Levels of Chunking Strategies in RAG (Greg Kamradt's taxonomy)"
url: "https://medium.com/@anuragmishra_27746/five-levels-of-chunking-strategies-in-rag-notes-from-gregs-video-7b735895694d"
category: agent-pattern
summary: "Taxonomy of RAG text-splitting strategies, from Greg Kamradt's '5 Levels of Text Splitting' (these are notes on that video): Level 1 fixed-size (character/sentence splitters), Level 2 recursive (hierarchical separators), Level 3 document/structure-based (respect headings, tables, code), Level 4 semantic (split at embedding-similarity breakpoints), Level 5 agentic (an LLM decides chunk boundaries from propositions). Higher levels trade cost/complexity for chunks that better match meaning; match the strategy to the data."
tags: [rag, chunking, text-splitting, embeddings, retrieval, semantic-chunking, langchain, llamaindex]
reviewed: 2026-08-17
acquired: 2026-08-17
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---
## What it covers

A widely-cited taxonomy of how to split documents into chunks for retrieval-augmented generation, popularized by Greg Kamradt's "5 Levels of Text Splitting" tutorial (the catalog source is a Medium write-up of notes on that video; the page itself returned HTTP 403 at review time, so this entry is grounded in the well-documented framework). The guiding principle: chunk so the data can be *retrieved for value later*, not for its own sake — and match the level to the data rather than using one method everywhere.

## The five levels

1. **Fixed-size** — split into N characters regardless of content/structure. Simplest; LangChain `CharacterTextSplitter`, LlamaIndex `SentenceSplitter`.
2. **Recursive** — split hierarchically with an ordered separator list (`"\n\n"`, `"\n"`, `" "`, `""`), recursing until chunks reach the target size. LangChain `RecursiveCharacterTextSplitter`. Good default for structured text.
3. **Document/structure-based** — split along the document's own structure so tables, code functions/classes, and sections stay intact and headings can become filterable metadata. Needs a parser per format (PDF/OCR/layout-rich docs need heavier tools like Unstructured.io hi-res, LlamaParse, Docling).
4. **Semantic** — detect breakpoints where meaning shifts between neighboring sentence windows (embedding similarity), aligning chunks with topic transitions. More expensive and implementation-sensitive than recursive. LangChain `SemanticChunker`, LlamaIndex `SemanticSplitterNodeParser`.
5. **Agentic** — let an LLM act like an editor: read propositions/statements and decide whether each joins an existing chunk or starts a new one. Experimental; framed as more viable as token costs fall.

## Notes

- Practical mapping from the source: fixed-size for simple homogeneous text (speed); recursive for structured text with clear separators; document-based for organized docs (e.g. papers); semantic for coherence when cost is acceptable; agentic for high-accuracy experimental use.
- This is a reusable technique/reference, not a tool — the named splitters live in LangChain / LlamaIndex.

## Security

- Conceptual/technique content — no executable component. License N/A (third-party article summarizing a public framework; recorded as NOASSERTION).
