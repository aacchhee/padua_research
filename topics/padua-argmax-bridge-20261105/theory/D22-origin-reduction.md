# PD-T?argmax-bridge-codex-D22-origin — A fully charged partial origin cancellation

ID kind: PD-T. Aliases: endpoint-relative hybrid allowance; asymmetric
retained-row origin subtraction. Split from: D22 lower near onset target.
Split into: none. This supports, but does not prove, D13's OPEN full
vanishing relative remainder or any new onset by itself.

## Statement and definitions

For integer n>=32 put m=n+1,L=log n,H=1+L. Use EXACTLY D05's corrected
odd-board primitive and D02's unchanged completed model M_infty:

    D_n(u,v)=sum_(i+j<=n) h_i h_j cos(iu)cos(jv),
    h_0=1,h_i=2(i>0), G_n=D_n−cos(nu),
    delta_r=(1−r) mod2,
    u_rk=(delta_r*pi+alpha+2k*pi)/n,
    v_r=(r*pi+beta)/m,
    R_r=sum_(k=0)^(n−1)|(-1)^delta_r G_n(u_rk,v_r)/2|,
    S_n=(nm)^(-1)sum_(r=0)^(2m−1) R_r.

First take alpha,beta>=0,rho=alpha+beta<=1/2, and put
a=(cos alpha+cos beta)/2,u=1−a,r2=alpha²+beta²,P=sin alpha+sin beta.
The origin is the SAME actual finite primitive, S_n(0)=Lambda_c(n).
All actual polynomial collisions use the finite G_n above. Signed phases
use the inherited separate evenness, without exchanging n and m.

Let G(n),G0(n),E0(n) be exactly D16-phase-allowance's positive functions:

    G=[(21/5)L+(9/4)log(2m)+1022/15]/m,
    G0=[(28/pi²)L+111/2+23/pi]/m,
    E0=D16's complete actual-origin absolute allowance.

Define

    Cstar=G+G0+22/n+162/n²+40H/(pi*n²),
    Kstar=[(112/pi+2)H+2L+61/3]/n+4/n².

Then on the entire closed signed near diamond,

    S_n(phi)−S_n(0)
      <=M_infty(phi,L)−M_infty(0,L)
                             +Cstar+Kstar*rho+u E0
      <=M_infty(phi,L)−M_infty(0,L)
                             +Cstar+Kstar*rho+(E0/4)r2.       (1)

Cstar,Kstar are positive and decreasing for every real n>=32. Overall
status: **PROVED**, written analytic developer theorem; distinct review
required. No numerical premise enters this result. The constant Cstar
is nonzero, so (1) is not a proof of D13's fully vanishing remainder.

## Exact operator telescope

Use D05's fixed six labels A6={0,1,2m−2,2m−1,m−1,m}, its complement
O6, K_fixed, and D07's G_n intermediate (distinct from the polynomial
named above), J6,C2,Rmesh,Rlog. Define

    Erow=S_n−K_fixed, Eout=K_fixed−G_n, Eret=J6−C2,
    delta_a X=X(phi)−a X(0), d=(sin beta−sin alpha)_+.

The accepted D07 identity, with its exact upper ordinary index m−2,
continuous Delta_2=E_infty−E_2 and unequal n,m meshes, gives

    delta_a(S_n−M_infty)
       =delta_a Erow+delta_a Eout+delta_a Eret
                           +delta_a Rmesh+(d/pi)Rlog.         (2)

Every term below belongs to (2). No old fixed-strip I_n or independent
cutoff residue is inserted or deleted.

## 1. Central reference complement, with both parity transitions

Let J=floor(n/2). D13's fixed endpoint reference sets are left
j=2,...,J and right j=3,...,J. The full ordinary folded labels are
left j=2,...,m−2 and right j=3,...,m−1. Their complementary central
labels therefore start at j=J+1 on each side. Their total number is

    (2n−4)−[(J−1)+(J−2)]=2n−2J−1<=n.                (3)

It equals n−1 for even n and n for odd n. For s=beta/pi on the left
and s=−beta/pi on the right, their folded angle z=pi(j+s)/m obeys

    z>=pi(J+1)/m−beta/m>=pi/2−1/(2m), z<pi.         (4)

For even n the first lower term is larger than pi/2; for odd n it is
exactly pi/2. Thus (4) includes the right transition row below pi/2.
The designated rows m−1,m are absent, so v is never a multiple of pi.

At a collision-free phase use the symmetric bounded cancellation
reference g0 with coefficients (−w,w), w=a cot(v/2)/2, and quadrature
error T0_r as in D04/D13. N1-cancellation-quadrature(2), or D04's
literal final central estimate, gives

    |T0_r|<=4|w|/|sin v|=a/sin²(v/2).

The folded value has the same sin²(v/2). By (4),

    sin²(v/2)>=(1−sin(1/(2m)))/2>=(1−1/(2m))/2.

Writing Zcen=(nm)^(-1)sum_central T0_r, (3) implies

    |Zcen(phi)|<=2a/(m−1/2), |Zcen(0)|<=2/m,
    |Zcen(phi)−a Zcen(0)|<=4a/n.                    (5)

The origin version uses z>=pi/2 exactly. Its ordinary board contains
no collision: coprimality of n,m makes p/n=q/m modulo2 require
(p,q)=(n,m) for an odd pair, and that row is retained, not ordinary.
The plus-sign collision reduces to this case by q ->2m−q modulo2m,
which preserves row parity and the central label.

## 2. The complete row-reduction increment

At a phase avoiding all polynomial collisions, D04's exact ordinary-row
decomposition reads

    Erow=(nm)^(-1)sum_O6 T_r+Epsilon−Delta_2,
    |Epsilon|<=10/n²+20a H_n/(pi*n²),
    H_n=sum_(j=1)^n 1/j<=H.

D03 bounds the perturbation from the symmetric reference by
112P H_n/(pi*n), and it vanishes at the actual origin. D13's endpoint
theorem includes the ENTIRE Delta_2 and gives
|delta_a Qep|<=a rho(2H_n+10)/n. Combining this with (5) and the two
weighted-pole absolute allowances gives

    delta_a Erow
      <=4a/n+20/n²+40a H/(pi*n²)
                    +rho[(112/pi)H+2H+10]/n.        (6)

No relative weighted-pole theorem is claimed. The two pole errors are
paid absolutely; the endpoint cancellation is precisely D13's theorem.

The complete Erow=S−K_fixed is continuous at every phase by D05's
weighted-Phi and integral continuity proof. Its actual-origin value is
fixed. The right side of (6) is continuous. For any target phase choose
a sequence in the near triangle avoiding the finite union of collision
lines; pass to the limit only in complete Erow and (6). This proves (6)
at collisions without assigning g0 or an individual pole error a value
there. The endpoint rows themselves are collision-free throughout the
near triangle by the D13 no-wrap theorem.

## 3. One-sided retained rows and regular quadrature

Write J6=Jend+Jcen, with Jcen the two ACTUAL central row norms. D07's
four endpoint theorem and its central theorem give

    |Jend−C2|<=(4a+7P)/n+(71a+4P)/n²,
    0<=Jcen<=[10a+P(1+L)]/n.

Subtract a times the actual-origin expression. Since Jcen(0)>=0,
the resulting one-sided upper is

    delta_a Eret
       <=[18a+P(8+L)]/n+(142a+4P)/n².               (7)

Specifically the endpoint pair pays 8a/n+142a/n², while the phase
central pair pays 10a/n. The nonnegative subtracted origin central
pair is retained algebraically and then dropped only for this upper.
This is neither a symmetric absolute estimate nor a vanishing relative
retained-row theorem. The linked beta=0 polynomial value in the
endpoint theorem is essential and is unchanged.

D07's full regular quadrature bound, simplified at the actual phases
exactly as in D16, gives

    delta_a Eout<=G+aG0<=G+G0.                      (8)

Thus the regular quadrature has NOT been assumed phase-relative.
D13's exact singular-mesh theorem gives

    |delta_a Rmesh|+(d/pi)|Rlog|<=rho(L+7/3)/n.      (9)

## 4. Assemble and convert to the actual origin

Insert (6)--(9) into (2), using a<=1 and P<=rho. The constant terms
are G+G0+(4+18)/n+(20+142)/n²+40H/(pi*n²)=Cstar. The linear terms
are exactly

    rho{[(112/pi+2)H+10+(8+L)+(L+7/3)]/n+4/n²}
       =Kstar*rho.

Let E=S_n−M_infty. The exact final conversion is

    E(phi)−E(0)=delta_a E−u E(0)
                 <=Cstar+Kstar*rho+u E0.

D16 supplies |E(0)|<=E0 at the SAME degree. This gives (1)'s first,
stronger upper; the cosine bound u<=(alpha²+beta²)/4 gives its second.
This last term is not omitted or
identified with the model's origin value.

G,G0 decrease for real n>=32 by D16's complete scalar proof. All added
terms in Cstar are positive inverse powers or positive multiples of
(1+log n)/n², hence decrease there. Kstar has form(c log n+d)/n+4/n²
with c,d>0 and d>c; its derivative is negative. This proves the stated
monotonicities without a scalar evaluation.

## Scope, checks and remaining target

The theorem includes both parities, both axes, the closed rho=1/2 seam,
all signed sectors and actual weighted collisions. It is an upper for
the common primitive, not a physical defect statement; any near argmax
application must still subtract C02's single noncorner defect floor and
treat actual corners separately. D10's fractional true constant and
the entire logarithmic coefficient remain in the model comparison.

No onset, finite range, numerical run or model correction is asserted.
Distinct proof review and a separately frozen scalar application remain
necessary. Candidate/attempt are ../ideas/D22-origin-reduction.md and
../attempts/D22-origin-reduction.md. 2026-11-06, requested Astra ultra;
serving metadata unexposed. Original rules/input ca8d52aa, current
read-only integration head c1e5bef6; no old proof/source was changed.
