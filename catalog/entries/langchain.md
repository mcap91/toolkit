---
name: langchain
title: LangChain
url: https://github.com/langchain-ai/langchain
category: framework
summary: Open-source (MIT) LLM application framework providing composable components — chains, runnables, tools, retrievers, prompts — for building model-agnostic agents; as of 2026, its create_agent ReAct-pattern agents run on LangGraph's durable runtime, inheriting persistence, checkpointing, rewind, and human-in-the-loop support rather than implementing orchestration independently.
tags:
  - llm-framework
  - agents
  - orchestration
  - open-source
  - rag
  - tools
  - python
  - langgraph
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT
security_flags: []
overlaps:
  - langgraph
  - langsmith
  - llama-index
  - langflow
source: text
---

## What it does

A framework for building LLM applications from composable parts: chains (sequences of calls), runnables (the common interface those calls implement), tools, retrievers, and prompts. Historically positioned as the orchestration layer itself, but by 2026 LangChain's own agent constructor (`create_agent`) builds on LangGraph's durable runtime rather than a separate execution model — so LangChain agents inherit LangGraph's persisted state, step-level resumability, and human-in-the-loop checkpoints. Control flow in LangChain proper is mostly sequential with some branching; loops, conditional routing, and multi-agent coordination as first-class constructs are LangGraph's domain. The two layers are separable: LangGraph runs without LangChain's components, and LangChain's components can be used without adopting LangGraph's graph abstraction directly.

## Sources

- [LangChain vs LangGraph: Key Differences — sim.ai](https://www.sim.ai/library/langchain-vs-langgraph)
- [LangChain — Open Source AI Agent Framework](https://www.langchain.com/langchain)

## Security

MIT, fully open source.
