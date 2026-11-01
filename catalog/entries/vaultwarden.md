---
name: vaultwarden
title: Vaultwarden
url: "https://github.com/dani-garcia/vaultwarden"
category: framework
summary: Production-grade self-hosted Bitwarden-compatible password server in Rust; fraction of the resource footprint of the official server
tags: [password-manager, self-hosted, bitwarden, rust, docker, security, secrets]
reviewed: 2026-06-10
acquired: 2026-06-10
license: AGPL-3.0
security_flags: [stores-credentials, requires-https, backup-critical]
overlaps: []
source: unknown
---

## What it does

Vaultwarden is an unofficial, community-maintained reimplementation of the Bitwarden server API, written in Rust. It is fully compatible with all official Bitwarden clients — desktop apps, browser extensions, mobile apps, and the CLI — while running on a fraction of the resources required by the official server. A single container with a small SQLite database is sufficient for personal or small-team deployments.

The server implements nearly the complete Bitwarden feature surface: personal vault, organizations with collections and sharing, member roles and groups, policies, directory connector, emergency access, event logs, admin password reset, and all major MFA methods (TOTP authenticator, email, FIDO2/WebAuthn, YubiKey, Duo). It also bundles a modified Bitwarden Web Vault client directly in the container image, so no separate web-client deployment is needed.

Vaultwarden is distributed as container images on ghcr.io, docker.io, and quay.io, and can also be built from source. It uses the Rocket web framework and stores data in SQLite (default), MySQL, or PostgreSQL. The recommended production setup pairs it with a TLS-terminating reverse proxy (nginx, Caddy, Traefik).

## Assessment

Vaultwarden is the de-facto standard for self-hosted password management in the open-source community. It is extremely mature — originally released as `bitwarden_rs`, it has been actively maintained for years with a large contributor base and a thorough GitHub issue tracker. The Rust implementation gives strong memory-safety guarantees compared to the official .NET server. One of its active maintainers is now employed by Bitwarden and permitted to contribute on their own time, adding implicit alignment with upstream protocol changes.

For individuals, families, and small organizations that want full Bitwarden client compatibility without the overhead of the official server stack (which requires Docker Compose with multiple services), Vaultwarden is an unambiguous adopt. The container image is small, startup is fast, and the SQLite default makes backup trivial (single file). The `adopt` verdict reflects that this is battle-tested infrastructure, not experimental software.

The `framework` category fits because Vaultwarden is self-hosted server infrastructure that agent workflows can integrate with via the Bitwarden CLI (`bw`) or Secrets Manager SDK for secure credential retrieval. Its relevance to an agent toolkit is primarily as a secrets backend.

## Mechanical details

**Installation (Docker):**
```
docker run --detach --name vaultwarden \
  --env DOMAIN="https://vw.domain.tld" \
  --volume /vw-data/:/data/ \
  --restart unless-stopped \
  --publish 127.0.0.1:8000:80 \
  vaultwarden/server:latest
```

**Docker Compose** (`compose.yaml`):
```yaml
services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    restart: unless-stopped
    environment:
      DOMAIN: "https://vw.domain.tld"
    volumes:
      - ./vw-data/:/data/
    ports:
      - 127.0.0.1:8000:80
```

A reverse proxy (nginx, Caddy, or Traefik) is required for TLS in production. The data directory (`/vw-data/` or `./vw-data/`) contains the SQLite database and attachments — back this up regularly. For agent integration, use the official `bw` Bitwarden CLI or the Bitwarden Secrets Manager SDK to retrieve secrets from a running Vaultwarden instance.

## Security

**License**: AGPL-3.0. Copyleft applies to modifications distributed as network services — relevant if you fork and host publicly, not for typical self-hosted personal use.

**Credential storage**: Vaultwarden stores encrypted password vaults. Vault encryption happens client-side using keys derived from the master password; the server never sees plaintext passwords. However, the server does store encrypted vault data, so the host machine and database must be treated as sensitive infrastructure.

**Deployment security flags**:
- `stores-credentials`: The server stores encrypted user vault data — compromise of the host exposes encrypted blobs plus any unencrypted metadata (URLs, usernames).
- `requires-https`: Must be served over HTTPS; running over plain HTTP exposes authentication tokens. The project warns against this in its docs.
- `backup-critical`: Data loss is irreversible for users without external backups. The project disclaimer explicitly notes no liability for data loss.

**Mitigations**: Use a reverse proxy for TLS termination. Enable firewall rules to restrict access. Perform regular automated backups of the data directory. Use strong admin credentials and restrict the `/admin` panel by IP if possible. Keep the container image updated — the project releases regularly and the community actively tracks CVEs relevant to the Bitwarden protocol.
