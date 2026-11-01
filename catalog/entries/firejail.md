---
name: firejail
title: Firejail
url: "https://github.com/netblue30/firejail"
category: cli-tool
summary: "SUID Linux sandbox in C — restricts untrusted applications via namespaces, seccomp-bpf, capabilities, and optional Landlock/AppArmor/SELinux; 1,300+ bundled per-application profiles, desktop integration via firecfg, no daemon; GPL-2.0, ~7.6k stars, actively maintained since 2015"
tags: [sandbox, linux, security, namespaces, seccomp, landlock, apparmor, isolation, suid]
reviewed: 2026-09-10
acquired: 2026-09-10
license: GPL-2.0
security_flags: [suid-root-binary, cve-history]
overlaps: [bubblewrap-containers]
source: unknown
---

## What it does

Firejail is a lightweight Linux sandbox for running potentially untrusted applications in a restricted environment. It is an SUID program that gives a process and its descendants a private view of shared kernel resources (network stack, process table, mount table) using Linux namespaces, seccomp-bpf syscall filtering, and capability dropping. It integrates with AppArmor, SELinux, and cgroups, and has experimental Landlock LSM support (`--landlock` flags) for unprivileged filesystem restriction.

Usage is prefix-style: `firejail /usr/bin/firefox`. It sandboxes servers, GUI applications, and even login sessions. `sudo firecfg` integrates it into the desktop by symlinking supported applications so launchers transparently run sandboxed — over 900 applications are covered by default, with 1,342 bundled security profiles in `/etc/firejail/`.

## Differentiators

- No daemon, no socket, no configuration database — all enforcement is kernel-native; written in C with virtually no dependencies, runs on any Linux 3.x+ kernel.
- The profile library is the moat: 1,300+ curated per-application profiles with layered includes (disable-common, whitelist-var, dbus filtering, `net none`, private-bin/etc/tmp, memory-deny-write-execute).
- Profile statistics tool (`profstats`) quantifies hardening coverage across the profile set.
- Landlock support (kernel 5.13+) adds irreversible unprivileged filesystem self-restriction on top of the namespace sandbox; enabling it forces No New Privileges.

## Mechanical details

- Install: distro packages (Debian/Ubuntu users pointed at the latest release .deb or source builds because distro versions lag; historic example — Ubuntu 20.04 shipped vulnerable to CVE-2021-26910 for months), `mkdeb.sh`/`mkrpm.sh` build scripts, AUR `firejail-git`.
- Run: `firejail <full path to program>`; `firejail --list` shows active sandboxes; `firecfg --fix-sound` + `sudo firecfg` for desktop integration; `sudo firecfg --clean` before uninstall.
- Landlock example: `firejail --landlock --landlock.read=/media --landlock.proc=ro /usr/bin/mc`.
- C, GPL-2.0, ~7.6k stars, 675 forks, 523 open issues; created 2015, pushed same day as review (active); latest release 0.9.80, dev 0.9.81; CI on GitHub Actions, GitLab, and Debian salsa.

## Security

- **License:** GPL-2.0 — copyleft; relevant only if redistributing modified binaries.
- `suid-root-binary` — firejail runs SUID root by design; its own attack surface has historically been a target (privilege-escalation CVEs including CVE-2021-26910 and the 2022 CVE-2022-31214 local root class). A SECURITY.md documents supported versions and reporting.
- `cve-history` — multiple past CVEs; the project's own README warns that distro-packaged versions can remain vulnerable long after upstream patches, and recommends the latest release.
- Mature single-maintainer-led project (netblue30) with a large contributor base, active CI on three platforms, and 10+ years of history.