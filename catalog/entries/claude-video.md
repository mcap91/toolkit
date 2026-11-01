---
name: claude-video
title: Claude Video (/watch)
url: "https://github.com/bradautomates/claude-video"
category: skill
summary: "Agent Skill that lets Claude (and 50+ other skill hosts) 'watch' a video from a URL or local path: yt-dlp fetches captions/video, ffmpeg extracts scene-aware or keyframe images (with a dedup pass and duration-aware frame budget), a timestamped transcript comes from native captions or a Whisper fallback (Groq/OpenAI), and the frames + transcript are handed to the model to answer grounded in what's on screen and in audio."
tags: [claude-code, agent-skill, video, multimodal, yt-dlp, ffmpeg, whisper, transcription, plugin]
reviewed: 2026-08-17
acquired: 2026-08-17
license: MIT
security_flags: [runs-external-binaries, downloads-arbitrary-urls, third-party-transcription-api]
overlaps: []
source: unknown
---
## What it does

`/watch` gives an agent the ability to analyze a video it otherwise could only guess at from title/description. Given a URL (anything yt-dlp supports — YouTube, Loom, TikTok, X, Instagram, Vimeo, hundreds more) or a local file (`.mp4/.mov/.mkv/.webm`) plus a question, it fetches captions first, downloads only what it needs, extracts frames, pulls a timestamped transcript, and hands the frames (read as images) plus transcript to the model. Common uses cited: breaking down someone else's content/hook, diagnosing a bug from a screen recording, summarizing long videos, and turning playlists into per-video notes.

## Mechanical details

- **Pipeline:** `watch.py` orchestrates download (`yt-dlp`) → frame extraction (`ffmpeg`) → transcript (VTT parse or Whisper) → hands paths/transcript to the model, which Reads each JPEG. Prints a working dir; cleans up if no follow-ups.
- **Frame budget:** duration-aware (~30 frames ≤30s up to a 100-frame cap on capped modes past 10 min, which prints a "sparse scan" warning). `--detail transcript|efficient|balanced|token-burner` trades speed/tokens for fidelity (keyframes vs scene-change detection; token-burner is uncapped). `--start`/`--end` for focused, denser passes (capped 2 fps); `--timestamps`, `--max-frames`, `--resolution`, `--fps` knobs.
- **Dedup:** a pure-stdlib pass scales each frame to a 16×16 grayscale thumbnail and drops near-duplicates (mean-abs-diff ≤ threshold vs last kept frame) before the budget cap; `--no-dedup` disables.
- **Transcript:** native captions via yt-dlp (free) preferred; fallback extracts mono 16 kHz mp3 and ships to Whisper — Groq `whisper-large-v3` (preferred) or OpenAI `whisper-1`. `--no-whisper` for frames-only.
- **Install:** Claude Code plugin (`/plugin marketplace add bradautomates/claude-video`, `/plugin install watch@claude-video`); `npx skills add bradautomates/claude-video -g` for Codex/Cursor/Copilot/Gemini CLI/others; `.skill` bundle for claude.ai web (needs "Code execution" capability). First run auto-installs ffmpeg/yt-dlp (brew on macOS; prints commands on Linux/Windows).

## Security

- **License:** MIT.
- **Runs external binaries:** shells out to `yt-dlp` and `ffmpeg`; first run may auto-run `brew install`. Requires a host with code-execution enabled.
- **Downloads arbitrary URLs:** fetches whatever video URL/path it is given via yt-dlp.
- **Third-party transcription:** when a video has no captions, audio is uploaded to Groq or OpenAI Whisper (requires `GROQ_API_KEY`/`OPENAI_API_KEY`, scaffolded into `~/.config/watch/.env` at mode 0600). `--no-whisper` avoids sending audio off-box.
- Test suite uses ffmpeg-synthesized clips (no network). Built on yt-dlp, ffmpeg, and the model's multimodal Read tool.
