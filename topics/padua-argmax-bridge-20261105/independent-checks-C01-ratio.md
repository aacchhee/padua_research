# C01 ratio enclosure: independent mathematical check

2026-11-06. Rules/input head `4b728b04216a5490910780bc609a82b853058426`.
Reviewer: distinct Codex agent, assigned Astra high; serving model/effort
metadata not independently exposed. This supplements, and does not replace,
the pending formal Claude audit. No Git or developer-file edits.

Original frozen input: `theory/C01-ratio-enclosures.md`, 14094 bytes,
SHA-256 `063138b375aa81c230ac1a20e20c7af6555839563d973039c9414b89fe3ba0db`.
Also read its idea/attempt records, handoffs06/05, current campaign LOG
entry, AGENTS/WORKFLOW/CODEX, PD-T364, phase-checker reduction and the
relevant producer/checker root construction and old ratio implementation.

**Final disposition: ACCEPTED within mathematical scope** at revised
proof SHA-256
`ce6101733c9297c00a7e32431e9c0188ba4ce053e059e1080523013993b80890`
(16311 bytes). Value/derivative mathematics and the total guarded
scalar-operation contract pass. The author corrected the narrow
geometry-to-existing-roots finding by the reviewed addendum below.
No executable replacement, speedup or whole-cover acceptance is approved
by this mathematical review.

This review makes no novelty, priority or historical-coverage judgment.
The candidate explicitly retains the existing identity as an internal
backend variant. Full registry/literature novelty review is therefore
outside scope; no new mechanism is proposed by this report.

## Independent reconstruction

1. Pair the frequencies `k-1,k-3,...,1-k`. The geometric exponential sum
   equals sin(kz)/sin(z) off its poles and defines a smooth finite
   trigonometric polynomial everywhere. Every frequency is congruent to
   k-1 modulo2; translation by an exact integer ell times pi multiplies
   both value and derivative by the same parity sign. This holds for
   negative ell as well. An approximate turn proposal is harmless only
   after exact integer storage and outward residual construction; no
   nearest-pole hypothesis is needed for correctness.

2. The absolute frequency sum is 2h² for k=2h and 2h(h+1) for k=2h+1,
   exactly floor(k²/2). Summing the squared arithmetic progression gives
   k(k²-1)/3. These bound the first and second derivatives globally.
   Since R(0)=k and R'(0)=0, integrate the second derivative once and
   twice to obtain the local derivative and value caps. Thus no runtime
   frequency list is needed. For k=1 all derivative caps are zero and
   the exact value is1. Invalid/nonfinite input rejection precedes that
   shortcut, as required by the statement's success contract.

3. Integrating cos(tx), -t sin(tx), and -t² cos(tx) on 0<=t<=1 gives
   sinc and its first two derivatives. The integrals of1,t,t² give
   1,1/2,1/3; |sin(tx)|<=t|x| gives |s'(x)|<=|x|/3. Integrating
   cos(tx)>=1-(tx)²/2 gives s(x)>=1-x²/6. This works across zero and
   does not use a singular `(cos-sinc)/x` evaluation.

4. Taylor-expand cos through degree2J+1 and sin through degree2J.
   Their next derivative bounds are1, independently of x or monotonicity
   of alternating terms. Integrating the value remainder gives
   |x|^(2J+2)/((2J+2)!(2J+3)); integrating t times the sine remainder
   gives |x|^(2J+1)/((2J+1)!(2J+3)). These are exactly (5), including
   the derivative factor2J+2. The derivative estimate does not follow
   from differentiating an absolute error inequality. Exact integer
   comparisons verify both stated J32 bounds. A polynomial interval
   enclosure still has its additional arithmetic-rounding radius.

5. On a literal residual interval A inside[-3/2,3/2], s(A) is bounded
   below by5/8. The positive-denominator quotient rule gives precisely
   epsilon*k*[k*s'(kr)*s(r)-s(kr)*s'(r)]/s(r)². At r=0 the result is
   (epsilon*k,0). Numerator zeros cause no division and require no
   branch. Intersecting the denominator enclosure with[5/8,1] is valid;
   a finite empty intersection signals inconsistent enclosures. The
   second guard k*A inside[-4,4] supplies the fixed Taylor error cap.

6. For separated intervals, differentiation of sin(kz)/sin(z) yields
   (11). Exclusion of zero by a validated sine interval, together with
   a validated nonzero square denominator, is sufficient. The caps form
   an unconditional finite baseline for valid inputs. A nonfinite
   optional calculation may leave it intact; finite contradictory
   candidates cannot be silently skipped. Staging value and derivative
   together avoids partially committing an invalid pair. Multiple poles,
   failed turn proposals, broad intervals and oversized residuals can
   all safely return the caps. Overflow in constructing those caps must
   fail before success, rather than becoming an infinite enclosure.

7. With exact interval midpoint c and half-width h, the second-order
   integral remainder bounds (12) uniformly. Point evaluations must
   contain this exact c; a rounded midpoint with an underestimated
   radius is insufficient. This optional refinement needs only one
   point evaluation without recursive refinement.

8. At fixed J the two Horner jets and the fixed remainder powers require
   bounded scalar interval work. The quotient uses two paired sin/cos
   evaluations (or four separate scalar trigonometric calls), still
   independent of k. Closed caps and parity use a fixed count of exact
   integer operations. Integer bit length, argument reduction and working
   precision costs remain explicit. No actual dependency implementation
   of a new backend has been audited here. Using a library sinc or
   degree-k polynomial routine would require a separate inspection and
   may violate the claimed count. The O(n³) all-center profile scan is
   unaffected; an O(n²) board call count is not an overall certifier bound.

## Geometry finding and exact endpoint-slack check

**F1 — MAJOR, resolved (narrow scope correction).** Original §4 lines169–170 says intervals of
width at most the true pi include every existing quadrant root. Actual
producer roots and `check_r8.py`'s root validation use supplied outward
`pi_hi`; these widths exceed the true pi. The exact ideal geometry proof
under its stated width assumption is correct, and the literal runtime
guard/fallback caveat already protects evaluator correctness. The bridge
from that ideal assumption to the actual enclosing roots needs a scoped
correction, not an unqualified assertion that rounding was absent.

An independent elementary repair is available. If the input phase widths
are at most P<16/5, then for n>=2 and k in{n,n+1},

    w <= P/2*(1/n+1/(n+1)) <= 5P/12 < 4/3 < 3/2,
    k*w <= P*(1+1/(2n)) <= 5P/4 < 4.

For a genuine pole inside the exact image, every residual has absolute
value at most w. Because w<pi, there is at most one pole and its distance
to the exact interval midpoint is at most w/2<pi/2, so it is the unique
nearest midpoint pole. Descendant intervals inherit the width bound.

The four saved n17/24/32 candidates independently read below all use
P=7074237752028441/2251799813685248<16/5. Their conservative true-image
margin to3/2 is1720402628730753/9007199254740992; the margin to4 after
scaling is657608258821763/9007199254740992. Thus the outward endpoint
extension itself is harmless. This calculation is not a uniform bound
on additional interval inflation from arbitrary pi enclosures, turn
reduction or arithmetic. The actual A and k*A guards remain mandatory.
For arbitrary allowed outward pi/root constants, chart admission is not
guaranteed; the finite fallback is still sound.

Finding sent to the coordinator before any author correction. This
reviewer has not altered the frozen mathematical file.

**Author response and focused recheck.** The author appended a dated
quadrant-root width correction, freezing the revised hash recorded above.
It explicitly supersedes only the incorrect application to actual saved
roots, retaining the original ideal-width theorem and its narrower
hypotheses. The extension to all1<=k<=n+1 is valid because k*w<=m*w;
the monotone bounds and P<16/5 comparisons are exactly those reconstructed
here. The addendum states that interval rounding still requires guard(7)
and does not guarantee admission at arbitrary Pi, Z, turn or degree.
It makes no executable or cover-acceptance claim. Exact hashing of the
first14094 bytes confirms the original frozen text is unchanged; only
the addendum was added. F1 is closed with no unresolved mathematical
finding. This focused recheck adds no arithmetic run or cover execution.

## Executed checks and retained evidence

Executed from repository root:

    python topics/padua-argmax-bridge-20261105/code/cheap_c01_ratio_review/controls.py

Actual exit0: **9270 exact assertions PASS**, Python process CPU
0.150478662s, within the60CPU-s cap. Python3.12.14 standard library only;
no producer/checker import, kernel execution, cover replay or external
dependency download. No random seed is involved.

`evidence/c01-review-ratio.json` retains the source SHA, command,
environment, exact rational remainder bounds, and source identities for
the four read-only saved gzip headers. The checks independently use
paired positive frequencies for k=1..1024, seven positive/negative/zero
turns, integral coefficient identities, and exact rational root widths.
The symbolic reconstruction above establishes the all-k statements; the
finite controls do not substitute for it. Small source/evidence are
retained locally for coordinator publication. No large artifact or
physical cold-storage delivery was created or claimed.

Implementation follow-up must independently check finite-input guards,
exact integer ranges, parity and negative turns, genuine poles and
crossings, numerator zeros, rejected charts, broad intervals, staged
nonfinite optional candidates and finite empty intersections. Selected
old-case width/performance comparisons remain separate. This report
authorizes no whole-cover computation or additional certified degree.
