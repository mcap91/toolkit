---
name: context-graphs-trillion-dollar-elephant
title: "Context Graphs: The Trillion Dollar Elephant"
url: "https://dadhichgaurav1.medium.com/context-graphs-the-trillion-dollar-elephant-7b78cd3fc96f"
category: reference
summary: "Practitioner analysis of context graphs for enterprise AI — identifies five human challenges (implicit decisions, trust, outcome attribution, forgetting, change continuums) and six technical challenges (trace extraction UX, canonicalization, temporal extraction, storage architecture, data security, graph structure) that must be solved before context graphs become operational"
tags: [context-graphs, enterprise-ai, knowledge-graphs, decision-traces, agent-memory]
reviewed: 2026-07-06
acquired: 2026-07-06
license: unlicensed
security_flags: []
overlaps: [graphrag-agent-memory-linkedin-series]
source: unknown
---

## What it says

Gaurav Dadhich's response to Foundation Capital's (Jaya Gupta / Ashu Garg) "trillion-dollar context graph" thesis. Agrees the opportunity is real — context graphs that trace enterprise decision-reasoning could power AI managers and "1-person unicorn" companies — but argues the path is harder than the hype suggests due to fundamental human and technical obstacles.

Foundation Capital's original thesis: the next trillion-dollar platforms will be systems of record for *decisions* (the "why"), not just data (the "what"). The $4.6T enterprises spend annually on salaries is mostly human judgment that has never been made operational.

## Key takeaways

**Human challenges:**
1. **Implicit decisions** — most decisions are never justified, explained, or elaborated; decision traces don't naturally exist
2. **Trust in traces** — humans justify decisions post-facto; real reasons (politics, quota pressure, personal relationships) rarely surface in formal records
3. **Outcome attribution** — even with accurate decision traces, establishing causation between decisions and outcomes is hard; humans struggle with this too
4. **Forgetting is a feature** — context graphs must know when things have changed; most change is continuous, not discrete, and seldom captured
5. **Temporal boundaries** — drawing the line between current and stale context has no clean solution

**Technical challenges:**
1. **Trace extraction UX** — past decisions yield timeline traces (steps taken) not decision-rationale; future decisions need low-friction documentation formats (webform, Slack post, email) without making people feel exposed
2. **Intra-org canonicalization** — same concept, different names across teams ("PR FAQ" vs "6-pager", "Account Executive" vs "Sales Rep")
3. **Temporal extraction** — detecting temporal signals in text is easy; marrying them to correct document creation time and handling implicit temporality is hard and expensive
4. **Storage architecture** — ephemeral vs long-term validity determination, trivial vs non-trivial — the same problems that created data warehouses and data lakes haven't gone away
5. **Data security** — fragmented data across systems is coincidental security; colocation into one logical system makes previously low-ROI attack methods high-ROI
6. **Graph structure** — open question whether to use graphs as data structures, databases, or representations; whether to store relationships, provenance, or both

**Counterpoint raised:** Recursive LMs and expanding context windows may allow agents to wander data warehouses/lakes and APIs (MCPs) directly, potentially bypassing the need for a separate graph layer.

## Mechanical details / What to adopt

This is an analysis piece, not a tool. The human-challenge taxonomy (implicit decisions, post-facto justification, forgetting-as-feature) is a useful checklist when evaluating any context graph or agent memory system's claims about capturing "organizational knowledge."

## Security

N/A — opinion article, no code or dependencies.