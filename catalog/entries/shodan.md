---
name: shodan
title: Shodan
url: "https://www.shodan.io/"
category: cli-tool
summary: "Search engine for internet-connected devices — crawls all public IPv4 addresses weekly, indexes service banners/vulnerabilities/exposed services; search filters for ports, protocols, products, OS, geo, vulns; CLI and REST API for programmatic access; Shodan Monitor for real-time network exposure alerts; data streaming firehose; 3M+ registered users including 89% of Fortune 100; free tier, one-time $49 membership, subscriptions from $69/mo; proprietary"
tags: [security, osint, network-scanning, iot, vulnerability, api, cli, reconnaissance, attack-surface]
reviewed: 2026-09-26
acquired: 2026-09-26
overlaps: [revealer-us]
license: Proprietary
security_flags: []
source: unknown
---

## What it does

Shodan is a search engine that indexes internet-connected devices rather than web pages. It sends connection requests to every public IPv4 address across dozens of common ports, captures service response banners, and stores the data in a searchable index. Updated weekly via continuous global crawling.

Key capabilities:

- **Device search**: Query by port, protocol, product name, version, operating system, geography, organization, SSL certificate details, and known vulnerabilities (CVE). Returns banner data, open ports, HTTP headers, SSL certificates, and device metadata.
- **Shodan Monitor**: Real-time network monitoring — define IP ranges and receive notifications when new services appear, vulnerabilities are detected, or unexpected changes occur. Setup within 5 minutes per their documentation.
- **Vulnerability detection**: Cross-references discovered services against known CVEs. The `vuln` search filter (Small Business plan and above) finds devices with specific vulnerabilities.
- **Data streaming**: Firehose API providing real-time access to Shodan's crawl data as it is collected. Available on subscription plans.
- **IP enrichment**: Lookup any IP address for open ports, services, geolocation, organization, hostnames, and known vulnerabilities.
- **Network scanning**: On-demand scanning of specific IPs or CIDR ranges using Shodan's distributed infrastructure (consumes scan credits).

## CLI and API

The `shodan` CLI (`pip install shodan`) exposes most API functionality without writing scripts: `shodan search`, `shodan host`, `shodan scan`, `shodan stats`, `shodan download`, `shodan parse`. The REST API supports search, host lookup, scanning, DNS resolution, streaming, and network monitoring. API keys are sharable across an organization with no per-user limits.

Metered resources: query credits (1 per search), scan credits (1 per IP scanned), and monitored IP slots. Credit allocations vary by plan tier.

## Pricing

- **Free**: Basic search without filters, up to 100 results.
- **Membership**: $49 one-time — unlocks search filters, CLI access, basic API.
- **Freelancer**: $69/mo — most filters (excludes `vuln` and `tag`), paging, basic streaming, commercial use.
- **Small Business**: $359/mo — adds vulnerability search, more credits.
- **Corporate**: $1,099/mo — full feature set.
- **Enterprise**: Custom pricing.

Grandfathered pricing: existing customers keep their rate even if prices increase for new customers, with no multi-year commitment required.

## Security

Proprietary SaaS platform. 3M+ registered users, used by 89% of the Fortune 100, 5 of the top 6 cloud providers, and 1,000+ universities. Shodan is a reconnaissance tool — its data is publicly observable (service banners from internet-facing devices), but the aggregation and searchability create an attack-surface discovery capability. Intended for defensive security, penetration testing, and research. API data must be attributed to Shodan when integrated into products.

## How to use it

pip install shodan
