# J03 — Independent phase-certificate arithmetic and closed-cover replay

Verification record; no new mathematical novelty or global ID is claimed.
Aliases: I25, second arithmetic, from-paper referee checker.
Split from / into: none. Rules and input head:
`b45e29fa1fe3dbfa2517ff8043e5d9c440870530`.

## Statement and status

**CONDITIONAL on the explicit arithmetic model and analytic premises.**
Distinct supplementary soundness review accepted the pilot implementation and
its focused seam correction. The reviewed v2 pilot passed all eight
certificates, 31 arithmetic controls and 27 corruption controls. Full replay
accepted 942 certificates for all 471 degrees 41..511; distinct review accepted
the complete records and six separately executed arithmetic replays. The
independent Claude audit remains pending.
For each accepted certificate with integer degree 41..511, the checker constructs
new rigorous intervals for the paper's finite primitive and actual Lebesgue
function, reconstructs the complete closed midpoint partition, and proves its
strict comparisons using its own upper vertices, lower corner value and global
norm. The implication to exactly the parity-correct two nonnode maximizers
depends on the paper's positive interpolation, folding, selected-pair floor,
squared Peano and analytic corner/far lemmas. This record does not independently
prove those analytic lemmas. It removes the native numerical evaluator premises
only within the certificates actually accepted by a reviewed implementation.

The 246-line `code/independent_phase_checker/check.py` is the core checker;
`controls.py` and `run.py` supply controls, data reading and accounting. No
production evaluator, engine, row reduction, Arb, MPFR, FLINT or libm trig is
imported. The prototypes in audit-03 were read as unreviewed guidance. In
particular, their floating pi assertion and their `lo <= native upper`
comparison are not used as proof of a native upper endpoint.

## Definitions, sources and dependencies

Sources read: paper `preliminaries.tex` angular kernel; `localization-unified.tex`
cardinal reflection, primitive, finite floors and analytic branches;
`certification-unified.tex` phase, norm and squared-corner predicates. These
displayed finite formulas, rather than production code, specify this checker.
The existing approved I25 supplies the implementation scope; this is no new
ideas campaign or priority claim.

Let m=n+1 and R_k(x)=sin(kx)/sin(x), with value
k(-1)^(j(k-1)) at x=j*pi. Then, with s=(u+v)/2 and t=(v-u)/2,

    G_n(u,v)=R_(n+1)(s)R_(n+1)(t)+R_n(s)R_n(t)-cos(nu).

To derive this identity from the displayed finite angular kernel, its cosine
products are the diamond exponential sum over integer (p,q), |p|+|q|<=n.
The transformation (i,j)=(p+q,q-p) maps that diamond onto the square
max(|i|,|j|)<=n with i+j even. Its two parity classes are products of
the geometric sums with n+1 and n terms, respectively. Thus the product formula
is a finite-polynomial identity, including its removable values by continuity.
The subtracted cosine makes the highest first-coordinate coefficient one.

`S` evaluates every odd-board entry, takes its interval absolute value and
divides the summed interval by the exact integer 2nm. `actual_lambda` evaluates
all four reflected G values for every even node, adds those four signed values
before taking absolute value, and applies e_j f_k/(2nm), including endpoint
halves in both coordinates. The physical arguments are theta=pi(1-xi),
phi=pi(1-zeta). This is the cardinal-reflection formula with all endpoint
multiplicities and cancellations retained; there is no triangle-inequality
replacement for the actual lambda values.

## Arithmetic soundness

Trusted base: Python integer/Fraction arithmetic and conversions, NumPy int64
indexing/remainders after explicit overflow guards, binary64 IEEE-754 correctly
rounded round-to-nearest elementwise +,-,*,/ with gradual underflow, finite
comparisons/minimum/maximum and `nextafter` to adjacent binary64 values. NumPy
operations are separate ufunc operations; no fused Horner expression is assumed.
The OS, Python/NumPy implementation and hardware remain trusted. This is an
interval proof under that explicit computational model, not literal exact
arithmetic throughout. Runtime identities are recorded by the runner. Invalid
or nonfinite arithmetic rejects. No NumPy reduction rounding assumption is
used: summation is an explicitly widened pairwise tree.

1. Alternating rational arctangent sums at 1/5 and 1/239, each cut after 80
   terms with the next term as remainder, enclose their exact values. Machin's
   identity pi=16 atan(1/5)-4 atan(1/239) therefore gives exact Fraction endpoints
   which are rounded outwards to dyadic Fraction endpoints PLO, PHI with
   denominator 2^100. The identity follows by rational tangent addition:
   tan(4 atan(1/5)-atan(1/239))=1, with the angle in (0,4/5), hence pi/4.
   No floating pi constant is trusted. The code verifies 3<PLO<PHI<22/7.
2. All input angles are pi*num/den. Python integers first validate conservative
   bounds covering every subsequent int64 multiply, sum and parity product.
   The denominator obeys 0<den<2^52; the guarded operands stay below 2^62.
   Exact integer remainder and reflection reduce each sine to a sign times
   sin(pi*r/den), 0<=r<=den/2. r=0 returns exactly zero. Collisions in R_k
   use the exact removable value and parity, never division through zero.
3. Set u=2^-53 and p=float(PLO). Exact Fraction checks establish
   1-2u<=pi/p<=1+2u. For t=RN(p*RN(r/den)) and r>0,
   ordinary relative rounding gives |pi*r/den-t|<6u*t. Here 0<t<2;
   the denominator guard gives t>2^-52, so all nonzero Taylor products,
   including t^2 and coefficient products, are normal. The intermediate
   alternating Horner tails have the sign of their constant coefficient:
   each preceding factorial ratio is at least 6 while t^2<4. Their magnitudes
   exceed one third of that coefficient. Thus cancellation cannot invalidate
   the normal-operation error model. Zero products are exact.
4. Evaluate degree-25 Taylor sine as t times a degree-12 polynomial in
   RN(t*t), using correctly rounded coefficient floats c_j. The code checks
   |c_j-(-1)^j/(2j+1)!|<=u/(2j+1)!, and
   sum(4^j/(2j+1)!,j=0..12)<2 in exact rationals. Expanding the Horner
   expression, each monomial has at most 2*12+1 evaluation rounding factors,
   12 factors from rounding t^2, and one coefficient-conversion factor.
   With gamma_38=38u/(1-38u), its evaluation error is at most
   2*gamma_38*t<77u*t. Taylor's remainder divided by t is at most
   2^26/27!<u, checked exactly. Sine is 1-Lipschitz, so argument error adds
   less than 6u*t. The combined error is below 84u*t, strictly below the
   implemented 128u*t=t*2^-46. This last multiplication is an exact normal
   power-of-two scaling. Widening s-error and s+error by one adjacent float
   contains their exact differences/sums. Intersecting with [0,1] is valid
   because the *true reduced angle* belongs to [0,pi/2]; no monotonicity of
   sine at a rounded endpoint past pi/2 is assumed. Restoring the sign gives
   a rigorous interval for every original angle, including near half-pi.
5. Every general interval addition, product and quotient is computed by
   endpoint operations and widened by one float in each direction. This
   includes subnormal results. A denominator interval containing zero rejects.
   Absolute value uses its exact interval formula. The sum repeatedly adds
   adjacent endpoints and widens every pair, carrying an odd final endpoint
   unchanged. Induction encloses the exact sum for any array length; it does
   not rely on an unproved gamma bound for NumPy's internal sum. Endpoint
   weights are also widened, including possible subnormal endpoints. Finally
   float endpoints convert losslessly to Fractions and normalization is exact.

## Complete cover and exact predicates

The iterative preorder parser starts at the closed unit square. An `a` or `b`
split appends both closed midpoint children. Only `.` and `f` are leaves. The
stack must become empty exactly at the final token. Thus no region or shared
edge is lost. A leaf is outside only if a0+b0>1; tangencies stay. Every
numerical vertex folds by (a,b)->(1-a,1-b) if a+b>1. On the closed seam a+b=1
both partners remain in the triangle, and the same paper symmetry permits the
lexicographically smaller partner to represent both. This is value reuse,
not deletion of a closed boundary point. All W lookups and quarter-grid keys
use the same fold. Reconstructed required keys, including the 15 GRID points
modulo that symmetry, must be a subset of retained S keys. Extra retained keys
are allowed only inside the closed triangle and are all independently evaluated.
Duplicate keys reject.

GRID uses its new V_E/(1-PHI^2/64). TREE uses the maximum new V_R/(1-theta_R)
over every numerical leaf meeting the triangle, with theta_R<1. Analytic far
leaves require GRID. The new M is the integer ceiling of this rigorous bound.
No stored native norm or vertex endpoint supplies a premise.

Each leaf's q_R is the paper's bilinear vertex interpolant plus its Peano
quadratic, using new W, M and PHI^2. Exact rational halfplanes form the closed
intersection of the rectangle, triangle and either near a+b<=1/(2PLO) or
far a+b>=1/(2PHI). All intersections of boundary lines give polygon vertices.
The maximum routine checks vertices, stationary points along all vertex
segments and a possible interior stationary point. This includes each true
polygon edge. If the Hessian is singular, an interior stationary maximum has
a flat direction extending to the boundary, so an edge/vertex supplies its
value. Degenerate segment/point intersections are also included. Consequently
the finite rational maximum is an upper bound, with no numerical optimizer.

For near points, r=min(1/2,PHI*(a1+b1)) and the degree-correct finite-floor
formula is evaluated exactly; strict L+delta-max(q)>0 is required on every
nonempty near proxy. For far points strict L-max(q)>0 is required on every
nonempty far proxy. The overlap keeps the physical rho=1/2 seam. This floor
is invoked in the physical implication only on actual noncorner near points.

For ACTUAL_THREE, the exact physical point keys are reconstructed and their
actual-function intervals recomputed. Using the new lower L and those new
uppers, the paper's q and g are rationally reconstructed with PHI^4 in the
threshold; g>0 is required. The exceptional origin has coefficient exactly the
true corner value, rather than an upper interpolant. Hence the squared Peano
argument gives strict descent at every other point. Reflection gives the
other parity-correct corner. ANALYTIC_E12_256 instead requires n>=256 and exact
closed-patch/loss/dependency metadata. Every `f` requires n>=192 and
a0+b0>=1/2, retaining its entire closed triangle intersection in the analytic
far domain. Exact analytic metadata is checked. These are explicit analytic
dependencies, not independent re-proofs of their estimates.

Frozen analytic metadata still contains the historical string
`computer-assisted PD-T271`. This is a pinned certificate-schema identity,
not an insistence on retaining that numerical premise. Once adopted, the
elementary rational inequalities in [J02](J02-elementary-constant-enclosure.md)
supply the same constants used by the corner/far analytic lemmas; this does
not require altering old evidence or its metadata.

## Scope, diagnostics and open items

Successful replay proves the tree again with substituted independent bounds.
A stored native upper below the new lower, or native lower above the new
upper, rejects as a contradiction. Otherwise it reports how many new uppers
are <= native uppers, and whether the new lower is >= the native lower.
**The test new lower <= native upper validates no native upper.** When
the new upper exceeds a native upper but the new strict predicates pass, only the independently
recertified tree is claimed. Stored verification summaries are not premises.

Pilot v2 accepted both passes at 41,199,238,511 with 31 exact arithmetic and
27 corruption controls: observed exit 0, inclusive CPU 21.010049836 seconds,
wall 21.031955808 seconds, maximum RSS 144084 KiB. Output prefix outside Git:
`local-output/argmax-bridge-20261105/i25-pilot-v2-20261108T105639Z`;
outer receipt SHA256 `2de69f5d4b9e53541618630ea5c9b16222737c1eaffcf5f11ac8466ca24a961f`.
The original reviewed v2 sources are preserved at commit `4846913`.
All strict near/far/corner tests passed. The inequality new S upper <= native
upper held for 63/64 at n41 and 44/45 at each other pilot degree, for each pass; this
explicitly excludes a universal native-endpoint validation claim.

The separately preregistered full run accepted all 560 old and 382 new
certificates, exactly two witnesses for each of the 471 integer degrees
41..511. Each worker ran 31 arithmetic controls. Observed exit 0; inclusive
CPU 2519.420775278 seconds, wall 646.839168173 seconds, maximum individual
child RSS 154176 KiB. Every strict near margin exceeds 289/50000, every
numerical far margin exceeds 33/200, and each numerical corner gap g exceeds
159/5, by exact comparison of the recorded rational margins. Analytic far
leaves retain their inherited gap 3/100. The full run checked 43116 S premises
(21558 distinct function arguments) and 1290 actual-lambda premises (645
distinct arguments); exact within-degree reuse was preregistered. New uppers
prove 42174 of the stored S uppers by new-upper <= old-upper; one per
certificate is not proved by that test. All 942 stored corner lowers are
proved by old-lower <= new-lower. No native upper containment is assumed.

Full output prefix: `local-output/argmax-bridge-20261105/i25-full-v1-20261108T110409Z`.
Its full-summary.json is 5755 B, SHA256
`46944f9ae15f344bbf5d38c1cf8c2d3b20ca1e24ee4b5b708d3c2976255a7bff`;
the manifest identifies all worker input/output records. The small
[RESULTS.json](../code/independent_phase_checker/RESULTS.json) records receipt
identities and reduced exact margin bounds.
[Distinct supplementary review](../independent-checks-onset512-response.md)
accepted the full records and a separate both-pass replay at 41,458,511:
six certificates, 31 arithmetic controls, exit 0, inclusive CPU 27.276321 seconds.
Its result fields equal the campaign's fields apart from timings; this is an
executed independent rerun, not merely inspection of the first output.

Native replay by Claude is a separate result. All full outputs remain off Git. Public
archival retrieval, Zenodo DOI and the independent Claude audit remain pending.

## History

2026-11-08: Pilot v1 stopped before numerical evaluation because the original
key reconstruction omitted antipodal tie canonicalization on a+b=1. The
required aliases (1,0),(3/4,1/4) were absent; their exact symmetry partners
(0,1),(1/4,3/4) were retained. The failed run and receipt remain intact.
The proposed v2 uses the paper's existing symmetry consistently on the seam,
permits legitimate extra retained premises and evaluates every retained key.
The material correction received focused acceptance before the successful v2
run. No tree, floor, threshold or numerical formula was changed.

2026-11-08: Codex subagent development; actual serving model/effort metadata
unexposed. Root allocated Sol technical development and a distinct Astra review.
Cheap isolated arithmetic and timing controls preceded the consequential pilot;
they establish feasibility only, not a certificate proof.


## Audit-04 clarification — 2026-11-13

J3-01: the 942 witnesses represent 471 distinct trees, each recorded in a
produce and verify witness. Checking both records with a shared per-degree
cache is not two independent numerical derivations. The original run and
its frozen source/results remain unchanged. [Audit-04](../audit-04.md)
independently reran the available old-return degrees; its new-range data
checks remain pending because the canonical archives were unavailable.

E4-05: historical worker exit codes were obtained through Python's Popen
interface, which can report zero on ECHILD. They are observations from that
interface, not an independent waitpid-level proof of normal worker exits.
The completed run also required all 942 accepted rows and the exact degree/
pass population; this clarification changes no stored record or theorem.
The frozen launcher has not been rewritten or retrospectively rerun.

J3-05: the supplementary `runtime_probe.py` executes 31 arithmetic controls
and four computed runtime probes for ties-to-even, gradual underflow and
nextafter. All passed here on Python 3.12.14 / NumPy 2.3.5; this is finite
runtime evidence, not proof of the full IEEE model or a certificate rerun.
Command: `python3 -E -B topics/padua-argmax-bridge-20261105/code/independent_phase_checker/runtime_probe.py`.


### Audit-05 runtime-probe correction — 2026-11-13

E5-04 found that the earlier floating-point equality probe could report
gradual underflow even with both FTZ and DAZ enabled: DAZ also affected
its comparison. Thus the earlier four true results do not establish
absence of that combined mode. The revised supplementary runtime_probe.py
compares actual uint64 encodings for the division result and nextafter
result. Its new tests reject FTZ and FTZ|DAZ on the probed operation.
This remains finite, prospective evidence for those operations in that
process, not proof of all binary64 operations/SIMD loops, a historical
worker's mode or universal hardware/libm conformance. The frozen numerical
checker, prior run sources and historical results are unchanged. Current
code identities, independent controls and limits belong to response-05.
