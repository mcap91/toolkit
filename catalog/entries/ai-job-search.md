---
name: ai-job-search
title: AI Job Search
url: "https://github.com/MadsLorentzen/ai-job-search"
category: framework
summary: "AI-powered job application framework built on Claude Code. Fork-and-own workflow: /setup (self-profiling from documents or interview), /scrape (multi-portal search with fit scoring), /apply (drafter-reviewer pipeline producing tailored LaTeX CV + cover letter with PDF verification loop and ATS text-layer check). Also ships /interview prep, /rank batch scoring, /outcome tracking, /gmail-sync, /notion-sync, /html-report dashboard, /upskill gap analysis, /expand competency enrichment, /add-portal and /add-template generators. Danish job portals built-in; LinkedIn and freehire.me for other markets; /add-portal scaffolds new portals. MIT."
license: MIT
tags: [claude-code, job-search, cv, cover-letter, latex, skills, workflow, career, automation, drafter-reviewer]
reviewed: 2026-07-28
acquired: 2026-07-28
overlaps: []
security_flags: []
source: unknown
---

## What it is

AI Job Search is a structured Claude Code workflow that turns the agent into a full-stack job application assistant. Created by Mads Lorentzen, a geophysicist who used it to land an AI engineering role (69 tailored applications, 20 first interviews, 1 signed contract). The user forks the repo, fills in their profile, and runs slash commands for each stage of the job search.

Core workflow:
- **/setup** — self-profiling from a documents folder (CV PDF, LinkedIn export, diplomas, references), single CV paste, or guided interview. Idempotent and safe to re-run.
- **/scrape** — searches multiple job portals, deduplicates, presents matches sorted by fit rating
- **/apply `<url>`** — full drafter-reviewer pipeline: evaluate fit (5 dimensions), draft tailored LaTeX CV + cover letter, spawn a reviewer agent (fresh context) to critique, revise, compile PDFs (lualatex/xelatex), visually inspect and iterate until layout is clean, ATS-check the text layer, present with verification checklist
- **/interview** — stage-specific prep pack from application archive, company research, STAR mapping, mock interview
- **/rank** — batch-score scraped postings against fit framework via parallel agents
- **/outcome** — record results, archive materials, follow-up drafting for stale applications
- **/gmail-sync** — auto-detect application status signals from Gmail
- **/notion-sync** — one-way read-only pipeline view in Notion
- **/html-report** — self-contained offline HTML dashboard with charts
- **/upskill** — skill gap analysis with learning plan and web-searched resources
- **/expand** — enrich profile from linked public sources (GitHub, portfolio, Kaggle, Google Scholar)
- **/add-portal** — generate a job-portal search skill for any market
- **/add-template** — register custom CV/cover letter templates (LaTeX, Typst, etc.)

## Mechanical details

- **Install:** Fork and clone, then `bun install` in each portal CLI tool directory
- **Requirements:** Claude Code CLI, Python 3.10+, Bun, LaTeX (lualatex + xelatex), optionally pdftotext (poppler)
- **Market:** Danish portals built-in (Jobindex, Jobnet, Jobbank, Jobdanmark); LinkedIn and freehire.me are country-agnostic; /add-portal generates new ones
- **Architecture:** CLAUDE.md holds the candidate profile; `.claude/commands/` holds slash commands; `.claude/skills/` and `.agents/skills/` hold skills and portal CLI tools
- **Cross-agent:** Portal search skills work on Codex, Antigravity, Gemini CLI via AGENTS.md; full workflow is Claude Code-native
- **Integrity:** All CV/cover letter claims verified against actual profile — never fabricates skills or experience. Job postings treated as untrusted input (no instructions followed, no links fetched from body).

## Security

MIT licensed. Job postings are treated as untrusted input — the workflow follows no instructions embedded in them and fetches no links from their body. SECURITY.md documents the threat model. CI runs LaTeX smoke compiles, skill lint, CLI typechecks, and security guards (permission allowlist, gitignore rules). LinkedIn scraping is against LinkedIn's ToS — personal-use-only warning included. No security flags observed beyond the standard caveat that agentic defenses are instruction-level, not sandboxed.

## Usage notes

- ATS parsing (r/jobsearchhacks thread, Oct 2026): parsers commonly scramble multi-column layouts, text boxes, icons, and unusual fonts, so a single-column, one-font (11–12pt), plain-bullet PDF/DOCX survives better; check by pasting the PDF's text into a plain-text file and confirming reading order. Complements this framework's ATS text-layer check on generated LaTeX CVs.

## How to use it

gh repo fork MadsLorentzen/ai-job-search --clone
