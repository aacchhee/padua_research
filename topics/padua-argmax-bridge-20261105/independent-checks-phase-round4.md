# Supplementary round-4 phase arithmetic review

Reviewer: distinct Codex subagent `/root/review_phase_round4`, assigned
gpt-6-astra high; serving model/effort are not independently exposed.
Rules/input read at `bda45a4c1392bea87de0841b6b23e5c35b2a694b`.
This supplements, and does not replace, the required Claude audit.

**Disposition: NOT ACCEPTED; finding R4-1 remains open.** The separately
required five-leaf gate also failed three leaves. The source, independent
diagnostic script and evidence are frozen below. No whole replay was run.
No false certificate acceptance is established: the production checker
retains its final finite-output guard. No phase degree is certified here.

## Scope and baseline

Read AGENTS, WORKFLOW, CODEX, handoff03, the complete round-4 gate,
the prior supplementary phase-math review, PD-T364's finite reduction,
the phase-checker reduction, and baseline arithmetic/checker/build source.
Baseline kernel SHA-256:
`236116452dc7aae66e39cbf8800fe847cffe931ac0ce8a9682397313de7c43a6`.
The N3-specific novelty gate was also read. This is a focused arithmetic
verification of the already recorded implementation/enclosure variant;
it proposes no new mechanism, novelty verdict, literature comparison or
negative theorem. Under the workflow's explicit no-novelty exception,
the full IDEAS registry is not reread. Review does not independently
endorse the historical novelty search.

No producer arithmetic is used as an implementation or numerical oracle
for this review. The shared finite identities are mathematical inputs.
The review owns only this report and, if needed, its small independent
diagnostic script and receipt. It changes no production source or Git state.

## Reconstructed mathematics

For integer k>=1, the sum of exp(i(k-1-2l)z), 0<=l<k, equals R_k(z)
where sin(z) is nonzero and extends it everywhere. Pairing frequencies
gives [k odd]+2 sum cos(jz) with 1<=j<k and j congruent to k-1 modulo2.
Differentiation gives -2 sum j sin(jz), valid also at all collisions.
Consequently |R_k|<=k. If k=2h, the positive frequencies sum to h²;
if k=2h+1, they sum to h(h+1). Thus |R'_k|<=floor(k²/2), including
R'_1=0. These are routine bounds of the inherited identity.

On any entire argument interval whose enclosing Arb sin ball excludes
zero, the quotient and its derivative are valid:

    R_k = sin(kz)/sin(z),
    R'_k = [k cos(kz) sin(z)-sin(kz) cos(z)]/sin(z)^2.

The denominator guard must concern the full enclosing ball. A rigorous
but overestimated product ball for the denominator square can contain
zero even when the original sine ball excludes zero; this case requires
an uninformative quotient enclosure or a checked fallback. If zero cannot be
excluded, the finite harmonic formula remains valid without selecting
a rounded collision index. Any outward enclosure of the intersection
of two valid ranges remains valid, even if its rounded endpoints extend
slightly beyond an input ball. An empty intersection is contradictory
and must reject, rather than silently choosing a bound.

For s=(u+v)/2 and t=(u-v)/2, write D_s,D_t for the differentiated two
ratio products. The corrected primitive G has derivatives

    G_u = (D_s+D_t)/2+n sin(nu),
    G_v = (D_s-D_t)/2.

The phase derivatives divide these respectively by n and n+1. They are
angle/phase derivatives; no derivative with respect to x=cos(u) is being
substituted. The subtraction -cos(nu) leaves coefficient1 at the
exceptional mode (n,0), and its derivative sign is positive above.

The inherited nonsmooth whole-sum argument uses absolute continuity
along segments and symmetric gradient hulls when a value ball touches
zero. It neither differentiates a sign function nor assumes signs are
constant across a collision. Exact endpoint midpoint and half-width
balls enclose the required center and radii. Four orbit copies must still
be summed before signs/absolute values. Complete projected profiles,
endpoint multiplicities and strict rational predicates remain necessary.

Taking the minimum of separately valid final S/corner upper bounds and
the maximum of separately valid defect lower bounds is valid. Keeping
the actual baseline scalar outputs also ensures these final bounds are
no weaker than baseline without presuming monotonicity of rounded ball
operations. No leaf kind, witness threshold or geometry may change.

## Frozen source inspection

| Artifact | SHA-256 |
|---|---|
| hybrid_kernel.cpp | `9a976e77d861c291468d6bfa4d2104c6c42ace953781ce1c5ff1a43073505d7d` |
| build_snapshot.py | `406368f07354f7d0d861eb92aa0bd2fc720ca9fccc86f8ed650d7da0872e8c18` |
| Unchanged check.py | `8713026a1b5a872f0e8dd33c311eafef2cf310f42ae2eebb4055ad224b8acfae` |
| Developer hybrid_controls.py | `e388f935f70dadfc342f4b9f9523e577fb018a65fef485cdf815ca3d05e71164` |
| Developer bounded receipt | `8bb4097c650d2429488a037cddd0c01df2df15bdd67538026b64e124769a441e` |

Read the complete changed kernel, builder diff and bounded receipt. A
`git diff --exit-code bda45a4 -- .../check.py .../arb_kernel.cpp` check
confirmed both previous files unchanged. The builder now selects the
fixed hybrid source and records its origin while retaining the fresh
snapshot and build/runtime provenance machinery. No candidate-provided
arithmetic library selector was introduced. Geometry, complete profiles,
strict rational predicates, ignored producer numeric fields and local
premise guards remain unchanged.

The hybrid computes deep-copied baseline jets before refining ratios,
preserves the exceptional coefficient and phase derivative factors,
and evaluates baseline and hybrid complete profiles separately. Final
upper/lower selection uses the correct min/max directions, including
the corner and pi intervals. The source contains no producer import or
copied producer arithmetic path. These findings do not close R4-1.

## R4-1 — MAJOR: successful ratio diagnostic with NaN derivative bounds

The independently rebuilt frozen kernel returns code0 for

    phase_ratio(1, -2, 0.125, 0.375, out, &used_quotient)

with used_quotient=1 and output

    [1, 1, 0, 0, 1, 1, NaN, NaN].

The first four entries are baseline value/derivative endpoints and the
last four are hybrid endpoints. The exact function is R_1(z)=1 and its
derivative is identically0 throughout this interval. Thus this successful
diagnostic does not return usable derivative bounds even though the
finite fallback was exact. No high-precision numerical premise is needed
for this counterexample to finite-output robustness.

Locations: hybrid_kernel.cpp:43–52 refines by dividing through `sz*sz`
and intersecting without a finiteness guard; its intersection helper at
line20 checks only the Arb intersection return flag; phase_ratio:170
returns success without checking its converted outputs. The suspected
path is an overestimated square followed by an indeterminate quotient
and intersection. That internal causal sequence was **not separately
instrumented** and is not represented as an executed observation.

This blocks a clean arithmetic-review acceptance. It does **not** show
a false accepted degree certificate: collect_bounds:126 checks all seven
final outputs for finiteness, and phase_bounds propagates its rejection.
The original five-leaf gate independently stopped the whole replay.
Return the finding to development; no reviewer source fix was made.
Any response must handle a denominator-square ball that still contains
zero, reject or safely fall back on nonfinite refinements/intersections,
and ensure successful diagnostic outputs are finite. A material response
needs new frozen bounded controls and focused review before any whole run.

## Actual independent execution and limits

Command:

    python topics/padua-argmax-bridge-20261105/code/review_phase_round4.py --source-sha 9a976e77d861c291468d6bfa4d2104c6c42ace953781ce1c5ff1a43073505d7d

The script compiles copied frozen source into its own local directory;
it does not load the developer's checker binary or producer arithmetic.
The independent oracle is a120-digit complex-exponential finite sum.
The run stopped at its first failed sample, after4completed ratio boxes
and20point checks. All4completed boxes have k=1, turn=-2; they include
the exact collision, two crossing neighborhoods and a tiny positive
offset interval. The failing fifth box is the one displayed above.
The planned k=2/3/17/18 cases, triangular primitive tests, disjoint-control
call and subsequent checks were **not reached**. They are not reported
as executed or passed.

Three actual invocations occurred: the initial assertion found the
failure; a second added the concrete case to the assertion; the third
preserved the same failure in the final small receipt. No arithmetic
source changed between them. The final run exited1, measured0.878496
compiler-child CPU seconds and0.008194387 diagnostic-process CPU seconds.
Its script SHA is
`9fccf44268ac910978f7dccb0cde3068c24a3c2a3c6bfa0f82bad569496a1c3a`;
the receipt pins source/binary identities, build command and runtime
versions. The receipt's added `accepted=false` field records the review
disposition. No full runtime-closure revalidation or whole-cover run is
claimed by this diagnostic. See [receipt](evidence/phase-round4-review.json).

## Attributed leaf gate and final scope

The developer's frozen bounded receipt independently records2/5passing
required original leaves. This is reviewed evidence, **not** this
reviewer's leaf rerun:

| Root/path | Outcome and failed comparison |
|---|---|
| 0/01010 | PASS; S upper7.63022063807659 < Lc lower8.6179478249936 |
| 0/1100111 | FAIL; corner upper8.742498890697016 > Lc lower8.6179478249936; defect lower0 |
| 0/11011111 | FAIL; S upper8.843523044070748 minus defect lower0 > Lc lower8.6179478249936 |
| 3/0011000 | FAIL; corner upper8.742498890669053 > Lc lower8.6179478249936; defect lower0 |
| 0/1111111111101111 | PASS; both original strict predicates |

The original plain candidate hash remains
`64f7befd86658c8d9f29b05c1cb5a0162e611b726b161e737610547bed218c4b`.
The fixed repair failed its predeclared bounded gate and its additional
independent robustness check. The failure concerns this frozen variant,
not every possible Arb enclosure or the mathematical target PD-T099.
No whole original n17 replay is warranted under this gate. Neither all
1288 leaves nor the120CPU-second whole-run gate was evaluated here.
No source fix, tree refinement, archival cleanup or Git mutation was made.
