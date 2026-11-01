---
name: flectar-mail
title: Flectar Mail
url: https://github.com/flectar/mail
category: framework
summary: "Native Rust email, calendar, and contacts client marketed on low memory use (README: as little as 80 MB RAM) and a no-WebView, no-script HTML rendering pipeline (Blitz); pre-release, AGPLv3."
tags:
  - email-client
  - rust
  - native-app
  - desktop
  - mobile
  - calendar
  - contacts
  - jmap
  - imap
  - local-first
  - privacy
  - agplv3
reviewed: 2026-10-30
acquired: 2026-10-30
license: AGPL-3.0
security_flags:
  - pre-release-unstable
  - experimental-html-renderer
  - processes-email-content
  - optional-oauth-credentials
  - unsigned-or-unnotarized-builds
overlaps: []
source: instagram
source_url: https://www.instagram.com/reel/DewW-AwCHKS/
---

## What it does

Flectar Mail is a native desktop/mobile client for email, calendars, and contacts, built in Rust. It connects to Gmail, Outlook/Microsoft 365, and standards-based IMAP, POP3, SMTP, JMAP, CalDAV, and CardDAV accounts, stores mail and calendar data locally for offline access, and targets low memory use — the README states "as little as 80 MB of RAM" (note: the Instagram reel that surfaced this tool claimed 20 MB; the project's own README gives the 80 MB figure, which this entry uses as the authoritative source).

Its defining architectural choice is rendering email HTML/CSS through Blitz, a Rust HTML/CSS renderer from the Dioxus team, instead of embedding a browser engine or WebView. Email scripts are not executed, and remote images are blocked by default to prevent tracking pixels. This renderer is explicitly called out as experimental — complex or unusual markup/CSS may not render correctly yet.

Other features: file/attachment browsing over JMAP/WebDAV with PDF/image/text preview; per-account signatures with separate new-message/reply defaults; desktop OpenPGP/MIME signing and encryption via an installed GnuPG 2.x plus pinentry (S/MIME and mobile OpenPGP are not supported); conversation threading with full keyboard navigation; browser-style tabs that persist per-tab scroll position and open item; named account profiles with per-profile colors; light/dark themes with custom color palettes; a frameless-window option; and storage/backup tooling including mbox/.eml/maildir export and import from Thunderbird, K-9 Mail, and Apple Mail.

## Assessment

Flectar Mail is pre-release software (its own README states it is "currently in development and is not yet stable") distributed only as GitHub pre-release builds for Linux (AppImage/.deb/.rpm/Flatpak preview), Windows (unsigned), macOS (ad-hoc signed, not notarized), and Android. Google and Microsoft OAuth verification for the app is still in progress; builds without bundled OAuth app keys disable Gmail/Outlook sign-in unless the user supplies their own OAuth app registration, so IMAP/POP3/JMAP are the only sign-in paths guaranteed to work out of the box.

The core differentiator — a from-scratch Rust HTML/CSS renderer instead of a WebView — is also its biggest open risk: the project calls it "new territory" and expects rendering issues, and the maintainers note they carry several unmerged patches on top of Blitz. This trades mature HTML compatibility for a smaller attack surface (no embedded browser engine, no script execution) and lower memory footprint.

License is AGPLv3, and the project is released under a single edition with no separate paid tier.

## Mechanical details

Build from source with the Rust toolchain:

```
cargo run --bin flectar-mail
```

Pre-release downloads come from GitHub Releases (look for the Pre-release badge). Linux installs: `sudo dnf install ./flectar-mail-<version>-linux-x64.rpm` (Fedora 43/44) or `flatpak install --user ./flectar-mail-<version>-linux-x64.flatpak`, then `flatpak run com.flectar.mail`. Each release ships SHA256SUMS and signed build-provenance attestations, verifiable with `gh attestation verify <download> --repo flectar/mail`.

Desktop OAuth goes through the system browser via the desktop portal and stores refresh credentials in the freedesktop Secret Service (e.g., GNOME Keyring); release builds refuse to open the OAuth page if no secure credential store is available. UI is built with the Slint toolkit; email HTML/CSS rendering uses Blitz (Dioxus team).

## Security

- `pre-release-unstable`: No stable release exists yet; only pre-release builds are published.
- `experimental-html-renderer`: Email HTML/CSS rendering via Blitz is explicitly flagged by the project as experimental, with patches not yet upstreamed.
- `processes-email-content`: Full mailbox content (mail, calendar, contacts) is synced and stored locally on-device; data is not routed through a third-party processing service, but local storage/backups contain full message content and OAuth/IMAP credentials (held in the system keyring).
- `optional-oauth-credentials`: Gmail/Outlook sign-in requires either bundled or user-supplied OAuth app credentials; IMAP/POP3/JMAP accounts avoid OAuth entirely.
- `unsigned-or-unnotarized-builds`: Windows pre-release builds are unsigned and macOS builds are ad-hoc signed but not notarized, so OS security prompts are expected on install.

Positive security-relevant design choices from the README: remote images blocked by default (anti-tracking), no email-script execution, no WebView/embedded browser engine for message content, and release provenance attestations for downloads.
