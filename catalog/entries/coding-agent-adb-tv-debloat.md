---
name: coding-agent-adb-tv-debloat
title: Coding-Agent TV Debloat over ADB
url: https://www.instagram.com/reel/De5smNojeZm/
source_url: https://www.instagram.com/reel/De5smNojeZm/
source: instagram
category: agent-pattern
summary: "Pattern for using a coding agent (Claude Code in the source) to debloat an Android TV / Google TV over network ADB without root — enable developer options and debugging, give the agent the TV model and IP, have it back up the package list and write a restore script before changing anything, classify installed packages (tracking, ads, background extras, used apps) for the user to choose from, disable with pm disable-user rather than uninstall, and verify each change by sending remote key events and pulling screenshots; extras: lower animation scales, swap the stock launcher for a lightweight one; documented risks: bricking from disabling the wrong system package, loss of disabled features, small gains on 1 GB TVs, leave debugging on"
tags:
  - agent-pattern
  - android-tv
  - google-tv
  - fire-tv
  - adb
  - debloat
  - claude-code
  - backup-before-change
  - screenshot-verification
  - restore-script
  - device-automation
reviewed: 2026-10-28
acquired: 2026-10-28
license: NOASSERTION
security_flags:
  - agent-executes-device-commands
  - network-adb-plaintext
  - user-reported-bricked-device
overlaps:
  - cleanyourtv
  - dumbtv
---

## What it says

The reel describes a ten-step workflow in which a general coding agent, not a purpose-built app, does the cleanup of a slow Android TV or Google TV over ADB. The agent connects to the TV, inventories packages, proposes what to disable, applies changes with a reversible command, and checks its own work by looking at the screen. Two repos the reel cites (CleanYourTV and dumbtv) package this same loop with prompts, scripts and per-model package lists.

The steps as given:

1. On the TV: Settings → Device Preferences → About, press OK on Build seven times to unlock Developer options.
2. In Developer options turn on USB debugging, plus Network debugging if present.
3. Note the TV's IP address from Wi-Fi settings.
4. On a laptop on the same Wi-Fi install Android platform tools (ADB) and the coding agent, and sign in.
5. Tell the agent the TV model and IP and ask it to connect over ADB. The reel notes that vague phrasing like "hack my TV" can be refused; being specific about the owned device and the goal works.
6. Accept the "Allow USB debugging?" prompt on the TV. Only approved computers get in.
7. Have the agent back up the full app list and current settings and write a `restore.sh` before anything is changed. This is the undo button.
8. The agent sorts every installed package into tracking, ads, background extras, and apps the user uses. The user picks what stays.
9. The agent disables the extras with `pm disable-user`. Disabled, not deleted, so each step can be undone.
10. The agent presses remote buttons via key events and pulls screenshots of the TV to check each change landed.

Additional tips: lower the animation scales in Developer options, and swap the heavy stock home screen for a lighter launcher (one user reported going from a 192 MB launcher to an 83 MB one and disabling 25 bloat packages; the reel's on-screen text names Projectivy, FLauncher and ATV Launcher as alternatives).

## Key takeaways

- **Backup and restore script before the first change.** The agent writes the undo path first, then mutates. Both cited repos encode this as a hard rule (record prior state, replay on restore).
- **Classify, then let the human choose.** The agent produces a categorised inventory; the user approves the disable set. Both repos extend this with discovery on the actual device rather than a fixed list, because bloat varies by brand.
- **Reversible primitive over destructive one.** `pm disable-user` (same switch as Settings → Apps → Disable) instead of `pm uninstall`. The TV's own Settings → Apps page can re-enable packages even without the laptop.
- **Closed-loop verification through the device's own UI.** Key events plus screenshots give the agent ground truth on a device with no test harness.
- **Order of operations for Home.** Install and confirm the new launcher before disabling the stock one, otherwise HOME can land on a factory-test app or crash-loop. CleanYourTV's scripts enforce this ordering.
- **Agent approval prompts are the safety boundary.** The reel's closing advice: the agent asks before each command, read it before pressing yes.

## What to adopt

The reusable shape is device-agnostic: inventory → categorise → human selects → reversible apply → screenshot verify → scripted restore. It applies to any ADB-reachable Android device and, more generally, to agent-driven configuration of hardware the user owns where a non-destructive toggle exists.

Constraints and risks the source reports:

- Works on Android TV and Google TV only; Samsung Tizen, LG webOS and Roku have no ADB. Fire TV supports the debloat half but will not hand HOME to a third-party launcher.
- One user bricked their TV. Disabling the wrong system package can break Home or HDMI input.
- Whatever is disabled is gone until restored, including voice search and system updates.
- Gains on 1 GB RAM TVs may be small.
- Turn USB and network debugging off when finished; network ADB on port 5555 is plaintext.

## Security

- The pattern grants a coding agent a shell on a consumer device via the one-time ADB authorisation. The agent's per-command approval prompt is the only review step unless the user adds one.
- Network ADB is unauthenticated beyond the initial pairing and unencrypted on the LAN; the source and both cited repos say to disable it afterwards.
- Reversibility depends on the backup being taken first and on not writing to `/system`; the cited repos document that a factory reset remains the fallback.
- The reel is sponsored content from an animation account; the technical claims align with the two cited repos' READMEs, which were fetched directly for the companion entries.

## Usage notes

- Samsung Tizen TVs have no ADB and no screenshot API, so an agent-driven debloat/launcher session there substitutes the TV's own local remote-control API for ADB and a phone pointed at the screen for the screenshot-pull verification step: the agent stood up a small local web server, generated a QR code to pair a phone as a camera taking photos of the TV every 4 seconds, and used that as its only visual ground truth through an 11-hour, ~14M-read/1.5M-write-token Claude Code (Opus 5.5) session (source: https://www.reddit.com/r/ClaudeAI/comments/1xbj7jr/i_used_claude_to_fix_my_samsung_tv/; see also the resulting repo entry [[glass-home-samsung-tv]], whose own `tools/phonecam.py` documents the same substitution)
