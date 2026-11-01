---
name: skills-visibility
title: skills-visibility (Evil Martians)
url: "https://github.com/evilmartians/agent-skills/blob/main/skills/skills-visibility/SKILL.md"
category: skill
summary: "Agent skill (by Evil Martians) that walks through publishing a discoverable, installable catalog of agent skills: lay each skill out as skills/<name>/SKILL.md in a git repo, classify its shape (single-file / multi-file / bundle), re-host and hash the served bytes from a domain you control, build flat reproducible tar.gz archives, and publish a .well-known/agent-skills/index.json discovery index (agentskills.io schema / Cloudflare's RFC 8615 extension) so npx skills, gh skill, and Claude's plugin marketplace resolve them. Emphasizes sha256 integrity digests and offering multiple install commands."
tags: [agent-skills, skill, distribution, discovery-index, well-known, packaging, claude-code, integrity, evil-martians]
reviewed: 2026-08-17
acquired: 2026-08-17
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---
## What it does

A skill that tells an agent how to publish *many* agent skills so installers and coding agents can discover and install them without being handed a URL each time — "what llms.txt does for pages, done for skills." The mechanism is a discovery index at a well-known path; get it right and `npx skills`, `gh skill`, and Claude's plugin marketplace all resolve your skills. It is scoped to distribution/discovery, explicitly *not* authoring a single skill's content or making web pages LLM-readable.

## Mechanical details

- **Layout & shapes:** each skill as `skills/<name>/SKILL.md` in a git repo (required — `gh skill` and Claude's marketplace resolve directly from the repo). Classify each as single-file (just SKILL.md, `type: skill-md`), multi-file (SKILL.md + siblings → flat `<name>.tar.gz`, `type: archive`), or bundle (one repo publishing several skills; a container, not a skill).
- **Serve + hash from a domain you control:** download each payload from its repo, write it into your own published output, and hash *that* file. Never point the index at `raw.githubusercontent.com` (bytes you don't control → digest drift → broken installs). Re-hosting lets you track a branch instead of pinning a commit ("always latest" with a correct hash), but protects only the trip to the installer — reviewing repo contents is still required.
- **Reproducible archives:** build and hash in one pass; flat tarball (SKILL.md at root, no wrapping folder). For determinism: `chmod 0644`, `tar --sort=name --owner=0 --group=0 --numeric-owner --mtime='UTC 2020-01-01'`, `gzip -n`.
- **Discovery index:** `.well-known/agent-skills/index.json` served as `application/json`; exactly two top-level keys (`$schema`, `skills`); five per-skill fields (`name` unique/valid-slug, `description`, `type`, `url` on your domain, `digest` `sha256:<hex>`). Schema: `schemas.agentskills.io/discovery/0.2.0` (RFC 8615 extension from Cloudflare). Bundles are represented only by their member skills.
- **Install methods to offer:** `npx skills add https://…/agent-skills`, `claude plugin marketplace add`/`install` (best for bundles), `gh skill install`, and dependency-free `curl | tar`. Optional install analytics; a Verify checklist (content-type, JSON validity, digest match, flat tarball, clean `npx skills` install).

## Security

- **Integrity is central:** a conformant installer MUST re-hash a downloaded payload and MUST NOT use content that fails the digest — a wrong/undeclared digest blocks the install rather than degrading it. The skill's core security point is publish-time integrity: hash the exact bytes you serve, from where you serve them.
- **Threat noted:** re-hosting gives consistency, not immunity from upstream — a malicious/bad push is re-hosted and hashed faithfully; review the branch you track.
- **License:** not stated in the fetched SKILL.md (recorded as NOASSERTION); check the `evilmartians/agent-skills` repo LICENSE.
- The skill is instructional text (no executable payload of its own); it directs the agent to run `tar`/`curl`/`gzip` and publish files.
