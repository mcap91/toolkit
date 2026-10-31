"""Shared media-fetch stage (yt-dlp): anonymous caption/info probe plus audio
and video download (WK-0094 Phase B; formerly half of `instagram_probe.py`).

Logic ported from `toolkit-workbench/reel/scripts/run_bench.py` stage1 (probe) —
reduced from the bench's multi-contender comparison down to the single
WK-0079 "Results — run 2" recommended default stack (I4): yt-dlp `-j`
anonymous probe, yt-dlp bestaudio/bestvideo download. Not imported from the
workbench (it is gitignored and not a dependency of this package, R9/I8) —
re-implemented here against this package's own yt-dlp/ffmpeg.

Any adapter that needs a yt-dlp-backed media fetch (the Instagram reel
adapter today; a future Instagram-post/carousel adapter, WK-0087) calls into
this module — it carries no reel-only assumption itself.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

import imageio_ffmpeg

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()


class ProbeFailedError(RuntimeError):
    """yt-dlp -j produced no usable info JSON."""


class AudioDownloadFailedError(RuntimeError):
    """yt-dlp bestaudio download failed."""


class VideoDownloadFailedError(RuntimeError):
    """yt-dlp bestvideo download failed."""


@dataclass
class ProbeResult:
    info_json_text: str  # raw yt-dlp -j stdout (one JSON object), verbatim
    caption: str | None


def probe_caption(url: str, *, timeout: int = 120) -> ProbeResult:
    """yt-dlp `-j` anonymous (I4/WK-0079 S6: `--sleep-requests 2`, curl-cffi
    impersonation via the `yt-dlp[curl-cffi]` extra already installed)."""
    proc = subprocess.run(
        ["yt-dlp", "-j", "--no-warnings", "--sleep-requests", "2", url],
        capture_output=True, text=True, timeout=timeout,
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        raise ProbeFailedError(proc.stderr.strip()[-800:] or f"yt-dlp -j exit {proc.returncode}, no output")
    info_line = proc.stdout.splitlines()[0]
    data = json.loads(info_line)
    return ProbeResult(info_json_text=info_line, caption=data.get("description"))


@dataclass
class PlaylistProbeResult:
    """yt-dlp `-J` (dump the whole playlist as one JSON object) used only as
    an independent cross-check on an Instagram carousel's declared slide
    count (WK-0087 step 4, `instaloader`'s `carousel_media_count`) — never
    the primary slide fetch. WK-0094 Phase A evidence: yt-dlp returns no
    slide images for an Instagram post (`No video formats found!` per
    entry) and can exit non-zero for that reason while still printing a
    usable `playlist_count` on stdout (the real De9SalRGOhy probe: exit 1,
    `playlist_count` 20) — so a non-zero exit alone is not treated as a
    failure to parse `playlist_count` from, but a failure here is always
    recorded and never fatal to the post capture."""

    raw_stdout: str
    playlist_count: int | None
    error: str | None


def probe_playlist_count(url: str, *, timeout: int = 120) -> PlaylistProbeResult:
    """Never raises — any failure (timeout, no stdout, unparsable JSON) is
    recorded on `.error`, since this is a cross-check, not the adapter's
    required fetch path."""
    try:
        proc = subprocess.run(
            ["yt-dlp", "-J", "--no-warnings", "--sleep-requests", "2", url],
            capture_output=True, text=True, timeout=timeout,
        )
    except Exception as e:  # noqa: BLE001 - a cross-check failure is recorded, not fatal
        return PlaylistProbeResult(raw_stdout="", playlist_count=None, error=str(e))

    stdout = proc.stdout or ""
    if not stdout.strip():
        err = proc.stderr.strip()[-800:] or f"yt-dlp -J exit {proc.returncode}, no output"
        return PlaylistProbeResult(raw_stdout=stdout, playlist_count=None, error=err)
    try:
        data = json.loads(stdout)
    except json.JSONDecodeError as e:
        return PlaylistProbeResult(raw_stdout=stdout, playlist_count=None, error=f"invalid JSON: {e}")

    count = data.get("playlist_count") if isinstance(data, dict) else None
    if count is None:
        err = proc.stderr.strip()[-800:] or "no playlist_count in yt-dlp -J output"
        return PlaylistProbeResult(raw_stdout=stdout, playlist_count=None, error=err)
    return PlaylistProbeResult(raw_stdout=stdout, playlist_count=count, error=None)


def download_audio(url: str, outdir: Path, *, timeout: int = 180) -> Path:
    """yt-dlp bestaudio DASH download (I4: "video-only DASH: audio comes from
    the separate bestaudio download"). `--ffmpeg-location` pins this package's
    own imageio-ffmpeg binary, never a system ffmpeg."""
    proc = subprocess.run(
        ["yt-dlp", "-f", "bestaudio", "--sleep-requests", "2", "--no-warnings",
         "--ffmpeg-location", FFMPEG_EXE, "-o", str(outdir / "audio.%(ext)s"), url],
        capture_output=True, text=True, timeout=timeout,
    )
    found = [p for p in outdir.glob("audio.*") if p.suffix != ".log"]
    if proc.returncode != 0 or not found:
        raise AudioDownloadFailedError(proc.stderr.strip()[-800:] or f"yt-dlp bestaudio exit {proc.returncode}")
    return found[0]


def download_video(url: str, outdir: Path, *, timeout: int = 180) -> Path:
    proc = subprocess.run(
        ["yt-dlp", "-f", "bestvideo", "--sleep-requests", "2", "--no-warnings",
         "--ffmpeg-location", FFMPEG_EXE, "-o", str(outdir / "video.%(ext)s"), url],
        capture_output=True, text=True, timeout=timeout,
    )
    found = [p for p in outdir.glob("video.*") if p.suffix != ".log"]
    if proc.returncode != 0 or not found:
        raise VideoDownloadFailedError(proc.stderr.strip()[-800:] or f"yt-dlp bestvideo exit {proc.returncode}")
    return found[0]
