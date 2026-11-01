---
name: tracer-bullets-vertical-slices
title: Tracer Bullets / Vertical Slices for Agent Plans
url: "https://thedailyai.news/"
category: agent-pattern
summary: "Matt Pocock's argument (via thedailyai.news clip) that AI coding agents fail on horizontal layer-by-layer plans (database → API → frontend) for lack of an integrated feedback loop; the fix is the Pragmatic Programmer 'tracer bullet' idea — thin vertical tasks that cross database, service, and frontend to prove the whole flow, reframing work from 'complete phase 1' to 'ship one visible, testable slice'"
tags: [planning, vertical-slices, tracer-bullets, agent-workflow, task-decomposition, feedback-loops, kanban, matt-pocock]
reviewed: 2026-09-10
acquired: 2026-09-10
license: LicenseRef-news-content
security_flags: []
overlaps: []
source: unknown
---

## What it says

A thedailyai.news clip summary of Matt Pocock's point about why AI coding agents fail: usually not because the task is "too hard," but because they are handed **horizontal plans** — database first, API next, frontend last — and code layer by layer with no integrated feedback loop until the end.

The fix is an old idea from *The Pragmatic Programmer*: **tracer bullets**, i.e. vertical slices. Instead of asking the agent to build one layer at a time, create thin tasks that cross the database, service/API, and frontend just enough to prove the whole flow works end to end.

## Key takeaways

- Reframes the unit of agent work from "complete phase 1" to "ship one visible, testable slice."
- Earlier feedback for the agent (integration errors surface on slice 1, not at phase 3), and earlier review material for humans (something real runs sooner).
- Vertical slices also make a Kanban backlog more agent-friendly: independent thin tasks that agents can grab without cross-phase dependencies.

## What to adopt

- When writing plans for agents, decompose by end-to-end flow, not by architectural layer.
- Gate each slice on a runnable, observable behavior rather than on layer completion.

## Security

- Editorial/news content summarizing a public talk clip; no code or tooling involved.