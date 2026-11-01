---
name: landlock-lsm
title: Landlock LSM (org and ecosystem)
url: "https://github.com/landlock-lsm"
category: reference
summary: "GitHub org for Landlock, the Linux security module (kernel 5.13+) letting unprivileged processes irreversibly restrict their own filesystem/network access — hosts rust-landlock and go-landlock libraries, the island CLI sandboxing tool (Rust, Apache-2.0), landlockconfig, kernel dev tree, test tools, and the landlock.io site"
tags: [landlock, linux, sandbox, lsm, kernel, security, rust, go, unprivileged, isolation]
reviewed: 2026-09-10
acquired: 2026-09-10
license: MIT
security_flags: []
overlaps: [firejail, bubblewrap-containers]
source: unknown
---

## What it does

Landlock is a Linux Security Module (mainlined in kernel 5.13, 2021) that lets **unprivileged** processes create sandboxes restricting their own access to the filesystem (and, in newer kernel versions, network and IPC scopes). Restrictions are stackable, inherited by all children, and can never be removed once applied — a process opts itself in, requiring either `CAP_SYS_ADMIN` or the No New Privileges flag. It is the kernel-native building block that tools like Firejail (`--landlock`) and various agent sandboxes wrap.

The `landlock-lsm` GitHub org hosts the ecosystem:

- **rust-landlock** — Rust library for the Landlock API (used by other sandboxing tools); actively updated
- **go-landlock** — Go library (MIT, ~360 stars)
- **island** — a standalone CLI sandboxing tool powered by Landlock (Rust, Apache-2.0, ~324 stars): run a command under a filesystem-restricted policy without containers or root
- **landlockconfig** — declarative Landlock policy configuration format (in development)
- **linux** — kernel development tree for the LSM itself
- **landlock-test-tools**, **workshop-imagemagick** — testing and tutorial material
- **landlock-lsm.github.io** — the landlock.io documentation site

## Differentiators

- Unprivileged and irreversible by design: no SUID binary (unlike Firejail), no daemon, no user-namespace requirement (unlike bubblewrap's typical setup); enforcement lives in the kernel LSM stack.
- Sandboxing is opt-in from inside the program — designed for developers to harden their own applications, not only for wrapping others' binaries (island covers the wrapper case).
- Feature availability is kernel-version-gated (ABI versions): filesystem rules from 5.13, network TCP rules from 6.7, IPC scoping later — libraries expose best-effort degradation.

## Mechanical details

- Program self-sandboxing: create a ruleset with allowed access rights per path (`landlock_create_ruleset`, `landlock_add_rule`, `landlock_restrict_self` syscalls); rust-landlock/go-landlock wrap these with ABI-compatibility helpers.
- CLI use: `island` runs a command under a policy; Firejail integrates via `--landlock*` flags.
- Maintained by the kernel Landlock maintainer (Mickaël Salaün); org repos updated through Aug 2026.

## Security

- Licenses vary per repo: go-landlock MIT, island Apache-2.0, test tools GPL-2.0, docs CC-BY-SA-4.0; the kernel LSM itself is GPL-2.0.
- This is upstream kernel security infrastructure with mainline review — the highest-assurance tier of Linux sandboxing primitives.
- Main practical caveat is kernel-version dependence: policies silently offer less protection on older kernels unless the library's ABI-check is used strictly.