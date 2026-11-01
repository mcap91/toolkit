---
name: scrub-context-engineering
title: "SCRUB: A Framework for Context Engineering in Claude Code"
url: "https://example.com"
category: agent-pattern
summary: "Five-action framework (Subagents, Cut/rewind, Reduce/compact, Upload/handoff, Burn/clear) for proactively managing an agent's context window, from a practitioner report of ~3000 hours in Claude Code"
tags: [context-engineering, subagents, compaction, context-management, claude-code, attention]
reviewed: 2026-08-09
acquired: 2026-08-09
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---

## What it does

Names five distinct actions for managing an agent's context window, framed as the mnemonic SCRUB, drawn from roughly 3000 hours of hands-on Claude Code use:

- **S — Subagents**: dispatch disposable workers that carry their own separate context window, keeping bulk exploration/research out of the main conversation
- **C — Cut/rewind**: use conversation time-travel to jump back to an earlier point, restoring code state while trimming the accumulated conversation history
- **R — Reduce/compact**: summarize the conversation in place rather than letting it grow unbounded
- **U — Upload/handoff**: write context out to files, clear the conversation, then re-inject only what's needed from those files
- **B — Burn/clear**: a full reset of the conversation when the above aren't sufficient

## Differentiators / Key takeaways

- Context rot is described as having no clean dropoff point — degradation is gradual, not a cliff
- Attention degrades starting from the first token, not just once the window fills up
- Cites the "Lost in the Middle" effect (content in the middle of a long context is attended to less reliably than content at the start or end)
- Central claim: proactive context management (trimming/handing off before problems appear) outperforms reactive management (waiting until the agent visibly degrades)
- Author's reported baseline configuration is roughly 16k tokens of fixed overhead, achieved by: disabling unused tools, running without a CLAUDE.md, setting skills to `disable-model-invocation`, and turning auto-compact off (managing compaction manually via the R action instead)

## Mechanical details / What to adopt

The five SCRUB actions map roughly to session lifecycle stages: subagents for parallel/disposable work, cut/reduce for mid-session trims, upload for cross-session continuity, burn as the reset valve. The auto-compact-off + manual-compact stance is a specific, adoptable configuration choice, not just a general principle.

## Security

Reference/pattern content — no code shipped, no security concerns.

## Usage notes

- **Disable Artifact tool to save ~10K tokens per session**: The Artifact tool definition consumes ~10K of the ~20K system tool definition tokens loaded at session start — roughly half the tool-definition overhead and ~5% of the effective 200K "smart zone." Three ways to disable: (1) `"enableArtifact": false` in `~/.claude/settings.json` (permanent), (2) `claude --disallowed-tools Artifact` (per-session), (3) env var `CLAUDE_CODE_DISABLE_ARTIFACT=1`.
