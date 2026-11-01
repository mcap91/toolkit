---
name: bitnet-cpp
title: BitNet (bitnet.cpp)
url: "https://github.com/microsoft/BitNet"
category: framework
summary: "Microsoft's official inference framework for 1-bit LLMs (BitNet b1.58) — runs 100B models on a single CPU at human reading speed (5-7 tok/s), 2-6x faster than FP16 with 55-82% energy reduction; optimized kernels for x86/ARM CPU and GPU"
tags: [llm-inference, quantization, 1-bit, cpu-inference, edge-ai, local-llm]
reviewed: 2026-06-19
acquired: 2026-06-19
license: MIT
security_flags: []
overlaps: [qwen3-6-27b]
source: unknown
---

## What it does

Official inference framework for 1-bit (ternary/1.58-bit) LLMs. Built on llama.cpp with specialized kernels for ternary weight matrices using lookup-table methods (from T-MAC).

Performance characteristics:
- **ARM CPUs**: 1.37-5.07x speedup over FP16, 55-70% energy reduction
- **x86 CPUs**: 2.37-6.17x speedup, 72-82% energy reduction
- **100B model on single CPU**: achieves 5-7 tokens/second (human reading speed)
- **GPU**: official GPU inference kernels (May 2025)
- **Parallel kernels**: additional 1.15-2.1x speedup with configurable tiling and embedding quantization

Supports Microsoft's official BitNet-b1.58-2B-4T model plus community 1-bit models (Falcon3, Llama3-8B-1.58, etc.).

## Assessment

Significant for the trajectory of local/edge LLM inference. Running a 100B model on a CPU at readable speed without a GPU is a genuine capability milestone. The energy reduction numbers make this relevant for sustainable computing and resource-constrained environments.

For bioinformatics: not directly applicable today since the available 1-bit models are general-purpose and small (2B-10B range). The framework becomes relevant when domain-specific 1-bit models emerge or when running local LLMs for agent workers on CPU-only lab machines. Worth monitoring rather than adopting immediately.

Microsoft Research backing gives strong confidence in continued development. The codebase builds on llama.cpp (proven, well-maintained) with specialized kernel additions.

## Mechanical details

- **Build**: Python 3.9+, CMake 3.22+, Clang 18+, conda recommended
- **Windows**: Visual Studio 2022 with C++/Clang toolset
- **Models**: download from HuggingFace (`huggingface-cli download`), quantize with `setup_env.py`
- **Inference**: `python run_inference.py -m model.gguf -p "prompt" -cnv`
- **Benchmark**: `python utils/e2e_benchmark.py -m model -n 200 -p 256 -t 4`
- **Quantization types**: `i2_s` (x86+ARM), `tl1` (ARM), `tl2` (x86)
- **Model conversion**: `.safetensors` → GGUF via `convert-helper-bitnet.py`

## Security

- **License**: MIT
- **Dependencies**: llama.cpp (vendored), Python requirements, HuggingFace Hub for model download
- **Code quality**: benchmarking suite, technical report, optimization guide
- **Supply chain**: Microsoft Research, multiple contributors, academic publications (ICLR-level)
- **Dangerous patterns**: none — offline inference framework, no network services
- **Maintenance**: actively developed (latest update Jan 2026), backed by Microsoft Research