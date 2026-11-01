---
name: adguard-home
title: AdGuard Home
url: "https://github.com/AdguardTeam/AdGuardHome"
category: framework
summary: "Production-ready network-wide DNS ad/tracker blocker — infrastructure tool, not an agent/dev workflow component"
tags: [dns, privacy, ad-blocking, network, self-hosted, docker]
reviewed: 2026-06-10
acquired: 2026-06-10
license: GPL-3.0
security_flags: [install-script-curl-pipe]
overlaps: []
source: unknown
---

## What it does

AdGuard Home is a self-hosted, network-wide DNS server that blocks ads, trackers, phishing domains, and malware at the DNS layer. Once deployed, it covers all devices on a network without requiring any per-device client software — it works by routing tracking and advertising domains to a black hole instead of resolving them normally.

The software ships with a web-based admin UI (accessible over HTTPS), a built-in DHCP server, per-client configuration (different filtering rules per device or group), and access control for who may use the DNS server. It supports encrypted DNS upstream resolvers: DNS-over-HTTPS (DoH), DNS-over-TLS (DoT), and DNSCrypt — making it substantially more capable than the Pi-Hole it is frequently compared against. Parental controls, Safe Search enforcement on major search engines, and custom blocklist management are all built-in with no additional software required.

It ships as a single Go binary with a React frontend bundled in. Deployment options include a one-line install script, Docker (official image on DockerHub), and Snap. A REST API and a Python client library enable programmatic integration; third-party integrations exist for Home Assistant, OpenWrt, GLiNet routers, iOS, and more.

## Assessment

AdGuard Home is a polished, production-grade tool with a large user base, active maintenance from the AdGuard team, and a broad feature set. The verdict is `note` rather than `adopt` because it is infrastructure software for home/small-office network privacy — it has no direct relevance to Claude Code agent workflows, bioinformatics pipelines, or LLM tooling that is the focus of this catalog. It is cataloged here because it was submitted to the inbox; the note verdict signals it is worth knowing about without implying it should be integrated into agent workflows.

The GPL-3.0 copyleft license is fine for self-hosted use but would impose obligations if redistributed as part of a larger product. For the target use case (self-hosted home network DNS), this is not a concern.

## Mechanical details

Install via one-line script (Linux/macOS/FreeBSD):
```
curl -s -S -L https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh | sh -s -- -v
```

Docker:
```
docker pull adguard/adguardhome
```

Build from source requires Go 1.25+, Node.js 24.10+, npm 10.8+; run `make` from the repo root.

After install, the admin interface is available at `http://<host>:3000` for initial setup. DNS clients on the network are pointed at the AdGuard Home host's IP as their DNS server. Per-client rules, upstream DNS providers, blocklist subscriptions, and DHCP leases are all managed through the web UI or REST API.

## Security

License: GPL-3.0 — copyleft, obligations apply only on redistribution, not self-hosted use.

Security flags:
- `install-script-curl-pipe`: The recommended quick-install method pipes a remote shell script directly into sh via curl/wget/fetch. This is a standard pattern for this type of software but carries supply-chain risk if the CDN or GitHub is compromised. Users should prefer Docker or manual binary download with checksum verification for production deployments.

No telemetry or external calls are made by default — the README explicitly states the software does not collect usage statistics or contact external services unless the user configures upstream DNS resolvers. The project is maintained by a commercial company (AdGuard) with a long track record in privacy software. Release cadence is active (beta and edge channels, regular stable releases). The Go codebase uses well-known dependencies (miekg/dns, dnsproxy, urlfilter) maintained by AdGuard themselves.
