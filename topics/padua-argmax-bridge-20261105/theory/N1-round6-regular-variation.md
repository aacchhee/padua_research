# PD-T?argmax-bridge-codex-N1-13 — Uniform regular-profile variation

ID kind: PD-T. Aliases: global folded coefficient variation; regularized
pole-numerator variation. Split from: round-6 outer compactification.
Split into: none. The cancellation integral is a separate component.

## Statement

Let alpha,beta>=0, alpha+beta<=1/2 and use a,p,q,ce,cd,U0,Phi0,A,
eta_-,eta_+ from N1-05. For s=L,R put v_L(z)=z,v_R(z)=2pi-z and

    N_s(z)=ce Phi0(eta_-(v_s(z)))+cd Phi0(eta_+(v_s(z))),
    f_s(z)=A(v_s(z))-4a/(pi*z),
    P_s(z)=N_s(z)/[2sin(z/2)]-U0/z.

Take the continuous extensions at z=0. On 0<=z<=pi,

    ||f_s||_infinity<3/5,
    Var(f_L)+Var(f_R)<6/5,
    ||P_s||_infinity<6,
    Var(P_L)+Var(P_R)<23.                              (1)

For any unions of actual centered cells of width h=pi/m contained in
the two folded halves, with their center samples, midpoint quadrature
for L*f_s+P_s after normalization 1/m therefore has total error at most

    [(6/5)*L+23]/(2m).                                (2)

For L=log n,m=n+1,n>=10^6 this is less than 1/50000. The cell unions
may have holes; the total variation is not multiplied by their count.
No replacement of the actual cell boundaries is part of (2).

## Status and dependencies

Overall status: **PROVED**, analytic developer proof; independent review
pending. N1-04 supplies the periodic regularized Phi0 and its Lipschitz
bound, N1-06 the exact max formulas, and N1-10 the local differentiated
series estimates. The existing endpoint_check child developed this
bounded piece under the round-6 preregistration. No external theorem,
mathematical computation or fit is used.

## Proof

The elementary identities from N1-06 remain exact for all 0<z<=pi:

    A_L=max(p,q+T)/pi, A_R=max(p,|q-T|)/pi,
    T=2a cot(z/2), u=T-4a/z,
    pi*f_L=max(q,p-T)+u,
    pi*f_R=max(-q,p-T,q-2T)+u.

The max terms increase while u decreases from zero to -4a/pi.
The same monotone-piece estimate used there now gives

    sum_s Var(f_s)<=2max(p,q)/pi+8a/pi^2,
    ||f_s||_infinity<=max(p,q)/pi+4a/pi^2.

With max(p,q)<=1/2,a<=1 and pi>31/10 these imply the first two
bounds in (1).

N1-10's differentiated R(t) series and sinc estimate hold throughout
0<t<=1/2, not merely its smaller stated use interval. Reflection thus
gives |Phi0''|<35 on every open period. The derivative has jump
2(2gamma-2log pi) at an integer, with magnitude below 6. Each argument
eta traverses half a period, so it encounters at most one such jump.
The already proved sup/Lipschitz bounds and this derivative variation
give, for each folded numerator,

    ||N_s||_infinity<=8, Lip(N_s)<=12/pi,
    Var(N_s)<=12, Var(N_s')<=47/(2pi).                 (3)

For the last inequality, each composed derivative contributes at most
[(35/2)+6]/(2pi)=47/(4pi), and ce+cd<=2. Endpoint one-sided values
and jumps are included in derivative variation.

Put d0(z)=1/[2sin(z/2)]-1/z. It increases from zero to 1/2-1/pi.
Indeed its derivative is nonnegative precisely when
sin^2 x>=x^2 cos x, x=z/2. The derivative of the difference is
x^2 sin x-2cos x*(x-sin x), nonnegative by
sin x>=2x/pi, x-sin x<=x^3/6 and 2/pi>1/3 on [0,pi/2].
Write exactly

    P_s(z)=[N_s(z)-N_s(0)]/z+N_s(z)*d0(z).

The first term equals integral_0^1 N_s'(tz)dt. Its variation is at
most Var(N_s'), by the variation definition followed by integration.
The product variation inequality for the second term and (3) imply

    Var(P_s)<=47/(2pi)+20*(1/2-1/pi)=10+7/(2pi),
    ||P_s||_infinity<=12/pi+8*(1/2-1/pi)=4+4/pi<6.

The combined variation is below 23. The endpoint limits are +U1 and
-U1 from N1-10. This proves (1), including zero phases without an
inverse phase-distance constant.

For a BV function on a centered cell, the sample minus its cell mean
has magnitude at most half its variation. Sum over the disjoint cells
and divide by m; their variations sum to at most the whole-half
variation. This gives (2). Its scalar bound follows from log(10^6)<14
and monotonicity of [(6/5)log n+23]/(n+1) for n>=10^6.

## Scope and history

This supplies a degree-uniform quadrature error for the two regular
pieces. It does not bound the cancellation integral, central logarithm,
singular harmonic term or special-row evaluation. Their additional
errors must be included before the round-6 target can pass.
2026-11-06 after 88e7023, requested gpt-6-astra ultra. Candidate:
../ideas/N1-round6.md. Previous frozen proofs remain unchanged.
