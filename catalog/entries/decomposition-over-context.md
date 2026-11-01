---
name: decomposition-over-context
title: "Decomposition Over Context: Chat Is the Wrong Abstraction"
url: "https://example.com"
category: agent-pattern
summary: "Argues larger context windows aren't the fix for agentic-coding limits — task decomposition with explicit ownership, dependencies, and file boundaries is; illustrated with a TESTER/FIXER agent split and an issue-based parallel-implementation workflow"
tags: [context-engineering, decomposition, subagents, software-engineering-workflow, github-issues, agent-orchestration]
reviewed: 2026-08-09
acquired: 2026-08-09
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---

## What it does / What it says

Central argument: "chat is the wrong abstraction for software engineering." Bigger context windows are framed as treating the symptom, not the cause — a context window is working memory for the current turn, not project memory across a whole effort. Compaction preserves the conversation's gist but loses the actual decisions made along the way, which is what later work actually needs.

The concrete example given is a TESTER/FIXER agent pair with explicit ownership boundaries: TESTER owned test structure (had exclusive authority to change it); FIXER was allowed to continue making functional code changes but had to respect TESTER's ownership and wait on/coordinate around it rather than editing test structure itself. The argument is that this kind of explicit ownership, dependency tracking, file-boundary assignment, and defined resume conditions is what makes multi-agent engineering work reliably — not a larger shared context.

## Differentiators / Key takeaways

- Companion piece referenced: "The next generation of software engineering won't happen inside a chat" — same author's broader thesis that chat-as-interface is a transitional stage, not the end state, for agentic software engineering.
- A practical workflow is described for putting this into practice: ADRs/PRDs kept as in-repo documents (not chat-only decisions), GitHub issues used for planning/task breakdown, a "burn issues" skill that dispatches subagents in waves to implement issues in parallel, each issue resulting in its own PR, with a merge-orchestration tool (mergify) coordinating how those PRs land.

## Mechanical details / What to adopt

The reusable structural pattern: assign explicit ownership of specific files/areas to specific agents/roles, make dependencies and wait-conditions explicit rather than implicit in conversation, and persist decisions as durable repo artifacts (ADRs/PRDs/issues) rather than relying on conversation history or compaction summaries to carry them forward.

## Security

Reference/pattern content — no code shipped, no security concerns.