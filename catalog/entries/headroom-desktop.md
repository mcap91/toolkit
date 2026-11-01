---
name: headroom-desktop
title: Headroom Desktop
url: "https://github.com/gglucass/headroom-desktop"
category: plugin
summary: "Solid local-first Claude Code cost optimizer with hook injection into ~/.claude/settings.json — worth monitoring given agent-lockdown relevance, but macOS-only stable and single-contributor"
tags: [token-optimization, cost-reduction, claude-code, proxy, compression, tauri, hook, token-reduction]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: [modifies-claude-settings, anthropic-base-url-redirect, telemetry-aptabase, telemetry-sentry, single-contributor, private-backend-repo, 2gb-runtime-download]
overlaps: []
source: unknown
---

## What it does

Headroom Desktop is a macOS menu-bar tray app (Tauri/Rust shell, Python optimization brain) that intercepts Claude Code's API traffic through a local proxy and applies token-saving transforms before requests reach the Anthropic API. It claims ~50% cost reduction. Three bundled tools: `headroom` (prompt optimization pipeline), `rtk` (rewrites bash command outputs to strip noise before they enter the context window), and `vitals` (project health scanner). All transforms run entirely locally — no data leaves the machine except through the normal Anthropic API call.

On install it: downloads a ~2 GB self-contained Python runtime to `~/.headroom`; injects a `PreToolUse` hook and a rewrite script into `~/.claude/settings.json`; redirects `ANTHROPIC_BASE_URL` to the local proxy; stores a session token in the macOS Keychain. On quit/uninstall it reverses every change. A watchdog auto-pauses if the proxy crashes so Claude Code continues working uninterrupted.

Compression benchmarks (self-reported from the underlying `headroom` library): JSON arrays 86–100%, structured logs 82–95%, multi-tool agentic conversations 56–81%, plain text 43–46%. Code in recent messages is intentionally not compressed.

Stable target is macOS 14+ on Apple Silicon. Linux x86_64 builds exist as an experimental preview covering only the core proxy flow.

## Assessment

**Watch** rather than pilot for three reasons:

1. **Hook injection into agent settings.** The install path writes a `PreToolUse` hook and redirects `ANTHROPIC_BASE_URL` — the exact surface that the `agent-lockdown` skill is designed to harden and audit. Adopting a tool that modifies this surface deserves careful review before use in production agentic workflows.

2. **macOS-only stable build.** This project's primary environment (Windows/WSL, with Linux parity as a goal per memory notes) is not the stable target. Linux support is an experimental preview.

3. **Single-contributor, young project.** Version 0.2.9 from one contributor (gglucass). The supply chain is thin, the account backend lives in a private repo, and the project is new enough that longevity is unproven.

The value proposition is genuine — local-first, zero host pollution, clean uninstall, SHA-256-pinned deps, signed/notarized macOS binary, rollback-before-edit settings changes — and the design is notably transparent and well-engineered. If the Linux build matures and multi-contributor activity increases, this would be a strong pilot candidate.

## Mechanical details

Architecture: Tauri (Rust) desktop shell with a bundled Python runtime. The Rust layer owns tray lifecycle, managed installs, client detection, and auto-update delivery. The Python layer does the optimization work.

Key install footprint:
- `~/.headroom/` — ~2 GB self-contained Python runtime
- `~/.claude/settings.json` — `PreToolUse` hook entry added (backup written first)
- `~/.claude/hooks/headroom-rtk-rewrite.sh` — the hook script
- `~/Library/Application Support/Headroom` — logs, caches, state
- macOS Keychain — session token under `com.extraheadroom.headroom`
- Shell profile (`.zshrc`/`.zprofile`) — managed block prepending `~/.headroom/bin` to PATH

Dependency pinning: `headroom-ai` wheel is pinned by version string, exact PyPI wheel URL, and SHA-256 in `src-tauri/src/tool_manager.rs`. The Python standalone runtime and other bundled components are pinned the same way — one version, one checksum, per platform.

Release process: feature branches → staging (rc.N) → main (stable). Main is branch-protected; stable releases require an rc ancestor commit; `./scripts/verify-release.sh` must pass before any artifact is published.

What to monitor: Linux build maturity, contributor growth, whether the hook injection pattern becomes configurable/opt-in, and any changes to the private backend's data handling.

## Security

**License:** MIT (desktop shell). Account/backend is a private repo with unknown license — no data flows there during normal use; it only handles opt-in account and paid plan features.

**Dependency pinning:** Strong. Python wheel and all bundled components are pinned by URL + SHA-256. No automatic PyPI upgrade path — users pick up dependency bumps only via a desktop app release.

**Credential handling:** Session token stored in macOS Keychain (correct practice). No plaintext credential storage evident.

**Hook injection:** The app adds a `PreToolUse` hook to `~/.claude/settings.json` and redirects `ANTHROPIC_BASE_URL` to the local proxy. This is the highest-privilege integration point in Claude Code — every tool call passes through it. The code is MIT-licensed and auditable, and the hook script path is disclosed, but this warrants explicit review before deployment in a hardened agent setup.

**Telemetry:** Aptabase analytics key and Sentry DSN are included as build-time env vars. Aptabase is an open-source, privacy-focused analytics backend. Sentry is for error reporting. Both are opt-in keys — the `.env.example` ships with placeholders. Self-hosted or disabled options are not explicitly described.

**Supply chain:** Single contributor. Signed and notarized macOS binary (Gatekeeper-clean). GitHub Actions CI with `verify-release.sh` gate. No evidence of eval or shell injection in the open-source shell code based on the documented architecture. The private backend repo cannot be audited.

**Security flags summary:** `modifies-claude-settings` (PreToolUse hook injection), `anthropic-base-url-redirect` (local proxy intercept), `telemetry-aptabase`, `telemetry-sentry`, `single-contributor`, `private-backend-repo`, `2gb-runtime-download`.
