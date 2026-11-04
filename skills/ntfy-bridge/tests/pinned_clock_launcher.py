#!/usr/bin/env python3
"""Test-side launcher: runs ntfy_bridge.main() as a subprocess with the clock
pinned to the fixture capture era, so the e2e smoke test stays independent of
the wall-clock date. Not part of the shipped script; ntfy_bridge.py gets no
clock flag or env var of its own.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import ntfy_bridge  # noqa: E402

# Matches the FakeClock default in test_ntfy_bridge.py: inside the 12h cache
# window of every captured fixture message (all ~1793680493-1793680600).
FIXTURE_ERA_TIME = 1793680600.0

if __name__ == "__main__":
    sys.exit(ntfy_bridge.main(sys.argv[1:], time_fn=lambda: FIXTURE_ERA_TIME))
