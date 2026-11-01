---
name: cobalt
title: Cobalt
url: "https://github.com/imputnet/cobalt"
category: cli-tool
summary: "General-purpose media downloader with a self-hosted API; no agent, skill, or bioinformatics relevance."
tags: [media-download, self-hosted, api, proxy, youtube, video]
reviewed: 2026-06-10
acquired: 2026-06-10
license: AGPL-3.0
security_flags: [agpl-copyleft]
overlaps: []
source: unknown
---

## What it does

Cobalt is a self-hosted media downloading service. Users paste a public video/audio URL (YouTube, Twitter/X, TikTok, Instagram, etc.) into the web frontend or call the REST API, and cobalt streams the file back without caching it — acting as a transparent proxy to the platform's CDN. The monorepo ships three components: an API server (Node.js), a web frontend (SvelteKit), and shared packages. It is designed to be ad-free, tracker-free, and paywall-free, and explicitly limits itself to freely accessible public content only.

## Assessment

Cobalt is a polished, actively maintained utility for downloading public media. It has no connection to agent orchestration, skill authoring, bioinformatics pipelines, or Claude Code tooling — the entire scope is consumer media retrieval. It is cataloged as `note` because it could be useful as a data-acquisition utility in a workflow that needs to pull publicly available video/audio data, but it offers nothing to adopt or pilot for the agent-toolkit use cases this catalog serves. Watch/pilot would overstate its relevance.

## Mechanical details

- **Architecture**: Monorepo (api/, web/, packages/, docs/). API is Node.js; frontend is SvelteKit.
- **Deployment**: Self-hosted via Docker or direct Node.js. Documentation covers instance setup, protection (rate limiting, authentication), and environment variables.
- **API**: REST — POST a URL, receive a file stream or redirect. No LLM calls, no agent interface.
- **Proxy model**: No content is cached server-side; cobalt fetches from the platform on demand and streams to the client.
- **License**: The top-level repository is AGPL-3.0. Per-component licenses are in the api/ and web/ READMEs (may differ).
- **Sponsor**: royalehosting.net hosts part of the infrastructure.

## Security

- **License**: AGPL-3.0 at repo root; component-level licenses documented separately. AGPL copyleft obligations apply if modified and offered as a network service — flagged.
- **Scope risk**: Cobalt is explicitly scoped to public, free content and acts as a proxy (no caching). However, self-hosting a media proxy introduces network exposure and potential abuse vectors (rate limiting, auth are covered in their docs).
- **Supply chain**: Active open-source project on GitHub; contributor count not assessed from fetched content. No signed releases observed.
- **Code quality**: CI configuration and test presence not confirmed from the top-level README; full assessment would require inspecting api/ subtree.
- **Dangerous patterns**: No agent-execution, eval, or credential-handling patterns visible at the monorepo level; risks are standard web-service patterns (input URL validation, SSRF mitigations on the proxy path).
