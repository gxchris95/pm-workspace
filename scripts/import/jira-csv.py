#!/usr/bin/env python3
"""
Jira CSV export → inbox/jira/

Reads a Jira CSV (Issues view export) and writes one markdown file per ticket
to inbox/jira/YYYY-MM-DD-<key>-<short>.md.

This is a scaffold. Adjust the column names to match your Jira export.

Usage:
    python scripts/import/jira-csv.py <export.csv> [--statuses "To Do,In Progress"]
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INBOX = ROOT / "inbox" / "jira"

DEFAULT_COLS = {
    "key": "Issue key",
    "summary": "Summary",
    "status": "Status",
    "priority": "Priority",
    "assignee": "Assignee",
    "reporter": "Reporter",
    "created": "Created",
    "description": "Description",
    "labels": "Labels",
}


def slug(s: str, max_len: int = 40) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.strip().lower()).strip("-")
    return s[:max_len] or "ticket"


def to_md(row: dict[str, str], cols: dict[str, str]) -> str:
    out: list[str] = []
    out.append(f"# {row.get(cols['key'], '?')} — {row.get(cols['summary'], '')}")
    out.append("")
    out.append(f"- **Status**: {row.get(cols['status'], '')}")
    out.append(f"- **Priority**: {row.get(cols['priority'], '')}")
    out.append(f"- **Assignee**: {row.get(cols['assignee'], '')}")
    out.append(f"- **Reporter**: {row.get(cols['reporter'], '')}")
    out.append(f"- **Created**: {row.get(cols['created'], '')}")
    out.append(f"- **Labels**: {row.get(cols['labels'], '')}")
    out.append("")
    out.append("## Description")
    out.append("")
    out.append(row.get(cols["description"], "").strip() or "_(empty)_")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="Jira CSV export path")
    parser.add_argument("--statuses", help="Comma-separated statuses to include (default: all)")
    args = parser.parse_args()

    src = Path(args.csv)
    if not src.exists():
        print(f"error: {src} not found", file=sys.stderr)
        return 1

    statuses = (
        {s.strip() for s in args.statuses.split(",")} if args.statuses else None
    )

    INBOX.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    count = 0
    with src.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            if statuses and row.get(DEFAULT_COLS["status"]) not in statuses:
                continue
            key = row.get(DEFAULT_COLS["key"], "TICKET")
            short = slug(row.get(DEFAULT_COLS["summary"], ""))
            fn = f"{today}-{key}-{short}.md"
            (INBOX / fn).write_text(to_md(row, DEFAULT_COLS))
            count += 1

    print(f"wrote {count} ticket file(s) to {INBOX.relative_to(ROOT)}")
    print("next: run /intake on the inbox.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
