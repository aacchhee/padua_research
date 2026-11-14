# Supplementary phase mathematics and source review

Reviewer: distinct Codex subagent `/root/phase_math_review`, assigned
gpt-6-astra high; serving model/effort are not independently exposed.
Rules/input read at `3dda890275a7599caa707b0fb8c0b6e6f6a80643`.
This supplements, and does not replace, the required Claude audit.

**Disposition:** no unresolved mathematical or source-correctness finding in
the reviewed phase reduction for the intended n17/24/32 overlap. The one
concrete provenance finding R1 is CLOSED at the revised hashes below.
This does **not** accept a degree certificate: the subsequently executed
complete n17 producer partition failed 364 of the independent checker's
1288 leaf predicates. It remains an unaccepted phase certificate. The
separate already accepted native n33–36 certificates are outside this review.

N5-02's central-strip theorem also passes this supplementary mathematical
inspection at its stated scope. Whole-edge ordering, a maximum bound for its
one-dimensional model, effective onset, and PD-T099 remain OPEN.

## Scope, inputs and evidence

Read AGENTS, WORKFLOW, CODEX, handoff01, plan and the novelty baseline;
the full PD-T364 reduction and normalization; N3-enclosure-spec; producer
`n3_outward.c`, `n3_outward_interval.h`, `n3_outward_run.py`; checker
`arb_kernel.cpp`, `check.py`, `controls.py`, `setup.py`, `build.sh`; and
phase-checker-reduction plus the frozen calibration receipt. PD-T364 is
itself sufficient; this review changes no native Bernstein predicate and
does not claim a new reconstruction of predecessor PD-T210.

For N5, read the full frozen N5-central-edge-defect proof/code/receipt and
precise round-2 gate; PD-T185, PD-T222 and PD-T366; N1-row-model and the
N1 cancellation-quadrature continuation for context. N1's previously
reviewed partial-cotangent dependency is used at its recorded scope, not
reaudited here. No literature transfer or novelty claim is made. This is
the workflow's no-novelty review exception: the full IDEAS registry was not
reread, and no new candidate or novelty disposition is issued.

The initial frozen inputs and actual independent execution are pinned in
[phase-math-review-rerun.json](evidence/phase-math-review-rerun.json).
Important initial identities are:

| File | SHA-256 |
|---|---|
| n3_outward.c | `cfeae9fe2b61e9c7ec2c4d943762ac988e64fa02652ccfe4342430c4ee5f22dd` |
| n3_outward_interval.h | `6dca513ddbd94264d454872c9f5e753e355d15b49152dc4b19d51cff7635131b` |
| n3_outward_run.py | `9110c663e749afb86240250a3cc77f7b824df556804c11481ac65c1239370e87` |
| Arb kernel, unchanged by R1 | `236116452dc7aae66e39cbf8800fe847cffe931ac0ce8a9682397313de7c43a6` |
| Initial checker | `d38f268e817518dd02ff00a102f9c0c2a0afa05598a4abb586d5ea602aa85bac` |
| N5-02 proof | `51ed4849ea1ff68bdd607596f8de1f893613b3bf644380dde4e00024591a4870` |

R1 inputs and the subsequent independent manifest/guard checks are pinned in
[phase-math-review-r1.json](evidence/phase-math-review-r1.json). The revised
checker is `8713026a1b5a872f0e8dd33c311eafef2cf310f42ae2eebb4055ad224b8acfae`;
build_snapshot.py is
`a8a805ba27e880a3a5cf1db7d0707dab4a982d7a988b493c822015518ee2e2c2`.
Line references to checker Python below use this revision unless explicitly
marked initial. The reviewed producer and Arb arithmetic hashes did not
change during the review.

## Reconstruction of the enclosure and normalization

For any center c inside a convex box B, set F=sum_i |h_i| with C1
primitives h_i. Along z(t)=c+t(x-c), each |h_i(z(t))| is absolutely
continuous. Almost everywhere its derivative is sign(h_i(z(t))) times
the smooth chain derivative; at zeros the derivative is zero almost
everywhere on the zero set. The symmetric hull in the specification
therefore contains it, including a zero crossing or an identically zero
term. Coordinate hulls may be independent; that enlarges the enclosure.
Consequently the line derivative lies in

    (x_a-c_a) sum_i D(H_i,A_i) + (x_b-c_b) sum_i D(H_i,B_i).

Integrating and using the two maximum distances from c gives the displayed
whole-sum mean-value bound. No derivative of a discontinuous sign function
is required. Taking the minimum with a natural absolute-value upper bound
is valid because both independently bound the same F. A strict-sign test
is needed only to use the nonsymmetric derivative interval; a range merely
touching zero correctly takes the symmetric hull.

The producer's c is a rounded binary64 midpoint, not the exact midpoint.
That is safe: n3_outward.c:31 evaluates at that same c and uses the maximum
of **both** outward center-to-endpoint distances. The lemma works for this
center as well. The Arb kernel:63–64 instead forms the exact-endpoint
midpoint and half-width in Arb, which encloses their exact values.

For s=(u+v)/2 and t=(u-v)/2, differentiating the finite identity gives

    G_u=(D_s+D_t)/2+n sin(nu),   G_v=(D_s-D_t)/2.

The phase derivatives divide these by n and m=n+1. Producer:14–22 and
Arb:36–41 use precisely these factors. The producer's quotient derivative
is used only when its sine denominator excludes zero; the fallback finite
frequency sum includes every collision. Arb's finite cosine polynomial
and differentiated sine polynomial are denominator-free and valid at all
collisions, including (pi,pi). The corrected highest x mode is retained.

Endpoint reflection has multiplicity two with weight 1/2 in either endpoint
coordinate, and multiplicity one with weight one for an interior residue.
This gives exactly 2nm odd-board terms and S normalization 1/(2nm).
The four-copy orbit must be summed before absolute value and before sign
selection. Both implementations do so (producer:35; Arb:70–73), with
normalization 1/(8nm). Fixed index reflections at an actual odd corner are
r->-r and s->-s modulo 2n,2m for either parity; no new corner symmetry is
being assumed.

For projected defects, d(x,y)=|x|+|y|-|x+y| is nonnegative and equals
2 min(|x|,|y|) on opposite signs. Producer:45–46 sums the latter lower
bound, zero otherwise; Arb:76–82 encloses the former directly. Both use
1/(4nm), including the double counting of each nonfixed reflected pair.
Integer indices reflect while alpha,beta remain unchanged. Fixed pairs
have zero exact defect and cause no endpoint correction.

Both implementations enumerate every odd noncorner physical center and
take a minimum of the maximum of horizontal/vertical lower profiles.
Arb:86–93 omits endpoint centers only on an incompatible inward phase
sign; retaining extra centers whose precise intersection is empty only
decreases the lower bound. Producer:48 uses outward physical interval
exclusion, also conservative. Clipping the resulting bound against zero
is justified by exact nonnegativity. T366 is used only for n>=48 and an
entire box satisfying |alpha|+|beta|<=1/10; it is not extrapolated to the
17/24/32 overlap.

## Geometry, strictness and numerical domain

The four closed quadrant roots contain the phase diamond because their
outer endpoint is an outward pi bound. Checker:109–113 independently
validates the constants and reconstructs the root geometry. Its outside
test uses exact rational endpoint minimum distances and strict comparison
with its own pi upper bound. Boundaries of the diamond cannot disappear
through an equality test.

The root/path trie checks duplicates, ancestor overlap and missing siblings,
then reduces every root to its empty path (checker:63–82). Reconstruction
uses the producer's actual binary64 split midpoint and gives both children
the same endpoint. Stagnant splits are rejected. Pending leaves participate
in the cover but forbid acceptance. A max-leaf cap cannot imply acceptance
unless every leaf was actually checked.

Far leaves require S_upper<Lc_lower. Nonlocal leaves require both the
corner-orbit upper and S_upper-defect_lower to be strictly below Lc_lower.
The final subtraction/comparison is Fraction arithmetic, so a rounded
equality cannot become strictness. Local leaves substitute the inherited
corner theorem for the orbit comparison while retaining strict comparison
for every noncorner center. Since 1-cos t<=t²/2, checker:96–100's exact
H test suffices for T251 or T369 on its own domain. It proves strictness
for H>0 and leaves precisely the two actual nonnode corners as equality
points; a positive numerical margin at H=0 is neither required nor claimed.

Producer directed pi/transcendental endpoints and one-ulp-expanded basic
operations are sound on the documented IEEE binary64, round-to-nearest,
no-fast-math domain. For the CLI range 2<=n<=1000, all mesh integer products
used as exact doubles are <2^53, and n*n, 4n(n+1) fit signed 32-bit
integers. Root phases remain within +/-pi_hi. The elementary arguments
used by the producer's extrema/pole search are then small enough that
the approximate integer search with a +/-3 extremum window cannot miss
an extremum. Near a quotient pole, the enclosing q=x-l*pi and sinc
form preserve the exact periodic identity; the fallback [-k,k] is valid.
The positive denominator guard is retained. No large-argument lround or
integer-overflow behavior is relied on for arbitrary external C calls.

The checker explicitly supports only 2<=n<=512; its products and exact
integer conversions are safe there. The producer/checker degree mismatch,
producer reliance on Python assertions, and lack of a producer stagnation
guard are bounded-domain/termination limitations, not an accepted false
certificate: the independent checker rejects unsupported degrees and bad
paths. They do not block the specified 17/24/32 runs. Arbitrary direct C
entry-point inputs and hostile floating-environment modification are outside
the stated trusted domain. The actual review process observed FE_TONEAREST
(fegetround=0), radix 2, 53-bit mantissa and 8-byte doubles. Compiler/runtime
correctness remains an explicit computational trust assumption.

## R1 finding and author response

**R1, medium, evidence correctness:** initial check.py:19–20 loaded a fixed
local `.so` without a source/build link. Initial main:110–113 parsed one
file read and hashed a second read. The output did not pin its checker,
compiled library and numerical dependency closure. This blocked treating a
future acceptance receipt as a reproducible computer-proof record, although
it did not invalidate the frozen bounded inequalities themselves.

The author responded with a fresh per-Kernel build in a unique directory,
an arithmetic source snapshot and a pinned preprocessed translation unit;
binary/compiler/flags/header/dependency identities; pre/post build checks;
and verification of actually mapped dependency bytes. Revised main:167
takes one immutable candidate byte snapshot for both parsing and identity.
The parser rejects duplicate keys and nonfinite JSON, including exponent
overflow. The receipt identifies its Python sources and checks them and
the binary again after replay. No arithmetic kernel changed.

Independent disposition: **CLOSED** at the revised hashes above. Inspection
of build_snapshot.py:33–94 confirms the source-to-build chain and actual
loaded-library check. The targeted independent command
`python topics/padua-argmax-bridge-20261105/code/review_phase_r1.py`
verified all 450 manifest identity entries in the two distinct author R1
builds, their input pins and source snapshots, and independently exercised
five parser rejection controls plus the finite-instance guard. This was
an actual source/evidence validation, not a claim to rerun those two builds.
It preserves the normal trusted compiler/runtime assumptions.

The added local premise is separately scoped. Checker:31–54 hardpins the
**corrected** corner receipt
`573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b`
and resolves every source identity, including the historical proof prose
at c000899. Its fixed-instance test allows only n=33,64,128, phases bounded
by 1/128 and the exact n²H upper bound <=1/12500. Thus it cannot be enabled
by a caller Boolean, cannot affect n17/24/32, and does not extrapolate the
finite theorem. The old receipt `28050ad2...` and noncanonical-GMP checker
`84cbbe85...` are withdrawn and supply no premise here. This review checks
the new guard/interface; the exact energy replay remains check_rows' work.

## Executed bounded checks and full17 limitation

The actual independent initial command was
`python topics/padua-argmax-bridge-20261105/code/review_phase_math.py`, on
the initial pinned source set. It rebuilt both arithmetic libraries into
the review's own directory and used no author's output directory. Results:

- All three n17 bounded samples passed their real leaf predicates; all
  retained pending boxes and `accepted=false`.
- All ten corruption controls rejected for a substantive geometry,
  partition, constant or predicate failure, not merely incompleteness.
- Three explicitly synthetic logic controls exercised positive strictness,
  equality rejection, and capped-replay rejection. They are not mathematical
  degree evidence.
- 54 sampled producer jet points agreed with an independent 90-digit
  triangular-polynomial value/gradient sum, including collision and
  zero-crossing boxes. This is a numerical diagnostic with the recorded
  1e-80 comparison tolerance, not a proof of interval containment.
- The six N5 finite-polynomial diagnostics and exact rational constants
  passed a distinct execution at 90 digits.

The receipt records the initial script/source/binary/runtime hashes;
its historical rerun command is to be used with that pinned initial
source set, not silently relabeled as an R1 execution. Bulk output is
`local-output/argmax-bridge-20261105/phase-math-review/independent-rerun.json`
SHA `e4534d0d3475f15d383dbf63afad5e20a8c64636c5f4f233f3ad4cd490b97415`.
No full cover was run by this reviewer and no author receipt was overwritten.

Subsequently phase_checker reported its complete n17 replay against candidate
`64f7befd86658c8d9f29b05c1cb5a0162e611b726b161e737610547bed218c4b`:
1288/1288 leaves checked, 364 failed enclosure predicates (184 far and 180
corner-orbit-plus-defect), all 28 local and 32 outside leaves passed.
Its full receipt is SHA
`021ded297f360245fb30a884efe7a3670321e4a736c22873abaa6079cc0257d7`.
This is attributed execution, not this reviewer's rerun. Finite-cosine
interval overestimation can explain failure without any producer false
bound; a failed sufficient predicate proves neither acceptance nor a
counterexample. Any changed kernel intended to resolve these failures
needs a new pinned impact review and actual full replay.

## N5-02 mathematical disposition

At frozen proof SHA `51ed4849...`, equations (1)–(3) are supported by the
written analytic argument. In particular:

- PD-T185's corrected edge formula yields the two signed half-kernels
  exactly, with tau_j common to the pair and with the x exceptional mode
  fixed. Its physical weighted triangle defect is S_n(0,s)-lambda.
- For b_k in [pi/8,pi/4] and phi in [11pi/24,13pi/24], both target angles
  lie in [5pi/24,19pi/24]. The stated derivative bound makes f_r decreasing
  for 0<=r<=1/2. The square-root/half-angle rational inequalities give the
  claimed c(r)>0, without a numerical trigonometric premise.
- The open band phi-pi/8<u_j<phi+pi/8 excludes both denominator collisions.
  The denominators have opposite signs and magnitude <=2, giving pair
  defect >=c(r). All selected nodes are interior. Either endpoint parity
  has first-grid spacing 2pi/n, so the open-band count >=n/8-1 is valid,
  including exact grid endpoint coincidences. The second count >=m/8-1
  and physical weight 2/(nm) give d_n(r), with no missing factor of two.
- At n=32, (1-8/n)(1-8/m)=25/44 and these factors increase. Thus the
  two floors in proof:178–179 exceed 1/2048 and 1/512 respectively.
  The N1 error interface is |S-M|<=r_n, so it is its upper side that is
  subtracted from the actual-lambda defect. Using H_n<=n yields the
  decreasing error envelope and exact 65536-scaled bound
  7/288+112/225=33831/64800<1. The margins 31/65536 and 127/65536 follow.

This accepts the supporting finite central-strip statement in supplementary
review, retaining its separately stated N1/N5 dependencies and pending
Claude audit. It supplies no bound on max M_n, no whole-cell E-C comparison,
no degree-uniform maximum proof and no effective all-degree onset. New
N5-03 work, if any, is outside this frozen review.
