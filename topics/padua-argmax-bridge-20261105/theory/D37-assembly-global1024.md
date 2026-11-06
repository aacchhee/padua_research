# PD-T?argmax-bridge-codex-D37-assembly — A fixed1024 five-gate sufficient global criterion

ID kind: PD-T. Aliases: near/inner-far/outer-far analytic1024;
fixed half-multiplier and monotone large-coordinate branches.
Split from: D37 final feasibility candidate. Separate dependencies are
D37 floor, constant, envelope and helper's relative-wide theorem.

## Statement and current status

Use precisely PD-T101/364's corrected Padua cardinals, exceptional
highest first-coordinate coefficient ONE, original endpoint weights,
unequal n,n+1 meshes and actual finite-polynomial collision values.
Define the FIVE fixed gates below. IF all five are positive at the
ONE prospectively fixedN=1024 under validated arithmetic, then for
EVERY integer n>=1024,

    max_[-1,1]² lambda_n=Lambda_c(n)=lambda_n(-1,-1),
    argmax lambda_n={(-1,-1),(1,-1)} if n even,
                    {(-1,-1),(-1,1)} if n odd.   (1)

Status: **PROVED analytic sufficient implication**, under the explicit
component hypotheses and proof below, independent review pending.
The UNCONDITIONAL global1024 target remains **OPEN**: no gate has
been computed, no source/job is released. All new D37 component
claims require distinct review. Supporting lemmas are not an onset.
No unproved D31/D33 endpoint or isolated degree certificate is a premise.

## Fixed scalar functions: all charges retained

For real n>=32 put m=n+1,L=logn,H=1+L,b=4/pi²,r=log(5/2)+1/18.
Use the accepted D16 ACTUAL-origin E0 and OLD D20 global Cnew:

    D=[(52/pi²)H+7]/n+10/n²+20H/(pi*n²),
    MA=1/pi+4/pi²,gpar=1+log(2+8m/(3pi)),
    VB=23+[3gpar+14logm+46+2log2]/pi,
    Qg=(4/m)[7+(2/pi)(5+2log(2m))],
    Gg=(2L*MA+VB)/(2m)+6L*MA/m+Qg+4logpi/(pi*m)+16/m,
    Mesh=b(2L+2r)/n+[4+b(L+1/n)]/(4n²-1)
          +b/(2n-1)²+[5+b(log(n+1/2)+2)]/[4(n-1/2)²],
    W=[3logm+log2+2logpi+2]/(pi*m),
    E6old=(193+21L)/n+21600/n²,
    Cnew=D+Gg+E6old+Mesh+W,
    G0=[(28/pi²)L+111/2+23/pi]/m,
    E0=D+G0+Mesh+14/n+71/n²,
    KD35=[(6+16/(3pi))*H+2/pi]/n,
    T=(4L²-3L)/pi²,V=T-E0.                     (2)

Cnew retains the OLD GLOBAL six-row comparison and every full
ordinary/regular outer/mesh/log charge. Accepted D35 changes ONLY
the P-dependent ordinary coefficient, so its full-domain fixed-row
theorem plus the SAME D20 telescope gives

    |S_n-M_infty|<=Cnew+KD35*P, P=sinx+siny.

The unchanged non-P ordinary error is D. E0 is the SAME actual
finite-origin allowance: no origin U0=0, model-origin identity or
new numerical corner lower is invented. D35's distinct acceptance is
report781e1077eb52c87e4f9f1718a0d658c3f8a342b0db3733c15c8ac1851c31083e.

The NEAR allowance is accepted D35 on rho<=1/2:

    CN=22/n+162/n²+40H/(pi*n²),
    KN=[8H+(39/2)L+286/3]/n+4/n².

The WIDE allowance is helper D37-relative-wide, frozen proof
7acfa8f1a7d75f5eb9fdcce91227f4e969ae522379395f4312f95c5683d7347d,
on the NEW closedrho<=1 domain:

    CW=23/n+204/n²+40H/(pi*n²),
    KW=[8H+20L+292/3]/n+4/n².                    (3)

Each establishes the actual finite increment
S_n(psi)-S_n(0)<=M_infty(psi,L)-M_infty(0,L)+C+K*rho+uE0,
u=1-a. The wide proof rebuilds EVERY endpoint, central, scalar mesh,
regular outer, origin shift and collision domain; it is NOT a transfer
of D22/D25's half-radius quantifiers. Its review remains required.
Both preserve the exact conversion-uE(0)<=uE0, which is combined
FIRST with the model's-uT to give-uV. No finite charge is dropped.

Define the exact radical supremum

    z(B,q,k)=[3B+sqrt(9B²+32qk)]/(8q),
    Psi(B,q,k)=(B/4)z³+(k/2)z², q>0,B,k>=0.

## The FIVE fixed gates

Near rho<=1/2 uses accepted D22/D10 coefficients:

    qNx=(47/192)V-89/72,qNy=(47/192)V-23/24,
    GN=3/50-CN-Psi(77/96,qNx,KN)-Psi(1/12,qNy,KN). (4)

Inner FAR1/2<=rho<=1 uses the NEW proved radius-one constant from
D37-constant-wide and D37-assembly-envelope's FIXED eta1/2:

    qBx=(47/192)V-53/40,qBy=(47/192)V-119/120,
    qLx=(11/48)V-53/40,qLy=(11/48)V-119/120,
    GB=1/4-CW-Psi(1,qBx,KW+1/2)-Psi(1/10,qBy,KW+1/2),
    Ex=1/(2sqrt2)-qLx/4+KW/2,
    Ey=1/(20sqrt2)-qLy/4+KW/2,
    GX=-CW-Ex-Psi(1/10,qLy,KW),
    GY=-CW-Ey-Psi(1,qLx,KW).                    (5)

Require positive V and all q, and the large-coordinate tail domains

    qLx>3/(2sqrt2)+KW,
    qLy>3/(20sqrt2)+KW.                         (6)

Outer FARrho>=1 uses UNIFORM completed constantgapDc, not another
K*u bound:

    u1=47/384,s1=sqrt(47/48),Dc=6211/7260,
    GO=u1*T-Dc-Cnew-KD35*s1-E0.                 (7)

The sole proposed primary would require ALLGN,GB,GX,GY,GO lower
endpoints strictly positive atN1024. No region, branch, charge or
domain predicate may be dropped after seeing its result.

## PAPER domains before any scalar source or endpoint

At fixedN1024=2^10, accepted69/100<log2<7/10 gives
69/10<L<7,H<8. ThusT>8487/500. The SAME E0 in(2) obeys the
following coarse PAPER bounds, withpi>3,pi²>9,b<1/2,r<3/2:

    D<479/(9N)+190/(3N²)<1/10,
    G0<1529/[18(N+1)]<1/10,
    Mesh<17/(2N)+14/N²<1/100,
    14/N+71/N²<15/N<1/50.

For the mesh last three terms use respectively8/(3N²),1/(2N²),
10/N²; their sum is<14/N², since log(N+1/2)<log(2N)<8.
The displayed endpoint comparisons use only
4910660<9437184,15290<18450,1743600<2097152 and750<1024.
HenceE0<23/100<1/4,so

    V>4181/250,
    qLx>30091/12000>2.

qLy is larger, qBx/qBy exceed their L counterparts, and qNx/qNy
have a larger cosine coefficient AND smaller subtractive constants.
Thus ALL six q>2. From(3),L<7,H<8 gives

    KW<904/(3N)+4/N²<1/3,
    KN<1775/(6N)+4/N²<1/3.

Since3/(2sqrt2)<15/14 and15/14+1/3=59/42<2, both tail
conditions(6) follow (the y coefficient is smaller). These domains
are proved before any scalar preview. Source must still validate
its outward interval signs and retain any failure honestly.

## All-n monotonicity, with every constrained region retained

T increases for realn>=1024. E0,Cnew decrease by accepted D16/D20;
KD35 decreases becauseH/n and1/n decrease. The positive CN,KN and
CW,KW decrease by the accepted D35 and new complete wide proofs.
Consequently V and all q increase, while linear coefficients KN,KW,
KW+1/2 decrease. The positive domains and tail inequalities persist.
Psi decreases under these changes by pointwise ordering inside its
explicit polynomial supremum. Ex,Ey decrease since-q/4+KW/2 does.
Therefore ALL FIVE gates strictly increase on realn>=1024.

On NEAR physical noncorner charts, (4)'s scalar bound gives
S_n-S_n(0)<=3/50-GN. D37-floor1024 proves the ACTUAL full defect
Delta>3/50 only under the ACTUAL signedrho<=1/2 guard, so
lambda_n<Lambda_c-GN. No projection is added or used at a corner.

On the inner FAR strip, combine(3) with the full model loss and
new true-constant modulus. Ifx,y<=1/2, D37-envelope gives
S_n-Lambda_c<=-GB. Ifx>=1/2 its proved decreasing quartic tail
gives<=-GX; ify>=1/2 it gives<=-GY. Those CLOSED cases cover
the strip, including coordinate ties; no axis/balanced maxima are
mixed and no multiplier is fitted. A polynomial supremum's enlarged
domain is used only AFTER reducing the ACTUAL physical expression.

On the outer FAR region, acos identity givesu>=1-cos(1/2)>=47/384.
AlsoP<=min(2,sqrt(8u)), ands(u)/u decreases on0<u<=1. Accepted
globalC_infty<8/3 and its explicitly inherited PD-T271 limiting-origin
lower>4383/2420 giveDeltaC<Dc. Thus

    Lambda_c-S_n>u*T-Dc-Cnew-KD35*s(u)-E0
                       >=(u/u1)*GO.

All uniform Dc/non-P charges divided byu decrease; this is the
complete old global telescope with ONLY its proved KD35 improvement.
The outer proof inherits its stated numerical limiting-origin trusted
base; no new corner-constant or phase point is evaluated here.

## Complete physical global assembly if all five signs pass

Every physical square point belongs to a legitimate PD-T364 CLOSED
odd-center chart withrho<=pi. In any physical mesh cell the two
odd-vertex normalized L1 distances sum to2, so at least one is<=1;
this includes tied charts and all square boundaries. The exact identity
is lambda_n=S_n-Delta,Delta>=max(Q_h,Q_v)>=0, with original endpoint
multiplicities, node values and finite-polynomial collisions.

If actualrho>=1/2, inner/outer FAR exclusion above gives strict
lambda_n<Lambda_c because each gate is positive. The seamrho1 is
in BOTH closed regions andrho1/2 remains included. If actualrho<=1/2
at a NONCORNER center, use GN and the guarded3/50 floor. At an actual
nonnode corner, accepted D27 gives lambda_n<=Lambda_c-(A²+B²)/8
on its CLOSED inwardpi/4 square for EVERYn>=1024. Sincepi/4>1/2,
the whole remaining inwardA+B<=1/2 half diamond is inside it. This
is strict unless A=B=0, where the value remains exactLambda_c.

The only odd endpoint-pair centers are(n,n+1),(0,n+1) for even n,
or(n,n+1),(n,0) for odd n. Admissibility supplies their inward signs.
Every other odd center has an interior coordinate for the near floor.
Node-preserving x reflection for even n or y reflection for odd n
identifies exactly the two displayed corner values. Unequal n,m
are never interchanged. Nodes, edges, axes, ties and every collision
are covered. Thus the five fixed positive signs imply(1) for EVERY
integern>=1024, not merely an isolated1024 certificate. QED.

## Release, falsifiability and present limit

All PAPER domain/operator/constant/floor/optimization obligations are
now explicit, under the separately frozen helper support. None of the
FIVE1024 gate signs has been evaluated. The global1024 target is OPEN
until one source/SPEC/freeze receives distinct mathematical/source
review, publication, ROOT RELEASE, the sole<=5CPU directed endpoint,
and distinct fresh arithmetic/result review. No native/phase/board/
rootfinder/quadrature/degree job, preview, threshold/multiplier scan,
retune/cap/source rescue or retry is licensed. A failed sign retains
THIS sufficient allocation's failure; it does not refute the actual
argmax or permit a forced lower onset. Old D31/D33 recipes stay intact.

This implication uses accepted D35/D27 and new D37 complete proofs,
not any uncomputed D31/D33 endpoint. It does not claim minimum onset,
all-degree PD-T099, remaining finite-degree closure, full vanishing
D13 remainder, hermetic arithmetic or measured native speedup.
2026-11-06, Codex gpt-6.1-sol xhigh45min coordinated paper lead;
inputeb9329c28be18d77eeb817f634202d626ee11f92, serving metadata unexposed.
