# C07 guarded rational-phase point S — independent check

2026-11-06. Rules reread at
`e8fad1671fb736247e4c510284f6f935e6345efb`; author input/rules
`b6e67b3c78cb668b6d2f9da5a5560537d2960bf3` and base
`f654e32daff27b6846849311092f6daebbbf235b`.
Distinct Codex supplementary reviewer, assigned Astra high; actual serving
model/effort metadata independently unexposed. Formal Claude audit remains
separate. No author, shared, prior-review or Git state was changed.

**ACCEPTED for successful native point calls on the frozen LP64 target.**
No unresolved enclosure or coverage finding. The native interface encloses
the exact finite S for rational alpha/pi,beta/pi in the closed first-quadrant
triangle, at 2<=n<=2147483647, when its guards succeed. This is not a
total-success or useful-tightness promise. Arbitrary phase balls, whole-box
roots, gradients, corner/defect assembly and a production certifier remain
OPEN. No new degree, cover, performance scaling or novelty claim is made.

Read the repository rules, C07 gate/attempt/source/reference/driver/receipt,
C02 theory and completed independent review, C06 source and this reviewer's
completed implementation review, N2 full-phase decomposition and N1 row
normalization. This is a bounded implementation/integration check of those
accepted identities, not historical novelty, priority or literature work;
the full registry/literature novelty audit is outside its declared scope.

## Frozen code and independent execution

| File in code/cheap_rows_C07 | SHA256 |
| --- | --- |
| point.cpp | `8913a96d79f7d687c201f5e38efa5cceec5a18bdc88ed0ada8f578056e7e575e` |
| reference.cpp | `dc9c3e5f208a9919437e572d71e0bc3834f493db7ea8689b777fac6566ba8470` |
| control.py | `17cac7535df1f2b7c7c9436a140e3844ae2638cca191cb1ba18e5faad710c8d4` |

The transitive C06 partial.cpp remains
`f381738049d793e81a93626bef11eeb1d2a0ff49d0027b6518dd3fec8ff0bcf0`.
These source identities were checked before/after the independent run.
Separately verified245 byte-size/SHA256 identity records in the developer
receipt and its local raw manifest. The1964-byte developer receipt has
SHA256 `459e2db013bb430ab62e7876dae56e94674eb8ab91a9c15291d063e19ea9425e`.
That identity verification was not a rerun of the developer's suite.

Executed once:

    python topics/padua-argmax-bridge-20261105/code/cheap_rows_C07_review/control.py

Exit0, **PASS**: 13.338906 parent-plus-child CPU seconds including a fresh
compile, below the60-second allocation. Python3.12.14; x86_64-linux-gnu
g++14 Debian14.2.0-19, LP64. No random seed or random cases.

The reviewer reference uses the original odd board j+r odd and explicitly
sums every term h_a h_b cos(a*u)cos(b*v) of D_n at512 bits, subtracts the
single exceptional cos(nu), takes its absolute value and divides by2n(n+1).
It calls neither the author's Chebyshev reference nor a collapsed ratio,
row formula, root selector or C06 sum. Cosines are evaluated directly;
the rational board coordinates and trusted Arb/FLINT libraries are shared.

Forty native cases yield26 production containments of complete512-bit
reference balls, six exact vertex values1 lying inside the reference
balls, and eight invalid-input failures with indeterminate output.
Vertex converse containment is explicitly distinct from production
containment of a wider numerical reference. No tested valid point failed.

Cases include n=2,3,4,5,8,12; both parities; alpha0 nodal rows at
(n,beta/pi)=(3,1/3),(5,1/5); origin; beta0 halfphase collisions;
halfphase and2/5 closed-edge tangencies; generic phases2/7,3/11 and1/7,2/9;
both vertices; and each axis at phase fraction10^-60. Invalid cases cover
out-of-range n, negative phases, triangle overflow, zero denominator and
malformed rational strings. This is a bounded finite diagnostic, not a
new certified degree or full-domain numerical test.

Twenty-one additional root-selector controls cover all eight exact grid
roots, eight roots between successive grid samples, two roots outside the
grid, a wide root cluster that must reject, and threshold balls straddling
each of+1/-1 whose tangent samples must enter the direct set. All pass.

Small receipt `evidence/c07-review-rows.json` pins review.cpp/control.py,
builder, compiler/binary and the local raw manifest
`c07-review-rows/check-2cg0uoi_/review.json`,54319 bytes, SHA256
`14964cc41152dd468528a74e73ee2a4ceb60dc77a7be8f13241d3bdaa8183305`.
The raw record includes all cases and196 source/header identities,
four compiler tools,13 tool dependencies, eight linked dependencies and
eight actually mapped dependencies. Preprocessed-source/toolchain hashes
are checked across compilation and loaded identities match before/after
controls. The included C07/C06 sources are among the pinned preprocessing
dependencies. Raw outputs remain local/regenerable; physical archival
transfer is pending, with no remote retrieval claim.

## Row identity, parity and finite evaluations

The row grid uses delta=(1-r) mod2 in{0,1}, hence j=delta+2k runs through
exactly the odd-board first indices. After the exact vertices are removed,
sigma=(delta+alpha/pi)/2 lies in[0,1); no fractional relabeling is missing.
Separate phase evenness is an external domain reduction; no mesh exchange
or exceptional-mode symmetry is assumed.

With F=(-1)^delta G/2, the coefficient pair is

    C=(p-q-A*cot(v/2))/4, D=(p+q+A*cot(v/2))/4.

The signed-row term is n[(cos(alpha)+cos(beta))/2-q*cot(v/2)/2].
These are exactly half of N2's Q formulas. For regular negative samples,
subtracting2C times the minus-channel sum and2D times the plus-channel
sum implements sum|F|=sum F+2sum(-F)_+. Ambiguous samples instead add
2max(-F,0), using their complete finite primitive. Normalization by
n(n+1) is correct; the finite reference independently checks the matching
1/[2n(n+1)] convention before F's factor1/2 is introduced.

Rows0,2m-1,m-1,m are distinct for n>=2 and include every possible
v=0,pi,2pi on the closed phase triangle. Each is evaluated directly
with n finite primitives. All ordinary cot(v/2) coefficients are finite.
No singular row coefficient is evaluated and multiplied by a zero phase.

For an exact rational turn z/pi, ell=floor(z/pi+1/2) gives
x=z-ell*pi in[-pi/2,pi/2). The finite ratio satisfies

    R_k(z)=(-1)^(ell*(k-1))*k*sinc(k*x)/sinc(x).

The sign test uses odd ell and even k, valid for negative ell as well.
The denominator sinc(x) stays positive; the numerator's entire sinc
handles exact removable turns. Substitution into

    G=R_m((u+v)/2)R_m((u-v)/2)
      +R_n((u+v)/2)R_n((u-v)/2)-cos(nu)

is the accepted collapsed finite polynomial identity. All arithmetic,
pi, rational-conversion, sinc and cosine uncertainty remains in the
returned balls, including abs/max and the retained-row sum. There is
zero row-model truncation at these samples, not zero arithmetic error.
The C01 approximate-series code is not used, so no C01 truncation radius
is missing; the exact-function Arb calls supply the required enclosures.

## Complete root coverage and guarded integer blocks

For an ordinary row the only denominator zeros satisfy u=v or2pi-v.
The folded rational D roots d=min(v/(2pi),1-v/(2pi)) and1-d cover both.
Their computed balls enclose the exact roots. Both cotangent channel
wraps occur at these same roots, so a root-free core cannot cross a
channel wrap without a cut.

For actual p>0, numerator roots solve sin u=c/p. A threshold ball
strictly above1 or below-1 certifies that no root exists. Otherwise,
clamping its exact outward endpoints to[-1,1] preserves every possible
true threshold that can have roots. Asin is increasing there; evaluating
each clamped scalar endpoint separately and taking their hull is valid
even at tangency. Dividing by2pi yields the first root interval;1/2
minus it yields the second. Translates by-1,0,1 cover the complete
[0,1) circle, including a root interval crossing the seam. Extra roots
when the true threshold lies outside[-1,1] only make conservative cuts.

For a root interval in index units, cl=ceil(lower) and fu=floor(upper)
are computed with outward endpoint extraction and exact integer rounding.
If cl<=fu, every potentially coinciding grid index is in this integer
range; more than one causes failure. Its sole member becomes direct and
gets cuts before/after. If cl>fu, the whole root interval lies between
adjacent grid samples and the cut at cl separates them. Early returns
when fu<0 or cl>=n discard only roots outside the sampled index range.
Successful insertion never creates an index outside[0,n].

The sorted cut set{0,n,...} partitions every grid index once. A direct
index has a cut on both sides, so skipping a segment beginning there
skips exactly that one direct sample. Set insertion merges coincident
roots, tangent roots and coincident numerator/denominator roots. Seam
index0 is direct precisely when sigma=0. Thus direct samples are never
also included in a cotangent block and no grid sample falls into a gap.

Within each remaining contiguous core, no actual numerator or denominator
zero lies at a grid sample or between its samples. Certifying their signs
at the first sample therefore certifies every discrete sample in that
core. Strict equal/opposite sign checks select positive/negative cores;
an undecidable sign rejects the call. No rounded sign is trusted. A
core containing only an exact zero numerator can also be skipped under
the independently justified p=c=0 branch below.

The exact rational channel start y=lo+sigma+/-n*v/(2pi), reduced modulo
n by an exact floor, is correct for cot's pi-periodicity. C06 additionally
checks the whole block satisfies0<y and y+q-1<n. Any overlooked numerical
pole ambiguity therefore fails rather than reaching a divergent partial
sum. The two channels use the same block index range and each counts its
selected samples once. The guards enforce at most five direct samples
and24 combined channel calls; calls occur in pairs, so there are at most
12 per channel.

## Axes, boundary and machine domain

At alpha=0, p is exactly zero. For beta<pi,

    c=(1+cos beta)(1+cos v)+sin beta*sin v
      =4*cos(beta/2)*cos(v/2)*cos((v-beta)/2).

In0<v<2pi the only zeros are v=pi and v=pi+beta. The former is covered
by retained rows whenever it occurs; the latter is detected exactly by
the rational equality vf=1+bf. Setting c=0 there is mathematically exact,
so skipping regular zero numerator cores is valid. Collision corrections
and the signed row are still retained. On beta=0, q is exactly zero.
These are algebraic tests, not smallness tolerances.

On alpha+beta=pi, A is exactly zero. The two sines are enclosed separately,
so an exactly zero coefficient can have a small interval radius; it is
still carried through the product and cannot erase any uncertainty.
Both exact vertices return1 only after the phase-domain guard proves the
other phase is0, agreeing with the accepted N2/T365 identity. No
zero-times-infinity limit is substituted.

The n guard precedes n+1,2m and all grid arithmetic. On LP64, n<=2^31-1
gives m<=2^31,2m<=2^32, and2k+delta<2^32. Floor conversions for reduced
turns and channel wraps are bounded; root index balls come from bounded
circle turns, not arbitrary caller integers. Counts such as4n and at
most24(2m-4) blocks also fit signed64 bits. Rational products use FLINT,
and normalization multiplies Arb values rather than overflowing a native
n*m product. The separate reference's2n(n+1) also fits signed64 at this
ceiling. No ILP32/LLP64 portability approval is implied.

Malformed fractions/zero denominators are rejected before canonicalizing
an invalid rational. Negative phases and sum>1 are rejected exactly.
The native API catches C++ exceptions and writes an indeterminate output;
the final finite check prevents returning a nonfinite numerical answer.
All precision arguments are explicit, with no mutable precision global.
As in C06, process-level allocation/library aborts and invalid C pointers
are outside this mathematical return-value contract.

## Error charge, operation count and remaining limits

Every channel call returns the unchanged C06 full Arb ball: J48 smooth
remainder, both K32/L16 harmonic errors, WD96 derivative remainder,
coefficient and arithmetic uncertainty, and rational-moment input-radius
propagation. Multiplication by C/D and summation over every ordinary row
preserve these radii automatically. No separate four-row estimate is
used to pay for the other rows. Division by the positive exact n(n+1)
normalizes the complete accumulated enclosure. This does not claim the
smaller analytic J96/K64/L32 all-row theorem or infer derivative accuracy
from a small value radius.

Production performs2m outer rows,4n retained finite evaluations, at most
five direct finite evaluations per ordinary row and at most24 C06 calls
there. Root/cut/edge sets have bounded size and do not scan n indices.
The exact finite primitive has a bounded number of elementary calls.
C06's only q-dependent loop is its prefix capped at32. The large board
loops occur only in reviewer/author diagnostics; no reference fallback
is called on production failure. These statements concern arithmetic
operation counts; rational bit lengths, precision/argument reduction and
actual useful runtime remain separate. No speedup is inferred here.

**NOTE — developer driver.** The author's control.py records return
codes/containments without asserting every case passes, so its exit0 alone
is not a pass certificate. Its recorded final22 outcomes support the
stated narrow result; this reviewer's driver independently asserts the
required outcomes and keeps vertex checks distinct. The historical
64/72 initial successes and eight safe tangency rejections remain
preserved in the attempt; they are not changed-source reruns.

General success/tightness, arbitrary real-phase packaging, whole-box
root movement, gradients, corner orbits, projected defects and final
certifier integration remain OPEN. Formal Claude review is still separate.
