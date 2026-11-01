---
name: ossu-computer-science
title: OSSU Computer Science
url: "https://github.com/ossu/computer-science"
category: reference
summary: "Open Source Society University's free, self-taught CS curriculum modeled on undergraduate degree requirements (ACM/IEEE CS 2013 guidelines), assembled from free online courses (MIT, Harvard, Princeton, etc.); organized into Intro CS, Core CS (programming, math, tools, systems, theory, security, applications, ethics), Advanced CS electives, and a peer-evaluated final project; ~2 years at 20 hrs/week"
tags: [computer-science, learning, curriculum, self-taught, mooc, open-education]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: []
overlaps: [build-your-own-x, data-science-for-beginners]
source: unknown
---

## What it does

A community-maintained, free curriculum that reproduces the CS-specific portion of an undergraduate computer science degree using open online courses. Course selection follows fixed criteria (open enrollment, regular/self-paced offering, high pedagogical quality, alignment with the CS 2013 curricular guidelines); where no suitable course exists, a book is substituted. It targets learners already educated outside CS, so it omits general-education requirements.

## Structure / contents

Four stages:

- **Intro CS** — a single try-it course (Introduction to CS and Programming using Python) to gauge fit.
- **Core CS** (~first three years of a major, all required): core programming (functional/OO design, testing, ML-family and Lisp-family languages), core math (calculus, discrete math for CS), CS tools (shell, vim, version control via *The Missing Semester*), core systems (Nand2Tetris I/II, OS, networking), core theory (algorithms design & analysis), core security, core applications (databases, ML, graphics, software engineering), and core ethics.
- **Advanced CS** (electives, choose by interest): advanced programming, systems (Computation Structures), theory, information security, and math.
- **Final project** — a self-directed project, peer-evaluated worldwide.

Prerequisites: high-school math for Core CS; completion of Core CS for Advanced CS; a basic physics course for Advanced systems.

## Mechanical details

- Data-only repository: curriculum tables and course links, no code.
- Estimated ~2 years at ~20 hrs/week; a linked spreadsheet estimates completion dates.
- Most material is free; some courses charge for graded assignments/exams (Coursera and edX offer financial aid).
- Progress tracking: learners fork the repo and check off completed courses as a kanban board.
- Community via Discord and GitHub issues. Maintainers: Eric Douglas (founder), Josh Hanson (lead technical), Waciuma Wanjohi (lead academic). ~207k GitHub stars / ~26k forks as of mid-2026.
- The README warns off outdated third-party mirrors (a deprecated Firebase app, Trello board, and Notion templates); the canonical sources are the OSSU CS website and this repo.

## Security

MIT-licensed (confirmed via the repo's `LICENSE`). Educational content only — course links and Markdown tables, no executable code or installable dependencies. Individual linked courses are hosted by third parties (edX, Coursera, university sites) with their own terms.