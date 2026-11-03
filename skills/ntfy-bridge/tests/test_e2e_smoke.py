"""End-to-end smoke test: runs ntfy_bridge.py as a real subprocess against a
localhost http.server that replays the golden fixtures. Never contacts ntfy.sh
(NTFY_BRIDGE_SERVER always points at 127.0.0.1); real-network checks against a
live ntfy.sh channel are separate, manual, and out of scope here.
"""
import http.server
import json
import os
import subprocess
import sys
import tempfile
import threading
import unittest

HERE = os.path.dirname(__file__)
SCRIPT = os.path.join(HERE, "..", "ntfy_bridge.py")
FIXTURES = os.path.join(HERE, "fixtures")


def load_fixture(name):
    with open(os.path.join(FIXTURES, name), "rb") as f:
        return f.read()


class FixtureReplayHandler(http.server.BaseHTTPRequestHandler):
    """Serves canned publish/poll responses, recording every request path."""

    poll_bodies = []  # class-level: set per test before the server starts
    requests = []

    def _record(self):
        FixtureReplayHandler.requests.append((self.command, self.path))

    def do_POST(self):
        self._record()
        length = int(self.headers.get("Content-Length", 0))
        self.rfile.read(length)
        body = load_fixture("publish-1.json")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._record()
        item = FixtureReplayHandler.poll_bodies.pop(0) if FixtureReplayHandler.poll_bodies else b""
        status, body = item if isinstance(item, tuple) else (200, item)
        self.send_response(status)
        self.send_header("Content-Type", "application/x-ndjson")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass  # keep test output quiet


class SmokeTest(unittest.TestCase):
    def setUp(self):
        FixtureReplayHandler.requests = []
        FixtureReplayHandler.poll_bodies = [
            load_fixture("poll-one.jsonl"),
            load_fixture("poll-several.jsonl"),
        ]
        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), FixtureReplayHandler)
        self.port = self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

        self.tmpdir = tempfile.TemporaryDirectory()
        self.registry_path = os.path.join(self.tmpdir.name, "channels.json")
        self.env = dict(os.environ)
        self.env["NTFY_BRIDGE_SERVER"] = f"http://127.0.0.1:{self.port}"
        self.env["NTFY_BRIDGE_REGISTRY"] = self.registry_path

    def tearDown(self):
        self.server.shutdown()
        self.thread.join(timeout=5)
        self.server.server_close()
        self.tmpdir.cleanup()

    def run_cli(self, *args):
        proc = subprocess.run(
            [sys.executable, SCRIPT, *args],
            env=self.env,
            capture_output=True,
            text=True,
            timeout=10,
        )
        return proc

    def test_create_send_ask_poll_twice_hits_expected_paths(self):
        create = self.run_cli(
            "create", "--name", "smoke-chan", "--mode", "two-way",
            "--purpose", "smoke test", "--repo", "test-repo",
        )
        self.assertEqual(create.returncode, 0, create.stderr)
        entry = json.loads(create.stdout)
        topic, reply_topic = entry["topic"], entry["reply_topic"]

        send = self.run_cli("send", "--name", "smoke-chan", "--message", "hello")
        self.assertEqual(send.returncode, 0, send.stderr)

        ask = self.run_cli(
            "ask", "--name", "smoke-chan", "--question", "proceed?", "--if-no-reply", "CONTINUE"
        )
        self.assertEqual(ask.returncode, 0, ask.stderr)

        poll1 = self.run_cli("poll", "--name", "smoke-chan")
        self.assertEqual(poll1.returncode, 0, poll1.stderr)
        result1 = json.loads(poll1.stdout)
        self.assertEqual(result1["unrecognized"], 1)  # "capture one" is not a vocabulary word

        poll2 = self.run_cli("poll", "--name", "smoke-chan")
        self.assertEqual(poll2.returncode, 0, poll2.stderr)
        result2 = json.loads(poll2.stdout)
        # 5 new messages in poll-several beyond poll-one's single repeat
        self.assertEqual(len(result2["matched"]) + result2["unrecognized"], 5)

        methods_paths = FixtureReplayHandler.requests
        post_paths = [p for m, p in methods_paths if m == "POST"]
        get_paths = [p for m, p in methods_paths if m == "GET"]
        self.assertEqual(post_paths, [f"/{topic}", f"/{topic}"])  # send, then ask
        self.assertEqual(len(get_paths), 2)  # poll, poll
        for p in get_paths:
            self.assertTrue(p.startswith(f"/{reply_topic}/json?poll=1&since="))

    def run_wait(self, name, *extra_args):
        return subprocess.run(
            [sys.executable, SCRIPT, "wait", "--name", name, "--interval", "0.01", *extra_args],
            env=self.env,
            capture_output=True,
            text=True,
            timeout=10,
        )

    def test_wait_polls_twice_then_exits_with_json_on_a_vocabulary_word(self):
        FixtureReplayHandler.poll_bodies = [b"", load_fixture("poll-several.jsonl")]
        create = self.run_cli(
            "create", "--name", "wait-smoke", "--mode", "two-way",
            "--purpose", "smoke test", "--repo", "test-repo",
        )
        self.assertEqual(create.returncode, 0, create.stderr)
        entry = json.loads(create.stdout)

        proc = self.run_wait("wait-smoke")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        result = json.loads(proc.stdout)
        self.assertEqual(result["acted_on"], "STOP")

        get_paths = [p for m, p in FixtureReplayHandler.requests if m == "GET"]
        self.assertGreaterEqual(len(get_paths), 2)
        self.assertTrue(proc.stderr.strip())  # the live log line
        self.assertNotIn(entry["reply_topic"], proc.stderr)
        self.assertNotIn("capture", proc.stderr)  # no message text leaks into the log

    def test_wait_retries_a_503_then_exits_with_json(self):
        FixtureReplayHandler.poll_bodies = [(503, b""), load_fixture("poll-several.jsonl")]
        create = self.run_cli(
            "create", "--name", "wait-smoke-503", "--mode", "two-way",
            "--purpose", "smoke test", "--repo", "test-repo",
        )
        self.assertEqual(create.returncode, 0, create.stderr)
        entry = json.loads(create.stdout)

        proc = self.run_wait("wait-smoke-503")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        result = json.loads(proc.stdout)
        self.assertEqual(result["acted_on"], "STOP")
        self.assertIn("503", proc.stderr)  # the transient retry is logged
        self.assertNotIn(entry["reply_topic"], proc.stderr)
        self.assertNotIn("capture", proc.stderr)

    def test_wait_exits_non_zero_on_a_404(self):
        FixtureReplayHandler.poll_bodies = [(404, b"")]
        create = self.run_cli(
            "create", "--name", "wait-smoke-404", "--mode", "two-way",
            "--purpose", "smoke test", "--repo", "test-repo",
        )
        self.assertEqual(create.returncode, 0, create.stderr)

        proc = self.run_wait("wait-smoke-404")
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("404", proc.stderr)  # the cause is on stderr


if __name__ == "__main__":
    unittest.main()
