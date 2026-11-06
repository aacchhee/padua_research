# PD-T?nn-mop-stability-codex-31 — local joint-data NN backward geometry

ID kind: PD-T. Aliases: common-support compatible image; mass-gauged NN
embedding; nearest compatible array; projected joint-data backward error.
Split from: none. Split into: none.

## Statement

Fix N>=1. Let D be the ordered, mass-normalized input domain

    x_1<...<x_N, w_{j,l}>0, sum_l w_{j,l}=1, j=1,2,

restricted to inputs for which every mixed index |nu|<=N is normal.
Let F:D->R^K contain all four monic NN coefficient fields at |nu|<=N-1,
including their structural zero entries, in a fixed order. Fix p0 in D.
Then:

1. F is real analytic and injective; its derivative has rank 3N-2.
   Near y0=F(p0), its image M is an embedded real analytic manifold of
   dimension 3N-2. It is the actual positive common-support compatible
   manifold, rather than an arbitrary zero-curvature variety.
2. Fix any positive definite matrix W on the ambient coefficient space.
   Every y in a sufficiently small neighborhood of y0 has a unique nearest
   point pi(y) in F(D) for the W-norm. The corresponding p*(y)=F^{-1}(pi(y))
   is unique and real analytic locally. Thus the pair

       eta_c(y)=||y-pi(y)||_W,
       eta_d(y;p0)=||p*(y)-p0||_B

   is well defined for any fixed norm B on the gauge-fixed input tangent
   coordinates. Neither norm is implicitly the forward metric of PD-T290.
3. Write A=DF(p0) in independent input coordinates and
   A_W^+=(A^T W A)^(-1) A^T W. For e->0,

       p*(y0+e)-p0 = A_W^+ e + O(||e||^2),
       pi(y0+e)-y0 = A A_W^+ e + O(||e||^2).

   In particular eta_d is bounded locally by C||y-y0|| for a finite C.
4. The strict joint-data backward error

       beta(y;p0)=inf{||p-p0||_B:p in D,F(p)=y}

   has value +infinity for y outside F(D). For y in F(D) near y0 it is
   finite and equals ||F^{-1}(y)-p0||_B. The two-component projected
   quantity above never silently substitutes for beta.

## Definitions and assumptions

Normality and the monic NN convention are PD-T286. The normalized input
space has N node coordinates and two open (N-1)-simplices, dimension3N-2.
Normality is open: there are finitely many nonzero mixed determinants.
Mass gauges remove the two independent positive scaling symmetries;
ordered nodes remove the permutation ambiguity. Polynomials remain monic.
W must be positive definite and frozen near p0. A field-scaled Euclidean
norm qualifies; the nonsmooth maximum-of-field-sup norms need not give a
unique nearest projection. No assertion is made at nonnormal data, zero
weights, colliding nodes, or with unfixed masses.

## Status by part

Overall status: **PROVED**, by the analytic argument below. No computer
proof or numerical stability theorem. Candidate disposition: retained
known-geometry application; no novelty or priority claim. The numerical
computation of a certified nearest projection remains separate and OPEN.

## Depends on

PD-T286 (mixed defining systems and NN identities). Elementary finite
spectral theory of real symmetric matrices, the analytic implicit function
theorem, and compactness in finite dimensions; needed uses are supplied
below. No source theorem about arbitrary compatible NN arrays is assumed.

## Proof

**Analyticity.** Each polynomial coefficient solves a finite linear system
whose entries are polynomials in nodes and weights and whose determinant
does not vanish on D. Thus polynomial coefficients are rational analytic.
The h-ratio and subleading-coefficient formulas in PD-T286 make F analytic;
their denominators are nonzero by neighboring normality.

**A smooth left inverse from both complete marginal axes.** Extract from y
the N diagonal coefficients b_((k,0),1) and N-1 positive coefficients
a_((k,0),1), k=1,...,N-1, and likewise the second marginal axis. Form the
symmetric tridiagonal matrices J_j with these b's on the diagonal and
sqrt(a)'s as positive off-diagonals. At y0 they are Jacobi matrices.

For the j-th normalized measure, let phi_0=1,...,phi_(N-1) be its
orthonormal polynomials with positive leading coefficients. The square
matrix Q_{l,k}=sqrt(w_{j,l}) phi_k(x_l) is orthogonal, because its column
inner products are precisely their discrete orthogonality relations.
The marginal recurrence gives diag(x)Q=QJ_j, including the final column:
the degree-N node polynomial vanishes on the support. Consequently J_j
has the distinct eigenvalues x_l and e0^T E_l(J_j)e0=w_{j,l}, where E_l
is the spectral projection for the l-th ordered eigenvalue. This proves
the inverse identity without presuming an inverse Favard theorem.

Simple eigenvalues and their ordering persist near J_j(y0). Each ordered
eigenvalue is real analytic there by the analytic implicit function
theorem applied to det(lambda I-J), whose derivative at a simple root is
nonzero. The spectral projection is the analytic matrix polynomial

    E_l(J)=product_(h!=l) (J-lambda_h I)/(lambda_l-lambda_h).

Its e0 entry gives analytic positive weights near y0, summing to1 because
sum E_l=I. For arbitrary ambient y near y0 define G(y) using the nodes of
J_1, the weights of J_1, and the ordered weights of J_2. G is analytic,
lands in D after shrinking the neighborhood, and G(F(p))=p. J_2's nodes
need not equal J_1's for arbitrary y; this deliberate definition supplies
a left inverse only and is not itself a compatibility assertion.

Thus G composed with F is the identity on D. Differentiation gives
DG(y0) A=I, so A is injective and has rank3N-2. The same spectral inverse
also proves global injectivity of F on D. Choose 3N-2 independent rows of
A. Their coordinate projection composed with F has nonsingular derivative;
the analytic inverse function theorem expresses F(D) locally as a graph
over those coordinates. The topology assertion uses continuity of the same spectral left inverse:
if F(p_j) tends to y0 for inputs anywhere in D, then p_j=G(F(p_j)) tends
to p0. Thus no distant part of the image accumulates at y0. This is also
the exclusion argument detailed in the nearest-point paragraph below.
This proves the embedded manifold statement.
An explicit local compatibility equation is

    y = F(G(y)).

Its solutions are exactly the local image: one direction is immediate
from G F=identity; the other is the displayed equality with p=G(y).
It includes matching marginal spectra, all mixed orthogonality, every
path identity and the terminal boundary. Flatness alone is not substituted.

**Nearest point.** Use independent input coordinates near p0 and set

    L(p,y) = (1/2)(F(p)-y)^T W(F(p)-y),
    H(p,y) = D_p L(p,y) = DF(p)^T W(F(p)-y).

At (p0,y0), H=0 and D_p H=A^T W A is positive definite. The analytic
implicit function theorem gives a unique stationary solution p*(y) near
p0. By continuity, the Hessian of L stays uniformly positive definite
on a sufficiently small convex closed input ball and for y near y0.
Hence L is strictly convex there and this stationary point is its unique
minimum. On the boundary of that ball ||F(p)-y0||_W has a positive minimum:
the boundary is compact, F is continuous and injective, and p0 lies
strictly inside. Shrinking y's neighborhood excludes boundary minimizers.

To exclude an input outside this ball with a still closer image, use G:
if F(p_r)->y0 for any sequence in D, its extracted marginal Jacobi data
converge to those of y0. The ordered spectral inversion just proved
forces p_r=G(F(p_r))->p0. Thus a neighborhood of y0 in the full image is
already in the chosen ball. An image outside that neighborhood has a
fixed positive distance from y0, larger than ||F(p0)-y|| when y is close
enough. The local minimum is therefore also the unique global nearest
point in F(D). This proves existence, uniqueness and analyticity of pi
and p*, despite D itself being open.

**First order.** Differentiate H(p*(y),y)=0 at y0:

    (A^T W A) Dp*(y0) = A^T W.

The displayed derivative and chain rule give part3, with quadratic
remainders from analyticity in fixed finite dimensions. Norm equivalence
and continuity give a finite local Lipschitz constant for any B. Finally
injectivity supplies part4; the infimum over the empty preimage is
defined as +infinity. This completes the proof, including N1.

## Checks and evidence

Analytic proof only; no execution is needed for its conclusion. The
measured native-array records must separately report actual projection
or feasible-pair computations and their precision/optimization limits.
An alternating path and an extra scalar anchor cannot certify the
equation y=F(G(y)) on the full triangle.

## Sources, scope and open items

Closest local predecessors are PD-T286/289 and PD-T058's analogous
projection distinction. LIT-347 and LIT-565/568 are repository-mediated
context; this worker has not freshly read their fulltexts. No source
claim, absence claim, new inverse theorem or optimal-precision algorithm
is inferred. Constants/radius are local and input dependent. Uniform
radius bounds, scalable certified nonlinear projection, and a rounding
analysis yielding joint backward stability of a native algorithm remain
OPEN. Supporting geometry does not label that stability target PARTIAL.

## History

2026-11-05, Codex requested gpt-6.1-sol xhigh; pinned source/rules
823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1. Original D5 request retained:
define/prove local full joint-data well-posedness and separate approximate
compatibility. The theorem addresses that geometry; its algorithmic
stability application remains a distinct target.

Parent unresolved target: [stable-solver-target.md](stable-solver-target.md); supporting results do not establish its general stability conclusion.
