# PD-T?argmax-bridge-codex-N2-02 — Lower-order full-diamond profile target

ID kind: PD-T. Aliases: N2 B,C profile; polygonal interior transition.
Split from: IDEA-459's unchanged full-diamond profile obligation.
Split into: supporting exact reduction PD-T?argmax-bridge-codex-N2-01.

## Statement and definitions

For n>=2 put m=n+1, mesh product N=nm, and ell=n+1/2. Write
L=log ell and a=(cos alpha+cos beta)/2 on |alpha|+|beta|<=pi.
The requested model is

    M(alpha,beta,L)=(4/pi^2)*a*L^2+B(alpha,beta)*L+C(alpha,beta),
    R_n(alpha,beta)=S_n(alpha,beta)-M(alpha,beta,log(n+1/2)).

The target is to specify B,C explicitly (piecewise charts with compatible
transition formulas are allowed) and prove an explicit r(n) with
sup_diamond |R_n|<=r(n), small enough for B3. The coefficients and r(n)
are **not supplied by the current exact decomposition**. They remain
unknown functions in this target definition, and no fit has occurred.

## Assumptions and status

Overall status: **OPEN**. The exact row reduction is a supporting result,
not a conjunct of this target and not a reason to call it PARTIAL.

Dependencies: PD-T216/T364 for S, PD-T365 for the closed boundary and
PD-N132 for the obstruction to omitting the phase-dependent logarithm.
No external source theorem is used.

The exact n-dependent row sum has zero algebraic error; this does not
make it the requested degree-independent polynomial in L and does not
supply a B3 remainder bound. No inferred n1 or all-degree certificate.

## Required boundary data

On (alpha,beta)=(pi*t,pi*(1-t)), 0<t<1, T365 gives

    S_n=(sin(pi*t)/pi)*[2 log(2N/pi)+C_T365(t)]+error,
    |error|<=7/(12*N^2).

Since log N=2L+log(1-1/(4*ell^2)), the necessary boundary restrictions are

    B=4*sin(pi*t)/pi,
    C=(sin(pi*t)/pi)*[2 log(2/pi)+C_T365(t)].

At t=0,1 these extend to B=0,C=1. The conversion adds the explicit
remainder (2 sin(pi*t)/pi)*log(1-1/(4*ell^2)); retain it before taking an
absolute bound. Both signs of each phase use S's separate evenness.
These are inherited boundary restrictions, not newly solved interior data.

## Precise next obligation

Apply a regularized-cotangent sum formula to the at most four intervals
per row in N2-01. Bound the total error after multiplying by its explicit
row coefficients, including rows whose cutoffs coalesce with a cotangent
pole and every polynomial collision. B,C must match the boundary limits.
Pointwise Euler–Maclaurin error away from those transitions is insufficient.

## Checks, sources and history

No computation or fit is a premise. Gate: ../novelty-gate-N2.md.
Written 2026-11-05, Codex requested gpt-6.1-sol xhigh, input/rules
98d6c00d8a474cf97602c9cfdea631a837191ac0. Independent review pending.

## Provisional-label normalization — 2026-11-05

Coordinator normalized the provisional prefix to the handoff convention,
adding `codex` to the earlier `?argmax-bridge-N2-*` aliases.
Those earlier aliases remain historical references; no final ID, mathematical
statement, proof, executable source or run receipt changed.
