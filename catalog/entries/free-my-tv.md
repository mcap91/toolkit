---
name: free-my-tv
title: Free My TV
url: https://github.com/simbasjungles/free-my-tv
source_url: https://github.com/simbasjungles/free-my-tv
source: web
category: cli-tool
summary: Open-source, ad-free home-screen replacement for Google TV/Android TV, LG webOS and Samsung Tizen TVs — a glass-shelf launcher showing only the owner's own apps, hourly TMDB trending picks limited to installed apps, Continue Watching from the TV's own Watch Next list, weather/crypto cards, a matching screensaver, and a sunset-driven day/night theme; runs through the TV's own ADB (pm disable-user/pm grant/pm revoke, cmd package set-home-activity) with nothing rooted or uninstalled and a one-button "Original" revert; agent-driven install (Claude Code, Codex, Antigravity given the TV's IP and city) builds and adb-installs it, with a prebuilt, signature/SHA-256-verified auto-updating APK also offered for Google TV; Java/Python/plain JS, MIT.
tags:
  - android-tv
  - google-tv
  - webos
  - tizen
  - lg
  - samsung
  - adb
  - debloat
  - launcher
  - claude-code
  - agent-driven
  - tmdb
  - plex
  - immich
  - pm-disable-user
  - restore-script
  - auto-update
reviewed: 2026-10-29
acquired: 2026-10-29
license: MIT
security_flags:
  - network-adb-plaintext
  - agent-executes-device-commands
  - accessibility-service-notification-listener
  - embedded-credentials-in-apk
  - self-updating-binary
overlaps:
  - cleanyourtv
  - dumbtv
---

## What it does

Free My TV replaces the home screen on Google TV/Android TV, LG webOS and Samsung Tizen TVs with an ad-free, open-source launcher: a shelf of the owner's own streaming apps, three to six TMDB trending/new-release picks refreshed hourly and limited to apps already on the TV (plus the owner's own Plex library on Google TV), Continue Watching pulled from Android TV's Watch Next list, weather and crypto-price cards, a "Now Playing" widget for background audio, a matching full-screen screensaver, and a light/dark theme that follows the TV's real local sunset. Nothing is rooted, flashed, or uninstalled — the app runs the TV's own ADB from inside the TV (connecting to `127.0.0.1:5555` with its own key) to run commands like `cmd package set-home-activity`, `settings put secure screensaver_components`, `pm disable-user`, and `pm grant`/`pm revoke` for the Continue Watching permission. A single "Original" menu item restores the factory home screen, screensaver, and every disabled app; the switch also reverts itself automatically after three crashes in five minutes.

Install is agent-driven on all three platforms. For Google TV/Android TV, the owner enables Developer Mode and USB debugging, gives a coding assistant (Claude Code, Codex, or Antigravity are named) the TV's IP and city, and the assistant clones the repo, installs the JDK/Android SDK/adb tooling, builds a signed ~2 MB APK (`aapt2` → `javac` → `d8` → `zipalign` → `apksigner`, no Gradle), and installs it with `adb install`. A prebuilt APK from GitHub Releases is also offered, which checks weekly (or on demand) for a newer signed release matching GitHub's listed size and SHA-256 before self-updating. LG webOS and Samsung Tizen ship the same UI rewritten in plain HTML/CSS/JS, installed through each platform's own Developer Mode (`webos/install.py`, or the community TizenBrew Installer for Samsung) rather than adb.

## Differentiators

- **Picks come only from apps already on the TV.** Trending/new-release titles are drawn from TMDB but filtered to streaming services the TV actually has installed (and the services the owner opts into), so nothing points to an app they don't use; an optional free Watchmode key makes a pick open the title's own page instead of just the app's home screen.
- **Three platforms, one design.** The same shelf/picks/weather/screensaver UI ships natively for Google TV/Android TV (Java, Canvas-drawn with Android 13 shaders for frosted glass) and as near-identical plain-JS apps for LG webOS and Samsung Tizen, each installed through that platform's own developer tooling rather than root.
- **Remote-button passthrough.** On TCL, Vestel, Xiaomi, Sony, Hisense, KTC, and the Google TV Streamer, a notification-listener/accessibility service reroutes hardware remote buttons (Netflix, Prime, YouTube, BRAVIA CORE, etc.) to an app the owner picks, since the stock home app that used to answer them is disabled.
- **Self-updating, signature-checked APK.** The release build checks GitHub weekly for a newer release, verifying size, SHA-256, and the project's signing key before installing through Android's own installer (which still prompts); a self-built APK only checks on demand and never auto-installs.
- **Own-photo and Immich support.** Up to 100 photos can be pushed to the TV directly (`tools/photos.py`) or, with an Immich server configured, the TV pulls a rotating batch itself every six hours using a key pushed over adb (never baked into the APK).
- **"Ask Claude" extensibility.** The README positions the repo as agent-adaptable: pointing Claude Code at an unsupported brand has it read the TV's installed apps and promo bloat, then update the project's per-brand lists itself.

## Mechanical details

- Platforms: Google TV and Android TV 8+ (TCL, Sony, Hisense, Philips, Xiaomi, Vestel, KTC/NextStar, Chromecast with Google TV, Google TV Streamer, onn 4K, Mi TV Stick, NVIDIA Shield, Wanbo projectors); LG webOS 3+; Samsung Tizen (2015+, with caveats on 2015–2018 sets: no TizenBrew, no TV Settings access, some models refuse developer installs). Fire TV, Huawei HarmonyOS, and the Kalley 43G200 run it only as a regular app, not as the home screen.
- Host requirements: a computer on the same Wi-Fi as the TV. Google TV build: JDK 17+, Android SDK command-line tools (build-tools 34, platform android-34), adb. LG/Samsung: Python 3 only.
- Key commands: `./build.sh` (Google TV), `python3 webos/build.py` + `webos/install.py <ip>` (LG), TizenBrew Installer or `python3 tizen/build.py` + `tizen/install.py <ip>` (Samsung); `python3 tools/photos.py <ip> <files>`, `python3 tools/send_key.py <ip> <immich-key>`, `python3 tools/translate.py`.
- Config: a single `config.properties` (TMDB key, Watchmode key, Plex URL/token, Immich server, Trakt client ID, location, language, theme, currency) read by all three platform builds; most values can also be changed on-device in Home Settings, which wins over the file.
- Data sources: TMDB (trending/new titles, regional availability), Open-Meteo (weather, sunrise/sunset), and optionally Binance (crypto prices), Watchmode (deep links), the owner's Plex server, the owner's Immich server, and Trakt (watch history/watchlist, Google TV only).
- Repo stats at review (GitHub API, 2026-10-29): ~5,400 stars, ~900 forks, 63 open issues, created 2026-10-19, primary language Java, MIT license.

## Security

- Trust model: all device changes go through the TV's own ADB after the owner explicitly approves an "Allow USB debugging" prompt for the app; nothing is written to `/system`, and disabled apps are flipped with the same per-user disable Settings → Apps already exposes, not uninstalled.
- Network ADB exposure: initial setup and the manual/LG/Samsung install paths use `adb connect <ip>:5555`, which is plaintext network ADB; the README does not instruct turning debugging off afterward (unlike comparable tools in this category), though the on-device approval prompt still gates it per app.
- Accessibility service and notification listener: remote-button passthrough and the Now Playing widget use an accessibility service and a notification listener respectively — permission classes Google Play Protect flags more aggressively on some Android 14 builds/regions ("App blocked to protect your device" for sideloaded apps using either, per the README and issue #378).
- Embedded credentials: the README states the Plex token is baked into the installed APK, which "any app on the TV can read" — it explicitly recommends a scoped Plex Home managed-user token rather than the owner's own, and to never commit it to the repo. The TMDB and Watchmode keys carry the same exposure. The Immich key is pushed separately over adb to the app's private storage instead, specifically to avoid this exposure.
- Self-update path: the release APK fetches `api.github.com` weekly and installs new releases through Android's own installer after checking release size, SHA-256, and the project's signing key — a self-built APK only checks on demand, never auto-installs.
- No accounts, analytics, or tracking; the stated network surface is TMDB, Open-Meteo, and — only when configured — Binance, Watchmode, Plex, Immich, Trakt, and GitHub (update checks).
- Supply chain: single-author young repo (created 2026-10-19), MIT license matches the LICENSE file; built with Claude Code per the README's credits, with install-flow instructions written for an AI coding assistant to execute directly on the user's behalf.