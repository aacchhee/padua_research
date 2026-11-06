# PD-T?argmax-bridge-codex-N1-17 — Residual obligation for the near-edge model comparison

ID kind: PD-T. Aliases: C1 finite-part target; phase increment after exact
logarithmic subtraction. Split from: C1's near-model inequality.
Split into: supporting coefficient theorem N1-16, in
`N1-round7-coefficients.md`. The target itself is not PARTIAL: the
coefficient theorem is a supporting result, not a proved phase case.

## Exact target and status

Overall status: **OPEN**. For every integer n>=10^6 and every
alpha,beta>=0 with alpha+beta<=1/2, the target remains

    M_near(alpha,beta,log n)<=Lambda_c(n)+1/4096.       (C1)

M_near is exactly N1-15, including R128,delta1/1000, every retained
cutoff, H8 block, actual collision and polynomial endpoint value. No
new correction or alternative model is introduced. Separate phase
evenness extends the domain to |alpha|+|beta|<=1/2.

N1-16 proves its two explicit coefficients are no larger than the
corner coefficients, uniformly with negative quadratic phase gaps.
It also proves the residual below is uniformly bounded. It supplies
no small bound or phase modulus for that residual; (C1) is unproved
at general phase and no argmax onset is asserted.

## Exact remaining function

Use B_M,b_M,B_c,b_c of N1-16 and L=log n. Define functions, without
changing any summand of M_near,

    R_n(alpha,beta)=M_near(alpha,beta,L)-B_M L^2-b_M L,
    F_n(alpha,beta)=R_n(alpha,beta)-R_n(0,0),
    G_n(alpha,beta)=(B_c-B_M)L^2+(b_c-b_M)L,
    eta=1/4096-3/14000=107/3584000.

Since the exact primitive has S_n(0,0)=Lambda_c(n), N1-15 already gives

    M_near(0,0,L)-Lambda_c(n)<3/14000.

The exact identity

    M_near(alpha,beta,L)-Lambda_c(n)
      =M_near(0,0,L)-Lambda_c(n)+F_n(alpha,beta)-G_n(alpha,beta)

shows that the explicit sufficient next obligation is

    F_n(alpha,beta)<=G_n(alpha,beta)+eta.               (R)

N1-16 gives the usable lower bound

    G_n>=A(L)*(alpha^2+beta^2),
    A(L)=47L^2/(48pi^2)+L/(24pi^2).                   (1)

Thus the bounded finite part is now a specific function F_n with all
normalizations/cutoffs fixed, rather than an unspecified asymptotic
constant. Its exact finite-count formula is obtained by subtracting
the two displayed polynomial terms from N1-15(4). This algebraic
identity is not a new approximation or model family.

## Cheapest proposed next bounded test — not executed

Before an expensive validated cover, try to prove, on the same n/phase
domain, a finite-part increment estimate with explicit constants

    F_n(alpha,beta)<=K0*(alpha^2+beta^2)
                       +c(n)*(alpha+beta)+J(n).       (2)

Every actual cutoff/collision transition must be included. J(n)>=0
would be a proved total allowance for model jumps or other discrete
boundary changes, not a tolerance inferred from samples. A continuous
formula or a differentiation argument cannot simply omit those changes.
The finite endpoint rows, central special rows and their ordinary-cell
replacements are the cheapest places to test (2), before differentiating
the full integrals. This is a possible continuation, not a preregistered
new round or a claimed estimate.

If K0<A(L0), L0=log(10^6), then rho^2<=(2r2) and completing the
square give the purely algebraic sufficient condition

    J(n)+c(n)^2/[2(A(log n)-K0)]<=eta                 (3)

for every n>=10^6. This turns any proved modulus into a concrete
budget test. A larger onset requires an explicit proof of its own
threshold; no threshold is supplied here. If (2) has a negative
right-hand denominator in (3), that certificate is inadequate at
that degree; it does not refute (C1).

There is an existing precise warning against setting c(n)=0 for an
exact-primitive version of (2): PD-T220 proves its alpha-axis cusp
coefficient

    ell_n=[n(n+1)]^-1 sum_(j=1)^floor(n/2) cot(j*pi/n)>0
    for n>=3,
    ell_n<=H_floor(n/2)/[pi(n+1)].                    (4)

The logarithmic coefficients subtracted here are smooth and even, so
they do not remove that finite-n linear cusp. The bound in (4) is
O(log n/n), which may fit (3); it is not an obstruction to retaining
a small explicit linear allowance. Formula (4) does not by itself
prove the two-phase estimate (2) for the actual model, whose H8/floor
choices may also have finite discontinuities.

An alternative sufficient target is the exact-primitive inequality
S_n-Lambda_c<=eta: adding N1-15's uniform model error would imply
(C1). That alternative avoids model-enumeration jumps, but its exact
finite-n cusp still requires the retained linear allowance. Merely
using the existing uniform model error twice would cost6/14000,
larger than eta, and cannot prove (R).

Kill tests for a future bounded round: a coefficient/formula mismatch,
a phase modulus that misses (4), an uncharged cutoff jump, or a proved
leftover J/c budget exceeding eta kills only that proposed finite-part
certificate. A numerical phase reversal greater than eta would be a
MEASURED steering observation until independently enclosed. None is
a counterexample to PD-T099. No such test has yet been executed.

## Checks, limits and history

No numerical model value, integral, finite-part sample, fit or derivative
estimate was computed in round7. Its only pilot was the separately
recorded n17/24/32 primitive/corner normalization. That does not use
M_near below its validity domain. The finite energy range2–128 has
not been extrapolated to n>=10^6. Far phases, true-corner coherence,
other center classes, global2–40 and B3/B4 statuses are unchanged.

2026-11-06, input/rules `8dc1521cf68f7780bd10e02495f6f71a639c03c6`.
Codex mathematical worker, inherited model/effort; serving metadata
unexposed. The coordinator requested the exact remaining-function
contract and a cheap prospective kill test, with no next round launched.
