---
name: open-webui
title: Open WebUI
url: "https://github.com/open-webui/open-webui"
category: framework
summary: "Leading self-hosted LLM web UI with RAG, pipelines, and enterprise auth — relevant infrastructure context but custom non-SPDX license limits adoption"
tags: [llm-ui, self-hosted, rag, ollama, openai-compatible, pipelines, enterprise, docker, python]
reviewed: 2026-06-10
acquired: 2026-06-10
license: LicenseRef-OpenWebUI
security_flags: [custom-license, byof-code-execution, pipeline-code-execution]
overlaps: [onyx-ai-platform]
source: unknown
---

## What it does

Open WebUI is a self-hosted, offline-capable web application that provides a ChatGPT-style interface for any Ollama or OpenAI-compatible LLM backend. It bundles a comprehensive feature set in a single deployable unit: local RAG (9 vector DB options, Tika/Docling/OCR extraction engines), web search (15+ providers), image generation (DALL-E, ComfyUI, AUTOMATIC1111), voice/video calls (Whisper, Deepgram, ElevenLabs), a Python function-calling tool workspace (Bring Your Own Function), and a Pipelines plugin framework for custom middleware. Enterprise features include LDAP/AD, SCIM 2.0, SSO/OAuth, RBAC, Redis-backed horizontal scaling, OpenTelemetry observability, and cloud storage backends (S3, GCS, Azure Blob). Installed via `pip install open-webui` or Docker; runs at localhost:8080/3000.

## Assessment

Open WebUI is the dominant open-source self-hosted LLM UI project by adoption and feature breadth — awareness of it is valuable for anyone building or deploying LLM infrastructure. However, it is not a Claude Code skill, MCP server, agent pattern, or CLI tool that integrates directly into this toolkit's workflows. The custom "Open WebUI License" (branding preservation requirement) is not a standard SPDX identifier and introduces uncertainty about redistribution and embedding. The Pipelines framework and BYOF Python execution surface are powerful but represent meaningful code-execution attack surface. Cataloged as `watch` — monitor for a Pipelines-based MCP bridge or bioinformatics-specific integration that would warrant a `pilot` upgrade.

## Mechanical details

- **Install**: `pip install open-webui` (Python 3.11 required) or `docker run ghcr.io/open-webui/open-webui:main`
- **GPU support**: `:cuda` Docker image; requires Nvidia CUDA container toolkit on Linux/WSL
- **Bundled Ollama**: `:ollama` image ships both Open WebUI and Ollama in one container
- **RAG**: `#` command in chat to reference docs or URLs; supports ChromaDB, PGVector, Qdrant, Milvus, Elasticsearch, OpenSearch, Pinecone, S3Vector, Oracle 23ai
- **Pipelines**: Separate plugin server; set OpenAI URL to Pipelines URL to intercept/augment requests — enables rate limiting, usage monitoring (Langfuse), live translation, filtering
- **BYOF**: Pure Python functions added via web editor become callable tools for the LLM
- **Scaling**: Redis session backend + WebSocket multi-worker support for load-balanced deployments
- **Storage**: SQLite (default, optional encryption), PostgreSQL, or cloud blob backends
- **Auth**: Local accounts, LDAP/AD, SCIM 2.0 (Okta, Azure AD, Google Workspace), SSO via trusted headers or OAuth

## Security

- **License**: Custom "Open WebUI License" with mandatory branding preservation — not a recognized SPDX identifier; review `LICENSE` and `LICENSE_HISTORY` before embedding or redistributing. Prior contributions may be under separate original licenses.
- **BYOF / Pipelines code execution**: The Python function calling workspace and Pipelines framework execute arbitrary Python server-side. Any user with tool-creation permissions can run code in the server process — treat this as a privileged capability requiring strict RBAC enforcement.
- **API key handling**: OpenAI API key passed via environment variable (`OPENAI_API_KEY`) — standard practice but ensure the Docker volume and env are not world-readable.
- **Network exposure**: Default Docker run exposes port 3000 publicly; the `--restart always` flag means the container auto-restarts. Ensure firewall rules or a reverse proxy with auth are in place before exposing to a network.
- **Supply chain**: Large project with many contributors; no mention of signed releases in the README. Dependency pinning not visible from the README alone — review `requirements.txt`/`pyproject.toml` before production use.
- **Offline mode**: `HF_HUB_OFFLINE=1` prevents Hugging Face model downloads — recommended for air-gapped or security-sensitive deployments.
