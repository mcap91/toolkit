---
name: agent-link
title: agent-link
url: "https://github.com/Riccardo8888/agent-link"
category: mcp-server
summary: "End-to-end encrypted channel between coding agents on different machines: the agents split work, hand off tasks, and report progress to each other. Transport is a shared private git repo (an orphan 'agent-link' branch) — no server, account, or open ports — with an optional relay for sub-second delivery. Installs an MCP server (link_* tools) plus a notification hook for Claude Code and/or Codex, and a human CLI. Frames are AES-256-GCM sealed and device-signed. Python 3.10+, one dependency, Windows/Linux/macOS."
tags: [multi-agent, coding-agents, mcp, end-to-end-encryption, git, claude-code, codex, collaboration]
reviewed: 2026-08-17
acquired: 2026-08-17
license: NOASSERTION
security_flags: [private-repo-required, no-forward-secrecy, carrier-sees-social-graph, untrusted-peer-input]
overlaps: []
source: unknown
---
## What it does

agent-link connects two (or more) coding agents running on different machines so they coordinate directly — splitting work, handing off tasks, and reporting progress in an end-to-end encrypted "room" — instead of a human copying messages back and forth. The message carrier is an ordinary shared private git repo (it can be the project repo you already collaborate on); a local daemon on each machine moves sealed frames through an orphan branch (`agent-link`) scoped to `claude-link/`, and your code is never fetched or touched.

## Mechanical details

- **Install:** `pipx install git+https://github.com/Riccardo8888/agent-link.git` then `agent-link install` (wires up Claude Code and/or Codex; `--agent`, `--skip-hook`, `--dev` options). Point at a repo: `agent-link config --set git_remote=...`; `agent-link doctor` verifies reachability/credentials/privacy.
- **Rooms:** `agent-link join --room <name>` mints a 128-bit secret and prints an invite (`name#<secret>`); peers join with `--invite`. Secretless "door codes" (`--door`) let others knock and be admitted by a per-member prompt; the room key is sealed only to the admitted device.
- **MCP tools:** `link_status`, `link_join`, `link_send`, `link_inbox` (≈1ms, hands off to daemon), `link_read`, `link_wait` (bounded blocking), `link_channel` (subagent side channels), `link_history`, `link_leave`. A notification hook pushes incoming messages into the session so agents needn't poll.
- **Transports:** git (default carrier), optional relay (`wss://`, client-side only; server ships separately), opt-in direct WebSocket on a trusted network. Presence heartbeats push ~every 45s. Messages logged per machine under `.conv/<room>/` (jsonl + transcript.md).
- **Tests:** 509 tests across Linux (3.10–3.14), macOS, Windows; drive real daemons and git clones, no network required.

## Security

- **Crypto:** rooms keyed by a generated 128-bit secret (never written to repo/relay). Frames are AES-256-GCM sealed under a key the carrier never sees and signed per device; the routing header is bound into signature and AEAD tag so a relay can't relabel or forge. Two independent security audits run against the threat model.
- **Stated limits (by design):** no forward secrecy (one long-lived room key — holders read past and future until rekey); removal rekeys forward but does not rewind; whatever carries messages learns the social graph (git host retains it — repo must be private; `doctor` fails a public carrier unless `allow_public_carrier` is set); transcripts stored in plaintext under `.conv/` on every member's machine.
- **Untrusted input:** a peer's message reaches a model's context, so remote content is fenced and marked as data; treat a room as a shared chat among mutually trusting parties and do not send credentials or client data.
- **Repo required to be private**; a repo with `on: push` CI needs `branches-ignore: [claude-link]` or heartbeats trigger builds. **License:** none stated in the README (repo private at time of review; recorded as NOASSERTION).
