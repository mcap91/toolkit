---
name: nvidia-pair
title: NVIDIA Personal AI Router (PAIR)
url: "https://www.nvidia.com/en-us/ai-on-rtx/personal-ai-router/"
category: framework
summary: "Open-source local inference router (public beta) that proxies AI app/agent requests to a single endpoint and schedules them across NVIDIA DGX Spark, RTX Windows/Linux PCs, and Apple Silicon Macs on the same LAN — infrastructure tool, not an agent/dev workflow component"
tags: [inference-routing, local-inference, llm-serving, ollama, lm-studio, rtx, dgx-spark, macos, self-hosted, proxy, nvidia, lan-discovery]
reviewed: 2026-09-25
acquired: 2026-09-25
license: Apache-2.0
security_flags: [beta-software, new-project, binds-local-network-endpoints]
overlaps: []
source: unknown
---

## What it does

NVIDIA Personal AI Router (PAIR) is a local inference router that gives AI apps and agents a single local endpoint while it routes each request to whichever compatible machine on the same LAN has capacity. It targets a household or small-office mix of NVIDIA DGX Spark units, Windows/Linux PCs with RTX GPUs, and macOS devices (Apple M4+), presenting Ollama-compatible, OpenAI-compatible, and Anthropic Messages API proxy endpoints so existing clients need no code changes to talk to it.

PAIR discovers eligible nodes on the network via mDNS, establishes trust through PIN-based pairing, and encrypts node-to-node traffic with mTLS. It tracks per-node state — which inference engines are running, which models are already loaded, current job load, and GPU utilization — and schedules each incoming request to a single eligible node. At launch it drives two backend engines: Ollama and LM Studio.

Critically, PAIR is a router, not a distributed inference runtime: it does not pool VRAM or combine GPUs across machines into one larger logical device, and it does not shard a model across nodes. A node is only a scheduling candidate if it already has the exact requested model loaded. The stated benefit is maximizing use of a household's/lab's existing idle local compute (e.g., diverting work off a machine someone starts gaming on) while keeping prompts, files, and agent context on the local network rather than sending them to a cloud API.

## Assessment

PAIR is infrastructure software — a local network proxy/scheduler daemon — rather than a skill, plugin, or agent-workflow component, so it does not map cleanly onto this catalog's `category` enum (no `infrastructure` value exists). It is filed as `framework`, the convention already used in this catalog for standalone, non-agent-specific infrastructure software (e.g. AdGuard Home, ChromaDB, Amazon Bedrock); the `infrastructure` framing from the source material is preserved in the summary text instead.

Relevance to this catalog's focus (Claude Code agent workflows, bioinformatics pipelines, LLM tooling) is closer than a typical "infrastructure, note only" entry: PAIR explicitly targets AI agent workflows and multi-device local LLM serving, which is directly applicable to anyone running local models (e.g., Ollama-backed agents) across more than one machine on a home or lab network. It is useful to know about for that scenario, but it is NVIDIA-vendor infrastructure for LAN inference scheduling, not something integrated into this toolkit's skills or subagents.

The project is very new — public beta v0.1.1, announced/released September 3, 2026 (about three weeks before this review) at IFA 2026 alongside NVIDIA's broader local-AI push. It has no long maintenance track record yet. NVIDIA's own published benchmarks (a 5-subagent Hermes Desktop + Ollama workload completing in 8m48s across a 3-device PAIR cluster vs. 18m on one RTX Spark laptop; ~1.6x speedup across two RTX 5090 PCs running Qwen3.6 35B A3B) are vendor-reported and have not been independently reproduced.

## Mechanical details

Distribution: signed installers for Windows, macOS, and Linux (x64 and arm64; Windows on ARM is experimental), downloadable from the NVIDIA product page. Full source is public at `github.com/NVIDIA/Personal-AI-Router`.

Supported hardware: GeForce RTX 20-series and newer, RTX PRO workstation GPUs, DGX Spark, and Apple M4+ silicon. RTX Spark PCs/laptops are planned once available later in the release cycle. Validated minimum configuration: 8 GB RAM, ~20 GB disk recommended.

Backend engines at launch: Ollama and LM Studio. Client-facing endpoints: Ollama-compatible, OpenAI-compatible, and Anthropic Messages API-compatible proxy endpoints, so existing OpenAI/Anthropic/Ollama SDK clients can point at the local PAIR endpoint without modification.

Building from source requires Node.js 25.5.0+, npm, Go 1.25+, jq, and Git. The system runs entirely on the local network; internet access is only needed to download models, not for routing or inference itself.

## Security

License: Apache-2.0 (permissive, source public on GitHub under `NVIDIA/Personal-AI-Router`).

Security flags:
- `beta-software`: Public beta (v0.1.1) as of this review; behavior, defaults, and security posture may change before a stable release.
- `new-project`: Released September 3, 2026 — no extended track record, third-party security audit, or CVE history exists yet.
- `binds-local-network-endpoints`: PAIR runs local HTTP proxy endpoints and LAN discovery (mDNS) on each participating machine to route agent/app traffic between nodes. Node-to-node pairing uses PIN-based trust bootstrap and mTLS encryption, which is a reasonable design, but the software should be treated as a network service and evaluated against the trust level of the local network it runs on.

No credential exfiltration, telemetry, or cloud-dependency concerns were found in the material reviewed — PAIR is explicitly positioned as local-only, with internet access limited to model downloads.
