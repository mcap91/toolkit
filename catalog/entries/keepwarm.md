---
name: keepwarm
title: keepwarm (Claude Code prompt-cache keep-warm mod)
url: https://github.com/declanbx/keepwarm
category: plugin
summary: Claude Code mod (early-access plugin/hooks feature) that keeps an idle interactive session's prompt cache warm by forking a tool-less, text-free copy of the session's own transcript as a cache-read ping once 57 minutes pass with no model request — restarts the 1-hour cache TTL without adding anything to the conversation; stops after 20h since the last real prompt, after a refresh that reads under 1,000 cached tokens, or if a refresh gets no reply; turns itself off for a session if a refresh has to write more of the conversation than it reads (cache unreachable — 6 of 132 refreshes on record did this); never runs under claude -p or the SDK. Controlled via /keepwarm on|off|status and env vars (KEEPWARM_OFF, KEEPWARM_IDLE_MIN, KEEPWARM_TTL_MIN, KEEPWARM_MAX_HOURS, KEEPWARM_PROMPT); state kept locally in ~/.claude/state/keepwarm/<session id>.json. Installed by cloning into a folder referenced by CLAUDE_CODE_PLUGIN_DIRS.
tags:
  - claude-code
  - prompt-caching
  - cache-warming
  - mod
  - plugin
  - hooks
  - cost-optimization
  - early-access
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps:
  - cold-cache-session-resume
  - anthropic-prompt-caching-guide
license: MIT
security_flags: []
source: reddit
source_url: https://www.reddit.com/r/ClaudeCode/comments/1x1ybwb/best_way_to_handle_cold_cache_hits_you_overpay_5x/
---

## What it does

A Claude Code "mod" (the early-access plugins-of-function-hooks feature; interface may change
between Claude Code releases, and only loads where the feature is switched on) that keeps an
idle interactive session's prompt cache warm. Inspired by `cachebeat` (ARahim3), a similar
Claude Code skill using an inactivity-triggered heartbeat; keepwarm does the same job as a mod
instead — the refresh is a tool-less fork of the session sent beside it, so nothing is added to
the visible conversation.

Mechanism: once the main thread sends no model request for 57 minutes (`KEEPWARM_IDLE_MIN`), it
forks a copy of the session's own transcript and sends a minimal cache-read ping (reply text
`..`). The API serves the cached prefix and restarts its 1-hour TTL clock. The clock restarts on
any request (a prompt, a tool return, or a refresh); a subagent's own transcript and TTL are not
affected (subagents use the 5-minute TTL regardless). Refreshing stops 20 hours after the last
real prompt (`KEEPWARM_MAX_HOURS`), when a refresh reads under 1,000 cached tokens, or when a
refresh gets no reply (dropped connection, abort, 429/529 — retried on the next 30s tick instead).
If a refresh inside the hour has to write more of the conversation than it reads (the fork
couldn't reach that session's cache), keepwarm turns itself off for that session until
`/keepwarm on`; the author logged this on 6 of 132 refreshes across a Team-plan and a Max-plan
account. Never active for headless runs (`claude -p` or SDK sessions, where `isInteractive` is
false).

Controlled via `/keepwarm off | on | status` per session, with a status row under the prompt
(`keepwarm: on, no refresh yet`, `keepwarm: last refresh 20:19, read 50k cached`, etc.). State is
written to `~/.claude/state/keepwarm/<session id>.json` and stays on the local machine.
Environment overrides: `KEEPWARM_OFF`, `KEEPWARM_IDLE_MIN` (57), `KEEPWARM_TTL_MIN` (60),
`KEEPWARM_MAX_HOURS` (20), `KEEPWARM_PROMPT`. Installed by cloning the repo into a folder listed
in `CLAUDE_CODE_PLUGIN_DIRS` inside `~/.claude/settings.json`'s `env` block, then starting a new
session.

The README publishes its own cost math: each refresh reads the full cached conversation at the
cached-token rate (Opus 5.5 API pricing, $0.20/M cached tokens) — about $0.02 per refresh for a
100k-token conversation, ~$0.16 for 800k. A session idle for 20 hours refreshes roughly once an
hour (~21 refreshes), costing an estimated ~$3.40 total on an 800k-token conversation, against
~$6.40 to rewrite that same 800k tokens once at the 2x write price when it finally goes cold. On
a subscription plan, refreshes count against usage limits instead of billing directly.

Includes a test suite (`claude plugin test`) and type checking (`tsc` against Claude Code's
plugin types); version history published back to 0.1.0 (2026-10-02), currently 0.3.1
(2026-10-07). Single-maintainer project (Declan Brennan).

## Security

Runs as a Claude Code mod with access to fork session transcripts and send API requests on the
user's behalf — review the hooks module before installing, as with any third-party plugin that
executes alongside every session. State file and refresh history stay local to the machine
(no telemetry described in the README). MIT license.
