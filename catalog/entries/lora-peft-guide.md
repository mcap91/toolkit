---
name: lora-peft-guide
title: LoRA (Hugging Face PEFT conceptual guide)
url: "https://huggingface.co/docs/peft/main/en/conceptual_guides/lora"
category: reference
summary: "Hugging Face PEFT conceptual guide to LoRA (Low-Rank Adaptation): fine-tune large models by training two small low-rank update matrices while the original weights stay frozen — drastically fewer trainable parameters, portable per-task adapters, and no added inference latency once merged. Covers LoraConfig parameters, merge/unmerge/unload utilities, and initialization options (Gaussian, LoftQ for QLoRA, rank-stabilized rsLoRA)."
tags: [lora, peft, fine-tuning, parameter-efficient, qlora, transformers, huggingface, adapters]
reviewed: 2026-08-17
acquired: 2026-08-17
license: Apache-2.0
security_flags: []
overlaps: []
source: unknown
---
## What it covers

A conceptual overview of LoRA (Low-Rank Adaptation) as implemented in Hugging Face's PEFT library. LoRA represents weight updates as the product of two smaller low-rank matrices (A and B) via low-rank decomposition; the original pre-trained weight matrix stays frozen and only the update matrices are trained. Advantages the guide states: far fewer trainable parameters, multiple lightweight/portable adapters over one frozen base, orthogonality to other parameter-efficient methods, performance comparable to full fine-tuning, and no inference latency because adapter weights can be merged into the base. In Transformers, LoRA is typically applied to attention blocks; in principle it applies to any dense layer (including diffusion models).

## Mechanical details

- **Workflow:** instantiate a base model → create a `LoraConfig` → wrap with `get_peft_model()` → train the resulting `PeftModel` normally.
- **Key `LoraConfig` parameters:** `r` (rank of update matrices), `target_modules`, `lora_alpha` (scaling), `bias` (`none`/`all`/`lora_only`), `use_rslora` (rank-stabilized scaling `lora_alpha/sqrt(r)` instead of `lora_alpha/r`), `modules_to_save`, `layers_to_transform`, `layers_pattern`, `rank_pattern`, `alpha_pattern`.
- **Merging utilities:** `merge_and_unload()` (fold adapter into base for a standalone model with no latency), `merge_adapter()`/`unmerge_adapter()` (keep the `PeftModel`), `unload()` (recover the base model), `delete_adapter()`, `add_weighted_adapter()` (combine multiple LoRAs by a weighting scheme).
- **Initialization (`init_lora_weights`):** default (Kaiming-uniform A, zeros B → identity transform), `"gaussian"` (diffusers-style), `"loftq"` (LoftQConfig — minimizes quantization error for QLoRA; do not pre-quantize the base), or `False` (non-identity, for debugging only).

## Security

- Documentation page only — no executable content in the guide itself.
- **License:** the PEFT library is Apache-2.0; this is its documentation.
- Applying the technique loads model weights and runs standard training/inference (PyTorch/transformers stack); no security surface beyond that toolchain.
