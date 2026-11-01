---
name: breachdirectory
title: BreachDirectory
url: "https://breachdirectory.org/"
category: cli-tool
summary: "Free breach lookup engine — searches billions of breached credentials and personal records by email, username, or domain; shows plaintext and hashed passwords from real data dumps; API available via RapidAPI (free basic tier, paid pro); dual-use OSINT tool for breach monitoring and credential exposure checking; proprietary, web-based"
tags: [osint, breach-search, security, credentials, email-lookup, password, api, reconnaissance]
reviewed: 2026-09-26
acquired: 2026-09-26
overlaps: [revealer-us, shodan]
license: Proprietary
security_flags: [dual-use, shows-partial-passwords]
source: unknown
---

## What it does

BreachDirectory is a web-based search engine over publicly disclosed data breaches. It indexes billions of breached credentials and personal records, allowing lookup by email address, username, or domain to determine if they appear in known breach datasets.

Key capabilities:

- **Email/username search**: Checks an email or username against known breach datasets and returns which breaches contained that identifier, along with the types of data exposed (email, username, password hash, plaintext password, IP address, etc.).
- **Password exposure**: Shows plaintext and hashed passwords from real data dumps associated with the searched identifier. This distinguishes it from services like Have I Been Pwned, which only indicate breach membership without revealing credential details.
- **Domain search**: Check whether any accounts under a domain have appeared in breaches.
- **API access**: Available via RapidAPI with a free Basic plan and a paid Pro plan. Third-party tools like BreachCheck integrate with the API for programmatic breach lookups.

## Pricing

Free web search with no account required. API access via RapidAPI: Basic (free, rate-limited) and Pro (paid, higher limits).

## Mechanical details

The service operates as a search engine over aggregated breach datasets. The data comes from publicly disclosed breaches — combolists, forum database dumps, and credential leaks. The service does not claim to detect new breaches; it indexes existing public breach data.

## Security

Proprietary, web-based service. Dual-use tool — designed for legitimate security research, journalism, and personal breach monitoring, but the exposure of actual credential data (including partial/hashed passwords) creates potential for misuse. The site returned a 403 when fetched programmatically, suggesting anti-bot protections. Listed in OSINT tool directories (OSINT Yourself) with the caveat that listing is not an endorsement. Users should verify their authorization context before using breach lookup services that expose credential data.