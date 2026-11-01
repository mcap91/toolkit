---
name: claude-seo
title: Claude SEO
url: "https://github.com/AgricIDaniel/claude-seo"
category: plugin
summary: "Open-source SEO analysis plugin for Claude Code — 25 sub-skills and 18 specialist agents running in parallel across technical SEO, E-E-A-T content quality, Schema.org markup, AI search optimization (GEO), local SEO, e-commerce, and international SEO; falsifiable recommendations with leading indicators; 4-tier Google API integration; 8 optional MCP extensions (Ahrefs, DataForSEO, SE Ranking, etc.); MIT"
tags: [claude-code-plugin, seo, technical-seo, schema-org, ai-search, e-e-a-t, local-seo, ecommerce-seo]
reviewed: 2026-07-06
acquired: 2026-07-06
license: MIT
security_flags: []
overlaps: [claude-skills-rezvani]
source: unknown
---

## What it does

Claude Code plugin that runs parallel SEO audits across 7 domains: technical SEO, content quality (E-E-A-T), Schema.org markup, AI search optimization (GEO/AEO), local SEO, e-commerce SEO, and international SEO. 25 slash commands, 18 specialist agents that can run up to 15 simultaneously.

**Key commands:** `/seo audit <url>` (full parallel site audit), `/seo page <url>` (deep single-page), `/seo technical`, `/seo content`, `/seo schema` (detect/validate/generate), `/seo geo` (AI Overviews optimization), `/seo local` (GBP/NAP/citations), `/seo maps` (geo-grid/GBP audit), `/seo backlinks`, `/seo cluster` (SERP-based semantic clustering), `/seo drift` (SQLite-based monitoring), `/seo ecommerce`, `/seo google` (GSC/PageSpeed/CrUX/GA4/PDF reports).

**4-tier Google API integration:** Tier 0 (API key → PageSpeed/CrUX), Tier 1 (+OAuth → Search Console/Indexing API), Tier 2 (+GA4 config → organic traffic), Tier 3 (+Ads token → Keyword Planner).

## Differentiators

- **Falsifiable recommendations** — every finding carries the first-principle observation, dependency relationships, an explicit "how would we know this failed?" check, and a leading indicator
- **AI-search-first** — aligned with Google's AI Optimization Guide (May 2026); explicitly rejects three influencer myths (llms.txt as citation lever, content chunking for AI, AI-specific keyword rewriting); scores passage citability (134-167 word answer blocks)
- **10-principle PERCEIVE→ANALYZE→VALIDATE→ACT methodology** — structured audit phases from observation through falsifiability testing to artifact delivery
- **Headless SPA rendering** — Playwright Chromium with auto-detection of Next.js/React/Vue/Nuxt/Astro; trafilatura for boilerplate removal
- **Schema.org depth** — 30+ active types, deprecation tracking (FAQPage May 2026, HowTo Sept 2023, etc.), dual validator (Rich Results Test + Schema Markup Validator)
- **8 optional MCP extensions:** DataForSEO (22 commands), Firecrawl (full-site crawl), Banana (AI image gen), Ahrefs, SE Ranking (AI Share-of-Voice), Profound (LLM citation tracking), Bing Webmaster + IndexNow, Unlighthouse
- **Codex port available** — Codex SEO with TOML agents and deterministic runners
- **271 tests** including 83 SSRF and DNS-rebinding bypass tests

## Mechanical details / What to adopt

- **Install:** `/plugin marketplace add AgriciDaniel/claude-seo` → `/plugin install claude-seo@agricidaniel-claude-seo`
- **Manual:** `git clone` → `bash install.sh` (Unix) or `powershell install.ps1` (Windows)
- **Requirements:** Python 3.10+, Claude Code CLI; optional Playwright Chromium for SPA rendering
- **Credentials:** stored under `~/.config/claude-seo/` with 0o600 permissions; nothing checked into repo
- **Output:** Markdown reports (primary), PDF via WeasyPrint + matplotlib (~32 A4 pages for full audit), JSON
- **Architecture:** 3-layer (directive/orchestration/execution), auto-discovery from `skills/seo-*/` and `agents/seo-*.md`
- Author: Agrici Daniel; single maintainer with community contributors

## Security

MIT licensed. Zero telemetry. Works fully offline without API keys. Credentials stored with 0o600 permissions. 271 tests including 83 SSRF/DNS-rebinding bypass tests. Per-PR audit gate with 14-assertion manifest consistency check, test suite, and 8-dimension security review. Single primary maintainer. Optional MCP extensions connect to external paid services (DataForSEO, Ahrefs, etc.) — opt-in only.