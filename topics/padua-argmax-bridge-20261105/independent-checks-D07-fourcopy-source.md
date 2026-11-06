# Supplementary source check — D07 actual four-copy point prototype

Rules/read input `084a64f6465956f9c75b5538f83752c30318f151`, unchanged
at observed source input `2e4ac49fa0687a7736bc1df82c12e6483b1c7a94`.
Distinct reviewer `/root/d01_far_review`, parent-requested Astra xhigh;
serving metadata unexposed. Formal Claude audit remains separate.

**Final focused verdict: ACCEPTED for the stated pre-execution source
contract. F1 and F2 are closed; no unresolved finding.** Final pins and
the correction check appear at the end. Execution still requires the
parent's separate release; no numerical/performance result is asserted.

## Initial verdict and exact scope

**Execution clearance withheld pending the two controller findings below.**
The complete mathematical point/root/reference source pass found no
enclosure defect. This is a pre-execution source review, not a numerical
validation or a release to run. Any source/freeze change requires the
focused recheck recorded below before acceptance.

The scope is the D07 point API for LP64 n=2..2048, rational inward turns
in [0,1], its independent n<=128 reference, exact fixed CASES inputs,
fresh builder, runtime provenance and bounded one-shot controller. No
whole-box bound, runtime theorem, useful enclosure width, certified degree
or global argmax statement is reviewed or inferred.

## Findings sent before fixes

**F1 — MAJOR, final aggregate CPU accounting after a group kill.**
In the original controller, `group_cpu` observes all active process-group
members, but the final accounting at lines 147–154 only uses the
supervisor's `RUSAGE_SELF` plus `RUSAGE_CHILDREN`. If a compiler child or
grandchild is still active when the worker's whole group is killed, the
worker can die before reaping it. Its usage is then not necessarily
included in the worker usage collected by the supervisor. The final
record can consequently understate actual helper-inclusive CPU, despite
the earlier live guard having observed it. This affects the stated
resource/provenance contract, not the numerical formula. Required
disposition: preserve a valid complete accounting mechanism on kill
paths, for example supervisor subreaper adoption plus reaping all
descendants, and distinguish any merely observed lower bound from a
complete final total. A stale live snapshot alone is not an exact final
CPU receipt. No numerical execution is necessary to make this fix.

**F2 — MINOR, completed slow case remains listed as pending.**
The original `call()` appends a completed record and raises `CostStop`
when its measured CPU exceeds 20 seconds. This happens before the outer
case loop removes that item from `pending` or stores it in `point_results`.
The durable checkpoint therefore records the same case as both completed
and pending; no final worker summary is written on that exit path.
Required disposition: commit completion to the case ledger before
enforcing the completed-call stop, with no subsequent native call.
This is a record-consistency finding and does not change the frozen cases.

Both findings were sent to the parent before any requested fix; F1 was
also sent to the developer for coordination. The reviewer has not edited
author source or the freeze manifest.

## Frozen initial inputs

All assigned SHA-256 identities matched the files read:

| File in code/post_audit_D07_fourcopy_point | SHA-256 |
| --- | --- |
| point.cpp | `03dc79bbbc7563ba9066137c0a52467624c810a758f865f9931511c82985ff6f` |
| controls.cpp | `5db13088e9fff85a134c95851337750ca03ea62be2f5d3ecf07e1f6e7d49c3fa` |
| controller.py | `fd561ea714812a70abc4bb2bdc6d3c9fce196be3180e412740c69947483aeb5d` |
| SPEC.md | `5ce1efbde7dd816d6e842cf54b61066b6a3df5df5c616f35bdee097f111fbd22` |
| FREEZE.json | `dbd9166b1022a0055238d8bea3e94732bfdf401c4a76c08ac1dd6e0f293a8f97` |

The initial manifest pins CASES.json, SOURCES.json and build.py, plus
unchanged C11 point/partial and root-header ancestors. Prose hashes are
passive audit provenance and are not enforced by the runtime checker.
The mathematical D06 source remains
`8eb7d781e91c52aaca80f160a24f5198a758b7c99fc397bbba3fd6178e7ca824`.

## Mathematical and native source reconstruction

The accepted D06 review is
[independent-checks-D06-four-copy-rows.md](independent-checks-D06-four-copy-rows.md).
The new point.cpp, controls.cpp and complete inherited C11 point.cpp and
partial.cpp were read line by line; the installed declarations for root
finding, Taylor shift, exact complex midpoints and Chebyshev functions
were checked against the calls. The complete C11 source review and
C02's partial-sum hypotheses/error construction were also read/refreshed.

**Actual values and weights.** `g7` evaluates the finite rhombus using
two entire sine-ratio products and subtracts cos(nu). Rational-turn
reduction and exact quarter-turn sine/cosine values preserve this mode.
`four7` combines all sigma,tau copies before `absolute` is applied.
Both direct and ordinary row paths use j+r odd, retain half weights at
j=0,n, apply the separate row endpoint half weights, and normalize by
2n(n+1). The API's xi,zeta are inward pi turns, matching the reflected
physical point in D06. None of these calls evaluates a removable
rational alias in place of the actual polynomial.

The exact mesh-node test n*xi=J, m*zeta=R, J+R odd is the reflected
original even-node condition and safely returns one. The xi=zeta=0
shortcut is the accepted nonnode corner S0 identity. These branches are
separately counted, not relabeled as successful ordinary root rows.

**Coefficient families and exact axes.** The implemented quadratic
denominators and affine paired numerators match D06, including epsilon,
both signs of E and every factor of two. Ball operations enclose the
complete actual coefficient vector. For exact zeta=0, the tau copies
coincide and the alias is 2ell/d. For exact xi=0, b=E=0, a=A=1,
so the sigma pairs give 2k_tau/(c-y_tau); the stated affine/quadratic
sum is correct. Original denominator events are retained after both
reductions, so canceled factors cannot conceal an actual collision.

**Root certification is independent of the Acb candidate guarantee.**
Only exactly zero leading coefficients are removed. Any remaining
uncertain leading coefficient triggers fallback. With degree d>=1,
each proposed center is replaced by its exact dyadic complex midpoint.
Taylor shifting the full ball-coefficient polynomial encloses every
Taylor coefficient of every member of that family at that same center.
The code requires strictly

    lower(|p1|)*r > upper(|p0|)+sum(j>=2) upper(|pj|)*r^j,
    r=2^-60.

For each member, its linear term has one zero in the disk and dominates
the remaining Taylor terms on the boundary. Rouche's theorem therefore
gives exactly one zero there, counting multiplicity. Pairwise strict
center separation greater than 2r makes the d disks disjoint. A leading
coefficient excluding zero fixes the degree for the complete family,
so these d disks cover all roots, not just roots of a midpoint
polynomial. The unused return count of `acb_poly_find_roots` is thus
irrelevant to certification: it supplies candidates only. Any failed
disk/count/separation certification throws to complete-row fallback.

The real and imaginary projections are enlarged by r. A disk is
discarded as nonreal only when its imaginary projection excludes zero;
its real projection is discarded only when strictly outside [-1,1].
Clamping exact outward endpoints before separately evaluating acos avoids
an interval overhang outside its domain. The decreasing acos orientation
is handled by an enclosing union before mapping to the parity index.
An exactly zero numerator yields zero on all regular samples; uncertain
constant sign still triggers fallback. Multiple roots need not succeed.

**Original poles, buffers and sign blocks.** The exact rational fold of
xi+/-eta_tau gives every original denominator event in t/pi. All root
and pole intervals are mapped to the same k coordinate. Buffering
floor(lower)-1 through ceil(upper)+1, clipping to valid parity indices,
and inserting both cuts around each direct index leaves contiguous
ordinary blocks. Admitted physical endpoints are also direct. The
bounded n and clamped root/pole domains keep these integer conversions
within signed-long range; a wide event or buffer size over 40 falls back.

Before using any ordinary block, every event interval must be strictly
outside the full span of its sample indices. A certified strict sign of
U/W at its first sample then extends throughout that continuous span
by complete root and pole coverage. Repeated roots, canceled poles and
roots exactly at grid points are conservatively handled by buffering.
No off-grid equality between the true cardinal polynomial and the
rational alias is assumed: only the signs and grid identity are used.

**Partial-sum offsets and all errors.** Channel 0 uses (w-eta)/2 with
coefficient epsilon E/2-k/(2sin eta); channel 1 uses (w+eta)/2 with the
plus coefficient. Both sigma directions and both tau values are retained.
For sigma=-1, starting at the largest j reverses the block and gives the
same positive mesh increment pi/n. The exact rational floor fixes the
cotangent period; the first-offset and final-distance guards in C11's
`partial()` certify all samples strictly between its poles. A block
crossing a pole cannot pass those guards.

The entire returned partial ball is multiplied by the entire new
coefficient ball and accumulated. This retains the CP640 coefficient
and moment construction, J16 smooth remainder, K32/L16 harmonic tails,
WD96 derivative remainder, input-radius charge and all subsequent Arb
rounding. No C11 all-row coefficient budget is imported. The underlying
C02 theorem applies on the whole strict interval (0,pi); no uncounted
midpoint subdivision is needed. Large new channel coefficients may give
wide enclosures; that is reported uncertainty, not an omitted error.

**Fallbacks and bounded API arithmetic.** Exact integer eta rows use
complete finite rows; D06 bounds their number by two at any fixed point.
Every caught candidate failure discards the attempted row total and
recomputes the complete actual row, preserving endpoint weights. Earlier
direct/partial attempts remain in work counters. Numerical fallbacks can
occur on arbitrarily many rows, so quadratic work is explicitly possible.
Direct nonfinite values propagate failure if recomputation cannot recover.
All loops/products/counters are safe on the admitted n<=2048 LP64 range.
Rational parsing checks length, parse status, denominator and closed
domain before use. Final lower/upper binary64 endpoints use directed
rounding and reject nonfinite exports; production failure returns NaNs.

## Independent controls and execution contract

The controls use 512-bit cosines and Chebyshev divided differences, with
P'_n=n U_(n-1)+(n+1)U_n at exact rational-angle collisions. Their
collision predicate checks u-v or u+v in 2Z exactly. This is independent
of the production sine-ratio, rational-row, root and partial-sum paths.
The reference combines four copies before the absolute value and applies
the same physical endpoint factors and 1/(2nm) normalization. It is
limited to n<=128 and is never used as a production fallback.

The controller checks complete reference-ball containment, not merely
overlap. The exact node value may instead be contained by its reference
ball and is checked as the exact exported interval [1,1]. CASES.json
matches the specified generic/node/corner cases at n=2,17,32, one generic
n=128 reference, and three n=512 point-only cases. The following n=512
common-S call is explicitly context, not an actual-lambda reference.
Invalid degree/domain/parse controls are fixed. No additional degree,
precision rescue, adaptive case or whole-board large reference is hidden.

The builder creates a unique local build directory, snapshots and hashes
the preprocessed translation unit, captures compiler/header/library
closures, compiles that snapshot, and checks its source/toolchain
identities. The worker checks frozen executable/data inputs and ancestors
before work and at exit, verifies the registered controller/freeze
identity, uses exclusive worker-entry creation, checks LP64/binary64,
records actual loaded dependencies and checks them after completion.
Direct stdout/stderr files avoid a blocked pipe. Atomic checkpoints
preserve complete prior calls, raw native output representations and
first exceptions. Prose hashes are not an execution dependency.

The intended CPU controls are 180 seconds aggregate, safety stop 170,
worker hard limit 175, reserve before another case at 160, completed-call
stop at 20 and unfinished-call kill at 25 process-group CPU seconds,
with wall cap 360. Native calls remain serial. The two findings concern
the killed-descendant final total and the completed-call ledger; the
ordinary live process-group guard, fixed cases and no-retry behavior
are otherwise consistent with the contract.

## Novelty and review execution

This is implementation of the accepted D06 structure and C11 backend,
without a new historical-novelty claim. The complete D07 idea, attempt
and SPEC were read. The full unchanged registry reading and relevant
PD-T101/185/228, C02/N5, PD-N085 and N6 source comparisons are documented
in the D06 review and reused explicitly. Current state/IDEAS.md retains
SHA-256 `68bf789c82967944421e6fc54f8164dbdb91d1096fa10694008261fbd54f9e9d`.
The new Rouche family-coverage argument was reconstructed here rather
than inherited from the root-finding API or the structural D06 theorem.

Initial review tools only read/searched files, inspected headers, checked
hashes/read-only diffs and written this report. No native build, library
load, root solve, numerical diagnostic, board/reference evaluation,
quadrature or replay has run. No scientific CPU or performance result
is claimed. The optional <=10 CPU-second pure structural-helper allowance
was not used in that initial pass. The author's preparation syntax CPU is historical
reported evidence, not an independently executed test by this reviewer.

## Focused correction review

**F1 and F2 CLOSED; final source contract ACCEPTED.** The original
unexecuted candidate is preserved at
`cbfdb044e184731984e3bf8be487008a86e68c37`. The complete focused diff
against it was read. Final SHA-256 pins:

| File | SHA-256 |
| --- | --- |
| controller.py | `af8d357badba85786fec088c735cc988f0950587d112e2e63a8d5b39cc14a9a5` |
| SPEC.md | `98dd88fa9a61441c486a54611e6afa59463feb2d91c6aca4584c8f3b96c62c87` |
| SOURCES.json | `f81f9d2640d6e7cde012d06201e9b22d719086b84bf3381352fbbe8152fe5c2a` |
| FREEZE.json | `c8b8e49e5c5af5ff520f00f8b7bac655a6c31cc132a5cb06cd87397c36fa33fb` |

All eleven final executable/data and ancestor identities matched.
Point.cpp and controls.cpp retain the initial hashes above.

F1: Linux subreaper setup is verified before launching the worker.
After waiting that worker, the supervisor kills its residual group and
wait4-reaps adopted subtrees until there are no children. This preserves
their CPU in RUSAGE_CHILDREN without double counting usage already
reaped by a descendant. An incomplete cleanup is explicitly labeled a
lower bound and cannot produce a completed result. Per-adoptee records
are retained. Final samples still precede their own tiny serialization,
which is stated honestly.

F2: `commit_call` updates completed_calls, point_results and pending
together before the atomic checkpoint and completed-call CostStop.
Node validation occurs before completion. The combined native
point/reference API is explicitly indivisible in the active-call record;
no unavailable intermediate point output is claimed after a kill.

Independent command, preregistered before execution:

    python topics/padua-argmax-bridge-20261105/code/post_audit_D07_fourcopy_review/negative_controls.py

**PASS**, nine Python-only failure/flow checks, 0.031124 total CPU seconds,
below the 10-second cap. AST-selected frozen functions were checked with
stubbed platform/prctl/reaping failures, complete/incomplete reap paths,
ledger mismatch, the actual nested slow-call branch and failed-reference
branch. No native library, compiler, subprocess or research computation
was invoked. The author's separate live fake-grandchild test was read,
not independently rerun; it reports two adopted helpers in 0.337978 CPU.

Reviewer helper SHA-256:
`d868850b798e9eda1ba877ac07803a9c842d077e65dd5dd28499b99f8981bb5f`.
[Independent receipt](evidence/d07-review-source.json), 872 bytes, SHA-256
`991edaa4bcf697dea176b724bf8772c4a5e7333628b5f562e8c41d9f80783643`.
Only this report and the disjoint reviewer helper/receipt were written;
author fixes remain attributable to the author. No Git/shared mutation.
