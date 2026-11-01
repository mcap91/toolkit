---
name: pi-hole
title: Pi-hole
url: "https://github.com/pi-hole/pi-hole"
category: reference
summary: "Network-wide DNS ad blocker — mature infrastructure tool, informational for lab network hygiene"
tags: [dns, ad-blocking, privacy, self-hosted, network, sinkhole, dhcp]
reviewed: 2026-06-10
acquired: 2026-06-10
license: EUPL-1.2
security_flags: [curl-pipe-bash-install]
overlaps: []
source: unknown
---

## What it does

Pi-hole is a DNS sinkhole that runs on Linux hardware (typically a Raspberry Pi or any low-power server) and blocks advertisements and tracking domains at the network level. It intercepts DNS queries from every device on the local network and returns NXDOMAIN (or a blank IP) for any domain on its blocklists, preventing ad content from ever loading — in browsers, mobile apps, smart TVs, and any other networked device — without installing client-side software.

The core engine is FTLDNS (Faster Than Light DNS), a purpose-built daemon that handles DNS resolution, query caching, and real-time statistics. FTLDNS exposes a REST API (`/api/`) that surfaces query counts, block rates, top domains, and unique client metrics, making it easy to integrate Pi-hole data into dashboards or scripts. A web UI dashboard presents graphs, query logs, and configuration panels, and the `pihole` CLI provides full administrative control without the web interface.

Pi-hole can also function as a DHCP server, enabling it to automatically assign itself as the DNS resolver for every device that joins the network. It supports IPv4 and IPv6, custom allow/deny lists, regex-based rules, and long-term query history.

## Assessment

Pi-hole is a well-established, widely deployed privacy tool with a large community, active maintenance, and a clear, stable feature set. It earns "note" rather than "adopt" or "pilot" here because it is entirely outside the scope of AI agent workflows, bioinformatics pipelines, or Claude Code skill orchestration. It is a network infrastructure tool — useful for personal lab infrastructure (blocking telemetry from lab devices, for instance) but not something an agent would invoke, compose, or integrate into an agentic workflow.

The verdict "note" reflects that this is informational: worth knowing about for personal/home-lab network hygiene, but there is no workflow integration path in this catalog's domain. Users who operate self-hosted AI infrastructure may find Pi-hole useful for blocking unwanted outbound DNS from lab machines, which is a mild tangential overlap with the `agent-lockdown` skill's network hardening concerns.

## Mechanical details

Install (recommended non-piped method):
```bash
git clone --depth 1 https://github.com/pi-hole/pi-hole.git Pi-hole
cd "Pi-hole/automated install/"
sudo bash basic-install.sh
```

Or via Docker using the official `pihole/pihole` image. After installation, point your router's DHCP DNS setting to the Pi-hole's IP address, or enable Pi-hole's built-in DHCP server. The web UI is available at `http://<IP>/admin/`. The CLI is invoked as `pihole <command>` (e.g., `pihole status`, `pihole -w domain.com`, `pihole updateGravity`). The FTLDNS REST API is available at `http://<IP>/api/`.

## Security

License is EUPL-1.2, a weak copyleft license permitting use, modification, and distribution with attribution; compatible with most open-source use cases. The primary security concern is the canonical one-liner install (`curl -sSL https://install.pi-hole.net | bash`), which pipes a remotely fetched script directly to bash without inspection — a well-known supply chain attack vector. The project acknowledges this and provides alternative methods (clone + review + run, or manual wget). The `curl-pipe-bash-install` flag is set for this reason. FTLDNS is a compiled C binary distributed as part of the install; its source is in a separate repository (`pi-hole/FTL`). The project has many contributors, an active issue tracker, and a regular release cadence; no known credential-handling issues or dangerous eval patterns in the shell scripts.
