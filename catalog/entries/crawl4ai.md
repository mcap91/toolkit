---
name: crawl4ai
title: Crawl4AI
url: "https://github.com/unclecode/crawl4ai"
category: framework
summary: "Best-in-class async web-to-Markdown crawler for agent/RAG pipelines, but Docker API has had dense critical CVEs; library mode is safe to pilot"
tags: [web-scraping, markdown, rag, agents, async, playwright, docker, llm-extraction]
reviewed: 2026-06-10
acquired: 2026-06-10
license: Apache-2.0
security_flags: [docker-api-rce-history, ssrf-history, unaudited-litellm-fork, hook-sandbox-escape-history]
overlaps: []
source: unknown
---

## What it does

Crawl4AI is an async Python web crawling framework that converts web pages into clean, LLM-ready Markdown for RAG pipelines, agents, and structured data extraction. It wraps Playwright (Chromium/Firefox/WebKit) with an `AsyncWebCrawler` API, an async browser pool, caching, and a CLI (`crwl`).

Core capabilities:

- **Markdown output modes:** raw, "fit" (BM25-filtered noise removal), and citation-annotated variants
- **Structured extraction:** CSS/XPath schema extraction (no LLM needed), LLM-driven extraction via any provider (through a litellm fork), chunking strategies
- **Deep crawling:** BFS/DFS/BestFirst strategies with crash recovery (`resume_state`), prefetch mode (5-10x faster for URL discovery only), adaptive crawling that learns site patterns
- **Browser control:** stealth/undetected mode, Shadow DOM flattening, virtual scroll, session persistence, proxy chains with anti-bot escalation, custom hooks at 8 pipeline points
- **Deployment:** Docker image with FastAPI server, JWT auth, monitoring dashboard, MCP integration (direct connection to AI tools)
- **CLI:** `crwl <url> -o markdown`, deep crawl flags, LLM question mode

## Assessment

Crawl4AI is the correct choice when an agent workflow needs to turn arbitrary web URLs into clean Markdown or structured JSON without building a crawler from scratch. It covers the full range from simple single-URL fetches to large multi-hop deep crawls with crash recovery. The 51K+ star community and active release cadence (multiple releases per month in 2025) indicate sustained maintenance.

The `pilot` verdict (not `adopt`) is driven by two concerns:

1. **Docker API security track record.** Versions 0.8.5–0.8.9 patched RCE via deserialization, hook sandbox escapes, hardcoded JWT secrets, SSRF on multiple endpoints, arbitrary file write, monitor auth bypass, stored XSS, and unauthenticated JS execution — all in the self-hosted Docker API server. The library-only mode (no Docker API server) does not expose these surfaces, but the churn indicates the hosted mode is not yet hardened enough for production without additional network controls.
2. **litellm fork dependency.** After a PyPI supply chain compromise of the upstream `litellm` package, the project replaced it with `unclecode-litellm` — a private fork maintained by the same single author. This fork is less auditable than a well-known upstream and creates a single-maintainer supply chain dependency for all LLM extraction features.

For bioinformatics agent workflows that need web data (literature scraping, database fetching, tool documentation ingestion), the Python library mode is the right adoption surface. Avoid exposing the Docker API server to untrusted networks without additional hardening.

## Mechanical details

**Install:**
```bash
pip install -U crawl4ai
crawl4ai-setup   # installs Playwright browsers
crawl4ai-doctor  # verify
```

**Minimal usage:**
```python
from crawl4ai import AsyncWebCrawler

async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://example.com")
    print(result.markdown)  # clean Markdown
```

**BM25-filtered output (fit_markdown):**
```python
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai import CrawlerRunConfig

config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.48)
    )
)
result = await crawler.arun(url=url, config=config)
print(result.markdown.fit_markdown)
```

**CSS/XPath schema extraction (no LLM):**
```python
from crawl4ai import JsonCssExtractionStrategy, CrawlerRunConfig

schema = {"name": "Items", "baseSelector": ".item", "fields": [{"name": "title", "selector": "h2", "type": "text"}]}
config = CrawlerRunConfig(extraction_strategy=JsonCssExtractionStrategy(schema))
result = await crawler.arun(url=url, config=config)
# result.extracted_content is JSON
```

**Deep crawl with crash recovery:**
```python
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai import CrawlerRunConfig

strategy = BFSDeepCrawlStrategy(max_depth=3, resume_state=saved_state, on_state_change=save_checkpoint)
config = CrawlerRunConfig(deep_crawl_strategy=strategy)
```

**Docker (avoid exposing publicly):**
```bash
docker pull unclecode/crawl4ai:latest
docker run -d -p 11235:11235 --shm-size=1g unclecode/crawl4ai:latest
```

The Docker server exposes `/crawl`, `/task/{id}`, `/dashboard`, `/playground`, and monitor endpoints. MCP integration allows direct connection from Claude Code.

## Security

**License:** Apache-2.0 — permissive, no copyleft obligations.

**Security flags:**

- `docker-api-rce-history` — v0.8.5–0.8.7 fixed multiple RCE vectors in the Docker API server: eval()-based deserialization in `/crawl`, AST sandbox escape, hook sandbox RCE. If running the Docker server, stay on the latest release.
- `ssrf-history` — SSRF on webhook, crawl, and proxy endpoints patched across v0.8.7, v0.8.8, v0.8.9. As of 0.8.9, proxy destinations are validated like crawl URLs, but SSRF hardening has required three sequential patches; a "larger secure-by-default release with breaking changes" is forthcoming.
- `hook-sandbox-escape-history` — Hooks execute user-provided Python functions at 8 pipeline points. The sandbox was escaped in 0.8.7; hooks are now disabled by default in Docker (`CRAWL4AI_HOOKS_ENABLED=false`). In library mode, hooks run in-process with full permissions — treat as trusted code.
- `unaudited-litellm-fork` — LLM extraction uses `unclecode-litellm` (a fork replacing the compromised upstream `litellm`). This is a single-maintainer fork with less community audit coverage than a mainstream package.

**Mitigations for production use:**
- Use library mode only; do not expose the Docker API server to untrusted networks.
- If Docker server is required, place behind an authenticating reverse proxy, restrict to localhost, and set `CRAWL4AI_HOOKS_ENABLED=false`.
- Pin the version (`pip install crawl4ai==0.8.9`) and review changelogs before upgrades.
- Avoid LLM extraction features if `unclecode-litellm` supply chain provenance is a concern; CSS/XPath extraction has no such dependency.
