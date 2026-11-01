---
name: odysseus
title: Odysseus
url: "https://github.com/pewdiepie-archdaemon/odysseus"
category: framework
summary: "Feature-rich self-hosted AI workspace with massive community momentum, but weeks-old with unsandboxed agent shell execution"
tags: [self-hosted, ai-workspace, agents, local-models, docker, research, email, mcp]
reviewed: 2026-06-16
acquired: 2026-06-16
license: AGPL-3.0-or-later
security_flags: [unsandboxed-shell, new-project]
overlaps: [open-webui, headroom]
source: unknown
---

## What it does

Self-hosted AI workspace created by PewDiePie (Felix Kjellberg), launched May 31 2026. Provides a Docker-deployed browser UI combining chat, autonomous agents, deep research, document editing, email (IMAP/SMTP), notes, tasks, calendar (CalDAV), and local model serving via Ollama. Built on a Python/FastAPI backend. Hardware-aware "Cookbook" recommends and downloads models based on local GPU. Compare mode enables blind side-by-side model evaluation. Supports MCP tool integration, agent skills, and memory. ~72k GitHub stars and ~9.2k forks within weeks of launch. Local-first, privacy-first, no telemetry.

## Assessment

Watch. The project has extraordinary community momentum and a genuinely broad feature set that goes well beyond most open-source AI UIs — email, calendar, document editing, and research workflows in a single self-hosted package. However, it is only weeks old (launched 2026-05-31), the agent bash tool runs unsandboxed as the host user (full RCE surface), and the ecosystem is still stabilizing. The overlapping features with Open WebUI and Headroom mean we should monitor which platform the community consolidates around before investing setup time. Worth revisiting once sandboxing lands and the project survives its first few months of real-world security scrutiny.

## Mechanical details

- **Deploy**: `docker compose up -d --build` on port 7000; first admin password in container logs.
- **Models**: Ollama-compatible local serving plus API providers (OpenAI, Claude, etc.).
- **Agents**: Tool-using agents with shell, MCP, file access, skills, and memory. No sandbox — agents run as the Docker container's user.
- **Research**: Multi-step web research with source reading and report generation (similar to deep-research patterns).
- **Email**: Full IMAP/SMTP integration with AI triage, tagging, summarization, and draft replies.
- **Branches**: `dev` (bleeding edge) vs `main` (curated).

## Security

- **License**: AGPL-3.0-or-later (copyleft; derivatives must share source).
- **Unsandboxed agent execution**: The agent bash tool provides shell access as the running user with no sandboxing. Pointing agent mode at sensitive repos or production systems is a full RCE surface. This is the primary security concern.
- **Docker isolation**: Runs in containers, which provides some OS-level isolation, but the agent shell operates within that container with full access.
- **Supply chain**: Very new project (weeks old); contributor base and release signing practices are still forming. High star count reflects hype-cycle attention, not maturity.
- **Maintenance**: Extremely active — daily commits on the `dev` branch. Responsiveness to issues appears high given community size.
- **No telemetry**: Explicitly advertised as collecting no usage statistics.