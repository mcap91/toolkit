---
name: bubblewrap-pwa
title: Bubblewrap (PWA)
url: "https://github.com/googlechromelabs/bubblewrap"
category: cli-tool
summary: "Google Chrome Labs CLI for wrapping Progressive Web Apps as Android Trusted Web Activity (TWA) APKs — Node.js toolchain with core library, CLI, and validator; Apache-2.0"
tags: [pwa, android, twa, mobile, google]
reviewed: 2026-06-23
acquired: 2026-06-23
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Bubblewrap (Google Chrome Labs) is a CLI and library for packaging Progressive Web Apps (PWAs) as Android applications that launch via Trusted Web Activity (TWA). Not related to the containers/bubblewrap Linux sandboxing tool despite the same name.

Components:
- **@aspect/core**: JavaScript library for generating, building, and updating TWA projects
- **@aspect/cli**: Command-line interface
- **@aspect/validator**: Validates and compares TWA projects against quality criteria

Powers PWABuilder for generating APKs from PWAs.

## Assessment

Unrelated to agent/sandboxing workflows. Useful if building mobile-accessible bioinformatics dashboards as PWAs and wanting native Android distribution via TWA. Very specific use case with no agent or developer-tool relevance.

## Mechanical details

Requires Node.js 14.15.0+. Community contributions welcome; monthly public office hours.

## Security

- **License**: Apache-2.0
- **Maintainer**: Google Chrome Labs (not an officially supported Google product per disclaimer)
- **Supply chain**: Established project, community-maintained