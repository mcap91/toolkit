---
name: skillspector
title: SkillSpector (NVIDIA)
url: "https://github.com/nvidia/skillspector"
category: cli-tool
summary: "NVIDIA open-source security scanner for AI agent skills — scans SKILL.md files, folders, repos, and libraries for prompt injection, credential theft, data exfiltration, remote scripts, hidden persistence, and MCP tool poisoning; returns 0–100 risk score; installable as MCP server"
tags: [security, skills, scanning, mcp, nvidia, supply-chain]
reviewed: 2026-09-16
acquired: 2026-09-16
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

Reads an AI agent skill (Claude Code, Codex, or MCP skill) and returns a 0–100 risk score plus a list of exact findings, so a skill can be vetted before installation rather than after.

- Accepts SKILL.md files, local folders, ZIP archives, GitHub repo URLs, or entire skill libraries as input
- Checks for prompt injection, credential theft, data exfiltration, remote script execution, dangerous code execution, hidden persistence, risky dependencies, and MCP tool poisoning
- Detects dangerous instructions hidden in comments, invisible text, encoded scripts, or clean-looking dependency manifests
- Combines fast static analysis with an optional LLM-powered semantic pass
- Runs as a standalone CLI or as an MCP server that Claude Code can call for pre-install scanning

## Differentiators

- Purpose-built for the emerging agent-skill format (SKILL.md) rather than a generic SAST/dependency scanner
- Two-stage pipeline: a static pass (AST walk flagging `exec`/`eval`/`subprocess`/dynamic imports, taint tracking from environment variables and file contents to network sinks, YARA rules for known malware/webshells/cryptominers) followed by an optional LLM pass that re-reads flagged code in context to reduce false positives and produce a plain-language explanation
- The LLM analysis prompt itself carries anti-jailbreak instructions, since the artifact being scanned is a set of instructions to a model
- Scoring model is additive by finding severity, with a 1.3x multiplier when the skill ships executable content; scores above 50 return a do-not-install verdict
- Anchored in NVIDIA's own research: across a 31,132-skill dataset, 26.1% of public agent skills contained vulnerabilities and 5.2% showed signs of malicious intent
- Forms the security tier (Tier 1) of NVIDIA's broader SkillEvaluator, and underlies NVIDIA's Verified Skills pipeline that scans, evaluates, and signs skills before publication

## Mechanical details

- GitHub: NVIDIA/SkillSpector; at version 2.0.0 as of August 2026, in active development
- Input formats: single SKILL.md file, directory, ZIP, GitHub repo URL, or a whole skill library
- Static analysis runs by default and requires no external service or key
- Optional LLM pass requires an OpenAI-compatible endpoint and API key, configured via `SKILLSPECTOR_PROVIDER`; defaults to NVIDIA's build.nvidia.com if enabled
- Output includes SARIF reports for CI integration, alongside the human-readable risk report
- MCP server mode lets Claude Code invoke SkillSpector directly for pre-install scanning

## Security

- License: Apache-2.0
- Static analysis only — does not sandbox, contain, or isolate a skill once the user chooses to install it
- Stated limitations: may miss patterns in non-English content, cannot analyze text embedded in images, and cannot inspect encrypted or compiled code
- The optional LLM pass sends flagged code to an external endpoint (NVIDIA's build.nvidia.com by default, or a user-configured OpenAI-compatible provider) — this pass is off unless explicitly configured
- Maintained by NVIDIA; part of a larger published pipeline (SkillEvaluator, Verified Skills) rather than a standalone side project
