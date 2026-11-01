---
name: microsoft-activation-scripts
title: Microsoft Activation Scripts (MAS)
url: "https://massgrave.dev/"
category: cli-tool
summary: "Open-source Windows and Office activator using HWID, Ohook, TSforge, and Online KMS methods — batch-script-based; HWID for permanent Windows 10/11 activation, Ohook for permanent Office activation, TSforge for permanent Windows/ESU/Office, Online KMS for 180-day renewable activation; includes edition changing and troubleshooting; v3.12 (July 2026)"
tags: [windows, office, activation, batch-scripts, hwid, kms, open-source]
reviewed: 2026-09-18
acquired: 2026-09-18
license: ""
security_flags: [powershell-remote-execution]
overlaps: []
source: unknown
---

## What it does

Microsoft Activation Scripts (MAS) provides multiple methods for activating Windows and Office products:

- HWID (Hardware ID): permanent Windows 10/11 activation tied to hardware fingerprint; requires internet
- Ohook: permanent Office activation; works offline
- TSforge: permanent activation for Windows, ESU, and Office; mostly offline
- Online KMS: 180-day renewable activation for Windows/Office; lifetime with scheduled renewal task

Primary install: PowerShell one-liner that downloads and executes a script. Also available as a downloadable offline package. Built entirely on batch scripts. Includes utilities for changing Windows/Office editions and checking activation status.

Latest release: v3.12 (July 4, 2026). Hosted on GitHub, Azure DevOps, and self-hosted Git.

## Security

- Remote execution: primary install downloads and executes a script from a remote URL via PowerShell
- Open-source: fully open batch scripts, auditable on GitHub
- The project warns users to verify URLs before executing and to watch for third-party malware disguised as MAS