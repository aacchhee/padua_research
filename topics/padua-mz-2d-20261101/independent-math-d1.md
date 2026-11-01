# Supplementary analytic peer check by the D1 developer

Rules read at `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; unchanged after
the accepted main merge. Peer checker: Codex `/root/d1_aliasing`,
requested `gpt-6.1-sol` xhigh mathematical effort; serving model/effort
metadata is not independently exposed. Input working head:
`df44db49b407a26c55bb2229dc382255e66289df`.

This is a bounded supplementary review of **another developer's** D3
mathematics, requested by the orchestrator. It is neither a self-audit of
D1 nor the required Claude mathematical audit, which remains PENDING.
No D3 proof or candidate file was edited by the peer checker.

## Frozen scope and identities

| Record reviewed | SHA-256 | Claimed status |
|---|---|---|
| `tracks/mz-constants/theory/mz2d-lower-corner-weights.md`, PD-T?mz2d-codex-20 | `3c763e54a5758db7f444917c46d07312bc97c411f400b4c85f6a59af7232dc07` | PROVED analytic |
| `tracks/mz-constants/theory/mz2d-lower-corner-subtraction-obstruction.md`, PD-N?mz2d-codex-21 | `b7ebf2023118c2fbd2c492ff6318addee2802a3faad1244caed5db840705fcac` | PROVED scoped mechanism failure |

Read both records in full, the D3 direction/candidate records, the
accepted PD-T101 cardinal proof and the fixed definitions. The complete
registry gate and directly related MZ predecessor records were read in
D1 development; this peer check introduces no new mechanism or novelty
claim. A2's audit-pending corner asymptotics are not assumed.

## Findings

No mathematical error or scope overclaim was found in these two records
within this review. Both analytic proofs reconstruct correctly under the
stated even-checkerboard, signed `dx dy`, total-degree conventions.
This conclusion does not extend to an all-node sign classification,
positive definiteness, a leverage bound, or endpoint eigenvalue order.

## Independent reconstruction

At the two actual node corners, all even Chebyshev modes have value one.
Integrating accepted PD-T101's corrected cardinal kernel therefore gives

\[
 w_c=\frac1{2m(m+1)}
 \left(\sum_{i+j\le r}t_it_j-2h_m\right),\qquad
 t_0=2,\quad t_i=-4/(4i^2-1),\quad r=\lfloor m/2\rfloor.
\]

The corner set is correct: for even m only `(1,1),(-1,1)` have even
index parity; for odd m only `(1,1),(1,-1)` do. When m is even the
exceptional x-mode has value one at both corners, and when m is odd
its integral `h_m` vanishes. No corner-dependent sign was dropped.

The telescoping partial sum is `sum_(j=0)^q t_j=2/(2q+1)`. With
`N=2r+1`, the triangular convolution is

\[
 \frac4N-8\sum_{i=1}^r
 [(2i-1)(2i+1)(N-2i)]^{-1}.
\]

Independently combining the three displayed partial fractions yields
the numerator one. Their reciprocal sums are respectively
`S_r`, `S_r+1/N-1`, and `S_r`, because `N-2i` runs through the odd
integers `2r-1,...,1`. The coefficient of `S_r` in their combination
is `2/(N^2-1)`; the remaining constant is
`(N-1)/(2N(N+1))`. Substitution gives exactly

\[
 A_r=8/[N(N+1)]-16S_r/(N^2-1).
\]

For odd m>=3, `N=m` and the stated negative factorization follows
from `S_r>=1>(N-1)/(2N)`. For even m, the asserted weight numerator
is zero at m=2. At each even m>2, replacing `S_r` by one gives a
strictly negative upper bound: clearing the positive common
denominator reduces the comparison to
`16(m^2-1)>12m^2`, equivalent to `m>2`. Thus the claimed signs cover
all stated m and both parities. Finally
`S_r=H_(2r)-H_r/2=(1/2)log m+O(1)` gives
`w_c=-(4log m+O(1))/m^4` with the correct coefficient four.

For the scoped negative result, each corner Legendre value has squared
magnitude `(2a+1)(2b+1)/4`. The generating function for their cumulative
sum is `(1+z)^2/[4(1-z)^5]`. Its coefficient at `z^(m-1)` equals

\[
 \frac14\left[{m+3\choose4}+2{m+2\choose4}+{m+1\choose4}\right]
 =\frac{m(m+1)(m^2+m+1)}{24}.
\]

Multiplication by the proven corner-weight asymptotic therefore yields
the rank-one norm `(1/6)log m+O(1)`. All summands of the negative-weight
magnitude form are positive semidefinite, so it dominates this single
corner subform. A constant upper comparison by the continuous norm
would bound that corner norm by the same constant and is impossible.
This exactly refutes the stated **constant continuous-metric
subtraction** mechanism; it says nothing adverse about leverage in the
positive-node metric or the actual signed difference.

## Evidence and limits

This peer check is a written analytic reconstruction. Shell reads and
SHA-256 identity checks were performed; no numerical or exact-arithmetic
experiment is claimed by this checker. Independent finite regressions
from other workers remain separate evidence. The reported formulas
do not require those regressions for their all-m proofs.

Required Claude Opus 5.5 xhigh audit remains PENDING. Subsequent edits to
the hashed D3 files require impact review before inheriting this peer
check.
