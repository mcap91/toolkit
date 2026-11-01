---
name: amazon-bedrock
title: Amazon Bedrock
url: "https://aws.amazon.com/bedrock/"
category: framework
summary: "AWS managed platform for building generative AI applications — 100+ foundation models (Amazon Nova, Anthropic Claude, OpenAI GPT-5.x, Meta Llama, DeepSeek, Mistral, etc.) through one API; AgentCore for production agent deployment with any framework (LangChain, OpenAI Agents SDK, Claude Agent SDK, Strands); Knowledge Bases for RAG; Guardrails; model distillation, prompt caching, intelligent routing; enterprise security (SOC, ISO, FedRAMP High, HIPAA eligible)"
tags: [aws, cloud, model-gateway, agents, rag, guardrails, enterprise, multi-provider, agentcore, knowledge-bases]
reviewed: 2026-07-15
acquired: 2026-07-15
license: proprietary
security_flags: []
overlaps: [litellm, nvidia-build]
source: unknown
---

## What it says

AWS's managed platform for generative AI, serving 100,000+ organizations. Provides a unified API to 100+ foundation models from ~18 providers, plus infrastructure for agents, RAG, customization, and governance.

### Model access

Single API to models from Amazon (Nova Micro/Lite/Pro/Premier, Canvas, Reel, Sonic), Anthropic (Claude 4 family), OpenAI (GPT-5.5, GPT-5.4, Codex — limited preview), Meta (Llama), DeepSeek, Mistral, Cohere, AI21, Stability AI, Google Gemma, Qwen, Writer, Luma AI, TwelveLabs, NVIDIA Nemotron. Includes evaluation tools for model comparison on performance and cost.

### AgentCore (GA 2026)

Production agent infrastructure: Agent Registry, managed orchestration for multi-agent pipelines, Runtime (pay-per-active-use, not pre-allocated), Gateway (secure tool/model/agent access with auth), Code Interpreter (sandboxed execution), Memory (built-in strategies), Policy (per-call authorization), Evaluations (13 built-in + custom evaluators), Observability (CloudWatch), Payments (Coinbase/Stripe, preview). Supports any framework: LangChain, OpenAI Agents SDK, Claude Agent SDK, Strands SDK, or custom.

### Key capabilities

- **Knowledge Bases:** RAG with managed retrieval over enterprise data
- **Guardrails:** Block up to 88% harmful content, 99% accuracy on hallucination detection via Automated Reasoning checks
- **Model Distillation:** Distilled models run up to 500% faster, cost up to 75% less
- **Intelligent Prompt Routing:** Up to 30% cost reduction by routing to the cheapest capable model
- **Prompt Caching:** Reduce repeated-context costs
- **Batch inference:** 50% lower price than on-demand
- **Fine-tuning and data customization**

### Pricing (on-demand examples)

- Amazon Nova Micro: $0.035/M input tokens (cheapest tier)
- Amazon Nova Pro: $0.80/$3.20 per M input/output tokens
- Frontier models (Claude, OpenAI): significantly higher
- AgentCore Runtime: $0.0895/vCPU-hour, $0.00945/GB-hour (active use only)
- AgentCore Memory: $0.25/1K records + model inference
- Agent Registry free tier: 5K records, 1M search calls, 2M list/get calls per month

### Reported deployments

Robinhood scaled from 500M to 5B tokens daily in 6 months, 80% AI cost reduction, 50% faster development. Epsilon accelerated agent development from months to weeks.

## Key takeaways

- Broadest model selection of any managed platform — hedges against vendor lock-in at the model layer
- AgentCore's active-use billing is significant for agentic workloads that spend 30–70% of time in I/O wait
- 12 independently billable AgentCore components create pricing complexity — idle session memory accumulation, CloudWatch charges, and per-tool-call Policy charges are common surprises
- Guardrails with Automated Reasoning checks provide a managed hallucination-reduction layer not available on most alternatives
- Enterprise compliance (SOC, ISO, FedRAMP High, HIPAA eligible) makes it the default for regulated industries

## Security

Proprietary AWS service. Data never stored or used for model training. Encryption in transit and at rest. Identity-based policies for data access. Comprehensive monitoring/logging. In-scope for ISO, SOC, CSA STAR Level 2, GDPR, FedRAMP High; HIPAA eligible.