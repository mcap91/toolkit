---
name: agentic-resource-discovery
title: Agentic Resource Discovery (ARD)
url: "https://huggingface.co/blog/agentic-resource-discovery-launch"
category: reference
summary: "Draft open specification (contributors from Microsoft, Google, GoDaddy, Hugging Face, and others) for a discovery layer in front of MCP/Skills/A2A: agents search federated registries in natural language to find tools, skills, and other agents at runtime instead of pre-installing them. Defines a static ai-catalog.json manifest at a well-known URL and a dynamic POST /search registry API. Hugging Face's 'Discover' tool (hf discover CLI + REST + MCP endpoint) is a reference implementation over Hub Spaces, Agent Skills, and MCP servers."
tags: [agent-discovery, specification, mcp, skills, a2a, registry, huggingface, federation, tool-discovery]
reviewed: 2026-08-17
acquired: 2026-08-17
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---
## What it covers

Agentic Resource Discovery (ARD) is a draft, open specification for the discovery layer that sits in front of MCP (tool calls), Skills (instructions), and A2A (agent-to-agent). Those three protocols all assume the user already knows which capability they need; ARD defines how agents/tools are cataloged, indexed, and searched across federated registries so an agent can find capabilities at runtime rather than having them pre-installed. It moves capability selection outside the LLM (a registry indexes richer signals — publisher identity, representative queries, compliance attestations, tags — and the client searches in natural language) instead of dumping all tool descriptions into the context window. It is a shared standard, not a product or marketplace; contributors span Microsoft, Google, GoDaddy, Hugging Face, and others.

## Mechanical details

- **Spec surface:** (1) a static `ai-catalog.json` manifest that publishers host at a well-known URL; (2) a dynamic registry API at `POST /search` for live ranked discovery. Federation modes: auto, referrals, none.
- **HF Discover (reference implementation):** wraps the Hub's semantic search over Spaces (with `agents=true`) plus Agent Skills, serving results as ARD catalog entries. Filters to `RUNNING` Spaces; response media type is request-driven — `application/ai-skill` (default; a generated SKILL.md wrapping the Space's `agents.md`), `application/mcp-server+json` (for `mcp-server`-tagged Spaces, pointing at the Gradio MCP endpoint), or `application/vnd.huggingface.space+json` (raw Space metadata).
- **Access:** `hf discover search "<query>"` (built into the `hf` CLI; `uv tool install huggingface_hub`), with `--json`, `--kind mcp`, `--registry-url`. Direct REST at `POST https://huggingface-hf-discover.hf.space/search`; catalog well-known URL `https://huggingface.co/.well-known/ai-catalog.json`; MCP endpoint `https://huggingface-hf-discover.hf.space/mcp`.
- Spec site: https://agenticresourcediscovery.org/ ; reference tool: https://github.com/huggingface/hf-discover .

## Security

- **License:** the blog does not state a license for the spec or the hf-discover implementation (recorded as NOASSERTION); verify the spec site and repo before relying on terms.
- ARD separates discovery from execution — a search returns capability descriptors; the agent still decides what to invoke. Runtime discovery means capabilities are selected dynamically from federated registries, so trust/provenance signals (publisher identity, attestations) and validation of returned MCP/A2A endpoints matter before invocation.
- The HF Discover endpoints are public HTTP/MCP services; queries are sent to Hugging Face's infrastructure.
