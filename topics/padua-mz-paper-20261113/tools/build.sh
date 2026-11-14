#!/bin/bash
# usage: build.sh <srcdir> <outdir>  — pdflatex; bibtex; pdflatex; pdflatex
set -u
S=$(readlink -f "$1"); O="$2"; mkdir -p "$O"; cp "$S"/*.tex "$S"/*.bib "$O"/ 2>/dev/null; cp "$S"/*.cls "$S"/*.bst "$O"/ 2>/dev/null
cd "$O" || exit 1
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex >/dev/null || { echo "PASS1 FAIL"; grep -A3 '^!' manuscript.log|head -20; exit 1; }
bibtex manuscript >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex >/dev/null || { echo "PASS3 FAIL"; grep -A3 '^!' manuscript.log|head; exit 1; }
echo "pages: $(pdfinfo manuscript.pdf | awk '/^Pages/{print $2}')  $(pdfinfo manuscript.pdf | awk '/^Page size/{print $3"x"$5}')"
echo "log issues:"; grep -nE 'Warning|Overfull|Underfull|undefined|^!' manuscript.log | grep -v infwarerr | head -20
echo "blg warnings:"; grep -E '^Warning|warning\$' manuscript.blg | head
sha256sum "$S"/manuscript.tex "$S"/refs.bib manuscript.pdf
