# PD-T?argmax-bridge-codex-D27-norm — Global norm from the whole-profile error

ID kind: PD-T. Aliases: D20 global-error norm; actual signed-cardinal
norm with all retained rows. Split from: D27 wider actual-corner target.
Split into: none.

## Exact statement and status

For every integer n>=32 put L=log n and use EXACTLY the unchanged
corrected PD-T101/PD-T364 primitive S_n, weighted cardinals and
finite-polynomial collision conventions. Let Cnew(n),KD(n) be exactly
the accepted D20-global-error positive functions and define

    Mnew(n)=[4L^2+(79/5)L]/pi^2+8/3+Cnew(n)+2KD(n).       (1)

Then S_n<Mnew on ALL real phases, lambda_n<Mnew on the physical
square, and Mnew bounds every complete signed board polynomial and
every complete signed cardinal polynomial whose coefficient magnitudes
are<=1. After the actual-corner substitution
(-cos(alpha/n),-cos(beta/(n+1))), the signed-cardinal bound is GLOBAL
for ALL real alpha,beta. No unknown argmax value or phase maximum is
used to define Mnew.

Overall status: **PROVED**, developer analytic application of accepted
global norm and error arguments; distinct review required. This changes
the error majorant in D17's norm, not its finite period adapter or the
underlying model. No scalar or native computation is a premise.

## Dependencies and proof

Accepted D20-global-error gives on the full closed signed phase diamond,
n>=32,

    |S_n(psi)-M_infty(psi,logn)|<=Cnew+KD*P,
    P=sin|alpha|+sin|beta|<=2.

Its proof retains all six actual rows, the complete D07 global
regularized quadrature and exact singular meshes, weighted Phi limits
and the corrected highest first-coordinate mode. It is not D05's old
UF formula with an interior term omitted. D20's distinct ACCEPTED
report is independent-checks-D20-global-hybrid.md,
SHA256e1284bce7f95e332cba284cbafa03c7667772d7518076aea3d3596331cb82398.

Accepted D17-global-norm reconstructs the completed-model coefficients:
4a/pi^2<=4/pi^2 and b_full<=b_c+3/pi^2<(79/5)/pi^2. Indeed
b_c=8k_shift/pi^2,k_shift=gamma+log(8/pi)<8/5 using gamma<3/5,
pi>3 and e>8/3. Accepted D10-global-constant proves C_infty<8/3.
Since L>0, the TRUE completed model therefore obeys

    M_infty(psi,L)<[4L^2+(79/5)L]/pi^2+8/3

on the full closed diamond. Combining with D20 and P<=2 proves(1)
there.

The exact accepted D09/D17 finite reindexing preserves S_n under
translations by pi(p,q),p+q even, and separate phase sign reflections.
Reducing (alpha+beta)/(2pi) and(alpha-beta)/(2pi) into[-1/2,1/2]
maps every real phase pair to the closed diamond with the SAME S_n
value. No n,n+1 coordinate exchange is made. Thus(1) is GLOBAL,
as needed by D08's actual signed-family derivative/Peano theorem.

Every complete signed board polynomial is pointwise dominated by S_n.
The exact physical cover gives lambda=S_n-Delta,Delta>=0 at each
physical point, hence lambda<Mnew. Every signed cardinal polynomial
is pointwise dominated by lambda. Its actual-corner substitution lies
in the physical square for every real pair of phases, proving the
last claimed global signed-family norm.

## Scope, checks and history

This is a global NORM, not a value/location assertion for an unknown
maximum, sampled data, degree certificate or argmax onset. The actual
corner comparison is separate. All underlying D17/D20 source/data and
proof bytes stay unchanged. No scalar/native/actual-point/phase/board/
root/quadrature/degree job ran. 2026-11-06, parent-assigned Codex
Sol xhigh25min; rules/input1ebf813c73bb51025c10db5a0e6b8a5745832c6d,
serving metadata unexposed. Distinct review precedes adoption.


## Current result and root review closure — 2026-11-06

Current norm implication and actual-corner theorem are **PROVED**. Final review [D27](../independent-checks-D27-corner.md), SHA256 `830eaf21c0104180f3874531b268253a3958d4e1de52b202b08306e59d4232c3`, accepts the global norm and both actual-corner closed pi/4 squares with loss(alpha²+beta²)/8 for EVERY n>=1024. Root adopts those exact scopes. Sole primary1024 F>.14441754 and radial>.23412089; independent34intervals+pi/10controls accepted. This is not global argmax1024. The launch-only missing-time-wrapper event and sole successful independent execution are preserved in the review. Historical prerelease text above is preserved; final Claude audit remains separate.
