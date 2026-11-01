---
name: paddleocr
title: PaddleOCR
url: "https://github.com/PaddlePaddle/PaddleOCR"
category: framework
summary: "PaddleOCR provides three product lines for document understanding — PP-OCRv6 scene text recognition, PP-StructureV3 document-structure-to-Markdown/JSON conversion, and the PaddleOCR-VL 0.9B-parameter vision-language model for full document parsing across 109 languages"
tags: [ocr, document-parsing, vision-language-model, multilingual, pdf-extraction, text-recognition, table-recognition, rag, paddlepaddle]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: []
license: Apache-2.0
security_flags: []
source: unknown
---

## What it does

PaddleOCR provides three product lines for document understanding:

### PP-OCRv6 (Scene OCR)
Universal text recognition for natural scenes — IDs, street views, books, industrial
components. Three model tiers: tiny (1.5M params), small (7.7M), medium (34.5M). Single
unified model covers Chinese, English, Japanese, and 46 Latin-script languages. 5.2x CPU
inference speedup over v5.

### PP-StructureV3 (Document Structure)
Converts complex PDFs and images into Markdown or JSON with fine-grained coordinate
information including table cell coordinates, text coordinates, and layout regions.

### PaddleOCR-VL (Vision-Language Model)
0.9B parameter VLM for document parsing — 96.3% accuracy on OmniDocBench v1.6. Handles
text, formulas, tables, charts, ancient documents, rare characters, and seals. Supports
109 languages. Structured output in Markdown and JSON.

## Deployment

- **Inference backends:** PaddlePaddle, ONNX Runtime, OpenVINO, TensorRT
- **Hardware:** NVIDIA GPU, Intel CPU, Kunlunxin XPU, Apple M-series, NVIDIA RTX 50 series
- **SDKs:** Python, C++, C#, Java, browser (PaddleOCR.js)
- **Serving:** Docker-based high-stability service deployment

## Ecosystem Integration

Deeply integrated with Dify (agentic workflows), RAGFlow (RAG engine), Pathway (ETL),
Cherry Studio (LLM client), Haystack (AI orchestration), and OmniParser (GUI agents).

## Usage notes

- On a real-world IRS depreciation table (3 years, dollar/percentage/deduction columns), PaddleOCR's default table settings on a regular-resolution PDF export correctly read all 3 dollar amounts but mislinked them to years (left first two years blank, merged years 2 and 3 into one row) — a numeric-only check would have missed the error. A higher-resolution export run through PaddlePaddle's hosted Hugging Face demo, which uses a separate table-cell-detection model, correctly linked amounts to years but left the percentage/deduction headers blank. Takeaway: validate table-structure accuracy against your specific document layout, not just whether individual values are read correctly. (source: https://www.instagram.com/reel/DecS5IkjwSA/)

- PP-DocLayoutV3, the layout-detection model used by PP-StructureV3/PaddleOCR-VL (`from paddleocr import LayoutDetection`), predicts block reading order jointly with block detection in a single model rather than using a separate ordering model — it compares every pair of detected blocks in parallel, estimates which should come first, and sorts blocks by the resulting pairwise vote counts. On OmniDocBench, this joint approach scored a 0.041 ordering error versus 0.189 when reading order was learned by a separate model with the same text-reading model held constant. (source: https://www.instagram.com/reel/DeZgZk7AhlR/)

- PP-DocLayoutV3 segments regions with non-rectangular (angled/warped-fitted) bounding boxes rather than axis-aligned rectangles — useful for crooked scans, product photos shot from different angles, security footage, and robotics where camera angle varies. The video contrasts this with an axis-aligned approach, where a bounding box has to be oversized to contain curved/angled text, causing unrelated text (e.g., part of a title) to fall inside a paragraph's box — a problem the creator says commonly affects user intake forms and identity documents like driver's licenses. (source: https://www.instagram.com/reel/DePNK6AgMsN/)

- On an IRS tax-computation worksheet table (income-range rows with tax calculations), PaddleOCR's table extraction misread the upper limit of the "over $197,300" row as $50,525 instead of $250,000 — making the row read "over $197,300 but not over $50,525," a logically inconsistent range that a $200,000 income cannot match. (source: https://www.instagram.com/reel/DeUWz-7FAgX/)
