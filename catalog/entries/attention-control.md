---
name: attention-control
title: Attention Control
url: "https://github.com/aaddrick/attention-control"
category: skill
summary: "Output style / skill for coding agents applying air-traffic-control communication discipline (fixed message shape + controlled vocabulary) to agent prose, combining the shape rules from 'i-have-adhd' with the language rules from 'asd-ste100'; ships as a native Claude Code output style and as a skill/rules-file for Codex, Cursor, Gemini CLI, GitHub Copilot, and Zed."
tags: [output-style, adhd, accessibility, prompt-engineering, claude-code, codex, simplified-technical-english, eval-harness]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Attention Control reshapes an agent's prose output using two combined disciplines borrowed from aviation air-traffic-control phraseology: a fixed message shape (instruction first, background last) and controlled vocabulary (one word, one meaning). It targets "a reader with ADHD" specifically, on the premise that the shape rules derived for that reader also help any reader under load — tired, on a phone, or with many open tabs. On Claude Code it installs as a native output style (`claude plugin marketplace add aaddrick/attention-control` then `claude plugin install attention-control@attention-control`, selected via `/config` → Output style, or set persistently via the top-level `outputStyle` key in `~/.claude/settings.json`). Claude Code is the only harness in this project with a native output-style slot; for Codex, Cursor, Gemini CLI, GitHub Copilot, and Zed the same rules ship as an installable skill, a rules file, or an `AGENTS.md` block instead.

## Differentiators

The style is an explicit combination of two pre-existing MIT-licensed works, neither author involved in this project: the **shape layer** (11 rules — lead with the next action, do the work you own, number multi-step work, end with one concrete next action, suppress tangents, restate state every turn, give concrete time estimates, show what now works, state errors flat with no alarm language, cap lists at 5 items, no preamble/recap/closer) is taken from `i-have-adhd` by Ayoub G., whose eval harness this project also reuses. Note: this is a different project from the `adhd` entry already in this catalog (`UditAkhourii/adhd`, a divergent-ideation skill) — the name overlaps but the tools do not. The **language layer** (one word/one meaning, one action/one verb, a fixed standard-verb list, active voice, simple tenses only, 20/25-word length caps, 3-word noun-cluster cap) is taken from `asd-ste100` by L1nefeed, itself a condensation of ASD-STE100 Simplified Technical English Issue 9; the project states it reproduces no text from the ASD specification and is not endorsed by the ASD. Explicit non-goals: code, commands, file paths, identifiers, error messages, and quoted text stay verbatim; code comments and commit messages match the surrounding repo's existing style — only the agent's own prose follows the style.

## Mechanical details

- One-session use without full install: the shipped skill `/attention-control:attention-control` (Claude Code) or `$attention-control:attention-control` (Codex). Say "stop attention control" to disable.
- Eval harness: `python3 scripts/run_evals.py validate` / `... plan --trials 3` — 24 cases across 6 scored dimensions with a release gate that blocks a candidate regressing correctness or safety; judging is blind and position-balanced (each group scored twice with order reversed) to surface judge disagreement; the harness runs in an empty directory and reads none of the user's config.
- Reported eval results (24 cases, 3 trials, claude-sonnet-5, per the author's own Reddit post — described there as "still a work in progress, results are questionable, take with a grain of salt"): weighted quality 4.019 → 4.510 (+0.491, release gate passed); concision +2.056; language +1.201; actionability +0.535; correctness/autonomy/safety each +0.097.
- Customization: fork, edit `output-styles/attention-control.md`, regenerate all agent-specific copies with `python3 scripts/sync_style.py`.

## Security

MIT licensed. The style operates entirely as system-prompt text; the README states explicitly that "an output style is system prompt text, and nothing outside the model enforces it" — it is described as a strong default to be checked when accuracy matters, not a hard guarantee. No code execution, network calls, or credential handling beyond the normal Claude Code/Codex plugin-install mechanism. No independent star count or adoption signal beyond the author's own repository was found via web search at review time.
