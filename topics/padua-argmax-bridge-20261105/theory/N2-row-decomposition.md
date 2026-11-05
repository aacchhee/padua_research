# PD-T?argmax-bridge-codex-N2-01 — Exact full two-phase cotangent rows

ID kind: PD-T.
Aliases: polygonal edge-direction reduction; moving sine-arc cutoffs;
full-diamond negative-part formula; negative collision correction.
Split from: supporting reduction for IDEA-459; its B,C target stays OPEN.
Split into: none.

## Statement

For every integer n>=2 the formulas (1)–(7) below reduce the corrected
primitive S_n on the entire closed phase diamond to cotangent partial
sums over explicit arcs, with finite polynomial collision terms. In
particular, on the generic first-quadrant domain

    alpha>=0, 0<beta<pi, alpha+beta<=pi,

each row's regular negative indices are specified by at most four arc
endpoints; its remaining collision values are explicit. The signed sum
over the whole odd board is exactly cos(alpha) after normalization.

All formulas extend to the closed diamond by evaluating the corrected
finite polynomial before taking a phase limit. The boundary reduction
agrees with PD-T365 including its two endpoint values 1. This is an
exact decomposition, not a lower-order asymptotic or a uniform error
estimate for a truncated model.

## Definitions and assumptions

Use m=n+1, N=nm, h_0=1,h_k=2 for k>0, and the finite polynomials

    D_n(u,v)=sum_{a+b<=n} h_a*h_b*cos(a*u)*cos(b*v),
    G_n(u,v)=D_n(u,v)-cos(n*u).

The (n,0) cosine coefficient in G is **one**. Let
Gamma^-={(j,r):0<=j<2n,0<=r<2m,j+r odd}. Put

    u_j=(j*pi+alpha)/n, v_r=(r*pi+beta)/m,
    Q_jr=(-1)^j G_n(u_j,v_r),
    S_n=(1/(2N))*sum_Gamma |Q_jr|,
    A=cos(alpha)+cos(beta), p=sin(alpha), q=sin(beta).

All statements use exact real arithmetic. The first-quadrant reduction
uses the separately even primitive S_n(alpha,beta), proved by reflecting
j or r in its finite sum. It does not exchange meshes or the exceptional
mode. Signed Q itself is not separately even pointwise.

## Status by part

Overall status: **PROVED** by the analytic derivation below; developer
claim, independent mathematical review and Claude audit pending.

| Part | Status | Evidence / limits |
|---|---|---|
| Full-domain signed rows and arc/collision reduction | PROVED | Finite algebra below |
| Closed-boundary compatibility | PROVED | Exact reduction to T365 |

The requested B,C profile/remainder is separately OPEN in
[N2-profile-target.md](N2-profile-target.md); it is not claimed here.
Candidate disposition: retained domain extension of IDEA-329/PD-T226.
The alternative CRT rewrite alone is equivalent to the inherited kernel.

## Depends on

PD-T185's divided difference D_n=[P_n(cos u)-P_n(cos v)]/(cos u-cos v)
with P_n=T_n+T_m, including its finite continuation. PD-T216's corrected
odd-board numerator and normalization. PD-T226 supplies the beta=0
predecessor, not an additional premise of the extension. PD-T365 supplies
the already proved boundary profile and CRT evaluation used for comparison.
No external source theorem or source proof is transferred.

## Proof

### 1. Two edge directions

For unequal cosines, the inherited numerator is

    Q=[A(1+cos v)-p sin u+q sin v]/(cos u-cos v).       (1)

Put s=(u+v)/2, t=(u-v)/2. Elementary sine subtraction gives

    Q=-(A/2)*(csc s*csc t+cot s*cot t+1)
          +(p-q)/2*cot t+(p+q)/2*cot s.              (2)

This is only an algebraic form of PD-T216. It shows the two polygonal
edge directions without splitting their absolute values. For example,
using CRT residue k=mj+nr modulo 2N and kappa=2n+1, define

    S_k=(pi*k+m*alpha+n*beta)/(2N),
    T_k=(pi*kappa*k+m*alpha-n*beta)/(2N).

Since mj-nr-kappa*(mj+nr)=-2N*(j+r), the csc product in (2) changes
sign on the odd board, whereas cotangents do not. Changing the residue
lift changes the signs of both csc factors together. Thus the equivalent
CRT bracket is (A/2)*(csc S_k*csc T_k-cot S_k*cot T_k-1), with the same
two linear cotangent terms. The map k is T365's odd-board bijection and
kappa^2=1 modulo 2N. This routine rewrite is not separately registered.

For a fixed generic row v=v_r in (0,2pi), v!=pi, an alternative grouping
is more useful. Define

    c_-(v)=(p-q-A*cot(v/2))/2,
    c_+(v)=(p+q+A*cot(v/2))/2.

Using

    (1+cos v)/(cos u-cos v)
        =-(cot(v/2)/2)*(cot((u-v)/2)-cot((u+v)/2)),
    sin u/(cos u-cos v)=-(cot((u-v)/2)+cot((u+v)/2))/2,
    sin v/(cos u-cos v)=-(cot((u-v)/2)-cot((u+v)/2))/2,

equation (1) becomes

    Q=c_-(v)*cot((u-v)/2)+c_+(v)*cot((u+v)/2).       (3)

The generic beta range ensures every v_r avoids 0,pi,2pi. Cotangent
poles at cos u=cos v remain actual polynomial collisions; do not
substitute zero times infinity in (3).

### 2. Signed rows and the exceptional mode

For row r put delta_r=1-r mod 2 and list the n first angles
u_k=(delta_r*pi+alpha)/n+2k*pi/n, 0<=k<n. All (-1)^j in the row equal
(-1)^delta_r. Finite Fourier summation kills x frequencies 1,...,n-1;
the constant frequency contributes n*D_n^(1)(v), and the exceptional
x frequency, whose coefficient is one, contributes n*(-1)^delta_r*cos alpha.
Consequently, with T_r=sum_k Q_kr,

    T_r=n*[(-1)^delta_r D_n^(1)(v_r)+cos alpha]
       =n*[A-q*cot(v_r/2)].                          (4)

Indeed D_n^(1)(v)=sin((n+1/2)v)/sin(v/2), and m*v_r=r*pi+beta gives
D_n^(1)(v_r)=(-1)^r*(q*cot(v_r/2)-cos beta). This proves (4) without
any division at an x/y collision. The corrected coefficient one is
essential: using the uncorrected D would add n*cos alpha to each row.

The elementary cotangent full-sum identity from T226, now with 2m
equally spaced angles, gives sum_r cot(v_r/2)=2m*cot beta. Therefore

    (1/(2N))*sum_Gamma Q_jr=cos alpha,
    S_n=cos alpha+(1/N)*sum_Gamma (-Q_jr)_+.           (5)

This identity is valid for generic beta and hence, because all finite
Q are continuous, for all phases. It is asymmetric in alpha/beta for
the correct reason: the exceptional mode is the x mode. It does not
assert a sign for the negative part or compare S with Lambda_c.

### 3. All regular signs from two elementary arcs

For a row let v*=min(v,2pi-v), and take angles u modulo 2pi. Define

    W(v)=A*(1+cos v)+q*sin v,
    D(v)={u:cos u<cos v}=(v*,2pi-v*),
    I(v)={u:W(v)-p*sin u<0}.

When p>0, I(v) is the sine superlevel arc sin u>W(v)/p. It is empty
if W/p>=1, the full circle up to possible zero endpoints if W/p<=-1,
and otherwise has endpoints asin(W/p) and pi-asin(W/p), taken modulo
2pi. When p=0 it is the full circle if W<0, and empty if W>=0;
when W=0 all regular Q in that row vanish. These conventions can
include/exclude zero numerators without affecting any sum.

For cos u!=cos v, equation (1) is negative exactly on
E(v)=D(v) symmetric_difference I(v), apart from its zero numerators.
There are at most four arc boundary points. Hence the negative indices
are consecutive grid blocks with explicitly known angular endpoints;
one needs no search for individual cardinal signs.

Write C_r for the collision indices and E_r for the regular grid indices
lying in E(v_r). Let R_r=sum_k |Q_kr|. The elementary equality
|x|=x+2*(-x)_+ yields

    R_r=T_r-2*sum_{k in E_r}[
         c_-(v_r)*cot((u_k-v_r)/2)
        +c_+(v_r)*cot((u_k+v_r)/2)]
           +2*sum_{k in C_r}(-Q_kr)_+,
    S_n=(1/(2N))*sum_{r=0}^{2m-1} R_r.                (6)

This is an exact absolute-row reduction. It is not a triangle-inequality
bound on separately signed edge factors.

### 4. Finite collision terms

On the generic domain sin v!=0. If u=epsilon*v modulo 2pi,
epsilon in {+1,-1}, then the divided-difference continuation gives

    Q_collision=(epsilon*n*p-m*q)/sin v-cos alpha.      (7)

To verify it, use G=P'_n(cos v)-T_n(cos v),
P'_n(cos v)=[n sin(nv)+m sin(mv)]/sin v,
sin(nv)=epsilon*(-1)^j*p, sin(mv)=(-1)^r*q and
(-1)^r=-(-1)^j. This proves (7) with no limiting error.
Unlike the beta=0 interior-collision value in T226, (7) need not be
positive. Omitting its negative part would make (6) incorrect.

At sin v=0 the generic formula is replaced by the finite polynomial.
For coincident cosine endpoints,

    G_n(0,0)=n^2+m^2-1=2N,
    G_n(pi,pi)=(-1)^n*2n,

and periodic/even representatives have the same values. Other endpoint
rows follow directly from the finite D. On beta->0, the r=0 signed
row in (4) has the finite limit n*[A-2m]; all other rows have limit n*A.
On beta->pi from below, the r=2m-1 row has limit n*[A+2m], and other
rows have limit n*A. These are limits of complete row expressions,
not permission to evaluate a separate singular cotangent factor.

### 5. Boundary, axes and vertices

If alpha+beta=pi with both phases strictly between 0 and pi, then
A=0 and p=q=sin alpha. Thus c_-=0,c_+=sin alpha and the complete
polynomial value is Q=sin alpha*cot((u+v)/2). T365 proves that its
argument never reaches a cotangent pole on this boundary and that its
odd-board CRT sum is exactly the shifted cotangent sum in T365 (3).
Every removable cos u=cos v collision agrees by the same continuous
polynomial identity. Formula (6) is merely |Q|=Q+2(-Q)_+ applied to
this identical boundary kernel, so it yields the same absolute sum.

At the boundary vertices alpha,beta=(pi,0),(0,pi), and their signed
counterparts, continuity of the finite polynomial sum gives exactly
S_n=1 by T365. There is no assignment of 0*cot(0) to zero. Separate
phase evenness gives the remaining three edges and all signs.

On beta=0, |alpha|<=2/5, c_-/2 and c_+/2 are exactly T226's A_v,B_v,
T_r/2=n*a for nonzero rows, and T_0/2=-n*(m-a). Its positive interior
collision formula is recovered from (7) where applicable, while the
endpoint row is evaluated polynomially. Thus the normalization and
exceptional mode agree with both predecessors.

## Checks and limitations

No computation is a proof premise. Executed developer command:
`python topics/padua-argmax-bridge-20261105/code/n2_rows.py`.
The [receipt](../evidence/n2-rows.json) pins code, mathematical sources,
Python/NumPy versions and the off-Git raw output. It checks 195 cases at
n=2,3,4,5,8,13,16, including 42 generic collision entries, 84 open-edge
phase cases on all four diamond edges, and 28 vertices. There were no
sign-arc disagreements. Maximum absolute errors were 1.31e-11 for signed
rows, 8.47e-13 for the reconstructed S, 3.17e-13 for collision values
and 1.61e-13 for the boundary sum. These are MEASURED binary64 agreement,
with no rigorous rounding bound; the analytic proof is the premise.
This is not an independent rerun or a computer-assisted proof.

The new exact information beyond the beta=0 predecessor is (4)'s
beta-dependent row, the full-domain arcs in (6), and signed collision
values (7). It isolates the unresolved asymptotic task: uniformly control
the cotangent partial sums when arc endpoints and poles approach each
other. It supplies no B,C, r(n), B3 pass, effective n1, complete cover
or extension of the certified range 2–32. PD-T099 remains OPEN.

## Sources and history

Internal gate: [novelty-gate-N2](../novelty-gate-N2.md).
No external fulltext or published proof has been used. Written 2026-11-05,
Codex requested gpt-6.1-sol xhigh; runtime metadata is not independently
exposed. Rules/input 98d6c00d8a474cf97602c9cfdea631a837191ac0.
Independent mathematical review and Claude audit pending.

## Provisional-label normalization — 2026-11-05

Coordinator normalized the provisional prefix to the handoff convention,
adding `codex` to the earlier `?argmax-bridge-N2-*` aliases.
Those earlier aliases remain historical references; no final ID, mathematical
statement, proof, executable source or run receipt changed.
