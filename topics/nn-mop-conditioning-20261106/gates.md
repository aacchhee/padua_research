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

Initial replay checkpoint: M1–M4 remained as written in handoff01; no verdict had yet been reached. Completed verdicts are appended below.

## Completed direction verdicts — 2026-11-06

| Gate | Verdict | Evidence and limits |
|---|---|---|
| M0 original | UNASSESSABLE at requested1e-10 | Historical committed values have7digits; raw historical data absent. Original criterion retained above. |
| M0a | PASS | Twelve values match historical rounding and fresh180/260dps; independent210dps rerun agrees. m0a-receipt.json and independent checks. |
| M1 | intrinsic, MEASURED within defined fieldwise gauges | Both fixed and differentiable-gauge NN fit bounds exceed5: Kraw[9.181247,10.370243], Hahn[10.355428,13.261407]. Step-line bounds also exceed5. Scalar fitted ratios≈1.02. Bounds use signed OLS coefficients; no exact optimizer or outward interval certificate. c1-summary.json, theory/c1-measurements.md. |
| M2 | PASS | Actual pinned exact generator fidelity checked for Kraw/Hahn atN6. An exploratory stronger requirement that every computed solver output have error<=1e-12 failed for unstable KRYL and is retained as a separate forward-error diagnostic. c4-m2-bits-receipt.json. |
| M3 | unactivated; target OPEN | No general C3 theorem/constant claimed. Full58-case-per-method grid completed but is not a theorem test or PASS. |
| M4 | PASS, selected actual configuration | Unchanged G5 driver rerun Octave9.4, selected CORE2.691214553706643e-10 vs prior authenticated paper6.851191e-10, log10ratio−.4058. Source archive/all27members verified. |

Source-dependent gates were initially BLOCKED because the archive was absent.
AC subsequently supplied the exact bytes; dated source/run records supersede
that state without deleting the earlier access attempt. Final comparison
uses hex transport after the initial JSON decimal route failed an identical-
input check; all58 shared cases now match bitwise. See external-code.md and
attempts/C4.md. No numerical criterion was silently weakened.
