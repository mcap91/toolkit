---
name: instagram-saved-reels-obsidian-knowledge-graph
title: Instagram Saved-Reels-to-Obsidian Knowledge Graph Pipeline
url: https://www.instagram.com/reel/DeaAbkiyU-A/
source_url: https://www.instagram.com/reel/DeaAbkiyU-A/
source: instagram
category: agent-pattern
summary: A personal-archiving technique that uses yt-dlp to bulk-download a user's own saved Instagram reels (about 500 in the creator's case), then an AI-assisted script transcribes each reel and extracts named entities and proper nouns, categorizes it (memes, tutorials, conspiracies, health, etc.), and writes a node into an Obsidian vault with an executive summary, tags, the source video's hash, key takeaways, and screenshots; Obsidian's graph view then shows reel-to-reel links, and the creator deletes each reel from Instagram's saved library after scraping it and manually prunes the resulting graph.
tags:
  - obsidian
  - yt-dlp
  - instagram
  - knowledge-graph
  - personal-archiving
  - video-transcription
  - entity-extraction
  - second-brain
  - data-liberation
reviewed: 2026-10-29
acquired: 2026-10-29
license: N/A
security_flags: []
overlaps:
  - obsidian-claude-second-brain-workflow
  - karpathy-llm-wiki
  - third-brain-v5-wiki
---

## What it does

Describes a personal-archiving pipeline the creator built to turn their saved Instagram reels into a browsable Obsidian knowledge graph, framed as "taking control of my data" from Instagram:

1. **Bulk download**: yt-dlp scrapes every reel in the creator's Instagram "saved" library — about 500 videos at the time of the reel.
2. **Delete from Instagram**: each reel is deleted from the saved library immediately after download, so Instagram's app no longer surfaces it back to the creator (the creator notes Instagram itself still retains the data server-side — this only removes it from their own saved list).
3. **Transcribe and extract**: a separate, AI-assisted script transcribes each reel and pulls out "important information like names and proper nouns."
4. **Categorize**: reels are auto-sorted into topic buckets (memes, tutorials, conspiracies, health, etc.).
5. **Write to Obsidian**: each reel becomes one node/page containing an executive summary, tags, the original video's hash, key takeaways, and screenshots; Obsidian's native graph view renders links between related nodes.
6. **Manual pruning**: the creator describes the automated linking as "not perfect" and "about 80% of the way there," requiring ongoing manual pruning of incorrect or low-value links.
7. **Ongoing ingestion**: new saved reels get the same treatment and are added to the growing vault, which the creator calls "the encyclopedia of bravidus."

## Notes

- No code, repo, or product is linked — the creator says "DM or comment" for more detail and the caption calls it "literally all just python scripts," but no script is shared or named in the post.
- yt-dlp and Obsidian are both named but only as generic, off-the-shelf components; the AI transcription/entity-extraction/categorization script is custom and undescribed beyond "I use AI to help build scripts."
- Differs from [[obsidian-claude-second-brain-workflow]] (which structures books/articles/posts a person reads) in its data source and intake mechanism: this pipeline's input is bulk-scraped video from a specific social platform via yt-dlp, with an automated transcribe → extract → categorize → graph step, rather than a human pasting highlights for Claude to structure.
- Overlaps conceptually with the "LLM compiles raw sources into a persistent wiki" idea in [[karpathy-llm-wiki]], and with [[third-brain-v5-wiki]]'s Obsidian-specific vault schema, but neither of those is video-scrape-specific.
- Downloading and re-hosting another platform's user-generated video content, then deleting it from one's own account while the platform retains it server-side, is a data-portability workaround rather than a sanctioned export feature; the reel does not address Instagram's terms of service.

## Sources

- [Instagram reel](https://www.instagram.com/reel/DeaAbkiyU-A/) — caption, transcript, on-screen text, and key claims (catalog source).

## Security

N/A — a described personal workflow, not distributed software. No repo, script, or service is shared in the post to audit.
