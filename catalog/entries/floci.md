---
name: floci
title: Floci — Local Cloud Emulators
url: "https://floci.io/"
category: framework
summary: "Local cloud emulators for AWS (119 services, port 4566), Azure (28 services), GCP (25 services), and OCI (8 services) — native binaries compiled with GraalVM Mandrel, 24ms cold start, 13 MiB idle; drop-in LocalStack replacement (same port, zero code changes); real engines (Lambda in Docker, RDS with real PostgreSQL/MySQL, ElastiCache with real Redis); no auth tokens, no accounts, no telemetry; unified CLI and visual dashboard; MIT"
tags: [cloud-emulator, aws, azure, gcp, oci, localstack-alternative, local-development, docker, lambda, s3, ci, terraform, mit]
reviewed: 2026-09-18
acquired: 2026-09-18
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Floci provides standalone cloud emulators for four cloud providers, each running as a native binary with no cloud account or authentication required.

Emulators:
- floci (AWS): 119 services on port 4566; drop-in replacement for LocalStack with same port and zero code changes
- floci-az (Azure): 28 services on port 4577; Blob, Queue, Table, Functions, App Config, Key Vault, Event Hubs, Service Bus
- floci-gcp (GCP): 25 services on port 4588; GCS, Pub/Sub, Firestore, Cloud Run, Cloud SQL, GKE
- floci-oci (OCI): 8 services on port 4599; Object Storage, Identity, Queue, Streaming, KMS, Vault, Functions

Performance: 24ms cold start, 13 MiB idle memory. Compiled with GraalVM Mandrel.

Real engines: Lambda runs in real Docker containers, RDS uses real PostgreSQL/MySQL, ElastiCache runs real Redis. Works with every SDK, CLI, Terraform/OpenTofu module, and test runner.

Developer tools: floci-cli (unified CLI) and floci-ui (visual dashboard to browse resources across all providers).

Positioned as a credential-free alternative to LocalStack, which started requiring an auth token in March 2026.

## Security

- License: MIT for all emulators
- No credentials, API keys, or telemetry
- All operations are local with zero blast radius