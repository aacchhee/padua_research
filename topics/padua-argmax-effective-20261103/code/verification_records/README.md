# Executed record wrappers

These are unchanged copies of the actual checker-worker scripts. Their
hardcoded paths describe this campaign's `/workspace/padua_research` and
`/workspace/padua-work` layout; relocate those paths deliberately for a new
workspace and record the new script hash.

`canonical_sweep.py START END` runs the normal independent checker CLI,
records child CPU and wall time, and writes the17/24 timing subset.
`freeze_summary_corrected.py` reads the actual per-worker receipts,
checks source/binary/certificate identity and reference payload equality,
and writes the compact corrected acceptance summary. It requires the raw
working receipts; the committed summary itself is retained for use when
those regenerable working files are absent. Neither wrapper substitutes
for the arithmetic checker. Replaying certificates uses the commands in
the native checker README and finite theorem.

The summary-generator SHA in the compact receipt is the hash of these
unchanged script bytes. Its original execution path was outside Git.
