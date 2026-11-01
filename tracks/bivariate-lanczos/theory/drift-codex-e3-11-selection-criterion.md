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

The remainder constant and its neighborhood may depend on the fixed measure, the selection, s, and **the particular perturbation family**: its second-order terms and the smoothness of its coefficient path. **No remainder uniform over all (Hres)-families is asserted.** For example, f_k(t)=t d_k+t²G g_k satisfies (Hres) for every G, while its second-order term grows with G. Suppose instead the families form a compact set in a fixed smooth perturbation implementation, i.e. f_k(t;ω) is jointly C² in (t,ω) on a neighborhood of {0}×Ω, with Ω compact and every member satisfying the hypotheses. Then the remainder can be taken uniformly over ω∈Ω. This is a **fixed-degree first-order theorem**. It is not a uniform finite-u estimate with a specified radius.

## Definitions

The exact L_R^* of PD-T032/PD-T041 has diagonal (1,β_1^*,...). Here Lbar_R^*=diag(1,1/β_1^*,...)L_R^*. Therefore minimizing an unqualified ||L_R^*(-1)|| is not identical to the criterion above. The source budget and normalization must be specified together.

Full reorthogonalization means exact projection onto all previous computed columns in the smooth aggregate-residual model; small operational perturbations may also be admitted if they satisfy (Hres), preserve convergence to that unperturbed run, and have a uniformly smooth local realization. This theorem does **not** identify an arbitrary aggregate direction d with a realizable IEEE rounding pattern.

## Assumptions

U(s), admissible parents, exact start, fixed staircase R, positive exact pivots, smooth perturbation family, and (Hres). χ and K are computed from exact data and operator products, not from the unknown drift. Neither (C) alone nor full reorthogonalization is assumed to bound them. At t=0 exact full projection produces an orthonormal basis and consequently σ_min(Q^*)=1.

## Status by part

Overall status: PROVED (analytic fixed-degree implication). Codex independent-math-01 reconstructed it, and Claude audit-01 CONFIRMED it WITH CORRECTIONS (E34-F4, F5). The response-01 corrections below await re-audit.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Computable filtered minimax criterion and bound (6) | PROVED | Proof below |

Candidate / claim disposition: retained, variant. **Application as an all-degree polynomial stability theorem is CONDITIONAL on the separate, unverified hypothesis** that accepted selections exist with K_0(s), χ_0 and C_loc bounded polynomially in the declared size parameters. The unrestricted existence/safety target is OPEN. No such bound is claimed on the triangle or rotated-square families. Its proposed durable OPEN home is PD-T054's open item, cross-referenced from IDEA-151 (see E3.md and the response-01 proposal for proposed-record-changes.md); it is not carried only in topic prose.

## Depends on

PD-T?drift-codex-10, exact residual-to-span certificate. PD-T054 supplies the characterization and count of (C)-staircases; the proof could instead enumerate all admissible selections, but its implicit-section interpretation would then require care. PD-T050 supplies that interpretation only under (C) and preceding-column support. E1's normal-graph sensitivity is a compatible, sharper diagnostic, not a dependency.

## Checks

No new finite certification or benchmark search is claimed. Exact rational/algebraic data allow exact construction of the Gram–Schmidt coefficients and certified upper bounds for these finite matrix norms. A floating estimate used without an enclosure is MEASURED only. Independent analytic checks:

- **Codex independent-math-01** ([checks/independent-math-01.md](../../../topics/padua-lanczos-drift-20261101/checks/independent-math-01.md), E3 paragraph and finding 3) reconstructed the first-order argument and required the represented-input computability qualification, which is applied.
- **Claude audit-01** ([checks/audit-01/E3-E4-records-10-15.md](../../../topics/padua-lanczos-drift-20261101/checks/audit-01/E3-E4-records-10-15.md)) confirmed (6) for each fixed family, with corrections E34-F4/F5 applied here. Its float64 K_R/χ_R evaluations (`e3_check.py` part C, T_8, s=5) are MEASURED illustrations, not certified scores.

No certified score evaluation of the frozen T_24/rotated-Q_24 rules exists.

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

If K_0(s), χ_0 and C_loc are explicitly bounded by polynomials, (6) has the requested O(u poly(s)χ) first-order form (t=u, with other size parameters declared). This statement does not assume a drift bound: K_R is the inverse norm of a finite exact recurrence and χ_R is a local ratio. They can be checked before the perturbed run. However **their polynomial boundedness is a substantive additional property, not a proved consequence of the staircase structure**. Thus this gives a finite exact-data criterion together with a sufficient first-order theorem. The criterion is a definition, decidable for represented rational/real-algebraic inputs. Neither part shows that the criterion accepts any selection, or that it is efficient or online. It does not settle the unrestricted a priori staircase theorem and does not refute all one-relation selections.

**The staircase restriction is not used in the proof of (6).** (6) holds for any fixed admissible selection R, staircase or not, whose exact pivots are positive and whose scores satisfy K_R(s)≤K_0(s) and χ_R(s)≤χ_0, because PD-T?drift-codex-10 assumes only admissibility. The restriction to (C)-staircases serves only the implicit-section interpretation through PD-T050/PD-T054.

The restriction also excludes the pivot-adaptive rule, which violates (C) on several benchmarks (PD-T050/PD-T054). That rule is nevertheless E1's good comparator and PD-T051's best measured one-relation rule (its reference-free drift bound stays below √u on five of six non-product benchmarks). The same proof gives (6) for the finite criterion over all 2^(s(s−1)/2) admissible selections, in which each middle column (t,j), 1≤j≤t−1, chooses X or Y. That larger search contains the selection the pivot rule makes on exact data (ties broken by a fixed rule), but its accepted selection then lacks the (C)-based implicit-section interpretation. For an adaptive rule, (6) applies only to the selection frozen from exact data; a perturbed run that switches selection is outside it.

**Classification.** The first-order transfer (6) is a routine continuity corollary of PD-T?drift-codex-10 (2) (audit-01 E34-F5 suggestion considered). This file is kept separate for three reasons:

- its main object is the selection criterion itself — its definition, finiteness, represented-input decidability and acceptance/failure semantics — which PD-T?drift-codex-10 does not contain;
- PD-T?drift-codex-10 is a non-asymptotic certificate for arbitrary computed data, whereas (6) has a family-dependent O(t²) remainder, and keeping them apart prevents either quantifier from being read into the other;
- the CONDITIONAL family application and the OPEN safety target attach to the criterion.

The condition cannot erase the old failures: dev, mirror and alt are staircases, and PD-N015 records their measured failures. PD-T041 shows why a small-inverse certificate can fail dramatically for dev on T_24 and rotated Q_24. Its unnormalized entry bounds do not numerically certify the present normalized score without conversion.

## Open items

Prove or refute useful polynomial score bounds for any non-product family; make the selection online without global exponential enumeration; provide a finite-u transfer radius; compare the conservative score with the E1 projected sensitivity κ. An exact upper score is a certificate, not a guarantee that an accepted candidate exists.

## History

- 2026-11-01: Codex mathematical developer; requested `gpt-6.1-sol`, xhigh, actual runtime variant/effort not separately exposed; rules 806cc7b4509fd93bae652f9545d32d95529f8281. The initially considered unqualified minimization of L^*(-1) was corrected to row-normalized Lbar and a χ filter. General polynomial safety remains OPEN. Independent mathematical check noted the input-representation issue; the computability statement now explicitly restricts to represented rational/algebraic data, with the general-real case distinguished.
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): audit-01 E34-F4. The remainder now depends explicitly on the particular perturbation family, with the f_k=t d_k+t²G g_k example, and no uniformity over all (Hres)-families is asserted. The compact-family uniformity sentence is made precise. Original wording: «The remainder constant and its neighborhood may depend on the fixed measure, selection and s. If the residual directions range over a compact bounded set in a fixed smooth perturbation implementation, the remainder…»
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): audit-01 E34-F5. Scope now states that the staircase restriction is unused in the proof of (6) and excludes the pivot-adaptive rule, records the all-admissible-selection extension and the classification as a routine corollary kept in a separate file (with reasons), and qualifies the earlier claim to settle the subproblem. Original wording: «Thus this settles the computable-criterion subproblem and provides a sufficient theorem; it does not settle the unrestricted a priori staircase theorem…»
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): audit-01 E34-F6/F8. Checks now cite independent-math-01 and audit-01, and the status parenthetical is updated. Added the proposed durable OPEN home (PD-T054 open item / IDEA-151). Original wording: «Independent analytic audit and any numerical score evaluation remain to be performed.»; «Overall status: PROVED (analytic fixed-degree implication; independent audit pending).»
