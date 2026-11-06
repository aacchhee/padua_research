# PD-T?lanczos-nonproduct-codex-p5-01 — exact unsaturated Padua admission

ID kind: PD-T.
Aliases: positive Chebyshev Padua measure; non-affine-product hexagonal
support; sharp cubature cutoff; truncated checkerboard admission.
Split from: P5 aggregate-capacity target (the capacity result is PD-T?lanczos-nonproduct-codex-p5-02).
Split into: none.

## Statement

For each integer m>=1 define x_j=cos(j*pi/m),0<=j<=m and
y_k=cos(k*pi/(m+1)),0<=k<=m+1. Put c_j^(r)=1/2 at j=0,r and 1 otherwise,
lambda_j^(r)=c_j^(r)/r, and

    ν_m = sum_(j+k even) 2 lambda_j^(m) lambda_k^(m+1) δ_(x_j,y_k).

This is a positive probability measure on M=N_m=(m+1)(m+2)/2 distinct
nodes. All coordinates are real algebraic numbers and all weights are
positive rational numbers. It agrees with the continuous probability
product Chebyshev measure

    dμ = dx dy / (pi² sqrt(1-x²) sqrt(1-y²))

on every polynomial of total degree <=2m-1, and this cutoff is sharp:
ν_m(T_(2m)(x))=1 whereas μ(T_(2m)(x))=0. It agrees with the discrete product
of its two normalized Lobatto reference measures on total degree <=2m.

No invertible real affine change of coordinates makes ν_m a product
measure. Its convex hull has exactly three vertices at m=1, five at m=2,
and six at every m>=3. Thus every order is genuinely non-affine-product,
including the low-degree exceptions to the hexagonal hull description.

For m>=2 and 0<=s<m, the weighted evaluations of Pi_s are injective and
M>N_s. The orthonormal polynomials in graded order x^a y^b, first by a+b
then increasing b, are q_ab(x,y)=p_a(x)p_b(y), where
p_0=1 and p_l=sqrt(2)T_l for l>=1. In particular each exact normalized
creator through degree s is a univariate Chebyshev three-term relation.

## Definitions

A positive measure is affine-product if the pushforward under some
invertible affine map R²→R² is a product of two positive measures.
Genuinely non-product means the negation of this property. Weighted
evaluation represents p by (sqrt(w_jk)p(x_j,y_k))_(j+k even), with the
ordinary Euclidean inner product. N_s=(s+1)(s+2)/2.

This ν_m uses positive Chebyshev cubature weights. It is distinct from the
signed Lebesgue-interpolatory weights in the Padua MZ track.

## Assumptions

Exact real arithmetic; the specified even-parity Padua convention. No
floating-point node substitution, external cubature theorem, source-error
model or square-case positivity-radius assertion is used.

## Status by part

Overall status: PROVED (written analytic proof; supplementary check sought
by coordinator separately).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Positive exact data, sharp continuous cubature cutoff and discrete-product transfer | PROVED | Elementary finite cosine sums below |
| Non-affine-product status, all m and low-degree hull exceptions | PROVED | Explicit hull and affine-product hull obstruction below |
| Unsaturated injectivity and product orthonormal creators | PROVED | Exact inner products below |

Candidate disposition: retained variant IDEA?lanczos-nonproduct-codex-P5-01.
No historical novelty claim; product-type recurrence transfer is an
explicit predecessor, PD-T039, and is rederived for these exact conventions.

## Depends on

Self-contained cosine, polynomial and convex-hull algebra. Context only:
PD-T033/039 contain product-type recurrence/moment mechanisms. Their source
reports are not used as imported external proofs.

## Checks

Supplementary exact cases m=2,3,4,5 passed, including122 continuous cubature
moments, all four sharp T_(2m) failures and202 Gram entries. See
[attempts/P5](../attempts/P5.md) for the command and
[exact receipt](../evidence/p5-exact-checks.json) for actual results. The
proof does not depend on a finite computation. Independent
rerun/reconstruction is not claimed by this developer.

## Sources

No external theorem used. Relevant literature INDEX and repository
predecessors were read in the prospective gate. The formulas are classical
ingredients; no priority assertion follows from this local proof.

## Proof

For any r>=1, summing complex exponentials on the 2r equally spaced points
of the circle and pairing l with 2r-l gives

    A_r(a):=sum_(j=0)^r lambda_j^(r) cos(a*j*pi/r)
           = 1 if 2r divides a, and 0 otherwise             (a>=0).

Indeed the paired full-circle average has interior terms twice and the
two endpoint terms once; its weights are exactly lambda. The ordinary
geometric sum is zero unless its frequency is divisible by 2r.
Also (-1)^j cos(a*j*pi/r)=cos((a+r)*j*pi/r) at these nodes, so

    B_r(a):=sum_j (-1)^j lambda_j^(r) cos(a*j*pi/r)
           =1 if a ≡ r (mod 2r), and 0 otherwise.

The parity identity 2*1_(j+k even)=1+(-1)^(j+k) now yields

    ν_m(T_a(x)T_b(y))=A_m(a)A_(m+1)(b)+B_m(a)B_(m+1)(b). (1)

For a+b<=2m-1 the first term is nonzero only at a=b=0, while the second
term would require a>=m and b>=m+1, hence a+b>=2m+1. These moments coincide
with μ's. Products of Chebyshev polynomials form a basis of the same
total-degree space, proving cubature. Formula (1) at (a,b)=(2m,0) gives the
sharp failure. The B product also vanishes throughout a+b<=2m, proving
agreement with the reference discrete product measure at that degree.
At (0,0), (1) equals one; all node weights are strictly positive. One of
m+1,m+2 is even, so exactly half their product grid has each parity.
Monotonicity of cosine on [0,pi] gives distinct axis nodes and M=N_m.
Each cos(j*pi/r) is algebraic, since it is half the sum of a root of unity
and its inverse. Its indicated angle, or monotone index in [-1,1], fixes
the exact real embedding. Weights are the displayed rational numbers.

For s<m, products q_ab with a+b<=s have Gram products of total degree
<=2s<=2m-2. Cubature identifies these inner products with μ's; elementary
cosine orthogonality gives the identity matrix. Thus evaluation is
injective. These products have the prescribed leading monomials and no
other monomials of equal total degree, so they are the unique graded
Gram–Schmidt basis with positive leading coefficient. The standard
identity 2xT_l=T_(l+1)+T_(l-1) proves the creator recurrence. With

    β_0=0, β_1=1/sqrt(2), β_l=1/2 (l>=2),

it reads x p_l=β_(l+1)p_(l+1)+β_l p_(l-1). For creating degree <=s, all
terms are in the established orthonormal range. Finally N_m>N_s when s<m.

It remains to prove the geometric admission independently of the moments.
For even m>=2 put a=cos(pi/m), b=cos(pi/(m+1)). Nodes with x=±1 have
y in [-b,1]; every other node has |x|<=a. Hence all nodes lie in the hull
of the following listed nodes:

    (1,1),(-1,1),(-1,-b),(-a,-1),(a,-1),(1,-b).           (2)

Each is present by parity. For m>=4, 0<a<1 and 0<b<1, so they are precisely
six vertices, with positive-length horizontal, vertical and sloping edges.
For m=2, a=0 makes the two bottom entries coincide, giving precisely five
vertices; none of the other vertices becomes collinear.

For odd m>=3 the corresponding list is

    (1,1),(-a,1),(-1,b),(-1,-b),(-a,-1),(1,-1).           (3)

Nodes with x=-1 have |y|<=b; all other nodes have x>=-a. These facts show
containment in the hull of (3); every listed point is a parity-admissible
node. Again 0<a,b<1 gives precisely six vertices. At m=1 direct enumeration
gives (1,1),(1,-1),(-1,0), a triangle. This also proves full affine span for
every m and proves the asserted hulls without relying on a picture.

If an invertible affine image of ν_m were a product, both factors would
have finite support (the image measure is finite) and at least two support
points (full affine span excludes a line). The support of their product
is the Cartesian product of the two supports, whose convex hull is the
rectangle joining their four extrema. Its invertible affine preimage is
a parallelogram with exactly four vertices. This contradicts the three,
five or six vertices just proved. Thus ν_m is never affine-product.

## Scope

N1 is established for every m>=2 and s<m with exact algebraic coordinates
and rational positive weights. The continuous measure μ is a proof
reference only; it is product, and is not the admitted sample family.
There is no assertion of continuous moment exactness at total degree2m,
no top-stage s=m capacity claim, and no IEEE rounding statement.

## Open items

Independent mathematical check, coordinated separately. Aggregate capacity
is the separate PD-T?lanczos-nonproduct-codex-p5-02 theorem. Alternating/pivot capacity upper bounds are
not supplied by this admission lemma.

## History

2026-11-05: Codex `/root/p5_padua`, assigned gpt-6.1-sol xhigh; rules/input
`cafb74ab6f7738c8af83d0cd0f518b81af16f253`. Gate and candidate records saved
prospectively. All-degree analytic proof, no computer-proof dependency.
