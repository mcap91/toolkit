---
name: llama-index
title: LlamaIndex
url: "https://github.com/run-llama/llama_index"
category: framework
summary: "Open-source Python data framework for building LLM/RAG and document-agent apps: data connectors, indices/graphs, retrievers, and query engines to augment LLMs with private data, with 300+ integration packages (LLMs, embeddings, vector stores) on LlamaHub. Pairs with the commercial LlamaParse/Parse agentic-OCR platform. MIT."
license: MIT
tags: [rag, llm, data-framework, retrieval, vector-store, document-agents, ocr, llamaparse]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it does

LlamaIndex is an open-source Python framework for building LLM applications over private data. It provides data connectors to ingest sources and formats (APIs, PDFs, docs, SQL), ways to structure data as indices and graphs, and a retrieval/query interface that returns knowledge-augmented output for a given prompt. A high-level API can ingest and query data in a few lines; lower-level APIs allow customizing connectors, indices, retrievers, query engines, and rerankers. It integrates with outer frameworks (LangChain, Flask, Docker, and others).

The library is namespaced: `llama-index` is a starter package bundling core plus common integrations, while `llama-index-core` installs core alone for pairing with any of 300+ integration packages on LlamaHub. LlamaParse/Parse is the company's separate commercial platform for agentic OCR, parsing, extraction, and indexing (130+ formats), usable with the framework or standalone.

## Mechanical details

- **Install:** `pip install llama-index` (starter) or `pip install llama-index-core` plus chosen integration packages (e.g. `llama-index-llms-openai`, `llama-index-embeddings-huggingface`, `llama-index-llms-ollama`)
- **Minimal RAG:** `SimpleDirectoryReader(...).load_data()` → `VectorStoreIndex.from_documents(...)` → `index.as_query_engine().query(...)`; persist with `index.storage_context.persist()`
- `llama-index-core` ships an `_static` folder (nltk/tiktoken caches) whose build provenance is verifiable via GitHub `attest-build-provenance` / `gh attestation verify`

## Security

MIT licensed. LlamaIndex orchestrates calls to third-party LLM/embedding/vector-store providers using credentials the caller supplies (e.g. `OPENAI_API_KEY`); those integrations make outbound API calls. The 300+ optional integration packages are a broad dependency surface — install only what an application needs. Build assets in `llama-index-core/_static` can be verified against the repo via GitHub build-provenance attestations. No security flags recorded from the observed material.

## Usage notes

- As of 2026, the core orchestration primitive is **Workflows** (event-driven, async-first, step-based execution) — Query Pipelines are deprecated. Agent classes include `FunctionAgent` and `ReActAgent`.
- **LlamaAgents** (`run-llama/llama-agents`) is a separate repo for building and deploying document-centric agents; uses the Workflows primitive under the hood.
- The `run-llama` org also ships a standalone Rust document parser (12k+ stars) and `llamactl` CLI for one-command agent deployment.
- ACP (Agent Client Protocol) integration landed in 2026, enabling interop with other agent frameworks.

## How to use it

pip install llama-index
