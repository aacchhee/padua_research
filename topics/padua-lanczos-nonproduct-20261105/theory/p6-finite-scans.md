# PD-T?lanczos-nonproduct-codex-P6-01 — exact finite-grid capacity endpoints

ID kind: PD-T (provisional). Aliases: P6 weighted endpoint pilots.
Split from: finite scans; all-degree family targets remain separate.
Split into: none.

## Statement

On the admitted fixed T24 uniform, H24_222 triangle and D36x9 rational ring
measures, exact all-source aggregate capacity endpoint rows for each degree
2,3,4 and each rule BJ, mirror, alternating and X-tie-broken exact-pivot
were computed by two rational arithmetic paths and match exactly (36 rows).
The four endpoints are the rational squared L,H,Urow,U bounds of P4-02.
They bound the spectral-normal-output capacity; no endpoint equality with
that capacity is asserted. This is finite **MEASURED** evidence and does
not establish an asymptotic growth law or a complete N2 window.

## Definitions

All native inputs have rational positive weights summing exactly to one.
Sources range over every nonconstant column through the completed degree,
with the relative raw-product aggregate Hilbert budget of P4-02. Spectral
normal-column output is used, not a scalar-operation cube or IEEE model.
All parent choices, including pivot ties, are frozen at the exact base run.

## Assumptions

The exact admitted supports and weights in P1-01/P2-01, their injectivity
and oversampling ranges, and P4-02's finite weighted quotient model.
D36x9 is a D4-symmetric finite ring measure, not a continuous radial disk
cubature or a measure invariant under every rotation.

## Status by part

Overall status: MEASURED.

| Part | Status | Evidence |
|---|---|---|
| All36 finite pilot rows and two-path exact equality | MEASURED | Three compact receipts linked below |

## Depends on

`p1-triangle-admission.md`, `p2-01-family-admission.md` and
`p4-weighted-normal-quotient.md`. Existing uniform T24 results through20
are inherited PD-T338 evidence, separate from the fresh degree4 pilot.

## Checks

Producer uses common-denominator integer vectors with GMP; checker uses
per-entry scalar GMP rationals, adapted from the two existing predecessor
implementations. Both build their own exact bases/source propagation and
check complete Gram orthogonality, pivots, source scales, projector diagonal
range, trace, all-source dimensions, endpoints and choices/ties. The generic
row guard compares exact rational endpoints and metadata. T24 additionally
matches the pinned historical legacy sweep on every pilot row.

These are two actual arithmetic executions by the same technical worker,
not distinct-agent scientific approval. A separate auditor/rerunner remains
necessary for consequential computational conclusions.

## Sources

Repository PD-T136/137/324/338 and P4-02; no external literature theorem or
historical novelty claim. This is a retained implementation variant of
IDEA-246/248, with T24 duplicate baseline reuse explicitly recorded in the
gate. The weight extension is justified by P4-02 before implementation.

## Evidence

- `../evidence/p6-pilot-T24.json`: twelve rows, maximum producer/checker
  case wall time .0671/.1158 seconds.
- `../evidence/p6-pilot-H24_222.json`: twelve rows, maximum
  producer/checker .0648/.1151 seconds.
- `../evidence/p6-pilot-D36x9.json`: twelve rows, maximum
  producer/checker .0653/.2151 seconds.

The decimals above are rounded-up displays; actual timings, exact commands,
code/input hashes, output size/hash and environments are in those receipts.
Every case was capped prospectively at60 seconds, with two native processes
at once; no case timed out. Raw outputs/specifications are retained under
`/tmp/padua-lanczos-nonproduct-20261105/p6/pilot-<family>/` and remain
regenerable temporary artifacts; cold-storage archival is pending.

Reproduce with the following command for each family T24,H24_222,D36x9,
using a new work directory for a fresh execution:

```sh
python -B topics/padua-lanczos-nonproduct-20261105/code/p6_scan.py --family H24_222 --max-degree 4 --seconds 60 --work-dir /tmp/padua-lanczos-nonproduct-20261105/p6/pilot-H24_222 --receipt topics/padua-lanczos-nonproduct-20261105/evidence/p6-pilot-H24_222.json
```

## Scope

Finite complete-source endpoints on three named fixed measures only. No
atomless-measure inference, derivative activation by actual arithmetic,
all-degree rate, capacity ordering or new family admission follows from
these pilots. Matching all finite moments would not identify the ambient
source/projector model, as P4-02 states explicitly.

## Open items

Admitted H24_222 and D36x9 complete degree2–16 scans under the prospective
600-second case cap; separate N2 interval reanalysis; distinct-agent checks.
Further perturbed-SH/Padua exact grids remain unscanned pending viable specs.

## History

2026-11-05, Codex technical worker, requested gpt-6.1-sol medium; serving
metadata not independently exposed. P6 round1 gate/schema preceded all P6
runs. Coordinator pushed round1 `3d49d32` and authorized round2 before the
pilots. P4-02 formula proof and P1/P2 admissions were read before execution.

### Round3 additive coverage — H24_222 through16

The H24_222 statement now additionally covers every degree2–16 and all four
rules (60 exact rows), all-source, with two-path exact agreement. Status
remains MEASURED. Actual cap600seconds/case; max producer3.231s/checker10.195s.
`../evidence/p6-full16-H24_222.json` pins every command, input/source and
output identity. Degree8 cost benchmarks for H24_222/D36x9 also matched all
28 rows per family, with evidence `p6-benchmark8-*.json`. These finite
completions do not broaden the underlying model or imply a rate. Disk16
is running, explicitly not yet included in complete coverage.
