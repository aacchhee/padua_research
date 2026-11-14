# D01 far diagnostic: preregistered mathematical contract

Rules/input: `4cf68980fa0538b53e2aea7174ed6e5782a34908`.
Task: handoff08 B2 / audit01 P1 T1-a,T1-c. Status of numerical results:
MEASURED. Math owner `/root/d01_far_math`; implementation owner
`/root/d01_far_code`. No producer, model modification or degree certificate.
All execution, builds and controls together have a 600 CPU-second cap.

## Inputs, identity and topology

Use R=64, delta=1/100, n=512,2048,8192, and phase labels
(.25,.25), (1.38,0), (1.45,1.45), (pi/2,pi/2). The first three labels
are real-radian targets. If the backend accepts rational multiples of pi,
record the exact rational inputs and use their same actual radian values
in every model calculation. The midpoint is exactly (pi/2,pi/2).
No decimal-radian phase is an exact rational multiple of pi by declaration.

Let m=n+1, L=log n, v_r=(r*pi+beta)/m, z_r=min(v_r,2*pi-v_r),
and R_r=sum_k |F_rk| with the original corrected polynomial and odd board.
The accepted C11 O(n) point backend may expose its existing row norms;
snapshot and instrument it without changing frozen source. Verify its total
against the unchanged point call. No O(n^2) board loop at n8192.

P={0,...,R-1} union {2m-R,...,2m-1};
K=exact polynomial-collision rows outside P;
T={m-1,m} minus (P union K);
O=all other rows; Z={r in O:z_r<=delta}; J={r in O:z_r>delta}.
Classify collisions by exact rational phase/mesh arithmetic, never a
floating tolerance. A zero-phase endpoint belongs to P. A central row
with v=pi belongs to K or T and must never enter an H sample.

At every requested degree delta*m/pi<R. Thus Z is empty and P extends
outside the strip. N1-06/08's admissibility n>=ceil(2*pi*R/delta) FAILS.
The exact algebra below remains valid, but its potentially large cancelling
mesh/interior values are not small-n instances of the proved error budget.

## Exact additive telescope

Use the unchanged C06 definitions A,B,V_L=A*L+V, H=A*L+B,
S0(v)=[U0+(4a/pi)*log z]/z, H0=A*L+S0, C_R,c_mesh,b_full.
Let D=(delta,2*pi-delta),
b_end=b_full-(1/pi)*integral_D A, and
P_end(L)=B0*L^2+b_end*L+c_mesh. The exact coefficient identity gives

    M_far=C_R+P_end(L)+(1/pi)*integral_D H.

Define actual signed components (no fitted remainder allocation):

    endpoint = sum_P R_r/(nm) - C_R
    mesh     = sum_Z H0(v_r)/m - P_end(L)
    collision= sum_K R_r/(nm)
    central  = sum_T R_r/(nm)
    ordinary_quadrature = sum_J H(v_r)/m - integral_D H/pi
    Q_actual = sum_Z [B(v_r)-S0(v_r)]/m
    E_actual = sum_O [R_r/n - Pn(v_r) - I(v_r)/pi]/m
    D_actual = sum_O [Pn(v_r)-V_L(v_r)]/m,

where Pn=(|C|B_n(t_minus)+|D|B_n(t_plus))/n is the exact sum of
the two separate pole norms at a noncollision ordinary row. Then

    S_n-M_far = endpoint+mesh+collision+central
                  +ordinary_quadrature+Q_actual+E_actual+D_actual.

The positive E_n,D_n,Q in C06/N1 are upper bounds, not signed components.
Print signed values above and separately their bound formulas and domain
flags. Print central and collision separately as well as their sum. At the
requested degrees Q_actual=0 by topology; this does not say the omitted
fixed-strip limiting residual is zero. Report raw component sum, total
S-M_far, closure error and sum of component absolute values.

The O(n) native partial-cotangent sums may compute Pn using the accepted
C11 mechanism. If an N5 approximation Bhat is needed, define Ehat,Dhat by
the same replacement; their errors have opposite signs and each is bounded
by N1-01 r_n. Print that analytic uncertainty and keep their sum exact.
No O(n^2) calculation is needed to split E,D.

## Pole and quadrature controls

Keep H's cancellation integral combined; do not integrate divergent pole
channels separately. Phi_0 uses periodic continuous integer value1 and
reflection to the closest integer for stable evaluation. J(u,s,e) uses
the exact s<=u, no-root and root branches; zero coefficients use their
continuous limits. At v=pi, subtract d*log|v-pi|/pi from B before
ordinary integration and integrate that logarithm explicitly. Split at
the phase-offset integer crossings, central seams, and coefficient/root
switches. Never sample the undefined central logarithm as a finite value.

Use tightened quadrature targets around 1e-11 or better and a separate
precision/tolerance control; retain integration warnings and estimates.
These are numerical diagnostics, not validated enclosures.

For x=R+t, h_R(t)=-digamma(x) exactly. Replace the old g_R truncation by
the Euler--Maclaurin evaluation of its exact defining infinite constant:

    g_R(t)= -.5*log(x)^2 + log(x)/(2*x)
       + sum_{j=1}^6 B_(2j)/(2j) * [log(x)-H_(2j-1)]/x^(2j)
       + remainder.

The elementary EM integral remainder has magnitude at most

    C12*x^(-12)*[(log(x)+H_12)/12+1/144],
    C12=sum_{k=0}^12 binom(12,k)*|B_k|.

This follows from |B_12({y})|<=C12 and
f^(12)(y)=12!*y^(-13)*(log(y)-H_12), f=log(y)/y.
Use exact rational Bernoulli coefficients; print this bound multiplied by
B0 for each channel. Compare with old K4096 g_R and its published tail
bound, multiplied by coefficients. Binary64 evaluation still has roundoff.

## T1-c boundary oracle and sensitivity

At exact midpoint a=0,U0=1,I=0 and, t=v/(2*pi),

    B(v)=[-psi(t)-psi(1-t)-2log(pi)]/(2*pi).

With eps=delta/(2*pi), the exact constant is independently

    C_far=(2/pi)*[-psi(1/2)+log(delta/pi)
       +logGamma(eps)-logGamma(1-eps)-(1-2eps)*log(pi)].

The limiting residual of the unchanged model is

    b_delta=(4/pi)*[(gamma-log(pi))*eps
          +sum_{k>=1} zeta(2k+1)*eps^(2k+1)/(2k+1)].

PD-T365 gives
S_n-M_far=b_delta+(2/pi)*log(1+1/n)+e_n,
|e_n|<=1/[4*n^2*(n+1)^2]. This analytic oracle must agree numerically
with the tightened original model evaluation. The bias is genuinely
linear in delta at this phase cusp and nonzero at delta=.01.

Sensitivity evaluations at delta=.005,.0025 are authorized ONLY as
diagnostics for the same fixed-count formula; report them separately from
the unchanged original model. No new model/correction is adopted. At
(1.45,1.45), compare tighter original model values, g_R controls and the
continuous omitted strip integral integral_[strips](B-S0)/pi. The latter
is a diagnostic, not automatically the entire limiting residual: finite-R
endpoint/cancellation errors can also survive n->infinity.

## Gates and stopping

First verify phase identity, exact row partition, backend total, model
boundary oracle, weighted g_R tails, tightened-quadrature stability and
telescope closure. Failure stops interpretation. Success T1-a is the
audit rule sum_abs<=2L/n away from a~0, and O(1) components <=.02 atn8192.
Its explicit kill is O(1) components summing in magnitude >.3 atn8192
and cancelling jointly. These are competing gates, not exhaustive outcomes;
record neither-pass-nor-kill honestly. Geometry-induced cancellation below
N1 admissibility is not a universal obstruction to a re-partitioned method.

T1-c has an analytic nonzero boundary residue. Consequently no uniform
C(L+1)/n error claim for the unchanged full-diamond M_far is allowed.
Keep an explicit fixed residual allowance if this route is later resumed.
No validated box run, correction, new degree or further campaign follows
from this diagnostic. Save a small receipt with hashes, actual inputs,
commands, version/timing/CPU accounting and all observed outcomes.
