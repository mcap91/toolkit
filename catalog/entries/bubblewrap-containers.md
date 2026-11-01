---
name: bubblewrap-containers
title: Bubblewrap (containers)
url: "https://github.com/containers/bubblewrap"
category: cli-tool
summary: "Low-level unprivileged Linux sandboxing tool using user namespaces — used by Flatpak, creates empty mount namespaces with selective filesystem binding; C, LGPL-2.0+, mature and auditable"
tags: [sandbox, linux, security, namespaces, isolation]
reviewed: 2026-06-23
acquired: 2026-06-23
license: LGPL-2.0+
security_flags: [linux-only]
overlaps: []
source: unknown
---

## What it does

Bubblewrap (`bwrap`) is a low-level sandboxing tool that creates new Linux mount namespaces where the root is on an invisible tmpfs, then lets you selectively bind-mount host filesystem paths into the sandbox. It uses unprivileged user namespaces (no setuid required) and provides:

- **Mount namespace isolation**: Empty root tmpfs with selective `--ro-bind`, `--bind`, `--symlink`
- **User namespace** (CLONE_NEWUSER): Hides all but current uid/gid
- **PID namespace** (CLONE_NEWPID): Sandbox sees no outside processes; built-in pid1 reaper
- **Network namespace** (CLONE_NEWNET): Loopback only, no host network
- **IPC/UTS namespaces**: Isolated shared memory and hostname
- **Seccomp filters**: Limit allowed syscalls
- **PR_SET_NO_NEW_PRIVS**: Prevents setuid escalation from within sandbox

Used by Flatpak, rpm-ostree, and bwrap-oci. The tool itself is not a complete sandbox — it provides the primitives; the calling program defines the security policy via command-line arguments.

## Assessment

Bubblewrap is the gold standard for unprivileged Linux sandboxing. Its small codebase (~few thousand lines of C) makes it auditable, and its design philosophy of providing primitives rather than policies is sound. Relevant for agent sandboxing on Linux: you could wrap agent-executed commands in `bwrap` to restrict filesystem/network access without Docker overhead.

The limitation is that it's Linux-only (requires kernel user namespaces) and policy-free — you must compose the right `bwrap` arguments yourself. Not useful on Windows/macOS, but directly relevant for Linux-based CI, containers, or headless agent servers.

## Mechanical details

```bash
# Install (most Linux distros have it packaged)
sudo apt install bubblewrap    # Debian/Ubuntu
sudo dnf install bubblewrap    # Fedora

# Example: shell with read-only /usr, no network, isolated PIDs
bwrap --ro-bind /usr /usr --symlink usr/lib64 /lib64 \
      --proc /proc --dev /dev --unshare-pid --unshare-net \
      --new-session bash
```

Build from source: `meson _builddir && meson compile -C _builddir && meson install -C _builddir`

## Security

- **License**: LGPL-2.0+ — permissive for dynamic linking
- **Codebase**: Small C, purpose-built for auditability
- **CVE history**: CVE-2017-5226 (TIOCSTI escape) mitigated by `--new-session`; maintainers proactively document limitations
- **No setuid**: Removed legacy setuid mode; relies entirely on unprivileged user namespaces
- **Policy responsibility**: Bubblewrap itself is not a security policy — whatever constructs the bwrap command line is responsible for the sandbox's actual security guarantees