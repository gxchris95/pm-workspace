#!/usr/bin/env python3
"""
Surface eval cases for manual review across all skills.

For each skill, lists the should_trigger and should_not_trigger phrases.
Flags potential collisions: phrases listed in multiple skills' should_trigger.

Run: python scripts/run-evals.py [--report evals-report.md]
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"


def load_evals() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        evals_path = skill_dir / "evals.json"
        if not evals_path.exists():
            continue
        try:
            out[skill_dir.name] = json.loads(evals_path.read_text())
        except json.JSONDecodeError as e:
            print(f"warn: skipping {evals_path.relative_to(ROOT)} ({e})", file=sys.stderr)
    return out


def find_collisions(evals: dict[str, dict]) -> dict[str, list[str]]:
    """Phrases that appear in multiple skills' should_trigger."""
    seen: dict[str, list[str]] = defaultdict(list)
    for skill, data in evals.items():
        for phrase in data.get("should_trigger", []):
            seen[phrase.strip().lower()].append(skill)
    return {p: skills for p, skills in seen.items() if len(skills) > 1}


def render_text(evals: dict[str, dict]) -> str:
    lines: list[str] = []
    for skill, data in evals.items():
        lines.append(f"\n=== /{skill} ===")
        lines.append(f"  should_trigger ({len(data.get('should_trigger', []))}):")
        for p in data.get("should_trigger", []):
            lines.append(f"    + {p}")
        lines.append(f"  should_not_trigger ({len(data.get('should_not_trigger', []))}):")
        for p in data.get("should_not_trigger", []):
            lines.append(f"    - {p}")

    collisions = find_collisions(evals)
    if collisions:
        lines.append("\n=== COLLISIONS (phrases triggering multiple skills) ===")
        for phrase, skills in sorted(collisions.items()):
            lines.append(f"  '{phrase}' -> {', '.join(skills)}")
    else:
        lines.append("\nNo collisions detected.")
    return "\n".join(lines)


def render_markdown(evals: dict[str, dict]) -> str:
    out: list[str] = ["# Eval Report\n"]
    out.append(f"Skills: **{len(evals)}**\n")
    total_trigger = sum(len(d.get("should_trigger", [])) for d in evals.values())
    total_not = sum(len(d.get("should_not_trigger", [])) for d in evals.values())
    out.append(f"Total should_trigger cases: **{total_trigger}**")
    out.append(f"Total should_not_trigger cases: **{total_not}**\n")

    for skill, data in evals.items():
        out.append(f"\n## /{skill}\n")
        out.append("### should_trigger\n")
        for p in data.get("should_trigger", []):
            out.append(f"- {p}")
        out.append("\n### should_not_trigger\n")
        for p in data.get("should_not_trigger", []):
            out.append(f"- {p}")

    collisions = find_collisions(evals)
    out.append("\n## Collisions\n")
    if collisions:
        out.append("Phrases that trigger multiple skills (consider sharpening one description):\n")
        for phrase, skills in sorted(collisions.items()):
            out.append(f"- `{phrase}` → {', '.join('/' + s for s in skills)}")
    else:
        out.append("No collisions detected.")
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", help="Write a markdown report to this path")
    args = parser.parse_args()

    evals = load_evals()
    if not evals:
        print("No skills with evals.json found.", file=sys.stderr)
        return 1

    if args.report:
        Path(args.report).write_text(render_markdown(evals))
        print(f"wrote {args.report}")
    else:
        print(render_text(evals))
    return 0


if __name__ == "__main__":
    sys.exit(main())
