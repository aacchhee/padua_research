# F08 — The actual two-sided entropy coefficient and diagonal endpoint limit

ID kind: PD-T; final allocation belongs to root.
Alias: PD-T?argmax-bridge-codex-F08-entropy-coefficients.
Split from: the coefficient-matching step of OPEN F08(T100).
Split into: none. Interior asymptotics below are not box-uniform remainders.

## Statement

Use exactly the generic J(u,s,e) and R=J-2(s-u)_+log(sine) of N1/C06.
For fixed u>0 and0<e*<pi/2, let v=s-u tend to0. Then

    J(u,u+v,e*)=|v|log|v|-(1+log(2u))|v|
                         +2v_+log(tan e*)+o(|v|).       (1)

For the registered CLOSED comparison box
(|alpha|,|beta|) in[1/10,1/4]^2, evaluate the actual central curves at
separate absolute phases, with a=(cos|alpha|+cos|beta|)/2>0.
On a coefficient-zero curve s_s(e*)=u with0<e*<pi/2, the derivative
kappa=s_s'(e*) is nonzero. Consequently the literal E12 B profile satisfies

    lim_(e->e*) [B_s(pi-e)-B_s(pi-e*)]
                    /[|e-e*|log|e-e*|]=|kappa|.        (2)

The limits use a FIXED phase. They are NOT declared uniform as e*
approaches0: the explicit regular coefficient2log(tan e*) in(1)
already records a nonuniform quantity requiring joint treatment.

There is a separate UNIFORM endpoint statement on the balanced diagonal.
For every c in[1/10,1/4], alpha=beta=c, a=cosc, and0<e<=1/64,

    |B_L(pi-e)-B_L(pi)-(a/2)e loge|<=10e,
    |B_R(pi-e)-B_R(pi)+(a/2)e loge|<=10e.              (3)

Thus the two endpoint logarithmic coefficients have opposite signs.
Unequal Q offsets and hole lengths prevent simply deleting them from
the actual paired operator. Statement(3) does not cover the full
off-diagonal transition in the ratio |alpha-beta|/h.

Status: **PROVED developer PAPER supporting result**, distinct review/
adoption pending. The full balanced-box K<=100 target remains OPEN.

## Proof of the interior coefficients

For s<u the accepted entropy branch is

    J=2[c0log(c0/u)+b0log(b0/u)],
    c0=(u-s)/2,b0=(u+s)/2.

Its derivative in s is log((u+s)/(u-s)). For s>u sufficiently close
to u at the fixed e*, the root branch applies. The accepted formula is

    J_s=2log(sine*)+log[(s cose*-D)/(s cose*+D)],
    D=sqrt(u^2-s^2sin^2e*).

Rationalizing uses (s cose*)^2-D^2=s^2-u^2. Therefore, on the two sides,

    J_s=-log(-v)+log(2u)+o(1)                        (v<0),
    J_s=logv-log(2u)+2log(tan e*)+o(1)               (v>0).

Integrating from J(u,u,e*)=0 proves(1). For an actual curve,
v=kappa(e-e*)+O((e-e*)^2), with |kappa|>0 by the accepted tan curves.
At fixed e* the separation derivative J_e is O(|v|) near the crossing:
on s<=u it is0, and on s>u rationalize R_e and add2v*cote*.
Thus changing e simultaneously changes(1) only by o(|v|).
The origin and logarithmic subtractions defining B_s are smooth at
this INTERIOR point. Scaling |v|log|v| proves(2).

This calculation keeps the same-sign and opposite-sign coefficients.
A single odd v log|v| prototype would have the wrong two-sided slopes.

## Proof of the uniform diagonal endpoint estimate

Let u=sin c/2 and w=a tan(e/2). On the stated diagonal,

    1/24<=u<=1/8, a>=31/32,
    0<w<=e<=1/64<u/2.

Use sin c>=5c/6 and cosc>=1-c^2/2 for these bounds. Near the endpoint
the actual parameters are s_L=u+w,s_R=u-w,d=0. The exact b terms in
F04's identity are b_L=0,b_R=-2w. Hence

    B_L(pi-e)=R(u,u+w,e)-qlog(pi-e),
    B_R(pi-e)=R(u,u-w,e)-2wlog(sine)+qlog(pi-e),       (4)

where q=sin c=2u. Both R limits at e=0 tend to0 along these curves.

Write H(u,s)=R(u,s,0), the EXACT N1 entropy limit. For0<w<=u/2,

    |H(u,u+w)-wlogw|<=4w,
    |H(u,u-w)-wlogw|<=4w.                            (5)

For the plus case use
H=wlog(w/2)+2u logu-(2u+w)log(u+w/2).
The derivative of xlogx has magnitude below3 on[u,u+w/2], since
x>=1/24 and x<=5/32. The non-wlogw terms cost at most
(3+log2)w<4w. For the minus case use
H=wlog(w/(2u))+(2u-w)log(1-w/(2u)); the two extra costs are
at most wlog12<3w and w, respectively.

F04's generic bound0<=R_e<=2s at fixed s implies
|R(u,s,e)-H(u,s)|<=2se<e for both s=u+/-w here. Thus

    |R(u,u+/-w,e)-wlogw|<=5e.                        (6)

Put k=a/2. On0<=x<=1/128, tan x<=2x and
tan x-x=integral_0^x tan^2t dt<=4x^3/3,

    |w-ke|<=e^3/6,
    |wlogw-ke loge|<=2e.                             (7)

For the second inequality, w/e lies in[a/2,a] inside[31/64,1],
so |log(w/e)|<1; also e^2log(1/e)<1. Similarly the sine Taylor bound
gives |log(sine/e)|<=e^2/(6-e^2), whence

    2|wlog(sine)-ke loge|<e.                          (8)

Indeed its upper is2[e/6+e/5]<e. Finally
q|log((pi-e)/pi)|<e. At the endpoint B_L(pi)=-qlogpi,
B_R(pi)=qlogpi. Substituting(6)--(8) in(4) costs at most8e
on the left and9e on the right, proving the safe common bound(3).

## Scope, first-test outcome and provenance

The singular coefficient is explicit and the endpoint pair is matched
with opposite signs, but(1)'s regular coefficient depends on the feature
location. The diagonal estimate(3) is uniform only on its stated local
domain; it is not a replacement for the full box. A complete F08 proof
still needs a joint off-diagonal/endpoint residual bound and all actual
fixed-cell/hole budgets. No positive feature separation or K<=100 is
inferred from these local formulas. No whole-target refutation is claimed.

Prospective F08 idea+attempt preceded ALL algebra, after full gate and
separate root release. These calculations are registered P1's actual
two-sided coefficient test. Only owned F08 prose changed. No source/
script/import/numerical/scalar/degree/endpoint/native/quadrature/build/
pack or shared/Git action.2026-11-07, requested Sol xhigh, serving
metadata unexposed; rules4a5de2012bad94601c713b2ff5517f2e3fb80af2.
F01/F04 and all original proofs remain frozen.


## Root disposition after distinct mathematical acceptance —2026-11-07

Root adopts the exact mathematical statement under its written quantifiers, hypotheses and dependencies. The original frozen proof/record prefix is preserved and identified in [independent review](../independent-checks-F08-F10.md), final SHA2561e63875c450d08f87b4b2b24934bf8baad67958f727b8df3e789998757db9d72. No global-onset change, new finite degree, source integration, strict runtime saving, novelty/priority verdict, protocol waiver or readiness follows beyond the exact statement. Final Claude review remains separate.
