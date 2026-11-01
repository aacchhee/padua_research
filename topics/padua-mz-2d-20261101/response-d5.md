# D5 response to the supplementary corner-majorant finding

Rules/base `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; 2026-11-01.
Developer: Codex, allocated xhigh; runtime model metadata unexposed.
This file responds only for D5. The orchestrator owns the combined campaign
response, Git operations, final IDs and shared registry updates.

## Finding and disposition

**Accepted.** The initial D5 records correctly proved finite-degree
absolute-weight norm bounds, but left two proposed uniform sufficient
majorants as merely unclosed. D3's subsequently available corner formula
shows that they cannot remain candidate routes to an m-independent endpoint
constant. This meaningful mechanism failure is now retained explicitly.

For either actual Padua node corner c,

\[
w_c=-\frac{4\log m+O(1)}{m^4},\qquad
K_{m-1}(c,c)=\frac{m(m+1)(m^2+m+1)}{24}.
\]

The absolute Gramian contains the positive rank-one summand
`|w_c|u_c u_c^T`, and the negative-leverage sum contains its trace. Hence

\[
\beta_{\rm abs}(m,m-1),\ \chi_m
\ \ge\ |w_c|K_{m-1}(c,c)=\frac16\log m+O(1)\to\infty.
\]

Together with `tau_m>=4` and signed `lambda_+(m,m-1)>=1`, this proves
divergence of both proposed sufficient majorants.

## Changes and preserved statements

- Added the scoped negative record
  [PD-N?mz2d-codex-32](../../tracks/mz-constants/theory/mz2d-hyperinterpolation-absolute-obstruction.md),
  with the exact rank-one proof and explicit rejected scope.
- Split [IDEA?mz2d-codex-33](ideas-d5.md) into the unchanged OPEN actual-norm
  target and its **REJECTED: failed** uniform absolute-Gram / bounded-negative-
  leverage mechanisms. Original question and former disposition are preserved
  in its history.
- Updated [D5.md](directions/D5.md) and the
  [uniform-norm target](../../tracks/mz-constants/theory/mz2d-hyperinterpolation-uniform-open.md)
  to record this failure and revised resumption criterion.
- PD-T?mz2d-codex-30's finite-degree norm theorem and
  PD-T?mz2d-codex-31's valid reproduction/error theorem were not changed or
  weakened. Both remain PROVED in development. The actual operator-norm
  target PD-T?mz2d-codex-32 remains **OPEN**, rather than being rejected or
  relabeled PARTIAL.

The divergence of the quadratic majorant does not establish divergence of
the exact operator norm, which uses the weighted L1 expression
`sup_(||p||2=1) sum |w_z| |p(z)|`. The supremum of the single-corner term
is `|w_c|sqrt(K_(m-1)(c,c))=O(log(m)/m^2)->0`. Direct weighted-L1 control,
a useful degree-dependent estimate, or another specified majorant remains
a possible resumption direction.

## Checks and audit status

Read the complete local corner-weight and corner-subtraction records
PD-T?mz2d-codex-20 / PD-N?mz2d-codex-21, and reconstructed the Legendre
endpoint sum, rank-one Rayleigh inequality, total-variation floor and
constant-polynomial Rayleigh floor. The proof is analytic; no numerical
execution or independent replay is claimed.

Supplementary Astra confirmed the proposed correction's scope before the
edit and was sent the final scientific-file hashes for focused review.
Focused review of those bytes is **PENDING** until its receipt arrives.
The required Claude audit remains **PENDING** regardless of this
supplementary review.
