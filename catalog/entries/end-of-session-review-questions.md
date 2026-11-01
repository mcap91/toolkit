---
name: end-of-session-review-questions
title: End-of-Session Review Questions
url: "https://example.com"
category: agent-pattern
summary: "Two standing end-of-session prompts ('what are you least confident about' and 'what am I probably missing') used to surface glossed-over assumptions and context gaps, with community variants and known failure modes"
tags: [prompting, meta-prompting, confidence, verification, session-review, agent-pattern]
reviewed: 2026-08-09
acquired: 2026-08-09
license: NOASSERTION
security_flags: []
overlaps: [confidence-probing-prompts]
source: unknown
---

## What it does

Describes a practice of asking two fixed questions at the end of every Claude session:

1. **"What are you least confident about in what you just did?"** — forces enumeration of assumptions and issues the agent glossed over during the session. Reported to catch a real problem roughly 25% of the time.
2. **"What's the biggest thing I'm probably missing that I haven't thought to ask?"** — aimed at the user's blind spots rather than the agent's; surfaces "you told me X but Y will bite you later" class issues that a narrowly-scoped session wouldn't otherwise reveal.

Community-contributed additions collected alongside the core pair: "What did you just tell me works that you didn't actually verify?" (targets unverified success claims specifically), requesting explicit numeric confidence scores per claim, and using a dedicated `/reflection` command to run this check consistently.

## Differentiators / Key takeaways

This is a near-duplicate of the existing catalog entry `confidence-probing-prompts` — both center on the same two core questions ("least confident about" and "biggest thing missing"). The distinguishing content here is operational rather than conceptual: it frames the questions as a fixed **end-of-session ritual** rather than an ad hoc prompting technique, adds the "what did you claim works but didn't verify" variant, and — notably — documents two caveats not present in the other entry:

- **Token cost**: asking both questions at the end of a long session is expensive relative to the value returned, since the model has to re-scan a large context to answer honestly.
- **Bait for hallucinated "revelations"**: the second question ("what am I missing") can pressure the model into inventing a plausible-sounding but false gap just to produce an answer, rather than reporting genuine uncertainty.

## Mechanical details / What to adopt

Run the two questions as a closing step before ending a session or before committing/merging significant work; treat any answer to question 2 with more skepticism than question 1, given the documented tendency to fabricate a plausible gap when none is actually known.

## Security

Reference/pattern content — no code shipped, no security concerns.