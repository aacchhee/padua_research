# IDEA?argmax-bridge-codex-N1-04 — Joint endpoint mesh sum and finite-row chart

2026-11-06. Gate preparation at `0039456f3cf45c3cf4564d57bea30f80156b5483`.
This is a quantitative continuation of IDEA-337/459 and N1-05, not a new
mechanism. The parent authorized reading and preregistration now; substantive
development starts only after its published continuation boundary. Accepted
N1-01 through N1-05 statements and proofs remain unchanged. The separate
[endpoint review](../independent-checks-n1-endpoint.md) accepts N1-03/04/05
at their stated supporting scopes, without a full compactification claim.

## Exact target to test

Use N1-05's first-quadrant phases, m=n+1, L=log n, v_r=(r*pi+beta)/m,
z_r=min(v_r,2pi-v_r), a,A(v),U0 and corrected polynomial row norm
R_r=sum_k |F_rk|. Fix an integer R>=2 and 0<delta<=pi/4. Work with
n>=ceil(2pi*R/delta), so the first and last R rows lie in the endpoint
strips. Let C_n be the actual polynomial-collision rows and set

    P_R={0,...,R-1} union {2m-R,...,2m-1},
    X_(n,R,delta)=(P_R union C_n) intersect {r:z_r<=delta},
    Y_(n,R,delta)={r:z_r<=delta} minus X_(n,R,delta).

There are at most 2R+2 rows in X. They use the exact finite polynomial,
including the corrected (n,0) mode, rather than the continuous pole
profile at a collision. Define the following *target quantity*, not a
claimed compact model:

    E_(n,R,delta)=(1/(nm))*sum_{r in X} R_r
       +(1/m)*sum_{r in Y}
          [A(v_r)*L + {U0+(4a/pi)*log z_r}/z_r].          (T)

The N1-05 integrable residual is deliberately outside (T), with its
already proved cost Q(P,delta). That cost is not altered or absorbed
into an unspecified constant here.

The primary conjectural target is explicit coefficient functions b,c and
an explicit finite K(R,delta), uniform on the entire closed phase diamond,
such that, for both integer parities,

    |E_(n,R,delta) - [(4a/pi^2)*L^2
               +b_(R,delta)(alpha,beta)*L
               +c_(R,delta)(alpha,beta)]|
       <= r4(n;R,delta),
    r4(n;R,delta)=K(R,delta)*(1+log n)^2/n.              (H4)

Finite separate parity charts are allowed only if the derivation requires
them, and must be labeled rather than hidden in b,c. All coefficient
formulas and the numerical/exact expression for K must be written in a
new theory record before any model evaluation. K is a proof obligation,
not a fitted or presently known constant. A statement merely asserting
the existence of b,c,K does not complete this target.

Admissible coefficient formulas have a number of terms and integrals
depending on R,delta, not n. A convergent-series representation is allowed
only with a proved explicit truncation bound; coefficient truncation
errors must retain their L factors. Definitions by an unknown limit of
E, an unresolved growing sum, or a supremum of its error are inadmissible.
No exact formula for a growing sum alone counts as compactification.

The claimed leading coefficient and full uniformity in (H4) are tests,
not inherited results for this artificially separated endpoint block.
If they fail, preserve the exact failed formulation and the obstruction;
do not silently weaken its domain or rate.

## Cheapest decisive test and proof order

1. Derive the joint finite-row/pole expression for the two closest rows
   and one adjacent row from N2/N1-01 before any asymptotic interchange.
   Check the polynomial collision values, both parities and the diamond
   vertices. Compare the fixed-phase limit with coalescing phase sequences
   approaching a vertex on the h=1/n scale. Two different normalized
   limits with the same proposed coefficient data kill that phase-only
   chart immediately; no floating fit is needed.
2. If that chart survives, define local convergent-series constants for
   the shifted 1/(k+t) and log(k+t)/(k+t) sums, with explicit tails.
   Prove the finite-row and mesh-sum remainder **jointly**, including
   offset endpoints and the two cutoff-rounding contributions. Do not
   transfer an unread special-function theorem.
3. Produce b,c and K, then evaluate the assembled analytic error against
   the existing margin budget. Any calculation must be reproducible and
   labeled as such; sparse B1 diagnostics cannot certify the margin.

The separating property is removal of all degree-dependent summation
counts from (T), with a uniform quantified error. A new row identity,
an isolated row limit, a special-function renaming, or more phase samples
does not establish it. N1-05 already supplies an integrable endpoint
residual; repeating that result is not the target.

## Gate, obstacles and retained alternatives

The [round-4 gate addendum](../novelty-gate-N1.md) records the registry
update and exact reading scope. Closest full records are IDEA-337/459,
T216/T226/T269/T270/T365 and N1-01 through N1-05/N2. No external source
or historical priority claim is used. N132 rules out dropping the
phase-dependent logarithmic term; a=0 therefore remains in the domain.

- **Primary phase-only logarithmic chart (H4): active, OPEN.** Kill it
  if a coalescing collision or endpoint sequence prevents its uniform
  error, or if the purported coefficients still depend on a growing set
  of degree indices. Failure of this chart does not refute the full N1
  target.
- **Explicit bounded transition/sawtooth chart: deferred repair.** If
  the first test exposes missing microscopic data, retain that data as
  an explicit bounded coordinate derived from the actual pole offset,
  with finitely many charts and a proved tail. State its formula/domain
  before testing it. This is the one permitted correction of this model,
  not an unlimited sequence of fitted refinements.
- **Shifted-special-function notation alone: equivalent bookkeeping.**
  It may simplify a proof but is not a distinct result without the
  degree-independent evaluation and uniform remainder obligations.
- **Independent unweighted bounds for the finite rows and singular
  sum: deferred.** Resume only with a proof that they retain the joint
  endpoint cancellation. The existing positive terms cannot simply be
  bounded separately and then declared an absolute-small error.

The original B3 rule is unchanged: if the complete proposed remainder
stays at least half the relevant comparison margin through 10^6, permit
one explicit correction and then stop that model. No B3 verdict follows
from one component or an unknown K. Two empty rounds stop the direction;
max15 is a cap, not a quota. A result with a different rate or domain
requires its own preserved formulation and a concrete budget test.

## Scope, allocation and stopping boundary

Even success on (H4) leaves the central v=pi chart, interior outer
quadrature and complete S-minus-defect comparison to be assembled. It
does not by itself supply an effective n1, certify new degrees or release
B4. No full-profile claim will be inferred from the endpoint block alone.

The configured N1 allocation remains the parent's explicitly justified
gpt-6-astra ultra, as retained in handoff02. This step merits that hard-math
allocation because it must control simultaneous phase, lattice-offset
and h->0 limits through colliding poles while preserving absolute values
and the exceptional corrected mode. The runtime does not independently
expose serving metadata. Root alone owns Git and shared records.

No mathematical development, model computation or fit is claimed in this
gate-preparation record. The first substantive checkpoint must report a
uniform chart/remainder or a precise obstruction with its one repair.
