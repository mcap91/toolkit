---
name: glass-home-samsung-tv
title: Glass Home for Samsung Tizen TV
url: https://github.com/victaphu/glass-home-samsung-tv
source_url: https://www.reddit.com/r/ClaudeAI/comments/1xbj7jr/i_used_claude_to_fix_my_samsung_tv/
source: reddit
category: cli-tool
summary: Apple TV-style home screen for Samsung Tizen TVs (2018-2025, Tizen 4-10) — a frosted-glass app dock, crossfading nature photos, clock/weather (Open-Meteo), and a screensaver, paired with a small password-protected website the TV itself serves on the home LAN for uploading photos and adding website/YouTube shortcuts from a phone; sideloaded via Tizen Developer Mode with a free per-TV Samsung certificate (no universal download, no root); one Tizen package bundles the UI and a Node.js service on 127.0.0.1:8090; ships tvremote.py (stdlib client for the TV's local control API), phonecam.py (turns a phone into a camera pointed at the TV, since "Samsung TVs can't take screenshots"), and wake.py; plain HTML/CSS/JS, MIT.
tags:
  - tizen
  - samsung
  - launcher
  - debloat
  - claude-code
  - agent-driven
  - home-screen
  - developer-mode
  - sideload
  - nodejs
  - python
  - camera-verification
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags:
  - no-prebuilt-binaries
  - agent-executes-device-commands
  - plaintext-local-http
overlaps:
  - free-my-tv
  - coding-agent-adb-tv-debloat
---

## What it does

Glass Home replaces the visible home screen on a Samsung Tizen TV (it cannot replace Samsung's own Home button, which still opens Smart Hub; the README's workaround is pinning Glass Home first on the Home row and enabling Autorun Last App so the TV reopens it at power-on). The screen itself is full-screen nature photos crossfading every 45 seconds, a frosted-glass dock of the owner's apps plus website and YouTube shortcuts, a clock/date, optional 7-day weather from Open-Meteo, and a screensaver after 3 minutes idle. A `+` tile opens a small password-protected website — served by the TV itself on the home network — for uploading photos from a phone (resized client-side so iPhone HEIC works) and adding website or YouTube shortcuts.

Install happens through Tizen's own Developer Mode: the owner makes a free, per-TV Samsung developer certificate, builds the app with Samsung's Tizen SDK command-line tools, and sideloads it — there is no universal downloadable package, since a signed build only installs on the TV it was certified for. The repo documents this as reported working on Samsung TVs from 2018 to 2025 (Tizen 4 through 10), with per-TV-model notes in a "Tested TVs" table built from community reports.

The repo's own account of its origin: "Built in an evening with Claude Code, which did the research, drove the TV over Wi-Fi, checked every step through the iPhone camera, and wrote and tested the app." Because Samsung Tizen TVs have no screenshot API, the repo ships `tools/phonecam.py`, a page that turns a phone on the same Wi-Fi into a camera pointed at the TV, as the only way an agent (or the owner) can see what's on screen during development.

## Mechanical details

- Platform: Samsung Tizen TVs only, reported Tizen 4 (2018 models, needing `photoService: false` and `smartHubLaunch: true` in config) through Tizen 10 (2025 models).
- Architecture: one Tizen web-app package containing the UI (`index.html`/`js`/`css`) and a bundled Node.js service (tested against the TV's Node 16, code restricted to the Node 12 API) listening on `127.0.0.1:8090`; the UI calls the service for photos/shortcuts and caches the last answer so it still renders if the service is down. With the free (public-level) signing certificate the service cannot start at boot, so the app starts it on each launch.
- Install tooling: Samsung's Tizen SDK command-line tools, `scripts/build.sh` then `scripts/install.sh`; config in `app/js/config.js` (dock apps by Tizen app ID, HDMI/tuner input tiles, weather coordinates, locale, screensaver delay, evening dimming hours, YouTube-shortcut launch mode, photo-rotation interval).
- `tools/`: `tvremote.py` (stdlib Python client for Samsung's local TV remote-control API — move/select/back, HDMI and tuner source switching via `tizen.tvwindow.setSource`), `phonecam.py` (phone-as-camera screen capture), `wake.py` (Wake-on-LAN).
- `docs/SAMSUNG-SETTINGS.md` documents turning off Samsung's content recognition (ACR), advertising ID, promotions and autoplay, plus a DNS-based ad filter, each with an undo path.
- Dev/test tooling (Node 22, a Chromium-based browser): `node dev/run.js --demo` runs the service and TV app locally; `dev/test-api.sh`, `node dev/ui-test.js`, and five more `dev/test-*.js` scripts cover the address-validation rules, hostile-page parsing, sign-in rate limiting, the TV app's service client, and the YouTube-link parser; all run in CI (GitHub Actions, macOS, Node 22) on every PR and push to main.
- Two related community projects are cross-referenced for a harder problem this repo explicitly does not solve — rewriting Home's own target app — CleanFrame and Arn0, each tested on only one TV.

## Security

- Trust model: installed only through Tizen's own Developer Mode with a user-obtained Samsung developer certificate scoped to one TV; nothing is rooted, and no universal binary exists to distribute.
- The password-protected local website runs over plain HTTP on the home network: the README states it only answers private-network/loopback addresses and needs the password, but acknowledges anyone else on the same Wi-Fi who intercepts traffic could see the password and photos in transit.
- Password handling: a three-random-words-plus-two-digits password stored as a PBKDF2-SHA256 hash, five-attempt lockout per device (five minutes), with claimed protection against one device's guessing blocking others; CSRF protection, a strict content-security policy, DNS-rebinding rejection (only private-network/loopback hosts answered), and real-JPEG validation with upload size caps on the photo-upload endpoint.
- Network surface: the app contacts only its own bundled service, Open-Meteo (if weather is enabled), each added website once for its favicon, and YouTube for shortcut titles/thumbnails — no analytics, accounts, or third-party favicon services.
- Agent-executed device changes: per the repo's own account, Claude Code built and tested this by driving the TV live over Wi-Fi during an unattended multi-step session, using a phone camera as its only visual feedback loop since Tizen has no screenshot API; no sandboxing or step-by-step human approval of each device command is described beyond the Reddit source's report that the agent asked about which apps/features to keep before changing anything.
- Supply chain: single-author repo; license is MIT per the repo, with separate photo/data credits.
