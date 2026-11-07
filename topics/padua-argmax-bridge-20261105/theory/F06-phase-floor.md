# F06 — A joint signed projected floor at endpoint distance two

ID kind: provisional PD-T?argmax-bridge-codex-F06-01.
Aliases: s2 direct finite floor; distance-two signed straddling certificate.
Split from: the distance-two support for I09's still-OPEN full fifth floor.
Split into: none. Other distances and the larger hybrid remain OPEN.

Status: **PROVED developer PAPER support**, distinct review required.
This is a quantitative selected-pair continuation, not a new principle.

## Statement

For every integer n>=128 put m=n+1,N=nm. Take any physical odd center

    0<=J<=n,0<=K<=m,J+K odd,
    theta=(J*pi+alpha)/n,phi=(K*pi+beta)/m in[0,pi],
    |alpha|+|beta|<=r<=pi/4.

Use the ORIGINAL corrected polynomial Padua kernels and full projected
defects of PD-T364/C01, with their endpoint weights and finite collision
values. Then, separately,

    Q_v(K)>1/5-3r/20 when min(K,m-K)=2,
    Q_h(J)>1/5-3r/20 when min(J,n-J)=2.                 (1)

In particular each exceeds the released target1/5-3r/20-3/n. This
does not cover any other endpoint distance, prove the full fifth floor,
establish a primitive upper comparison or change a global onset. Actual
corner centers receive no floor, and projections are NEVER added.

## Exact objects and normalization

Let P=T_(n+1)+T_n and

    G(u,v)=[P(cos u)-P(cos v)]/(cos u-cos v)-cos(nu),
    d(X,Y)=|X|+|Y|-|X+Y|.

The divided difference is its finite polynomial value at equality. The
exceptional highest first-coordinate coefficient remains ONE. Write

    a=(cos alpha+cos beta)/2,
    p=sin alpha,q=sin beta,Pabs=|p|+|q|.

At regular odd-board points the signed half kernel is EXACTLY

    A(u,v)/(cos u-cos v),
    A(u,v)=a*(1+cos v)-(p/2)*sin u+(q/2)*sin v.        (2)

This is obtained with the exceptional subtraction cos(alpha), not1.
The full periodic projection coefficient is1/(4N). Folding just its
physical reflected coordinate and passing to common-sign halves gives

    Q_v=(1/N)*sum_(k=0)^m f_k
          sum_(0<=z<2n,z+k=J mod2) d(V_+,V_-),
    V_+/-=(-1)^z G((z*pi+alpha)/n,phi+/-k*pi/m)/2;

    Q_h=(1/N)*sum_(j=0)^n e_j
          sum_(0<=z<2m,z+j=K mod2) d(W_+,W_-),
    W_+/-=(-1)^(J+j) G(theta+/-j*pi/n,(z*pi+beta)/m)/2. (3)

Original physical endpoint weights e,f are1/2, otherwise1. Phases in
reflected partners are unchanged. Both periodic branches below are
different terms of(3), not a change in its coefficient. Every omitted
term, including every collision, has nonnegative d.

## 1. FIRST: exact signed straddling sets, crossings and collisions

This subsection gives the complete denominator-straddling ranges before
the floor estimates. It does not assert that every positive defect must
straddle: signed numerators can also give cancellation elsewhere.

Use the following orientation notation:

| Projection | Physical mesh M | Periodic mesh L | Physical phase mu | Periodic phase eta |
|---|---|---|---|---|
| Vertical | m | n | beta | alpha |
| Horizontal | n | m | alpha | beta |

Let epsilon=+1 for the lower distance-two center and epsilon=-1 for
the upper center. Put

    xi=epsilon*mu,t=(2pi+xi)/M,b=l*pi/M,0<=l<=M.

The actual physical selected row is l at the bottom and M-l at the top.
Both target cosines, in either orientation, are

    y_+=cos(b+t),y_-=cos(b-t), y_+<y_- if0<l<M.     (4)

For example at the upper vertical center phi=pi-t and physical row
angle pi-b, its two second angles are2pi-t-b and b-t. The analogous
horizontal first angles have those same cosines. No kernel transpose
has been used. Here0<t<pi/2, since M>=128 and |xi|<=pi/4.

For a periodic index z, split its interior representatives into

    z=R, w_+=(R*pi+eta)/L,
    z=2L-R, w_-=(R*pi-eta)/L, 1<=R<=L-1.             (5)

The actual periodic angles are w_+ and2pi-w_-, respectively. They
have identical cosine coordinates only when the phases warrant it;
their actual sine coordinates and defects are not identified.
In either orientation the required parity is R+l odd. At the bottom
the other center index is odd because the distance-two index is even.
At the top it has parity1-M, while the actual physical row is M-l;
the same condition R+l odd follows. Negation modulo2L preserves parity.

For every0<l<M define the folded target angles

    a_l=|b-t|, c_l=min(b+t,2pi-b-t).

They satisfy0<=a_l<c_l<=pi. For sigma=+1,-1, branch w_sigma in(5)
straddles EXACTLY when

    (L*a_l-sigma*eta)/pi < R < (L*c_l-sigma*eta)/pi,
    1<=R<=L-1, R+l odd.                              (6)

Equivalently take every integer of the required parity between

    max(1,floor((L*a_l-sigma*eta)/pi)+1)

and

    min(L-1,ceil((L*c_l-sigma*eta)/pi)-1).

These are exact-real integer formulas, not numerical rounding rules.
They retain every moving branch crossing: equality with either bound
is a target-cosine collision and is excluded from the STRICT set(6).

The remaining seam representatives are z=0 and z=L, each counted ONCE.
Their folded angles are |eta|/L and pi-|eta|/L. Include one in the
strict straddling set precisely when its folded angle is in(a_l,c_l)
and its original parity z+l is odd. Equality again indicates a collision.
The actual sine at either seam remains its original value, not the sine
of an arbitrarily chosen folded branch. At l=0,M the target kernels
are identical and d=0, including their polynomial collision values.

At every equality in these formulas the finite polynomial, not a rational
0/0, defines the signed halves. The polynomial identity obtained by
multiplying(2) by cos u-cos v forces its numerator to vanish at such
an admitted collision. It does not determine its finite quotient value.
All equality/collision terms remain in the full(3) with nonnegative d.
The regular selection below omits them; no positive collision value is
assumed or needed. Thus(6) and the two seam tests cover all exact
straddling possibilities and all boundary equalities for every signed
phase in the stated domain.

## 2. A regular four-term selection on the registered physical band

Select every integer l with

    M/6<=l<=M/2,

and in EACH sigma branch select R=l+j for j=-1,+1. These are
four distinct periodic representatives per physical row. Indeed
1<=l-1<l+1<L from M,L>=128 and |M-L|=1; their reflected partners
lie on the other half-circle. Every physical row is interior and has
weight1. Their parity is R+l=2l+j odd.

Here b in[pi/6,pi/2]. Both b-t,b+t lie strictly in(0,pi). The
exact displacement of either branch is

    M*(w_sigma-b)=(M/L-1)*l*pi+(M/L)*j*pi
                                      +sigma*(M/L)*eta. (7)

Since M/L<=129/128, l<=M/2 and |mu|+|eta|<=r, we have

    |M*(w_sigma-b)|+|xi|
       <=(129/128)*(3pi/2+r)
       <=903pi/512<2pi.                              (8)

Consequently |w_sigma-b|<t=(2pi+xi)/M in every branch, at both
orientations and both meshes. The selected denominators therefore
straddle STRICTLY and are regular. No selected collision or phase
crossing is lost. This verifies the selection by the exact ranges(6),
rather than extrapolating the zero-phase k+/-1 statement.

## 3. Each branch's actual signed numerator and a common lower bound

Write w=w_sigma. Vertically the two exact numerators from(2) are

    A_+=a*(1+cos(b+t))-sigma*p*sin w/2
                                  +epsilon*q*sin(b+t)/2,
    A_-=a*(1+cos(b-t))-sigma*p*sin w/2
                                  -epsilon*q*sin(b-t)/2. (9)

Horizontally they instead are

    A_+=a*(1+cos w)-epsilon*p*sin(b+t)/2
                                           +sigma*q*sin w/2,
    A_-=a*(1+cos w)+epsilon*p*sin(b-t)/2
                                           +sigma*q*sin w/2. (10)

In particular the horizontal baseline is the ACTUAL fixed second angle.
The sigma signs are retained explicitly, so no equality of branches or
separate phase-evenness of a projected quantity is presumed.

For |w-b|<t and b in this band, every relevant absolute sine is at
most sin b+t, by the sine Lipschitz inequality. Each actual baseline
in(9)--(10) is at least

    1+cos b-t*sin b-t^2/2,

by angle addition, sin t<=t and cos t>=1-t^2/2. Set

    D=2pi+r,T=D/M,
    C=Pabs/2+(a+Pabs)*T+a*T^2,
    F(b)=a*cot(b/2)-C.                              (11)

Using sin b>=1/2 and t<=T, EACH of the four actual numerator
inequalities separately gives

    A_+/- /sin b
      >=a*cot(b/2)-Pabs/2-(a+Pabs)*t-a*t^2
      >=F(b).                                      (12)

Thus the actual joint phase data a,Pabs remain together in the
finite bound; only their final admissible-radius bounds will be used.

The lower function is positive on the whole band. Indeed

    27/32<a<=1, Pabs<=r<4/5,
    T<=9pi/512<99/1792<1/18,

using pi^2<10, pi<22/7 and |alpha|+|beta|<=r<=pi/4.
Since cot(b/2)>=1,

    F(b)>27/32-2/5-(9/5)/18-1/324
         =11/32-1/324>1/3.                         (13)

All selected halves therefore have positive numerators and opposite
nonzero denominators. The full cosine span is2sin b sin t. For EACH
selected term the exact opposite-sign defect obeys

    d=2min(|H_+|,|H_-|)
       >=[min(A_+,A_-)]/(sin b sin t)
       >=F(b)/t.                                  (14)

The four contributions can now be added because each satisfies(14),
not because their values coincide. From(3), their actual interior1/N
weights and M*t<=D,

    Q >=4/[L*D]*sum_(M/6<=l<=M/2) F(l*pi/M).        (15)

This is a direct finite discrete bound, with no full-band limiting
reference or uniform integral approximation in a shrinking center angle.

## 4. Finite row sum and exact radius comparison

The positive function F is decreasing. The elementary monotone-grid
inequality, valid when band endpoints are not mesh points, gives

    sum F >=(M/pi)*integral_(pi/6)^(pi/2) F(b)db-F(pi/6).

Here

    integral cot(b/2)db=2log(1+sqrt3)>2,
    F(pi/6)<=a*(2+sqrt3)<15/4.                      (16)

For completeness the strict logarithmic lower bound is elementary:
sqrt3>19/11, while
exp1<8/3+(1/24)*sum_(j>=0)5^(-j)=87/32<30/11.
Thus1+sqrt3>exp1. No numerical integral or measured logarithm is used.
The row-sum inequality itself compares the descending rectangle sums
with the integral and loses at most the left endpoint value; it is the
finite mesh lemma already used by C02/D29.

Insert(11),(16) into(15) and define

    H(a,Pabs,r)=[8a/pi-2Pabs/3]/D.

All finite losses remain explicit:

    Q >(M/L)*H-4(a+Pabs)/(3L)-4aD/(3LM)-15/(LD).    (17)

We next use only written rational bounds. Since D<=9pi/4,
pi^2<10 and pi>3,

    H>16a/45-Pabs/9
      >=(16/45)*(1-r^2/4)-r/9>0,
    H<=4/pi^2<1/2.                                (18)

Also M/L>=1-1/n, L,M>=n, a+Pabs<9/5 and D<8. Therefore,
for EVERY n>=128, the total losses in(17), including replacement of
M/L by1, are strictly less than

    1/(2n)+12/(5n)+32/(3n^2)+5/(2n)
       <=[1/2+12/5+1/12+5/2]/n
        =329/(60n)<11/(2n).                        (19)

No fixed smaller-degree scalar value has been evaluated. These are
inequalities on the complete released degree domain.

Subtract the desired radius floor from the lower expression in(18):

    (16/45)*(1-r^2/4)-r/9-(1/5-3r/20)
       =7/45+7r/180-4r^2/45
       >37/375,                                   (20)

because0<=r<=pi/4<4/5. Finally

    11/(2n)<=11/256<37/375,

the last comparison being4125<9472. Equations(17)--(20) prove
Q>1/5-3r/20 for BOTH projections whenever their center endpoint
distance is two. This proves(1) and hence the original weaker target.

## Scope, provenance and review boundary

All counts are finite and hold for every signed phase, both endpoint
orientations and either original adjacent-mesh projection. The four
selected terms are independently bounded; they are not identified by
an unproved symmetry. Actual polynomial collisions, omitted regular
terms and physical endpoint half weights stay in the exact full object.
No projection is added to another and no actual-corner floor is used.

The result escapes F02 by proving a finite lower bound directly rather
than approximating the unmodified full-band integral. It does not repair
that reference or extend this support to other distances. The full
I09 floor, distances1/3/4, shrinking-angle region and fixed-height compact
reference remain OPEN. No global onset or new degree is certified.

The gate/release/local-inventory chronology is recorded candidly in
../ideas/F06-phase-floor.md and ../attempts/F06-phase-floor.md. The full
gate and root prospective registration/separate release preceded all
mathematics, but the first informal band estimates preceded the required
local inventory. Root was immediately notified and directed continuing
the authorized SAME task after the actual records, with NO waiver or
retrospective registration claim. Mathematical success is not a protocol
verdict; final Claude judgment/readiness remain separate.

2026-11-07. Requested/API-assigned Sol xhigh, serving metadata unexposed;
rules/input4a5de2012bad94601c713b2ff5517f2e3fb80af2. Inputs are PD-T364,
C01/C02/D29 finite projection/count identities and elementary trigonometry.
No external theorem, quadrature, fitted coefficient, numerical evaluation,
script/import/scalar/phase/degree/endpoint/native/compile/job, Git/shared
or old-proof mutation. Scientific CPU0; ordinary tool overhead unmeasured.
Distinct mathematical reconstruction and root adoption remain required.


## Root disposition after distinct mathematical acceptance —2026-11-07

Root adopts the exact mathematical statement under its written quantifiers, hypotheses and dependencies. The original frozen proof/record prefix is preserved and identified in [independent review](../independent-checks-F06-F07.md), final SHA256832ec81ce4aaba07198ecbef2bfb571f0e7011c405b622601d105dd25b9ffbec. No global-onset change, new finite degree, source integration, strict runtime saving, novelty/priority verdict, protocol waiver or readiness follows beyond the exact statement. Final Claude review remains separate.
