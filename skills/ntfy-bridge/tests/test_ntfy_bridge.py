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
    """Fake http_post: records calls, optionally raises like a network failure.
    Returns a publish-response shape (id/time) by default -- callers that do
    not care about the own-message-drop mechanism can ignore it; a test that
    does care passes a real captured `body` instead."""

    def __init__(self, raise_error=False, body=None):
        self.calls = []
        self.raise_error = raise_error
        self._body = body
        self._next_id = 0

    def __call__(self, url, body, headers):
        self.calls.append((url, body, dict(headers)))
        if self.raise_error:
            raise urllib.error.URLError("simulated network failure")
        if self._body is not None:
            return 200, self._body
        self._next_id += 1
        fake = json.dumps({"id": f"fake-id-{self._next_id}", "time": 1793680600}).encode()
        return 200, fake


def run_main(argv, http_get=None, http_post=None, sleep_fn=None, time_fn=None):
    kwargs = {}
    if http_get is not None:
        kwargs["http_get"] = http_get
    if http_post is not None:
        kwargs["http_post"] = http_post
    if sleep_fn is not None:
        kwargs["sleep_fn"] = sleep_fn
    if time_fn is not None:
        kwargs["time_fn"] = time_fn
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = ntfy_bridge.main(argv, **kwargs)
    stdout_text = out.getvalue()
    parsed = json.loads(stdout_text) if stdout_text.strip() else None
    return code, parsed, stdout_text, err.getvalue()


def single_message_line(fixture_name, index):
    """One real captured message, sliced out of a multi-message fixture by line index."""
    return load_fixture(fixture_name).splitlines()[index] + b"\n"


def unexpected_get(url):
    raise AssertionError(f"http_get must not be called: {url}")


class FakeSleep:
    """Fake sleep_fn: records seconds requested, never actually blocks."""

    def __init__(self):
        self.calls = []

    def __call__(self, seconds):
        self.calls.append(seconds)


class FakeClock:
    """Fake time_fn: a fixed value, so timestamps never depend on real wall time."""

    def __init__(self, value=1793680600.0):
        self.value = value

    def __call__(self):
        return self.value


class FailNthGet:
    """Fake http_get: raises `error` on call number `fail_at` (1-based), otherwise
    serves canned bodies from `bodies` in order."""

    def __init__(self, bodies, error, fail_at=2):
        self.bodies = list(bodies)
        self.error = error
        self.fail_at = fail_at
        self.call_count = 0

    def __call__(self, url):
        self.call_count += 1
        if self.call_count == self.fail_at:
            raise self.error
        return 200, self.bodies.pop(0)


class SnapshottingGet:
    """Fake http_get: wraps another fake, recording the registry's on-disk bytes
    at the start of every call, so a test can prove a failed poll left it untouched."""

    def __init__(self, inner, registry_path):
        self.inner = inner
        self.registry_path = registry_path
        self.snapshots = []

    def __call__(self, url):
        with open(self.registry_path, "rb") as f:
            self.snapshots.append(f.read())
        return self.inner(url)


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
    """normalize()/parse_message() — the closed vocabulary, pure function."""

    def test_normalize_collapses_whitespace_uppercases_strips_one_trailing_period(self):
        # real captured body: server trims outer whitespace, leaves internal runs
        self.assertEqual(ntfy_bridge.normalize("finish   up."), "FINISH UP")

    def test_every_vocabulary_word_matches_after_normalization(self):
        # each vocabulary word must match once normalized, case- and spacing-insensitive
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
        # a new ask makes the previous code stale
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

    def test_create_two_way_writes_one_topic_and_no_reply_topic(self):
        # A channel has exactly one topic; no reply_topic is written.
        entry_a = self.create_channel("chan-a", mode="two-way")
        entry_b = self.create_channel("chan-b", mode="two-way")
        self.assertIn("topic", entry_a)
        self.assertNotIn("reply_topic", entry_a)
        self.assertNotIn("reply_topic", entry_b)
        self.assertNotEqual(entry_a["topic"], entry_b["topic"])

    def test_rotate_replaces_the_topic_and_resets_state(self):
        entry = self.create_channel("rot-chan", mode="two-way")
        post = RecordingPost()
        get = RecordingGet([load_fixture("poll-one.jsonl")])
        run_main(["ask", "--name", "rot-chan", "--question", "q?", "--if-no-reply", "CONTINUE"], http_post=post)
        run_main(["poll", "--name", "rot-chan"], http_get=get)

        code, rotated, _, err = run_main(["rotate", "--name", "rot-chan"])
        self.assertEqual(code, 0, err)
        self.assertNotEqual(rotated["topic"], entry["topic"])
        self.assertNotIn("reply_topic", rotated)
        self.assertEqual(rotated["cursor"]["seen"], {})
        self.assertIsNone(rotated["pending"])
        self.assertEqual(rotated["unrecognized_total"], 0)
        self.assertEqual(len(rotated["rotations"]), 1)

    def test_topic_format_is_name_dash_ten_phone_typable_chars(self):
        # topic = <name>-<10 chars from the look-alike-free alphabet>.
        entry = self.create_channel("fmt-chan", mode="two-way")
        pattern = re.compile(r"^fmt-chan-[abcdefghjkmnpqrstuvwxyz23456789]{10}$")
        self.assertRegex(entry["topic"], pattern)
        self.assertNotIn("reply_topic", entry)

    def test_create_refuses_name_over_twelve_chars(self):
        code, _, _, err = run_main(
            ["create", "--name", "thirteen-chr1", "--mode", "one-way", "--purpose", "p", "--repo", "r"]
        )
        self.assertNotEqual(code, 0)
        self.assertIn("invalid channel name", err)

    def test_create_refuses_uppercase_name(self):
        code, _, _, err = run_main(
            ["create", "--name", "UPPERNAME", "--mode", "one-way", "--purpose", "p", "--repo", "r"]
        )
        self.assertNotEqual(code, 0)
        self.assertIn("invalid channel name", err)

    def test_create_refuses_empty_name_leaving_registry_unchanged(self):
        self.create_channel("seed-chan", mode="one-way")
        with open(self.registry_path, "rb") as f:
            before = f.read()
        code, _, _, err = run_main(
            ["create", "--name", "", "--mode", "one-way", "--purpose", "p", "--repo", "r"]
        )
        self.assertNotEqual(code, 0)
        with open(self.registry_path, "rb") as f:
            after = f.read()
        self.assertEqual(before, after)

    def test_create_accepts_twelve_char_name(self):
        entry = self.create_channel("max-name-len", mode="one-way")
        self.assertRegex(
            entry["topic"], re.compile(r"^max-name-len-[abcdefghjkmnpqrstuvwxyz23456789]{10}$")
        )

    def test_create_refuses_leading_hyphen_leaving_registry_unchanged(self):
        self.create_channel("seed-chan", mode="one-way")
        with open(self.registry_path, "rb") as f:
            before = f.read()
        code, _, _, err = run_main(
            ["create", "--name=-x", "--mode", "one-way", "--purpose", "p", "--repo", "r"]
        )
        self.assertNotEqual(code, 0)
        self.assertIn("invalid channel name", err)
        with open(self.registry_path, "rb") as f:
            after = f.read()
        self.assertEqual(before, after)

    def test_create_refuses_all_hyphens_leaving_registry_unchanged(self):
        self.create_channel("seed-chan", mode="one-way")
        with open(self.registry_path, "rb") as f:
            before = f.read()
        code, _, _, err = run_main(
            ["create", "--name=---", "--mode", "one-way", "--purpose", "p", "--repo", "r"]
        )
        self.assertNotEqual(code, 0)
        self.assertIn("invalid channel name", err)
        with open(self.registry_path, "rb") as f:
            after = f.read()
        self.assertEqual(before, after)

    def test_create_refuses_trailing_hyphen_leaving_registry_unchanged(self):
        self.create_channel("seed-chan", mode="one-way")
        with open(self.registry_path, "rb") as f:
            before = f.read()
        code, _, _, err = run_main(
            ["create", "--name", "abc-", "--mode", "one-way", "--purpose", "p", "--repo", "r"]
        )
        self.assertNotEqual(code, 0)
        self.assertIn("invalid channel name", err)
        with open(self.registry_path, "rb") as f:
            after = f.read()
        self.assertEqual(before, after)

    def test_create_refuses_two_char_name_ending_in_hyphen(self):
        self.create_channel("seed-chan", mode="one-way")
        with open(self.registry_path, "rb") as f:
            before = f.read()
        code, _, _, err = run_main(
            ["create", "--name", "a-", "--mode", "one-way", "--purpose", "p", "--repo", "r"]
        )
        self.assertNotEqual(code, 0)
        self.assertIn("invalid channel name", err)
        with open(self.registry_path, "rb") as f:
            after = f.read()
        self.assertEqual(before, after)

    def test_create_refuses_name_with_trailing_newline_leaving_registry_unchanged(self):
        # Python's $ matches before a final newline, so NAME_RE.match alone would
        # accept "tst-eval\n" and corrupt the topic; must use a full-string match.
        self.create_channel("seed-chan", mode="one-way")
        with open(self.registry_path, "rb") as f:
            before = f.read()
        code, _, _, err = run_main(
            ["create", "--name", "tst-eval\n", "--mode", "one-way", "--purpose", "p", "--repo", "r"]
        )
        self.assertNotEqual(code, 0)
        self.assertIn("invalid channel name", err)
        with open(self.registry_path, "rb") as f:
            after = f.read()
        self.assertEqual(before, after)

    def test_create_accepts_single_letter_name(self):
        entry = self.create_channel("a", mode="one-way")
        self.assertRegex(
            entry["topic"], re.compile(r"^a-[abcdefghjkmnpqrstuvwxyz23456789]{10}$")
        )

    def test_create_accepts_letter_digit_name(self):
        entry = self.create_channel("a1", mode="one-way")
        self.assertRegex(
            entry["topic"], re.compile(r"^a1-[abcdefghjkmnpqrstuvwxyz23456789]{10}$")
        )

    def test_create_accepts_internal_hyphen_name(self):
        entry = self.create_channel("tst-eval", mode="one-way")
        self.assertRegex(
            entry["topic"], re.compile(r"^tst-eval-[abcdefghjkmnpqrstuvwxyz23456789]{10}$")
        )

    def test_create_accepts_twelve_char_name_with_internal_hyphen(self):
        entry = self.create_channel("abcdef-ghijk", mode="one-way")
        self.assertRegex(
            entry["topic"], re.compile(r"^abcdef-ghijk-[abcdefghjkmnpqrstuvwxyz23456789]{10}$")
        )

    def test_rotate_gives_new_format_topic_to_a_pre_existing_long_name(self):
        # a registry entry with an old-style name (over 12 chars), an old-format
        # topic, and a leftover reply_topic (the old two-topic shape) must still
        # rotate cleanly into the new one-topic format, with reply_topic dropped.
        legacy_name = "legacy-long-channel-name"

        def fn(data):
            data[legacy_name] = {
                "topic": f"{legacy_name}-{'a' * 12}",
                "reply_topic": f"{legacy_name}-{'b' * 12}",
                "mode": "two-way",
                "purpose": "legacy",
                "repo": "r",
                "created": "2026-01-01",
                "interval_minutes": None,
                "cursor": {"since": 0, "seen": {"x": 1}},
                "pending": {"code": "AAAA", "asked": "2026-01-01"},
                "unrecognized_total": 3,
                "rotations": [],
            }

        ntfy_bridge.transact(self.registry_path, fn)

        code, rotated, _, err = run_main(["rotate", "--name", legacy_name])
        self.assertEqual(code, 0, err)
        pattern = re.compile(rf"^{legacy_name}-[abcdefghjkmnpqrstuvwxyz23456789]{{10}}$")
        self.assertRegex(rotated["topic"], pattern)
        self.assertNotIn("reply_topic", rotated)
        self.assertEqual(rotated["cursor"], {"since": rotated["cursor"]["since"], "seen": {}})
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
        self.create_channel("one-way-ch2", mode="one-way")
        code, _, _, err = run_main(["poll", "--name", "one-way-ch2"])
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

    def test_poll_url_uses_the_channel_topic(self):
        # There is no separate topic for replies; poll reads the one topic.
        entry = self.create_channel("topic-url-ch", mode="two-way")
        get = RecordingGet([load_fixture("poll-zero.jsonl")])
        run_main(["poll", "--name", "topic-url-ch"], http_get=get)
        self.assertEqual(len(get.urls), 1)
        topic = entry["topic"]
        self.assertTrue(get.urls[0].startswith(f"http://example.invalid/{topic}/json?poll=1&since="))

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


class OwnMessageDropTests(RegistryTestCase):
    """send/ask must mark their own published message as already seen (by the
    publish response's real id/time), so a later poll on the channel's one
    topic never parses the agent's own message as a reply or counts it as
    unrecognized.
    """

    def test_ask_echo_on_next_poll_yields_no_match_and_no_unrecognized(self):
        # publish-1.json is the real captured publish response for the exact
        # message poll-one.jsonl later serves back (same id/time) -- the shape
        # of an agent's own question coming back on its next poll.
        self.create_channel("echo-chan")
        post = RecordingPost(body=load_fixture("publish-1.json"))
        code, _, _, err = run_main(
            ["ask", "--name", "echo-chan", "--question", "proceed?", "--if-no-reply", "CONTINUE"],
            http_post=post,
        )
        self.assertEqual(code, 0, err)

        # clock pinned to the fixture era: a real wall clock would eventually
        # prune the own-message id past the 12h cache window and defeat dedup.
        get = RecordingGet([load_fixture("poll-one.jsonl")])
        code, result, _, err = run_main(
            ["poll", "--name", "echo-chan"], http_get=get, time_fn=FakeClock()
        )
        self.assertEqual(code, 0, err)
        self.assertEqual(result["matched"], [])
        self.assertEqual(result["unrecognized"], 0)

    def test_ask_echo_still_dropped_after_a_simulated_restart(self):
        # each run_main call reloads the registry from disk with no in-memory
        # state carried over, so two separate calls already simulate a process
        # restart; the own-message id, written to disk by ask, must still be
        # recognized as already-seen after that reload.
        self.create_channel("echo-restart")
        post = RecordingPost(body=load_fixture("publish-1.json"))
        code, _, _, err = run_main(
            ["ask", "--name", "echo-restart", "--question", "proceed?", "--if-no-reply", "CONTINUE"],
            http_post=post,
        )
        self.assertEqual(code, 0, err)

        get1 = RecordingGet([load_fixture("poll-one.jsonl")])
        code1, result1, _, err1 = run_main(
            ["poll", "--name", "echo-restart"], http_get=get1, time_fn=FakeClock()
        )
        self.assertEqual(code1, 0, err1)
        self.assertEqual((result1["matched"], result1["unrecognized"]), ([], 0))

        get2 = RecordingGet([load_fixture("poll-one.jsonl")])
        code2, result2, _, err2 = run_main(
            ["poll", "--name", "echo-restart"], http_get=get2, time_fn=FakeClock()
        )
        self.assertEqual(code2, 0, err2)
        self.assertEqual((result2["matched"], result2["unrecognized"]), ([], 0))

    def test_operator_stop_in_same_poll_as_echoed_own_message_is_still_acted_on(self):
        # poll-several carries the same "capture one" id as the ask echo, plus
        # a real STOP message with a different id: the STOP must still be
        # recognized even though the echoed own message in the same batch is
        # dropped.
        self.create_channel("echo-stop-ch")
        post = RecordingPost(body=load_fixture("publish-1.json"))
        code, _, _, err = run_main(
            ["ask", "--name", "echo-stop-ch", "--question", "proceed?", "--if-no-reply", "CONTINUE"],
            http_post=post,
        )
        self.assertEqual(code, 0, err)

        get = RecordingGet([load_fixture("poll-several.jsonl")])
        code, result, _, err = run_main(
            ["poll", "--name", "echo-stop-ch"], http_get=get, time_fn=FakeClock()
        )
        self.assertEqual(code, 0, err)
        self.assertEqual(result["acted_on"], "STOP")

    def test_send_records_its_own_message_as_seen(self):
        self.create_channel("send-echo-ch")
        post = RecordingPost(body=load_fixture("publish-1.json"))
        code, _, _, err = run_main(
            ["send", "--name", "send-echo-ch", "--message", "hello"], http_post=post
        )
        self.assertEqual(code, 0, err)

        get = RecordingGet([load_fixture("poll-one.jsonl")])
        code, result, _, err = run_main(
            ["poll", "--name", "send-echo-ch"], http_get=get, time_fn=FakeClock()
        )
        self.assertEqual(code, 0, err)
        self.assertEqual((result["matched"], result["unrecognized"]), ([], 0))

    def test_ask_publish_response_with_no_id_is_an_error_and_records_nothing(self):
        self.create_channel("bad-ask-chan")
        with open(self.registry_path, "rb") as f:
            before = f.read()
        post = RecordingPost(body=b"{}")
        code, _, _, err = run_main(
            ["ask", "--name", "bad-ask-chan", "--question", "q?", "--if-no-reply", "CONTINUE"],
            http_post=post,
        )
        self.assertNotEqual(code, 0)
        self.assertTrue(err.strip())
        with open(self.registry_path, "rb") as f:
            after = f.read()
        self.assertEqual(before, after)

    def test_send_publish_response_with_no_id_is_an_error_and_records_nothing(self):
        self.create_channel("bad-send-ch")
        with open(self.registry_path, "rb") as f:
            before = f.read()
        post = RecordingPost(body=b"not json")
        code, _, _, err = run_main(
            ["send", "--name", "bad-send-ch", "--message", "hello"], http_post=post
        )
        self.assertNotEqual(code, 0)
        self.assertTrue(err.strip())
        with open(self.registry_path, "rb") as f:
            after = f.read()
        self.assertEqual(before, after)


class WaitLoopTests(RegistryTestCase):
    """wait — the blocking poll loop: it must call the exact same poll logic as
    `poll` on every iteration, and classify every failure as transient (keep
    waiting) or permanent (stop) per the fixed rule in _classify_error.
    """

    # "STOP" and "finish   up." sliced out of the real poll-several capture, each a
    # different message id, so each is a genuinely new arrival across separate polls.
    STOP_LINE = single_message_line("poll-several.jsonl", 2)
    FINISH_UP_LINE = single_message_line("poll-several.jsonl", 1)

    def test_word_on_third_poll_exits_after_exactly_three_polls_with_right_json(self):
        # the loop must stop on the very poll that first produces a word, not later
        self.create_channel("third-poll")
        get = RecordingGet([load_fixture("poll-one.jsonl"), load_fixture("poll-zero.jsonl"), self.STOP_LINE])
        code, result, _, err = run_main(
            ["wait", "--name", "third-poll", "--interval", "1"], http_get=get, sleep_fn=FakeSleep()
        )
        self.assertEqual(code, 0, err)
        self.assertEqual(len(get.urls), 3)
        self.assertEqual(
            result,
            {
                "matched": ["STOP"],
                "acted_on": "STOP",
                "superseded": [],
                "unrecognized": 0,
                "unrecognized_total": 1,  # "capture one" from poll 1
            },
        )

    def test_first_poll_happens_before_any_sleep(self):
        # the loop must poll immediately, never sleep first
        self.create_channel("order-chan")
        order = []
        bodies = [load_fixture("poll-zero.jsonl"), self.STOP_LINE]

        def get(url):
            order.append("poll")
            return 200, bodies.pop(0)

        def sleep(seconds):
            order.append("sleep")

        code, _, _, err = run_main(["wait", "--name", "order-chan", "--interval", "1"], http_get=get, sleep_fn=sleep)
        self.assertEqual(code, 0, err)
        self.assertEqual(order, ["poll", "sleep", "poll"])

    def test_unrecognized_or_empty_polls_keep_waiting_until_a_word_arrives(self):
        # a poll with only unrecognized messages, or none, must not end the loop
        self.create_channel("keep-wait-ch")
        get = RecordingGet([load_fixture("poll-one.jsonl"), load_fixture("poll-zero.jsonl"), self.STOP_LINE])
        code, result, _, err = run_main(
            ["wait", "--name", "keep-wait-ch", "--interval", "1"], http_get=get, sleep_fn=FakeSleep()
        )
        self.assertEqual(code, 0, err)
        self.assertEqual(len(get.urls), 3)  # all three polls ran; nothing exited early
        self.assertEqual(result["acted_on"], "STOP")

    def test_interval_resolution_order_and_sleep_receives_seconds(self):
        # flag beats the registry entry beats the 20-minute default; sleep gets minutes*60
        scenarios = [
            ("flag-chan", 5, ["--interval", "2"], 2 * 60),
            ("registry-ch", 5, [], 5 * 60),
            ("default-chan", None, [], ntfy_bridge.DEFAULT_WAIT_INTERVAL_MINUTES * 60),
        ]
        for name, registry_interval, extra_flags, expected_seconds in scenarios:
            with self.subTest(name=name):
                create_args = ["create", "--name", name, "--mode", "two-way", "--purpose", "t", "--repo", "r"]
                if registry_interval is not None:
                    create_args += ["--interval", str(registry_interval)]
                code, _, _, err = run_main(create_args)
                self.assertEqual(code, 0, err)

                get = RecordingGet([load_fixture("poll-zero.jsonl"), self.STOP_LINE])
                sleep = FakeSleep()
                code, result, _, err = run_main(
                    ["wait", "--name", name] + extra_flags, http_get=get, sleep_fn=sleep
                )
                self.assertEqual(code, 0, err)
                self.assertEqual(sleep.calls, [expected_seconds])

    def test_zero_or_negative_interval_is_refused(self):
        # a non-positive interval is a config error: refuse before ever touching HTTP
        self.create_channel("bad-interval")
        for bad in ("0", "-5"):
            with self.subTest(interval=bad):
                code, _, _, err = run_main(
                    ["wait", "--name", "bad-interval", "--interval", bad], http_get=unexpected_get
                )
                self.assertNotEqual(code, 0)

    def test_transient_errors_keep_waiting_and_leave_registry_unchanged(self):
        # connection error, timeout, 500, 503, 429: logged, loop continues, no write on the failed poll
        errors = {
            "conn": urllib.error.URLError("simulated connection failure"),
            "timeout": TimeoutError("simulated timeout"),
            "500": urllib.error.HTTPError("http://x", 500, "Internal Server Error", None, None),
            "503": urllib.error.HTTPError("http://x", 503, "Service Unavailable", None, None),
            "429": urllib.error.HTTPError("http://x", 429, "Too Many Requests", None, None),
        }
        for label, error in errors.items():
            with self.subTest(label=label):
                name = f"tr-{label}"
                self.create_channel(name)
                inner = FailNthGet([load_fixture("poll-one.jsonl"), self.STOP_LINE], error, fail_at=2)
                get = SnapshottingGet(inner, self.registry_path)
                code, result, _, err = run_main(
                    ["wait", "--name", name, "--interval", "1"], http_get=get, sleep_fn=FakeSleep()
                )
                self.assertEqual(code, 0, err)
                self.assertEqual(result["acted_on"], "STOP")
                self.assertEqual(inner.call_count, 3)  # the failed poll did not stop the loop
                # snapshot before the failing call must equal the snapshot before the next one
                self.assertEqual(get.snapshots[1], get.snapshots[2])

    def test_permanent_http_errors_exit_non_zero_leaving_last_good_poll(self):
        # HTTP 4xx other than 429 is a permanent error: stop, do not retry
        for code_ in (400, 403, 404):
            with self.subTest(code=code_):
                name = f"perm-{code_}"
                self.create_channel(name)
                error = urllib.error.HTTPError("http://x", code_, "client error", None, None)
                inner = FailNthGet([load_fixture("poll-one.jsonl")], error, fail_at=2)
                get = SnapshottingGet(inner, self.registry_path)
                result_code, _, _, err = run_main(
                    ["wait", "--name", name, "--interval", "1"], http_get=get, sleep_fn=FakeSleep()
                )
                self.assertNotEqual(result_code, 0)
                self.assertTrue(err.strip())  # the cause is on stderr
                self.assertEqual(inner.call_count, 2)  # no retry after a permanent error
                with open(self.registry_path, "rb") as f:
                    after = f.read()
                self.assertEqual(after, get.snapshots[1])  # unchanged since the last good poll

    def test_corrupt_registry_exits_non_zero_with_cause_and_is_not_touched(self):
        # an unreadable registry is a permanent error, caught before any HTTP call
        self.create_channel("corrupt-chan")
        with open(self.registry_path, "w") as f:
            f.write("{not valid json")
        code, _, _, err = run_main(["wait", "--name", "corrupt-chan"], http_get=unexpected_get)
        self.assertNotEqual(code, 0)
        self.assertTrue(err.strip())
        with open(self.registry_path) as f:
            self.assertEqual(f.read(), "{not valid json")

    def test_restart_after_printed_word_does_not_return_it_again(self):
        # the cursor persists on disk: a replayed message must not fire its word twice.
        # Clock pinned to the fixture era (real wall time would prune the "seen" id
        # past the 12h cache window and defeat the dedup this test proves).
        name = "restart-chan"
        self.create_channel(name)
        get1 = RecordingGet([self.STOP_LINE])
        code1, result1, _, err1 = run_main(
            ["wait", "--name", name, "--interval", "1"], http_get=get1, sleep_fn=FakeSleep(), time_fn=FakeClock()
        )
        self.assertEqual(code1, 0, err1)
        self.assertEqual(result1["acted_on"], "STOP")

        # a fresh wait, as if the process had restarted, replays the same message once
        # more (the server's cache), then serves one genuinely new message
        get2 = RecordingGet([self.STOP_LINE, self.FINISH_UP_LINE])
        code2, result2, _, err2 = run_main(
            ["wait", "--name", name, "--interval", "1"], http_get=get2, sleep_fn=FakeSleep(), time_fn=FakeClock()
        )
        self.assertEqual(code2, 0, err2)
        self.assertEqual(result2["acted_on"], "FINISH UP")
        self.assertIn("matched=0", err2)  # the replayed STOP did not fire again


class RegistryDefaultPathTests(unittest.TestCase):
    """The registry default path must live under the user config dir, not the repo."""

    def test_default_registry_path_is_under_user_config_dir(self):
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        self.assertTrue(ntfy_bridge.DEFAULT_REGISTRY_PATH.startswith(os.path.expanduser("~")))
        self.assertIn(".config/ntfy-bridge/channels.json", ntfy_bridge.DEFAULT_REGISTRY_PATH)
        self.assertFalse(ntfy_bridge.DEFAULT_REGISTRY_PATH.startswith(repo_root))


if __name__ == "__main__":
    unittest.main()
