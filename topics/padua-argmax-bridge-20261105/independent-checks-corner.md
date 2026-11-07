# Independent supplement — practical corner bounds, N6 round 2, N1 round 2

2026-11-05. Distinct Codex checker `/root/check_rows`, assigned gpt-6-astra
high by the coordinator under handoff01. Serving model/effort are not
independently exposed. Rules read at
`3dda890275a7599caa707b0fb8c0b6e6f6a80643`. Only assigned independent
report/code/evidence files were written. No developer/shared/Git edits.
The published `independent-checks-rows.md` remains unchanged.
This is supplementary review, not the required Claude audit.

## Disposition

**PASS after corrected actual replay**: the analytic corner reduction and independent exact
finite replay at n=33,64,128 support the claimed common local radius
`H<=1/(12500 n^2)` and symmetric scaled phase box radius `1/128`.
All four producer corner/energy endpoints at each degree are verified,
not merely numerically close. No full-degree/global certificate follows.

**PASS at scoped hypotheses**: N6's full-vector trace-support application
and scalar-equivalence disposition; N1 round2's cancellation-variation,
shifted-grid and weighted-row error theorem. The unrestricted scalar
comparison, compact all-degree profile, effective onset and B3 remain OPEN.

Minor notation finding **C1**, N1-cancellation-quadrature.md Statement(4):
`rho` is used without a local definition. The established convention
`rho=|alpha|+|beta|` (margin-anatomy and PD-T217) makes the displayed
inequality correct. State that definition explicitly at the next author
revision. This is not an analytic blocker; the reviewed claim uses that
convention. No mathematical formula or developer file was fixed here.

## Checker-contract correction C2 and replacement replay

The coordinator found a substantive defect in the initial independent
checker before publication/use: `Q two_w(4,Z(n)*m)` was followed by
`two_w/=2` before canonicalization. For n33 the constructed 4/1122 is
not reduced. GMP requires canonical rational operands for arithmetic;
canonicalizing later inside `I::rat` does not establish that contract.
The checker author had noticed the construction but incorrectly dismissed
its contract consequence. The initial corner PASS was withdrawn.

Only checker-owned code changed: `two_w.canonicalize()` now immediately
follows construction and precedes either endpoint division. The entire
list of two-argument `Q` constructors was audited:

- `lo` and `hi` canonicalize immediately before returning a rational.
- Angle fractions, cosine remainder, endpoint gradients and the n-squared
  gradient factors pass immediately to `I::rat`, which canonicalizes its
  argument before any rational or interval arithmetic.
- Arctangent summands/tail, Taylor recurrence factors, initial mass and
  threshold/phase constants have numerator one and positive denominator.
- The remaining phase factor n-squared/(n+1)-squared is reduced because
  consecutive integers are coprime. Its denominator is positive.
- `two_w` now canonicalizes immediately; its subsequent exact arithmetic
  starts with a canonical operand. Single-integer constructors are canonical.

The initial source, collector, report, receipt, executable and all four
outputs are preserved with a hash manifest under
`local-output/argmax-bridge-20261105/check-corner/initial-withdrawn/`.
The withdrawn source SHA-256 is
`84cbbe858b52711c99713b05f6b538eb352efb73aa41c2c1eac715288362bfa6`;
the withdrawn receipt is
`28050ad27ecccb011faf0df4958744041e3843e3cd1581ca921b830e1504983f`.
Those artifacts are historical evidence, not the basis of this PASS.

The corrected source was actually rebuilt and executed separately for
n2,33,64,128 between 2026-11-05 21:25:32 and 21:25:34 UTC. The mandatory
`--run` collector reran the exact n2 coefficient control and every
per-degree predicate, checked frozen producer pins before and after, and
compared all four new raw outputs against the preserved initial outputs.
Every raw output is byte-identical; this is an observed replay result,
not an inference that violating GMP's contract was harmless. The new
receipt supplies execution commands/times, compiler, Python, platform,
linked libraries and GMP runtime version6.3.0, with old hashes explicitly
superseded. Scoped PASS is restored solely on the corrected execution.

Corrected source SHA-256:
`3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3`.
Collector SHA-256:
`59e6aeec23433c877b99ec86aee71eaa03b514697dcd0ba1df711dc0f643dfe4`.
Replacement receipt SHA-256:
`573afc5d5ae229b0fa1d47df9b6bf334e47e0e437288a3543826838e5403cb4b`.
The N6 and N1 analytic reconstructions below do not depend on this checker.

## Frozen inputs

| Path below this topic | SHA-256 |
|---|---|
| theory/N3-corner-radius-reduction.md | `8cf89c491a4d82df81a69bd1024139d1224bd1f43fd91b1d1fe58a1dd519aee4` |
| theory/N3-corner-bounds.md | `7241cd4221643473cf34c9a36e502d1095a916a0b2f67075d2fb4093d2142fe6` |
| evidence/n3-corner-bounds.json | `fe843711ff66e4a89f7856fc952441537a69d2907a5c78a6a844d61fec3e9c46` |
| code/n3_corner_bounds.c | `a0497ca1219850e28f2bf51e72cb4fc8f78cde238b81fd678262d646511402bd` |
| theory/N6-trace-mixture-application.md | `f7b52cd59d56f7a666168ad7cce1b510d5ee63ff8fefb8fe0cfb23c434dd6c52` |
| theory/N6-round2-disposition.md | `e85ec4af2108504dcf7fa379132c64fce17a67abb0b64c2ec2d8428abc4d9598` |
| theory/N1-cancellation-quadrature.md | `5be3cca27524eea360668386636388dd109e85165b4c87fcaeb8769953e9052a` |

These hashes were checked after execution/reconstruction. The producer's
pending status is its frozen publication state; this supplement supplies
the distinct replay without editing or silently upgrading that record.

## Corner analytic reduction

Read PD-T227 and PD-T251 in full. With `z=n^2 H`, the exact aggregate
Taylor inequality, including initially zero cardinal slopes, gives

    lambda(c+h)/Lambda_c <= 1-z/8+(b/2)z^2+K(exp(z)-1-z).

The assumed bounds imply `W<=b n^4 Lambda_c` and `Lambda_n<=K Lambda_c`.
For z<=1, the exponential remainder is at most `e z^2/2<3z^2/2`.
Consequently `z<=1/[8(b+3K)]` makes the total positive remainder at
most z/16. The strict decrease is exactly `Lambda_c z/16` for H>0.
The min with1 correctly imposes the exponential estimate's domain.
No affine or true cardinal-sign preservation is required.

The metric is the physical inward L1 distance `H=h_x+h_y`. The other
nonnode corner is covered by the node-preserving x reflection for even
n and y reflection for odd n; values and squared gradient energy are
permuted unchanged. There `h` means inward coordinates after reflection,
not two globally positive Cartesian increments at a positive endpoint.

The scaled chart satisfies
`n^2 H<=alpha^2/2+[n^2/(n+1)^2]beta^2/2`. Thus the symmetric phase box
r=1/128 needs only `r^2[1+n^2/(n+1)^2]/2<=1/12500`.
In fact the left side is less than1/16384 for every n, so the implication
is immediate and was also checked by exact rational arithmetic per degree.
The optional global majorant u is valid by PD-T368 and
`log(n+1)<=log2(n+1)<=ceil(log2(n+1))`; its integer ceiling is verified
without floating logs.

## Independent exact arithmetic path

The checker is [code/check_corner_exact.cpp](code/check_corner_exact.cpp).
It imports no producer kernel, header or arithmetic helper and uses no
MPFR. The finite sums use expanded **physical gradient brackets** from
PD-T227, not the producer's normalized q_x/q_y formulas. The common
parity sign tau_j cancels from squared derivatives and absolute values.

Every interval endpoint is an integer divided by `2^512`. Addition and
subtraction are exact. Multiplication takes all four integer endpoint
products and applies floor/ceiling division by the scale. Reciprocals
require a separated sign and use directed integer division of the squared
scale. Negative reciprocals are reduced by negation; sign-crossing squares
have lower bound zero. Thus every operation encloses its exact real result.

For pi, compute240 alternating terms for each of atan(1/5),atan(1/239),
with the next positive term bounding the omitted tail. Exact rational
arithmetic and outward dyadic conversion enclose
`pi=16 atan(1/5)-4 atan(1/239)`. For completeness, if a=atan(1/5),
then tan(2a)=5/12 and tan(4a)=120/119; subtracting atan(1/239) gives
tangent1 exactly. Elementary bounds place that angle in(0,pi/2), proving
the Machin identity without a numerical pi premise.

For an interior node angle x=j*pi/n, interval multiplication first
constructs x, with a checked0<=x<=4. Evaluate the degree200 cosine Taylor
polynomial by its term recurrence using interval operations. The degree201
Taylor polynomial is the same polynomial, so Lagrange's remainder has
absolute value at most `4^202/202!`; add this exact rational error outward.
The known endpoint and midpoint coordinates1,−1,0 are assigned exactly.
There is no correctly-rounded transcendental-library assumption here.

For each even-checkerboard index, the checker verifies the strict sign of
`d=b_k-a_j` against `m*j-n*k`. It omits exactly k0,j>0 even, and handles
00 separately with

    |L00|=1/m,
    |gradient_x L00|=(2n^2+1)/(6m),
    |gradient_y L00|=(2n+1)/6.

Every other nonzero term uses `|2w C/d|` and the two expanded PD-T227
physical derivatives. Their interval squared sum divided by the positive
cardinal modulus encloses the exact energy contribution. The checker
requires each retained modulus to be separated from zero, and checks both
the full cardinal count and zero-mask count. Summing gives rigorous
intervals for Lambda_c and W_n.

The Python collector [code/check_corner_receipt.py](code/check_corner_receipt.py)
compares these independent endpoints with the frozen producer receipt using
`fractions.Fraction`. For **each** n33/64/128 it verified

    producer_corner_lo <= own_corner_lo <= Lambda_c
      <= own_corner_hi <= producer_corner_hi,
    producer_energy_lo <= own_energy_lo <= W_n
      <= own_energy_hi <= producer_energy_hi.

It also recomputes both own and producer kappa, physical radius and the
producer's dyadic phase-radius predicate exactly. In particular the actual
frozen producer ell/E endpoints, not a replacement decimal estimate,
satisfy the bound hypotheses and common-radius claim.

| n | Nonzero / omitted | Own kappa (decimal diagnostic) | Certified common kappa | Phase box |
|---|---:|---:|---:|---:|
| 33 | 579 / 16 | 0.00008592443849760094 | 1/12500 | 1/128 |
| 64 | 2113 / 32 | 0.00008268390232855796 | 1/12500 | 1/128 |
| 128 | 8321 / 64 | 0.0000810996007879208 | 1/12500 | 1/128 |

A separate exact rational control at n2 constructs the corrected cardinal
coefficient kernel on rational nodes and differentiates its Chebyshev
modes directly at the corner. It obtains `Lambda_c=3`, `W_2=331/18` and
one zero cardinal, all enclosed by the C++ result. This control does not
reuse the quotient or physical gradient brackets.

Actual build command:

    g++ -O2 -std=c++17 -Wall -Wextra -Werror topics/padua-argmax-bridge-20261105/code/check_corner_exact.cpp -lgmpxx -lgmp -o local-output/argmax-bridge-20261105/check-corner/check_corner_exact

The corrected replay invoked that binary separately with arguments2,33,64,
and128, writing `n2-control.json`, `n33.json`, `n64.json`, `n128.json`
under `local-output/argmax-bridge-20261105/check-corner`. The collector
was actually executed with `--run`; it now requires that option before
issuing a replacement receipt. The corrected build and all executions
succeeded. The contract defect and historical withdrawal are recorded in
C2 above; no developer producer code was edited.

To reproduce the build, all four executions and collection in one command:

    python topics/padua-argmax-bridge-20261105/code/check_corner_receipt.py --run

The small [independent receipt](evidence/independent-corner-replay.json)
pins source, binary, exact inputs and raw outputs, with compiler/platform
metadata. Trust is limited to GMP exact integer/rational arithmetic,
compiler/runtime and the proved finite formulas; correctly rounded MPFR
transcendentals are not a dependency of this independent path. Raw outputs
remain off Git but are fully regenerable from committed checker sources.
Cold-storage archival is pending, with no unavailable proof input.

## N6 round2 scope reconstruction

Read both frozen files and the complete round2 candidate record. The
already reviewed generic N4 variance theorem remains its sole home.
For complete cardinal vectors, reproducing coordinates and their squares
forces a probability representing measure to be delta_z. The finite trace
union is compact, so an off-support z cannot have the stated lift.

The unimodular torus inverse gives trace phase
`s=m eta phi-n epsilon theta modulo2pi`. Phase0 or pi is equivalent to
`m phi +/- n theta in pi Z`, hence to
`T_n(x)^2=T_m(y)^2`. This proves both inclusions of the support identity,
including endpoints. The proposed points have Chebyshev squares0 and1,
and the n2 witness has squares1 and1/2, so they are exactly off support.

Mass1 and total variation<=1 force a real signed measure's negative
Jordan mass to vanish. A common scalar envelope equals1 by partition of
unity. An invertible common regrouping can be undone. These are
consolidations of the same full-vector class. Complete Hadamard pair
features retain the original norm through2max(|E|,|O|); they do not evade
reproduction. Scalar or noninvertible nonlinear features are not excluded.

On the two full traces, lambda has minimum1 (a node corner belongs) and
attains a maximum C_n by compactness. Any scalar value in[1,C_n] is a
probability mixture of those two extremal values, including the C_n=1
case. Scalar feasibility therefore restates the desired global inequality.
Both nonnode corners lie on Gamma_pi, so C_n>=Lambda_c; neither the
lift obstruction nor this lower bound proves C_n<=Lambda_c or square
comparison. The stated OPEN/deferred dispositions are appropriate.

## N1 round2 cancellation reconstruction

Read the frozen theorem and complete `ideas/N1-outer.md`. Reduction of v
modulo pi and reflection reduces to0<v<=pi/2. For CD>0 the opposite-sign
pieces are `(pi/2-v,pi/2)` and `(pi-v,pi)`; the minimum of the two weighted
cotangent magnitudes is unimodal on each. Replacing both coefficients by
M=max(|C|,|D|) bounds their peaks by `M tan(v/2)` and `M cot(v/2)`.
The negative twice-minimum excursion has variation four times its peak,
including the jumps to the assigned zero values at poles. Their sum is
`8M/sin v`.

For CD<0 the two cancellation pieces are monotone, with endpoint heights
`|D|cot v` and `|C|cot v`; their variations including pole jumps are
`4(|C|+|D|)cot v<=8M/sin v`. At v=pi/2 they are empty; CD=0 is trivial.
At a pole the assigned zero agrees with one one-sided limit (or both
when that other channel vanishes), so no omitted isolated spike occurs.

On each centered mesh cell, the Stieltjes error weight lies in[−1/2,1/2].
Summing over one period bounds the shifted-grid quadrature error by half
of the periodic variation. Samples are continuity points because both
poles are excluded; moving absolute-value zeros remain continuous. Pole
jumps within or on boundaries of cells are included, with no derivative
or root-separation premise.

The exact offsets follow from `nv_r=r*pi+beta-v_r` and odd parity of
`delta_r+r`. Both odd-board maps `mj+nr` and `mj−nr` have exactly one
representative per residue modulo2nm, so each collision equation supplies
at most one point. Thus there are at most two collision points/rows and
`|A_R|<=2R+4`, including endpoints and coincident collision conditions.
Rows outside A_R avoid v in pi*Z and both channel poles; no invalid
phase-limit argument is used at excluded rows.

The cancellation error after coefficient substitution is exactly bounded
by `(p+q)/|sin v|+a*csc^2(v/2)`. The half-angle identity removes the
central singularity from its a term. Outside the extracted rows, the
endpoint and central distances produce integers k_r>=R and l_r>=1,
each with multiplicity at most two and values<=n. Sine chord bounds
then give sums at most2mH_n and2m^2/(R−1). Division by nm gives precisely
`2(p+q)H_n/n+2am/[n(R−1)]`. The single-pole norm quadrature costs only
one e_n per coefficient, whereas N1-01's negative-part row bound allowed
two, so its existing r_n bounds the combined error. At excluded collision
rows the original finite model is used directly. The theorem is valid
for n>=2, integer2<=R<=n, all phases in its closed diamond, with the rho
notation clarification C1 above.

This removes numerator-root integer cutoffs only from nonexceptional
rows. Exact shifted reciprocal sums, exact cancellation integrals and an
O(n) outer sum remain. The fixed O(1/R) term is not an all-degree
certificate or an effective threshold; the record correctly says so.

## Reading limits and remaining review

The complete unchanged1015-line registry and all obstruction/disposition
tables were read in the earlier row supplement; its hash remains
`948c30b35cdb3ffacefe398acfb35439fc7e69f8be33fd94bc605b052b8d03c6`.
No new candidate or external novelty claim is generated by this review.
Additional full reads comprise the new corner gate/records, PD-T227,
PD-T251, N6 round2 candidates/theory and N1 outer candidates/theory.
The earlier full N1/N2/N4/N5 and relevant predecessor reconstructions
remain dependencies at their frozen scopes. No external source theorem
is imported, and this is no comprehensive historical-priority audit.

No unresolved substantive finding remains in these reviewed scopes.
C1 is a minor standalone notation clarification. C2 was repaired in the
independent checker and resolved by actual corrected replay. Required Claude audit,
full phase-cover replay, full-degree certification, B2/B3 and the global
all-degree bridge remain outside this supplement and unresolved here.
