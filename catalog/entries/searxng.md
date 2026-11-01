---
name: searxng
title: SearXNG
url: https://github.com/searxng/searxng
category: framework
summary: Free, self-hostable, privacy-first federated metasearch engine (fork of the discontinued searX) — queries dozens of external search engines/services in parallel and aggregates results without tracking users, storing queries, profiling, or ads; supports !bang shortcuts to target a single engine and extensive per-engine/ranking customization; no official hosted/cloud offering, self-hosting (typically Docker) is the only deployment model though public community instances exist; ~15k GitHub stars
tags:
  - metasearch
  - self-hosted
  - privacy
  - search
  - docker
  - federated-search
reviewed: 2026-10-29
acquired: 2026-10-29
license: AGPL-3.0
security_flags: []
overlaps:
  - on-prem-llm-deployment-architecture
source_url: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/
source: reddit
---

## What it does

SearXNG aggregates results from dozens of external search engines and services (up to ~251 configurable sources) into one interface without tracking users, storing queries, building profiles, or showing ads. It is server-side software meant to be self-hosted (official Docker image `searxng/searxng`), though public community-run instances also exist. `!bang` shortcuts target a single underlying engine, and administrators can select which engines to query and tune ranking/display behavior.

## Security

AGPL-3.0. Self-hosting keeps all query data under the operator's control; public instances rely on the instance operator's own privacy practices, which SearXNG itself does not enforce beyond not tracking by design.

## Usage notes

- Practitioner report (r/Qwen_AI, Oct 2026): backs an MCP server used for web research in a Zed + Qwen Code harness for self-hosted Qwen 3.8 27B; described as far more effective than Opus 4.8's basic HTTP fetch for that purpose. (source: https://www.reddit.com/r/Qwen_AI/comments/1x7u4kd/self_hosted_qwen_38_27b_for_real_work_my_1_month/)
