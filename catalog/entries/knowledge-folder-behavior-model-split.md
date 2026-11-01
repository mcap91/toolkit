---
name: knowledge-folder-behavior-model-split
title: "Knowledge in the Folder, Behavior in the Model: A Fine-Tuning vs. RAG Split"
url: https://www.instagram.com/reel/DfAmYQQDsNW/
source_url: https://www.instagram.com/reel/DfAmYQQDsNW/
source: instagram
category: agent-pattern
summary: "A three-step strategy for deciding what to fine-tune versus what to retrieve: keep facts (pricing, policies, specs) in documents the model reads at answer time rather than baking them into weights, since fine-tuning changes model behavior, not factual recall, so tuning on company documents still produces factual errors; tune only for behavior (output format, tone, how to answer a complaint) using a few hundred clean, human-approved examples of one task rather than thousands of unreviewed ones; and do that tuning on a small open-weight model run on a single workstation, A/B tested against the untuned baseline before deployment."
tags:
  - fine-tuning
  - rag
  - knowledge-vs-behavior
  - open-weight-models
  - sft
  - evaluation
  - model-ownership
reviewed: 2026-10-29
acquired: 2026-10-29
license: N/A
security_flags: []
overlaps:
  - llms-from-first-principles-course
  - five-levels-of-chunking
  - rag-retrieval-recipe
---

## What it does

Argues that teams conflate two different problems when they decide to "fine-tune on our documents": teaching a model *what you know* (facts) versus teaching it *how to behave* (format, tone, decision protocol). Fine-tuning addresses the second, not the first — a model tuned on a document corpus still hallucinates facts, because gradient updates shape response patterns, not a reliable store of retrievable facts. The reel frames this as a three-step split:

1. **Facts go in a folder, not in weights.** Business knowledge that changes often (pricing, policies, specs) should be read by the model at answer time (i.e., retrieved, as in RAG) rather than trained in, so updates don't require retraining and the model always answers from current source documents.
2. **Tune for behavior with a small, curated set.** Collect a few hundred clean examples of one task (e.g., how to write a quote, how to answer a complaint), each approved by the person who does that task best, rather than thousands of unreviewed/messy examples. The claim is that example quality and consistency matter more than volume for behavior tuning.
3. **Tune a model you can host, and test it against the baseline.** Use an open-weight model small enough to fine-tune on a single high-memory workstation (the reel names "Qwen 3.8 27B" as an example, unverified against any actual released model name) rather than a much larger model, and A/B test the tuned version against the untuned original before anyone uses it in production.

This matches the broader industry consensus on RAG-vs-fine-tuning (see Sources): RAG keeps knowledge current, permissioned, and swappable without retraining, while fine-tuning is reserved for narrow, stable behavioral tasks — and most production deployments combine both rather than picking one.

## Notes

- The reel is promotional content signed "-MM" / "FACTION" with hashtags including `#aidirectedengineering`; no product, repo, or named tool is linked — the content is a technique/strategy, not a tool.
- "Qwen 3.8 27B" is named only as an illustrative example of a small open-weight model; no such exact model name could be confirmed, and it is not load-bearing to the strategy itself.
- This is a specific instance of the general RAG-vs-fine-tuning decision framework ([[llms-from-first-principles-course]] AMA heuristics, [[rag-retrieval-recipe]]), adding two concrete operational numbers not found elsewhere in the catalog: "a few hundred clean examples" as a target training-set size for behavior tuning, and "single high-memory workstation" as the hardware bar for owning a tuned small open model.

## Sources

- [Instagram reel (creator signs off as "-MM", posted under "FACTION")](https://www.instagram.com/reel/DfAmYQQDsNW/) — caption, transcript, and key claims (catalog source).

## Security

N/A — a decision framework/strategy, not software. No code or service is distributed by this item.
