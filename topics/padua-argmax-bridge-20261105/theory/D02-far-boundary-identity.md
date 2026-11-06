# PD-T?argmax-bridge-codex-D02-far-boundary — Exact fixed-model bias on every diamond edge

ID kind: PD-T. Aliases: full a=0 bias oracle; boundary finite-h contract;
D01 midpoint extension. Split from: D02 full-diamond joint-remainder target,
OPEN. Split into: none; full interior limit is separately recorded.

## Statement

Let n>=2, N=n(n+1), R>=2 integer and 0<delta<=1/100. Use the C06 parameter
family M_(R,delta)=B0 L^2+b_full L+C_(R,delta) defined without changing
its published R64,delta=.01 member. On any signed diamond edge set
alpha=pi*t, beta=pi*(1-t), 0<=t<=1, and p=sin(pi*t). Define epsilon=delta/(2pi)
and the exact scalar from D01,

    b_delta=(4/pi)[(gamma-log pi)*epsilon
       +sum_(k>=1) zeta(2k+1)*epsilon^(2k+1)/(2k+1)]<0.  (1)

Then the full-phase bias from D02-far-bias-identity restricts to

    beta_(R,delta)(alpha,beta)=p*b_delta.                 (2)

It is independent of R on these edges. The actual finite-n identity is

    S_n(alpha,beta)-M_(R,delta)(alpha,beta,log n)
        =p*b_delta+(2p/pi)log(1+1/n)+e_(n,t),
    |e_(n,t)|<=7/(12N^2).                               (3)

Thus the unchanged model has the explicit entire-boundary contract

    |S_n-M_far|<=p*|b_(1/100)|+2p/(pi*n)+7/(12N^2).       (4)

At t=0,1 both actual primitive and model equal exactly 1 and e=0.
At t=1/2 the sharper D01 bound |e|<=1/(4N^2) remains valid. All sign
choices follow by separate phase evenness; both degree parities and all
polynomial collisions are included. This theorem covers only a=0,
not an open interior neighborhood.

## Status, assumptions and dependencies

**PROVED**, exact-real analytic derivation. No fit or numerical premise.
Independent supplementary and formal Claude review are separate.
Dependencies: accepted PD-T365's exact boundary formula and uniform error;
D01 midpoint identity; C08 endpoint constant and increment identity;
D02-far-bias-identity's exact definitions. C06 and the near model are frozen.

## Proof

For 0<t<1 one has a=0, c_e=0, c_d=p, U0=p and C(v)=0,D(v)=p/2.
Hence I=0, and the regularized pole products give exactly

    B(v)=p[-psi(v/(2pi))-psi(1-v/(2pi))-2log pi]/(2pi).

Thus B, the singular subtraction S0 and K_delta are p times their
midpoint counterparts. In C08's endpoint formula,
t_d=t and t_e=1. The continuous weighted product therefore gives

    E_infty=p*C(t)/pi, C(t)=-psi(t)-psi(1-t).             (5)

To see E_R=E_infty here for all R>=2, use its exact cutoff-increment
identity (C08 (15)). It is derived from the finite convolution and exact
h/g recurrences and holds algebraically for every R>=2; only its later
numerical tail estimate required R>=64. Its right side is a times a
sum with finite large digamma arguments. It therefore vanishes when
a=0, including the continuous closed-phase extension. E_R is constant
in R and equals its known limit E_infty. Equivalently, the finite harmonic
sums in the two endpoint orientations telescope with h_R=-psi(R+t).
No zero times an unweighted endpoint digamma is assigned.

By the midpoint calculation in D01, K_0-K_delta=b_delta. Its linear
scaling by p and E_infty-E_R=0 prove (2). Equations (5) and the same
midpoint calculation give the completed boundary constant explicitly:

    C_infty=p/pi*[C(t)+2log(2/pi)].                     (6)

The logarithmic coefficient is b_full=4p/pi. PD-T365 yields

    S_n=p/pi*[2log(2n(n+1)/pi)+C(t)]+e_(n,t),
    |e_(n,t)|<=7/(12N^2).

Subtraction of M_infty using (6) leaves (2p/pi)log(1+1/n)+e.
Then M_infty-M_(R,delta)=p*b_delta proves (3), and log(1+1/n)<=1/n
proves (4). The sign of b_delta and its convergent series are exactly
the already proved D01 scalar calculation.

As t tends to either endpoint, p*C(t)/pi tends to 1 and every other
term in the model tends to zero. PD-T365 gives the same exact actual
value 1 by polynomial continuity. Thus the vertices, removable collisions
and all signs are included without singular substitution. QED.

## Scope, checks and open items

This is an exact all-n oracle for every a=0 phase and quantifies the
nondecaying bias there. It does not prove a uniform interior C(1+L)/n
rate. The entire boundary limit agrees with the normalization of PD-T365;
the midpoint is the independent D01 control. No new run is required.

History: 2026-11-06, rules/input 084a64f6465956f9c75b5538f83752c30318f151;
Codex parent-requested Astra ultra hard mathematics, serving metadata
unexposed. Gate in ideas/D02-far-joint.md; no old proof/source edits.
