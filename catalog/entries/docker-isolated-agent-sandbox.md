---
name: docker-isolated-agent-sandbox
title: Docker-Isolated Agent Sandbox Pattern
category: agent-pattern
summary: "Architecture pattern for running multiple AI coding agents in Docker containers with filesystem isolation — agents access only explicitly shared files and connections, work in git worktrees, all changes visible and reviewable in git; includes port collision prevention, resource exhaustion guards, zombie process cleanup, and merge conflict prevention; reported 38% token savings vs uncontained agents"
tags: [agents, docker, isolation, sandbox, worktrees, multi-agent, resource-management, security]
reviewed: 2026-09-18
acquired: 2026-09-18
license: ""
security_flags: []
overlaps: []
source: unknown
---

## What it does

A practitioner-described architecture for running multiple AI coding agents concurrently in isolated Docker containers:

- Filesystem isolation: agents run inside Docker, accessing only files explicitly dropped in and connections explicitly granted
- Git-backed workspace: entire filesystem agents work in lives in git, making all changes visible and reviewable
- Worktree isolation: agents work in git worktrees to prevent merge conflicts between concurrent sessions
- Resource management: port collision prevention, resource exhaustion guards, and zombie process cleanup (e.g. leftover browser sessions consuming RAM)

Described as "a VSCode inside docker that's focused on agentic work." Reported benefit: 38% token savings over the past month compared to uncontained agent operation.

The pattern is described at a conceptual level without naming a specific open-source project.

## Security

- Isolation is the primary design goal
- Git-backed changes provide full auditability