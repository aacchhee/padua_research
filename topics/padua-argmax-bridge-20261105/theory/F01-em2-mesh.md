# F01 EM2 mesh — Exact first-order term and a uniform second-order remainder

ID kind: PD-T; final allocation belongs to root.
Alias: PD-T?argmax-bridge-codex-F01-em2-mesh; paired-mesh first-order extraction.
Split from: supporting P3 in F01-em2-operator; full four-component I06 stays OPEN.
Split into: none.

## Statement and definitions

For EVERY integer n>=32 set m=n+1,L=log n. Initially take alpha,beta>=0,
rho=alpha+beta<=1, a=(cos alpha+cos beta)/2, t=beta/pi and B=4a/pi^2.
Use EXACTLY D07/D13/D37's Rmesh and delta_a X=X(phi)-aX(0) at the SAME
degree. In the original convergent-series notation put

    H_j(t)=h_j(t)+h_j(1-t), Q_j(t)=g_j(t)+g_j(1-t),
    Gamma_mesh(phi)=-B[H_2(t)-H_2(0)].

Then, uniformly on this ENTIRE closed domain,

    0<=Gamma_mesh<=beta/(8pi)<=rho/24,                    (1)
    |delta_a Rmesh-Gamma_mesh/m|
                   <=(9/2)rho(1+L)/m^2.                 (2)

Signed comparison objects use their inherited separate absolute phases;
thus replace beta,rho by |beta|,|alpha|+|beta| in (1)--(2). Both degree
parities, axes and zero phase are included. There is no n,m exchange.
In I06 notation this ONE component has lambda=0, exact first-order
gamma=Gamma_mesh and a degree-free stronger O((1+L)/m^2) remainder.

Overall status: **PROVED developer PAPER support**, distinct review and
root adoption pending. This is a quantitative extraction from the existing
paired identity, not a new mesh or a result for the other three components.
Full I06 and full D13 remain OPEN. No onset/endpoint has been evaluated.

## Dependencies and exact subtraction

Accepted D13-mesh-support supplies the exact h/g series, their uniformly
convergent derivatives and the actual upper index n=m-1. Accepted D37-
relative-wide section5 supplies the same subtraction on rho<=1, including
its widened endpoint numerator bound. Let

    D=U0/pi+B log pi, eps=log(m/n), Z=D-B eps,
    DeltaD=D-aD^0,

where superscript0 always means the same-degree origin. Write
DeltaH_j=H_j(t)-H_j(0), DeltaQ_n=Q_n(t)-Q_n(0). The unchanged exact identity is

    delta_a Rmesh=-B eps DeltaH_2-aZ^0 DeltaH_n
                      -B DeltaQ_n-DeltaD[H_n(t)+2L].      (3)

Those predecessor results give, on the stated closed domain,

    B<=1/2, |Z^0|<5, |DeltaD|<=5rho/3,
    |DeltaH_2|<=2rho/3,
    |DeltaH_n|<=rho/[3(n-1)^2],
    |DeltaQ_n|<=rho(L-1)/[3(n-1)^2],
    |H_n(t)+2L|<1/n^2.                                 (4)

These are paired bounds; replacing them by unrelated single-tail bounds
would lose the exact cancellation of the large logarithm in (3).

## Proof

First sharpen ONLY the phase dependence of the LOWER harmonic constant.
From the original derivative series,

    h_2'(v)=-sum_(k=2)^infinity(k+v)^(-2),
    h_2''(v)=2sum_(k=2)^infinity(k+v)^(-3)>0.

Consequently H_2''(v)=h_2''(v)+h_2''(1-v)>0. Symmetry gives
H_2'(1/2)=0, while exact telescoping gives

    H_2'(0)=h_2'(0)-h_2'(1)=-1/4.

Because 0<=t<=1/pi<1/2, integrate -1/4<=H_2'(v)<=0 to obtain

    0<=H_2(0)-H_2(t)<=t/4.

Multiplication by 0<=B<=1/2 proves (1), using pi>3. No numerical value
of a special function is used. The same convergent-limit definition also
gives h_2(v)=-psi(2+v), so the exact coefficient can equivalently be
evaluated as

    Gamma_mesh=B[psi(2+t)+psi(3-t)-psi(2)-psi(3)].        (5)

For the remainder retain the exact denominator m. Elementary integration
gives

    0<=eps-1/m
      =int_n^(n+1)[1/x-1/(n+1)]dx<=1/(2nm).

Subtract Gamma_mesh/m from (3), then apply (4). The first term costs at
most rho/(6nm); the two upper-constant increments together cost at most
rho(L+9)/[6(n-1)^2]; the last term costs at most5rho/(3n^2). Thus

    |delta_a Rmesh-Gamma_mesh/m|
       <=rho{(L+9)/[6(n-1)^2]+11/(6n^2)}.               (6)

For n>=32, (n-1)^2>7n^2/8. Therefore the right side is at most

    (rho/n^2)[4L/21+149/42]<=4rho(1+L)/n^2.

Finally (m/n)^2<9/8, so this is at most the right side of (2).
At rho=0 every exact increment vanishes, and all final inequalities
are weak. Every other step used the exact paired same-degree identity,
which has both parity and weighted-continuation conventions already
proved by D07/D13/D37. This proves the stated closed-domain result.

## Scope, checks and history

This bounds ONLY delta_a Rmesh. T already includes the signed Rlog term;
Rlog must not be added to (2) as a second charge. Ordinary rows, retained
rows, the outer/log block and actual-origin conversion remain separate.
No smaller global onset or full-component EM2 theorem follows here.

PAPER only: bounded reads and hand algebra, no scientific source/import,
script, measurement, scalar/phase/degree/endpoint/native/root/quadrature/
threshold/compiler/build/pack job. No external theorem or priority claim.
Own idea/attempt register P3 before derivation; the exact constants emerged
during released hand algebra and were reported to root before this full
proof. Rules/input4a5de2012bad94601c713b2ff5517f2e3fb80af2,
2026-11-07; requested Sol xhigh, actual serving metadata unexposed.
Distinct mathematical review is required; root owns final IDs/adoption.


## Root disposition after distinct review —2026-11-07

Root adopts the written mathematical statement at its exact quantifiers and named dependencies. The original frozen proof/interface prefix is preserved and identified in [F01 independent mathematical review](../independent-checks-F01-seam.md), final13512B SHA25639dcb7fbf90e619f07a99ecb75b5f533722e9c3deec62d0b2ca0d5eb6a960313. This supplies no smaller onset, new finite degree, novelty/priority verdict, protocol waiver or readiness. Final Claude review remains separate.
