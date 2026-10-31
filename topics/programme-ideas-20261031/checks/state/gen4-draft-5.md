# Padua points are asymptotically Fekete, Dubiner-equidistributed and weighted-Fekete-stationary: closing the deduction gap
Model: claude-fable-5-1, effort xhigh · Angle D · 2026-11-01 · Status: not returned (note-sized; folded into gen4-draft-2 sub-problem 4)

## Central question
Are Padua points asymptotically Fekete for the square (n-th root of |det V| → transfinite diameter, counting measures → product arcsine), and are they stationary points of a *weighted* Fekete functional whose weight is explicit?

## Template theory
Fekete/Leja asymptotics (Berman–Boucksom–Witt Nyström 2011; Bloom–Bos–Calvi–Levenberg survey Thm 7; Bloom–Bos–Levenberg "Asymptotic approximate Fekete arrays" arXiv 2210.10682, web-fetched 2026-10-31: points may lie in shrinking neighbourhoods K_n of K), and the 1D electrostatics: Gauss–Lobatto nodes are the Fekete points of [−1,1], Gauss–Lobatto–Jacobi nodes the weighted ones (Stieltjes). R1 §"Padua observations" and NOTES optimal_point_sets §1/§7 record "Padua asymptotically Fekete" as an UNVERIFIED deduction (subexponential Lebesgue constant ⇒ asymptotically Fekete ⇒ equidistribution to μ_K).

## Sub-problems
| # | Sub-problem | Kind | Payoff |
|---|---|---|---|
| 1 | Write the deduction: Λ_n = O(log² n) ⇒ |det V(Pad_n)|^{1/ℓ_n} / δ(K)-normalisation → 1 (Lebesgue-constant comparison with Fekete points: |det V_Fek| ≤ Λ_n^{N}|det V_Pad| ... standard) ⇒ BBWN equidistribution to the product arcsine measure. | theory (short) | remark / lemma |
| 2 | Weighted stationarity: ∇_B log|det V| = ∇ℓ_B(B); MEASURED: the gradient at interior Padua nodes is *not* zero and not separable (ptp of G_x across nodes with the same x is of the same size as max|G|: 0.6–4.1 for n = 4…12); its size grows ≈ n² in the bulk (n²·max|G| ≈ 34, 160, 484, 2330, 7180 for n = 8…32: faster than n², roughly n^{3.9}) — so Padua is not a weighted-Fekete configuration for any smooth weight with a product-type Jacobi correction (the hypothesis "G_x/n = 2αx/(1−x²)" was tested: α estimates scatter from −0.13 to +0.05 with no stable value). Kill fired. | numerics | negative note |
| 3 | Dubiner equidistribution (De Marchi 2022 "interesting unproved conjecture": nearly optimal points are asymptotically equidistributed w.r.t. the Dubiner metric; web-fetched 2026-10-31): for the square the Dubiner metric is the product Chebyshev-angle metric (Bos–Levenberg–Waldron), and Padua points are equidistributed in Chebyshev angles by construction — the conjecture for Padua is immediate; the nontrivial statement is the converse (equidistributed ⇒ nearly optimal), which is false (equispaced-angle checkerboard sets with Y asymmetric achieve 7–8% lower Λ, draft 2). | theory (remark) | remark |

## Entry points and cheap decisive tests
1. Gradient of log|det V| at Padua nodes via the Lagrange basis (finite differences of ℓ_B(B+h)) — kill: if ∇ ≠ 0 and non-separable, Padua is not weighted-Fekete for a separable weight. **Outcome: kill fired (gradient non-zero, non-separable, growing like ≈ n^{3.9}).**
2. n-th root of |det V(Pad_n)| in the orthonormal Chebyshev basis: MEASURED |det|^{1/ℓ} = 1.709, 1.440, 1.331, 1.269, 1.228, 1.199 (n = 4…24) decreasing slowly — consistent with convergence to a limit but not decisive about the transfinite diameter (needs the Zaharjuta normalisation; not pursued).

## Why not returned
A single deduction (sub-problem 1) plus a negative note (2) plus a remark (3): note-sized. Sub-problem 2's negative result and the GLJ drift of the checkerboard-Fekete optimum are carried by gen4-draft-2 sub-problem 4, where the question "which checkerboard sets are weighted-Fekete" has a programme-scale continuation.

## Closest prior work
Bos–De Marchi–Waldron 2009; De Marchi–Usevich 2014 (Vandermonde product formulae); BBCL survey Problem 5 (explicit Fekete points for d > 1 unknown); Bloom–Bos–Levenberg 2022; De Marchi 2022 (Dubiner conjecture); Briani–Sommariva–Vianello 2012 (Padua is numerically not Fekete: |det| 1.69e35 vs 2.38e35 at n = 9).

## Exclusions
None touched; (c) owns unisolvence of the same sets over fields, not their real extremal geometry.

## IDEA-template record
# IDEA?programme-ideas-claude-4-5 — Padua asymptotically Fekete / weighted-Fekete stationarity

Aliases: asymptotically Fekete Padua; Dubiner equidistribution conjecture; weighted Fekete stationarity; Padua gradient of log det.

- Question / scope: Padua points and the Fekete/equilibrium theory on the square.
- Mechanism and hypotheses: Lebesgue-constant comparison ⇒ asymptotically Fekete; weighted stationarity with a separable Jacobi weight (refuted MEASURED).
- Closest registry entries: R1 "Padua asymptotically Fekete" (UNVERIFIED deduction); CH LIT-030/031; gen4-draft-2.
- Separation criterion: none claimed; note-sized.
- Literature baseline and search limitations: web checks 2026-10-31 (BBL 2022; De Marchi 2022).
- Applicable obstructions: none.
- Novelty gate verdict: deduction is routine; negative note new within documented search.
- Cheapest decisive test: gradient test (done; kill fired for separable weights).
- Kill criterion written before testing: non-zero, non-separable gradient ⇒ not weighted-Fekete with separable weight.
- Test discriminability: finite-difference gradient of an exact Lagrange formula, h = 1e-6, O(1e-9) error vs O(1) values.
- Actual test results and committed evidence: gen4_tests5.py, gen4_tests8.py (scratchpad).
- Disposition: not returned (note-sized); negative part folded into gen4-draft-2.
- Disposition reason: abandoned as a programme; retained as a remark + negative note.
- Canonical theory / negative-result ID: a PD-N candidate ("Padua points are not stationary for any separable Jacobi-type weighted Fekete functional", MEASURED n ≤ 32) if ever written up.
- Topic / audit / history: programme-ideas-20261031, angle D, draft 5, 2026-11-01.
