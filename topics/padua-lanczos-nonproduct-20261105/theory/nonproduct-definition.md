# PD-T?lanczos-nonproduct-codex-P4-01 — affine-product definition and admission lemmas

ID kind: PD-T.
Aliases: genuinely non-product; invertible-affine independence; support-hull
admission; nonmultiplicative rectangular weights.
Split from: the P4 structural-family target, which remains OPEN.
Split into: none. The weighted model, atomless model and transfer are
separate supporting results split from that same target, not from these
admission lemmas; see the corresponding P4 theory records.

## Statement

Normalize every nonzero finite positive Borel measure to mass one. A
probability measure mu on R^2 is **affine-product** if there are probability
measures nu1,nu2 on R, neither a point mass, and an affine map

    F(s,t)=B(s,t)^T+c,             det(B) != 0,

such that mu=F_#(nu1 tensor nu2). Equivalently an invertible affine coordinate
change makes the two coordinates independent with nonconstant factors.

The campaign's class of **genuinely non-product** measures consists of
probability measures whose support is not contained in any affine line and
which are not affine-product under this definition. Measures supported on a
line or a point are called **degenerate** and are excluded from family
admission, rather than counted as genuinely non-product. Noninvertible
maps and a Dirac factor are never admissible certificates of affine-product
structure. Finite atomic and continuous measures use the same definition.

The following admission statements hold.

1. If mu has compact full-dimensional support K and is affine-product,
   conv(K) is a nondegenerate parallelogram. If K itself is convex it must
   itself be that parallelogram.
2. Consequently a measure with support a nondegenerate triangle or a closed
   disk is genuinely non-product. A finite measure with strictly positive
   weight at every node of `{(i,j):i,j>=0,i+j<=L}`, L>=1, is genuinely
   non-product. An invertible
   affine image of any of these remains genuinely non-product.
3. Let A={a_1,...,a_r}, B={b_1,...,b_s}, with distinct real entries and
   r,s>=2. Give every point of A times B a positive weight W_ij, with total
   weight one. This measure is affine-product iff W has rank one. The same
   criterion holds after any invertible affine image of that support.
   Thus one nonzero 2-by-2 minor proves genuine non-product status even
   though its support hull is a parallelogram.
4. For a compactly supported measure, U(n) means

       integral p^2 dmu > 0 for every nonzero p in Pi_n.

   A positive density almost everywhere on a nonempty open set implies
   U(n) for every n. On the finite triangular support in part2, U(n)
   holds for 0<=n<=L. If L>=n+1 then M=N_L>N_n. Mere M>N_n does not
   imply U(n) on an arbitrary finite support.

## Definitions

Support is the closed topological support, not a sampling domain. A random
cloud drawn from a disk does not automatically have support equal to the
disk. Pi_n is the real polynomial space of total degree at most n and
N_n=(n+1)(n+2)/2. All weights used for admission are strictly positive.
The coordinate order used for capacities is separately fixed; affine
invariance of the *admission class* does not imply affine invariance of a
specific BJ or mirror capacity.

The finite exact model is a positive atomic measure with arbitrary
represented Euclidean vector sources and M>N_n plus U(n). The continuous
exact model is H=L2(mu), bounded coordinate multiplication on compact
support and arbitrary H-valued sources. Its polynomial dimension is N_n,
while H is infinite-dimensional for the atomless families considered
here. Exact cubature may identify polynomial moments and recurrence
coefficients; transfer of arbitrary-source capacity is a separate
theorem, as proved in the linked P4 model/transfer records. In particular
finite cubature is never identified silently with the atomless source
space.

## Assumptions

All affine maps in the definition and admission statements are invertible
over R. Compactness is required in part1 and in the elementary extrema
argument for part3. Continuous Jacobi-type triangle or disk examples must
have integrable positive weights and the stated full support. Signed
quadrature weights lie outside this positive-measure setting.

## Status by part

Overall status: PROVED (written analytic admission lemmas).

| Mathematical part | Status | Evidence |
|---|---|---|
| Parts1–4 under the explicit definition | PROVED | Self-contained proof below |

Candidate disposition: retained definitions/admission support. These
statements give no growth-rate classification.

## Depends on

Elementary support, convexity and polynomial facts proved below. No
external theorem or unverified literature fact is used.

## Checks

Analytic development only. No numerical experiment or independent audit
claimed. Direction workers must instantiate the hypotheses for their own
families; this file does not certify a point set that was not supplied.

## Sources

The controlling handoff01 requests an affine-product definition. Existing
PD-T324 discloses SH's latent affine product; PD-N012 warns that support
shape does not classify measured loss. Neither is used as a proof premise.
The P4 prospective gate records repository and literature coverage limits.

## Proof or evidence

For probability measures nu1,nu2, the support of their product is the
Cartesian product of their supports: a product neighborhood has positive
mass exactly when each factor neighborhood does; rectangles form a local
base. An invertible affine map is a homeomorphism, so

    K=F(A times B),       A=supp(nu1), B=supp(nu2).

If K is compact, its inverse image A times B is compact, hence each nonempty
factor is compact. Neither is a singleton. Write their extrema as
a_-<a_+ and b_-<b_+. Their convex hull satisfies

    conv(A times B)=[a_-,a_+] times [b_-,b_+].

Containment from left to right is immediate; the four corners belong to
A times B and span the rectangle, proving the other containment. Applying
F proves part1's convex-hull assertion. If K is convex, F^{-1}(K)=A times B
is convex. Its coordinate projections A,B are convex subsets of R, so they
are the complete intervals; K is the parallelogram itself.

A triangle has three extreme points. A parallelogram has four. Every point
on the circle bounding a disk is extreme, whereas a parallelogram has four
extreme points. The finite triangular lattice has hull with vertices
(0,0),(L,0),(0,L). These are full-dimensional non-parallelogram hulls, so
part1 excludes affine-product structure. If F_#mu were affine-product for
an invertible F, composing its product representation with F^{-1} would
make mu affine-product. This proves part2 and affine invariance.

For part3, the hull of the given support is an axis-aligned rectangle. In
any affine-product representation its two product-axis directions are
exactly the two edge directions of that rectangle. Each column of its
linear map must therefore be parallel to one of the physical axes, with
different axes for the two columns, possibly after exchanging factors.
The latent change of coordinates is thus a separate scaling/translation
of each physical coordinate, possibly exchanged. Independence is unchanged
by these separate invertible maps. Hence physical weight independence is
necessary: W_ij=u_i v_j. Conversely such a factorization is a product
representation. A positive matrix has rank one iff all its 2-by-2 minors
vanish: fixing W_11>0 gives W_ij=W_i1 W_1j/W_11. Normalizing the positive
factors gives probability factors. Invertible affine invariance extends
this to a parallelogram grid.

For part4, if integral p^2 vanishes and the density is positive almost
everywhere on an open set O, p is zero almost everywhere on O. Continuity
then makes p zero on O: a nonzero value has a neighborhood on which |p|
is bounded below. A polynomial zero on an open rectangle is identically
zero, by the univariate polynomial identity applied successively to each
coordinate. Every nonempty open O contains such a rectangle. This proves
U(n) for every n.

For a polynomial of degree<=n<=L vanishing on the triangular lattice,
restrict to row j=0: there are L+1>=n+1 distinct x values, so p(x,0)=0
identically and y divides p. On row j=1, divide by its nonzero y factor;
the remaining polynomial has degree<=n-1 and vanishes at L>=n distinct
x values. Hence y-1 divides that remainder. Continue through j=n; the
result would be divisible by product_(j=0)^n(y-j), of degree n+1, unless
p=0. Positive weights turn injectivity into positive definiteness. Finally
M=N_L>N_n when L>=n+1. An arbitrary support on a conic can have arbitrarily
many nodes while violating U(2), proving why cardinality alone is inadequate.

## Scope

SH_n and rotQ_N are affine-product controls. Triangle families and
full-support disk measures pass the geometric part of N1. Finite disk
grids pass this part only if their actual convex hull is proved not a
parallelogram (or another explicit non-product proof is given). Nonlinear
perturbations require their own support/hull or weight proof. Padua needs
its exact finite support, positivity, U(n) and M>N_n checked at the tested
degree. A square interpolation measure has M=N_n and cannot be admitted
at that degree under the finite N1 gate.

## Open items

Each direction's exact-data and dimension obligations; all-degree
aggregate separation on an admitted family; a useful structural criterion.

## History

- 2026-11-05: Codex P4 developer, gpt-6.1-sol xhigh allocation, runtime
  metadata unexposed; rules read at ed5515ed84e0e7b12163175dce9f22a859c89c99.
  Definition explicitly excludes singular affine maps and degenerate factors.
  No shared registry, Git or handoff mutation by this worker.
