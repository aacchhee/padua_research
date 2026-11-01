# PD-T112 — signed hyperinterpolation norm from absolute weights

Provisional alias: `PD-T?mz2d-codex-30`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-T. Aliases: absolute Gram repair; signed adjoint norm;
negative-leverage bound. Split from: D5 signed-hyperinterpolation application.
Split into: none; reproduction/error application is the separate
PD-T113. The uniform Padua target is PD-T114, OPEN.

Rules/base `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; 2026-11-01.
Codex mathematical worker, allocated xhigh; actual runtime model metadata
unexposed. Development proof; independent audit pending.

## Statement and definitions

Let `Omega` be a compact subset of a Euclidean space with a finite positive
measure `mu`, mass `V>0`. Let `P` be a finite-dimensional real polynomial
space containing constants, with L2(mu)-orthonormal basis
`phi_1,...,phi_d`. Let distinct nodes `z_1,...,z_s` lie in Omega, and let
real weights `w_i` satisfy `sum w_i=V`; weights need not be positive.
For `f` continuous on Omega define

\[
Hf=\sum_{j=1}^d\left(\sum_{i=1}^s w_i f(z_i)\phi_j(z_i)\right)\phi_j.
\]

Put `B_(i,j)=phi_j(z_i)`,

\[
G=B^T\operatorname{diag}(w)B,\quad
A=B^T\operatorname{diag}(|w|)B,\quad
\tau=\sum_i|w_i|,\quad \beta=\lambda_{\max}(G),\quad
\beta_{\rm abs}=\lambda_{\max}(A).
\]

The exact continuous-input norm is

\[
\|H\|_{C(\Omega)\to L^2(\mu)}
=\sup_{\substack{p\in P\\\|p\|_{L^2(\mu)}=1}}
\sum_i|w_i|\,|p(z_i)|
\le\sqrt{\tau\beta_{\rm abs}}. \tag{1}
\]

In particular the norm is unchanged when all `w_i` are replaced by `|w_i|`
while keeping the same basis and nodes. Define

\[
\delta=\sum_{w_i<0}|w_i|,\quad
K(z,z)=\sum_j\phi_j(z)^2,\quad
\chi=\sum_{w_i<0}|w_i|K(z_i,z_i).
\]

Then

\[
\tau=V+2\delta,\qquad
\beta_{\rm abs}\le\beta+2\chi,\qquad
\|H\|\le\sqrt{(V+2\delta)(\beta+2\chi)}. \tag{2}
\]

No lower bound on `G` is assumed. The right hand sides involve the absolute
nodal measure; an upper bound on `beta` alone is insufficient.

## Assumptions and status

All quantifiers and measure/node assumptions are stated above. The continuous
L2 form is positive definite on P, as required by existence of an orthonormal
basis. Repeated nodes, if present in a different formulation, must first be
combined with their signed weights; the distinct-node assumption matters to
the exact norm identity.

Overall status: **PROVED** in development.

| Mathematical part | Status | Evidence |
|---|---|---|
| Exact norm identity and absolute-Gram bound | PROVED | Finite-dimensional duality and explicit continuous sign data below |
| Negative-leverage estimate (2) | PROVED | Positive-semidefinite rank-one sum and trace bound below |

These are the norm theorem and its routine computable corollary, not an
all-m Padua asymptotic statement. No rejection disposition applies.

## Depends on / sources

Elementary Euclidean duality and Cauchy--Schwarz only. PD-T025 is the closest
positive-weight predecessor, not an assumed theorem in this proof.
The D5 gate and source limits are in
`topics/padua-mz-2d-20261101/ideas-d5.md` and `literature.md`.

## Proof

For a unit coefficient vector `a`, write `p_a=sum a_j phi_j`. Then
`||p_a||_2=1`, and coefficient duality gives

\[
\|Hf\|_2=\sup_{\|a\|_2=1}
\left|\sum_i w_i f(z_i)p_a(z_i)\right|.
\]

For fixed `a`, the supremum over `||f||_infinity<=1` equals
`sum_i |w_i| |p_a(z_i)|`. The upper bound is the triangle inequality.
For equality assign `f(z_i)=sign(w_i p_a(z_i))`, using any value in
`[-1,1]` when the product is zero. These values are realized by a continuous
function of norm at most one: choose disjoint small Euclidean balls around
the distinct nodes, take a continuous tent of height one at each node
supported in its ball, multiply by the assigned signs and sum. Restrict the
result to Omega. Interchanging the two suprema proves the equality in (1).

Cauchy--Schwarz with the **nonnegative** weights `|w_i|` gives

\[
\sum_i|w_i||p_a(z_i)|
\le\sqrt{\tau}\left(\sum_i|w_i|p_a(z_i)^2\right)^{1/2}
=\sqrt{\tau}\,(a^TAa)^{1/2}
\le\sqrt{\tau\beta_{\rm abs}}.
\]

The exact norm formula only involves absolute weights, giving the stated
sign invariance. For (2), define

\[
G_-=\sum_{w_i<0}|w_i|\,b_i b_i^T\succeq0,
\]

where `b_i` is the column vector of basis values at `z_i`. Direct expansion
gives `A=G+2G_-`. Also `trace(G_-)=chi`, so
`lambda_max(G_-)<=chi`. The Rayleigh quotient inequality gives
`beta_abs<=beta+2chi`. Finally `sum w_i=V` gives `tau=V+2delta`.
Substitution in (1) proves (2). Since constants belong to P and `Q(1)=V`,
`beta>=1`, so the displayed square roots are real.

## Checks, scope, and open items

This is an analytic proof; no numerical execution or independent rerun is
claimed. The basis normalization and the continuous sign construction were
checked explicitly. Independent mathematical audit remains pending.

For the campaign, `V=4`, `P=Pi_n`, and all `w_i` are the actual signed
Lebesgue Padua weights from definitions.md. The estimate is finite for every
fixed m,n. Uniform Padua estimates on `tau beta_abs`, or on the exact norm
in (1), have not been proved here. A diverging upper majorant would not
prove divergence of the true operator norm. SVZ's reported `tau_m->4`
does not by itself control `beta_abs` or `chi`.

## History

2026-11-01: D5 signed repair independently reconstructed after primary-source
verification and D1 PASS. No novelty claim for the generic duality mechanism.
