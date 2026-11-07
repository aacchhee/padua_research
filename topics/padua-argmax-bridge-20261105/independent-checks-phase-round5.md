# Focused supplementary round-5 response review

Reviewer: distinct Codex subagent `/root/review_phase_round4`, assigned
gpt-6-astra high; serving model/effort are not independently exposed.
Input/rules: `3888dd37c362a0689943f33e6b7e44c1dd1c3050`. AGENTS, WORKFLOW
and CODEX were previously read at bda45a4; their diff to this input is
empty. This supplements, and does not replace, the required Claude audit.

**Disposition: focused source/arithmetic response ACCEPTED; R4-1 CLOSED
at the frozen v2 hashes below.** No unresolved finding remains within
this focused scope. No complete candidate was replayed by this reviewer,
and no degree certificate is accepted by this record. The developer's
five required original leaf predicates all passed in its frozen receipt.
The one authorized complete original n17 replay remains a separate gate.

## Scope, identities and preserved history

Read the round-5 gate, complete changed-source diff against round4,
builder/checker changes, developer controls and bounded receipt. The
previous mathematical reconstruction and normalization review remain
the baseline: [round4 review](independent-checks-phase-round4.md) and
[original phase review](independent-checks-phase-math.md). This focused
review concerns the response to R4-1, not a new mechanism, novelty claim,
literature transfer or negative theorem. Under the explicit no-novelty
exception, the full IDEAS registry was not reread. No new novelty verdict
is issued. No producer arithmetic is imported or used as an oracle.

| Artifact | SHA-256 |
|---|---|
| hybrid_kernel_v2.cpp | `17fea91d4fa02e4183823e5d70b44705e96da7acfd26b04a0f3ed1cac443d9a2` |
| build_snapshot.py | `19a5a7c2296768853b94672b9b5dc4cf16c9ae87c37abbcde073ffaf89246bfb` |
| check.py | `88dde644a77a286e547679b0547c4d35814a4dda7373575208246882d9a26820` |
| Developer hybrid_v2_controls.py | `e8224a0ccd735d676178a44d1db3959ba4bd647f3ac5a40ca46770b99d4cf09a` |
| Developer bounded receipt | `6eb2371ba9a80d688db329e6930374751afc7c407a7891b1a978dc545a608df1` |
| Independent diagnostic script | `3cc33d5c01b4f40e0942f910de966e827025e4488930b0482c85b0bc4f121892` |
| Independent diagnostic receipt | `617ca089876b4854b44755baeb0a4ce3571b4201379c766b523da8bea19302cd` |

The original finite kernel remains `236116452dc7aae66e39cbf8800fe847cffe931ac0ce8a9682397313de7c43a6`;
failed round4 remains `9a976e77d861c291468d6bfa4d2104c6c42ace953781ce1c5ff1a43073505d7d`.
A zero-diff check against3888dd3 confirms the old failed source, review,
independent script and independent receipt are unchanged. Their failure
is historical evidence and is not relabeled as a passing round5 run.

## Source and mathematical response

The quotient identities and global clipping bounds are unchanged:
|R_k|<=k and |R'_k|<=floor(k²/2). The new source uses `arb_sqr` on the
enclosing sine ball. This encloses the square while accounting for the
same operand appearing twice. The source tests both the original sine
ball and its square for finiteness and zero exclusion before dividing.
Even a square enclosure may touch zero through overestimation; that
case now preserves the finite harmonic bound rather than dividing.

The optional quotient value and derivative are staged together. If
either candidate is nonfinite, neither is installed. For a finite
candidate pair, each intersection receives finite inputs; a disjoint
intersection throws and propagates rejection. Each resulting ball must
be finite before the pair is committed. Thus optional failure preserves
the already valid globally clipped finite-harmonic pair. The baseline
and global-bound intersection uses the stricter helper that rejects
nonfinite inputs/results as well as disjoint inputs. No empty finite
intersection is converted to zero or selected as a successful bound.

The finite-output checks added to phase_ratio and phase_term ensure that
success cannot carry NaN or infinite converted endpoints. The existing
complete-bounds finite guard remains. R4-1's actual reproducer now returns
code0, used_quotient=0, and the exact eight endpoints

    [1, 1, 0, 0, 1, 1, 0, 0].

That is the correct exact value/derivative for R_1 throughout the original
interval. Its closure does not depend on a floating-point comparison to
a transcendental reference. The old finding did not establish a false
accepted certificate, and the response does not change that assessment.

The finite primitive, exceptional coefficient1 at (n,0), phase derivative
factors1/n and1/(n+1), finite-collision formulas and global caps are
unchanged. So are whole-sum sign hulls, exact midpoint/radius arithmetic,
four-copy sums before absolute values, endpoint weights and complete
projected-center profiles. Baseline/hybrid final min-upper/max-lower
selection is retained. No new sign assumption, local patch, threshold,
tree refinement, or representative-center reduction was introduced.

## Kernel selection and provenance

`build_snapshot.build` now accepts only a fixed mapping of baseline,
round4 and round5 to repository filenames. Its bare default is the
original finite kernel. `Kernel` and the CLI use the same baseline
default; an explicit `--kernel round5` selects v2. Candidate fields do
not supply the selector or an arbitrary filesystem path. Each manifest
records the variant, source origin, frozen source, fresh unique build,
preprocessed input, toolchain, headers and actual loaded dependency
closure. The previously reviewed provenance checks remain in place.

The only checker changes are this selection interface. Geometry, exact
rational strictness, tree coverage, immutable input hashing, complete
replay requirements and finite local-premise guards remain unchanged.
The reviewer actually constructed fresh round5 and bare-default baseline
builds, checked their distinct workdirs and expected source hashes, and
exercised rejected builder/CLI selectors. This is independent execution,
not merely reading the developer's build receipt.

## Actual focused independent checks

Executed once, successfully:

    python topics/padua-argmax-bridge-20261105/code/review_phase_round5.py

The [small receipt](evidence/phase-round5-review.json) records the command,
all source identities, script, Python/mpmath versions, cases and hashes
of the separate full build-provenance manifest. The latter stays in the
reviewer's own local-output directory. Process CPU was0.89035272seconds;
child CPU was2.106632seconds, including both fresh builds and the invalid
CLI-selector process. These timings are not a complete-cover measurement.

The bounded checks were selected for the material response:

- 31 ratio boxes and 93 sample points, k=1/2/3/17/18. They include the exact
  original R4-1 box, positive/negative wide neighborhoods translated by
  integer*pi, exact collision, a crossing, a tiny positive interval,
  an away-from-zero point and a broad interval containing several zeros.
  Every successful output was finite; all prescribed crossings used
  fallback. Values and derivatives agreed with an independently summed
  complex-exponential polynomial at120digits, tolerance1e-100.
- 12 primitive jets at n=2,17,32, including exact and nearby collisions
  at(0,0) and(pi,pi), and translated mesh phases. Value and both phase
  derivatives agreed with the independent triangular polynomial with
  the exceptional coefficient explicitly corrected.
- Two directly injected nonfinite candidate cases preserved the exact
  finite pair; two finite-disjoint controls rejected. These include both
  the optional refinement route and the strict intersection helper.
- The actual bare default built the original finite kernel. Three invalid
  builder selectors and one invalid CLI selector rejected. A tiny box
  with asymmetric adjacent binary64 endpoints returned finite bounds;
  combined upper/lower bounds were no weaker than that fresh baseline.

The numerical polynomial comparisons are MEASURED diagnostics, not a
proof of interval containment by sampling. Correctness of the interval
operations depends on the stated Arb/FLINT, compiler and runtime trust
assumptions. The source derivation supplies the mathematical argument.
Unchanged complete partition-corruption and full-tree tests were not
indiscriminately repeated. No independent leaf or whole-tree replay is
claimed here.

## Remaining complete-certificate gate

The developer's frozen receipt reports all five prescribed original leaf
predicates passing. This is attributed execution whose arithmetic source
has now passed focused independent review. Its maximum S upper among the
four nonlocal samples is8.616364533784965; each recorded comparison uses
its own appropriate corner/defect predicate and Lc lower8.6179478249936.
Sample success alone supplies no complete-cover conclusion.

The permissible next test is one replay of the unchanged original compact
n17 candidate, plain hash
`64f7befd86658c8d9f29b05c1cb5a0162e611b726b161e737610547bed218c4b`,
using explicit round5 selection. It must check all1288original leaves,
with zero failed predicates and zero pending regions, accepted=true,
within the declared120checker-CPU-second gate, reporting compiler child
CPU separately. Stop and preserve a failure/cap; no silent subdivision
or second formula is included. This report neither executes that test
nor predicts its result. No new degree or all-degree PD-T099 claim follows.
