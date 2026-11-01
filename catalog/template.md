# Catalog entry template

An agent can answer a later question about the thing from the entry alone, and the entry names exactly what to fetch at adoption.

## Frontmatter fields

- `name` — kebab-case slug; must match the entry's filename.
- `title` — display name.
- `url` — the subject itself: the repo, tool site, paper, or page this entry is about.
- `source_url` — the link the item came in on, when different from `url` (the reel, post, or thread that pointed here).
- `source` — what `source_url` derives to: `instagram`, `reddit`, `x`, `web`, `text`, or `unknown`.
- `category` — one of the catalog's fixed categories.
- `summary` — a factual one-line description.
- `tags` — free-text keywords for lexical search.
- `topics` — optional list of post-hoc topic labels; defaults to empty.
- `related` — optional list of related entry names (the machine-readable mirror of `## Related`); defaults to empty.
- `overlaps` — entries covering substantially the same ground.
- `acquired` — the date this entry was captured (`YYYY-MM-DD`).
- `reviewed` — the date this entry was last written or rewritten (`YYYY-MM-DD`).
- `license` — the subject's SPDX identifier, when it has one.
- `security_flags` — short flags for any security issues found; empty when clean.

## Body sections, in order

1. `## What it is` — 2-4 sentences on what the thing is.
2. `## How it works` — components and how they connect, the loop or algorithm step by step, key data structures, prompts, config, parameters, commands, and the design choices and reasons given.
3. `## How to use it` — install/run, requirements, integration points; omit for a pure idea with nothing to install.
4. `## Evaluation and limits` — how it is measured, claimed numbers (attributed), failure modes, known issues, community pushback.
5. `## Context from the source` — what the reel/post/carousel adds beyond the subject itself: the poster's use case and claims, top comments, attributed, with the source link.
6. `## Where to look next` — required when `url` is set; one line per target: `- <what you learn there> — <URL or repo path>`.
7. `## Related` — catalog entries found by search, one line each on how they relate.
8. `## Security` — license, dependency health, code quality signals, supply chain, dangerous patterns, maintenance, from observed evidence.

## Neutrality rule

Entries are factual. No verdicts, no adoption recommendations, no notes on whether the operator should use the thing — those decisions happen outside the entry.

## Provenance rule

`url` is the subject itself. `source_url` is the link the item came in on. `source` is what that link derives to.
