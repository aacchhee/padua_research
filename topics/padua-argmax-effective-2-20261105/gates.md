# Phase-2 gates — 2026-11-05

The original criteria remain unchanged in handoff01. This file records actual
scope and verdicts; it does not replace unavailable proofs by sample fits.
Rules/input integration: ed21cc0bf205549936fccde90244a291bc6de324.
Mathematics: AC-requested Astra ultra. Technical probes: Sol medium.
Supplementary independent mathematics: distinct Astra high. Claude audit-01
accepted the mathematics at its stated scopes; this record response remains
subject to the response check.

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
PD-T227 Scope (8) is the aggregate-radius predecessor; PD-T228 already
gives the eventual 2^-17/n² radius, in particular for log n>=10^7. T07's
separation is an explicit constant for every n>=2. The available all-degree
strict-descent radius is max(1/(2[n(n+1)]³),10^-11/n²), combining PD-T251
and T07 without extending either theorem's loss estimate.

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

The phase/projection/box-pilot observations have the proposed scoped MEASURED
home T08 in `theory/phase2-measurements.md`; this is transcription of existing
evidence, not a new run or status. PD-T232/247 are the phase/defect-screen
predecessors and PD-T233 is the separate measured energy predecessor. The
hypothetical C=1.4–1.7 in A0 comes from handoff-01 and the finite primitive
screens PD-T247/252; those samples do not establish a global C. T02 stays
CONDITIONAL gate evidence linked to deferred R1 and is not proposed for
registration.

## Separately dated criterion clarifications

2026-11-05, response to audit-01 F3: interpret handoff-01's R1 reopening
criterion “if that value is ≤10^4” as referring to the inherited
PD-T216+PD-T225 coarse route. Its log n values 17456–21197 at ρ=1/16
(and about 2.8–3.4·10^5 at 1/64) do not meet that threshold. The
sharpened geometric variant gives 7076–8592 at 1/16, so it meets the
literal numeric cutoff if the criterion is instead extended to that
variant. Our recorded interpretation keeps R1 deferred: the refinement
is separate, C is unproved, and no practical bridge or corner comparison
follows. T04 now covers the noncorner radius 1/16, so that radius itself
is no longer the missing defect ingredient. **AC may choose the broader
interpretation; this decision item is preserved for AC.** The original
criterion is unchanged, and the record response proceeds without
reopening R1 or requiring a new permission request.

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

2026-11-05, response to audit-01 E8: optional degree-40 cross-check
(handoff-01 task 5) **not attempted**. Within its analytic small-radius
branch, the current box pilot uses the valid constant 1/8192 instead of
the maximum of that constant and the projected-profile bound. This can
weaken acceptance near n≈48–64; it is recorded as an implementation
limitation, with no code change or new run.

## Runs needed

Complete A1's actual cover/independent checker, then define the full-diamond A3
profile/remainder and evaluate A4 from those measured/proved inputs. A5 requires
its own continuous coverage and exact re-examination of any genuine candidate.
No n>32 global certificate or all-degree PD-T099 proof is claimed.
