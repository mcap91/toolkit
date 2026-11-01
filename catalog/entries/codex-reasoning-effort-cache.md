---
name: codex-reasoning-effort-cache
title: Codex reasoning_effort_override (Prompt Cache Preservation)
url: "https://github.com/openai/codex/issues/42996"
category: reference
summary: "Undocumented Codex CLI flag (reasoning_effort_override) that preserves 98.9% prompt cache when switching Astra reasoning effort levels — instead of changing the request-level effort (which invalidates the cache), adds a trusted configuration_update to the conversation; tested on bundled 0.155.0-alpha.2.6 in ChatGPT 26.911.61220"
tags: [codex, openai, gpt-6-astra, prompt-caching, reasoning-effort, workaround, cli]
reviewed: 2026-09-25
acquired: 2026-09-25
license: N/A
security_flags: []
overlaps: []
source: unknown
---

## What it does

Workaround for Codex CLI prompt cache invalidation when switching GPT-6 Astra reasoning effort levels.

**Problem:** Changing reasoning effort on a Codex session changes the request parameters, invalidating the prompt cache. On a low → medium switch: only 55.8% cache hit (12,160/21,791 tokens).

**Fix:** Enable `reasoning_effort_override` flag. Codex keeps the request-level effort fixed and instead adds a trusted `configuration_update` to the conversation. Result: 98.9% cache hit (21,504/21,743 tokens). Switching back: 99.3% cached.

**Usage:**
```
codex --enable reasoning_effort_override -m gpt-6-astra   # one session
codex features enable reasoning_effort_override            # persistent
```

**Caveats:** Marked "under development"; tested on bundled 0.155.0-alpha.2.6. Newer builds also check a model-capability flag. Astra-only as of Sep 2026. Fully quit and reopen the Mac app after enabling.

Discussion source: r/codex (Sep 2026). GitHub issue #42996 was the discovery vector.

## Assessment

Niche but high-value for heavy Codex users switching effort levels mid-session. The underlying technique (conversation-level config injection instead of request-level parameter changes) is a general pattern worth noting for any system with prefix caching.