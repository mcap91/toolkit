---
name: pentagi
title: PentAGI
url: https://github.com/vxcontrol/pentagi
category: framework
summary: Fully autonomous, multi-agent AI system (Go, MIT) for penetration testing — given a target and goal in plain English, a delegation system of specialized agents (research, development, infrastructure) plans and executes testing steps, running tools like Nmap and Metasploit inside an isolated Docker sandbox, and produces a report; supports OpenAI, Anthropic, Ollama, AWS Bedrock, Google AI/Gemini, DeepInfra, OpenRouter, DeepSeek, and Moonshot as LLM providers; ships a ctester utility for evaluating agent-model capability; self-described as an autonomous/assistant-guided platform, not a CALDERA-style BAS product with predefined attack campaigns
tags:
  - security
  - pentesting
  - offensive-security
  - ai-agents
  - autonomous-agents
  - multi-agent
  - docker
  - sandbox
  - golang
reviewed: 2026-10-30
acquired: 2026-10-30
license: MIT
security_flags:
  - executes-exploits
  - mutates-target-state
overlaps:
  - shannon
source_url: https://www.instagram.com/reel/De2LjyNNS4H/
source: instagram
---

## What it does

PentAGI (vxcontrol/pentagi) is a fully autonomous, multi-agent AI system for penetration testing, written in Go and licensed MIT. Given a target and goal described in plain English, it plans and executes testing steps through a delegation system of specialized agents (research, development, infrastructure tasks), running tools such as Nmap and Metasploit inside an isolated Docker sandbox, and produces a report. It supports multiple LLM providers — OpenAI, Anthropic, Ollama, AWS Bedrock, Google AI/Gemini, DeepInfra, OpenRouter, DeepSeek, and Moonshot — plus custom configurations. The project positions itself as "an autonomous and assistant-guided penetration testing platform," explicitly distinct from a CALDERA-style Breach and Attack Simulation (BAS) or adversary-emulation product with predefined campaigns or attack plans.

## Mechanical details

- Deploy via Docker Compose: create a project directory, fetch the env template with `curl -o .env https://raw.githubusercontent.com/vxcontrol/pentagi/master/.env.example`
- Includes `ctester`, a utility for testing and validating LLM agent capabilities (project recommends enabling both Execution Monitoring and Task Planning for open-source models under 32B parameters)
- Monitoring integrations: Langfuse, Grafana
- Site: pentagi.com; Discord and Telegram communities

## Security

MIT license. All penetration-testing operations run inside a sandboxed, fully isolated Docker environment by design. This is an offensive-security tool whose purpose is executing real reconnaissance and exploitation tooling (Nmap, Metasploit) against a specified target — authorization and scope boundaries are the operator's responsibility; the sandbox isolates the tool's own execution environment but does not restrict which targets it is pointed at.
