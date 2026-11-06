# PD-T?argmax-bridge-codex-D30-rows — The actual six retained rows through radius three quarters

ID kind: PD-T. Aliases: wider R2 finite-h comparison; four fixed positive
samples; same C2 with wider endpoint/central domains.
Split from: D30 two-region far candidate. Split into: the true-constant
strip bound and full-profile gate have separate D30 files.

## Statement and status

For EVERY integer n>=32 put m=n+1,L=logn. First take alpha,beta>=0,
rho=alpha+beta<=3/4 and define

    a=(cos alpha+cos beta)/2,p=sin alpha,q=sin beta,P=p+q.

Use EXACTLY D05's corrected finite polynomial G=D-cos(nu), whose
exceptional highest first-coordinate coefficient is ONE, and its n
signed samples per row F=(-1)^delta G/2 and absolute row norms R_r.
There is no change to the common-primitive normalization1/(nm).
Define

    Jend=[R_0+R_1+R_(2m-2)+R_(2m-1)]/(nm),
    Jcen=[R_(m-1)+R_m]/(nm),J6=Jend+Jcen,
    C2=ell_0(beta)+ell_1(alpha,beta)+ell_1(alpha,-beta)
                                               +ell_2(alpha,-beta),
    ell_0(beta)=sinc beta,ell_0(0)=1,
    ell_r(alpha,b)=sin(b)/(r*pi+b)
          +8a sum_(j=-r+1,-r+3,...,r-1)
                  1/[(r*pi+b)²-(j*pi+alpha)²].

This is precisely the C2 of N1-07/D04/D07/D20, not a new reference.
Then on the COMPLETE closed domainrho<=3/4,

    |Jend-C2|<=[4a+9P]/n+[90a+4P]/n²,            (1)
    0<=Jcen<=[10a+P(1+L)]/n,                   (2)
    |J6-C2|<=B6wide,
    B6wide=[14a+P(10+L)]/n+[90a+4P]/n².         (3)

Signed comparison objects are defined by separate absolute phases,
as in D05's fixed-row model. Raw fixed row labels at negative beta
are not asserted invariant; unequal coordinate meshes are not exchanged.
Both parities, both axes and all actual finite-polynomial central
collisions are included. The six labels are distinct at this n range.

Status: **PROVED analytic developer extension**, by the proof below;
distinct mathematical review required before adoption. D07's old literal
rho<=1/2 theorem and constants remain unchanged. No numerical premise,
full S error, new far onset or global argmax result follows from(3) alone.

## Actual operator and fresh finite sign set

For signed b=beta or-beta set w=r*pi+b,z_j=j*pi+alpha,
u_j=z_j/n,v=w/m,mu=n/m,eta=1/m. The exact corrected finite-row
and signed-sum identities, away from poles initially, are

    F_j=[a(1+cosv)-(p/2)sin u_j+(sin b/2)sinv]
                                             /(cos u_j-cosv),
    sum_j F_j=T_r=n[a-(sin b/2)cot(w/(2m))].      (4)

These are the full finite polynomial identities of N1-07/N2, not a
near-only error theorem. There are n integers j of parity opposite
to r in the half-open representative mesh-pi<=u_j<pi.
The three nonzero endpoint cases are(1,beta),(1,-beta),(2,-beta).
They represent original labels1,2m-1,2m-2 exactly by evenness in v.
In each case0<w<7,|z_j|<4 for the proposed positive samples.
The fourth endpoint hasr0,beta and w=beta.

On this NEW domain, a>=1-rho²/4>=55/64 andP<=rho<=3/4.
For every endpoint rowv<=7/m<=7/33<pi/2. Its COMPLETE numerator
in2F is bounded below uniformly in the row angle by

    2a(1+cosv)-p*sin u_j+(sin b)*sinv
       >=2a-P>=31/32>0.                        (5)

Thus the sign is the sign of cos u_j-cosv, not a channel sign.
Sincev<pi and |u_j|<=pi, this denominator is positive iff|z_j|<mu*w.
For the indicesj=-r+1,...,r-1 of the opposite parity, the two gaps
satisfy, with k=r+/-j in{1,3},

    w+/-z_j>=k*pi-rho>(19/8)k,
    mu*w+/-z_j=(w+/-z_j)-w/m>(17/8)k.           (6)

The second bound follows from7/33<1/4 andk>=1. Thus all proposed
indices are positive-denominator indices. At the first excluded indices,
|z_j|>= (r+1)pi-alpha>r*pi+|b|>=w>mu*w, sincepi>rho.
More distant indices are excluded as well. The samples0 and-1,1 are
inside the actual half-open mesh for every n>=32. Hence the complete
positive sets are EXACTLY{0},{0},{-1,1}, with no endpoint collision.

Forr0 the mesh is odd and|z_j|>=pi-alpha>beta>=mu*beta, so all
denominators are negative. Equations(4)--(5) give EXACTLY

    R_r=-T_r+2 sum_(positive j)F_j,
    R_0=-T_0,
    R_0/(nm)=sinc(beta)*tau(beta/(2m))-a/m,
    tau t=t*cot t,tau0=1.                       (7)

Atbeta0 use the linked polynomial limit
sin(beta)cot(beta/(2m))->2m, so T_0=n(a-m),R_0=n(m-a).
No separately vanishing factor is set to zero at a pole. This freshly
proves the exact short-sign and closest-row identities throughrho3/4;
N1-09's near-domain conclusion is not extrapolated by assertion.

## Exact finite-h difference and denominator sums

For each of the four positive samples set

    D=w²-z²,Dh=mu²*w²-z²,
    K=sinc((u+v)/2)*sinc((u-v)/2),
    H=(1+cosv)/(2K),g=-p*sin u+(sin b)*sinv.

Factorization gives cosu-cosv=Dh*K/(2n²). Inserting(7),
subtracting the SAME displayed ell_r, and grouping terms gives

    e_r=R_r/(nm)-ell_r
       =-a/m+(sin b/w)[tau(v/2)-1]
          +8a sum_j[mu/Dh-1/D]
          +8mu*a sum_j(H-1)/Dh
          +2mu sum_j g/(Dh*K),                  (8)
    e_0=-a/m+sinc(beta)[tau(beta/(2m))-1].        (9)

This is a direct finite algebraic identity on the newly proved
pole-free endpoint domain; no old small-domain derivative theorem
is used. Partial fractions give the exact nonnegative displacement

    mu/Dh-1/D=(eta/2){1/[(mu*w-z)(w-z)]
                              +1/[(mu*w+z)(w+z)]}. (10)

The wider denominator bounds(6) imply

    sum_(four samples)1/Dh
       <=(64/289)(1+1+1/3+1/3)=512/867,          (11)
    S:=sum_(samples,both signs)1/[(mu*w+/-z)(w+/-z)]
       <=(64/323)(2+2+2+2/9)=3584/2907<5/4.     (12)

All denominators are positive. The four signed-a/m terms total-4a/m,
whereas their combined displacement is4a*S/m in[0,5a/m). Thus their
SUM lies in[-4a/m,a/m) and has absolute value<=4a/m<=4a/n.
This preserves the signed cancellation; bounding the two pieces
independently would unnecessarily enlarge the leading constant.

## Remaining endpoint errors with new constants

For all four positive samples|u|<4/n,v<7/n. The elementary sinc
bound gives

    49/50<K<=1,1-K<=(u²+v²)/12,
    |H-1|<=[u²/12+v²/3]/K<19/n².               (13)

For example65/(12n²)<1/50 atn>=32 proves the first lower; the last
coefficient is at most(50/49)(16/12+49/3)=2650/147<19.
Equations(11),(13) give a total H error at most

    (8a*19/n²)(512/867)=(77824/867)a/n²<90a/n². (14)

Also|g|<=p|u|+qv<=7P/n, and(11),(13) yield the total sine error

    2mu sum_j |g|/(Dh*K)
       <=[358400/42483]P/n<=9P/n.              (15)

The coefficient is strictly below9; the weak final inequality includes
P=0, when both terms vanish.

For|t|<=pi/4 the elementary linked bound0<=1-tau t<=t² holds.
The nonzero w values sum to4pi-beta. On0<=beta<=3/4,
sinbeta>=beta(1-beta²/6)>=(29/32)beta>=beta²; this NEW Taylor
argument replaces the older half-radius chord step. Therefore the
three nonzero tau terms and(9)'s closest-row tau term together cost

    [q(4pi-beta)+beta²]/(4m²)
       <=q(4pi+1)/(4m²)<=4P/n².                (16)

All vanish correctly atbeta0. Combine the balanced signed term,
(14)--(16) to prove(1). In particular the old7P/71a constants are
NOT silently retained; the wider domain has paid9P/90a.

## Central rows: fresh weights and full collision-safe inequality

The ACTUAL angles arev_(m-1)=pi-(pi-beta)/m,v_m=pi+beta/m,
so|v_r-pi|<=pi/m. Their full weighted row upper is the accepted
C06 proof component, valid for all interior rows atn>=2:

    R_r/n<=A(v_r)L+V(v_r)+5(|C|+|D|)/n²,
    A=2(|C|+|D|)/pi,
    C=(p-q-2a*cot(v/2))/4,D=(p+q+2a*cot(v/2))/4,
    V=[c_e Phi0(eta_-)+c_d Phi0(eta_+)]/[2sin(v/2)].

Its WHOLE weighted-Phi form extends from dense noncollision phases
to actualv=pi,axes and all finite-polynomial collisions. This uses
the proved component, not C06's unrelated assembledn>=10^6 theorem.
It never gives a value to an unweighted0*infinity product.

Herec_e,c_d>=cos(3/8)>=119/128 andc_e*c_d=a. Hence
c_e+c_d<=256a/119. Since|Phi0|<=4,pi²<10,m>=33,

    sin(v_r/2)>99/100,|cot(v_r/2)|<=pi/m,
    V(v_r)<=51200a/11781<(9/2)a,
    |C|+|D|=(1/2)max(p,|q+2a*cot(v/2)|)<=P/2+a*pi/m.

These are NEW wider-domain weight checks. They give the SAME safe
central intermediate upper

    Jcen<=9a/m+2PL/(pi*m)+4aL/m²
                                +5P/(m*n²)+10pi*a/(m²*n²).

UsingL<=n/4 for n>=32, the two small a terms are<=a/n, while
the two P terms are<=P(L+1)/n. This proves(2). FinallyJcen>=0
by its actual absolute-row definition, so|J6-C2|<=|Jend-C2|+Jcen
proves(3). QED.

## Use and limitations

The operator/reference match is exact: the four endpoint rows above
are the endpoint part of D05's fixedA6, the two central rows are its
remainingA6, and C2 is literally the C2 in D07's full global mesh
identity. No endpoint weight, highest mode, row label or normalization
is changed. The central integral/root modulus is a DIFFERENT object
and is never substituted forJcen. No ordinary collision is deleted.

For convenience(3) implies the uniform wider bound

    B6wide<=[43/2+(3/4)L]/n+93/n²,

but a far comparison may retaina=1-u andP before bounding. Every
ordinary-row, global regular-quadrature, scalar mesh/log and actual-
origin term remains a separate obligation. This component does not
assert that a2048 gate passes, or any all-n far/global theorem.
Old D07/D20 records are unchanged; no scalar/native/phase/board/
quadrature/degree job occurred. 2026-11-06, parent-assigned Codex
gpt-6.1-sol xhigh30min PAPER block; rules/input
09cc533678a22b38f40b70be95426ebbe81faa93, serving metadata unexposed.


## Root review closure — 2026-11-06

Distinct [D30 review](../independent-checks-D30-far.md), SHA256 `9ae9c0415625b36f908c1cabe70e44fd64028af08ec162641dde58fdc9ab85b8`, accepts the wide actual-six-row bound, inner11u constant and conditional two-region far implication without unresolved findings. Root adopts those exact support scopes. Both2048 endpoint signs remain UNCOMPUTED here; no unconditionalfar/global2048 follows until the separately frozen D33 computation/result review and other assembly premises. Reviewed prefix is preserved; final Claude audit remains separate.
