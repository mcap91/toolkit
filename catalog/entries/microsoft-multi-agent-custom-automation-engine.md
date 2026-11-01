---
name: microsoft-multi-agent-custom-automation-engine
title: Multi-Agent Custom Automation Engine Solution Accelerator
url: "https://github.com/microsoft/Multi-Agent-Custom-Automation-Engine-Solution-Accelerator"
category: framework
summary: "Microsoft solution accelerator where specialized AI agents plan, execute, and validate multi-step business tasks from natural-language input, built on Microsoft Agent Framework + Azure AI Foundry + Cosmos DB + Container Apps; ships reference scenario packs (product marketing, employee onboarding, retail remediation, RFP/contract review, content generation); MIT, explicitly marked proof-of-concept"
tags: [azure, multi-agent, agent-framework, azure-ai-foundry, cosmos-db, azure-container-apps, solution-accelerator, task-automation, semantic-kernel]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: [vendor-marked-poc-not-production, requires-openai-quota]
overlaps: []
source: unknown
---

## What it does

An agentic task-automation pipeline: a user states a task in natural language, and a coordinated group of specialized agents plans it, executes sub-steps, and validates results before returning output. Built on Azure OpenAI/Foundry, Azure Container Apps (frontend host), Azure Cosmos DB (metadata/results), and Azure Container Registry. Ships with six documented example scenarios, each with its own persona/challenge/approach writeup: product marketing release planning, employee onboarding, retail customer-success remediation, RFP review, contract compliance review, and marketing content generation.

## Differentiators / Key takeaways

- Framework lineage: originally built on Microsoft Research's AutoGen framework (a related fork, `Multi-Agent-Custom-Automation-Engine-Solution-Accelerator-Dev`, still reflects this); the current `main` production repo has since moved to Microsoft Agent Framework + Semantic Kernel.
- Actively maintained: 770 stars / 625 forks and 47 open / 820 closed PRs as of an August 2026 snapshot, latest tagged release v4.1.0.
- Has a WAF (Well-Architected Framework)-supported deployment variant for tenants with stricter network-security policies (e.g., public network access blocking) that would otherwise break the default deployment.
- Deployment requires Azure Developer CLI ≥1.18.0 and, for local/non-Codespaces deploys, Bicep CLI ≥0.33.0; requires pre-flighting Azure OpenAI quota availability before deploying.
- Cross-references sibling Microsoft accelerators for adjacent problems: Document Knowledge Mining, "Modernize your Code" (SQL dialect translation), and Conversation Knowledge Mining.

## Mechanical details / What to adopt

- Quick deploy via the deployment guide's `azd up`-based flow; requires Microsoft Foundry Service, Foundry Models, Azure AI Search, and Search Semantic Ranker availability in the target region (example regions: Australia East, East US2, France Central, Japan East, Norway East, Sweden Central, UK South, West US).
- Uses Azure Key Vault for inter-resource connection secrets, Managed Identity for local dev/deployment auth.
- MIT license, confirmed by fetching the repo's `LICENSE` file directly (Microsoft Corporation copyright).

## Security

MIT-licensed; uses Key Vault + Managed Identity rather than embedded secrets in the documented path. The repo's own disclaimers state this release "is intended as a proof of concept only, and is not a finished or polished product... not intended for commercial use or distribution," and explicitly disclaims medical, legal, and financial-advice use. Recommends Microsoft Defender for Cloud and Container Apps firewall/VNet protection as additive measures. Multi-agent validation is framed by Microsoft as reducing, not eliminating, manual-coordination error risk — outputs still require human review per the disclaimers.
