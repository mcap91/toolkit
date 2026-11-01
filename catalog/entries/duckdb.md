---
name: duckdb
title: DuckDB
url: "https://github.com/duckdb/duckdb"
category: framework
summary: "High-performance in-process analytical (OLAP) SQL database. Rich SQL dialect (window functions, correlated subqueries, nested types), zero-config, embeddable; runs as a standalone CLI and as clients for Python, R, Java, Wasm, etc., with direct querying of CSV/Parquet files and pandas/dplyr integration. MIT."
license: MIT
tags: [database, sql, olap, analytics, embedded, parquet, columnar, in-process]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it does

DuckDB is an in-process analytical SQL database management system designed for fast, reliable, portable, and easy analytical (OLAP) workloads. It provides a rich SQL dialect extending well beyond basic SQL — arbitrary and nested correlated subqueries, window functions, collations, and complex/nested types (arrays, structs, maps) — plus extensions. It runs embedded in the host process with no separate server, available as a standalone CLI and as clients for Python, R, Java, WebAssembly, and more, with deep integrations for packages like pandas and dplyr. Files can be queried directly, e.g. `SELECT * FROM 'myfile.parquet'` or `'myfile.csv'`.

## Mechanical details

- **Install:** see the DuckDB installation page; the Python client is `pip install duckdb`
- **Query files directly:** reference a CSV/Parquet path in the `FROM` clause
- **Build from source:** requires CMake, Python 3, and a C++17 compiler; `make` (release) / `make debug`; `make unit` / `make allunit` for tests

## Security

MIT licensed. DuckDB is an embedded database engine running in-process; it reads/writes local files and, via extensions, can reach remote/cloud data sources using the caller's credentials. No security flags recorded from the observed material.

## How to use it

pip install duckdb
