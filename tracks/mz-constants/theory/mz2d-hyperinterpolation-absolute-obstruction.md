# PD-N052 — uniform absolute-Gram and negative-leverage majorants fail

Provisional alias: `PD-N?mz2d-codex-32`. Final ID assigned at PR preparation, 2026-11-01; required Claude audit PENDING.

ID kind: PD-N. Aliases: endpoint absolute-Gram divergence;
negative-corner leverage obstruction; failed uniform D5 majorants.
Split from: the sufficient uniform-majorant mechanisms of
IDEA-222. Split into: none. The actual operator-norm target
PD-T114 remains OPEN and is not rejected.

Rules/base `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; 2026-11-01.
Codex mathematical worker, allocated xhigh; runtime model metadata unexposed.
Written in response to the supplementary Astra finding, after D3's corner
formula became available. Independent focused review pending.

## Statement

Use the actual even-checkerboard signed Padua rule, unnormalized measure
`dx dy`, and endpoint degree `n=m-1`, with integer `m>=3`. Retain the
definitions from PD-T112:

\[
A_m=B^T\operatorname{diag}(|w|)B,\quad
\beta_{{\rm abs},m}=\lambda_{\max}(A_m),\quad
\tau_m=\sum_z|w_z|,\quad
\chi_m=\sum_{w_z<0}|w_z|K_{m-1}(z,z).
\]

Fix either node corner c, and set

\[
s_m=|w_c|\,\frac{m(m+1)(m^2+m+1)}{24}.
\]

Then, over both parities,

\[
\beta_{{\rm abs},m}\ge s_m,\qquad
\chi_m\ge s_m,\qquad
s_m=\frac16\log m+O(1)\longrightarrow\infty. \tag{1}
\]

In particular `tau_m>=4` and

\[
\tau_m\beta_{{\rm abs},m}\ge4s_m\longrightarrow\infty. \tag{2}
\]

Thus the sufficient strategy of proving a uniform bound on
`tau_m beta_abs(m,m-1)` cannot establish a uniform endpoint operator norm.
Likewise a uniformly bounded negative-leverage estimate cannot hold.
More explicitly, the negative-leverage majorant from
PD-T112 itself diverges:

\[
\sqrt{(4+2\delta_m)(\lambda_+(m,m-1)+2\chi_m)}
\ge\sqrt{4(1+2s_m)}\longrightarrow\infty. \tag{3}
\]

These are failures of the **uniform sufficient majorants**, not failures of
their valid degree-dependent upper-bound inequalities, and not divergence
of the actual `C->L2` operator norm.

## Assumptions, status, and negative-result scope

Overall status: **PROVED** in development. Candidate mechanism disposition:
**REJECTED: failed**, precisely for obtaining a finite m-independent
endpoint constant through bounded `tau_m beta_abs`, or through bounded
negative leverage `chi_m`. Degree-dependent estimates remain admissible.
The parameter range is the endpoint `n=m-1`, all sufficiently large m,
with inequalities (1)--(2) valid for every `m>=3`.

The underlying question whether `sup_m ||H_(m,m-1)||_(C->L2)` is finite
remains PD-T114, **OPEN**. This negative record does not decide
that question, any fixed-ratio operator bound, or the signed MZ spectrum.

## Depends on

PD-T111, the exact corner weights and
`w_c=-(4 log m+O(1))/m^4`, negative at both node corners for every `m>=3`.
PD-N048 supplies the continuous corner evaluation calculation;
its elementary finite sum is also repeated below. These are local analytic
results, not mathematical claims imported from an unread source.

## Proof

Let `u_c=(ell_a(c_1)ell_b(c_2))_(a+b<=m-1)` be the vector of the
continuously orthonormal Legendre basis values. Since
`P_a(1)=1`, `P_a(-1)=(-1)^a` and
`ell_a=sqrt((2a+1)/2)P_a`,

\[
K_{m-1}(c,c)=\|u_c\|_2^2
=\frac14\sum_{a+b\le m-1}(2a+1)(2b+1)
=\frac{m(m+1)(m^2+m+1)}{24}. \tag{4}
\]

For example the sum follows by taking the coefficient of `z^(m-1)` in
`(1+z)^2/(1-z)^5`, which is
`binom(m+3,4)+2 binom(m+2,4)+binom(m+1,4)` before division by four.

Every summand in A_m is positive semidefinite, so

\[
A_m\succeq |w_c|u_cu_c^T.
\]

Evaluate its Rayleigh quotient at `u_c/||u_c||_2` to obtain
`beta_abs>=|w_c| ||u_c||_2^2=s_m`. Because `w_c<0`, the corner contribution
is included in the nonnegative sum defining chi, giving `chi>=s_m`.
Combining (4) with the corner-weight asymptotic gives
`s_m=(log m)/6+O(1)`, proving (1).

The rule has `sum_z w_z=4`; hence `tau_m>=4`, and (2) follows. For (3),
the constant polynomial `1/2` has continuous L2 norm one and its signed
quadrature square equals one. Therefore `lambda_+(m,m-1)>=1`. Also
`delta_m>=0`. Substitute these inequalities and `chi_m>=s_m` in the
majorant to obtain (3).

To separate this obstruction from the actual operator norm, recall its
exact formula in PD-T112 has **one** power of `|p(z)|`.
The single-corner contribution to its supremum is instead

\[
|w_c|\sqrt{K_{m-1}(c,c)}
=O\!\left(\frac{\log m}{m^2}\right)\longrightarrow0.
\]

Thus the rank-one quadratic-form divergence does not supply an operator
norm divergence. Direct control of the weighted L1 expression, or another
specified majorant, remains outside the rejected uniform routes. ∎

## Checks, scope, history

The proof is analytic; no numerical execution or finite regression is
claimed. The dependency corner formula and the continuous Legendre endpoint
calculation were read in full. Supplementary Astra identified this failure;
the D5 developer reconstructed the proof and requested focused review.
Required Claude audit remains pending. 2026-11-01: split the failed uniform
majorants from the unchanged OPEN actual-norm target and unchanged valid
degree-dependent D5 theorems.
