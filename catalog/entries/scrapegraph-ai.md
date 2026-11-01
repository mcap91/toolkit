---
name: scrapegraph-ai
title: ScrapeGraphAI
url: "https://github.com/ScrapeGraphAI/Scrapegraph-ai"
category: framework
summary: "Python web-scraping library that uses LLMs plus graph-based pipelines (SmartScraperGraph, SearchGraph, SpeechGraph, ScriptCreatorGraph, and multi-page variants) to extract structured data from websites and local documents (HTML, XML, JSON, Markdown); MIT-licensed open-source core with a separate paid managed cloud API/SDKs"
tags: [web-scraping, llm, python, data-extraction, mcp-server, agent-tooling]
reviewed: 2026-08-25
acquired: 2026-08-25
license: MIT
security_flags: [telemetry-enabled-by-default]
overlaps: []
source: unknown
---

## What it does / What it says

ScrapeGraphAI is a Python library that combines LLMs with graph-based scraping pipelines to extract information from web pages and local documents (XML, HTML, JSON, Markdown, etc.) given a natural-language prompt and a source. It ships several pipeline classes: `SmartScraperGraph` (single page), `SearchGraph` (multi-page, top-N search results), `SpeechGraph` (page-to-audio), `ScriptCreatorGraph` (generates a Python scraping script), plus `*MultiGraph` variants that parallelize LLM calls across multiple sources given one prompt.

The project distinguishes an open-source self-hosted library (this repo) from a separate managed cloud API (`scrapegraph-py` / `scrapegraph-js` SDKs, billed per credit) that adds managed browser rendering, proxies/anti-bot handling, crawling, and scheduled monitoring.

## Differentiators / Key takeaways

- LLM-backend agnostic: works with OpenAI, Groq, Azure, Gemini, MiniMax, and local models via Ollama; configured via a `graph_config` dict passed to each pipeline.
- Integrates with LangChain, LlamaIndex, Crew.ai, Agno, CamelAI, and low-code platforms (Pipedream, Bubble, Zapier, n8n, Dify, Toolhouse); ships an MCP server and official Python/Node SDKs.
- Requires Playwright for live website fetching (`playwright install` after `pip install scrapegraphai`).

## Mechanical details / What to adopt

Install via `pip install scrapegraphai` (recommended inside a virtualenv) plus `playwright install`. Instantiate a pipeline (e.g., `SmartScraperGraph`) with a prompt, source URL/file, and an LLM config dict, then call `.run()`; output is a JSON-serializable dict matching the requested extraction.

## Security

MIT license. The library collects anonymous usage telemetry by default; opt out via `SCRAPEGRAPHAI_TELEMETRY_ENABLED=false`. The README states the library "is meant to be used for data exploration and research purposes only" and disclaims responsibility for misuse. No CI/test/dependency-health details were surfaced in the fetched README; not independently verified beyond GitHub-reported star count (~20k+ as of mid-2026 per third-party sources).
