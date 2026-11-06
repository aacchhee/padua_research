# PD-T505 — full C1 scalar and gauge screen

ID kind: PD-T. Aliases: M1 bounded gauge-infimum fits; scalar Jacobi
controls; finite Hahn diagonal lower; input-model variants.
Split from: none. Split into: none.

## Statement

For each integer N=4,...,64, both exact rational benchmark families and
both marginal measures were evaluated at 180 and 260 decimal digits.
Scalar monic and symmetric-orthonormal output conditions were computed
exactly as induced first-order row supports, including each of four
explicit input models. A single terminal balanced-beta derivative row
gave a lower bound for every fixed and C1 input-dependent diagonal gauge;
the historical full monic table gave the identity-gauge upper bound.
No new full NN Jacobian sweep was run.

The resulting possible OLS per-node fitted ratios over all integer
N=32,...,64 satisfy the following numerically evaluated bounds, for
either gauge-infimum definition:

| Output | Krawtchouk | Hahn |
|---|---|---|
| NN fieldwise, mixed input | [9.181247,10.370243] | [10.355427,13.261408] |
| Step-line fieldwise, mixed input | [9.745754,9.755463] | [11.685726,11.765132] |

Printed endpoints are rounded away from the numerical interior. This
display convention does not make the floating evaluation an outward
arithmetic certificate.

Every lower endpoint exceeds the unchanged M1 threshold five for both
families. Thus the finite screen verdict is **intrinsic**, in the declared
fieldwise metric, by bounds on the actual infimum's fitted sequence.
An exact optimizer or exact value of the gauge infimum was not computed.
The Krawtchouk all-N invariant exponential proof is separate; Hahn
asymptotic exponential growth is not inferred from this finite screen.

## Definitions and assumptions

The input families, N-as-number-of-nodes convention and frozen source
identities are those of PD-T290/432/434. Scalar shift alpha and monic
offdiagonal beta are field-sup scaled separately; symmetric output uses
sqrt(beta). Exact symmetric zero alpha fields use absolute scale one.
The scalar control is consequently mixed absolute/relative in those
cases, not relative division by a sensitive zero field.

Input models: mixed node scale one; componentwise-node scale |x_l|;
natural-spacing scale 2/(N-1); and node scale one with separate fixed-mass
tangent constraints. All use componentwise-relative weights. Natural
log-weight coordinates give exactly the same first-order weight input.
The spacing and componentwise models resolve two possible meanings of
"relative node perturbations in natural spacing" without conflating them.

## Status by part

Overall status: MEASURED. The analytic derivative/support/gauge bounds are
PROVED separately. Precision convergence is not an outward enclosure and
does not certify the printed numerical endpoints as rigorous intervals.
No polynomial theorem for scalar controls is asserted.

## Depends on

PD-T432/434 and its historical 61-row monic table;
`c1-gauge-invariants.md`, `c1-scalar-derivative.md`, and
`c1-matrix-metric.md`. Finite Hahn normality is supplied by predecessor
PD-T436's explicit N4–64 computer-assisted domain (the predecessor theory
file `conditioning-hahn-normality-finite.md` is the authoritative ID home).
No all-N Hahn statement is needed for these measurements.

## Evidence and results

`c1-grid.csv` contains every N4–64 primary scalar value and terminal
diagonal lower bound. `c1-summary.json` records all four input-model fits,
endpoints, precision comparisons, source identities, versions and raw
artifact hashes. Both are compact essential evidence. The large raw
artifacts remain regenerable local working outputs, with no cold-storage
delivery claimed.

Scalar mixed-input results:

| Marginal | Monic N64 | Symmetric N64 | Symmetric fitted ratio32–64 |
|---|---|---|---|
| Krawtchouk p1=2/5 | 277.027956 | 277.027956 | 1.020563 |
| Krawtchouk p2=1/2 | 126 | 63 | 1.021848 |
| Hahn first | 64.459710 | 44.071364 | 1.019709 |
| Hahn second | 355.836410 | 355.836410 | 1.019878 |

These controls show small, roughly linear growth within the finite grid;
they do not establish an all-N polynomial upper bound. Merely changing
monic beta to sqrt(beta) does not remove the dominant scalar shift-alpha
condition in the asymmetric marginals.

Under spacing and componentwise-node variants, all NN gauge-fit lower
endpoints remain at least 8.4822 for Krawtchouk and 10.2814 for Hahn.
The fixed-mass lower fits agree with mixed at reported precision. This is
not an assertion that their exact conditions are identical. The original
mixed monic upper remains a valid upper for each restricted input box.

The authenticated monic integer-node matrix spectral condition is also
bounded at all 61 sizes, using the exact inequalities in
`c1-matrix-metric.md`. Its possible OLS ratio intervals for absolute
integer-node scale one are [6.826640,13.380272] Krawtchouk and
[8.456263,15.940784] Hahn. With normalized-node scale one they are
[7.389245,12.584685] and [8.517136,15.831249]. These bounds concern the
specific authenticated monic output, not arbitrary matrix similarities.
They do not calculate the exact box-to-spectral induced norm.

## Why these bounds bound the fitted infimum

Let L_N<=K_N<=U_N be the pointwise analytic bounds, with values evaluated
numerically. The OLS log slope over N32–64 is

    slope(K)=sum_N a_N log K_N,
    a_N=(N-48)/sum_(r=32)^64(r-48)².

For its minimum over compatible sequences choose log U_N when a_N<0
and log L_N when a_N>=0; reverse these choices for its maximum.
Exponentiating gives the reported bounds. Fitting L_N alone would not
give a valid lower bound for the fitted K_N slope, so it is not used.
The upper historical table is widened by half its last printed place
before this assembly. That only addresses display rounding, not
certification of the historical floating Jacobians.

## Checks

Both precisions completed all 61 sizes for all eight scalar/terminal
family/precision runs. Maximum relative 180/260 differences:

| Quantity | Krawtchouk | Hahn |
|---|---|---|
| scalar conditions, both marginals/all models | 1.614e-176 | 2.551e-170 |
| terminal gauge lower bounds/all models | 5.728e-102 | 8.476e-87 |

The producer pins frozen derivative and input code hashes before import.
Developer small-N forward-AD checks agree on every derivative coordinate.
The separate checker ran both families N4/8/16 at 200 digits, compared all
scalar/terminal rows, checked 135 exact fixed-mass support cases by primal
vertex enumeration, reviewed the written proofs, and independently
recomputed all 16 signed OLS intervals. See `independent-checks-01.md` for
the exact accepted scope; this file is not self-approval.

## Scope and open items

Finite fits and floating precision convergence remain MEASURED. The
original M1 threshold is unchanged; signed lower/upper regression bounds
are the dated instrumentation for applying it without exact gauge
optimization. Exact infima, outward derivative enclosures, and an all-N
polynomial scalar bound remain open here. This finite screen supplies no
Hahn asymptotic theorem; the separate C2 result `c2-hahn-lower.md` now
proves a weaker all-N exponential lower, inherited by the gauges in
`c1-hahn-gauge-lower.md`. The separate Krawtchouk sharp gauge-rate squeeze
is in `c1-gauge-sharp-rate.md`. Final source error diagnostics have been
regenerated against C4's bit-preserving tables and are recorded in
`c1-error-measurements.md`; they do not establish a weak-stability theorem.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, rules/input snapshot
`b4a04981d42c7cd872957facf5e3995e4096ca67`. No new full NN sweeps;
the independent terminal row is evaluated through a moment primal/adjoint
solve, and base field scales through scalar-arithmetic layer recursion.

## Final ID aliases (2026-11-06)

- `PD-T?nn-mop-cond-codex-C1-04` → `PD-T505`.
