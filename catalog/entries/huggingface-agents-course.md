---
name: huggingface-agents-course
title: HuggingFace Agents Course
url: "https://huggingface.co/learn/agents-course/unit1/dummy-agent-library"
category: reference
summary: "Free framework-agnostic course on AI agent fundamentals — covers tool-calling loop mechanics (Thought/Action/Observation), stop-token control to prevent hallucinated observations, system prompt construction, and hands-on progression from dummy agents to smolagents/LangGraph/LlamaIndex"
tags: [agents, course, huggingface, smolagents, tutorial, tool-calling]
reviewed: 2026-06-26
acquired: 2026-06-26
license: unlicensed
security_flags: []
overlaps: [smolagents, huggingface-llm-course]
source: unknown
---

## What it says

A free, multi-unit course from HuggingFace teaching AI agent concepts from first principles. Unit 1 builds a "dummy agent" — a raw Python implementation of the Thought → Action → Observation loop — to demonstrate the mechanics before introducing frameworks. Subsequent units cover smolagents, LangGraph, and LlamaIndex.

The course is deliberately framework-agnostic in its conceptual teaching, using a minimal Python function as a Tool and a HuggingFace Serverless API (InferenceClient) as the LLM backend. Each unit includes runnable notebooks.

## Key takeaways

- Demonstrates the core agent loop: system prompt with tool descriptions → LLM generates Thought + Action JSON → generation stops at "Observation:" token → real tool executes → result injected as Observation → generation resumes.
- Highlights the hallucinated-observation problem: without a stop token, models fabricate tool results. The `stop=["Observation:"]` parameter prevents this.
- Shows that the "agent library" abstraction is primarily system-prompt construction + stop-token management + tool dispatch — demystifies what frameworks do under the hood.
- Uses HuggingFace's Serverless Inference API with `InferenceClient`, providing free model access for experimentation.

## Mechanical details

- **Format:** Multi-unit online course with Jupyter notebooks.
- **LLM backend:** HuggingFace Serverless API via `huggingface_hub.InferenceClient`.
- **Progression:** Dummy agent (raw Python) → smolagents → LangGraph → LlamaIndex.
- **Prerequisites:** Basic Python. No framework installation required for Unit 1.

## Security

Educational content — no software artifact to assess.