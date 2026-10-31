---
name: catalog-intake
description: Full catalog pipeline — Gmail pull, inbox curation, drain, and headless processing. Use when adding tools to the catalog or processing saved links.
---

# Catalog intake + processing

## Stage 1 — Intake (interactive)

1. **Read cursor:** call `config { action: "get-state" }` to read `gmail_last_pull_iso`. This is the
   timestamp of the last successful Gmail pull. Use it to scope the search (step 2).
2. **Gather:**
   - Gmail: search `from:me subject:catalog after:{date from cursor, YYYY/MM/DD}`.
   - **Filter duplicates:** Gmail `after:` has only day-level granularity, so the search will
     return messages from earlier in the cursor day that were already processed. Compare each
     message's `date` against the cursor timestamp and discard any message dated at or before it.
   - Extract URLs from the remaining message bodies; capture prose bodies as fenced ```text
     blocks with a `source:` line. Append all to `catalog/inbox.md`.
3. **Update cursor:** call `config { action: "set-state", key: "gmail_last_pull_iso", value: "<newest ISO>" }`
   with the `date` of the newest message you appended, not the current time: a message sent
   between the search and this call would otherwise be skipped. If no message was new, leave the
   cursor unchanged. Do this **after** successfully appending to inbox, not before.
4. **Curate** `catalog/inbox.md` with the user: delete junk; for any `⚠ needs-link` item
   (LinkedIn posts, X, paywalled), replace with the real fetchable URL or paste the relevant prose
   as a ```text block. Reddit post/share links, Instagram reel links, and Instagram `/p/` posts
   (single images and image carousels) need no manual link — the capture step (step 6) resolves
   them.
5. **Drain:** call the `drain {}` MCP tool. It ingests ready items into the queue and marks
   unfetchable items `⚠ needs-link` (blocked domains, Reddit post/share links). Those stay in
   inbox until the user resolves them or the capture step (step 6) does.
6. **Capture Reddit, Instagram reels, and Instagram posts:** one-time setup if Chromium isn't
   already available to Playwright: `uv run --project packages/catalog-capture playwright install
   chromium`. Then, from the repo root, with nothing else writing the inbox concurrently, run the
   one `needs-link` command:
   ```
   uv run --project packages/catalog-capture python -m catalog_capture needs-link --inbox catalog/inbox.md --sources catalog/sources
   ```
   Each `⚠ needs-link` Reddit line becomes a captured ```text block, `⚠ capture-failed <url> — <reason>`,
   or `⚠ pdf <url>`. Each `⚠ needs-link` Instagram reel line becomes one captured ```text block per
   reel (caption, transcript, on-screen text, and unverified tool/URL hints) or `⚠ capture-failed
   <url> — <reason>`. Each `⚠ needs-link` Instagram `/p/` line (a single image or an image
   carousel) becomes one captured ```text block per post (caption, each slide's text under its
   slide number, and unverified tool/URL hints) or `⚠ capture-failed <url> — <reason>`; a video
   `/p/` post, or a carousel with a video slide, has no capture yet and becomes `⚠ capture-failed
   <url> — unsupported media_type <n>`. Pass `--only reddit`, `--only instagram_reel`, or
   `--only instagram_post` to run just one source type.
   A `capture-failed`/`pdf` line needs a manual reset (edit it back to `⚠ needs-link <url>`)
   before it will retry; same for a Reddit item returned from processing as
   `⚠ empty-fetch`/`⚠ fetch-error` — reset it to `⚠ needs-link <url>` to have this step recapture
   it. The processing agent decides what each captured block becomes — one entry, several, or
   annotations.
7. **Drain again:** call `drain {}` once more — the only items still ready are the fenced blocks
   the capture step just wrote.
8. Report what was ingested, blocked, captured, and skipped.

## Stage 2 — Processing (headless)

Run the headless pipeline to assess every queued item and write catalog entries:

```
npm run -w @catalog/mcp catalog:process
```

Run this in the background. Code reads `catalog/queue.json` and runs one fresh `claude --print`
session per item, started in stored queue order — never one session over the
whole queue, which gets expensive per item and drifts off the recipe's steps after a handful of
items. Each session's prompt is `catalog/recipe.md` plus that one item (key, url, content); the
session never sees the rest of the queue. Each session is locked to `--model sonnet`,
`--strict-mcp-config` with only the catalog MCP server attached, and `--allowedTools` scoped to
`WebSearch`, `WebFetch`, `Read`, and the catalog MCP tools the recipe calls — no `Edit`, `Write`,
`Bash`, or project MCP servers reach the session. Pass `--limit N` for a test run of just the
first N queued items. Pass `--concurrency N` to run N item sessions at once (default 1); the queue, inbox,
and entry writes are guarded by cross-process lock files. After a parallel run, check for duplicate entries:
two items about the same tool can both miss in `search`. Add `--group` with `--concurrency` to keep items that
hint the same tool in one session slot, run one after another. To stop gracefully, run `touch catalog/.stop-processing`:
in-flight items finish and no new ones start. To resume, run the same command again.

**What it does per item:** fetch URL (if the item has no content already) → search for a
duplicate → build research prompt → assess the tool → validate → write entry to
`catalog/entries/` or annotate an existing one → remove from queue. An item it can't fetch or
can't catalog is returned to `catalog/inbox.md` marked `⚠ <reason>`.

**After each item's session**, code re-reads the queue: if the item is gone, it's done; if it's
still queued (including a session that ran past the 15-minute per-item timeout and was killed),
code logs a failure in `catalog/process-log.jsonl` and leaves it queued for the next run — the
loop always continues. One JSON line per item in `catalog/process-log.jsonl` tracks status, wall
time, model, cost, turns, token usage, and tool-call counts. The full session transcript is copied
to `catalog/runs/<session_id>/`. Both are gitignored: run logs stay local, because this repo is public.

**After the whole loop finishes**, code calls the index generator directly once — no LLM step.

**After it finishes:**
- Check `catalog/queue.json` — any item still present failed its session and needs another run
  or manual attention.
- Check `catalog/process-log.jsonl` for per-item cost and failure detail.
- New entries are in `catalog/entries/`. `catalog/index.md` is regenerated automatically.
- Commit the new entries and updated index. Do not commit the run logs (gitignored).
