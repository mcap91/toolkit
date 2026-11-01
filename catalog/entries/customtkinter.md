---
name: customtkinter
title: CustomTkinter
url: "https://github.com/tomschimansky/customtkinter"
category: framework
summary: "Python UI library built on Tkinter providing modern, customizable widgets (CTkButton, CTkFrame, scrollable frames) with light/dark appearance modes, HighDPI scaling, and JSON-based theming across Windows, macOS, and Linux"
tags: [python, gui, tkinter, desktop, cross-platform, theming, dark-mode]
reviewed: 2026-09-25
acquired: 2026-09-25
license: CC0-1.0
security_flags: []
overlaps: [tkinter]
source: unknown
---

## What it does / What it says

CustomTkinter is a Python UI library built on top of the standard `tkinter` module. It provides
drop-in replacement widgets (`CTkButton`, `CTkLabel`, `CTkFrame`, `CTkEntry`, scrollable frames, etc.)
that are created and used the same way as normal Tkinter widgets, and can be freely mixed with plain
Tkinter elements in the same application. Widgets and window chrome adapt to the OS light/dark
appearance mode (`set_appearance_mode("System" | "light" | "dark")`) or a manually set mode, and all
widgets/windows support HighDPI scaling on Windows and macOS. The stated goal is a consistent, modern
look across Windows, macOS, and Linux. Install via `pip3 install customtkinter`; current release is
6.0.0 (PyPI, uploaded Jun 24, 2026). Maintained by creator Tom Schimansky with current co-developer
Federico Spada.

## Differentiators / Key takeaways

- Widgets follow Tkinter's own construction pattern (`master=`, `.place()/.pack()/.grid()`,
  `command=` callbacks), so adopting it is an incremental change to existing Tkinter code rather than
  a switch to a new framework.
- Built-in color themes (`blue`, `dark-blue`, `green`) plus support for custom themes defined in JSON
  files, applied via `set_default_color_theme()`.
- Scrollable frames (vertical or horizontal) compose with other widgets; buttons support images via a
  `PhotoImage` object passed to the `image` argument, with a `compound` option for text/image layout.
- `ctk.run_showroom()` launches a built-in demo app that displays every available widget.
- Companion library `TkinterMapView` (same author) adds an OpenStreetMap/tile-based map widget that
  integrates directly into a CustomTkinter app.
- Overlaps with the catalog's existing `tkinter` entry: CustomTkinter is a third-party layer on top of
  that standard-library toolkit, not an alternative to it — code migrates between the two with minimal
  changes.

## Mechanical details / What to adopt

- Install: `pip3 install customtkinter` (`pip3 install customtkinter --upgrade` to update; the author
  notes the library is under active development and recommends updating often).
- Minimal usage:
  ```python
  import customtkinter
  customtkinter.set_appearance_mode("System")
  customtkinter.set_default_color_theme("blue")
  app = customtkinter.CTk()
  app.geometry("400x240")
  button = customtkinter.CTkButton(master=app, text="CTkButton", command=lambda: print("pressed"))
  button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
  app.mainloop()
  ```
- Docs: https://customtkinter.tomschimansky.com/documentation covers the widget reference,
  appearance-mode/scaling behavior, and theming.
- Support: GitHub Discussions for questions/help/showcase; GitHub Issues for bug reports (requires a
  complete error message plus a minimal reproducing example) and feature requests.
- General-purpose desktop GUI toolkit, not bioinformatics-specific — relevant as a way to put a local
  desktop front-end on scripts/pipelines rather than as a domain tool itself.

## Security

License is CC0-1.0 (public domain dedication) per PyPI/libraries.io metadata — no copyleft or
commercial-use restriction. No dependency manifest, CI configuration, or contributor-count data was
available from the fetched sources (GitHub README, official docs site, PyPI project page), so
supply-chain and maintenance signals beyond "actively releasing" (6.0.0, Jun 2026) are unverified.
Nothing in the reviewed content indicates dangerous patterns (eval, shell injection, credential
handling, unsafe deserialization).