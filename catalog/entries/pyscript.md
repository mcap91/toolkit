---
name: pyscript
title: PyScript
url: "https://github.com/pyscript/pyscript"
category: framework
summary: "Open-source platform for running Python in the browser via Pyodide (CPython on WASM) or MicroPython; embed Python in HTML with a <script type='py'/'mpy'> tag to build browser apps that run client-side on desktop, mobile, or any browser. Born at Anaconda; Apache-2.0."
license: Apache-2.0
tags: [python, webassembly, browser, pyodide, micropython, wasm, frontend, anaconda]
reviewed: 2026-07-27
acquired: 2026-07-27
overlaps: []
security_flags: []
source: unknown
---

## What it does

PyScript is an open-source platform for running Python in the web browser. It builds on Pyodide (a WebAssembly build of CPython), MicroPython, WASM, and standard web technologies, letting developers embed Python directly in HTML using `<script type="py">` (Pyodide) or `<script type="mpy">` (MicroPython) tags. Code runs client-side wherever a browser runs — desktop, laptop, mobile, or tablet — with no server-side Python. It supports terminal output, rich in-browser applications, and interoperation with the DOM and web APIs.

PyScript began at Anaconda Inc.; its core contributors are employed by Anaconda to work on the project, which is otherwise an independent open-source effort.

## Mechanical details

- **Load in a page:** link `https://pyscript.net/releases/<version>/core.css` and load `https://pyscript.net/releases/<version>/core.js` as a module, then add a `<script type="mpy">` or `<script type="py">` block
- Tooling includes an online IDE (pyscript.com), the Pyodide/MicroPython runtimes, and community docs/tutorials

## Security

Apache-2.0 licensed. Python executes inside the browser's WebAssembly sandbox on the client; there is no first-party server component. As with any client-side code, embedded Python and any packages it loads run with the browser tab's privileges and can make network requests the browser permits. No security flags recorded from the observed material.

## How to use it

script src=https://pyscript.net/releases/<ver>/core.js
