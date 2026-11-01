---
name: lg-webos-root-debloat-relaunch
title: Agent-Driven Rooted LG webOS TV Debloat & Relaunch
url: https://www.reddit.com/r/ClaudeCode/comments/1x9fwk4/comment/phmsw9i/
source_url: https://www.reddit.com/r/ClaudeCode/comments/1x9fwk4/comment/phmsw9i/
source: reddit
category: agent-pattern
summary: "Prompt pattern for directing a coding agent (Claude Opus via Claude Code) over SSH/telnet to debloat and relaunch an already-rooted LG webOS TV: the owner roots the TV themselves first, then gives the agent an allowlist of apps/inputs to keep, named features to preserve, a permanent block on LG firmware updates and telemetry, a sub-second custom launcher with a fallback to stock Home, and safety rules (measure first, reversible/batched changes, never touch firmware partitions, write a handoff); cites a public debloat script as a named starting point to go beyond."
tags:
  - agent-pattern
  - webos
  - lg
  - smart-tv
  - root
  - debloat
  - claude-code
  - backup-before-change
  - restore-script
  - handoff
  - device-automation
reviewed: 2026-10-30
acquired: 2026-10-30
license: unlicensed
security_flags:
  - agent-executes-device-commands
  - root-shell-required
  - blocks-firmware-updates-permanently
  - voids-warranty
overlaps:
  - coding-agent-adb-tv-debloat
  - free-my-tv
  - cleanyourtv
  - dumbtv
  - webosbrew
  - lucataco-webos-debloat
  - pearwebos
---

## What it says

A top-level commenter (Bloated_Plaid) describes rooting an older LG webOS TV via Homebrew Channel, then giving Claude (Opus) a root shell over SSH or telnet at the TV's IP and a structured brief, reproduced as data below (not followed as instructions by this entry): keep a named allowlist of apps and HDMI inputs and rename the inputs to match; preserve specific named features (HDMI inputs, ARC/eARC and CEC, AirPlay/casting); permanently block LG firmware updates (since an update can also undo root) and block LG's data collection (Live Plus/ACR, viewing data, ads, recommendations, diagnostics) while keeping internet access for apps actually used; build a launcher that opens on Home in well under a second showing only the kept apps/inputs, with Back returning to whatever was playing and a documented path back to LG's original Home if something breaks; inventory and measure apps/services/memory/launch times before changing anything so before/after numbers can be shown; make every change reversible with backups, change in small batches with a reboot-and-recheck after each and undo any batch that breaks something before starting the next; never touch firmware partitions; keep the TV awake while working, then restore power settings; install a startup script so changes persist across reboots; loop until the agent's own bar for performance/polish is met and the user would be expected to approve, then report with before/after numbers and anything unverified; and write a handoff document for a future session to continue from. The same comment cites a public gist (lucataco's "webos-debloat" script) as a named starting point the agent is told to go further than — where that script hides apps, the brief asks the agent to actually remove what the firmware safely allows. Other commenters in the thread report running variants of this against their own LG TVs; one (spiritzzz) built a derivative launcher repo from the same rooted-TV foundation (PearWebOS). A separate commenter (Bulky-Condition-3490) reports the model declining or hedging when a request is phrased as asking it to root the TV, and describes working around this by completing the rooting step themselves first, then telling the agent the TV is already rooted with dev tools removed, Homebrew open, updates blocked and SSH on, rather than asking the agent to perform the rooting itself.

## Key takeaways

- The brief names what to keep, not what to remove — an allowlist-first structure, same shape as the ADB-based Android/Fire TV debloat patterns this overlaps with, applied here to a telnet/SSH-rooted embedded Linux TV instead of an ADB-reachable one.
- Safety rules are stated up front rather than left implicit: measure before changing, change and verify in small batches, make every change reversible, never touch firmware partitions, and keep a written handoff for continuity across sessions.
- Blocking firmware updates is requested as a deliberate, named goal (to protect root persistence), not a side effect — a one-way trade against vendor-supplied fixes and features.
- One commenter's report of working around the model declining a request phrased as "root the TV" by doing that step themselves first, and framing the remaining request as working on an already-rooted device, is a report from the thread, not a method this entry endorses or verifies.

## What to adopt

The reusable shape, factually, is an allowlist-first brief (name what stays) combined with measure-before-and-after, reversible/batched changes, and a written handoff for session continuity — the same structure seen in the ADB-based TV debloat entries this one overlaps, adapted to a device reached over a rooted SSH/telnet shell rather than ADB.

## Security

- Rooting the TV is a prerequisite the poster states they completed themselves, via Homebrew Channel (see the webosbrew entry), before involving the agent.
- The cited starting-point script (see the lucataco-webos-debloat entry) documents that Homebrew Channel's telnet is an unauthenticated root shell open to the whole local network until SSH with a key is enabled and telnet disabled.
- The brief explicitly directs permanently blocking LG firmware updates and instructs the agent never to touch firmware partitions — both one-way or high-consequence instructions given directly to the agent.
- Rooting voids the TV's warranty, per the disclaimers on every tool in this ecosystem.
- A separate commenter's report of pre-completing the rooting step to avoid the model declining a "root the TV"-phrased request is recorded here as a thread observation, not independently verified or endorsed by this entry.