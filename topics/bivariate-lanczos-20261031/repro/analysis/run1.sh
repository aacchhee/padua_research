#!/bin/bash
# usage: run1.sh <script-basename-without-.py> [args...]
SP=/tmp/claude-0/-home-claude/78895e52-4b23-52e6-98cc-27f64a107887/scratchpad
IN=/home/claude/padua_research/tracks/bivariate-lanczos/code/inputs
name=$1; shift
tag=$name; [ $# -gt 0 ] && tag="${name}_$(echo "$*" | tr ' ' '_')"
wd=$SP/repro_run/$tag; rm -rf $wd; mkdir -p $wd; cd $wd
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
start=$(date -u +%Y-%m-%dT%H:%M:%SZ); t0=$(date +%s.%N)
timeout 1800 python3 -I -B $IN/$name.py "$@" > $SP/repro_full/$tag.log 2>&1
rc=$?
t1=$(date +%s.%N)
printf 'script=%s\nargs=%s\nstart_utc=%s\nexit=%s\nwall_s=%.1f\nlist_cwd_after=%s\n' "$name.py" "$*" "$start" "$rc" "$(echo "$t1 - $t0" | bc)" "$(ls $wd | tr '\n' ' ')" > $SP/repro_full/$tag.meta
