---
name: claude-projects
title: Claude Projects
url: "https://support.claude.com/en/articles/9517075-what-are-projects"
category: reference
summary: "Anthropic support documentation for Claude Projects — persistent workspaces with an uploaded-file knowledge base and custom instructions across claude.ai chat, Cowork, and Claude Code, plus a September 2026 beta redesign (Claude Code first) that turns a project into one coordinator conversation dispatching parallel cloud-hosted worker threads"
tags: [claude, anthropic, projects, claude-code, rag, knowledge-base, documentation, cowork]
reviewed: 2026-09-25
acquired: 2026-09-25
license: proprietary
security_flags: [proprietary-feature, hosted-saas-only]
overlaps: []
source: unknown
---

## What it says

Official Anthropic Help Center article explaining the Projects feature, describing two versions that coexist as of this writing.

**Current (established) version**: a project is a self-contained workspace bundling a chat history, an uploaded-file knowledge base, and custom project instructions (e.g. tone, role framing) that Claude references across every chat scoped to that project — distinct from a plain chat, which does not persist this context.

**New version (beta, rolling out from Claude Code first)**: a project becomes a single ongoing conversation. The user states needs as they come up; Claude decomposes the work into parallel threads that run as cloud sessions and keep going after the user disconnects. Every thread starts from the project's files, connected repositories, instructions, and memory. A project-level "Library" collects both user-added files and Claude-produced outputs.

## Key takeaways

- The beta redesign shifts the unit of work from "chat with attached files" to "coordinator conversation that spawns cloud worker threads" — external reporting on the September 17, 2026 Anthropic announcement (MarkTechPost, ClaudeDevs/X, XenoSpectrum) describes each thread as an independent Claude Code cloud session with its own git branch and repo copy, able to open pull requests, run tests, and further fan out into subagents; a cap of 200 new threads/day is reported during beta.
- RAG-backed knowledge base: on paid plans, project knowledge auto-switches to Retrieval Augmented Generation once content approaches context limits, expanding effective knowledge-base capacity "up to 10x" per Anthropic's own description, rather than loading all uploaded content every turn.
- Team/Enterprise plans add sharing and permission levels so multiple members can contribute documents and chats to one shared project.
- Existing (current-version) projects in chat and Cowork keep working unchanged and will be migrated to the new version as the beta rollout expands to those surfaces; only Claude Code is on the new version today.

## Mechanical details

- Availability (beta redesign): limited to select Pro/Max subscribers who use Claude Code, surfaced as "Projects" in the claude.ai/code sidebar and the Code tab of the Claude desktop app; a waitlist exists for Pro/Max users without access yet; chat, Cowork, Team, and Enterprise access is planned to follow.
- Usage: project activity draws from the plan's normal usage allotment; running several parallel threads at once consumes usage faster than a single chat.
- File uploads (current version) support documents, text, code, and other file types into the knowledge base; users can set per-project custom instructions.
- The article cross-references related first-party docs: "How can I create and manage projects?", "Usage limit best practices", "Retrieval augmented generation (RAG) for projects", "Use Claude's chat search and memory to build on previous context", "Organize your tasks with projects in Claude Cowork", and "Project visibility and sharing" (Team/Enterprise permission levels and sharing options).

## Security

Anthropic first-party hosted-SaaS documentation, not installable software — no source code, license terms beyond Anthropic's own ToS, or dependency surface to assess. Data handling for uploaded knowledge-base files and cross-thread memory is referenced only at a policy-pointer level in this article (linking out to a separate "Project visibility and sharing" page) and is not detailed in the fetched content itself.
