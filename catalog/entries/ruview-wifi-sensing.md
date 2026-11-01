---
name: ruview-wifi-sensing
title: RuView WiFi Sensing Platform
url: "https://github.com/ruvnet/RuView"
category: framework
summary: "Interesting hardware+agent integration with a Claude Code plugin and MCP server, but beta software requiring physical ESP32 hardware for core capabilities"
tags: [wifi-sensing, esp32, mcp-server, claude-code-plugin, edge-ai, vital-signs, presence-detection, iot, physiological-signals]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: [beta-software, hardware-dependent, readme-benchmark-corrections-noted]
overlaps: []
source: unknown
---

## What it does

RuView turns commodity WiFi signals into a spatial intelligence and physiological sensing platform. It uses Channel State Information (CSI) from low-cost ESP32-S3 nodes (~$9 each) to detect presence through walls, measure breathing rate (6–30 BPM) and heart rate (40–120 BPM) contactlessly, estimate 17-keypoint body pose, classify activities (walking, falls, sleep stages), and fingerprint rooms via RF reflection patterns — all on edge hardware with no cloud, no cameras, and no wearables required.

The system ships several Claude Code-adjacent components: a Claude Code plugin (`plugins/ruview/`) providing 9 skills and 7 `/ruview-*` commands for onboarding, firmware flashing, provisioning, and running sensing applications; an MCP server (`@ruvnet/rvagent`, `npx @ruvnet/rvagent stdio`) with 6 tools exposing live sensing data to AI agents (`ruview.presence.now`, `ruview.vitals.get_breathing`, `ruview.vitals.get_heart_rate`, `ruview.vitals.get_all`, `ruview.bfld.last_scan`, `ruview.bfld.subscribe`); and a Python package (`pip install ruview`) plus a Rust sensing server core. A catalog of 105 signed edge modules covers health monitoring, security, retail analytics, industrial safety, and swarm coordination.

## Assessment

**Watch** rather than pilot or adopt because:

1. **Hardware gating.** All substantive capabilities — through-wall sensing, vital signs, pose estimation — require physical ESP32-S3 nodes. The Docker image runs on simulated data only, limiting evaluation without a hardware purchase.
2. **Beta status with known gaps.** The README explicitly documents that the JSONL model format is not yet accepted by the live sensing server (`--model` flag errors with invalid magic), causing silent degradation to null output rather than heuristic fallback. Camera-free pose accuracy is acknowledged to be low (PCK@20 ~2.5% with proxy labels).
3. **Benchmark credibility is mixed but improving.** The README retracted an earlier "100% presence" single-class artifact and replaced it with an honest 82.3% held-out temporal-triplet figure — this transparency is a positive signal. However, SOTA claims on MM-Fi are self-reported on an "AetherArena" leaderboard maintained by the same author.
4. **Claude Code integration is genuinely novel.** The `/ruview-*` slash commands and `@ruvnet/rvagent` MCP server represent a real pattern for hardware-tethered AI agents, which is worth tracking as a design reference even if the hardware overhead is prohibitive for most users.
5. **Bioinformatics adjacency.** RuView's physiological signal pipeline (breathing, heart rate, sleep stage, gait analysis) is adjacent to research and clinical monitoring workflows where contactless sensing could replace wearables, but the current implementation targets smart home and commercial verticals more than research tooling.

## Mechanical details

- **Hardware**: ESP32-S3 (~$9/node) for CSI capture; optional Cognitum Seed ($140 appliance) adds persistent vector store, kNN search, and Ed25519 witness chain.
- **Firmware**: ESP-IDF, flashed via `esptool`. Supports ESP32-C6 (WiFi 6) as a research node.
- **Software stack**: Rust core (`wifi-densepose-sensing-server`), Python SDK (`ruview`/`wifi-densepose`, PyO3 wheels, `abi3-py310`, Linux/macOS/Windows), Node.js scripts for RF scanning and SNN processing.
- **ML models**: Pretrained on Hugging Face at `ruvnet/wifi-densepose-pretrained` (128-dim contrastive encoder, 4-bit quantized, 8 KB); pose model at `ruvnet/wifi-densepose-mmfi-pose`. Models fit in 8–55 KB on ESP32.
- **MCP server**: `npx @ruvnet/rvagent stdio` or HTTP (POST /mcp, Origin-validated, bearer-token auth, 127.0.0.1 bind). 6 live tools + 5 governance tools.
- **Claude Code plugin**: `plugins/ruview/` — install via `/plugin marketplace add ruvnet/RuView` then `/plugin install ruview@ruview`.
- **Smart home**: Home Assistant via MQTT auto-discovery (`--mqtt` flag); Matter bridge for Apple Home, Google Home, Alexa; 21 HA entities per node + 3 starter blueprints.
- **105 edge modules**: Signed binaries (~400 KB each), OTA-updated, Ed25519-verified; browsable at `seed.cognitum.one/store`.

## Security

- **License**: MIT — no copyleft or commercial restrictions.
- **MCP server auth**: Bearer token + 127.0.0.1 bind by default; Streamable HTTP uses Origin validation. Reasonable local-service posture.
- **Edge binary signing**: Ed25519 signatures on all 105 cog modules (ADR-100), verified before install. Witness chain (Ed25519 attestation log) for audit.
- **Privacy design**: BFLD layer (ADR-118) is documented as preventing identity leakage from beamforming feedback — raw BFI never leaves the node, identity embeddings are RAM-only, cross-site correlation blocked via per-site BLAKE3 keyed hash with daily rotation. These are architectural claims; independent verification not available.
- **Benchmark retraction noted**: The README itself corrected a "100% presence" overclaim — this is a positive transparency signal but also confirms claims should not be taken at face value without reproduction.
- **Supply chain**: Single primary author (ruvnet). No signed releases visible from the README. Contributor count unknown from README alone.
- **Known gap**: `--model` flag with JSONL RVF format silently degrades to null output instead of falling back to heuristics — a reliability concern for production sensing pipelines.
- **Security flags**: `beta-software` (known functional gaps, unstable APIs), `hardware-dependent` (core claims unverifiable without hardware), `readme-benchmark-corrections-noted` (prior overclaims retracted in-situ).
