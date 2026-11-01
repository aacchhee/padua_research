# PD-T142 — A computed polynomial recurrence gives a span-error certificate

Provisional alias: `PD-T?drift-codex-10`. Final ID assigned at PR preparation, 2026-11-01 (handoff 11, after Codex audit-04 acceptance).

ID kind: PD-T.
Aliases: polynomial surrogate span certificate; normalized node inverse certificate; residual-to-span upper bound.
Split from: none. This is a successor to the node-row identity PD-T032, not a reclassification of it.
Split into: none.

## Statement

Fix a positive discrete measure with nodes z_i=(x_i,y_i), weights w_i>0 summing to one, and U(s): evaluation on Π_s is injective. Order all N=N_s monomials by degree and, within degree t, x^(t-j)y^j, j=0,...,t. Let q_0=(sqrt(w_i))_i. For k=1,...,N-1 choose an admissible parent p(k)<k and A_k in {X,Y} so that its monomial is A_k times the parent's monomial. Suppose given vectors and coefficients satisfy the **exact residual relations**

  β_k qhat_k=A_k qhat_p−Σ_(l<k)c_kl qhat_l−f_k,       β_k>0.              (1)

Coefficients include every window and reorthogonalization coefficient; all unlisted coefficients are zero. They need not be close to exact coefficients. Let Qhat=[q_0,qhat_1,...,qhat_(N-1)] have full column rank. Define the unit-diagonal lower triangular matrix

  Lbarhat(z)_00=1,
  (Lbarhat(z)v)_k=v_k+Σ_(l<k)(c_kl/β_k)v_l−(a_k(z)/β_k)v_p,

where a_k(z)=x or y. Put

  Khat_s=max_i ||Lbarhat(z_i)^(-1)||_2,
  ε_s²=Σ_(k=1)^(N-1)||f_k||_2²/β_k²,
  θ_s=||Phat_s−P_s||_2.

Here P_s projects onto the exact evaluated Π_s and Phat_s onto range(Qhat). Then

  θ_s ≤ Khat_s ε_s / σ_min(Qhat).                                      (2)

In particular, if ||Qhat^T Qhat−I||_2≤η<1, then

  θ_s ≤ Khat_s ε_s / sqrt(1−η).                                       (3)

The bound also holds with Khat_s replaced by max_i||Lbarhat(z_i)^(-1)E_+||_2, where E_+ embeds coordinates 1,...,N-1: the start-vector residual is zero. The right side may exceed one; it is then uninformative. No lower bound or prediction of a particular rounding realization is asserted.

## Definitions

The normalized matrix differs from PD-T032's Lhat: Lbarhat=diag(1,β_1^(-1),...)Lhat. Its inverse is Lhat^(-1)diag(1,β_1,...). This distinction is essential when displaying χ separately. All vector norms use ordinary Euclidean coordinates after weights enter q_0. A whole completed degree is required for the identification with Π_s.

## Assumptions

U(s), positive weights, nonzero intended pivots, admissible monomial parents, preceding-column coefficient support, exact q_0, and full column rank. A start-vector error needs an extra source column; it is not silently included. Staircase condition (C) is **not** needed for (2). It matters only for the implicit-section constructions of PD-T050/PD-T054.

## Status by part

Overall status: PROVED (written analytic proof). Codex independent-math-01 reconstructed it, and Claude audit-01 CONFIRMED it.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact certificate (2), (3) | PROVED | Proof below |

Candidate / claim disposition: retained as a variant with a new output quantity; no historical novelty claim.

## Depends on

No unproved result. PD-T032 is the closest predecessor: its node-row identity is re-derived below with all preceding-column coefficients and normalized rows. PD-T053 gives a lower bound, not this upper bound. E1's normal-graph derivative is compatible but unnecessary for this theorem.

## Checks

The result is analytic and does not rely on a computer calculation. A finite evaluation of Khat, ε_s and σ_min is a numerical certificate only if its evaluation errors are bounded. No certified run of this new certificate is claimed. An independently evaluated residual relation can be used even when an implementation did not record individual rounding errors. Independent checks:

- **Codex independent-math-01** ([checks/independent-math-01.md](../../../topics/padua-lanczos-drift-20261101/checks/independent-math-01.md), E3 paragraph) reconstructed the surrogate-span and projector argument.
- **Claude audit-01** ([checks/audit-01/E3-E4-records-10-15.md](../../../topics/padua-lanczos-drift-20261101/checks/audit-01/E3-E4-records-10-15.md), run 3) reconstructed the proof independently and confirmed it. That run includes an exact Fraction check of surrogate triangularity and of the node-row identity, and float64 (MEASURED) corroboration of (2), (3) and the E_+ refinement.

## Sources

Repository predecessors: PD-T032; PD-T037 (measured selection-dependent propagators); PD-T041 (finite exact entry-growth certificate); PD-T047/PD-T050/PD-T053/PD-T054. Literature context: LIT-241–243, Barrio–Peña–Sauer 2010, triangular-substitution bounds and selection freedom; LIT-280–284, multivariate V+A exact span and orthogonality statements as digested in the existing L2 review. Those digests do not supply a locally read span-accuracy theorem. No source-priority claim is made.

## Proof or evidence

Define polynomials phat_0=1 and

  β_k phat_k(z)=a_k(z)phat_p(z)−Σ_(l<k)c_kl phat_l(z).                  (4)

Induction shows phat_k has degree at most deg(k), has a nonzero coefficient on monomial k, and contains no monomial later than k. Indeed multiplication by one coordinate preserves the monomial order; admissibility gives the intended leading monomial, and preceding-column subtraction cannot cancel it. Positive β_k does not change nonvanishing. Thus phat_0,...,phat_(N-1) form a basis of Π_s. This remains true if the coefficients are inaccurate or large.

Let Vhat_ik=sqrt(w_i)phat_k(z_i). Its range is exactly S_s, even though its columns need not be well conditioned or orthogonal. Write ξ_i=(qhat_ik)_k and ζ_i=(0,f_1(i)/β_1,...,f_(N-1)(i)/β_(N-1)). Equations (1) and (4), at node i, give

  Lbarhat(z_i)(ξ_i−sqrt(w_i)phat(z_i))=−ζ_i.

Consequently, for E=Qhat−Vhat,

  ||E||_F²=Σ_i||Lbarhat(z_i)^(-1)ζ_i||_2²≤Khat_s² ε_s².              (5)

Let Uhat=Qhat(Qhat^T Qhat)^(-1/2), an orthonormal basis of the computed span. As (I−P_s)Vhat=0,

  ||(I−P_s)Uhat||_2
    ≤||E||_2 ||(Qhat^TQhat)^(-1/2)||_2
    ≤Khat_s ε_s/σ_min(Qhat).

U(s) makes both spaces N dimensional. For equal-dimensional subspaces, ||Phat_s−P_s||_2=||(I−P_s)Uhat||_2: this follows, for example, by diagonalizing the cross Gram matrix of orthonormal bases, which gives the cosine/sine two-dimensional principal-angle blocks. This proves (2). The Gram hypothesis gives σ_min(Qhat)≥sqrt(1−η), proving (3). Since ζ_i has zero first coordinate, restricting the inverse to E_+ also proves the refinement. ∎

## Scope

This converts the old node-row identity into an upper bound for distance to the **exact polynomial space**. The extra argument is that the computed-coefficient polynomial surrogate spans Π_s regardless of coefficient accuracy. Neither orthogonality of that surrogate nor closeness of computed coefficients is assumed. It does not show Khat is small. In particular PD-T041's large exact propagator entries and PD-N013/PD-N015's drift are preserved, not bypassed.

## Open items

An inexpensive rigorous Khat bound; useful sharp bounds for the projected inverse instead of the unprojected Khat; transfer of an exact-data score to a finite working precision with a usable radius. The first-order, exact-data selection criterion is treated separately in PD-T143.

## History

- 2026-11-01: Codex mathematical developer; requested `gpt-6.1-sol`, xhigh, actual runtime variant/effort not separately exposed here; rules read at 806cc7b4509fd93bae652f9545d32d95529f8281. New analytic result. No Git operations by this subagent.
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): stale independence text updated, consistent with audit-01 E34-F6; no mathematical change. Original wording: «Overall status: PROVED (written analytic proof; independent audit pending).»
