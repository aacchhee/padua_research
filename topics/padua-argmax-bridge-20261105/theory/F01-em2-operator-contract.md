# F01 EM2 — Exact operator interface and missing implementation contract

Alias: four signed E14 components; I06 completed-model triage interface.
Status: **OPEN implementation/whole-component feasibility contract**.
The identities below are accepted D07/E03/E12 facts or routine finite
product evaluations, not a new whole-component EM2 theorem. New scalar
support and the scoped entropy obstruction have their own files.

## Scope and exact definitions

Use alpha,beta>=0,rho<=1,n>=32,m=n+1,L=logn,h=pi/m,t=beta/pi,
a=(cos alpha+cos beta)/2,d=(sin beta-sin alpha)_+. Signed comparison
objects use separate absolute phases. All origins use this SAME n.
The corrected polynomial is G_n=D_n-cos(nu), highest first-coordinate
coefficient ONE. Its literal finite-polynomial values apply at collisions.
The target S is the odd-board primitive, not physical lambda.

    A6={0,1,2m-2,2m-1,m-1,m}, O6={0,...,2m-1}\A6,
    J6=(nm)^(-1)sum_(r in A6)R_r,
    B=(1/m)sum_(r in O6)Hrow(L,v_r),
    t_L=t,t_R=1-t, v_L(z)=z,v_R(z)=2pi-z,
    Tref(L,z)=[U0+(4a/pi)(L+log z)]/z,
    P=(1/m)sum_s sum_(k=2)^(m-2)Tref(L,h(k+t_s)),
    Clog=(1/m)sum_s sum_(k=2)^(m-2)log(pi-h(k+t_s)),
    F_s=Hrow(L,v_s)-Tref-(d/pi)log(pi-z),
    IF=(1/pi)integral_0^pi(F_L+F_R)dz,
    Kfixed=J6+B+Delta2.

The exact four outputs MUST be

    Xrow=delta_a(S-Kfixed), Xret=delta_a(J6-C2),
    Xmesh=delta_a Rmesh,
    T=delta_a[B-P-(d/pi)Clog-IF]+(d/pi)Rlog,             (1)
    Rlog=Clog-2(log pi-1), delta_a X=X(phi)-aX(0).

T includes Rlog and EXCLUDES Xmesh. No second combined mesh/log allowance
may be added. E=S-M_infty obeys the separate exact origin conversion
E(phi)-E(0)=delta_a E-(1-a)E(0); an origin allowance is not part of(1).

## Uncoded exact retained and scalar operations

Actual R_r are row l1 norms on the original parity mesh; normalize only
by nm as above. D01's row-capture snapshot can supply those actual rows
after a new reviewed source binding. Its R64 pole mask is not A6. D07's
physical four-copy point routine cannot substitute for S or J6.

The endpoint reference is the original

    C2=ell0(beta)+ell1(alpha,beta)+ell1(alpha,-beta)+ell2(alpha,-beta),
    ell0(beta)=sinc(beta), ell0(0)=1,
    ell_r(alpha,b)=sin(b)/(r*pi+b)
       +8a sum_(j=-r+1,-r+3,...,r-1)
                     1/[(r*pi+b)^2-(j*pi+alpha)^2].

D37/E04's radius-one sign/denominator proofs cover these finite terms;
they are NOT the actual central rows. For those rows E03/E04 give the
linked finite cyclic vector

    L_(n,k)(theta)=sin(theta)cot((k*pi+theta)/n),
    L_(n,0)(0)=n, L_(n,k)(0)=0 for k not0modn,
    theta_+/−=(alpha+/−(n/m)beta)/2,
    eta_−=(alpha-(n/m)beta-pi/m)/2,
    eta_+=(alpha+(n/m)beta+pi/m)/2,
    F_(m,k)=[ce L_k(theta_−)+cd L_k(theta_+)]/[2cos(beta/(2m))],
    F_(m-1,k)=[ce L_k(eta_−)+cd L_(k-1)(eta_+)]
                                              /[2cos((pi-beta)/(2m))].

All n residues and actual coefficient weights are required. The n/m
and pi/m dependence is explicit, including every sample zero/collision;
no n-independent-feature premise is supplied by this representation.
Actual Jcen(0)=2/m is a useful independent design control.

Let B0=4a/pi^2,D0=U0/pi+B0 logpi,H2=h2(t)+h2(1-t),
G2=g2(t)+g2(1-t). Exact lower constants and completion are

    E2=C2+D0 H2+B0 G2, Delta2=E_infty-E2,
    E_infty=a/3+a C(td)C(te)/pi^2,
    C(v)=-psi(v)-psi(1-v),
    td=1/2+(alpha-beta)/(2pi), te=1/2+(alpha+beta)/(2pi),
    Rmesh=P-D0 H2-B0 G2-B0 L^2-2D0 L.

Here h2(v)=-psi(2+v). The g2 constants still need their exact convergent
centered-cell sum plus N1's analytic tail, or an independently proved
equivalent evaluator. The arbitrary old g_R default R64 is not g2.
P may be computed as its finite singular sum; no upper g_n evaluator is
needed for that finite implementation. The new F01-em2-mesh theorem
supplies a separate analytical check for Xmesh, not its definition.

## Regular integral, entropy and analytical log evaluations

Hrow=A(v)L+Bprofile(v) uses the exact weighted Phi numerator and generic
cancellation integral I from D37 section6. Old D01 A/B point helpers can
be considered only after matching these definitions; its profile() and
fixed-delta integral are M_far and cannot compute IF or M_infty.

The completed integral is

    IF=(b_full-2D0)L+K0-(2d/pi)(log pi-1),
    M_infty=B0 L^2+b_full L+E_infty+K0.

Either IF needs convergent full-interval regular quadrature, or K0 needs
the COMPLETE D02 bias-completion integral, including(0,delta) and its
signed endpoint constant completion. No fixed-delta residue is omitted.
Using M_far here and then observing a small closure tests the wrong model.

For T alone, E12's exact decomposition isolates both logarithms. Write

    C_s=I_s(phi)-aI_s(0)-d log(pi-z),
    B_L=C_L-q log z, B_R=C_R+q log z,
    q=sin beta,
    Q_tau[f]=(1/m)sum_(k=2)^(m-2)f(h(k+tau))-(1/pi)integral_0^pi f.

Then the unchanged signed block is

    T=L(Q_t[g_L]+Q_(1-t)[g_R])+Q_t[P_L]+Q_(1-t)[P_R]
      +(Q_t[B_L]+Q_(1-t)[B_R])/pi
      +(q/pi)(Q_t[log z]-Q_(1-t)[log z])
      +Shift+(d/pi)(Q_t+Q_(1-t))[log(pi-z)].             (2)

P_s,g_s and the FIXED-origin Shift are exactly E14's definitions; Shift
must not be dropped. The logarithm pieces need no endpoint sampling:

    Q_tau[log z]=[(m-3)logh+logGamma(m-1+tau)
                             -logGamma(2+tau)]/m-(logpi-1),
    Q_tau[log(pi-z)]=[(m-3)logh+logGamma(m-1-tau)
                             -logGamma(2-tau)]/m-(logpi-1).

These follow by multiplying the m-3 positive sample arguments and using
Gamma(x+1)=x Gamma(x); they are finite product identities. Both offsets,
all four holes and the full integral normalization are retained.

For source design (2) isolates the endpoint logarithms, but its remaining
B_s are only BV. F01-em2-entropy-obstruction proves that Var(B_R') can
be INFINITE at an interior entropy crossing. Thus (2) is a legitimate
evaluation interface, not yet a finite-BV-derivative EM2 certificate.
Legacy numerical J clamps near zero cannot be adopted as exact weighted
limits or as a validated enclosure. Stable entropy/linked endpoint
evaluation and explicit branch breakpoints require a new reviewed design.

## Two closure controls, neither a definition of a missing component

First test the original four-output closure against independently obtained
completed-model values:

    Xrow+Xret+Xmesh+T=delta_a[S-M_infty].                (3)

Second test the already accepted E03 joint cancellation identity:

    Xrow+Xret+T=delta_a[S-P-IF-Delta2-C2]
                                      -(2d/pi)(logpi-1). (4)

The explicit ordinary H sum cancels in(4). Independent implementations
of IF and the completed K0 identity are needed for a meaningful absolute
model closure; solving for a missing fourth component from(3) is not an
independent check. Shared quantities/dependencies must be disclosed.

## Future T1 design, unexecuted and unreleased

An implementation owner should next prepare immutable NEW source/SPEC
for(1)--(4), with exact input units, error controls and resource accounting.
Freeze the eight rational-radian phases
(3/20,11/100),(13/50,0),(0,13/50),(13/100,13/100),
(3/10,1/5),(1/4,1/4),(1/2,1/2),(4/5,1/5), and fixed degrees
128,200,256,320,1024. A turn-only native API needs a separately reviewed
radian wrapper or an explicit changed-input disclosure; an unnoticed
binary64 alpha/pi round trip is not the exact rational-radian input.

Cache each same-degree origin once, output every signed component and
both closure discrepancies, and retain numerical error/convergence
information. Freeze precision, quadrature feature handling, g2 tail and
closure tolerances BEFORE execution. The proposed binding subset is the
first six phases (rho<=1/2), with all eight still reported; root must fix
that interpretation in the actual preregistration because the audit says
"binding phases" without an exact subset. No case/precision/cap rescue
or replacement after a failed check.

The eventual run is MEASURED only and has an aggregate600 CPU-s cap,
including any measured-build/child work admitted in that later SPEC.
No claim that a new implementation fits the cap is made from this PAPER
design. A single bounded source review/release precedes the first run;
no pilot or unregistered timing run is authorized here.

Keep success<=.02, cancellation signal>=.1 and the intermediate region
INCONCLUSIVE, with numerical uncertainty charged. These are heuristic
route-selection tests; they do not prove a uniform bound or refute all
signed EM estimates. Every prescribed degree is EVEN and every phase is
nonnegative with rho<=1. No odd/signed/class/box coverage or five-fourths
extension follows. No residual degree or global onset is certified.

## Decisive mathematical recommendation and freeze boundary

STOP the original finite-Var(B_s') justification: it fails on an interior
balanced phase already. Retain the four-component target OPEN. The mesh
component has a separate explicit uniform first-order/remainder support.
The next mathematical release should prospectively test exact local
entropy subtraction OR explicitly charged crossing-cell h^2 logm error
for the literal complete Q operator, preserving cusp and all holes.
It must cover moving roots on boxes, p approaching0, axes and coalescing
features; a balanced fixed-phase calculation alone is insufficient.
These are feasibility recommendations only: no alternative estimate,
new route proof or future-round candidate derivation is performed here.

2026-11-07, rules/input4a5de2012bad94601c713b2ff5517f2e3fb80af2;
requested Sol xhigh, serving metadata unexposed. Same coordinated F01.
Full gate, separate release and local pre-derivation registration are in
the owned idea/attempt. PAPER reads/hand algebra/prose only; no source
implementation/import, script, measurement, endpoint/degree/threshold/
native/root/quadrature/compiler/build/pack or Git/shared action.
Distinct review of the new mesh/obstruction and this interface is pending.


## Root disposition after distinct review —2026-11-07

Root adopts only the exact identity/evaluation interface; implementation and full-component feasibility remain OPEN. The original frozen proof/interface prefix is preserved and identified in [F01 independent mathematical review](../independent-checks-F01-seam.md), final13512B SHA25639dcb7fbf90e619f07a99ecb75b5f533722e9c3deec62d0b2ca0d5eb6a960313. This supplies no smaller onset, new finite degree, novelty/priority verdict, protocol waiver or readiness. Final Claude review remains separate.
