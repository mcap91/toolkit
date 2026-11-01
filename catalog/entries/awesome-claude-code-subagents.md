---
name: awesome-claude-code-subagents
title: Awesome Claude Code Subagents (VoltAgent)
url: "https://github.com/VoltAgent/awesome-claude-code-subagents"
category: reference
summary: "Curated collection of 161+ Claude Code subagent definitions across 10 categories (core dev, language specialists, infrastructure, quality/security, data/AI, developer experience, specialized domains, business/product, meta-orchestration, research/analysis); installable via Claude Code plugin marketplace, interactive shell script, or manual copy to ~/.claude/agents/; each subagent is a Markdown file with YAML frontmatter (name, description, tools, model); includes a /subagent-catalog skill for browsing and fetching agents; MIT, 6.4k stars"
tags: [claude-code, subagents, agents, curated-list, plugin, orchestration, developer-tools, awesome-list]
reviewed: 2026-09-26
acquired: 2026-09-26
overlaps: [awesome-claude-code, agent-dispatcher, awesome-design-md]
license: MIT
security_flags: []
source: unknown
---

## What it does

A curated repository of 161+ Claude Code subagent definitions organized into 10 plugin categories: Core Development (13 agents — API designer, backend/frontend/fullstack developer, mobile, microservices, etc.), Language Specialists (30 agents — TypeScript, Python, Go, Rust, Java, PHP, Ruby, Swift, C++, C#, Kotlin, Elixir, and framework-specific variants like Next.js, Django, Laravel, Rails, Spring Boot), Infrastructure (16 agents — cloud architect, DevOps, Kubernetes, Terraform, Docker, SRE, network, security), Quality & Security (17 agents — code reviewer, penetration tester, chaos engineer, GDPR compliance, accessibility, performance), Data & AI (13 agents — ML engineer, data scientist, LLM architect, NLP, MLOps, reinforcement learning), Developer Experience (16 agents — CLI developer, MCP developer, documentation, refactoring, git workflow, build engineer), Specialized Domains (16 agents — blockchain, fintech, IoT, game dev, healthcare, SEO), Business & Product (17 agents — product manager, scrum master, technical writer, UX researcher, sales engineer), Meta & Orchestration (16 agents — multi-agent coordinator, context manager, workflow orchestrator, agent installer, memory curator), and Research & Analysis (11 agents — competitive analyst, market researcher, trend analyst, A/B test analysis).

Each subagent is a standalone Markdown file with YAML frontmatter specifying name, description, tool permissions (Read/Write/Edit/Bash/Grep/Glob/WebFetch/WebSearch scoped per role), and model routing (opus for deep reasoning, sonnet for everyday coding, haiku for quick tasks). Subagents run in isolated context windows and can be shared across projects.

## Installation

Four installation methods:

1. **Plugin marketplace** (recommended): `claude plugin marketplace add VoltAgent/awesome-claude-code-subagents` then `claude plugin install <plugin-name>` (e.g., `voltagent-lang`, `voltagent-infra`).
2. **Interactive installer**: `./install-agents.sh` — browse categories, select agents, install/uninstall.
3. **Standalone installer** (no clone): `curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh && chmod +x install-agents.sh && ./install-agents.sh`.
4. **Manual**: copy `.md` files to `~/.claude/agents/` (global) or `.claude/agents/` (project-specific).

Also ships a `/subagent-catalog` skill for browsing and fetching agents from within Claude Code, and an agent-installer meta-agent that can install other agents from the repo via GitHub.

## Mechanical details

Subagent files install to `~/.claude/agents/` (global, lower precedence) or `.claude/agents/` (project, higher precedence). Project-specific subagents override global ones on name collision. Claude Code auto-engages matching subagents or they can be invoked explicitly ("Have the code-reviewer subagent analyze my latest commits"). The meta-orchestration category (`voltagent-meta`) works best when other categories are also installed.

## Security

MIT licensed. The subagent definitions are Markdown files containing system prompts and tool permission lists — they do not execute code themselves. The tool permission model (`tools:` field) follows Claude Code's built-in permissions system. The repository does not audit or guarantee the security or correctness of community-contributed subagent definitions. 6.4k GitHub stars, 691 forks, actively maintained with recent PRs as of September 2026.

## How to use it

claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
