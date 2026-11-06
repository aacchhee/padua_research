# PD-T?lanczos-nonproduct-codex-P2-04 — a common-denominator rational ring variant

ID kind: PD-T.
Aliases: D65x9; 36 directions with common hypotenuse65; resource-response ring grid.
Split from: P2 finite-family implementation; original D36x9 is retained unchanged.
Split into: none.

## Statement

Let A contain the four integer axis vectors (±65,0),(0,±65), and all
eight sign/swap images of each of the four integer pairs

    (16,63), (25,60), (33,56), (39,52).

Define the finite probability measure D65x9 by equal mass1/324 at each
point

    z_(k,a,b)=(ka/585,kb/585),  (a,b)∈A,  1<=k<=9.       (1)

There are exactly36 directions and324 distinct rational nodes. The least
positive integer that is a common denominator for all node coordinates
is585, a factor85 smaller than the corresponding denominator49,725 for
the original D36x9. D65x9 has injective evaluation on Π_17, is not an
invertible affine image of any product of two univariate measures, and
has M>N_s for every2<=s<=16. Its positive exact moment, monic GS and
squared-norm data through17 are rational; normalized data are algebraic.
Thus it independently passes N1 for the requested degrees2–16.

The label65 denotes the common hypotenuse, not the number of directions.
This is a different finite measure from D36x9 and from every continuous
radial disk measure ν_μ.

## Definitions

Π_s, N_s=(s+1)(s+2)/2, and affine-product have exactly the definitions in
[PD-T?lanczos-nonproduct-codex-P2-01](p2-01-family-admission.md). A common denominator means an integer
q>0 such that q times every coordinate is an integer. Directions are
(a/65,b/65); the nine radii are k/9. All weights are exactly1/324, not
radial cubature weights. D65x9 is invariant under the sign/swap D4 group.

## Assumptions

The directions, nine radii and weights are precisely (1). All324 points
are included once. Comparisons with D36x9 use its fixed original four
triples, not a changed version of that family. No optimality of65 among
all possible common denominators is claimed.

## Status by part

Overall status: PROVED (elementary analytic admission).

| Mathematical part | Status | Evidence |
|---|---|---|
| Exact direction count and denominator reduction | PROVED | Integer identities and denominator argument below |
| Non-affine-product and injectivity through17 | PROVED | Extreme points and circle-factor proof below |
| Rational exact data and M>N_s through16 | PROVED | Positive rational moment form and dimension count |

Candidate disposition: retained routine implementation variant. The
capacity-rate target and any claimed runtime advantage remain OPEN.

## Depends on

The elementary support/product and circle-divisibility arguments in
PD-T?lanczos-nonproduct-codex-P2-01. They are recalled below for this exact measure; no external
theorem or unread published formula is used. Prospective Round3 delta
gate: [novelty-gate-P2.md](../novelty-gate-P2.md).

## Checks

The admission proof preceded the one-shot exact direction/count, radius,
D4 and denominator check below. It executed successfully with exit0 in
under one second. No matrix rank experiment or capacity scan is needed
for the analytic proof. P6 owns fresh scan code, its own full-input hash,
resource preregistration and independently checked endpoints. No actual
runtime or capacity improvement is claimed before those runs.

Frozen executed command, from repository root (standard-library exact
arithmetic; canonical text uses sorted Fraction coordinate pairs):

```sh
python3 -B - <<'PY'
from fractions import Fraction as F
from math import lcm, isqrt
import hashlib,json
A={(65,0),(-65,0),(0,65),(0,-65)}
for a,b in ((16,63),(25,60),(33,56),(39,52)):
    for u,v in ((a,b),(b,a)):
        for sx in (-1,1):
            for sy in (-1,1):
                A.add((sx*u,sy*v))
assert len(A)==36 and all(a*a+b*b==65*65 for a,b in A)
G={(F(k*a,585),F(k*b,585)) for k in range(1,10) for a,b in A}
assert len(G)==324
assert all((y,x) in G and (-x,y) in G for x,y in G)
assert {x*x+y*y for x,y in G}=={F(k*k,81) for k in range(1,10)}
q=lcm(*(v.denominator for z in G for v in z))
assert q==585
oldA={(F(1),F(0)),(F(-1),F(0)),(F(0),F(1)),(F(0),F(-1))}
for a,b,c in ((3,4,5),(5,12,13),(8,15,17),(7,24,25)):
    for u,v in ((F(a,c),F(b,c)),(F(b,c),F(a,c))):
        for sx in (-1,1):
            for sy in (-1,1):
                oldA.add((sx*u,sy*v))
oldG={(F(k,9)*x,F(k,9)*y) for k in range(1,10) for x,y in oldA}
oldq=lcm(*(v.denominator for z in oldG for v in z))
assert oldq==49725 and oldq//q==85 and G!=oldG
circle=set()
for a in range(-65,66):
    b=isqrt(65*65-a*a)
    if a*a+b*b==65*65:
        circle.update(((a,b),(a,-b)))
assert circle==A
raw=''.join(f'{x} {y}\n' for x,y in sorted(G)).encode()
print(json.dumps({'directions':len(A),'nodes':len(G),'radii':9,'D4':True,'circle_integer_enumeration_matches':True,'least_common_denominator':q,'old_least_common_denominator':oldq,'denominator_reduction_factor':oldq//q,'different_from_D36x9':G!=oldG,'node_sha256':hashlib.sha256(raw).hexdigest(),'node_text_bytes':len(raw),'weight':'1/324','analytic_rank_scope':17},indent=2,sort_keys=True))
PY
```

Actual output:

```json
{
  "D4": true,
  "analytic_rank_scope": 17,
  "circle_integer_enumeration_matches": true,
  "denominator_reduction_factor": 85,
  "different_from_D36x9": true,
  "directions": 36,
  "least_common_denominator": 585,
  "node_sha256": "1e86eb8db994e48f395fb357ddee77102bc386053237296931bfcd6026d315b7",
  "node_text_bytes": 4002,
  "nodes": 324,
  "old_least_common_denominator": 49725,
  "radii": 9,
  "weight": "1/324"
}
```

This supplements the analytic proof and is not a separately audited
computer proof. No independent checker or scientific scan was executed by
P2 in this round. The rank scope in this receipt labels the analytic
argument; no numerical or exact matrix-rank computation is claimed.

## Sources

No external source imported. The coordinator suggested considering a
common hypotenuse such as65; the explicit four-pair set and proof here
are derived directly. No new geometry or priority mechanism is claimed.

## Proof or evidence

The elementary identities

    16²+63² = 256+3969 = 4225 = 65²,
    25²+60² = 625+3600 = 4225,
    33²+56² = 1089+3136 = 4225,
    39²+52² = 1521+2704 = 4225

give four rational unit-direction orbits. Each pair has positive distinct
coordinates, so its eight sign/swap images are distinct. Their unordered
absolute coordinate pairs differ, and none meets an axis. Thus the four
axis directions plus four eight-point orbits give4+4·8=36 directions.
Nodes at different k have different radii, so there are9·36=324 points.
Equation(1) gives common denominator585. The coordinate16/585 occurs and
gcd(16,585)=1, so every common denominator must be divisible by585. The
least common denominator is therefore exactly585.

For original D36x9, all coordinates have denominators dividing9c for
c∈{5,13,17,25}. Their LCM is9·25·13·17=49,725. Its k=1 points include
the coordinates7/225,5/117 and8/153, each in reduced form. Their
denominator LCM is49,725, proving that this original common denominator
is exact. Consequently49,725/585=85. This is a common-denominator
reduction; it is not a claim that every individual coordinate denominator
is smaller (585 exceeds the old individual upper bound225).

Each outer-ring node d has norm1. The linear functional z↦d·z has unique
maximum1 over the support at z=d, since equality in d·z<=||z||<=1 forces
z=d. Hence the convex hull has36 extreme points. A compact nondegenerate
product support has a rectangle as its convex hull; an invertible affine
image has a parallelogram, with four extreme points. A degenerate product
factor would put the support on a line, also impossible. D65x9 is not
affine-product.

If p∈Π_17 vanishes at all nodes, its restriction to each radius-k/9 circle
is a trigonometric polynomial of degree at most17 with36 distinct zeros.
Multiplying by exp(17iθ) turns it into an ordinary polynomial of degree
at most34 in exp(iθ); thus it vanishes on the entire circle. Polynomial
division in y, with the values at y=±sqrt((k/9)²-x²), shows that
x²+y²-(k/9)² divides p, exactly as in PD-T?lanczos-nonproduct-codex-P2-01. Repeating across nine
distinct circles gives nine distinct quadratic factors. A nonzero p
would have degree at least18, a contradiction. Evaluation onΠ_17 is
injective. With positive weights this makes every moment Gram matrix
through17 positive definite. Its entries are finite rational sums, so
monic elimination and squared norms are rational and normalization is
algebraic. Finally N_16=153<324.

The two finite measures are distinct. For example, the outer-ring point
(16/65,63/65) occurs in D65x9. Its unordered absolute coordinates differ
from every original D36x9 direction, so it is absent there. Equal node
counts, radii and weights do not identify their moments or capacities.

## Scope

This admits one new fixed finite family. It supplies no cubature relation,
continuous rotation symmetry, continuum approximation or capacity result.
Original D36x9 expensive/partial runs and their resource outcomes remain
valid records for that original measure. The unchanged N2 thresholds
apply independently to any fresh D65x9 scan. N3's prior redirect remains
in force; no all-degree P2 capacity theorem is attempted.

## Open items

The cheap exact implementation check is complete and the specification
has been sent to P6/root. A separate fresh generic-rational scan, actual
cost advantage, full finite N2 controls and the P2 rate question remain
OPEN. Original D36x9 cost and partial-prefix evidence are unchanged.

## History

- 2026-11-05, focused Round3 after pushed Round2 `13c3146`: Codex P2
  developer, assigned gpt-6.1-sol xhigh; serving metadata unexposed.
  Original rules read at `cafb74ab6f7738c8af83d0cd0f518b81af16f253`.
  Written after delta gate and before any new direction/check execution.
