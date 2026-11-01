---
name: claw-code
title: Claw Code
url: "https://github.com/ultraworkers/claw-code"
category: framework
summary: Rust reimplementation of a CLI agent harness; self-described museum exhibit maintained by agents rather than a production tool
tags: [rust, cli-agent, claude-code-alternative, agent-harness, ultraworkers]
reviewed: 2026-06-16
acquired: 2026-06-16
license: MIT
security_flags: [deprecated-crate-name-collision]
overlaps: [openclaw]
source: unknown
---

## What it does

A Rust implementation of a CLI agent harness (similar to Claude Code) from the UltraWorkers ecosystem. Provides an interactive CLI for running LLM-powered coding sessions with support for Anthropic, OpenAI, and local OpenAI-compatible providers (Ollama, llama.cpp, vLLM). Features include interactive sessions, prompt mode, doctor health checks, file context via `@path`, and a parity harness for migration testing. Part of a broader ecosystem including LazyCodex, Gajae-Code, clawhip, and oh-my-* tools.

Notably, the repository is self-described as "closer to a museum exhibit than a product pitch" — it's maintained by agents (LazyCodex and Gajae-Code) rather than human developers, serving as a demonstration of agent-managed code maintenance.

## Assessment

The project explicitly directs users to LazyCodex and Gajae-Code for actual work, positioning itself as an agent-managed artifact rather than a production tool. The `claw-code` crate name on crates.io is deprecated (installs a stub that says "renamed to agent-code"), creating potential confusion. The agent-managed maintenance philosophy is interesting from a research perspective but means the codebase may evolve unpredictably. Note as a curiosity and reference for agent-managed repository patterns, but not a tool to adopt or pilot.

## Mechanical details

- Build from source: `git clone` → `cd rust` → `cargo build --workspace`
- Requires API key (ANTHROPIC_API_KEY or OPENAI_API_KEY); Claude subscription login not supported
- CLI commands: `claw prompt`, `claw doctor`, interactive session mode
- Windows/PowerShell first-class support with dedicated docs
- Local model support via OpenAI-compatible providers
- Parity harness for tracking Rust port completeness (PARITY.md)
- ACP/Zed integration not yet implemented (tracked in ROADMAP.md)
- Part of UltraWorkers ecosystem: clawhip, oh-my-openagent, oh-my-claudecode, oh-my-codex, gajae-code

## Security

- **License**: MIT
- **Dependency health**: Rust workspace; standard cargo dependencies
- **Code quality signals**: Test suite (`cargo test --workspace`); comprehensive documentation; mock parity harness; contributing/security/support policies
- **Supply chain**: UltraWorkers community; the `claw-code` crate on crates.io is deprecated (installs wrong binary) — name collision risk
- **Dangerous patterns**: Not affiliated with Anthropic despite similarities to Claude Code. Agent-managed codebase means changes may not have human review. The deprecated crate name on crates.io could confuse users into installing the wrong package
- **Maintenance**: Maintained by agents (LazyCodex/Gajae-Code) rather than humans; active development but unconventional maintenance model