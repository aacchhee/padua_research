<a id="pd-tlanczos-nonproduct-codex-p2-01--radial-disk-and-rational-ring-admission"></a>

# PD-T474 — radial disk and rational ring admission

Provisional alias: `PD-T?lanczos-nonproduct-codex-P2-01`.

ID kind: PD-T.
Aliases: disk support obstruction to affine products; D36x9; rational D4 rings.
Split from: P2 family admission; the capacity-rate target remains OPEN.
Split into: none.

## Statement

A probability measure on R² is **affine-product** if its pushforward by
some invertible affine map is a product of two univariate probability
measures. A measure is genuinely non-product if it is not affine-product.

1. For every real μ>-1, the probability measure

       dν_μ=(μ+1)/π (1-x²-y²)^μ 1_(x²+y²<1) dx dy

   is genuinely non-product. Its polynomial form is positive definite in
   every finite degree. For rational μ>-1 all polynomial moments are
   rational, hence its graded monic orthogonal polynomials and squared
   norms are rational; their normalized versions have algebraic data.
2. Define D to contain the four axis directions and, for each triple

       (a,b,c)=(3,4,5),(5,12,13),(8,15,17),(7,24,25),

   all eight directions (±a/c,±b/c),(±b/c,±a/c). Let G contain

       (x,y)=(k/9)d,   1<=k<=9, d∈D,

   with equal positive weights (either 1 or 1/324). Then G has exactly
   M=324 rational points, is genuinely non-product and has injective
   evaluation on Π_17. In particular M>N_s for every 2<=s<=16, where
   N_s=(s+1)(s+2)/2. This fixed family is admitted for those test degrees.

## Definitions

Π_s denotes the real bivariate polynomials of total degree at most s.
The continuous model uses H=L²(ν_μ), with coordinate multiplication X,Y.
The finite model uses the weighted evaluation Hilbert space on G. They
are different measures. D36x9 is invariant under sign changes and x/y
interchange (D4), and is not invariant under all rotations.

## Assumptions

μ>-1; invertibility in the affine-product definition; every finite-grid
weight is strictly positive. The tested grid is exactly the one above.

## Status by part

Overall status: PROVED (written analytic proof).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Continuous disk admission and exact moments | PROVED | Elementary integral and support proofs below |
| D36x9 admission through degree 17 | PROVED | Root count, divisibility and convex hull below |

Candidate disposition: retained family admission. No drift-rate conclusion.

## Depends on

No external theorem or unproved scientific dependency. Elementary
polynomial root counting and linear algebra are used explicitly.

## Checks

The proof is independent of computation. The small rational checker in
code/p2_disk_probe.py executed and verified point distinctness, radii and
D4 closure, recorded in evidence/p2-disk-probe.json. Its continuous disk
moment reconstruction is a separate finite check through degree8. These
outputs supplement the proof; they do not supply its degree reduction.

## Sources

No literature theorem imported. Standard disk terminology is descriptive.

## Proof or evidence

For a compactly supported product measure ρ₁⊗ρ₂, support equals
supp(ρ₁)×supp(ρ₂): a product neighborhood has positive measure exactly
when each factor neighborhood does. Its convex hull is
conv(suppρ₁)×conv(suppρ₂), a rectangle if both factors are nondegenerate.
An invertible affine image has a parallelogram as convex hull. A
two-dimensional measure cannot have a degenerate product factor, since
that would put its support on an affine line.

The support of ν_μ is the closed unit disk, because its density is positive
on the open disk and every neighborhood of a boundary point intersects
the open disk in a positive-area set. The disk is not a parallelogram:
every point of its boundary circle is extreme, whereas a parallelogram
has exactly four extreme points. Thus ν_μ is not affine-product. A nonzero
polynomial is nonzero on some open subset of the disk (otherwise it
vanishes identically, by applying the one-variable identity successively
on an open rectangle). Its squared integral is therefore strictly
positive. This proves positive definiteness in every finite degree.

Reflection makes every moment with an odd exponent zero. Polar
coordinates and the elementary beta integral give

       ∫ x^(2a)y^(2b) dν_μ
       = [(2a)!(2b)!/(4^(a+b) a! b!)] / (μ+2)_(a+b),       (1)

where (u)_m=u(u+1)…(u+m-1), (u)_0=1. To verify the beta evaluation,
the angular integral is 2 B(a+1/2,b+1/2), the radial integral is
B(a+b+1,μ+1)/2, and Γ(a+1/2)/Γ(1/2)=(2a)!/(4^a a!). Their product
times (μ+1)/π is (1). Rational μ gives rational positive-definite moment
matrices. Gaussian elimination/Gram–Schmidt uses rational operations and
positive rational divisions; normalization introduces only square roots
of positive rationals. No transcendental quadrature is required.

For the grid, the four triples have distinct unordered absolute
coordinate pairs, and each has 0<a<b<c with a²+b²=c². Thus all 36
directions are distinct rational unit vectors. Different k have different
Euclidean norms, so all 9·36 points are distinct. Every coordinate has a
representation whose denominator divides 9c, with c<=25. On the outer
unit circle all 36 points are extreme: the linear functional z↦d·z has
unique maximum 1 at z=d, since all points have norm<=1. Hence the convex
hull has 36 extreme points and cannot be a parallelogram. The support
argument above proves genuine non-productness, independently of weights.

Let p∈Π_17 vanish at every grid point. On each of the nine circles,
p(r cosθ,r sinθ) is a trigonometric polynomial of degree at most 17.
Multiplication by exp(17iθ) writes it as a polynomial of degree at most
34 in exp(iθ). It has 36 distinct roots; hence it vanishes identically.
If a real polynomial vanishes on the circle x²+y²=r², divide it in y by
the monic polynomial y²+x²-r². The remainder is a(x)y+b(x). At both
points (x,±sqrt(r²-x²)), for -r<x<r, its two values vanish. Subtraction
and addition force a(x)=b(x)=0 throughout an interval, hence identically.
Therefore x²+y²-r² divides p.

Apply this successively to r=1/9,…,1. On each new circle all previous
circle factors are nonzero constants, so the remaining quotient also
vanishes identically there and the next factor divides it. If p were
nonzero it would have degree at least 18, a contradiction. Evaluation on
Π_17 is injective. Finally N_16=153<324, so the oversampling requirement
holds throughout the proposed finite scan.

## Scope

This admits the continuous radial disk and the particular finite rational
grid. It does not equate them or assert cubature, convergence, area-uniform
sampling, full rotational invariance of the grid or identical recurrences.
Nine equally populated radii do not by themselves approximate the radial
law r(1-r²)^μ dr. A scan on D36x9 only concerns that discrete measure.

## Open items

The capacity-rate question remains OPEN. Exact continuous recurrence
reconstruction and finite-grid N2 belong to separate records. N2/N3 must
be disposed before an all-degree P2 capacity theorem is attempted.

## History

2026-11-05, Codex gpt-6.1-sol xhigh assignment. Written after the P2 gate.
No Git mutation, final-ID allocation or independent audit by this worker.
