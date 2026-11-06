# PD-T?lanczos-nonproduct-codex-P1-02 — Exact continuous triangle creator probe

ID kind: PD-T. Aliases: P1 degree-eight moment probe; final-level Legendre
chain under BJ; continuous triangle frozen-response matrix.
Split from: P1 all-degree separation target (OPEN). Split into: none.

## Statement

The executed exact rational probe constructs the monic graded basis through
degree eight of the probability measure with constant density `1/2` on

    D={-1<=x<=1, -1<=y<=-x}.

There are 45 basis columns. In the increasing-total-degree, then increasing
y-exponent order it verifies 153 moment identities, full basis orthogonality,
132 full-projection creator polynomial identities across three rules, 45
squared-norm formula matches, and the same-degree creator pattern stated
below. These are finite computational observations, not an all-degree proof
or an independently checked computer-assisted theorem.

For `r+j=d<=8`, the computed squared norm of the monic column `b_(r,j)` is

    d_(r,j)=4^d / [(d+1)(2j+1) binom(2j,j)^2
                                      binom(2d+1,r)^2].       (1)

For each Y creator of target `(r,j)`, `j>=1`, through degree eight, its
only nonzero earlier *same-degree* monic projection coefficients are

    alpha_(j,j-1)=-1/2,
    alpha_(j,j-2)=(j-1)^2/[4(4(j-1)^2-1)]  (j>=2).           (2)

Every X creator through degree eight has no earlier same-degree coefficient.
Under BJ, for a source injected at `(8,0)` and zero responses before total
degree eight, the scalar final-degree response is independent of the
evaluation point and equals

    g_j=1/binom(2j,j), j=0,...,8,                            (3)

as exactly verified by the BJ frozen recurrence. The chain check in
`p1_moment_probe.py` uses only `records["BJ"]`; (3) is not a three-rule
identity. Equations (1)–(3) are reported only within the executed finite
range.

## Definitions and assumptions

The monic basis is built directly by exact Fraction Gram–Schmidt from the
moment matrix; (1) and (2) are hypothesis checks *after* construction and
are not used to construct its entries. Creator relations use exact full
projection and frozen parents. BJ uses X on j=0 and Y otherwise. Mirror uses
X if r>0 and Y on r=0. Alternating uses X if `2j<r+j` when both parents
exist, and Y otherwise; pure-axis columns use their unique parent. This is
the inherited e1_exact alternating convention.

Sources are the common P4 continuous model's arbitrary L2 aggregate
injections relative to each rule's own raw-product scales. Let `C_d(z)` be
the matrix in [P4-03](p4-continuous-capacity.md). That PROVED model lemma
implies, for this admitted atomless triangle,

    kappa_R(d)=max_(z in D) ||C_d(z)||_2.

This application changes the source space from a finite node set to L2(D).
It neither applies that identity to T24 nor equates their capacities.

## Status by part

Overall status: MEASURED.

| Part | Status | Evidence / limit |
|---|---|---|
| Rational basis/creator identities (1)–(3) through eight, with (3) under BJ | MEASURED | Actual exact developer execution; separate reruns recorded in [audit 01](../audit-01.md#independent-reruns-actually-executed) |
| Seven-point spectral diagnostics | MEASURED, exploratory | Exact C entries plus binary64 SVD; no outward enclosure or global maximization |

Candidate disposition: retained finite structure evidence. N3 full-capacity
recursion route is redirected to P4; no all-degree family or symmetry
conjecture is rejected.

## Depends on

P1-01 admission; P4-03 and its weighted conventions for the continuous
capacity interpretation. All exact arithmetic in the probe is implemented
using Python standard-library Fraction. NumPy is used only for explicitly
exploratory finite-point singular values.

## Checks and commands actually run

Initial exact probe, before the independent moment-formula comparison and
compact-summary option were added:

    timeout 180 python topics/padua-lanczos-nonproduct-20261105/code/p1_moment_probe.py --max-degree 8 --output /tmp/padua-lanczos-nonproduct-20261105/p1-moment-probe.json

It completed the 45/132 creator/norm checks in 0.9911 seconds; the initial
source SHA256 was `2af5ef2d95ffb9c67577eab44231cf153ed358f1711560aadd109be50aea5683`.

After adding the direct physical-triangle moment comparison and summary:

    timeout 180 python topics/padua-lanczos-nonproduct-20261105/code/p1_moment_probe.py --max-degree 8 --output /tmp/padua-lanczos-nonproduct-20261105/p1-moment-probe.json --summary topics/padua-lanczos-nonproduct-20261105/evidence/p1-moment-probe.json

The complete new summary reports all checks true, 153 moments and 1.2289
seconds internally. Python 3.12.14, NumPy 2.3.5 are recorded in the summary
(these reported versions must be read from that file if the environment is
changed). Source SHA256:
`877b77c025734b1a20801f8b4d4f63d53c466b532f22419b79221fb39aab5ff0`.
Raw regenerable output: 33,434 bytes, SHA256
`080c84ee3518ed8407de599f48114d1bec711342d8cc4f9dfcb70de79a1a890f`,
kept at the local temporary output path. The 5,814-byte
[compact evidence](../evidence/p1-moment-probe.json) retains counts,
final-level norms, the chain under BJ, versions, identities and sampled
diagnostics.
The raw output is not a required hidden certificate; the source regenerates
every exact row and no computer-proof status depends on temporary retention.

## Sources

No external orthogonal-polynomial theorem is imported. The reference to a
Legendre-type chain under BJ is descriptive of the finite rational pattern
only. Suggested primary literature remains a separate reading task.

## Evidence and explanation

The routine supporting moment identity (PROVED, excluded from status
aggregation) is

    E[u^a v^b]=2a!b!/(a+b+2)!,  (u,v) in Delta,

obtained by integrating in v and integrating by parts a times in u.
The physical binomial transform follows from x=2u-1,y=2v-1. A separate direct
physical integration checks the constructed moments exactly:

    E[x^a y^b]=(-1)^(b+1)/(2(b+1)) * (I_(a+b+1)-I_a),
    I_k=0 if k odd, and 2/(k+1) if k even.

Every creator residual is checked coefficient by coefficient against the
independently constructed monic column, retaining all earlier-degree terms.
Under BJ, for the special final-degree source, all lower-degree responses
vanish, so only same-degree coefficients from (2) enter. The actual checked
chain under BJ is

    1, 1/2, 1/6, 1/20, 1/70, 1/252, 1/924, 1/3432, 1/12870.

This chain under BJ is explicitly restricted: general sources propagate
through all lower-degree coefficients, and capacity additionally involves
all source scales and the largest singular value of the complete matrix C.
Thus (3), under BJ, does not supply a bounded-order capacity recurrence.

For orientation only, the maxima over seven specified points of the
*numerically computed* singular values are:

| Degree | BJ | Mirror | Alternating |
|---:|---:|---:|---:|
| 1 | 1.7321 | 1.7321 | 1.7321 |
| 2 | 8.8327 | 8.2887 | 8.8327 |
| 3 | 35.6080 | 24.9869 | 32.0729 |
| 4 | 156.2243 | 61.4316 | 93.6080 |
| 5 | 747.5079 | 164.8671 | 253.7508 |
| 6 | 3737.8564 | 413.9343 | 711.5148 |
| 7 | 19200.5138 | 989.4904 | 2143.6533 |
| 8 | 100477.7730 | 2481.3044 | 6862.0927 |

The sample points are the three vertices, three edge midpoints and centroid:
`(-1,-1),(1,-1),(-1,1),(0,-1),(-1,0),(0,0),(-1/3,-1/3)`.
Their exact squared Frobenius traces are retained in the compact evidence
at the points attaining these exploratory sample maxima. Neither numerical
rounding nor continuum maximization is certified. Ratios of these sample
values do not certify capacity ratios or N2.

## Scope and gate outcome

At the end of the degree-eight structure probe no bounded-order recursion
for the **full capacity** was identified. N3's prescribed outcome is
**REDIRECT TO P4**, not PASS and not a theorem excluding every possible
recursion. The symbolic creator recurrences and the restricted chain under
BJ survive as useful exact finite data. P6's separate T24 N2 scan is awaited.
There is no all-degree separation claim and no all-degree proof was attempted.

## Open items

Distinct exact rerun; certified full-support matrix upper bounds or another
P4 criterion; N2 and a correctly matched continuous/discrete comparison;
the suggested primary sources. No automatic x/y swap identifies two rules
when the fixed within-degree Gram–Schmidt order is retained.

## History

2026-11-05: Codex P1 developer, assigned gpt-6.1-sol xhigh; round 2 began only
after the coordinator reported round 1 pushed at `3d49d32`. Preregistered
the probe before creating/executing its code. All computation above is the
developer's own execution; no self-audit or independent rerun is asserted.

2026-11-06: In response to audit-01 A3, corrected the previously unqualified
statement of (3) and its downstream uses to say **under BJ**. The existing
code checks this chain only under BJ. This is a material statement correction;
the degree-eight scope and MEASURED status are unchanged. No new experiment,
proof or candidate was developed, so no new novelty gate applies.
