# E14 — A rebuilt signed outer upper on the closed radius-one diamond

Provisional developer PAPER theorem, no global ID. Status: **PROVED
developer**, distinct mathematical/protocol audit and root adoption
pending. This is disjoint annular support inside the SAME fixed320 E14
round, not a new research round, endpoint selection or main320 theorem.
The old E09 half-radius proof and constants remain unchanged.

## Statement and literal objects

For EVERY integer n>=32 set m=n+1,L=log n,h=pi/m. Initially take
alpha,beta>=0,rho=alpha+beta<=1 and define

    a=(cos alpha+cos beta)/2, p=sin alpha,q=sin beta,
    d=(q-p)_+,t=beta/pi,
    T_n=Eout(phi)-aEout(0)+(d/pi)Rlog.

Eout and Rlog are EXACTLY the accepted D07/D25/D37 operators, with
the same six removed polynomial labels, weights and finite origin. Then

    T_n<=rho[(23/3)L+50]/n+beta(17L+27)/n^2.          (1)

The ENTIRE CLOSED signed diamond |alpha|+|beta|<=1 is included under
the inherited separate-absolute-phase convention, with |beta| in(1).
Both axes, phasezero, both degree parities, every coefficient/root switch,
weighted periodic cusp and actual polynomial collision are included.
No exchange of n,m or of phase axes is used. The corrected highest
first-coordinate coefficient remains ONE, with original endpoint weights.

This is a ONE-SIDED bound for the entire literal T block, including
its scalar log. It is not a bound on Eout or Rlog separately, nor on
the complete finite error. Ordinary/retained rows, Rmesh and the true
origin conversion remain separate. In particular full D13, the stronger
mixed no-log-linear target and any new global onset remain OPEN.

## 1. Match the complete operators on the NEW phase domain

For0<=tau<=1 define

    Q_tau[G]=(1/m)sum_(k=2)^(m-2)G(h(k+tau))
                                      -(1/pi)integral_0^pi G(z)dz.

The original removed labels are{0,1,2m-2,2m-1,m-1,m}; each ordinary
mesh has m-3 samples. Its ACTUAL centered-cell initial holes have
lengths h(3/2+t),h(5/2-t), total4h, and central holes h(3/2-t),
h(1/2+t), total2h. Since0<=t<=1/pi<1/3, all retained cells lie in
[h/2,pi-h/2], and the holes stay in their stated initial/central halves.
No collision-dependent mask, changed reference or off-grid actual row
is introduced. D37 rebuilt this geometry on the closedrho1 domain.

Let f(x)=Phi_0(1/2+x/(2pi)) be the SAME even2pi-periodic profile,
with its continuous weighted values. Put e=rho,delta=alpha-beta and

    ce=cos(e/2),cd=cos(delta/2),a=ce*cd,
    N_L=ce f(z+delta)+cd f(z-e),
    N_R=ce f(z-delta)+cd f(z+e),N0=2f(z),
    V_s=N_s-aN0,V0=V_L(0)=V_R(0),
    d0(z)=1/[2sin(z/2)]-1/z,
    P_s=(V_s(z)-V0)/z+V_s(z)d0(z).

Let I_s be the original generic cancellation integral on the two
folded sides v_L=z,v_R=2pi-z, with

    C(v)=(p-q-2a cot(v/2))/4,
    D(v)=(p+q+2a cot(v/2))/4,
    I(C,D,v)=int_0^pi[|C cot x+D cot(x+v)|
                                -|C cot x|-|D cot(x+v)|]dx,
    C_s(z)=I_s(phi,z)-aI_s(0,z)-d log(pi-z).

The bounded integral and all weighted profiles keep their original
zero/root/coalescing conventions; no unweighted pole is assigned an
actual polynomial-row value. D37's exact profiles, before any estimate,
give the SAME algebraic decomposition as E09:

    T_n=L{Q_t[g_L]+Q_(1-t)[g_R]}
       +Q_t[P_L]+Q_(1-t)[P_R]
       +(Q_t[C_L]+Q_(1-t)[C_R])/pi
       +Shift+(d/pi)Rlog,                            (2)
    pi*g_L=max(q,p-Z),pi*g_R=max(-q,p-Z,q-2Z),
    Z=2a cot(z/2),
    Rlog=(Q_t+Q_(1-t))[log(pi-z)].

The last equality is the EXACT actual finite operator, not a leading
logarithm match. C_s already contains -d log(pi-z); its separate Rlog
must remain in(2). Paying both complete allowances below is conservative
and does not double-count the scalar log in a later telescope.

The literal baseline shift remains

    Shift=(a/m)sum_(k=2)^(m-2)
      [F0(h(k+t))+F0(h(k+1-t))-F0(hk)-F0(h(k+1))],
    F0(z)=(L/pi)[2cot(z/2)-4/z]
       +2[f(z)-f(0)]/z+2f(z)d0(z)
       +[2cot(z/2)log(sin z)-4log z/z]/pi.

Accepted E02's paired Shift theorem is ALREADY valid onrho<=1:

    |Shift|<=beta(17L+27)/m^2.                       (3)

Its two boundary first differences and disjoint interior second
differences are unchanged. It is not set to0 by symmetry.

## 2. Prove the paired L coefficient is nonpositive onrho1

D37 section6 establishes the displayed max identities onrho<=1
directly from A(v_L)=max(p,q+Z)/pi and
A(v_R)=max(p,|q-Z|)/pi. Thus no E09 half-guard is extended by assertion.
Here a>=49/64>0, so Z decreases from infinity to0 on[0,pi]. Define

    v_L=g_L-q/pi=(p-q-Z)_+/pi,
    v_R=g_R+q/pi=max(0,p+q-Z,2q-2Z)/pi.

They are continuous, nonnegative and nondecreasing, including endpoints
and every max switch. For ANY such G and0<=tau<=1, the disjoint right
rectangles [h(k+tau),h(k+tau+1)] lie in[0,pi] for2<=k<=m-2.
Their integrals dominate h times the corresponding left sample; adding
the remaining nonnegative intervals gives Q_tau[G]<=0. This comparison
does not change the centered-cell geometry for other error terms.

Because Q_tau[1]=(m-3)/m-1=-3/m independently of tau, the opposite
constants cancel EXACTLY. Therefore

    Q_t[g_L]+Q_(1-t)[g_R]=Q_t[v_L]+Q_(1-t)[v_R]<=0.   (4)

Since L>=0, the complete first term of(2) is nonpositive at EVERY
finite n and every wide phase. No fixed-phase limit or root smoothness
is used. All other charges are retained.

## 3. Global scalar facts used for the NEW wide pole estimate

Accepted C08/N1 gives0<f<=1 globally,Lip(f)<2, and |f''|<1 on
each OPEN smooth period. Accepted C04 supplies the FULL measure bound

    mu=d f'<=(3/pi^2)dx.

Its total mass on the circle is0, so its positive and negative Jordan
masses agree. Thus its full periodic total variation, INCLUDING the
negative atom, obeys

    |mu|(circle)=2mu_+(circle)<=12/pi<4.             (5)

This is not a smooth-density-only estimate. The weighted f is continuous
and f' is BV. Also f'(0)=0. No smooth derivative through the periodic
cusp at odd multiples of pi is asserted.

We use the accepted E09 bound |f'''|<13/20 on the ENTIRE smooth
principal interval, whose domain is independent of phase radius. To
make that scope explicit, reconstruct it from E07's exact identity:

    f(x)=f(0)cos(x/2)+2int_0^(1/2)
                         [cos(xt)-cos(x/2)]/cos(pi*t)dt.

The differentiated numerator N=t^3sin(tx)-sin(x/2)/8 vanishes at
t=1/2. For |x|<=pi its t derivative is at most3/4+pi/8<23/20.
The sine chord cos(pi*t)>=2(1/2-t) bounds its quotient by23/40.
The factor2 and interval length1/2 cancel in this bound; the exterior
term is at most f(0)/8<3/40. Hence

    |f'''(x)|<13/20, -pi<x<pi.                     (6)

E07 justifies ordinary differentiation by the same endpoint-cancelled
dominator, with finite one-sided limits. Thus(6) is not an old
rhohalf phase estimate being applied onrho1.

## 4. Rebuild V,V0 and the initial quotient onrho<=1

Write r=ce+cd-2a. The exact cosine estimate gives

    0<=r<=(e^2+delta^2)/8<=rho^2/4<=rho/4.

Expanding each V_s as two translated f differences plus r*f, using
the GLOBAL Lipschitz bound and0<f<=1, proves

    |V_s|<=2(|delta|+e)+r<=17rho/4.                 (7)

At z=0, the translated arguments are within[-1,1]. Ordinary smooth
second derivatives and f'(0)=0 give |f(b)-f(0)|<=b^2/2. Therefore

    |V0|<=(delta^2+e^2)/2+r
          <=5(delta^2+e^2)/8<=5rho^2/4<=5rho/4.    (8)

On the initial half0<=z<=pi/2, ALL shifted arguments remain in
(-pi,pi), since |delta|,e<=1<pi/2. Consequently both smooth derivative
estimates apply there, with no atom crossed. They give the NEW bounds

    |V_s'|<=|delta|+e+2r<=5rho/2,
    |V_s''|<=(13/20)(|delta|+e)+r<=31rho/20.        (9)

Keep the quotient intact before differentiating:

    d/dz[(V_s(z)-V0)/z]
       =[zV_s'(z)-V_s(z)+V0]/z^2
       =z^-2 int_0^z w V_s''(w)dw.

It is bounded by31rho/40 including its continuous z=0 limit. Its
initial variation is at most31pi*rho/80<31rho/25. For the product,
the accepted increasing0<=d0<=1/5 gives

    Var_[0,pi/2](V_s*d0)
       <=(17rho/4)(1/5)+(1/5)(5rho/2)(pi/2)
       <33rho/20,

using pi<16/5. Hence, for EACH side,

    Var_[0,pi/2](P_s)<=289rho/100,
    sup_[0,pi/2]|P_s|<=5rho/2+17rho/20=67rho/20.   (10)

The variation comparison is strict at positive rho and read weakly
at zero. No artificial rho log m term is created by separating the
two internally cancelling quotient derivatives.

## 5. Central variation with the periodic atom retained

On I=[pi/2,pi], for every |b|<=1 the translated interval enlargement
has length at mostpi/2+2<2pi. The measure translation argument gives

    Var_I[f(.+b)-f(.)]
       =int_I|f'(z+b)-f'(z)|dz<=4|b|,              (11)

by Tonelli and(5): each measure point is counted for a set of z of
length at most |b|. The total variation on an interval shorter than
one period is at most a full periodic total, including the atom. No
smooth Taylor estimate through that atom is used.

The two translations in V_s thus cost at most4(|delta|+e)<=8rho.
Its residual r*f term has variation at most pi*r<4r<=rho^2<=rho,
by Lip(f)<2 and the length pi/2. Therefore

    Var_I(V_s)<=9rho.                              (12)

Use the exact P_s=V_s/[2sin(z/2)]-V0/z on I. The first weight has
sup/variation at most3/4,1/4; the second at most2/3,1/3. Equations
(7),(8),(12) give, for EACH side,

    Var_I(P_s)<=[27/4+17/16+5/12]rho=395rho/48,
    sup_I|P_s|<=[51/16+5/6]rho=193rho/48.           (13)

The profiles are continuous at the initial/central split, so its two
variation estimates add with no partition jump. Piecewise absolutely
continuous/BV derivatives and their atoms are included as above.

The normalized midpoint BV error on actual cells is the SUM of both
side variations divided by2m. Initial holes cost their total4h times
the initial supremum, divided bypi; central holes cost2h similarly.
Thus every cell and all FOUR holes give

    |Q_t[P_L]+Q_(1-t)[P_R]|
       <=(rho/m)[289/100+395/48+4(67/20)+2(193/48)]
        =(39073/1200)(rho/m)<=33rho/m.              (14)

Indeed39073<39600. The two midpoint factors are included; neither a
side nor an initial/central hole has been dropped. This is the complete
NEW wide pole estimate; E09's near30 is not transferred to this domain.

## 6. Retain the complete wide cancellation, scalar log and Shift

Accepted D37 section6b independently rebuilt, on CLOSEDrho<=1,

    |Q_t[C_L/pi]+Q_(1-t)[C_R/pi]|
                          <=rho[175/4+20logm]/(pi*m). (15)

It rechecks the initial no-root margin a-P/2>=17/64, the entire
central parameter box and generic J formulas, and the actual small-
mesh root-free alternative rho<=epsilon^2/8. In that case the exact
criterion is s*sin(e)>=p/2; the other case uses its logarithmic
parameter-integral bound. All max/coalescing/root transitions and
BOTH integrable endpoint envelopes on the actual holes are charged.
This is an already accepted WIDE theorem, not D25's half quantifier.

The accepted full-phase D07 log-mesh estimate is

    |Rlog|<=[3logm+log2+2logpi+2]/m.                 (16)

Here d<=q<=beta<=rho. Together with(3),(4),(14),(15), it proves

    T_n<=(rho/m){33+
          [23logm+175/4+log2+2logpi+2]/pi}
                         +beta(17L+27)/m^2.        (17)

Every term in(2) is accounted for. No ordinary row, retained row or
actual-origin charge was added to or removed from T in this process.

Use pi>3,log2<7/10,logpi<23/20,logm<=L+1/32. The positive braces
in(17) are less than

    (23/3)L+33+65/4+23/96
        =(23/3)L+4751/96<(23/3)L+50.

Replace m by n in the positive denominators to obtain(1). The number
4751/96 is GREATER than49: this aggregation proves50, not49. That
fact does not refute a different proof of49 or sharper true T bounds.
All proposed constants were fixed in the parent release before checking.

At rho0, every exact difference, Shift and log charge vanishes, so
(1) is literal equality zero. For each fixed phase the RHS decreases
for ALL real n>=32: the derivative numerators of(c logn+50)/n and
(17logn+27)/n^2 are c-c logn-50<0 and17-2(17logn+27)<0, respectively,
where c=23/3. These are scalar allowance statements, not actual T
monotonicity or finite Padua objects at noninteger degrees.

## 7. Separate Rmesh and full-telescope application boundary

The exact complete D07/D37 telescope remains

    delta_a E=delta_a Erow+delta_a Eret+delta_a Rmesh+T_n,
    E=S_n-M_infty,delta_a X=X(phi)-aX(0).

Accepted D37 section5 separately proves, on the SAME n>=32,rho<=1,

    |delta_a Rmesh|<=rho/(2n).                       (18)

Thus a later complete wide comparison may combine(1) with(18) and
its SAME actual ordinary/retained estimates. It must NOT also add the
old combined mesh/logrho(L+7/3)/n: the scalar log is ALREADY inside
T_n. The exact true-origin conversion remains
E(phi)-E(0)=delta_a E-uE(0), with its own legitimate lower/absolute
origin allowance. No origin term is hidden in this T theorem.

No completed-model formula or physical floor/corner domain changes.
The finite ell_n|alpha| cusp and fractional true-model axis obstruction
remain intact. Full D13 and stronger fixed-near/interior mixed targets
remain OPEN. E14's unfrozen main comparison is not a premise; no320
endpoint, actual S/Lambda value, new degree or runtime saving is asserted.

## Provenance, registration and execution boundary

2026-11-07. Requested Codex gpt-6.1-sol xhigh; actual serving metadata
unexposed. Rules63c70b7,input84956ade8cfc5f9d6f309a5c8c379d7e14cd3337.
The complete gate return precedes root's separate mathematical release.
Root prospectively registered the EXACT claim/domain/constants/route
in durable LOG BEFORE the author's independent checks. The first
reasoning checks preceded the local idea inventory; that exact narrower
order is disclosed there and in the attempt, not restated as an earlier
local-file timestamp. Root requests independent application of the
actual registration rule, without automatic waiver or violation finding.

This is one support within SAME E14, not a16th research round. Only
the three new E14-wide-signed-outer prose files changed. No source,
script/import/scalar/endpoint/native/phase/root/quadrature/degree/
threshold/board/compile/control/scientific/pack/shared/Git job or
mutation. Accepted older files remain frozen. Distinct D30 review/root
adoption are required before a lead consumes this new wide bound.


## Root adoption —2026-11-07

Root adopts this exact 14318-byte frozen proof (SHA256 c7aeba3d6080f16cc8016e83949f27d6f9de6d36793d9a03cc4c5d171528e8a8), after distinct [wide signed-outer ACCEPT](../independent-checks-E14-wide-signed.md), report 19156 bytes, SHA256 d0c3699f97e34c43725b3276bb5585d4a9ccf477cb56413058bb8fd2ff55a266. The original proof prefix remains unchanged. The literal T50 bound holds on the CLOSED signed radius-one domain for every integer n>=32, with its stated scalar monotonicity. Rmesh, ordinary/retained rows and actual-origin charges remain separate. No global320 theorem, endpoint computation or runtime/source change follows from this support alone. No new finding or protocol violation was identified; prior findings and the final Claude audit remain separate.
