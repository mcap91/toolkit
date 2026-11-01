---
name: seo-god
title: seo-god
url: "https://github.com/AKCodez/seo-god"
category: skill
summary: "Claude Code skill that turns the agent into an SEO operator for a site you own — five-phase pipeline (setup → audit → measure → ai_visibility → schedule) using a local OpenSEO Docker container for crawling, Google Search Console for metrics, and a daily act loop that fixes regressions and improves near-ranking pages; no SERP scraping, no paid API keys required on the free path; MIT"
tags: [seo, claude-code-skill, docker, google-search-console, site-audit, scheduling, ai-visibility, automation]
reviewed: 2026-09-03
acquired: 2026-09-03
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

seo-god is a Claude Code skill that operates as an autonomous SEO pipeline for a website you own. It installs into `~/.claude/skills/seo-god` and activates via `/seo-god`. The skill orchestrates five numbered phases plus a daily loop:

1. **Setup**: boots an OpenSEO container in Docker, registers the site, writes `seo-god.json` for state tracking
2. **Audit**: crawls the site via the local OpenSEO container, triages issues by impact, fixes what lives in the repo (titles, metas, broken links, thin content) — gated by the project's own build and typecheck
3. **Measure**: connects Google Search Console, writes dated snapshots, diffs against the last run; review order: regressions → quick wins at positions 4–15 → new queries
4. **AI Visibility**: locks ten prompts for the site's niche on the first run (never edits them), measures whether the domain appears in search results for those prompts — a search-visibility proxy, not a citation-rate claim
5. **Schedule**: installs the daily loop as a real OS job (Task Scheduler / launchd / cron) or cloud routine, with a 48-hour self-check for missed runs

The daily **act** loop (unnumbered): fix regressions, improve 2–3 near-ranking pages, add at most one new page only if data supports it, leave a dated readout.

## Differentiators

- Complete free path — no paid API keys required; uses local OpenSEO Docker container instead of scraping Google
- Scheduled unattended runs edit files but never commit — changes wait in the working tree for human review
- Hard rules enforced: no bought links, no fake reviews, no SERP scraping, no auto-posting, no fabricated claims
- Budget-capped paid paths: DataForSEO (rank data), LLM keys (direct model probing), Telegram digest — all optional with per-run spending caps
- Secrets stored in gitignored `.seo-god/secrets.env`, never printed or committed
- Missing data reported as missing, never zero-filled or extrapolated
- Requests minimal permissions (curl + read-only git); never requests git add/commit/push
- Production-proven method: five phases are a rewrite of a pipeline running daily on a production site
- Includes smoke test report (`docs/SMOKE.md`) and 240-run triggering eval (`docs/EVAL.md`)

## Mechanical details

- Install: `git clone` into `~/.claude/skills/seo-god`; activate with `/seo-god` in Claude Code
- Requires: Docker (Desktop or Engine + Compose v2), Claude Code, a publicly reachable website
- State: `seo-god.json` in project root (committed — no secrets); `.seo-god/` directory (gitignored — secrets and scratch)
- Architecture: `SKILL.md` is a thin orchestrator routing to one `references/*.md` phase file per invocation
- Linting: `node scripts/skill-lint.mjs` checks structural rules before PRs
- Tested on Windows 11 + Git Bash with Docker 29.6.2 and OpenSEO 0.1.3; macOS/Linux paths stub-verified

## Security

- MIT license
- No SERP scraping anywhere in the skill
- Secrets confined to gitignored env file; never printed to output
- All paid API paths budget-capped before first call (per-run cap, balance floor where provider supports it, spend ledger)
- Requests only curl and read-only git permissions per turn
- OpenSEO crawler blocks private/loopback targets with no override
- Scheduled runs have 48-hour failure visibility check