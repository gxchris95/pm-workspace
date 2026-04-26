#!/usr/bin/env bash
# Render Reviewed/Final workspace artifacts to dist/.
#
# Currently renders:
#   - workspace/decks/*.md  (status: Reviewed | Final)  -> dist/decks/<name>.pptx + .pdf
#
# Reads the YAML frontmatter `status:` field; only Reviewed or Final are rendered.
# dist/ is gitignored.
#
# Usage:
#   scripts/publish.sh           # render decks
#   scripts/publish.sh decks     # explicit target
#   scripts/publish.sh clean     # remove dist/

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$ROOT/dist"
DECKS="$ROOT/workspace/decks"

if [[ "${1:-}" == "clean" ]]; then
  rm -rf "$DIST"
  echo "removed $DIST"
  exit 0
fi

target="${1:-decks}"

mkdir -p "$DIST/decks"

if ! command -v marp >/dev/null 2>&1; then
  echo "error: marp-cli not installed." >&2
  echo "install with: npm install -g @marp-team/marp-cli" >&2
  exit 1
fi

publish_decks() {
  local count=0
  for src in "$DECKS"/*.md; do
    [[ -f "$src" ]] || continue
    local base
    base="$(basename "$src" .md)"
    [[ "$base" == _* ]] && continue
    # extract status from YAML frontmatter
    local status
    status="$(awk '/^---$/{f++; next} f==1 && /^status:/{print $2; exit}' "$src" || true)"
    if [[ "$status" != "Reviewed" && "$status" != "Final" ]]; then
      echo "skip: $base (status=$status)"
      continue
    fi
    echo "rendering: $base"
    marp --pptx --allow-local-files -o "$DIST/decks/$base.pptx" "$src"
    marp --pdf  --allow-local-files -o "$DIST/decks/$base.pdf"  "$src"
    count=$((count + 1))
  done
  echo
  echo "published $count deck(s) to $DIST/decks"
}

case "$target" in
  decks) publish_decks ;;
  *) echo "unknown target: $target (use 'decks' or 'clean')" >&2; exit 2 ;;
esac
