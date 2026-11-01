# PD-T113 — signed Padua hyperinterpolation at the correct reproduced degree

Provisional alias: `PD-T?mz2d-codex-31`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-T. Aliases: `m>=n+r` reproduction; signed relaxed-exactness
error; aliasing-term estimate. Split from: D5 application. Split into:
norm theorem PD-T112; the unresolved uniform operator target is
PD-T114, not part of this statement.

Rules/base `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; 2026-11-01.
Codex, allocated xhigh; runtime model metadata unexposed.

## Statement and definitions

Use the campaign's exact signed Padua rule `Q_m` for `dx dy` on
`Omega=[-1,1]^2`, fixed in definitions.md. It has mass four and is exact on
`Pi_m`. For an integer `n>=0`, let `{phi_alpha}` be the continuous
L2(dx dy)-orthonormal total-degree Legendre basis of `Pi_n`. Define the
direct quadrature coefficient operator, without a Gram inverse,

\[
H_{m,n}f=\sum_{|\alpha|\le n} Q_m(f\phi_\alpha)\phi_\alpha.
\]

Let `G_(m,n)`, `tau_m`, and `beta_abs(m,n)` be the signed Gramian, weight
total variation, and largest absolute-Gram eigenvalue from
PD-T112. Put
`C_(m,n)=sqrt(tau_m beta_abs(m,n))`. For every integer

\[
0\le r\le n,\qquad n+r\le m,
\]

the operator reproduces `Pi_r`, and every real continuous f satisfies

\[
\|f-H_{m,n}f\|_{L^2(dx\,dy)}
\le(2+C_{m,n})E_r(f),\qquad
E_r(f)=\inf_{q\in\Pi_r}\|f-q\|_\infty. \tag{1}
\]

The exact norm in PD-T112 may replace `C_(m,n)` in (1).
The negative-leverage majorant from that theorem is another valid choice.
No positivity of the signed weights or lower Gram bound is required.

For every `q in Pi_n`, there is also the valid aliasing-term estimate

\[
\|f-H_{m,n}f\|_2
\le(2+C_{m,n})\|f-q\|_\infty
+\|q-H_{m,n}q\|_2, \tag{2}
\]

where, if c is the orthonormal coefficient vector of q,

\[
\|q-H_{m,n}q\|_2
=\|(I-G_{m,n})c\|_2
\le\eta(m,n)\|q\|_2. \tag{3}
\]

In particular at the campaign endpoint `n=m-1`, affine polynomials are
reproduced for every `m>=2`, so (1) applies with `r=1`. For `m=1,n=0`, use
`r=0`. For `m>=3`, degree one is the **maximal complete total-degree space**
reproduced, by the separate obstruction PD-N051. An E2-only or
E_(m-1)-only estimate is therefore not inferred from this operator.

## Assumptions and status

Overall status: **PROVED** in development; independent audit pending.

| Mathematical part | Status | Evidence |
|---|---|---|
| Reproduction and error bound at `n+r<=m` | PROVED | Product-degree argument and norm theorem below |
| Aliasing-term estimate | PROVED | Coefficient identity below |

The reproduced-degree statement is a routine exactness step within the error
application. No all-m uniform bound for `C_(m,n)` is asserted. The original
uniform operator target remains separately OPEN rather than being narrowed
to this finite-m statement.

## Depends on / sources

PD-T112 supplies the norm bound. Only the stated degree-m exactness
of the signed Padua rule is otherwise needed; it is independently established
by the campaign foundation / PD-T106. The primary source
provenance for integrating the degree-m interpolant is
LIT-312/LIT-427 in literature.md. PD-T025 is the positive-rule
predecessor; ASV equation (7) is relevant aliasing context, not a theorem
assumed for signed weights.

## Proof

Let `q in Pi_r`. Every `q phi_alpha` has total degree at most `r+n<=m`.
Therefore `Q_m(q phi_alpha)=integral q phi_alpha`. Since `r<=n`, expansion
in the orthonormal basis gives `H_(m,n)q=q`.

For every such q, the triangle inequality and PD-T112 give

\[
\|f-H_{m,n}f\|_2
\le\|f-q\|_2+\|H_{m,n}(f-q)\|_2
\le(2+C_{m,n})\|f-q\|_\infty,
\]

because the square has mass four. Take the infimum over q to obtain (1);
attainment of the best approximation is unnecessary.

For arbitrary `q in Pi_n`, retain `q-Hq` in that same decomposition to get
(2). If `q=sum c_alpha phi_alpha`, direct evaluation of each quadrature
coefficient gives coefficient vector `Gc` for Hq. Orthonormality then gives
(3). This remains valid for an indefinite symmetric G.

## Checks, scope, and open items

No numerical execution is needed or claimed. The factors `sqrt(4)=2`, the
two separate inequalities `r<=n` and `r+n<=m`, and the absence of a Gram
inverse were checked explicitly. Independent audit is pending.

For a sequence of degree choices, (1) implies convergence whenever
`(2+C_(m,n_m))E_(r_m)(f)->0` with `r_m<=min(n_m,m-n_m)`. At the endpoint
this sufficient reproduced-degree argument fixes `r=1`; it alone gives no
convergence claim for a general fixed f. Formula (2) can give better
conclusions only after separately bounding its aliasing term.

## History

2026-11-01: signed analogue of the known positive-rule error decomposition
written with repaired norm hypothesis and exact reproduced degree. No
historical novelty claim; no submitted manuscript changed.
