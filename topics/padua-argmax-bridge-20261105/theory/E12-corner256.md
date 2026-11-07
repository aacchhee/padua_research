# E12 — Both actual-corner closed pi/4 squares from256

Status: **PROVED developer PAPER support**, distinct audit/root adoption
pending; no global ID. Split from the OPEN E12-assembly256 target.
Requested Sol xhigh, serving metadata unexposed,2026-11-07;
rules5fac9e1. ONE prospectively fixed256, no numerical/source job.

For EVERY integer n>=256,m=n+1, with the ORIGINAL corrected Padua
cardinals, set

    Lambda_n(A,B)=lambda_n(-cos(A/n),-cos(B/m)),
    Lambda_c=Lambda_n(0,0),h=pi/4.

Then on the ENTIRE CLOSED square0<=A,B<=h,

    Lambda_n(A,B)<=Lambda_c-(A²+B²)/30.             (1)

The same holds in inward coordinates at the other parity-correct actual
nonnode corner. This is local support, not global argmax256/minimality.
Every nonorigin point of each square has strict actual descent.

## 1. Named premises and legal absolute/relative roles

Use E09's original scalars L=logn,H=1+L,m=n+1,T=(4L²-3L)/pi²,
the exact full-global D,Gg,Mesh,W and E08's independently accepted
absolute phase-global theorem8886d44e..., reviewbf146792.... Its
uniform corollary is

    CEbar=D+Gg+(64+16L)/n+318/n²+Mesh+W,
    |S-M_infty|<=CEbar+KD*P, ENTIRE CLOSED diamond,
    KD={ [6+16/(3pi)]H+2/pi }/n, P<=2.             (2)

The combined64+16L is NOT a standalone six-row bound. All ordinary,
six actual retained rows, regular outer holes/cells, endpoint weights,
scalar meshes/logs and finite polynomial collision terms remain.
CEbar,KD are positive/decreasing for realn>=32.

Accepted E07 Hmax461214a5... and E06 mapb6a9db93... supply global
C_infty<9/4 and j>23/250. NEW E11 final review3407c50d16d23001e5a2532af80dd82d920263366d9091af1877b3d6c9ab29d2
accepts original pairdea44db8... and CLOSEDpi/2-model695800c1....
At every phase used below,

    Delta C_infty<=Ec-j*u,
    Ec<=kappa*p^(3/2)/sqrt(a)-Bbeta(a,q),Bbeta>=0,
    kappa=4I4/pi²,I4<319/360,
    a=(cosx+cosy)/2,u=1-a,p=sinx,q=sin y.          (3)

The extra nonpositive regular mixed term is safely dropped. The named
PD271 limiting-origin/outward-enclosure premise in the H/regular map
remains; no finite Lambda_c lower is inferred from it. E11's model
radius does NOT extend any finite operator.

Accepted E08-origin-lowerbba01a43..., mathematical review92775b0d...,
gives ONLY E_n(0)>-ebar, ebar=D+Mesh+1/n, every integern>=160.
ebar is positive/decreasing for realn>=160. No E_n(0)>=0 or absolute
origin bound is assumed. Canonical upstream protocol findings remain
unwaived; mathematical adoption is not a protocol waiver.

## 2. A genuine GLOBAL signed norm, independently of the origin lower

D27-global-norm's accepted full-phase coefficient bounds are
4a/pi²<=4/pi² and b_full<(79/5)/pi². Substitute ONLY the accepted
absolute(2) and global C_infty<9/4 in its unchanged adapter:

    M(n)=[4L²+(79/5)L]/pi²+9/4+CEbar+2KD.           (4)

This bounds S on the FULL closed diamond. The exact even-lattice
translations pi(j,k),j+k even, and separate phase sign reflections
reduce EVERY real phase pair to that diamond preserving S. There is
no exchange of n,m. Complete signed board polynomials are dominated by
S, physical lambda=S-Delta<=S, and complete signed-cardinal polynomials
are dominated by lambda. After(-cos(A/n),-cos(B/m)), every real pair
still maps into the physical square. Thus M is a GLOBAL norm for the
signed-cardinal families required by D08. Neither ebar nor an unknown
argmax/sample/local maximum was used to obtain it.

The coordinate frequencies are at most1 and n/m. D08's common signed
family Bernstein/Peano proof applies before absolute values, including
its even squared-coordinate mass1/3 and every collision. Relax n/m<=1
only in its nonnegative fourth-power remainder.

## 3. Separate ACTUAL axis and diagonal loss inequalities

Put q0=7/48. The exact axis deficit
uA=(1-cos h)/2>q0, since cos(pi/4)<17/24. At both axesrho=h<1,
so the ORIGINAL complete wide finite relative theorem is legal:

    A4=4/n+40H/(pi*n²),C4=A4+20/n²,
    JW=[(3/2)H+6]/n+148/n²,
    kWy=[(19/2)H+15L+265/3]/n+(179+17L)/n²,
    S-Lambda_c<=Ec-u*(T-ebar+A4+rho*JW+j)
                                                +C4+kWy*rho. (5)

This is the component-wise n>=32 wide allowance with the one-sided
origin conversion E(phi)-E(0)=delta_aE-uE(0). It is not an extension
of E09's sharper T theorem past1/2. Restoring a=1-u produces the
favorable A4+rho*JW; dropping them gives the weaker upper used below.

From I4<319/360 and pi²>197/20,
kappa<638/1773<9/25 (15950<15957). At(h,0),p=1/sqrt2 and
a=(1+1/sqrt2)/2>17/20, so sqrt(a)>9/10 and
p^(3/2)=2^(-3/4)<3/5 (648>625). Equation(3) gives Ec(h,0)<6/25<1/4.
At(0,h), the accepted exact E11 identity gives Ec(0,h)=-Bbeta<=0.
Consequently both actual axis losses are greater than

    delta_A=q0*(T-ebar+j)-1/4-C4-h*kWy,            (6)

provided T-ebar+j>0, proved at the base below and increasing. Actual
lambda<=S and S(0)=Lambda_c are exact; these are ACTUAL losses.

At(h,h),rho=pi/2. Use the NEW closed-boundary MODEL(3), but ONLY
the FULL GLOBAL finite error(2). Here a=p=q=1/sqrt2, uD=2uA>2q0,
P=sqrt2<3/2, and the fractional model term is kappa/sqrt2<9/35<4/15.
Dropping the favorable Bbeta still gives a valid LOWER loss. Thus

    delta_D=2q0*(T+j)-4/15-CEbar-(3/2)KD-ebar       (7)

is a strict lower for the actual diagonal loss. No finite wide theorem
is used atpi/2, and no diagonal>=twiceaxis assertion is needed.

## 4. Complete fixed256 paper component bounds

Since256=2^8, the written atanh terms and geometric tail give

    842/1215<log2<842/1215+1/6804<111/160,
    277/50<L<111/20,H<131/20,
    157/50<pi<22/7,197/20<pi²<10,logpi<6/5.

The lower log comparison is336800>336555. The tail starts at t^7
after t^5/5, as in the separate near obstruction. Use
hr=log(5/2)+1/18<1, b=4/pi²<41/100 and pi>31/10. Then

    T>6501467/605000>107/10,
    D<629/3840+161/196608<1/6.                     (8)

The D comparison uses52/pi²<16/3 and pi>3 in its positive terms.
For Gg use its EXACT collected full-global form

    Gg={7MA*L+111/2+
       [63+log2+4logpi+7logm+16log(2m)+(3/2)g]/pi}/m,
    MA=1/pi+4/pi²<3/4,g=1+log(2+8m/(3pi)).

At this base2+8m/(3pi)<256 gives g<7;
logm<L+1/256<139/25,log(2m)<63/10. The pi-bracket is<219,
and7MA*L<2331/80, so

    Gg<[2331/80+111/2+2190/31]/257<157/257<5/8,
    (64+16L)/256+318/256²<191/320+159/32768<61/100.

The complete mesh has its SAME three positive tails<14/n², by the
accepted denominator/numerator bounds (logm<7 suffices). Therefore

    Mesh<5371/256000+14/256²<11/500,
    W<1089/39835<7/250,
    CEbar<1/6+5/8+61/100+11/500+7/250<3/2,
    ebar<1/6+11/500+1/256<1/5.                    (9)

Every global positive component is present. Also

    KD<240503/1205760<1/5,
    C4<1697/98304<9/500,
    kWy<28057/30720+5467/1310720<93/100,
    M(256)<4218/197+9/4+3/2+2/5<26.               (10)

For KD use pi>157/50,H<131/20; for C4 use pi>3; for kWy insert
H<131/20,L<111/20 into its TWO displayed positive terms. The norm
uses4L²+(79/5)L<2109/10. These are written rational inequalities,
not machine evaluations or new numerical premises. M(n) is NOT
claimed bounded by26 for n>256.

## 5. Combined all-real-n gates and the exact squared-Peano factor

Fix rU=2/125>pi^4/6144. Indeed pi<22/7 and
125*22^4=29282000<29503488=2*7^4*6144. Define

    FA(n)=delta_A(n)-rU*M(n),
    FD(n)=delta_D(n)-2rU*M(n).                     (11)

At the ONE base256, (6)--(10) and h<11/14 give

    delta_A>2317/1500-1/4-9/500-1023/1400
                =2293/4200,
    FA>2293/4200-52/125=2729/21000>1/8,
    delta_D>9443/3000-4/15-3/2-3/10-1/5=881/1000,
    FD>881/1000-104/125=49/1000.                  (12)

For ALL real n>=256, FA's leading polynomial after expansion is

    [4(q0-rU)L²-(3q0+(79/5)rU)L]/pi².

FD has twice that polynomial. Their L derivatives are positive for
L>=1: 8(q0-rU)=779/750>1 and3q0+(79/5)rU=6903/10000<7/10.
FA's remaining terms are the constant q0*j-1/4-(9/4)rU MINUS

    q0*ebar+C4+h*kWy+rU*CEbar+2rU*KD.

FD's remaining terms are the constant2q0*j-4/15-(9/2)rU MINUS

    (1+2rU)CEbar+(3/2+4rU)KD+ebar.

Every subtracted cost is positive/decreasing on its OWN accepted real
domain, which includes n>=256. In particular
kWy=[(49/2)L+587/6]/n+(179+17L)/n² is decreasing directly; C4
is too. Thus FA,FD increase strictly for all realn>=256. This proves
the integer actual-loss premises throughout that tail without assuming
a decreasing M or fitting a degree endpoint.

D08 uses U=V=h²/2=pi²/32. With delta=min(delta_A,delta_D/2),

    delta-M*pi^4/6144>min(FA,FD/2)>49/2000.

Its origin-weighted squared Peano proof therefore supplies radial loss
coefficient at least

    (16/pi²)*[delta-M*pi^4/6144]
          >(8/5)*(49/2000)=49/1250>1/30.

This proves(1). The factor1/2 from u+v=(A²+B²)/2 is INCLUDED in
16/pi². No double coefficient, omitted frequency factor or positive
origin interpolation error is introduced. The true Lambda_c remains
symbolic, and signed smooth cardinal polynomials are interpolated
before taking absolute values.

## 6. Both parity-correct corners and exact scope

Node-preserving reflection transports the same square to(-1,-1) and
(1,-1) for even n, and(-1,-1) and(-1,1) for odd n. Unequal n,m
meshes are not exchanged. Original endpoint weights, highest first
coefficientONE, all actual nodes/ties and polynomial collision values
remain. D08's even squared chart includes both closed axes and the
origin; there is no sign-stability hypothesis on individual cardinals.

Each square contains the inward A+B<=1/2 diamond since h>1/2.
No noncorner floor or full physical complement is certified here.
The OPEN global256 target and the retained-B near-allocation failure
remain separate. This useful local support needs distinct review/root
adoption, and any source guard adaptation needs a separate allocation.
No script/import/scalar/endpoint/native/phase/quadrature/degree/source/
compile/control/pack/shared/Git job or numerical point call occurred.


## Root adoption at reviewed scope —2026-11-07

Root adopts BOTH closedpi/4actual-corner squares, EVERYintegern>=256, radialloss(A²+B²)/30, after distinct [E12 corner/frontier ACCEPT](../independent-checks-E12-corner-frontier.md), report21214Bb7436e8f4c5f2d6c1e7c2fc0d7313c1f136648a489cdfd0cee3e8ef71e97df2a. The frozen9921B proof prefix586c4e07bf683b3a3cb7913666a51f3541b9c0c6fa484dd12a45890b56b3639d is preserved. No global256 theorem or failure of the new absolute/relative minimum/actual argmax is inferred. All-real-n norm/corner and gate-before-development chronology were checked. Upstream findings remain unwaived; no new finding or numerical/source job occurred. Final Claude audit is separate.


## Audit-02 citation and current-state clarifications — 2026-11-07

The header's pending-adoption wording is historical; the preceding root
adoption records the accepted n>=256 corner support at exactly (1), after
the distinct [E12 review](../independent-checks-E12-corner-frontier.md).
The current global theorem is [E14 from320](E14-assembly320.md), leaving
273 OPEN degrees43–62,65–158,161–319; see [current report](../report.md).
No global256 conclusion follows from this pointer.

In §1, `461214a5` identifies the SHA-256 prefix of the **review file**
[independent-checks-E07-H.md](../independent-checks-E07-H.md), and
`b6a9db93` identifies the **review file**
[independent-checks-E06-H.md](../independent-checks-E06-H.md). They are
not hashes of the E07 or E06 theory files.

For the §3 axis allowance (5), the citation to
[E04-assembly640 (4)](E04-assembly640.md) refers to its component
collection, not its n>=640 global theorem or its n>=640 derivative
estimates. The individual accepted bounds used in that collection are:

| Charge | Exact source and individual review | Applicable guard |
|---|---|---|
| Ordinary Erow | [D37-relative-wide (3), §3](D37-relative-wide.md), [D37 review, Endpoint reference and ordinary rows](../independent-checks-D37-global1024.md) | n>=32, closed signedrho<=1 |
| Retained rows | [E04-wide-retained-origin (3), §§1–5](E04-wide-retained-origin.md), [individual E04 review](../independent-checks-E04-wide-retained-origin.md) | n>=32, closed signedrho<=1 |
| Scalar mesh plus log | [D37-relative-wide (5), §5](D37-relative-wide.md), [D37 review, Wide operator](../independent-checks-D37-global1024.md) | n>=32, closed signedrho<=1 |
| Paired regular outer | [E02-paired-outer (1W), §§1–3](E02-paired-outer.md), [individual E02 review](../independent-checks-E02-paired-outer.md) | n>=32, closed signedrho<=1 |

Each guard includes n=256 and the two axis phasesrho=pi/4<1.
E04-assembly640's review section “Finite allowance and all-real-n
monotonicity” reconstructs precisely these charges; its global640
conclusion is separate. The signed origin conversion is the exact
identity already displayed here; the separately accepted
[E08-origin-lower](E08-origin-lower.md) supplies its one-sided allowance
only for n>=160. That guard includes256. The diagonal retains only the
full absolute finite error and closedpi/2 MODEL bound, as originally
written. This citation clarification adds no estimate or enlarged guard.
P1–P4 remain unwaived; final Claude audit remains separate.
