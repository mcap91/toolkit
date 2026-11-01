---
name: simon-says-mother-goose
title: Simon Says / Mother Goose (Agent Skills collections)
url: "https://github.com/jawsublime-byte/simon-says"
category: skill
summary: "Two companion MIT-licensed, explicit-invocation Agent Skills collections (SKILL.md-compatible) by a solo hobbyist author, targeting recurring AI-coding-agent failure modes — Simon Says covers scope/execution/investigation/testing/alignment drift (e.g. Patty Cake: diffs instructions vs plan vs completed work and stops on material drift); Mother Goose covers repair loops, verification, evidence, automation scope, and provenance (e.g. Pinocchio: requires evidence for completion claims; The Emperor's New Clothes: protected dissent against groupthink)"
tags: [agent-skills, skill-collection, guardrails, verification, alignment, claude-code, codex]
reviewed: 2026-08-25
acquired: 2026-08-25
license: MIT
security_flags: [single-maintainer, no-external-adoption-signal, unverified-by-web-search]
overlaps: []
source: unknown
---

## What it does / What it says

Simon Says and Mother Goose are two companion collections of Agent Skills (installable into Claude Code, Codex, ChatGPT, and other Agent-Skills-compatible hosts) written by a solo author ("Joe," a self-described online English teacher and hobbyist builder, not a company). Each skill maps a mnemonic (a childhood game or story) to one recurring failure pattern observed in AI-assisted coding, with a defined, testable procedure rather than a vague instruction like "be careful."

- **Simon Says** (https://github.com/jawsublime-byte/simon-says): playground-game-themed skills for scope control, execution fidelity, investigation, testing, and user-agent alignment. Named skills include Simon Says (router: execute a supplied build order exactly, or route to another skill), K.I.S.S. (minimum sufficient code), M.I.S.S. (deep investigation without scope expansion), Hide and Seek (search beyond the first visible failure), Battleship (black-box test before inspecting implementation), Patty Cake (compares the latest directive, active plan, and actual work; classifies each requirement as matched/drifted/missing/blocked/unknown; stops on material drift instead of self-resolving), Perfection (locates a required missing piece without inventing extra scope), Referee (tracks repeated builder drift via evidenced yellow/red cards; can bench or expel a repeat offender), and Life (simulates long-term usage to surface storage growth, stale state, latency creep, log/cache bloat), among others (Red Rover, Chutes and Ladders, Recess, Dodgeball, Sand Castles, Double Dutch, Etch A Sketch, Go Fish, Heads Up Seven Up, Hungry Hippos, Teacher's Pet, Rock 'Em Sock 'Em).
- **Mother Goose** (https://github.com/jawsublime-byte/mother-goose): nursery-rhyme/fairy-tale-themed skills for repair loops, resilience, evidence, automation scope, and provenance. Named skills include Mother Goose (router), Humpty Dumpty (stop repeating a failed repair strategy; preserve requirements, replace the strategy), Three Little Pigs (escalating resilience tests), Goldilocks (justifies a bounded-middle configuration choice over an extreme), The Emperor's New Clothes (creates a protected dissenting review to counter groupthink/yes-man consensus), The Sorcerer's Apprentice (requires scope/budget/stop-conditions/override/cleanup before unbounded automation), Pinocchio (attaches an evidence class to every material completion claim), and Hear No Evil Speak No Evil See No Evil (independent verifier role that may investigate/reproduce/diagnose but cannot self-repair the candidate or bypass the architect), among others (Ring Around the Rosie, Hickory Dickory Dock, Old Lady Who Swallowed a Fly, Boy Who Cried Wolf, Goose That Laid the Golden Eggs, Five Little Monkeys, Hansel and Gretel, Tortoise and the Hare, Little Red Hen).

Stated philosophy (both READMEs): "AI can investigate, propose, test, build — but should not quietly decide what the project was supposed to become."

## Differentiators / Key takeaways

- Both collections are explicit-invocation only (`$skill-name` in Codex, `@skill-name` in ChatGPT) — skills do not silently alter ordinary task behavior.
- Zero-dependency Python installer (`scripts/install.py`, standard library only) supports `--host codex|claude-code|custom`, `--scope user|project`, per-skill selective install, `--dry-run`, and won't overwrite existing skill folders without `--force`. A separate `update_skills.py` can pull newly added skills from the public repo without reinstalling the whole collection.
- Both repos include a `validate_repo.py` script that checks each skill's name, frontmatter, UI metadata, evaluation coverage, plugin manifest, and unresolved placeholders; both ship a `.codex-plugin/plugin.json` for ChatGPT/Codex plugin distribution.
- No premium/paid tier for either collection.

## Mechanical details / What to adopt

Install full collection: `python scripts/install.py --host claude-code --scope user` (or `--host codex`, `--scope project --project PATH`). Install a single skill: `--skill <name>`. `--host custom --destination PATH` targets any other Agent-Skills-compatible host.

## Security

MIT license (both repos; see NOTICE.md in each for an independent-project/third-party-mark notice). Both READMEs state an explicit safety boundary: "Adversarial skills are for defensive testing of systems the user owns or is authorized to assess. They do not authorize destructive payloads, credential theft, persistence, evasion, or attacks against third parties," and that all skills "yield to higher-level safety rules, repository policy, permission limits, and explicit approval gates." No external adoption, star-count, or third-party review signal was found (targeted web search for the author/repos returned no matches); this is a single-maintainer hobby project and the skills' effectiveness/adherence claims are unverified beyond the repos' own text.
