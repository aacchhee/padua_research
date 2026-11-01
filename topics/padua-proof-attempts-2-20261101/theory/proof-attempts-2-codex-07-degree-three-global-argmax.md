# PD-T?proof-attempts-2-codex-07 — The global Padua argmax for degree three

ID kind: PD-T.
Aliases: A4(d) n=3; exact corner argmax; exclusion of non-strict cubic plateaus.
Split from: the n=3 finite verification case of A4(d), `PD-T?programme-ideas-claude-05`.
Split into: none. The all-n corner argmax remains OPEN.

## Statement

For the degree-three even-checkerboard Padua family defined in result06,

max_{[−1,1]²} λ_3 = 17/6 + (2/3)sqrt2,

and equality holds exactly at (−1,−1) and (−1,1). Thus A4(d) is established for n=3 if the exact finite checks recorded below complete successfully.

## Definitions

Use the physical coordinates, cardinals, mask convention and relative maxima of result06. A flat mask means one physical gradient component of its signed cubic P_s is identically zero; its polynomial depends on at most one coordinate. Flat here is a verification category, not an assertion that the polynomial is constant.

## Assumptions

The exact degree-three count certificate of result06, together with its additional `global` fields: every non-flat mask has constant gradient gcd and nonzero projection resultants; every flat mask has a complete univariate partition bound below3; every accepted non-corner maximum has a rigorous value enclosure below15/4; and both non-node corners have the exact value stated above, greater than15/4.

## Status by part

Overall status: **OPEN — final finite verification and independent execution pending**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| global maximum value and its exact equality set for n=3 | OPEN | final additional certificate predicates and independent run pending |

The argument below closes the potential non-strict-maximum gap explicitly. A strict-local-maxima list by itself would not prove the statement. Required Claude audit of Part 2 remains pending.

## Depends on

- `PD-T?proof-attempts-2-codex-05`, the finite signed-cubic reduction.
- `PD-T?proof-attempts-2-codex-06`, the complete strict maximum count and boundary certificate.
- `PD-T?proof-attempts-codex-03 (audit pending)`, through result06's reused two degree-three edge representatives. Dated note 2026-11-01: part1 Claude audit ACCEPTED the local theorem and response 7b8884a2f98518784ff3698dd2f3f9c49c9cdd62 disposed its minor record findings without changing the proof. The literal dependency spelling is retained as requested.

## Checks

The same single compressed essential certificate as result06 has a `global` section. New producer module `../code/a5_global.py` writes the explicit flat-mask panels, value enclosures and exact corner identity. The separate `a5_checker.py` verifies these fields without a root search, as well as the count predicates. Actual final developer, independent checker and independent producer/checker commands and receipts will be recorded here after completion; they are not yet claimed.

## Sources

Authoritative programme A4(d) and THEORY-05 at 9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. This is one finite degree, not the all-n conjecture. The source's finite-mesh agreement is not used as proof. No literature priority claim is made.

## Proof or evidence

### 1. Exact corner value and rigorous separating threshold

The cardinals at each non-node corner give, by exact algebra,

C = 17/6 + (2/3)sqrt2.

Both node corners have value1. The verified rational radical bracket gives C>15/4. The certificate supplies exact outward value enclosures for every accepted interior and open-edge maximum, each with upper endpoint below15/4. Thus every strict maximum apart from the two non-node corners is strictly smaller than C. It remains to prove that a non-strict global maximum cannot evade this list.

### 2. Every interior global maximum is strict

Let z be an interior global maximum of λ_3, and let M=λ_3(z). Since a corner has value C, M≥C>3. Every active signed cubic P has an ordinary local maximum at z, by P≤λ_3 and equality at z.

Every flat signed polynomial is bounded strictly below3 throughout the square by its supplied32-panel interval certificate. Hence no active P is flat at z. For every remaining P, the checker verifies that its two gradient components A,B have constant gcd, so they are coprime, and neither is zero.

The Hessian H_P(z) is negative semidefinite. Suppose it were singular and choose a nonzero null vector v. Since P is cubic and ∇P(z)=0, the exact restriction P(z+tv)−P(z) is ct³. Local maximality forces c=0. Therefore P equals P(z) on a line segment through z. Every sufficiently near point of that segment lies inside the original maximum neighbourhood and also has the same maximal value, so each is itself a local maximum and satisfies A=B=0. The verified nonzero projection resultants put every common real zero of A and B in a finite Cartesian set, by result05. A whole stationary line segment contradicts that finite set. This uses the actual resultant certificate directly and needs no additional coefficient-field argument.

Thus every active P has negative definite Hessian at z and is a strict local maximum there. There are finitely many active patterns. Choose a common sufficiently small neighbourhood where all of them are strictly below their value at z away from z. Every inactive pattern has a strict value gap at z, which persists after further shrinking the neighbourhood. Taking the maximum of all patterns shows that λ_3 itself has a strict maximum at z. It is therefore one of result06's seven accepted interior maxima, all of value below15/4, contradicting M≥C. No global maximum lies in the interior.

### 3. Every possible open-edge global maximum is already covered

At an open-edge global maximum z, every active restricted signed cubic q has a one-dimensional local maximum. A constant restricted q must be either1 or−1, because each edge contains a Padua node and P_s takes a sign value±1 at that node. Since λ_3(z)≥C>1 and q(z)=λ_3(z), no active restriction is constant.

A nonconstant cubic with a local maximum has q'=0 and q''<0; the zero-second-derivative case leaves an odd cubic term and is not a maximum. Consequently z is included in the complete edge root enumeration. The verifier's exclusions remain valid for a global maximum: no derivative or sign mismatch is possible, q''<0 defeats the Hessian exclusion, a regular zero defeats the active-polynomial tangent condition, and a positive inward derivative defeats relative maximality. Every surviving edge candidate in the completed certificate is an accepted root with strictly negative actual inward derivative, hence is a strict relative maximum. Each of those six values is below15/4<C. Thus no open-edge point is a global maximum.

### 4. Equality set

The continuous function λ_3 has a global maximum on the compact square. Parts2–3 exclude every interior and open-edge point. The two node corners have value1, while the remaining two corners both have value C. Therefore the global maximum equals C and is attained precisely at (−1,±1). ∎

## Scope

Only the n=3 instance of A4(d). No statement about large-n corner neighbourhoods, the edge-midpoint expansion or the all-n corner argmax follows. The flat-mask and coprime-gradient predicates are specific verified facts of this degree, not universal properties of arbitrary cubic families.

## Open items

Finish the finite evidence and independent execution before promotion. Extend to n=4 only with a valid quartic treatment; cubic null-line arguments do not exclude singular strict maxima of quartics. Required Claude audit remains pending.

## History

2026-11-01, Codex `/root/a5_develop`, allocated gpt-6.1-sol xhigh. Root and independent checker flagged that strict counts alone leave non-strict global plateaus uncovered. The present separate result adds explicit flat-mask bounds and coprime-gradient reasoning, independently checked as a conditional proof route by `/root/a2_independent_route`. This is a separate mathematical claim from result06 and remains OPEN pending its exact additional finite checks.
