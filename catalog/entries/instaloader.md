---
name: instaloader
title: Instaloader
url: https://github.com/instaloader/instaloader
category: cli-tool
summary: Python CLI and library that downloads public and private Instagram profiles, hashtags, stories, feeds, and saved media along with captions, comments, and geotags — supports incremental re-sync (`--fast-update`, `--latest-stamps`) and session-cookie login for private content; MIT licensed, ~13.7k GitHub stars as of 2026
tags:
  - instagram
  - web-scraping
  - cli-tool
  - python
  - media-download
  - metadata-extraction
  - osint
reviewed: 2026-10-29
acquired: 2026-10-29
license: MIT
security_flags:
  - unofficial-unaffiliated-third-party
  - platform-tos-violation-risk
  - account-ban-risk
  - stores-session-cookies-on-disk
overlaps: []
source: web
source_url: https://github.com/instaloader/instaloader
---

## What it does

Instaloader is a Python command-line tool and library for downloading Instagram content along with its metadata. It pulls pictures, videos, captions, comments, and geotags from public or private profiles, hashtags, user stories, feeds, and saved media. It automatically detects when a profile changes its username and renames the local target directory to match, and automatically resumes a previously-interrupted download.

## Mechanical details

Install via `pip3 install instaloader`. CLI form: `instaloader [--comments] [--geotags] [--stories] [--highlights] [--tagged] [--reels] [--igtv] [--login YOUR-USERNAME] [--fast-update] profile | "#hashtag" | :stories | :feed | :saved`.

`--fast-update` stops a re-run at the first already-downloaded post per profile. `--latest-stamps` instead records a per-profile last-downloaded timestamp, so locally moving or deleting downloaded files does not cause re-downloads on the next run. `--login=your_username` authenticates and stores a session cookie file in the system temp directory, reused on later invocations so private-profile downloads (where the login account already has access) can run non-interactively. Also usable as a Python library, not just the CLI. MIT licensed; ~13.7k GitHub stars and active maintenance (releases through mid-2026) per third-party trackers (scrapfly.io, socialcrawl.dev), since the repo's own star count is not visible in the fetched README.

## Security

Instaloader's own README states it is "in no way affiliated with, authorized, maintained or endorsed by Instagram or any of its affiliates or subsidiaries" and to "use at your own risk." Automated use risks Instagram's bot detection: the project's GitHub issues document recurring 429 rate-limit errors, and at least one user reports Instagram permanently disabling their account after using the tool (issue #828). `--login` stores a session cookie file on disk for reuse, so running it against a real account carries a credential-handling consideration. No license concerns on the tool itself (MIT); downloaded content retains whatever copyright and platform-ToS status it had on Instagram.
