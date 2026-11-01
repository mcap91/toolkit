---
name: confidence-probing-prompts
title: Confidence-Probing Prompts
url: "https://reddit.com"
category: agent-pattern
summary: "Collection of meta-prompting patterns that surface agent blind spots — 'what are you least confident about' (forces enumeration of uninvestigated areas), 'what's the biggest thing I'm missing' (Altman), plus future-proofing, hidden-bias, and session-improvement variants"
tags: [prompting, meta-prompting, agent-patterns, confidence, verification]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: [claude-decision-pressure-test]
source: unknown
---

## What it does

Two primary prompting patterns plus four variants for surfacing what an AI agent hasn't properly investigated or what the user is missing about a situation.

**Primary patterns:**

1. **"What are you least confident about right now?"** — forces the agent to enumerate 6–7 areas it didn't properly investigate. Author reports ~25% of the time one item is a major issue the agent acted on without understanding. Follow-up: have the agent investigate each issue exhaustively.

2. **"What's the biggest thing I'm missing about the situation right now? What don't I realize?"** — attributed to Sam Altman. Surfaces the user's blind spots rather than the agent's.

**Community-contributed variants:**

3. **Future-proofing:** "If this breaks in 3 months, what's the most likely reason?"
4. **Innovation:** "If you could add one unrequested, industry-leading feature, what would it be?"
5. **Hidden biases:** "What assumptions did you make that you never stated explicitly?"
6. **Session improvement:** "What could I have done differently to make this session smoother?"

## Key takeaways

The confidence-probing pattern works because agents tend to act on incomplete information without flagging uncertainty. Explicitly asking "what didn't you investigate" forces an enumeration that the agent wouldn't volunteer. The hidden-assumptions variant is particularly useful before committing to architectural decisions.

## Security

N/A — prompting patterns, no code or dependencies.