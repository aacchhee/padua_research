# PD-T?argmax-bridge-codex-D14-norm — A finite phase-grid global norm

ID kind: PD-T.
Aliases: quarter-phase norming mesh; Peano norm absorption; sampling
bootstrap; continuous global S norm from finite vertices.
Split from: D14 model-dependency simplification.
Split into: the degree512 instance and model-free global argmax
application are in `D14-model-free-512.md`.

## Statement

For EVERY integer n>=2 set m=n+1,N=nm,kappa=n/m,h_0=1,h_j=2 for j>0.
Use the original corrected finite kernel and odd board

    G_n(u,v)=sum_(r+s<=n) h_r*h_s*cos(ru)*cos(sv)-cos(nu),
    Gamma^-={(j,k):0<=j<2n,0<=k<2m,j+k odd},
    S_n(alpha,beta)=(1/(2N))*sum_Gamma^-
         |G_n((j*pi+alpha)/n,(k*pi+beta)/m)|.

The exceptional(n,0) coefficient is ONE and all collision values are
the values of this finite polynomial. Define

    T={(a,b):a>=0,b>=0,a+b<=1},
    E={(i/4,j/4):i,j nonnegative integers,i+j<=4},
    V_n=max_((a,b) in E) S_n(pi*a,pi*b),
    M_n*=sup_((alpha,beta) in R²) S_n(alpha,beta).

Then M_n* is finite, attained on pi*T, and

    M_n* <= V_n/[1-pi²(1+kappa²)/128]
          <= V_n/(1-pi²/64)
          < (784/663)*V_n.                           (1)

In particular, if ACTUAL outward vertex uppers give V_n<=V and
784V<663B for a rational B>0, then S_n<B on ALL real phases.
The non-strict safe bound M_n*<=784V/663 also holds.

The same B bounds the original corrected physical Lebesgue function
lambda_n and EVERY complete signed board/cardinal polynomial family:

    |(1/(2N))*sum_Gamma^- sigma_jk*G_n(...)|<=M_n*,
    |sum_(Padua nodes) epsilon_i*L_i(x,y)|<=lambda_n(x,y)<=M_n*,

for all real |sigma_jk|,|epsilon_i|<=1 and all(x,y) in[-1,1]².
After actual-corner phase substitution the latter bound is GLOBAL in
all real phase variables as required by D08's signed-family theorem.

## Definitions, assumptions and status

The L_i are exactly PD-T101/PD-T364's corrected Padua cardinal
polynomials with their original endpoint weights. No statement about
the location/value of an unknown physical maximizer is assumed.
All algebra is exact; the displayed rational factor uses pi<22/7.

Overall status: **PROVED analytic developer theorem**. Distinct D14
mathematical review is pending. The finite-degree instance and its
validated numerical inputs are split off and are not premises of(1).

Candidate disposition: retained standard quantitative variant of D08
Peano/Bernstein and the existing norm-absorption mechanism. No historical
novelty, first norming theorem or priority claim is made.

## Depends on

The finite kernel definition; D08-point-box.md's proved finite Riesz
Bernstein identity and common Peano interpolation; D08-point-box-norm.md's
finite period/evenness adapter; PD-T364's exact reflection inequality
lambda=S-Delta<=S at an all-physical-center cover. The essential parts
of the absorption and geometry are proved below.

No completed asymptotic model, D05 uniform model-error theorem, D06
completed-model numerical allowance, PD-T271 corner constant, global
argmax theorem, sampled maximum identity or log-squared norm theorem
is used. Even D08's coarse Parseval numerical norm is unnecessary:
compactness supplies the finite true norm variable.

## Proof

### 1. Finite continuous global norm before any estimate

S_n is a finite sum of absolute values of trigonometric polynomials,
so it is continuous on R², including every collision. Reindexing j,k
modulo2n,2m shows, for integers p,q with p+q even,

    S_n(alpha+p*pi,beta+q*pi)=S_n(alpha,beta).        (2)

The parity filter is unchanged because p+q is even. Separately replacing
j by-j or k by-k, and using the kernel's separate cosine evenness,
gives separate evenness in alpha and beta. These are exact finite sums;
there is no n,m exchange or limiting argument.

For any real pair put s=(alpha+beta)/(2pi),t=(alpha-beta)/(2pi).
Choose integers j,k so s'=s-j,t'=t-k lie in[-1/2,1/2]. Then

    alpha'=pi(s'+t'), beta'=pi(s'-t'),
    |alpha'|+|beta'|=2pi*max(|s'|,|t'|)<=pi.

The original and primed pairs differ by the even-lattice vector
pi(j+k,j-k), so(2) and evenness map the original S value into pi*T.
The closed T is compact. Continuity therefore proves

    M_n*=max_T S_n(pi*a,pi*b)<infinity.              (3)

This is an existence statement about the TRUE continuous norm. Its
value is not supplied by the grid, Lambda_c or the desired argmax.
It is positive: at(alpha,beta)=(pi,0) the odd-board point(j,k)=(2n-1,0)
has kernel G_n(2pi,0)=2N>0. Hence V_n>=S_n(pi,0)>0.

### 2. Why the true M_n* is a legitimate Peano input

Let f_jk(alpha,beta)=G_n((j*pi+alpha)/n,(k*pi+beta)/m)/(2N).
Then ||f||_1=S_n<=M_n* GLOBALLY by(3). Every fixed signed linear
combination of these components is a trigonometric polynomial with
alpha frequencies r/n and beta frequencies s/m, |r|,|s|<=n. The
accepted finite Bernstein identity therefore gives, choosing the signs
of the derivative components at the target point,

    ||f_alphaalpha||_1<=M_n*,
    ||f_betabeta||_1<=kappa²*M_n*.                  (4)

The norm is over the whole real phase domain before derivatives are
estimated. Finite degree n in the physical angle becomes bandwidth1
in alpha and kappa in beta. No grid derivative inequality is assumed.

The common nonnegative linear-interpolation Peano kernel on[x_l,x_h]
has integral(x-x_l)(x_h-x)/2. Apply it to the SMOOTH vector f, then
take the l1 norm. Apply the two positive interpolation operators in
succession on a real rectangle B. Equations(4) give precisely

    sup_B S_n <= max_(vertices B) S_n
        +(M_n*/8)[width(alpha)²+kappa² width(beta)²]. (5)

This is D08 ordinary Peano, with a mathematically valid true global
norm substituted for its abstract M. The proof needs finiteness and
global validity of M, not a prior numerical estimate. It never
differentiates nonsmooth S_n and never sums individual derivative
suprema. Thus there is no component-count factor or cusp assumption.

### 3. Closed quarter-square cover and every outside vertex

For integers i,j>=0,i+j<=3 use the TEN closed rectangles in turns

    B_ij=[i/4,(i+1)/4]x[j/4,(j+1)/4].               (6)

They cover T after clipping. Explicitly, for(a,b) in T choose
i=max(0,ceil(4a)-1),j=max(0,ceil(4b)-1). These integers are0..3,
their intervals contain a,b, and i+j<=3: if a+b<=1 and at least
one coordinate is positive, i+j<4; the origin is immediate. This
also covers all axes, grid intersections and the hypotenuse exactly.
No tangent patch or irrational boundary strip is discarded.

The distinct RAW vertices of these rectangles are the15 points E
plus the FOUR points(i/4,j/4) with i,j in{1,2,3,4},i+j=5.
Each extra point lies in[0,1]² and folds by

    (a,b)->(1-a,1-b)                               (7)

to a point of E with coordinate sum3/4. Formula(7) preserves S^t(a,b)
=S_n(pi*a,pi*b): translate by(-1,-1), an even-lattice vector, then
reflect both signs. Consequently EVERY vertex of EVERY B_ij has
S value<=V_n, including vertices outside T. Folding changes only
the S evaluation argument; it does not alter a rectangle's widths.
Further boundary canonicalization is optional and changes no value.

In radians both widths in(6) are pi/4. Therefore(5) gives on every
rectangle, and hence on the whole closed T,

    S_n <= V_n + theta_n*M_n*,
    theta_n=pi²(1+kappa²)/128 <=pi²/64<121/784<1.   (8)

### 4. Absorption and the signed families

Take the maximum over T in(8) and use(3). Since1-theta_n>0,

    (1-theta_n)M_n*<=V_n,
    M_n*<=V_n/(1-theta_n)<=V_n/(1-pi²/64).

The exact upper pi<22/7 gives1-pi²/64>1-121/784=663/784.
Together with V_n>0 this proves all of(1). For outward uppers V_n<=V,
M_n*<=784V/663<B whenever the stated strict rational test holds.

Every board coefficient family of magnitude<=1 is dominated pointwise
by S_n. At any physical point PD-T364 provides a physical odd-center
phase chart and lambda=S_n-Delta with Delta>=0. Thus lambda<=M_n*.
Every cardinal coefficient family of magnitude<=1 is dominated by
lambda. Actual-corner phase substitutions stay in[-1,1]² for ALL real
alpha,beta, so this last signed-family bound is global there too.
This proves the family assertions without any argmax premise. QED.

## Checks, obstruction comparison and limitations

The proof is analytic, with no new numerical execution. PD-N183/IDEA598
remains valid: it treats degree-M algebraic polynomials on M+1
equispaced integer nodes and disproves a uniform polynomial grid
derivative transfer. Here(4) uses the TRUE continuous norm, and(6)--(8)
PROVE the finite-set norming comparison at fixed scaled bandwidth.
The grid maximum is never asserted equal to the global maximum.

This theorem alone proves no argmax, useful vertex size, all-degree
complexity or onset. It holds for every n>=2, but a useful B requires
validated actual point uppers for that degree. No numerical conclusions
at untested degrees follow from the degree512 instance.

The prospective gate, alternatives, source freeze and bounded metadata
command are in `../ideas/D14-grid-norm.md` and
`../attempts/D14-grid-norm.md`. Distinct mathematical review and final
Claude audit are separate. Root alone may adopt dependency changes.

2026-11-06, Codex gpt-6.1-sol xhigh, rules/input
`e13a538bda80e6cc785f4835937b2ca338bc1d6f`; bounded20min.
