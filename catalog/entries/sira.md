---
name: sira
title: SIRA (Superintelligent Retrieval Agent)
url: "https://github.com/facebookresearch/sira"
category: framework
summary: "Meta (FAIR) research pipeline that uses LLMs to enrich both documents and queries to improve BM25 retrieval without training. Five stages: data prep, BM25 indexing, corpus enrichment (LLM indexing phrases), query expansion (LLM search terms), and LLM pointwise reranking; reports SOTA on BEIR using only inference-time compute. MIT."
license: MIT
tags: [information-retrieval, bm25, rag, reranking, query-expansion, llm, beir, meta]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it does

SIRA (Superintelligent Retrieval Agent) is a research codebase from Meta's FAIR (facebookresearch) implementing a multi-stage retrieval pipeline that uses LLMs to enrich both documents and queries, improving BM25 retrieval quality without any training. The pipeline has five stages: data preparation, BM25 indexing, corpus enrichment (LLM-generated indexing phrases added to documents), query expansion (LLM-generated search terms), and LLM-based pointwise reranking. The authors report state-of-the-art results on the BEIR benchmark suite using only inference-time compute (no fine-tuning). It ships a configurable pipeline runner that can process one or many BEIR datasets and run selected stages, and can auto-start a local LLM server. Introduced in the paper "Superintelligent Retrieval Agent: The Next Frontier of Information Retrieval" (arXiv 2605.06647).

## Mechanical details

- **Requirements:** Python ≥ 3.12, a CUDA-capable GPU (tested on NVIDIA H100), the Rust toolchain (to build the `bm25x` extension), and Conda (recommended)
- **Install:** `conda create -n sira312 python=3.12 -y && conda activate sira312 && pip install -e .`, then `source sandbox.sh`
- **Run:** `python scripts/run_pipeline.py data=scifact server.auto_start=true`; multiple datasets via `datasets='[scifact,arguana,fiqa]'`; specific stages via `stages='[enrich_query,rerank]'`

## Security

MIT licensed; the `src/sira/bm25x/` directory derives from LightOn's `bm25x` (Apache-2.0, see NOTICE). SIRA is research code that runs local LLM inference on a GPU; enrichment/reranking stages invoke an LLM server (auto-started locally by default). No security flags recorded from the observed material.

## How to use it

conda create -n sira312 python=3.12 && pip install -e .
