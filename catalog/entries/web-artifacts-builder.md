---
name: web-artifacts-builder
title: Web Artifacts Builder
url: "https://github.com/anthropics/skills/blob/main/skills/web-artifacts-builder/SKILL.md"
category: skill
summary: "use when markdown isn't enough for interactive reports/dashboards"
tags: [html, reports, dashboards, visualization]
overlaps: []
security_flags: []
license: Apache-2.0
reviewed: 2026-05-25
acquired: 2026-05-25
source: unknown
---

## What it does

Generates self-contained HTML reports and interactive dashboards as skill output. Fills the gap between static markdown output (which lacks interactivity) and full application development (which is overkill for analysis reports). Suitable for QC summaries, pipeline result dashboards, and comparative analyses where users need to explore data rather than just read it. Source is the official Anthropic skills repository.

## Assessment

Markdown is sufficient for most workflow documentation, but interactive outputs are needed for analysis results that users need to explore — differential expression tables, QC metric comparisons, spatial transcriptomics overlays. This skill is already in the Anthropic skills repo and is ready to adopt as a named output format option.

## Mechanical details

Install from `https://github.com/anthropics/skills/blob/main/skills/web-artifacts-builder/SKILL.md`. Use when a workflow produces results that benefit from interactivity: sortable tables, filterable lists, toggle views. Default to markdown; escalate to this skill when markdown is insufficient.

## Security

This skill is published by Anthropic in their official skills repository under the Apache 2.0 license, which provides a known, auditable provenance. It executes entirely client-side: the bundling pipeline (React + Vite + Parcel) runs locally and produces a single self-contained HTML file — no outbound network calls are made at runtime. The generated bundle inlines all JavaScript and CSS, so the security boundary is the same as for any static HTML file viewed in a browser. No credentials, API keys, or server-side components are involved. The main operational consideration is that bundled artifacts may include user-supplied data rendered as HTML; agents should sanitize untrusted input before passing it into templates to prevent XSS in the output artifact.
