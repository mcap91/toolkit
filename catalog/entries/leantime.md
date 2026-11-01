---
name: leantime
title: Leantime
url: "https://github.com/leantime/leantime"
category: framework
summary: "Open-source project management system designed for non-project managers; combines strategy, planning, and execution with neurodivergence-friendly UX (ADHD, dyslexia, autism); self-hosted PHP/MySQL with Docker support, AGPLv3"
tags: [project-management, self-hosted, kanban, gantt, php, docker, neurodivergent, adhd, open-source]
reviewed: 2026-07-12
acquired: 2026-07-12
license: AGPL-3.0
security_flags: [self-hosted, requires-database]
overlaps: []
source: unknown
---

## What it is

Leantime is a self-hosted, open-source project management system positioned as an alternative to ClickUp, Monday, Asana, and Jira. It targets non-project-manager users and is explicitly designed with neurodivergent users in mind (ADHD, dyslexia, autism).

## Features

- **Task management.** Kanban boards, Gantt charts, table/list/calendar views, unlimited subtasks and dependencies, sprint management, milestone management.
- **Strategy tools.** Goal and metrics tracking, Lean Canvas, Business Model Canvas, SWOT analysis, risk analysis.
- **Knowledge management.** Wikis/docs, idea boards, retrospectives, comments/discussions on everything.
- **Administration.** LDAP/OIDC integration, two-factor auth, per-project permissions, multiple user roles, plugin/API extensibility.
- **Integrations.** Slack, Mattermost, Discord; file storage via S3 or local filesystem; JSON-RPC API.
- **Localization.** Available in 20+ languages via Crowdin.

## Technical requirements

PHP 8.2+, MySQL 8.0+ or MariaDB 10.6+, Apache/Nginx (IIS with modifications). Official Docker image available on Docker Hub. Development environment includes MySQL, maildev, phpMyAdmin, S3 ninja, and Xdebug.

## Security

AGPLv3 license with an exception for plugins in `/app/Plugins` which may use other licenses including proprietary. Self-hosted — data stays on user infrastructure. Supports 2FA, LDAP, OIDC for authentication. No external telemetry mentioned in the README. The plugin marketplace includes paid/enterprise options under separate licensing.