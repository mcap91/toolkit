---
name: hackingtool-plugin
title: Hackingtool Plugin
url: "https://github.com/AKCodez/hackingtool-plugin"
category: plugin
summary: "Claude Code plugin wrapping 183 pentesting/OSINT tools from Z4nzu/hackingtool — auto-selects backend (native Bash, WSL, Docker with purpose-built images), 56 plug-and-play / 127 environment-dependent tools across 20+ categories; MIT"
tags: [pentesting, osint, security, claude-code-plugin, docker, offensive-security]
reviewed: 2026-06-23
acquired: 2026-06-23
license: MIT
security_flags: [runs-offensive-tools, requires-authorization, sudo-required-for-many]
overlaps: [shannon]
source: unknown
---

## What it does

A Claude Code plugin that wraps Z4nzu/hackingtool's collection of 183 pentesting and OSINT tools into a skill that Claude can invoke directly. The plugin's `ht_run.py` picks the right execution backend automatically:

- **Native** (Linux/macOS): `bash -lc <cmd>`
- **WSL** (Windows + real distro): `wsl -d <distro> -- bash -lc <cmd>`
- **Docker** (anywhere): Purpose-built images for each tool category

**Tool categories** (183 total, 56 plug-and-play / 127 environment-dependent):
- Port scanning: nmap, masscan, rustscan
- Subdomain recon: subfinder, amass, httpx
- Vuln scanning: nuclei, katana
- OSINT: holehe, maigret, spiderfoot, theHarvester
- Secrets: trufflehog, gitleaks
- Web attack: ffuf, gobuster, testssl.sh, wafw00f
- SQL injection: sqlmap, nosqlmap
- Post exploitation: chisel, evil-winrm, havoc, ligolo-ng, PEASS-ng, pwncat-cs, sliver
- Active Directory: impacket, netexec, certipy, kerbrute, bloodhound
- Cloud security: pacu, prowler, scoutsuite, trivy
- Forensics: binwalk, volatility, pspy
- Mobile: frida, mobsf, objection
- And more: phishing recon, wireless, steganography, reverse engineering, XSS

Docker images are mapped per-tool (instrumentisto/nmap, projectdiscovery/nuclei, etc.) with a kali-rolling fallback. Tools auto-retry with elevated privileges on permission errors.

## Assessment

Comprehensive offensive security toolkit with impressive engineering — the backend auto-detection (native/WSL/Docker) and per-tool Docker image mapping are well-designed. The 56 plug-and-play tools (nmap, subfinder, nuclei, trufflehog, gitleaks, etc.) cover the most common pentesting workflows.

Important context: this is explicitly for authorized security testing, bug bounty, CTFs, and research. Many tools (phishing, DDOS, RAT, wireless attacks) require physical hardware, sudo, or should only be used with explicit written authorization against owned targets.

The kali-rolling fallback for unmapped tools means first-use pulls a ~2GB image. The `--install` flag for native/WSL backends runs tool-specific install commands — review these before running.

## Mechanical details

```bash
# Install into Claude Code
/plugin marketplace add AKCODEZ/hackingtool-plugin
/plugin install hackingtool@hackingtool-marketplace

# Then just describe what you want:
# "recon example.com"
# "scan my repo for vulnerabilities"
```

Tool runner: `ht_run.py <tool_id> [args]`
Environment detection: `ht_env.py`
Tool index: `data/tools.json` (regenerate with `ht_index.py`)

## Security

- **License**: MIT (plugin wrapper); upstream Z4nzu/hackingtool also MIT
- **Authorization required**: For authorized security testing only — many tools perform active scanning, exploitation, or credential attacks
- **Sudo**: 127 of 183 tools require elevated privileges
- **Docker images**: Per-tool from known publishers (projectdiscovery, trufflesecurity, etc.); kali-rolling fallback is large
- **Auto-retry with sudo**: `ht_run.py` auto-retries with elevated privileges on permission errors — could escalate unintentionally
- **No sandboxing of tool output**: Tool results returned as structured JSON directly to Claude