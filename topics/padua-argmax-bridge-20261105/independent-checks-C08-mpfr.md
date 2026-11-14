# C08 MPFR component — independent source and bounded review

2026-11-06. Rules read at
`cc4e51210f51ff51c773dcdd458e25f934d02598`.
Codex independent component reviewer, requested Astra high; serving model
metadata unexposed. **ACCEPTED for the revised component below.**
The original source had one geometry-domain finding, now repaired and
independently rechecked. This is a source/conformance and bounded-control
review, not a full producer/candidate run or the separate formal Claude
audit. Historical novelty is excluded: this is an internal implementation
of accepted C01/C03 mathematics, with no external priority claim.

## Reviewed identities and scope

- Final `code/cheap_C08_mpfr/producer.c`:6341 bytes, SHA256
  `270eb7b0f073efcb996c7c832f6e946d37b0e6f780fdac63fc66591332560a5e`.
- Unchanged `c08_interval.h`:6575 bytes, SHA256
  `275936b502180f2d92af94eb2138815114ba75afb9c258cadffa44e580be0a03`.
- Builder `build.py`:3463 bytes, SHA256
  `fff281f0c765025ec182937aff38398e7eedfd11b66bfeb36f105734b730d81f`.
- First reviewed producer:6318 bytes, SHA256
  `bf32c04994abf53cda5aca1cc63ceb2778d6339565a8cbc7c6337d9af22dc87d`.
  Its original independent control and finding remain preserved.

I read the entire producer/header and builder, not only the C03 additions.
The transitive mathematical/source comparison includes the full inherited
C02 MPFR producer/header, source hashes `3c5240cc991162fd0b859a7de81a9f37d7d44107ebe8ec315899c0761f0feb04`
and `e9841471f2372cc93dd6d97b79332c0501514008623f1ffa4a24c913ecf5d6df`.
Those historical controls were not treated as independent source acceptance.
C02 is a source ancestor, not a dynamically imported arithmetic dependency.
The new compiled arithmetic includes only the frozen C08 source/header and
recorded system/MPFR/GMP headers and libraries.

Mathematical dependencies reviewed here are C01 ratio enclosures, the
accepted C03 ratio tightness proof SHA256
`8634fc469f18a9555032c140b9969a56a74c53dea388cadd54c29ed2b3e83a01`,
the C01 allclass defect theorem, and N3's full-board projected-defect
normalization/reduction. No C02 stronger floor or C03 centered/ODE variant
is used. The adopted native degree range is2..512 and ratio range1..513.
These finite implementation ranges do not extend any external certificate
theorem's accepted degree range.

## Directed arithmetic and trigonometric enclosure

Intervals store **binary64 endpoints**, not arbitrary-precision MPFR
endpoints. Each finite stored endpoint is an exact dyadic real. Elementary
add/subtract/multiply/reciprocal operations expand toward the relevant
infinity with `nextafter`; multiplication examines all four endpoint
products. This encloses the exact endpoint operations under the declared
IEEE arithmetic assumptions, including underflow. Division refuses a
denominator spanning zero. `square` uses the exact min/max absolute
endpoints and returns lower0 when zero is included.

Transcendental endpoint values are computed by MPFR128 with downward or
upward rounding, followed by conversion to binary64 in the same direction.
Input binary64 conversion to MPFR128 is exact. Pi is enclosed using
separately directed MPFR constants. Factorials/reciprocals and Taylor
remainders use MPFR256 in the correct directions: an upward factorial
serves the reciprocal lower bound, a downward factorial its upper bound.

For a valid interval of width less than6.28 and maximum absolute value at
most1e6, `trig` evaluates both endpoints and includes every intersecting
critical point `(j+offset)*Pi` in the seven-index search. The nearest
integer proposal about the midpoint is within one half plus negligible
binary64/pi-proposal error of its intended index; any true critical point
is less than approximately one further index from the midpoint because
the interval width is below2*pi. The three-index margin on each side is
ample throughout the literal1e6 bound. Critical-point intervals are
outward, so uncertain intersections conservatively insert an extremum.
Negative odd integer remainders correctly select the negative extremum.
Wide, large or invalid trig arguments return[-1,1], never an unproved
endpoint-only range.

The frozen build uses the declared non-fast-math C11 flags, the captured
x86_64 compiler/toolchain and ordinary IEEE operations. Default rounding
and sequential native calls are part of the implementation contract;
static MPFR workspaces/counters do not support concurrent native calls.
A read-only environment check returned `fegetround()==0`. Numerical
trust remains in MPFR/GMP, compiler, Python/hardware and the captured
runtime. High-precision finite sums below are diagnostics, not exact
proof substitutes.

## Complete ratio path and endpoint refinement

`base_pair` checks finite ordered input and k1..513 before the exact R1
shortcut. The initial value cap[-k,k] and derivative cap
[-floor(k*k/2),floor(k*k/2)] are finite exact integers in this range.
The separated-denominator quotient and its uncancelled derivative are
computed outward. Value/derivative are staged together: nonfinite
optional pairs are ignored, finite disjoint intersections flag failure,
and neither can silently replace a valid pair with a malformed bound.

The pole branch uses a bounded midpoint solely to propose an integer
turn. `lround` is safe after |midpoint|<=100; the selected exact integer
need not be the nearest mathematical turn for the identity to hold.
Residual `Z-turn*Pi` and its k-multiple are outward. Literal guards
|r|<=1.5 and |kr|<=4 precede all use of the fixed J32 sinc polynomial.
Coefficient signs, derivative Horner indices, and remainders
4^66/67! and66*4^65/67! agree with the accepted proof. The integral
caps |sinc|<=1, |sinc'|<=1/2 and sinc(r)>=5/8 provide valid intersections
and a positive divisor. Exact parity uses odd turn/even k, including
negative turns, without an overflow-prone parity product.

`fixed_pair` performs outer endpoint refinement even when the base quotient
succeeded. The actual binary64 absolute endpoints of the outward residual
give exact folded l,u; no inward cast occurs. The test uses u<=1.5 and the
**outward upper** of k*u<=4. Endpoint values use nonrecursive `base_pair`
calls; F(0)=k is exact. The image `[lower(F(u)),upper(F(l))]`, parity
reversal, and one-sided derivative clipping match C03 on both sides of
the first numerator zero. Guard rejection retains valid base bounds.
It is expected that an ideal exact4/k endpoint can be rejected after
outward construction. No source path invokes a k-term harmonic sum.

## Kernel, phase gradients and full-board collection

The primitive is

    G(u,v)=R_(n+1)((u+v)/2)R_(n+1)((u-v)/2)
          +R_n((u+v)/2)R_n((u-v)/2)-cos(nu).

The two product-rule combinations `ds,dt` give the first-coordinate
phase derivative `((ds+dt)/2+n*sin(nu))/n` and the second-coordinate
phase derivative `(ds-dt)/(2*(n+1))`. Thus the exceptional cosine term
and both phase normalizations are retained, including collisions.
The center evaluation uses the same primitive. A rounded binary64 center
inside the input box is a valid mean-value center; outward radii bound
the distances to both endpoints. At an absolute-value sign crossing,
`adabs` encloses the possible signed derivatives by their symmetric cap.
Adding these intervals encloses the gradient of the whole sum. Taking
the minimum of the natural sum and centered mean-value upper bounds is
valid because each independently bounds that same sum.

The odd board contains exactly2N entries, N=n(n+1), with positive total
normalization2N. Four periodic reflection values form each corner-orbit
sum and are divided by8N. Endpoint multiplicities are retained by the
full periodic board. Reflection preserves parity and never flips the
phase offsets. Integer indices, normalizers and allocation-size products
are safe for n<=512.

The lazy branch returns `C_upper=S_upper`, defect0, only after comparing
its S upper with downward(lc-eps). Triangle inequality makes C<=S
independently of the caller's threshold. A future producer must still
provide its independently computed Lc bound and correct acceptance
predicates. The n>=64 analytic branch requires the full input rectangle's
radius<=1/2, checked with exact dyadic conversion and an outward MPFR sum.
Its1/2048 is for admissible **noncorner** classes, never the true corners.
The orbit/local predicate for corners remains necessary externally.

Otherwise the implementation retains every horizontal/vertical projected
profile. `pairlower` is downward2*min(abs endpoints) only for rigorously
opposite signs, and0 otherwise. Downward accumulation/division by4N is
valid even if rounding makes an otherwise zero lower sum slightly negative.
The final max with0 is safe. All potentially physical odd centers survive
outward endpoint tests, and actual corner index pairs are excluded.
The minimum over centers of the larger projected lower bound is therefore
uniformly valid. If none survive, nonfinite output fails instead of
inventing a positive finite conclusion. The inherited comment calling
these intervals “only diagnostics” is stale wording: the returned profile
lower bound is mathematically justified producer output under this review.

## Geometry finding, author repair and focused disposition

The original `n3_geometry` accepted arbitrary finite ordered endpoints
but estimated a whole-box sine-square radius from the largest absolute
endpoint without constraining the monotone range. The exact executed
binary64 input

    n=2, [-25.132741228718345,25.132741228718345] x [0,0]

returned2 (local). This is an invalid local classification for that broad
box. Original candidate roots are bounded by pi_hi and do not reach the
example; nevertheless the native API itself lacked its necessary guard.
The finding was sent before any author edit and is retained in the first
independent receipt. Unrestricted geometry was not approved.

The author inserted exact endpoint maxima and `if(aa>4||bb>4)return 3`
before geometry classification, moving the existing maxima declaration.
An independent literal function comparison confirms that this is the
only source change; the entire ratio/header/box/constants code is unchanged.
For n>=2, admitted absolute alpha/(2n)<=1<pi/2 and
absolute beta/(2(n+1))<=2/3<pi/2. Hence sine-square increases on the
whole admitted coordinate range. The endpoint values now rigorously
bound the whole-box radius. The exact guard admits all original
pi_hi<4 roots, while rejecting equality+oneULP and the counterexample.
Outside classification and the original local-radius thresholds remain
unchanged within the accepted domain.

Independent focused controls PASS50 assertions over25 geometry cases:
the original counterexample now returns3; boundary4 is admitted; oneULP
beyond4 is rejected in either coordinate; all original root quadrants
at n2,32,512 are unchanged; zero/small local boxes, an outside point,
reversed/nonfinite endpoints and invalid degrees behave as specified.
No ratio or saved-box evaluations were repeated after this local repair.
The finding is **resolved** for the final source identity above.

## Independent executed controls and provenance

Actual commands:

```text
python topics/padua-argmax-bridge-20261105/code/cheap_c08_review/control.py
python topics/padua-argmax-bridge-20261105/code/cheap_c08_review/geometry.py
```

The first fresh build/control returned exit0,
`PASS_WITH_DOMAIN_FINDING`:382 assertions,38 ratio cases,4 kernel/phase
gradient cases, and8 box cases. The ratios include both signed turns,
crossed poles, exact R1, invalid inputs, high k513, genuinely straddling
numerator-zero intervals verified against high-precision pi, positive
and negative residuals on the negative lobe, chart rejection, shifted
charts and global caps. Each scalar/gradient reference is a separate
85-digit finite harmonic calculation used only in review code.

Two independently evaluated small n2/n3 point boards check full S/orbit
normalization and both projected-defect orientations against separately
summed reflected values. Six saved n32 inputs reproduce every published
MPFR bound exactly and each relevant strict predicate passes an explicit
`Fraction` assertion. The first five pass S<Lc; the near box passes
S-defect<Lc with S=11.320627362850086 and defect=.4182930441744107.
The independently recomputed Lc interval is
[10.993594541097181,10.993594541103743]. Exact-half-radius and oneULP
outward guards are also checked. These are selected cases, not a cover.

The developer's primary matrix alone did not exercise its promised
numerator-zero/negative-lobe intervals; the later edge receipts do.
The first edge failure is correctly preserved as an incorrect rejection
expectation for R3 on[2,2.1], which admits a chart about pi. Its preceding
negative-lobe tests passed; the next receipt checks the corrected shifted
chart and genuinely rejected[1.4,1.5]. There is no basis to relabel the
first receipt PASS. Also, the developer's primary driver records its six
strict booleans without asserting them; the saved booleans are all true,
and this review explicitly asserts all six. Reported coverage is38 own
ratio cases plus the stated developer matrices, not a fabricated combined
count of distinct mathematical cases.

Each independent build captured source/header snapshots, preprocessed TU,
binary, builder and commands,4 tool identities,13 tool-runtime entries,
42 headers,5 linked-runtime entries and actual loaded mappings. The
original run captured13 actual mappings; the focused run captures both
old/new libraries for its comparison. All captured native/source/input
identities and actual mapping sets stayed unchanged through each run.
The first control was finished before the author source edit. The final
guard control separately freezes the revised source. The numerical
diagnostic mpmath calculations are not part of the production arithmetic
dependency graph or the accepted exact proof.

Original full supervised CPU was4.645847918s, including build descendants
and supervisor, with no55s watchdog trigger. The focused follow-up records
.293119604s own plus.568518s child CPU; its sampling precedes final receipt
serialization, so their sum is not advertised as exact whole-process CPU.
Both bounded jobs are comfortably within the shared60s review budget.
No full producer, candidate traversal, new candidate or new degree ran.

## Cost and artifact freeze

One outer ratio pair calls at most three fixed-work base pairs, each with
at most four scalar trig interval calls. There are exactly16N outer pairs
per box, plus6N correction trig calls: at most198N scalar trig calls,
each with at most four directed MPFR endpoint evaluations and a fixed
seven-extrema check. Constants separately cost at most98N scalar trig
calls. Polynomial work is fixed J32. The projected profile fallback still
has cubic board-pair work; no practical large-degree throughput or full
producer acceptance follows from this component review.

Preserved essential first receipt `evidence/c08-review-mpfr.json`,2153 bytes,
SHA256 `33ea73039d6ad7c3ea44cc2281e734995e0a933875af4b5582e5d8ad33dab275`.
Its42527-byte raw manifest is `/tmp/c08-independent-review-n9ks1as2/raw.json`,
SHA256 `f95d15500dd107481fd2bb687c72a01ed465c9a2b39898cc3a1b1df9f93e3b62`.
First control SHA256
`1debd24f60b8b01f4cff383bfce47030cf33dc86c24df4aca1257f831b6361fd`.

Focused receipt `evidence/c08-review-mpfr-geometry.json`,1083 bytes,
SHA256 `8fcf1f963b31fdf25b029064f0d634df63cd6be490bf7026fbf4665dae2e3be2`.
Its23456-byte raw manifest is `/tmp/c08-geometry-review-mucq1qqy.json`,
SHA256 `513e23c94b64b25903ef119c82aa7678d90ab51261e1aba738adef02525cbe40`.
Focused control SHA256
`f84194075ee8838f297b6ec7b4ae51122ce78f03a9f4d702b8ddd2d5e69de4b6`.
Large build/runtime artifacts remain local; physical archive transfer is
pending. Future consequential use still needs its own frozen controller,
publication/release, and complete-run evidence. This acceptance supplies
the reviewed numerical component only.
