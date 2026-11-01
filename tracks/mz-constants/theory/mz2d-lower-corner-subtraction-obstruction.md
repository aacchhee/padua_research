# PD-N?mz2d-codex-21 — A crude continuous corner-subtraction bound diverges

ID kind: PD-N.
Aliases: continuous Christoffel loss; negative-corner rank correction.
Split from: IDEA?mz2d-codex-22, the crude continuous-metric sufficient
comparison inside the leverage route.
Split into: none. The exact corner weights are separately PROVED in
[PD-T?mz2d-codex-20](mz2d-lower-corner-weights.md).

## Statement

For the signed Padua rule, fix either of its actual node corners `c`,
and let `u_c=(ell_a(c_1)ell_b(c_2))_(a+b<=m-1)` in the continuously
orthonormal product-Legendre basis. The magnitude of the corresponding
negative-corner rank-one form has norm

\[
 \big\|(-w_c)u_cu_c^T\big\|_2
 =(-w_c)\,\frac{m(m+1)(m^2+m+1)}{24}
 =\frac16\log m+O(1)\longrightarrow\infty.                 \tag{1}
\]

Consequently no estimate of this corner correction by a constant
independent of m times the continuous squared norm is possible. In
particular the sufficient mechanism

\[
 Q_{m,+}(p^2)\ge a\|p\|_2^2,\qquad
 Q_{m,-}(p^2)\le b\|p\|_2^2,\qquad b<a,
                                                               \tag{2}
\]

with fixed finite constants a,b independent of m cannot work by bounding
the actual negative-node form this way. Here `Q_(m,+)` is the positive-
weight part and `Q_(m,-)` is the magnitude of all negative weights.

### Fixed-ratio corollary

More generally, fix any real theta>0 and put `n=floor(theta m)`.
On `Pi_n`, the same single-corner correction has norm

\[
 (-w_c)K_n(c,c)
 =(-w_c)\frac{(n+1)(n+2)(n^2+3n+3)}{24}
 =\frac{\theta^4}{6}\log m+O_\theta(1)\longrightarrow\infty.
                                                               \tag{4}
\]

For `0<theta<=1/2`, the original signed form is nevertheless **exactly**
the continuous form on these spaces, since `2n<=m`. Thus both the
positive and negative parts can have unbounded continuous operator norm
while their signed difference is the identity. Divergence of the negative
part alone cannot refute a signed spectral estimate even at a fixed ratio.

## Definitions and assumptions

Fixed campaign conventions, every m>=3. Both positive and negative parts
are defined from the actual weights; no global sign classification is
assumed. The negative part dominates the single corner form because all
its summands are nonnegative quadratic forms.

## Status by part

Overall status: **PROVED**, analytic; audit pending.

Candidate disposition: **REJECTED: failed** only for the constant
continuous-metric subtraction mechanism (2). No rejection of the all-m
positivity target or of the positive-node leverage route is made.

## Negative-result scope

Attempted mechanism: dominate each negative corner using continuous
point evaluation, then subtract it from a fixed continuous lower bound
for the positive-node form. Parameter range: all sufficiently large m,
with divergence (1) over both parities. A metric adapted to the positive
node form is outside this obstruction.

## Depends on

PD-T?mz2d-codex-20, exact corner weight and its asymptotic. The elementary
finite Legendre endpoint calculation is written below. No A2 dependency.

## Proof

Since `P_a(1)=1` and `P_a(-1)=(-1)^a`,

\[
 \|u_c\|_2^2=\frac14\sum_{a+b\le m-1}(2a+1)(2b+1).
\]

The generating series `sum_(a>=0)(2a+1)z^a=(1+z)/(1-z)^2` shows that
the cumulative sum equals the coefficient of `z^(m-1)` in
`(1+z)^2/(1-z)^5`. Thus

\[
 \|u_c\|_2^2=\frac14\left[
 {m+3\choose4}+2{m+2\choose4}+{m+1\choose4}\right]
 =\frac{m(m+1)(m^2+m+1)}{24}.                              \tag{3}
\]

Equivalently, (3) follows by expanding and summing the finite polynomial
in a,b. A rank-one positive matrix `(-w_c)u_cu_c^T` has its sole nonzero
eigenvalue `(-w_c)||u_c||^2`. The corner-weight theorem gives
`-w_c=(4log m+O(1))/m^4`, so (3) proves (1).

If the upper bound in (2) held, every rank-one corner subform of the
negative part would have norm at most b. Equation (1) contradicts this.
This disproves the needed premise of that mechanism, without deciding
the signed difference of its positive and negative parts.

For (4), apply (3) with m replaced by n+1: the squared norm of the
point-evaluation vector on `Pi_n` is
`K_n(c,c)=(n+1)(n+2)(n^2+3n+3)/24`. Since `n=theta m+O(1)`, this is
`theta^4 m^4/24+O_theta(m^3)`. Multiplication by the corner-weight
asymptotic proves (4). When theta<=1/2, exactness of Q_m through total
degree m applies to every product of two degree-n polynomials and gives
`G=I`. In that range `P=I+Q_-` in continuous coefficients, so its norm
also diverges while its difference from Q_- is exactly I. ∎

## Checks, scope and open items

No finite computation is required. Numerical leverage values below one
in a bounded range cannot remove this analytic obstruction to a different
metric; nor does divergence in (1) imply an actual negative eigenvalue
of the signed Gram matrix. The exact unresolved leverage estimate is
recorded in the D3 direction file. Independent/Claude audit pending.

## History

2026-11-01, Codex D3, requested gpt-6.1-sol xhigh, rules
`806cc7b4509fd93bae652f9545d32d95529f8281`. Scoped failure split from
the supporting corner formula, preserving the universal positivity and
endpoint targets as OPEN.

2026-11-01, routine corollary appended at root's request after D3 STOP,
following D4's observation. The original endpoint statement is preserved;
the additional fixed-theta statement extends the parameter scope and
explains exact cancellation within half-exactness. It starts no new D3
mechanism round and changes no signed positivity/order target.
