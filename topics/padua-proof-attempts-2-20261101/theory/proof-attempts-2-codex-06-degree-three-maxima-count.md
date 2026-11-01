# PD-T?proof-attempts-2-codex-06 — Degree-three Padua strict-local-maxima count

Current audit note, 2026-11-01: Claude audit-01 accepted this record at its stated scope. Historical audit-pending statements below describe development checkpoints.

LITERATURE attribution (audit-01 F8): arXiv 2605.23299v1, §3.3 Table 3, LIT-388. Its reported counts are source statements; the local certificate/proof and candidate-correction scope are separate.

ID kind: PD-T.
Aliases: A5 n=3; 15 total / 7 interior / 6 edge / 2 corner; exact all-sign cubic certificate.
Split from: `PD-T?programme-ideas-claude-06`, A5's n=3 case, preserving the original n=3,…,8 statement and all other cases.
Split into: none; A4(d) global-value corollary is separate result07.

## Statement

For the even-checkerboard Padua nodes

Pad_3={(cos(jπ/3),cos(kπ/4)):0≤j≤3,0≤k≤4,j+k even},

let L_b be their unique polynomial cardinals of total degree at most3 and let λ_3=Σ_b|L_b|. Then λ_3 has exactly **15 strict relative local maxima** on [−1,1]²: **7 interior,6 open-edge and2 corner maxima**. The corner maxima are exactly the two non-node corners (−1,−1) and (−1,1).

## Definitions

Cardinal indices b=0,…,9 are in lexicographic(j,k) order with j+k even. A mask m has sign+1 at b iff bit b is set, and sign−1 otherwise. Interior means both physical coordinates lie in(−1,1); open edges exclude corners. Strictness is relative to the closed square. No floating seed is identified with an exact root.

## Assumptions

Exactly the board above and the exact arithmetic model recorded here. The proof uses algebra over Q(sqrt2), rational Sturm counts and outward Fraction intervals. Trusted implementation dependencies are Python3.12.14 integer/Fraction arithmetic and SymPy1.14.0 exact algebra. The checker independently reconstructs the cardinals and verifies supplied root partitions; it does not trust the producer's root isolation or search decisions. No old certifier arithmetic is used.

## Status by part

Overall status: **PROVED** (written finite reduction, complete exact certificate, separate independent checker and actual independent producer/checker rerun).

| Mathematical part | Status | Evidence |
|---|---|---|
| exact count15 with7 interior,6 open-edge,2 corner maxima | PROVED | complete certificate and verified root IDs |
| obligation(1): finite reduction | PROVED under separate result05 | every mask, projected root pair and boundary type covered |
| obligation(2): degenerate points and boundary coverage | PROVED | part1theorem03 reused; direct physical edge/corner/node tests |
| obligation(3): rigorous root existence, uniqueness and exclusion | PROVED | supplied Sturm partitions and whole-box Krawczyk/contraction predicates |
| obligation(4): every consistent sign pattern | PROVED | all1024 interior masks and3584 canonical edge masks; no early return |
| obligation(5): exact crease/crossing treatment | PROVED | exact polynomial identities and injectivity, without a coincidence tolerance |

The five obligations are routine verification parts of this one degree-three count. No prefix pilot or numerical agreement is used as the proof. Required Claude audit of Part2 remains **PENDING**.

## Depends on

- `PD-T?proof-attempts-2-codex-05`: cubic finite reduction and exact regular-crease/crossing exclusions.
- `PD-T?proof-attempts-codex-03 (audit pending)`: existing local strictness/uniqueness at the two edge representatives x=1,y=±1/sqrt3. Dated note2026-11-01: part1 Claude audit at95279b833bca5967fcf47c1b71a56ff622185b4e accepted this proof; response7b8884a2f98518784ff3698dd2f3f9c49c9cdd62 disposed minor findings without changing the mathematical proof or code. The task's literal dependency spelling is retained. The old MEASURED trace supplies no global coverage.

The new checker reconstructs cardinals by its own exact10×10 monomial Vandermonde inverse and verifies interpolation and partition of unity.

## Checks

Actual final developer command, from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_producer.py --output topics/padua-proof-attempts-2-20261101/outputs/a5_n3_certificate.json.gz --unresolved /tmp/a5-n3-final-unresolved.json > topics/padua-proof-attempts-2-20261101/outputs/a5_n3_producer.json 2> /tmp/a5-n3-final.log
```

It exited0 with `complete:true`, no unresolved disposition and15=7+6+2 maxima. Producer modules are `a5_producer.py`, `a5_arithmetic.py`, `a5_boundary.py`, `a5_global.py`. Every preconditioner is selected from an exact rational enclosure; no floating approximation enters proof arithmetic.

The single essential artifact `../outputs/a5_n3_certificate.json.gz` is386415bytes, SHA256 `401a99243ebeb7b3844216a47f8466bbb60086cbba71d2de2088d7626f532b2b`. Its uncompressed content is2809931bytes, SHA256 `8340b56cfa17f735645c6585ea059bf489ee001cb76dcc254e24ea165242eae1`. This is genuine compression of one artifact, not splitting. The committed file is below1MB and needs no cold-storage dependency.

Separate checker command:

```text
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a5_checker.py topics/padua-proof-attempts-2-20261101/outputs/a5_n3_certificate.json.gz
```

Independent checker implementer `/root/a5_checker` actually executed this on the complete artifact, exiting0 in217.540s. Receipt `../outputs/a5_checker_full-integration.json` has SHA256 `425fd02d3a599b419867f9c985b4aadccf0b049cd32b6b6a235b0306411f77cc`. Checker source hash: `d32810f1b478315cd240f7f68c41177fd97836c8337aefd9de8aa90203884cde`. It imports no producer or old search module and calls no root-isolation routine. It verifies exact algebra, supplied Sturm partitions, all pair dispositions, boundary coverage and values. Its record is `../independent-checks-a5-checker.md`.

A different subagent, `/root/input_manifest`, actually reran the entire producer into `../outputs/a5_independent_n3_certificate.json.gz`, obtaining a byte-identical artifact with the same hash. It then separately ran the checker on both its own certificate and the developer certificate: both exited0 with `verified:true`, counts15/7/6/2 and the additional global predicates. Receipts:

| Actual independent run | Receipt SHA256 | Result |
|---|---|---|
| checker on own producer artifact | `ecc16c09c78cb1305df6e200d693b0673a05cbdb0c5443737da8ea37912fcf2b` | verified;220.972s |
| checker on developer artifact | `e1f5061deaf0867171dffbb11981e122a8c43e996bcbcf3053cbd7aa9badb975` | verified;220.474s |

Their files are `../outputs/a5_independent_n3_checker.json` and `a5_independent_n3_developer_certificate_check.json`; commands, frozen source hashes and all six before/after code pins are in `../independent-execution-a5.md`. These are actual independent executions, not readings of the first output.

Both the checker implementer and the independent executor ran14 malformed-certificate controls. Every omission, false factor/node assertion, unknown disposition and false global bound was rejected. Their identical adverse-control receipt hash is `075ed516a278130134468d2ff3d02775cff930da819f6d758fd85a62ab39454d`. This supplements the positive verification and is not the required Claude audit.

Coverage checked: all1024 interior masks,35376 Cartesian pairs; all3584 canonical edge masks and10508 edge root dispositions; all four corners. Exact crossings are excluded at2 interior pair records and26 edge records. All accepted root boxes/intervals are disjoint and IDs complete. The evidence manifest records source/output identities; temporary developmental intermediates are not proof dependencies.

## Sources

Authoritative programme `OPEN_TARGETS.md` A5, THEORY-06 and frozen t3 sources at9bd14a6d2c4da69139a10107d8a787f2be0c5c9e. The new count is independent of the source's measured reference value.

Primary count comparison: Białas-Cież–De Marchi–Suder, [arXiv2605.23299v1](https://arxiv.org/pdf/2605.23299v1), §3.3, printedp.9, Table3. The directly inspected n=3 row gives7 interior and15 total maxima, agreeing with the certified count. Reading coverage and limits are in `../outputs/a5_n3_literature-comparison.md`; literature/INDEX was read first. No certified n=6,7,8 comparison or published correction is asserted.

## Proof or evidence

The following reduction and every finite predicate have been verified by the separate checker and the actual independent rerun.

1. Construct the exact cardinals from the Vandermonde inverse. Matrix multiplication verifies interpolation and partition of unity. Every signed polynomial has total degree at most3.
2. Enumerate all1024 interior masks. If one gradient component vanishes identically, the signed polynomial cannot have a strict interior maximum. Otherwise verify its exact common-factor divisions, nonzero residual projection resultants and complete supplied Sturm partitions for their squarefree rational norms.
3. For every residual pattern, verify **every Cartesian pair** of projected root intervals. Each disposition excludes the candidate from the open square, excludes a gradient zero, excludes sign consistency, excludes a negative definite Hessian, identifies an exact regular-crease/crossing root uniquely, or certifies exactly one strict maximum with strict cardinal signs. Every injectivity bound applies to the whole box discarded. Accepted root boxes are pairwise disjoint, and root IDs are complete.
4. On all four edges enumerate every canonical mask of the non-identically-zero restricted cardinals. First discard constant restrictions by result05; then cover all real roots of the norm of each nonzero tangent derivative by supplied Sturm partitions. Every root receives an exact exclusion or a strict tangential maximum with the actual one-sided full mask and a strictly negative inward derivative. Zero edge restrictions are treated by exact factor identities. For n=3 only L_6 vanishes identically on an edge: x=1, with quotient(2y²+1)/3>0.
5. On x=1 the two accepted root intervals identify y=±1/sqrt3 exactly: their tangent derivatives are nonzero multiples of1−3y² and the intervals have the required positive/negative signs. Their local strictness and uniqueness are reused from part1theorem03. The new physical boundary certificate corroborates normal descent and incorporates them in complete global coverage; the old disc Hessian proof is not redone.
6. At the four corners, exact cardinal values identify the node corners(1,±1), excluded since λ≥1, and the two non-node corners. At each non-node corner, both inward derivatives are strictly negative for every active pattern, proving strictness. Arbitrary nearby interior and edge points were already covered in steps2–4; no old(D)/(E) neighbourhood discard is used.
7. Result05 puts every strict maximum in one of these covered types. Every exclusion is valid, and every accepted point has a rigorous strictness proof. The verified lists therefore give exactly7 interior,6 open-edge and2 corner maxima, hence15 in total.

All consistent patterns continue to be checked after a root is accepted. Exact crease identification uses a polynomial identity and uniqueness on the entire candidate box, replacing the old1e−10 convention. No exclusion follows from an unconstrained Newton iterate leaving a box.

### Why the supplied interval predicates prove what they claim

For each rational rectangle Q, interval evaluation first encloses sqrt2 by a verified rational bracket, then applies inclusion-preserving rational addition, multiplication and integer powers to every polynomial term. Products take all four endpoint products; even powers across zero include zero. Induction on these operations encloses the polynomial and its derivatives throughout the entire supplied rectangle.

For a signed polynomial P, put f=∇P and J=H_P. Let c be the midpoint of a nondegenerate rectangle Q and C its supplied rational2×2 preconditioner. The checker encloses E=I−CJ(Q) and verifies q=max_i Σ_j sup|E_ij|<1. The map T(z)=z−Cf(z) then has Lipschitz constant at most q on Q, by integration along segments. Its range is contained in the supplied Krawczyk enclosure

K = c−Cf(c) + (I−CJ(Q))(Q−c).

If K lies strictly inside Q, T maps the complete rectangle into itself. Successive iteration is Cauchy with geometric ratio q, proving existence and uniqueness of a fixed point in Q. C is nonsingular: if it were singular, a nonzero left null vector would give eigenvalue1 to I−CJ at every point, contradicting its induced-norm bound q<1. Thus a fixed point is exactly a zero of f, and the strict inclusion places it in the interior. The same contraction inequality, even without a Krawczyk existence test, proves that any two zeros of f in Q coincide. This is the uniqueness argument for an exactly supplied regular-crease point; no Newton iterate outside Q enters it.

The accepted root predicate also verifies H_xx<0 and detH>0 throughout its rectangle, hence H is negative definite there. At the certified stationary point this proves a strict maximum of P. All signed cardinals are strictly positive on that rectangle, so λ=P there and the maximum is a strict maximum of λ. Conversely, at an excluded pair box a nonzero gradient component, incompatible cardinal sign, or failed negative-definiteness condition rules out a strict maximum by result05. An exact regular zero plus uniqueness rules out the sole possible stationary point by the active-polynomial argument. Thus every actual candidate in every projected pair has the claimed disposition.

## Scope

Only n=3. Higher degrees are not certified by this file. This theorem counts strict local maxima; result07 separately treats non-strict global maxima and compares values. For this new procedure, the old(D)/(E) boundary obligations are covered by direct physical edge/corner/node arguments, without asserting correctness of the old floating handlers.

## Open items

The n=3 count is complete. Cases n=4,…,8 remain OPEN until their own certificates are complete; the cubic Hessian exclusion cannot be copied to quartics. Required Claude audit of Part2 remains PENDING. Global argmax is established separately in result07, including the non-strict-maximum issue.

## History

2026-11-01, Codex `/root/a5_develop`, allocated gpt-6.1-sol xhigh. The initial draft was OPEN while final verification ran. After the complete exact artifact, separate checker, actual independent producer/checker runs and adverse controls all succeeded, promoted this n=3 count to PROVED. Supporting reduction05 was separately inspected by `/root/a2_independent_route`; the checker's independent mathematical rationale is in its own record. Required Claude audit remains PENDING. The original programme n=3,…,8 statement is preserved; this file splits its n=3 case.
