---
name: claude-code-remote-prompt-hardening
title: Claude Code Remote Prompt Hardening
url: "https://www.reddit.com/r/ClaudeCode/comments/1tmizuy/claude_code_v21150_now_allows_anthropic_to/"
category: reference
summary: env vars to block remote system prompt injection in Claude Code; operational hardening knowledge for security-sensitive environments
tags: [claude-code, security, privacy, env-vars, hardening, system-prompt, version-pinning]
reviewed: 2026-05-27
acquired: 2026-05-27
overlaps: []
license: unknown
security_flags: []
source: unknown
---

## What it says

Starting with Claude Code v2.1.150, two network-sourced data channels can inject content into the LLM system prompt at runtime. First, an API call to `api.anthropic.com/api/claude_cli/bootstrap` at startup (cached to disk). Second, a GrowthBook feature flag (`tengu_heron_brook`) that refreshes every 60 seconds with background sync. Previous versions had these injection points as dead code returning null; v2.1.150 activated them. The changelog described this as "Internal infrastructure improvements (no user-facing changes)."

Two environment variables block this behavior:
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` — blocks the bootstrap API call and other non-essential network traffic. Verified by the original researcher.
- `DISABLE_GROWTHBOOK=1` — disables the GrowthBook feature flag sync.

Verification approach (on the Linux binary): `npm pack`, extract, then `strings` the binary to find the minified functions responsible for reading cached values (`nAA`) and registering them as system prompt sections (`Rv("heron_brook", ...)`). Function names are specific to each binary version.

## Assessment

Operational awareness item. Relevant if running Claude Code in environments where you want full control over what enters the system prompt — e.g., when prompt-patching for effectiveness or in security-sensitive contexts. Not a tool to install; these are environment variables to set. The env vars are already documented in the user's workflow for Claude Code customization.

## What to adopt

Set both env vars in shell profile or wrapper script for Claude Code sessions where prompt control matters:

```bash
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
export DISABLE_GROWTHBOOK=1
```

On Windows (PowerShell):

```powershell
$env:CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC = "1"
$env:DISABLE_GROWTHBOOK = "1"
```

Re-verify after each Claude Code upgrade — the minified function names change per binary version, and Anthropic may change the mechanism.

### Version pinning

To prevent Claude Code from auto-updating past a verified version, pin the CLI and disable the auto-updater:

```bash
npm install -g @anthropic-ai/claude-code@2.1.150
```

Add to `~/.claude/settings.json`:

```json
{
  "env": {
    "DISABLE_AUTOUPDATER": "1"
  }
}
```

Or via `jq`:

```bash
jq '.env.DISABLE_AUTOUPDATER = "1"' ~/.claude/settings.json > /tmp/s.json && mv /tmp/s.json ~/.claude/settings.json
```

`DISABLE_AUTOUPDATER` stops the background update check. To also block manual `claude update` commands, use `DISABLE_UPDATES=1` instead. Do not use `npm update -g` to upgrade — always use `npm install -g @anthropic-ai/claude-code@<version>` with an explicit version or `@latest`.

## Security

This entry is a knowledge reference, not an installable tool — there is no software supply chain to audit. The source is a Reddit community post with no formal license; the documented techniques (env vars, version pinning) are derived from reverse-engineering a publicly distributed npm package (`@anthropic-ai/claude-code`), which is MIT-licensed. No code from the entry is executed; the risk surface is limited to the operational decision of whether to apply the described settings.

The security flags are empty because the entry documents mitigations rather than threats: setting `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` and `DISABLE_GROWTHBOOK=1` reduces the attack surface for remote system prompt injection. The primary residual risk is version drift — if Claude Code is upgraded without re-verifying the env var behavior against the new binary, the mitigations may silently stop working. Re-verification via `npm pack` + `strings` after each upgrade is the recommended practice.
