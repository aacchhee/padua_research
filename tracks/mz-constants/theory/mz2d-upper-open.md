# PD-T?mz2d-codex-10 — endpoint Padua upper spectrum remains open

ID kind: PD-T.
Aliases: signed two-dimensional upper MZ threshold; parity-block Schur target.
Split from: the upper-threshold part of PD-T028, whose original other
positivity, lower-order and eta-convergence questions remain unchanged.
Split into: no proved part of the universal target. Scoped mechanism
failures are [PD-N?mz2d-codex-10](mz2d-upper-sign-obstruction.md) and
[PD-N?mz2d-codex-11](mz2d-upper-tensor-obstruction.md).
The orchestrator owns the final crosswalk and registry integration.

## Statement

For every integer `m>=2`, determine whether the signed interpolatory
Padua rule with the fixed even-checkerboard `dx dy` conventions satisfies

\[
 Q_m(p^2)<2\int_{[-1,1]^2}p^2\qquad
 (0\ne p\in\Pi_{m-1}),                                  \tag{1}
\]

equivalently `lambda_+(m,m−1)<2`. If true, derive an explicit all-`m`
upper bound below two. This statement is not weakened to a marginal,
positive-weight cubature, tensor-degree space, or finite observation.

## Definitions

Use [definitions.md](../../../topics/padua-mz-2d-20261101/definitions.md).
In the unnormalized product-Chebyshev basis of `Pi_(m-1)`, write `H`
for the positive continuous mass matrix and `R` for the signed Padua
mass matrix. The target is exactly `A:=2H−R` positive definite.
The Legendre Gram spectrum equals the generalized spectrum of `(R,H)`.

## Assumptions

All `m>=2`, real polynomials, total degree `m−1`, unnormalized Lebesgue
measure of mass four, and signed interpolatory weights. Positive
Chebyshev Padua cubature weights are a different rule.

## Status by part

Overall status: **OPEN**.

The three bounded D2 rounds did not prove (1), disprove it, or produce
an explicit universal gap. D1's exact aliases and finite-family
architecture are supporting results, not proved parts of (1).
The elementary `m=2` exactness observation is not aggregated into a
separate substantive case theorem. The finite D0 spectra retain their
own measured/certified scopes and supply no universal inference here.

Candidate disposition: the target is retained OPEN; the final block
route IDEA?mz2d-codex-12 is **deferred**, not rejected.

## Depends on

[PD-T?mz2d-codex-01](mz2d-aliasing.md) gives exact moments and the
mass pencil. [PD-T?mz2d-codex-04](mz2d-defect-structure.md) gives the
bounded masked-tensor architecture. These are development proofs with
their own pending audit. PD-T021 supplies only marginal compression;
PD-T014/022 concern one-dimensional CC and do not control the missing
Padua modes. No published theorem is imported as a proof of (1).

## Checks

Read prior M1/M3 theory, the Padua marginal and OPEN target, existing
MZ manuscript and relevant implementations before attempting transfer.
D1 PASS was received before D2 mechanism generation. Gate, prewritten
separations and round limits are in
[ideas-d2.md](../../../topics/padua-mz-2d-20261101/ideas-d2.md).
Executed small diagnostics and exact command/source identities are in
[D2.md](../../../topics/padua-mz-2d-20261101/directions/D2.md).

## Sources

Local predecessors IDEA-056/062/072/073, PD-T014/021/022/028 and D1.
The literature index was screened; primary convention checks belong to
the separate literature worker. No historical novelty or priority claim.

## Proof or evidence

There is no proof of (1). The following block organization makes the
remaining obligation concrete, without presenting an equivalent
reformulation as a solved mechanism.

### Exact parity blocks

Let a basis index be `alpha=(i,j)`. If `m` is even, a nonzero Padua
moment has even x degree; if `m` is odd, it has even y degree. To see
this directly from D1, folding preserves parity. On the direct branch
both moment degrees must be even. On the complementary branch they
must have the parities of `(m,m+1)`. Thus the x degree is always even
for even `m`, and the y degree is always even for odd `m`.

Product-to-sum therefore shows that `H,R,A` split by x-index parity
when `m` is even, and by y-index parity when `m` is odd. Within each
preserved parity sector, split by the other index parity. Then

\[
 A=\begin{pmatrix} A_{00}&C\\ C^T&A_{11}\end{pmatrix},
 \qquad H_{01}=0,\qquad C=-R_{01}.                       \tag{2}
\]

For `alpha=(i,j)` and `beta=(k,l)` in opposite secondary parity groups,
the exact mixed block is

\[
 C_{\alpha\beta}=-\frac14
 \sum_{u\in\{i+k,|i-k|\}}\sum_{v\in\{j+l,|j-l|\}}
 \mathbf1_{F_m(u)+F_{m+1}(v)>m}
 h_{m-F_m(u)}h_{m+1-F_{m+1}(v)},                         \tag{3}
\]

where `F_N` is the triangular fold. The direct moment branch vanishes
by the secondary parity difference. All sums are multiset sums. The
diagonal blocks are obtained from the same exact D1 formula by
restricting both indices to the corresponding group; no positivity
has been asserted for them.

If both nonempty diagonal blocks in (2) are positive definite, put

\[
 \kappa_{m,p}=\|A_{00}^{-1/2}C A_{11}^{-1/2}\|_2.          \tag{4}
\]

Then that preserved sector is positive definite if and only if
`kappa_(m,p)<1`. Indeed congruence by the two inverse square roots
turns (2) into `[[I,K],[K^T,I]]`; minimizing its quadratic form over
one block gives the Schur complement `I−K^T K`. Empty secondary
blocks require only positivity of the remaining block.

This identifies the missing quantitative result precisely: prove
positive diagonal blocks and strict contractions (4) for both preserved
parities, preferably with explicit margins sufficient to recover an
upper bound relative to `H`.

### Why the available architecture does not finish this obligation

D1's finite-family scalar kernels retain triangular truncations, whose
generic coefficient-space norms grow logarithmically with the degree.
That bound does not yield a number below one after the continuous
mass normalization in (4). Taking absolute values also discards the
boundary and cross-coordinate signs exhibited in PD-N?mz2d-codex-10.
No mass-weighted bound for the combined kernel (3), or usable positive
lower bound for the two diagonal blocks, was derived in this bounded
round. This is an unproved obligation, not an impossibility theorem
about all block methods.

The small floating check `m=3..15` found positive diagonal blocks and
mixed-block norms below one, the largest about `0.685`. Those checks
were explicitly exploratory and do not establish any all-degree
contraction or asymptotic rate.

## Scope

The universal upper threshold and quantitative gap remain OPEN.
Neither of the two exact mechanism failures is a counterexample to
the upper target. The parity organization preserves cancellation but
currently supplies a resumption point, not a new spectral theorem.
No manuscript theorem or existing accepted claim was changed.

## Open items

Resume only with a genuinely new mass-normalized estimate of (3) and
the diagonal blocks, or a different explicitly gated mechanism.
A proposed scalar bound should first be tested on the boundary modes
with a reflected zero index, where the `h_0` factor reverses the
mixed-kernel sign. An argument using positive nodal Cauchy–Schwarz or
the doubled tensor weight majorant is excluded by the exact failures.

## History

2026-11-01, Codex, requested gpt-6.1-sol xhigh, rules
`cf89b140530d5838bdb208a8c28f3e7aa676ace3`, unchanged after the merge
of `806cc7b4509fd93bae652f9545d32d95529f8281`.
Three bounded D2 rounds stopped without a universal proof; all killed
or deferred candidates retained. Only assigned D2 files were written.
