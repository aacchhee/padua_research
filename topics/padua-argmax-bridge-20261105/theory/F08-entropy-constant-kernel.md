# F08 — Exact translated entropy midpoint and hole moments

ID kind: PD-T; final allocation belongs to root.
Alias: PD-T?argmax-bridge-codex-F08-entropy-kernel.
Split from: supporting local-kernel obligation of OPEN F08(T100).
Split into: none. These are prototype estimates, not a whole B-profile bound.

## Statement and definitions

Let f_r(x)=|x-r|log|x-r| with0log0=0 and

    P(y)=(y^2/2)logy-y^2/4 for y>0, P(0)=0.

For every h>0 and cell I=[c-h/2,c+h/2] put
M=h f_r(c)-integral_I f_r(x)dx and theta=(r-c)/h.
If |theta|<=1/2, then EXACTLY

    M=h^2[A(theta)logh+B(theta)],
    A(theta)=-(1/2-|theta|)^2,
    B(theta)=|theta|log|theta|
                        -P(1/2+theta)-P(1/2-theta).     (1)

In particular, uniformly through a root on the sample or cell boundary,

    |M|<=h^2[(1/4)|logh|+1/2].                        (2)

If r is outside the cell (including its endpoints by continuity),

    |M|<=h^2[(log2)/2-1/4]<h^2/8.                    (3)

The logarithmic coefficient1/4 in(2) is sharp as h decreases to0,
already at r=c. No feature separation is assumed.

For a hole[0,ell],0<ell<=1, define
E=integral_0^ell[f_r(x)-f_r(0)]dx. If r=ell*zeta with0<=zeta<=1,

    E=ell^2[A0(zeta)logell+B0(zeta)],
    A0(zeta)=(1-zeta)^2-1/2,
    B0(zeta)=P(zeta)+P(1-zeta)-zeta logzeta,
    |E|<=ell^2[(1/2)|logell|+1/2].                    (4)

For every r in[-pi,pi], including exterior roots approaching the hole,

    |E|<=ell^2[(1/2)log(1/ell)+5/2].                  (5)

The coefficient1/2 is sharp at the endpoint r=0. Exact moments for
arbitrary r are also given by the continuous primitive
sgn(x-r)P(|x-r|), followed by subtraction of ell*f_r(0).

Status: **PROVED developer PAPER support**, distinct review/adoption
pending. F08(T100) stays OPEN: its actual coefficients and residual
must still be charged uniformly on the entire balanced box.

## Proof

Set x=c+hy. For an interior root,

    integral_(-1/2)^(1/2)|y-theta|dy=1/4+theta^2,
    integral_(-1/2)^(1/2)|y-theta|log|y-theta|dy
                           =P(1/2+theta)+P(1/2-theta).

Scaling gives(1). On[0,1], P decreases from0 to-1/4 because
P'(y)=ylogy<=0. Also -1/e_Euler<=ylogy<=0, and e_Euler>2.
Thus B lies between-1/e_Euler and1/2, and |B|<=1/2. Since
-1/4<=A<=0, this proves(2). At theta=0,A=-1/4, establishing
sharpness of the logarithmic coefficient.

If r lies strictly outside I, f_r''(x)=1/|x-r|>0 on I.
The centered midpoint Peano kernel is nonnegative for the integral
minus the midpoint value. Increasing the distance of an exterior r
decreases this second derivative pointwise, so the absolute midpoint
error is maximized as r approaches the nearer cell endpoint.
The exact moment is continuous in r, and(1) at theta=1/2 gives
M=h^2[1/4-(log2)/2]. Hence(3), also on the left by reflection.
The inequalities1/2<log2<3/4 follow by comparing the integral of1/x
on[1,2] with the constant1/2 and the strict convex trapezoid upper3/4.
This argument uses smooth exterior roots followed by the exact limit;
it assumes no globally finite derivative variation across the root.

For the hole set x=ell*y. Direct integration gives

    integral_0^1 |y-zeta|dy=[zeta^2+(1-zeta)^2]/2,
    integral_0^1 |y-zeta|log|y-zeta|dy=P(zeta)+P(1-zeta).

Subtracting f_r(0) gives(4). Here |A0|<=1/2 and
P(zeta)+P(1-zeta) is in[-1/2,0], while
-zeta logzeta is in[0,1/e_Euler]. Thus |B0|<=1/2.
At r=0 the moment is P(ell), which proves sharpness of1/2.

It remains to justify uniform exterior-hole bound(5). On a one-sided
exterior branch, absolute continuity gives

    |E|<=integral_0^ell(ell-x)|f_r'(x)|dx.

All distances |x-r| are at most2pi, whose logarithm is below2.
For r<=0, |x-r|>=x; for r>=ell, |x-r|>=ell-x. Consequently

    |f_r'(x)|<=3+log(1/x)                 (r<=0),
    |f_r'(x)|<=3+log(1/(ell-x))           (r>=ell).

The two resulting elementary integrals are bounded, respectively, by

    ell^2[(1/2)log(1/ell)+9/4],
    ell^2[(1/2)log(1/ell)+7/4].

Together with(4), these imply(5). Endpoint equalities follow from
the continuous exact primitive. No quadrature measurement was used.

## Scope and provenance

The prototype is TWO-SIDED |x-r|log|x-r|; replacing it by xlog|x|
would lose the nonzero centered-root logarithmic term. These exact
moments can be used only after the actual B profiles' singular
coefficients and residual are matched. They do not by themselves
give K<=100, a root-separation theorem, or an onset improvement.

F08 idea+attempt were written before ALL F08 algebra, after completed
gate and separate root release. This is registered P1's first local
test. PAPER hand algebra/prose only, no scripts/imports/numerical/
scalar/degree/endpoint/native/root/quadrature/build/pack jobs or shared/
Git edits.2026-11-07, requested Sol xhigh, serving metadata unexposed;
rules4a5de2012bad94601c713b2ff5517f2e3fb80af2. F04 remains frozen.


## Root disposition after distinct mathematical acceptance —2026-11-07

Root adopts the exact mathematical statement under its written quantifiers, hypotheses and dependencies. The original frozen proof/record prefix is preserved and identified in [independent review](../independent-checks-F08-F10.md), final SHA2561e63875c450d08f87b4b2b24934bf8baad67958f727b8df3e789998757db9d72. No global-onset change, new finite degree, source integration, strict runtime saving, novelty/priority verdict, protocol waiver or readiness follows beyond the exact statement. Final Claude review remains separate.
