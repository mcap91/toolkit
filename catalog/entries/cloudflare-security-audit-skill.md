---
name: cloudflare-security-audit-skill
title: Cloudflare Security Audit Skill
url: "https://github.com/cloudflare/security-audit-skill"
category: skill
summary: "Six-phase coding-agent skill for structured security audits — reconnaissance, coverage-led hunting with isolated agents, adversarial candidate validation, structured JSON output with schema validation, independent record verification, and target-neutral reporting; seeds Cloudflare's internal vulnerability discovery harness; installs via `npx skills add`; MIT"
tags: [security-audit, vulnerability-discovery, agent-skill, multi-agent, adversarial-validation, coverage-tracking, cloudflare, pen-testing]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

A coding-agent skill that orchestrates a structured security audit in six phases, each using isolated sub-agents. Seeded from Cloudflare's internal vulnerability discovery harness.

**Phases:**
1. **Reconnaissance** — map architecture, trust boundaries, input surfaces, prior evidence. Outputs `architecture.md` and `coverage-ledger.json`.
2. **Coverage-led hunting** — assign isolated hunters from ledger units. Coverage critics find gaps.
3. **Candidate validation** — fresh verifier agents try to disprove each candidate (adversarial — finder ≠ verifier).
4. **Structured output** — write confirmed/needs_validation/rejected records to `findings.json`, validated against `report-schema.json`.
5. **Independent record verification** — fresh agents verify final source claims. Material replacements get another independent verifier.
6. **Target-neutral reporting** — derive `REPORT.md`, `FINDINGS-DETAIL.md`, and `NEEDS-VALIDATION.md` from verified records.

Multiple runs are additive — the skill uses prior ledgers and findings to target gaps and carry forward current-source evidence.

**Attack class libraries:** core, wildcard, memory-safety/binary, AI/LLM (prompt injection, agent/tool, output handling), web/protocol/auth, client-side (DOM, XSS, prototype pollution), supply-chain/release, cloud/deployment, protocols/RPC/messaging, resource exhaustion, data isolation, desktop/mobile/IPC.

## Mechanical details

Install: `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit` (add `--global` for user-level).

Triggers on: "security audit", "find vulnerabilities", "pen-test the code", etc. Full audit mode for codebase-wide requests; guidance mode for focused questions.

Requires: coding agent with tool use + parallel sub-agents, Node.js (for zero-dep validators), OS-enforced sandbox (disabled networking, allowlisted env, resource limits, assigned scratch paths). Without sandbox controls, leads stay as `needs_validation`.

Design principles: only confirm established boundary failures; adversarial validation (finder ≠ checker); severity requires impact (not checklist deviation); defense-in-depth gaps are hardening notes, not vulnerabilities.

## Security

MIT licensed. The skill itself writes only to a user-specified output directory (defaults to `~/security-audit-skill/<repo>/run-<N>`). Requires OS-enforced sandboxing for any target code execution.