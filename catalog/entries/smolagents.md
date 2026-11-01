---
name: smolagents
title: smolagents
url: "https://github.com/huggingface/smolagents"
category: framework
summary: "HuggingFace's minimal code-first agent framework — CodeAgent writes actions as Python (30% fewer steps than JSON tool calling), sandboxed execution via E2B/Blaxel/Docker, model/modality/tool-agnostic, CLI included; Apache-2.0, 26K stars, 207 contributors"
tags: [agent-framework, code-agent, huggingface, sandbox, multi-modal, python]
reviewed: 2026-06-23
acquired: 2026-06-23
license: Apache-2.0
security_flags: []
overlaps: [crewai]
source: unknown
---

## What it does

smolagents is a Python library for building AI agents where the core logic fits in ~1,000 lines of code. Its key differentiator is the CodeAgent, which writes actions as Python code snippets rather than JSON tool-call dictionaries — demonstrated to use 30% fewer LLM calls and achieve higher performance on benchmarks.

Two agent types:
- **CodeAgent**: Writes actions as Python code (loops, conditionals, nested calls). Recommended default.
- **ToolCallingAgent**: Standard JSON/text tool calling for compatibility.

Key capabilities:
- **Model-agnostic**: Local transformers/ollama, HF Inference API, OpenAI, Anthropic (via LiteLLM), Azure, Bedrock
- **Modality-agnostic**: Text, vision, video, audio inputs
- **Tool-agnostic**: MCP servers, LangChain tools, Hub Spaces as tools
- **Hub integration**: Share/pull tools and entire agents via HuggingFace Hub
- **CLI**: `smolagent` for general agents, `webagent` for browser automation (helium-based)
- **Sandboxed execution**: E2B, Blaxel, Modal, Docker backends; LocalPythonExecutor available but explicitly not a security boundary

## Assessment

The strongest open-source code-agent framework available. The code-as-action approach is both more expressive (a single action can loop over search queries) and more efficient (30% fewer steps) than JSON tool calling. HuggingFace backing, 207 contributors, and 26K stars signal strong community health.

The sandbox integration story is well-designed — smolagents delegates to E2B/Blaxel/Docker rather than building its own isolation, which means it benefits from improvements in those tools. The LocalPythonExecutor warning is refreshingly honest about its non-sandbox status.

Relevant to this catalog because it's the agent framework most likely to appear in bioinformatics pipeline automation, and its tool/model agnosticism means it works with our existing Claude infrastructure via LiteLLM.

## Mechanical details

```bash
pip install "smolagents[toolkit]"    # with default tools
```

```python
from smolagents import CodeAgent, WebSearchTool, InferenceClientModel
agent = CodeAgent(tools=[WebSearchTool()], model=InferenceClientModel())
agent.run("your task here")
```

CLI usage:
```bash
smolagent "Plan a trip to Tokyo" --model-type InferenceClientModel --tools web_search
webagent "go to site.com and get the price" --model-type LiteLLMModel --model-id anthropic/claude-4-sonnet-latest
```

## Security

- **License**: Apache-2.0 — fully permissive
- **Sandbox**: LocalPythonExecutor is explicitly documented as NOT a security boundary; production use requires E2B/Blaxel/Docker
- **Supply chain**: HuggingFace-maintained, 207 contributors, 26K stars, active CI
- **Code quality**: Tests, linting, CI pipeline, well-documented API
- **Arbitrary code execution**: By design (CodeAgent runs generated Python) — sandboxing is the mitigation, not code inspection