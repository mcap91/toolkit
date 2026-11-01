---
name: ingame-debug-console
title: In-game Debug Console (UnityIngameDebugConsole)
url: https://github.com/yasirkula/UnityIngameDebugConsole
source_url: https://www.instagram.com/reel/DeuQdK6THpz/
source: instagram
category: framework
summary: yasirkula's uGUI-based in-game console for Unity — shows runtime log/warning/error/exception output and lets players or testers execute registered commands (e.g. cheats) from a resizable, minimizable window inside a running build, including on mobile/device builds where the editor console isn't available; supports Android logcat forwarding; 2.8k stars, 268 forks; MIT.
tags:
  - unity
  - debug-console
  - developer-tools
  - cheats
  - game-development
  - csharp
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags: []
overlaps: []
---

## What it does

UnityIngameDebugConsole ("In-game Debug Console") is a uGUI-based console overlay that runs inside a live Unity build (not just the editor), surfacing `Debug.Log`/warning/error/exception output and accepting typed commands at a bottom input field. Registered commands can return values (printed back to the console) and are commonly used to expose cheats or debug toggles for QA/playtesting directly on-device — e.g. testing a build on a phone where the Unity editor console isn't accessible. The console window is resizable, can be hidden/minimized to a popup indicator, and (as a "Singleton") persists across scene loads.

## Mechanical details

2.8k GitHub stars, 268 forks. On Android it can additionally forward native `logcat` output into the console (prefixed `LOGCAT:`) for device-side diagnostics. Implementation uses a recycled list view for log entries and is documented to cost only 1 SetPass draw call when sprite packing is enabled. Five install paths: import the bundled `.unitypackage`, clone/download the repo, install from the Unity Asset Store, install via Package Manager git URL, or install via OpenUPM.

## Security

MIT licensed. Local developer/QA tool — reads Unity's log stream and executes locally-registered C# methods; it does not itself open network ports or transmit data. Shipping it (and any exposed cheat/debug commands) in a public release build is a product decision for the integrating developer, not a defect in the library.

## Sources

- [GitHub: yasirkula/UnityIngameDebugConsole](https://github.com/yasirkula/UnityIngameDebugConsole) — README, feature list, license
- [Instagram reel](https://www.instagram.com/reel/DeuQdK6THpz/) — named the tool as one of eight repos used to build a Claude-assisted farm game (catalog source; no link given in the reel itself)