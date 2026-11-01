# PD-T?proof-attempts-2-codex-07 — The global Padua argmax for degree three

Final ID: **PD-T162**. Provisional ID `PD-T?proof-attempts-2-codex-07` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T099 (finite global or exact edge/central-scope split; full-square all-n statement remains OPEN).

ID kind: PD-T.
Aliases: A4(d) n=3; exact corner argmax; exclusion of non-strict cubic plateaus.
Split from: the n=3 finite verification case of A4(d), `PD-T?programme-ideas-claude-05`.
Split into: none. The all-n corner argmax remains OPEN.

## Statement

For the degree-three even-checkerboard Padua family defined in result06,

max_{[−1,1]²} λ_3 = 17/6 + (2/3)sqrt2,

and equality holds exactly at (−1,−1) and (−1,1). This establishes the n=3 finite case of A4(d).

## Definitions

Use the physical coordinates, cardinals, mask convention and relative maxima of result06. A flat mask means one physical gradient component of its signed cubic P_s is identically zero; its polynomial depends on at most one coordinate. Flat here is a verification category, not an assertion that the polynomial is constant.

## Assumptions

The exact degree-three count certificate of result06, together with its additional `global` fields: every non-flat mask has constant gradient gcd and nonzero projection resultants; every flat mask has a complete univariate partition bound below3; every accepted non-corner maximum has a rigorous value enclosure below15/4; and both non-node corners have the exact value stated above, greater than15/4.

## Status by part

Overall status: **PROVED** (written non-strict-maximum exclusion, complete exact value certificate, separate checker and actual independent producer/checker rerun).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| global maximum value and exact equality set for n=3 | PROVED | exact global predicates verified on developer and independently regenerated certificates |

The argument below closes the potential non-strict-maximum gap explicitly. A strict-local-maxima list by itself would not prove the statement. Required Claude audit of Part 2 remains pending.

## Depends on

- `PD-T?proof-attempts-2-codex-05`, the finite signed-cubic reduction.
- `PD-T?proof-attempts-2-codex-06`, the complete strict maximum count and boundary certificate.
- `PD-T?proof-attempts-codex-03 (audit pending)`, through result06's reused two degree-three edge representatives. Dated note 2026-11-01: part1 Claude audit ACCEPTED the local theorem and response 7b8884a2f98518784ff3698dd2f3f9c49c9cdd62 disposed its minor record findings without changing the proof. The literal dependency spelling is retained as requested.

## Checks

The same single essential compressed certificate as result06 has a `global` section. Producer module `../code/a5_global.py` supplies the explicit flat-mask panels, value enclosures and exact corner identity. The separate checker verifies these fields without a root search, as well as the count predicates. The artifact is386415bytes with SHA256 `401a99243ebeb7b3844216a47f8466bbb60086cbba71d2de2088d7626f532b2b`.

The checker implementer's complete run exited0 in217.540s. A different subagent actually regenerated the entire certificate byte-identically, then checked both the independent and developer artifacts, exiting0 in220.972s and220.474s. Full actual commands, code pins, output hashes and receipts are in result06, `../independent-checks-a5-checker.md` and `../independent-execution-a5.md`. All14 malformed-certificate controls were rejected in both independent sessions.

The three complete positive checker receipts agree exactly on the mathematical predicates:

| Verified value bound | Exact rational bound |
|---|---|
| maximum of all supplied flat-mask panel upper bounds |225879/125000<3 |
| largest interior maximum upper enclosure |1188087/500000<15/4 |
| largest open-edge maximum upper enclosure |3021223/1000000<15/4 |
| non-node corner value |17/6+(2/3)sqrt2>15/4 |

Every one of the1004 non-flat masks has constant gradient gcd and nonzero resultants; every one of the20 flat masks has all32 partition panels checked. Every accepted non-corner root has its own rigorously enclosed value. The exact part1 edge representative map is also verified. These finite facts supply precisely the additional hypotheses used in the proof below; numerical fit agreement is not used.

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

This n=3 case is complete. Required Claude audit of Part2 remains PENDING. Higher-degree A4(d) cases and the all-n conjecture remain OPEN; quartic singular maxima require a separate argument.

## History

2026-11-01, Codex `/root/a5_develop`, allocated gpt-6.1-sol xhigh. Root and independent checker identified that strict counts alone do not cover non-strict global plateaus. This separate result adds exact flat-mask bounds and finite stationary-set reasoning, inspected independently by `/root/a2_independent_route`. Initial status was OPEN while the finite checks ran. Promoted to PROVED only after the separate checker and actual independent producer/checker rerun verified the complete count and global fields. Required Claude audit remains PENDING.
