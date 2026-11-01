---
name: browser-use
title: Browser Use
url: "https://github.com/browser-use/browser-use"
category: framework
summary: "MIT-licensed Python/Rust framework giving LLM agents real browser control — useful for web scraping, form automation, and accessing bioinformatics portals, but Rust-core beta is still experimental and full capability requires commercial cloud"
tags: [browser-automation, web-scraping, agent, python, rust, claude-code-skill]
reviewed: 2026-06-10
acquired: 2026-06-10
license: MIT
security_flags: [curl-install-pattern, cloud-data-sharing-risk]
overlaps: []
source: unknown
---

## What it does

Browser Use gives LLM agents a real browser action space — navigate, click, type, screenshot, read DOM state — via a Python API backed by a Rust core (v0.13+). The agent receives a task string, an LLM handle (OpenAI, Anthropic, Google, or the proprietary `bu-*` models), and an optional `BrowserProfile`, then autonomously drives the browser through recovery loops inspired by coding agents until the task is complete or exhausted. A CLI provides headless/interactive one-liner automation. A Claude Code skill (installable via curl) exposes browser control directly within Claude Code sessions. There is also a commercial cloud offering with stealth browsers, proxy rotation, CAPTCHA solving, and 1000+ integrations, but the core library is fully self-hostable.

## Assessment

**Pilot** — the capability is genuinely novel and relevant: bioinformatics workflows frequently need to interact with web-only tools (NCBI, Ensembl, cBioPortal, GEO submission forms, data portals). Browser Use provides a principled, agent-driven way to do this with real browser state rather than raw HTTP. The MIT license is clean, the project is active, and there is an explicit Claude Code skill that integrates directly into this toolkit's model. The Rust-core beta is still flagged experimental, and the highest-accuracy models (`bu-3-max`) are proprietary and metered. Adopt after the Rust core stabilizes and after evaluating cloud data-sharing implications for genomics data.

## Mechanical details

- **Install:** `pip install "browser-use[core]"` or `uv add "browser-use[core]"` (Python >= 3.11)
- **Architecture:** Python API → Rust core → browser harness (Chromium-based) → web
- **LLM support:** OpenAI, Anthropic (Claude), Google, Ollama (local), proprietary `ChatBrowserUse` (`bu-3`, `bu-3-max`)
- **Key classes:** `Agent` (orchestrator), `BrowserProfile` (headless, allowed_domains, proxy), `Tools` (custom action extension)
- **Claude Code skill:** `curl -o ~/.claude/skills/browser-use/SKILL.md https://raw.githubusercontent.com/browser-use/browser-use/main/skills/browser-use/SKILL.md`
- **CLI:** persistent browser session; commands: `open`, `state`, `click`, `type`, `screenshot`, `close`
- **Template generator:** `uvx browser-use init --template default|advanced|tools`
- **Benchmark:** open-source benchmark at `browser-use/benchmark` covering 100 real-world tasks
- **Cloud tier:** stealth proxies, CAPTCHA, scaling, persistent memory — separate paid API key

## Security

- **License:** MIT — no copyleft, no commercial restrictions on library use.
- **Curl-install pattern:** the Claude Code skill install uses `curl -o` (writes file, does not pipe to shell), which is safer than `curl | sh` but still fetches remote code without pinning a commit hash or verifying a signature. Pin the URL to a tagged release SHA before adopting in regulated environments.
- **Cloud data sharing:** the recommended production path routes browser sessions through Browser Use Cloud infrastructure. For genomics pipelines handling identifiable patient data or pre-publication sequences, this is a meaningful risk surface — evaluate their Terms of Service and Privacy Policy before integrating.
- **Credential handling:** `BrowserProfile` can reuse existing Chrome profiles with saved logins; this is powerful but means agent errors could expose credentials to task output or logs. Scope `allowed_domains` carefully.
- **Dependency surface:** native Rust binary + Chromium; supply chain is larger than a pure-Python package. No evidence of pinned deps or signed releases from the README.
- **No eval/shell-injection signals** observed in the documented API surface.
