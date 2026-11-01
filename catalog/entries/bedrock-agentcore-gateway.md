---
name: bedrock-agentcore-gateway
title: Amazon Bedrock AgentCore Gateway
url: "https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/"
category: framework
summary: "Fully managed AWS service that converts REST APIs and Lambda functions into MCP-compatible tool servers — zero-code MCP creation from OpenAPI/Smithy specs, semantic tool discovery, OAuth inbound + IAM/API-key/OAuth outbound auth, CloudWatch observability; solves M×N agent-to-tool integration at enterprise scale"
tags: [aws, bedrock, mcp, agent-tools, gateway, enterprise, oauth, lambda, openapi, semantic-search]
reviewed: 2026-08-02
acquired: 2026-08-02
overlaps: [a2a-protocol]
license: proprietary
security_flags: []
source: unknown
---

## What it does

Amazon Bedrock AgentCore Gateway is a fully managed AWS service that acts as a centralized MCP tool server for AI agents. It converts existing REST APIs (via OpenAPI or Smithy specs) and AWS Lambda functions into MCP-compatible tools without writing MCP server code. Agents connect to a single gateway endpoint and discover/invoke tools through the standard MCP protocol.

Core capabilities:

- **Zero-code MCP creation**: Point at an OpenAPI spec (inline or S3) or Lambda ARN with a tool schema, and Gateway exposes them as MCP tools.
- **Semantic tool discovery**: Optional built-in `x_amz_bedrock_agentcore_search` tool that lets agents find relevant tools via natural language queries, addressing "tool overload" when agents face hundreds of tools.
- **Dual-sided security**: Inbound OAuth (MCP auth spec compliant — works with Cognito, Okta, Auth0, or any OAuth provider) + outbound auth per target (IAM roles for Lambda/Smithy, API keys or 2LO OAuth for REST APIs). Credentials managed through AgentCore Identity.
- **Composition**: Multiple APIs, functions, and tools behind a single MCP endpoint.
- **Observability**: CloudWatch metrics (latency, error rates, concurrent executions, p50/p90/p99) and CloudTrail audit logging.
- **Framework integrations**: Works with Strands Agents, LangChain/LangGraph, and any MCP-compatible client via streamable HTTP transport.

Part of the broader Amazon Bedrock AgentCore suite (Runtime, Identity, Code Interpreter, Memory, Browser, Observability).

## Mechanical details

Gateway is created via Boto3, AWS Console, CLI, or AgentCore starter toolkit. Each gateway has multiple targets (Lambda, OpenAPI, Smithy). Targets are grouped by business domain, outbound auth method, and API type. Supports streamable HTTP transport. Debug mode (`exceptionLevel: "DEBUG"`) provides granular error messages during development. Usage is billed per AgentCore Gateway pricing.

## Security

Proprietary AWS managed service. Enterprise-grade security architecture: inbound OAuth validation (authorization code + client credentials flows), outbound IAM/API-key/OAuth per target, credential isolation per target with AgentCore Identity. No self-hosted option — runs entirely within AWS infrastructure. Standard AWS shared-responsibility model applies.