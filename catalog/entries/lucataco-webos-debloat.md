---
name: lucataco-webos-debloat
title: webos-debloat (lucataco)
url: https://gist.github.com/lucataco/7c303b443934008a9031a55cfca552ec
source_url: https://gist.github.com/lucataco/7c303b443934008a9031a55cfca552ec
source: web
category: cli-tool
summary: Single shell script for a rooted LG webOS TV that hides launcher bloat tiles and background apps, stops those apps from preloading into RAM, and disables home-screen promotions, sports alerts, recommendations and LG's Live Plus (ACR) tracking by editing LG's own app block list, preload-manager policy and settings keys (never the root filesystem), making every change reversible without blocking firmware updates; tested on one 2026 LG OLED (webOS 26, firmware 11.2).
tags:
  - webos
  - lg
  - debloat
  - shell-script
  - root
  - preload-manager
  - telemetry
  - acr
  - privacy
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags:
  - root-shell-required
  - unauthenticated-telnet-root-shell
  - single-device-tested
overlaps:
  - free-my-tv
---

## What it does

"webos-debloat" is a single shell script for a rooted LG webOS TV that hides bloat tiles and background apps from the launcher, stops the OS from preloading apps into RAM whether or not they're opened, and turns off home-screen promotions, promo videos, sports alerts, content recommendations and LG's Live Plus (ACR) tracking. Per the gist, it only edits LG's own app block list, the preload manager's policy file, and a handful of system settings — the root filesystem is never touched — so every change is reversible and firmware updates continue to install as on a stock TV. The author states it was written and tested on one TV (a 2026 LG OLED running webOS 26, firmware 11.2, US region) and recommends starting with `--plan`/`--dry-run` on other models, since untested app IDs or settings keys are skipped rather than causing failures.

## Mechanical details

- Requires: root via Homebrew Channel (webosbrew.org; method depends on firmware) and a root shell on the TV — SSH recommended, or Homebrew Channel's telnet.
- Delivery onto the TV: `ssh root@<tv-ip> 'cat > /tmp/webos-debloat.sh' < webos-debloat.sh`, or (telnet-only) serve the folder with `python3 -m http.server` and `curl` it from the TV, since `/tmp` is wiped on reboot (`--install-boot-hook` copies the script to a persistent path).
- Flags: `--list`, `--plan`, `--apply` (default categories), `--preload-off` (frees RAM — the step `--apply`'s cosmetic hiding doesn't achieve on its own), `--settings-off` (promos/alerts/recommendations/ACR), `--install-boot-hook` (replays settings at boot via `/var/lib/webosbrew/init.d/*`), `--status`. Category selection via `--only a,b,c` or `--id <app-id>`: `ad`/`sdk`/`demo`/`remote` default on; `promo`/`visible`/`extras`/`all` default off. A `PROTECTED_IDS` list in the script always exempts Home, Settings, Live TV, inputs, the browser, first-run setup and Homebrew Channel itself.
- Undo: `--remove-boot-hook`, `--restore`, `--preload-on`, `--settings-restore`; the first run backs up every file it edits to `*.orig` and never overwrites those backups.
- Documented findings in the gist: hiding apps is cosmetic and doesn't free memory by itself; the actual RAM savings come from the preload manager's `allowedApps` map in `/var/preferences/webos-preload-manager-conf.json` (read/set via `luna-send`); powering the TV "off" is usually suspend rather than a real reboot, so boot hooks (which fire only on real reboot) don't replay on resume — webOS instead relaunches LG Home with `reason:"boot"` on resume, observable via `luna-send getAppLifeEvents`.

## Security

- Homebrew Channel's telnet access is an unauthenticated root shell open to the whole local network; the gist's own security note recommends enabling SSH with a key and disabling telnet once set up.
- Requires root, which (per the wider webOS Homebrew ecosystem) voids the TV's warranty and can be undone, or made un-reapplicable, by an LG firmware update.
- MIT licensed; single-author gist, stated as tested on exactly one device/firmware combination at time of review.