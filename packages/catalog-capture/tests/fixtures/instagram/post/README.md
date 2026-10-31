# Single-image post fixture (WK-0087)

Source: the WK-0094 Phase A probe, run 2026-10-29/30 (UTC), one of the five single-image `/p/`
posts out of the 12 links listed in WK-0087 (the other seven are carousels; two of those seven
are the committed goldens under `tests/fixtures/instagram/carousel/`).

`Deqni2Tic2N/` is an unedited copy (`cp`, no re-encoding, no edits) of
`toolkit-workbench/carousel/probe/instaloader/Deqni2Tic2N/` (gitignored workbench): `cmd.txt`,
`stdout.txt`, `exit_code.txt`, and `dl/` (instaloader's own download directory — the post's JSON
metadata, a `.txt` caption file, and one `.jpg`, `media_type` 1, no `carousel_media` key).
Integrity verified at copy time with `diff -r` against the workbench original (byte-identical).

Instagram posts of `media_type` 1 are not read through yt-dlp — WK-0094 Phase A found yt-dlp
returns no usable data for a single-image Instagram post (`stdout.json` is literally `null`), so
this adapter only cross-checks slide count via yt-dlp for carousels (`media_type` 8).
