---
name: revealer-us
title: Revealer.US
url: "https://revealer.us/"
category: cli-tool
summary: "OSINT platform for username, email, and phone lookup across 800+ live sources (social, gaming, forum, developer platforms) plus breach and stealer-log dataset search; results arrive as each source responds; AI Deep Search (paid) follows reused handles and writes cited reports with confidence scores; REST API for programmatic access; SaaS with free demo tier, paid from $12.99/mo; domain registered January 2026, low third-party trust score (27/100 Gridinsoft)"
tags: [osint, username-lookup, email-lookup, breach-search, security, reconnaissance, api, saas]
reviewed: 2026-09-26
acquired: 2026-09-26
overlaps: [shodan]
license: Proprietary
security_flags: [young-domain, low-trust-score, saas-only]
source: unknown
---

## What it does

Revealer.US is a web-based OSINT platform that checks a username, email, or phone number against 800+ live sources and known breach/stealer-log datasets. Three main capabilities:

- **Username lookup**: Checks a handle across 700+ social, gaming, forum, and developer platforms in real time. Each source returns its own display name, bio, and outbound links. Results arrive progressively as sources respond.
- **Email lookup**: Checks an email address against 157 email-specific modules plus breach and stealer-log datasets. Breach results show the source type, date, and exposed field types (email, username, IP, browser, etc.). Password values are always redacted — the record indicates a password was present but does not display it.
- **AI Deep Search** (Basic plan and above): Reads all rows from the sweep, follows reused handles and linked accounts, and writes a short report with citations back to specific rows and confidence values for each claim. Reports explicitly flag uncertain matches.

Also offers a REST API for email lookup, username search, breach detection, and OSINT enrichment, available on Pro plan and above.

## Pricing

Free tier: limited demo search on the website, no account required. Starter: $12.99/mo. Basic: $29.99/mo (adds AI Deep Search). Higher tiers add more searches, breach monitoring, and device exposure alerts. API access on Pro and above.

## Mechanical details

Results are fetched live per search — the service states it does not store search history. Account holds only a counter of searches used in the current period. The platform is not a data broker and states it does not own or sell data. Breach partner datasets include combolists, forum database dumps, and infostealer logs.

The service is operated by a small remote team (American/Thai owners). Domain registered January 28, 2026 via NameCheap with privacy-protected WHOIS.

## Security

Proprietary, SaaS-only. Domain is 8 months old as of September 2026. Gridinsoft rates it 27/100 trust score with warnings from 2 of 26 security sources — young domain age is the primary factor. The service states compliance with FCRA (not a consumer reporting agency — results may not be used for credit, insurance, employment, housing, or tenant screening). Password values are never displayed. Users should exercise due diligence given the domain's short history.