---
name: cleanyourtv
title: CleanYourTV
url: https://github.com/Gathin23/cleanyourtv
source_url: https://www.instagram.com/reel/De5smNojeZm/
source: instagram
category: cli-tool
summary: Debloats Android TV / Google TV over network ADB without root — backs up package state, disables manufacturer telemetry, ad rows and preloads with pm disable-user (nothing uninstalled, one-line restore), and builds/installs a ~532 KB plain-Java launcher sized for 1 GB TVs; driven by a coding agent (Claude Code, Codex, Gemini CLI) via PROMPT.md/AGENTS.md or by hand with bash/PowerShell scripts and a pure-Python ADB client; per-model debloat lists for 170+ TV models from 200+ contributors; Python/Java, MIT (launcher font OFL)
tags:
  - android-tv
  - google-tv
  - adb
  - debloat
  - privacy
  - launcher
  - claude-code
  - agent-driven
  - python
  - java
  - pm-disable-user
  - restore-script
reviewed: 2026-10-28
acquired: 2026-10-28
license: MIT
security_flags:
  - no-prebuilt-binaries
  - network-adb-plaintext
  - agent-executes-device-commands
overlaps:
  - dumbtv
---

## What it does

CleanYourTV removes manufacturer bloat from any Android TV or Google TV from a computer on the same Wi-Fi, using the standard Android Debug Bridge. The owner enables Developer options and USB/network debugging on the TV and approves the computer once. The tool then runs three steps: back up the installed-package list and settings, disable telemetry, ad services, content rows and preloaded apps with `pm disable-user` (nothing is uninstalled, so a restore script can replay the recorded state), and install a small native launcher as the default Home.

The primary workflow is agent-driven. The user clones the repo, opens it in a coding assistant (Claude Code, Codex, Gemini CLI or Antigravity CLI are named), pastes `PROMPT.md` with their TV model, and answers a checklist (which apps they use, dock size, whether to keep voice assistant, Chromecast and updates). The assistant reuses the repo's `tools/disable.sh` and `launcher/build-and-install.sh`, and verifies each step with screenshots pulled from the TV. Because bloat differs by brand, the prompt has the assistant discover packages on the actual TV and ask before touching anything, rather than applying a fixed list.

Everything the assistant does can also be run by hand. The README lists bash scripts with PowerShell twins for Windows.

## Differentiators

- **Discovery, not a fixed list.** The agent prompt inspects the specific TV and asks before disabling; contributed per-model lists in `examples/` (one folder per model, 170+ models across ~100 brands and 14 projector brands) let the next person with that model skip discovery.
- **Pure-Python ADB client.** `tools/tv.py` talks to network ADB on port 5555 without the stock `adb` binary (shell, batch, push, pull, reboot, screenshots with optional key presses first), with an optional paired backend for encrypted Wireless debugging. Motivation given: macOS Local Network privacy blocks `adb connect`.
- **Home guard.** Install scripts ask the TV which launcher owns HOME and only disable one of four recognised stock launchers (tvlauncher, launcherx, leanbacklauncher, Xiaomi PatchWall). `disable.sh` skips the Home owner from a list if no other app answers HOME, so a list applied before launcher handover cannot leave the TV without a Home app. On Google TV it also handles the setup wizard (`setupwraith`) taking HOME and crash-looping.
- **Restore record.** Before any change, `disable.sh` writes the TV's prior state to `~/.cleanyourtv/`; `restore.sh` replays it, keeping packages the user had disabled themselves disabled and returning Home to the original component.
- **Firmware-update drift check.** `check.py` compares the TV against the applied list after an update and `--fix` reapplies.
- **Launcher.** ~532 KB plain Java, Android 8.0+ (API 26), no blur, no video, no network permission, no background services; themes via pushed `config.json` without rebuild, 30 languages, optional app library, tile menu and module cards (third-party apps can contribute a tile with explicit approval). Build requires JDK 17–22 and Android SDK platform 34; a Docker build script is provided. No prebuilt APKs are distributed.
- **Measurement tooling.** `bench.py` (key latency, janky frames, cold start, idle CPU/PSS), Perfetto trace capture and reports, flame chart generation, and pixel screenshot diffing.
- **Privacy audit.** `privacy.py` lists voice, ACR and telemetry candidates with evidence; `--write` turns findings into a debloat list.

## Mechanical details

- Platforms: Android TV and Google TV (full). Fire TV: debloat half only (Fire OS will not hand HOME to a third-party launcher; 2015 Fire OS 5 box refuses all `pm` routes). Some China-market TCL sets refuse any launcher install. Samsung Tizen, LG webOS, Roku, Vizio, Hisense VIDAA: unsupported (no ADB); a separate page covers remote-only tracking toggles.
- Host requirements: Python 3 for the tools; JDK 17–22 (full JDK with jlink; JDK 23+ breaks Gradle 8.9) and Android SDK platform 34 / build-tools 34.x for the launcher build. macOS: `brew install openjdk@17 android-commandlinetools`. Windows: PowerShell scripts use `JAVA_HOME` or Android Studio's bundled JDK.
- Key commands: `tools/tv.py --probe`, `tools/disable.sh <list>`, `tools/restore.sh <list> [stock-launcher-pkg]`, `tools/check.py <list> [--fix]`, `launcher/build-and-install.sh`, `tools/theme.sh themes/<name>`, `tools/adb-closed.py <ip>` (exit 0 when ADB port is closed).
- Remote use: documented over a private Tailscale link; the README says never to expose the ADB port on a router.
- Related: a community-built Android phone app by @udhaykumarbala does the same cleanup from a phone with no laptop or coding agent. `SHOWCASE.md` indexes ~147 derived projects (home screens, forks, add-ons, webOS ports). Stated origin: a 17 October 2026 before/after post of the author's parents' TV cleaned by Claude Code; renamed from `tv-vibehack` on 19 October 2026.
- Repo stats at review (GitHub API, 2026-10-29): ~44k stars, ~5.4k forks, 149 open issues, created 2026-10-17, language Python; topics include adb, debloat, claude-code, vibe-coding. GitHub reports license as NOASSERTION; README and LICENSE state MIT with the Outfit font under SIL OFL.

## Security

- License: README states MIT; GitHub's detector returns NOASSERTION, likely because the LICENSE file combines MIT with the OFL font notice.
- Trust model: the tool runs shell commands on a device the user owns via an explicit "Allow USB debugging" approval. Nothing is rooted, flashed or written to `/system`; packages are disabled in the user profile, the same switch as Settings → Apps → Disable.
- Network ADB on port 5555 is plaintext, and on some firmware any LAN device gets a shell while it is open. The README instructs turning debugging off and revoking authorisations when done, and ships `adb-closed.py` to confirm the port is closed.
- Agent-driven mode means a coding assistant executes device commands; the README notes assistants ask before each command. The reel this entry derives from reports one user bricked a TV; the README says disabling something the TV relies on is the risk, mitigated by small batches, a ready restore script, the TV's own Settings → Apps re-enable path, and factory reset as last resort.
- No prebuilt binaries: the launcher is built from source on the user's machine, which requires a JDK and Android SDK.
- Supply chain: very young repo (12 days at review) with very high contributor volume (README cites 200+ contributors, releases note 323 PRs from 176 people in two days). Most contributions are per-model debloat lists; `CONTRIBUTING.md` and `AGENTS.md` describe testing asked of contributors. A SECURITY.md private-report path exists. Tests and CI were not inspected for this entry.
- Optional Private DNS ad blocking (e.g. AdGuard DNS) is documented with the trade-off that the resolver sees all TV DNS queries.

## Usage notes

- Fire TV reel demo: setup needs the device name, software version and IP address (from Settings → My Fire TV → About) given to the coding agent before it configures the connection (source: https://www.instagram.com/reel/DfDh40rPknX/)
- A separate `apply-wallpapers.sh` script pushes custom wallpaper images to the launcher; it needs ADB Debugging left on (an unencrypted LAN connection), which can be toggled off after setup and back on only when pushing new wallpapers (source: https://www.instagram.com/reel/DfDh40rPknX/)
- Observed launcher config fields beyond theme: apps-per-row (4 or 5), rows-below-dock (0 or 1), dock-band-opacity (70% or 100%), and per-app ordering/prioritization (e.g. pinning specific streaming apps to the top) (source: https://www.instagram.com/reel/DfDh40rPknX/)
