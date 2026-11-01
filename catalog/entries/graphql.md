---
name: graphql
title: GraphQL
url: "https://graphql.org/"
category: reference
summary: "Open-source query language for APIs with strongly-typed schemas — request exactly the data needed, retrieve multiple resources in one request, evolve without versioning; governed by the GraphQL Foundation under the Linux Foundation; libraries available in most languages"
tags: [api, query-language, schema, web-development, linux-foundation]
reviewed: 2026-07-06
acquired: 2026-07-06
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Open-source query language for APIs and a server-side runtime. Clients define the structure of the data they need, and the server returns exactly that shape — no over-fetching or under-fetching. APIs are organized around types and fields rather than endpoints, with a strongly-typed schema that enables tooling, validation, and self-documentation.

**Five design principles:** hierarchical (queries mirror UI structure), strongly-typed (syntactic validation before execution), client-specified (clients control what data they receive at field level), introspective (schema is queryable), and community-driven.

## Differentiators

- **Precision** — request exactly what's needed, get exactly that back
- **Single request** — follow relationships between data in one query, replacing multiple REST API calls
- **Type-safe schema** — self-documenting, clear error messages, IDE autocompletion
- **Versionless evolution** — add fields and types without impacting existing queries; deprecate instead of version
- **Storage-agnostic** — works with databases, REST APIs, and third-party services behind a single schema
- **Fragment colocation** — define each UI component's data needs alongside it

## Mechanical details / What to adopt

- Open-sourced by Facebook in 2015, in production at Facebook since 2012
- Governed by the GraphQL Foundation (Linux Foundation) since 2018
- Server implementations available in most languages
- GraphiQL — open-source in-browser IDE for exploring GraphQL APIs

## Security

Specification licensed under OWFa 1.0. Reference implementations typically MIT licensed. Inherits standard API security concerns — requires proper access controls, query depth/complexity limits to prevent denial-of-service via deeply nested queries.