---
name: googleworkspace-cli
title: Google Workspace CLI (gws)
url: "https://github.com/googleworkspace/cli"
category: cli-tool
summary: Rust CLI with agent-first JSON output and 100+ bundled SKILL.md files covering all Workspace APIs; pre-v1.0 with breaking changes expected
tags: [google-workspace, gmail, drive, calendar, sheets, agent-skills, oauth, json-output, rust, meta-skill]
reviewed: 2026-06-10
acquired: 2026-06-10
license: Apache-2.0
security_flags: [pre-v1.0-breaking-changes, unverified-app-scope-limit, runtime-discovery-fetch]
overlaps: []
source: unknown
---
## What it does

`gws` is a single binary CLI that provides uniform command-line access to every Google Workspace API (Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, Apps Script, and more). Rather than shipping a static command list, it fetches Google's own Discovery Service documents at runtime (cached 24 h) and dynamically constructs a full `clap` command tree. All output — success responses, errors, download metadata — is structured JSON, making it directly pipeable to `jq` or consumable by AI agents without parsing.

The repository bundles 100+ SKILL.md files (one per supported API plus higher-level helpers) and 50 curated recipes for common Gmail, Drive, Calendar, and Sheets workflows. Skills can be installed with `npx skills add https://github.com/googleworkspace/cli` or selectively copied per service. Helper commands (`+send`, `+reply`, `+agenda`, `+standup-report`, `+meeting-prep`, `+weekly-digest`, `+email-to-task`, etc.) are hand-crafted on top of the auto-generated surface for common human/agent tasks.

Authentication covers interactive OAuth, headless/CI credential export, service accounts, and pre-obtained access tokens. Credentials are encrypted at rest with AES-256-GCM using the OS keyring (or a file fallback).

## Assessment

**Pilot.** The agent-skills bundle is immediately useful for this repo's focus on reusable Claude Code workflow components — 100+ SKILL.md files matching the catalog's native format is a large, directly applicable asset. The CLI itself is well-designed (structured JSON, typed exit codes, Model Armor integration), and the Apache-2.0 license is clean.

The blockers for `adopt` are: (1) explicitly pre-v1.0 with documented breaking changes expected, (2) the full recommended OAuth scope preset (85+ scopes) is blocked for unverified apps, requiring careful scope selection in practice, and (3) runtime Discovery Document fetching introduces a network dependency at command-parse time with no documented certificate pinning. These are manageable but warrant piloting before committing workflows to it.

## Mechanical details

- **Language:** Rust (binary distribution via GitHub Releases, Homebrew, Nix, or `npm install -g` as a downloader shim)
- **Architecture:** Two-phase parse — service name from `argv[1]`, fetch Discovery Document, build `clap::Command` tree, re-parse remaining args, authenticate, execute
- **Discovery cache:** 24-hour TTL; all API surface additions are picked up automatically
- **Output format:** Structured JSON for all responses; NDJSON for paginated streams (`--page-all`)
- **Pagination:** `--page-all`, `--page-limit <N>`, `--page-delay <MS>` flags
- **Auth precedence:** token env var > credentials file > encrypted credentials > plaintext credentials
- **Model Armor:** optional `--sanitize <template>` flag pipes responses through Google Cloud Model Armor for prompt-injection filtering (`warn` or `block` mode)
- **Exit codes:** 0 success / 1 API error / 2 auth error / 3 validation / 4 discovery error / 5 internal
- **Skills install:** `npx skills add https://github.com/googleworkspace/cli` (all) or per-service paths
- **Gemini CLI integration:** `gemini extensions install https://github.com/googleworkspace/cli`

## Security

**License:** Apache-2.0 — permissive, no copyleft obligations.

**Credential handling:** Credentials encrypted at rest with AES-256-GCM; key in OS keyring by default with a file fallback (`~/.config/gws/.encryption_key`). Credential export (`gws auth export --unmasked`) produces a plaintext JSON file — must be handled carefully in CI.

**Runtime network dependency:** Discovery Documents are fetched from Google APIs at command parse time. No documented certificate pinning beyond the OS TLS stack; a MITM could theoretically inject a malformed Discovery Document, though exploitation is constrained by the clap command-building path.

**OAuth scope exposure:** The recommended scope preset includes 85+ scopes, which exceeds the ~25-scope limit for unverified (testing-mode) OAuth apps. Operators should select only required service scopes (`gws auth login -s drive,gmail`) to minimize the blast radius of a compromised token.

**Not officially supported by Google:** Community project under the `googleworkspace` GitHub org but explicitly disclaimed as not a Google product. Supply chain and release signing should be verified against GitHub Releases before deploying in sensitive environments.

**`security_flags` rationale:** `pre-v1.0-breaking-changes` — documented instability; `unverified-app-scope-limit` — broad default scope preset is a footgun; `runtime-discovery-fetch` — network call at parse time without documented pinning.
