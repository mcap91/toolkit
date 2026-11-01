---
name: usbtree
title: usbtree
url: "https://github.com/gnomeria/usbtree"
category: cli-tool
summary: "Cross-platform Rust TUI for live USB device tree inspection — enumerates hubs/devices/classes/speeds via nusb (no root, no libusb), hot-plug watch with timestamped event log, live per-device activity sparklines and bandwidth graphs (Linux), safe eject, PCI view, filter/yank; single static binary (~1.5 MB), zero runtime deps; Linux/macOS/Windows; MIT"
tags: [rust, tui, usb, hardware, device-tree, linux, macos, windows, cross-platform, cli]
reviewed: 2026-09-26
acquired: 2026-09-26
overlaps: []
license: MIT
security_flags: []
source: unknown
---

## What it does

A terminal UI for inspecting USB device trees across Linux, macOS, and Windows. Enumerates all connected USB devices via the `nusb` crate (pure Rust, no libusb dependency) and displays them in a hierarchical tree with color-coded class gutters, per-class icons, tree rails, and speed badges (low/full ▂, high 480M ▄, SuperSpeed+ 5G/10G █). Rescans every second.

Key capabilities:

- **Hot-plug detection**: plugged devices flash green, unplugged devices linger as red ghosts for 30 seconds; all events logged with timestamps.
- **Live activity metrics** (Linux only): inline sparklines showing URBs/s (unprivileged) or real bytes/s bandwidth via usbmon (requires root + `modprobe usbmon`).
- **Detail panel**: sysfs path, vid:pid, vendor name, device class, speed, bMaxPower, serial number, connected children.
- **Device names**: resolved via a fallback chain — `overrides.ids` (user-defined) → USB descriptor strings → downloaded `usb.ids` → embedded snapshot → vendor/class heuristics.
- **Safe eject** (Linux): unmounts + cuts port power via udisks2 with a confirm dialog.
- **PCI view**: flat address-sorted PCI device list with detail pane (prog-if, subsystem, link speed/width, NUMA, IOMMU group, power state).
- **Composite device classification**: Misc (0xef) class devices reclassified by interface class (e.g., a MOTU M2 shows as Audio, not Misc).
- **Utilities**: live filter (`/`), yank vid:pid (`y`) or full details (`Y`), `--dump` for non-interactive output, `--demo` for scripted fake tree.

## Installation

Available via Homebrew (`brew install usbtree`), shell installer (`curl -fsSL .../install.sh | sh`), PowerShell installer (Windows), or `cargo install --git`. Prebuilt binaries for Linux amd64/arm64, macOS arm64, Windows amd64. Installers verify sha256 against `checksums.txt`. macOS/Windows binaries are not code-signed — may require quarantine bypass or SmartScreen override. Self-update via `usbtree --upgrade`.

## Mechanical details

Config lives in `~/.config/usbtree/` (Linux/macOS) or `%APPDATA%\usbtree\` (Windows). The `overrides.ids` file allows user-defined device name overrides. `usb.ids` is updated via `--updatelist` from the systemd/hwdata mirror. Releases are automated with release-please from conventional commits. Development uses Taskfile for common commands. Demo screenshots rendered headlessly via VHS tapes.

## Security

MIT licensed. No root required for basic operation. Root required only for usbmon real bandwidth metrics on Linux (`sudo modprobe usbmon`). macOS and Windows binaries are unsigned — verify sha256 or build from source. No network access during normal operation; `--updatelist` fetches from a public GitHub mirror.

## How to use it

cargo install --git https://github.com/gnomeria/usbtree
