# L6 actual-n1 implementation contract — prospective and unexecuted

Rules `9825d184517db81d0aad8542fbd6639f2164b803`. Codex mathematical developer, requested `gpt-6.1-sol`, xhigh; runtime variant/effort not independently exposed. Date: 2026-11-05. **Status: OPEN; no scientific code, implementation run, output bytes or nearby measure has been produced under this contract.** This is an implementation specification for IDEA-262 / IDEA?lanczos-frontier-codex-L6-02, not a new PD-T claim. It follows the completed gate and target/kill record in [ideas-l6-continuation.md](../ideas-l6-continuation.md).

## Exact first target and kill conditions

First determine the exact partial coefficient data produced by the scalar square n1 construction below. Determine whether its prescribed algebraic completion is consistent, and whether its complete operator residuals permit a nontrivial PD-T145 comparison. Only then attempt a certified positive localized representation. General PD-T056(G) remains OPEN even if this one n1 case is decided.

Before execution, the implementation must implement this operation order literally and pass an independent review of its source and exact byte-level interpreter. An unrecorded operation, reassociation, changed input, alternative completion or post hoc tolerance change invalidates this experiment. A failed consistency test or a radius-zero fit at the frozen allowance is a legitimate stopping outcome, not a reason to change the target. No search over precision, node rotation or input order is part of the first run.

The scoped theorem [l6-01](l6-01-full-square-residual-bound.md) already rules out exact PD-T145 matching with unbounded e/u, bounded Q conditioning and two complete uniformly O(u) residuals. This contract does not attempt to evade that result by omitting a Y column. It records which hypothesis the actual data satisfy or fail.

## Frozen input and arithmetic

- Intended base measure: `mu_0=(delta_(0,0)+delta_(1,0)+delta_(0,1))/3`; row order exactly `(0,0),(1,0),(0,1)`. Original coordinate matrices: `X=diag(0,1,0)`, `Y=diag(0,0,1)`. Coordinates are exact binary64 zero/one. The intended mass is one; rounded startup normalization does not redefine the intended measure.
- Precision: IEEE binary64 only, `u=2^-53`; round to nearest, ties to even after **each** addition, subtraction, multiplication, division and square root. No fused multiply-add, extended register evaluation, BLAS, parallel reduction, compiler reassociation or fast-math. Scalar square root must be correctly rounded. No free aggregate perturbation may be injected.
- Startup: `s=RN(sqrt(3))`, `a=RN(1/s)`, `q0=(a,a,a)^T`. The operations `sqrt(3)` and division are separate roundings. Preserve their actual results and the signed-zero bits of every stored scalar. Any exceptional or subnormal result is recorded; no flush-to-zero mode is allowed.
- Basis order: `(1,y,x)`. Y injects the pure-y column and X is the full operator. This mirror convention makes the omitted Y product explicit below. For comparison with PD-T145's `(1,x,y)` sections, use the exact section map in `(1,y,x)`, equivalently a simultaneous orthogonal change of the theorem's gauge. Do not compare arrays in different gauges entrywise.

Here `RN` always means the arithmetic just specified. A stored binary64 word is interpreted as its exact dyadic rational in all later certified analysis.

## Scalar primitives and basis generation

`DOT(v,w)` starts from binary64 `+0` and, for rows r=0,1,2 in that order, computes `p=RN(v_r*w_r)`, then `s=RN(s+p)`. It returns s. `NORM(v)=RN(sqrt(DOT(v,v)))`. Coordinate multiplication `PROD(A,q)` computes `RN(A_rr*q_r)` separately for rows 0,1,2, with A exactly X or Y.

`CGS2(v; q0,...,q_(k-1))` means exactly two classical Gram–Schmidt passes. In each pass:

1. Set `b_i=DOT(q_i,v)` for i=0,...,k-1, using the **same unmodified** v for every dot product in the pass.
2. For each row r=0,1,2, start an accumulator at `+0`; for i=0,...,k-1, compute `p=RN((q_i)_r*b_i)` and `s=RN(s+p)`; set `w_r=RN(v_r-s)`. All rows use the saved b values and saved v.
3. Replace v by the complete saved w.

Return the final v and coefficients `h_i=RN(b_i^(1)+b_i^(2))`. Do not replace these coefficients by a fresh dot product. Save both passes' b values, row updates and returned coefficients.

Create q1 from `v=PROD(Y,q0)`, `CGS2(v;q0)`, `beta1=NORM(v)`, then `(q1)_r=RN(v_r/beta1)`. Its stored generation coefficient is `g0=h_0`. Create q2 from `v=PROD(X,q0)`, `CGS2(v;q0,q1)`, `beta2=NORM(v)`, then `(q2)_r=RN(v_r/beta2)`. Its stored generation coefficients are `h0,h1`. Stop as INVALID if a beta is nonpositive/nonfinite. Save Q with these three columns; do not reorthogonalize it again or replace it by a reference basis.

This is a specified one-relation scalar construction, not an identification with an existing library executable or a historical BJ receipt.

## Degree-one section data and saturation

The square count is `M=N1=3`. No fourth vector is normalized. Degree-two raw products are used only to define degree-one section coefficients; a small terminal vector is not promoted to a new basis column.

Let e0,e1,e2 denote the coefficient coordinate vectors in the stored order. The **raw formed data D** are:

- `H_X e0=h0 e0+h1 e1+beta2 e2`, directly from q2 generation;
- for j=1,2, form `v=PROD(X,qj)` and run `CGS2(v;q0,q1,q2)`, without normalization; its returned three coefficients form `H_X ej`; save the terminal vector;
- `j0=g0 e0+beta1 e1`, directly from q1 generation;
- form `v=PROD(Y,q1)` and run `CGS2(v;q0,q1,q2)`, without normalization; its returned coefficients form `j1`; save the terminal vector.

These are exactly 14 stored scalars: nine entries of H_X, two nonzero slots of j0 (its last slot is an exact prescribed zero), and three entries of j1. Generation coefficients and final projection coefficients are never silently substituted for each other.

The missing coefficient column is prescribed by an **exact algebraic interpretation of those bytes**:

`j2=(H_X j0-h0 j0-h1 j1)/beta2`, `H_Y=[j0,j1,j2]`.                  (C1)

All operations in (C1) are on exact rationals; it is a deterministic interpretation/completion, not an additional floating-point computation whose rounding is omitted. This fixes the completion uniquely and gives `[H_X,H_Y]e0=0` on the interpreted data. It does not assert symmetry, positive-moment consistency or a small local residual. Save the raw D and completed pair separately. No symmetrization, last-block adjustment, free-entry fit or near-commuting repair is part of the computed output.

## Complete residuals, including omitted Y

After D and (C1) are frozen, evaluate **every** column of

`F_X=XQ-Q H_X`, `F_Y=YQ-Q H_Y`

as exact rational expressions from the stored words and (C1). In particular,

`(F_Y)e2=Yq2-Qj2`                                                      (C2)

is an explicit omitted-product diagnostic. `Yq2` was not used by the construction; forming it for the diagnostic does not repair Q or D. No O(u) label is attached to (C2) without an actual certified bound. Report columnwise norms as well as the complete spectral norms. A bound only on the formed columns is not a bound on F_Y.

Compute exact rational `Q^TQ-I`, certify invertibility, and enclose its spectral norm, `||Q||_2`, `sigma_min(Q)` and both full residual norms with rational outward bounds. These enclosures may use exact symmetric characteristic polynomials plus rational root isolation; any future checker must be independently reconstructed. Convert neither decimal approximations nor singular values from an ordinary floating-point library into certificates. No such enclosure calculation has yet been run.

Freeze the diagnostic budget at `c=64`: record separately whether `||Q^TQ-I||_2<=1/2` and whether **each complete** residual is at most `64u||Q||_2`. Failure of that particular budget is an outcome; it does not refute an O(u) statement with a different declared constant. If exact PD-T145 matching is established, report the actual bound `e/u<=24 sqrt(3)c_actual`, with a certified residual constant, rather than asserting separation from selected formed columns.

## Consistency and a nontrivial positive-model gate

Treat (C1) as exact data. First test the full degree-one structured-consistency conditions and positive leading pivots in this fixed gauge, using PD-T057's section map. Symmetry by itself is only used with the verified pattern/interior identities; do not invoke PD-T070 without checking its data-convention hypotheses. If the pair is consistent, reconstruct its unique **mass-one** functional `Lhat` on all ten monomials of degree at most three and verify `M1(Lhat)>0` exactly. No free rescaling of Lhat is allowed.

If raw data are inconsistent, the exact-match branch stops as INCONSISTENT. A separately labeled toleranced branch may propose corrected raw data `D_c` only with a certified maximum-entry correction at most `rho_D=64u`, positive pivots and all exact consistency conditions. Preserve D. The correction is a certificate sought after the run, not a change to the operation contract. Every claimed conversion of `rho_D` into a moment error requires an explicit certified local section-to-moment bound; an unspecified O(rho_D) is insufficient. Any assertion robust to correction choice must be proved for all admissible corrections, rather than selecting one that manufactures a large forward effect.

For an accepted consistent reference Lref (raw exact branch, or an explicitly certified corrected branch), define

`epsilon=||Lref-L_mu0||_infinity`,

using maximum absolute monomial moment error through degree three. Freeze the positive-fit allowance at `rho_L=epsilon/6`; fit measures must have mass exactly one. Before support optimization, certify that the original measure does not already meet the **total** allowance. The correction, conversion and fit errors must be included in that total; require the correction/conversion contribution to be at most `epsilon/12`, and establish the corresponding inequality relative to the original raw data. If no such certified bridge from raw data exists, the corrected model cannot be reported as an actual-run conclusion. If epsilon=0 or the radius-zero original measure meets the total allowance, stop as NON-DISCRIMINATING.

An exact PD-T145-family match requires all ten reconstructed moments to equal its specified moments for one certified `0<e<=1/300`; recognizing only the three changed second moments is insufficient. For that exact match, the fixed allowance `e/6` is below `e/3`, so PD-T145 gives the nonzero lower radius `sqrt(e/6)` and its explicit four atoms give an exact upper radius `sqrt(6e)`. Those statements become applicable only after the actual-data matching and correction obligations have been proved. For approximate family matching, its moment mismatch must be added to the fit and correction budgets before applying PD-T145; the theorem's exact-match residual barrier cannot be applied unchanged.

For a general consistent output, a positive localized-model certificate must provide positive weights, atoms in the stated closed node balls and exact or certified moment residual at most rho_L. A failed optimizer or a finite search without a separating certificate is INCONCLUSIVE, not nonexistence. No n3/4 Padua attempt begins under this n1 contract; it requires a separate frozen input/operation/data specification.

## Required future receipt and review

A future run record must contain the reviewed source hash, implementation/runtime/compiler/platform arithmetic settings, fixed input words, every intermediate and final scalar as hexadecimal binary64 bytes, exact rational interpretations, raw D, Q, (C1), terminal vectors, full (C2), certified norm/consistency checks, explicit correction and moment-error bounds if used, and the positivity/support certificate if one is found. A distinct checker must reconstruct the scalar operation trace and the exact interpretation. Routine independent mathematical review uses high effort; no new structural xhigh review is implied by this contract.

This specification has no executable, no producer/checker hashes and no observed outputs. **Runs needed: future implementation plus independent source/trace review and one frozen n1 execution; not assigned or performed in the present analytic task.**

Distinct reviewer `/root/reviewer`, requested `gpt-6-astra` high (runtime metadata not independently exposed), read this full prospective specification at SHA256 `e2d5e70ec1f6aab7f5748e388001d882f6aeb6eb163f3a4dd35ceb314ae4ffdb` and returned **scoped prospective PASS**: literal scalar order, exact completion, explicit omitted-Y diagnostic and consistency/correction/nontriviality limits are sufficiently separated. The durable record is [independent-checks-frontier-05.md](../independent-checks-frontier-05.md). This accepts the specification's scope, not a nonexistent implementation, source trace, run or model. The review also confirms that `sqrt(e/6)` uses the exact PD-T145 reference with allowance e/6; any correction-inclusive or approximate-family application must use its separately enlarged total gamma budget. Changes after that reviewed input are review metadata only.

## History and status boundary

2026-11-05: prospective contract saved after the completed L6 reading gate and the analytic complete-residual theorem. It fixes a mirror one-relation n1 construction and a deterministic exact completion, while exposing the omitted Y column and all raw-data/correction obligations. It supplies no actual nearby measure and changes no status of PD-T056(G). Parent owns Git, shared registries and final allocation.

2026-11-05: distinct Astra-high scoped prospective review PASS at the input hash recorded above. No contract operation, data convention, acceptance threshold or mathematical status changed after review.
