# E04 defect support — Rebuilt projected floors through actual radius one

Provisional PD-T?argmax-bridge-codex-E04-defect. Aliases: shortpi10
positive middle band; radius-one noncorner projection. Split from the
fixed640 assembly; this is a separate substantive support theorem.

## Statement and status

For EVERY integer n>=64,m=n+1, physical odd center0<=J<=n,
0<=K<=m,J+K odd, and every ACTUAL admissible signed phase with

    theta=(J*pi+alpha)/n in[0,pi],
    phi=(K*pi+beta)/m in[0,pi], rho=|alpha|+|beta|<=r<=1,

use the corrected PD-T101/364 finite kernel, exceptional top x-mode
coefficient ONE, original endpoint weights and actual polynomial
collision values. Put p=22/7,a=1-r^2/4 and

    eta_n(r)=a*[1-(4p+r)/n]-r/2,
    Fn(r)=[2eta_n(r)/(p+r)]*[n/(n+1)]*(1/4-1/n),
    Fs(r)=(35/286)*(1-6/n)^2*(a-r/2),
    A0(r)=97a/100-r/2,
    It(r)=1163a/5000-1413r/10000,
    Rt(r)=11087a/5000-5r/4,
    Ft(r)=(539/1936)It(r)-140A0(r)/(157n)
                       -400Rt(r)/(157n)-800A0(r)/(3n^2).
                                                               (1)

Each applicable projection satisfies

    Q_v(K)>=min(Fn,Fs,Ft) if0<K<m,
    Q_h(J)>=min(Fn,Fs,Ft) if0<J<n.                  (2)

For EVERYn>=640 on the FULL actualrho<=1 domain these improve to

    Q_v(K)>1/200, Q_h(J)>1/200 where applicable,
    Delta_JK>1/200 at every NONCORNER odd center.    (3)

Status: **PROVED developer PAPER theorem**, distinct review required.
No global640 or primitive upper comparison is claimed. The minimum in
(2) is permitted to be negative for some small n; (3) is separately
proved at its own onset. Actual corners are excluded. Projections are
not added; Delta>=max(Q_h,Q_v)>=0 is the full exact defect relation.

## Exact normalization and the new domain checks

Use C02/E01's SAME full periodic definition with factor1/(4nm) and
pair deficit d(X,Y)=|X|+|Y|-|X+Y|. Folding reflected preimages
gives coefficient1/(nm) for each selected INTERIOR physical row;
BOTH opposite periodic branches are explicitly counted. Original
endpoint half weights remain in the full projection. Omitting other
terms, including polynomial collision terms, is legal by nonnegativity.

At regular selected denominators the common-sign half kernel is

    H(u,v)=A(u,v)/(cosu-cosv),
    A=a_actual(1+cosv)-(sin alpha/2)sinu+(sin beta/2)sinv,
    a_actual=(cos alpha+cos beta)/2>=1-r^2/4=a,
    (|sin alpha|+|sin beta|)/2<=r/2.                 (4)

This inequality is valid through r=1 by the same cosine/sine Taylor
inequalities, not by transferring an old half-radius theorem. The
horizontal baseline stays the ACTUAL fixed1+cosv. No n,m swap is made.

For either projection let M,L be its adjacent physical/periodic meshes
(m,n vertically; n,m horizontally), and gamma the actual center-angle
distance from the nearest endpoint. M,L>=n and M/L<=65/64. The
two physical cosine targets at b=l*pi/M are z0+/-D, with
z0=cosgamma*cosb>=0,D=singamma*sinb. The three center classes below
are exhaustive for every applicable interior coordinate.

## Nearest four center-index distances

For1<=s<=4 choose the SAME rows M/4<=l<=M/2 and offsets
q=-(s-1),-(s-3),...,s-1, with indices l+q and2L-(l+q).
Parity and distinctness are literal integer facts from C02: l+q>=13,
l+q<=M/2+3<L; negation preserves parity, and top reflection changes
the physical row as before. The mesh estimate is

    |M(w-b)|<=(s-1)pi+71pi/128+(65/64)|periodic_phase|.

Its sufficient straddling condition now holds because

    |physical_phase|+(65/64)|periodic_phase|
           <=65/64<57pi/128,

usingpi>3. Thus all selected angles are strictly between the two
physical targets; no selected denominator is zero. With
t<=(s*pi+r)/M, one has t<=(4pi+1)/64<pi/4, so all row angles
remain inside(0,pi). The selected targets vertically, and the fixed
periodic cosine horizontally, are>=-t. Each numerator is>=eta_n(r)>0.
For alln>=64,r<=1,

    eta_n(r)>= (3/4)*(1-95/448)-1/2
                         =163/1792>0.             (5)

The denominator span is at most2t and each pair deficit is at least
eta_n(r)/t. Count s offsets, TWO branches and at least M/4-1 rows.
Exactly as a new radius-one calculation,

    Q>=[2s eta_n(r)/(s*pi+r)]*(M/L)*(1/4-1/M)>=Fn(r).

Every substituted factor is positive. Original endpoint weights were
never absorbed into the two-branch count.

## Remaining small center angles: matched count and numerator

For s>=5, gamma>4pi/L follows from L(pi-r)>4pi. It is valid at
r<=1,L>=64 because60pi>64. For gamma<pi/6 take physical rows
b in[pi/6,pi/3] and the two reflected OPEN periodic arcs
(b-gamma,b+gamma). They are disjoint and inside their half-circles.
Both numerator baselines in(4) are>=1+cos(pi/3+gamma). Put

    A_gamma=a[1+cos(pi/3+gamma)]-r/2>0,
    h(g)=A_g*(1-pi/(Lg)).

The physical count is M/6-1; periodic count is2Lgamma/pi-2;
pair deficit is at least2A_gamma/(sqrt3 gamma). Therefore

    Q>=[4/(pi sqrt3)]*(1/6-1/M)*h(gamma).

On[4pi/L,pi/6], A>0,A'<0,A''<=0, so
h''=A''(1-c/g)+2A'c/g^2-2Ac/g^3<0,c=pi/L.
The endpoint comparison, STILL valid at r<=1, is

    h(4pi/L)-h(pi/6)
       >=[1/8+(6-3pi)/L]a+[1/8-3/L]r>0.

Both coefficients are positive fromL>=64,pi<22/7; the larger radius
does not change their signs. Thus h>=h(pi/6)=(a-r/2)(1-6/L).
Usepi<22/7,sqrt3<26/15 and M,L>=n to get EXACTLY Fs(r).
This is the radius-one reconstruction of the concavity proof, not an
application of a half-radius small-angle bound. The seamgamma=pi/6
belongs to the middle case, with continuous endpoint lower estimates.

## Middle center angles: the NEW short positive band

For gamma>=pi/6 choose

    a0=pi/100, b0=pi/10, c=2, Tcap=4log2,
    C=a-r/2, A(b)=C-a sinb.

The central new positivity check is

    sin(pi/10)<5/16,
    A(b)>(11/16)a-r/2>=1/64>0.                   (6)

Indeed sin(pi/10)=(sqrt5-1)/4 and sqrt5<9/4 by80<81.
This is why the old wider physical bands cannot simply be used at r1.
A and A/sinb are positive/decreasing on this band. Keep the capped
reciprocal pair function A(b)/D*min(2,2/(1+|x-z0|/D)) on the open
cosine interval between the targets. Its cosine-coordinate integral
is Tcap*A(b), its maximum2A(b)/D. The two parity arcs lose at most
one point EACH; the finite physical row sums lose their first value.
These COMPLETE lattice losses give

    Q>=Tcap*I/pi^2-Tcap*A0_exact/(pi*n)
                     -8R_exact/(pi*n)-8A0_exact/(n^2 sin a0),
    I=C*(b0-a0)+a*(cosb0-cosa0),
    A0_exact=C-a sin a0,
    R_exact=C log[tan(b0/2)/tan(a0/2)]-a*(b0-a0).   (7)

No convergence or asymptotic center-minimum assertion enters(7).
Both projection orientations have the same legal numerator lower;
the exact fixed-v baseline remains horizontal throughout.

Use sin(pi/100)>3/100, cosa0<1,cos(pi/10)>19/20 and
b0-a0=9pi/100>1413/5000. The cosine lower follows from
cosx>=1-x^2/2 andpi^2<10. Further,

    tan(pi/20)<88/553<4/25, tan(pi/200)>157/10000,
    log[tan(pi/20)/tan(pi/200)]<5/2.

For the tangent upper use sinx<x,cosx>79/80 atx=pi/20.
For the logarithm, the ratio is<1600/157 while
exp(5/2)>(8/3)^2*(8/5)=512/45>1600/157; the last comparison
is80384>72000. All exact weighted integrals in(7) are positive.
These bounds giveI>It,A0_exact<A0,R_exact<Rt from(1).
With11/4<Tcap<14/5 and157/50<pi<22/7, (7) becomesFt(r).
This proves(2), including all signed phases, parity classes, edges,
initial zeros and complete polynomial collision conventions. QED.

## Uniform1/200 through radius one from640

Choose r=1 directly for EVERY actualrho<=1; no monotonicity of Ft in
r is assumed. At n>=640,

    eta_n(1)>=4195/17920>1/5,

andp+1<5,n/(n+1)>1/2,1/4-1/n>1/8 giveFn>1/200.
AlsoFs>1/80 by35/286>1/10,(1-6/n)^2>1/2 and a-r/2=1/4.
For the middle bound at r1,

    It=663/20000, A0=91/400, Rt=8261/20000,
    (539/1936)It=357357/38720000>9/1000,
    [140A0+400Rt]/157=19707/15700<13/10,
    800A0/3=182/3<61.

The two losses at640 are bounded by893/409600<1/250, since
223250<409600. ThereforeFt>9/1000-1/250=1/200, and all three
center classes prove(3). Each bound increases with n at fixed r;
all loss coefficients are positive and the nearest factors increase.

## Interface, stronger old bands and limits

Apply a chosen bound ONLY after identifying an ACTUAL noncorner
center withrho<=r<=1. A mere nonempty intersection of a rational
outer proxy with this radius is not enough. Physical phase signs,
node values, endpoint multiplicities and collisions stay literal.
No floor is applied at an actual corner or above radius one.

The previously accepted Fh floor remains available on its proved
r<=21/40 domain, Fw onr<=pi/4, and their stronger uniform floors
on their original guards. They can be maximized with(2) at points
where BOTH hypotheses hold. No new claim is made for those old bands
outside those domains, and no sampled argmax or phase value is used.

This is a quantitative selected-pair domain continuation. It proves
no near upper comparison, global640, minimum onset or all-degree result.
Only the assigned prose files were written; no mathematical script,
scalar/source/native/endpoint/phase/degree/pack/Git/shared action ran.
2026-11-07; requested Sol xhigh, serving metadata unexposed;
rules/input1045157b45f6ede45802975656a06ecf064dc21a.


## Root adoption of reviewed support —2026-11-07

The rebuilt three-class radius-dependent projected floors hold for EVERY n>=64 under ACTUALrho<=r<=1; full actual noncorner defect is >1/200 for EVERY n>=640. The new pi/100..pi/10 positive band and all geometry/count/finite losses are proved; no old radius quantifier is transferred.

Distinct [review](../independent-checks-E04-assembly640.md), frozen support-report identity
a2b15344905afb4b42489fbec8e66b706df3e7b9436c7c2540de82ff53e91fef, accepts the unchanged reviewed prefix
f6d0cbea1337c922d7be1d27442abb646839fa161c4cedce81a499761e988778.
No scalar/source/native/finite-degree/pack job occurred. Global onset
remains768, residual719; fullD13 and matched640 remain OPEN here.
