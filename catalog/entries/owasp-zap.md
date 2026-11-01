---
name: owasp-zap
title: OWASP ZAP
url: https://www.zaproxy.org/
source_url: https://www.instagram.com/reel/DeJyswKCtCY/
source: instagram
category: cli-tool
summary: Dynamic application security testing (DAST) tool that attacks a running web app from outside — intercepting proxy plus automated/passive scanners for SQL injection, XSS, CSRF, etc.; GUI or headless daemon mode with a REST API for CI/CD automation; Apache-2.0, no paid tier; forked from Paros, became an OWASP project in 2010, Checkmarx-sponsored since Sep 2024 as 'ZAP by Checkmarx' while remaining independently governed; ~15k GitHub stars
tags:
  - dast
  - security-scanner
  - penetration-testing
  - owasp
  - ci-cd
  - java
reviewed: 2026-10-29
acquired: 2026-10-29
license: Apache-2.0
security_flags:
  - active-scanning
  - requires-authorization
overlaps: []
---

## What it does

ZAP (Zed Attack Proxy) is a dynamic application security testing (DAST) tool that tests a running application from the outside rather than reading its source. As an intercepting proxy it can view and manipulate all traffic passing through it, including HTTPS; its automated scanner and passive scanner probe the running app for vulnerabilities such as SQL injection, XSS, and CSRF by sending real attack inputs and observing the responses. Also includes traditional and AJAX web spiders/crawlers, forced browsing, a fuzzer, WebSocket support, and scripting-language support.

## Mechanical details

Written in Java; runs on Linux, Windows, and macOS. Stable release 2.17.0 (March 2025). Can run with its normal GUI or in a headless daemon mode controlled via a REST API, which is how it's typically wired into CI/CD pipelines to scan a staging deployment on each build. Originally forked from Paros (Chinotec Technologies); became an OWASP project in 2010; since September 2024 its three core maintainers (Simon Bennetts, Ricardo Pereira, Rick Mitchell) are employed by Checkmarx to continue the work under the "ZAP by Checkmarx" sponsorship, while the project remains independently governed by the ZAP core team rather than owned by Checkmarx.

## Security

Apache-2.0, free for commercial use with no feature gate or paid tier. Because ZAP performs active scanning — sending real attack payloads at the target rather than passively reading code — it should only be pointed at systems the operator is authorized to test (e.g. a staging environment the team controls), not production systems or third parties without permission.
