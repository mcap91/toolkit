---
name: pandas-tutor
title: Pandas Tutor
url: "https://pandastutor.com/"
category: reference
summary: "Browser-based tool that visualizes step-by-step how Python pandas code transforms DataFrames across chained operations like filtering, sorting, grouping, and joining."
tags: [pandas, data-visualization, python, education, debugging, dataframes]
reviewed: 2026-09-16
acquired: 2026-09-16
license: NOASSERTION
security_flags: []
overlaps: []
source: unknown
---

## What it does
Pandas Tutor is a free, browser-based tool that runs user-submitted Python pandas code and produces a step-by-step visual trace of how each operation (filtering, sorting, grouping, pivoting, joining, aggregating) transforms a DataFrame, rather than showing only the final output. Users type or paste pandas code into an in-browser editor; the tool renders input and output tables side by side, connecting rows across each step of a chained expression with arrows/coloring. It was created by Sam Lau and Philip Guo (UC San Diego) for teaching data science. Sibling tools from the same project cover R's tidyverse (Tidy Data Tutor) and SQL (SQL Tutor); a related tool, Python Tutor, visualizes general-purpose code in Python, Java, C, C++, and JavaScript.

## Differentiators
Running code in a Jupyter notebook shows only the input and final result of a chained expression. Pandas Tutor decomposes multi-step chains (e.g., filter -> sort -> groupby -> aggregate) into individually visualized steps, including intermediate states such as which rows were filtered out or how rows were grouped together — information not visible when printing a DataFrame or GroupBy object directly. Visualizations are shareable via URL.

## Mechanical details
Runs entirely in-browser via Pyodide (a WebAssembly build of the Python/pandas stack). An earlier implementation executed user code server-side in a per-request Docker container, taking up to ~5 seconds per run; the Pyodide port replaced this to run client-side instead. The tool targets small inputs: code is limited in size and larger datasets typically need to be trimmed (e.g., to the first ~50 rows) for the visualization to stay readable. Source repository: github.com/SamLau95/pandas_tutor (Jupyter Notebook/Python, uv-based dev environment). The GitHub API reports `license: null` for this repository, and no LICENSE file was found.

## Security
No authentication, account creation, or persistent data storage was observed on the site. Pandas code submitted to the tool now executes client-side in the browser via Pyodide rather than on pandastutor.com's servers (a change from the tool's original server-side Docker-based execution model). No security disclosures or CVEs were found for this tool during this research.