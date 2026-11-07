# PD-N?argmax-bridge-E03-joint-outer-log — The joint absolute mixed allowance fails

ID kind: PD-N. Aliases: exact outer/log pairing; fixed-phase endpoint-hole
logarithm; nonuniform order of phase and degree limits.
Split from: the proposed ABSOLUTE mixed-bound variant of E03's joint
regular-outer plus signed scalar-log target. Split into: none.

## Statement

Use the original D25/D37 regular-outer operator and D07 logarithmic mesh.
For n>=32, absolute phases alpha,beta>=0, rho=alpha+beta<=1/2, define

    T_n(alpha,beta)=Eout(phi)-aEout(0)+(d/pi)Rlog(phi),
    a=(cos alpha+cos beta)/2, d=(sin beta-sin alpha)_+,
    H=1+log n.                                           (1)

For every r in(0,1/2], every finite C,K>=0 and every integer N>=32,
there exist integer n>=N and 0<alpha<=r, beta=0, for which

    |T_n(alpha,0)|>C alpha/n+K H alpha^2/n.                (2)

More precisely, for EACH FIXED 0<alpha<=1/2,

    T_n(alpha,0)=-(2sin alpha/pi)(log n/n)+O_alpha(1/n)
                                                as n tends to infinity. (3)

This refutes only a uniform ABSOLUTE C rho/n+K H rho^2/n estimate on a
whole near diamond. The one-sided upper estimate without absolute values
is NOT refuted: the leading term in(3) is negative. Its uniform remainder
and the original full D13 joint remainder remain OPEN.

## Definitions and exact joint operator

Let m=n+1,L=log n,h=pi/m,t=beta/pi,ell(z)=log(pi-z), and

    Q_tau[G]=(1/m)sum_(k=2)^(m-2) G(h(k+tau))
                                      -(1/pi)integral_0^pi G(z)dz.

F_L,F_R are the literal regularized weighted profiles in accepted E02,
equation(3), with the same periodic f, coefficients C,D, bounded cancellation
integral I and weighted pole values. In particular F_s includes
-(d/pi)ell. At phase zero F_L=F_R=F0. Set W_s=F_s(phi)-aF0.
Eout=Q_t[F_L]+Q_(1-t)[F_R] and its origin uses offsets0,1 at the SAME n.

D07's exact Cmesh is the sum of ell over these SAME two ordinary meshes:

    Rlog=Cmesh/m-2(log pi-1)=(Q_t+Q_(1-t))[ell].             (4)

Indeed each mesh has precisely k=2,...,m-2 and
integral_0^pi ell(z)dz=pi(log pi-1). This is equality of operators,
not agreement merely of a leading logarithm. Thus

    T_n=Q_t[W_L+(d/pi)ell]+Q_(1-t)[W_R+(d/pi)ell]+Shift,   (5)

where Shift is exactly the accepted E02 finite origin-mesh shift. All
ordinary weights, k labels and integral normalizations match. There is
no logarithmic term at the origin because d(0)=0.

The original removed polynomial labels remain
{0,1,2m-2,2m-1,m-1,m}; centered-cell holes are
h(3/2+t),h(5/2-t) initially and h(3/2-t),h(1/2+t) centrally.
Their totals are4h and2h. The original n,n+1 meshes, their parities,
weighted pole continuity, endpoint numerators and exceptional top mode ONE
are unchanged. No scalar identity here approximates any of those six rows.

## Status, candidate disposition and negative-result scope

Overall status: **PROVED**, paper developer negative theorem; distinct
audit required. Candidate P2 disposition: **REJECTED: refuted**.

Attempted mechanism: use matching-log first-variation cancellation to infer
a uniform absolute mixed allowance for(1), with no remaining linear
logarithmic phase term. Covered range: ANY nontrivial near diamond,
arbitrary fixed starting degree, constants independent of phase and n.
The obstruction already occurs on beta=0 and so does not require a moving
collision, a nonzero scalar d, or a parity restriction.

The exact joint reduction and first-variation diagnostic below are steps
supporting this scoped mechanism test. They do not turn full D13 into PARTIAL.

## Dependencies and sources

Accepted E02-paired-outer and final independent audit3556b5ff... supply
the exact Shift and derivative diagnostic. D07-global-mesh supplies literal
Cmesh/Rlog; D25 supplies the max formulas, regular numerator differences and
initial no-root equality. N1-round6-central-log proves the coalescing-pole
subtraction is continuous and BV INCLUDING all root thresholds. D37's wider
checks are needed only to extend the exact identities/diagnostic to rho<=1;
the negative theorem itself uses the stated near domain. No D22 bound,
ordinary-row theorem or retained-six-row estimate is used.

No external theorem or priority claim is used. Gate, unchanged-baseline
hashes, new complete immediate shortlist and literature reading limitations
are in the companion idea record. C03/C04's limiting noncentral estimates
were read for comparison and are NOT transferred to this finite operator.

## Proof

### 1. First variation: the matching common logarithm really cancels

For fixed n and direction (A,B)>=0 set (alpha,beta)=epsilon(A,B) and
c_*=(B-A)_+. Accepted E02's exact directional derivative is

    D(delta_a Eout)=(B/m)[J(2h)-J(pi-h)]
       -(c_*/pi)(Q_0+Q_1)[ell]
       +(B/m^2)[F0'(2h)-F0'(pi-h)],
    J(z)=L/pi-f'(z)/sin(z/2)+log(sin z)/pi.

By(4), D[(d/pi)Rlog]=(c_*/pi)(Q_0+Q_1)[ell], since d(0)=0.
Therefore the exact joint first variation is

    D T_n=(B/m)[J(2h)-J(pi-h)]
               +(B/m^2)[F0'(2h)-F0'(pi-h)].              (6)

The integrable-envelope and finite-sample derivative justifications are
those accepted in E02; no new interchange of moving singular limits is
assumed. The L/pi constant in J cancels between the two boundaries.
For reference, |J(2h)-J(pi-h)|<8: |f'(2h)|<=2h,
sin h>=2h/pi, |f'|<=2, cos(h/2)>2/3, and
0<log(sin(2h)/sin h)=log(2cos h)<1. E02 also gives
2sup|F0'|<=4L+14. Hence

    |D T_n|<=B[8/n+(4L+14)/n^2]<9B/n.                    (7)

For the last inequality, (log n)/n decreases for n>=32 and log32<4.
In particular the alpha-axis derivative is zero for every fixed n.
This is not a phase neighborhood bound uniform in n.

### 2. Fix a positive alpha BEFORE letting the degree grow

Now fix alpha in(0,1/2] and put beta=0,p=sin alpha,q=d=t=0.
Then a=(1+cos alpha)/2>0 and Shift=0 EXACTLY. Both relative coefficient
profiles in D25's literal max formula reduce to

    g(z)=(p-2a cot(z/2))_+/pi,
    g(0)=0, g(pi)=p/pi.                                 (8)

The relative weighted pole parts agree on the two sides: the actual
numerators are both cos(alpha/2)[f(z+alpha)+f(z-alpha)]. The cancellation
integrals also agree by coefficient exchange/separation reflection in
N1's exact generic formula. Thus write exactly

    W_L=W_R=L g+R_alpha,
    T_n(alpha,0)=L(Q_0+Q_1)[g]+(Q_0+Q_1)[R_alpha].         (9)

We verify that R_alpha has finite variation on the FULL closed interval
for this fixed alpha, so no hidden endpoint or cusp logarithm is placed
in the error. The pole part is

    Pdiff=[V(z)-V(0)]/z+V(z)d0(z),
    V=N_s-aN0, d0=1/(2sin(z/2))-1/z.

Near zero, all shifted arguments lie in an open smooth period, V is C2,
and the difference quotient has a finite continuously differentiable
extension. On the remaining compact interval the periodic f is Lipschitz;
crossing a derivative atom keeps the function continuous and BV. The
displayed weights are smooth and bounded there. Thus Pdiff is BV.

For the cancellation part, D25's exact initial no-root formula gives
I_s(phi,z)-aI_s(0,z)=0 for0<z<=pi/2, since q=0. On the central
half N1-round6-central-log proves I_s(phi,z)-d log(pi-z) has a
finite continuous limit and finite variation, with all root crossings
included. Here d=0. The origin profile I_s(0,z) has the same property.
Consequently the cancellation difference is BV on the full interval;
the expressions join continuously at pi/2. This proves R_alpha is BV.
No uniform bound for its variation as alpha tends to zero is needed or
claimed. Its endpoint values are its regularized one-sided limits,
not evaluations of separate unweighted poles or actual collision rows.

Midpoint quadrature on the exact cells now gives

    |(Q_0+Q_1)[R_alpha]|
       <=[Var(R_alpha)+6sup|R_alpha|]/m=O_alpha(1/m).     (10)

Here the variation is paid once per side with factor1/(2m), and all
four holes have total length6h. Thus(10) includes every missing interval.

### 3. The actual central holes produce the surviving logarithm

For each fixed alpha, g is zero up to a point z_* in(0,pi), then is the
smooth function (p-2a cot(z/2))/pi. Its first derivative has finite
variation: only the finite jump at z_* is added to a smooth derivative
on[z_*,pi]. Composite midpoint error for g on the actual cells is therefore
O_alpha(m^-2). For completeness, integrating the Taylor remainder on a
cell bounds it by h^2 times the derivative variation on that cell after
normalization; summing disjoint cells proves this order, including the
cell containing z_*.

At t=0 the initial holes have lengths3h/2 and5h/2; both have zero
leading endpoint value g(0)=0. The central holes have lengths3h/2 and
h/2, with the same endpoint value g(pi)=p/pi. Lipschitz continuity of
g gives their integrals as the respective length times that endpoint
value, with O_alpha(h^2) remainders. Therefore

    (Q_0+Q_1)[g]=-2p/(pi*m)+O_alpha(m^-2).               (11)

This uses the TRUE missing intervals. Replacing the cell union by the
full interval before this step would erase exactly the leading term.
Combine(9)--(11):

    T_n(alpha,0)=-2p L/(pi*m)+O_alpha(1/m)+O_alpha(L/m^2).

Since m=n+1 and L/n is bounded for n>=32, this is(3). Both parities use
the same exact folded operator, so the limit holds along all integers.

### 4. Refute precisely the absolute candidate

If an absolute mixed bound held for all n>=N and all phases in any fixed
near diamond of radius r>0, then fixing any alpha in(0,r], beta=0,
multiplying the bound by n/log n and using(3) would imply

    2sin alpha/pi<=K alpha^2.                           (12)

But sin alpha>=alpha/2 on[0,1/2]. Choose alpha>0 smaller than both
r and1/[2pi(K+1)]. Then the left side of(12) is at least alpha/pi,
whereas its right side is less than alpha/(2pi). This is a contradiction.
The fixed C term vanishes in that limit. Equivalently, for any proposed
C,K,N some degree beyond N violates the bound, which is exactly(2).
This completes the scoped negative theorem.

## Scope and best next paper task

The common logarithm DOES cancel in the exact fixed-n derivative. A
different linear logarithmic charge survives when phase is fixed first,
because the L-profile's central endpoint value is nonzero and two actual
holes remain. These facts are compatible: phase and degree limits are
not uniform here. The argument does not show a positive upper obstruction.
Indeed(3)'s leading sign is favorable for a one-sided comparison.

Best next PAPER task: retain the negative coefficient contribution with
its actual holes, and bound the paired remaining phase profiles uniformly
across p comparable to h, moving roots and numerator derivative atoms.
A fixed-alpha O_alpha(1/n) constant and fixed-n first variation cannot
supply that bound. Full D13 and the one-sided mixed target remain OPEN.
All row-origin, retained-six-row and true-origin conversion terms stay
unchanged: E(phi)-E(0)=delta_a E-uE(0)<=delta_a E+uE0, |E(0)|<=E0.

## Checks and history

Paper only. Actual work consisted of bounded complete reads, mechanism
searches and byte/hash comparisons, exact finite algebra, and the written
BV/midpoint proof. No scientific source/code/job, scalar/phase/degree/
endpoint/threshold/native/compile/pack action, scientific import or shared/
Git mutation. Only the three assigned E03 prose files were written; all
accepted E02 files remain frozen. No independent review or new global
onset/coverage is claimed. Source/SPEC review, publication and root release
would be required before any later scalar use of a successful successor.

2026-11-06, Codex mathematical developer; parent-requested Sol xhigh,
actual serving metadata unavailable. Rules/input
017f8ecc45534b4a6dd38b0488020463cb914edb. This is one component of E03,
not an extra round per identity. Root controls shared registration and Git.

## Cross-component coupling boundary — 2026-11-07

The initial11806-byte theorem prefix above is frozen at SHA256
ce83f8272092521f27c4d3894e16e3453a91d5baff2fcc4bb9d2567232b92396.
Root requests coordination with D16's separately owned row-origin paper.
This appendix identifies the match and the remaining obligation; it does
not infer a full signed remainder bound from(3) or(6).

Let B=(1/m)sum_O6 H, P=(1/m)sum_O6 Tref, where Tref is D07's
endpoint reference, and Gint=(1/pi)integral(F_L+F_R). D07 gives
Eout=B-P-(d/pi)(Cmesh/m)-Gint. Therefore(4) gives exactly

    T_n=delta_a B-delta_a P-delta_a Gint
                            -(2d/pi)(log pi-1).

D16/root's joint-row identity is Erow+Eret=S_n-B-Delta2-C2. Adding its
delta_a increment cancels the SAME ordinary H sum BEFORE any bound:

    delta_a(Erow+Eret)+T_n
       =delta_a[S_n-P-Gint-Delta2-C2]
                            -(2d/pi)(log pi-1).          (13)

This is exact algebra on the unchanged mask. It is not a bound on S_n
or the whole remainder; the full true-origin conversion and the remaining
scalar Rmesh also retain their own terms.

For beta=0 the central labels m-1,m have angles pi-h,pi. Their continuous
log-coefficient PROFILE values are max(p,2a tan(h/2))/pi and p/pi.
For EACH FIXED alpha>0 they eventually both equal p/pi, giving the
coefficient allocation +2p L/(pi*m). D07-central proves an actual-row
UPPER using these coefficients; that inequality alone is not equality
for the actual rows and does not insert a regularized H at a collision.

D16 additionally supplies the ACTUAL linked finite vectors on this axis:
put c=cos(alpha/2) and L_k(theta)=sin(theta)cot((k*pi+theta)/n), with
the complete finite linked value L_0(0)=n and periodic index k. For the
original first-coordinate labels j=n+2k and j=n-1+2k respectively,

    F_(m,k)=c L_k(alpha/2),
    F_(m-1,k)=[c/(2cos(h/2))]
       [L_k((alpha-h)/2)+L_(k-1)((alpha+h)/2)].

These are reported from D16's separately developed row-origin paper;
their verification/adoption is separate and they are NOT premises of the
negative theorem above. D16 derives Jcen(0)=2/m and, for FIXED alpha>0,

    Jcen(alpha,0)=+2p L/(pi*m)+O_alpha(1/m).

That signed coefficient matches the omitted-cell charge in(11) at the
SAME order of limits. No central-log obstruction is asserted for their
sum. A uniform ACTUAL-row/outer coupling, including p comparable to h,
parity, finite numerator and top mode ONE, remains OPEN. Neither the
fixed-n alpha cusp nor either fixed-alpha asymptotic proves that missing
uniform statement. The negative result(2) remains restricted to the
ABSOLUTE outer/log component and does not reject the full one-sided goal.

Closed-direction convention for the minor diagnostic(7): its last strict
comparison applies when B>0; when B=0 the derivative is exactly zero and
the bound is non-strict. This does not affect(2), (3) or their proof.


## Root adoption after distinct focused audit —2026-11-07

Root adopts the exact joint outer/log identity and the scoped ABSOLUTE mixed-bound obstruction for THAT block. Its fixed-alpha negative leading logarithmic charge is favorable for an upper comparison. No one-sided/fullD13/full-joint-row obstruction follows; attributed separate row observations are not premises.

Distinct [review](../independent-checks-E03-joint-outer-log.md), SHA256
6c2c619d44d471bf072cb100e550d94dcda91bf640530baee7df9260bacac654, accepts the unchanged reviewed prefix
642176ed25cdeff819ca5ff65074c0e0a7f2582bee835751802225f182c693a6.
Full D13 remains OPEN. No numerical/source/native/pack job occurred.
Current global onset768 and residual719 are unchanged; final Claude is separate.
