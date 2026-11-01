---
name: teampcp-miasma-npm-supply-chain-attack-2026
title: TeamPCP/Miasma npm Supply Chain Attack (June 2026)
category: reference
summary: Incident writeup documenting credential-harvesting malware and ~/.claude/settings.json hook persistence — directly relevant to agent-lockdown hardening (WK-0031)
tags: [security, supply-chain, npm, claude-code, incident-report, credential-theft, persistence]
reviewed: 2026-06-10
acquired: 2026-06-10
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---
## What it says

A detailed writeup of the TeamPCP/Miasma npm supply chain attack discovered in June 2026. 32 packages under the `@redhat-cloud-services` npm scope were compromised (approximately 117K weekly downloads), with a second wave hitting 57 additional packages (647K monthly downloads).

The malware capabilities:

- **Credential harvesting:** Collects AWS, GCP, Azure, Kubernetes, SSH, GitHub, and npm tokens from the victim environment.
- **Claude Code persistence:** Plants `SessionStart` hooks in `~/.claude/settings.json` to survive across Claude Code sessions.
- **VS Code persistence:** Injects tasks into `.vscode/tasks.json`.
- **Destructive wipe:** Wipes the home directory if tokens are revoked before the attacker cleans up.

Sources cited: Microsoft Threat Intelligence, StepSecurity, Snyk, Tenable, GitGuardian, Krebs on Security.

Remediation order documented: check then clean then rotate (order matters; rotating before checking can trigger the wipe payload).

## Assessment

`note` rather than `adopt` because this is a passive reference — there is no installable tool or technique to adopt directly. Its value is informational: it establishes the threat model that motivated WK-0031 and the `agent-lockdown` skill, confirms that `~/.claude/settings.json` hooks are a real attack vector, and provides the correct remediation sequence for incident response.

## What to adopt

- **Remediation sequence:** Always check, then clean, then rotate. Premature token rotation can trigger the wipe payload.
- **Hook auditing:** Periodically verify that `~/.claude/settings.json` contains only expected `SessionStart`/`PreToolUse`/`PostToolUse` hooks. The `agent-lockdown` skill (WK-0031) is the proactive countermeasure.
- **Scope scrutiny:** Treat unexpected `@redhat-cloud-services` (or any large-org-scoped) package installs as a supply chain risk until confirmed clean.

## Security

This entry describes a real attack. The content itself is inert reference material; no code from this incident should be executed or copied. The persistence mechanism targeting `~/.claude/settings.json` is directly mitigated by the `agent-lockdown` skill's settings integrity check.
