---
name: prompt-assembly-cache-discipline
title: Prompt Assembly and Cache Discipline
category: agent-pattern
summary: "Rules for LLM prompt assembly that preserve KV-cache efficiency — never rewrite the front of a prompt (invalidates cached tokens), avoid sliding windows that evict oldest turns (same cost), cap fat messages in-place to stay cacheable, put retrieval/per-query content last as a suffix so changes do not poison the cached prefix; includes five-layer assembler concept and ablation methodology"
tags: [prompt-engineering, kv-cache, context-management, token-efficiency, prompt-assembly, caching]
reviewed: 2026-09-18
acquired: 2026-09-18
license: ""
security_flags: []
overlaps: []
source: unknown
---

## What it does

A set of rules for assembling LLM prompts that preserve KV-cache efficiency:

1. Do not rewrite the front: summarizing conversation history rewrites the beginning of the prompt, forcing recomputation of every cached token behind it
2. Sliding windows are expensive: evicting the oldest turn from the front has the same cache-invalidation cost as summarization
3. Cap in place: truncating an oversized message without moving it preserves its position in the cache
4. Retrieval goes last: per-query content (RAG results, search hits) placed as a suffix means changes cannot invalidate the cached prefix
5. Measure without API calls: use a validity gate that voids a run if a probe question could be answered by a different mechanism

The source also describes a five-layer prompt assembler architecture, an ablation ladder (each rung adds one mechanism), and a technique for identifying which layer earns its token budget.

## Security

No security implications; this is a prompt engineering technique.