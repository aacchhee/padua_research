# Independent supplementary checks — part 3

Auditor: Codex subagent, actual model `gpt-6-astra`, high effort, 2026-11-01.
Role: independent supplementary mathematical/code checker of Codex development;
this does not replace the required Claude audit.

Rules/source input: `328be35e55143013047ec03a70e9906e82b95353`.
Read `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`, and open
handoff `02-part3-work.md`. Workspace is the orchestrator's selected-file
snapshot, not a Git clone; input paths/blob identities are recorded in
`input-snapshot.json`. Newly developed files are identified below by SHA256.
No Git operations, developer source edits, registry writes, or handoff edits
were performed by this subagent.

## Exact n=2 certificate

**Finding: no unresolved mathematical or checker finding in this scope.**
The written proof establishes the maximum 3 and exactly the two non-node
corners (-1,-1),(1,-1) for the stated even-checkerboard nodes. This is a
finite-instance verification of the existing P0 target, with no new
mechanism, novelty, priority, literature, or negative claim; full IDEAS
review is not needed for this narrow initial scope.

Inspected files and hashes at this check:

| File relative to topic | SHA256 |
|---|---|
| `code/part3/finite_n2_exact.py` | `a5f00e6039d6ec76660cac90fb5720e0d6721348ed34c9e62775e1125d3e87c2` |
| `theory/argmax-alln-codex-02-degree-two-global-argmax.md` | `9e0ad83d6ffd5705a2f5b873d985916f2dc24eb081f9954cb0ea335e3d2fd9b3` |
| `outputs/part3/finite_n2_independent.json` | `8c3e9948db4b09d9eec5a2aaf3f8e5c0f8ec3e710e6ab63c72598613aa3e49c9` |

Actually executed independently, from repository snapshot root:

```sh
python -B topics/padua-argmax-alln-20261101/code/part3/finite_n2_exact.py --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n2_independent.json > topics/padua-argmax-alln-20261101/outputs/part3/independent_n2_stdout.json
sha256sum topics/padua-argmax-alln-20261101/code/part3/finite_n2_exact.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n2_independent.json topics/padua-argmax-alln-20261101/outputs/part3/finite_n2_exact.json topics/padua-argmax-alln-20261101/theory/argmax-alln-codex-02-degree-two-global-argmax.md
python --version
```

Environment: Python 3.12.14; standard-library `fractions.Fraction`, no seed.
Run exited 0, `accepted=true`; independent JSON is byte-identical to the
producer JSON. All mathematical predicates are rational. This was an actual
new execution, not merely reading the producer output.

Independently checked the reduction: the listed nodes are exactly j+k even
on the degree-two cosine grid; the displayed six polynomials have total
degree at most two and satisfy the nodal cardinal equations. Nonsingular
Vandermonde inversion establishes uniqueness. The tensor Bernstein basis
is nonnegative and sums to one on each of four covering closed quadrants.
The coefficient conversion formula follows from the three identities for
1,u,u² and their products, so the triangle-inequality majorant is valid.
All four coefficient-sum matrices agree with the rerun. Upper quadrants
have all entries <3; each lower quadrant has exactly one entry equal to 3,
at a tensor vertex. A convex combination can equal 3 only when that
vertex's weight is 1. The elementary formulas B0=(1-u)² and B2=u² force
the stated corner coordinates, including boundaries. Direct evaluation
there gives sum of absolute cardinals 3. No equality case was lost by
using only a sufficient majorant: attainment is verified separately.

Trusted computation dependencies: the Python interpreter and standard
library Fraction implementation. The proof also displays the small
rational tables explicitly, so its mathematical content is checkable
without treating floating-point sampling as a proof. Assertions must stay
enabled when executing the checker; the recorded command does so.

Residual scope: n=2 only. This check supplies no evidence of an n=8 or
all-degree certificate. Claude audit remains pending.

## Broader review gate and numerical scope

Before extending this check beyond n=2, read the complete 850-line
`state/IDEAS.md`, including every obstruction/disposition table, in bounded
chunks (re-reading the portions truncated by initial tool output).
Also read topic `plan.md`, `ideas.md`, `gate.md`; the full part-2
`preparation/ideas-registration.md`; and merged edge theory records
70,71,72,74,75,76,77. Searched the registry and candidate files for
`triangle defect|phase locali|primitive|central envelope|R_cen|argmax|majorant|monoton|profile`.
Closest mechanisms are IDEA-303–305 and the current topic's profile
extension, with IDEA-290–302 for finite certificates. This is verification
of those scoped extensions, not a priority claim or an exhaustive literature
novelty determination. No new mechanism is proposed by this auditor.

Read all of `tests_common.py`, `tests_T1.py`, `tests_T2_T3.py`, and
`tests_T4.py`. The product-U formula, divided-difference fallback and the
exceptional x-mode agree with the merged all-edge convention. In particular
horizontal evaluation retains that x correction rather than incorrectly
swapping the two coordinate meshes. Cell optimization is a sampled local
search; it cannot certify an upper bound or a complete list of extrema.
The T3 offsets are angular, as explicitly disclosed in the script.

The literal T1 all-cell positive-gap criterion includes a non-node corner
and therefore has zero gap there; the literal result and a noncorner-cell
interpretation must remain distinct. The numerical general-beta integral
is a replacement diagnostic, not the still-unwritten requested general-beta
series. In T4 the optimistic central-only fitted remainder is not a bound
for P1–P5 assembly. The literal-existing-bound projection is likewise a
measured projection, not an effective theorem or a proof that every possible
asymptotic strategy must fail.

Executed independent bounded T1/formula checks using
`outputs/part3/independent_sample_checks.py`, which is separate audit code:

```sh
OPENBLAS_NUM_THREADS=1 python -B topics/padua-argmax-alln-20261101/outputs/part3/independent_sample_checks.py > topics/padua-argmax-alln-20261101/outputs/part3/independent_sample_checks.out
```

It reruns the registered evaluator validation (seed 20261101), all n=12
T1 cells on all four edges, and independent edge-versus-four-copy formula
comparisons at n=3,8,101,400 and angles 0,0.173π,π/2,π on each edge.
Exit 0, largest difference 7.73603403558809e-12. It also independently
executes general-beta integral quadrature at beta/π=0.1,0.25,0.5,0.75,0.9,
obtaining approximately 1.511217769054,0.882775641653,0.548514842400,
0.882775641653,1.511217769054. This is float64 measurement, not certified
quadrature or a global minimizer proof. Source hashes were checked unchanged
before/after this bounded run and are included with package versions in
`outputs/part3/independent_sample_checks.json`. Full T1 is not independently
rerun here.

Full independent T3 and T4 executions also completed with exit 0:

```sh
OPENBLAS_NUM_THREADS=1 python -B topics/padua-argmax-alln-20261101/code/part3/tests_T2_T3.py T3 topics/padua-argmax-alln-20261101/outputs/part3/independent_T3.json > topics/padua-argmax-alln-20261101/outputs/part3/independent_T3.out
OPENBLAS_NUM_THREADS=1 python -B topics/padua-argmax-alln-20261101/code/part3/tests_T4.py topics/padua-argmax-alln-20261101/outputs/part3/independent_T4.json > topics/padua-argmax-alln-20261101/outputs/part3/independent_T4.out
```

Each JSON agrees with the developer's output in every field after removing
only `seconds`. T3 covers all 507 specified points and has maximum
lambda-minus-corner 0. T4 independently reproduces the literal projection
n0≈1.3305929067842247e14 (>60); its two central-only optimistic projections
are 32 with their explicitly limited scopes. None becomes a rigorous
all-degree bound. Independent T3 and T4 JSON SHA256 values:
`4e4c94c497780962c2e9e354e0686a09387acdb3bbd1bc4d15ffa56818634ffa` and
`f187181ee583166789aa2aecd70c29b0a016bab73a6551cba0bae3f0d7a87a64`.

## Complete n=8 certificate — priority supplementary audit

**Finding: independent replay accepted the complete certificate; no
unresolved mathematical/source finding in the inspected implication and
implementation. Required Claude audit remains separate.**

Read the complete new `finite_bernstein.py`, `finite_bernstein_run.py`,
`finite_bernstein_check.py`, the complete unchanged merged
`a5_n8_field.py`, and the full new correctness theory record 03.
The generic implication is sound under its stated assumptions: positive
Bernstein weights give strict bounds off a single designated tensor
vertex, and d≥1 makes vertex weight 1 possible only at that vertex.
The root and binary subdivision form a cover by closed positive-width
boxes. Boundary overlap cannot create or lose an equality point.

Implementation inspection confirms:

- The 45 cardinals are explicitly constructed in total degree ≤8, with
  all 45×45 nodal equalities and partition of unity checked exactly.
  This also establishes that the specified nodes are distinct and that
  the 45 cardinals give the intended interpolation basis.
- The principal embedding is checked through exact Chebyshev-root counts,
  isolated largest roots, field-basis conversion identities and outward
  integer rational interval arithmetic at 160 binary places. The field
  source is pinned to the merged SHA256 below; unresolved signs fail.
- Exact field evaluation and verified signs give equal positive corner
  values at (-1,-1),(1,-1), both nonnodes on the stated even degree-eight
  grid. `threshold_interval[0]` is a rigorous lower bound in the same
  integer scale as every coefficient upper bound.
- Tensor power-to-Bernstein conversion is an exact rational linear map
  of valid coefficient enclosures. Negative weights reverse endpoints.
  De Casteljau subdivision uses lower floor and upper ceiling, including
  negative endpoints. Coefficient absolute sums use the larger endpoint
  modulus and therefore remain upper bounds.
- A corner leaf can omit only the tensor index corresponding to the
  actual physical corner of that box. Every other coefficient sum must
  be strictly below the lower threshold. The omitted exact coefficient
  is the already verified polynomial value at that corner; interval
  overestimation there does not weaken the equality argument.
- The checker reconstructs all geometry and intervals from the root,
  compares each supplied leaf with its recomputed verdict, enforces
  prefix-freeness and traverses both children at each internal node.
  Thus a missing sibling cannot be hidden by stored counters or a
  complete flag. It calls no discovery/search function.

Hashes at inspected/replayed snapshot:

| File relative to topic unless stated | SHA256 |
|---|---|
| `code/part3/finite_bernstein.py` | `a3133c6c22a365380f6c2ab14f6d31f60153d0df902b325cfcfbeeccc1bed74f` |
| `code/part3/finite_bernstein_check.py` | `096e60475252ebeff871efd3b87eab8029fef0971c0f3b94bfd1ad83a71f6fa1` |
| `code/part3/finite_bernstein_run.py` | `d03b0830b4e23261ee82ea5265b3f5123956a083b34418e6124ea9e4bbb352ac` |
| part-2 `code/a5_n8_field.py` | `764a7d7e50718c04f076ab3bbc86270adad1c47bc902d0b8d4eecf32ebbd2ec2` |
| `theory/argmax-alln-codex-03-finite-certificate-correctness.md` | `3b8dc64c27f059f60cf1079cdd4bbdbbd0888de9f6bfe328f4c03e71ad60b79a` |
| `outputs/part3/finite_n8_pilot.json.gz` | `92528fc9575407cfbb6c097a814327ebc8666a15fe736bc387044f6f6ff54f22` |

Actually independently executed from the snapshot root, assertions enabled:

```sh
python -B topics/padua-argmax-alln-20261101/code/part3/finite_bernstein_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n8_pilot.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n8_independent_check.json
```

Exit 0, elapsed 45.72194707599999 seconds, accepted=true,
complete_partition=true, all_supplied_bounds_verified=true.
Counts: 32 strict bound leaves, 2 corner leaves, 33 internal splits.
The stored certificate reports 67 visited boxes and maximum depth 6;
its corner leaves are paths `000000` and `101010`, for (-1,-1) and
(1,-1). No pending box remains. The equality characterization follows
from the written implication and exact corner calculations, not merely
from the producer's `complete` field (its `accepted` field is false).

Trusted dependencies: Python, SymPy exact algebra/real-root counting and
its arithmetic backend, the inspected integer enclosure implementation,
and the elementary written finite reduction. Producer and checker share
arithmetic code, so this is a different-agent execution plus source/proof
inspection, not an independently implemented arithmetic kernel. No
floating-point comparison is used for any mathematical predicate. The
claim is degree eight only; it gives no new interior maximum count, no
termination guarantee at other degrees, and no effective all-n threshold.

### Independent adversarial controls

Actually executed:

```sh
python -B topics/padua-argmax-alln-20261101/outputs/part3/independent_n8_controls.py > topics/padua-argmax-alln-20261101/outputs/part3/independent_n8_controls.out
```

Exit 0, elapsed 49.89682959300001 seconds, Python 3.12.14 / SymPy 1.14.0.
This separate audit harness runs the full exact setup once, caches that
verified immutable setup within the harness, reaccepts the authentic
certificate, and passes five altered in-memory copies to the unchanged
checker. Missing leaf: rejected `uncovered box`; wrong designated corner:
rejected `invalid/relabelled bound`; altered lower threshold, duplicate
leaf, and producer `accepted=true`: all rejected by assertions. All source
and certificate hashes were unchanged before/after. Full receipt:
`outputs/part3/independent_n8_controls.json`. No developer fix was made or
counted as independent acceptance.

### Completion of independent T2 replay

Actually executed:

```sh
OPENBLAS_NUM_THREADS=1 python -B topics/padua-argmax-alln-20261101/code/part3/tests_T2_T3.py T2 topics/padua-argmax-alln-20261101/outputs/part3/independent_T2.json > topics/padua-argmax-alln-20261101/outputs/part3/independent_T2.out
```

Exit 0; 147.645454407 seconds. Every field agrees with developer evidence
except elapsed seconds. All 243 configured cell searches completed;
32 of the 81 macro-position comparisons exceed the registered 0.05
change criterion. The largest is 0.38230450050563114 at a=b=5. This
reproduces the finite diagnostic; it does not refute a broader existence
of an asymptotic limit or a reformulated interior argument.

`outputs/part3/independent_manifest.json` records current source/output
SHA256 identities, byte sizes and Python/NumPy/SciPy/SymPy versions for
these actual independent runs. Source hashes were taken for the scripts
as inspected and independently executed; the n8 control harness additionally
enforces before/after hash equality. The manifest is an evidence index,
not an external cold-storage archival receipt.

### Numerical record review completed

Read final numerical record 01, `attempts/T1-T5.md`, and postprocessing
scripts `tests_analyze.py` and `tests_crosschecks.py`. No unresolved finding
in their finite-scope statements or planning dispositions. In particular
they explicitly distinguish a measured planning kill from proof of
nonconvergence or refutation of the target strict inequality. The independent
n=12 T1 profiles agree exactly, on all four edges and every retained row,
with the developer's `tests_T1_n12.json`. The missing general-beta series
is disclosed and remains an unfulfilled component.

Inspected record hashes (later addition of independent-check pointers would
be metadata changes): numerical record 01
`4768e6bcae1aa77f02588beb00c4b776286a8bfb9f49b6412afba751fdf94358`;
attempt T1–T5
`e8b07032ad854c4cb5ff6ef337ecd010cb62f8c291a4a163b8fe67d434cb3362`.

## General constructor and degrees 9–12

Read the complete new `finite_general.py`, `finite_general_run.py`,
`finite_general_check.py`, the complete PD-T101 dependency proof, and the
new general-constructor proof appendix in correctness record 03.
**No blocking mathematical or implementation finding.** A minor stale
Scope sentence claiming the discovery implementation targets only n=8 was
returned to development for clarification; it does not affect a predicate.

The rational arctangent alternating bounds are valid at 1/5 and 1/239.
Independently reconstructed the tangent calculation: tan(2a)=5/12,
tan(4a)=120/119 for a=atan(1/5), and subtracting atan(1/239) gives tangent
one in the first quadrant; thus the Machin identity selects π/4 without
branch ambiguity. The cosine alternating tail is valid from its x²/2
term on for 0≤x≤2 because subsequent ratios are ≤1/3. Monotonicity of
cosine on [0,2] correctly orders the two π-interval endpoints.
The recurrence and period/reflection indexing enclose each exact node
mode; overwriting known endpoint/midpoint values by ±1,0 is exact.
Integer polynomial coefficients, the endpoint half weights and the
exceptional (n,0) kernel coefficient 1 agree with PD-T101 §1. Two rational
linear coefficient transforms, followed by the previously inspected
subdivision, preserve enclosure validity. Corner absolute-value lower
bounds correctly use zero on intervals crossing zero.

The two target corner values are equal by cardinal uniqueness and an
actual symmetry of the node set: x reflection for even n and y reflection
for odd n. Hence intersecting their intervals encloses the same value.
For even n the nonnodes are (±1,-1); for odd n they are (-1,±1).
No sign test or interval overlap is incorrectly used to infer this equality.
The interval constructor depends on the proved all-degree cardinal
identity, unlike the independent n8 field reconstruction; that dependency
is explicit and was read in full here.

Frozen general source hashes:

| File | SHA256 |
|---|---|
| `code/part3/finite_general.py` | `b20b7f88ddfc0bbc92e68096063ef626664028c2a379c34d16dc9f84e17aa74a` |
| `code/part3/finite_general_check.py` | `f9d33648eb05f9539f32c7d8f9003ed61410c7acfff9095bf7ea665989ac8281` |
| `code/part3/finite_general_run.py` | `fe1647086b2db5c47d75e24d386cc6456782bb6ea36bc25acd39b75bd4752511` |
| PD-T101 dependency file | `ea59aa077a4d021fc69354383f69340f21d17d87d3a28c6ecaaf302cc763612c` |
| correctness record 03 with new appendix | `1c38484c12c18139b69616c3208e230f7f043fe8889d47b312a73815a4a50f89` |

Actually executed, from repository root, with assertions enabled:

```sh
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n9_general.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n9_independent_check.json
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n10_general.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n10_independent_check.json
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n11_general.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n11_independent_check.json
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n12_pilot.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n12_independent_check.json
```

All four exit 0 with accepted=true, complete_partition=true and all supplied
bounds verified. Each has two corner leaves and no pending region:

| n | Strict bound leaves | Splits | Independent seconds | Certificate SHA256 |
|---|---:|---:|---:|---|
| 9 | 40 | 41 | 1.266229188 | `5d3a17d91ab5931b88bb5084213d0c0c3f972f8e7e2f0fa09511efe85269f7a8` |
| 10 | 46 | 47 | 3.484055248 | `80f98ed868c82116bd1534c6b15b3f49d77c53b69e54bfc12d3ed8658c23a52c` |
| 11 | 48 | 49 | 5.165295624 | `4d19c769d4ef8713c71feb4109f80a0b4f93643ca65d9e52d70753220e975073` |
| 12 | 52 | 53 | 6.278169898 | `f44e2897e5b9432720293bf0a9243d6a6bada6a4e33642bc7924a2f65d635a8e` |

Executed additional independent mutation controls:

```sh
python -B topics/padua-argmax-alln-20261101/outputs/part3/independent_general_controls.py > topics/padua-argmax-alln-20261101/outputs/part3/independent_general_controls.out
```

This harness independently reconstructs n=12 once and caches that verified
setup only for repeated mutation checks. The authentic certificate is
accepted; a missing leaf, wrong corner, changed threshold, and changed
cosine seed are rejected by the unchanged checker. Receipt:
`outputs/part3/independent_general_controls.json`; all source and artifact
hashes unchanged before/after. No developer source was edited by the auditor.
These checks certify only the listed finite degrees and do not supply an
unbounded-degree theorem or an automatic n=100 success guarantee.

## Analytic compact edge results 04/05

**No unresolved mathematical finding within the written scopes.** Read
both full records and `attempts/P1-P2-edges.md`, with the merged 70–72 and
74–77 dependencies already read. Hashes of reviewed theory:

- 04 vertical: `84c4b82e79041480fd9756f6d3b66c7119194c061cc0bdae472d16ce8d110bee`.
- 05 horizontal: `21d65ed24a1d1358f33b12187ef7552490ea023ba58a592c8b365c96c4a9e654`.

Independently reconstructed 04's denominator separation and the bound by
twice the smaller half. The separated denominator stays regular at a
collision of the other half. Endpoint rows have exactly identical halves
and zero defect. For compact beta, the two endpoint-tail numerators are
uniformly positive once s is sufficiently small, restricting the positive
defect to an angular band of width ≤2min(b,π-b). Counting mesh sites in
that band gives O_delta(eta+log(n)/n), uniformly in edge sign/parity.
The bounded bulk, finite folded line segments, tube mass estimate and
common derivative bounds justify uniform parity Riemann convergence,
including moving beta and s. The density is π^-2 for the weighted
checkerboard defect, giving 2/π² times h in the displayed limit.
The positive rectangle has dimensions δ/4 by δ/4 and minimum defect
1-cos(δ/2), establishing the stated constant δ²[1-cos(δ/2)]/(16π²).

For the vertical envelope, the lower comparison may approximate a
boundary minimizer by complementary phases from inside the interval.
A maximizing angle has a nearest complementary phase at distance ≤π/m;
this phase remains in a slightly larger fixed compact set. The global
phase estimate forces s→0; the local primitive-gain bound and the uniform
defect limit then give the matching upper estimate. Continuity allows
the nearest phase to lie slightly outside the prescribed interval.
No uniqueness, differentiability, center-minimality or effective rate is
needed, and none is silently inferred.

Independently reconstructed 05's different correction algebra:
Pn(B)=κ(1+B), cos(nv)=-κ cos(s), and
Pn(cos(v))=-κ[cos(s)(1+cos(v))-sin(s)sin(v)]. Adding cos(s) after multiplying
the divided difference by κ produces exactly
[cos²(s/2)(1+B)-(sin(s)/2)sin(v)]/[B-cos(v)]. This is not a coordinate
swap of the vertical quotient. Translating the periodic first mesh and
reflecting the second produces the odd checkerboard with normalization
1/N. At s=0 its half kernel is the negative of the vertical half kernel,
so the primitive has the same zero-phase corner value.

The horizontal outside-band argument is valid: denominators have the
same sign, so positive defect requires opposite numerator signs. Each
numerator magnitude is then bounded by their difference,
|sin(s)cos(theta)sin(a)|≤|s|sin(a). The separated denominator cancels the
sin(a), giving O_delta(|s|). The closed-band count includes every removable
collision and gives the remaining endpoint tail. Bulk convergence and
the positive rectangle then establish the compact defect result. These
arguments do not supply a bound on the horizontal primitive's gain;
the record correctly leaves the P2 envelope OPEN.

These are analytic reconstructions. No finite computation is represented
as verification of an asymptotic limit or of its uniform quantifiers.
The required Claude mathematical audit remains pending.

## Final finite extension and closure of assigned check

At the orchestrator's request, independently replayed degrees 13–16 with
the same frozen general checker and no new mathematical assumptions.
Each command follows the exact pattern below with n=13,14,15,16:

```sh
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n13_general.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n13_independent_check.json
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n14_general.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n14_independent_check.json
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n15_general.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n15_independent_check.json
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n16_general.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/finite_n16_independent_check.json
```

All exit 0, accepted=true, complete_partition=true,
all_supplied_bounds_verified=true, with two corner leaves and no pending box:

| n | Strict bound leaves | Splits | Independent seconds | Certificate SHA256 |
|---|---:|---:|---:|---|
| 13 | 54 | 55 | 15.432521913 | `730a22d7fde68c97b58791a77545bb449cd4249f3e181fd53fc705261b774d41` |
| 14 | 56 | 57 | 22.886571838 | `2b9cbed8288910fca1b0519cf8302ba1ecb1c4048976248a32ba6b2a45db48b9` |
| 15 | 80 | 81 | 28.970977128 | `d528cf2768307a00d4b8751e514df9a6cd069e80a9487d7192dbb632a15c4ca1` |
| 16 | 94 | 95 | 44.681331388 | `8e51d6ae34852b34f828cff637b201277e668cf06389b613d64b7ecb1175f5c7` |

No degree beyond 16 was run by this auditor.

Also read the developer's separate `finite_general_controls.py` and
actually reran it independently:

```sh
python -B topics/padua-argmax-alln-20261101/code/part3/finite_general_controls.py topics/padua-argmax-alln-20261101/outputs/part3/finite_n8_general.json.gz --output topics/padua-argmax-alln-20261101/outputs/part3/independent_general_developer_controls.json
```

Exit 0 in 5.459965728 seconds. The authentic n8 general certificate
was accepted; all fourteen deliberate corruptions were rejected, while
a genuine partial cover had its supplied bounds verified but was not
accepted as a global certificate. Source hashes were unchanged. Controls
source SHA256 `c850f635736882de65134465279744c9e4990f08361824c8b13498e0136c030b`;
certificate SHA256
`9c008ae3f0a2774312d1eda32ac1e12dc7df3410f7ecefb8cff936bf5a7355fc`.
This supplements the separately completed field-based n8 replay.

Re-read the administrative updates to numerical record 01 and n2 record
02 and the correctness-record Scope/control appendix. The stale n8-only
Scope sentence is resolved: it now explicitly distinguishes the frozen
field implementation and the separate general implementation. No
mathematical source change or re-execution is needed for that wording.
Updated inspected hashes: record01
`38515c79b2122e33dc6e69518475aa2f7f484c1064d918686b48a3c19de7e67c`;
record02 `1040ea4c1083ea4925dc10c9772dd8ad49840df1884ce7f97cb58a5e0fd6a460`;
record03 `486e346f784f69bb277f20ebb947d942bcc3f62716a34bdfe044c622ea7d8c41`.
Also read the degree-eight result record07: its statement, exact tensor
corner vector, 34-leaf reduction and limitation excluding local-maxima
counts agree with the independently executed certificate. Its initial
pending-replay wording can be updated by development from this receipt.

Final scope conclusion: no unresolved finding in the inspected n2 proof,
finite correctness/constructors and actual n8–16 certificates, edge04/05
proofs, or the checked numerical record. Full T1 was not independently
rerun; finite degrees 3–7 were not re-audited in this assignment; the new
pairing/negative records and global all-n assembly were outside this
supplementary scope. Required Claude audit remains pending. The independent
manifest is refreshed with final source, artifact and receipt identities.
