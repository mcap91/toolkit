"""Unit tests for ntfy_bridge.py against the golden ntfy.sh captures in fixtures/.

Public seams exercised: the parser/poll-processing pure functions, the CLI entry
point (main) with an injected HTTP function, and the registry file on disk.
"""
import contextlib
import io
import json
import os
import re
import sys
import tempfile
import unittest
import urllib.error

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import ntfy_bridge  # noqa: E402

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")


def load_fixture(name):
    with open(os.path.join(FIXTURES, name), "rb") as f:
        return f.read()


class RecordingGet:
    """Fake http_get: serves canned bodies in order, records every URL asked."""

    def __init__(self, bodies):
        self.bodies = list(bodies)
        self.urls = []

    def __call__(self, url):
        self.urls.append(url)
        return 200, self.bodies.pop(0)


class RecordingPost:
    """Fake http_post: records calls, optionally raises like a network failure."""

    def __init__(self, raise_error=False):
        self.calls = []
        self.raise_error = raise_error

    def __call__(self, url, body, headers):
        self.calls.append((url, body, dict(headers)))
        if self.raise_error:
            raise urllib.error.URLError("simulated network failure")
        return 200, b"{}"


def run_main(argv, http_get=None, http_post=None):
    kwargs = {}
    if http_get is not None:
        kwargs["http_get"] = http_get
    if http_post is not None:
        kwargs["http_post"] = http_post
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = ntfy_bridge.main(argv, **kwargs)
    stdout_text = out.getvalue()
    parsed = json.loads(stdout_text) if stdout_text.strip() else None
    return code, parsed, stdout_text, err.getvalue()


class RegistryTestCase(unittest.TestCase):
    """Base class: each test gets its own temp registry file (no shared state)."""

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.registry_path = os.path.join(self.tmpdir.name, "channels.json")
        self._old_registry = os.environ.get("NTFY_BRIDGE_REGISTRY")
        self._old_server = os.environ.get("NTFY_BRIDGE_SERVER")
        os.environ["NTFY_BRIDGE_REGISTRY"] = self.registry_path
        os.environ["NTFY_BRIDGE_SERVER"] = "http://example.invalid"

    def tearDown(self):
        self.tmpdir.cleanup()
        if self._old_registry is None:
            os.environ.pop("NTFY_BRIDGE_REGISTRY", None)
        else:
            os.environ["NTFY_BRIDGE_REGISTRY"] = self._old_registry
        if self._old_server is None:
            os.environ.pop("NTFY_BRIDGE_SERVER", None)
        else:
            os.environ["NTFY_BRIDGE_SERVER"] = self._old_server

    def create_channel(self, name, mode="two-way", post_fn=None):
        code, entry, _, err = run_main(
            ["create", "--name", name, "--mode", mode, "--purpose", "test", "--repo", "test-repo"],
            http_post=post_fn,
        )
        self.assertEqual(code, 0, err)
        return entry


class ParserTests(unittest.TestCase):
    """normalize()/parse_message() — Decision 7's closed vocabulary, pure function."""

    def test_normalize_collapses_whitespace_uppercases_strips_one_trailing_period(self):
        # real captured body: server trims outer whitespace, leaves internal runs
        self.assertEqual(ntfy_bridge.normalize("finish   up."), "FINISH UP")

    def test_every_vocabulary_word_matches_after_normalization(self):
        # each Decision 7 word must match once normalized, case- and spacing-insensitive
        self.assertEqual(ntfy_bridge.parse_message("STOP", None), "STOP")
        self.assertEqual(ntfy_bridge.parse_message("  stop  ", None), "STOP")
        self.assertEqual(ntfy_bridge.parse_message("finish   up.", None), "FINISH UP")
        self.assertEqual(ntfy_bridge.parse_message("pause", None), "PAUSE")
        self.assertEqual(ntfy_bridge.parse_message("continue", None), "CONTINUE")
        self.assertEqual(ntfy_bridge.parse_message("Status.", None), "STATUS")
        self.assertEqual(ntfy_bridge.parse_message("approve 3f9a", "3F9A"), "APPROVE 3F9A")

    def test_near_miss_is_null(self):
        # "STOP please" (real captured body) must not match STOP
        self.assertIsNone(ntfy_bridge.parse_message("STOP please", None))

    def test_free_text_is_null(self):
        # real captured body, no vocabulary word present at all
        self.assertIsNone(ntfy_bridge.parse_message("free text reply", "3F9A"))

    def test_wrong_code_is_null(self):
        # code present but does not equal the channel's pending code
        self.assertIsNone(ntfy_bridge.parse_message("approve 0000", "3F9A"))

    def test_stale_code_is_null_after_a_second_ask(self):
        # a new ask makes the previous code stale (Decision 7 amendment)
        self.assertIsNone(ntfy_bridge.parse_message("approve 3f9a", "AAAA"))

    def test_approve_with_no_pending_question_is_null(self):
        # APPROVE with nothing pending can never match
        self.assertIsNone(ntfy_bridge.parse_message("approve 3f9a", None))


class ProcessPollCursorTests(unittest.TestCase):
    """process_poll() — cursor dedup, since-advance, and 12h cache pruning."""

    def test_poll_one_then_poll_several_yields_only_five_new(self):
        # poll-one's single message is already seen when poll-several (which repeats it) arrives
        cursor = {"since": 0, "seen": {}}
        cursor, matched, acted_on, superseded, unrecognized = ntfy_bridge.process_poll(
            load_fixture("poll-one.jsonl").decode(), cursor, None, now=1793680600
        )
        self.assertEqual(unrecognized, 1)  # "capture one" is not a vocabulary word
        cursor, matched, acted_on, superseded, unrecognized = ntfy_bridge.process_poll(
            load_fixture("poll-several.jsonl").decode(), cursor, None, now=1793680600
        )
        # 6 messages in poll-several, 1 already seen -> 5 new: 2 matched + 3 unrecognized
        self.assertEqual(len(matched) + unrecognized, 5)

    def test_repeat_poll_yields_nothing(self):
        cursor = {"since": 0, "seen": {}}
        cursor, *_ = ntfy_bridge.process_poll(
            load_fixture("poll-several.jsonl").decode(), cursor, None, now=1793680600
        )
        cursor, matched, acted_on, superseded, unrecognized = ntfy_bridge.process_poll(
            load_fixture("poll-several.jsonl").decode(), cursor, None, now=1793680600
        )
        self.assertEqual((matched, acted_on, superseded, unrecognized), ([], None, [], 0))

    def test_fresh_process_reading_same_registry_yields_nothing(self):
        # simulate a restart: rebuild the cursor dict from scratch (no in-memory state carried)
        cursor = {"since": 0, "seen": {}}
        cursor, *_ = ntfy_bridge.process_poll(
            load_fixture("poll-several.jsonl").decode(), cursor, None, now=1793680600
        )
        reloaded_cursor = json.loads(json.dumps(cursor))  # round-trip through JSON like disk would
        cursor2, matched, acted_on, superseded, unrecognized = ntfy_bridge.process_poll(
            load_fixture("poll-several.jsonl").decode(), reloaded_cursor, None, now=1793680600
        )
        self.assertEqual((matched, acted_on, superseded, unrecognized), ([], None, [], 0))

    def test_same_second_reorder_replay_after_seen_yields_nothing(self):
        # poll-since-ts-last's two same-second messages, already seen via poll-several, replay clean
        cursor = {"since": 0, "seen": {}}
        cursor, *_ = ntfy_bridge.process_poll(
            load_fixture("poll-several.jsonl").decode(), cursor, None, now=1793680600
        )
        cursor, matched, acted_on, superseded, unrecognized = ntfy_bridge.process_poll(
            load_fixture("poll-since-ts-last.jsonl").decode(), cursor, None, now=1793680600
        )
        self.assertEqual((matched, acted_on, superseded, unrecognized), ([], None, [], 0))

    def test_prune_drops_seen_ids_older_than_twelve_hours(self):
        # injected clock: an id seen at t=1000 must be pruned once now > t + 43200
        cursor = {"since": 1000, "seen": {"old-id": 1000, "fresh-id": 1793680000}}
        new_cursor, *_ = ntfy_bridge.process_poll("", cursor, None, now=1000 + 43200 + 1)
        self.assertNotIn("old-id", new_cursor["seen"])
        self.assertIn("fresh-id", new_cursor["seen"])

    def test_mixed_poll_precedence_and_superseded(self):
        # pending code 3F9A; polling poll-several after poll-one (spec's exact scenario)
        cursor = {"since": 0, "seen": {}}
        cursor, *_ = ntfy_bridge.process_poll(
            load_fixture("poll-one.jsonl").decode(), cursor, "3F9A", now=1793680600
        )
        cursor, matched, acted_on, superseded, unrecognized = ntfy_bridge.process_poll(
            load_fixture("poll-several.jsonl").decode(), cursor, "3F9A", now=1793680600
        )
        self.assertEqual(set(matched), {"STOP", "FINISH UP", "APPROVE 3F9A"})
        self.assertEqual(acted_on, "STOP")
        self.assertEqual(set(superseded), {"FINISH UP", "APPROVE 3F9A"})
        self.assertEqual(unrecognized, 2)  # "STOP please" and "free text reply"


class CreateRotateTests(RegistryTestCase):
    """create/rotate — independent random topics, duplicate/name validation."""

    def test_create_rejects_invalid_name(self):
        code, _, _, err = run_main(
            ["create", "--name", "Bad_Name", "--mode", "one-way", "--purpose", "p", "--repo", "r"]
        )
        self.assertNotEqual(code, 0)

    def test_create_refuses_duplicate_name(self):
        self.create_channel("dup-chan", mode="one-way")
        code, _, _, err = run_main(
            ["create", "--name", "dup-chan", "--mode", "one-way", "--purpose", "p", "--repo", "r"]
        )
        self.assertNotEqual(code, 0)

    def test_create_gives_independent_random_topics(self):
        entry_a = self.create_channel("chan-a", mode="two-way")
        entry_b = self.create_channel("chan-b", mode="two-way")
        self.assertNotEqual(entry_a["topic"], entry_a["reply_topic"])
        self.assertNotEqual(entry_a["reply_topic"], entry_a["topic"] + "-reply")
        hex_a_topic = entry_a["topic"].rsplit("-", 1)[-1]
        hex_a_reply = entry_a["reply_topic"].rsplit("-", 1)[-1]
        self.assertNotEqual(hex_a_topic, hex_a_reply)
        self.assertNotEqual(entry_a["topic"], entry_b["topic"])
        self.assertNotEqual(entry_a["reply_topic"], entry_b["reply_topic"])

    def test_rotate_replaces_both_topics_and_resets_state(self):
        entry = self.create_channel("rot-chan", mode="two-way")
        post = RecordingPost()
        get = RecordingGet([load_fixture("poll-one.jsonl")])
        run_main(["ask", "--name", "rot-chan", "--question", "q?", "--if-no-reply", "CONTINUE"], http_post=post)
        run_main(["poll", "--name", "rot-chan"], http_get=get)

        code, rotated, _, err = run_main(["rotate", "--name", "rot-chan"])
        self.assertEqual(code, 0, err)
        self.assertNotEqual(rotated["topic"], entry["topic"])
        self.assertNotEqual(rotated["reply_topic"], entry["reply_topic"])
        self.assertEqual(rotated["cursor"]["seen"], {})
        self.assertIsNone(rotated["pending"])
        self.assertEqual(rotated["unrecognized_total"], 0)
        self.assertEqual(len(rotated["rotations"]), 1)


class OneWayRefusalTests(RegistryTestCase):
    """One-way channels must refuse ask and poll outright."""

    def test_one_way_refuses_ask(self):
        self.create_channel("one-way-chan", mode="one-way")
        code, _, _, err = run_main(
            ["ask", "--name", "one-way-chan", "--question", "q?", "--if-no-reply", "CONTINUE"]
        )
        self.assertNotEqual(code, 0)
        self.assertIn("one-way", err)

    def test_one_way_refuses_poll(self):
        self.create_channel("one-way-chan2", mode="one-way")
        code, _, _, err = run_main(["poll", "--name", "one-way-chan2"])
        self.assertNotEqual(code, 0)
        self.assertIn("one-way", err)


class PollRequestAndErrorTests(RegistryTestCase):
    """poll's HTTP request shape and failure handling."""

    def test_request_url_carries_since_timestamp_never_an_id(self):
        self.create_channel("url-chan", mode="two-way")
        get = RecordingGet([load_fixture("poll-zero.jsonl"), load_fixture("poll-zero.jsonl")])
        run_main(["poll", "--name", "url-chan"], http_get=get)
        run_main(["poll", "--name", "url-chan"], http_get=get)
        since_re = re.compile(r"since=(\d+)$")
        for url in get.urls:
            m = since_re.search(url)
            self.assertIsNotNone(m, f"no numeric since= in {url}")

    def test_http_error_leaves_registry_byte_identical(self):
        self.create_channel("err-chan", mode="two-way")
        with open(self.registry_path, "rb") as f:
            before = f.read()
        post = RecordingPost(raise_error=True)
        code, _, _, err = run_main(
            ["ask", "--name", "err-chan", "--question", "q?", "--if-no-reply", "CONTINUE"], http_post=post
        )
        self.assertNotEqual(code, 0)
        with open(self.registry_path, "rb") as f:
            after = f.read()
        self.assertEqual(before, after)

    def test_unknown_channel_exits_non_zero(self):
        code, _, _, err = run_main(["poll", "--name", "does-not-exist"])
        self.assertNotEqual(code, 0)


class RegistryDefaultPathTests(unittest.TestCase):
    """The registry default path must live under the user config dir, not the repo."""

    def test_default_registry_path_is_under_user_config_dir(self):
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        self.assertTrue(ntfy_bridge.DEFAULT_REGISTRY_PATH.startswith(os.path.expanduser("~")))
        self.assertIn(".config/ntfy-bridge/channels.json", ntfy_bridge.DEFAULT_REGISTRY_PATH)
        self.assertFalse(ntfy_bridge.DEFAULT_REGISTRY_PATH.startswith(repo_root))


if __name__ == "__main__":
    unittest.main()
