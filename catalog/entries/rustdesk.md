---
name: rustdesk
title: RustDesk
url: "https://github.com/rustdesk/rustdesk"
category: framework
summary: "Open-source remote desktop application (Rust core, Flutter UI) designed for self-hosting as a TeamViewer/AnyDesk alternative — end-to-end encrypted P2P with relay fallback, cross-platform (Windows/macOS/Linux incl. Wayland, iOS, Android, web), self-hostable rendezvous/relay server (hbbs/hbbr) so no traffic touches vendor infrastructure; AGPL-3.0, ~123k stars"
tags: [remote-desktop, self-hosted, rust, flutter, p2p, encryption, teamviewer-alternative, cross-platform, wayland]
reviewed: 2026-09-10
acquired: 2026-09-10
license: AGPL-3.0
security_flags: [remote-access-tool-abuse-surface]
overlaps: [remote-control]
source: unknown
---

## What it does

RustDesk is a full remote-desktop application — screen sharing, keyboard/mouse control, file transfer, clipboard sync, audio — positioned as a self-hostable alternative to TeamViewer/AnyDesk. The client is a Rust core with a Flutter UI running on Windows, macOS, Linux (X11 and Wayland), iOS, Android, plus a web client. Connections are end-to-end encrypted (NaCl-based) and go peer-to-peer when NAT allows, falling back to a relay.

The defining feature is the self-hosted server pair: **hbbs** (ID/rendezvous server) and **hbbr** (relay), both open source and runnable via Docker on a small VPS — giving full control of the signaling and relay path with no dependency on vendor infrastructure. Public rendezvous servers operated by the RustDesk company are the zero-config default.

## Differentiators

- The only mainstream-quality open remote desktop where the *entire* stack (client + signaling + relay) is self-hostable; address book and permanent-password unattended access included.
- Wayland support, hardware-accelerated codecs (VP8/VP9/AV1, H.264/H.265 where available), and adaptive quality — closer to commercial RAT polish than VNC-lineage tools.
- One of the largest OSS projects by stars (~123k) with very active maintenance (149 open issues against that scale, same-week pushes).
- Pro server (paid) layers on OIDC/2FA/ACLs for organizations; the OSS server covers core rendezvous+relay.

## Mechanical details

- Clients from rustdesk.com or GitHub releases (Flatpak, MSI, dmg, apk); server: `docker run` hbbs/hbbr, then point clients at the ID server and public key.
- Config via client settings or mass-deployment flags; unattended access via permanent password.
- Rust + Dart/Flutter, AGPL-3.0; created 2020; ~19k forks, 636 watchers; wiki + discussions; homepage rustdesk.com.

## Security

- **License:** AGPL-3.0 — strong copyleft; network use triggers source obligations for modified server deployments.
- `remote-access-tool-abuse-surface` — like all remote-desktop software, RustDesk is repeatedly abused in tech-support scams; enterprise allowlisting/blocklisting of the public rendezvous servers is common. Self-hosting with a private key removes exposure to the public network.
- E2E encryption with server-held public key verification; the self-hosted path means the operator controls key distribution.
- Established project with a company behind it; releases are signed and widely packaged (Flathub, Homebrew, winget).