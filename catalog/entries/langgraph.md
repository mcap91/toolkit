---
name: langgraph
title: LangGraph
url: https://github.com/langchain-ai/langgraph
category: framework
summary: Open-source (MIT) low-level agent-orchestration engine built around a directed graph of nodes and edges over shared state — supports loops, conditional routing, and multi-agent coordination as first-class constructs, with persisted state that survives steps (resumable from the last successful node, step-level checkpointing, human-in-the-loop interrupts). LangChain's own agents run on this runtime as of 2026 rather than a separate execution model; LangGraph itself runs standalone without LangChain's components.
tags:
  - agent-orchestration
  - graph-execution
  - state-machine
  - open-source
  - durable-runtime
  - python
  - langchain
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT
security_flags: []
overlaps:
  - langchain
  - langsmith
source: text
---

## What it does

The execution engine beneath both standalone agent code and LangChain's higher-level agent constructors. Where LangChain's native abstraction is the chain/runnable, LangGraph's core abstraction is a directed graph of nodes and edges operating over shared, persisted state. This makes loops, conditional routing, and multi-agent coordination first-class — not something bolted onto a sequential chain. Because state persists between steps, a failed run can resume from its last successfully completed node rather than restarting from scratch, and human-in-the-loop interrupts can pause execution at a checkpoint. LangGraph is separable from LangChain: it runs fine without LangChain's components, and `create_agent`-style LangChain agents run on top of it as of 2026 rather than on an independent orchestration path.

## Sources

- [LangChain vs LangGraph: Key Differences — sim.ai](https://www.sim.ai/library/langchain-vs-langgraph)
- [LangGraph Pricing: A Complete Breakdown for 2026 — TrueFoundry](https://www.truefoundry.com/blog/langgraph-pricing)

## Security

MIT, fully open source.
