---
name: windows-god-mode
title: Windows 11 God Mode
url: "https://www.tomshardware.com/how-to/enable-god-mode-windows-11"
category: reference
summary: "Windows 10/11 trick — create a folder named GodMode.{ED7BA470-8E54-465E-825C-99712043E01C} to get a flat list of 200+ Control Panel shortcuts; useful for quick access to buried settings like environment variables, audio devices, power options"
tags: [windows, tips, productivity]
reviewed: 2026-06-22
acquired: 2026-06-22
license: ""
security_flags: []
overlaps: []
source: unknown
---

## What it says

Create a folder on the Windows desktop named `GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}`. The folder becomes a flat, searchable list of 200+ Control Panel settings organized by category (Security, Power Options, Network, etc.). Individual shortcuts can be dragged to the desktop for one-click access.

Useful shortcuts it surfaces:
- Environment variables (normally Settings → System → About → Advanced System Settings)
- Audio device management
- Printer settings
- Bluetooth settings
- Power options

## Assessment

Simple Windows power-user trick. Relevant when working on a Windows dev machine and needing quick access to system settings — particularly environment variables, which matter for agent tool configuration (API keys, PATH, etc.). Not a tool to adopt, just a reference to know about.

## Security

No security concerns — uses a built-in Windows shell CLSID, not third-party software.