# PD-T?argmax-bridge-codex-D33-far — Prospective full far exclusion from2048

ID kind: PD-T. Aliases: fixed D30 two-region endpoint application;
full unbounded far2048 target. Split from: D33 global assembly.

## Exact target and status

For EVERY integer n>=2048 and EVERY real signed phase pair with
1/2<=rho=|alpha|+|beta|<=pi, the target is

    S_n(alpha,beta)<Lambda_c(n),Lambda_c(n)=S_n(0,0).

Use precisely PD-T101/364's corrected finite polynomial, exceptional
highest x coefficient ONE, endpoint weights/normalization and actual
collision values. Overall status: **OPEN**, pending the SOLE directed
N2048 pair of lower gate signs and distinct fresh result review.
No primary has run. The sufficient implication below is accepted D30;
supporting lemmas do not make this target PARTIAL.

## Complete endpoint formulas and all-n implication

Let m=n+1,L=logn,H=1+L,b=4/pi²,r=log(5/2)+1/18. Use EXACT
accepted D20/D16 functions

    D=[(52/pi²)H+7]/n+10/n²+20H/(pi*n²),
    KD=[352H/(3pi)+2/pi]/n,
    MA=1/pi+4/pi²,gpar=1+log(2+8m/(3pi)),
    VB=23+[3gpar+14logm+46+2log2]/pi,
    Qg=(4/m)[7+(2/pi)(5+2log(2m))],
    Gg=(2L*MA+VB)/(2m)+6L*MA/m+Qg
                                      +4logpi/(pi*m)+16/m,
    Mesh=b(2L+2r)/n+[4+b(L+1/n)]/(4n²-1)
          +b/(2n-1)²+[5+b(log(n+1/2)+2)]/[4(n-1/2)²],
    W=[3logm+log2+2logpi+2]/(pi*m),
    Cbase=D+Gg+Mesh+W,
    E6old=(193+21L)/n+21600/n²,Cnew=Cbase+E6old,
    G0=[(28/pi²)L+111/2+23/pi]/m,
    E0=D+G0+Mesh+14/n+71/n²,T=(4L²-3L)/pi²,
    A=14/n+90/n²,Kinner=KD+(10+L)/n+4/n²,
    u0=191/6144,ueta=2277/32768,
    s0=sqrt(191/768),seta=sqrt(2277/4096),
    Fin=u0*(T-11)-Cbase-A*(1-u0)-Kinner*s0-E0,
    Fout=ueta*(T-25/2)-Cnew-KD*seta-E0.          (1)

The accepted D30 report
9ae9c0415625b36f908c1cabe70e44fd64028af08ec162641dde58fdc9ab85b8
independently reconstructs literal SAME-C2/six-row/full-profile matching,
new rho<=3/4 endpoint and collision-safe central weights, inner11u
constant, outer25/2 constant and complete all-n transfer. In detail,
on the INNER CLOSED strip1/2<=rho<=3/4, the true constant increment
is<11u and the full actual error is<=Cbase+A*a+Kinner*P. On the
OUTER CLOSED region3/4<=rho<=pi, keep OLD GLOBAL E6old and the
full error<=Cnew+KD*P with true constant increment<(25/2)u.
Hereu=1-a,P=sin|alpha|+sin|beta|<=min(2,sqrt(8u)). All other
ordinary/global-outer/mesh/log/ACTUAL-origin charges in(1) stay intact.

D30 proves, respectively,

    Lambda_c-S_n(psi)>(u/u0)*Fin(n),
    Lambda_c-S_n(psi)>(u/ueta)*Fout(n).          (2)

The quotient argument uses s(u)/u decreasing and a=1-u in the INNER
error ONLY. No different finite profile, hidden norm or fictitious
phase tuple is introduced. The outer ratio retains its inherited
PD-T271 limiting-origin Arb premise, distinguished from finite Lambda_c.

At fixed2048=2^11,L>759/100 and
T>129789/6250>25/2>11 by exact paper bounds, before any scalar job.
All error functions in(1) decrease on realn>=2048, while T increases;
A decreases and Kinner decreases since[(10+logn)/n]'=(-9-logn)/n².
Thus both gates strictly increase. BOTH sole signs

    Fin(2048)>0 AND Fout(2048)>0                 (3)

would prove a uniform full-far gap>min(Fin(2048),Fout(2048)) for
EVERY integer n>=2048 by(2). Both CLOSED phase regions cover the
entire old far diamond; seams, axes,a0, vertices and finite-polynomial
collisions remain. There is no actual phase or degree enumeration.

## Sole computational obligation and limits

The new source/SPEC fixes ONLY2048, directed Decimal50, exact
Fraction Machin70/20 and four hash-pinned accepted AST definitions.
It retains all component intervals, both roots/gates and exact controls,
requires T.lower>25/2 and BOTH strict lower signs, soft4/hard5 whole
CPU and no children. Freeze/proof/SPEC must receive distinct prerelease
review and publication, then root release BEFORE the first scalar.
First failed sign/control/arithmetic/budget/freeze is retained, no
alternate case/threshold/parameter/precision/source/cap rescue or retry.
A passed artifact requires observed EXIT0 and distinct fresh result
replay/review before adopting this all-n target. No source import,
control or endpoint has run during preparation.

This is a new two-region application of accepted D30, not a retry
of D26's different fixed4096 gate. Old D20/D26/D30 data/source/proofs
remain unchanged. It is not an isolated2048 certificate, minimal-onset
proof, full D13 relative theorem, near/corner/global result or runtime
claim. The separate D33 global target needs D31 near2048 as well.
2026-11-06, parent-assigned Codex gpt-6.1-sol xhigh20min PREP;
rules/inputeb9329c28be18d77eeb817f634202d626ee11f92,
serving metadata unexposed.
