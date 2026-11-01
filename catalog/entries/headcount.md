---
name: headcount
title: Headcount
url: "https://github.com/cbrock84/headcount"
category: plugin
summary: "Claude Code plugin structured as a 16-department company org chart — 146 skills across CEO, Technology, Security (reviewer-class), IT Ops, Product, Marketing, Demand Gen, Revenue, Finance, Operations, PMO, Customer Experience, Data & Analytics, Corporate Strategy, People/HR, and Legal & Risk (reviewer-class); each department independently installable via marketplace, skills addressed as department:skill, agent charters for subagent delegation, exclusive write-surface enforcement; MIT"
tags: [claude-code-plugin, skills-library, organizational, departments, agent-hierarchy, subagents, write-surface, reviewer-class, enterprise]
reviewed: 2026-08-31
acquired: 2026-08-31
overlaps: [claude-skills-rezvani, agent-skills-osmani]
license: MIT
security_flags: []
source: unknown
---

## What it does

Headcount is a Claude Code plugin that organizes 146 agent skills as a simulated company with 16 departments, each independently installable. Skills load automatically when a request matches their territory, or can be invoked directly by name (e.g., `/finance:financial-modeling`).

**Architecture:**
- Each department is an independently installable plugin (`/plugin install security@headcount`)
- Skills addressed as `department:skill` — names never collide across departments
- Each department ships an agent charter in `.claude/agents/` for subagent delegation
- Exclusive write-surface enforcement via `docs/AGENT-SURFACES.md` — every path has exactly one owner
- Two reviewer-class departments (Security/CISO, Legal & Risk/CLO) whose blocking findings cannot be overridden by the department under review

**Departments (16):**
- Office of the CEO (6 skills) — agent hierarchy design, business growth, CEO advisory
- Technology/CTO (18 skills) — code review, debugging, TDD, architecture, release, observability
- Security/CISO (6 skills, reviewer-class) — threat modeling, incident response, security architecture
- IT Operations/CIO (11 skills) — endpoint, network, identity lifecycle, backup
- Product/CPO (9 skills) — design system, interface craft, UX audit, visual reference
- Marketing/CMO (18 skills) — brand voice, content strategy, social, video, newsletters
- Demand Generation (11 skills) — SEO, AI search optimization, CRO, paid ads, experiments
- Revenue/CRO (8 skills) — pricing, retention, referral, sales enablement
- Finance/CFO (10 skills) — modeling, unit economics, budgeting, revenue recognition
- Operations/COO (10 skills) — process design, vendor management, supply chain
- PMO (7 skills) — program management, portfolio governance, dependency/risk
- Customer Experience/CCO (5 skills) — support ops, escalation, knowledge base
- Data & Analytics/CDO (6 skills) — data engineering, BI, governance, ML governance
- Corporate Strategy/CSO (5 skills) — M&A, portfolio strategy, scenario planning
- People/CHRO (10 skills) — hiring, comp, org design, performance management
- Legal & Risk/CLO (6 skills, reviewer-class) — contracts, compliance, privacy, enterprise risk

Seven cross-department use cases documented in `docs/USE-CASES.md` (SOC 2 demand, security incident, stalled funnel, etc.).

## Mechanical details

Requires Claude Code with plugin support. Interactive org chart at `docs/org-chart.html` (also published to GitHub Pages). CI script (`scripts/check-all.sh`) verifies surface map coherence, frontmatter validity, uniqueness, no third-party license text, spelling, and that every `department:skill` reference resolves. All skills written from scratch for this repo (no external skill dependencies).

## Security

MIT licensed. All 146 skills written by a single author (Chris Brock). No external dependencies or third-party skill code. CI checks enforce that no third-party license text appears. The reviewer-class department pattern (Security, Legal) provides built-in review gates for security-sensitive work.

## How to use it

/plugin marketplace add cbrock84/headcount
