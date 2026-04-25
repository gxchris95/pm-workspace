#!/usr/bin/env python3
"""
PM Workspace validator.

Checks:
- Every skills/<name>/SKILL.md has agentskills.io-compliant frontmatter:
    * name (lowercase, hyphens, <=64 chars, matches parent dir)
    * description (<=1024 chars, mentions "use" or "when")
- Every skill has an evals.json with should_trigger and should_not_trigger arrays
- Every wiki page has YAML frontmatter with last_updated
- Product pages have product, status, adoption
- Topic pages have topic

Exit code: 0 on success, 1 if any errors found.
Run: python scripts/validate.py [--strict]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent

NAME_RE = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    out: dict = {}
    block = m.group(1)
    current_key: str | None = None
    for raw in block.splitlines():
        if not raw.strip():
            continue
        if raw.startswith(" ") and current_key is not None:
            # nested value — record as raw string under current_key as dict-ish
            existing = out.setdefault(current_key, {})
            if isinstance(existing, dict):
                kv = raw.strip()
                if ":" in kv:
                    k, v = kv.split(":", 1)
                    existing[k.strip()] = v.strip()
            continue
        if ":" not in raw:
            continue
        key, val = raw.split(":", 1)
        out[key.strip()] = val.strip()
        current_key = key.strip()
    return out


def err(errors: list[str], path: Path, msg: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def check_skills(errors: list[str]) -> None:
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        err(errors, skills_dir, "skills/ directory missing")
        return
    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        evals = skill_dir / "evals.json"
        if not skill_md.exists():
            err(errors, skill_dir, "missing SKILL.md")
            continue
        text = skill_md.read_text()
        fm = parse_frontmatter(text)
        if fm is None:
            err(errors, skill_md, "missing YAML frontmatter")
            continue
        name = fm.get("name", "").strip()
        if not name:
            err(errors, skill_md, "frontmatter missing 'name'")
        elif not NAME_RE.match(name):
            err(errors, skill_md, f"name '{name}' violates spec (lowercase, hyphens, <=64 chars)")
        elif name != skill_dir.name:
            err(errors, skill_md, f"name '{name}' does not match parent dir '{skill_dir.name}'")
        desc = fm.get("description", "").strip()
        if not desc:
            err(errors, skill_md, "frontmatter missing 'description'")
        elif len(desc) > 1024:
            err(errors, skill_md, f"description is {len(desc)} chars (>1024)")
        elif not re.search(r"\b(use|when|whenever)\b", desc, re.I):
            err(errors, skill_md, "description should describe WHEN to use the skill")
        if not evals.exists():
            err(errors, skill_dir, "missing evals.json")
        else:
            try:
                data = json.loads(evals.read_text())
                for key in ("should_trigger", "should_not_trigger"):
                    if key not in data or not isinstance(data[key], list):
                        err(errors, evals, f"missing or non-list '{key}'")
                    elif len(data[key]) < 5:
                        err(errors, evals, f"'{key}' has {len(data[key])} items (recommend >=5)")
            except json.JSONDecodeError as e:
                err(errors, evals, f"invalid JSON: {e}")


def check_wiki_page(path: Path, errors: list[str], required: Iterable[str]) -> None:
    text = path.read_text()
    fm = parse_frontmatter(text)
    if fm is None:
        err(errors, path, "missing YAML frontmatter")
        return
    for field in required:
        if field not in fm:
            err(errors, path, f"frontmatter missing '{field}'")


def check_wiki(errors: list[str]) -> None:
    wiki = ROOT / "wiki"
    if not wiki.is_dir():
        return
    for md in wiki.rglob("*.md"):
        if md.name.startswith("_"):
            continue  # skip templates
        rel = md.relative_to(wiki)
        parts = rel.parts
        required = ["last_updated"]
        if parts[0] == "products":
            required = ["product", "status", "adoption", "last_updated", "sources"]
        elif parts[0] == "topics":
            required = ["topic", "last_updated", "sources"]
        check_wiki_page(md, errors, required)


def main() -> int:
    errors: list[str] = []
    check_skills(errors)
    check_wiki(errors)
    if errors:
        print(f"FAIL: {len(errors)} issue(s) found")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
