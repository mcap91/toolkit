---
name: jit-agent
title: JIT-Agent (Just-in-Time Harness Evolution)
url: "https://github.com/bingreeky/JIT"
category: framework
summary: "Research meta-agent (arXiv 2608.25593) that generates a task-specific agent harness on the fly — given a task spec, protocol, and tool registry it emits executable harness code factored into memory/planning/action/capability modules against shared HarnessFactory interfaces, revises it from execution traces, and selects among N candidates by judge or logprob; ships a JIT-27B meta-model checkpoint and 7 benchmark adapters; Python, ~440 stars"
tags: [meta-agent, harness-generation, agent-research, harness, benchmark, vllm, code-generation, arxiv, model-as-a-harness]
reviewed: 2026-09-10
acquired: 2026-09-10
license: NOASSERTION
security_flags: [generated-code-execution, unclear-license]
overlaps: []
source: unknown
---

## What it does

JIT-Agent ("Scaling Harness Intelligence via Just-in-Time Harness Evolution," arXiv 2608.25593, Zhang et al. 2026) is a research meta-agent that writes the agent harness itself, per task, instead of using one precompiled general-purpose scaffold. Given a task spec, a protocol, a tool/skill registry, and a few retrieved prior harnesses, it emits an executable task-specific harness that wraps any off-the-shelf agentic LLM — the authors call this "Model-as-a-Harness."

Every generated harness is factored into four modules — memory, planning, action, and capability orchestration — implemented against shared interfaces in `HarnessFactory`, so generation means emitting structured code rather than free-form agent programs. As traces and feedback return, JIT-Agent revises the harness and updates an archive: harnesses improve at test time while the generator stays frozen. The published JIT-Agent-27B checkpoint reportedly lifts a range of backbone agents across deep research, daily work, planning, and workspace tasks.

## Differentiators

- Treats scaffold construction as a trainable, transferable axis of agent intelligence, orthogonal to scaling the base model.
- Three-model split: a meta model writes the harness, an execution model runs its agent loop, a judge model grades artifacts; every role independently configurable (hosted API or local vLLM/SGLang endpoint).
- Best-of-N harness selection: `judge` selector for hosted APIs, `logprob` selector (needs the meta model's tokenizer) for the local checkpoint.
- Eleven hand-written harness designs in `harness_factory/` runnable directly (`run_seed_harness`) without any meta model — usable as a harness-design reference library.
- Resume semantics: identical re-runs skip completed generation/selection/execution work.

## Mechanical details

- Setup: Python 3.11 conda env; `.env` for `OPENAI_API_*`/`EXEC_MODEL`, `JUDGE_MODEL`, `META_MODEL`, plus `SERPER_API_KEY`/`JINA_API_KEY` for web_search/crawl_page tools.
- Benchmarks: xbench, deepsearchqa, agentif, officebench, odyssey, shopping, travel (adapters + evaluator per benchmark; full data ~1 GB via `fetch_datasets.sh`).
- Runs: `python -m scripts.run_seed_harness --bench xbench --harness plan_and_execute` (fixed design); `python -m scripts.run_jit --bench xbench --selector judge --rollouts 3` (hosted meta); `serve_meta_model.sh` + `--selector logprob` for the JIT-27B checkpoint.
- Output tree: `summary.json`, `generate/` (N candidates with prompts), `select/` (pick + scores), `execute/` (trajectory + reported numbers).
- Python, ~440 stars, 50 forks; created 2026-08, pushed 2026-08-27; 16-author paper (incl. Wangchunshu Zhou, Shuicheng Yan).

## Security

- **License:** repo shows "Other"/NOASSERTION on GitHub — not a recognized SPDX license; check LICENSE before any reuse.
- `generated-code-execution` — the whole point of the system is executing model-generated harness code; running it means running LLM-written Python with tool access (web search, crawling). No sandbox is bundled.
- Requires shipping task data to up to three model endpoints; credentials via `.env` with CLI override.
- Research-grade code, single-owner repo, 2 open issues, no CI visible from the README.