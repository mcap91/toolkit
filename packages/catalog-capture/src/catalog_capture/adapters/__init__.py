"""Registers the shipped adapters (Reddit, Instagram reel, Instagram post)
into the shared registry on import. `cli.py` imports this package before
building any adapter list; a test that wants the real registered set does
the same."""

from __future__ import annotations

from ..registry import register
from .instagram_post import InstagramPostAdapter
from .instagram_reel import InstagramReelAdapter
from .reddit import RedditAdapter

reddit = RedditAdapter()
instagram_reel = InstagramReelAdapter()
instagram_post = InstagramPostAdapter()

register(reddit)
register(instagram_reel)
register(instagram_post)

__all__ = [
    "InstagramPostAdapter",
    "InstagramReelAdapter",
    "RedditAdapter",
    "instagram_post",
    "instagram_reel",
    "reddit",
]
