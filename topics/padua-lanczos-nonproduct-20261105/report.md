# Non-affine-product Lanczos span drift — development report

2026-11-05. Branch `codex/padua-lanczos-nonproduct-20261105`,
[draft PR #30](https://github.com/aacchhee/padua_research/pull/30).
Coordinator: Codex, requested gpt-6-astra high; mathematical development:
gpt-6.1-sol xhigh; exact scan development: gpt-6.1-sol medium. Rules/input
head `cafb74ab6f7738c8af83d0cd0f518b81af16f253`; base main
`be9a8318150204711d5446d2ea26284cf1ed0819`. Final IDs are not assigned.

## Main result and its limit

The requested existence goal is proved for the authorized weight-perturbation
route. There is an explicit family of positive measures that are **not an
affine image of any product measure**, on which BJ has an exponential
first-order aggregate span-capacity lower bound and mirror has a polynomial
full-source upper bound. One fixed nonzero perturbation parameter works at
every degree. The support stays the sheared tensor grid; the nonmultiplicative
weight mode changes with degree. This does not isolate a nonlinear geometric
effect or prove robustness under one fixed smooth density.

Let m=n+2, theta_k=k*pi/(m+1), s_k=cos(theta_k), and
v_k=2*sin(theta_k)^2/(m+1). At physical nodes

    (x_kl,y_kl)=(s_k,2s_k+s_l)

use weights

    w_kl=v_k*v_l*[1+eta*(-1)^(k+l)],  0<|eta|<1.

The measures are positive, normalized and genuinely non-product; a nonzero
weight minor and convex-hull edge rigidity exclude all alternate affine
product axes. The perturbation is invisible to polynomial moments through
degree2n+1. Crucially, the top-U witness remains unit and normal to the
*actual* reweighted polynomial space. This proves, for every n>=2,

    kappa_BJ >= sqrt(2*(4^(n+1)-1)/3),
    0<kappa_mirror <= 2sqrt(6)(n+1)^2(N_n-1).

The ratio lower is exponential up to a polynomial factor; it need not exceed
one at small degrees. A sufficient parameter-radius certificate is
eta_0(n)=1/2 for all n>=2, including each requested n=2,...,10. The theorem
actually covers the larger open interval0<|eta|<1. This is not a maximal
radius or a claim of strict small-degree ordering.

Proofs: [admission](theory/p3-01-high-mode-weight-admission.md),
[moments and normal witness](theory/p3-02-exact-moments-creators.md),
[capacity and radius](theory/p3-03-uniform-capacity-radius.md).

Every capacity statement here fixes physical coordinates, the graded scalar
order, admissible parents and the rule's own relative raw-product Hilbert
source norm. Sources are arbitrary vectors/functions before exact full
orthogonalization. Output is first-order spectral span drift. No actual
IEEE/scalar-error activation, every-error lower, closure growth, uniform
finite-error remainder or adaptive switching theorem is asserted.

## A non-product family with polynomial capacity

Positive Chebyshev Padua measures provide a contrast. Their support hull
has3,5,6 vertices for orders m=1,2,>=3; hence they are never affine-product.
Local finite-cosine identities prove the exactness cutoffs and product
creators without an imported cubature theorem. At every unsaturated degree
1<=s<m, both BJ and mirror satisfy

    sqrt(ceil(s/2)) <= kappa_R(s;m)
                    <= 2sqrt(2)(s+1)(N_s-1).

Thus both are unbounded but polynomially bounded, uniformly in m>s. Every
fixed admissible rule has capacity at least1, so BJ/best also has a polynomial
upper for any finite collection of those rules. This supplies neither a
matching polynomial exponent nor an upper for alternating/pivot capacities.
The full stage s=m is outside this theorem.

Proofs: [Padua admission](theory/p5-01-padua-admission.md),
[capacity classification](theory/p5-02-padua-polynomial-capacity.md).

## Model and structural results

The [common definition](theory/nonproduct-definition.md) uses invertible
affine maps and excludes line-supported measures from admission. The
[weighted finite normal quotient](theory/p4-weighted-normal-quotient.md)
accounts explicitly for weights, monic norms and source scales. In the
[atomless L2 model](theory/p4-continuous-capacity.md), capacity equals the
maximum support value of the pointwise response matrix's spectral norm.
Finite-rank polynomial projection does not reduce that norm because sources
can concentrate on arbitrarily small sets. Finite atoms do not have this
property. [Moment transfer](theory/p4-moment-capacity-transfer.md) therefore
distinguishes exact atomless transfer, bounded-density finite comparison and
one-sided finite-cubature comparison.

The [thin-annulus obstruction](theory/p4-covariance-capacity-obstruction.md)
shows that fixed covariance and fixed distinct principal axes do not bound
even absolute degree-two capacity. It does **not** refute the original
all-degree BJ/best ratio iff. A useful general growth criterion remains OPEN.

## Triangle, disk and the gates

| Gate | Result | Meaning |
|---|---|---|
| N0 | PASS | Fresh exact predecessor replay: six SH cases,88 symbolic identities,44 native prefix rows |
| N1 | PASS in recorded scopes | Triangle, rational ring grid, SH reweighting and unsaturated Padua have written admission/injectivity proofs |
| N2 | T24/H24 INCONCLUSIVE; disk in progress | Finite interval screens do not establish or refute an asymptotic rate |
| N3 | P1/P2 redirect to P4 | No bounded-order full-capacity recursion obtained through8; not a nonexistence theorem |
| N4 | PASS analytically | Uniform sufficient eta_0=1/2; not a numerical scan or optimal radius |

The [triangle admission](theory/p1-triangle-admission.md) covers all positive
weights on its full lattice, with elementary injectivity through the lattice
order. The [continuous creator probe](theory/p1-continuous-creator-probe.md)
checks exact moments,45 basis polynomials and132 creators through8. Sparse
basis relations and a restricted final-source chain do not close the full
capacity norm. No all-degree triangle separation is claimed.

The bounded [primary-source checkpoint](theory/p1-literature-checkpoint.md)
includes a complete read of Xu's preprint
[arXiv1309.1510v1](https://arxiv.org/html/1309.1510v1), documenting standard
Jacobi/Hahn bases rather than a creator-capacity theorem. Unread/unreachable
sources are retained for AC:

| Source | Access/read limit |
|---|---|
| [Dunkl–Xu2014 Chapter5 DOI](https://doi.org/10.1017/CBO9781107786134.007), [publisher chapter](https://www.cambridge.org/core/books/abs/orthogonal-polynomials-of-several-variables/examples-of-orthogonal-polynomials-in-several-variables/485109A71BD36A194B6BC616D95BC371) | Preview/Get access only; no chapter theorem used |
| [Xu journal DOI](https://doi.org/10.1016/j.jat.2014.03.013), [journal page](https://www.sciencedirect.com/science/article/pii/S0021904514000574) | Journal403/DOI resolver unavailable through tool; preprint read instead |
| [Tratnik Meixner/Krawtchouk DOI](https://doi.org/10.1063/1.528507), [Hahn DOI](https://doi.org/10.1063/1.528430) | Fulltexts and reliable article landing pages not acquired in bounded search; metadata only |

Griffiths–Spanò's fulltext was acquired but only its introduction read;
no theorem is imported. No third-party PDF or extract is committed.

The [disk admission](theory/p2-01-family-admission.md) distinguishes continuous
radial measures from the324-point rational D36x9 grid. The latter has only
D4 symmetry and no asserted cubature relation to the continuous disk.
[Whole-algorithm covariance](theory/p2-02-rotation-covariance.md) is proved,
but coordinate swapping mixes fixed Gram–Schmidt columns already at degree2.
It therefore does not identify fixed-order BJ and mirror. The
[finite probe](theory/p2-03-finite-recurrence-probe.md) gives restricted
witness information only. **The disk rate question remains OPEN.**

A separately admitted [D65x9 variant](theory/p2-04-low-denominator-rings.md)
uses36 integer-circle directions with hypotenuse65 and nine radii. Its
coordinate denominator is585 instead of49,725; it is a distinct measure,
not a replacement identity for D36x9. Its exact2–8 pilot matches both
arithmetic paths. The change was motivated by arithmetic cost before
observing a high-degree capacity result; N2 thresholds are unchanged.

## Exact scans and verification

Four rules are BJ, mirror, alternating and exact pivot (X wins ties), with
every source in each prefix. The finite [endpoint record](theory/p6-finite-scans.md)
and [interval screens](theory/p6-n2-screen.md) preserve the distinction between
rational bounds and actual capacities. T24 degree2–20 is inherited accepted
evidence, with fresh N0 replay and a new screen; it is not relabeled a fresh
complete scan. H24_222 uses normalized rational weights proportional to
(i+1)(j+1)(25-i-j), on the same325 triangle nodes.

| Family | Completed matched coverage at this checkpoint | N2 |
|---|---|---|
| Uniform T24 | inherited2–20; fresh pilots/replay | INCONCLUSIVE |
| H24_222 | fresh2–16, four rules,60 exact rows | INCONCLUSIVE |
| D36x9 | fresh2–8, four rules,28 exact rows;16 running | No completed16-window verdict |
| D65x9 | fresh2–8 pilot, four rules,28 exact rows; cost12 checker timed out | No completed16-window verdict |
| SH reweighting | analytic all-degree proof; no bulk algebraic scan | UNRUN |
| Positive Padua | analytic all-degree bounds; algebraic m2–5 checks | UNRUN |

T24 slope intervals on8–12 and12–16 are approximately
[.1374,1.8024] and[-.2165,1.8228]; H24 intervals are
[.0553,1.5395] and[-.2202,1.6512]. Exact outward rational receipts are
authoritative. Independent signed-OLS/corner calculations agree. These
screens are inconclusive because of interval uncertainty, not because a
true rate was computed and rejected.

[Distinct mathematical reconstruction](independent-checks-math.md) accepts
the P3/P4/P5 proofs in its recorded scope and actually reruns exact checks.
[Distinct scan review](independent-checks-scans.md) reproduces the60 Hahn
and28 disk row pairs, independently reconstructs12 small cases with Fraction
arithmetic, verifies the two N2 outcomes and exercises malformed controls.
These supplement the required subsequent Claude substantive audit.
The mathematical review also accepts the P1/P2 admission and covariance
proofs in its dated additions. Registry readiness and pending disk16
additions remain outside completed review scopes unless explicitly added.

The bounded generic/block inverse-checker performance attempts are retained
in [FLINT notes](flint-check-notes.md); no degree16 result used them.
The separately proved [reflection method](p6-reflection-methods.md) reuses
equal squared responses at90 sign-orbit representatives, then expands them
over all324 original node/normal contributions. It retains every source
position and full basis/Gram calculation. Distinct proof review preceded
experiments; a fresh distinct56-row pilot matches all nonelapsed fields.
It is a new dated method variant, not a silent change to earlier plans.
Any subsequent full16 completion must explicitly identify this checker and
its guards before a disk N2 verdict is reported.

## Remaining scope and paper consequence

For the bivariate Lanczos/V+A note, the all-degree separation theorem can
now say **non-affine-product positive measures**, with the explicit
n-dependent rank-two weight family and the original worst-case aggregate
first-order model. The Padua theorem demonstrates that non-productness alone
does not force exponential BJ capacity. The statement must retain the
degree-dependent weight frequency, exact projection and free-source
limitations; it does not become an IEEE or geometry-only instability theorem.

OPEN work includes continuous triangle/disk rates, a useful cross-family
growth criterion, fixed smooth-density or nonlinear-node robustness, sharp
Padua exponents and general-rule uppers, adaptive switching and scalar/IEEE
activation. N3 redirects and incomplete/unrun scans remain explicit rather
than being replaced by supporting lemmas. Candidate dispositions are retained
in `ideas/` and `attempts/`; actual round budgets are in [rounds](rounds.md).

The [canonical P3 gate-timing disclosure](LOG.md#canonical-protocol-disclosure--p3-gate-timing)
requires a separate protocol disposition; mathematical acceptance does not
waive it. Final IDs, shared registry application, the Claude audit and
readiness review remain later steps. Only AC merges.
