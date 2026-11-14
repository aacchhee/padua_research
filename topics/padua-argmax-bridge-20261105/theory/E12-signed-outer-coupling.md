# E12 — Match both endpoint logarithms before bounding the outer error

ID kind: PD-T. Aliases: opposite initial logarithms; unequal-offset log
cancellation; finite beta-axis outer upper. Split from the OPEN fixed-near
one-sided mixed bound for the literal outer-plus-log block. Split into none.

2026-11-07, requested Astra ultra, serving metadata unexposed. Paper
developer theorem; distinct mathematical/protocol audit and root adoption
are required. The gate-only prefix and subsequent explicit root release
are recorded in the companion idea/attempt. No old artifact is edited.

## Statements and exact scope

Let n>=32 be an integer, m=n+1, h=pi/m, L=log n, and use the original
folded absolute phases alpha,beta>=0, rho=alpha+beta<=1/2. Put

    a=(cos alpha+cos beta)/2, p=sin alpha, q=sin beta,
    d=(q-p)_+, t=beta/pi,
    T_n=Eout(alpha,beta)-a Eout(0,0)+(d/pi)Rlog.

Eout and Rlog are the EXACT accepted D25/E02/E03 operators, not a changed
reference or an independently defined error. Two conclusions hold.

**A. Fixed-phase logarithmic coefficient.** For EACH FIXED phase in the
closed half diamond, along all integer degrees tending to infinity,

    T_n(alpha,beta)=-(2p/pi)(log n/n)+O_(alpha,beta)(1/n).       (1)

The implicit constant may depend on phase. This is not a uniform moving-
phase theorem. At the zero phase T_n=0 identically. In particular the
beta-axis coefficient is ZERO, not a positive multiple of q log n/n.

**B. A finite uniform beta-axis upper.** For EVERY integer n>=32 and
EVERY 0<=beta<=1/2,

    T_n(0,beta)<=40beta/n.                                  (2)

Both endpoints are included. This is the entire literal T block, with
its scalar log, both pole profiles, paired origin shift and all actual
omitted cells. It is not a bound for Eout or Rlog separately. Separate
absolute-phase symmetries give the inherited signed-axis formulation;
no exchange of n and m or of the phase axes is used.

The full rho<=1/2 mixed family C rho/n+K(1+log n)rho^2/n remains OPEN.
So does an analogous uniform fixed-near cone estimate. The COMPLETE
finite error still has its real ell_n|alpha| cusp from E03. Ordinary and
retained-row terms, scalar Rmesh and actual-origin conversion remain
outside T. No global onset, degree coverage or physical corner theorem
follows from(1) or(2) alone.

## 1. Literal decomposition and inherited complete bounds

For0<=tau<=1 define

    Q_tau[G]=(1/m)sum_(k=2)^(m-2)G(h(k+tau))
                                  -(1/pi)integral_0^pi G(z)dz. (3)

Each mesh has m-3 samples. Its initial centered-cell hole has length
h(3/2+tau), and its central hole has length h(3/2-tau). Thus the two
meshes t,1-t have initial holes h(3/2+t),h(5/2-t), and central holes
h(3/2-t),h(1/2+t). Their totals remain4h and2h. The original removed
polynomial labels are{0,1,2m-2,2m-1,m-1,m}. All endpoint weights,
actual polynomial collision values, unequal n,m parity meshes and the
exceptional highest first-coordinate coefficient ONE remain unchanged.

Use E09's literal pole differences P_L,P_R and cancellation differences

    C_s(z)=I_s(alpha,beta;z)-a I_s(0,0;z)-d log(pi-z).

With Z(z)=2a cot(z/2), the accepted exact identity is

    T_n=L{Q_t[g_L]+Q_(1-t)[g_R]}
       +Q_t[P_L]+Q_(1-t)[P_R]
       +(Q_t[C_L]+Q_(1-t)[C_R])/pi
       +Shift+(d/pi)Rlog,                                  (4)
    pi*g_L=max(q,p-Z),
    pi*g_R=max(-q,p-Z,q-2Z),
    Rlog=(Q_t+Q_(1-t))[log(pi-z)].

Here Shift is EXACTLY

    (a/m)sum_(k=2)^(m-2)
      [F0(h(k+t))+F0(h(k+1-t))-F0(hk)-F0(h(k+1))],

where F0 is the same origin regularized profile as in E02/E09, including
its L coefficient and endpoint-cancelled finite part. We use the complete
accepted bounds

    |Q_t[P_L]+Q_(1-t)[P_R]|<=30rho/m,
    |Shift|<=beta(17L+27)/m^2.                              (5)

The first bound includes the periodic derivative atom and all four holes;
the second is the paired finite F0 shift, not an independent-grid estimate.
For specificity E09 defines P_s=(V_s(z)-V0)/z+V_s(z)d0(z),
V_s=N_s-2a f(z), d0=1/[2sin(z/2)]-1/z, with the literal weighted
N_L=ce f(z+alpha-beta)+cd f(z-alpha-beta),
N_R=ce f(z-alpha+beta)+cd f(z+alpha+beta),
ce=cos((alpha+beta)/2),cd=cos((alpha-beta)/2). Its continuous quotient
and weighted atom conventions are retained here.

Accepted D25 gives the EXACT initial-half identities

    C_L=q log(sin z)-d log(pi-z),
    C_R=-q log(sin z)-d log(pi-z), 0<z<=pi/2.               (6)

Accepted N1-round6-central-log proves that I_s-d log(pi-z) has a
finite continuous central limit and bounded variation, including all
root/parameter transitions. The origin I_s(0,0;z) on the central half
is2tan((pi-z)/2)log(sin z), also BV and continuous at the endpoint.
These are full operator facts, not observations about sampled collisions.

Dependencies are accepted E03 literal log matching, E09 signed-profile
and pole theorem, E02 paired Shift, D25 initial/root formulas and the
N1 uniform central finite-part proof. Their full relevant records were
read in the gate or refreshed before use. E10/E11 supply current scope
and comparison context but are NOT premises of these two results. No
PD-T271 scalar enclosure, external source theorem or numerical premise
is used. Old chronology findings of accepted E09 are not waived here.

## 2. An endpoint-log quadrature lemma with the actual holes

For any FIXED tau in[0,1], the actual Q in(3) satisfies

    Q_tau[log z]=(3/2+tau)log m/m+O(1/m),
    Q_tau[log(pi-z)]=(3/2-tau)log m/m+O(1/m).              (7)

These estimates can in fact be uniform in tau, but no such strengthening
is required for(1). Here is a direct proof without a Gamma asymptotic.
On the actual centered-cell union, the midpoint error for log z is at
most h^2/8 times the integral of1/z^2, then divided by pi. The union
starts at b h with b=3/2+tau>=3/2, so this error is O(h). The missing
initial integral is

    -(1/pi)integral_0^(bh)log z dz
       =(b/m)log m-(b/m)[log(pi b)-1].

The other hole lies at a bounded positive z and contributes O(1/m).
This proves the first formula. Reflection proves the second, since
its singular hole has c=3/2-tau>=1/2. In particular

    (Q_t-Q_(1-t))[log z]=(2t-1)log m/m+O(1/m),
    Rlog=2log m/m+O(1/m).                                (8)

The midpoint estimate used here also applies to a continuous function
with BV derivative: the error on a cell is bounded by h^2/8 times the
total variation measure of that derivative on the cell. It follows by
the midpoint Peano kernel, whose magnitude is at most h^2/8; summing
disjoint cells includes derivative jumps. The logarithms in(7) are only
used on the union away from their singular endpoint; the missing interval
has been integrated exactly, not put into a false global BV norm.

## 3. Proof of the complete fixed-phase coefficient

Set v_L=g_L-q/pi and v_R=g_R+q/pi. Accepted E09 gives

    pi*v_L=(p-q-Z)_+,
    pi*v_R=max(0,p+q-Z,2q-2Z).                            (9)

For a fixed phase these are zero on an initial neighborhood, continuous
and piecewise smooth, with derivative of bounded variation on the whole
closed interval. Indeed their finitely many active max branches are
smooth away from zero, and only finitely many finite derivative jumps
occur at switches. The zero phase is immediate. Their endpoint values are

    pi*v_L(pi)=(p-q)_+,
    pi*v_R(pi)=max(p+q,2q)=p+q+d.                         (10)

Applying the actual midpoint cells, their O(m^-2) quadrature error and
the central holes give

    Q_t[v_L]+Q_(1-t)[v_R]
      =-{(3/2-t)(p-q)_++(1/2+t)(p+q+d)}/(pi m)
                                                   +O_phi(m^-2). (11)

The initial holes eventually lie inside the zero neighborhoods. The
opposite constants in g_L,g_R cancel EXACTLY because Q_tau[1]=-3/m.

To treat the cancellation profiles, subtract their INITIAL logarithms
before calling a remainder BV:

    B_L=C_L-q log z,  B_R=C_R+q log z.                   (12)

Equation(6) shows that near zero these are respectively
plus/minus q log(sin z/z)-d log(pi-z), which are smooth at zero.
On the central half the N1 theorem just cited gives a finite BV limit
for C_s; log z is smooth there. Thus B_L,B_R are continuous BV on the
FULL interval for each fixed phase, including all root thresholds and
periodic profile conventions. They agree across the artificial pi/2
split because they are the same literal profiles. Consequently

    Q_t[C_L]+Q_(1-t)[C_R]
       =q(2t-1)log m/m+O_phi(1/m).                      (13)

For example the BV midpoint estimate plus all holes bounds each Q[B]
by[Var(B)/2+3sup|B|]/m. Calling C_L+C_R at a common argument BV would
NOT justify(13): the grids differ. Formula(12) matches those grids first.

Insert(8),(11),(13) in(4), using(5). If p>=q, d=0 and the numerator
of the L coefficient from(11) is2p+(2t-1)q; (13) cancels its q part.
If p<q, (11) gives-(1+2t)q, (13) gives(2t-1)q and scalar Rlog gives
2d=2(q-p). Their sum is again-2p. Replacement of log m by L and of m
by n changes only O_phi(1/n) here; L/m^2=O(1/m). This proves(1) with
the fixed phase held throughout, for both degree parities.

This explicitly refutes the root-supplied TEST formula with a positive
beta-axis coefficient. The missing term in that test was precisely(13).
It does not refute the proposed uniform upper family, and it does not
deduce its truth from a nonpositive fixed-phase coefficient.

## 4. Exact finite beta-axis reduction

Now set alpha=0,0<=beta<=1/2. Then

    p=0, d=q=sin beta, a=cos^2(beta/2), t=beta/pi.

The generic N1 cancellation integral at u=p/2=0 is exactly
J(0,s,e)=2s log(sin e) for every s>=0, with its continuous zero case.
Using the actual left/right coefficient magnitudes gives, on ALL0<z<pi,

    I_L-aI_L(0)=q log(sin z),
    I_R-aI_R(0)=[-q+2(q-Z(z))_+]log(sin z),
    g_L=q/pi, g_R=[-q+2(q-Z(z))_+]/pi.                 (14)

These formulas also follow directly by splitting the two cases Z>=q and
Z<q. On the central half they use s_L=q/2+a tan(e/2),
s_R=|q/2-a tan(e/2)|, e=pi-z; on the initial half they agree with(6).
There is no moving numerator-root integral at p=0. The switch Z=q
is retained explicitly. Recombine the d log(pi-z) subtraction in C_s
with the EXACT scalar Rlog in(4) before any estimate.

Define the integrable, possibly negative near-zero function

    G(e)=(q-2a tan(e/2))_+ log(n sin e), 0<e<pi,
    G(e)=0 for e>=beta.                                  (15)

The support statement is exact because q/(2a)=tan(beta/2). The function
is continuous with value0 at e=beta; its logarithmic singularity at e=0
is integrated, not assigned a finite endpoint value. Equations(4),(14)
give the FINITE identity

    T_n(0,beta)=Pole+Shift
      +q/(pi m) log[sin(h(2-t))/sin(h(1+t))]
      +(2/pi^2){h sum_(j=1)^(m-3)G(h(j+t))
                                      -integral_0^pi G(e)de}, (16)
    Pole=Q_t[P_L]+Q_(1-t)[P_R].

To verify the logarithmic boundary term, the common integrals cancel in
(Q_t-Q_(1-t))[log(sin z)]. Reflection of the second finite sum changes
its indices to1,...,m-3 with offset t, while the first is2,...,m-2.
Only the last and first terms remain, giving exactly the ratio in(16).
For the active coefficient term, e=pi-h(k+1-t)=h(j+t) with
j=m-k-1 in1,...,m-3. Thus every original sample and endpoint hole is
preserved. No asymptotic step is involved in(16).

## 5. Uniform signed quadrature on the entire beta axis

Write D for the bracket in(16) and b=h(1/2+t), the EXACT missing first
interval in the reflected right mesh. Its actual cells are centered at
h(j+t), j=1,...,m-3. Their union extends from b to h(m-5/2+t), which
is beyond1/2 for all m>=33; hence it contains the whole remaining support
of G. The only omitted nonzero interval is(0,b).

First retain the sign of that interval. Since0<=q-2a tan(e/2)<=q on
the support, and sin e>=5e/6 for0<=e<=1/2,

    integral_0^b(-G(e))_+ de
      <=q integral_0^infinity[-log(5ne/6)]_+ de
      =6q/(5n).                                         (17)

If beta<=b, every sample is zero and D<=6q/(5n). Suppose beta>b.
Then throughout[b,beta], n sin e>=n sin(h/2)>1: here h/2<1,
sin(h/2)>=5h/12, and5pi*n/(12m)>1 using pi>3,n/m>=32/33.
Put Z_e=2a tan(e/2). On this interval differentiation gives

    G'=-Z_e' log(n sin e)+(q-Z_e)cot e,
    G''=-Z_e'' log(n sin e)-2Z_e'cot e
                                      -(q-Z_e)csc^2 e<=0. (18)

Thus G' decreases up to beta. Extension by zero past beta introduces
the POSITIVE derivative atom of size log(nq), because
Z_e'(beta)=a sec^2(beta/2)=1 and G'(beta-)=-log(nq).
It is incorrect to declare that extension globally concave. Including
that atom gives the exact total variation on[b,infinity):

    Var(G')=G'(b)+2log(nq)
       <=2q/h+2nq.                                      (19)

Indeed G'(b)<=q cot b<=q/b<=2q/h, and log(nq)<=nq.
The variation identity remains valid if G'(b) is negative: it is the
decrease to G'(beta-) followed by the jump to0. All functions are smooth
inside[b,beta], and G is zero beyond, so there are no other atoms.

Apply the BV-derivative midpoint lemma from section2 on the ACTUAL cells:

    h sum_jG(h(j+t))-integral_b^infinity G
       <=(h^2/8)Var(G')
       <=qh/4+nqh^2/4 <(21/20)qh,                       (20)

using nh<pi<16/5. Also nh=pi*n/m>2, so(17)<(3/5)qh.
Combining the signed missing interval with(20), or using the zero-sample
case beta<=b directly, proves the simple UNIFORM bound

    D<=2qh.                                             (21)

This includes beta comparable to h, beta much smaller than h, every
crossing of beta through an actual cell boundary, and both parities.
No fixed-phase constant or exchanged limit is used. Beta=0 is exact zero.

Finally0<=t<1/2 and sine's decreasing sinc imply

    sin(h(2-t))/sin(h(1+t))<=(2-t)/(1+t)<=2.

The nonpole part of(16), using(21), is at most

    q log2/(pi m)+4q/(pi m)<2beta/m.                     (22)

Use(5). For all real n>=32 the function(17log n+27)/n decreases, and
log32=5log2<7/2 gives its value there below173/64<3. Hence

    |Shift|<3beta/n,
    T_n(0,beta)<32beta/m+3beta/n<35beta/n<=40beta/n

for beta>0; equality zero holds at beta=0. This proves the prospective
constant40 in(2), without a scalar job, fit or phase scan.

## Scope, dispositions and remaining obligation

The parent-proposed positive beta-axis coefficient is REFUTED as an
asymptotic formula: initial opposite logarithms on unequal offsets were
missing. This is a scoped correction of an explicitly unproved test,
not an obstruction to any accepted theorem. The fixed-phase coefficient
in(1) agrees with the accepted E03 alpha-axis result and vanishes on the
entire beta axis. It supplies no uniform remainder as phase moves with n.

The uniform finite result(2) follows instead from the exact root-free
axis identity(16), actual cells, signed missing interval and charged
derivative atom. It complements E09's shrinking alpha-axis32alpha/n
bound, but these two axis statements do NOT bound an interior phase.
There is no justified convexity or interpolation between phase axes.

The next cheapest PAPER obligation is to subtract both initial logs in
the actual two meshes, retain the scalar-log coupling, and control the
remaining paired central root terms for p>0 without independent phase-
logarithm overcharges. E11's limiting paired-root majorant is not a finite
quadrature theorem. The full mixed target and full D13 remain OPEN.

The actual-origin identity remains exactly
E(phi)-E(0)=delta_a E-uE(0). Any upper must still use its accepted signed
lower allowance for E(0), or safely +uE0 when |E(0)|<=E0; neither cost
is removed by a theorem about T. Original finite ell_n|alpha| remains.

Only bounded complete reads/searches, clock/hash metadata, paper algebra
and these three owned prose files were used. No scientific script/source/
import/scalar/endpoint/phase/degree/threshold/native/compile/pack action,
extra agent, Git or shared mutation. Current accepted global384 and
residual337 are unchanged. Root owns distinct audit and adoption.


## Root adoption —2026-11-07

Root adopts the exact15979B frozen proof above (SHA256caa32293290497bc0abe20d5dafdde0fa13c54054c76586ff9d2df5b3ddfd6a2), after distinct [E12 signed-coupling ACCEPT](../independent-checks-E12-signed-coupling.md), report20888Bdede6884f9cb67bfbe48dfb522b1b2981608cdfa141d8057988d72e2ae500060. Both fixed-phase leading coefficient and uniform CLOSED beta-axis upper are accepted. Original prefix/gate-only6631B record remain preserved. The fixed-phase remainder is not uniform in phase; the beta-axis result does not cover the interior. Parent positive-beta candidate is refuted by the retained initial unequal-grid logarithms. No new protocol violation was identified under the actual before-expensive-work rule. Upstream findings remain unwaived, full mixed/D13 targets OPEN, and no new onset or numerical/source job is inferred. Final Claude audit is separate.
