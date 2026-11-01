---
name: vphone-cli
title: vphone-cli
url: "https://github.com/Lakr233/vphone-cli"
category: cli-tool
summary: "Virtual iPhone on Apple Silicon Mac — uses Apple's Virtualization.framework and PCC research VM infrastructure to boot full iOS (up to iOS 27) as a VM; firmware patching, restore, and VM lifecycle management; GUI window with app/file browsing, clipboard, screenshots, recording; local HTTP/WebSocket API for automation (screenshots, touch, swipes, hardware keys); guest control daemon with Irisin package manager; macOS 15+, Apple Silicon only; MIT, ~12k stars"
tags: [ios, virtualization, apple-silicon, macos, mobile-testing, automation, api, swift]
reviewed: 2026-09-26
acquired: 2026-09-26
overlaps: []
license: MIT
security_flags: [requires-sip-modification]
source: unknown
---

## What it does

vphone-cli creates and runs virtual iPhones on Apple Silicon Macs using Apple's Virtualization.framework and PCC (Private Cloud Compute) research VM infrastructure. It boots a real iOS system image (up to iOS 27) as a full virtual machine, not an emulator.

Key capabilities:

- **VM lifecycle**: Create, launch, stop, export (backup as `.tzst`), import, and manage multiple VMs. VMs live under `~/.vphone/` by default.
- **Firmware management**: Downloads iPhone and cloudOS IPSWs from Apple's firmware catalog, applies a complete firmware patch set, handles restore tickets. Supports custom IPSW files.
- **GUI window**: App and file browsing, clipboard sync, preference tools, screenshots, screen recording, and diagnostics — all through a native macOS window.
- **Local API**: HTTP and WebSocket API on `127.0.0.1:8765` with bearer token authentication. Exposes screenshots, touch events, swipes, hardware key presses. Token rotates per launch or can be pinned via `VPHONE_API_TOKEN`. Useful for AI-driven end-to-end testing and MCP server integration.
- **Guest environment**: Bundled `vphoned` daemon in the guest provides controls used by the window and API. Irisin package manager for installing packages (apt, bash) in the guest. Bootstrap install resolves initial dependency cycles.

## Installation

Download the notarized `vphone-launchpad` app from GitHub releases. Requires physical Apple Silicon Mac running macOS 15+. No Xcode, Python, or Homebrew needed at runtime. Host setup requires running two commands in macOS Recovery: `csrutil enable --without debug` and `csrutil allow-research-guests enable` (SIP remains enabled with debugging restrictions relaxed). Launchpad's privileged helper allows each verified VM binary through AMFI.

Version 2.x only starts VMs created with its `schemaVersion=2` format — older VMs must be recreated.

## Mechanical details

Written primarily in Swift (58.6%), Objective-C (17%), Shell (11.6%), and Python (11.5%). 373 commits, 26 releases. Repository organized into `VPhoneExecutable/` (CLI, VM process, firmware patcher, restore backend), `VPhoneKit/` (shared host libraries and API client), `VPhoneDaemon/` (guest control daemon), `VPhoneGuestComponents/` (guest hooks and support binaries). ~12k GitHub stars, 1.5k forks, first commit February 2026. Rapid star growth indicates strong community interest.

## Security

MIT licensed. Requires SIP modification (`csrutil enable --without debug` + research guest allowance) — this relaxes macOS security restrictions, which is the primary security consideration. The AMFI allowlisting ensures only verified VM binaries execute. API access is token-authenticated and refuses requests from web pages. Creates substantial disk usage for firmware images. The tool leverages Apple's own Virtualization.framework rather than hardware emulation, staying within Apple's intended research VM infrastructure.

## How to use it

Download vphone-launchpad from GitHub releases
