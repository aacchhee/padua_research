# PD-N?drift-codex-14 — A pathwise positive lower bound is false in a model admitting zero errors

**Withdrawn as a registry vehicle (Claude response-01 to audit-01 E34-F3).** This file is not to be registered as a PD-N. Its candidate is recorded as the IDEA disposition IDEA?drift-codex-14 in `topics/padua-lanczos-drift-20261101/ideas-e3-e4.md`: REJECTED, refuted only as an ill-posed formalization of PD-T055's quantifier. That entry preserves the full mathematical content below. The U(3) lemma for T_3 is proved inside PD-N?drift-codex-15. The orchestrator is asked to remove this file; nothing else depends on it.

ID kind: PD-N.
Aliases: zero-error quantifier test; noiseless exact-projection counterexample; universal versus worst-case reorthogonalization.
Split from: none. PD-T055 remains the original OPEN target; this file refutes only the explicitly stated interpretation below.
Split into: none.

## Statement

Consider the BJ parent rule, exact positive weights and an admissible degree s. Let the allowed perturbation set contain the all-zero perturbation, as every usual upper-bound rounding model |δ|≤u does. Permit exact projection against all previous columns and exact normalization in this idealized perturbation model.

For every such node measure satisfying U(s), there is a permissible rule and an allowed perturbation realization for which

  range(Qhat_t)=S_t,       δ_X(t)=δ_Y(t)=0       (0≤t<s),

and the implicit J-section of PD-T047 equals the exact J-section. Therefore no assertion of the form

  for every rule and **every allowed error realization**, max_(t<s)δ_J(t)≥cρ^s u||J||,

with c>0, ρ>0, u>0 and ||J||>0 can hold in that model. The assertion remains false if the measure is required to be non-product: the uniform measure on T_3={(i,j): i,j≥0, i+j≤3}, for example, satisfies U(3) and has non-Cartesian support.

## Definitions

δ_A(t)=||(I−Phat_(t+1))A Phat_t||_2, as in PD-T053. “Allowed errors” means the mathematical perturbation set, not the unique output of a specified IEEE implementation. Exact zero errors in an upper-bound model are not asserted to be physically realizable by a finite-precision machine on these nodes.

## Assumptions

Exact inputs and exact start, U(s), fixed BJ admissible parents, full prior projection, nonzero exact pivots. Zero perturbations are allowed. Vectors in this counterexample are exact reals inside the perturbation model; this is an explicit relaxation of working-precision storage, not an IEEE construction.

## Status by part

Overall status: PROVED (analytic scoped refutation; independent audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Universal-over-all-admissible-errors lower bound is false | PROVED | Exact run below |

Candidate / claim disposition: REJECTED for the pathwise perturbation-model interpretation only.
Rejection reason: refuted. Neither deterministic IEEE behavior nor a worst-case-over-errors obstruction is refuted.

## Negative-result scope

Attempted mechanism: deduce a positive drift lower bound from BJ's omission of products and the clamped commutator recursion, independently of the actual error realization.
Parameter range: every fixed unisolvent measure and degree in a zero-admitting idealized perturbation model. The literal PD-T055 includes working-precision storage and has not yet frozen its error quantifier; it is **not** silently relabeled false by this result.

## Depends on

Elementary polynomial Gram–Schmidt; PD-T047's implicit-section definition is used only for identifying the same object. No measured evidence or literature theorem is a proof dependency.

## Checks

Analytic proof; no executed floating computation is needed. The T_3 illustration is exact by the elementary row-factor argument below. No deterministic IEEE experiment is claimed.

## Sources

PD-T055 (wording and open quantifiers), PD-T047 (the identity alone gives no lower bound), PD-N013 (failure of tested actual schemes), PD-N015 (tested selections only). Literature context and coverage limits are in the existing L2 prior-art review; no new literature priority claim.

## Proof or evidence

Run exact Gram–Schmidt: at column k form A_kq_p, subtract its orthogonal projection onto all earlier columns, then divide by the positive residual norm. Inductively each resulting polynomial has the intended nonzero leading monomial and only preceding monomials. Under U(s), no intended residual vanishes. At each completed degree t its columns are therefore an orthonormal basis of S_t. Multiplication by X or Y maps S_t into S_(t+1), so both defects vanish.

The formed J-columns are exact by construction. For an unformed J-product, multiply the creator's Y-relation by J, commute JY=YJ, and substitute earlier exact J-products. PD-T047's implicit recursion is precisely this identity; its acyclicity for BJ follows directly by marching in degree and within degree. Induction gives JQ_(s-1)=Q_s H_J, so the implicit section is exact too. Taking every perturbation equal to zero is allowed, and contradicts any strictly positive proposed lower bound.

For the example, T_3 is not a Cartesian product: both marginals contain 0 and 3, but (3,3) is absent while (3,0) and (0,3) are present. To prove U(3), let p∈Π_3 vanish on T_3. Its restriction to y=0 has four distinct roots, so it vanishes identically and y divides p. On y=1 the quotient has degree at most two and three distinct roots, so y−1 divides that quotient. Repeating on y=2 and y=3 forces a factor y(y−1)(y−2)(y−3) of degree four. Thus p=0. The same argument proves U(m) for T_m. ∎

## Scope

The distinction is logical and material:

| Proposed quantifier | What this file decides |
|---|---|
| Every rule, every model-admissible error sequence | Refuted |
| Every rule, some model-admissible adverse error sequence | Not refuted; PD-N?drift-codex-15 gives a limited example |
| Every rule, its actual specified IEEE output | OPEN; a different assertion |
| Some tested rules, measured actual outputs | Existing PD-N013/PD-N015; unchanged |

There is no zero-rounding argument against the second or third row. In particular, this does not claim that exact-real projection satisfies literal finite working-precision storage. Any final formalization of PD-T055 must choose one of those models instead of interchanging them.

## Open items

A quantitative adverse-error lower bound larger than ordinary local O(u) error; whether the relevant adverse directions occur under a fixed IEEE implementation; a quantified rule class allowing parent repairs or extra products. These remain OPEN.

## History

- 2026-11-01: Codex mathematical developer; requested `gpt-6.1-sol`, xhigh, actual runtime variant/effort not separately exposed; rules 806cc7b4509fd93bae652f9545d32d95529f8281. Original PD-T055 wording preserved. New proposed interpretation explicitly adds “every allowed error realization”; only that interpretation is refuted.
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): audit-01 E34-F3. Added the withdrawal banner only; the rest of the file is unchanged. Converted to IDEA?drift-codex-14 (REJECTED: refuted, ill-posed formalization; no PD-N), with its content moved there and U(3) moved to PD-N?drift-codex-15. No original wording was removed or changed.
