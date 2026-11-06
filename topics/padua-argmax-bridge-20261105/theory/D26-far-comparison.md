# PD-T?argmax-bridge-codex-D26-far — Fixed4096 far comparison with the new true-constant coefficient

ID kind: PD-T. Aliases: unchanged D20 error with25/2 coefficient;
prospective analytic far4096. Split from: D26 global4096 target.
Split into: the global closed-cover assembly has its own D26 file.

## Target, status and fixed dependencies

Target: for EVERY integer n>=4096 and every real signed phase pair
with1/2<=rho=|alpha|+|beta|<=pi, prove

    S_n(alpha,beta)<Lambda_c(n),
    Lambda_c(n)=S_n(0,0)=lambda_n(-1,-1).           (1)

Use the unchanged corrected finite polynomials, endpoint weights,
exceptional highest x coefficient ONE and collision values of
PD-T101/364. Overall status: **OPEN**, pending the SOLE prospective
N4096 directed endpoint. The complete conditional reduction below
is proved; it does not make(1) PARTIAL. D24's new constant proof was
distinctly ACCEPTED before this source freeze, report
600b395672d6ade4607e6c9980aff7df778a729cf5e17095e182d9ca04ff3500.
The NEW D26 source/SPEC review/publication/root release are still
execution prerequisites. No scalar execution or onset is asserted.

Accepted D20-global-error supplies SAME positive decreasing functions
Cnew,KD on real n>=32 and the FULL signed-diamond bound

    |S_n(psi)-M_infty(psi,logn)|<=Cnew(n)+KD(n)*P,
    P=sin|alpha|+sin|beta|.                       (2)

Its exact ordinary-row/global-regular-quadrature/six-retained-row/mesh/
central-log telescope is unchanged. Accepted D16 supplies its ACTUAL
origin allowance E0(n)>0, decreasing on real n>=32, with
|S_n(0)-M_infty(0,logn)|<=E0(n). This is not a U0=0 fictitious
origin or a completed-limit corner lower. The new D24-far-constant
supplies DeltaC<(25/2)(1-a) on the SAME closed far domain. Its
PD-T271 limiting-origin Arb trusted premise remains explicit.
Accepted C08's full completed-model coefficient comparison supplies
the remaining logarithmic model loss. No near-only theorem is used
at far phases and no old22 coefficient is retained in the new gate.

## Exact definitions and conditional far implication

Put m=n+1,L=logn,H=1+L,b=4/pi²,r=log(5/2)+1/18 and

    D=[(52/pi²)H+7]/n+10/n²+20H/(pi*n²),
    KD=[352H/(3pi)+2/pi]/n,
    MA=1/pi+4/pi²,
    g=1+log(2+8m/(3pi)),
    VB=23+[3g+14logm+46+2log2]/pi,
    Qg=(4/m)[7+(2/pi)(5+2log(2m))],
    Gg=(2L*MA+VB)/(2m)+6L*MA/m+Qg
                                      +4logpi/(pi*m)+16/m,
    endpoint_rows=(181+19L)/n+21600/n²,
    central_rows=(12+2L)/n,
    E6=endpoint_rows+central_rows=(193+21L)/n+21600/n²,
    Mesh=b(2L+2r)/n+[4+b(L+1/n)]/(4n²-1)
             +b/(2n-1)²+[5+b(log(n+1/2)+2)]/[4(n-1/2)²],
    W=[3logm+log2+2logpi+2]/(pi*m),
    Cnew=D+Gg+E6+Mesh+W,
    G0=[(28/pi²)L+111/2+23/pi]/m,
    E0=D+G0+Mesh+14/n+71/n²,
    T=(4L²-3L)/pi², u0=191/6144,
    s(u)=min(2,sqrt(8u)), s0=sqrt(191/768),
    FarGate(n)=u0*(T-25/2)-Cnew-KD*s0-E0.        (3)

These are literally accepted D20/D16 positive formulas, not a new
error telescope. In particular the old four-row allowance is NOT
misidentified as a six-row allowance: both components above remain.
The original D20 formula/data at7000 stay immutable.

For absolute phases x,y with rho=x+y<=pi, put
a=(cosx+cosy)/2=cos(rho/2)cos((x-y)/2) and u=1-a in[0,1].
On rho>=1/2, a<=cos(1/4), and the alternating cosine bound gives

    u>=1/32-1/6144=191/6144=u0.

Also P<=2 and P²<=2(sin²x+sin²y)<=8u, so P<=s(u).
Apply(2) at ACTUAL phases first. Bounding its positive scalar error
by Cnew+KD*s(u) afterwards is valid; it does not invoke a physical
theorem at independently fictitious p,q,a values.

C08 and D24 imply, with exactly the full completed model,

    M_infty(0,L)-M_infty(psi,L)>u*(T-25/2).

Combining this strict model loss, (2) and the actual-origin allowance,

    Lambda_c-S_n(psi)
       >u*(T-25/2)-Cnew-KD*s(u)-E0
       >=(u/u0)*FarGate(n).                      (4)

To prove the last inequality, the quotient
[Cnew+KD*s(u)+E0]/u decreases foru in[u0,1]:1/u decreases and
s(u)/u is sqrt8/sqrtu up to u1/2, then2/u; the two coincide at
their seam. All coefficients are positive. This is exactly D20's
accepted phase-correlation argument, with only the separate constant
coefficient changed. If FarGate(n)>0 then(4) gives a uniform strict
primitive gap>FarGate(n), sinceu/u0>=1.

## Fresh all-n transfer before any evaluation

At the FIXED natural barrier N=4096=2^12, accepted elementary
log2>69/100 impliesL>207/25>8. Since4L²-3L increases forL>3/8
and pi²<10,

    T(4096)>155871/6250>25/2.                    (5)

The last exact comparison is311742>156250. Thus T-25/2 is positive
for all real n>=4096, and T'=(8L-3)/(pi²n)>0. No D20 paper
shortcut3^8<7000 is reused at4096, where that shortcut would fail.
The accepted full Cnew,KD and E0 decrease on all real n>=32; their
COMPLETE positive components, not an asymptotic order estimate, have
the proved monotonicity. Consequently FarGate strictly increases on
real n>=4096. A single rigorous FarGate(4096)>0 would therefore
prove(1) for EVERY integer n>=4096 by(4), with no degree enumeration.

## Sole prospective endpoint and trusted arithmetic

The new source/SPEC freeze proposes ONLY N4096 with exact Fraction
Machin pi brackets and directed Decimal50 arithmetic. It computes ALL
components(3) and the strict gate, retaining their outward intervals.
Correctly rounded ln/sqrt are expanded to adjacent Decimal values;
only accepted hash-pinned D06 AST helper definitions execute. No old
main, mpmath, phase/model values, native, kernel, board, quadrature,
degree or threshold scan. Total soft4/hard5CPU includes startup/imports/
helper/serialization/output/return, no children. The first exclusive
attempt is retained even on source/control/budget failure; no retry,
fallback or precision/parameter/cap change is authorized.

PASS requires all exact controls,T.lower>25/2 andFarGate.lower>0,
the published source/freeze identities and directly observed exit0.
The CPU sample before receipt is a checkpoint, not exact post-exit
CPU. A provisional receipt alone cannot establish completion. The
new endpoint remains UNEXECUTED; source/math review and root release
must precede it, then a distinct fresh replay/review precedes adoption.

Failure of this sufficient gate would preserve(1) OPEN; it would
not refute the actual inequality. This is not a minimum-onset result,
lower-degree scan, change to PD-T271, full-relative D13 proof, native
performance claim or alteration of the old accepted global7000 theorem.
2026-11-06, parent-assigned Codex gpt-6.1-sol xhigh; rules/input
0174900a19087d728f3f947b52f205e5b76b0a41, serving metadata unexposed.
