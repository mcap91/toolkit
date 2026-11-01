---
name: kde-connect
title: KDE Connect
url: https://kdeconnect.kde.org
category: cli-tool
summary: Free, open-source app (GPLv2/v3) that pairs a phone and computer over the same local Wi-Fi network for direct device-to-device sync — no account, no cloud relay, no vendor servers in the data path; shared clipboard, instant file/link/SMS transfer, phone-as-touchpad/presentation-remote, and browsing phone storage over SFTP; official Linux/Android support plus Windows (Microsoft Store or .exe) and macOS (Homebrew cask) builds, with a more limited native iOS app
tags:
  - kde-connect
  - device-sync
  - clipboard-sync
  - file-transfer
  - cross-platform
  - android
  - linux
  - windows
  - macos
  - local-network
  - open-source
reviewed: 2026-10-29
acquired: 2026-10-29
license: GPL-2.0-or-later
security_flags: []
overlaps: []
source: instagram
source_url: https://www.instagram.com/reel/DeupHCKFS7F/
---

## What it does

KDE Connect pairs a phone and a computer over the same local Wi-Fi network so they can exchange data directly, without an account, a cloud relay, or a vendor server in the middle. Once paired, it provides a shared clipboard (copy on one device, paste on the other), instant file and link transfer, notification sync with the ability to read/reply to Android notifications and SMS from the desktop, remote control of Linux media players, a virtual touchpad/keyboard mode, a presentation-remote mode, running shell commands on the computer from the phone, and browsing the phone's filesystem from the computer over SFTP.

The project originates from KDE and targets Plasma/Linux as the primary platform; the Android app is the reference mobile client. Non-KDE desktop environments get KDE Connect's protocol through separate client implementations: GSConnect for GNOME Shell, Valent for GTK4/libadwaita desktops, Soduto for macOS, and Konnect as a headless server.

## Differentiators

- Fully local/offline operation: devices communicate directly over LAN (or via a self-hosted relay for remote use), so no third party handles clipboard or file data.
- Broad plugin surface beyond clipboard/file sync — SMS, run-commands, media control, touchpad/keyboard, presentation remote, find-my-phone — in one pairing.
- Cross-desktop ecosystem of independent client implementations (GSConnect, Valent, Soduto) built on the same open KDE Connect protocol.

## Mechanical details

- Desktop: official builds for Linux (native KDE package), Windows (Microsoft Store or `.exe` installer from kdeconnect.kde.org), and macOS (`brew install --cask kde-connect`, or nightly builds).
- Mobile: Android app on Google Play/F-Droid; a native iOS app exists but exposes a reduced feature set due to Apple platform restrictions.
- Pairing happens automatically for devices on the same Wi-Fi network; no account creation or sign-in step.
- License: GPL-2.0-or-later / GPL-3.0 (dual-licensed across the codebase); maintained under the KDE project (`KDE/kdeconnect-kde` on GitHub, ~4.1k stars).

## Security

- **License:** GPLv2/GPLv3 — copyleft, standard for KDE projects.
- No cloud account or server dependency for core operation reduces third-party data exposure; traffic stays on the local network unless a relay is configured.
- Remote-command execution and SMS access plugins mean a compromised or maliciously paired device has a meaningful control surface over the other device — pairing confirmation is the main safeguard, so it should only be accepted for trusted devices on a trusted network.
- No CVE history reviewed as part of this entry; not independently audited here.