<a id="pd-tlanczos-nonproduct-codex-p6-01--exact-finite-grid-capacity-endpoints"></a>

# PD-T487 — exact finite-grid capacity endpoints

Provisional alias: `PD-T?lanczos-nonproduct-codex-P6-01`.

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
that capacity is asserted. The completed extensions below also cover every
degree2–16 and all four rules for H24_222 and D36x9 (60 matched rows per
family). This is finite **MEASURED** evidence, without an asymptotic law.

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
| H24_222 and D36x9, all60 rows per family through16 | MEASURED | Full scan/recovered acceptance receipts below |
| Distinct D65x9 degree2–8 four-rule pilot,28 matched rows | MEASURED | p6-pilot8-D65x9.json |

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

Cross-family substantive audit and archival delivery of large raw outputs.
H24_222 and D36x9 degree2–16 coverage is complete under the recorded original
and separately preregistered successor caps; N2 is recorded separately.
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
completions do not broaden the underlying model or imply a rate. The later
D36 completion is recorded in the dated addendum below.

### Round6 completion — D36x9 and bounded D65x9 scope

D36x9 now has every degree2–16, all four rules and every original source
matched exactly:60 producer/checker row pairs, including all nonelapsed
fields, choices/ties and full Gram counts. Final accepted evidence is
`../evidence/p6-disk16-recovered-acceptance.json`. The producer is the
original full-node common-denominator GMP code. BJ/mirror use completed
original full-node scalar GMP checks (1883.126099577/1980.343642943seconds);
ALT/PIVOT use the reviewed scalar reflection implementation, SHA256
`09d524f915076105b04fb196ee98c6c6cd4cecbc6b6e49bcfacb541ffc999088`.
ALT's saved harness wall time is1611.668965790seconds. PIVOT's native
timer reports approximately1172.1seconds before final JSON emission; its
harness wall time was not saved and is not reconstructed. Both native
outputs retain completed phase logs, all152 source positions and all15
prefix rows. The separately admitted reflection method retains324 original
nodes,90 verified representatives,99144 exact basis parity checks and
307800 expanded original-node/source snapshots per rule. Full-node normal
diagonals, all-source budgets and all endpoint formulas are unchanged.

The original reflection parent closed after saving ALT, leaving its own
seven-case receipt INCOMPLETE. The artifact-only recovery adapter validates
retained PIVOT output/guards and all60 full-field pairs without any native
rerun. It preserves that interrupted receipt's bytes and hash, the full
per-case source catalog and earlier resource receipts. The exact parent
exception is unavailable; no cause is asserted. Original600second failures
and cancelled scalar cases remain separately INCOMPLETE, with actual masks
and timings in their original receipts. Canonical resumption chronology is
in `../attempts/P6.md`.

D65x9 remains a distinct measure: its degree2–8 four-rule pilot has28 matched
rows. Its ALT-only degree12 producer completed32.901309618seconds, but the
scalar check timed out120.002498008seconds with zero emitted endpoint rows.
That paired cost probe remains INCOMPLETE; no D65 full16 or N2 is claimed.
The bounded generic/block FLINT attempts and scalar optimization failures
remain retained cost outcomes, with small exact successes and no promoted
high-degree result; see `../flint-check-notes.md` and `../p6-speed-notes.md`.

H24_222/D36x9 compact outward-log tables preserve all60 completed rows and
all eight source/output identities per family. Each is below16KiB and uses
fixed10^15 outward rounding after two exact rational log routines. The
standalone integer N2 replay needs only these tables. Rechecking their log
generation still requires the pinned raw exact rows or regenerating them;
large artifacts remain temporary, with archival delivery pending. This is
MEASURED finite evidence, not a complete computer proof of any growth law.
