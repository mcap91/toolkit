---
name: karakeep
title: Karakeep
url: "https://github.com/karakeep-app/karakeep"
category: framework
summary: "Self-hostable AI bookmark manager with REST API, official agent skills, and Ollama support — agent-friendly but self-described as under heavy development."
tags: [bookmarks, knowledge-management, self-hosted, llm, tagging, search, rest-api, agent-friendly]
reviewed: 2026-06-10
acquired: 2026-06-10
license: AGPL-3.0
security_flags: [puppeteer-in-production, agpl-copyleft, heavy-development]
overlaps: []
source: unknown
---

## What it does

Karakeep (previously Hoarder) is a self-hostable bookmark-everything platform that ingests links, notes, images, and PDFs into a centralized, searchable knowledge store. It automatically fetches link metadata (title, description, preview image) and uses LLMs — either OpenAI or local models via Ollama — to apply automatic tags and generate summaries. Full-text search is powered by Meilisearch, and OCR extracts text from images for indexing.

Beyond basic bookmarking, Karakeep supports full-page archival via monolith (protecting against link rot), video archiving via yt-dlp, RSS feed auto-ingestion, content highlights, and a rule-based engine for automated list management. Browser extensions exist for Chrome, Firefox, and Safari, plus native iOS and Android apps. Collaboration is supported at the list level. Importers are provided for Chrome bookmarks, Pocket, Linkwarden, Omnivore, and Tab Session Manager.

The platform is explicitly designed to be LLM agent-friendly: it exposes a REST API, a CLI, and ships official agent skills compatible with LLM agents (specifically calling out OpenClaw and Hermes). This makes it tractable as a backing store or knowledge-retrieval target within agent workflows.

## Assessment

Karakeep earns a pilot verdict. It is the most feature-complete self-hostable bookmark+AI tagging platform available, and its explicit REST API + CLI + official skills design makes it unusually accessible for agent-driven workflows. Ollama support means it can run fully air-gapped without OpenAI dependency, which is relevant for local agent setups.

The main caution is the project's own self-description: "under heavy development." API stability and schema migrations may be disruptive. The AGPL-3.0 license imposes network-service copyleft obligations, which matters if Karakeep is ever wrapped into a proprietary service. For personal or internal agent infrastructure use, this is largely a non-issue. The cloud tier (cloud.karakeep.app) offers a hosted escape hatch if self-hosting is too operationally heavy.

For agent toolkit workflows specifically, Karakeep is most interesting as a persistent, queryable knowledge store that agents can write bookmarks into and retrieve from, particularly once semantic search lands (currently planned). Worth piloting in an agent infrastructure setup.

## Mechanical details

Self-hosted deployment is Docker-based (docker compose). The stack is NextJS + Drizzle ORM + tRPC + Puppeteer + Meilisearch. Authentication supports SSO via NextAuth. A demo is available at https://try.karakeep.app (demo@karakeep.app / demodemo, read-only).

For agent integration, use the REST API or the CLI. Official skills are provided for LLM agents. Browser sync via floccus allows automatic bidirectional sync with browser bookmarks. Video archiving requires yt-dlp to be available in the deployment environment. Full-page archival requires monolith.

## Security

License is AGPL-3.0, owned by Localhost Labs Ltd. AGPL requires that any modifications to a network service using Karakeep must be open-sourced — this is a strong copyleft obligation if you ever wrap it in a proprietary service. Personal or internal use is not affected.

Puppeteer is used for link crawling in production, which introduces a headless browser attack surface; malicious URLs could potentially exploit the crawler. This is a known pattern in self-hosted bookmark tools but should be accounted for by restricting which URLs are queued for crawling.

The project is under active development with no stated API stability guarantees. No evidence of signed releases or pinned dependencies from the README alone. The project has a managed cloud offering (Localhost Labs Ltd.) and an active Discord community, suggesting ongoing maintenance.
