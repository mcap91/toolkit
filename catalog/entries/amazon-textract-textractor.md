---
name: amazon-textract-textractor
title: Amazon Textract Textractor
url: "https://github.com/aws-samples/amazon-textract-textractor"
category: cli-tool
summary: "Textractor is a Python wrapper around Amazon Textract for document intelligence — handles API calls, response parsing, and output formatting for text recognition, table extraction, form extraction, ID analysis, and expense processing"
tags: [ocr, document-extraction, aws, textract, table-extraction, form-extraction, pdf, cloud-service]
reviewed: 2026-09-02
acquired: 2026-09-02
overlaps: [paddleocr]
license: Apache-2.0
security_flags: [requires-cloud-credentials]
source: unknown
---

## What it does

Textractor is a Python wrapper around Amazon Textract that simplifies document intelligence
workflows. It handles API calls, response parsing, and output formatting in one package.

Capabilities:

- **Text recognition:** `detect_document_text()` — extract lines and words from images/PDFs
- **Table extraction:** `analyze_document(features=[TABLES])` — extract tables, export to
  Excel/CSV/DataFrame
- **Form extraction:** `analyze_document(features=[FORMS])` — extract key-value pairs with
  fuzzy matching via `document.get("email")`
- **ID analysis:** `analyze_id()` — extract structured fields from identity documents
- **Expense processing:** `analyze_expense()` — extract receipt/invoice fields (totals,
  line items, vendors)

Supports image files, PDFs, bytes, and S3 paths. Both synchronous and asynchronous APIs.

## Installation

```bash
pip install amazon-textract-textractor            # minimal (Lambda-ready)
pip install "amazon-textract-textractor[pandas]"  # + DataFrame/CSV export
pip install "amazon-textract-textractor[pdfium]"  # + PDF rasterization
pip install "amazon-textract-textractor[torch]"   # + ML-based word search
```

## CLI

```bash
textractor analyze-document input.png output.json --features TABLES --overlay TABLES
```

## Cost Note

Uses Amazon Textract APIs — calls incur AWS charges. Requires AWS credentials configured
(profile, environment variables, or IAM role).
