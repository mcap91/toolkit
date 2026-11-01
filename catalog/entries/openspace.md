---
name: openspace
title: OpenSpace
url: "https://github.com/HKUDS/OpenSpace"
category: meta-skill
summary: "Compelling skill-evolution engine for Claude Code agents but very new (v0.1.0), self-published benchmark, and significant security surface from community skill ingestion"
tags: [skill-evolution, mcp-server, claude-code, agent-learning, skill-sharing, token-efficiency, meta-skill, token-reduction]
reviewed: 2026-06-10
acquired: 2026-06-10
license: LicenseRef-unknown
security_flags: [untrusted-skill-execution, community-code-download, self-published-benchmark, license-not-stated]
overlaps: []
source: unknown
---
## What it does

OpenSpace is a self-evolving skill engine that plugs into any agent supporting SKILL.md-format skills (Claude Code, Codex, OpenClaw, nanobot, Cursor) via an MCP server. It observes every task execution and autonomously evolves skills through three modes: FIX (repair a broken skill in-place with a new version), DERIVED (create a specialized child skill from a parent), and CAPTURED (extract a novel reusable pattern from a successful execution with no prior skill).

Skills are stored in SQLite with a full version DAG and quality metrics (applied rate, completion rate, fallback rate). A local React dashboard visualizes lineage, diffs, and health. A cloud community at open-space.cloud enables cross-agent sharing with public/private/group access control.

The GDPVal benchmark (self-published, 50 tasks, 6 industries) reports 4.2x higher "income capture" and 46% fewer tokens vs. a ClawWork baseline using the same backbone LLM. Integration is two steps: add the MCP server to `.mcp.json` and copy two host skills (`delegate-task`, `skill-discovery`) into the agent's skills directory.

## Assessment

The concept is directly aligned with this toolkit's domain — automating skill quality improvement for Claude Code is exactly the problem the toolkit addresses. The MCP-first integration and SKILL.md compatibility mean it could slot in without workflow changes.

However, several factors argue for watching rather than piloting now:

1. **Immaturity**: Open-sourced 2026-03-25 (v0.1.0, ~11 weeks old). The changelog shows rapid churn — multiple breaking fixes per week for the first month.
2. **Benchmark credibility**: GDPVal is self-designed and published by the same team; ClawWork is also their own framework used as baseline. No independent replication yet.
3. **Security surface**: The evolved skill engine writes and executes code on the host. Downloading community skills is effectively untrusted code execution (addressed partially with safety checks, but unaudited).
4. **Cloud dependency for full value**: Local-only operation works, but the core differentiator (collective intelligence, cross-agent sharing) requires a cloud API key from open-space.cloud — a service with no stated SLA or longevity guarantee.

Worth tracking closely. If independent benchmarks validate the token savings and the codebase stabilizes past v0.2, this becomes a pilot candidate.

## Mechanical details

- **Install**: `pip install -e .` from cloned repo; or sparse checkout to skip 50 MB assets folder.
- **MCP integration**: `openspace-mcp` command; supports stdio (default), SSE (`--transport sse`), and streamable HTTP (`--transport streamable-http`).
- **Host skills**: Copy `openspace/host_skills/delegate-task/` and `openspace/host_skills/skill-discovery/` into the agent's skills directory. These two SKILL.md files teach the agent when and how to invoke OpenSpace.
- **Evolution triggers**: (1) post-execution analysis after every task; (2) tool degradation monitor (batch-evolves skills when tool success rates drop); (3) periodic metric monitor scanning skill health.
- **Skill storage**: SQLite at `.openspace/openspace.db` with version DAG, lineage tracking, quality metrics. Browsable in any SQLite viewer.
- **Dashboard**: `openspace-dashboard --port 7788` (backend) + `npm run dev` in `frontend/` (React + Tailwind). Requires Node >= 20.
- **Cloud CLI**: `openspace-download-skill <id>` / `openspace-upload-skill <path>`.
- **LLM support**: LiteLLM-backed; auto-detects credentials from host agent config; respects `OPENSPACE_MODEL` and `OPENSPACE_LLM_*` env vars.
- **Python API**: `async with OpenSpace() as cs: result = await cs.execute(...)` with `evolved_skills` in the result.

## Security

**Untrusted skill execution**: The core loop writes LLM-generated code to SKILL.md files and executes them as agent instructions. Community-downloaded skills are effectively arbitrary code from strangers — the stated safety checks (prompt injection, credential exfiltration scanning) are LLM-based heuristics, not sandboxing. No isolated execution environment by default (E2B sandboxing is referenced in code structure but not documented as default).

**Path traversal**: Hardened zip extraction and `import_skill` against path traversal in 2026-03-31 patch — was vulnerable prior to that version.

**Supply chain**: litellm pinned to `<1.82.7` to avoid PYSEC-2026-2 (a confirmed supply-chain CVE). Dependency pinning practice is present but reactive rather than proactive.

**License**: Not stated in the README or fetched content. HKUDS is an academic lab at Hong Kong University; prior HKUDS repos (LightRAG, etc.) have used MIT, but this repo's license is unconfirmed from available content.

**Multi-channel gateway**: WhatsApp and Feishu adapters ship with the framework. Enabling these exposes the agent to inbound messages from external parties; allowlist-based access control is mentioned but adds attack surface.

**Maintenance signal**: Active — multiple commits per week since open-sourcing. But rapid churn in security-adjacent areas (path traversal, supply chain) in the first few weeks signals the codebase was not hardened before release.
