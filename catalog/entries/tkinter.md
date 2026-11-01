---
name: tkinter
title: tkinter
url: "https://docs.python.org/3/library/tkinter.html"
category: framework
summary: "Python's standard library interface to the Tcl/Tk GUI toolkit, bundled with CPython on Windows, macOS, and Linux"
tags: [gui, python, tcl-tk, standard-library, desktop, cross-platform]
reviewed: 2026-09-16
acquired: 2026-09-16
license: PSF-2.0
security_flags: []
overlaps: []
source: unknown
---

## What it does

tkinter is Python's standard library binding to Tcl/Tk, used to build desktop GUI applications. It ships with CPython on Windows, macOS, and Linux (on some Linux distributions the Tk runtime is a separate OS package), so no `pip install` is required for the core module. It provides widgets (buttons, labels, entries, text boxes, canvas, frames, menus, and standard dialogs), event-driven programming via callback binding, and three geometry managers (`pack`, `grid`, `place`) for layout. The `tkinter.ttk` submodule adds themed widgets that draw using the host platform's native theme engine where available.

## Differentiators

- **No separate install**: part of the Python standard library, so scripts that use only base tkinter run on any standard CPython install without extra dependencies.
- **Direct Tcl/Tk wrapper**: exposes the underlying Tcl interpreter and Tk widget set rather than reimplementing a toolkit, inheriting Tk's event loop and widget model.
- **Three geometry managers**: `pack`, `grid`, and `place` offer different layout strategies (flow-based, table-based, absolute) within the same toolkit.
- **ttk theming layer**: `tkinter.ttk` provides a themed widget set as a separate API surface from the classic tkinter widgets, for closer-to-native appearance.

## Mechanical details

Import via `import tkinter` (and `import tkinter.ttk as ttk` for themed widgets). As of the current CPython release cycle, the standard binary installers bundle Tcl/Tk 8.6, not the newer Tcl/Tk 9.0 line; building against 9.0 requires a custom build. On some Linux distributions, the `tkinter` Python module is packaged separately from the base Python install (e.g., a `python3-tk` OS package) and must be installed via the system package manager. High-DPI display scaling (e.g., 150% scaling on Windows) can render text and widgets at incorrect sizes without manual configuration.

## Security

Distributed as part of CPython under the PSF License; the underlying Tcl/Tk toolkit is separately licensed under the Tcl/Tk license (a BSD-style license). No network access, credential handling, or code execution beyond standard GUI event dispatch and the Tcl interpreter it wraps. As a GUI toolkit invoked from local scripts, the primary consideration is trust in the script's own code (e.g., via Tcl's `eval`-style interfaces), not the library itself.
