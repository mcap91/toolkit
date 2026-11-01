---
name: ornith-dgx-spark-setup
title: Ornith-1.5-35B-A3B DGX Spark Setup
url: "https://github.com/Hitheshkaranth/Ornith-1.5_A3B_Model_DGX_Spark_Setup"
category: reference
summary: "Deployment toolkit for serving Ornith-1.5-35B-A3B (35B MoE, 3B active) on a single NVIDIA DGX Spark (128GB unified memory) via vLLM 0.24 with multi-token prediction — includes multi-user API gateway with per-user token counting and Grafana dashboards; 79 tok/s single-user, 25 tok/s × 20 concurrent users (490 tok/s aggregate), 262K context; NVFP4 checkpoint (~22 GiB)"
tags: [ornith, dgx-spark, vllm, moe, self-hosted, multi-user, local-inference, deployment, gpu, grafana, api-gateway]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: [on-prem-llm-deployment-architecture]
license: unknown
security_flags: []
source: unknown
---

## What it does

Complete deployment setup for running Ornith-1.5-35B-A3B (35B total / 3B active MoE from DeepReinforce) on a single NVIDIA DGX Spark for a 20-person team. Includes vLLM serving config, a Python API gateway, and Grafana monitoring.

Key components:

- **Model**: Ornith-1.5-35B-A3B NVFP4 checkpoint (~22 GiB). 3B active parameters per token. Vision and tool calling supported.
- **Inference**: vLLM 0.24 with multi-token prediction (speculative decoding from in-checkpoint MTP layer, ~86-88% draft acceptance). No separate draft model needed.
- **Gateway**: Python service fronting vLLM — per-user/device API keys, live input/output token counting per user, Grafana dashboard integration, direct-access alerting.
- **Performance**: Single user 79 tok/s decode. 20 concurrent users: 25 tok/s each, 490 tok/s aggregate. Full 262K context available to every request.

## Mechanical details

Reasoning scores: MATH-500 97%, GSM8K 98%, MMLU-Pro 81%. Not frontier-level but adequate for daily coding, docs, and Q&A workloads.

Operational notes from the deployment:
- GPU memory utilization must be capped at 0.70 on unified memory or concurrency degrades under load.
- Past 20 concurrent slots, throughput drops as requests queue.
- Open WebUI stores the default model in its own database and ignores the env var after first setup.

GitHub repo includes setup scripts, gateway source, Grafana dashboards, and benchmark scripts with raw results.

## Security

License not stated in the queue content. Model weights are from ornith-ai/Ornith-1.5-35B-A3B-NVFP4. The gateway runs between users and vLLM, preventing direct access. All inference is local — no external API calls.