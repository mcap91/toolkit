---
name: comfyui
title: ComfyUI
url: "https://github.com/comfy-org/comfyui"
category: framework
summary: "Node-graph GUI, API, and backend for diffusion/generative-media models (Python/PyTorch) — build image/video/audio/3D pipelines visually from modular nodes (samplers, ControlNet, LoRA, upscalers), with smart partial re-execution, low-VRAM offloading, workflows saved as reproducible JSON (embedded in generated PNGs), a headless API mode, custom-node ecosystem via ComfyUI-Manager, and a cross-platform desktop app; GPL-3.0, ~132k stars, Comfy-Org backed"
tags: [diffusion, stable-diffusion, image-generation, video-generation, node-graph, pytorch, python, workflow, low-vram, api]
reviewed: 2026-09-10
acquired: 2026-09-10
license: GPL-3.0
security_flags: [custom-node-supply-chain, workflow-json-code-execution-history]
overlaps: []
source: unknown
---

## What it does

ComfyUI is the de-facto standard open-source interface for running diffusion and generative-media models as **node graphs**: checkpoints, samplers, conditioning, ControlNets, LoRAs, VAEs, upscalers, and post-processing are nodes wired into executable pipelines. It supports the full modern model zoo — Stable Diffusion 1.x/SDXL/SD3, Flux, video models (Hunyuan, Wan, LTX, Mochi), audio and 3D generation — on NVIDIA/AMD/Intel/Apple Silicon, with aggressive VRAM management (model offloading and smart caching let large models run on small GPUs; `--lowvram`/`--cpu` fallbacks).

Only changed subgraphs re-execute between runs. Every generated PNG embeds its full workflow JSON, making outputs self-documenting and drag-to-reproduce. A queue-based HTTP/WebSocket API runs workflows headless, which is how agent pipelines and hosted services drive it programmatically.

## Differentiators

- Graph-as-artifact: workflows are portable JSON, shareable, versionable, and embeddable in outputs — reproducibility is structural, not optional.
- The custom-node ecosystem (thousands of community nodes via ComfyUI-Manager) extends it into segmentation, face tools, video pipelines, and LLM integration; this is both its power and its main risk surface.
- Comfy-Org (company formed 2024) ships a desktop app (Windows/macOS/Linux), a registry for vetted nodes, and comfy.org cloud services while the core stays GPL.
- Partial re-execution + offloading made it the performance/VRAM reference point against A1111-style web UIs.

## Mechanical details

- Install: desktop app, or `git clone` + `pip install -r requirements.txt` + `python main.py` (PyTorch env), or the standalone Windows build; `--listen` exposes the server beyond localhost.
- API: POST a workflow JSON to `/prompt`; progress via WebSocket; the same graph the GUI edits.
- Python, GPL-3.0, ~132.4k stars, ~15.6k forks, 4,847 open issues; created 2023-01 (comfyanonymous), now under Comfy-Org; pushed same day as review.

## Security

- **License:** GPL-3.0 — copyleft for redistribution/modification of ComfyUI itself; generated content unaffected.
- `custom-node-supply-chain` — custom nodes are arbitrary Python fetched from community repos; multiple real incidents exist of malicious ComfyUI nodes exfiltrating credentials (e.g. 2024 "ComfyUI_LLMVISION" malware). Treat node installs like npm installs from unknown authors; the Comfy Registry mitigates but does not eliminate this.
- `workflow-json-code-execution-history` — some nodes execute embedded code/expressions; loading untrusted workflows can trigger untrusted node code if those nodes are installed.
- Exposing the server (`--listen`) publishes an unauthenticated API by default — front with auth or keep on localhost.