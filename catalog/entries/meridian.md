---
name: meridian
title: Meridian
url: "https://github.com/Rajsuthan/meridian"
category: framework
summary: "GPU-accelerated document processing pipeline — Docling (8 load-balanced instances) for PDF layout detection, Qwen3-VL via vLLM for table/figure/formula reading, Ollama for embeddings, Qdrant for vector storage; stateless Celery workers on CPU calling long-lived GPU services over HTTP; measured at 118 pages/min on a single H200; includes text-only path (pypdfium2, 1000 docs/min on CPU); Apache-2.0"
tags: [document-parsing, ocr, vlm, vllm, docling, qdrant, celery, gpu, pdf, table-extraction, embeddings, qwen, batch-processing]
reviewed: 2026-09-03
acquired: 2026-09-03
license: Apache-2.0
security_flags: []
overlaps: [unstructured, docling-mcp]
source: unknown
---

## What it does

Meridian is a GPU-accelerated pipeline for converting PDFs (including scanned documents with tables, figures, and formulas) into searchable vector embeddings. It orchestrates multiple services through stateless Celery workers that call long-lived GPU services over HTTP.

The six-step pipeline per document:

1. **Docling**: parse PDF, detect layout, extract table/figure/formula regions (8 load-balanced instances with round-robin via Redis atomic counter, failover, and watchdog auto-restart)
2. **Annotate**: draw numbered boxes on formula pages so the VLM can identify which formula is being asked about
3. **VLM**: send all tables, figures, and annotated formula pages concurrently to vLLM (Qwen3-VL-8B default) or AWS Bedrock
4. **Chunk**: build ordered document chunks with injected VLM descriptions in the correct reading-order positions
5. **Embed**: generate vector embeddings via Ollama
6. **Store**: persist embeddings and metadata in Qdrant

Architecture: stateless CPU workers → long-lived GPU services (Docling, vLLM, Ollama) + infrastructure (Redis as Celery broker + batch state, Qdrant for vectors). Models load once and are shared across workers rather than each worker loading its own copy.

## Differentiators

- Measured throughput: 118.7 pages/min on academic papers, 77–83 pages/min on scan-heavy NASA Apollo reports, on a single H200
- Throughput comes from many documents in different pipeline stages simultaneously, not from any single document being fast (~10 pg/min for a single doc)
- 8-instance Docling load balancing with automatic failover and 30-second watchdog auto-restart
- Pluggable VLM backend: local vLLM (default) or AWS Bedrock when no GPU is available for the vision model
- Batch orchestration: submit/pause/resume/retry with full Redis state tracking
- GPU memory management: cleanup after each document to prevent VRAM accumulation across long batches
- Adaptive image scaling based on file size (2.0x for small, 0.75x for large)
- Also ships a text-only path (pypdfium2) that processed 1,000 NASA docs (78K pages) in under a minute on 32 CPU workers — no tables/figures/formulas, just bulk text
- Honest performance reporting: SETUP_NOTES.md includes tuning tables, bugs found, and what did not work

## Mechanical details

- Language: Python, pip-installable with `[gpu]` and `[bedrock]` extras
- CLI: `meridian submit`, `meridian status`, `meridian resume`, `meridian retry`, `meridian pause`, `meridian failed`, `meridian list`, `meridian clear`
- Services: Docling (ports 8001–8008), vLLM (port 8000), Ollama (port 11434), Redis (port 6379), Qdrant (port 6333)
- Default VLM: Qwen/Qwen3-VL-8B-Instruct; Bedrock alternative: us.amazon.nova-2-lite-v1:0
- Deployment: shell scripts (`make start`) or Docker Compose for full stack
- Configuration: environment variables with sensible defaults (see `docs/configuration.md`)
- Test hardware: single NVIDIA H200 (143 GB) on RunPod
- Includes Bedrock cost benchmark script (`examples/bedrock_cost_benchmark.py`) for projecting API costs

## Security

- Apache-2.0 license
- AWS credentials for Bedrock follow standard boto3 chain (env/config/instance role), never read from Meridian's config
- No eval() or shell injection patterns observed
- All services communicate over localhost HTTP by default
- Single-author project (Raj); open-sourced from production use in aerospace and finance document processing