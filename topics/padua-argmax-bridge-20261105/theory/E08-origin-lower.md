# PD-T?argmax-bridge-codex-E08-origin-lower — One-sided actual-origin allowance

ID kind: PD-T. Aliases: signed corner error lower allowance; origin outer
midpoint remainder; retained-origin positive displacement.
Split from: none; supporting quantitative refinement of the accepted
D16/E02 absolute-origin allowance. Split into: none. The estimates below
are internal steps of this one allowance, not separately proposed results.

## Statement

For every INTEGER n>=32, with the corrected primitive S_n and TRUE
completed model M_infty of D02/E02, put

    E_n(0)=S_n(0)-M_infty(0,log n), m=n+1, L=log n, H=1+L,
    b=4/pi^2, hr=log(5/2)+1/18,
    D=[(52/pi^2)H+7]/n+10/n^2+20H/(pi*n^2),
    Mesh=b(2L+2hr)/n+[4+b(L+1/n)]/(4n^2-1)
          +b/(2n-1)^2+[5+b(log(n+1/2)+2)]/[4(n-1/2)^2],
    Bout=pi[L+25log(2m)+193/3]/(8m^2)+1/(8n^2),
    Rplus=[71/n^2-22/(45m)]_+, [x]_+=max(x,0),
    e0=D+Mesh+Bout+Rplus.                                  (1)

Then

    E_n(0)>=-e0(n).                                       (2)

All scalar functions in (1) extend to real n>=32. On that domain e0 is
positive and strictly decreasing, Rplus is nonincreasing, and

    Bout<3/n;  Rplus=0 for n>=148;  Bout<1/n for n>=160.    (3)

Consequently for every integer n>=160,

    E_n(0)>-D(n)-Mesh(n)-1/n.                              (4)

The right allowance D+Mesh+1/n is itself positive and strictly decreasing
on all real n>=160. This refines the accepted absolute allowance

    E0=D+Mesh+G0+14/n+71/n^2,
    G0=[(28/pi^2)L+111/2+23/pi]/m:
    0<e0<E0 for every real n>=32.                         (5)

## Definitions and assumptions

Exact real arithmetic, natural logarithms, both parities. S_n(0) is the
ACTUAL non-node corner value Lambda_c(n), including the exceptional
highest first-coordinate mode and all polynomial collision values.
The unequal n,m meshes, original four endpoint rows, original two
central rows and continuous weighted pole regularizations are retained.
No definition of a finite Padua object at noninteger n is asserted;
real-n assertions concern only the explicit scalar allowances.

## Status by part

Overall status: **PROVED**, developer paper proof; distinct audit pending.
The one theorem is (1)--(5). No sign assertion E_n(0)>=0 is part of it.
Candidate disposition: retained quantitative variant; no priority claim.

## Depends on

- [D08 near representation](D08-near-representation.md), [D07 mesh](D07-global-mesh.md),
  and [D04 row reduction](D04-row-reduction.md): exact complete telescope,
  origin row bound D and scalar mesh bound Mesh, valid n>=32.
- [D07 finite endpoint identity](D07-endpoint-finite-h.md), equations
  (2)--(6),(8),(11): the original R2 reference C2, four positive samples,
  linked closest-row limit and geometry remainder <=71/n^2 at origin.
- [E03 retained-origin proof](E03-joint-row-origin.md), equation (13):
  Jcen(0)=2/m for BOTH parities, with actual polynomial collisions.
- [E02 paired outer](E02-paired-outer.md), equations (3),(9)--(12), and
  its accepted D25/D37 inputs: exact outer operator, fixed origin profile,
  derivative bounds. The enlarged-cutoff variation is rederived below.
- [C08 pole functional](C08-far-pole-functional.md), equation (4):
  0<f(0)<=f(z)<=1. This is a global accepted scalar bound, not an
  extension of a local asymptotic estimate.
- [D16 allowance](D16-phase-allowance.md) and [E02 assembly](E02-assembly768.md):
  definitions and scope of D,Mesh,G0,E0; their published monotonicity.
- PD-T159/269/270 and the D02 true limit identify the exact origin
  polynomial below. No PD-T271 decimal enclosure enters (1)--(5).

## Sources and checks

Repository proofs only. No new external source theorem or literature
priority is asserted. The [idea](../ideas/E08-origin-lower.md) and
[attempt](../attempts/E08-origin-lower.md) give gate coverage and timing.
No code, scalar evaluation, degree job, quadrature, endpoint job or
numerical sign test was run. Independent reconstruction remains required.

## Proof

### 1. Identify the finite corner before estimating its error

For clarity this paragraph reconstructs accepted finite identities; it
does not turn their limiting constants into finite inequalities. In
PD-T159 notation, a_j=j*pi/n,b_k=k*pi/m, epsilon_j=1/2 at j=0,n and
eta_k=1/2 at k=0,m, all other weights one. Write

    F(a,b)=(1+cos b)/|cos a-cos b|,
    L_n=(2/n)sum_(r odd,1<=r<=n)d_r csc(r*pi/(2n)),
    d_r=1 except d_n=1/2 when that endpoint is present.

On the odd board j+k odd no same-mesh diagonal occurs. PD-T159 gives

    Lambda_c=(4/(nm))sum_(0<=j,k<=n,j+k odd)
                       epsilon_j eta_k F(a_j,b_k)+1/m,
    L_n^2=(4/n^2)sum_(0<=j,k<=n,j+k odd)
                       epsilon_j epsilon_k F(a_j,a_k),
    Delta_n=(4/(nm))sum_(0<=j,k<=n,j+k odd)epsilon_j eta_k
                         [F(a_j,b_k)-F(a_j,a_k)],
    Lambda_c=(n/m)L_n^2+1/m+Delta_n.                       (6)

The k=n reference row is zero, so eta_n=1 causes no reference-weight
error. The removed (n,m) endpoint is an actual polynomial collision:
its contribution is exactly 1/m, not a generic rational pole value.
PD-T269 derives, for the full integer sequence,

    kappa=(8/pi)integral_0^1 t^2 cot(pi*t/2)
                         sum_(l odd>=1)1/[l(l^2-t^2)]dt
          =lim_n[Lambda_c-L_n^2].

The integral has continuous limiting endpoint values. PD-T270 gives

    A_n=(2/pi)[log n+gamma_E+log(8/pi)],
    |L_n-A_n|<=1/(4n^2),
    L_n=(1/n)sum_(r=1)^n cot((2r-1)pi/(4n)).

The harmonic singular part of this last sum is
(2/pi)(2H_(2n)-H_n); thus the bound is the accepted BOTH-parity
finite harmonic/cotangent theorem, not an inferred parity cancellation.
D02's true origin polynomial and polynomial uniqueness give
M_infty(0,log n)=A_n^2+kappa, exactly as reconstructed in
[D03's baseline attempt](../attempts/D03-corner-baseline.md). Hence

    E_n(0)=Delta_n-kappa-(L_n^2-1)/m+(L_n^2-A_n^2).         (7)

C07 positivity of the paired Delta_n alone does not pay the kappa
or normalization terms in (7). A log(n+1/2) reparametrization alone
does not control their finite remainder. We use the complete accepted
operator telescope instead of inferring a sign from (7).

### 2. The complete origin telescope and its unchanged terms

Use the exact D07/D08 definitions, with Kfixed=J6+B+Delta2 and the
accepted intermediate model Gintermediate:

    Erow=S-Kfixed, Eout=Kfixed-Gintermediate,
    Eret=J6-C2,
    E_n(0)=Erow(0)+Eout(0)+Eret(0)+Rmesh(0).               (8)

The potential logarithmic mesh coefficient d=(q-p)_+ is zero at origin.
No constant is omitted: Gintermediate-M_infty=Eret+Rmesh there.
D04/D08/D16 give |Erow(0)|<=D and |Rmesh(0)|<=Mesh. These costs,
including ordinary central references and pole terms, are unchanged.
Only the lower estimates on Eret(0) and Eout(0) are improved below.

### 3. Retain the finite R2 displacement and the central origin

At origin a=1,p=q=0. Put mu=n/m. D07's four positive samples are
two copies of (w,z)=(pi,0), followed by (2pi,pi),(2pi,-pi).
For each sample let

    D=w^2-z^2, Dh=mu^2*w^2-z^2, u=z/n, v=w/m,
    K=sinc((u+v)/2)sinc((u-v)/2), Hh=(1+cos v)/(2K).

These denominators are positive for n>=32. The exact nonzero-row
error is -1/m plus the sum of
8[mu/Dh-1/D]+8mu(Hh-1)/Dh over that row's positive samples.
All sine/tau terms vanish at origin, while the linked closest-row
error remains -1/m. Thus the FOUR endpoint rows contribute -4/m,
and the TWO actual central rows contribute Jcen(0)=2/m. In total

    Eret(0)=-2/m+8sum[mu/Dh-1/D]+8mu sum(Hh-1)/Dh.         (9)

This counts the actual collision rows, not their ordinary references.
D07 proves the exact partial fraction

    mu/Dh-1/D=(1/(2m)){
        1/[(mu*w-z)(w-z)]+1/[(mu*w+z)(w+z)]}.

Sum the bracket over the four samples, retaining their multiplicity:

    Sdisp=(1/pi^2)[4/mu+2/(2mu-1)+2/(3(2mu+1))]
          >=56/(9pi^2).                                  (10)

Here 1/2<mu<=1 and each displayed summand decreases with mu, so
the value at mu=1 is a lower bound. The accepted D07 geometry estimate
is |8mu sum(Hh-1)/Dh|<=71/n^2. Equations (9)--(10), with pi^2<10,
therefore give

    Eret(0)>22/(45m)-71/n^2 >=-Rplus.                    (11)

Indeed 4*(56/(9pi^2))-2>22/45. The weak final inequality in
(11) also holds if the preceding positive gain exceeds 71/n^2.
The only nontrivial finite floor used is the accepted n>=32 endpoint
identity; no asymptotic rate or extra parity hypothesis was inserted.

### 4. Keep the signed holes of the actual origin outer operator

Let h=pi/m and f(z)=Phi_0(1/2+z/(2pi)). E02 gives exactly

    F0=(L/pi)b0+P0+Q0/pi,
    b0=2cot(z/2)-4/z,
    d0=1/(2sin(z/2))-1/z,
    P0=2[f(z)-f(0)]/z+2f(z)d0,
    Q0=2cot(z/2)log(sin z)-4log z/z,
    Q_tau[g]=(1/m)sum_(k=2)^(m-2)g(h(k+tau))
                                      -(1/pi)integral_0^pi g,
    Eout(0)=Q_0[F0]+Q_1[F0].                              (12)

The left centers are kh, k=2,...,m-2; right centers are kh,
k=3,...,m-1. Their centered-cell unions are respectively
[3h/2,pi-3h/2] and [5h/2,pi-h/2]. Thus the initial holes have
lengths 3h/2,5h/2 and central holes lengths 3h/2,h/2. The full
integrals in (12) remain. Every retained cell lies in
I=[h/2,pi-h/2].

We first rederive E02's derivative variation with THIS larger interval:

    Var_I(F0')<=V:=L/2+(25/2)log(2m)+37/3.                (13)

The accepted fixed-profile bounds are |f'|<=2,|f''|<=1,
f'(0)=0, 0<f(0)<=f<=1. There are no derivative atoms inside (0,pi).
Put c(x)=cot x-1/x. PD-T270's local partial fractions prove |c''|<1
on [0,pi/2], so b0=2c(z/2) has |b0''|<=1/2 and
Var(b0'/pi)<=1/2. Also |b0'|<=1,|b0|<=z,b0<=0,
d0=[c(z/4)-c(z/2)]/2, |d0''|<=5/32,
0<=d0<=1/5 and 0<=d0'<=1/3, as in D25/E02.

For r=2(f-f(0))/z, |r''|<=8/z follows from |f'|<=z and
|f-f(0)|<=z^2/2. Therefore its variation on I is at most
8log(2m). The integral of |(2f d0)''| over [0,pi] is <9,
already proved by E02 even using its weaker |f|<=4 bound. Thus
Var_I(P0')<=8log(2m)+9.

On the initial half write Q0=b0 log(sin z)+g, where
g=4log(sin z/z)/z=4 integral_0^1 c(tz)dt and |g''|<=4/3.
The b0'' log(sin z) term costs <1, using
integral_0^(pi/2)-log(sin z) dz=(pi/2)log2<2.
The 2b0'cot z and -b0 csc^2 z terms cost together
at most (9/2)integral dz/z; g'' costs <3. Starting at h/2
therefore gives <=(9/2)log(2m)+4.

On the central half put u=pi-z, T=2tan(u/2). The second derivative
of T log(sin u) costs <4+9 integral du/u, since
T<=2u,T'<=2,T''<=2. The other term -4log z/z costs <2.
Ending at pi-h/2 gives <=9log(2m)+6. The first derivatives match
at the partition pi/2; no atom is lost. Consequently
Var_I(Q0')<=(27/2)log(2m)+10. Divide this bound by pi>3 and add
the preceding two bounds to obtain (13). The cutoff change from
E02's [2h,pi-h] is thus accounted for explicitly.

For a centered cell of width h and a function with BV derivative,

    |hF(center)-integral_cell F|<=h^2 Var_cell(F')/8.       (14)

For example subtract the center tangent and integrate the two linear
remainders; the coefficient of each derivative-variation mass is at
most h^2/8. Applying (14) separately to the disjoint cells of each
side of (12) gives a total midpoint lower error >=-pi V/(4m^2).
This is the midpoint error only; the holes are handled next.

On either initial hole 0<z<=5h/2<=pi/4<1. Taylor's sine bound gives
0<=d0<z/23<z/16, while 2(f-f(0))/z<=z. Hence P0<7z/6.
Since g<=0 and sin z>=2z/pi,

    F0(z)<=7z/6+(z/pi)log_+(pi/(2nz)),                    (15)

where log_+(x)=max(log x,0). Indeed the other logarithmic term is
(b0/pi)[L+log(sin z)], with b0<=0 and |b0|<=z. For c_n=pi/(2n)
and any ell>=0,
integral_0^ell z log_+(c_n/z)dz<=c_n^2/4. Thus the SUM of the
two initial-hole integrals, divided by pi, is at most

    [7/(12pi)][(3h/2)^2+(5h/2)^2]+c_n^2/(2pi^2)
      =119pi/(24m^2)+1/(8n^2).                           (16)

The central holes have a favorable sign. Throughout their union
z>=pi-3h/2>=21pi/22 and v=(pi-z)/2<=pi/44<1/14.
Therefore sin(z/2)=cos v>391/392, its reciprocal is <101/100,
and cot(z/2)=tan v<28/391<1/13. Using 3<pi<22/7 yields

    b0/pi<2/39-49/121<-7/20,
    P0=f(z)/sin(z/2)-2f(0)/z<101/100.

Also Q0<=0 here: cot(z/2)>=0, log(sin z)<=0 and z>1.
Since L>3 for n>=32, F0<-21/20+101/100=-1/25 on the
interiors of both central holes. The regular endpoint value has the
same weak sign. Thus their integrals are nonpositive and subtracting
them from the cell expression only improves the LOWER bound.

Combining (13)--(16) with all four holes in (12) gives

    Eout(0)>=-pi V/(4m^2)-119pi/(24m^2)-1/(8n^2)
             =-Bout.                                    (17)

Equations (8),(11),(17) prove (2).

### 5. All-real-n transfer and strict improvement

The accepted D16 elementary derivatives show D and Mesh positive
and strictly decreasing for real n>=32. For completeness their terms
are positive sums of (c log n+d)/n^j, the inverse-square term, the
split pair (4+bL)/(4n^2-1)+b/[n(4n^2-1)], and the last term with
numerator 5+b(log(n+1/2)+2). Differentiation gives negative
derivatives on this domain, as in D16.

Set K=L+25log(2m)+193/3. Direct differentiation gives

    (n Bout)'=pi[(1-n)K+m+25n]/(8m^3)-1/(8n^2)<0.        (18)

Indeed K>64 and (n-1)64>26n+1=m+25n for n>=32. At n=32,
log32<4,log66<5,pi<22/7 and n/m^2<1/n give

    n Bout < [(22/7)(4+125+193/3)+1]/256<3.

At n=160 the analogous estimate, using log160<6,log322<6, gives

    n Bout < [(22/7)(6+150+193/3)+1]/1280<1.

These are rational inequalities, not scalar jobs. The logarithmic
inequalities follow, for example, from e>8/3 and its indicated
integer powers. Thus (18) proves the Bout assertions on entire
real half-lines, and also proves Bout strictly decreasing.

The function n^2/(n+1) increases. For n>=148 it is >n-1>=147,
and 22*147>71*45, proving Rplus=0. Wherever Rplus>0,

    Rplus'=-142/n^3+22/(45m^2)
          <-142/n^3+71/(n^2*m)<0.

Its positive support is an initial interval because n^2/(n+1)
increases; after its unique zero Rplus stays zero. Thus Rplus is
nonincreasing everywhere, including its corner, and e0 is positive
and strictly decreasing. This proves (3)--(4) and the monotonicity
of their usable allowance. Finally Rplus<=71/n^2 and Bout<3/n give

    E0-e0>=G0+14/n-Bout>G0+11/n>0,

which proves (5) for all real n>=32.

## Scope and next unresolved step

This pays only a smaller one-sided ACTUAL-origin charge. For any
otherwise valid upper comparison with a<=1 and u=1-a>=0, the exact
identity E(phi)-E(0)=delta_a E(phi)-u E(0) now permits
delta_a E(phi)+u e0 as its upper bound. The phase-relative allowance,
all original degree floors and global comparisons require their own
matched proofs. No new global onset, source deployment or finite pack
result is asserted. The stronger E_n(0)>=0 remains unproved; its
candidate is preserved in the idea record, not included as a part of
this theorem. Next step is distinct reconstruction of (9)--(18).

## History

2026-11-07, assigned Codex developer, parent-requested Sol xhigh;
serving model/effort metadata unexposed. Rules/source input
8f1211b6162b0e49e042f293665b3a4a7e95f667. Paper-only development.
The gate timing limitation is stated explicitly in the attempt.


## Root mathematical adoption in WORK —2026-11-07

Root adopts the exact15142B frozen mathematical proof above (SHA256 bba01a431ce3d7f4bfc4345eb693eb605fc3e82883cb7466a5ec597e1456d979), after distinct [origin mathematical ACCEPT](../independent-checks-E08-origin.md), report15746B92775b0dce5f79cb3d06ef2cee998b63ce1f026013666bf714709e787a1f8625. Original prefix remains unchanged. Thus the one-sided actual-origin bound and its exact all-real-n simplifications may be used in continuing WORK; it is not an absolute error bound or a proof E_n(0)>=0.

The report separately records unwaived MAJOR protocol findingP1, whose canonical timing disclosure is in the [idea record](../ideas/E08-origin-lower.md). Mathematical adoption does not waive that finding or establish PR readiness; final Claude audit and disposition remain separate. No new numerical/source job or onset claim occurs.
