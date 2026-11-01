---
name: cold-cache-session-resume
title: Cold-Cache Session Resume Strategies (trim vs compact vs keep-warm)
url: https://www.reddit.com/r/ClaudeCode/comments/1x1ybwb/best_way_to_handle_cold_cache_hits_you_overpay_5x/
category: agent-pattern
summary: Practitioner techniques for resuming a long agent session after its prompt cache has expired (>5 min or >1 h idle) — the first resumed turn re-reads the whole prefix at full input price (author measured ~5x a warm turn); below ~150K context just continue, above it either trim (replace old tool results with one-line stubs, strip thinking blocks, no model call; same-provider only) or compact with a cheap model (e.g. Haiku summary + last 2 exchanges; works cross-provider); prevent coldness with UX warnings, keep-warm pings, or the API's 1-hour cache TTL (2x write vs 1.25x for 5-minute); never splice summaries into the middle of a warm session since the cache is prefix-based
tags:
  - prompt-caching
  - context-management
  - cost-optimization
  - session-resume
  - compaction
  - claude-code
  - cache-ttl
  - token-efficiency
  - harness-design
reviewed: 2026-10-26
acquired: 2026-10-26
overlaps:
  - anthropic-prompt-caching-guide
  - prompt-assembly-cache-discipline
  - scrub-context-engineering
  - agent-session-resume
  - claude-code-fable-cost-playbook
license: N/A
security_flags: []
source: unknown
---

## What it does

Collects techniques from an r/ClaudeCode thread (Oct 2026, started by a meta-harness developer) for the cost spike when a session resumes after its prompt cache has gone cold. The cost comes from re-reading the cached prefix at full price, not from what is typed — "Continue" and a long instruction cost the same on that turn.

Decision rule proposed by the author (benchmarked with Opus 5.5 xhigh):

- **< ~150K tokens of context:** resume normally; the one-time re-read is acceptable and the model continues best from its own transcript.
- **> ~150K, same provider:** **trim** — deterministic rewrite of the transcript replacing older tool results with one-line stubs and stripping thinking blocks, no extra model call. Author reports a trimmed Claude session retained work memory better than seed/compact approaches.
- **> ~150K, switching provider:** **compact** — summary by a cheap model (Haiku 5.5 or similar) plus the last couple of exchanges; needed because session-record formats are incompatible across providers. A commenter's reading of the author's own cost table: cheap summary + last 2 exchanges cost less (2.48) than the deterministic trimmer (3.61), versus 10.68 for replaying everything.

Prevention and adjacent tips from replies:

- UI warnings before a session goes cold; auto-pings to keep the cache warm (one commenter pings every 58 minutes outside "away mode"; another reserves ~1% of usage limit for pings); open-source keep-warm mods exist (e.g. `github.com/declanbx/keepwarm`).
- Use the API's 1-hour cache TTL when gaps are between 5 minutes and an hour (write costs 2x base vs 1.25x for the 5-minute TTL).
- Subagents use the 5-minute cache; long-running compute inside a subagent repeatedly hits cold cache — have the agent wake every ~4 minutes, or write a handoff and restart fresh if compute exceeds ~12 minutes and context exceeds ~200K.
- Prefix caching means trimming or splicing a summary into the middle of a warm session invalidates every later turn; only do it when the cache is already cold. Dropping from the tail preserves the prefix.
- Freeze a session in the harness once its cache cools so an accidental message doesn't bill a full re-read; offer explicit choices (trim / compact with cheap model / continue from full transcript).
- Manual variant: export the JSONL, strip thinking and tool output, `/clear`, paste back; or `/export` and have another model write a handoff (key files, done/active/pending work).

## Security

Discussion content, no code. Third-party keep-warm plugins and harness mods modify session behavior and should be reviewed before installing.
