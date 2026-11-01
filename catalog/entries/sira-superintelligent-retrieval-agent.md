---
name: sira-superintelligent-retrieval-agent
title: SIRA — Superintelligent Retrieval Agent
url: "https://arxiv.org/abs/2605.06647"
category: agent-pattern
summary: "Meta research framework that compresses multi-round agentic retrieval into a single corpus-discriminative BM25 action — LLM enriches documents offline with missing vocabulary, predicts query-side evidence terms, validates via IDF tool calls, then issues one weighted sparse retrieval; outperforms dense retrievers and multi-round agents on BEIR/NQ/HotpotQA with no fine-tuning"
tags: [retrieval, RAG, BM25, query-expansion, corpus-enrichment, sparse-retrieval, meta-ai]
reviewed: 2026-06-26
acquired: 2026-06-26
license: unlicensed
security_flags: [no-code-release]
overlaps: [contextual-retrieval-anthropic, rag-retrieval-recipe]
source: unknown
---

## What it does

SIRA (Superintelligent Retrieval Agent) is a retrieval framework from Meta AI (arxiv 2605.06647) that redefines "superintelligent retrieval" as the ability to compress multi-round exploratory search into a single, corpus-discriminative retrieval action. Instead of iteratively querying and reformulating like typical RAG agents, SIRA programs one precise weighted BM25 call.

The framework operates in two phases:

**Offline corpus-side enrichment:** A frozen LLM processes each document once, proposing "missing search vocabulary" — synonyms, abbreviations, aliases, and domain-specific phrases a user might search for but which are absent from the document's original text.

**Online query-side planning:** Given a query, the LLM predicts evidence vocabulary omitted by the query, then validates proposed expansion terms against corpus statistics via IDF tool calls. Terms that are absent, overly common, or unlikely to create retrieval margin are filtered. The final retrieval step is a single weighted BM25 call combining the original query with validated expansions.

## Key takeaways

- Reverses the trend toward dense vector retrieval — demonstrates that one well-formed sparse lexical action outperforms substantially more expensive multi-round search while remaining interpretable, training-free, and efficient.
- Core insight: ask which terms *separate* desired evidence from corpus-level confusers, not merely which terms are relevant.
- Uses corpus statistics (IDF) as tool calls during planning, grounding the LLM's expansion proposals in actual corpus distribution.
- Introduces BrowseComp-Wikipedia, a 232-query hard-search benchmark on a 25.6M-document Wikipedia index.
- Performance is bounded by the LLM's internal knowledge of the domain — breaks down on corpora completely absent from training data (proprietary contracts, post-cutoff medical literature).

## Mechanical details

- **Corpus enrichment:** One-time LLM pass per document adds missing search terms to the BM25 index.
- **Query expansion:** LLM generates candidate expansion terms + per-term weights; IDF tool validates discriminative power.
- **Retrieval:** Single weighted BM25 call with original + validated expansion terms.
- **Benchmarks:** Strongest average on 10 BEIR benchmarks vs. dense retrievers, learned sparse retrievers, and LLM search-agent baselines. On NQ and HotpotQA, retrieval-only answer coverage exceeds RL-trained agentic QA systems. On BrowseComp-Wikipedia, outperforms multi-round Perplexity agents at every retrieval budget (9.7% R@1, 15.3% R@10, 36.1% R@100).
- **Requirements:** No relevance labels, no retriever fine-tuning, no dense embeddings at query time.

## Security

Research paper only — no code release as of June 2026. No software artifact to assess. The technique itself has no security surface beyond the LLM used for enrichment/planning.