---
name: rea
title: REA (Reverse Engineer Anything)
url: https://github.com/morluto/rea
source_url: https://github.com/morluto/rea
category: mcp-server
summary: Open-source MCP server and CLI (npm package rea-agents) that connects coding agents (Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and others) to reverse-engineering tooling — native binaries, JavaScript/Electron apps, .NET assemblies, Android APKs, websites, firmware, packet captures, and dozens of other artifact types — so an agent can inspect a target's behavior without its source and return pseudocode/evidence the agent uses to explain a feature or reimplement it. Setup (`npx rea-agents setup`) registers the MCP server and workflow instructions for the chosen agent(s), writing to `~/.claude.json` and copying skill files into `~/.claude/skills` (applies to future projects, not just the current one). Deep native-binary analysis needs a caller-supplied Hopper, Ghidra, IDA, or Kuna installation (setup can install Hopper with approval); static JS/.NET/APK inspection needs no native engine. Requires Node.js 22.23.4+/24.22.1+/26.12.1+ and npm; many per-target features need their own external tool (JADX+JDK, Apktool, adb, tshark, sigrok-cli, pwntools, mitmdump, WABT). Repo created 2026-04-14, single primary maintainer (1,566 commits as of review), MIT license for REA-authored code (third-party dependencies and commercial decompilers like IDA/Hopper/JEB keep their own licenses and require the user's own authorization). Went viral in October 2026 —
tags:
  - reverse-engineering
  - mcp-server
  - cli
  - binary-analysis
  - ghidra
  - hopper
  - ida
  - android-apk
  - electron
  - dotnet
  - firmware-analysis
  - claude-code
reviewed: 2026-10-29
acquired: 2026-10-29
overlaps: []
license: MIT
security_flags:
  - "Dual-use reverse-engineering tool: disclaimer limits intended use to lawful research, education, interoperability, software preservation, and analysis of software the user owns or is authorized to examine; does not prevent unauthorized use"
  - "Copycat/trojan risk from its own virality: a fake 'rea-tools' org distributed an 82.6MB Windows executable flagged as Wacatac-family malware (8/45 VirusTotal engines) before takedown, downloaded 172 times (discovered 2026-10-13); official distribution is only github.com/morluto/rea, rea.tools, or the npm package rea-agents"
  - Setup writes persistent global agent configuration (~/.claude.json, ~/.claude/skills) affecting all future projects for the chosen agent, not just the current one
  - Project's own SECURITY.md states REA is not a sandbox and cannot protect against a malicious target process during runtime capture (process behavior capture, website/Electron analysis run the target using the user's own permissions)
source: web
---

## What it does

REA ("Reverse Engineer Anything") is an MCP server and terminal CLI that gives a coding agent an investigation workflow for understanding how an existing app, binary, or website implements a feature, without needing its source. The agent asks about a target (an installed app, a binary, a URL); REA inspects it with the matching analysis tool, traces the relevant code, and returns findings together with their supporting evidence and stated limitations; the agent uses that to explain the behavior or write and test a reimplementation. The same operations are callable directly from the terminal as `rea <command>`.

Target coverage is broad: native binaries (via a caller-supplied Hopper, Ghidra, IDA, or Kuna), JavaScript/Electron apps, .NET assemblies, Android APKs/signatures/devices, websites, HAR/SAZ network captures, Go/Rust binaries, GPU code objects (CUDA/HIP), model files (GGUF/safetensors), Godot PCK, IL2CPP metadata, firmware (Binwalk/Unblob), packet captures (tshark), and more — each with its own built-in static parser or a required external tool. It can also turn a recorded web-app session (HAR) into a runnable RL (reinforcement learning) environment for the AgentEnv framework.

## Mechanical details

- Install/update: `npx rea-agents setup` registers the MCP server and matching workflow instructions for the selected agent(s) (Claude Code, Codex, Cursor, Gemini CLI, Grok Build, others via manual MCP registration); `rea update` / `npx rea-agents@latest setup` refresh an existing install. Global install: `npm install --global rea-agents`.
- Static JavaScript/Electron and .NET inspection need no native analysis engine; deep native-binary decompilation needs an existing Hopper, Ghidra, IDA, or Kuna license/install (setup can install Hopper with user approval).
- Requires Node.js 22.x (>=22.23.4), 24.x (>=24.22.1), or 26.12.1+, and npm. Per-target features add their own external-tool requirement (JADX+JDK for APKs, Apktool for Android resources, adb for devices, tshark/sigrok-cli/pwntools for captures, mitmdump, WABT for WASM).
- Repo created 2026-04-14; single primary maintainer (1,566 commits as of review). npm package rea-agents reached v6.5.0+ by mid-October 2026 with frequent releases; reported MCP tool counts vary by version (126 vs 207 across sources) because of this release pace.
- Virality: #1 on GitHub Trending in October 2026; npm reports 231,579 downloads of rea-agents for the week of 2026-10-06 to 2026-10-12. The project's README separately reports 400,000 GitHub stars (self-reported, not independently re-verified here).

## Security

MIT license for REA-authored code; bundled/required third-party tools (including commercial decompilers IDA/Hopper/JEB) keep their own licenses, and REA grants no license, key, or activation for them. The project's disclaimer scopes intended use to lawful research, education, interoperability, software preservation, and analysis of software the user owns or is authorized to examine, and explicitly excludes license/DRM/anti-cheat circumvention — the tool itself does not enforce this. Its own SECURITY.md states REA is not a sandbox and cannot protect against a malicious target process during runtime-capture operations (website, Electron, process-behavior capture all run the target under the user's own OS permissions). The project's rapid popularity drew a copycat: a fake "rea-tools" GitHub org distributed a Windows executable (82.6MB) flagged by 8 of 45 VirusTotal engines as Wacatac-family trojan malware before detection and takedown (discovered 2026-10-13, 172 downloads); the real README now warns that only github.com/morluto/rea, rea.tools, and the npm package rea-agents are official. Setup (`npx rea-agents setup`) writes persistent configuration into the user's global agent config (`~/.claude.json`) and copies skill files into `~/.claude/skills`, affecting future projects for that agent, not just the current one.