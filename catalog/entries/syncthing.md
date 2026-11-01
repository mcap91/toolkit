---
name: syncthing
title: Syncthing
url: "https://github.com/syncthing/syncthing"
category: cli-tool
summary: "Mature, audited, decentralized file sync daemon — production-grade for agent artifact persistence and cross-machine data sharing."
tags: [file-sync, decentralized, p2p, self-hosted, cross-platform, golang, tls, data-safety]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MPL-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Syncthing is a continuous file synchronization daemon written in Go that keeps directories in sync across two or more computers in real time without requiring a central server or cloud intermediary. It uses a custom block-exchange protocol (BEP) over TLS 1.3, with device identities anchored to self-generated public/private key pairs — no accounts, no passwords, no third-party infrastructure required. Peers discover each other via a global discovery server (optional, can be self-hosted) and then communicate directly or via relay servers when NAT traversal fails.

The program exposes a web-based GUI on localhost and a REST/JSON API, making it scriptable and embeddable. It handles conflict resolution, file versioning (simple, staggered, or external strategies), selective sync (ignore patterns), and per-folder sharing with fine-grained read-only vs. read-write permissions. Native packages are available for Linux, macOS, Windows, FreeBSD, and ARM systems; a Docker image is also maintained. Background operation is supported via systemd units, Windows services, or launchd plists included in the repository.

For agent-toolkit workflows specifically, Syncthing is useful as the persistence and artifact distribution layer: agent output directories, model checkpoints, or shared data stores can be kept in sync across workstations, servers, and CI nodes without a cloud upload step.

## Assessment

Syncthing reaches the `adopt` bar on every axis. It has been in continuous active development since 2013, with hundreds of contributors and a sustained release cadence (tagged releases appear on a regular schedule, all GPG-signed). The protocol has received independent security audits (2017 audit by Cure53 is publicly documented). The codebase has a comprehensive test suite, CI configuration, and uses a linter — all visible in the repository structure. Release binaries are GPG-signed at the key published on syncthing.net/security, and macOS/Windows binaries carry platform code-signing as well; the built-in updater uses an ECDSA signature, so even auto-updates are cryptographically verified.

The license (MPL-2.0) is a weak copyleft that applies only to modified Syncthing source files — it imposes no obligation on code that merely uses Syncthing as a running process, which covers every normal agent-toolkit integration pattern. The project has a formal security disclosure process (security@syncthing.net) and a published security policy, with no known unpatched CVEs at time of review.

Compared to alternatives like rsync (no automatic bidirectional sync, no NAT traversal), Dropbox/Google Drive (cloud custody of data), or Seafile (requires central server), Syncthing is the only option that is fully decentralized, vendor-free, and open source while still supporting Windows natively — which matters for this toolkit's Windows-first stance.

## Mechanical details

**Install:** Download a signed release binary from https://github.com/syncthing/syncthing/releases, or use a package manager (`winget install Syncthing.Syncthing`, `brew install syncthing`, `apt install syncthing`). Docker: `docker run -d syncthing/syncthing`.

**Run:** `syncthing` — starts the daemon and opens the web GUI at http://127.0.0.1:8384 by default. On first run it generates a device ID (hash of the TLS certificate) shown in the GUI. Share the device ID with other nodes to pair them.

**Scripting/API:** The REST API at http://127.0.0.1:8384/rest/ supports folder management, device management, event polling, and status queries. An API key is auto-generated and shown in the GUI settings. Useful for agent scripts that need to trigger rescan, check sync completion, or poll for changes.

**Background service (Windows):** `syncthing --no-browser --no-restart` as a Windows Service via NSSM, or use the community SyncTrayzor GUI wrapper which installs a service automatically.

**Config file:** XML at `%APPDATA%\Syncthing\config.xml` (Windows) or `~/.local/state/syncthing/config.xml` (Linux/XDG). Ignore patterns per folder via `.stignore` files (gitignore syntax).

## Security

License is MPL-2.0 — weak copyleft, no obligations for typical integration-as-running-process use.

Security posture is strong: TLS 1.3 for all traffic, ECDSA device identity, no credentials stored on any server, optional relay-only mode to prevent direct connections. The discovery server and relay infrastructure can be self-hosted entirely. The 2017 Cure53 audit found no critical issues; findings were remediated. Release signing provides a clear chain of custody. The auto-update mechanism verifies an ECDSA signature compiled into the binary before applying any update — this is more rigorous than most tools in this category.

No security_flags warranted: the codebase does not use eval, has no credential-handling antipatterns, releases are signed, tests and CI exist, and the project is actively maintained with a published security contact.
