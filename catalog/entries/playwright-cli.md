---
name: playwright-cli
title: Playwright CLI
url: "https://github.com/microsoft/playwright-cli"
category: cli-tool
summary: "Microsoft-maintained CLI interface to Playwright browser automation (npm package @playwright/cli), pitched as more token-efficient than Playwright MCP for coding agents since it avoids loading MCP tool schemas and full accessibility trees into model context; installs as a Claude Code / GitHub Copilot skill"
tags: [playwright, browser-automation, cli, testing, coding-agent, skill, screenshots, network-mocking, tracing]
reviewed: 2026-08-09
acquired: 2026-08-09
license: Apache-2.0
security_flags: []
overlaps: [browser-use]
source: unknown
---

## What it does

Playwright CLI provides command-line access to Playwright browser automation, positioned by its README as the better fit for coding agents compared with Playwright MCP: CLI invocations avoid loading large MCP tool schemas and verbose accessibility trees into the model's context, so an agent issues concise, purpose-built commands instead. The README frames Playwright MCP as still preferable for agentic loops that need persistent state and iterative reasoning over page structure (self-healing tests, exploratory automation), positioning the two as complementary rather than strictly one replacing the other.

Commands cover navigation (`open`, `goto`, `close`, `go-back`, `reload`), interaction (`click`, `type`, `fill`, `drag`, `hover`, `select`, `upload`, `check`), snapshot-based element targeting (`snapshot` returns refs; elements can also be targeted by CSS selector or Playwright locator string), keyboard/mouse control, screenshots/PDF/video capture, tracing, console/network/request inspection, request mocking (`route`), and storage management (cookies, localStorage, sessionStorage, full storage-state save/load). A `playwright-cli show` command opens a visual dashboard with a live-screencast session grid and a per-session detail view supporting full remote takeover of mouse/keyboard — useful for observing or steering agent-driven browser sessions running in the background.

## Differentiators

- Snapshot-based `ref` targeting plus a `find` command (grep-style text/regex search over a snapshot) lets an agent locate elements without pulling the entire accessibility tree into context on every step; `snapshot --depth=N` further limits scope for efficiency.
- Named, addressable sessions (`-s=name`, or the `PLAYWRIGHT_CLI_SESSION` env var) let multiple projects or concurrent agent runs use isolated in-memory or `--persistent` (disk-backed) browser profiles.
- Shares its configuration surface (JSON config file or `PLAYWRIGHT_MCP_*` environment variables) with Playwright MCP — allowed/blocked origins and hosts, headless mode, browser channel, CDP endpoint, proxy, secrets file, output directory, and more.
- Ships detailed per-task reference guides (test running/debugging, request mocking, running arbitrary Playwright code, session management, storage-state handling, test generation via plan/generate/heal, tracing, video recording, attribute inspection) alongside the installed skill.

## Mechanical details

- Install: `npm install -g @playwright/cli@latest`; requires Node.js 18+.
- Install the agent skill: `playwright-cli install --skills` (Claude Code and GitHub Copilot pick up locally installed skills automatically); without the skill, an agent can still discover commands via `playwright-cli --help`.
- Headless by default; pass `--headed` to `open` to watch the browser.
- Local (non-global) fallback: `npx --no-install playwright cli ...` if the global command isn't available.
- Config file default path: `.playwright/cli.config.json`, or pass `--config path/to/config.json`.
- The older `playwright-cli` npm package is deprecated in favor of the `@playwright/cli` package documented here; both are published from the same `microsoft/playwright-cli` repository by the Playwright team.

## Security

Apache-2.0 licensed, maintained by the Microsoft Playwright team in the `microsoft/playwright-cli` GitHub org — an established, actively maintained project rather than an independent third party. File uploads are restricted to paths within configured MCP/workspace roots by default (`allowUnrestrictedFileAccess` must be explicitly set to widen this), and navigation to `file://` URLs is blocked unless `PLAYWRIGHT_MCP_ALLOW_UNRESTRICTED_FILE_ACCESS` is set. Network access can be scoped via `PLAYWRIGHT_MCP_ALLOWED_ORIGINS`/`PLAYWRIGHT_MCP_BLOCKED_ORIGINS`, though the docs explicitly caveat these are not a security boundary and do not affect redirects. Because it drives a real, potentially headed browser with persistent-profile and CDP-attach options, it can reuse existing browser sessions/cookies (`--persistent`, `attach --cdp`) — scope sessions and allowed origins deliberately when handling authenticated sites. No eval-style or credential-harvesting patterns are documented in the CLI surface itself.