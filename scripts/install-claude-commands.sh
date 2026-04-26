#!/usr/bin/env bash
# Wire all skills as native Claude Code slash commands.
#
# Symlinks every skills/<name>/SKILL.md to .claude/commands/<name>.md so
# Claude Code picks each one up as a slash command without copying content.
#
# Usage:
#   scripts/install-claude-commands.sh        # install
#   scripts/install-claude-commands.sh clean  # remove the symlinks

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CMD_DIR="$ROOT/.claude/commands"
SKILLS_DIR="$ROOT/skills"

mkdir -p "$CMD_DIR"

if [[ "${1:-}" == "clean" ]]; then
  echo "removing symlinks in $CMD_DIR"
  find "$CMD_DIR" -maxdepth 1 -type l -delete
  echo "done."
  exit 0
fi

count=0
for skill_dir in "$SKILLS_DIR"/*/; do
  name="$(basename "$skill_dir")"
  src="$skill_dir/SKILL.md"
  if [[ ! -f "$src" ]]; then
    echo "skip: $name (no SKILL.md)"
    continue
  fi
  dest="$CMD_DIR/$name.md"
  ln -sf "$src" "$dest"
  echo "linked /$name -> $src"
  count=$((count + 1))
done

echo
echo "installed $count slash commands in $CMD_DIR"
echo "Claude Code will pick them up on next session."
