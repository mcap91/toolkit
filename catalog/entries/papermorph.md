---
name: papermorph
title: Papermorph
url: https://github.com/DozenTwelve/Papermorph
category: skill
summary: Agent skill (Claude Code / OpenCode, invoked as /papermorph) that turns a textbook PDF or a story into a self-hosted static web book — narrated step-by-step lessons with graded quizzes, paper-puppet picture-book films, or documentaries/shorts/explorable pages; plans chapters, writes narration, animates visuals to per-word TTS timing, and self-reviews output before publishing; exports to MP4+SRT or SCORM; MIT license (bundled MathJax Apache-2.0, media assets keep own licenses); ~1,000 GitHub stars
tags:
  - agent-skill
  - claude-code
  - opencode
  - pdf-to-web
  - text-to-speech
  - interactive-learning
  - static-site
  - education
  - video-generation
  - mit-license
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
source: instagram
source_url: https://www.instagram.com/reel/DeGtjz6kV5N/
---

## What it does

Papermorph is an agent skill (`npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code` or `--agent opencode`, then `/papermorph`) that turns a PDF textbook, a story, or a book idea into a self-hosted, static interactive web experience. From math/science textbooks it builds narrated, step-by-step lessons with graded quizzes; from stories, paper-puppet picture-book films with voices, subtitles, sound effects, and music; from books or ideas, documentaries, vertical shorts, or explorable "play" pages (an interactive essay, a historical map walked year by year). Output is a self-contained static site — no server, database, or account — that is just a folder you can host anywhere.

## Pipeline

1. Plan — splits the source into chapters or scenes.
2. Script — writes narration text per chapter/scene.
3. Storyboard — generates a frame-by-frame visual plan in code; lesson content needs no image model, picture books/documentaries can optionally use one for painted sets.
4. Narration — text-to-speech via Edge TTS (free, online) or Kokoro (free, local); every word gets a timestamp.
5. Animation — visuals (diagrams, scenes, draggable 3D objects) are coded to match the narration's per-word timing.
6. Self-review — checks its own output via contact sheets, overlap/blank-frame checks, end-to-end tests, and a director's-review pass against approved books, then fixes what it finds; large chapters are split across a team of subagents, each step on a model chosen in `core/team.md`.

## Differentiators

- Fully static output (a book is a folder) — no server/DB/account, hosts anywhere.
- One pipeline, three output shapes: graded interactive lessons, paper-puppet picture-book films, and documentaries/shorts/explorable pages.
- Narration-driven timing: animation syncs to per-word TTS timestamps rather than hand-keyed cues.
- Self-correcting render loop (contact sheets, overlap/blank-frame checks, end-to-end tests, director's review) before publishing.
- Model-agnostic: published examples used Opus 5.5, GPT-6.1-Sol, and Sonnet 5.5 per-step via `core/team.md` — the source reel's "Opus 5.5 only, no image models" framing describes the lesson examples shown, not a hard limit; picture books/documentaries do optionally call image models (OpenRouter/OpenAI) for painted sets.
- Exports to 1080p MP4+SRT (`scripts/export.py`) or SCORM packages for an LMS (`scripts/scorm.py`).
- Player UI in English/Russian/Chinese/Japanese, with pause/step/speed, keyboard shortcuts, and per-book saved progress; each book bundles its own copy of the player (`engine/`) so site-wide updates don't break already-published books.

## Mechanical details

- Requires `uv`, `ffmpeg`, and Playwright browsers (`uv run --with playwright playwright install chromium firefox`).
- Narration is free (Edge TTS online or Kokoro local); optional paid steps need API keys — painted sets for picture books via OpenRouter or OpenAI, and ElevenLabs narration/clips for documentaries via OpenRouter.
- Maintainers estimate an illustrated physics chapter costs about $10–18 of model usage.
- Published "bookshelf" examples: Elementary Algebra (68 chapters), Linear Algebra (40 chapters, draggable 3D planes), Elementary Mathematics (23), Elementary Physics (9), a Joke Collection (7 episodes), Little Red Riding Hood, the documentary Madness and Civilization (10 min + 4 shorts), The Pandemic (7 min, 6 shorts, a scroll story), Shooting an Elephant (interactive Orwell essay), and Time of the Magicians (walkable map).
- Per-book style choices persist to a `style.json` so later chapters match the established look.
- Repo reports ~1,000 GitHub stars as of this capture (Oct 2026).

## Security

- MIT license covers the Skill/player code; bundled MathJax (`engine/vendor/mathjax`) is Apache-2.0; media under `site/` (images, recordings, data) keeps its own per-asset license noted beside it (e.g., `site/pandemic/img/SOURCES.md`) — some toned CC BY-SA images stay CC BY-SA. Mixed licensing across code vs. bundled media; check per-asset terms before reuse.
- Runs local code generation plus Playwright headless-browser automation and ffmpeg rendering — standard for a codegen skill, not sandboxed beyond the host agent/OS.
- Optional paid steps send content to third-party APIs (OpenRouter, OpenAI, ElevenLabs) using a user-supplied API key.
- No eval()/injection patterns observed in the fetched README; full source not reviewed line-by-line.
- Maintainers ask contributors not to submit copyrighted book PDFs or lessons derived from them, and note that using someone else's textbook as a private input is fine, but publishing a book derived from it is the user's call to clear for copyright.
