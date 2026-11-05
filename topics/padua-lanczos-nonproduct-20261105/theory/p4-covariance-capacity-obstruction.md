# PD-N?lanczos-nonproduct-codex-P4-01 — covariance does not bound absolute capacity

ID kind: PD-N.
Aliases: thin-annulus fixed-covariance obstruction; distinct fixed principal
axes; degree2 last-pivot blowup; second-moment capacity limitation.
Split from: P4-04's covariance-only finite-degree control candidate.
Split into: none. Original P4-01's all-degree BJ/best ratio iff remains OPEN.

## Statement

Let 0<epsilon<=1, c in R and lambda>0. Let (S,T) have the probability
measure of constant area density on the annulus

    1-epsilon <= S^2+T^2 <= 1+epsilon,

and set physical coordinates x=S, y=cS+lambda T. Denote their measure by
mu_(epsilon,c,lambda). For every epsilon>0 it is atomless, genuinely
non-affine-product in the common definition, and satisfies U(n) for every
n. Its covariance is independent of epsilon:

    Cov(x,y) = (1/2)*[[1,c],[c,c^2+lambda^2]].               (1)

For every admissible fixed parent rule, in the continuous arbitrary-L2
aggregate source model, its degree2 spectral span capacity satisfies

    kappa_mu(2)^2 >= [3(c^2+3lambda^2)/(8lambda^2)]
                          *(1+epsilon^2)/epsilon^2.        (2)

In particular c=1,lambda=2 gives the same distinct covariance eigenvalues
(3-sqrt(5))/2 and (3+sqrt(5))/2, and the same nonzero principal-axis angles
to x and y, for every epsilon. Yet kappa_mu(2) is unbounded as epsilon->0.
Thus no finite-valued upper bound on this absolute degree2 capacity can
depend only on covariance and physical principal-axis angles for the
campaign's full class of atomless non-affine-product measures.

This does not refute an all-degree iff for exponential BJ/best **ratios**:
the lower (2) holds for every admissible rule and supplies no ratio growth.

## Definitions

Graded order is 1,x,y,x^2,xy,y^2 through degree2. The model is exactly
P4-03: arbitrary L2 injections immediately before exact full projection,
rule's own relative raw-product norm, spectral normal output, exact start.
For epsilon=1 the annulus fills a disk (its inner radius is zero).

## Assumptions

Strict epsilon>0, lambda>0 and fixed physical coordinates are essential.
The singular limit epsilon=0 is a measure on an ellipse and is excluded:
it violates U(2). Formula (2) concerns actual positive-width measures,
not the degenerate limit's recurrence.

## Status by part

Overall status: PROVED (analytic fixed-degree negative statement).

| Mathematical part | Status | Evidence |
|---|---|---|
| Admission, fixed covariance, unbounded lower (2) | PROVED | Written proof below |

Candidate disposition: P4-04 REJECTED: refuted for covariance-only finite
absolute-capacity control. P4-01's original asymptotic ratio target is
deferred/OPEN, not rejected by this result.

## Negative-result scope

Attempted mechanism: bound first-order aggregate absolute capacity using
only second moments and coordinate/principal-axis angle, independently
of higher moments and positive pivots.
Parameter range: degree2, all0<epsilon<=1 on the explicit annulus families;
the c=1,lambda=2 subfamily fixes distinct axes at nonzero angles.

## Depends on

P4-01 common admission lemmas, P4-03 continuous model derivative. The lower
uses just a last-column source normal to Pi_2; it does not need numerical
maximization of the pointwise response matrix.

## Checks

Executed exact rational radial/angular moment and monic Gram–Schmidt
check, epsilon=1,1/2,1/4,1/8, c=0/1,lambda=2:

    python3 topics/padua-lanczos-nonproduct-20261105/code/p4_annulus_check.py > topics/padua-lanczos-nonproduct-20261105/evidence/p4-annulus-check.json

All8 cases PASS, preserving covariance, last-pivot squared norm, last raw
source squared norm and their displayed ratio. The finite check corroborates
the analytic formulas; it is not a finite reduction of the epsilon->0
proof. Receipt records source hash, Python and platform. Developer
execution only; no independent rerun or cross-family12–16 gate claimed.

## Sources

No external theorem or historical novelty claim. P4 gate reads the
earlier support/selection and normal-quotient classifier limitations.

## Proof or evidence

Write R^2=S^2+T^2. Polar coordinates make R^2 uniform on
[1-epsilon,1+epsilon] and angle uniform on [0,2pi], independently. Set
tau=epsilon^2. Then

    E R^2=1,       E R^4=1+tau/3.

Symmetry and the elementary angular integrals E cos^2=1/2,
E cos^4=3/8, E cos^2 sin^2=1/8 give

    E S=E T=E ST=0,
    E S^2=E T^2=1/2,
    E S^4=E T^4=(3+tau)/8,
    E S^2 T^2=(3+tau)/24.                                 (3)

These angular identities follow by expanding cos^2(theta)=(1+cos2theta)/2
and integrating its square and its product with sin^2. The pushforward
under the fixed invertible linear map gives (1).

The annulus has nonempty open interior for every epsilon>0, with positive
density there, so U(n) holds for all n. Its support hull is a disk; after
the invertible map its hull is an ellipse, with infinitely many extreme
points. The common support-hull lemma excludes affine-product structure.

In latent S,T coordinates, monic Gram–Schmidt through degree2 gives

    b_0=1, b_1=S, b_2=T,
    b_3=S^2-1/2, b_4=ST,
    b_5=T^2-1/2 - a*(S^2-1/2),
    a=(tau-3)/[3(1+tau)].

Odd moments vanish, and (3) makes this basis pairwise orthogonal.
For its last norm, write

    d_3=(1+tau)/8,
    Cov(S^2,T^2)=(tau-3)/24,
    d_5=d_3-Cov(S^2,T^2)^2/d_3
        =tau*(3+tau)/[9(1+tau)].                           (4)

In physical graded order the monic basis becomes
1,S,lambda T,S^2-1/2,lambda ST,lambda^2 b_5. Indeed substituting
y=cS+lambda T changes each monomial by a triangular combination of
earlier monomials, with the indicated positive leading scale.
Consequently the physical last squared norm is lambda^4 times (4).

Every admissible parent for the monomial y^2 is y from the previous
degree, using multiplication by Y. Its physical monic parent is
lambda T. The raw product is

    y*(lambda T)=c lambda ST+lambda^2 T^2.

Its squared norm, using the vanishing odd mixed moments and (3), is

    sigma_last^2
       =lambda^2(c^2+3lambda^2)*(3+tau)/24.                 (5)

Choose any unit function e orthogonal to Pi_2 in L2(mu). Such a function
exists because an atomless probability space has infinitely many
orthogonal indicator functions, whereas Pi_2 has dimension6. Inject
only f_last=sigma_last e. Its source norm is1, and all preceding frozen
responses vanish; the last response is f_last because its monic
diagonal coefficient is1. The normal projector fixes it. Thus the output
has one column, of norm sigma_last/sqrt(d_last). Dividing (5) by the
physical lambda^4*(4) proves (2).

For c=1,lambda=2, (1) is [[1/2,1/2],[1/2,5/2]], with distinct eigenvalues
(3+-sqrt5)/2. Its nonzero off-diagonal entry prevents either coordinate
axis from being a principal axis. Both axes and their angles stay fixed
as epsilon varies. The positive constant in (2) is39/32 and epsilon can
approach zero. Any finite-valued covariance/angle-only upper at this
fixed covariance contradicts (2), proving the scoped negative statement.

## Scope

This proves that higher moments/near polynomial breakdown cannot be
omitted from quantitative absolute-capacity bounds. It neither proves
nor refutes exponential dependence on degree, gives no rule-ratio lower,
and says nothing about finite arithmetic source realizability. The
positive source is free and can depend on epsilon; no finite-epsilon
uniform remainder follows. All-degree P4 controls remain incomplete.

## Open items

Original covariance/axis asymptotic iff; useful normalized invariants
including higher-degree Gram data; complete cross-family exact tests;
independent mathematical check of this negative result.

## History

- 2026-11-05: Codex P4 developer, gpt-6.1-sol xhigh allocation, runtime
  metadata unexposed; rules head ed5515ed84e0e7b12163175dce9f22a859c89c99.
  Registered the diagonal variant before the exact run, then added the
  fixed-shear variant before execution to ensure nonzero fixed axis angles.
  Coordinator explicitly approved this fixed-degree candidate kill test
  before the incomplete all-degree cross-family criterion gate.
