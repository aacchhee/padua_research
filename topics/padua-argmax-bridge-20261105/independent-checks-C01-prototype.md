# C01 prototype: independent source and bounded-control review

2026-11-06. Rules/input head `4b728b04216a5490910780bc609a82b853058426`.
Distinct reviewer: Codex, assigned Astra high; serving model/effort metadata
not independently exposed. Read AGENTS/WORKFLOW/CODEX and handoffs06/05 in
the preceding ratio review; this is its separately assigned implementation
follow-up. No historical novelty review: internal backend variant only.
No Git, old-source, author-proof or shared-record edits by this reviewer.

**ACCEPTED within bounded prototype scope.** No unresolved mathematical or
executable-source finding. This is an independent fresh build and bounded
control run, not approval of a complete candidate, a certificate acceptance,
a new degree, or overall certifier complexity. Formal Claude audit remains
separate. Any consequential replay still needs its own release and complete
source/input/runtime checks.

Frozen source `code/cheap_C01/prototype.cpp`, 14311 bytes, SHA256
`178bbe5a969a018d91454dc877572a691c9831a4b8793971f5aa303343465dab`.
Mathematical dependencies checked against accepted ratio specification
`ce6101733c9297c00a7e32431e9c0188ba4ce053e059e1080523013993b80890`
and all-class defect theorem
`858634a7f38bbd870fa652e059c1fff72e2102ea3ca374f24506bce0f3f5b9fd`,
whose independent report is
`8fdf43316f9fe39e9c18da8deee9a40d94a2a1e02232028a7644379333d73d52`.
These identify reviewed prose; no executable prose hash is introduced.

Also read the prototype attempt, both generations of unit/box drivers,
the essential developer receipt, `build_prototype.py`, the complete
transitive `build_snapshot_r9.py`, the old v3 kernel and the existing
phase acceptance/reduction contract. The profile driver was inspected for
its different instrumentation and source/build dependency path.

## Ratio and finite-output reconstruction

The runtime implementation follows the accepted guarded identities.
`sincjet` initializes exactly33 rational coefficients using factorials and
outward Arb division. Its value Horner loop is degree32 in x²; its
derivative loop gives x times the degree31 polynomial with coefficient
2j/(2j+1)!. Fixed exponent66 and65 remainder calculations have the exact
67! denominator and derivative factor66. `arb_add_error` includes their
absolute upper magnitudes. The subsequent value and derivative hull
intersections are valid integral bounds. No library sinc, Chebyshev
routine or degree-dependent frequency loop supplies this computation.

`quotient_pair` validates sine/cosine results, excludes zero from the sine
denominator, uses `arb_sqr` and independently checks that square before
division. It stages both quotient candidates through the finite
intersection helper. An indeterminate candidate leaves the entire prior
pair unchanged; finite contradictory intersections throw. The pole branch
never divides by the numerator sinc and includes zero and numerator roots.

`ratio_fixed` rejects invalid k/nonfinite Arb input before the k1 shortcut.
Its checked k range1..513 makes k*k<=263169 and floor(k²/2)<=131584;
the signed-int cap arithmetic cannot overflow. All integer-to-double
conversions in this path are exact. A finite midpoint with |mid|<=100
only proposes an integer turn: `lround` is safe in this small range, the
stored ell is exact, and B(ell) represents it exactly. Negative `ell%2`
is tested by nonzero, so negative odd turns have the correct sign.
Rounding of the midpoint or the decimal pi proposal cannot invalidate the
identity for the selected exact ell. Actual outward residuals must pass
both |A|<=1.5 and |k*A|<=4 guards; then the denominator is intersected
with[5/8,1] and squared positively. Guard failure returns only the global
caps. The fixed-range implementation makes no arbitrary-k promise.

For n2..512, board indexing, sizes4*n*(n+1), N, doubled indices, and
normalizers4N/8N stay within signed-int range. The correction term keeps
the exceptional first-coordinate mode. Gradients match the accepted
phase chain rule and continue through all removable poles. Midpoints
and half-widths are formed from exact binary64 endpoint Arb points;
no binary64 midpoint substitutes for the exact mean-value center.

The collector's two early-return branches precede its final generic
finite-output loop. This does not create a nonfinite result on its checked
domain: ratio caps bound every primitive by a modest degree polynomial,
the natural sums and corner constant stay finite, and the mean-value
upper may be infinite only as an optional upper discarded by the finite
natural bound. The analytic branch uses finite fixed outputs. Invalid
binary64 endpoints and n are rejected before board work. The extreme
finite-endpoint control below also exercises this route. This conclusion
uses the stated outward Arb arithmetic assumptions; no floating-point
exception or allocation failure is reclassified as successful proof.

## Collection shortcuts and class coverage

The lazy return tests its own outward S_upper against its own Lc_lower.
Both are already binary64 bounds, so the ordinary strict comparison is
exactly their strict ordering. For the corner orbit, triangle inequality
and the four periodic reflection bijections give

    (1/(8N))*sum |H_rs+H_-r,s+H_r,-s+H_-r,-s|
      <= (1/(2N))*sum |H_rs| = S.

Consequently returning C_upper=S_upper is valid, and defect_lower0 is
valid for every noncorner class. Skipping both orbit and profile scans
here loses no needed strictness because S_upper<Lc_lower already holds.

If that comparison fails, the orbit scan still runs. The analytic floor
then requires integer n>=64 and the **entire input rectangle's** radius
<=1/2. Absolute value and max of finite binary64 endpoints are exact;
conversion to Arb points is exact; the sum is outward. Testing its upper
bound against exactly represented.5 is conservative. It admits the exact
.25+.25 boundary and rejects one-ULP outward perturbation. This proves the
condition for every point in the original requested rectangle; any extra
Arb hull inflation need not belong to that original rectangle. The
returned1/2048 is an exact dyadic lower bound from the accepted all-class
theorem on every admissible **noncorner** physical intersection.

The analytic branch is not a floor for the two actual nonnode corner
classes. Their separate orbit/local predicate remains required in the
external acceptance contract. The zero-phase n64 control makes this
distinction concrete: S_upper-defect_lower<Lc_lower holds, but
C_upper>=Lc_lower, so the defect alone must not exclude the actual corner.
This prototype exports bounds, not a certificate acceptance function.

Outside the radius/degree guards, the old full projected scan remains:
both natural defect and opposite-sign positive-pair bounds, both
orientations, all center parities, original normalization, endpoint
physical-sign exclusions, and exclusion of actual corner index pairs.
There is no representative-center sampling or phase-sign swap. The bound
can weaken while staying valid; weaker enclosures may fail more leaves.

## Cost and dependency inspection

Each of three boards contains2n(n+1) primitive calls, each with four ratio
evaluations and one correction sine/cosine. Each ratio uses at most two
paired sine/cosine calls and fixed-order arithmetic. Thus the source count
is exactly24n(n+1) ratios and at most54n(n+1) paired trigonometric calls per
box. The nine independent box controls satisfy those counts. Fixed33-term
coefficient initialization, fixed32 Horner steps and fixed exponent powers
do not grow with degree.

The retained `base` and `hybrid` fields contain copies of the same new
jet; the old harmonic baseline is neither computed nor intersected back
into the result. The no-op `refine_ratio` is unused in the primitive.
The final duplicated output pair likewise adds no second arithmetic
backend. Profile fallback still has cubic arithmetic outside the lazy
and analytic branches. Trigonometric argument reduction, precision and
integer bit costs remain ordinary library costs, not a constant bit-time
claim. There is no hidden degree-k library polynomial call in this path.

`build_prototype.py` imports and adapts the preserved r9 builder by two
literal substitutions. Inspection confirms that the actual source origin
and snapshot in the fresh manifest point to the frozen prototype, not
old v3. The builder preprocesses pinned headers, snapshots FLINT/GMP/MPFR,
compiles the preprocessed unit, records toolchain/linked closures and
checks dependency stability. The independent driver additionally pins
and rechecks both project builder modules, the prototype and itself;
checks source snapshot, preprocessed unit and binary after execution;
captures actual loaded mappings and rechecks them and all dependency
groups. Runtime proof guards contain integer/constants/validated inputs,
not caller assertion fields or prose hashes.

**NOTE P1, historical driver provenance limitation.** The author's
`box_controls_v2.py` verifies linked dependencies but does not itself
record/recheck actual loaded mappings; its receipt also does not pin the
transitive r9 builder source as an executed Python dependency. This was
reported to the coordinator before any changes. The independent fresh
run closes those checks for the results below; it does not retroactively
add them to old receipts. No author correction was needed to establish
the present bounded source result. A future full-candidate wrapper must
carry all of these checks, including its acceptance modules and input
identity. This review does not authorize such a replay.

## Executed independent controls

Command, from repository root:

    python topics/padua-argmax-bridge-20261105/code/cheap_c01_ratio_review/prototype_review.py

Actual exit0, **651 assertions PASS**,54 valid ratio cases and9 boxes.
Own CPU3.160681920s plus build-child CPU1.204038s, total4.364719920s;
wall4.364311275s. This is below the90CPU-s review cap. Source hashes and
loaded dependency identities were unchanged before/after the run.

The54 ratio cases use k in{1,2,3,64,511,513}, turns{-4,-1,1,4}, exact
and crossed poles, numerator zeros, rejected guards, broad residuals and
maximum finite binary64 input. They exercised41 pole-chart returns,
11 quotient/R1 returns and2 global fallbacks. Distinct100-digit direct
harmonic point comparisons supplement the source proof; they are
numerical controls, not validated proofs. Exact pole values and parity
were checked separately. Invalid k, turns, reversed/nonfinite inputs,
paired nonfinite staging and finite contradictions were also checked.

| Bounded box control | Observed result |
|---|---|
| Two saved n32 former-failure boxes | Reproduce all seven published prototype bounds exactly; profile scan retained; strict S-minus-defect predicate passes. |
| n63,[0,.25]² | Profile scan retained; no analytic-floor use. |
| n64,[0,.25]² | Analytic1/2048 floor; broad strict comparison still fails. |
| n64, upper alpha one ULP above.25 | Profile scan restored; no analytic-floor use. |
| n64,[-.25,0]×[0,.25] | Analytic1/2048 floor includes negative boundary phases. |
| n64, zero-phase point | Analytic noncorner floor; corner upper remains at least Lc_lower. |
| n64, saved synthetic narrow box | Own strict S comparison; lazy C=S,defect0; no orbit/profile scan. |
| n2, alpha from-negative to-positive maximum finite binary64 | Finite successful global-cap route; numerical profile retained. |

The independent narrow n64 call took about.260CPU-s. No n128 timing was
rerun here. The developer's n128 selected timing1.136CPU-s versus the
previous instrumented24.120CPU-s remains a separately labeled measurement;
different instrumentation and weakened outputs prevent inferring a
whole-cover speedup. In particular the two n32 S upper bounds weaken
relative to old v3 by about.160915 and.151455; their defect lower bounds
also weaken. Those two selected predicates pass, but no assertion about
the other original leaves follows. Broad synthetic non-strictness is
preserved rather than treated as successful acceptance.

Small retained receipt: `evidence/c01-review-prototype.json`, containing
exact selected outputs, counts, command, source/dependency identities and
the hash/locator of the full local manifest. That manifest records4
toolchain entries,13 toolchain runtime entries,212 headers,6 dependency
inputs,8 linked and8 actually loaded dependency entries, plus Python
runtime module identities. The86,901-byte raw manifest is local under
`/tmp`, regenerable by the committed driver; physical cold-storage
transfer remains pending. No large generated artifact is proposed for Git.

The developer's four existing raw receipts were independently hash/size
checked. They remain unchanged. Their original failed broad predicates
and first conservative radius-guard version remain preserved. The
independent driver imports no producer interval arithmetic and invokes
no acceptance traversal, tree refinement, whole candidate or new degree
certificate. Formal audit and any future full-replay readiness checks
remain outside this completed bounded review.
