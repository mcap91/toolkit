#!/usr/bin/env python3
"""ntfy phone bridge: channel registry, send, ask, poll. See SKILL.md.

Config is env-only (no other paths or names are hardcoded):
  NTFY_BRIDGE_REGISTRY  -- registry JSON path (default: ~/.config/ntfy-bridge/channels.json)
  NTFY_BRIDGE_SERVER    -- ntfy server base URL (default: https://ntfy.sh)
"""
import argparse
import fcntl
import json
import os
import re
import secrets
import sys
import tempfile
import time
import urllib.error
import urllib.request
from datetime import date

DEFAULT_REGISTRY_PATH = os.path.expanduser("~/.config/ntfy-bridge/channels.json")
DEFAULT_SERVER = "https://ntfy.sh"
CACHE_WINDOW_SECONDS = 43200  # ntfy.sh observed cache window (12h)
DEFAULT_WAIT_INTERVAL_MINUTES = 20

# Fixed precedence, low to high priority in iteration order below (first match wins).
PRECEDENCE_ORDER = ["STOP", "FINISH UP", "PAUSE", "APPROVE", "CONTINUE", "STATUS"]
NAME_RE = re.compile(r"^[a-z0-9]([a-z0-9-]{0,10}[a-z0-9])?$")
APPROVE_RE = re.compile(r"^APPROVE ([0-9A-F]{4})$")
EXACT_WORDS = {"STOP", "FINISH UP", "PAUSE", "CONTINUE", "STATUS"}
# Phone-typable topic suffix: lowercase letters and digits minus look-alikes.
TOPIC_SUFFIX_ALPHABET = "abcdefghjkmnpqrstuvwxyz23456789"
TOPIC_SUFFIX_LENGTH = 10


class NtfyBridgeError(Exception):
    """A user-facing error: unknown channel, wrong mode, bad input."""


# --- vocabulary parser (pure function) --------------------------------------

def normalize(text):
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    text = text.upper()
    if text.endswith("."):
        text = text[:-1]
    return text


def parse_message(raw_text, pending_code):
    """Return the matched canonical word, or None if unrecognized."""
    norm = normalize(raw_text)
    if norm in EXACT_WORDS:
        return norm
    m = APPROVE_RE.match(norm)
    if m is not None and pending_code is not None and m.group(1) == pending_code:
        return norm
    return None


def _category(word):
    return "APPROVE" if word.startswith("APPROVE ") else word


def process_poll(body_text, cursor, pending_code, now):
    """Pure poll-response processor: cursor in, (new_cursor, matched, acted_on,
    superseded, unrecognized) out. `now` is injected so cache pruning is testable.
    Matched/acted_on/superseded are derived by fixed precedence, never by arrival
    order, so same-second server reordering cannot change the result.
    """
    since = cursor.get("since", 0)
    seen = dict(cursor.get("seen", {}))
    messages = []
    for line in body_text.splitlines():
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        if obj.get("event") != "message":
            continue
        messages.append(obj)

    new_messages = [m for m in messages if m["id"] not in seen]
    matched_words = []
    unrecognized = 0
    for m in new_messages:
        seen[m["id"]] = m["time"]
        word = parse_message(m.get("message", ""), pending_code)
        if word is None:
            unrecognized += 1
        else:
            matched_words.append(word)

    cats = {}
    for w in matched_words:
        cats[_category(w)] = w
    matched = [cats[c] for c in PRECEDENCE_ORDER if c in cats]
    acted_on = matched[0] if matched else None
    superseded = matched[1:]

    all_times = [m["time"] for m in messages]
    new_since = max([since] + all_times) if all_times else since

    cutoff = now - CACHE_WINDOW_SECONDS
    seen = {mid: t for mid, t in seen.items() if t >= cutoff}

    new_cursor = {"since": new_since, "seen": seen}
    return new_cursor, matched, acted_on, superseded, unrecognized


# --- registry: temp-file-plus-rename writes under an fcntl lock ------------

def _ensure_dir(path):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)


def read_registry(path):
    """Shared-lock read. Returns {} if the registry does not exist yet."""
    if not os.path.exists(path):
        return {}
    _ensure_dir(path)
    with open(path + ".lock", "a+") as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_SH)
        try:
            with open(path, "r") as f:
                content = f.read()
        finally:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
    return json.loads(content) if content.strip() else {}


def transact(path, fn):
    """Exclusive-lock read-modify-write. `fn(data)` mutates `data` in place and
    returns a result. If `fn` raises, `data` is never written back, so a failed
    send/ask/poll leaves the registry unchanged.
    """
    _ensure_dir(path)
    with open(path + ".lock", "a+") as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        try:
            if os.path.exists(path):
                with open(path, "r") as f:
                    content = f.read()
                data = json.loads(content) if content.strip() else {}
            else:
                data = {}

            result = fn(data)

            dir_name = os.path.dirname(path) or "."
            fd, tmp_path = tempfile.mkstemp(dir=dir_name, prefix=".ntfy-bridge-tmp-")
            try:
                with os.fdopen(fd, "w") as tmp:
                    json.dump(data, tmp, indent=2, sort_keys=True)
                    tmp.write("\n")
                os.replace(tmp_path, path)
            except Exception:
                os.unlink(tmp_path)
                raise
            return result
        finally:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)


def _new_topic(name):
    suffix = "".join(secrets.choice(TOPIC_SUFFIX_ALPHABET) for _ in range(TOPIC_SUFFIX_LENGTH))
    return f"{name}-{suffix}"


def _require_channel(data, name):
    if name not in data:
        raise NtfyBridgeError(f"unknown channel: {name}")
    return data[name]


def _require_two_way(entry, name, action):
    if entry["mode"] != "two-way":
        raise NtfyBridgeError(f"channel '{name}' is one-way; {action} requires two-way")


# --- HTTP (real implementation; tests inject fakes) -------------------------

def http_post(url, body, headers):
    req = urllib.request.Request(url, data=body.encode("utf-8"), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.status, resp.read()


def http_get(url):
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.status, resp.read()


# --- subcommands -------------------------------------------------------------

def cmd_list(args, registry_path):
    data = read_registry(registry_path)
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0


def cmd_create(args, registry_path):
    if not NAME_RE.fullmatch(args.name):
        raise NtfyBridgeError(
            f"invalid channel name: {args.name!r} "
            "(must be 1-12 characters of lowercase letters, digits, and hyphens, "
            "starting and ending with a letter or digit)"
        )

    def fn(data):
        if args.name in data:
            raise NtfyBridgeError(f"channel already exists: {args.name}")
        now = int(time.time())
        entry = {
            "topic": _new_topic(args.name),
            "reply_topic": _new_topic(args.name) if args.mode == "two-way" else None,
            "mode": args.mode,
            "purpose": args.purpose,
            "repo": args.repo,
            "created": date.today().isoformat(),
            "interval_minutes": args.interval,
            "cursor": {"since": now, "seen": {}},
            "pending": None,
            "unrecognized_total": 0,
            "rotations": [],
        }
        data[args.name] = entry
        return entry

    entry = transact(registry_path, fn)
    print(json.dumps(entry, indent=2, sort_keys=True))
    return 0


def cmd_rotate(args, registry_path):
    def fn(data):
        entry = _require_channel(data, args.name)
        now = int(time.time())
        entry["topic"] = _new_topic(args.name)
        if entry["mode"] == "two-way":
            entry["reply_topic"] = _new_topic(args.name)
        entry["cursor"] = {"since": now, "seen": {}}
        entry["pending"] = None
        entry["unrecognized_total"] = 0
        entry.setdefault("rotations", []).append(date.today().isoformat())
        return entry

    entry = transact(registry_path, fn)
    print(json.dumps(entry, indent=2, sort_keys=True))
    return 0


def cmd_send(args, registry_path, server, post_fn):
    data = read_registry(registry_path)
    entry = _require_channel(data, args.name)
    headers = {}
    if args.title is not None:
        headers["Title"] = args.title
    if args.priority is not None:
        headers["Priority"] = args.priority
    url = f"{server}/{entry['topic']}"
    try:
        post_fn(url, args.message, headers)
    except (urllib.error.URLError, OSError) as e:
        raise NtfyBridgeError(f"send failed: {e}") from e
    print(json.dumps({"name": args.name, "topic": entry["topic"], "sent": True}, indent=2, sort_keys=True))
    return 0


def cmd_ask(args, registry_path, server, post_fn):
    def fn(data):
        entry = _require_channel(data, args.name)
        _require_two_way(entry, args.name, "ask")
        code = secrets.token_hex(2).upper()
        body = f"{args.question}\nReply APPROVE {code}.\n{args.if_no_reply}"
        url = f"{server}/{entry['topic']}"
        post_fn(url, body, {"Priority": "high"})
        entry["pending"] = {"code": code, "asked": date.today().isoformat()}
        return code

    try:
        code = transact(registry_path, fn)
    except (urllib.error.URLError, OSError) as e:
        raise NtfyBridgeError(f"ask failed: {e}") from e
    print(json.dumps({"name": args.name, "code": code, "sent": True}, indent=2, sort_keys=True))
    return 0


def _do_poll(entry, name, server, get_fn, now):
    """One poll of a channel's reply topic: request, dedup, prune, parse, pick
    the word acted on by precedence, mutate `entry` in place, return the
    result dict. The only poll logic in the script; `poll` and `wait` both
    call this so they can never drift apart.
    """
    _require_two_way(entry, name, "poll")
    since = entry["cursor"]["since"]
    url = f"{server}/{entry['reply_topic']}/json?poll=1&since={since}"
    status, body = get_fn(url)
    pending = entry.get("pending")
    pending_code = pending["code"] if pending else None
    new_cursor, matched, acted_on, superseded, unrecognized = process_poll(
        body.decode("utf-8"), entry["cursor"], pending_code, now=now
    )
    entry["cursor"] = new_cursor
    approved = acted_on is not None and acted_on.startswith("APPROVE ")
    if approved:
        entry["pending"] = None
    entry["unrecognized_total"] = entry.get("unrecognized_total", 0) + unrecognized
    return {
        "matched": matched,
        "acted_on": acted_on,
        "superseded": superseded,
        "unrecognized": unrecognized,
        "unrecognized_total": entry["unrecognized_total"],
    }


def cmd_poll(args, registry_path, server, get_fn, time_fn):
    def fn(data):
        entry = _require_channel(data, args.name)
        return _do_poll(entry, args.name, server, get_fn, now=time_fn())

    try:
        result = transact(registry_path, fn)
    except (urllib.error.URLError, OSError) as e:
        raise NtfyBridgeError(f"poll failed: {e}") from e
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


# --- wait: the blocking poll loop -------------------------------------------

def _classify_error(exc):
    """Sort a wait-loop failure: "transient" keeps waiting, "permanent" stops.
    Connection errors, timeouts, HTTP 5xx, and HTTP 429 are transient; every
    other failure (other HTTP 4xx, bad config, a corrupt registry, an unknown
    or one-way channel) is permanent.
    """
    if isinstance(exc, urllib.error.HTTPError):
        return "transient" if exc.code == 429 or 500 <= exc.code < 600 else "permanent"
    if isinstance(exc, (TimeoutError, urllib.error.URLError, OSError)):
        return "transient"
    return "permanent"


def _error_label(exc):
    """Stderr label for a transient failure: error class and HTTP status only."""
    if isinstance(exc, urllib.error.HTTPError):
        return f"http {exc.code}"
    if isinstance(exc, TimeoutError):
        return "timeout"
    return "connection error"


def _resolve_wait_interval(flag_value, entry):
    interval = flag_value if flag_value is not None else entry.get("interval_minutes")
    if interval is None:
        interval = DEFAULT_WAIT_INTERVAL_MINUTES
    if interval <= 0:
        raise NtfyBridgeError(f"invalid interval: {interval} (must be a positive number of minutes)")
    return interval


def _stamp(epoch_seconds):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch_seconds))


def cmd_wait(args, registry_path, server, get_fn, sleep_fn, time_fn):
    try:
        data = read_registry(registry_path)
        entry = _require_channel(data, args.name)
        _require_two_way(entry, args.name, "wait")
        interval = _resolve_wait_interval(args.interval, entry)
    except NtfyBridgeError:
        raise
    except Exception as e:
        raise NtfyBridgeError(str(e)) from e

    def fn(data):
        entry = _require_channel(data, args.name)
        return _do_poll(entry, args.name, server, get_fn, now=time_fn())

    while True:
        try:
            result = transact(registry_path, fn)
        except Exception as e:
            if _classify_error(e) == "permanent":
                raise NtfyBridgeError(str(e)) from e
            print(f"{_stamp(time_fn())} transient: {_error_label(e)}", file=sys.stderr, flush=True)
            sleep_fn(interval * 60)
            continue

        now = time_fn()
        print(
            f"{_stamp(now)} channel={args.name} matched={len(result['matched'])} "
            f"unrecognized={result['unrecognized']} next_poll={_stamp(now + interval * 60)}",
            file=sys.stderr,
            flush=True,
        )
        if result["acted_on"] is not None:
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0
        sleep_fn(interval * 60)


# --- CLI ---------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(prog="ntfy_bridge.py")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list")

    p = sub.add_parser("create")
    p.add_argument("--name", required=True)
    p.add_argument("--mode", required=True, choices=["one-way", "two-way"])
    p.add_argument("--purpose", required=True)
    p.add_argument("--repo", required=True)
    p.add_argument("--interval", type=int, default=None)

    p = sub.add_parser("rotate")
    p.add_argument("--name", required=True)

    p = sub.add_parser("send")
    p.add_argument("--name", required=True)
    p.add_argument("--message", required=True)
    p.add_argument("--title", default=None)
    p.add_argument("--priority", choices=["default", "high"], default=None)

    p = sub.add_parser("ask")
    p.add_argument("--name", required=True)
    p.add_argument("--question", required=True)
    p.add_argument("--if-no-reply", dest="if_no_reply", required=True)

    p = sub.add_parser("poll")
    p.add_argument("--name", required=True)

    p = sub.add_parser("wait")
    p.add_argument("--name", required=True)
    p.add_argument("--interval", type=float, default=None)

    return parser


def main(argv=None, *, http_get=http_get, http_post=http_post, sleep_fn=time.sleep, time_fn=time.time):
    parser = build_parser()
    args = parser.parse_args(argv)

    registry_path = os.environ.get("NTFY_BRIDGE_REGISTRY", DEFAULT_REGISTRY_PATH)
    server = os.environ.get("NTFY_BRIDGE_SERVER", DEFAULT_SERVER)

    try:
        if args.command == "list":
            return cmd_list(args, registry_path)
        if args.command == "create":
            return cmd_create(args, registry_path)
        if args.command == "rotate":
            return cmd_rotate(args, registry_path)
        if args.command == "send":
            return cmd_send(args, registry_path, server, http_post)
        if args.command == "ask":
            return cmd_ask(args, registry_path, server, http_post)
        if args.command == "poll":
            return cmd_poll(args, registry_path, server, http_get, time_fn)
        if args.command == "wait":
            return cmd_wait(args, registry_path, server, http_get, sleep_fn, time_fn)
        raise NtfyBridgeError(f"unknown command: {args.command}")
    except NtfyBridgeError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    except (urllib.error.URLError, OSError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
