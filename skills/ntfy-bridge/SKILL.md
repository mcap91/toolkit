---
name: ntfy-bridge
description: Set up a phone notification bridge over ntfy.sh for a pipeline or an unattended agent session. Use when the user says "set up an ntfy connection for X", "notify my phone", "reply from my phone", or wants a long-running job or unattended session to reach them on their phone.
---

# ntfy-bridge

A phone bridge over the public `https://ntfy.sh` relay. Two modes: a one-way notifier wired straight
into a pipeline's existing logging, and a two-way channel an agent polls for operator replies. The
skill text below owns judgment (mode choice, naming, wiring, what each control word means); the script
owns everything deterministic (topic generation, the channel registry, send, poll, vocabulary
parsing). Invoke the script by its path inside this skill directory, e.g.:

```
python3 <path-to-this-skill>/ntfy_bridge.py list
python3 <path-to-this-skill>/ntfy_bridge.py create --name NAME --mode one-way --purpose "..." --repo "..."
```

## Mode choice

Pipeline, job, or run means one-way. Unattended session, or "I want to reply", means two-way. Unclear
means ask the operator.

## Bare invocation

If the operator gives no purpose, run `list` first and show them the existing channels. Then ask one
question: is this for a pipeline, or for an unattended session? The answer sets the purpose and the
mode. Once both are set, run the setup flow below.

## Setup flow

"Set up an ntfy connection for X" runs this flow from any repo:

1. Run `list`. Reuse a registry entry if one already fits the purpose, or propose a new channel
   name: short enough to type on a phone, 12 characters at most — the script enforces the limit.
2. Pick the mode from the rule above, or ask the operator if it's unclear.
3. Run `create` with the chosen name, mode, purpose, and repo.
4. Tell the operator to subscribe on their phone: install the ntfy app, keep the default server
   `ntfy.sh`, and add the printed topic (and the reply topic too, if two-way). The app can show a
   display name for each subscription, so a short topic is no harder to tell apart on the phone.
   Subscription is manual — the script cannot do it for them.
5. Send the test message with the script's `send` command.
6. Wait for the operator to confirm receipt at the terminal before leaving the session unattended. Do
   not proceed to unattended operation on silence here — this confirmation is not a veto window.

## One-way wiring

One-way pipelines do not call the script. Setup wires an env var holding the topic plus an inline
`curl -s -m 10` into the pipeline's existing logging, so cluster jobs never depend on the skill being
installed:

```
curl -s -m 10 -H "Title: <title>" -H "Priority: <priority>" -d "<body>" "https://ntfy.sh/${NTFY_TOPIC}"
```

Use default priority for routine milestones (start, in-progress milestones); use `Priority: high` for
failure and done — it buzzes through phone defaults. A failed notification is logged and does not stop
the pipeline.

Setup prints the `export NTFY_TOPIC=...` line and stops there. The operator sets it themselves, in
their own shell profile or the job scheduler's environment. The agent never writes a topic into any
file inside a repo — not a script, not `.env`, not a config file, not a doc.

## Two-way loop

The poll loop is code, not the agent's judgment. Run:

```
python3 <path-to-this-skill>/ntfy_bridge.py wait --name NAME [--interval MINUTES]
```

as a Claude Code background command (`run_in_background`) so the harness wakes the agent when it exits.
`wait` polls immediately, then every interval, until a vocabulary word arrives; it prints the same JSON
object `poll` prints (`matched`, `acted_on`, `superseded`, `unrecognized`, `unrecognized_total`) and
exits 0. Act on `acted_on`, report any `superseded` words to the operator, then re-arm `wait` again.
Never schedule polls yourself — no sleeping, no manual timers.

When the session ends on its own — the task is done, not cut short by `STOP` or `FINISH UP` — a `wait`
armed earlier is usually still running in the background. Send one done message. Then stop that running
background `wait`: in Claude Code, stop the background task. Do not re-arm `wait` after that. This
differs from `STOP` and `FINISH UP`: there, `wait` has already exited by delivering the matched word, so
there is nothing left to stop.

Transient network trouble (a connection error, a timeout, HTTP 5xx, or HTTP 429) is retried inside
`wait` itself: it logs one line to stderr and keeps waiting, so no action is needed. A non-zero exit is
a permanent error instead — an HTTP 4xx other than 429, an unknown or one-way channel, a corrupt
registry, or a bad interval: read stderr for the cause, report it to the operator, and do not re-arm
until it's fixed.

The interval is: the `--interval` flag, then the channel's registry entry, then a default of 20 minutes.

Use `ask` for every question that needs an operator decision, and always state the null default in the
question text (what happens if the interval passes with no reply).

## Vocabulary

Inbound is a closed vocabulary enforced in code: the script normalizes each message (trim, collapse
whitespace, uppercase, strip one trailing period) and returns an exact match or null. Anything else is
dropped silently to the agent — it only ever sees a count of unrecognized messages.

| Word | Effect |
|---|---|
| `STOP` | Halt now: kill background processes, leave files as they are, send one report. No commit. |
| `FINISH UP` | Graceful shutdown (see below). |
| `PAUSE` | Stop work, keep polling until `CONTINUE`. |
| `CONTINUE` | Resume, or take the default the pending question stated. |
| `STATUS` | Send one status line. |
| `APPROVE <code>` | Approve one pending question. The code is generated per question; a stale or wrong code is null. Never covers a destructive or spend-raising action — those wait for the operator at the terminal. |

One word per meaning, no aliases. If a poll returns several matched words, the script names the one
acted on by fixed precedence — `STOP` > `FINISH UP` > `PAUSE` > `APPROVE <code>` > `CONTINUE` > `STATUS`
— and reports the rest as superseded, never dropped silently. A superseded `APPROVE` is not consumed:
its question stays pending, and the operator can resend it.

Each `ask` generates one code and replaces any previous pending question — the old code goes stale. A
code matches once, then clears.

## FINISH UP

`FINISH UP` means gracefully finish a long-running task at a checkpoint, with every process accounted
for, then commit and push. It does **not** call the `wrap-up` skill — that skill is for interactive
end-of-session housekeeping, aborts before committing on failure, always pushes, and may ask the
operator; none of that fits an unattended agent acting on a one-word instruction.

1. Start no new work. Bring the current unit to the next safe checkpoint (not the end of the whole
   task).
2. Check each process the session started: stop it, or record its PID, log path, and reattach command
   if it must keep running.
3. Write a checkpoint note (done, stopped, still running, exact resume command, next step) so a fresh
   agent can continue. In a repo with a kb wiki (`wiki/` dir), append it to the active WK; if none, the
   active IN; if neither, create a new WK holding it. `CHECKPOINT.md` at the repo root is only for repos
   with no kb wiki.
4. Run the repo's documented validation command (`AGENTS.md` / `CLAUDE.md`); if none is documented,
   skip and say so.
5. Commit (current branch; never amend or force). Push only if validation passed; otherwise keep the
   commit local and say so.
6. Send one high-priority `FINISHED: <sha>, pushed yes/no, checkpoint at <path>`, then stop polling.

## Content rules

Topics are public by obscurity: anyone who knows a topic can read and post to it. So message bodies
never carry secrets, emails, record contents, or repo content — only status lines (suite names,
pass/fail counts, durations, costs).

Never put a topic name in a repo, a commit, a doc, or a screenshot. The topic itself is the only lock on
the channel. This is why one-way setup prints the `export NTFY_TOPIC=...` line instead of writing it
anywhere — see One-way wiring above.

## Rotation

Channels are long-lived, one per purpose — no calendar rotation. Rotate a channel's topics when a leak
is suspected: the topic was seen in a commit or a screenshot, or `unrecognized_total` is above 0 on a
live channel. Any `unrecognized_total` above 0 gets reported to the operator with a rotate proposal; it
is the leak signal, since inbound is otherwise a closed vocabulary.

## Two-way is Claude Code only

Two-way channels (the `wait`/poll loop) target Claude Code only in this version. Codex and other
harnesses are out of scope for now.
