---
name: anthropic-financial-services
title: Claude for Financial Services
url: "https://github.com/anthropics/financial-services"
category: plugin
summary: "Official Anthropic reference agents and skills for financial services — 10 named workflow agents (Pitch Agent, Market Researcher, GL Reconciler, etc.), 7 vertical skill bundles (IB, equity research, PE, wealth management, fund admin, ops), 12 MCP data connectors (FactSet, S&P, Morningstar, PitchBook, LSEG, etc.); dual deployment as Cowork plugins or Managed Agents API; Apache-2.0"
tags: [anthropic-official, financial-services, investment-banking, equity-research, private-equity, wealth-management, mcp-server, managed-agents]
reviewed: 2026-07-06
acquired: 2026-07-06
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Official Anthropic repository of reference agents, skills, slash commands, and MCP data connectors for financial-services workflows. Everything ships in dual form: as Claude Cowork plugins and as Claude Managed Agent templates deployable via `/v1/agents`.

**10 named agents:**
1. **Pitch Agent** — comps, precedents, LBO → branded pitch deck end-to-end
2. **Meeting Prep Agent** — briefing pack before client meetings
3. **Market Researcher** — sector/theme → industry overview, competitive landscape, peer comps, ideas shortlist
4. **Earnings Reviewer** — earnings call + filings → model update → note draft
5. **Model Builder** — DCF, LBO, 3-statement, comps — live in Excel
6. **Valuation Reviewer** — ingests GP packages, runs valuation template, stages LP reporting
7. **GL Reconciler** — finds breaks, traces root cause, routes for sign-off
8. **Month-End Closer** — accruals, roll-forwards, variance commentary
9. **Statement Auditor** — audits LP statements before distribution
10. **KYC Screener** — parses onboarding docs, runs rules engine, flags gaps

**7 vertical plugins:** financial-analysis (core), investment-banking, equity-research, private-equity, wealth-management, fund-admin, operations. Plus 2 partner-built verticals (LSEG, S&P Global).

**12 MCP data connectors:** Daloopa, Morningstar, S&P Global (Kensho), FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, Egnyte, Box.

## Differentiators

- **Official Anthropic authorship** — reference implementations from the company behind Claude
- **Dual deployment** — same system prompt and skills work as Cowork plugins or headless Managed Agents via API
- **Managed Agent cookbooks** — `agent.yaml`, leaf-worker subagents, steering-event examples, and security notes for each agent
- **MCP connector hub** — 12 financial data providers pre-wired, including FactSet, S&P, Morningstar, PitchBook, LSEG
- **Partner-built plugins** — LSEG (bond RV, swap curves, FX carry, options vol) and S&P Global (tear sheets, earnings previews, funding digests)
- **Claude for Microsoft 365** — included admin tooling to provision the Claude M365 add-in against Vertex AI, Bedrock, or internal LLM gateway
- **pptx-author / xlsx-author** — headless PowerPoint and Excel file generation in Managed Agent mode
- Everything is file-based (markdown + JSON + YAML), no build step

## Mechanical details / What to adopt

- **Install (Claude Code):** `claude plugin marketplace add anthropics/financial-services` → install core + agents
- **Install (Cowork):** Settings → Plugins → paste repo URL or upload zip of any plugin directory
- **Deploy (Managed Agents):** `scripts/deploy-managed-agent.sh <agent-slug>` — resolves file references, uploads skills, creates leaf-worker subagents, POSTs orchestrator to `/v1/agents`
- **Customization:** swap MCP connectors in `.mcp.json`, add firm context/terminology to skill files, bring branded PowerPoint templates via `/ppt-template`
- **Validation:** `python3 scripts/check.py` lints manifests, verifies cross-file references, detects skill drift between vertical sources and agent bundles
- Notable slash commands: `/comps`, `/dcf`, `/lbo`, `/earnings`, `/ic-memo`, `/source`, `/screen-deal`, `/rebalance`, `/tlh`

## Security

Apache-2.0 licensed. Official Anthropic repository. Explicit disclaimer: agents draft work product for human review, do not make investment recommendations or execute transactions. MCP connectors may require provider subscriptions/API keys. Subagent delegation (`callable_agents`) is a research preview capability. All file-based — no build step, no runtime dependencies beyond Claude.