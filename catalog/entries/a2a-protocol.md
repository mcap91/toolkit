---
name: a2a-protocol
title: Agent2Agent (A2A) Protocol
url: "https://github.com/a2aproject/A2A"
category: reference
summary: "Google/Linux Foundation open protocol for inter-agent communication — JSON-RPC 2.0 over HTTP, Agent Cards for discovery, async-first with streaming; SDKs in 6 languages; complements MCP (tool access) with agent-to-agent collaboration"
tags: [a2a, protocol, agent-interop, multi-agent, google, linux-foundation]
reviewed: 2026-06-18
acquired: 2026-06-18
license: Apache-2.0
security_flags: []
overlaps: [awesome-a2a]
source: unknown
---

## What it does

Agent2Agent (A2A) is an open protocol from Google (now under the Linux Foundation) enabling AI agents built on different frameworks to communicate and collaborate as peers — not as tools. Agents remain opaque: they interact without sharing internal logic, memory, or tool implementations.

Core mechanics:

- **Discovery**: Agents publish an Agent Card (JSON) describing capabilities, endpoints, and auth requirements
- **Communication**: JSON-RPC 2.0 over HTTP(S) — client agent sends Task requests containing Messages with Parts to a server agent
- **Interaction modes**: Synchronous request/response, streaming (SSE), and async push notifications
- **Data exchange**: Text, files, structured JSON, forms
- **Task lifecycle**: Long-running tasks with status updates, human-in-the-loop support

Key principles: simple (HTTP + JSON-RPC + SSE), enterprise-ready (auth, security, privacy, monitoring), async-first, modality-agnostic, opaque execution.

**A2A vs MCP**: A2A handles agent-to-agent collaboration (peer communication). MCP handles agent-to-tool access (client-server tool invocation). They're complementary — an agent can use MCP to access tools and A2A to collaborate with other agents.

SDKs: Python (`pip install a2a-sdk`), Go, JavaScript (`npm install @a2a-js/sdk`), Java (Maven), .NET (NuGet), Rust (`cargo add a2a-lf`).

DeepLearning.AI course available covering ADK, LangGraph, and BeeAI integrations.

Docs: https://a2aproject.github.io/A2A

## Assessment

Important protocol to track for multi-agent system design. The MCP/A2A distinction is clean: MCP gives agents access to tools and data sources; A2A lets agents delegate to and collaborate with other agents. If we build specialized bioinformatics agents (alignment agent, variant calling agent, annotation agent), A2A would be the interoperability layer between them.

Not immediately actionable for this toolkit — we'd need concrete multi-agent scenarios first. But the protocol design (Agent Cards, opaque execution, async tasks) informs how we might structure agent interfaces. The 6-language SDK coverage means broad integration options.

The Linux Foundation governance and Google backing give it durability that most agent protocols lack. Worth monitoring as the ecosystem matures and framework adoption broadens.

## Mechanical details

- **Spec**: JSON-RPC 2.0 over HTTP(S), SSE for streaming
- **Discovery**: Agent Cards — JSON documents describing capabilities and auth
- **SDKs**: Python, Go, JS, Java, .NET, Rust
- **Samples**: Official examples with Google ADK, LangGraph, CrewAI, Genkit
- **Course**: DeepLearning.AI short course (Google Cloud + IBM Research)
- **Roadmap**: Dynamic UX negotiation, QuerySkill() method, transport improvements

## Security

- **License**: Apache-2.0, Linux Foundation governance
- **Protocol security**: Auth and security built into spec design — Agent Cards include authorization schemes
- **Enterprise focus**: Designed for auth, privacy, monitoring, observability from the start
- **Governance**: Open contribution model, Google Cloud partner program, Linux Foundation oversight
- **No dangerous patterns** — protocol spec, not executable code