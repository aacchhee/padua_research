#!/usr/bin/env bash
# Fetch pinned publisher-template dependencies and build into local-output.
set -euo pipefail
paper_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
repo_dir=$(cd -- "$paper_dir/../../.." && pwd)
output_dir=${PADUA_PAPER_OUTPUT_DIR:-"$repo_dir/local-output/padua-argmax-bridge-20261105/paper"}
mkdir -p "$output_dir/template"
output_dir=$(cd -- "$output_dir" && pwd)
python3 - "$paper_dir/template/dependencies.json" "$output_dir/template" <<'PY'
import hashlib, json, pathlib, subprocess, sys
lock = json.loads(pathlib.Path(sys.argv[1]).read_text())
destination = pathlib.Path(sys.argv[2])
for item in lock['files']:
    path = destination / item['name']
    def valid():
        return path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256']
    if not valid():
        temporary = path.with_suffix(path.suffix + '.download')
        try:
            subprocess.run(['curl', '--fail', '--location', '--silent', '--show-error',
                            item['url'], '--output', str(temporary)], check=True)
            if hashlib.sha256(temporary.read_bytes()).hexdigest() != item['sha256']:
                raise SystemExit('Dependency hash mismatch: ' + item['name'])
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)
    print('Verified ' + item['name'] + ' ' + item['sha256'])
PY
if [[ ${1:-} == --fetch-only ]]; then exit 0; fi
for program in pdflatex latexmk; do
    command -v "$program" >/dev/null || { echo "Missing dependency: $program" >&2; exit 1; }
done
export TEXINPUTS="$output_dir/template//:${TEXINPUTS:-}"
export BSTINPUTS="$output_dir/template//:${BSTINPUTS:-}"
# Stable timestamps where supported; engine/package versions still affect PDF bytes.
export SOURCE_DATE_EPOCH=${SOURCE_DATE_EPOCH:-1794009600}
export FORCE_SOURCE_DATE=1
cd -- "$paper_dir"
latexmk -norc -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
    -outdir="$output_dir" main.tex
echo "PDF: $output_dir/main.pdf"
