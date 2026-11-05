# PD-T116 continuation — signed Padua fixed-ratio target remains OPEN

ID kind: PD-T (existing PD-T116; no duplicate global claim allocated).
Aliases: F3 actual signed eta(theta); restricted signed-energy comparison.
Split from: none; continuation preserves the existing target.
Split into: the supporting result
`PD-T?mz2d-frontier-codex-f3-01` is not a parameter part of the target.

## Statement

Preserve the original PD-T116 wording: for every real `0<=theta<1`,
find an explicit `eta(theta)<1` such that for every integer `m>=1`,
integer `0<=n<=theta*m`, and real `p in Pi_n`,

\[
 (1-\eta(\theta))\int_{[-1,1]^2}p^2\,dx\,dy
 \le Q_m(p^2)
 \le(1+\eta(\theta))\int_{[-1,1]^2}p^2\,dx\,dy.
\]

Alternatively supply a fixed theta below one and a rigorous counterexample.

## Definitions

Q_m is exactly the signed interpolatory Lebesgue rule on the physical
even checkerboard with x/y denominators m,m+1, total-degree-m exactness
and mass-four dxdy measure. The Gram spectrum is in the continuous
orthonormal Legendre-product basis. The desired assertion requires
`lambda_min>0` uniformly at fixed ratio and `lambda_max<2` uniformly.
The positive reference form S_m from the supporting result is a
different rule and is not substituted for Q_m.

## Assumptions

All integer m>=1, real polynomials, total degree, fixed checkerboard
and signed interpolatory weights. No global classification of negative
nodes, no positive-weight theorem, no uniform negative-corner leverage
bound, and no unverified spectral asymptotic is assumed.

## Status by part

Overall status: **OPEN**.

| Target part | Status | Remaining gap |
|---|---|---|
| Uniform positive lower endpoint for every fixed theta<1 | OPEN | No bound for the actual combined signed correction on the admissible value space |
| Uniform upper endpoint strictly below two | OPEN | Positive-reference equivalence supplies only a large reference upper bound |
| Any new nontrivial range theta<=theta0 with theta0>1/2 | OPEN | No such signed bound obtained here |
| Alternative rigorous fixed-ratio counterexample | OPEN | None produced |

Half-exactness at `2n<=m` is inherited routine context, not a new
substantive split. The supporting positive-reference theorem does not
change this record to PARTIAL. Candidate f3-02 is **deferred**, not
rejected; a missing signed cancellation estimate is not a disproof.

## Depends on

Existing PD-T106/109 give exact aliases and operator architecture.
PD-T115 supplies the original exact diamond reconstruction. New
`PD-T?mz2d-frontier-codex-f3-01` supplies an explicit positive reference
MZ equivalence with the actual diagonal weights checked. These are
supporting results, not proofs of either signed endpoint. PD-N045/048/053
remain the applicable scoped transfer obstructions.

## Checks

Complete gate and retained candidates in `../ideas-f3.md`; analytic
attempt in `../attempts/F3.md`. No mathematical computation or
independent rerun by the F3 developer. No all-m or fixed-ratio inference
is drawn from the separate G0 or campaign float spectra.

## Sources

Original full PD-T116 record and the full relevant local predecessor
records, read as documented in the gate. No new primary source or
historical priority claim.

## Proof or evidence

There is no proof or counterexample for the displayed target.
The supporting theorem closes a formerly unchecked localization step:
an exactly reconstructing kernel has summable weighted diagonal
envelopes, and its positive sampled form is coercive at fixed ratio.
It leaves a separate signed step, which cannot be replaced by a
pointwise floor because the actual corner weights are negative.

In particular, writing `Q_m=Q_(m,+)-Q_(m,-)` and using the supporting
norm equivalence does not bound `Q_(m,-)` by a small constant. PD-N048
already shows a logarithmically divergent continuous rank-one corner
norm even within the half-exactness range where the signed answer is
exact. Thus the cancellation must be retained before taking a norm.

For a concrete next obligation, let `V_(m,n)` be the range of polynomial
sampling into `L2(mu_Gamma,nu_m)`. Prove two uniform inequalities for
the **actual signed form on V_(m,n)**, with explicit constants
`a(theta)>0,b(theta)<2` relative to the continuous norm. A sharper
comparison to the reference S_m is permissible, but its constants must
combine with the reference theorem to yield those precise endpoints;
an unspecified bounded residual or a lower estimate alone does not.

## Scope and open items

F3 supplies a new supporting theorem but no newly resolved signed
ratio case. Resume candidate f3-02 only with an actual combined signed
kernel estimate, an effective limiting comparison, or a rigorously
certified counterexample. A direct norm restatement without estimates
does not meet the resumption condition. Independent and Claude audits
are pending for the supporting proof.

## History

2026-11-05, Codex F3 developer, requested gpt-6.1-sol xhigh; rules/input
`83cf6f1ee244f2e72057332a7ec04ee74db1f0de`. Original PD-T116 wording,
quantifiers and OPEN status preserved. New work resolves a supporting
localization obligation only; no silent narrowing of the original target.
