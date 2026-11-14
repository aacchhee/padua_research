# PD-N?padua-xu-lebesgue-20261114-claude-35 — the unshifted lattice does not maximise the shifted-lattice sum Ξ_n (pointwise "shift rigidity" fails)

ID kind: PD-N.
Aliases: X2-N35; shift rigidity; J(ψ) is not maximal at ψ = 0.
Split from: none.
Split into: none.

## Statement

MEASURED (float64, scope under Checks). For M = n + 2 ∈ {62, 102, 202} there are shifts (a₁, a₂) with Ξ_n(a₁, a₂) > Ξ_n(0, 0) = λ_n(1,1) (Ξ_n as in X2-34): at (a₁, a₂) = (0.9/M, −0.9/M), Ξ_n(a)/Ξ_n(0) = 1.0796 for M = 202 (Ξ_n(a)/M² = 0.5553 against Ξ_n(0)/M² = 0.5144).

Heuristic limit (derivation in `attempts/X2-round3.md` §4; OPEN as a theorem, MEASURED agreement): Ξ_n(φ₁/M, φ₂/M)/M² → |cos((φ₁+φ₂)/2)|·J((φ₂−φ₁)/2), with
J(ψ) := (4/π)∫_𝒮 |sin 2τ sin τ|·κ(τ + ψ) dτ, 𝒮 := ∪_{j∈ℤ}(jπ, jπ + π/2), κ(x) := |sin x − x cos x|/|x|³,
a π-periodic function with J(0) = c* and (quadrature) max J ≈ 0.56058 at ψ ≈ −0.92, min J ≈ 0.47741 at ψ ≈ 0.64.

Consequence: the mechanism "Λ_n ≤ sup_a Ξ_n(a) and sup_a Ξ_n(a) = Ξ_n(0)" cannot prove Λ_n = λ_n(1,1), nor lim Λ_n/n² = c*. The averaged bound X2-34 (b) is not affected: it involves symmetric box means of Ξ_n, for which the linear term cancels.

## Definitions

As in X2-34.

## Assumptions

None beyond the definitions; finite scope.

## Status by part

Overall status: MEASURED.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Ξ_n(a) > Ξ_n(0) at the listed shifts and M | MEASURED (float64; closed form of G̃ checked against the double sum to 3.6e−14) | a ball-arithmetic certificate at one n would make it PROVED at that n; not done |
| limit formula with J | OPEN (heuristic); MEASURED agreement within 0.006 at M = 202 on 10 shifts and a 13-point scan | no proof |
| max J > c* | MEASURED (quadrature, error estimated < 1e−5) | — |

Candidate / claim disposition: REJECTED (the mechanism below).
Rejection reason: failed (measured within the stated scope).

## Negative-result scope (PD-N only)

Attempted mechanism: bound λ_n(P) by the supremum over shifts of Ξ_n (Jensen applied to the translation formula X2-34 (a) before averaging) and show that the supremum is attained at the zero shift.
Parameter range: M ∈ {62, 102, 202}, shifts of size ≤ π/M; measured failure only, not a universal refutation.

## Depends on

X2-34 (definition of Ξ_n).

## Checks

- `python3 code/mp/research/x2r3_checks.py shift` (float64; 2026-11-14; 10 s). M = 202, (Mφ₁, Mφ₂) ↦ Ξ/M² [heuristic]: (0,0) 0.5144 [0.5170]; (0.9,−0.9) 0.5553 [0.5606]; (−0.9,0.9) 0.4837 [0.4843]; (1.8,0) 0.3404 [0.3485]; (0,1.8) 0.2939 [0.3010]; (0.6,0.6) 0.4200 [0.4267]; (−0.6,0.6) 0.4774 [0.4777]; (π,π) 0.5071 [0.5170]; (π,0) 0.0047 [0]; (0,π) 0.0079 [0]. Scan Ξ(s/M, −s/M)/M² against J(−s), s = −1.5…1.5: agreement within 0.006. `Jmax_on_grid` 0.560585, `Jmin_on_grid` 0.477408, `J(0)` 0.516954.
- Independent rerun: pending.

## Sources

None.

## Proof or evidence

Measured evidence only.

## Scope

A measured failure of one mechanism. It says nothing against the target Λ_n = λ_n(±1,1).

## Open items

Certificate at one n (cheap; ball arithmetic of a finite sum). Proof of the limit formula (part of item W in the X2-28 addendum).

## History

- 2026-11-14, Claude Fable 5.2 (xhigh), researcher subagent of round X2-3; uncommitted at writing. First version.
