# Gates — original criteria preserved in handoff01

## M0 — 2026-11-06 amendment before higher-precision replay

Original: reproduce historical PD-T434 values to 1e-10 relative at
N4,16,32, both families/maps. The committed historical table contains
only seven significant figures; its raw 180/260-dps outputs are not in
this repository or runtime. Thus the original precision comparison is
UNASSESSABLE, not a numerical mismatch and not PASS.

M0a replacement: freshly evaluate frozen committed AD at 180 and 260 dps;
require their twelve NN/step-line values to agree to 1e-10 relative and
require every value to round to the historical seven-digit table cell.
This tests repeatability and the published table, not historical raw-byte
identity or rigorous accuracy. A mismatch kills dependent work.

M1–M4 remain as written in handoff01. No verdict yet.
