# Independent degree-five A5 certificate verifier

Rules read at `44be0080c69495cc6959e3d4c2b602fa73678d76`.
Role: independent verifier implementer, assigned Codex gpt-6.1-sol xhigh; a
separate serving-model receipt is not exposed. This is supplementary checker
work, not the required Claude audit. No degree-five count is asserted here
without a completed full-certificate receipt and the separate executor record.

## Gate and source coverage

The full task/rule reading from the earlier degree-three assignment was retained;
the three current rule files were reread. Repeated the complete registry
heading/identifier/alias/summary scan, reread every current obstruction and
disposition table, and verified the complete registry blob is unchanged from the
previous full read: `3bc9f45599e3bd3b29ef08dd8673793732b79055` at both `3db1eee`
and the current rules head. Searched `node.cone`, `node cone`, `radial`,
`node.gap`, `breakpoint`, `directional.deriv`, `physical node`, `Bernstein`,
`crease`, `degenerate` and certification synonyms across state, topics, tracks
and literature. Read full programme IDEA17 / source06, contextual IDEA048,
the old floating N-node-cone definition and implementation, part1 audit F2,
current n4 schema and proof09, and the complete new proof15 / n5 schema. The
literature index supplied no additional local node-cone proof dependency.

Closest entries are the same registered maxima problem (IDEA048 / programme
IDEA17 / source06), old N-node-cone floating predicate, and the retained n4
compatible-sign spatial certificate. Verdict: proof completion / exact variant,
with no novelty or priority claim. The new distinction must be complete exact
feasible-direction breakpoint coverage plus a whole-cube radial remainder bound.
Missing breakpoints, zero/unverified gap, an inactive face met by the cube, or a
leaf not strictly inside its cube kills that discard. Cheapest decisive test:
independently reconstruct and check all 21 node-gap records before trusting any
node leaf. Degree-three singular-Hessian exclusions are not imported to degree
five. The old boundary/corner handlers supply no proof authority.

## Implementation provenance and scope

Only new `code/a5_checker_n5*`, `outputs/a5_checker_n5*` and this record are owned
by this implementer. Existing n3/n4 files remain frozen. The general spatial,
root, Sturm and edge replay core is adapted from the independently written,
frozen n4 checker, SHA-256
`1fe4f74ffe21447134e1c2f34e6364f3ca73929f207c7ebd8f3ea8977e53d143`.
The new module imports no producer or old numerical evaluator and performs no
subdivision, Newton iteration, geometric root isolation or search.

The checker independently reconstructs the degree-five monomial Vandermonde for
explicit exact cos(j*pi/5), cos(k*pi/6) coordinates, verifies its inverse,
cardinal values and partition of unity, and derives every polynomial/gradient/
Hessian over Q(sqrt(3),sqrt(5)). Interval arithmetic uses integers on the fixed
2^-96 lattice, with exact outward division, independently checked square-root
brackets for 3, 5, 15, direct powers, and natural/centered enclosure intersection.
The compatible-mask coefficient arrays now have 21 monomials and 84 rational
field components. There is no ambiguity cap or early return over ordinary masks.

The whole binary prefix partition, every ordinary compatible mask, every exact
factor/regular point, Krawczyk existence and whole-hull injectivity, disjoint
interior roots, all four edge arrangements and all four corners must pass for a
count. Hessian exclusions require strict positive curvature or strictly negative
determinant; singularity alone gives no degree-five exclusion.

The producer's boundary diagnostic reports every restricted cardinal nonzero and
the multiplicity-one crease cover on all four edges. These are checked again
independently before using the n4 boundary serialization: squarefree product,
complete four-conjugate rational norm-root partitions, exact gap samples and all
sample masks, reduced derivative-root partitions, every candidate disposition,
strict tangent maximum and strict inward descent/ascent, and all-active corner
derivatives. Failure of these hypotheses blocks acceptance; no identically-zero
edge cardinal is silently omitted. Zero-normal and degenerate tangent roots
require a separate explicit predicate or remain unresolved.

## New node-cone verifier predicates

Every certificate must supply all 21 node records in exact board order, including
unused `zero_gap` / `no_cube` records. Every node coordinate, every feasible
unit-square side segment and every breakpoint is checked independently.

For each node and each coordinate fixed at +/-1, feasibility is derived from the
exact square faces containing the node. The other coordinate ranges over
[-1,1], [0,1] or [-1,0] as required. The supplied segments must equal this entire
ordered list. Every segment's endpoints and bounds are checked. All supplied
breakpoints are exactly ordered, distinct and in range; every zero of a
nontrivial other-cardinal directional linear form in the segment is derived from
the exact reconstructed gradient and required in the list. Extra verified
breakpoints are harmless. At every supplied breakpoint the exact field value
of grad(Lq).d + sum(other)|grad(Li).d| must be at least the supplied rational m.
Piecewise affinity then gives the claimed bound on the entire feasible direction
set, rather than a sample set. Supplied zero-gap witnesses are verified exactly.

Only `accepted` records receive discard authority. Each requires m>0, no zero
witness, exact node strictly inside rational rectangle B, and B meeting no square
face not containing the node. The radius must bound the full infinity-distance
from node to B, not only a center/leaf. The checker independently verifies Lq>0
on all B, all 21 nonnegative quadratic-form bounds
Hi >= sup_B(|Hxx_i|+2|Hxy_i|+|Hyy_i|), H >= sum Hi, and R*H<m. A node leaf
must have no ordinary pattern list and its entire rational Q must lie strictly
inside the accepted B. A `zero_gap`, `no_cube` or missing record cannot be
referenced. Node leaves contribute to leaf-count statistics but never to the
ordinary mask-check count or maximum count.

These are exactly the finite hypotheses of proof15's radial integral argument,
including its treatment of zero cardinal values along a ray. Independent
mathematical review of proof15 is separately owned by the orchestrator/reviewer;
this verifier role does not self-approve that theorem or substitute for Claude.

## Actual checks and Runs needed

Actual initial smoke command used `PYTHONDONTWRITEBYTECODE=1`, `python -B`,
`PYTHONPATH=/tmp/padua2-deps`, importing only the new checker and constructing
its Verifier. All 21 exact cardinals / node interpolation identities / partition
of unity passed in 18.467 seconds. No producer module was imported.

The first symbolic node-only attempt was deliberately stopped with exit143
before completion and is not a pass. Native exact arithmetic replaced repeated
radical expression reparsing: alpha=sqrt(3)+sqrt(5), alpha^2=8+2sqrt(15),
alpha^3=18sqrt(3)+14sqrt(5). The checker verifies its primitive generator and
maps native coefficients (a3,a2,a1,a0) to
(a0+8a2,a1+18a3,a1+14a3,2a2). Exact basis-vector and cubic-generator checks
passed. Node gradients are evaluated directly in native exact polynomial
representations; their basis data and outward interval arithmetic remain
independent of the producer.

Environment for the following actual runs: Python3.12.14, SymPy1.14.0,
python-flint0.9.0 / FLINT3.6.0, SymPy ground types `flint`, via
`PYTHONPATH=/tmp/padua2-deps`. All commands also set
`PYTHONDONTWRITEBYTECODE=1` and invoke `python -B`.

1. `code/a5_checker_n5.py /tmp/a5-n5-node-cones.json --nodes-only --output
   outputs/a5_checker_n5_nodes-integration.json` completed with exit0 in9.920s.
   Input SHA-256 `d70d297aaf727d0d6b13ba690fb0768a7f5465aeb2d23b04a2fd0b7d5bb55eb8`,
   62,895bytes. All21 node records, all21 accepted cubes and all738 supplied
   direction breakpoints (including every independently derived required zero)
   passed. Its initial receipt is preserved as `outputs/a5_checker_n5_nodes-initial.json`, hash
   `0153f86c6d64e856edaad68f95fb2cc72f31b88baf9799bc24220cee5cacd8aa`,
   737bytes; explicitly `count_certified:false` and local-only scope.
2. `code/a5_checker_n5_controls.py /tmp/a5-n5-node-cones.json --output
   outputs/a5_checker_n5_controls.json` completed in11.498s with all controls
   passed:16 negative controls and three positive controls. Rejections cover an
   omitted node/side/internal directional-zero breakpoint, false m, inactive
   face, underestimated whole-box radius, false Lq lower bound, underestimated
   individual Hessian bound, failed radial remainder, whole-leaf and non-strict
   containment, missing/zero-gap cone authority, hidden ordinary patterns,
   overlapping paths, singular-Hessian-only exclusion and omitted Sturm root.
   Positive controls verify all21 cubes, complete versus missing prefix subtree,
   and84-component integer mask vectors against independent symbolic sums for
   ten masks. Receipt hash
   `b16d62cd55b2788b08169e0cc1db7e5a08c4c33d65898eb196b052b95a8d2db3`,
   3499bytes.
3. `code/a5_checker_n5.py /tmp/a5-n5-spatial-pilot.json.gz --allow-partial
   --output outputs/a5_checker_n5_pilot-integration.json` completed with exit0
   in39.817s. Input hash
   `44831f98746d2a7e0871550c62c7a3efe18d228ed5b2295214243903954d1998`,
   41,165bytes. All supplied4920 leaves,91,421 ordinary compatible-mask
   dispositions,88 whole-node leaves and11 disjoint root enclosures passed.
   Its initial receipt is preserved as `outputs/a5_checker_n5_pilot-initial.json`,
   hash `97253d1e2e67103d6fb7b10cbd479cffdd8b3006d36cd665092603c637e1a526`,
   2764bytes. The partition/boundary were incomplete and the checker correctly reported
   `count_certified:false`, `total_maxima:null`. This is witness integration,
   not a degree-five count.

Initial provisional frozen checker hash, communicated to root and producer after those runs:
`25be744f0095ce38aee6468dce5875bc3286edafd6e1a9861bfe82a232b44a02`.
Frozen controls hash:
`b94acddef8167bc72822ccef599f9f5d334f1fa90b0e3de461ab87cffdaa6160`.
The subsequently supplied optional global schema required a documented addition
and a new freeze, described below; no existing n3/n4 file was edited.

## Optional global extension and current freeze

The n5 lead supplied `a5-n5-global-v1` after the initial freeze. Root was informed
before the authorized addition. The count/node predicates were preserved; global
bookkeeping records every ordinary `flat` and `factor` occurrence. The separate
global artifact must be bound to the compressed count artifact by SHA-256 and
verify all occurrence counts/value bounds below19/4, all interior/edge root IDs
and enclosures below19/4, every constant edge restriction exactly±1, exact node
value1, and the exact common value above19/4 at(-1,±1).

This explicitly treats non-strict global maxima: gradient/strict-curvature
predicates exclude them, regular-point injectivity identifies a node of value1
or a regular crease, and root injectivity identifies a strict root. Flat/factor
curves might support non-strict maxima, so every such occurrence is separately
bounded below the cut. Accepted node cones give radial ascent at every nonnode
point; nodes have value1. Complete edge coverage plus constant-edge value1
handles the boundary. Thus the comparison does not assume that the strict list
automatically includes all global maxima. No global claim is made before the
actual full count and global evidence pass.

Current refrozen checker SHA-256:
`6390d465a0e4c83f5cb75673834da4bfbda98c507266c9a81c60c85baceb7bab`.
Current refrozen controls SHA-256:
`0508b79bd96f3a3b12c6f907992c5e179910f869d2fdabe3e669e8286164ef91`.
The same actual commands were rerun at these hashes after the global addition:

| Run | Actual outcome | Receipt SHA-256 / size |
| --- | --- | --- |
| node-only | all21 cubes /738 complete breakpoints pass,13.400s; no count | `10b41f509bd8e4e794d05ee8288129ab9962e9a075e71a4ce041de1ce67c7720`,738bytes |
| partial pilot | all4920 leaves /91421 ordinary masks /88 node leaves pass,44.288s; count false | `41c8ef5125382e5c4abe6e97883c67a221c55a90b015f6f131c8e144f4d38446`,2764bytes |
| expanded controls with `--spatial-certificate /tmp/a5-n5-spatial-pilot.json.gz` |18 negative /three positive controls pass,15.473s, including omitted ordinary mask and singular root preconditioner | `858a0005f368f696655e95c5152a5ed5a1e4e17d9b664add34eaf44edf400a28`,3829bytes |

The first two current receipts use the `*-integration.json` names; expanded
controls use `outputs/a5_checker_n5_controls-spatial.json`. Initial observed
receipts were preserved byte-for-byte, with their original recorded SHA-256
verified, after canonical integration names were refreshed for the new hash.
The new optional global controls also test count-artifact binding, disposition
coverage, exception counts/bounds, node value, omitted/counterfeit root value
rows and an altered exact corner value when a complete artifact is available.

An additional actual control at the initial count/node hash replaced only
node0's lower bound by0 and status by `zero_gap`. All21 gap records still passed,
but only20 cones received authority; a leaf referencing cone0 was rejected.
Initial receipt preserved as `outputs/a5_checker_n5_zero-gap-initial.json`, SHA-256
`fbd173a36f4bb136f73a473947d416ddb2705611134659d1021d67f33ca02e66`,
601bytes. The same actual mutation and replay were repeated with the current
refrozen checker; `outputs/a5_checker_n5_zero-gap-control.json` has SHA-256
`805b0f8d8a1b301d0b4650855dbea6395c851242aa4f869da2d21770c28eb250`,
601bytes, and again verified21 gap records but granted only20 cones and rejected
the cone0 reference. This exercises the zero-lower-bound branch itself rather
than merely removing a lookup entry.

No further code change is planned except an essential documented bug correction
with affected runs restarted.

## Completed full count and global integration

The frozen checker and controls were actually run on the helper-generated
complete artifacts, rather than waiting for the slower developer boundary run.
Input count artifact: `outputs/a5_independent_n5_certificate.json.gz`,125252bytes,
SHA-256 `d22c9b1e32728e511ca4ac20506df614b501669a37bc287ed1cde802b6c7f4b3`.
Global artifact: `outputs/a5_independent_n5_global.json`, SHA-256
`47d50f724471904d4873c471e48a2dec9992eb537f5597afe13d07fe17152ccb`.

Actual commands from repository root, with the environment described above:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n5.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_checker_n5_full-integration.json
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n5_controls.py topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_certificate.json.gz --spatial-certificate topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_certificate.json.gz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_independent_n5_global.json --output topics/padua-proof-attempts-2-20261101/outputs/a5_checker_n5_controls-full.json
```

The full positive command completed with exit0 in **298.948s**, accepting all
required evidence. Its8352-byte receipt has SHA-256
`d9bf5b17a7c308c377be42e0df9c57d7539ce1b8a60850486bb77b6d66be943f`.

| Verified scope | Actual outcome |
| --- | --- |
| Complete binary square cover |10182 leaves, including150 whole-node leaves |
| Ordinary compatible masks |225656 dispositions:225462 gradient,48 strict-curvature,4 flat,142 root references |
| Node certificates |all21 accepted cubes and738 complete direction breakpoints |
| Interior maxima |14 distinct disjoint Krawczyk root boxes |
| Four open edges |139 complete sign masks,1815 root dispositions:1070 derivative,216 minimum,330 outside,190 sign,9 root |
| Corners |two exact node exclusions and two strict maxima;8 active sign patterns checked |
| Closed square total |**25 strict local maxima:14 interior,9 edge,2 corner** |

The additional global evidence passed: every one of the four flat/factor
occurrences was bounded below19/4; all accepted interior/edge values were below
19/4; exact node/constant-edge values were handled; exact nonnode-corner value

**38/15 + 8*sqrt(3)/15 + 2*sqrt(5)/3**

has a verified lower bound above19/4 and is attained precisely at **(-1,-1) and
(-1,1)**. Non-strict plateaus are excluded by the additional argument above,
not inferred from strict counts alone. The exact root/value and exception bounds
are retained in the positive receipt.

The full controls command independently replayed the complete count and global
certificate again and completed with exit0 in **292.773s**. All **27 negative
and four positive controls** passed, including the global input binding,
exception-code/count/value bounds, exact node value, omitted root value rows,
counterfeit root value enclosure and altered exact corner value. Its5358-byte
receipt has SHA-256
`729f5ea523c7e38caf01e894c00db03ca294432ec9b8bd850ee33952ffbfab7f`.

No code changed during these full runs. The actual different-agent producer /
checker runs and cross-check of the developer artifact are separately owned and
recorded by root's helper; this implementer's integration does not substitute
for that record or the required Claude audit. Developer artifacts subsequently
arrived with their own input hashes; the actual full integration above remains
pinned to the stated helper pair. New n7 verifier work was assigned only after
this n5 component closed; all n5 code remains frozen.
