---
name: netscanner
title: netscanner
url: "https://github.com/Chleba/netscanner"
category: cli-tool
summary: "Rust TUI network scanner and diagnostic tool — lists hardware interfaces, WiFi scanning with signal strength charts, IPv4 CIDR ping with hostname/OUI/MAC resolution, TCP/UDP/ICMP/ARP packet dump with pause/filter, open port scanning, traffic counting with DNS records, CSV export; requires root; built on Ratatui + libpnet; Linux/macOS/Windows (Npcap); MIT, ~1.8k stars"
tags: [rust, tui, network, scanner, packet-capture, wifi, port-scanner, diagnostics, security, ratatui]
reviewed: 2026-09-26
acquired: 2026-09-26
overlaps: []
license: MIT
security_flags: [requires-root]
source: unknown
---

## What it does

A terminal-based network scanner and diagnostic tool written in Rust using Ratatui for the TUI and libpnet for packet capture. Provides multiple network inspection capabilities in a single interface:

- **Interface listing**: enumerates hardware network interfaces, allows switching active interface for scanning and packet dumping.
- **WiFi scanning**: discovers nearby WiFi networks with signal strength visualization (charts).
- **IPv4 CIDR ping**: scans a subnet range, resolving hostname, OUI vendor, and MAC address for each discovered host.
- **Packet dump**: captures and displays TCP, UDP, ICMP, ARP (IPv4) and ICMP6 (IPv6) packets with start/pause control and log filtering.
- **Port scanning**: TCP open port scanning against discovered hosts.
- **Traffic counting**: tracks traffic volume with DNS record resolution.
- **CSV export**: exports scanned IPs, ports, and packets to CSV files (default path: user's `$HOME` directory).

## Installation

Available via `cargo install netscanner`, Arch Linux (`pacman -S netscanner`), and Alpine edge (`apk add netscanner`). On Windows, requires Npcap for packet capture (otherwise `packet.dll` error). Must be run with root/sudo privileges. Post-install, the binary can optionally be given setuid permissions (`chown root:user` + `chmod u+s`) to avoid running the shell as root. ~1.8k GitHub stars, 36k+ crates.io downloads across 28 versions, latest v0.6.43 (July 2026).

## Mechanical details

Built on Ratatui (TUI framework) and libpnet (cross-platform packet capture). ~5,700 lines of Rust across 34 files. Demo recordings use VHS tapes. 13 contributors.

## Security

MIT licensed. Requires root privileges for packet capture — the primary security consideration. On Linux, can use setuid bit to limit root exposure. On Windows, depends on Npcap (third-party packet capture library). The tool performs passive and active network scanning, which should only be used on networks the operator controls or has authorization to scan.

## How to use it

cargo install netscanner
