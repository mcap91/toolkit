---
name: pandera
title: Pandera
url: "https://github.com/unionai-oss/pandera"
category: framework
summary: "Union.ai's dataframe validation library: define schemas (object-based DataFrameSchema or class-based DataFrameModel) with typed columns, built-in and custom checks, and validate pandas/polars/pyspark and other dataframe-like objects for correctness in data pipelines. MIT."
license: MIT
tags: [data-validation, schema, pandas, polars, pyspark, dataframes, testing, union-ai]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it does

Pandera is an open-source data-validation library (a Union.ai project) that provides an expressive API for validating dataframe-like objects, aiming to make data pipelines more readable and robust with statistically typed dataframes. Schemas can be defined two ways: an object-based API (`pa.DataFrameSchema({...})` with `pa.Column(type, pa.Check...)`) or a class-based API (`class Schema(pa.DataFrameModel)` with typed fields, `pa.Field(...)`, and `@pa.check` methods). Checks cover types, ranges, membership, and arbitrary custom predicates. It supports multiple backends including pandas, polars, and pyspark.

As of v0.24.0 the recommended import for pandas is `import pandera.pandas as pa`; using the top-level `pandera` module for pandas structures emits a `FutureWarning` and is slated for deprecation in v0.29.0.

## Mechanical details

- **Install:** `pip install 'pandera[pandas]'` (or `uv pip install …`, or `conda install -c conda-forge pandera-pandas`); extras select the dataframe backend
- **Validate:** `schema.validate(df)` / `Schema.validate(df)` returns the validated frame or raises on failure
- Backends installed via extras (pandas, polars, pyspark, and more)

## Security

MIT licensed. Pandera is an in-process validation library with no network surface; custom checks execute user-provided Python. No security flags recorded from the observed material.

## How to use it

pip install 'pandera[pandas]'
