# PD-T?argmax-alln-codex-01 — Pre-registered edge, interior, corner and effectivity measurements

ID kind: PD-T.
Aliases: part-3 T1–T4; profile kill tests; effectivity projection.
Split from: none; finite numerical evidence supporting the OPEN PD-T099.
Split into: none. The exact n=2 claim is separate record codex-02.

## Statement

For the Padua conventions of PD-T101 and the finite searches specified in
[the test attempt](../attempts/T1-T5.md), float64 evaluation observes:

1. T2: on the stated 9×9 lattice and complementary-cell convention, 32 of
81 positions have cell-max gap changes exceeding .05 from n=64 to 128.
The largest change is .382304500506 at the macroscopic centre.
2. T3: on the 13×13 angular corner-offset grid at n=16,64,256, several fixed
offsets have increasingly negative λn−Λc; no off-origin sample has gap
magnitude less than 1e−6. At (.25,0), the gaps are −.761788147,
−1.445328813, −2.357884098.
3. T4: the measured global phase coefficient is .673599799639 at n=400;
the local-window search finds no positive S−Λc at any tested degree.
The central gap at 400 is .550442436683 and its excess over numerically
integrated g is .001927594284. A literal inferred-constant implementation
of PD-T189→190 projects n₀≈1.33×10¹⁴; central-only fitted error models
already fit a g/2 budget at n=32. These are different, non-rigorous scopes.
4. T1: all-four-edge cell profiles are evaluated at the degrees through
400 listed in the attempt, with raw per-cell evidence retained. The
positive PD-T186 defect integral is numerically evaluated at 19
macroscopic ordinates; its centre is .548514842400. The requested general-β
PD-T188 series has not been derived. Excluding both edge-end cells, no
sampled degree n≥100 has gap below g−.01. The smallest is .550440482023
at n=399 on x=−1, β=π/2; at 400 the vertical minimum is .550442549884.

These statements describe finite searches and calculations. No convergence,
divergence, all-degree inequality, certified maximum or rigorous global
threshold is claimed.

## Definitions

λn is the sum of absolute Padua cardinal polynomials; Λc is its non-node
corner value. S_n(s), the primitive phase and the local window |s|≤π/6 are
exactly those of PD-T189/190. R_cen uses PD-T192's precise central-edge
envelope. T1's edge cells are Lobatto intervals. T2's complementary-cell
rounding and T3's angular corner scaling are specified in the attempt;
the original plan did not fully specify those conventions.

## Assumptions

NumPy/SciPy float64 arithmetic, finite grids and local optimization, without
outward rounding. Evaluation formulas are the corrected kernel of PD-T101
and PD-T185 and the primitive definition of PD-T189. Numerical quadrature
error reports are estimates, not interval bounds.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| T1 finite profiles and integral evaluations | MEASURED | tests_T1*.json; general-β series missing; no exhaustive maximum enclosure |
| T2 finite threshold breaches | MEASURED | tests_T2.json; rounding convention and phases stored |
| T3 finite profile drift and no sampled near-tie | MEASURED | tests_T3.json; no nonconvergence proof |
| T4 fitted constants and model-dependent thresholds | MEASURED | tests_T4.json; no all-n constant or assembly bound |

Planning dispositions are scoped separately: the registered T2 threshold
triggers; T3's n-independent raw angular profile is killed for planning;
T4's literal existing-proof projection exceeds the cutoff 60, while the
unspecified improved global strategy has no uniquely defined projection.
The original T1 all-cell threshold includes zero-gap corner cells and is
ill-posed; its dated noncorner-cell interpretation is assessed separately
in tests_summary.json. None of these dispositions rejects PD-T099, P3's
strict corner inequality or P4's strict interior inequality.

## Depends on

PD-T101 (kernel and conventions), PD-T185/186 (edge identity and positive
complementary defect), PD-T188 (central g), PD-T189/190 (phase estimates),
PD-T192 (central envelope definition). The effectivity projection uses the
proved but coarse Λc≥(4/π²)log²n−54 only as a formula in an explicitly
non-rigorous extrapolation with inferred C.

## Checks

Source/rules pin `328be35e55143013047ec03a70e9906e82b95353`.
Commands, finite grids, runtimes, numerical discrepancies and input newline
qualification are in [T1-T5.md](../attempts/T1-T5.md). The original matrix
and fast rhombus evaluators agree within 7.8e−15 on validation points at
n=2,3,4,8,16. T1 also compares the independently expressed
divided-difference edge evaluator with the rhombus formula through n=400.
These are developer comparisons. No different-agent replay of T1–T4 is
implied by those comparisons. The separate `gpt-6-astra high` checker
subsequently reran full T2, T3 and T4: every non-time JSON field matches.
It independently reproduced every T1 n=12 profile row on all four edges,
and executed additional bounded formula checks through n=400 and five
general-β integral evaluations. The full T1 degree range was **not**
independently rerun. Coverage, commands, hashes and the no-unresolved-finding
assessment are recorded in
[independent-checks-part3.md](../independent-checks-part3.md). These are
supplementary independent checks; required Claude audit remains pending.

## Sources

Plan v2 §6, retained unchanged; merged part-2 theory 70–77, read at the
source pin. No literature or novelty claim.

## Proof or evidence

Evidence is the JSON/text output family `../outputs/part3/tests_*`, produced
by `../code/part3/tests_*.py`. The rhombus identity expresses the full diamond
kernel as a product of two sine quotients plus the adjacent product, with
the corrected x mode subtracted. Singular-looking arguments use continuous
sinc evaluation. The edge evaluator uses PD-T185's polynomial divided
difference with rhombus fallback near collisions.

The T4 global threshold calculation solves the explicit scalar inequality
in the attempt. Its number is not made rigorous by using one proved corner
bound: the phase constant itself is inferred and the other region and
defect errors remain unbounded.

## Scope

Only the stated finite float64 observations, search conventions and
conditional projection calculations. T1 samples selected degrees through
400, not every integer ≤400. Local optimizers can miss other maxima.
The grid has no resolution guarantee near cusps or shifted endpoint peaks.
T2's growing gaps can coexist with the desired strict interior bound.

## Open items

Required Claude audit; full-range independent T1 rerun; β-general PD-T188
series; rigorous uniform rates,
constants and thresholds; P1–P6 beyond the finite n=2 split. The exact T5
certificate is [codex-02](argmax-alln-codex-02-degree-two-global-argmax.md),
whose replay/audit status is independent of this measured record.

## History

2026-11-01, Codex development subagent, `gpt-6.1-sol xhigh`: executed the
pre-registered tests within assigned disjoint ownership. Separate dated
interpretations preserve every original criterion and expose ill-posed
components; no criterion was rewritten in plan.md. No Git operations or
shared registry edits were performed by this subagent.

2026-11-01 administrative follow-up: linked the completed Astra replay
coverage for full T2–T4 and T1 n=12, retaining the unrerun full T1 scope and
pending Claude audit explicitly. No numerical evidence or source code was
changed, and no mathematical status was upgraded.
