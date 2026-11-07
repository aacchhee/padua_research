# F02-N1 — The unmodified full-band integral has no uniform one-sided C/n mesh loss

ID kind: provisional PD-N?argmax-bridge-codex-F02-01.
Aliases: second-index mesh obstruction; fixed-distance parity alias;
unmodified full-band Riemann-reference failure.
Split from: the FIRST mesh-feasibility obligation of F02/I09.
Split into: none. The released fifth-floor target remains OPEN.

Status: **PROVED developer PAPER obstruction**, distinct review required.
Candidate disposition: the unmodified exact-integral reference is
**REJECTED: failed** at the scope below. This is not a Q-floor refutation.

## Exact statement and negative scope

Use the ORIGINAL corrected PD-T364/C01 finite kernel, projections and
weights. For every integer n>=128 put m=n+1,N=nm and take the admissible
physical odd center

    J=1,K=2, alpha=beta=0, theta=pi/n, gamma=phi=2*pi/m.

Let Q_n be its full vertical projected defect. Let g_v be EXACTLY the
zero-phase continuous full-band integral of PD-T211/266/267:

    y_+=cos(b+gamma), y_-=cos(b-gamma),
    h_gamma(x,b)=min((1+y_+)/(x-y_+),(1+y_-)/(y_--x))
                  if y_+<x<y_-, and0 otherwise,
    g_v(gamma)=(2/pi^2)*integral_[0,pi]^2 h_gamma(cos u,b)du db.

Integral boundary values are immaterial; finite polynomial values still
define the discrete Q_n at collisions. Then

    lim_(n->infinity) Q_n/log n=16/(3*pi^2),                 (1)
    lim_(n->infinity) [g_v(2*pi/(n+1))-Q_n]/log n
                      =(8*log2-16/3)/pi^2>0.              (2)

Consequently there is NO finite constant C for which

    Q_v(K)>=g_v(phi)-C/n                                  (3)

holds uniformly over all eligible physical interior-index centers and
zero phases for every n>=128. Even a uniformly bounded loss in place of
C/n is impossible for this UNMODIFIED integral reference. In particular
3/n and8/n cannot be its uniform loss.

The attempted mechanism is a sum-to-its-own-exact-full-band-integral lower
comparison. It is NOT the different claim Q>=1/5-3r/20-3/n, a capped or
smaller reference integral, or a separate discrete endpoint certificate.
Those statements are not negated by (1)--(2). Actual Q_n grows positively.

## Definitions, assumptions and dependencies

Exact real arithmetic; n integer, m=n+1; exceptional highest first-mode
coefficient ONE. Put P=T_(n+1)+T_n and

    G(u,v)=[P(cos u)-P(cos v)]/(cos u-cos v)-cos(nu),
    d(X,Y)=|X|+|Y|-|X+Y|.

The quotient is the finite polynomial divided difference at a collision.
PD-T364/C01 give, at this center and zero phase,

    Q_n=(1/N)*sum_(k=0)^m f_k
            sum_(0<=r<2n,r+k odd) d(H_+,H_-),
    H_+/-=(-1)^r G(r*pi/n,phi+/-k*pi/m)/2,
    f_0=f_m=1/2, f_k=1 otherwise.                         (4)

Both periodic branches are in this sum; they are not an extra factor in
the coefficient1/N. At every regular selected lattice point the EXACT
signed half numerator is1+cos v, hence

    H_+/-=(1+y_+/-)/(cos(r*pi/n)-y_+/-).                  (5)

Thus this witness uses the actual signed-pair formula, without a phase-
blind numerator relaxation. Its phases are zero, so it belongs to every
released radius guard, including r=0. PD-T267 supplies ONLY the already
proved endpoint expansion for the DEFINED continuous integral:

    g_v(gamma)=(8*log2/pi^2)*log(1/sin gamma)+O(1).        (6)

Its finite-n interchange is explicitly excluded there; no interchange
is used here. The discrete asymptotic (1) is proved independently below.
No measured value, quadrature, PD-T271 constant or source theorem enters.

## Proof of the discrete coefficient

### 1. Exact parity, straddling indices and the single collision

Write b=k*pi/m. For2<=k<=n-2, both target angles b-gamma,b+gamma
are in[0,pi]. Their cosines straddle cos u precisely when

    (k-2)/m<r/n<(k+2)/m, 0<=r<=n.

The required parity is r+k odd. For these rows the ONLY such first-half-
circle indices are r=k-1,k+1. Indeed for r=k+j the condition is

    -2<j+(k+j)/n<2,

and j must be odd. Both j=-1,+1 work for2<=k<=n-2, whereas
j<=-3 or j>=3 do not. Their reflected indices2n-r give the other
two distinct periodic representatives, with identical cosines and defects.
Outside this open cosine band the regular numerators in(5) are nonnegative
and the denominators have the same sign, so their defect is zero.

For completeness the remaining nonendpoint rows have these representatives:

| Physical row | Regular positive-half-circle straddling representatives | Other possibility |
|---|---|---|
| k=1 | r=2 | reflected2n-2 |
| k=n-1=m-2 | r=n-2, whose numerator1+y_+ is0 and defect is0 | r=n is the polynomial collision |
| k=n=m-1 | r=n-1 | reflected n+1 |

The regular r=n-2 at k=n-1 also has its reflected partner; both defects
are zero. The endpoint rows k=0,m have identical halves and defect zero,
so their half weights remain literal but contribute nothing.

There are no other quotient collisions on this odd board. Equality of
cosines on the adjacent zero-phase meshes implies r=0 or n modulo2n,
because n,m are coprime. The possible u=v=0 point has even board parity
and is absent. The admitted collision is r=n,k=m-2,v_+=pi. Its signed
polynomial half is n, since G(pi,pi)=2n*(-1)^n. Its other half is

    (1+y_-)/(-1-y_-)=-1,

so its defect is exactly d(n,-1)=2. It occurs ONCE, because r=n is
fixed by reflection. No collision value is replaced by0/0 or a limit
of(5) along arbitrary continuous angles.

Let d_(k,j) be the regular defect at r=k+j, j=-1,+1. We therefore have
the exact decomposition

    Q_n=(2/N)*sum_(k=2)^(n-2) [d_(k,-1)+d_(k,+1)]
                                                +R_n/N, (7)

where R_n is the two copies at k=1, the two at k=n and the single
collision defect2. In particular R_n>=0.

Moreover R_n/N=O(1), uniformly as n grows. One explicit check at k=1
uses u=2pi/n,v_-=pi/m. The chord inequality gives

    cos v_--cos u>=2*(u^2-v_-^2)/pi^2>=6/n^2.

Thus this half has magnitude<=n^2/3 and its defect<=2n^2/3.
At k=n, put t=pi/m. The target numerator maximum is
1-cos(3t)<=9t^2/2, while their cosine span is
2sin(2t)sin t>=16/m^2. The general opposite-denominator bound
d<=4*(numerator maximum)/(span) gives d<=9pi^2/8.
Hence R_n<=(4/3)n^2+9pi^2/4+2, which suffices for(7).

### 2. The logarithmic rows and their exact local coefficient

For2<=k<=n-2,j=-1,+1 set

    u=(k+j)pi/n, v_+=(k+2)pi/m, v_-=(k-2)pi/m.

Then u lies strictly between v_- and v_+, and(5) gives

    d_(k,j)=2min((1+cos v_+)/(cos u-cos v_+),
                (1+cos v_-)/(cos v_--cos u)).             (8)

The exact angle differences are

    v_+-u=pi*[(2-j)n-k-j]/N,
    u-v_-=pi*[(2+j)n+k+j]/N.                             (9)

In the regime k->infinity,k/n->0,n->infinity, angle addition and
sin z/z->1 show, UNIFORMLY in j=-1,+1,

    (N/k)*(cos u-cos v_+)->pi^2*(2-j),
    (N/k)*(cos v_--cos u)->pi^2*(2+j),
    1+cos v_+->2, 1+cos v_-->2.                         (10)

Here is the uniformity needed for summation, rather than a merely
pointwise assertion. For any epsilon>0 one can choose fixed K0 and
delta>0, then n0, so(10)'s errors are below epsilon for
K0<=k<=delta*n,n>=n0. Indeed factor each cosine difference as
2sin((u+v)/2)sin(|u-v|/2). Its first sine divided by k*pi/n is
the product of a sinc factor and

    (1/2)*[1+j/k+(n/m)*(1+/-2/k)].

This tends uniformly to1 as delta decreases, K0 increases and n
increases. Its second sine is |u-v|/2 times a sinc factor tending
uniformly to1 by(9). The remaining exact factors are
2-j-(k+j)/n or2+j+(k+j)/n. They stay bounded away from zero,
for example for delta<1/4 and sufficiently large K0,n. Numerators
converge uniformly to2 since |v_+/-|<=pi*(delta+2/n).
These explicit factors prove the asserted uniformity.

Taking the minimum in(8), which is continuous at these strictly positive
denominators, now gives

    k*d_(k,j)/N ->4/(3*pi^2)                            (11)

in that same uniform sense. The smaller reciprocal has denominator3
for either j. Thus the four periodic contributions per row in(7)
have coefficient16/(3*pi^2*k), rather than the continuous integral's
average coefficient.

### 3. Rows outside the logarithmic range do not change its coefficient

For fixed K0 the finitely many rows2<=k<K0 contribute O_(K0)(1)
after normalization. This follows directly from(8)--(9): each regular
denominator is of order n^-2 with a nonzero positive coefficient at
fixed k,j, so d_(k,j)/N stays bounded. The finitely many smaller n,
if needed, do not affect a limit. The remainder R_n/N is already bounded.

For each fixed delta>0, ALL rows k>delta*n in the bulk of(7)
contribute O_delta(1). To see this without discarding a top endpoint,
let M(b)=1+cos(b-gamma) be the largest numerator. The two denominator
magnitudes sum to2sin gamma sin b. Therefore

    d_(k,j)<=2*M(b)/(sin gamma sin b).                  (12)

For these rows b is bounded away from0 by a positive delta-dependent
constant. If b<=pi/2, M(b)/sin b is then bounded by2/sin b.
If b>=pi/2, put t=pi-b. In the bulk t>=3pi/m>gamma, so

    M(b)=1-cos(t+gamma)<=2t^2,
    sin b=sin t>=2t/pi.

Thus M(b)/sin b is again bounded, including the approach to pi.
Finally sin gamma>=4/m. Equation(12) yields d_(k,j)=O_delta(m),
hence O_delta(1/n) after division by N. There are at most n such
rows and four periodic contributions in each. This proves the claimed
O_delta(1) total with no unaccounted harmonic top tail.

Given an arbitrary eta>0, choose K0,delta,n0 so(11) differs from
4/(3pi^2) by at most eta throughout K0<=k<=delta*n. Equation(7),
nonnegativity, and the bounds just proved sandwich Q_n between

    4*[4/(3pi^2)-eta]*sum_(K0<=k<=delta*n)1/k

and the same expression with +eta plus O_(K0,delta)(1).
For fixed K0,delta this harmonic sum divided by log n tends to1.
Let n grow and then eta decrease to zero. This proves(1).

## Continuous comparison and the obstruction

The already proved PD-T267 expansion(6), applied at gamma=2pi/(n+1),
gives

    g_v(gamma)/log n ->8log2/pi^2,

because sin gamma/gamma->1 and log(n+1)/log n->1. Subtract(1)
to obtain(2). Its coefficient is strictly positive: the elementary
positive atanh series gives

    log2=2sum_(l>=0) (1/3)^(2l+1)/(2l+1)>2/3.

Hence g_v(gamma)-Q_n grows like a strictly positive multiple of log n.
It eventually exceeds EVERY finite constant, and therefore exceeds
C/n for any fixed C. This contradicts(3) on the admissible sequence
J1,K2,zero phases, completing the scoped negative proof.

## Meaning, limitations and the next decisive obligation

The zero-phase numerator is the actual numerator; neither the old N5
a0,c envelope nor independent phase worst cases cause this obstruction.
It comes from the finite parity sampling at the second interior index.
Both periodic branches are counted, the folded1/N normalization is
unchanged, and the sole polynomial collision contributes its exact2.
One-sidedness does not rescue the unmodified integral: the discrete
logarithmic coefficient is strictly SMALLER on this sequence.

The released target Q>=B(r)-3/n,B(r)>=1/5-3r/20 is still OPEN.
This sequence does not refute it, since Q_n itself grows. In particular
one must not infer that no uniform fifth floor, no useful capped integral,
or no endpoint-specific discrete bound exists. Nor is a logarithmic
discrepancy proved for every center or every signed phase.

The next useful test would require a NEW prospectively specified
endpoint-aware reference: either prove a direct finite floor on the
fixed-distance classes, or modify/cap the continuum integrand BEFORE
estimating its mesh loss, then prove that its retained integral still
supports the desired floor and that all intermediate shrinking angles
are covered. Mere macroscopic convergence or replacing(12) by a looser
BV estimate cannot solve this exact comparison. No replacement has been
derived or tested in this round after this first decisive obstruction.

## Checks and history

2026-11-07. Requested/API-assigned Sol xhigh; serving metadata unexposed.
Rules/input4a5de2012bad94601c713b2ff5517f2e3fb80af2. Full gate,
root's separate durable mathematical release and local idea/attempt
inventory preceded derivation. The original PD-T267 endpoint proof was
additionally read in full before invoking(6); PD-T211's full definition
and proof were refreshed. No new source theorem or priority claim.

Verification is the written integer-index enumeration, exact trigonometric
factorization and uniform harmonic-sum sandwich above. No scripts/imports,
scalar/endpoint/phase/degree/native/compile/quadrature/numerical-integral
evaluation or scientific job ran. No Git/shared/old-proof mutation.
Scientific CPU0; ordinary text-tool overhead unmeasured. Distinct review
and root adoption remain required; the developer does not self-approve.
