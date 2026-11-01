---
name: pdf24-creator
title: PDF24 Creator
url: https://www.pdf24.org/
category: cli-tool
summary: Free Windows desktop app and virtual printer from Geek Software GmbH (Berlin, developed since 2006) for merging, splitting, compressing, converting, OCR'ing (via Tesseract), signing, password-protecting, watermarking, and rearranging PDFs — offline, with no feature limits or paid tier; proprietary freeware funded by ads on PDF24's companion web tools; one patched local-privilege-escalation CVE in its MSI installer
tags:
  - pdf24-creator
  - pdf
  - pdf-tools
  - merge-pdf
  - compress-pdf
  - ocr
  - windows
  - virtual-printer
  - freeware
  - offline
reviewed: 2026-10-29
acquired: 2026-10-29
license: proprietary-freeware
security_flags:
  - "CVE-2023-49147: local privilege escalation via the MSI installer's repair function (msiexec.exe spawns a visible SYSTEM-level cmd.exe); fixed in 11.15.2 (Dec 2023) — update past that version"
overlaps:
  - stirling-pdf
source: instagram
source_url: https://www.instagram.com/reel/DesqA2cFbEe/
---

## What it does

PDF24 Creator is a free Windows desktop application that installs as a virtual PDF printer, so any application's print function can output a PDF. Beyond printing, it merges, splits, compresses, and converts to/from PDF; runs OCR on scanned pages using the bundled Tesseract engine; adds digital signatures and watermarks; sets or removes passwords/encryption; rotates and extracts pages; and provides a basic page editor. All desktop operations run offline — files are processed locally rather than uploaded to a server.

Geek Software GmbH, a Berlin-based company, has developed the product since 2006 (originally named PDFDrucker). It also runs pdf24.org, a set of browser-based PDF tools covering similar operations, monetized through advertising rather than subscriptions. The desktop Creator and the online tools are both free for personal and commercial use, with no feature gating or paid tier; Geek Software's terms of use reserve the right to change this in the future.

## Mechanical details

- Platform: Windows only (desktop app); PDF24's web tools at pdf24.org work from any browser.
- Under the hood: bundles private instances of Apache PDFBox, QPDF, and Ghostscript for PDF manipulation, plus Tesseract for OCR.
- License: proprietary freeware — free to use, not open source; Geek Software's published terms state the installer contains no spyware, adware, toolbars, or co-installed bundleware.
- Distribution: official installer from pdf24.org or Microsoft Store; over 5 million downloads; available in 32 languages.

## Security

- **License:** proprietary freeware, not open source — no public source for independent code audit.
- CVE-2023-49147 (SEC Consult advisory): the MSI installer's repair function (`msiexec.exe /f`) spawned a visible `cmd.exe` running as SYSTEM, letting a local attacker with GUI access escalate privileges; patched in version 11.15.2 (December 2023).
- No confirmed adware/spyware bundling in the official installer from pdf24.org or the Microsoft Store; third-party download mirrors have distributed repackaged installers flagged as malicious by sandbox tools (any.run) — download only from the official source.
- Revenue model is advertising on the companion web tools, not data sale; no independent telemetry audit reviewed here.
