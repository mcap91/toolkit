---
name: on-prem-llm-deployment-architecture
title: On-Prem LLM Deployment Architecture (Hardware + Inference Stack Selection)
category: reference
summary: "Community-sourced reference on selecting hardware (NVIDIA DGX Spark, RTX multi-GPU, Apple Silicon Mac Studio Ultra, AMD Instinct) and inference stacks (vLLM, SGLang, llama.cpp, MLX, Ollama, Open WebUI) for self-hosted LLM serving at 10–20 concurrent users; covers memory sizing, throughput data, and real deployment reports"
tags: [self-hosted, local-inference, gpu, hardware, vllm, ollama, inference, deployment, privacy, dgx-spark, apple-silicon]
reviewed: 2026-07-15
acquired: 2026-07-15
license: unlicensed
security_flags: []
overlaps: [parallel-local-inference, open-webui]
source: unknown
---

## What it says

Community discussion on choosing hardware and software for a fully private, on-prem ChatGPT-like platform serving 10–20 daily active users within a ~300-employee company. Requirements: no data leaves the network, web chat with auth, RAG over internal docs, agents/tool-calling, coding assistance, document analysis, full log control.

### Hardware options discussed

**NVIDIA DGX Spark (GB10 Grace Blackwell):** 128 GB unified LPDDR5x, ~1 PFLOP FP4, ~$4,700. Runs 200B-parameter models at 35–80 tok/s. Scales to multi-node via 200 GbE RoCE with pipeline parallelism (~$21–23K for a 4-node cluster). Ships DGX OS (Ubuntu) with Ollama pre-installed, Docker GPU passthrough, and CUDA 13. First-class vLLM support. Compact form factor (150×150×50mm, 1.2 kg). Respondents report two DGX Spark units serving Qwen 3.6-27B and Qwen 3.6-35B via vLLM with MTP DFlash speculative decoding at 30–90 tok/s depending on model and concurrent users.

**NVIDIA RTX multi-GPU:** One respondent serves 4–6 coding agents from a converted gaming rig with 4×RTX 3090. Budget-friendly but requires manual configuration and lacks unified memory.

**RTX 5090 / RTX PRO 6000:** Desktop Blackwell (SM 12.0). vLLM NVFP4 support landed later than datacenter Blackwell; still catching up as of mid-2026.

**Apple Silicon (Mac Studio Ultra, 256–512 GB unified memory):** High memory ceiling enables very large models. MLX and llama.cpp are the primary inference engines. Competitive for single-user or low-concurrency workloads. Less mature multi-user serving ecosystem compared to NVIDIA.

**AMD (Ryzen AI Max, Instinct):** Mentioned but less community deployment data available.

### Inference stacks discussed

- **vLLM** — server-grade, OpenAI-compatible API, continuous batching, NVFP4 on Blackwell delivers 3–4× throughput over BF16, recommended for multi-user serving
- **SGLang** — high-performance alternative to vLLM with structured generation strengths
- **llama.cpp** — optimized for single-stream low-latency; good for single-user, less efficient at concurrent serving
- **MLX** — Apple Silicon native; strong single-user performance on Mac hardware
- **Ollama** — easiest setup (one command), good for prototyping and small teams, ships pre-installed on DGX Spark
- **Open WebUI** — web chat frontend compatible with Ollama and OpenAI-compatible backends; provides the user-facing chat experience

### Models considered production-ready

Qwen 3.6 (27B, 35B), DeepSeek (R1, V3, V3.1), Llama, GLM, various MoE architectures. Qwen 3.6-27B specifically noted as matching 100–230B MoE models on coding benchmarks.

### Practical advice from respondents

- Rent cloud GPU clusters first to benchmark actual token throughput needs before purchasing hardware
- vLLM + Blackwell + NVFP4 supports concurrent multi-user requests without speed degradation
- Two DGX Spark units with Open WebUI + LiteLLM frontend is a tested small-team deployment
- A 4×3090 gaming rig conversion can serve a handful of coding agents

## Key takeaways

- For 10–20 concurrent users, DGX Spark (1–2 units) or a multi-GPU NVIDIA workstation are the most battle-tested options
- vLLM is the consensus choice for multi-user serving; Ollama for rapid prototyping
- Apple Silicon is competitive on memory capacity but the multi-user serving stack is less mature
- Rent before buying — actual throughput requirements depend heavily on workload type (chat vs coding vs document analysis)
- Total cost for a capable on-prem setup: $5K–23K hardware + ~$150/year electricity

## Security

Discussion post — no code to audit. All architectures described keep data on-premises by design.

## Usage notes

- Qwen3.8-27B (IQ4_XS, 14.25 GB) on 1x RTX 4090 24GB via llama-server + llama-swap: 115 t/s decode, 22,934 MiB peak VRAM, 196K context. DeepSWE single-task result: 40/43 hidden tests passed (partial 0.980). Code-review task: 12/12. Full config: `-ngl 99 --jinja --ctx-size 196608 --spec-type draft-mtp --spec-draft-n-max 4 --reasoning on -fa on -ctk q8_0 -ctv q8_0 --parallel 1`. Heavier alt: Q4_K_XL (17.56 GB). Context ceiling guide: https://ai.ttindall.com/blog/27b-24gb-context-ceiling/
