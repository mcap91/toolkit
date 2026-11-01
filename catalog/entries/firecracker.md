---
name: firecracker
title: Firecracker
url: "https://github.com/firecracker-microvm/firecracker"
category: framework
summary: "AWS-developed open-source VMM (KVM-based) that creates minimal-overhead 'microVMs' for secure multi-tenant workload isolation — ~125ms boot, <5MiB overhead per VM; powers every AWS Lambda/Fargate invocation and underlies sandbox platforms like E2B and Vercel Sandbox; Apache-2.0, Rust"
tags: [microvm, virtualization, kvm, sandbox, isolation, vmm, aws, agent-infrastructure, code-execution]
reviewed: 2026-09-25
acquired: 2026-09-25
license: Apache-2.0
security_flags: []
overlaps: [e2b, opensandbox, ai-agent-sandbox-ranking]
source: unknown
---

## What it does

Firecracker is an open-source virtualization technology built at Amazon Web Services for secure, multi-tenant execution of container and function workloads. It provides a virtual machine monitor (VMM) that uses Linux KVM to create and run "microVMs" — lightweight VMs that combine hardware-virtualization-grade isolation with container-like speed and density.

Firecracker's design is deliberately minimal: it excludes unnecessary devices and guest-facing functionality to shrink both memory footprint and attack surface. Each microVM gets its own guest kernel, fully separated from the host, so an attacker must escape both the guest kernel and the hypervisor to reach other tenants. Firecracker was purpose-built to power AWS Lambda and AWS Fargate — every Lambda invocation runs inside its own Firecracker microVM, making it the largest known production deployment of the technology.

Control surface: a single VMM process per microVM exposes a REST-like API (OpenAPI-specified) over a Unix socket, used to configure vCPUs/memory/CPU templates, attach network interfaces and file-backed block devices, set virtio rate limiters, configure logging/metrics, attach vsock/entropy/pmem devices, manage memory hotplugging, and (x86_64 only) stop the microVM. A `jailer` process wraps Firecracker for production use, applying cgroup/namespace isolation and dropping privileges before the VMM starts.

Firecracker is a low-level primitive, not a hosted sandbox product — it has no built-in orchestration, snapshotting UI, or multi-tenant control plane of its own. Higher-level platforms build on top of it: Kata Containers and Flintlock integrate it as a container-runtime backend, and AI-agent sandbox platforms such as E2B and Vercel Sandbox (built on Vercel's internal "Hive" orchestration layer) use it as the isolation layer under their SDKs.

## Assessment

Firecracker is the reference implementation for microVM-based isolation and the de facto baseline that competing approaches (gVisor, Kata Containers, SmolVM, Microsoft LiteBox, OpenSandbox's Firecracker runtime option) get compared against. For this toolkit, it is not something to install directly — running raw Firecracker requires KVM access, a kernel/rootfs image pipeline, and a jailer/orchestration layer, which is exactly the gap that E2B and OpenSandbox (already cataloged) fill. Its relevance here is as the underlying isolation technology referenced by those entries: understanding what Firecracker actually provides (hardware-level per-tenant isolation via a dedicated guest kernel, not just namespace/cgroup separation) clarifies what "microVM sandbox" claims in agent-sandboxing marketing actually mean, and why it's treated as stronger isolation than Docker for running untrusted or AI-generated code.

Worth tracking directly only if this toolkit ever needs to self-host a sandbox layer rather than consume one through an SDK (E2B) or platform (OpenSandbox, Vercel Sandbox).

## Mechanical details

```bash
git clone https://github.com/firecracker-microvm/firecracker
cd firecracker
tools/devtool build   # requires Docker + bash; builds via a dev container
```

Binary lands at `build/cargo_target/<arch>-unknown-linux-musl/debug/firecracker`. Requires a Linux host with KVM (`/dev/kvm`) and a supplied guest kernel image + rootfs; there is no packaged installer for end users — production deployments (including AWS's own) run it behind an orchestrator. Releases published on GitHub roughly every two to three months; a "production host setup" doc in the repo covers the host-hardening configuration AWS considers necessary for multi-tenant safety.

Tested/supported host CPUs per the README: Intel (Cascade Lake through Sapphire/Granite Rapids), AMD (Milan, Genoa), and AWS Graviton 2–5, across paired host/guest kernel and rootfs combinations.

## Security

- **License**: Apache-2.0.
- **Isolation model**: Hardware-virtualization-backed microVMs via KVM — each workload gets a dedicated guest kernel, not a shared-kernel namespace/cgroup boundary. Advanced per-thread seccomp filters and a jailer (cgroup/namespace barrier + privilege drop) are built in for production use.
- **Provenance**: Developed and operated in production by AWS since before 2018 to run Lambda/Fargate; this is the largest-scale, longest-running production deployment of any microVM technology.
- **Known limitation**: The pl031 RTC device on aarch64 does not support interrupts, so guest programs relying on RTC alarms (e.g., `hwclock`) will not work.
- **Disclosure process**: Maintains a documented private security-disclosure process (`firecracker-maintainers@amazon.com`); no independent CVE history was reviewed as part of this catalog pass.
- **Not directly executable-code-safe out of the box**: Firecracker itself is a VMM primitive — safe multi-tenant operation depends on correct host configuration (the README explicitly flags this), kernel/rootfs choice, and an orchestration/jailer layer, none of which ship as a turnkey product.