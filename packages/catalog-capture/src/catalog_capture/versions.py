"""Tool version strings for the capture record (R8, I4)."""

from __future__ import annotations

import importlib.metadata
import subprocess


def playwright_version() -> str:
    return importlib.metadata.version("playwright")


def pip_version(pkg: str) -> str:
    """Installed version of a pip/uv-managed package, or "unknown" if absent
    (mirrors toolkit-workbench/reel/scripts/run_bench.py `pip_version` — same
    fallback shape, not imported)."""
    try:
        return importlib.metadata.version(pkg)
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


def yt_dlp_version() -> str:
    return pip_version("yt-dlp")


def instaloader_version() -> str:
    return pip_version("instaloader")


def faster_whisper_version() -> str:
    return pip_version("faster-whisper")


def ctranslate2_version() -> str:
    return pip_version("ctranslate2")


def ffmpeg_version() -> str:
    """Version string of the imageio-ffmpeg-bundled binary (I4: never the
    system ffmpeg — this package pins its own via `--ffmpeg-location`)."""
    import imageio_ffmpeg

    try:
        exe = imageio_ffmpeg.get_ffmpeg_exe()
        out = subprocess.run([exe, "-version"], capture_output=True, text=True, timeout=10)
        first_line = out.stdout.splitlines()[0] if out.stdout else ""
        # e.g. "ffmpeg version 7.0.2-static https://..." -> "7.0.2-static"
        parts = first_line.split()
        if len(parts) >= 3 and parts[0] == "ffmpeg" and parts[1] == "version":
            return parts[2]
        return first_line or "unknown"
    except Exception:
        return "unknown"


def claude_version() -> str:
    try:
        out = subprocess.run(["claude", "--version"], capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or "unknown"
    except Exception:
        return "unknown"
