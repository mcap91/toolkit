---
name: shift-left-security
title: Shift Left Security
url: "https://owasp.org/www-project-devsecops-guideline/"
category: reference
summary: "Security testing practice — move checks earlier in the delivery pipeline; SAST (static, e.g. CodeQL/Semgrep in CI), DAST (dynamic, e.g. OWASP ZAP in staging), pre-commit hooks (Semgrep on changed files), editor plugins (SonarQube); canonical example is SQL injection prevented by parameterized queries"
tags: [security, devsecops, sast, dast, pre-commit, ci-cd, sql-injection, shift-left]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: unknown
security_flags: []
source: unknown
---

## What it does

Shift left is the practice of moving security checks earlier in the software delivery pipeline so issues are caught before code reaches production.

Four integration points:
1. **Editor plugins** (e.g. SonarQube) — flag problems as code is written
2. **Pre-commit hooks** (e.g. Semgrep) — scan changed files before code enters Git
3. **SAST in CI** (Static Application Security Testing, e.g. CodeQL) — scan code without running it, integrated into the CI pipeline
4. **DAST in staging** (Dynamic Application Security Testing, e.g. OWASP ZAP) — attack the running application from outside

The canonical teaching example is SQL injection: input like `' OR 1=1 --` inside a query returns every row. The fix is a parameterized query, treating user input as data rather than code.

## Mechanical details

Common tools by layer:
- Editor: SonarQube, Snyk IDE plugins
- Pre-commit: Semgrep, gitleaks, detect-secrets
- SAST: CodeQL, Semgrep, Bandit (Python), ESLint security plugins
- DAST: OWASP ZAP, Burp Suite, Nuclei

## Security

This entry is a reference about security practices. No software to evaluate.