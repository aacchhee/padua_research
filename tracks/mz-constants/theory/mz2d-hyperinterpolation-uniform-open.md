# PD-T?mz2d-codex-32 — uniform signed Padua hyperinterpolation norm target

ID kind: PD-T. Aliases: endpoint signed operator stability; absolute-Gram
closure. Split from: D5 signed-hyperinterpolation question. Split into:
PD-T?mz2d-codex-30 (exact norm / finite bounds) and
PD-T?mz2d-codex-31 (correct reproduction/error estimate), both PROVED in
development. These supporting results do not settle this target.

Rules/base `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; 2026-11-01.
Codex xhigh allocation; runtime model metadata unexposed.

## Statement and definitions

With exactly the signed Padua coefficient operator in definitions.md and
PD-T?mz2d-codex-31, determine whether there is a finite constant C,
independent of integer `m>=2`, such that

\[
\|H_{m,m-1}\|_{C([-1,1]^2)\to L^2(dx\,dy)}\le C.
\]

If such a constant exists, obtain a useful explicit value or a quantitative
degree-dependent replacement. No Gram inverse, different measure, or
replacement of the signed weights defines the operator in this target.

## Status and candidate disposition

Overall status: **OPEN**; the actual-norm target is **deferred**. The two
uniform sufficient-majorant mechanisms considered in IDEA?mz2d-codex-33
are now **REJECTED: failed**, by
[PD-N?mz2d-codex-32](mz2d-hyperinterpolation-absolute-obstruction.md).
This disposition applies to those mechanisms, not to this target. Resume
with direct control of the exact weighted-L1 norm, a useful degree-dependent
bound, or another specified majorant that escapes the corner obstruction.

## Proven supporting reduction and its limits

PD-T?mz2d-codex-30 identifies the exact norm as

\[
\sup_{\substack{p\in\Pi_{m-1}\\\|p\|_2=1}}
\sum_{z\in\operatorname{Pad}_m}|w_z|\,|p(z)|
\le\sqrt{\tau_m\beta_{\rm abs}(m,m-1)}.
\]

The initially proposed sufficient routes were a uniform bound on
`tau_m beta_abs`, or uniform control of `delta_m`, signed
`lambda_+(m,m-1)`, and `chi_m=sum_(w<0)|w|K_(m-1)(z,z)`. The latter gives
the valid bound `sqrt((4+2delta_m)(lambda_++2chi_m))`. Both routes to an
m-independent endpoint constant fail: the actual negative corner gives

\[
\beta_{\rm abs}(m,m-1),\ \chi_m
\ \ge\ |w_c|K_{m-1}(c,c)=\frac16\log m+O(1)\to\infty,
\qquad\tau_m\ge4.
\]

PD-N?mz2d-codex-32 writes the precise inequalities and proof. It follows
that both sufficient majorants diverge; their degree-dependent inequalities
remain valid. Neither divergence establishes divergence of the actual
operator norm. Its single-corner weighted-L1 contribution is
`|w_c|sqrt(K_(m-1)(c,c))=O(log(m)/m^2)->0`.

The source-reported `tau_m->4` concerns a linear integration functional;
it does not control polynomial values in this norm. PD-N?mz2d-codex-30
refutes the general signed upper-Gram-only transfer. The actual target
remains unaffected by that generic counterexample.

Even a positive answer would not imply an E_(m-1)-only error estimate:
PD-N?mz2d-codex-31 proves exact endpoint reproduction stops at degree one.
Fixed-function convergence needs a separate aliasing analysis.

## Checks, sources, open items, history

No numerical experiment or asymptotic formula for the actual operator norm
is claimed. Literature coverage is recorded in literature.md. This target
preserves the unresolved uniform question after splitting off the proved facts, rather
than relabeling it PARTIAL. Independent audit remains pending for the
supporting records. 2026-11-01, Codex xhigh: first scoped D5 target record.
Supplementary response the same day: retained the target verbatim as OPEN
while recording the failed uniform majorants in PD-N?mz2d-codex-32.
