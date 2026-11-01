---
name: dumbtv
title: dumbtv
url: https://github.com/humblemuzzu/dumbtv
source_url: https://www.instagram.com/reel/De5smNojeZm/
source: instagram
category: cli-tool
summary: Removes ads, tracking and clutter from Amazon Fire TV sticks, Cubes and Fire TV Edition televisions over ADB without root — disables ~50 Amazon packages (sponsored rows, ad services, ACR screen fingerprinting, telemetry, experiments) with pm disable-user, turns off ad tracking and usage reporting, optionally runs the open-source personalDNSfilter on the TV to block ~400 Amazon telemetry/ad/update hosts, and replaces Amazon's home screen with a 54 KB permissionless Java launcher; agent-driven via AGENTS.md (Claude Code, Codex, Cursor, Gemini) or by hand via preflight/configure/all/verify/restore bash scripts; nothing written to /system, one-command undo; MIT scripts and launcher, CC BY-SA 4.0 device catalog
tags:
  - fire-tv
  - fire-os
  - adb
  - debloat
  - privacy
  - telemetry
  - dns-filter
  - launcher
  - claude-code
  - agent-driven
  - bash
  - java
  - restore-script
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT
security_flags:
  - network-adb-plaintext
  - agent-executes-device-commands
  - blocks-os-updates-while-dns-filter-runs
  - downloads-third-party-apks-on-request
overlaps:
  - cleanyourtv
---

## What it does

dumbtv is a set of bash scripts and a launcher that clean up an Amazon Fire TV device from a computer over ADB, with no root. The author's stated origin: a Fire TV Edition television with 129 MB free memory, lagging menus and an ad-filled home screen; they asked a coding agent to clean it over ADB, posted the result, and published the scripts when people asked.

What it changes:

- **Amazon packages.** About 50 disabled: ads, sponsored content, ACR (automatic content recognition / screen fingerprinting), telemetry, crash and usage uploads, experiments, update nags. Disabled with `pm disable-user`, never deleted.
- **Protected packages.** The few Amazon does not let anyone disable lose background running; the DNS filter blocks what they upload.
- **Settings.** Ad tracking limited, interest-based ads off, usage reporting off, home-screen autoplay off.
- **DNS.** personalDNSfilter (GPL-2.0, from F-Droid) runs on the TV and blocks about 400 Amazon telemetry, ad and update hosts using HaGeZi's Amazon tracker list. YouTube, the Appstore and other apps are not blocked.
- **Home screen.** "dumbtv home" replaces Amazon's: apps, HDMI inputs and a clock, no promo tiles or sponsored rows.
- **User apps.** Untouched unless the user names one for removal.

## Differentiators

- **Consent-gated configuration.** `configure.sh` asks six questions (keep Prime Video reachable, keep Alexa and voice button, replace home screen, run DNS filter, apps to remove, replace YouTube with SmartTube) with defaults; answers persist in `dumbtv.conf`. `preflight.sh` reports what the TV is and what would change without changing anything, and takes the settings snapshot `restore.sh` later replays.
- **Agent entry point.** With a coding agent (Claude Code, Codex, Cursor, Gemini named), the user clones the repo and says "Clean up my Fire TV. Its IP address is X"; the agent reads `AGENTS.md`, asks the questions, and runs the scripts in order. `AGENTS.md` encodes the safety rule: never write to `/system`, no `adb remount`, no `adb root`, no hosts-file edits, no deleting system APKs.
- **On-device DNS filter** for what cannot be disabled, rather than a network-level blocker.
- **Launcher.** 54 KB plain Java, no libraries, no internet permission; on Fire OS 7 and 8 it requests no permissions at all. Accent colours, tile sizes, rows or grid, wallpapers, adaptive backgrounds, renaming and hiding from the remote. Installable standalone via `launcher/install.sh`.
- **Device catalog with test provenance.** Each tested row names the Fire OS version, status (tested = full pass with `verify.sh` passed, or partial) and the GitHub user who ran it; ~25 Fire OS devices plus ~11 Android TV / Google TV reports run by hand from lists in `data/androidtv/`. `scripts/contribute.sh` writes the report for a new device.

## Mechanical details

- Flow by hand: `adb connect <tv-ip>:5555` (press Allow on TV), `./scripts/preflight.sh`, `./scripts/configure.sh`, `./scripts/all.sh` (asks before each step, reboots the TV twice), `./scripts/verify.sh`. Individual steps: `debloat.sh`, `lockdown.sh`, `dnsfilter.sh`, `launcher.sh`, `youtube.sh` (only if YOUTUBE=1), each with `-y`.
- Undo: `./scripts/restore.sh` re-enables every package, clears app and network rules, restores snapshotted settings, removes the filter and gives HOME back to Amazon. A user-removed app comes back from the Appstore. A factory reset also removes everything dumbtv did.
- Host: macOS, Linux, Windows (WSL or Git Bash); needs `adb` and about ten minutes. Enable ADB on the TV: Settings → My Fire TV → About → press OK on the device name 7 times → Developer Options → ADB debugging.
- Fire OS coverage: SDK 25 (Fire OS 6), 28 (Fire OS 7), 30 (Fire OS 8). Tested end to end on Fire OS 7.7.1.7 (Android 9).
- Limits stated by the project: Fire OS updates are blocked while the DNS filter runs (FAQ covers updating anyway); the boot chain is locked so Fire OS cannot be replaced; YouTube ads cannot be blocked by DNS because they come from the video servers (SmartTube offered as the alternative).
- Points Android TV / Google TV users to cleanyourtv for a full tool; Samsung, LG, Roku and others have no ADB path (`docs/OTHER-TVS.md`).
- Third-party components are downloaded on request, not bundled: personalDNSfilter (GPL-2.0), HaGeZi's Amazon tracker list (GPL-3.0), SmartTube (MIT).
- Repo stats at review (GitHub API, 2026-10-29): ~1.7k stars, ~167 forks, 16 open issues, created 2026-10-18, language Java; topics include adb, debloat, dns-filter, fire-tv, telemetry. ~50 contributors credited for code, fixes and device reports.

## Security

- License: README states MIT for scripts, docs and launcher; device catalog CC BY-SA 4.0. GitHub's detector returns NOASSERTION, consistent with a multi-license LICENSE file.
- Trust model: shell commands run on a device the user owns via the one-time ADB "Allow" prompt. Nothing is written to `/system`, so a factory reset fully reverts; the project states this is the part whose modification bricks a device.
- Network ADB on port 5555 is plaintext; the README does not include an explicit "turn debugging off afterwards" step in the quick start (cleanyourtv does), so operators should add that themselves.
- Agent-driven mode has a coding assistant execute device commands under the `AGENTS.md` rules; `all.sh` asks before each step.
- Running the DNS filter blocks Fire OS updates, which is a deliberate trade-off the project documents; disabling the filter restores updates.
- The DNS filter and SmartTube are third-party APKs fetched from F-Droid and the SmartTube releases on request; the TV then runs them. The filter sees every DNS query the TV makes.
- Supply chain: young repo (11 days at review), single primary maintainer, many small community contributions mostly device reports. Tests and CI were not inspected for this entry.