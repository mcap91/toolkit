---
name: codeql
title: CodeQL
url: https://codeql.github.com/
source_url: https://www.instagram.com/reel/DeJyswKCtCY/
source: instagram
category: cli-tool
summary: GitHub's semantic SAST engine — compiles source into a queryable relational database and runs CodeQL-language queries (SQL injection, XSS, etc.) against it without executing the code; CLI integrates into GitHub Actions/Advanced Security code scanning and can fail CI on a match; 12 languages; CLI under GitHub's own Terms (free for OSI-licensed public repos/academic use, GHAS license required for private repos), query packs MIT
tags:
  - sast
  - static-analysis
  - github
  - code-scanning
  - security
  - ci-cd
reviewed: 2026-10-29
acquired: 2026-10-29
license: GitHub CodeQL Terms and Conditions (source-available); query packs MIT
security_flags: []
overlaps:
  - semgrep
---

## What it does

GitHub's semantic code-analysis engine for SAST (static application security testing). The CodeQL CLI compiles source code into a CodeQL database — a relational representation of the code's syntax and semantics — then runs queries written in the CodeQL query language against that database to find vulnerabilities (e.g. SQL injection, XSS, path traversal) and bugs without executing the code. Natively integrated into GitHub Advanced Security's code scanning, where the `github/codeql-action` runs analysis as part of a GitHub Actions workflow and can report or fail a pull request when a query matches.

## Mechanical details

Supports C/C++, C#, Go, Java, Kotlin, JavaScript, TypeScript, Python, Ruby, Rust, Swift, and GitHub Actions workflows (per codeql.github.com). The standard security query packs are maintained in the open-source `github/codeql` repo under the MIT license. The CodeQL CLI binary itself ships under GitHub's own CodeQL Terms and Conditions rather than an OSI-approved license. Typical usage: `codeql database create` to build the database, `codeql database analyze` to run a query pack against it; most users invoke it indirectly via the `github/codeql-action` workflow rather than the raw CLI.

## Security

License restricts use rather than granting unrestricted rights: free for analyzing public repositories released under an OSI-approved open-source license, for academic research, or for CI/CD analysis of such repos hosted on GitHub.com; analyzing private repositories requires a paid GitHub Advanced Security (GHAS) license (third-party pricing summaries put GHAS at roughly $30/active-committer/month). No security advisories surfaced against the CLI itself in this research pass; it is a passive analysis tool that does not execute the code it scans.
