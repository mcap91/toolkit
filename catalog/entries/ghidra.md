---
name: ghidra
title: Ghidra
url: "https://github.com/nationalsecurityagency/ghidra"
category: framework
summary: "Open-source software reverse engineering (SRE) framework from NSA's Research Directorate — disassembly, decompilation, graphing, and scripting for compiled code on Windows, macOS, and Linux"
tags: [reverse-engineering, security, disassembler, decompiler, malware-analysis]
reviewed: 2026-09-16
acquired: 2026-09-16
license: Apache-2.0
security_flags: [known-vulnerabilities-in-some-versions]
overlaps: []
source: unknown
---

## What it does

Ghidra is a software reverse engineering (SRE) framework created and maintained by the NSA Research Directorate. It analyzes compiled code across Windows, macOS, and Linux, providing disassembly, assembly, decompilation, graphing, and scripting. It supports a wide variety of processor instruction sets and executable formats, and can run in both interactive (GUI) and automated (headless) modes. Users can write custom extensions and scripts in Java or Python.

## Differentiators

- Multi-architecture disassembly and decompilation (x86, ARM, MIPS, PowerPC, and dozens of others) through a shared P-code intermediate representation
- Collaborative reverse engineering: multiple analysts can work on the same binary concurrently via a shared Ghidra Server
- Debugger integration with GDB, LLDB, and WinDbg
- Scriptable and extensible via Java or Python; extension development supported through the GhidraDev Eclipse plugin and VS Code project generation from the CodeBrowser
- PyGhidra launcher (`support/pyghidraRun`) for Python-based headless/automated workflows
- Publicly released by NSA in March 2019 at the RSA Conference; developed to address scaling and teaming problems on large SRE efforts

## Mechanical details

- Install (pre-built release): requires JDK 25 64-bit; download `ghidra_<version>_<release>_<date>.zip` from the GitHub Releases page; extract (not over an existing install); launch with `./ghidraRun` (`ghidraRun.bat` on Windows) or `./support/pyghidraRun` for PyGhidra
- Build from source: requires JDK 25 64-bit, Gradle 9.1.0+, Python3 (3.9–3.14) with pip, GCC/Clang + make (Linux/macOS), or Visual Studio 2017+/MSVC Build Tools with Windows SDK and C++ ATL (Windows); fetch dependencies with `gradle -I gradle/support/fetchDependencies.gradle`, then `gradle buildGhidra`; output in `build/dist/`
- Per web search (September 2026), the current stable release is version 12.1.3 (August 18, 2026); GitHub star count reported at roughly 69,800+

## Security

- The GitHub README contains an explicit warning: "There are known security vulnerabilities within certain versions of Ghidra," directing users to Ghidra's Security Advisories page before proceeding
- License: Apache-2.0
- No other security-relevant statements observed in the fetched README
