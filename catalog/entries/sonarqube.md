---
name: sonarqube
title: SonarQube
url: https://github.com/SonarSource/sonarqube
source_url: https://www.instagram.com/reel/DeJyswKCtCY/
source: instagram
category: framework
summary: Self-hosted continuous-inspection platform for code quality and security — static analysis (symbolic execution, data/control-flow analysis) across 20+ languages via quality gates and 6,000+ rules; free Community Build (LGPL-3.0) lacks branch/PR analysis and advanced security (taint analysis, secrets detection, IaC); paid Developer/Enterprise/Data Center editions add those plus portfolios and enterprise reporting; free IDE companion SonarLint gives real-time in-editor feedback; priced per instance/year by lines of code
tags:
  - code-quality
  - static-analysis
  - security
  - ide-plugin
  - continuous-inspection
  - devsecops
reviewed: 2026-10-29
acquired: 2026-10-29
license: LGPL-3.0 (Community Build); bundled analyzers under Sonar Source-Available License v1 (SSALv1); commercial editions separately licensed
security_flags: []
overlaps:
  - semgrep
  - codeql
---

## What it does

SonarQube is a self-hosted platform for continuous code inspection — it applies static-analysis techniques (symbolic execution, data-flow and control-flow analysis) to find bugs, vulnerabilities, code smells, and structural problems across 20+ languages (including infrastructure-as-code), surfaced through configurable quality gates and 6,000+ built-in rules. Its IDE companion, SonarLint ("SonarQube for IDE"), gives real-time feedback as code is typed, underlining the specific line an issue is found on.

## Mechanical details

The free Community Build is LGPL-3.0-licensed and self-hosted (download, install, run on your own server, no license fee); its bundled analyzer plugins moved to the Sonar Source-Available License v1 (SSALv1) in late 2024. It lacks branch analysis, pull-request decoration, taint analysis, and advanced security features. Paid Developer, Enterprise, and Data Center editions (SonarQube Server) add those capabilities plus portfolios, OWASP/CWE reporting, legacy-language support, and (Data Center) high-availability deployment; pricing is per instance per year scaled by lines of code (third-party summaries cite roughly $2,500/yr at 100K LOC for Developer, ~$20,000/yr at 1M LOC for Enterprise). SonarQube Cloud (formerly SonarCloud) offers a hosted alternative with its own free tier for individuals/small teams.

## Security

No security advisories surfaced against the Community Build itself in this research pass. Advanced security scanning (taint-analysis SAST, secrets detection covering third-party dependency interactions) is reserved for the paid Advanced Security add-on — the free build's security coverage is narrower than its "security" branding implies.
