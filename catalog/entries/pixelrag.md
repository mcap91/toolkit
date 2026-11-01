---
name: pixelrag
title: PixelRAG
url: https://github.com/StarTrail-org/PixelRAG
category: framework
summary: Open-source RAG framework from Berkeley Sky Computing Lab/BAIR/Berkeley NLP that renders web pages, PDFs, and images to screenshot tiles and retrieves over the images directly (via a LoRA-fine-tuned Qwen3-VL-Embedding-2B model) instead of parsing text, preserving tables/charts/layout; supports text or image queries; ships a hosted API over a pre-built 8.28M-page Wikipedia index, a Claude Code plugin (pixelbrowse) that lets Claude screenshot and read a page instead of fetching raw HTML, FAISS or Qdrant backends, and a separate LoRA training pipeline; Apache-2.0
tags:
  - rag
  - visual-rag
  - screenshot
  - multimodal-retrieval
  - vision-language-model
  - qwen
  - faiss
  - qdrant
  - claude-code-plugin
  - web-scraping-alternative
  - document-retrieval
reviewed: 2026-10-30
acquired: 2026-10-30
license: Apache-2.0
security_flags:
  - docker-root-sandbox-disabled
  - untested-docker-build
overlaps: []
source: instagram
source_url: https://www.instagram.com/reel/Dbb38hFCPuc/
---

## What it does

PixelRAG (paper: "PIXELRAG: Web Screenshots Beat Text for Retrieval-Augmented Generation," arXiv:2606.28344, Berkeley Sky Computing Lab/BAIR/Berkeley NLP) renders documents — web pages, PDFs, images — as screenshots and retrieves over the images directly, rather than parsing them to text first. Visual structure that text extraction discards (tables, charts, layout, infographics) stays intact in the retrieved tile, so a reader model can answer questions grounded in the image rather than a lossy text chunk. Queries can be text or an image (true visual search).

Two components: (1) a renderer (`pixelshot`) that converts a page or PDF into image tiles via headless Chromium (Playwright/CDP) or poppler, and (2) a Qwen3-VL-Embedding-2B model, LoRA-fine-tuned on screenshot data, that embeds page images into a retrievable vector space.

## Pipeline

- `pixelshot` — document/URL → screenshot tiles (standalone command, `pip install pixelrag`).
- `pixelrag chunk` / `embed` / `build-index` — tiles → vectors → FAISS (or Qdrant) index (`pip install 'pixelrag[embed]'`).
- `pixelrag index` — orchestrates the full source → ingest → embed → index pipeline (`pip install 'pixelrag[index]'`).
- `pixelrag serve` — FastAPI search API over an index, CPU or GPU (`pip install 'pixelrag[serve]'`).
- Each stage installs and runs independently via pip extras.

## Mechanical details

- Install: `pip install pixelrag`; `uv tool install pixelrag` or `pipx install pixelrag` recommended to keep `pixelshot` on PATH for agent use.
- Hosted, no-setup endpoint: `https://api.pixelrag.ai/search` serves a pre-built index of 8.28M Wikipedia pages (text or image query, no API key).
- Browser demo at pixelrag.ai and a Colab notebook render a page and search the hosted index inline.
- Claude Code plugin (`pixelbrowse` skill): `claude plugin marketplace add StarTrail-org/PixelRAG` then `claude plugin install pixelbrowse@pixelrag-plugins`; invoked via `/screenshot <url>` or natural-language prompts like `claude -p "screenshot https://news.ycombinator.com and summarize the top stories"`. No MCP server or backend — the skill calls local `pixelshot` (Playwright/CDP). Also ships for opencode as the `@startrail/pixelbrowse` npm package.
- Local index build: write a `pixelrag.yaml` (source path, embed model `Qwen/Qwen3-VL-Embedding-2B`, `device: auto` for CUDA/MPS/CPU), then `pixelrag index build` and `pixelrag serve --index-dir ./my_index --port 30001`. Works on Linux (CUDA) and macOS (Apple Silicon/MPS); README reports ~3 min to index one PDF on Apple M-series, ~1 min on GPU.
- PDF support needs the `[pdf]` extra and poppler.
- Pre-built FAISS indexes (base/LoRA Wikipedia-pixel, Wikipedia-text, news-pixel; ~217G for the base Wikipedia index) are distributed via the Hugging Face dataset `StarTrail-org/pixelrag-faiss-indexes`.
- Qdrant is an optional backend for quantized/disk-backed vectors, payload filtering, and sharing one collection across multiple `pixelrag serve` instances; FAISS remains the default for local indexes.
- Training (LoRA fine-tune of `Qwen/Qwen3-VL-Embedding-2B`) lives in a separate `train/` uv project with its own pinned env (torch 2.9.1+cu129, transformers 4.57.1, cuDNN 9.20); published adapters (`Chrisyichuan/wiki-screenshot-embedding-lora`) and training set (`Chrisyichuan/screenshot-training-natural-filtered-v2`) mean retraining is optional.
- Docker image (Dockerfile + docker-compose) bundles the `serve` extra and a pinned Chromium; the README states CI does not build this image ("best-effort, can drift") and on Apple Silicon it builds without a renderer (the pinned `headless_shell` is published linux-x64 only).

## Security

- License: Apache-2.0.
- The README states the Docker container runs as root with Chrome's sandbox disabled, because enabling the sandbox would require `--cap-add=SYS_ADMIN` or a tailored seccomp profile; it explicitly warns to keep the container isolated and "not point it at untrusted pages otherwise." Flagged as `docker-root-sandbox-disabled`.
- Flagged as `untested-docker-build`: the README states nothing in CI builds the Docker image, so it can drift from the current pip package and should be verified before relying on it.
- No eval()/injection patterns observed in the fetched README; full source not reviewed line-by-line.

## Usage notes

- Captured via an Instagram reel whose on-screen text and transcript frame this as making "web scraping dead," citing traditional scrapers' failure to capture images/graphs/tables and their breakage on blocked sites/social accounts — these are the reel creator's promotional framing, not claims verified in the project's own README (source: https://www.instagram.com/reel/Dbb38hFCPuc/).