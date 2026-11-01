---
name: azure-ai-foundry-chat-starter
title: Get Started with AI Chat (Azure AI Foundry)
url: "https://github.com/Azure-Samples/get-started-with-ai-chat"
category: framework
summary: "Microsoft starter template that deploys a RAG-capable chat web app to Azure Container Apps using Microsoft Foundry models and Azure AI Search for file-grounded, cited responses; deployable via azd up or a guided Copilot CLI /up skill; explicitly marked not production-ready without added security hardening"
tags: [azure, ai-foundry, rag, chat, azd, azure-container-apps, azure-ai-search, starter-template, application-insights]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: [vendor-marked-not-production-ready]
overlaps: []
source: unknown
---

## What it does

Deploys a web-based chat application to Azure Container Apps that talks to a Microsoft Foundry project/Foundry Tools deployment (default model `gpt-4o-mini`). Supports two modes: direct model chat, or Retrieval-Augmented Generation against files uploaded and indexed into Azure AI Search, with the app returning cited responses. Optional Application Insights + Log Analytics wiring gives request tracing for debugging and performance monitoring in the Foundry portal.

## Differentiators / Key takeaways

- Two deployment paths: a direct `azd up` (5–20 min, for users already familiar with `azd` templates) or a guided, conversational deployment through the GitHub Copilot CLI's `/up` skill (~40 min) that checks RBAC/quota, walks subscription/region selection, provisions infra, and health-checks the deployed app — `/up` only works in the Copilot CLI terminal, not the VS Code Copilot Chat panel.
- Uses Managed Identity throughout for local dev and deployment in the documented path (no long-lived keys in config).
- Ships with an explicit, prominent vendor disclaimer: "We strongly advise our customers not to make this code part of their production environments without implementing or enabling additional security features" — this is a demonstration/starter template, not a hardened reference architecture.

## Mechanical details / What to adopt

- Provisions: Azure AI Project, Azure OpenAI/Foundry Tools deployment, Azure Container Apps + Container Registry, Storage Account, optional AI Search (S1) and Application Insights/Log Analytics.
- Supports GitHub Codespaces, VS Code Dev Containers, or local dev environments.
- Teardown via `azd down` (up to ~20 min) or deleting the resource group directly; cost is usage-based except Container Registry (fixed daily cost).
- MIT license, confirmed by fetching the repo's `LICENSE` file directly (Microsoft Corporation copyright).

## Security

MIT-licensed; Managed Identity used for auth in the documented deployment path. The template carries a vendor security disclaimer recommending against production use without hardening, and points to a separate best-practices document for "Intelligent Applications." Recommends enabling Microsoft Defender for Cloud and firewalling/VNet-protecting the Container Apps instance as additional measures not enabled by default. Treat as a reference/demo starting point, not a production-ready deployment.
