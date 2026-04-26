#!/usr/bin/env python3
"""
Slack export → inbox/slack/

Reads a Slack workspace JSON export (extracted directory or .zip) and
writes one markdown file per thread to inbox/slack/YYYY-MM-DD-<channel>-<short>.md.

This is a scaffold. Adapt the channel selection and noise filtering to your needs.

Usage:
    python scripts/import/slack-export.py <export-dir-or-zip> [--channels eng-platform,prd-feedback]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INBOX = ROOT / "inbox" / "slack"


def slug(s: str, max_len: int = 40) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.strip().lower()).strip("-")
    return s[:max_len] or "thread"


def thread_to_md(thread: list[dict], channel: str) -> str:
    lines = [f"# #{channel} thread", ""]
    for msg in thread:
        ts = float(msg.get("ts", 0))
        when = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        user = msg.get("user_profile", {}).get("real_name") or msg.get("user", "?")
        text = msg.get("text", "").strip()
        lines.append(f"**{user}** — {when}")
        lines.append("")
        lines.append(text)
        lines.append("")
    return "\n".join(lines)


def iter_thread_groups(messages: list[dict]):
    by_thread: dict[str, list[dict]] = {}
    for m in messages:
        thread_ts = m.get("thread_ts") or m.get("ts")
        by_thread.setdefault(thread_ts, []).append(m)
    for ts, msgs in by_thread.items():
        msgs.sort(key=lambda x: float(x.get("ts", 0)))
        yield msgs


def process_dir(export_dir: Path, channels: set[str] | None) -> int:
    INBOX.mkdir(parents=True, exist_ok=True)
    written = 0
    for channel_dir in sorted(p for p in export_dir.iterdir() if p.is_dir()):
        if channels and channel_dir.name not in channels:
            continue
        for day_file in sorted(channel_dir.glob("*.json")):
            try:
                msgs = json.loads(day_file.read_text())
            except json.JSONDecodeError:
                continue
            for thread in iter_thread_groups(msgs):
                if len(thread) < 2:
                    continue  # skip non-threaded chatter
                first = thread[0]
                ts = float(first.get("ts", 0))
                when = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
                short = slug(first.get("text", ""))
                fn = f"{when}-{channel_dir.name}-{short}.md"
                (INBOX / fn).write_text(thread_to_md(thread, channel_dir.name))
                written += 1
    return written


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("export", help="Slack export directory or .zip")
    parser.add_argument("--channels", help="Comma-separated channel names to include")
    args = parser.parse_args()

    src = Path(args.export)
    channels = set(c.strip() for c in args.channels.split(",")) if args.channels else None

    if src.suffix == ".zip":
        with zipfile.ZipFile(src) as zf:
            tmp = src.with_suffix("")
            tmp.mkdir(exist_ok=True)
            zf.extractall(tmp)
            src = tmp

    if not src.is_dir():
        print(f"error: {src} is not a directory or zip", file=sys.stderr)
        return 1

    count = process_dir(src, channels)
    print(f"wrote {count} thread file(s) to {INBOX.relative_to(ROOT)}")
    print("next: run /intake on the inbox.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
