---
name: microsoft-agentic-unified-data-foundation-fabric
title: Agentic Applications for Unified Data Foundation Solution Accelerator
url: "https://github.com/microsoft/agentic-applications-for-unified-data-foundation-solution-accelerator"
category: framework
summary: "Microsoft solution accelerator that layers Microsoft Foundry agents + Agent Framework orchestration over a Microsoft Fabric unified data foundation (SQL Database in Fabric), enabling natural-language querying across governed enterprise datasets via a web front-end; ships configurable scenario packs (retail sales analysis, financial-services client-meeting prep) with synthetic sample data; MIT"
tags: [azure, microsoft-fabric, agent-framework, azure-ai-foundry, natural-language-query, solution-accelerator, data-foundation, scenario-packs]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: [synthetic-sample-data-only]
overlaps: []
source: unknown
---

## What it does

Builds an agentic natural-language query layer on top of a Microsoft Fabric-based "Unified Data Foundation" (a companion accelerator, `unified-data-foundation-with-fabric-solution-accelerator`, providing the underlying governed lakehouse via Fabric, Purview, and Databricks). Structured data in SQL Database in Fabric is queried through Microsoft Foundry agents orchestrated by the Microsoft Agent Framework, exposed through a web front-end for exploring semantic models/data assets in plain language, aimed at making governed data self-serve for non-technical business users rather than data specialists only.

## Differentiators / Key takeaways

- Ships as configurable "scenario packs" — reusable data mappings, agent instructions, and UI patterns — rather than a single fixed demo: a retail sales/product-performance pack ("what are my top-performing products?") and a financial-services client-meeting-prep pack ("has this customer ever been delinquent?").
- Three-tier adoption path documented explicitly: Deploy (working baseline) → Configure (apply a scenario pack + load data) → Customize (add enterprise data sources, security, networking, integrations) — each with its own guide.
- Companion/sibling repo relationship: depends conceptually on `microsoft/unified-data-foundation-with-fabric-solution-accelerator` for the underlying governed data platform (medallion lakehouse, Purview governance, Databricks) — this repo is the agent/query layer on top, not the data platform itself.
- All bundled scenario data is explicitly synthetic/generated ("Contoso" sample data), not real enterprise data.

## Mechanical details / What to adopt

- Deploy: `azd auth login`, `azd config set provision.preflight off`, `azd up`.
- Setup options include GitHub Codespaces, VS Code Dev Containers, VS Code Web, local environments, or direct Bicep deployment.
- Repo suggests opening it in VS Code with Copilot and asking "Help me deploy this accelerator" for guided setup assistance.
- MIT license, confirmed by fetching the repo's `LICENSE` file directly.

## Security

MIT-licensed. All sample/scenario data ships as synthetic/generated rather than real customer data, reducing data-handling risk during evaluation. Standard Microsoft-accelerator disclaimers apply (export-control compliance, not a substitute for professional financial/legal/medical judgment, no SOC 1/2 compliance audit performed) — the repo's own framing states it "should be adapted to your own environment before production use," so treat it as a template to adapt, not a compliance-ready deployment.
