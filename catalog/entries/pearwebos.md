---
name: pearwebos
title: PearWebOS
url: https://github.com/Arnedeklerk/PearWebOS
source_url: https://github.com/Arnedeklerk/PearWebOS
source: web
category: cli-tool
summary: Python CLI and home-screen replacement for rooted LG webOS TVs, styled after Apple TV's Home — name/date/clock/weather over the owner's own photos, six apps in a dock with every other installed app one press down, Inputs/Settings top right; runs entirely through the TV's own rooted SSH access with a one-command revert to LG's stock Home; built for webOS 6 (2021 TVs), with newer webOS (incl. 10) supported as a separate app install rather than a full Home replacement.
tags:
  - webos
  - lg
  - launcher
  - root
  - apple-tv-style
  - python
  - homebrew-channel
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags:
  - root-shell-required
  - default-ssh-password
  - voids-warranty
overlaps:
  - free-my-tv
---

## What it does

PearWebOS is a Python-based home-screen replacement for rooted LG webOS TVs, styled after the Apple TV Home screen: the owner's name, the date, a clock and weather displayed over their own photos, six apps shown in a "glass" dock with every other installed app one press down, and Inputs/Settings reachable from the top right. The README states Pear changes nothing in the TV's own system and that a single command restores LG's stock Home screen. It's built for webOS 6 (2021 TVs); on newer sets, including webOS 10, it installs as its own app rather than replacing Home outright, which the README calls new and asks users to report results on.

## Mechanical details

- Requires a rooted LG TV (Homebrew Channel with SSH enabled) and a computer with Python 3.
- Install: `git clone https://github.com/Arnedeklerk/PearWebOS.git && cd PearWebOS`, `python3 -m pip install --user pillow numpy`, `ssh-copy-id root@<tv-ip>` (Homebrew Channel's documented default telnet/SSH password is `alpine`), then `./pear setup`, which finds the TV, asks a few questions, and installs in about a minute.
- Remote control mapping once installed: left/right moves along the dock, down shows all apps, up opens Inputs/Settings, OK opens the selected item, holding OK rearranges the dock.
- `./pear photos` pushes files from a local `photos/` folder to the TV; `./pear update` updates Pear from either the on-TV Settings menu or the same CLI command.

## Security

- Requires root via Homebrew Channel; the README states rooting may void the TV's warranty.
- Setup authenticates over SSH using `ssh-copy-id` against Homebrew Channel's documented default password (`alpine`) and does not instruct changing it afterward.
- States it changes nothing in the TV's own system and ships a one-command revert to LG's stock Home; MIT licensed, not affiliated with LG or Apple.