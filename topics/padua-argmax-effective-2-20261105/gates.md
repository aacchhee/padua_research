# Phase-2 gates — 2026-11-05

The original criteria remain unchanged in handoff01. This file records actual
scope and verdicts; it does not replace unavailable proofs by sample fits.
Rules/input integration: ed21cc0bf205549936fccde90244a291bc6de324.
Mathematics: AC-requested Astra ultra. Technical probes: Sol medium.
Supplementary independent mathematics: distinct Astra high; Claude audit PENDING.

| Gate | Actual result / status | Exact remaining obligation |
|---|---|---|
| A0 | Coarse-route diagnosis CONFIRMED conditionally on hypothetical C. For C1.4–1.7, log n is about279292–339140 at rho1/64 and17456–21197 at1/16. | No global numerical C in that range is proved. The sharper geometric variant gives7076–8592 at1/16 and is preserved separately; this is still an impractical log n and no bridge. |
| A1 | Exact common-primitive structure PASS, including endpoints/collisions. Point timing and full projected samples completed. Bounded natural-interval pilot INCOMPLETE at every tested degree:17/32/64/128 hit2000 visited boxes;256 hit60 CPU seconds after802 boxes. No complete-cover growth law or exact timing projection. | A completed three-region cover, practical exact runtime and independent checker/corruption controls. No gate pass from O(n²) point evaluation. |
| A2 | ANALYTIC INGREDIENT PROVED: n>=48 and rho<=1/10 imply full noncorner defect>=1/8192. All-center samples at48/96/192 show positive projected comparison margins. | Uniform upper control of S−Lambda_c matching that budget and far annulus; samples over rho0.2/0.3 do not extend the theorem. |
| A3 | Full-diamond gate OPEN. Exact boundary profile proved with uniform error<=7/(12[n(n+1)]²). Leading-factor-only trial refuted at diamond midpoints. | Define and prove a compatible interior/boundary profile before a full-diamond fit. No such fit or full-diamond remainder law executed; no inferred constant or N1. |
| A4 | NOT EVALUABLE from current evidence. | No completed H1 cost curve or explicit full-diamond H2 N1 exists. A boundary-only remainder is not a bridge threshold; point timings are not certificate throughput. |
| A5 | Finite sample screen only; no confirmed counterexample. | No gap-free continuum cover through256. Failed sufficient predicates and roundoff-sized corner excesses are not lambda counterexamples. |

H3 separately closes the physical n^-2 scale: T05/T06/T07 yield strict descent
for every n>=2 at inward H<=10^-11/n². The constant does not establish a useful
H1 box count. PD-N085 remains valid because individual sign changes are allowed.

## Completed commands and evidence

- Frozen native n17/n24 producer/checker replays: independent-replay.md and
  evidence/replay-summary.json; all four replays accepted, no new degree.
- Exact Fraction reflection checks and floating A0 arithmetic: gates-structural.md.
- Compiled direct point sampling: phase-probe.md and evidence/phase-probe.json.
- Bounded full three-predicate interval attempt: box-pilot.md and evidence/box-pilot.json; unresolved frontiers880/902/774/802/308 at n17/32/64/128/256. All are incomplete floating covers.
- All-admissible-center projection sampling: projection-probe.md and
  evidence/projection-probe.json. This counts1,198,029 center-phase samples,
  not1,198,029 boxes or distinct certified points.
- Separate analytic reconstruction and70-digit diagnostics:
  independent-math-checks.md and evidence/independent-math.json.

## Separately dated criterion clarifications

2026-11-05: The inherited phrase "same safety margins as the exact version"
does not define an executable floating predicate before the enclosures exist.
The bounded pilot protocol in attempts/H1.md therefore pre-registers a diagnostic
budget and explicit caps. A cap is an inconclusive implementation outcome, not
the original asymptotic box-growth kill criterion.

2026-11-05: The original H2 proposal does not specify an explicit candidate
profile. The narrowly specified a(alpha,beta)*b_n trial is rejected by the exact
boundary theorem; this does not reject every H2 profile or imply a second
full-diamond fit has run. The retained boundary correction is useful but remains
restricted to the diamond boundary.

## Runs needed

Complete A1's actual cover/independent checker, then define the full-diamond A3
profile/remainder and evaluate A4 from those measured/proved inputs. A5 requires
its own continuous coverage and exact re-examination of any genuine candidate.
No n>32 global certificate or all-degree PD-T099 proof is claimed.
