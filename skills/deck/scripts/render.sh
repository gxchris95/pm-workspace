#!/usr/bin/env bash
# Render a Marp markdown deck to PPTX, PDF, or HTML.
#
# Usage:
#   skills/deck/scripts/render.sh <markdown-file> [pptx|pdf|html|all]
#
# Default format is pptx. The 'all' flag renders pptx + pdf + html.
# Output files land next to the source markdown.
#
# Requires: marp-cli  (npm install -g @marp-team/marp-cli)

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <markdown-file> [pptx|pdf|html|all]" >&2
  exit 2
fi

SRC="$1"
FMT="${2:-pptx}"

if [[ ! -f "$SRC" ]]; then
  echo "error: file not found: $SRC" >&2
  exit 1
fi

if ! command -v marp >/dev/null 2>&1; then
  echo "error: marp-cli not installed." >&2
  echo "install with: npm install -g @marp-team/marp-cli" >&2
  exit 1
fi

render() {
  local fmt="$1"
  echo "rendering $SRC -> $fmt"
  marp --"$fmt" --allow-local-files "$SRC"
}

case "$FMT" in
  pptx|pdf|html)
    render "$FMT"
    ;;
  all)
    render pptx
    render pdf
    render html
    ;;
  *)
    echo "error: unknown format '$FMT' (use pptx|pdf|html|all)" >&2
    exit 2
    ;;
esac

echo "done."
