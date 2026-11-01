# PD-N?mz2d-codex-30 — a signed upper Gram bound does not control continuous data

ID kind: PD-N. Aliases: failed positive-rule transfer; signed constant-space
counterexample. Split from: IDEA?mz2d-codex-30. Split into: none.

Rules/base `cf89b140530d5838bdb208a8c28f3e7aa676ace3`; 2026-11-01.
Codex, allocated xhigh; runtime model metadata unexposed.

## Statement / negative-result scope

For every `t>1`, consider Lebesgue measure on `[-1,1]`, the three nodes
`-1,0,1`, and the signed quadrature

\[
Q_t(f)=t f(-1)+(2-2t)f(0)+t f(1).
\]

It is exact through degree one. On the constant space `Pi_0`, with
orthonormal basis `phi_0=1/sqrt(2)`, its signed Gramian is the scalar one.
Nevertheless its quadrature coefficient operator satisfies

\[
\|H_{t,0}\|_{C[-1,1]\to L^2(dx)}=(4t-2)/\sqrt2\longrightarrow\infty.
\]

Thus the estimate `||H||<=sqrt(V lambda_max(G))` cannot be extended from
positive to arbitrary signed quadrature, even with fixed nodes, exactness
through degree one, `eta=0` on the approximation space, and exact polynomial
reproduction. The attempted mechanism is precisely the positive-rule
Cauchy--Schwarz transfer of IDEA?mz2d-codex-30.

## Assumptions and status

Parameter range: all real `t>1`; degree-zero approximation; fixed
three-node signed rules above. Overall status: **PROVED** in development.
Candidate disposition: **REJECTED: refuted** for the stated general transfer.
No claim about divergence of the actual Padua operator is included.

## Proof

`Q_t(1)=2` and `Q_t(x)=0`, establishing the exactness. Moreover
`Q_t(phi_0^2)=Q_t(1)/2=1`, hence `lambda_max(G)=1` and `eta=0`.
The operator is the constant polynomial `H_(t,0)f=Q_t(f)/2`. Its L2 norm
is `|Q_t(f)|/sqrt(2)`. The triangle inequality gives
`|Q_t(f)|<=(4t-2)||f||_infinity`. Equality holds for the continuous function
`f(x)=2|x|-1`, whose nodal values are `1,-1,1` and whose sup norm is one.
This proves the formula. The positive-rule expression `sqrt(V lambda_max)`
is `sqrt(2)` and is exceeded for every `t>1`.

## Dependencies, sources and checks

Elementary exact arithmetic only; no external theorem or numerical run.
Closest positive predecessor: PD-T025, whose positivity hypothesis is
explicit and is not being refuted. The absolute-weight repair is
PD-T?mz2d-codex-30. D5 gate: ideas-d5.md. Independent audit pending.

## Scope and history

This is a scoped obstruction to an invalid inference, not a rejection of a
Padua norm theorem or an approximation family. 2026-11-01, Codex xhigh:
retained exact counterexample after the frozen constant-space kill test.
