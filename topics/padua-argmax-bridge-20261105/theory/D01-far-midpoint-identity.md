# PD-T?argmax-bridge-codex-D01-far-identity — Exact midpoint identity for the unchanged far model

ID kind: PD-T. Aliases: D01 T1-c boundary oracle; midpoint fixed-cutoff
residue; obstruction to a uniformly vanishing C06 remainder.
Split from: PD-N?argmax-bridge-codex-D01-far-01, the scoped uniformly
vanishing error obstruction. Split into: none. This substantive identity
is a separate dependency; the original C06/C13 statements are unchanged.

## Statement

Use precisely C06's unchanged fixed-count M_far, with R=64 and
delta=1/100, exact infinite h_R,g_R constants, its continuous sinc
endpoint profiles and its exact retained-interior integral. Let
eps=delta/(2*pi) and N=n(n+1). For every integer n>=2,

    S_n(pi/2,pi/2)-M_far(pi/2,pi/2,log n)
      = b_delta+(2/pi)*log(1+1/n)+e_n,
    |e_n|<=1/(4*N^2),                                      (1)

where the exact nonzero constant is

    b_delta=(4/pi)*[(gamma-log pi)*eps
           +sum_{k=1}^infinity zeta(2k+1)*eps^(2k+1)/(2k+1)]<0. (2)

Formula (2) also holds when the same fixed formula is evaluated with
any 0<delta<=1/100. At this boundary phase its bias is linear, not
quadratic, in delta:

    b_delta=2*(gamma-log pi)*delta/pi^2+O(delta^3).          (3)

## Definitions and assumptions

All phases, kernel, odd-board normalization, polynomial collision
extensions and endpoint profiles are exactly those of
[C06 compact error](C06-far-compact-error.md). Arithmetic in (1)--(3)
is exact real arithmetic. The model formula is well-defined for all L;
using it at n<10^6 asserts no extension of C06's error theorem.

## Status by part

Overall status: **PROVED**, by the analytic argument below. Distinct
supplementary review and formal Claude audit are publication obligations.
The scoped obstruction to a uniform vanishing full-diamond error form is
separately recorded in [D01 far contract](D01-far-contract.md). Numerical
values remain MEASURED in the separate receipt.

## Depends on

- PD-T365, equations (3)--(4), especially its all-n exact midpoint
  identity and error 1/(4*N^2).
- N1-04/05/06/07/08 and C06 compact-error equations (1)--(7), for the
  exact model definitions. No C13 proof or estimate is extended.
- The convergent digamma series already used in N1-04. Its integral
  gives the log-Gamma difference below; no external theorem or numerical
  fit is a proof premise.

## Proof

At alpha=beta=pi/2 one has a=0,p=q=1,c_e=0,c_d=1,U0=1. Hence
C(v)=0,D(v)=1/2, I(C,D,v)=0. The coefficient b_full is 4/pi,
B0=0 and D0=1/pi. In particular the g_R contribution is exactly zero.

For t=v/(2*pi), reflection/periodicity of Phi_0 and cancellation of
its sine factor against 2sin(v/2) give

    B(v)=[-psi(t)-psi(1-t)-2log pi]/(2*pi).              (4)

The endpoint profiles simplify without assigning zero times infinity.
For the positive b=pi/2 branch, every sinc term vanishes and
ell_r=1/[pi(r+1/2)]. For b=-pi/2, the j=r-1 removable sinc term
equals 1/[pi(r-1/2)], all others vanish, and its doubled value combines
with sin(b)/w to give ell_r=1/[pi(r-1/2)]. Also ell_0=2/pi. Therefore

    C_R=(2/pi)*sum_{k=0}^{R-1}1/(k+1/2)
       =(2/pi)*[psi(R+1/2)-psi(1/2)].                   (5)

N1-06's defining h_R telescopes to h_R(t)=-psi(R+t).
This follows directly by taking K->infinity in its harmonic identity,
so no diagnostic truncation is used. Consequently

    C_R+c_mesh=(2/pi)*[-psi(1/2)+log(delta/pi)].         (6)

The dependence on R cancels exactly at this phase. Integrating (4),
using eps=delta/(2*pi), gives

    (1/pi)*integral_delta^(2pi-delta) B(v)dv
      =(2/pi)*[logGamma(eps)-logGamma(1-eps)
                                      -(1-2eps)*log pi]. (7)

For clarity, the log-Gamma difference in (7) can instead be defined
by integrating the convergent digamma series on a compact subinterval
of (0,1), then taking endpoint limits. Thus no unverified quadrature or
special-function approximation enters this identity.

The identity psi(1/2)=-gamma-2log2 follows directly by separating the
even and odd terms in the harmonic definition of psi and using
H_(2j)-H_j->log2. Also the same convergent pole series gives

    -psi(t)-psi(1-t)=1/t+2gamma
                      +2*sum_{k>=1}zeta(2k+1)*t^(2k), 0<t<1.

Integrating it, with Gamma(t)*t->1 at zero, gives

    logGamma(eps)-logGamma(1-eps)
      =-log eps-2gamma*eps
         -2*sum_{k>=1}zeta(2k+1)*eps^(2k+1)/(2k+1)       (8)

Substituting (6)--(8) shows that the limiting constant in the
true midpoint value, (2/pi)*(gamma+log(8/pi)), minus C_far is exactly
(2). PD-T365 gives

    S_n(pi/2,pi/2)=(2/pi)*[log(n(n+1))+gamma+log(8/pi)]+e_n

with its stated all-n remainder. Subtracting M_far=(4/pi)log n+C_far
proves (1).

Here is a coarse exact sign check. The elementary estimates gamma<=1,
e<11/4, pi>3 imply log pi>log3>1+1/12; the last inequality follows
from 3/e>12/11 and log(12/11)>1/12. Also eps<1/600 and
zeta(2k+1)<=zeta(3)<3/2. The positive series in (2), divided by eps,
is at most eps^2/[2(1-eps^2)]<1/12. Thus b_delta<0. The same bound
proves the O(delta^3) tail and (3). Equation (1) therefore has the
nonzero limit (2). QED.

## Checks, scope and open items

This proof uses no run. The implementation compared tightened
quadrature with (6)--(7), checked (1) against the accepted boundary oracle,
and exposed signed components at twelve fixed cases within 600 CPU-s.
Those MEASURED observations and CPU/source hashes live in the separate
[attempt](../attempts/D01-far.md).
Those checks do not upgrade binary64 quadrature to an enclosure.

The interior phase (1.45,1.45) may also have a finite-R cancellation
residue. Formula (2) does not identify its entire limit. A fixed-strip
tail integral alone must not be asserted to explain that phase before
the component and quadrature controls. The separately registered
obstruction cites this exact midpoint identity.

The cheapest next comparison question keeps an explicit residual
allowance and checks whether it fits the available phase-local margin.
No new correction, validated cover, degree certificate or improved onset
is proved or authorized by this record.

## History

2026-11-06, Codex math subagent, parent-requested D01 development at
rules/input `4cf68980fa0538b53e2aea7174ed6e5782a34908`; serving model/effort
metadata not independently exposed. Fresh gate is recorded in
ideas/D01-far.md. The exact boundary simplification preceded native
execution and was communicated to the code owner as a control oracle.
At the parent's explicit request this substantive identity was split into
its own PROVED PD-T record before distinct review; the negative consequence
remains in D01-far-contract.md. No old C06/C13 file is edited.
