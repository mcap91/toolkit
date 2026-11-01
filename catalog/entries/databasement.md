---
name: databasement
title: Databasement
url: "https://github.com/David-Crty/databasement"
category: framework
summary: "Self-hosted database backup manager with web UI — schedule, backup, and restore MySQL, PostgreSQL, MariaDB, SQL Server, MongoDB, SQLite, Firebird, and Redis to S3/SFTP/Samba/Azure Blob/local storage; SSH tunnels, remote agents, GFS retention, AES-256 encryption, cross-server restore, scheduled restores, built-in Adminer browser, multi-tenant RBAC with OAuth/SSO, REST API and MCP server; single Docker container; MIT"
tags: [database, backup, restore, self-hosted, docker, mcp-server, mysql, postgresql, mongodb, sqlite, ssh-tunnel, s3, encryption]
reviewed: 2026-09-18
acquired: 2026-09-18
license: MIT
security_flags: []
overlaps: []
source: unknown
---

## What it does

Databasement is a self-hosted web application for managing database backups across 8 database engines (MySQL, PostgreSQL, MariaDB, SQL Server, MongoDB, SQLite, Firebird, Redis/Valkey).

Key features:
- Automated backups on daily/weekly schedules with simple time-based or GFS (grandfather-father-son) retention policies
- Compression: gzip, zstd (20-40% better compression), or AES-256 encryption
- Storage targets: local disk, S3-compatible (AWS S3, MinIO), Azure Blob Storage, Samba/SMB, SFTP/FTP
- SSH tunnels for databases in private networks through bastion/jump servers
- Remote agents: lightweight agent connects out over HTTPS from firewalled networks, dumps locally, uploads to storage
- Cross-server restore: restore snapshots from production to staging or between compatible servers
- Scheduled restores: recurring prod-to-staging refreshes replaying the latest completed snapshot
- Built-in Adminer data browser for MySQL, PostgreSQL, and SQLite (admin-enabled, role-gated)
- Multi-tenant organizations with RBAC, OAuth/SSO (Google, GitHub, GitLab, OIDC), optional 2FA
- Notifications: Email, Slack, Discord, Telegram, Pushover, Gotify, Webhook
- REST API and MCP server for scripting, CI/CD, and AI assistant integration

Deployment: single Docker container with built-in web server, queue worker, and scheduler. Also supports Docker Compose, Kubernetes (Helm), and native Ubuntu.

## Security

- License: MIT
- Encryption: AES-256 for backup encryption
- Auth: RBAC, OAuth/SSO, optional 2FA
- Network: SSH tunnel support; remote agents connect outbound only