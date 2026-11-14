# C03 endpoint and centered refinements — independent source review

2026-11-06. Rules/input `b6e67b3c78cb668b6d2f9da5a5560537d2960bf3`.
Distinct reviewer: Codex, assigned Astra high; serving metadata unexposed.
Reviewed source `code/cheap_C03/prototype.cpp`,16881 bytes, SHA256
`9e357b25efde553211563bb69147644c67b7752bc703bf05ac502141c82e0861`.
**ACCEPTED for modes0,1,2 within bounded source/control scope.** No
unresolved source finding. The C03 math is independently accepted in
[ratio review](independent-checks-C03-ratio.md). Formal Claude audit and
any complete-candidate acceptance are separate. No author code or old
C01/C02 source/report/receipt was modified.

This is an internal tightness/backend variant, not a historical novelty
review. Read the complete new source, builder, controls, developer attempt
and essential evidence; compared with the previously reviewed C01 source,
ratio specification and frozen failed C02 full report. The source adds
no producer interval arithmetic or new defect theorem.

## Source reconstruction

The preserved C01 arithmetic is now named `ratio_base`. It retains its
validated k1 shortcut, checked1..513 integer range, exact cap and turn
parity, quotient guards, J32 sinc chart, finite global fallback and paired
intersection staging. `ratio_fixed` calls that base first, then continues
to optional refinements even when the base quotient succeeded. Endpoint
and center point evaluations call `ratio_base`, so there is no recursion.

`endpoint_chart` constructs the actual outward residual with Arb pi and
an exact stored integer turn. It first checks that residual, then extracts
absolute lower/upper ARF bounds into exact dyadic point objects l,u. The
second guard explicitly checks those extracted points against1.5 and
k*u<=4. It never replaces an outward radius by a rounded midpoint or
inward binary64 endpoint. Midpoint turn proposal is bounded by100, so
`lround` and integer-to-double conversions are safe and exact for the
stored ell; the correctness proof does not depend on nearest-pole choice.

At l0 the code supplies value k directly. Otherwise l and u receive
nonrecursive base point enclosures. The candidate interval takes the
lower bound of F(u) and upper bound of F(l), with parity reversal for
negative eps. Negative-lobe values are retained. The same actual residual
ball determines the derivative half-cap; negative odd turns and negative
residuals each contribute their proper sign reversal. Both sign tests
apply at an exact zero ball, giving derivative0. A zero-crossing ball
receives no unjustified one-sided sign.

Mode0 stops after this endpoint/sign refinement. Mode1 then uses the
exact ARF midpoint of the input ball, constructs actual T=Z-c and an
outward H, and applies the accepted global-C2 Taylor pair. The largest
integer products at k513 remain below2^31, so the long C2 product, k*k,
1-k*k and all double conversions here are exact and overflow-safe.
The center is inside the input ball, even if that ball over-encloses
the original requested interval.

Mode2 optionally bounds curvature by
(1-k*k)*r-2*(cos(Z)/sin(Z))*d, using the current valid r,d on the same
ball Z. It requires finite sin/cos and a sine interval excluding zero.
The exact midpoint belongs to Z, so the curvature controls every Taylor
path. `maxabs` gives an outward point upper bound; the conservative
binary64 comparison selects it only if it is below global C2. Otherwise
global C2 remains. The resulting Taylor radii use validated squares and
ordinary outward products; no local-curvature recurrence is invoked.

Every successful refinement passes through the existing joint finite
intersection helper. Nonfinite candidates leave the old pair intact;
finite disjoint candidates throw. The mathematical intersection preserves
the old C01 valid image enclosure. Arb's finite-radius representation can
add a tiny outward expansion after intersection, as the math explicitly
allows; this is not a promise that every exported bound is monotonically
smaller to its last bit. No harmonic baseline is recomputed or secretly
intersected back into the result. The copied base/hybrid board fields
hold the same new jet, and the collector uses one such board set.

The primitive chain derivatives, exact board parity, corner-orbit
normalization, lazy own-S comparison, guarded n>=64 half-radius floor,
all-center fallback and true-corner separation remain the accepted C01
collector. No stronger C02 floor is adopted. For a full box there are
exactly24n(n+1) outer ratio calls. Mode0 uses at most3 base evaluations
and6 paired sin/cos calls per outer ratio; mode1 at most4 and8; mode2
at most4 and9. Including primitive correction calls gives conservative
box caps150N,198N,222N paired trig calls. All twelve selected calls meet
these limits. Polynomial/order work is fixed, with ordinary precision,
integer and argument-reduction costs; no full-program complexity theorem
is claimed.

## Independent controls and preserved first diagnostic failure

The first reviewer driver incorrectly required chart admission for ideal
k8 input[0,1/2]. Its assertion stopped the run before any box call. Direct
inspection showed that Arb's outward hull inflation moves the actual
extracted endpoint beyond the literal k*u<=4 guard. The code correctly
returned finite global caps and endpoint_refinements0; no containment
assertion failed. This was a reviewer-test expectation error, not a source
defect. The original driver snapshot, exit1, diagnostic output and timing
limitation are preserved in
`evidence/c03-review-prototype-first-control.json` SHA
`9682f711e5b889d8176ce72c63e80827216fe97761d50638cce1ba4c762554af`.
No author code was corrected. The revised test retains this actual guard
rejection and adds interior[0,31/64] to exercise the negative-lobe image.

Corrected independent command:

    python topics/padua-argmax-bridge-20261105/code/cheap_c03_review/control.py

Actual exit0: **2896 assertions PASS**,60 scalar cases in each of3 modes
(180 total), plus12 selected-box calls. Recorded successful-run CPU is
3.928946773 own plus1.690729 build-child=5.619675773s; wall5.622902865s.
The controls stay within the bounded review allocation; they do not
traverse a candidate or launch a producer. The earlier stopped diagnostic
has no complete timing receipt, as recorded in its preserved limitation;
the successful-run timing is not mislabeled as cumulative review CPU.

Scalar cases cover k1,2,3,8,32,513; turns-4,-1,0,4; exact/crossed poles;
negative lobes and numerator zeros; parity/sign reversal; unadmitted
endpoints; the false-global-monotonicity region; wide intervals; maximum
finite binary64 input; invalid/nonfinite/reversed inputs; nonfinite pair
staging and finite contradictions. Three-point100-digit direct finite
frequency comparisons are diagnostic references only. Production code
contains none of those frequency loops. Exact pole values are checked
separately. New and old C01 pairs overlap in every valid control, with
all new samples enclosed. Separated quotient cases explicitly show an
additional endpoint refinement, so quotient success does not erase the
intended gain.

The new library was built freshly from the pinned source. The old C01
scalar comparator was the hash-verified binary from the frozen C02 build;
its source, preprocessed unit, binary and complete runtime closure were
checked before and after. The new project builder and transitive r9
builder, source, control, C02 raw report and C03 developer evidence were
also pinned before execution and rechecked afterward. The fresh source
snapshot matched the reviewed source exactly. Both libraries' actually
loaded mappings were captured after loading and verified after controls,
along with all toolchain/header/linked/dependency identities. No producer
arithmetic module or whole-checker acceptance function was imported.

## Selected failed-box recovery and recommendation

Selection was independently reconstructed from the frozen full C02 result:
its first/largest far failure, largest distinct far failure, largest
corner-orbit excess, and greatest near S-minus-defect demand. The last
case is a demanding previously passing near predicate, not one of C02's
76 failures. The four saved inputs were tested in each of the3 modes.
All seven bounds reproduce the developer's selected results exactly;
all twelve strict per-kind comparisons pass using Fraction arithmetic.

| root/path and kind | Mode0 S upper | Mode1 S upper | Mode2 S upper |
|---|---:|---:|---:|
|0/0101 far|10.52762339660344|10.485424688619837|10.453102385700959|
|1/0000 far|10.527623396460257|10.485424688486013|10.453102327858478|
|2/0100010 corner-orbit|10.969008269066904|10.603325483741413|10.529344164065483|
|3/000000000 maximum exclusion|11.332100625368787|11.241357700017968|11.222658467731103|

Lc_lower is10.993594541100443 in every case. The first three cases have
S_upper<Lc_lower already in mode0, so the inherited lazy collector returns
C_upper=S_upper and defect0. The near case has mode0 defect lower
.40084534366373437 and passes S-minus-defect strictly on its unchanged
full-radius bootstrap domain. No corner theorem or finite-energy premise
was broadened. The first far box improves from C02 S11.467798411235936
to mode0 S10.52762339660344; old v3 gave10.559446940553098.

Mode0 selected-box CPU ranged.111701–.172001s; mode1,.207895–.271955s;
mode2,.251860–.327959s. **Recommend frozen mode0 for a separately released
full original-candidate test:** it suffices on these cases at the lowest
observed cost. This recommendation is not complete-tree acceptance or
permission to rescue a failed mode0 replay by switching modes. All other
original leaves remain untested here, and C02's failure is preserved.

Essential new receipt `evidence/c03-review-prototype.json`,9053 bytes,
SHA`5185e675fca75ef3c06bc5de34257987bc80d9cdfeb7cb525593f3cd43d039e2`;
control source SHA
`11e8f438741e39621e5e0cacbc1d00eaf3fe8f096806af3ba4fad96d9c84ee52`.
The214630-byte full local manifest is at
`/tmp/c03-independent-review-4k5025ha.json`, SHA
`80496792f63aa85c2928f7b98dcc54e2f8f713f191c9627cb7a80899ca19150e`.
It includes all scalar records, old/new build/runtime closures and selected
box data. Large artifacts stay local; physical archive transfer is pending.

Source/math review is complete. A complete original-candidate replay still
requires a frozen mode0 wrapper, distinct wrapper review, publication and
explicit coordinator release. No full replay, producer, candidate change,
tree refinement or new degree has occurred in this review.

## Mode0 wrapper prepared; execution remains pending

After the mathematical and source PASS, this reviewer prepared
`code/cheap_C03/replay.py`, 22974 bytes, SHA256
`0e53a602103b6b5bf0afb80d338329ab8e3c442d7ab86e2051d3a88e9a447d37`.
This subsection records preparation and is not an independent audit of
the wrapper I authored. A distinct coordinator review, publication of
the frozen sources, and explicit release must precede execution.

The wrapper preserves the previously reviewed C02 supervisor structure
and invokes unchanged `check_r8.check(data, kernel)` with an explicit
newly built C03 kernel. It selects mode0 before every bound-producing
use, records the selection, collects all twelve native counters, and
rejects nonzero centered/ODE counters. It also checks the selection and
counter identity after completion. There is no mode switch or retry.
The original 21338-byte candidate, SHA256
`97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e`,
retains all364 leaves, with no cap, producer, refinement or new degree.

The future one-shot scope remains total group-plus-supervisor CPU180s,
watchdog176s, and worker CPU soft/hard178/179s, including compiler
helpers. Fresh outputs are reserved under
`local-output/argmax-bridge-20261105/cheap-C03/n32`, with essential receipt
`evidence/c03-cheap-n32.json`; both paths are absent at preparation.
The wrapper refuses existing outputs and requires the full published
source commit. Fifteen pinned inputs plus the wrapper are checked against
that commit. Source/input identities, transitive project Python files,
build snapshot, preprocessed translation unit, headers, toolchain,
linked dependencies and actually loaded closure are recorded and checked
before/after as in C02. The accepted old-v3 baseline remains the bounds
comparison; the failed C02 receipt is additionally pinned and preserved.

Preparation validation compiled the Python AST, verified all15 pinned
identities and the decompressed candidate bytes, checked that there is
one uncapped two-argument acceptance call, checked explicit mode selection
and twelve-counter use, and confirmed both output paths remain absent.
These checks imported only the wrapper's standard-library helper scope:
no acceptance module, native library, builder, full check or Git
publication check was executed. Full-tree acceptance is still unknown.
