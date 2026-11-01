# PD-T?drift-codex-11 — Exact-data inverse scores give a first-order selection guarantee

ID kind: PD-T.
Aliases: filtered staircase minimax rule; normalized inverse selection score; χ-explicit span bound.
Split from: none. The unrestricted staircase safety target remains OPEN; it is not replaced by this implication.
Split into: none.

## Statement

Fix nodes, weights and a completed degree s satisfying U(s). For every staircase selection R of PD-T054, compute its exact, positive-pivot, fully orthogonalized recurrence, using all preceding columns. Denote its unit-diagonal node matrix by Lbar_R^*(z), and set

  K_R(s)=max_i||Lbar_R^*(z_i)^(-1)||_2,
  χ_R(s)=max_(1≤k<N_s)||A_k q^*_(p(k))||_2/β_k^*.

Fix χ_0≥1. Among selections with χ_R(s)≤χ_0, select a minimizer of K_R(s), with any fixed tie break. Return **no accepted selection** if this set is empty or if its minimum exceeds a prescribed bound K_0(s). For represented rational or real-algebraic inputs and real-algebraic thresholds this is a finite computable criterion (2^(s−1) selections, s≥1), with no asserted efficient complexity. For unrestricted real inputs the minimizer is a finite mathematical definition; computability requires an appropriate exact comparison oracle or certified accepting enclosures, and is not asserted without it.

For a selected, accepted R, consider any smooth family of full-reorthogonalization runs satisfying the residual relations of PD-T?drift-codex-10, with exact unperturbed run at t=0, and

  f_k(t)=t d_k+O(t²),
  Σ_k ||d_k||_2²/(β_k^*)² ≤ C_loc² (N_s−1) χ_R(s)².                  (Hres)

Assume q_0 is exact and each unperturbed pivot is positive. Then

  θ_s(t) ≤ |t| C_loc sqrt(N_s−1) χ_0 K_0(s)+O(t²).                  (6)

The remainder constant and its neighborhood may depend on the fixed measure, selection and s. If the residual directions range over a compact bounded set in a fixed smooth perturbation implementation, the remainder can be taken uniformly over that set. This is a **fixed-degree first-order theorem**. It is not a uniform finite-u estimate with a specified radius.

## Definitions

The exact L_R^* of PD-T032/PD-T041 has diagonal (1,β_1^*,...). Here Lbar_R^*=diag(1,1/β_1^*,...)L_R^*. Therefore minimizing an unqualified ||L_R^*(-1)|| is not identical to the criterion above. The source budget and normalization must be specified together.

Full reorthogonalization means exact projection onto all previous computed columns in the smooth aggregate-residual model; small operational perturbations may also be admitted if they satisfy (Hres), preserve convergence to that unperturbed run, and have a uniformly smooth local realization. This theorem does **not** identify an arbitrary aggregate direction d with a realizable IEEE rounding pattern.

## Assumptions

U(s), admissible parents, exact start, fixed staircase R, positive exact pivots, smooth perturbation family, and (Hres). χ and K are computed from exact data and operator products, not from the unknown drift. Neither (C) alone nor full reorthogonalization is assumed to bound them. At t=0 exact full projection produces an orthonormal basis and consequently σ_min(Q^*)=1.

## Status by part

Overall status: PROVED (analytic fixed-degree implication; independent audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Computable filtered minimax criterion and bound (6) | PROVED | Proof below |

Candidate / claim disposition: retained, variant. **Application as an all-degree polynomial stability theorem is CONDITIONAL on the separate, unverified hypothesis** that accepted selections exist with K_0(s), χ_0 and C_loc bounded polynomially in the declared size parameters. The unrestricted existence/safety target is OPEN. No such bound is claimed on the triangle or rotated-square families.

## Depends on

PD-T?drift-codex-10, exact residual-to-span certificate. PD-T054 supplies the characterization and count of (C)-staircases; the proof could instead enumerate all admissible selections, but its implicit-section interpretation would then require care. PD-T050 supplies that interpretation only under (C) and preceding-column support. E1's normal-graph sensitivity is a compatible, sharper diagnostic, not a dependency.

## Checks

No new finite certification or benchmark search is claimed. Exact rational/algebraic data allow exact construction of the Gram–Schmidt coefficients and certified upper bounds for these finite matrix norms. A floating estimate used without an enclosure is MEASURED only. Independent analytic audit and any numerical score evaluation remain to be performed.

## Sources

PD-T032, PD-T037, PD-T041, PD-T046/PD-T047/PD-T050/PD-T053/PD-T054/PD-T055; PD-N013 and PD-N015. LIT-241–243 already contain selection freedom and triangular inverse error bounds; LIT-280–284 and the existing L2 prior-art review delimit what was read about multivariate V+A. No new literature search or novelty claim.

## Proof or evidence

**Exact computation and feasibility.** Under U(s), weighted Gram–Schmidt on the monomials gives a unique positive-leading orthonormal basis. For any admissible parent, A_k q_p has a nonzero intended leading term, so subtracting all preceding columns leaves a nonzero residual. Thus its exact β_k is positive. Coefficients and β can be obtained from the exact weighted polynomial Gram matrix. For rational nodes/weights they are real algebraic numbers; a norm threshold can be decided by exact real-algebraic methods, or conservatively accepted by certified upper bounds. A declared threshold equality may be retained or rejected consistently. The staircase set is finite by PD-T054; hence a minimum exists whenever the χ-filter is nonempty. Empty or over-threshold sets are recorded as failure to certify, never as safe selections.

**First-order transfer.** Positive pivots and smoothness give, for fixed degree,

  β_k(t)=β_k^*+O(t),
  Lbarhat_R(z_i,t)=Lbar_R^*(z_i)+O(t),
  σ_min(Qhat(t))=1+O(t).

The inverse map is smooth at every invertible matrix. With finitely many nodes, Khat_s(t)=K_R(s)+O(|t|). From (Hres),

  ε_s(t)≤|t| C_loc sqrt(N_s−1)χ_R(s)+O(t²).

Insert these three statements in PD-T?drift-codex-10 (2), then use the two acceptance bounds. This gives (6). Compactness gives the uniform remainder assertion because all pivots stay uniformly away from zero in a sufficiently small common neighborhood and only finitely many operations and nodes occur. ∎

**What (Hres) means.** The stronger local inequalities ||d_k||≤C_loc||A_kq_p^*|| imply (Hres) by dividing by β_k^* and summing. In an aggregate perturbation experiment they are a declared input model. For an actual floating implementation, a forward local-error analysis can establish an upper bound of this form, or a measured residual can be inserted directly into PD-T?drift-codex-10. Neither step proves that every budget direction is realizable. Conversely, a large K_R only invalidates this sufficient certificate: its maximizing response may project into S_s, and no drift lower bound follows without the normal projection and a realizability argument.

## Scope

If K_0(s), χ_0 and C_loc are explicitly bounded by polynomials, (6) has the requested O(u poly(s)χ) first-order form (t=u, with other size parameters declared). This statement does not assume a drift bound: K_R is the inverse norm of a finite exact recurrence and χ_R is a local ratio. They can be checked before the perturbed run. However **their polynomial boundedness is a substantive additional property, not a proved consequence of the staircase structure**. Thus this settles the computable-criterion subproblem and provides a sufficient theorem; it does not settle the unrestricted a priori staircase theorem and does not refute all one-relation selections.

The condition cannot erase the old failures: dev, mirror and alt are staircases, and PD-N015 records their measured failures. PD-T041 shows why a small-inverse certificate can fail dramatically for dev on T_24 and rotated Q_24. Its unnormalized entry bounds do not numerically certify the present normalized score without conversion.

## Open items

Prove or refute useful polynomial score bounds for any non-product family; make the selection online without global exponential enumeration; provide a finite-u transfer radius; compare the conservative score with the E1 projected sensitivity κ. An exact upper score is a certificate, not a guarantee that an accepted candidate exists.

## History

- 2026-11-01: Codex mathematical developer; requested `gpt-6.1-sol`, xhigh, actual runtime variant/effort not separately exposed; rules 806cc7b4509fd93bae652f9545d32d95529f8281. The initially considered unqualified minimization of L^*(-1) was corrected to row-normalized Lbar and a χ filter. General polynomial safety remains OPEN. Independent mathematical check noted the input-representation issue; the computability statement now explicitly restricts to represented rational/algebraic data, with the general-real case distinguished.
