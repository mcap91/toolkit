---
name: chandra-ocr
title: Chandra OCR
url: "https://github.com/datalab-to/chandra"
category: cli-tool
summary: "Chandra OCR 2 is a vision-language model for document parsing that converts images and PDFs into structured Markdown/HTML/JSON while preserving layout, with strength on math, tables, forms, handwriting, and 90+ languages; code is Apache-2.0, model weights use a modified OpenRAIL-M license"
tags: [ocr, document-parsing, vlm, multilingual, pdf-extraction, table-recognition, handwriting, math-recognition, vllm]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: [paddleocr]
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

Chandra OCR 2 is a vision-language model for document parsing that converts images and PDFs
into structured output while preserving layout information.

Strengths:

- **Math:** Equations, handwritten math, non-Latin math notation
- **Tables:** Statistical, financial, and complex multi-column tables
- **Forms:** Checkboxes, registration forms, leases
- **Handwriting:** Cursive writing, handwritten notes
- **Multilingual:** 90+ languages; 77.8% average accuracy across 43 common languages
  (vs 67.6% Gemini 2.5 Flash, 60.5% GPT-5 Mini)
- **Images:** Extracts diagrams/images and adds captions with structured data

## Output Formats

- Markdown (`.md`)
- HTML (`.html`)
- JSON metadata (page info, token counts)

## Usage

```bash
pip install chandra-ocr

# vLLM server (recommended for production)
chandra_vllm
chandra input.pdf ./output --method vllm

# Local HuggingFace inference
pip install chandra-ocr[hf]
chandra input.pdf ./output --method hf

# Interactive app
pip install chandra-ocr[app]
chandra_app
```

## Performance

- olmOCR benchmark: 85.8% overall (vs olmOCR 2: 82.4%, dots.ocr 1.5: 83.9%)
- Throughput: ~1.44 pages/s on H100 (benchmark set); ~2 pages/s real-world estimate

## Licensing

Code is Apache-2.0. Model weights use modified OpenRAIL-M — free for research, personal
use, and startups under $2M funding/revenue. Commercial self-hosting requires a license.
