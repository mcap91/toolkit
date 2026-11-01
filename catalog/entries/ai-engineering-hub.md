---
name: ai-engineering-hub
title: AI Engineering Hub
url: "https://github.com/patchy631/ai-engineering-hub"
category: reference
summary: "Curated collection of 93+ hands-on tutorial projects for LLM/RAG/agent engineering, organized by difficulty (beginner/intermediate/advanced), covering OCR, chat UIs, RAG variants, MCP integrations, model comparisons, fine-tuning, and production agent systems"
tags: [llm, rag, agents, mcp, tutorials, fine-tuning, multimodal, crewai, llamaindex]
reviewed: 2026-09-25
acquired: 2026-09-25
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does / What it says

GitHub repository maintained by Akshay Pachaar (patchy631), a Sr. AI Engineer & Developer Advocate at
Lightning AI. It is a collection of 93+ project-based tutorials for AI/LLM engineering, each living in
its own subdirectory with runnable code. Projects are grouped into three difficulty tiers:

- **Beginner (22 projects)**: OCR & vision (LaTeX/Llama/Gemma-3/Qwen 2.5 OCR apps), local ChatGPT-style
  chat UIs (DeepSeek, Llama 3.2, Gemma 3, "thinking" UIs with visible reasoning), basic RAG (LlamaIndex +
  Ollama, GitHub-repo RAG, ModernBERT RAG, Llama 4 RAG), multimodal/media apps (Janus-Pro image
  generation, Gemini video RAG), and misc tools (FireCrawl website-to-API, CrewAI news generator, a
  Siamese-network digit-similarity demo).
- **Intermediate (48 projects)**: agentic workflows (CrewAI, AutoGen, CrewAI Flow), voice/audio agents
  (AssemblyAI, Cartesia), advanced RAG (Docling, TLM "trustworthy RAG," Milvus+Groq low-latency
  retrieval, RAG+SQL routing), multimodal RAG, a cluster of MCP (Model Context Protocol) integration
  projects (Cursor+Linkup, EyeLevel, LlamaIndex, Firecrawl, Ragie video RAG, KitOps, Stagehand), and
  head-to-head model-comparison writeups (Llama 4 vs DeepSeek-R1, O3 vs Claude 3.7, Sonnet 4 vs
  O4/Qwen3-Coder, GPT-OSS vs Qwen3).
- **Advanced (23 projects)**: fine-tuning (DeepSeek + Unsloth, a from-scratch reasoning-model build, a
  from-scratch Transformer implementation), advanced agent systems (CrewAI Flows + NVIDIA NIM doc writer,
  MCP-powered multi-agent deep researcher, browser automation via Stagehand, a paralegal agent, corrective
  RAG, context-engineering workflow with TensorLake + Zep, a Parlant compliance agent), advanced
  MCP/infrastructure (MindsDB, Graphiti persistent memory, Pixeltable, a multi-MCP "ultimate AI
  assistant"), and two "production system" writeups (GroundX document pipeline, a NotebookLM clone with
  citations and podcast generation).

Each project links to a subdirectory with its own README and code; the top-level README serves purely as
an index/table of contents plus a link to an external "AI Engineering Roadmap" learning path and a
newsletter signup.

## Differentiators / Key takeaways

- Broad framework coverage rather than depth in one stack: CrewAI, AutoGen, LlamaIndex, LangChain-adjacent
  tooling, and multiple MCP client/server integrations all appear as separate worked examples.
- Heavy emphasis on running open-weight models locally (DeepSeek, Llama, Gemma, Qwen) alongside
  cloud-model comparisons (Claude, GPT, o3), useful as a reference for "same task, different model/stack"
  comparisons.
- Distinct from other cataloged reference material (e.g., Claude Cookbook, roadmap.sh) in that every entry
  is a complete, runnable project rather than a conceptual guide or career roadmap node.
- No bioinformatics-specific content; general-purpose AI/LLM engineering tutorials only.

## Mechanical details / What to adopt

- MIT licensed; browse by difficulty tier in the README, then open the linked subdirectory for
  project-specific setup/run instructions (each project manages its own dependencies).
- ~37.8k GitHub stars / 6.2k forks as of September 2026; was featured on GitHub Trending (#2, March 2025);
  actively maintained (97 open / 98 closed PRs at time of review), with new projects added regularly.
- Useful as a scan-for-patterns reference when evaluating an unfamiliar framework (CrewAI Flow, MCP
  server/client patterns, Stagehand browser automation, Graphiti memory) — pull the relevant subdirectory
  rather than adopting the repo wholesale.

## Security

No aggregate security review performed — this is a loosely-curated tutorial collection where each of the
93+ subprojects has independent dependencies (many pinned to specific model providers/API keys via `.env`
files, per typical LLM-tutorial convention). Treat each subproject as its own supply-chain surface; audit
before running rather than trusting the collection as a whole. No tests or CI apply at the repo level
(index-only top-level README).
