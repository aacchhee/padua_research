# C01 ratio enclosure lemma — bounded-work value and derivative charts

ID kind: implementation lemma, no new global ID requested.
Aliases: fixed-order sinc jet; quotient-first ratio; pole-chart derivative;
global-cap fallback. Split from/into: none. This makes PD-T364's existing
ratio chart and the phase-checker derivative contract explicit; the
identity is not proposed as new mathematics.

Rules/input: `4b728b04216a5490910780bc609a82b853058426`.
Developer: Codex, assigned Sol xhigh; serving metadata unexposed.

## Statement, assumptions and status

For every integer k>=1 define the entire real trigonometric polynomial

    R_k(z)=sum_{j=0}^{k-1} cos((k-1-2j)z).

It equals sin(kz)/sin(z) wherever sin(z)!=0. For every finite closed real
interval Z the algorithm below returns finite outward enclosures of
R_k(Z) and R'_k(Z), including every removable pole, using a number of
scalar interval operations and elementary-function calls independent of
k, at fixed working precision and fixed chart order. It is permitted to
return the global caps. No width, leaf acceptance or total certifier
complexity guarantee is included.

Assume correct outward real interval arithmetic, an outward pi interval,
validated real sin/cos operations, exact integer factors/parity and finite
global-cap construction. Machine overflow, nonfinite inputs and invalid
intervals must be rejected before reporting success. Arbitrary k requires
arbitrary-precision integers or a documented checked integer range.

Overall mathematical status: **PROVED**, developer proof below; distinct
review is a separate adoption requirement. Implementation conformance and
performance are not established by this lemma. PD-T099 remains OPEN.

| Part | Status / scope |
|---|---|
| Value/derivative continuation and interval contract | PROVED under stated arithmetic assumptions |
| Fixed-chart operation count, including fallback | PROVED as scalar-operation count; dependency and bit costs explicit below |
| New executable, selected-case tightness, actual speedup | Not a claim of this lemma; separate implementation evidence required |

## 1. Exact turns and caps

Let q_j=k-1-2j. Pairing exponentials proves the quotient identity away
from its poles, and the finite polynomial defines its continuation.
All q_j have parity k-1. Hence for every **exact integer** ell and real r,

    R_k(ell*pi+r)=epsilon R_k(r),
    R'_k(ell*pi+r)=epsilon R'_k(r),
    epsilon=(-1)^(ell*(k-1)).                            (1)

Compute epsilon by parity bits, without multiplying large signed integers:
it is -1 precisely when ell is odd and k is even. Negative odd ell has
the same parity rule. A rounded estimate may propose ell, but ell itself
must then be stored exactly. Correctness never assumes the proposed ell
is a nearest pole: every integer turn satisfies (1).

The exact global and local bounds are

    |R_k|<=k,  |R'_k|<=C1=floor(k^2/2),
    |R''_k|<=C2=k*(k^2-1)/3,                            (2)
    |R_k(ell*pi+r)-epsilon*k|<=C2*r^2/2,
    |R'_k(ell*pi+r)|<=min(C1,C2*|r|).                   (3)

Indeed |cos|,|sin|<=1 give the first two bounds from sum|q_j|. For
k=2h, that sum is 2(1+3+...+(2h-1))=2h^2. For k=2h+1 it is
2(2+4+...+2h)=2h(h+1). Expansion of
sum_j(k-1-2j)^2, using the elementary first and second integer sums,
gives C2. At r=0 all sine terms vanish and R_k(0)=k. Taylor's integral
formula and |sin(qr)|<=|qr| give (3). These finite identities are used
only to prove closed-form caps; **no runtime frequency enumeration is
required**. For k=1 return exactly R_1=1,R'_1=0 at every input.

## 2. A fixed-order sinc jet with explicit remainders

Write s(x)=sinc(x), s(0)=1. The integral identity

    s(x)=integral_0^1 cos(tx) dt

and differentiation under this bounded smooth integral show that s is
entire and

    |s(x)|<=1,  |s'(x)|<=min(1/2,|x|/3),
    |s''(x)|<=1/3,  s(x)>=1-x^2/6.                    (4)

For the last assertion use cos y>=1-y^2/2 under the integral. For the
|x|/3 estimate use |sin(tx)|<=t|x| in s'=-integral t sin(tx)dt.

For an integer J>=1 put

    P_J(x)=sum_{j=0}^J (-1)^j x^(2j)/(2j+1)!,
    D_J(x)=sum_{j=1}^J (-1)^j (2j)x^(2j-1)/(2j+1)!.

For every real x, without an alternating-term-size assumption,

    |s(x)-P_J(x)| <= |x|^(2J+2)/(2J+3)!,
    |s'(x)-D_J(x)| <= (2J+2)|x|^(2J+1)/(2J+3)!.      (5)

Proof: integrate the usual real Lagrange remainder of cos through degree
2J+1 (whose odd coefficients vanish). The bound becomes
|x|^(2J+2)/[(2J+2)!(2J+3)]. For the derivative integrate t times the
sin remainder through degree 2J; this gives
|x|^(2J+1)/[(2J+1)!(2J+3)], equal to (5). Differentiating an inequality
for the value remainder would not justify this derivative estimate.

For an interval X with outward B>=sup|X|, enclose P_J(X),D_J(X) by
ordinary outward polynomial arithmetic and add symmetric errors from
(5). Evaluate P by Horner in X^2 and D as X times a polynomial in X^2;
this retains even/odd structure and the derivative's exact zero at X={0}.
Coefficients are exact rationals enclosed outward, not rounded decimal
constants assumed exact. Use a dependency-aware square or an outward
enclosure of the true square; overestimating X*X is safe but less sharp.
Intersect the results with (4) whenever useful.

A concrete fixed choice is J=32, B<=4. The exact worst-case remainders are

    E0=4^66/67! < 2^-182,
    E1=66*4^65/67! < 2^-178.                           (6)

The strict rational inequalities follow by integer multiplication against
67!, and were reproduced by the exact diagnostic below. They are truncation
errors only: outward polynomial-rounding radii remain additional. The
derivative output subsequently scales with k^2, so (6) is **not** a
k-independent absolute-error promise. For a different precision choose
J from that precision and fixed B=4, never by enumerating k frequencies.

## 3. Pole-chart value and derivative

For any exact integer ell form the outward residual interval

    A=Z-ell*Pi,

where Pi encloses the exact real pi. Literal admission tests are

    A subset [-3/2,3/2],  k*A subset [-4,4].            (7)

The subtraction enclosure contains z-ell*pi for every z in Z. By (4),

    s(r)>=1-r^2/6>=5/8                                (8)

on A. Thus no denominator vanishes. With r=z-ell*pi the exact identities
are

    R_k(z)=epsilon*k*s(k*r)/s(r),
    R'_k(z)=epsilon*k*
      [k*s'(k*r)*s(r)-s(k*r)*s'(r)]/s(r)^2.            (9)

The value identity is PD-T364's existing sinc chart. Its derivative is
the ordinary quotient rule on a neighborhood where (8) holds. Both sides
are smooth there and agree with the finite polynomial on a dense set, so
they include r=0 continuously. Specifically the collision pair is
(epsilon*k,0). Numerator zeros of s(kr) require no special branch and
may never be cancelled by dividing by s(kr).

Apply (5) separately to A and k*A, intersect the denominator sinc enclosure
with [5/8,1], and evaluate (9) outward. Square the positive denominator
with a validated square operation. A finite empty intersection is an
error in purportedly valid candidates. It is not permission to discard
a contradiction. Intersect the resulting pair with (2) and, optionally,
(3). No frequency sum, divided zero or removable infinity occurs.

The simple admission |r|<=1/2 also works, with s(r)>=23/24; it is a
stricter valid subchart, not needed for correctness or the coverage below.

## 4. Why ordinary pole-crossing phase boxes have bounded kr

This is an exact-geometry assertion, independent of rounded code. Let
n>=2,m=n+1, k in {n,m}. Let alpha and beta range over intervals of
widths w_a,w_b<=pi. These include every quadrant root box and every
descendant in the existing longest-side bisection. For fixed integer board
indices form u=(r*pi+alpha)/n, v=(s*pi+beta)/m and either
z=(u+v)/2 or z=(u-v)/2. Its exact image interval Z has width

    w=w_a/(2n)+w_b/(2m) <= pi/2*(1/n+1/m).

If ell*pi belongs to this Z, every residual satisfies |z-ell*pi|<=w.
Therefore

    |r_residual|<=5*pi/12<3/2,
    k*|r_residual|<=pi*(1+1/(2n))<=5*pi/4<4.          (10)

The first maximum occurs at n=2, and the second uses k<=m. Elementary
pi<22/7 proves both strict comparisons. The width is <pi, so such a
pole is unique. A midpoint-nearest turn therefore proposes it; correctness
still rests only on the actual guard (7). Fixed-pi interval inflation,
arithmetic rounding, or a sine ball containing zero despite no true pole
are handled by literal admission or the global fallback, never by assuming
the exact-geometry conclusion for rounded inputs. The theorem proves why
the finite Taylor cap need not grow with n at genuine pole crossings;
it is more than observing that a formal sinc identity exists.

## 5. Separated quotient, total fallback and optional tightening

Begin with (R,D)=([-k,k],[-C1,C1]). Optionally first intersect with (3)
for any exact-turn residual. A quotient candidate is allowed only when
validated S=sin(Z) is finite and excludes zero, and C=cos(Z),
T=sin(kZ),U=cos(kZ) are finite. Then

    Q=T/S,   Q'= [k*U*S-T*C]/S^2                       (11)

are valid on all of Z. Use a validated square for S^2 and independently
check its finiteness and exclusion of zero before division. Stage the
value and derivative together; a nonfinite optional candidate leaves the
finite prior pair intact. Finite disjoint valid candidates throw an error.
The pole chart (9) is another optional pair, admitted by (7), with the same
staging rule. It is valid to prefer (11) first for speed or to intersect
both when both are valid. No accepted leaf semantics change.

For arbitrary very broad finite Z, or failure of both analytic candidates,
the global pair remains valid and finite. Multiple poles therefore require
neither splitting nor harmonic work for **validity**. Splitting may still
be needed for useful precision. This does not contradict PD-T364's older
advice to split or use the finite polynomial: the closed-form caps (2)
are themselves proved bounds for that polynomial.

An optional constant-work midpoint enclosure can reduce interval dependency.
Let c be the exact midpoint, h the exact half-width, V,D validated point
enclosures at c, and T=Z-c. Taylor's integral formula gives

    R_k(Z) subset V + D*T + [-C2*h^2/2,C2*h^2/2],
    R'_k(Z) subset D + [-C2*h,C2*h].                    (12)

Use outward midpoint/radius construction, exactly as in the existing
whole-sum lemma; rounded binary64 midpoint alone is insufficient. This
uses the same total evaluator at a point once, not recursive refinement.
Formula (12) is optional, and no tightness claim assumes its implementation.

## 6. Cost model, dependencies and independence

At fixed J=32 the pole chart uses two evaluations of a pair of fixed
polynomials (degree32 and31 in x^2), a fixed number of rational interval
operations and intersections, and no trigonometric evaluation. Coefficients
can be prepared once at the working precision; their initialization cost
is finite and independent of k. Computing powers for remainder radii costs
a fixed number of operations. The separated chart uses two scalar
sin/cos calls plus fixed arithmetic. Optional (12) adds one bounded point
evaluation. Global fallback uses fixed closed-form integer arithmetic.

This proves only a scalar-operation count. Integer bit length grows like
log k (and cap C2 needs O(log k) bits); multiplication by k, turn reduction,
output exponents and elementary-function argument reduction have their
ordinary precision/argument costs. A k-dependent trig argument kz can
need additional reduction work. There is **no** absolute constant bit-time
claim and no hidden call to a degree-k Chebyshev or finite-harmonic routine.
If library sinc is substituted for a polynomial, its actual implementation
must be inspected and its operation cost counted; the present lemma does
not rely on a library sinc API at all.

The Arb checker must implement these operations independently of the
MPFR producer. The mathematical identity may be shared, as PD-T364 already
does; producer interval helpers, constants or executable arithmetic may not
serve as the checking path. Directed-MPFR endpoint and Arb-ball arithmetic
remain distinct algorithms despite shared lower-level GMP/MPFR libraries.

For O(n^2) board entries this removes the old compulsory O(n) harmonic
factor from the **ratio evaluation count**. It does not remove the
O(n^3) all-center projected-profile arithmetic already stated in PD-T364,
and no box-count or whole-cover runtime conclusion follows.

## Checks, sources, limits and history

Dependencies: PD-T364's finite/sinc identities and exact phase geometry;
bridge `phase-checker-reduction.md`, `N3-enclosure-spec.md` and round5's
finite-intersection/sine-square contract. N1-07's sinc integral bound is
a direct predecessor. All bounds above are proved locally; no external
theorem, numerical sample, fitted constant or full cover is a premise.
Candidate/gate: `../ideas/C01-ratio.md`; attempt: `../attempts/C01-ratio.md`.

One standard-library exact integer/Fraction diagnostic was executed after
preregistration: k=1..512 verifies sum|q|=floor(k^2/2) and
sum q^2=k(k^2-1)/3; integer multiplication verifies (6) (and the weaker
2^-170 bounds). It passed. Float log2 outputs were only diagnostics of
those rational errors, never proof premises. It ran in less than one CPU
second. This finite algebra control does not replace the symbolic proofs.

No new arithmetic backend, selected-box comparison, timing study or
consequential certificate replay was performed by this worker. A distinct
review must reconstruct (5), (9), (10), exact turn parity and the total
finite-output contract before adoption. Actual implementation must test
k=1, negative turns, exact/crossed poles, broad intervals, numerator zeros,
rejected guards, nonfinite inputs and empty intersections. Width preservation
on selected old cases remains an empirical implementation obligation.

2026-11-06: developer proof frozen after prospective candidate record;
old v3 sources and all receipts preserved. No global ID allocated and no
scientific registry mutated.

## 2026-11-06 review response — quadrant-root width correction

The first frozen version (SHA256
`063138b375aa81c230ac1a20e20c7af6555839563d973039c9414b89fe3ba0db`)
proves §4 for widths<=pi, but incorrectly includes actual quadrant roots,
whose saved outward binary64 endpoint P=pi_hi exceeds pi. The original
derivation remains the narrower theorem; this addendum supersedes its
application to saved roots. Jet formulas, caps and guards are unchanged.

**Corrected bounded statement (PROVED).** Let n>=2, m=n+1,
1<=k<=m, and let P be any exact real number with 0<P<16/5. If the
two phase intervals have widths w_a,w_b<=P, then the exact image Z under
either z=(u+v)/2 or z=(u-v)/2 has width

    w=w_a/(2n)+w_b/(2m)
       <=P/2*(1/n+1/m)<=5P/12<4/3<3/2.

If ell*pi belongs to that exact image Z, every residual r=z-ell*pi
satisfies |r|<=w and

    k*|r|<=m*w<=P*(1+1/(2n))<=5P/4<4.                (13)

Proof: 1/n+1/(n+1) decreases for n>=2 and has initial value5/6;
also k<=m implies k*(1/n+1/m)<=m/n+1=2+1/n.
The strict upper comparisons use P<16/5. Thus (13) establishes both
unrounded chart guards for every genuine exact pole crossing in this
larger phase-width domain, without an n-dependent Taylor order.

For the saved n32 bootstrap and round6 inputs, exact JSON/binary64
conversion gives

    P=3.1415926535897936
     =7074237752028441/2251799813685248 <16/5.

Standard-library Fraction checked this exact inequality against
`evidence/n3-phase-n32-bootstrap-r8.json.gz` and
`evidence/n3-phase-n32-r6.json.gz`. The roots use phase width exactly P;
binary64 bisection children remain subsets of those root intervals, so
their exact real widths are at most P as well. This read-only check adds
no certificate acceptance.

Actual interval arithmetic still constructs A=Z-ell*Pi with rounded,
outward Z and Pi and **must** test (7). Neither (10) nor (13) asserts
guard admission for an arbitrary outward Pi, an arbitrarily inflated
Z, or arbitrarily huge integer turns/degrees at a fixed working precision.
Rounding may make the guarded chart unavailable; the finite global
fallback remains mandatory. The exact width proof explains the bounded
argument geometry and does not replace those runtime guards.
