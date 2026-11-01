---
name: unslop-skills
title: Unslop Skills (UI / Text / Code)
url: "https://github.com/JCarterJohnson/vibecoded-design-tells"
category: skill
summary: "Three Claude skills that flag and remove AI 'tells' — unslop-ui (vibe-coded website patterns), unslop-text (AI prose cadences), unslop-code (AI code artifacts); backed by 3.2M-post Reddit analysis across 47 subreddits, with standalone CI-gating scanners; MIT"
tags: [design, writing, code-quality, ai-detection, skill, claude-code]
reviewed: 2026-06-22
acquired: 2026-06-22
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Three Claude skills, each built from a Reddit-mined study of what people identify as AI-generated "slop":

- **unslop-ui** — flags vibe-coded website patterns: shadcn/Tailwind defaults, AI-purple gradients, gradient hero text, emoji-as-icons, centered-hero-plus-three-cards layout, cream+serif+sage "tasteful default." Build mode establishes a design brief before generation; audit mode scans existing code with line-level findings and a "vibe score."
- **unslop-text** — flags AI prose tells: em dashes, "it's not just X, it's Y" cadence, sycophantic openers, delve/leverage diction, "in conclusion" wrap-ups, leftover assistant boilerplate.
- **unslop-code** — flags AI code tells: leftover chat artifacts, placeholder comments, emoji in code, swallowed errors, narrating comments, generic placeholder names, hallucinated APIs.

Each skill includes a standalone scanner script that greps a codebase, prints findings with file/line references, and gates CI on exit code. Lines marked `unslop-ignore` are skipped.

Data: 3,214,533 posts scanned across 47 subreddits (2020–2026), 46,971 on-topic, 3,033 comments from 125 canonical threads. Tells ranked by share of on-topic comments, adversarially verified (11/12 held).

## Assessment

Data-backed approach to a real problem — AI-generated outputs have recognizable tells that undermine credibility. The Reddit mining methodology (share-of-posts, not raw counts) and adversarial verification give the rankings more weight than opinion-based lists. The CI-gating scanner is a practical touch.

The build mode (establish brief → generate → scan) is the right workflow: it prevents the default-palette problem rather than just flagging it after the fact. Useful for any agent-generated UI, prose, or code that needs to look intentionally crafted.

## Mechanical details

- Install (Claude Code): `unzip skill/unslop-ui.skill -d ~/.claude/skills/` (or upload .skill ZIP to claude.ai)
- Scanner: `python skill/scripts/devibe_scan.py <path>` — prints findings, returns exit code for CI
- Reproduce data: `pip install -r requirements.txt && cd unslop-ai-ui && python3 collect.py && python3 harvest.py 3000 && python3 analyze.py`
- Raw data: `corpus.jsonl.gz` (46K posts), `comments.jsonl` (3K comments), `comment_tell_counts.csv`
- All three skills are independent — install whichever applies

## Security

- **License**: MIT (code); harvested text is public Reddit content via Arctic Shift
- **No API keys required**: data collection uses free Arctic Shift archive
- **Scanner**: pure grep/regex — no network calls, no LLM invocations
- **Data**: no usernames collected; posts identified by Reddit permalink only