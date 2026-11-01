---
name: cross-encoder-reranking
title: Cross-Encoder Reranking for RAG
url: https://www.instagram.com/reel/Dey-HLsJ5Cz/
source_url: https://www.instagram.com/reel/Dey-HLsJ5Cz/
source: instagram
category: reference
summary: "Second-stage retrieval technique: a cross-encoder jointly encodes a query and one candidate document in a single transformer forward pass, using self-attention across both texts to produce one relevance score per pair — more accurate but far more expensive than first-stage bi-encoder vector search, so it only reorders a small top-k candidate set rather than scoring a whole corpus."
tags:
  - reranking
  - cross-encoder
  - rag
  - retrieval
  - information-retrieval
  - hard-negative-mining
  - sentence-transformers
reviewed: 2026-10-28
acquired: 2026-10-28
license: N/A
security_flags: []
overlaps:
  - rag-retrieval-recipe
  - rag-architecture-decision-tree
  - production-rag-system-taxonomy
  - contextual-retrieval-anthropic
---

## What it does

Fixes a specific failure of first-stage vector search: the correct document often ranks far down a list of otherwise-similar candidates (e.g., position 23 of 50) because bi-encoder similarity scores cluster when documents share vocabulary. A reranker re-scores only the top candidates from that first pass, more accurately, before the final top-N is handed to the LLM.

**Mechanism** — a cross-encoder (a transformer, not a separate bi-encoder) takes the query and one candidate document as a single input sequence (`[query] [SEP] [document]`) and runs one forward pass per pair. Because both texts share a sequence, self-attention lets query tokens attend directly to document tokens, letting synonymous or related vocabulary across the two texts reinforce each other. The hidden state at a designated output position passes through a small linear head to produce one relevance score for that pair. This repeats once per candidate; results are sorted by score and the top few are kept.

**Cost** — nothing can be precomputed, since the model's input depends on the query at request time. Every candidate costs a full forward pass over query+document, so rerankers are applied to dozens or a few hundred first-stage candidates, never a whole corpus — this is why retrieve-then-rerank is a two-stage pipeline rather than a single-stage one. A reranker also can only reorder what the first stage already retrieved; if the correct document isn't in that candidate set, reranking cannot recover it.

**Training** — cross-encoders are trained on (query, document, relevance-label) pairs, commonly with `BinaryCrossEntropyLoss` or losses like `MultipleNegativesRankingLoss` (sentence-transformers' `CrossEncoder` class, `num_labels=1`). Hard negatives — same-topic documents that don't actually answer the query — are mined (e.g., `sentence-transformers.util.mine_hard_negatives`, which can use FAISS to keep mining memory-bounded) and are what force the model to learn fine-grained distinctions rather than coarse topic matching; training on hard negatives alone, however, can hurt performance on easier queries, so random negatives are typically mixed in alongside them.

## Sources

- [Training and Finetuning Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-reranker) — CrossEncoder training workflow, loss functions, hard-negative mining tradeoffs.
- [Training Overview — Sentence Transformers documentation](https://sbert.net/docs/cross_encoder/training_overview.html) — `mine_hard_negatives` parameters, evaluation with `CrossEncoderRerankingEvaluator`.
- [sentence-transformers GitHub](https://github.com/huggingface/sentence-transformers) — reference implementation of `CrossEncoder`.

## Security

N/A — reference content describing a technique, not software. Implementations (e.g., sentence-transformers' `CrossEncoder`, Apache-2.0) are installed separately by practitioners.
