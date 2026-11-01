---
name: polars
title: Polars
url: "https://github.com/pola-rs/polars"
category: framework
summary: "Rust-core columnar DataFrame library with a multi-threaded, vectorized (SIMD) query engine and lazy query optimizer; Python/Rust/Node/R APIs, Apache Arrow memory model, streaming out-of-core execution, and readers/writers for CSV/JSON/Parquet/Delta/Arrow/databases/cloud storage. MIT."
license: MIT
tags: [dataframes, rust, apache-arrow, query-engine, simd, out-of-core, data-processing, python]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it does

Polars is an open-source DataFrame library for single-machine data manipulation. Its core is written in Rust with a multi-threaded query engine, vectorized/columnar processing, and SIMD, built on the Apache Arrow memory model for zero-copy interchange. It exposes both an eager API and a lazy API; the lazy API runs queries through a query optimizer. A streaming API supports out-of-core processing of datasets larger than memory. APIs are available for Python, Rust, Node.js, and R.

Polars reads and writes CSV and JSON (text); Parquet, Delta Lake, Avro, and Excel (binary); Feather/Arrow IPC; databases (MySQL, Postgres, SQL Server, SQLite, Redshift, Oracle); and cloud object storage (S3, Azure Blob/File).

A commercial managed offering, Polars Cloud, runs the same API with cloud or on-prem deployment; the open-source library is independent of it.

## Mechanical details

- **Install (Python):** `pip install polars`
- **Rust:** add `polars = { version = "x", features = ["lazy", ...] }` to Cargo.toml
- **Node.js:** `nodejs-polars`
- Vendor benchmarks (a derived TPC-H at scale factor 10, on a GCP c3-highmem-22) report large speedups over pandas; benchmark queries are open source.

## Security

MIT licensed. Polars is a data-processing library with no network service surface of its own; it reads/writes files, databases, and cloud storage using credentials the calling process provides. No security flags recorded from the observed material.

## How to use it

pip install polars
