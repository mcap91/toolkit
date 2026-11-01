---
name: rtk
title: rtk — CLI Proxy for LLM Token Reduction
url: "https://github.com/rtk-ai/rtk"
category: cli-tool
summary: "Directly reduces Claude Code token costs 60-90% via transparent Bash hook; Windows hook requires WSL but filters work natively"
tags: [token-optimization, claude-code, cli, rust, bash-hook, ai-tooling, token-reduction]
reviewed: 2026-06-10
acquired: 2026-06-10
license: Apache-2.0
security_flags: [curl-pipe-sh-install, hook-rewrites-all-bash]
overlaps: []
source: unknown
---

## What it does

rtk is a single Rust binary CLI proxy that intercepts shell commands and compresses their output before it reaches the LLM context window. It wraps 100+ dev commands (git, cargo, npm, docker, kubectl, AWS CLI, test runners, linters, etc.) and applies four strategies — smart filtering, grouping, truncation, and deduplication — to strip noise while preserving signal. Claimed savings are 60–90% per command type, aggregating to ~80% reduction over a typical 30-minute coding session.

For Claude Code the integration is a PreToolUse bash hook installed via `rtk init -g`. Every Bash tool call is transparently rewritten to `rtk <cmd>` before execution, giving 100% adoption across all subagents and conversations without any per-call overhead. Built-in Read, Grep, and Glob tools bypass the hook (they are not Bash calls), so those continue to use Claude's native implementations.

Additional features: `rtk gain` analytics for tracking actual savings, `rtk discover` to find missed opportunities, tee fallback that saves full output on failure for LLM recovery, and per-project TOML config for excluding commands or adjusting filter aggressiveness.

## Assessment

**Pilot** — the value proposition is concrete and directly applicable: this project uses Claude Code heavily and token consumption from verbose Bash outputs is a real cost. The hook mechanism is well-designed (auditable shell script, not opaque binary injection), the license is clean, and the telemetry is opt-in with GDPR compliance. 

The main constraint for this environment is Windows-native: the auto-rewrite hook (`rtk-rewrite.sh`) requires a Unix shell, so on native Windows it falls back to CLAUDE.md injection mode (instructions added to project file, no automatic rewriting). The project platform memory explicitly lists WSL as an acceptable fallback, so the full hook experience is achievable. Filters themselves work on native Windows — only the auto-rewrite hook is WSL-only.

Pilot (not adopt) because: (1) the hook occupies a privileged position rewriting all Bash commands — should be validated in practice before committing; (2) savings estimates are README-stated benchmarks, not measured against this specific project's actual command mix; (3) Windows/WSL setup adds friction to confirm before recommending broadly.

## Mechanical details

**Installation (recommended for this project):**
```sh
# Inside WSL for full hook support
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
rtk init -g   # installs PreToolUse hook + RTK.md into Claude Code global settings
```

**Hook mechanism:** `rtk init -g` writes a PreToolUse bash hook entry to Claude Code's `settings.json`. When Claude Code invokes a Bash tool call, the hook rewrites the command to `rtk <cmd>` before execution. The hook is a shell script (`rtk-rewrite.sh`) and can be inspected at `~/.local/share/rtk/`.

**Key commands:**
- `rtk gain` — summary of tokens saved to date
- `rtk discover` — scan recent sessions for commands that could have been filtered
- `rtk session` — RTK adoption rate across recent sessions
- `rtk init -g --uninstall` — clean removal of hook and injected files

**Config** (`~/.config/rtk/config.toml`): exclude specific commands from rewriting, set tee mode (failures/always/never), per-project filter overrides.

**Scope limitation:** only Bash tool calls are rewritten. Claude Code's built-in Read, Grep, Glob tools are not affected — use explicit `rtk read`, `rtk grep`, `rtk find` for those when needed.

**Windows native fallback:** filters work via explicit `rtk <cmd>` calls; hook auto-rewrite does not work without WSL.

## Security

**License:** Apache-2.0 — permissive, no copyleft obligations.

**Hook position:** The PreToolUse bash hook is in a privileged position — it rewrites every Bash command before Claude Code executes it. This is auditable (it's a shell script) but should be reviewed before installation. If rtk is compromised or behaves unexpectedly, it sits between Claude and every shell command.

**Installation method:** The quick-install uses `curl -fsSL ... | sh` — a standard but trust-on-first-use pattern with no signature verification. Homebrew install is preferable for a verified supply chain. Cargo source install is also available.

**Telemetry:** Disabled by default, explicit opt-in required. Collects salted device hash (not reversible), usage counts, command category distribution, and estimated savings. No source code, file paths, command arguments, secrets, or environment variables are collected. `rtk telemetry forget` triggers server-side erasure. GDPR Art. 6/7 compliant per documentation. Override: `RTK_TELEMETRY_DISABLED=1`.

**AWS output stripping:** rtk explicitly strips secrets and policy documents from AWS CLI output (e.g., `aws iam list-roles` strips policy docs, `aws lambda list-functions` strips secrets). This is a positive security behavior.

**RTK.md injection:** `rtk init -g` adds an `RTK.md` file to the project. This file should be reviewed — it contains instructions injected into the Claude Code context on Windows/CLAUDE.md mode.

**Maintenance:** Active project (v0.28.2 current), named 3-person core team, Discord community, multi-language documentation, Apache-2.0. No evidence of stale maintenance.

**Security flags:** `curl-pipe-sh-install` (quick install lacks signature verification; prefer Homebrew), `hook-rewrites-all-bash` (hook sits in privileged command-rewrite position; auditable but worth noting).
