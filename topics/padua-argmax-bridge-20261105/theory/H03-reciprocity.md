# PD-T?argmax-bridge-codex-H03 — Exact symmetric corner sum and its absolute residual

ID kind: PD-T, provisional supporting record; no global allocation.
Aliases: H03; numerator reciprocity; consecutive-mesh ordering count;
CRT cosecant correlation. Split from: none. Split into: none.

## Statement

For every integer n>=2 put m=n+1, Q=nm and a=2n+1. Define
x_j=cos(j*pi/n), y_k=cos(k*pi/m), and endpoint weights epsilon_j=1/2
at j=0,n, eta_k=1/2 at k=0,m, all others1. Let O' be the pairs
0<=j<=n, 0<=k<=m, j+k odd, with the sole collision(n,m) removed.
Then the actual Padua corner value of PD-T159 satisfies exactly

    Lambda_c= (2/Q) sum_(O') epsilon_j eta_k
                         (2+x_j+y_k)/|x_j-y_k| +1/(2Q).       (1)

Equivalently, for q_d=pi*d/(2Q), 1<=d<=2Q-1, put

    K_d=[1-cos(a*q_d)cos(q_d)]/[|sin(a*q_d)|sin(q_d)].

There are no poles at these indices, and

    Lambda_c=(1/(2Q))[1+sum_(d=1)^(2Q-1) K_d].                (2)

If the absolute sine factor in K_d is instead replaced by its signed
value, write the resulting expression as Ktilde_d. Then exactly

    sum_d Ktilde_d=4n^2+2n-1,
    (1/(2Q))[1+sum_d Ktilde_d]=(2n+1)/(n+1).                 (3)

Consequently that signed substitution deletes positive mass, asymptotic
to (4/pi^2)log^2 n. It cannot establish the original sharp expansion.

## Assumptions and status

**PROVED**, exact algebraic supporting identities and the scoped signed
substitution diagnostic, with proof below. This record makes no claim
that(2) has fewer terms, gives a faster evaluator, or proves a sharp
remainder. The original PD-T098 target remains **OPEN**. H03's proposed
global collapse is **DEFERRED after its first exact screen**: the residual
has 2Q-1 absolute terms and no sharp summed estimate was obtained.

This is an arithmetic variant of the inherited endpoint-complete Cauchy
formula. It does not assert a new classical cotangent identity or an
impossibility theorem for other reciprocity/resummation methods.

## Depends on

- PD-T159: actual positive corner sum, original half weights and the
  exceptional polynomial contribution1/m.
- PD-T226 at alpha=beta=0: signed periodic rows; used only to evaluate
  the explicitly invalid signed replacement in(3).
- PD-T269/270: Lambda_c~(4/pi^2)log^2 n, used only to state the size of
  mass deleted by that substitution.

## Proof

### 1. The weighted ordering count

Off the removed collision set f_y=(1+y_k)/|x_j-y_k| and
f_x=(1+x_j)/|x_j-y_k|. Their difference is sign(y_k-x_j).
Because the meshes are consecutive and j+k odd, their order is exactly

    y_k>x_j iff k<j;     y_k<x_j iff k>j.

Indeed k/m<j/n iff nk<mj; for 0<j<n, j<mj/n<j+1, and k=j is
excluded by parity. The j=0,n endpoint rows obey the same rule, with
the removed(n,m) collision handled separately.

For a fixed j, the eta-weighted lower-triangle count of k<j with
j+k odd is j/2. If j=2r there are r odd indices with unit weight;
if j=2r+1 the even indices0,2,...,2r have total r+1/2. The total
eta weight of either parity on0,...,m is m/2: reflection pairs prove
this directly when m is odd, and pairing adjacent interior terms with
the two half endpoints proves it when m is even. Removing(n,m) adds
1/2 to that last row's lower-minus-upper count. Thus

    C=sum_(O') epsilon_j eta_k sign(y_k-x_j)
      =sum_j epsilon_j[j-m/2+(1/2)1_(j=n)]
      =n^2/2-mn/2+1/4=-(2n-1)/4.                           (4)

Here sum epsilon_j=n and sum epsilon_j*j=n^2/2, including both
half endpoints. Therefore

    sum epsilon eta f_y
      =(1/2)sum epsilon eta(f_y+f_x)+C/2.

PD-T159 gives Lambda_c=(4/Q)sum epsilon eta f_y+1/m. Inserting(4)
leaves 2C/Q+1/m=1/(2Q), proving(1). In particular the apparent
order1/n antisymmetric term cancels with the actual exceptional atom.
This cancellation alone implies no value for the first asymptotic
coefficient of the remaining symmetric sum.

No identification of a swapped-mesh interpolation problem is used.
The numerator transpose is solely algebra inside the same finite sum;
the original exceptional x-mode and degree remain those of PD-T159.

### 2. Periodization and the consecutive-mesh CRT involution

Periodize the board to0<=j<2n,0<=k<2m, j+k odd. Reflection of either
coordinate preserves its parity and cosine. An interior folded index
has two representatives and an endpoint has one, so the full periodic
sum of any cosine-dependent summand is FOUR times the endpoint-weighted
sum in(1). There is exactly one periodic collision on this odd board,
(n,m); (0,0) has even parity. Remove it.

The map d=mj-nk modulo2Q bijects this odd periodic board with residues
modulo2Q. To check injectivity, equal residues imply equal j modulo n
and equal k modulo m. The two possible pairs on the full periodic board
then differ by simultaneous shifts(n,m); these shifts change j+k parity
because n+m is odd. Thus only one is in the odd board. Both sets have
2Q elements. The removed collision maps to d=0.

Let e=mj+nk for actual integer representatives. Exact algebra gives

    a*d-e=2Q(j-k),      a^2=4Q+1.                         (5)

Since j-k is odd, e congruent a*d+2Q modulo4Q. Put
P=(j*pi/n+k*pi/m)/2 and T=(j*pi/n-k*pi/m)/2. The symmetric summand is

    (2+x_j+y_k)/|x_j-y_k|
       =[1+cos P cos T]/|sin P sin T|.                       (6)

Writing the actual d as its canonical residue plus2Q times an integer,
(5) shows cos P cos T=-cos(a*q_d)cos(q_d), while
|sin P sin T|=|sin(a*q_d)|sin(q_d). This proves that(6)=K_d.
Also gcd(a,2Q)=1 from a^2=4Q+1, so sin(a*q_d) cannot vanish for
1<=d<=2Q-1. The other sine is positive on that range. Periodization
of(1) now proves(2). It also gives K_(2Q-d)=K_d and K_Q=1, but that
reflection only halves an O(n^2) term count.

### 3. The signed substitution is the old full-row obstruction

The same calculation gives cos(j*pi/n)-cos(k*pi/m)
=2 sin(a*q_d)sin(q_d). Thus Ktilde_d corresponds exactly to the
SIGNED periodic summand(2+x_j+y_k)/(x_j-y_k), with the collision
removed. Define folded signed sums

    R_y=sum_(O') epsilon eta (1+y)/(x-y),
    R_x=sum_(O') epsilon eta (1+x)/(x-y).

PD-T226's zero-phase signed periodic first-coordinate row equals n
for1<=k<=m-1, equals -n^2 at k=0, and has only its finite collision
value n at k=m. Removing that collision makes the last rational row
zero. Folding the first coordinate divides each row by2, and eta_0=1/2.
There are n interior rows; hence R_y=-n^2/4+n*n/2=n^2/4.

The weight of O' is Q/2-1/4. Since the difference of the two signed
numerators is -1 at every regular pair,

    R_y-R_x=-(Q/2-1/4),
    R_y+R_x=n^2/2+Q/2-1/4.

Multiplication by4 for the periodic board yields
sum Ktilde=2n^2+2Q-1=4n^2+2n-1, proving(3).
Every K_d is positive. There really are negative signed terms: at
d=m, a*q_d=pi+pi/(2n), whose sine is negative. Consequently the
absolute sum strictly exceeds the signed sum. Its deleted corner mass
is exactly Lambda_c-(2n+1)/m; PD-T269/270 make this asymptotic to
(4/pi^2)log^2 n. This is the SAME signed-full-row versus absolute-partial
obstruction in IDEA-329/F03, now displayed in the global arithmetic chart.
It is not a new negative mechanism and receives no PD-N allocation.

## Scope, exact residual and open items

The transpose test succeeds as the finite identity(1): it exposes the
endpoint atom1/(2Q) and a symmetric kernel. The global resummation test
does not pass: (2) is an equivalent O(n^2) absolute correlation. In
particular its alternating sine signs cannot be erased to invoke an
ordinary signed cotangent reciprocity formula. The missing quantity is
the controlled absolute-minus-signed correlation

    (1/(2Q))sum_d(K_d-Ktilde_d),

with all endpoints, to the original O(log n/n^2) scale after subtracting
the full A_(n+1/2)^2+kappa-1/(n+1/2) expression. This record supplies no
such estimate. Symmetry under exchanging n,m does not by itself force
an asymptotic first correction to vanish or identify it as -1/N.

The parent target remains OPEN, not PARTIAL. Other H rounds may control
the residual by a different uniform signed method; this round stops.

## Checks, sources and history

PAPER algebra only. No numerical/script/import/native/compiler/source/
control/quadrature/degree job occurred. No external theorem or PDF was
used; inherited local proofs supply all dependencies. Distinct review
has not occurred and this is not the required Claude audit.

2026-11-07, Codex requested/API gpt-6.1-sol xhigh; rules/input
2c69ba538473b8fdd9147635256289f74e75ccbb. Root released H03 only after
the shared gate, and the owned idea/attempt preregistered hypotheses,
separation and kill criteria BEFORE derivation. Root later supplied the
same transpose suggestion, already included in that first test. Original
sharp target and failed collapse are retained; no further round is implied.
