# C01 near-model continuation

2026-11-06, rules/input `4b728b04216a5490910780bc609a82b853058426`.
Parent-assigned Codex Astra ultra; serving metadata unexposed. The parent
recorded the escalation before allocation. Only new C01-near files are owned.

The target remains Q_n-G_n<=1/40000 for every integer n>=10^6,
alpha,beta>=0, alpha+beta<=1/2. No new approximation model is introduced.
The first analytic test is the central positive-root integral in the candidate.
No mathematical computation, numerical integral, fit or energy extrapolation
has been run. All old proofs, source files and reviews remain unchanged.

The current useful identity is that, in N1-14's opposite-sign root regime,
the correction T=J-2s log(sin epsilon) satisfies

    T_epsilon = -2*sqrt(u²-s² sin² epsilon)/sin epsilon,
    T(u,s,arcsin(u/s))=0.

This gives a nonnegative integral majorant that also bounds the same-sign
regime. Its monotonicity permits an exact translation of the right folded
coefficient. The full Q_n comparison stays OPEN until all noncentral,
endpoint, finite-h and cutoff-corrected terms have their own phase bounds.

## Frozen outcomes

The central positive-integral argument is now proved in
theory/C01-near-central-upper.md, with the directional fractional coefficient
15/32 and explicit separate entropy terms. The actual limiting Q_n on the
alpha axis is proved in theory/C01-near-axis-limit.md to have coefficient
4*integral_0^1 sqrt(1-y^4)dy/pi². The scoped quadratic/entropy-only uniform
modulus obstruction is in theory/C01-near-quadratic-obstruction.md.
The distinct reviewer accepted these three frozen records at their stated
scopes. No numerical computation was run. The coordinator subsequently
authorized the separate C02/C03/C04 quantitative continuations, whose own
records retain their comparison scopes; this C01 record does not assert a
finite-degree conclusion from the limiting axis calculation.
