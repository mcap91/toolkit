# ntfy-bridge test fixtures

Captured 2026-11-02 from `https://ntfy.sh` with `curl -s -m 10`, unedited (WK-0108 Capture section,
overseer ruling 2026-11-02 20:39).

The topic in every line below (`capture-1e21cce7798001e6`) is a burned capture topic: never registered
in any channel registry, never subscribed to on a phone, never reused for a live channel. The
topic-secrecy rule (random topics, never committed, never screenshotted) covers live channel topics
only — this topic was generated for this capture session and discarded, so publishing it here carries
no exposure.

Message bodies are test text only: `capture one`, `STOP`, `finish   up.`, `STOP please`,
`approve 3f9a`, `free text reply`, and title `capture title`. Nothing from any repo, record, or live
channel.

These fixtures are never edited, reformatted, or regenerated. A format question gets a fresh capture,
not a hand patch.

## What each file shows

- `poll-zero.jsonl` / `.headers.txt` — an empty poll: HTTP 200, `content-length: 0`, empty NDJSON body.
- `poll-one.jsonl` / `.headers.txt` — a poll with exactly one cached message (`capture one`).
- `poll-several.jsonl` / `.headers.txt` — a poll with six cached messages, including the same-second
  reorder (`STOP` sent before `finish up.`, polled after) and the vocabulary near-misses
  (`STOP please`, `approve 3f9a`, `free text reply`).
- `poll-since-ts.jsonl` / `.headers.txt` — `since=<since-ts.txt>` (a timestamp between the first and
  second message): returns the 5 messages at or after that second, dropping the first.
- `poll-since-ts-last.jsonl` / `.headers.txt` — `since=<the last message's own timestamp>`: returns
  both messages at that second (inclusive at one-second resolution), used to prove a cursor that has
  already seen both yields nothing on replay.
- `poll-since-ts-after.jsonl` / `.headers.txt` — `since=<last timestamp + 1>`: returns nothing, the
  other edge of the one-second-resolution inclusive boundary.
- `poll-since-all.jsonl` / `.headers.txt` — `since=all`: returns the whole cache, same shape as an
  unknown/expired id (kept only because the script never sends `since=all` or `since=<id>`; it proves
  why the cursor must not use those forms).
- `poll-since-id.jsonl` / `.headers.txt` through `poll-since-id5.jsonl` / `.headers.txt` — `since=<id>`
  for each of the six message ids in turn: each returns every message with `time >=` that message's
  time, minus the id itself, not "strictly after this id" — the behavior Decision 7's cursor
  requirement (timestamp cursor, never an id cursor) exists to avoid.
- `poll-since-last-id.jsonl` / `.headers.txt` and `poll-since-last-id-repeat.jsonl` / `.headers.txt` —
  `since=<last id>` polled twice: both calls re-return the same same-second message, showing an id
  cursor is not idempotent across repeats.
- `poll-since-latest.jsonl` / `.headers.txt` — `since=latest`: returns only the single newest message.
- `poll-since-unknown-id.jsonl` / `.headers.txt` — `since=<an id not in the cache>`: returns the whole
  cache, identical to `since=all` — the capture behind the "never `since=<id>`" rule.
- `publish-1.json` through `publish-6.json` — the publish response for each of the six messages sent
  during this capture, in send order (ids match the poll fixtures above).
- `since-ts.txt` — the timestamp used as `since=` for `poll-since-ts.jsonl`.
- `since-id.txt` — the id used as `since=` for `poll-since-id.jsonl`.
