#!/usr/bin/env bash
# Build the separate explanatory companion with the same pinned journal style.
set -euo pipefail
companion_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
repo_dir=$(cd -- "$companion_dir/../../.." && pwd)
output_dir=${PADUA_COMPANION_OUTPUT_DIR:-"$repo_dir/local-output/padua-argmax-bridge-20261105/onset512-companion-20261108"}
mkdir -p "$output_dir"
output_dir=$(cd -- "$output_dir" && pwd)
PADUA_PAPER_OUTPUT_DIR="$output_dir" bash "$companion_dir/../paper/build.sh" --fetch-only
export TEXINPUTS="$output_dir/template//:${TEXINPUTS:-}"
export BSTINPUTS="$output_dir/template//:${BSTINPUTS:-}"
export SOURCE_DATE_EPOCH=${SOURCE_DATE_EPOCH:-1794009600}
export FORCE_SOURCE_DATE=1
cd -- "$companion_dir"
latexmk -norc -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
    -outdir="$output_dir" main.tex
echo "Companion PDF: $output_dir/main.pdf"
