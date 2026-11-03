# PD-T?argmax-effective-codex-06b — All-degree negative corner slopes and an explicit local radius

ID kind: PD-T.
Aliases: R6 all-n corner descent; exact spectral slope bound; shrinking physical corner certificate.
Split from: R6 fixed scaled corner-zone comparison remains OPEN.
Split into: none; the exact spectral identity is the separate codex-06a.

## Statement

For every integer n>=2 use the even-checkerboard cardinals of PD-T101,
put m=n+1, N=nm, c=(-1,-1), and let Lambda_c=lambda_n(c). Let A_n and
B_n be the inward physical x and y derivatives of lambda_n at c.
Then

    -A_n >= (n^2/4)*(Lambda_c-1+2/N) >= n^2/3,                      (1)
    -B_n >= n^2*C_0n >= 8*n^2/15.                                 (2)

In addition, with delta_n=0 for odd n and delta_n=(n-1)/2 for even n,

    -B_n >= (m^2/4)*(Lambda_c-1)-delta_n,
    A_n,B_n <= -n^2*Lambda_c/8.                                   (2a)

Here C_0n is the explicit positive coefficient in codex-06a. In
particular the old all-degree normalized slope premise of PD-T227 holds.
For every h_x,h_y>=0, H=h_x+h_y with

    0<H<=1/(2*[n(n+1)]^3),

one has the explicit strict comparison

    lambda_n(c+(h_x,h_y)) <= Lambda_c-(n^2/6)*H < Lambda_c.          (3)

The same statements hold in inward coordinates at the other nonnode
corner. This proves an all-degree local theorem with n0=2, on a physical
radius of order n^(-6). It does **not** prove the requested fixed scaled
phase zone rho<=1/64, whose physical scale is n^(-2).

## Definitions and assumptions

Exact real arithmetic. All derivatives and h are physical coordinates.
The sigma signs and P_n are those of codex-06a, including the canonical
inward zero-row signs. C_ab, R_a and D_b denote its cosine coefficients,
row sums and column sums. No global argmax or local sign stability is
assumed.

## Status by part

Overall status: **PROVED** (development proof; independent and Claude review pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| All-degree strictly negative slopes and quantitative bounds (1), (2), (2a) | PROVED | Positive row/column sums and edge reflection relations |
| Explicit smaller local radius and decrease (3) | PROVED | Affine sign control and finite-polynomial Taylor bound |

The radius is an elementary corollary of the slope theorem. The fixed
rho target remains OPEN outside this theorem's statement.

## Depends on

PD-T101 exact cardinal formula and positive weights summing to one.
PD-T227 corner values, gradients, zero mask and inward linearity.
PD-T?argmax-effective-codex-06a exact spectrum, positivity and lower bounds.
The elementary endpoint derivative bound used below is also proved in
PD-T227; its recurrence is restated here. No external theorem is imported.

## Proof

### 1. The active polynomial has exactly the corner slopes

At every nonzero cardinal sigma_jk=sign L_jk(c). The zero cardinals have
k=0 and even j>0; by PD-T227 both physical derivatives equal
-2w_j0(-1)^n n/(1-cos(j*pi/n)). Their inward sign is precisely
sigma_j0=-(-1)^n. Therefore for every s,t>=0,

    D_(s,t)lambda_n(c)=D_(s,t)P_n(c)=s*A_n+t*B_n.

Since dT_a(-cos xi)/dx at x=-1 contributes -a^2 in the inward cosine
expansion, the coefficient formulas give

    -A_n=sum_a a^2 R_a,       -B_n=sum_b b^2 D_b.                  (4)

By codex-06a, R_a=R_(n-a)>=0 for 1<=a<n and R_n=1/N. Pairing a and
n-a, whose mean square is at least n^2/4, yields

    sum_a a^2 R_a >= (n^2/4)*sum_(a=1)^(n-1) R_a+n^2/N
                   = (n^2/4)*(Lambda_c-1+2/N).

Codex-06a also gives Lambda_c>=1+2/N+2(n-1)/m. Consequently

    -A_n/n^2 >= (n-1)/(2m)+1/N >= 1/3.

The last inequality is equivalent to (n-2)(n-3)>=0, valid for integer
n>=2. This proves (1). All D_b are positive, so (4) and
C_0n=D_n>=8/15 prove (2).

For the sharper y bound, restrict Q(eta)=P_n(-1,-cos eta) to the odd
m-grid eta=r*pi/m. Its values are 1, apart from r=m when n is even,
where its value is -1. For 1<=b<m, the exact parity-subgrid identity is

    sum_(r odd) f_r cos(a*r*pi/m) cos(b*r*pi/m)
      =(m/4)*(1_{a=b}-1_{a+b=m})                  (1<=a<m),
    sum_(r odd) f_r cos(b*r*pi/m)=0.

These follow by product-to-sum and the finite cosine geometric series.
Multiplying Q's nodal values by cos(b eta) therefore gives

    D_b-D_(m-b)=0                              (n odd),
    D_b-D_(m-b)=4*(-1)^(b+1)/m                 (n even).            (10)

The self-paired mode when m is even requires no separate constraint.
For n odd, positivity and pairing in (4) give
-B_n>=m^2*(Lambda_c-D_0)/4=m^2*(Lambda_c-1)/4.
For n even, write m=2s+1 and pair b with m-b for 1<=b<=s. The excess
over the same symmetric lower bound is bounded below by

    sum_(b=1)^s [m*(2b-m)/2]*(D_b-D_(m-b))
       =sum_(b=1)^s 2*(2b-m)*(-1)^(b+1)=-2s=-n.

The alternating sum is immediate by pairing adjacent b's; if s is odd,
the final unpaired term supplies the same formula. Since D_0=1-2/m,
this proves the first inequality in (2a).

Finally the lower bound in codex-06a implies Lambda_c>=2: its excess
over 2 is (n-1)(n-2)/N. Equation (1) then gives
-A_n>=n^2*Lambda_c/8. For odd n the analogous conclusion for B_n is
immediate. For even n, subtracting n^2*Lambda_c/8 from its new lower
bound gives

    [(2m^2-n^2)/8]*Lambda_c-m^2/4-(n-1)/2 >= 3/4 >0,

where Lambda_c>=2 was used. This completes (2a).

### 2. An explicit affine sign radius

Write l_B=L_B(c), g_B=gradient L_B(c), and w_B for the positive weight.
For k>0 the exact corner value of PD-T227 gives

    |l_B|=2w_B*(1-cos(k*pi/m))/|cos(k*pi/m)-cos(j*pi/n)|
          >= w_B*(1-cos(k*pi/m)) >= 2w_B/m^2.                       (5)

Here |cos v-cos u|<=2 and sin z>=2z/pi on [0,pi/2]. The only other
nonzero cardinal is 00, whose value 1/m also satisfies (5).

The positive kernel coefficients sum to exactly 2n(n+1)=2N, including
the halved exceptional mode. Since |T_a|<=1 at all nodes and
|T_a'(-1)|=a^2<=n^2, direct differentiation of the cardinal formula gives

    max(|g_B,x|,|g_B,y|)<=2w_B*N*n^2.                              (6)

When H<=1/(2N^3), equations (5), (6) imply

    |g_B.h| <= w_B/m^2 <= |l_B|/2

for every nonzero l_B. Hence the affine value l_B+g_B.h preserves its
corner sign. For l_B=0, the two equal derivative components have the
fixed inward sign specified above. Summing their exact affine absolute
values therefore gives

    sum_B |l_B+g_B.h|=Lambda_c+A_n*h_x+B_n*h_y.                     (7)

This argument preserves only the affine values; the true cardinal
remainders are bounded next, so true sign stability is not being assumed.

### 3. Bound all higher terms without a weighted-energy premise

The endpoint Chebyshev recurrence

    (2r-1) T_a^(r)(1)=[a^2-(r-1)^2] T_a^(r-1)(1)

gives |T_a^(r)(-1)|<=n^(2r) for every r>=0 (and zero beyond degree a).
It follows directly from the cardinal coefficient formula, summing the
positive w_B to one, that

    sum_B |partial_x^r partial_y^s L_B(c)|<=2N*n^(2r+2s).           (8)

Taylor expansion is finite, so no interchange or convergence issue
arises. Bounding the terms of total order at least two by the exponential
series gives

    sum_B |L_B(c+h)-l_B-g_B.h|
       <=2N*[exp(n^2 H)-1-n^2 H].                                 (9)

For 0<=z<=1, exp z-1-z<=e*z^2/2. On H<=1/(2N^3), z=n^2 H<=1 and

    RHS(9) <= e*N*n^4*H^2
             <= [e/(2m^2)] n^2 H <= (n^2/6)H,

using m>=3 and e<3. Combining the triangle inequality, (7), (1), (2)
and (9) proves (3). The other nonnode corner follows by the node-preserving
x reflection for even n and y reflection for odd n, exactly as in PD-T228.
QED.

## Checks

The proof is analytic. A separate agent is requested to reconstruct
codex-06a/06b, including all n=2 endpoint cases. Floating slope matches
against the coefficient kernel are only diagnostics, recorded in the R6
attempt. No new finite global certificate follows from these checks.

## Sources and scope

No external source theorem or priority claim. This closes the unrestricted
strict negativity of the two physical corner slopes and gives an explicit
all-n local neighborhood. It leaves global comparison and the uniform
rho<=1/64 comparison unresolved. The previously proposed normalized
bound A_n,B_n<=-n^2 Lambda_c/8 is proved for both axes by (2a).

## Open items

Upgrade the physical radius from order n^(-6) to order n^(-2) using
aggregate sign-change control. Both normalized slope premises are now
proved; the weighted-energy or an equivalent reflected remainder remains
unresolved. All-degree global PD-T099 stays OPEN.

## History

2026-11-03, Codex gpt-6-astra ultra, explicit handoff02 allocation;
rules/input 8a1f394739293953e1566fd24a0a193cc78ff26f, base 440d107.
New all-n slope proof; no assertion that an n-dependent radius resolves
the earlier fixed-phase target.
