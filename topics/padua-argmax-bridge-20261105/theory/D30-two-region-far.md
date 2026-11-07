# PD-T?argmax-bridge-codex-D30-cover — A sufficient two-region far budget with matched retained rows

ID kind: PD-T. Aliases: fixed three-quarter full-profile partition;
inner wide-six-row and outer global-six-row gate; prospective2048 far.
Split from: D30 far-only candidate. Depends on the separate substantive
D30-wide-retained-rows and D30-inner-constant results.

## Statement, status and the unresolved endpoint

Use the UNCHANGED corrected primitive S_n and completed model M_infty
of D05/D02, with the exceptional highest first-coordinate coefficient
ONE, original row weights/normalization and all actual finite-polynomial
collision values. Define the positive functions and two gates below.
If BOTH fixed endpoint conditions

    F_inner(2048)>0,F_outer(2048)>0                (1)

are rigorously verified, then for EVERY integer n>=2048 and EVERY
signed phase pair on the ENTIRE closed far diamond

    1/2<=rho=|alpha|+|beta|<=pi,

one has

    S_n(alpha,beta)<Lambda_c(n)-g,
    Lambda_c(n)=S_n(0,0),
    g=min(F_inner(2048),F_outer(2048))>0.          (2)

Status: **PROVED analytic sufficient implication**, by the reduction
and all-n monotonicity below. The UNCONDITIONAL far2048 target is
**OPEN** because(1) has NOT been evaluated. The component proofs
are developer-PROVED and need distinct review before adoption.
No endpoint existence, scalar source, numerical job, near exclusion,
actual-corner extension or global2048 result is claimed here.

The partition is FIXED at rho3/4. The inner closed strip uses NEW
D30 retained-row and true-constant bounds, each proved through its
actual domain. The outer closed region keeps the OLD D20 global
retained-row bound and accepted D24 coefficient25/2. The seam is
in both regions, and no phase is removed by strict clipping.

## Identical full-profile telescope and complete scalar charges

For realn>=32 putm=n+1,L=logn,H=1+L,b=4/pi²,r=log(5/2)+1/18.
Use EXACTLY accepted D20/D16 functions

    D=[(52/pi²)H+7]/n+10/n²+20H/(pi*n²),
    KD=[352H/(3pi)+2/pi]/n,
    MA=1/pi+4/pi²,
    gpar=1+log(2+8m/(3pi)),
    VB=23+[3gpar+14logm+46+2log2]/pi,
    Qg=(4/m)[7+(2/pi)(5+2log(2m))],
    Gg=(2L*MA+VB)/(2m)+6L*MA/m+Qg
                                    +4logpi/(pi*m)+16/m,
    Mesh=b(2L+2r)/n+[4+b(L+1/n)]/(4n²-1)
             +b/(2n-1)²+[5+b(log(n+1/2)+2)]/[4(n-1/2)²],
    W=[3logm+log2+2logpi+2]/(pi*m),
    Cbase=D+Gg+Mesh+W,
    E6old=(193+21L)/n+21600/n²,
    Cnew=Cbase+E6old,
    G0=[(28/pi²)L+111/2+23/pi]/m,
    E0=D+G0+Mesh+14/n+71/n²,
    T=(4L²-3L)/pi².                              (3)

There is no change to ANY ordinary-row, global regular-quadrature,
scalar mesh, central log or actual-origin allowance. In particular
D includes the complete D04 remainder; E0 is the SAME actual finite
origin allowance, not a completed-limit constant or an origin U0=0
substitution. Accepted D20 proves all functionsCbase,Cnew,KD,E0
positive and decreasing on realn>=32, with each displayed positive
component charged. No asymptotic O estimate is substituted.

For clarity the actual operator identity is D07's complete global
one, with exactlyA6={0,1,2m-2,2m-1,m-1,m} and literal ordinary
indicesk=2,...,m-2 on each folded side:

    Gintermediate-M_infty=(J6-C2)+Rmesh+(d/pi)Rlog,
    |S_n-M_infty|
       <=E_D04+E_global+|J6-C2|+Bmesh+(d/pi)Blog. (4)

Here d=(sin beta-sin alpha)_+ after taking absolute phases. The
continuous Delta2=E_infty-E2 has its accepted sign and EXACT SAME
E2=C2+D0*H2+B0*G2. The finite h ispi/m; the two central rows have
their actual polynomial values. Accepted full-domain estimates give

    E_D04<=D+KD*P,E_global<=Gg,
    Bmesh<=Mesh,(d/pi)Blog<=W,
    P=sin|alpha|+sin|beta|.                      (5)

These are applied to ACTUAL phases before positive scalar majorization.
Neither near-only outer quadrature nor an invented independent
phase tuple is used. There are no deleted ordinary collisions and
no old fixed-strip I_n/e_collision terms in this DIFFERENT accepted
telescope. D30 changes ONLY the matched |J6-C2| input by region.

## Inner phase-aware error and its gate

On rho<=3/4, D30-wide-retained-rows proves

    |J6-C2|<=[14a+P(10+L)]/n+[90a+4P]/n²,
    a=(cos|alpha|+cos|beta|)/2.

Therefore(4)--(5) give the complete bound

    |S_n-M_infty|<=Cbase+A*a+K_inner*P,
    A=14/n+90/n²,
    K_inner=KD+(10+L)/n+4/n².                   (6)

This preserves the actuala=1-u in the NEW retained-row allowance;
no old phase data, old M norm or old scalar result enters. Retaining
thisa does not change D20's ordinary error, which is still conservatively
bounded byD+KD*P.

Forrho>=1/2, the accepted cosine bound givesu=1-a>=u0=191/6144.
On the full phase diamond0<=a<=1, so0<=u<=1. AlsoP<=2 andP²<=8u;
write s(u)=min(2,sqrt(8u)),s0=s(u0)=sqrt(191/768). Since the inner
strip ALSO hasrho<=3/4, D30-inner-constant suppliesDeltaC<11u.
The accepted C08 full logarithmic coefficient comparison thus gives

    M_infty(0,L)-M_infty(psi,L)>u*(T-11).

Combining this with(6) and ACTUAL-originE0 yields

    Lambda_c-S_n(psi)
      >u*(T-11)-Cbase-A*(1-u)-K_inner*s(u)-E0
      >=(u/u0)*F_inner(n),                     (7)
    F_inner=u0*(T-11)-Cbase-A*(1-u0)-K_inner*s0-E0.

For the last inequality divide all error terms byu. The quotient
[Cbase+A+E0]/u+K_inner*s(u)/u-A decreases on[u0,1]:1/u decreases
and s(u)/u is sqrt8/sqrtu up to u1/2, then2/u with matching seam.
All coefficients are nonnegative. This proves(7) without assuming
a maximizer or an unknown sign of the sufficient gate.

## Outer phase-aware error and its gate

Onrho>=3/4, keep accepted D20's OLD GLOBAL retained-row bound
|J6-C2|<=E6old. Equations(4)--(5) give

    |S_n-M_infty|<=Cnew+KD*P.

Accepted D24 givesDeltaC<(25/2)u on the full far domain, with its
explicit inherited PD-T271 limiting-origin Arb premise. Also

    a=cos(rho/2)cos((|alpha|-|beta|)/2)<=cos(rho/2),
    u>=1-cos(3/8)>=u_eta=2277/32768,
    s_eta=s(u_eta)=sqrt(2277/4096).

Thus the same accepted C08 comparison, actual-origin allowance and
decreasing error/u argument yield

    Lambda_c-S_n(psi)>(u/u_eta)*F_outer(n),       (8)
    F_outer=u_eta*(T-25/2)-Cnew-KD*s_eta-E0,

with strictness in(8) inherited from the strict model loss.
The full row bound is never applied as if it were the new wide bound
outside rho3/4. All original completed-model and numerical-origin
trusted dependencies remain explicit; no model-free claim is made.

## All-n transfer before any endpoint

At the prospectively FIXED N2048=2^11, elementarylog2>69/100 gives
L>759/100. As4L²-3L increases here andpi²<10,

    T(2048)>129789/6250>25/2>11.                 (9)

The first exact lower is(4*(759/100)²-3*(759/100))/10.
For every realn>=2048,T'=(8L-3)/(pi²n)>0. All old charges in(3)
decrease by the accepted D20/D16 scalar proofs. The addedA decreases,
and K_inner decreases because(10+logn)/n has derivative
[-9-logn]/n²<0. The constantsu0,u_eta,s0,s_eta,1-u0 are positive
and fixed. Therefore BOTH F_inner and F_outer strictly increase on
realn>=2048.

If the two sole endpoint inequalities(1) pass, (7)--(9) prove the
uniform gap(2) for EVERY integern>=2048: each phase belongs to an
inner or outer CLOSED region, andu/u0 oru/u_eta is>=1. The actual
seamsrho1/2,rho3/4 and outerrho pi, axes,a0 and all polynomial
collisions stay included. No all-n conclusion is drawn from merely
sampling a degree or a few phases. QED for the sufficient implication.

## Falsifiable next step and scope

The PAPER operator/domain obligations have been supplied explicitly in
the separate row and constant proofs. The remaining numerical obligation
for the proposed far2048 application is EXACTLY the two directed lower
signs in(1), with EVERY positive component(3),(6) retained. Neither sign
has been computed in this task. A later source/SPEC must choose ONLY
N2048, freeze formulas/arithmetic/resource/source identities, obtain
distinct mathematics/source review and root release BEFORE one endpoint
job. A conservative nonpositive gate leaves this witness OPEN and
does not refute the actual far inequality; no retune/scan/fallback/retry
is licensed by this paper proof.

No scalar source, Fraction/Decimal numerical check, native/build/phase/
board/root/quadrature/degree job or new endpoint receipt was produced.
No near2048, actual-corner2048 or global2048 theorem is asserted or
borrowed from a separate worker. The accepted old D20/D26 applications
and their success/failure/unexecuted histories remain unchanged. This
result is a standard finite-error/phase-partition application, not a
new cover or historical-priority principle. 2026-11-06, parent-assigned
Codex gpt-6.1-sol xhigh30min PAPER block; rules/input
09cc533678a22b38f40b70be95426ebbe81faa93, serving metadata unexposed.


## Root review closure — 2026-11-06

Distinct [D30 review](../independent-checks-D30-far.md), SHA256 `9ae9c0415625b36f908c1cabe70e44fd64028af08ec162641dde58fdc9ab85b8`, accepts the wide actual-six-row bound, inner11u constant and conditional two-region far implication without unresolved findings. Root adopts those exact support scopes. Both2048 endpoint signs remain UNCOMPUTED here; no unconditionalfar/global2048 follows until the separately frozen D33 computation/result review and other assembly premises. Reviewed prefix is preserved; final Claude audit remains separate.
