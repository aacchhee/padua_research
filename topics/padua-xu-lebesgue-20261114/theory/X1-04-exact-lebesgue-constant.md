# PD-T?padua-xu-lebesgue-20261114-claude-04 — Global product bound and the exact Xu Lebesgue constant: Λ^Xu_n = L_n²

ID kind: PD-T.
Aliases: X1-04; T3; sharp global upper bound; Λ^Xu_n = (Lebesgue constant of n Chebyshev zeros)²; first part of BCDMV Conjecture (17).
Split from: round X1-2 target T3 (sharp global upper bound) and BRIEF §1.2 outcome 3.
Split into: none. The maximizer set is X1-05; the expansion is X1-07.

## Statement

Let n ≥ 1 (both parities). For real θ₁, θ₂ put x = (cos θ₁, cos θ₂), u = (θ₁+θ₂)/2, v = (θ₁−θ₂)/2, and let ω_n = ω_n^{C_n} be the function of X1-02 for the class C_n of X1-01. Then

  λ_n(x) = ω_n(u) ω_n(v) − Δ_n(θ₁, θ₂),  Δ_n(θ₁, θ₂) := Σ_{ξ∈X_n} ( Σ_{(p,q)∈F(ξ)} |t_{pq}| − | Σ_{(p,q)∈F(ξ)} t_{pq} | ) ≥ 0,   (1)

with t_{pq} = d_n(u − u_p) d_n(v − u_q). Consequently, for every x ∈ Q,

  λ_n(x) ≤ ω_n(u) ω_n(v) ≤ L_n²,   (2)

and the Lebesgue constant of Xu interpolation is exactly

  Λ^Xu_n := max_{x∈Q} λ_n(x) = L_n² = ( (1/n) Σ_{k=1}^n cot((2k−1)π/(4n)) )²,   (3)

the square of the Lebesgue constant of univariate interpolation at the n zeros of T_n (X1-02 (d)). The maximum is attained at every vertex of V* (X1-03).

## Definitions

As in X1-01 to X1-03. Λ^Xu_n is the norm of the Xu interpolation projector C(Q) → V_n in the uniform norm.

## Assumptions

Exact real arithmetic; n ≥ 1; conventions of `literature-xu-mp.md` §1 (even n is the setting of BCDMV Conjecture (17); odd n is the separately labelled variant with V* = {(1,−1), (−1,1)}).

## Status by part

Overall status: **PROVED** (written proof below; audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Identity (1) and bound (2), every n ≥ 1, both parities | PROVED | Proof below |
| Exact constant (3), even n (setting of Conjecture (17)) | PROVED | (2) and X1-03 |
| Exact constant (3), odd n (variant) | PROVED | (2) and X1-03 |
| Grid checks of (2), n ≤ 24; G1 screen n ≤ 60 | MEASURED (verification only) | Checks |

## Depends on

X1-01 (lift formula; fibers partition C_n²), X1-02 (c), X1-03 (b).

## Checks

- `python3 code/xu/research/x1_argmax_check.py --nmax 12 --fmax 24` (run 2026-11-14): float64 Path B (`xu_kernel.XuFloat`) on the uniform angle grid with 6n+1 points per axis, n = 2..24: `worst lam-prod 1.05e-13; worst prod-L2 5.15e-14; worst |gridmax-L2| 3.55e-15`; the grid argmax is V* for every n.
- `python3 code/xu/research/x1_lift_check.py`: at 6 random points for n = 1..12 (40 digits), λ ≤ ω(u)ω(v) ≤ L_n² asserted.
- `evidence/xu-g1-summary.json` (orchestrator, n = 2..60): no non-vertex candidate exceeds the vertex value.
- Published values (`lit-notes/X1-sources.md` §7): BCDMV Table 7 gives Λ^Xu_n ≈ 10, 12, 13, 14 for n = 34, 48, 62, 76; L_n² = 10.2881, 11.7445, 12.8877, 13.8351 (computed 2026-11-14 with `x1_lift.Lcheb`, mpmath 30 digits; they round to the published integers and equal the reader's reproduction of λ(1,1) in that table).

## Sources

- LITERATURE: BdMV, JAT 141 (2006), Thm 1: Λ^Xu_n ≤ 8((2/π) log n + 5)² + 4 (n even); BCDMV, Computing 76 (2006), eq. (17): conjecture Λ^Xu_n ≲ ((2/π)log(n+1))² with the maximum at the four vertices (`literature-xu-mp.md` §4, orchestrator primary checks).
- No source read states (3). Novelty wording allowed: "no matching result found in the documented search" (`lit-notes/X1-sources.md` §6, plus the digest-level look at Li–Sun–Xu 2009 recorded in X1-01). The novelty gate must be re-run by the orchestrator/auditor for the exact statement (3) before any priority claim.

## Proof or evidence

By X1-01 (1), ℓ_ξ(x) = Σ_{(p,q)∈F(ξ)} t_{pq}. Hence λ_n(x) = Σ_ξ |Σ_{F(ξ)} t_{pq}|. The fibers partition C_n × C_n (X1-01 (a)), so

 Σ_ξ Σ_{F(ξ)} |t_{pq}| = Σ_{(p,q)∈C_n²} |d_n(u − u_p)| |d_n(v − u_q)| = ω_n(u) ω_n(v).

Subtracting gives (1), and Δ_n ≥ 0 by the triangle inequality. X1-02 (c) gives 0 ≤ ω_n ≤ L_n, hence (2). Every x ∈ Q is of the form (cos θ₁, cos θ₂), so Λ^Xu_n ≤ L_n². By X1-03 (b), λ_n(v) = L_n² for v ∈ V* ≠ ∅. This proves (3). ∎

## Scope

- (3) is an exact formula for every n ≥ 1; it implies Λ^Xu_n ~ (4/π²) log² n (X1-07), which is the first part of BCDMV Conjecture (17) in the strong (asymptotic-equivalence) sense, and it improves BdMV's bound to the sharp one.
- The representation (1) shows where λ_n can be large: only near pairs (u, v) of midpoints, and there the loss is the cancellation deficit Δ_n. Quantitative information on Δ_n away from V* is in X1-08 (MEASURED).

## Open items

- Audit.
- Novelty gate for (3) (orchestrator/auditor; see Sources).

## History

2026-11-14, Claude Fable 5.2 (xhigh), round X1-2 researcher. T3 was assigned as "attempt a sharp global upper bound, PROVED or OPEN"; the lift of X1-01 turns the global bound into a triangle inequality, with no asymptotic analysis.
