---
name: sqltools
title: SQLTools
url: "https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools"
category: framework
summary: "VS Code extension for database management — connects to MySQL, PostgreSQL, SQL Server, SQLite, CockroachDB, MariaDB, TiDB via official drivers, plus 25+ community drivers (DuckDB, BigQuery, Snowflake, Oracle, ClickHouse, etc.); SQL formatter/beautifier, query runner with history and bookmarks, connection explorer, INSERT query generator; pluggable driver architecture; maintained by George James Software; MIT"
tags: [vscode, database, sql, mysql, postgresql, sqlite, duckdb, snowflake, bigquery, extension, query-runner]
reviewed: 2026-09-18
acquired: 2026-09-18
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

SQLTools is a set of VS Code extensions providing database management directly inside the editor. Core extension plus separate driver packages for each database engine.

Features:
- Connection management with explorer, add/edit/remove
- Query runner with history, bookmarks, and result display
- SQL beautifier and formatter
- INSERT query generator from table structure
- Pluggable driver architecture: install only the drivers you need

Official drivers: MySQL, PostgreSQL, SQL Server, SQLite, CockroachDB, MariaDB, TiDB.

Community drivers (25+): Amazon Redshift, ClickHouse, Databricks, Db2, DolphinDB, DuckDB, Google BigQuery, Google Cloud Spanner, Hive, InterSystems IRIS, kdb+/q, Mimer SQL, Netezza, Oracle, SAP HANA, SingleStore, Snowflake, Teradata, Trino, Vertica, and more.

Maintained by Matheus Teixeira and George James Software with community contributions.

## Security

- License: MIT
- Driver model: separate packages per database, install only what you need