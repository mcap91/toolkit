---
name: whisperx
title: WhisperX
url: "https://github.com/m-bain/whisperX"
category: framework
summary: Whisper + wav2vec2 forced alignment + pyannote speaker diarization — 70x realtime batched transcription with accurate word-level timestamps and speaker IDs; builds on faster-whisper; ideal for lecture/interview transcripts
tags: [asr, whisper, transcription, diarization, word-timestamps, speaker-id, audio]
reviewed: 2026-06-19
acquired: 2026-06-19
license: BSD-4-Clause
security_flags: [hf-token-required-for-diarization]
overlaps: [faster-whisper]
source: unknown
---

## What it does

Builds on faster-whisper to add two critical capabilities for structured transcription:

- **Word-level timestamps**: uses wav2vec2 forced alignment to produce accurate per-word timing (not just utterance-level)
- **Speaker diarization**: pyannote-audio pipeline assigns speaker IDs to each word/segment
- **70x realtime**: batched inference with faster-whisper backend, large-v2 in <8GB VRAM
- **VAD preprocessing**: reduces hallucination and enables efficient batching with no WER degradation
- **Sentence-level segments**: nltk sent_tokenize for subtitle-friendly output

Three-stage pipeline: (1) transcribe with Whisper, (2) align with wav2vec2, (3) diarize with pyannote. Each stage can be run independently.

Published at INTERSPEECH 2023, 1st place at Ego4d transcription challenge.

## Assessment

The right tool for lecture and interview transcription where you need to know who said what and when. faster-whisper gives raw speed; WhisperX layers on the alignment and diarization that make transcripts usable for knowledge extraction.

Limitations are honest and real: overlapping speech is poorly handled, diarization is "far from perfect," and words without dictionary characters (numbers, currency) can't be aligned. For single-speaker lecture capture these limitations are minor. For multi-speaker panel discussions, expect manual cleanup.

Requires a HuggingFace token with accepted model agreements for the diarization model — not a security issue but an onboarding friction point.

## Mechanical details

- **Install**: `pip install whisperx` (or `uvx whisperx` for CLI)
- **Python**: 3.9+, CUDA 12.8 for GPU
- **CLI**: `whisperx path/to/audio.wav --model large-v2 --diarize --highlight_words True`
- **Python API**: `whisperx.load_model()` → `model.transcribe()` → `whisperx.align()` → `whisperx.assign_word_speakers()`
- **Output**: segments with word-level timestamps, speaker IDs, .srt/.vtt subtitle export
- **Languages**: default models for en/fr/de/es/it via torchaudio; many more via HuggingFace wav2vec2 models

## Security

- **License**: BSD-4-Clause
- **Dependencies**: faster-whisper, pyannote-audio, torchaudio, wav2vec2 models, nltk — substantial dependency tree
- **Code quality**: academic publication (INTERSPEECH 2023), benchmarking code, active community contributions
- **Supply chain**: primary author (Max Bain, Oxford VGG), 50+ contributors, 13k+ stars
- **Dangerous patterns**: none — HuggingFace token is for model download auth only, not stored insecurely
- **Maintenance**: actively maintained, regular releases, responsive to PRs