---
name: book-to-skill
title: Book to Skill
category: skill
summary: directly useful for computational biology methods PDFs
tags: [pdf, knowledge, querying]
reviewed: 2026-05-25
acquired: 2026-05-25
license: unknown
security_flags: []
overlaps: []
source: unknown
---

## What it does

Turns a technical PDF into a queryable skill with chapter summaries, a glossary, and on-demand section loading. Rather than dumping a full document into context, it builds a structured index that Claude can query selectively. Directly applicable to computational biology methods texts — algorithm descriptions, protocol PDFs, and reference manuals that are too large for inline inclusion.

## Assessment

Bioinformatics work regularly involves large reference PDFs (tool manuals, method papers, protocol guides) that are impractical to keep in context. A queryable skill wrapping these documents enables precise retrieval without context bloat. Low-risk pilot: one computational biology methods book.

## Mechanical details

Source is a Reddit r/claudeskills post. No public repo URL confirmed at review time. Pilot by applying to one comp bio reference text (e.g., a STAR aligner manual or Seurat vignette compilation) and evaluating retrieval accuracy before broader use.

- **Update (2026-07-22):** Canonical repository confirmed at https://github.com/virgiliojr94/book-to-skill (MIT license) — resolving the "no repo confirmed / license unknown" gap noted above. Distributed as an Agent Skill on the open SKILL.md standard for Claude Code, GitHub Copilot CLI, and Amp; install via `git clone https://github.com/virgiliojr94/book-to-skill.git ~/.claude/skills/book-to-skill`, then run `/book-to-skill <path|folder|glob>`.
- Supported inputs: PDF, EPUB, DOCX, TXT, Markdown, reStructuredText, AsciiDoc, HTML, RTF, MOBI/AZW. Extractors tried in order per format (PDF → pdftotext/pypdf/pdfminer or Docling for technical books with tables/code; EPUB → ebooklib → stdlib zipfile). `python3 scripts/extract.py --check` reports which extractors are installed.
- Generates a skill folder: `SKILL.md` core (~4K tokens) + one file per chapter (loaded on demand, ~1K each) + `glossary.md`, `patterns.md`, `cheatsheet.md`. Chapter auto-segmentation needs explicit "Chapter N" headings.
- A separate, optional standalone extractor exists via `pip install book-to-skill`; it installs only the text-extraction engine (CLI), **not** the agent skill.
- README reports 24×–51× fewer tokens than context-dumping a book to answer one question, measured via `tools/discovery_tax.py` on three real books. Processing is local; the tool ships no book content.

- **Update (2026-08-09):** Author's 3-months-later Reddit follow-up reports the project reached #1 on Trendshift for Python, #3 on GitHub Trending, and 15,000+ GitHub stars, and expanded from PDF-only to EPUB/folders/multi-source/non-technical-book support directly in response to r/claudeskills community feedback. Independent web search corroborates strong popularity (third-party write-ups citing 12,000+ stars at an earlier snapshot) but did not independently re-verify the author's 15,000+ figure.

## Security

License is unknown — the skill originates from a Reddit community post with no associated repository or explicit license grant. Treat it as use-at-will with no redistribution guarantees; re-verify if a canonical repo surfaces. No `security_flags` apply: this skill is pure prompt text with no code execution, no external network calls, no file-system writes, and no dependency installation. The only data-handling consideration is that the source PDF is read into Claude's context window — ensure PDFs containing sensitive or proprietary content are not processed through shared or logged endpoints.
