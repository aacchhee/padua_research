# Supplementary independent review — round9 Arb pair-defect bound

2026-11-06. Rules/input `d974329331ee4090e8ca1d5100342e69039edbf0`.
Distinct reviewer `/root/review_bootstrap_r8`, coordinator allocation Astra
high; serving model/effort metadata unexposed. This supplements the required
Claude audit. Only this new report, new controls and new small receipt are
owned by this worker. No old proof, kernel, failure receipt, tree or Git
state is changed.

## Scope and frozen source

This is a focused independent implementation review of an existing real
triangle-defect identity, not a new mathematical-mechanism or novelty claim.
The identity already occurs in the producer's earlier pair calculation;
Arb arithmetic and the implementation below are independently derived.
The review does not assess priority or exhaustively repeat state/IDEAS.md.
The accepted PD-T364 all-class/profile identities and the round8 holistic
reduction remain dependencies. Read their full proofs in the preceding
review, and inspected the new diff against the frozen accepted v2 source.

| Frozen source | SHA256 |
|---|---|
| hybrid_kernel_v3.cpp |f52d1a9da3c86212663f7ac22e9475b76811d7be4bbc4916779fd32a59d95bf0|
| build_snapshot_r9.py |6e29f5990515d50829aa7978ebeeb97dcb49e8f62716d62d37fc8ddc69e82bfa|
| check_r9.py |1161ad5c7d4ced9736bffcbf633df349189c842314b04664ff6b465e50f2c01e|
| Developer r9_controls.py |8de427cc768b81cb59d9c3993a5b6c0e7d794f6033339548f11c92a8c8ff2b89|

The author-frozen implementation reduction theory/N3-defect-enclosure-r9.md,
SHA256aa160deac705d6ea3261820e80c33ee8ef99c5642378f0537bb989d1d4e63d13,
was read in full, with its idea/attempt records. Its rectangle witnesses,
zero cases, directed lower contract, fixed-pair zeros, profile normalization
and unchanged strict cover implication agree with the reconstruction below.
The author explicitly consolidates the mathematical identity as inherited;
the recorded gate scope/chronology was inspected without a novelty verdict.

All source paths above are within code/phase_checker. The final old acceptance source
check_r8.py remains3c71ada8..., check_r6.py437378a5..., original builder
19a5a7c2... and hybrid-v2 kernel17fea91d.... New checker calls the unchanged
r8 acceptance function with an explicit new backend; it does not monkeypatch
any old function or infer acceptance from the failed producer certificate.

## Independent rectangle proof

For real x,y, let d(x,y)=|x|+|y|-|x+y|. The triangle inequality gives
d>=0. If x,y have the same weak sign, d=0. If they have strict opposite
signs, write their magnitudes p,q>0. Then

    d=p+q-|p-q|=2min(p,q).

For nonempty closed intervals X=[a,b], Y=[c,e], if a>0 and e<0 the
exact rectangular infimum is2min(a,-e); if b<0 and c>0 it is2min(-b,c).
In every other case it is0. Indeed, an interval containing0 allows a zero
argument, giving d=0. If neither contains0, each has a strict fixed sign;
the only remaining possibility is equal signs, also giving d=0. This
covers endpoint equality, signed zeros, mixed-sign intervals and singleton
intervals. The opposite-sign infimum is attained at the endpoints nearest
zero, so the expression is both a lower bound and the exact infimum for
those supplied real rectangles.

No statistical or mathematical independence of the two primitive values is
assumed: their correlated attainable pairs lie inside the enclosing Cartesian
product, so its infimum is still a lower bound on the actual phase image.

The implementation's Arb balls can contain a slightly larger interval than
the original binary64 endpoint rectangle. It tests strict signs on those
balls and obtains rounded-down absolute lower endpoints. Therefore the
computed floor may be weaker than the original rectangle's exact infimum;
this is safe. If strict signs cannot be certified, returning0 is justified
by nonnegativity, including all zero-touch and mixed-sign cases.

For the independent test oracle, the same real function has both extrema
on rectangle corners. For fixed y>0, d is nonincreasing in x; for fixed
y<0 it is nondecreasing; for y=0 it is constant. The analogous statement
holds for fixed x as y varies. Optimizing one variable and then the other
therefore reduces both minimum and maximum to the four endpoint pairs.
The controls evaluate |x|+|y|-|x+y| there with exact Python Fractions,
without reusing the producer or new C++ sign-dispatch formula.

## One-sided accumulation and unchanged class reduction

`positive_pair_lower` first rejects nonfinite balls. Opposite strict
signs are certified with Arb's sign predicates. It forms absolute balls,
extracts both lower endpoints using arb_get_lbound_arf, chooses their arf
minimum, and multiplies by2 with an exact exponent shift. arb_set_arf
stores that scalar as a point-valued ball. This object is a lower bound,
not a two-sided enclosure of the true pair defect. Its comment states that
meaning, and its only production use is in the separate positive profiles.

Each pointwise pair floor is <= the actual pair defect throughout the
whole phase box. Arb addition encloses the sum of those scalar floors;
although its rounded ball may extend below the scalar sum, its lower
endpoint remains a valid lower bound for the true summed defect. Division
by the positive exact integer4n(n+1), followed by downward extraction,
preserves this inequality. The code never substitutes a floor as a true
pair value in a two-sided function enclosure, derivative, or upper bound.

The old natural qv/qh interval sums are retained verbatim. Taking the
maximum of zero, their old lower bounds and the two new positive-profile
lower bounds is valid because every constituent bounds the corresponding
full noncorner defect below. Taking the minimum over every admissible
noncorner center then supplies a bound for every such class. The existing
factor1/(4N), periodic index reflections, unchanged phase offsets,
endpoint sign screening, parity classes and actual-corner exclusions are
identical to v2. Zero-boundary centers are still retained. No center is
sampled or omitted to improve a bound.

Both finite and hybrid boards receive this refinement. Each has independent
valid enclosures, so their final maximum lower bound remains valid. The
existing natural bounds ensure the new defect bound cannot be weaker than
v2 when evaluated on the same exact boxes. Only defect lower bounds change:
S/orbit upper bounds, derivative machinery, Lc/pi constants, optional ratio
fallback and strict global acceptance conditions remain unchanged by diff.
No producer MPFR source/function is imported, copied or linked.

## Build, wrapper and provenance

The new builder selects only round9/v3, writes to a separate phase-r9
local directory and reuses the pinned runtime installation. Apart from
those names/defaults, its fresh snapshot, preprocessed translation unit,
toolchain/header/runtime and actual-loaded-mapping workflow is unchanged.
The new wrapper consumes one immutable candidate byte snapshot and invokes
unchanged check_r8.check with the explicit v3 kernel. It records transitive
Python sources, native source and complete build provenance, verifies
source/build/runtime entries after execution, and refuses report overwrite.
The actual candidate geometry, format/mode, fixed2..128 energy premise,
strict comparisons, full prefix partition and pending-leaf rejection are
therefore unchanged.

The unchanged old arithmetic functions were checked by source diff rather
than rerunning the old full ratio campaign. No whole n32 replay is part of
this review. The authenticated old failed candidate and report are inputs
to bounded comparison only; neither their files nor their paths are changed.

## Actual distinct controls

Executed once on the frozen sources:

    python topics/padua-argmax-bridge-20261105/code/phase_checker/r9_independent_controls.py

Own control source SHA256
991d9a280d7867abd331a774711d70524df2f2bb744d9d115078e1c7d4fe3726.
**PASS, exit0:237 exact-rational pair rectangles and1658 assertions.**
Own CPU1.441453486s, waited compiler/build-helper CPU1.167199s; well below
the120CPU-second control budget. A subsequent read-only check rehashed
254build/runtime entries, all unchanged, without another kernel execution.

The225 grid rectangles are all pairs of intervals with endpoints in
{-3,-1,0,1,3}. Twelve extra cases include opposite singleton equality,
asymmetric endpoints, zero touching, signed zero, mixed signs, one-ULP
endpoints, binary64 subnormals, scales2^500/2^-500 and a representable
large doubled singleton. The exact corner oracle verifies the new lower
bound, retained natural lower/upper interval and their final maximum.
Malformed/reversed/NaN/infinite inputs reject. A pair whose doubled lower
bound exceeds finite binary64 output range returns a failure status,
instead of supplying an accepted infinite bound.

A fresh independent Arb v3 build then evaluated only three saved failed
n32boxes, preregistered in this control source. Each kept its exact original
root/path/box and had unchanged S, corner, Lc and pi output bits. All three
new defect lower bounds are positive and the strict noncorner test passes:

| Root/path | New defect lower | Exact excess U_S-d-L |
|---|---:|---|
|0/111111111|0.39771335298227384|-762493341145887/4503599627370496|
|0/111111011|0.4055197168017104|-253349245284715/1125899906842624|
|0/1111111001|0.4472473916226339|-7568544686090273/18014398509481984|

The first was origin-adjacent, the second was an off-axis rectangle, and
the third had the smallest original positive failure excess. These bounded
passes do not claim the other17failed boxes or the full364-leaf candidate
pass. They supply the preregistered discrimination between a useful
independent pair bound and a purely cosmetic code change.

Full inputs, outputs, exact rational pair extrema, selected boxes and
source identities are in evidence/phase-r9-review.json. Its source manifest
pins the unchanged original candidate97c33918... and failed reportb7801039....
Fresh build closure is retained locally in
local-output/argmax-bridge-20261105/phase-r9/independent-controls/build-provenance.json,
48442bytes, SHAd81237f2a6a4e89d2c2c58bf9b4515dee1bacc477d0a3effb2358baf0a5a3f41.
These controls neither create a new producer tree nor convert the old
failed receipt into an acceptance.

## Disposition

**ACCEPTED before a consequential replay**, with no unresolved finding:
the frozen mathematical implementation reduction, new source/build/wrapper
and independent bounded controls satisfy the stated scope. The coordinator
may release its one budgeted full replay of the original364-leaf n32
candidate after publishing the reviewed source. No whole replay has run
here, and selected-box passes are not global acceptance. No producer rerun,
refinement, other degree or arithmetic source change is authorized by this
review. Required Claude audit remains separate.
