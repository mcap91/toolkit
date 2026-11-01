---
name: nginx
title: nginx
url: "https://nginx.org/"
category: framework
summary: "HTTP web server, reverse proxy, content cache, load balancer, TCP/UDP proxy, and mail proxy — originally by Igor Sysoev, 2-clause BSD license; enterprise distributions and commercial support from F5; mature infrastructure for hosting agent services and API gateways"
tags: [web-server, reverse-proxy, load-balancer, infrastructure]
reviewed: 2026-07-06
acquired: 2026-07-06
license: BSD-2-Clause
security_flags: []
overlaps: []
source: unknown
---

## What it does

HTTP web server, reverse proxy, content cache, load balancer, TCP/UDP proxy server, and mail proxy server. One of the most widely deployed web servers globally, used for serving static content, reverse-proxying to application servers, load balancing, and SSL termination.

## Differentiators

- **Event-driven architecture** — handles thousands of concurrent connections with minimal memory footprint
- **Mature and battle-tested** — in production since 2004, powers a significant share of the internet's web traffic
- **njs scripting** — JavaScript scripting engine (njs 1.0.0 released June 2026, now using QuickJS engine)
- **Active maintenance** — stable (1.30.x) and mainline (1.31.x) release tracks with regular security patches

## Mechanical details / What to adopt

- Available via package managers on all major platforms
- Configuration via declarative config files (`nginx.conf`)
- Enterprise distributions from F5, Inc. with commercial support and training

## Security

2-clause BSD license. Active CVE response — recent patches for buffer overflow in proxy_v2/gRPC modules (CVE-2026-42055), buffer overread in charset module (CVE-2026-48142), use-after-free in HTTP/3 module (CVE-2026-42530), and buffer overflow in rewrite module (CVE-2026-9256).