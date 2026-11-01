---
name: pullmd
title: PullMD
url: https://github.com/AeternaLabsHQ/pullmd
category: framework
summary: Self-hosted anything-to-Markdown conversion service for AI agents — converts web pages (including Reddit/Hacker News threads with comment trees), PDFs, Office documents, EPUB, images, audio, and YouTube videos (transcripts with timecodes) into clean, boilerplate-stripped Markdown with metadata in YAML frontmatter; multi-strategy extraction (Cloudflare's Markdown endpoint plus parallel Readability/Trafilatura scored for quality); exposed via a PWA, REST API, MCP server, and a Claude Code skill; v3 added a markitdown document-conversion sidecar and an opt-in media tier for image captioning/audio transcription via any OpenAI-compatible endpoint; multi-arch Docker images; AGPL-3.0
tags:
  - markdown-conversion
  - document-parsing
  - self-hosted
  - mcp-server
  - web-scraping
  - pdf
  - reddit
  - youtube-transcripts
  - claude-code-skill
reviewed: 2026-10-29
acquired: 2026-10-29
license: AGPL-3.0
security_flags: []
overlaps: []
source_url: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/
source: reddit
---

## What it does

PullMD takes a URL or uploaded file and returns clean Markdown for agent consumption. As of v3 it handles web pages (static and JS-heavy, with Reddit/Hacker News thread + comment-tree extraction and tunable `comment_depth`/`comment_limit`), documents (PDF, DOCX, PPTX, XLSX, EPUB, ZIP, CSV, JSON, XML via a bundled `markitdown` sidecar), images, audio, and YouTube videos (transcript with timecodes). Extraction picks between Cloudflare's native Markdown endpoint and parallel Readability/Trafilatura runs by a quality score, stripping ads/navigation/boilerplate and moving metadata (source URL, fetch date, subreddit/author/upvotes for Reddit) into YAML frontmatter rather than inline text, reducing token usage for downstream agents. Each conversion gets a refreshable share ID for re-fetching updated content. Access is via a Progressive Web App, a REST API, an MCP server (streaming HTTP), or a dedicated Claude Code skill. An opt-in media tier adds image captioning and audio transcription through any OpenAI-compatible endpoint (cloud or local), running inside the same container.

## Security

AGPL-3.0. Self-hosted, distributed as multi-arch (linux/amd64, linux/arm64) Docker images on Docker Hub and GHCR — operators control where fetched content and any media-tier transcription calls are sent.

## Usage notes

- Mentioned in a Reddit comment (r/Qwen_AI, Oct 2026) as hosted on a Raspberry Pi alongside an unnamed "Hermes agent" that used the commenter's main PC for inference over a LAN API, for converting files and websites to Markdown. No further detail on configuration or version given. (source: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/)
