# PD-N?argmax-bridge-E03-unified — A logarithmic linear charge survives in the complete signed error

ID kind: PD-N. Aliases: actual-origin finite-error cusp; complete one-sided
mixed-bound obstruction; nonuniform phase/degree cancellation.
Split from: the stronger no-log-linear sufficient charge proposed during
E03. Split into: none. The original D13 absolute target and the broader
one-sided quantitative continuation remain OPEN, without narrowing.

## Statement

Use EXACTLY D13's finite corrected primitive and completed model. For each
integer n>=32 put m=n+1,L=log n,H=1+L and

    E_n(phi)=S_n(phi)-M_infty(phi,L),
    a(phi)=(cos alpha+cos beta)/2,
    delta_a E_n=E_n(phi)-a(phi)E_n(0), rho=|alpha|+|beta|.

For every r in (0,1/2], every integer N>=32 and every pair of finite
nonnegative constants C,K, there exist an integer n>=N and a phase
0<alpha<=r,beta=0 such that BOTH

    E_n(alpha,0)-E_n(0)>C*alpha/n+K*H*alpha^2/n,
    delta_a E_n(alpha,0)>C*alpha/n+K*H*alpha^2/n.          (1)

In particular a uniform ONE-SIDED C*rho/n+K*H*rho^2/n upper for the
COMPLETE actual-origin error fails on every nontrivial near diamond.
The same conclusion holds if the quadratic coefficient K*H/n is replaced
by ANY finite coefficient q_n at each fixed n. No absolute values are
needed in this negative statement.

The precise finite term in the decisive test is the accepted PD-T220 slope

    ell_n=(nm)^(-1) sum_(k=1)^floor(n/2) cot(k*pi/n)>0,
    E_n(alpha,0)-E_n(0)=ell_n*alpha+o_n(alpha),
    delta_a E_n(alpha,0)=ell_n*alpha+o_n(alpha).          (2)

We use ell_n here to distinguish this slope from L=log n and from the
unrelated boundary cotangent Lebesgue constant. It is PD-T220's L_n.
Its inherited asymptotic is n*ell_n=(log n)/pi+O(1).

## Definitions and preserved normalization

For h_0=1,h_i=2 when i>0, let

    D_n(u,v)=sum_(i+j<=n) h_i*h_j*cos(iu)*cos(jv),
    Gpoly_n(u,v)=D_n(u,v)-cos(nu),
    delta_r=(1-r) mod2,
    u_rk=(delta_r*pi+alpha+2k*pi)/n,
    v_r=(r*pi+beta)/m,
    F_rk=(-1)^delta_r*Gpoly_n(u_rk,v_r)/2,
    R_r=sum_(k=0)^(n-1)|F_rk|,
    S_n=(nm)^(-1)sum_(r=0)^(2m-1)R_r.

The highest first-coordinate coefficient of Gpoly is ONE. These are the
literal unequal n,m meshes and polynomial values at every collision.
The equivalent physical reflection formula has endpoint factors e_j,f_r
equal to1/2 at their respective endpoints and1 otherwise:

    F_jr(alpha,beta)=(-1)^j*Gpoly_n((j*pi+alpha)/n,
                                      (r*pi+beta)/m)/2,
    S_n=(nm)^(-1)sum_(0<=j<=n,0<=r<=m,j+r odd)
               e_j*f_r*sum_(sigma,tau=+/-1)|F_jr(sigma alpha,tau beta)|.

No endpoint factor is changed in passing between these formulas. In
particular S_n(0)=Lambda_c(n), the ACTUAL finite corner value. The exact
model, including its constant, is

    M_infty=B0*L^2+b_full*L+C_infty,
    B0=4a/pi^2, C_infty=E_infty+K0,
    b_full=2U0/pi+[8a log2+4a loga
                         +2(alpha sin alpha+beta sin beta)]/pi^2,
    U0=ce*Phi0(1/2+(alpha-beta)/(2pi))
                       +cd*Phi0(1/2+(alpha+beta)/(2pi)),
    ce=cos((alpha+beta)/2), cd=cos((alpha-beta)/2).

Here phases in the model are absolute phases, exactly as in D13. Phi0
is the original continuous periodic weighted profile. These formulas are
the exact coefficient definitions from C06/D02, not an extension of C06's
separate n>=10^6 upper theorem to smaller degrees.

## Status, dependencies and scope of rejection

Overall status: **PROVED developer paper negative theorem**, pending
distinct mathematical audit and root adoption. Candidate disposition:
**REJECTED: refuted**, only for the no-log-linear complete-error family
specified in (1). The finite identity and first-variation calculation
below are proof diagnostics of this negative statement, not separate
claims that resolve the broad target or make it PARTIAL.

Dependencies are accepted PD-T216's exact periodic/physical normalization,
PD-T220's fixed-degree primitive cusp, D13's exact telescope and unchanged
model, D05-fixed-special-rows and D07-global-outer/global-mesh definitions,
C06's exact b_full identity, and D10-relative-constant / D10-axis-obstruction's
actual completed-constant behavior. The latter was accepted by the distinct
D10 review. The complete-error rejection can alternatively use only D10's
accepted one-sided near modulus, as shown below.

The E03 row and outer/log developer drafts suggested the useful coupling
diagnostic but are NOT accepted premises of this proof. The exact algebra
below follows directly from accepted D05/D07 definitions. Their fixed-phase
asymptotics are discussed only with their original quantifiers. No external
theorem, priority claim, numerical job, fit or source import is used.

## Proof

### 1. One exact finite operator, with ordinary rows and all holes retained

First take alpha,beta>=0,rho<=1/2. Put h=pi/m,t=beta/pi,
t_L=t,t_R=1-t,d=(sin beta-sin alpha)_+,v_L(z)=z,v_R(z)=2pi-z.
The exact six labels and ordinary complement are

    A6={0,1,2m-2,2m-1,m-1,m}, O6={0,...,2m-1}\A6.

Use the complete weighted D05 row profile Hrow(L,v), its polynomial-
compatible continuation, the unchanged Delta2=E_infty-E2 and endpoint
constant C2. Write

    J6=(nm)^(-1)sum_(r in A6)R_r,
    B=(1/m)sum_(r in O6)Hrow(L,v_r),
    T(L,z)=[U0+(4a/pi)(L+log z)]/z,
    ell(z)=log(pi-z),
    F_s(z)=Hrow(L,v_s(z))-T(L,z)-(d/pi)*ell(z),
    P=(1/m)sum_s sum_(k=2)^(m-2)T(L,h(k+t_s)),
    Clog=(1/m)sum_s sum_(k=2)^(m-2)ell(h(k+t_s)),
    I_F=(1/pi)integral_0^pi(F_L+F_R)dz.

Each integral here is of the COMPLETE regularized expression; no divergent
integral is assigned a separate value. D05's weighted continuation covers
every root/coefficient/collision transition in these expressions. The
ordinary cells have exact lower and upper boundaries

    l_L=h(3/2+t), l_R=h(5/2-t),
    u_L=pi-h(3/2-t), u_R=pi-h(1/2+t).

Thus both initial holes and both central holes remain present. The operator

    Q_tau[f]=(1/m)sum_(k=2)^(m-2)f(h(k+tau))
                                  -(1/pi)integral_0^pi f

has precisely these samples and the full integral, not just the cell union.
Its omission charges cannot be discarded by a formal pairing.

The accepted definitions give, without any estimates,

    Kfixed=J6+B+Delta2,
    Gintermediate=J6+Delta2+P+(d/pi)*Clog+I_F,
    Erow=S-Kfixed, Eret=J6-C2,
    Eout=B-P-(d/pi)*Clog-I_F,
    Rlog=Clog-2(log pi-1)=(Q_t+Q_(1-t))[ell].

Consequently ordinary Hrow terms cancel EXACTLY in the complete sum:

    delta_a(Erow+Eret)+delta_a Eout+(d/pi)Rlog
       =delta_a[S-P-I_F-Delta2-C2]
                            -(2d/pi)(log pi-1).             (3)

Here d(0)=0 is essential. In particular neither an uncoupled absolute
outer estimate nor deletion of a constant row allowance produced (3).
Adding the unchanged D13 scalar mesh remainder gives

    delta_a E_n=delta_a[S-P-I_F-Delta2-C2]
                 +delta_a Rmesh-(2d/pi)(log pi-1).          (4)

For a direct sign/normalization check, D07's exact formulas are

    Rmesh=P-D0*H2-B0*G2-B0*L^2-2D0*L,
    E2=C2+D0*H2+B0*G2,
    I_F=(b_full-2D0)L+K0-(2d/pi)(log pi-1).

Insert these and Delta2=E_infty-E2 into (4): the result is exactly
delta_a[S-B0 L^2-b_full L-C_infty], with no residual constant. H2,G2
are the original h_2(t)+h_2(1-t),g_2(t)+g_2(1-t); P is D07's Tmesh
with exact upper index m-1=n. This verifies that ALL ordinary/retained,
scalar-log, initial-hole and central-hole terms are in the tested error.
The actual row values remain in S even though explicit J6 cancels.

### 2. The complete model has zero first axis variation

Restrict beta=0,alpha down to0 at FIXED n. The function
f(x)=Phi0(1/2+x/(2pi)) is smooth and even near0 by its reciprocal-pair
series (also written in D10-relative-constant). Therefore

    a=(1+cos alpha)/2=1+O(alpha^2),
    U0=2cos(alpha/2)f(alpha)=U0(0)+O(alpha^2).

Since a remains positive, a loga=O(alpha^2), and alpha sin alpha is
O(alpha^2). The exact displayed b_full formula proves

    B0(alpha,0)-B0(0)=O(alpha^2),
    b_full(alpha,0)-b_full(0)=O(alpha^2).                  (5)

D10-axis-obstruction's supporting exact limit concerns THIS completed
constant, not an approximate model bridge:

    C_infty(alpha,0)-C_infty(0)
          =k_frac*alpha^(3/2)+o(alpha^(3/2)),
    k_frac=(4/pi^2)integral_0^1 sqrt(1-y^4)dy>0.          (6)

Equations (5)–(6) imply

    M_infty(alpha,0,L)-M_infty(0,L)=o_n(alpha).           (7)

Only fixed finite L is used here. No phase derivative of a moving root
inside an unjustified integral is taken: (6) is the accepted complete
constant asymptotic with its own justified coalescing-root proof.

There is also a weaker independent route sufficient for the rejection:
D10-near's one-sided bound gives the model increment at most
O(alpha^(3/2))+O(alpha^2[1+log(1/alpha)])+O_n(alpha^2)=o_n(alpha).
Together with the finite S slope this yields the needed lower liminf for
the error even without using the equality (6).

### 3. The actual finite polynomial cusp survives

PD-T220, with exactly the periodic normalization above, proves

    S_n(alpha,0)-S_n(0)=ell_n*alpha+o_n(alpha).            (8)

For the finite zero-mask check: at the origin the zero terms are on
r=m,j<n,j+n even. The common endpoint (j,r)=(n,m) has polynomial value
n and is nonzero. On the zero row the corrected numerator gives
partial_alpha F_jm=-(1/2)tan(j*pi/(2n)). The original f_m=1/2 and
four reflections contribute e_j*tan(j*pi/(2n))/(nm) per physical j.
Putting j=n-2k gives ell_n. The possible j=0 endpoint has derivative
zero, so its e_0=1/2 changes no slope. Every other reference value is
nonzero; its signed smooth first derivatives cancel under reflection.
This is the actual polynomial calculation for both degree parities,
not an unweighted pole limit or the first variation of physical lambda.

Subtracting (7) from (8) proves the first equality in (2). Since
1-a=O(alpha^2) and E_n(0) is finite at fixed n, it also proves the second.
Thus any putative uniform cancellation of the complete linear coefficient
must fail: its exact finite right derivative is ell_n, not zero.

### 4. Uniform one-sided contradiction and the order of limits

Suppose either of the corresponding upper inequalities with <= in place
of > in (1) held for all n>=N and all 0<=alpha<=r. Fix n FIRST, divide
that inequality by alpha and let alpha decrease to0. Equation (2) forces

    n*ell_n<=C.                                         (9)

This is impossible for all n, since PD-T220 gives
n*ell_n=(log n)/pi+O(1). An elementary quantitative divergence check
avoids even that asymptotic: for 1<=k<=floor(n/4), sin x<=x and
cos x>=1/2 at x=k*pi/n give cot(k*pi/n)>=n/(2*pi*k). Writing
H_j=sum_(k=1)^j 1/k for the harmonic sum, hence

    n*ell_n=(1/m)sum_(k=1)^floor(n/2)cot(k*pi/n)
        >=[n/(2*pi*m)] H_floor(n/4)
        >=H_floor(n/4)/(4*pi), n>=4.                    (10)

Choose any n>=N for which the last harmonic quantity exceeds C.
At this one fixed n, (2) and sufficiently small positive alpha<=r
make BOTH strict inequalities (1) hold; their two o_n terms can be
controlled simultaneously. Every finite q_n*alpha^2 vanishes after
division by alpha, proving the stated extension. There is no interchange
of a fixed-phase degree limit with a fixed-degree phase limit.

### 5. True-origin conversion and the preserved larger target

For u=1-a the identity remains exactly

    E_n(phi)-E_n(0)=delta_a E_n-u*E_n(0)
                  <=delta_a E_n+u*E0(n),                (11)

where E0(n) is the accepted complete absolute origin allowance. The
signed E_n(0) is not replaced by +E_n(0). Both the exact conversion
and its u*E0 allowance have zero alpha derivative at each fixed n;
neither can remove the obstruction. No AN or other baseline constant
has been deleted from a downstream proof.

If a complete one-sided charge has the form c_n*rho+o_n(rho), it MUST
satisfy c_n>=ell_n. For D13's still OPEN logarithmic linear form this
only imposes the necessary condition K1>=1/pi asymptotically; it is
compatible with that target and does not disprove it. In particular
this negative result does not justify an upper with coefficient ell_n:
a fixed-degree derivative is not a uniform neighborhood estimate.

## Limits and next unresolved step

The outer/log draft's negative fixed-positive-alpha logarithm and the
retained-row draft's positive fixed-positive-alpha logarithm can agree
at that order while (2) still holds. Their stated fixed-alpha estimates
are not uniform as alpha approaches the mesh scale or zero. The exact
surviving finite term identifies why their cancellation cannot establish
the proposed no-log-linear bound on a whole diamond.

A cusp-aware continuation is to test an explicit upper retaining
ell_n*|alpha| and a separately justified beta-direction charge, then bound
the remaining signed error across the alpha comparable-to-1/n transition.
One possible falsifiable target is

    E_n(phi)-E_n(0) <= ell_n*|alpha|+C*rho/n+K*H*rho^2/n,  (12)

or the corresponding delta_a E_n inequality with the FULL conversion
(11) charged. This is **deferred / OPEN**, not a proved upper or an
assertion that the exact alpha slope is the only crossover obstruction.
The new term escapes precisely the necessary derivative test (9), and
a failure in a finite moving-root/mesh transition would defeat (12).
No further candidate development is claimed in this bounded block.

The full D13 absolute target remains OPEN. A materially smaller complete
one-sided allowance remains OPEN. The physical Lebesgue argmax, accepted
global onset and finite certified degrees are unaffected: this is a
primitive-minus-model error, not the physical defect-corrected function.

## Checks, sources and history

Paper derivation only; no scalar, numeric, native, phase, degree, threshold,
compile, source import or pack job. The fresh complete registry gate,
shortlist, literature INDEX coverage and prospective kill test are in the
same-stem idea/attempt. No historical priority or external theorem transfer.
Independent mathematical review/root adoption is required; root alone
owns Git, shared records and any global ID allocation.

2026-11-07, parent-assigned Astra ultra, serving metadata unexposed;
rules/input `5fda5bbf8d44e10a31609161500d3b2881635b85`. This scoped negative
statement preserves the stronger candidate's original wording and the
larger OPEN target. Its exact operator and derivative are supporting
diagnostics within the proof, not a claim to complete a useful upper.


## Root adoption after distinct focused audit —2026-11-07

Root adopts the exact full-error operator/cusp and scoped ONE-SIDED no-log-linear obstruction. Any proposed uniform C*rho/n+K*H*rho²/n estimate on a whole near diamond fails: fixed-n alpha right slopeell_n forces n*ell_n<=C, contradicting elementary harmonic divergence. The correct limit order is preserved. This does not reject D13's logarithmic-linear target, a cusp-aware upper bound or actual argmax.

Distinct [review](../independent-checks-E03-unified-error.md), SHA256
818f912415d25f474807955aebe8a66af8dface5d10579bc95a2e59cc330db18, accepts the unchanged reviewed prefix
490fbd489c373565e66cf6c7d44b0aa7d86378fd7ab04e1041a981fcf5c74cee.
Full D13 remains OPEN. No numerical/source/native/pack job occurred.
Current global onset768 and residual719 are unchanged; final Claude is separate.

## Audit-02 dated current-state pointer — 2026-11-07

The onset768/residual719 line above records the state at this component's
adoption. Current adopted global onset320 and273 residual OPEN degrees
43–62,65–158,161–319 are recorded in [current report](../report.md) and
[E14's mathematical adoption](E14-assembly320.md). This pointer leaves
the scoped obstruction and its original accepted proof/status unchanged.
Full D13 remains OPEN; P1–P4 remain unwaived and the branch remains WORK.
