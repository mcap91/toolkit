---
name: api-anything
title: API Anything
url: https://github.com/goodnight000/api-anything
source_url: https://www.instagram.com/reel/DeON0MOB5oi/
category: mcp-server
summary: MCP server, CLI, and TypeScript library that turns a website's own frontend requests into a reusable HTTP "operation" an agent can call instead of driving a browser — a headless browser loads the target page once per example input, the part of the request that varies becomes a parameter, and cookies/tokens become references to a local store rather than literal values. Calls replay as plain HTTP where possible, falling back to in-browser fetch or full page render; when a learned operation drifts, the first caller to hit the failure repairs it and the fix is shared to a public Cloudflare Worker catalog (30 bundled read operations across 14 sites — Google Flights, Goodreads, Rotten Tomatoes, Hacker News, X, Instagram, YouTube, Steam, Airbnb, Amazon, Rightmove, Pinterest, LinkedIn, Domino's Australia). Writes are opt-in (--allow-writes) and guarded (write-interception during learning, duplicate-write refusal, idempotency keys). MIT, TypeScript, ~1.7k GitHub stars / 179 forks as of October 2026 (per trendshift.io), 2 contributors.
tags:
  - mcp-server
  - web-scraping
  - browser-automation
  - reverse-engineering
  - api
  - agent-tools
  - self-healing
  - typescript
  - cli
  - claude-code
  - shared-catalog
  - nodejs
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: MIT
security_flags:
  - "Dual-use web-automation tool: bypasses normal API access by learning a site's own frontend requests; README states 'read each site's terms, you're responsible for how you use it' and does not evaluate ToS compliance for bundled targets (e.g. LinkedIn, Instagram, X) or learned sites"
  - Source item (Instagram reel) describes using it to automate LinkedIn outreach and Reddit marketing — automated interaction with sites whose terms generally restrict scripted use is a user-assumed risk the tool does not evaluate or prevent
  - Session login imports live cookies from the user's local browser profiles (Chrome, Arc, Brave, Edge, Chromium, Firefox) to authenticate operations; project states specs persist only cookie/token references, not values, and redacts live values in error output, but the import step itself handles sensitive session credentials
  - Calling an unlearned site pulls a community-contributed operation spec from a public shared catalog before any independent audit — promotion to 'live' is based on crowd-reported success/failure counts (2 confirming networks, 3 failing networks to demote), not a security review
  - By the project's own documentation, a write operation's '2xx accepted' response does not confirm the action was actually applied server-side; only an operation with an author-defined readback check reports 'applied', so a write can silently misreport success
source: instagram
---

## What it does

API Anything is an MCP server, CLI, and TypeScript library that turns a website's own frontend network traffic into a reusable "operation" an agent can call over plain HTTP instead of driving a browser. A headless browser loads the target page once per example input; the part of the request that changes with the input becomes a parameter, and cookies/tokens become references to a local credential store rather than literal values. A learned call replays as a plain HTTP request first ("tier 1"); if the site blocks that, it falls back to fetching from inside a browser page, and as a last resort renders the full page and reads its own response. When a learned operation's shape drifts (a rotated id, a moved field), the first agent to hit the failure re-learns and repairs it, and the fix is pushed to a shared public catalog so other installs skip the repair.

## Mechanical details

- Setup: `npx -y api-anything setup` (Node 22.13+) auto-detects and registers the MCP server with Claude Code, Codex, Cursor, and Claude Desktop, adds the skill to clients that support skills, and backs up each edited config file to `<file>.bak-api-anything`. Manual per-client registration after `npm install -g api-anything`: e.g. `claude mcp add --scope user api-anything -- api-anything mcp` (Claude Code) or `codex mcp add api-anything -- api-anything mcp` (Codex).
- MCP tools: `find_sites`, `learn_site`, `list_sites`, `list_operations`, `call_operation` (reads only), `call_write_operation` (exposed only when the server is started with `--allow-writes`), `get_job` (for a call still running after ~25s), `login`.
- CLI equivalents: `api-anything sites | ops <site> | call <site> <op> k=v | add ...`; `--dry` prints the underlying HTTP request with credentials redacted before sending it for real. TypeScript library: `import { call } from "api-anything"`.
- Ships 30 pre-built read operations across 14 sites (Google Flights, Goodreads, Rotten Tomatoes, Hacker News, X, Instagram, YouTube, Steam, Airbnb, Amazon, Rightmove, Pinterest, LinkedIn, Domino's Australia); LinkedIn's bundled operations (`getMe`, `getProfile`, `getCompany`, `searchPeople`, `searchCompanies`) require a signed-in session.
- The shared catalog is a Cloudflare Worker storing anonymized operation specs and per-call success/failure reports — it never proxies a request, calls always run on the user's own machine/network/session. A new operation serves as confirmed "live" only once installs on 2 other networks report it working, and is demoted back to "candidate" once 3+ networks report it failing.
- Needs a local Chromium-family browser (Chrome, Brave, Edge, Chromium, Vivaldi, Arc) only to learn new sites; calling an already-learned or shared operation needs no browser. No account system — a per-install anonymous key lives at `~/.api-anything/key.json`.
- Self-reported benchmark (one site, one model, "a few dozen runs," not independently reproduced here): a 5-book Goodreads task via Claude Opus 5.5 in Claude Code took 182.5s driving a headless browser vs. 30.5s calling the learned API Anything operation, at roughly a third of the token cost.

## Security

MIT licensed. Operation specs store cookie/token references (e.g. `cookie:name`), never live values, and the project states a spec carrying a live credential is refused before it can be saved or published; `publish` previews exactly what an upload sends and which host it goes to before anything uploads. Session login (`login`) imports cookies from an already-signed-in local browser profile (Chrome, Arc, Brave, Edge, Chromium, Firefox on macOS/Linux; opens a window on Windows); a learned flow is designed to fail rather than type into a password or one-time-code field. Writes are opt-in end-to-end (`--allow-writes` server flag, `call_write_operation` tool, `allowWrites` library option); learning a write intercepts and aborts the underlying request so the learning phase itself never performs it, and a repeated write within 10 minutes is refused as a duplicate unless overridden with `--again`. By the project's own account, a "2xx" write response only means `accepted`, not confirmed — `applied` requires an operation-specific readback check, so a write can silently misreport success. No CAPTCHA-solving or bot-wall bypass is built in; a challenge shown to the real browser used for learning must be cleared by hand. The README states "read each site's terms, you're responsible for how you use it" — several bundled targets (e.g. LinkedIn) restrict automated access in their terms of service, and the source reel for this entry describes using the tool specifically to automate LinkedIn outreach and Reddit marketing, a user-assumed ToS/legal risk the tool does not evaluate or prevent. Calling a site this machine hasn't learned yet pulls a community-contributed spec from the shared catalog — a pulled operation is another anonymous installer's work, gated by the crowd-promotion rules above rather than an independent security audit.
