---
name: agent-reach
title: Agent Reach
url: "https://github.com/Panniantong/agent-reach"
category: cli-tool
summary: "Capability-layer CLI that gives AI agents internet access — routes to best backend per platform (Twitter/Reddit/YouTube/Bilibili/Xiaohongshu/GitHub/LinkedIn/RSS/web/search), auto-installs tools, health-checks with doctor command; cookie-based auth, self-described vibe-coded, agent-self-install pattern carries supply-chain risk; MIT"
tags: [web-access, twitter, reddit, youtube, bilibili, xiaohongshu, agent-capability, cli, internet-access]
reviewed: 2026-06-25
acquired: 2026-06-25
license: MIT
security_flags: [agent-self-install, cookie-handling, vibe-coded, pip-install-from-git]
overlaps: [crawl4ai, firecrawl]
source: unknown
---

## What it does

A Python CLI capability layer that gives AI coding agents internet access across 10+ platforms. It doesn't do the reading itself — it selects, installs, and health-checks the best available backend tool for each platform, then the agent calls that upstream tool directly.

Supported platforms: web pages (Jina Reader), Twitter/X (twitter-cli → OpenCLI fallback), YouTube (yt-dlp for subtitles and search), GitHub (gh CLI), Bilibili (bili-cli, replacing yt-dlp which got blocked by Bilibili anti-fraud June 2026), Reddit (OpenCLI → rdt-cli, no anonymous access possible), Xiaohongshu (OpenCLI → xiaohongshu-mcp → xhs-cli), LinkedIn (linkedin-scraper-mcp → Jina Reader), RSS (feedparser), full-web search (Exa via mcporter MCP). Also supports V2EX and Xueqiu (Chinese stock market).

Each platform has an ordered backend list (primary + fallbacks). When a backend breaks, the maintainer swaps the routing — users run `agent-reach update`. `agent-reach doctor` reports which backend is active per platform and what needs fixing.

Install model: paste a single line to your agent pointing at the raw install.md on GitHub — the agent reads the instructions and self-installs. Has `--safe` mode (preview-only) and `--dry-run`.

## Assessment

Solves a genuine pain point: giving agents broad internet read access without per-platform configuration. The routing/fallback architecture is pragmatic — when yt-dlp got blocked by Bilibili, they swapped to bili-cli with zero user action required. The doctor command for diagnostics is well-designed.

However, significant concerns:

1. **Self-install pattern**: the agent fetches and follows install instructions from a remote URL. This is a supply chain risk — a compromised repo could inject arbitrary commands into agent sessions.
2. **Self-described "vibe coded"**: the author explicitly says this, suggesting limited testing discipline.
3. **Cookie handling**: stores browser cookies locally (chmod 600) for Twitter, Reddit, Xiaohongshu. The README warns about account ban risk. Cookies are equivalent to full login credentials.
4. **pip install from git URLs**: some backends install from unpinned or loosely pinned git repos.
5. **Chinese platform focus**: Bilibili, Xiaohongshu, V2EX, Xueqiu support is unique and not available elsewhere, but the affiliate links (ByteDance model subscriptions, Tencent Cloud OpenClaw) suggest commercial interest.

Useful for users who need broad platform access (especially Chinese platforms), but the supply-chain and security posture is not production-grade. The capability-layer architecture (routing, not wrapping) is a sound design pattern worth noting.

## Mechanical details

- Install: `pip install agent-reach` then `agent-reach install --env=auto`
- Or: paste install URL to agent for self-install (not recommended for security-sensitive environments)
- Diagnostics: `agent-reach doctor`
- Update: `agent-reach update`
- Uninstall: `agent-reach uninstall` (removes all configs, cookies, skill files)
- Registers a SKILL.md in agent's skills directory for auto-discovery
- Works with Claude Code, Cursor, OpenClaw, Windsurf, Codex

## Security

MIT license. Cookie storage at `~/.agent-reach/config.yaml` with chmod 600 — local only, not transmitted. The agent-self-install pattern (fetching instructions from a remote raw GitHub URL) is the primary supply chain risk. Some backend tools install from git URLs rather than pinned package versions. The author recommends dedicated accounts (not primary accounts) for cookie-authenticated platforms due to ban risk. "Vibe coded" admission and single contributor suggest limited security review. Evaluate carefully before use in security-sensitive contexts.