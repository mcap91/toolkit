---
name: kasetto
title: Kasetto
url: "https://github.com/pivoshenko/kasetto"
category: cli-tool
summary: "Declarative environment manager for AI coding agents — one YAML config syncs skills, MCPs, commands, and instructions across 23 agents (Claude Code, Cursor, Codex, etc.) with lockfile pinning, secret injection, and per-agent format translation; Rust binary"
tags: [environment-manager, skills, mcp, configuration, multi-agent, rust]
reviewed: 2026-09-16
acquired: 2026-09-16
license: MIT OR Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Kasetto is a declarative environment manager for AI coding agents, written in Rust. A single YAML config (`kasetto.yaml`) describes the desired state of an agent environment — skills, MCP servers, commands, and instructions — and `kst sync` brings the local machine to that declared state. A lockfile (comparable to `Cargo.lock`) pins the exact resolved state (content hashes) for reproducibility across machines and CI; subsequent syncs diff against the lockfile and only touch what changed.

Four asset kinds are managed:
- **Skills**: reusable capabilities pulled from source repositories
- **MCPs**: Model Context Protocol server configs, merged into each agent's native settings file
- **Commands**: named directives (e.g., git operations)
- **Instructions**: prompt guidelines / agent rules (markdown or MDC format)

Kasetto auto-transforms each asset into the native format expected by the target agent, so one source config can populate Claude Code, Cursor, Codex, Windsurf, Copilot, Gemini CLI, and other supported tools without manual per-tool translation. Configs can be scoped globally or per-project, and can compose via `extends` so org/team/project configs layer on top of each other.

## Differentiators

- 23 built-in agent presets (Claude Code, Cursor, Codex, Windsurf, Copilot, Gemini CLI, Antigravity, OpenCode, and others) with automatic per-agent format translation from one source config
- Lockfile-based reproducibility modeled on Cargo/uv: content-hashed, diffed on each sync so only changed assets are touched
- Secret injection via `${kst:...}` placeholders resolved from environment variables, credentials.yaml, 1Password, HashiCorp Vault, KeePassXC, AWS Secrets Manager, Google Secret Manager, Azure Key Vault, pass/gopass, and macOS Keychain — no credentials file is written by the tool itself
- Pulls from any git host — GitHub, GitLab, Bitbucket, Codeberg, and self-hosted/enterprise instances — including private repos
- Sparse extraction for monorepos (pulls only the needed subpath) and parallel downloads
- Single static Rust binary (macOS, Linux, Windows), no runtime dependencies
- CI-friendly flags: `--dry-run`, `--locked`, `--json`, real exit codes

## Mechanical details

- **Install**: single static binary, released for macOS/Linux/Windows
- **Init**: `kst init` (project scope) or `kst init --global`
- **Add a source**: `kst add <source>` appends to the config while preserving comments
- **Apply state**: `kst sync` (supports `--dry-run` to preview, `--locked` to enforce the lockfile, `--json` for machine-readable output)
- **Self-update**: `kst self update` verifies the downloaded binary against a release `checksums.txt` via SHA256 before replacing the existing binary
- **Docs**: https://kasetto.dev

## Security

- **License**: dual-licensed MIT OR Apache-2.0
- **MCP merge behavior**: `kst sync` merges new MCP entries into each agent's native settings file automatically, with no confirmation prompt by default (`--dry-run` available to preview first); it does not overwrite MCP entries it didn't install itself — only a kasetto-managed entry is replaced, and only under `--update`
- **Code execution**: does not execute skill code
- **Credentials**: does not write a credentials file, but can read one (`credentials.yaml`) and other configured backends for secret injection at sync time
- **Update integrity**: `kst self update` checksum-verifies (SHA256) the new binary against the GitHub release's `checksums.txt` before applying; aborts on mismatch
- **Maintainer/activity**: single-maintainer project (pivoshenko); ~200 GitHub stars, ~509 commits, 9 forks, 3 open issues as of intake
