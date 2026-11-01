---
name: agent-browser
title: Agent Browser (Vercel Labs)
url: "https://github.com/vercel-labs/agent-browser"
category: cli-tool
summary: "Rust-native browser automation CLI for AI agents — snapshot-based accessibility tree with ref selectors, MCP server mode, annotated screenshots, multi-session isolation, plugin system, cloud provider integrations (Browserbase/Browserless/AWS AgentCore); Apache-2.0, Vercel-backed"
tags: [browser-automation, cli, mcp, rust, web-scraping, testing, ai-agent]
reviewed: 2026-06-19
acquired: 2026-06-19
license: Apache-2.0
security_flags: []
overlaps: [browser-use]
source: unknown
---

## What it does

Fast native Rust CLI for AI-agent-driven browser automation. Client-daemon architecture — daemon manages Chrome via CDP, CLI sends commands. Key capabilities:

- **Snapshot refs**: accessibility tree with `@e1`-style refs for deterministic element selection — the core AI workflow
- **MCP server mode**: `agent-browser mcp` with tool profiles (core, network, react, mobile, state, debug, tabs, all)
- **Annotated screenshots**: numbered overlays matching ref IDs for multimodal agents
- **Multi-session isolation**: named sessions with separate cookies, storage, auth state
- **Auth management**: profile reuse, session persistence, encrypted vault, state import from running Chrome
- **Plugin system**: out-of-process plugins for credential providers, cloud browsers, stealth, CAPTCHA solving
- **Cloud providers**: Browserbase, Browserless, Browser Use, Kernel, AWS AgentCore — swap local Chrome for cloud browser with env vars
- **React DevTools**: component tree, fiber inspection, render profiling, Suspense boundary analysis
- **Web Vitals**: LCP/CLS/TTFB/FCP/INP metrics
- **Batch execution**: multiple commands in one invocation to avoid per-command overhead
- **iOS Simulator**: real Mobile Safari testing via Appium
- **Observability dashboard**: live viewport streaming + activity feed on localhost

## Assessment

The most comprehensive agent-browser CLI available. Vercel backing gives confidence in maintenance and quality. The snapshot→ref workflow is the right abstraction for LLM-driven browsing — more reliable than CSS selectors or coordinate-based clicking. The MCP server mode with tool profiles keeps context small for everyday use while allowing full surface when needed.

Security design is thoughtful: domain allowlists, action policies, confirmation gates, content boundary markers, and encrypted credential vault. The plugin system isolates third-party code out-of-process.

For bioinformatics agent workflows: useful for accessing web portals (NCBI, EBI, Galaxy), filling out web-based analysis forms, and scraping results from tools that only have web UIs. The cloud provider integrations make it deployable in CI/CD and serverless contexts.

## Mechanical details

- **Install**: `npm install -g agent-browser && agent-browser install` (downloads Chrome for Testing)
- **Also**: Homebrew (`brew install agent-browser`), Cargo, from source
- **Platforms**: macOS ARM64/x64, Linux ARM64/x64, Windows x64 — all native Rust
- **MCP config**: `{"command": "agent-browser", "args": ["mcp"]}`
- **Skill install**: `npx skills add vercel-labs/agent-browser` for Claude Code
- **Config**: `agent-browser.json` (project) or `~/.agent-browser/config.json` (user), plus env vars
- **Daemon**: auto-starts on first command, persists between commands, configurable idle timeout

## Security

- **License**: Apache-2.0
- **Dependencies**: native Rust binary, Chrome for Testing (Google's official automation channel)
- **Code quality**: comprehensive CLI with `doctor` diagnostic command, JSON schema for config validation
- **Supply chain**: Vercel Labs (major company), active development
- **Security features**: domain allowlists, action policies, content boundaries, encrypted credential vault, plugin capability gating
- **Dangerous patterns**: `eval` command executes arbitrary JS in browser context (inherent to browser automation); `--allow-file-access` flag explicitly required for local file access
- **Maintenance**: actively developed, Vercel-backed, regular releases